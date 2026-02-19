one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
RESPONSE_SIZE

ROWS_PROCESSED

RUN_TIME

SESSION_KEY

STATUS_CODE

TIMESTAMP

TIMESTAMP_DERIVED

```

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
The HTTP response status code for the request.

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

##### Sandbox Event Type

Sandbox events contain details about sandbox copies.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
CURRENT_SANDBOX_ORG_ID

EVENT_TYPE

ORGANIZATION_ID

PENDING_SANDBOX_ORG_ID

REQUEST_ID

SANDBOX_ID

STATUS

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the current sandbox organization.

**Type**
String

**Description**
The type of event. The value is always `Sandbox` .

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


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Search Event Type

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

Search events contain details about the user’s search query. All searches within the app, including Experience Cloud sites, are included.
However, unauthenticated users won’t have a unique Salesforce user ID.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

```

**Type**
String

**Description**
##### The type of event. The value is always Search .


Standard Objects EventLogFile Supported Event Types

```
NUM_RESULTS

ORGANIZATION_ID

PREFIXES_SEARCHED

QUERY_ID

REQUEST_ID

SEARCH_QUERY

```

**Type**
Number

**Description**
Number of results returned by the search query.

**Possible Values**

**•** 0

**•** 25

**•** 1000

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


Standard Objects EventLogFile Supported Event Types

**Example**
Salesforce

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Search Click Event Type

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

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the result the user clicked in the search
results page.

**Example**
a07B00000031pRV

```
EVENT_TYPE

ORGANIZATION_ID

QUERY_ID

RANK

REQUEST_ID

TIMESTAMP

```

**Type**
String

**Description**
The type of event. The value is always `SearchClick` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

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


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

USER_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Sites Event Type

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
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Sites events contain details of Site.com requests. Requests can originate from the browser (UI).

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
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

```
DB_TOTAL_TIME

EVENT_TYPE

HTTP_HEADERS

HTTP_METHOD

IS_API

IS_ERROR

IS_FIRST_REQUEST

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


Standard Objects EventLogFile Supported Event Types

**Description**
1 if this page is the first Visualforce transaction in the request,
or 0 if it isn't.

```
IS_GUEST

IS_SECURE

LOGIN_KEY

ORGANIZATION_ID

PAGE_NAME

QUERY

REQUEST_ID

```

**Type**
Boolean

**Description**
True if this page was a guest (unauthenticated) request.

**Type**
Boolean

**Description**
True if this request is secure.

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


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_STATUS

REQUEST_TYPE

RUN_TIME

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


Standard Objects EventLogFile Supported Event Types

**Description**
The amount of time that the request took in milliseconds.

```
SESSION_KEY

SITE_ID

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

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


Standard Objects EventLogFile Supported Event Types

```
USER_ID

USER_ID_DERIVED

USER_TYPE

```

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
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.


Standard Objects EventLogFile Supported Event Types

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

Fields

**Field** **Details**

```
API_TYPE

API_VERSION

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

##### • S —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

CLIENT_NAME

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
ENTITY_NAME

EVENT_TYPE

EXCEPTION_MESSAGE

LOGIN_KEY

METHOD_NAME

ORGANIZATION_ID

QUERY

```

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

**Description**
The exception message for a SOAP API request. An exception
message gives details about errors in handling an API request,
such as why an API request failed.

For example: `common.exception.ApiException:`

```
   startDate cannot be more than 30 days
```

`ago` .

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


Standard Objects EventLogFile Supported Event Types

**Description**
The data that was queried.

```
REQUEST_ID

REQUEST_SIZE

REQUEST_STATUS

RESPONSE_SIZE

ROWS_PROCESSED

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


Standard Objects EventLogFile Supported Event Types

**Description**
The number of rows that were processed in the request.

For example: `150` .

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

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

```
USER_ID

USER_ID_DERIVED

USER_TYPE

```

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
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.


Standard Objects EventLogFile Supported Event Types

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

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


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LOG_GROUP_ID

LOGIN_KEY

NUMBER_OF_RECORDS

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The type of event. The value is always
`TimeBasedWorkflow` .

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


Standard Objects EventLogFile Supported Event Types

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

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

EVALUATION_TIME_MS

EVENT_TIMESTAMP

EVENT_TYPE

```

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Description**
The IP address of the client that is using
Salesforce services. A Salesforce internal
IP, such as a login from AppExchange,
is shown as “Salesforce.com IP”.

For example: `96.43.144.26`

**Type**
Number

**Description**
The CPU time in milliseconds used to
complete the request. This field
indicates the amount of activity taking
place in the app server layer.

**Type**
Number

**Description**
The time in milliseconds used to
evaluate the policy.

**Type**
String

**Description**
The time at which the Transaction
Security event was generated in
ISO8601-compatible format
(YYYY-MM-DDTHH:MM:SS.sssZ). This
value can be earlier than
TIMESTAMP_DERIVED by the amount
of time taken to log the event.

For example:

```
  2015-07-27T11:32:59.555Z

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always
`TransactionSecurity` .

```
LOGIN_KEY

ORGANIZATION_ID

PLANNER_IDENTIFIER

POLICY_ID

POLICY_ID_DERIVED

REQUEST_ID

```

**Type**
String

**Description**
The string that ties together all events
in a given user’s login session. It starts
with a login event and ends with either
a logout event or the user session
expiring.

For example: `GeJCsym5eyvtEK2I`

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
The 15-character ID of the policy being
evaluated.

For example: `00530000009M943`

**Type**
ID

**Description**
The 18-character case-insensitive ID of
the policy being evaluated.

For example:

```
  00590000000I1SNIA0

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A
transaction can contain one or more
events. Each event in a given transaction
has the same `REQUEST_ID` .

For example:

```
                      3nWgxWbDKWWDIk0FKfF5DV

```

```
RESULT

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The outcome of evaluating the policy.

For example: `TRIGGEREDzzz` or

```
  NOT TRIGGERED

```

**Type**
Number

**Description**
The amount of time that the request
took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can
use this value to identify all user events
within a session. When a user logs out
and logs in again, a new session is
started.

For example: `d7DEq/ANa7nNZZVD`

**Type**
String

**Description**
The access time of Salesforce services
in GMT.

For example:

```
  20130715233322.670

```

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services
in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example:
`2015-07-27T11:32:59.555Z` .
Timezone is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
String

**Description**
The URI of the page that’s receiving the
request.

For example: `/home/home.jsp`

**Type**
ID

**Description**
The 18-character case insensitive ID of
the URI of the page that’s receiving the
request.

**Type**
ID

**Description**
The 15-character ID of the user who is
using Salesforce services through the
UI or the API.

For example: `00530000009M943`

**Type**
ID

**Description**
The 18-character case insensitive ID of
the user who is using Salesforce services
through the UI or the API.

For example:

```
  00590000000I1SNIA0

```


Standard Objects EventLogFile Supported Event Types

##### UI Telemetry Navigation Timing Event Type

UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from the
[UI Telemetry Resource Timing Event on page 2393 and includes requests initiated with either the Fetch API or the XMLHttpRequest API.](https://fetch.spec.whatwg.org/)
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

CLIENT_ID

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CLIENT_IP

CONNECT_END

CONNECT_START

CONNECTION_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such
as a login from AppExchange, is shown as `Salesforce.com IP` .

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

The time in milliseconds after the browser completes the Domain Name System (DNS)
lookup and begins connecting to a server so that it can retrieve a resource.

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
DECODED_BODY_SIZE

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

DOM_COMPLETE

DOM_CONTENT_LOADED_EVENT_END

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

**Description**
The time in milliseconds when the page’s `readyState` property is set to `complete` .
Indicates that the page and its subresources have finished loading.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the page’s `DOMContentLoaded` event handler
completes.

To calculate the processing time for the `DOMContentLoaded` event handler, subtract
the `DOM_CONTENT_LOADED_EVENT_START` time from the
`DOM_CONTENT_LOADED_EVENT_END` time.

```
DOM_CONTENT_LOADED_EVENT_START

DOM_INTERACTIVE

DOMAIN_LOOKUP_END

DOMAIN_LOOKUP_START

DURATION

```

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
The time in milliseconds when the page’s `readyState` is set to `interactive` .
Indicates that the page has finished loading, but subresources, such as images and scripts,
are still loading.

**Type**
Number

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from
the `DOMAIN_LOOKUP_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from
the `DOMAIN_LOOKUP_END` time.

**Type**
Number

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`LOAD_EVENT_END` time.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
ENCODED_BODY_SIZE

EVENT_TYPE

FETCH_START

FIRST_INTERIM_RESPONSE_START

INITIATOR_TYPE

LOAD_EVENT_END

```

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

To calculate the time from when the browser sends a request to when it starts to receive
an interim response, subtract the `REQUEST_START` time from the
`FIRST_INTERIM_RESPONSE_START` time.

**Type**
String

**Description**
The HTML element that initiates the resource load.

**Example**
`css`, `image`, `link`

**Type**
Number

**Description**

The time in milliseconds when the page’s `load` event handler completes.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

To calculate the processing time for the `load` event handler, subtract the
`LOAD_EVENT_START` time from the `LOAD_EVENT_END` time.

```
LOAD_EVENT_START

LOGIN_KEY

NAVIGATION_TYPE

NEXT_HOP_PROTOCOL

ORGANIZATION_ID

```

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
OS_NAME

OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_URL

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

**Example**
`task`, `contacts`

**Type**
String

**Description**
The relative URL of the top-level Lightning Experience page that the user opened. The
page can contain one or more Lightning components. Multiple record IDs can be associated
with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REDIRECT_COUNT

REDIRECT_END

REDIRECT_START

RENDER_BLOCKING_STATUS

REQUEST_ID

REQUEST_START

```

**Type**
Number

**Description**
The total number of redirects since the last non-redirect navigation in the current browsing
context.

**Type**
Number

**Description**

The time in milliseconds when the browser receives the last byte of the response of the
final redirect.

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
The status that indicates whether the resource can block or delay the browser from
rendering page content.

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**

The time in milliseconds when the browser starts to request the resource from the server.

To calculate the total request time, subtract the `REQUEST_START` time from the
`RESPONSE_START` time.

```
RESPONSE_END

RESPONSE_START

RESPONSE_STATUS

SDK_APP_TYPE

```

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

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SDK_APP_VERSION

SDK_VERSION

SECURE_CONNECT_START

SERVER_REQUEST_ID

SESSION_KEY

START_TIME

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

The time in milliseconds when the browser begins the handshake process that secures
the connection.

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP

TIMESTAMP_DERIVED

TRANSFER_SIZE

UI_EVENT_RELATIVE_TIMESTAMP

UI_EVENT_TIMESTAMP

UI_ROOT_ACTIVITY_ID

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
UI_THREAD_RESPONSE_DELAY

UNLOAD_EVENT_END

UNLOAD_EVENT_START

URL

USER_ID

USER_ID_DERIVED

```

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_TYPE

WORKER_START

```

SEE ALSO:

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
If a service worker is installed, the time in milliseconds when the active service worker
receives the `fetch` event.

To measure the service worker processing time, subtract the `WORKER_START` time from
the `FETCH_START` time.

EventLogFile Supported Event Types

EventLogFile

##### UI Telemetry Resource Timing Event

UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 61.0 and later.](https://fetch.spec.whatwg.org/)

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

For information about resource timing attributes, including a diagram of the order that attributes follow, see section 4.6 of the W3
[Standards on Resource Timing.](https://www.w3.org/TR/resource-timing/)

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

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP.”

**Example**

```
  96.43.144.26

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CONNECT_END

CONNECT_START

CONNECTION_TYPE

DECODED_BODY_SIZE

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

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
Number

**Description**
The size in octets of the HTTP message body after the removal of any applied content
encoding.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

DOMAIN_LOOKUP_END

DOMAIN_LOOKUP_START

DURATION

```

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

**Description**

The time in milliseconds when the browser completes a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
Number

**Description**

The time in milliseconds when the browser starts a DNS lookup for a resource.

To calculate the DNS lookup time, subtract the `DOMAIN_LOOKUP_START` time from the
`DOMAIN_LOOKUP_END` time.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The total duration in milliseconds of the event from the `START_TIME` to the
`RESPONSE_END` time.

```
ENCODED_BODY_SIZE

EVENT_TYPE

FETCH_START

FIRST_INTERIM_RESPONSE_START

INITIATOR_TYPE

LOGIN_KEY

```

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

**Example**
`css`, `image`, `link`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
                   GeJCsym5eyvtEK2I

```

```
NEXT_HOP_PROTOCOL

ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

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

**Example**
`Android`, `iOS`, `OSX`, `Window`

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique entity identifier of the event.

**Example**

```
                   0013000000I3zJAAAZ

```

```
PAGE_ENTITY_TYPE

PAGE_URL

REDIRECT_END

REDIRECT_START

RENDER_BLOCKING_STATUS

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `blocking` : the resource can block rendering.

**•** code `non-blocking` : the resource doesn’t block rendering.

```
REQUEST_ID

REQUEST_START

RESPONSE_END

RESPONSE_START

RESPONSE_STATUS

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   200

```

```
SDK_APP_TYPE

SDK_APP_VERSION

SDK_VERSION

SECURE_CONNECT_START

SERVER_REQUEST_ID

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   346000000087551ecb

```

```
SESSION_KEY

START_TIME

TIMESTAMP

TIMESTAMP_DERIVED

TRANSFER_SIZE

UI_EVENT_RELATIVE_TIMESTAMP

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   29322.23

```

```
UI_EVENT_TIMESTAMP

UI_ROOT_ACTIVITY_ID

UI_THREAD_RESPONSE_DELAY

URL

USER_ID

USER_ID_DERIVED

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_TYPE

WORKER_START

```

SEE ALSO:

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


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

LOGIN_KEY

ORGANIZATION_ID

PLANNER_IDENTIFIER

QUERY_IDENTIFIER

QUERY_TYPE

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


Standard Objects EventLogFile Supported Event Types

**Possible Values**

**•** soql

**•** filter

**•** report

```
SESSION_KEY

SQL_ID

##### URI Event Type

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
The unique identifier generated for the database query.

URI events contain details about user interaction with the web browser UI.

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


Standard Objects EventLogFile Supported Event Types

```
DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REFERRER_URI

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


Standard Objects EventLogFile Supported Event Types

**Description**
The referring URI of the page that’s receiving the request.

```
REQUEST_ID

REQUEST_STATUS

RUN_TIME

SESSION_KEY

```

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
The URI of the page that’s receiving the request. For more
granular URI information for Lightning Experience and the
Salesforce app, see the Lightning Error, Lightning Interaction,
Lightning Page View, and Lightning Performance event types.

**Examples**
`/aura` (Lightning Experience), `/lightning` (Lightning
Experience and the Salesforce app), `/home/home.jsp`
(Salesforce Classic)

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

##### Visualforce Request Event Type

Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI).

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CONTROLLER_TYPE

CPU_TIME

DB_BLOCKS

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

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

```
DB_CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

HTTP_METHOD

IS_AJAX_REQUEST

IS_FIRST_REQUEST

```

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


Standard Objects EventLogFile Supported Event Types

```
LOGIN_KEY

MANAGED_PACKAGE_NAMESPACE

ORGANIZATION_ID

PAGE_NAME

QUERY

REQUEST_ID

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
If the page is part of a managed package, the namespace of
that package.

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


Standard Objects EventLogFile Supported Event Types

```
REQUEST_SIZE

REQUEST_STATUS

REQUEST_TYPE

RESPONSE_SIZE

```

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

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

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


Standard Objects EventLogFile Supported Event Types

**Description**
The size of the response, in bytes.

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

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

```
USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

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

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared


Standard Objects EventLogFile Supported Event Types

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

```
VIEW_STATE_SIZE

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Wave Change Event Type

**Type**
Number

**Description**
The size of the Visualforce view state, in bytes.

Wave Change events represent route or page changes made in the CRM Analytics user interface. A Wave Change event type is captured
every time the user opens a new CRM Analytics asset or tab, switches between tabs, or changes dashboard pages. Wave Change events
are logged when opening new tabs and switching back to previously opened tabs.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ANALYTICS_MODE

```

**Type**
String

**Description**
The location in which the dashboard is
displayed. In the Salesforce mobile app,
embedded dashboards are logged as
`embedded` first. When a user interacts
with the dashboard, a full-screen
dashboard is displayed to allow for user
interaction, and is logged as
`mobileNative` .

Possible values are:


Standard Objects EventLogFile Supported Event Types

**•** `studio` —Analytics Studio

**•** `tab` —Analytics tab

**•** `embedded`                     - Embedded in Aura
or Lightning.

**•** `embeddedInCommunities`                     Embedded in Experience Cloud.

**•** `mobileNative`                     - CRM Analytics
mobile app for iOS/Android or
Salesforce mobile app for
iOS/Android

```
CLIENT_IP

CPU_TIME

EVENT_TYPE

IS_MOBILE

IS_NEW

```

**Type**
String

**Description**
The IP address of the client that’s using
Salesforce services. A Salesforce internal
IP (such as a login from AppExchange)
is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to
complete the request. This field
indicates the amount of activity taking
place in the app server layer.

**Type**
String

**Description**
The type of event. The value is always
`WaveChange` .

**Type**
Boolean

**Description**
If `true`, the dashboard is displayed in
the Tableau CRM mobile app for iOS and
Android, in the Salesforce mobile app
for iOS and Android, or in a mobile
browser.

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Description**
The field indicates that this action opens
a new tab or goes back to a previously
opened tab. If the change routes to a
new page, the value of this field is true.
If it routes to an existing page, this field
is false.

```
LOGIN_KEY

ORGANIZATION_ID

PAGE_CONTEXT

```

**Type**
String

**Description**
The string that ties together all events
in a given user’s login session. It starts
with a login event and ends with either
a logout event or the user session
expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The context of the page in which the
dashboard is displayed. In the Salesforce
mobile app, embedded dashboards are
logged as `aura` first. When a user
interacts with the dashboard, a
full-screen dashboard is displayed to
allow for user interaction, and is logged
as `iOS` or `android` .

Possible values are:

**•** `aura` —Lightning Components

**•** `vf` —Visualforce

**•** `iOS`  - CRM Analytics or Salesforce
mobile app for iOS

**•** `android`  - CRM Analytics or
Salesforce mobile app for Android


Standard Objects EventLogFile Supported Event Types

```
PAGE_ID

RECORD_ID

REOPEN_COUNT

REQUEST_ID

RUN_TIME

SAVED_VIEW_ID

SESSION_KEY

```

**Type**
String

**Description**

The ID of the CRM Analytics dashboard
page.

This field is only available in v58.0 and
higher.

**Type**
String

**Description**
The Salesforce ID of the CRM Analytics
object.

**Type**
Number

**Description**
If `IS_NEW` is false, the number of times
that an existing page opens.

**Type**
String

**Description**
The unique ID of a single transaction. A
transaction can contain one or more
events. Each event in a given transaction
has the same `REQUEST_ID` .

For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request
took in milliseconds.

**Type**
String

**Description**
The ID of the CRM Analytics dashboard
saved view.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can
use this value to identify all user events
within a session. When a user logs out
and logs in again, a new session is
started.

For example: `d7DEq/ANa7nNZZVD` .

```
TAB_ID

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

URI

```

**Type**
String

**Description**
The ID of the particular Analytics tab in
the user interface.

For example:
`dashboard-0FKB0000000Ec64GDK` .

**Type**
String

**Description**
The access time of Salesforce services
in GMT.

For example:
`20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services
in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example:
`2015-07-27T11:32:59.555Z` .
Timezone is GMT.

**Type**
String

**Description**
The CRM Analytics object type.

**Type**
String

**Description**
The URI of the page that’s receiving the
request.


Standard Objects EventLogFile Supported Event Types

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

VIEW_MODE

WAVE_SESSION_ID

WAVE_TIMESTAMP

```

**Type**
ID

**Description**
The 18-character case insensitive ID of
the URI of the page that’s receiving the
request.

**Type**
Id

**Description**
The 15-character ID of the user who’s
using Salesforce services through the
UI or the API.

For example: `00530000009M943` .

**Type**
Id

**Description**
The 18-character case insensitive ID of
the user who’s using Salesforce services
through the UI or the API.

For example:
`00590000000I1SNIA0` .

**Type**
String

**Description**
The view mode for the CRM Analytics
asset. Possible values include `view`,
`edit`, `present`, `json`, or `print` .

**Type**
String

**Description**
The ID of a particular session of CRM
Analytics. Use this field to determine
which log lines originated from a
particular session.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The time at which this log line was
generated.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

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

**•** `Lens` —A _lens_ is a view into a dataset used in an exploratory mode or to get insight
to a specific business question. The lens can be saved and shared independently. It
can also be clipped to a dashboard.

**•** `Dashboard` —A _dashboard_ is a curated set of charts, metrics, and tables based on
the data in one or more lenses.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such
as a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**
96.43.144.26


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CPU_TIME

DATASET_IDS

DOWNLOAD_ERROR

DOWNLOAD_FORMAT

EVENT_TYPE

LOGIN_KEY

NUMBER_OF_RECORDS

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Description**
Comma-separated list of IDs of utilized data sets.

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The number of records exported.

```
ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**
00D000000000123

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
The user’s unique session ID. You can use this value to identify all user events within a
session. When a user logs out and logs in again, a new session is started.

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

WAVE_SESSION_ID

WAVE_TIMESTAMP

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
The 18-character case insensitive ID of the user who’s using Salesforce services through
the UI or the API.

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


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The time at which this log line was generated.

##### Wave Interaction Event Type

Wave Interaction events represent route or page changes made in the CRM Analytics user interface. A Wave Interaction event type is
captured when a tab is closed. It also collates the interaction statistics over the life of the tab, including total open time, read time, and
so on. These statistics are aggregated as you go to other tabs and return, and logged only once when the tab is closed.

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


Standard Objects EventLogFile Supported Event Types

For example: `GeJCsym5eyvtEK2I` .

```
NUM_CLICKS

NUM_SESSIONS

ORGANIZATION_ID

READ_TIME

RECORD_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

```

**Type**
Number

**Description**
The number of clicks performed on a page in the CRM Analytics
user interface.

**Type**
Number

**Description**
The number of times a user returned to a particular page.

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


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

```
TAB_ID

TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_TIME

TYPE

URI

```

**Type**
String

**Description**
The ID of the particular Analytics tab in the user interface.

**Example**
dashboard-0FKB0000000Ec64GDK

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

##### Wave Performance Event Type

Wave Performance events help you track trends in your Analytics performance.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

EPT

EVENT_TYPE

IS_INITIAL

LOGIN_KEY

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
The experienced page time in milliseconds.

**Type**
String

**Description**
The type of event. The value is always `WavePerformance` .

**Type**
Boolean

**Description**
Indicates whether the event is for the initial load of dashboard
( `true` ) or not ( `false` ).

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

```
NAME

ORGANIZATION_ID

QUERY_ID

RECORD_ID

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The asset title or query string.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
This field is deprecated in API version 50.0. The number of
queries can be determined using the Uri Event type logs,
referenced here on page 2406

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


Standard Objects EventLogFile Supported Event Types

```
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
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The ID of the particular Analytics tab in the user interface.

**Example**
dashboard-0FKB0000000Ec64GDK

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
The CRM Analytics object type. This field is scheduled for
deprecation in v59.0. Use the new `IS_INITIAL` field to
determine the log line type.

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


### Standard Objects EventRelation EventRelation

Represents a person (a user, lead, or contact) or a resource (such as a conference room) invited to an event. This object lets you add or
remove invitees from an event and use the API to manage invitees’ responses to invitations. If Shared Activities is enabled, EventRelation
can also represent other objects that are related to an event. EventRelation does not support triggers, workflow, or data validation rules.

### EventRelation allows a variable number of relationships and handles deleted events differently, depending on whether Shared Activities

is enabled.

A non-recurring event can have up to 1,000 invitees. A recurring event can have up to 100 invitees.

**If Shared Activities Isn’t Enabled**

### • EventRelation records only represent invitees (contacts, users, and resources).

**•** An event can be related to one contact or lead.

**If Shared Activities Is Enabled**

### • EventRelation records can represent:

**–** Invitees ( `IsInvitee=` is set to `true` )

OR

**–** Related contacts or lead ( `IsParent` is set to `true` )

**•** An event can be related to up to 50 contacts or one lead. These people may or may not be invitees. The number of allowed
invitees is not affected by the number of related contacts. If a contact or lead is also an invitee, there is one EventRelation record
for that person with `IsInvitee` and `IsParent` are set to `true` .

**•** An event can be related to a lead, contact, resource, account, or opportunity.

**•** An event can be related to a custom object that has the `HasActivities` attribute set to `true` .

**•** If you delete an event, then relations between the event and any specified contacts, leads, and other records are also deleted.

**•** If you delete the EventRelation record representing a relation then the corresponding relation field may be cleared on the event.

**•** If you delete the EventRelation record representing the `WhoId` on an event, then another Who, if any, from the event’s
`EventWhoIds` field will be promoted to the `WhoId` .

**•** If you restore a deleted event, relations between the event and any specified contacts, leads, and records are also restored. The
`WhoId`, `WhatId`, and `AccountId` field values are recalculated using the field values on EventRelation.

Whether or not Shared Activities is enabled, an event can be related to one other kind of record, such as an account, an opportunity, or
a custom object.

Note:

**•** With API versions 26.0 and later, the EventRelation object replaces the EventAttendee object, and the EventAttendee object
is no longer visible. You can still query the EventAttendee object using packages that support API versions 25.0 and earlier, or
by using Apex.

**•** An EventRelation object can’t be created for a child event.

### • EventRelation includes deactivated users.

**•** In API versions 25.0 and earlier, you can’t use `query()`, `delete()`, or `update()` with events related to more than one
contact.


Standard Objects EventRelation

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
AccountId

EventId

IsDeleted

IsInvitee

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the Account ID of the relation. For information on IDs, see ID Field Type.
`AccountId` is visible when Shared Activities is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Contains the ID of the event. This value can’t be changed after it’s been specified.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is `Deleted` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects EventRelation

**Field** **Details**

**Description**
Indicates whether the relation is an invitee.

**•** `IsInvitee` is visible while Shared Activities is being enabled, after it has been
enabled, and while it is being disabled.

**•** `IsInvitee` defaults to `true` while Shared Activities is being enabled, after
it has been enabled, and while it is being disabled if `IsInvitee`, `IsParent`,
and `IsWhat` are not set. This configuration ensures compatibility when Shared
Activities isn’t enabled and EventRelation represents event invitees only.

**•** `IsInvitee` defaults to `false` when Shared Activities is enabled if
`IsParent` is set to `true` .

```
IsParent

IsWhat

RelationId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
`IsParent` is visible only when Shared Activities is enabled. When `false`, indicates
that the relation is an invitee (a contact, lead, or user). When `true`, indicates that
the relation is a Who or What, as determined by `IsWhat` field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
`IsWhat` is visible only when Shared Activities is enabled. The value is relevant only
if `IsParent` is `true` . When `IsWhat` is `true`, the relation specified by
`RelationId` is a What (an account, opportunity, custom object, etc.). When
`IsWhat` is `false`, the relation specified by `RelationId` is a Who (a contact,
lead, or user).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Contains the ID of the person (User, Contact, or Lead) or the resource invited to an
event. When Shared Activities is enabled, `RelationId` can also contain the ID of
an account, opportunity, or other object related to an event.

This value can’t be changed after it’s been specified.

This is a polymorphic relationship field.


Standard Objects EventRelation

**Field** **Details**

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

```
RespondedDate

Response

Status

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the most recent date and time when the invitee responded to an invitation
to an event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains optional text that the invitee can enter when responding to an invitation
to an event.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the invitee status with one of the following values:

**•** `New` : Invitee has received the invitation but hasn’t yet responded. This value is
the default.

**•** `Declined` : Invitee has declined the invitation.

**•** `Accepted` : Invitee has accepted the invitation.

Note: `Uninvited` and `Maybe` aren’t currently supported.

**•** Invitee related lists display slightly different content. In the Salesforce mobile app, the invitee related list includes invitees only,
whereas in the full site, it also includes the event owner. To reproduce the full site functionality in the Salesforce mobile app, use the
following API queries.


Standard Objects EventRelation

If you use Shared Activities in your Salesforce org, use this query:

```
     SELECT RelationId FROM EventRelation WHERE isInvitee = true AND eventId='[Event_Id]'

```

where _`Event_Id`_ is the child event’s ID.

If you don’t use Shared Activities, use this query:

```
     SELECT RelationId FROM EventRelation WHERE eventId='[Event_Id]'

```

These queries get the main event’s relations and display them for the given child event. To further filter the results, add a `WHERE`
clause.

**Assigning resource attendance status**
You can add a resource to an event only when the resource is available. The only attendance status that can be assigned to resources
is Accepted. Events can’t be saved when resources you’ve added aren’t available.

**Create an invitee if Shared Activities is enabled (or during the process of enabling it or rolling back)**
If the invitee is already a contact or lead, update `IsInvitee` to `true` .

If the invitee is not already a contact or lead, create an EventRelation object for the invitee with `IsInvitee` set to `true` .

**Create an invitee if Shared Activities is not enabled**
Create an EventRelation object for the invitee.

**Insert a contact or lead relation**

```
     EventRelation er = new EventRelation(EventId = '00UD0000005zijH',

       RelationId = '003D000000Q8aeV', isParent = true, isInvitee = false);

     insert er;

```

**Determine what events a given invitee is attending**
To determine all the events that a particular person is attending during a given time period (for example, next week), you can have
a client application query the Event object for a given date range, iterate through the results, and, for each event, query the
EventRelation object to determine whether the particular person ( `RelationId` ) has accepted an invitation to that event.

**Insert an invitee relation**

If `isParent`, `isWhat` and `IsInvitee` are not set, and `RelationId` is a contact, lead, user, or calendar, `IsInvitee`
defaults to `true` . This means if an EventRelation isn’t specifically inserted as a relation to a contact or lead, it’s treated as an Invitee
relation by default.

```
     EventRelation er = new EventRelation(EventId = '00UD0000005zijH',

       RelationId = '003D000000Q8adV');

     insert er;

```

**Query relations to a contact or a lead**

```
     List<EventRelation> whoRelations = [SELECT Id, Relation.Name FROM

       EventRelation WHERE EventId = '00UD0000005zijD' AND isParent = true AND isWhat =

     false];

```

**Query invitee relations**

```
     List<EventRelation> inviteeRelations = [SELECT Id, Relation.Name FROM

       EventRelation WHERE EventId = '00UD0000005zijD' AND isInvitee = true];

```


Standard Objects EventRelation

**Update an invitee relation to a contact or lead invitee relation**

```
     EventRelation er = [SELECT Id FROM EventRelation WHERE EventId =

       '00UD0000005zijD' AND isInvitee = true and isParent = false LIMIT 1];

     er.isParent = true;

     update er;

```

**Update a contact or lead relation to a contact or lead invitee relation**

```
     EventRelation er = [SELECT Id FROM EventRelation WHERE EventId =

       '00UD0000005zijD' AND isParent = true and isInvitee = false LIMIT 1];

     er.isInvitee = true;

     update er;

```

**Reproduce invitee related list functionality in the Salesforce mobile app**
Invitee related lists display slightly different content in the Salesforce mobile app and the full site. In the app, the invitee related list
includes invitees only, whereas in the full site, it also includes the event owner.

If you use Shared Activities in your Salesforce org, use the following query to reproduce the full site functionality in the Salesforce
mobile app:

```
     SELECT RelationId FROM EventRelation WHERE isInvitee = true AND eventId='[Event_Id]'

```

where _`Event_Id`_ is the child event’s ID.

If you don’t use Shared Activities, use this query:

```
     SELECT RelationId FROM EventRelation WHERE eventId='[Event_Id]'

```

These queries get the main event’s relations and display them for the given child event. To further filter the results, add a `WHERE`
clause.

**Send email notifications**
To send email notifications for a given event, query EventRelation for the event, iterate through the list, examine the status, and send
email notifications to every person who accepted the invitation.

**Syncing Events with Lightning Sync**
Attendee statuses (Accepted or Maybe, Declined, or No Response) sync from Microsoft [®] Exchange or Google to Salesforce, but not
from Salesforce to Exchange or Google. Be wary of creating API flows that update attendee status in Salesforce for users set up to
sync both ways. Eventually the original Exchange or Google status overrides the update made in Salesforce.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EventRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

Event

EventWhoRelation

Overview of Salesforce Objects and Fields


### Standard Objects EventBusSubscriber EventBusSubscriber

Represents a trigger, process, or flow that’s subscribed to a platform event or a change data capture event. Doesn’t include CometD or
Pub/Sub API subscribers.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

### EventBusSubscriber is read only and can only be queried. As of Summer ’20 and later, only your Salesforce org's internal users can access

this object.

Fields

**Field** **Details**

```
ExternalId

IsPartitioned

LastError

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the subscriber. For example, the trigger ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the platform event Apex trigger is configured with parallel subscriptions
( `true` ) or not ( `false` ). The default value is `false` [. See Platform Event Processing at Scale](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm)
[with Parallel Subscriptions for Apex Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm) _Platform Events Developer Guide_ .

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message that the last thrown `EventBus.RetryableException` contains.
This field applies to Apex triggers only. Available in API version 43.0 and later.


Standard Objects EventBusSubscriber

**Field** **Details**

```
LastProcessed

LastPublished

Name

Position

Retries

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last event that the subscriber processed. This field replaces `Position`
as of API level 66.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last published event. This field replaces `Tip` as of API level 66.0.

Note: For high-volume platform events and change events, the value for Tip isn’t
available and is always -1.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subscribed item, such as the trigger or process name. If the subscribed
item’s name is “Process”, at least one flow Pause element is subscribed to the event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last event that the subscriber processed. This field has been deprecated
as of API level 66.0 and should no longer be used. Use `LastProcessed` instead. This
field may not be properly represented if the value exceeds the maximum integer size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the trigger was retried due to throwing the
`EventBus.RetryableException` . This field applies to Apex triggers only. Available
in API version 43.0 and later.


Standard Objects EventBusSubscriber

**Field** **Details**

```
Status

Tip

Topic

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the subscriber. Can be one of these values:

**•** `Error`  - The subscriber was disconnected and stopped receiving published events.
A trigger reaches this state when it exceeds the number of maximum retries with the
`EventBus.RetryableException` . Trigger assertion failures and unhandled
exceptions don’t cause the error state. We recommend limiting the retries to fewer than
nine times to avoid reaching this state. When you fix and save the trigger, or for a
managed package trigger, if you redeploy the package, the trigger resumes automatically
from the tip, starting from new events. Also, you can resume a trigger subscription in
the subscription detail page that you access from the platform event page.

**•** `Repartitioning` —The system is in the process of modifying the trigger's parallel
subscription configuration.

**•** `Running` —The subscriber is actively listening to events. If you modify the subscriber,
the subscription continues to process events.

**•** `Suspended` —The subscriber is disconnected and can’t receive events because a
Salesforce admin suspended it or due to an internal error. You can resume a trigger
subscription in the subscription detail page that you access from the platform event
page. To resume a process, deactivate it and then reactivate it. If you modify the
subscriber, the subscription resumes automatically from the tip, starting from new events.

[For more information, see View and Manage an Event’s Subscribers on the Platform Event’s](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm)
[Detail Page in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm) _Platform Events Developer Guide_ .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last published event. This field has been deprecated as of API level 66.0
and should no longer be used. Use `LastPublished` instead. This field may not be
properly represented if the value exceeds the maximum integer size.

Note: For high-volume platform events and change events, the value for Tip isn’t
available and is always -1.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EventRelayConfig

**Field** **Details**

**Description**
The name of the subscription channel that corresponds to a platform event or change event.
For a platform event, the topic name is the event name appended with `__e`, such as
`MyEvent__e` . For a change event, the topic is the name of the change event, such as
`AccountChangeEvent` .

```
Type

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subscriber type ( `ApexTrigger` ). If the subscriber is a process or flow Pause element,
the type is blank.

Use EventBusSubscriber to query details about subscribers to a platform event. You can get all subscribers for a particular event by
filtering on the `Topic` field, as follows.

```
SELECT ExternalId, Name, Position, Status, Tip, Type

FROM EventBusSubscriber

WHERE Topic='Low_Ink__e'

### EventRelayConfig

```

Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon
EventBridge. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** To retrieve or query this object, you must have the View Setup and Configuration permission.

**•** [This object is read-only. To configure an event relay, use EventRelayConfig in Tooling API or EventRelayConfig in Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_eventrelayconfig.htm)


Standard Objects EventRelayConfig

Fields

**Field** **Details**

```
DestinationResourceName

DeveloperName

EventChannel

Language

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the named credential, which stores the AWS account information.
The `destinationResourceName` value contains the `callout:` prefix. For example:

```
  callout:MyRelayNamedCredential

```

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
are reflected in a subscriber’s organization. Label is **Record Type Name** . This field is
automatically generated, but you can supply your own value if you create the record using
the API.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The full name of the event channel used in the event relay. For example:

```
  MyRelayChannel__chn

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the EventRelayConfig.

Possible values are:

**•** `da` —Danish

**•** `de` —German


Standard Objects EventRelayConfig

**Field** **Details**

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

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the EventRelayConfig. In the UI, this field is Event Relay Config.

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


Standard Objects EventRelayConfig

**Field** **Details**

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

```
RelayOption

State

UsageType

```

**Type**
textarea

**Properties**
Nillable

**Description**
A JSON-encoded string that contains an option for resuming an event relay after the system
recovers from an error. This option is used if the event relay can't resume after the last relayed
event. The options available are:

**•** `"{\"ReplayRecovery\":\"LATEST\"}"` —(Default) Start relaying events
from new events received in the event bus. Use this option if you aren’t interested in
missed events while the relay was down.

**•** `"{\"ReplayRecovery\":\"EARLIEST\"}"` —Resend all events stored in
the event bus and relay new events thereafter. The event bus stores events for up to
three days. Use this option if you want to reprocess all stored events and catch up on
missed events.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The execution state of the event relay. Possible values are:

**•** `RUN` —The event relay is running and actively relaying event messages from Salesforce
to Amazon EventBridge.

**•** `PAUSE` —An administrator paused the event relay. No events are relayed to Amazon
EventBridge during this status. All current state information is saved.

**•** `STOP` —(Default) The event relay is stopped and no events are relayed to Amazon
EventBridge. All current state information is deleted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.


### Standard Objects EventRelayFeedback EventRelayFeedback

Represents execution state information about an event relay from Salesforce to Amazon EventBridge for platform events and change
data capture events. Query this object to get information such as the event relay status and any error message. This object is available
in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ErrorCode

ErrorIdentifier

ErrorMessage

ErrorTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code of the last error that occurred during the relay of event messages. For a list
of possible error codes and messages, see Error Codes.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier of an unexpected system error that occurred during the relay of event messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The error message of the last error that occurred during the relay of event messages. For a
list of possible error codes and messages, see Error Codes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last error occurred during the relay of
event messages.


Standard Objects EventRelayFeedback

**Field** **Details**

```
EventRelayConfigId

EventRelayNumber

LastRelayedEventTime

RemoteResource

Status

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the event relay configuration that this feedback record is collecting the execution
information of.

This field is a relationship field.

**Relationship Name**
EventRelayConfig

**Relationship Type**
Lookup

**Refers To**
EventRelayConfig

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that identifies the EventRelayFeedback record. This field is of type Auto Number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last event was relayed to Amazon
EventBridge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the partner event source associated with the event relay. It is in the format
`aws.partner/salesforce.com/` _**`orgID`**_ `/` _**`channelID`**_ . For example:
`aws.partner/salesforce.com/00DRM000000Fxts2AC/0YLRM0000004Dfg4AE` .

**Type**
picklist


Standard Objects EventRelayFeedback

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the event relay.

Possible values are:

**•** `ERROR`                   - The event relay encountered an error while running or during a state change
that the administrator initiates. During the `ERROR` state, no events are relayed to Amazon
EventBridge. The system attempts periodically to recover from the error. If it succeeds,
the `Status` field value changes to `RUNNING` or to the new state that the administrator
selected. The event relay attempts to resume sending events from the event bus from
where it left off. In rare occasions, if it can't resume after the last relayed event, it uses
the error recovery option in the `relayOption` field of EventRelayConfig to determine
where to resume from.

**•** `DELETED` —Reserved for future use.

**•** `PAUSED`                   - An administrator paused the event relay. No events are relayed to Amazon
EventBridge during this status. When an administrator resumes the event relay, events
are relayed from the last position in the event bus, as long as they're within the retention
window.

**•** `RUNNING`                   - The event relay is running and actively relaying events from Salesforce to
Amazon EventBridge.

**•** `STOPPED` —The event relay is stopped and no events are relayed to Amazon
EventBridge. Some state information stored in EventRelayFeedback fields is deleted, such
as `LastRelayedEventTime` and error fields. When the event relay is resumed,
only new events are relayed.

The default value is `STOPPED` .

```
UsageType

```

Error Codes

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

This table contains the error codes and messages that a query on EventRelayFeedback can return in the `ErrorCode` and
`ErrorMessage` fields.


### Standard Objects EventStagedInviteeEmail EventStagedInviteeEmail

Represents the relationship between an event and an email address invited to the event that doesn’t match to a user, contact, or lead
record. Data about the unmatched email address is represented in StagedInviteeEmail. This object represents event-related details, such
as the invitee's attendance response to the event. This object is available in API version 66.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on.

Fields

**Field** **Details**

```
EventId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related event record.

This field is a relationship field.

**Relationship Name**
### Event

**Refers To**
### Event


Standard Objects EventStagedInviteeEmail

**Field** **Details**

```
IsArchived

IsOrganizer

Name

StagedInviteeEmailId

Status

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is archived ( `true` ) or not ( `false` ). This value helps manage
high volumes of archived events, improving query performance.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the invitee is the event organizer ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The invited email address.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related invitee email address record.

This field is a relationship field.

**Relationship Name**
StagedInviteeEmail

**Relationship Type**
Master-detail

**Refers To**
StagedInviteeEmail

**Type**
picklist


### Standard Objects EventTag

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The attendance response to the event from the invitee.

Possible values are:

**•** `Accepted`

**•** `Declined`

**•** `Maybe`

**•** `New`

**•** `Uninvited`

### EventTag

Associates a word or short phrase with an Event.

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

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.


### Standard Objects EventWhoRelation

**Field Name** **Details**

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

EventTag stores the relationship between its parent TagDefinition and the Event being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### EventWhoRelation

Represents the relationship between an event and a lead or contacts. This derived object is a filtered version of the EventRelation on
page 2435 object; that is, IsParent is _`true`_ and IsWhat is _`false`_ . It doesn’t represent relationships to invitees or to accounts, opportunities,
or other objects. This object is available in API versions 29.0 and later.

### EventWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared

Activities for your organization.

Note: EventWhoRelation objects aren’t created for child events.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects Expense

Fields

**Field Name** **Details**

```
EventId

RelationId

Type

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the person related to the event is a contact or lead.

**Apex example that queries relations to a contact or lead**

```
  List<EventWhoRelation> whoRelations = [SELECT Id, Relation.Name FROM

  EventWhoRelation WHERE EventId = '00UD0000005zijD'];

```

SEE ALSO:

Event

EventRelation

### Expense

Represents an expense linked to a work order. Service resource technicians can log expenses, such as tools or travel costs. This object is
available in API version 49.0 and later.


Standard Objects Expense

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

Amount

CurrencyIsoCode

Description

Discount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the account associated with the linked work order.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The amount of the expense.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage deducted from the `Subtotal` price. Available in version 51.0 and later.


Standard Objects Expense

**Field** **Details**

```
ExpenseEndDate

ExpenseNumber

ExpenseStartDate

ExpenseType

LastReferencedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the expense was incurred over multiple days, the Expense End Date is the last day that the
expense covers.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that uniquely identifies the expense.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the expense was incurred over multiple days, the Expense Start Date is the first day that
the expense covers.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of expense. Possible values are:

**•** `Billable`

**•** `Non-Billable`

The default value is `Billable` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects Expense

**Field** **Details**

```
LastViewedDate

OwnerId

Quantity

Subtotal

Title

TotalPrice

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the expense record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of items purchased in this record. Available in version 51.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The subtotal price calculated as the product of `Quantity` and `UnitPrice` . Available
in version 51.0 and later.

This is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense.

This field is available in API version 50.0 and later.

**Type**
currency


Standard Objects Expense

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total price of the transaction which is equal to the discounted subtotal: `Subtotal`                           ( `Discount`                                    - `Subtotal` ). Available in version 51.0 and later.

This is a calculated field.

```
TransactionDate

UnitPrice

WorkOrderId

```

Associated Objects

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The day that the expense was incurred, or the payment date for the expense.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The price of one item on the record. Available in version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work order associated with the expense.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseChangeEvent (API version 55.0)**
Change events are available for the object.

**ExpenseFeed**

Feed tracking is available for the object.

**ExpenseHistory**

History is available for tracked fields of the object.

**ExpenseOwnerSharingRule**

Sharing rules are available for the object.

**ExpenseShare**

Sharing is available for the object.


### Standard Objects ExpenseReport ExpenseReport

Represents a report that summarizes expenses. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

### `ExpenseReportNumber`

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects ExpenseReport

**Field** **Details**

```
LastViewedDate

OwnerId

Title

TotalExpenseAmount

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the expense report record.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense report.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all expense entries in the report.

This is a calculated field.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportFeed**

Feed tracking is available for the object.

**ExpenseReportHistory**

History is available for tracked fields of the object.

**ExpenseReportShare**

Sharing is available for the object.


### Standard Objects ExpenseReportEntry ExpenseReportEntry

Represents an entry in an expense report. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

ExpenseId

### `ExpenseReportEntryNumber`

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the expense.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The expense that corresponds to the expense report entry.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the expense report entry.


Standard Objects ExpenseReportEntry

**Field** **Details**

```
ExpenseReportId

ExpenseType

LastReferencedDate

LastViewedDate

Title

TransactionDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The expense report that’s associated with the expense report entry.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The type of expense. Possible values are:

**•** `Billable`

**•** `Non-Billable`

The default value is `Billable` .

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
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A title that identifies the expense.

**Type**
date


### Standard Objects ExpressionFilter

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The day that the expense was incurred, or the payment date for the expense.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseReportEntryFeed**

Feed tracking is available for the object.

**ExpenseReportEntryHistory**

History is available for tracked fields of the object.

### ExpressionFilter

Represents a logical expression that’s used to control the execution of macro instructions. This object is available in API version 46.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContextId

FilterConditionLogic

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the MacroInstruction object that contains the expression.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The filter conditions to use and the order in which to apply them. For example, ‘1
AND 2’ evaluates condition 1 and then condition 2.


### Standard Objects ExpressionFilterCriteria

**Field** **Details**

```
FilterDescription

Name

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. A description of the filter expression that helps to explain the logic to users. For
example, ‘Applies to New cases.’

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the expression.

The ExpressionFilter object is used with the `IF` and `ELSEIF` operations in a MacroInstruction. It lets you specify a logical expression
that determines whether macro instructions are executed. The object indicates whether any or all conditions must be true.

To represent the conditions that are evaluated, this object uses one or more ExpressionFilterCriteria child objects. The ExpressionFilter
to be used with each criteria is specified in the ExpressionFilterCriteria’s ExpressionFilterId field.

For example, to represent the following conditional statement, the ExpressionFilter object specifies the `FilterConditionLogic`
field as `1 AND 2`, where 1 and 2 are ExpressionFilterCriteria objects. In this example, condition 1 is `Case.Status EQUALS New`,
and condition 2 is `Case.Origin EQUALS Phone` .

```
IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)

    Select Email QuickAction

    Set Subject…

    Set To…

    Set Body…

    Submit

ENDIF

### ExpressionFilterCriteria

```

Represents a condition in an expression that’s used to control the execution of macro instructions. This object is available in API version
46.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects ExpressionFilterCriteria

Fields

**Field** **Details**

```
ExpressionFilterId

FilterTarget

FilterTargetValue

Name

Operation

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the ExpressionFilter object that references this condition.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The target object or field used in the condition. For example, to create a condition
that applies to new cases, use `Case.Status` as the `FilterTarget` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. The value that’s compared to the value of the FilterTarget. For example, to create
a condition that applies to new cases, use `New` as the `FilterTargetValue` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Optional. A label for the condition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the operator used to compare the target field and the target value. For
example, to create a condition that applies to new cases, use EQUALS for the `Operation`
field, as in `Case.Status EQUALS New` .

**•** `EQUALS`


### Standard Objects ExpressionSetConstraintObj

**Field** **Details**

**•** `NOTEQUALS`

**•** `CONTAINS`

**•** `NOTCONTAIN`

```
SortOrder

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The order in which the criteria are evaluated.

ExpressionFilterCriteria is a child object of the ExpressionFilter object. Use these objects with the `IF` and `ELSEIF` operations in a
MacroInstruction to control instruction execution. Each condition in a ExpressionFilterCriteria compares a target object or field to a value
using a condition operator; for example, `Case.Status EQUALS New` .

### ExpressionSetConstraintObj

Represents the association between a Product object and the constraint model tags defined in a given constraint model. This object is
available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in orgs where Revenue Cloud is enabled.

Fields

**Field** **Details**

```
ConstraintModelTag

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The product tag that is defined in the constraint model, for example, `Laptop` .


Standard Objects ExpressionSetConstraintObj

**Field** **Details**

```
ConstraintModelTagType

ExpressionSetId

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the product tag that is defined in the constraint model.

Possible values are:

**•** `Port`

**•** `Type`

The default value is `Type` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The expression set associated with the expression set constraint object.

This field is a relationship field.

**Relationship Name**
ExpressionSet

**Refers To**
ExpressionSet

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
the user accessed this record or list view (LastReferencedDate) but didn’t view it.

**Type**
string


### Standard Objects ExtDataShare

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the expression set constraint.

```
OwnerId

ReferenceObjectId

### ExtDataShare

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For internal use only.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The object associated with the expression set constraint object.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Refers To**
Product2, ProductClassification, ProductRelatedComponent

Represents a data share, which is a collection of Data Cloud objects that can be shared with other Data Cloud orgs or third-party partners.
This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ExtDataShare

Fields

**Field** **Details**

```
DataShareType

DataSpaceId

InboundDataShareName

InboundDataShareOrgIdentifier

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data share, indicating the direction of data flow. If `Outbound`, the data share
was created on this Data Cloud org and is shared to third-party partners or with another
Data Cloud org. If `Inbound`, the data share comes from another Data Cloud org and is
shared to this Data Cloud org.

Possible values are:

**•** `Inbound`

**•** `Outbound`

The default value is `Outbound` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the data space under which the data share was created.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the data share in the source Data Cloud org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the source Data Cloud org that shared a data share with the target org.


Standard Objects ExtDataShare

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

ObjectCount

```

Associated Objects

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

The timestamp when the current user last viewed this record or list view.

If this value is null, and `LastReferenceDate` is not null, the user accessed this record
or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the data share.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of Data Cloud objects added to this data share.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtDataShareChangeEvent on page 68**
Change events are available for the object.

**ExtDataShareFeed on page 55**
Feed tracking is available for the object.

**ExtDataShareHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ExternalAccountHierarchy

**ExtDataShareOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ExtDataShareShare on page 67**
Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Create a Data Stream](https://help.salesforce.com/s/articleView?id=data.c360_a_create_data_shares.htm&language=en_US)

### ExternalAccountHierarchy

Represents the external account hierarchy, which works like a role-based hierarchy. Use ExternalAccountHierarchy to allow partner and
customer users to share data with other external accounts in their hierarchy.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

You must have a Partner or Customer Community Plus license.

Fields

**Field** **Details**

```
AccountId

```

CurrencyISOCode

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the account in the external account hierarchy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `GBP`  - British Pound

**•** `USD`  - U.S. Dollar

The default value is `USD` .


Standard Objects ExternalAccountHierarchy

**Field** **Details**

```
Description

HierarchyType

IsAccessibleToParent

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the external account hierarchy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `CustomerPortal`  - Customer

**•** `Partner`

The default value is `Partner` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows data to be shared with parent account in the account hierarchy. The default value is
`true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When true, the hierarchy is turned on. The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


### Standard Objects ExternalAccountHierarchyHistory

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
Name

OwnerId

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external account hierarchy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent account.

### ExternalAccountHierarchyHistory

Represents the history of changes to values in the fields of an external account hierarchy. This object is available in API version 50.0 and
later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

You must have a Partner or Customer Community Plus license.


Standard Objects ExternalAccountHierarchyHistory

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** Address

**•** AnyType

**•** AutoNumber

**•** Base64

**•** BitVector

**•** Boolean

**•** Content

**•** Currency

**•** DataCategoryGroupReference

**•** DateOnly

**•** DateTime

**•** Division

**•** Double

**•** DynamicEnum

**•** Email

**•** EncryptedBase64

**•** EncryptedText

**•** EntityId

**•** EnumOrId

**•** ExternalId

**•** Fax

**•** File

**•** HtmlMultiLineText

**•** HtmlStringPlusClob

**•** InetAddress

**•** Json

**•** Location

**•** MultiEnum

**•** MultiLineText

**•** Namespace

**•** Percent


Standard Objects ExternalAccountHierarchyHistory

**Field** **Details**

**•** PersonName

**•** Phone

**•** Raw

**•** RecordType

**•** SfdcEncryptedText

**•** SimpleNamespace

**•** StringPlusClob

**•** Switchable_PersonName

**•** Text

**•** TimeOnly

**•** Url

**•** YearQuarter

```
ExternalAccountHierarchyId

Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the external account hierarchy.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** Account

**•** HierarchyType - Hierarchy Type

**•** IsAccessibleToParent - Is Accessible to Parent

**•** IsActive - Is Hierarchy Active

**•** Name

**•** Owner

**•** Parent

**•** Created - Created.

**•** FeedEvent - Feed Event

**•** IndividualMerged - Individual Merged

**•** Locked - Record Locked

**•** OwnerAccepted - Owner (Accepted)

**•** OwnerAssignment - Owner (Assignment)


### Standard Objects ExternalClientApplication

**Field** **Details**

**•** Unlocked - Record unlocked

```
NewValue

OldValue

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

### ExternalClientApplication

For internal use only.

### ExternalDataSource

Represents an external data source, which defines connection details for integration with data and content that are stored outside the
Salesforce org. This object is available in API version 27.0 and later.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

From API version 48.0 onwards, only authenticated internal and external users can access this object.


Standard Objects ExternalDataSource

Fields

**Field Name** **Details**

```
AuthProviderId

CustomConfiguration

DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce ID of the authentication provider, which defines the service that provides the login
process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders” permissions can
view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
textarea

**Properties**
Nillable

**Description**
A JSON-encoded configuration string that defines parameters specific to the type of external
data source.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With this
field, a developer can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization.


Standard Objects ExternalDataSource

**Field Name** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

```
Endpoint

isWritable

Language

MasterLabel

```

**Type**
textarea

**Properties**
Nillable

**Description**
The URL of the external system, or if that URL is defined in a named credential, the named
credential URL.

A named credential URL contains the scheme `callout:`, the name of the named credential,
and an optional path. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ .
You can append a query string to a named credential URL. Use a question mark (?) as the
separator between the named credential URL and the query string. For example:
`callout:` _`My_Named_Credential`_ `/` _`some_path`_ `?format=json` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Lets the Lightning Platform and users in this org create, update, and delete records for external
objects associated with the external data source. The external object data is stored outside
the org. By default, external objects are read only.

Available only for Salesforce Connect external data sources. Available in API version 35.0 and
later. However, with the cross-org adapter for Salesforce Connect, you can set this field to
`true` only in API version 39.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the `MasterLabel` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the external data source. This internal label doesn’t get translated.


Standard Objects ExternalDataSource

**Field Name** **Details**

```
NamedCredentialId

NamespacePrefix

PrincipalType

Protocol

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the referenced named credential for an external data source. Required
for Salesforce Connect adapters for Amazon DynamoDB, Amazon Athena, GraphQL, and
OData 4.01. For connecting to other external data sources, the field must be null. This field is
available in API version 58.0 and later.

This is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether the org uses one set ( `NamedUser` ), multiple sets ( `PerUser` ), or no
( `Anonymous` ) credentials to access the external system. Each set of credentials corresponds
to a login account on the external system. Corresponds to `Identity Type` in the user
interface.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects ExternalDataSource

**Field Name** **Details**

**Description**
Specifies whether to use OAuth, password authentication, or no authentication to access the
external system.

Some types of external data sources support only one value.

**•** For cloud-based Files Connect external systems, select **Oauth 2.0** .

**•** For on-premises systems, select **Password Authentication** .

**•** For Simple URL data sources, select **No Authentication** .

Additional authentication protocols are supported for the Amazon DynamoDB, Amazon
Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange

```
Repository

Type

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used for SharePoint Online. An optional name of the repository in the data source. Not
applicable to all data source types.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the adapter that connects to the external system.

Define an external data source to connect to data or content that’s stored outside the Salesforce org. Then create external objects, which
map to the external system’s data and behave similarly to custom objects.

Note: Some external data source fields rely on per-user authentication to connect with an external system. If an admin edits one
of these fields, then the previously authenticated credentials can get invalidated, requiring individual users to reauthenticate.

SEE ALSO:

ExternalDataUserAuth

NamedCredential


### Standard Objects ExternalDataUserAuth ExternalDataUserAuth

Stores authentication settings for a Salesforce user to access an external system. The external system must be defined in an external data
source or a named credential that’s configured to use per-user authentication. This object is available in API version 27.0 and later.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AuthProviderId

ExternalDataSourceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the authentication provider, which defines the service that
provides the login process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders”
permissions can view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce ID of the external data source or named credential that defines the
external system.

This is a polymorphic relationship field.


Standard Objects ExternalDataUserAuth

**Field Name** **Details**

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

```
Password

Protocol

UserId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Password portion of the credentials for the Salesforce user to access the external
system.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether to use OAuth, password authentication, or no authentication
when the user accesses the external system.

Additional authentication protocols are supported for the Amazon DynamoDB,
Amazon Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce user who’s accessing the external system.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects ExternalEncryptionRootKey

**Field Name** **Details**

**Refers To**
User

```
Username

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Username portion of the credentials for the Salesforce user to access the external
system.

These authentication settings enable a Salesforce user to access an external system. The external system is defined in Salesforce as one
of the following.

**•** External data source—Provides access to external objects, whose data is stored outside the Salesforce organization.

**•** Named credential—Enables the user’s actions to trigger authenticated callouts to the endpoint that’s specified in the named
credential.

If you grant users access to the external data source or named credential via permission sets or profiles, those users can manage their
[own authentication settings. See Store Authentication Settings for External Systems in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.external_authentication.htm&type=5&language=en_US)

SEE ALSO:

ExternalDataSource

NamedCredential

### ExternalEncryptionRootKey

Represents metadata about root keys stored in third-party key stores that are used to generate and secure keys that encrypt Salesforce
data. This object is available in API version 58.0 and later.

Root keys are used to generate data encryption keys (DEKs) in Salesforce, which are in turn used to encrypt and decrypt data. Root keys
are also used as wrapping keys to secure DEKs in the Salesforce database.

Supported Calls

`describeSObjects()`, `query()`, `update()`

Special Access Rules

This object is available as part of the Shield and Salesforce Platform Encryption add-on subscriptions. Access to this object also requires
the Cache-Only Key Service add-on subscription.


Standard Objects ExternalEncryptionRootKey

Fields

**Field** **Details**

```
ActivatedDate

CreatedBy

Description

LastModifiedBy

Region

RootKeyIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date the key was activated in Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who created the root key. For example,
`user@example.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The user-defined description of the root key.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who most recently modified the key. For example,
`user@example.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The region for the customer managed key. For example, if the `RootKeyService` is `AWS`,
the region is an Amazon Web Services (AWS) region such as `us-east1` .

**Type**
string


Standard Objects ExternalEncryptionRootKey

**Field** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The unique key identifier from the external KMS, such as an AWS Amazon Resource Name
(ARN). For example,

```
                   arn:aws:kms:us-west-2:123456789000:key/123ab456-7cd8-9012-3e4f-5gh678i901j2

```

```
RootKeyService

Status

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The external key management service connected to Salesforce. For example, `AWS` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The status of the key. This is the only value that can be changed using update(). You can
only change the status from Active to Inactive, or from Inactive to Active.

Possible values are:

**•** `Activation Pending` —Salesforce is waiting for confirmation of a valid key policy
in the external key store.

**•** `Active` —Can be used to encrypt new DEKs and decrypt existing DEKs.

**•** `Archived` —Can’t encrypt new DEKs. Can be used to decrypt previously created DEKs.

**•** `Canceled` —Root key activation canceled by a user.

**•** `Inactive` —The root key, and the DEKs that it encrypts, are inaccessible. Inaccessible
DEKs can’t be used to decrypt data, which renders that data also inaccessible.

**•** `Unavailable` —The root key, and the DEKs that it encrypts, cannot be accessed. The
root key has been removed or deactivated by the managing KMS.

Three functions are available: `describeSObjects()`, `query()`, and `update()`

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives you starter information](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_encryption_rest_api_guide.meta/platform_encryption_rest_api_guide/api_rest_encryption.htm)
on using REST to work with Shield Platform Encryption.


Standard Objects ExternalEncryptionRootKey

**Describe an external root key with** **`describeSObjects()`**

To get information about the ExternalEncryptionRootKey sObject, use `describe` .

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

     ExternalEncryptionRootKey/describe'

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN'

```

On success, the response is the full JSON description of the ExternalEncryptionRootKey sObject.

**Get info on an external root key with** **`query()`**

To get information about a specific root key, use `query` on the `ExternalEncryptionRootKey` sObject. Use the Identifier
value as listed on the Key Management Page for the root key Id in the WHERE clause.

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/query?' \

     ?q=SELECT+FIELDS(ALL)+FROM+ExternalEncryptionRootKey+WHERE+Id='48q001t5ddzbucnAAA'+\

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN'

```

On success, the response is be similar to

```
     {

       "totalSize": 1,

       "done": true,

       "records": [

          {

            "attributes": {

               "type": "ExternalEncryptionRootKey",

               "url":

     "/services/data/v62.0/sobjects/ExternalEncryptionRootKey/48q001t5ddzbucnAAA"

            },

            "Id": "48q001t5ddzbucnAAA",

            "RootKeyIdentifier": "97ee8238-c5ac-4320-a2d0-a728aaefd567",

            "CreatedDate": "2024-08-05T17:32:11.841+0000",

            "CreatedBy": "charley.t.pulasky@wise-raccoon-od1ly6.com",

            "LastModifiedDate": "2025-02-12T18:36:11.063+0000",

            "LastModifiedBy": "charley.t.pulasky@wise-raccoon-od1ly6.com",

            "RootKeyService": "SF",

            "Region": "KEY REGION",

            "Status": "Active",

            "Description": null,

            "ActivatedDate": null

          }

       ]

     }

```

**Update Status on an external root key with** **`update()`**

To update the status of an `ExternalEncryptionRootKey` from `Active` to `Inactive`, or from `Inactive` to `Active`,
use PATCH on the specific key object. Use the vaule for `Identifier` as listed on the Key Management Page for the root key
identifier.

```
     curl --location --request PATCH

     'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/ExternalEncryptionRootKey/ROOTKEYIDENTIFIER'

      \

     --header 'Content-Type: application/json' \

```


### Standard Objects ExternalEvent

```
     --header 'Authorization: Bearer TOKEN'\

     --data '{

      "Status": "Active"

     }'

```

On success, the response is be similar to I SEE NO RESPONSE.

### ExternalEvent

Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
ExternalId

Location

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The site where the external event takes place.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects ExternalEventMapping

**Field** **Details**

**Description**
The name of the external event’s organizer.

```
Notes

Time

Title

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Additional details about the external event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The time the external event is held.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the external event.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExternalEventChangeEvent on page 68**
Change events are available for the object.

### ExternalEventMapping

Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects ExternalEventMapping

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
EndDate

EventId

ExternalId

IsLocked

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the external event ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Salesforce event created by the external event.

This field is a relationship field.

**Relationship Name**
Event

**Refers To**
Event

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the external event.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the external event is locked, or `false` if it’s not.

The default value is `false` .


Standard Objects ExternalEventMapping

**Field** **Details**

```
IsRecurring

MayEdit

Name

OwnerId

StartDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the external event is recurring (true) or not (fales).

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

Indicates whether the external event can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the external event’s organizer.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the creator of the external event.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the external event begins.


### Standard Objects ExternalSocialAccount ExternalSocialAccount

Represents a managed social media account on a social network such as Facebook or Twitter. This object is available in API version 29.0
and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
AuthorizedBy

DataSourceId

DefaultResponseAccountId

DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Radian6 user who added the social account to Radian6.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 data source for the social account.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the managed social account to use by default when responding.

This is a relationship field.

**Relationship Name**
DefaultResponseAccount

**Relationship Type**
Lookup

**Refers To**
### ExternalSocialAccount

**Type**
string


Standard Objects ExternalSocialAccount

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
ExternalAccountId

ExternalPictureURL

IsActive

IsAuthenticated

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID of the social account on the social network.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to the picture of the social account on the social network.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is active or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is authenticated or not.


Standard Objects ExternalSocialAccount

**Field Name** **Details**

```
IsCaseCreationEnabled

IsDataSourceActive

Language

MasterLabel

ProfileUrl

Provider

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether case creation for the social account is enabled or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the data source is active or not.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the language of the social account.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the social account. This display value is the internal label and
does not get translated.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects ExternalSocialAccount

**Field Name** **Details**

**Description**
Social network, such as Facebook or Twitter, of the social account.

```
ProviderUserId

RuleId

SocialPropertyId

TopicId

UniqueName

Username

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID for the social network of the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 rule for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 social property for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the topic for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique name for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ExtKnowledgeConnector

**Field Name** **Details**

**Description**
Username for the social account.

Usage

[Although available, many of the Radian6-related fields are no longer accurate or used. We recommend using Social Engagement](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm)
[Resources in](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm) _Connect REST API Developer Guide_ .

### ExtKnowledgeConnector

Represents a connector to a third-party knowledge source for Unified Knowledge. This object is available in API version 60.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Knowledge must be enabled in your org. Salesforce Knowledge users, unlike customer and partner users, must also be granted
the Knowledge User feature license.

Fields

**Field** **Details**

```
IsLocked

LastSyncDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the connector last synced with the third-party knowledge source to import
articles into Salesforce.


Standard Objects ExtKnowledgeConnector

**Field** **Details**

```
LastSyncStatus

MayEdit

Name

NamedCredentialId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the connector’s last sync of articles from the third-party knowledge
source into Salesforce.

Possible values are:

**•** `articleLimitExceeded` —Exceeded article or version limits

**•** `completed` —Completed

**•** `completedWithErrors` —Completed with errors

**•** `ended` —Ended

**•** `failed` —Failed

**•** `initiating` —Started

**•** `invalidCredentials` —Invalid credentials

**•** `polling` —Polling for Zoomin sync to complete

**•** `queued` —Queued

**•** `syncing` —Syncing

**•** `timedOut` —Timed Out

**•** `unavailable` —Zoomin unavailable

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated import article condition record can be edited or not.

The default value is `false` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The connector’s label in Unified Knowledge setup.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ExtKnowledgeConnector

**Field** **Details**

**Description**
Salesforce ID of the named credential that’s used for a request. The named credential identifies
the third-party system and the third-party authentication settings.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

```
OwnerId

PartnerConnectorIdentifier

ShouldOpenInSource

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID of the owner of the connector.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether articles imported into Salesforce open in the third-party source from links
in Salesforce.

The default value is `false` .


### Standard Objects ExtlClntAppOauthPlcyCnfg

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtKnowledgeConnectorOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ExtKnowledgeConnectorShare on page 67**
Sharing is available for the object.

### ExtlClntAppOauthPlcyCnfg

For internal use only.

### ExtlClntAppOauthSettings

For internal use only.

### ExtlClntAppPlcyCnfg

For internal use only.

### ExtlRecShrCnct

Represents authentication data to make outbound calls to and inbound calls from an external system to publish events for Partner
Connect. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
CnctName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects ExtlRecShrCnct

**Field** **Details**

**Description**
Name of the connection.

```
CnctRole

CnctStatus

ExternalClientApplicationId

ExtlSystem

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
System’s role in the connection.

Possible values are:

**•** `Partner`

**•** `Vendor`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the connection.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**•** `Error`

**•** `Pending`

**•** `Unknown`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of external client app representing your org’s connection to the external system.

This field is a relationship field.

**Relationship Name**
ExternalClientApplication

**Refers To**
ExternalClientApplication

**Type**
string


### Standard Objects ExtlRecShrCnctAccnt

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
ID of the external system.

```
NamedCredentialId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the named credential.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Refers To**
NamedCredential

### ExtlRecShrCnctAccnt

Represents an association between an account and an external record share connection for Partner Connect. This object is available in
API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects ExtlRecShrField

**Field** **Details**

**Description**
ID of the account.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

```
ExtlRecShrCnctId

Name

### ExtlRecShrField

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ExtlRecShrCnct record.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

Represents an imported, exported, or updated external record share field for Partner Connect. This object is available in API version 63.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .


Standard Objects ExtlRecShrField

Fields

**Field** **Details**

```
ExtlRecShrObjectId

FieldDefaultValue

FieldSetType

IsFieldNillable

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrObject record.

This field is a relationship field.

**Relationship Name**
ExtlRecShrObject

**Refers To**
ExtlRecShrObject

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default value of the field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Set of fields associated with this record.

Possible values are:

**•** `ExportedFields`

**•** `ImportedFields`

**•** `InternalFields`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this field can be set to null ( `true` ) or not ( `false` ).

The default value is `false` .


Standard Objects ExtlRecShrField

**Field** **Details**

```
SendFieldUpdates

SharedFieldDevName

SharedFieldLabel

SharedFieldLength

SharedFieldType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether updates are tracked for this field, sent to the connected org, and stored
in the ExtlRecShrLead or ExlRecShrOpportunity objects ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Developer name of the field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label of the field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum length of the field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Field type of the imported, exported, or updated field.

Possible values are:

**•** `Address`

**•** `AddressCountry`

**•** `AddressState`

**•** `Boolean`


### Standard Objects ExtlRecShrFieldMap

**Field** **Details**

**•** `Currency`

**•** `DateOnly`

**•** `DateTime`

**•** `Double`

**•** `DynamicEnum`

**•** `Email`

**•** `EntityId`

**•** `EnumOrId`

**•** `Fax`

**•** `Integer`

**•** `MultiLineText`

**•** `Percent`

**•** `Phone`

**•** `StaticEnum`

**•** `Text`

**•** `Url`

### ExtlRecShrFieldMap

Represents the external record share field mapping between the sender and receiver for Partner Connect. This object is available in API
version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ImportedFieldId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ExtlRecShrLead

**Field** **Details**

**Description**
ID of the ExtlRecShrField record containing the field data sent from the external system.

This field is a relationship field.

**Relationship Name**
ImportedField

**Refers To**
ExtlRecShrField

```
InternalFieldId

### ExtlRecShrLead

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrField record containing the field data received on the internal system.

This field is a relationship field.

**Relationship Name**
InternalField

**Refers To**
ExtlRecShrField

Represents the Lead record of a vendor org if you’re a partner. If you’re a vendor for Partner Connect, this object represents a partner
org. This object is available in API version 62.0 and later.

In a related list, the label of this object is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .


### Standard Objects ExtlRecShrObject

Fields

**Field** **Details**

```
ExtlRecShrCnctId

LeadId

Name

### ExtlRecShrObject

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the partner lead.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Master-detail

**Refers To**
Lead (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

Represents a shared object for Partner Connect. This object is available in API version 62.0 and later.


Standard Objects ExtlRecShrObject

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
DefaultRecordOwnerId

ExtlObjectType

ExtlRecShrCnctId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the shared record owner. The owner can be a user or a queue, represented by a Group
ID.

This field is a polymorphic relationship field.

**Relationship Name**
DefaultRecordOwner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object type in the external org or system that is part of the object field mapping.

Possible values are:

**•** `ExtlRecShrLead`

**•** `ExtlRecShrOpportunity`

**•** `Lead`

**•** `Opportunity`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ExtlRecShrOpportunity

**Field** **Details**

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

```
FieldMapStatus

InternalObjectType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Exporter’s status of the field mapping.

Possible values are:

**•** `ActiveMapping`

**•** `Selected`

**•** `SystemOverride`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object type in your org or system used to group field selections and field mappings.

Possible values are:

**•** `ExtlRecShrLead`

### • ExtlRecShrOpportunity

**•** `Lead`

**•** `Opportunity`

### ExtlRecShrOpportunity

Represents the opportunity for Partner Connect in the vendor org if you’re a partner and the partner org if you’re the vendor. This object
is available in API version 62.0 and later.

The label of this object in the related list is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Standard Objects ExtlRecShrOpportunity

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrCnctId

Name

OpportunityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated opportunity.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Master-detail


### Standard Objects ExtlRecShrPcklstOptn

**Field** **Details**

**Refers To**
Opportunity (the master object)

### ExtlRecShrPcklstOptn

Represents a picklist option of an external record share picklist field shared between a partner and vendor for Partner Connect. This
object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrFieldId

IsDefaultOption

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated external record share field of type picklist.

This field is a relationship field.

**Relationship Name**
ExtlRecShrField

**Refers To**
ExtlRecShrField

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this picklist option is set as the default option ( `true` ) or not ( `false` ).

The default value is `false` .


### Standard Objects ExtlRecShrPicklistMap

**Field** **Details**

```
SharedOptionLabel

SharedOptionValue

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the picklist option.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the picklist option.

### ExtlRecShrPicklistMap

Represents the external record share picklist field mapping between the partner and vendor system for Partner Connect. This object is
available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ImportedPcklstOptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the external system.

This field is a relationship field.


### Standard Objects ExtlRecShrRecordMap

**Field** **Details**

**Relationship Name**
ImportedPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

```
InternalPcklstOptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the internal system.

This field is a relationship field.

**Relationship Name**
InternalPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

### ExtlRecShrRecordMap

Represents the lead or opportunity being mapped between a partner and vendor for Partner Connect. This object is available in API
version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ .

Fields

**Field** **Details**

```
ExtlRecShrCnctId

```

**Type**
reference


Standard Objects ExtlRecShrRecordMap

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

```
ExtlRecord

InboundStatus

InternalRecordId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead or opportunity record on the external system.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of imports and updates received.

Possible values are:

**•** `ImportSuccess`

**•** `ImportConctExtlRecError`

**•** `UpdateSuccess`

**•** `UpdateFieldMapError`

**•** `UpdateConctExtlRecError`

**•** `UpdateUnknownError`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the lead or opportunity record on the internal system.

This field is a polymorphic relationship field.

**Relationship Name**
InternalRecord


Standard Objects ExtlRecShrRecordMap

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
Lead, Opportunity (the master object)

```
IsImported

LastModifiedSent

Name

OutboundStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record originated on the internal system ( `true` ) or external system
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp of the last record update between the vendor and partner. This field doesn’t
capture when the result is received.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of exports, updates, and results received.

Possible values are:

**•** `ExportSuccess`

**•** `ExportInProgress`

**•** `ExportSuccessSkipped`

**•** `ExportSuccessPartial`

**•** `ExportPublishFieldMapError`


### Standard Objects FeedAttachment

**Field** **Details**

**•** `ExportSubscribeFieldMapError`

**•** `ExportPublishEventError`

**•** `ExportPublishUnknownError`

**•** `ExportSubscribeUnknownError`

**•** `ExportPublishConnectionError`

**•** `UpdateInProgress`

**•** `UpdateInProgressUpdateSuccess`

**•** `UpdatePublishFieldMapErrorUpdateSubscribeRecordNotFound`

**•** `UpdatePublishFieldMapError`

**•** `UpdateSubscribeFieldMapError`

**•** `UpdatePublishConnectionError`

**•** `UpdatePublishEventError`

**•** `UpdatePublishUnknownError`

**•** `UpdateSubscribeUnknownError`

```
UniqueRecordKey

### FeedAttachment

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Record key used internally for indexing. If `IsImported` is `false`, then this field contains
the `InternalRecordId` value. If `IsImported` is `true`, this field contains the
`ExtlRecord` value.

This field is a calculated field.

Represents an attachment to a feed item, such as a file attachment or a link. Use FeedAttachment to add various attachments to one
feed item. This object is available in API version 36.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `idEnabled()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** You can read, create, update, or delete a FeedAttachment only if you have the corresponding access to the associated FeedItem.

**•** Inline images aren’t creatable, updatable, or deletable through SOAP API.


Standard Objects FeedAttachment

Fields

**Field Name** **Details**

```
FeedEntityId

RecordId

Title

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated feed entity that contains this attachment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that this feed attachment contains. For inline images,
`RecordId` is a ContentDocument ID. For content attachments, `RecordId`
is a ContentVersion ID, For feed items, `RecordId` is a FeedItem ID.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of this feed attachment. When `Type` is `Link`, `Title` value is the
label for the attachment link. Otherwise, `Title` value isn’t used.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this feed attachment. Valid values are:

**•** 0 `Content` —A content attachment.

**•** 1 `InlineImage` —An inline image. The system creates an inline image
attachment when an image is added to the body of the associated FeedItem.
You can’t add an inline image directly using FeedAttachment.

**•** 2 `Link` —A link.

**•** 3 `FeedEntity` —A feed entity, for example, a post that is shared. Available
in API version 39 and later in Lightning Experience.

**•** 4 `ChatterExtension` —a Rich Publisher App that’s integrated with the
Chatter publisher.


Standard Objects FeedAttachment

**Field Name** **Details**

**•** 5 `Record` —A record.

```
Value

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The string value of this FeedAttachment. This field is optional. If the feed
attachment is a Link FeedAttachment, the value is the link URL string.

**•** This Apex example shows how to add an attachment to a Lead using API version 36.0 and later. First, post a feed item.

```
  //create and insert post

  FeedItem post = new FeedItem();

  post.Body = 'HelloThere';

  post.ParentId = ' ID_OF_LEAD_ENTITY ';

  post.Title = ' FileName ';

  insert post;

```

Then insert the attachment.

```
  //create and associate a content attachment to the post

  FeedAttachment feedAttachment = new FeedAttachment();

  feedAttachment.FeedEntityId = post.Id;

  feedAttachment.RecordId = ' ID_OF_CONTENT_VERSION ';

  feedAttachment.Title = ' FileName ';

  feedAttachment.Type = 'CONTENT';

  insert feedAttachment;

```

**•** You can create only one link attachment ( `FeedAttachment` of type `Link` ) per feed item.

**•** If the feed item type is one of the following, you can add content or link feed attachments to a FeedItem.

**–** `AdvancedTextPost`

**–** `TextPost`

**–** `ContentPost`

**–** `LinkPost`

**–** `QuestionPost`

**•** When a `FeedAttachment` is added or removed from a feed item, Salesforce updates the type of the feed item to its most
appropriate value, as follows.

**–** If all content feed attachments are removed from a feed item of type `ContentPost`, the type of this feed item is updated to
`TextPost` .

**–** Conversely, if a content feed attachment is added to a feed item of type `TextPost`, the type of this feed item is updated to
`ContentPost` .


### Standard Objects FeedComment

**–** If all link feed attachments are removed from a feed item of type `LinkPost`, the type of this feed item is updated to `TextPost` .

**–** Conversely, if a link feed attachment is added to a feed item of type `TextPost`, the type of this feed item is updated to
`LinkPost` .

**–** The type of all other feed items, such as `QuestionPost` or `AdvancedTextPost` feed items, doesn’t change when any
feed attachments are added or removed.

**–** If a content feed attachment is added to a feed item of type `LinkPost`, the feed item type is updated to `ContentPost` .

**–** If all content attachments are removed from a feed item of type `ContentPost`, but there's also a link attachment, the feed
item type is updated to `LinkPost` .

**•** Users without administrator privileges can’t retrieve a FeedAttachment by its ID in a SOQL query. They can retrieve attachments by
specifying the associated `FeedEntityId`, as follows:

```
     SELECT Id FROM FeedAttachment WHERE FeedEntityId = ' some_feedItem_id '

```

**•** Alternatively, retrieve attachments by using a SOQL query on FeedItem with a subquery on the FeedAttachments child relationship,
as follows.

```
     SELECT Body, (SELECT RecordId, Title, Type, Value FROM FeedAttachments)

     FROM FeedItem

     WHERE Id = ' some_feedItem_id '

```

**•** FeedAttachment is not a triggerable object. You can access feed attachments in FeedItem _update_ triggers by retrieving them through
[a SOQL query. For a trigger example, and to learn about trigger considerations for FeedAttachment, see Triggers for Chatter Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers_fields_not_updated_chatter.htm)
in the _Apex Developer Guide_ .

### FeedComment

Represents a comment added to a feed by a user.This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Special Access Rules

Note the following when working with feed comments.

**•** You must have read access to the feed’s parent type to see a FeedComment record.

**•** You must be able to access the feed to add a comment.

**•** If the comment is related to a user record, the user can delete the comment. For example, if John Smith makes a comment on Sasha
Jones’ profile feed, Sasha can delete the comment.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**•** Modify All Data


Standard Objects FeedComment

**•** Modify All Records on the object associated with the feed and delete permission on the parent feed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

**•** Manage Unlisted Groups

Only users with this permission can delete items in unlisted groups.

Fields

**Field** **Details**

```
CommentBody

CommentType

FeedItemId

HasEntityLinks

```

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The text in the comment.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of comment:

**•** `ContentComment` —an uploaded file on a comment

**•** `TextComment` —a direct text entry on a comment

Before API version 24.0, a text entry was required on a comment. As of version 24.0, a text
entry is optional if the `CommentType` is `ContentComment` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the feed item containing the comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed `CommentBody` includes at least one link to a record.


Standard Objects FeedComment

**Field** **Details**

Note: This field is available starting in API version 43.0.

```
InsertedById

IsRichText

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed `CommentBody` contains rich text. If you post a rich text feed
comment using SOAP API, set `IsRichText` to `true` and escape HTML entities from
the body. Otherwise, the comment is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`


Standard Objects FeedComment

**Field** **Details**

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: This attribute is available as of API version 38.0. In API version 38.0 and later,
the system replaces special characters in rich text with escaped HTML. In API version
37.0 and prior, all rich text appears as a plain-text representation.

```
IsVerified

LastEditById

LastEditDate

ParentId

RelatedRecordId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a comment on a question is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed comment.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date the feed comment was last edited.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of a record associated with the feed comment. For example, if you are commenting on a
change to a field on Account, `ParentId` is set to the account ID.

**Type**
reference

**Properties**
Create, Group, Nillable, Sort


Standard Objects FeedComment

**Field** **Details**

**Description**
ID of the ContentVersion record associated with a `ContentComment` . This field is null for
all comments except `ContentComment` .

For example, set this field to an existing ContentVersion ID and set the `CommentType` to
`ContentComment` .

```
Revision

Status

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number of times the comment was revised.

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed comment is published and visible to all who can access the parent
feed item. To change a comment’s status, the comment’s parent feed item must be in a
published state. This field is available in API version 38.0 and later.

Possible values are:

**•** `Published` —The comment is visible to all who can access the parent feed item.

**•** `PendingReview` —The comment is visible to its author. Users see the parent feed
item and have View All Data or Can Approve Feed Post and Comment permission also
see the comment. The author can delete the comment as can users who see the comment
and have Can Approve Feed Post and Comment or Modify All Data permission. If the
parent feed item is published, the author can edit the comment. Users who see the
comment and have Can Approve Feed Post and Comment or Modify All Data permission
can also edit the comment. Users with Can Approve Feed Post and Comment or Modify
All Data permission can change comment status from Published to PendingReview and
from PendingReview to Published.

Some actions are blocked when a feed comment is pending review:

**–** Select as Best—When a feed comment that is marked as best answer becomes
unpublished, it’s removed as the best answer. If the comment is published, its best
answer status is not restored.

**–** Like and unlike

**•** `Isolated` —The comment is visible only to admins. After an item is isolated, the author
no longer has view or edit access. The admin user can edit, view, and delete isolated
feed comments.


Standard Objects FeedComment

**Field** **Details**

```
SystemModstamp

ThreadChildrenCount

ThreadLastUpdatedDate

ThreadLevel

ThreadParentId

```

**Type**
datetime

**Properties**
Defaulted on create, Filter

**Description**
Date and time when a user or automated process (such as a trigger) last modified this record.
In this context, "trigger" refers to Salesforce code that runs to implement standard
functionality, and not an Apex trigger. `SystemModstamp` [is a read-only system field,](http://www.salesforce.com/developer/docs/api/Content/system_fields.htm)
available in FeedComment as of API version 37.0.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The count of comments associated with this parent feed object. The feed object can be
either a Feed Item or a Feed Comment. The count shows how many comments are directly
subordinate to the parent. This field is available on the object when **Allow discussion**
**threads** is selected in the Administration Workspace. This field is available in API version
44.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time the thread on this comment was last updated. This field is available on
the object when **Allow discussion threads** is selected in the Administration Workspace.
This field is available in API version 44.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier that shows the level of this Feed Comment in a thread. By default, there are a
maximum of three levels in a thread. The `ThreadLevel` value shows in which of the
three levels this comment falls. This field is available on the object when **Allow discussion**
**threads** is selected in the Administration Workspace. This field is available in API version
44.0 and later.

**Type**
reference


Standard Objects FeedComment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier of the feed item that is the parent of this comment. This field is available on
the object when **Allow discussion threads** is selected in the Administration Workspace.
This field is available in API version 44.0 and later.

This is a relationship field.

**Relationship Name**
ThreadParent

**Relationship Type**
Lookup

**Refers To**
FeedComment

Usage

**•** As of API version 23.0 and later, if you have View All Data permission, you can query FeedComment records directly without an ID
filter. If you don’t have View All Data permission, you can’t query FeedComment records directly, with or without an ID filter.

For example, the following query returns general information about a feed:

```
     SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName,

            CreatedBy.LastName, ParentId, Parent.Name, Body

     FROM FeedItem

     WHERE CreatedDate > LAST_MONTH

     ORDER BY CreatedDate DESC, Id DESC

```

**•** You can search for text in comments using SOSL. For example, the following Java class uses `search()` to find the string “foo” in
any field of a record:

```
     public void searchSample() {

      try {

       SearchResult sr = connection.search("find {foo} in all fields " +

          "returning feedcomment(Id, FeedItemId, CommentBody)");

       // Put the results into an array of SearchRecords

       SearchRecord[] records = sr.getSearchRecords();

       // Check the length of the returned array of records to see

       // if the search found anything

       if (records != null && records.length > 0) {

         System.out.println("Found " + records.length + " comments: ");

         // Display each comment

         for (SearchRecord record : records) {

          FeedComment comment = (FeedComment) record.getRecord();

          System.out.println(comment.getId() + ": " +

            comment.getCommentBody());

         }

       } else {

         System.out.println("No records were found for the search.");

```


### Standard Objects FeedItem

```
       }

      } catch (ConnectionException ce) {

       ce.printStackTrace();

      }

     }

```

**•** If you use an Apex trigger to modify the `Body` of a FeedComment object, all mentions hyperlinks are converted to plain text. The
mentioned users don't get email notifications.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.

SEE ALSO:

Custom Object __Feed __Feed

### FeedItem FeedItem represents an entry in the feed, such as changes in a record feed, including text posts, link posts, and content posts. This object

is available in API version 21.0 and later. This object replaces FeedPost.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

**•** You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**–** Modify All Data

**–** Modify All Records on the feed item’s parent object, for example, Account for a feed item on an account feed

**–** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments that they can see.

Only users with this permission can delete items in unlisted groups.

**•** Guest users can’t insert system field values for Chatter feeds. Even if you try to assign the CanInsertFeedSystemFields permission to
a Guest User, the permission isn’t granted.

Only users with the Modify All Data permission can delete a feed item of `Type TrackedChange` .

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.


Standard Objects FeedItem

Fields

**Field Name** **Details**

```
BestCommentId

Body

CommentCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

This is a relationship field.

**Relationship Name**
BestComment

**Relationship Type**
Lookup

**Refers To**
FeedComment

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
The body of the feed item. Required when `Type` is `TextPost` or
`AdvancedTextPost` . Optional when `Type` is `ContentPost` or
`LinkPost` .

Although a value for `Body` isn’t required for the `ContentPost` type, an
attachment is required. If an attachment isn’t present, the type changes to
`TextPost` or `AdvancedTextPost`, depending on the API version.
`TextPost` and `AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the
body of rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

Tip: In a feed that supports pre-moderation, `CommentCount` isn’t updated
until a comment is published. For example, say that you comment on a post
that already has one published comment and your comment triggers
moderation. Now there are two comments on the post, but the count says


Standard Objects FeedItem

**Field Name** **Details**

there's only one. In a moderated feed, comments aren’t counted until approved
by an admin or someone with Can Approve Feed Post and Comment or Modify
All Data.

Feed moderation has implications on how you retrieve feed comments. In a
moderated feed, rather than retrieving comments by looping through
`CommentCount`, go through pagination until the end of comments is
returned.

```
ConnectionId

ContentData

ContentDescription

ContentFileName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When a PartnerNetworkConnection modifies a record that is tracked, the
`CreatedBy` field contains the ID of the system administrator. The
`ConnectionId` contains the ID of the PartnerNetworkConnection. Available
if Salesforce to Salesforce is enabled for your org.

**Type**
base64

**Properties**
Create, Nillable

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is required if `Type` is `ContentPost` .
Encoded file data in any format, and can’t be 0 bytes. Setting this field
automatically sets `Type` to `ContentPost` .

**Type**
textarea

**Properties**
Create, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The description of the file specified in
`ContentData` .

**Type**
string

**Properties**
Create, Group, Nillable, Sort


Standard Objects FeedItem

**Field Name** **Details**

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The name of the file uploaded to the feed. Setting
`ContentFileName` automatically sets `Type` to `ContentPost` .

```
ContentSize

ContentType

FeedPostId

HasContent

HasFeedEntity

```

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the size of the file (in bytes) uploaded
to the feed. This field is read-only and is automatically determined during insert.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the MIME type of the file uploaded to
the feed. This field is read-only and is automatically determined during insert.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field was removed in API version 22.0, and is available in earlier versions for
backward compatibility only.

ID of the associated FeedPost. A FeedPost represents the following types of
changes in a feed item: changes to tracked fields, text posts, link posts, and
content posts.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has content.

**Type**
boolean


Standard Objects FeedItem

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a feed entity, for example, a post, as an
attachment. Available in API version 39 and later when sharing a feed entity in
Lightning Experience.

```
HasLink

HasVerifiedComment

InsertedById

IsClosed

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a link attached.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a question has an answer that is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application
migrates posts and comments from another application into a feed, the
`InsertedBy` value is set to the ID of the context user.

This is a polymorphic relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean


Standard Objects FeedItem

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
As of API version 43, a read-only field that indicates whether the feed item is
open or closed to new actions. A value of `true` places restrictions on the actions
a user can take on a feed item and its comments. For more information, see the
Usage section.

```
IsDeleted

IsRichText

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Standard system field. Indicates whether the record has been moved to the
Recycle Bin ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text
feed comment using SOAP API, set `IsRichText` to `true` and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use
`<p>&nbsp;</p>` to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`


Standard Objects FeedItem

**Field Name** **Details**

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`

```
                         src="sfdc://069B0000000omjh"></img>

```

Note: In API version 35.0 and later, the system replaces special characters
in rich text with escaped HTML. In API version 34.0 and prior, all rich text
appears as a plain-text representation.

```
LastEditById

LastEditDate

LikeCount

LinkUrl

NetworkScope

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed item.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date the feed item was last edited.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Create, Nillable, Sort

**Description**
The URL of a `LinkPost` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects FeedItem

**Field Name** **Details**

**Description**
Specifies whether this feed item is available in the default Experience Cloud site,
a specific Experience Cloud site, or all sites. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

`NetworkScope` can have the following values:

**•** `NetworkId` —The ID of the Experience Cloud site in which the FeedItem
is available. If left empty, the feed item is only available in the default
Experience Cloud site.

**•** `AllNetworks` —The feed item is available in all Experience Cloud sites.

Note the following exceptions for `NetworkScope` :

**•** Only feed items with a Group or User parent can set a `NetworkId` or a
null value for `NetworkScope` .

**•** For feed items with a record parent, users can set `NetworkScope` only
to `AllNetworks` .

**•** You can’t filter a feed item on the `NetworkScope` field.

```
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the object type to which the feed item is related. For example, set this field
to a `UserId` to post to someone’s profile feed, or an `AccountId` to post to
a specific account.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,


Standard Objects FeedItem

**Field Name** **Details**

CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentDocument, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, Event, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Identifier, Image, IndividualApplication, Invoice,
InvoiceLine, Lead, Location, MarketSegment, MarketSegmentActivation,
MemberPlan, MessagingSession, MktCalculatedInsight, OperatingHours,
Opportunity, Order, OrderItem, OtherComponentTask, PartyConsent,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, ProviderSearchSyncLog, PurchaserPlan, PurchaserPlanAssn,
ReceivedDocument, Report, ReportAnomalyEventStore, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderLineItem, ServiceAppointment,
ServiceResource, ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember,
ServiceTerritoryWorkType, SessionHijackingEventStore, Shift, Shipment,
ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

```
RelatedRecordId

Revision

```

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC
thanks posts, it’s the ID of the WorkThanks object associated with a
`RypplePost` . This field is typically null for all posts except `ContentPost`
and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed
with `Type` set to `ContentPost` .

**Type**
int


Standard Objects FeedItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item.

```
Status

Title

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is published and visible to all who can access
the feed. This field is available in API version 37.0 and later.

Possible values are:

**•** `Published` —The item’s visible to all with access to the feed.

**•** `PendingReview` —The item’s visible to its author and users who see the
item and have View All Data or Can Approve Feed Post and Comment
permission. Some people can delete and edit the item. They include the
author and users who see the item and have Can Approve Feed Post and
Comment or Modify All Data permission.

Note: These permissions don’t apply when you retrieve feed items
using SOQL. To filter out Pending Review feed items you must add an
explicit clause.

Some actions are blocked when a feed item is pending review:

**–** Comment

**–** Like and unlike

**–** Bookmark

**–** Share

**•** `Isolated` —The item is visible only to admins. After an item is isolated,
the author no longer has view or edit access. The admin user can edit, view,
and delete isolated feed items.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is
the URL and this field is the link name. The `Title` field can be updated on posts
of `Type QuestionPost` .


Standard Objects FeedItem

**Field Name** **Details**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`,
`QuestionPost`, and `TextPost`, all the FeedItem types listed here are
system-generated. In most situations, we recommend that you don't create
system-generated fields using Apex or our APIs. One exception is during Chatter
data migrations, which can require admins to migrate system-generated post
types.

**•** `ActivityEvent` —indirectly generated event when a user or the API
adds a Task associated with a feed-enabled parent record (excluding email
tasks on cases). Also occurs when a user or the API adds or updates a Task or
Event associated with a case record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the
series only. For a recurring Task with CaseFeed enabled, events are generated
for the series and each occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement
and, in Lightning Experience as of API version 39.0 and later, when a user
shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a
public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from
the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric
or gauge exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a
dashboard snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter
profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.


Standard Objects FeedItem

**Field Name** **Details**

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post.
Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply
only to CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an
article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through
the user interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment
for a case object.

**•** `ChangeStatusPost` —generated event when a user changes the status
of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved
to a case.

**•** `EmailMessageEvent` —generated event when an email related to a
case object is sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a
case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or
reaches violation status.

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData`
and `ContentFileName` .

```
Visibility

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is available to all users or internal users only. This
field is available in API version 26.0 and later, if digital experiences is enabled for
your org.

`Visibility` can have the following values:

**•** `AllUsers` —The feed item is available to all users who have permission
to see the feed item.

**•** `InternalUsers` —The feed item is available to internal users only.

Note the following exceptions for `Visibility` :


Standard Objects FeedItem

**Field Name** **Details**

**•** For record posts, `Visibility` is set to `InternalUsers` for all internal
users by default.

**•** External users can set `Visibility` only to `AllUsers` .

**•** `Visibility` can be updated on record posts.

**•** The `Update` property is supported only for feed items posted on records.

Usage

**•** When a feed item’s `IsClosed` field is set to true, some actions are blocked and others are blocked to most users. This table sets
out the actions that are blocked when a feed item is closed.


Standard Objects FeedItem

**•** This Apex example shows how to add a feed item with an attachment to a lead using API version 36.0 and later. First, post a feed
item.

```
     //create and insert post

     FeedItem post = new FeedItem();

     post.Body = 'HelloThere';

     post.ParentId = ' ID_OF_LEAD_ENTITY ';

     post.Title = ' FileName ';

     insert post;

```

Then insert the attachment.

```
     //create and associate a content attachment to the post

     FeedAttachment feedAttachment = new FeedAttachment();

     feedAttachment.FeedEntityId = post.Id;

     feedAttachment.RecordId = ' ID_OF_CONTENT_VERSION ';

     feedAttachment.Title = ' FileName ';

     feedAttachment.Type = 'CONTENT';

     insert feedAttachment;

```

**•** If you’re using API version 23.0 or later and have View All Data permission, you can directly query for a FeedItem. The following
example returns the 20 most recent feed items.

```
     SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName, CreatedBy.LastName, ParentId,

      Parent.Name, Body,

      (SELECT ID, FieldName, OldValue, NewValue FROM FeedTrackedChanges ORDER BY ID DESC)

     FROM FeedItem

     WHERE CreatedDate > LAST_MONTH

     ORDER BY CreatedDate DESC

```

**•** If you’re using an earlier API version than version 23.0, query FeedItem objects through a feed (such as AccountFeed or
OpportunityFeed). The following example returns all feed items for a given account, ordered by date descending:

```
     SELECT Id, Type, FeedItem.Body

     FROM AccountFeed

     WHERE ParentId = AccountId ORDER BY CreatedDate DESC

```

Note: Provide the `ParentId` for API version 22.0 and earlier.

**•** A feed item of type `UserStatus` is automatically created when a user adds a post to update the status. You can’t explicitly create
a feed item of type `UserStatus` .

**•** The FeedItem object doesn’t support aggregate functions in queries.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

**•** The size limit for an attachment on a feed is 2 GB.

**•** You can’t use the content fields to update or delete the content.

**•** You can’t filter or update the content fields.

**•** Deleting a feed item via the API also deletes the associated content. Likewise, undeleting a feed item restores associated content.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.


### Standard Objects FeedLike

**•** After uploading to a feed, it’s possible for an attachment or document to be deleted, marked private, or hidden by sharing rules. In
this case, all content fields in a FeedItem object appear as `null` in a SOQL query.

**•** You can’t explicitly create or delete a FeedTrackedChange record.

**•** Imagine that you insert a feed item or feed comment of `Type ContentPost` on a User or Group to create a file. Then the
`NetworkScope` field value of the feed item is passed to the file.

**•** If you use an Apex trigger to modify the `Body` of a FeedItem object, all mentions hyperlinks are converted to plain text. The mentioned
users don’t get email notifications.

**•** If you insert rich text into the feed item body, make sure that the case of the opening and closing HTML tags matches. For example,
`<b>This is bold text</B>` generates an error.

**•** To check file sharing with Apex triggers, write triggers on ContentDocumentLink instead of FeedItem. For an example, see
ContentDocumentLink.

**•** In API version 36.0 and later, use FeedAttachment to attach one or more content items to a feed item. As a result of support for
multiple attachments through FeedAttachment, all fields related to content attachments have been removed. These fields are:
`ContentData`, `ContentDescription`, `ContentFileName`, `ContentSize`, and `ContentType` .

**•** For all API versions of FeedItem, you can’t query a FeedItem object using the `System Modstamp` filter.

**•** When you use the FeedItem object to create a record-triggered flow, and the flow tries to update a field on the parent record, the
field may not update in the UI until the page is refreshed.

### FeedLike

Indicates that a user has liked a feed item. This object is available in API version 21.0 and later.

### FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API. A FeedLike is a

child object of an associated FeedItem, FeedTrackedChange, or object feed, such as AccountFeed.

Supported Calls

`create()`, `delete()`, `describeSObjects()`

Special Access Rules

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

Fields

**Field Name** **Details**

```
FeedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the feed item that the user liked.


### Standard Objects FeedPollChoice

**Field Name** **Details**

```
FeedEntityId

InsertedById

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of a feed item or feed comment the user liked.

If the user liked a comment, `FeedEntityId` is set to the ID of the comment. If the user
liked a feed item, `FeedEntityId` is set to the ID of the feed item.

This field is optional. The default value is the ID of the feed item.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

You can't query FeedLike records directly. They can only be queried via the entity feed, such as AccountFeed.

FeedLike records represent likes on posts and not likes on comments. Likes on comments can’t be queried via the API.

### FeedPollChoice

Shows the choices for a poll posted in the feed. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects FeedPollChoice

Special Access Rules

To delete feed items they didn’t create, users must have one of these permissions:

**•** Modify All Data

**•** Modify All Records on the parent object, for example on Account for a poll on an AccountFeed

**•** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments they can see.

Only users with this permission can delete items in unlisted groups.

Fields

**Field Name** **Details**

```
ChoiceBody

FeedItemId

Position

```

Usage

**Type**
textarea

**Properties**
Group

**Description**
A choice in the poll.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.

**Type**
int

**Properties**
Group, Sort

**Description**
Shows the position of the poll choice.

Use this object to query all of the choices associated with a particular poll. To view how people voted on the poll, see the FeedPollVote
object.


### Standard Objects FeedPollVote FeedPollVote

Shows how users voted on a poll posted in the feed. This object is available in API version 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ChoiceId

FeedItemId

```

Usage

**Type**
reference

**Properties**
Filter, Group

**Description**
Indicates which choice a user selected on a poll posted in a feed.

This is a relationship field.

**Relationship Name**
Choice

**Relationship Type**
Lookup

**Refers To**
FeedPollChoice

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed item for the poll.

Use this object to query how users voted on a particular poll.

### FeedPost FeedPost represents the following types of changes in a record feed, such as AccountFeed: text posts, link posts, and content posts. This

object is available in API version 18.0 through 21.0. FeedPost is no longer available in later versions. Starting with API version 21.0, use
FeedItem to represent text posts, link posts, and content posts in feeds.


Standard Objects FeedPost

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `search()`

Special Access Rules

You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**•** “Modify All Data”

**•** “Modify All Records” on the object associated with the feed and delete permission on the parent feed

**•** “Moderate Chatter”

Note: Users with the “Moderate Chatter” permission can delete only the feed items and comments they can see.

**•** Manage Unlisted Groups

Only users with this permission can delete items in unlisted groups.

Only users with the Modify All Data permission can delete a feed item of `Type TrackedChange` .

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

Fields

**Field** **Details**

```
Body

ContentData

ContentDescription

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the FeedPost. Required when `Type` is `TextPost` or
`AdvancedTextPost` . Optional when `Type` is `ContentPost` or `LinkPost` .

**Type**
base64

**Properties**
Create, Nillable

**Description**
This field is required if `Type` is `ContentPost` . Encoded file data in any format,
and can’t be 0 bytes. Setting this field automatically sets `Type` to `ContentPost` .

**Type**
string

**Properties**
Create, Nillable, Sort


Standard Objects FeedPost

**Field** **Details**

**Description**
The description of the file specified in `ContentData` .

```
ContentFileName

ContentSize

ContentType

FeedItemId

InsertedById

```

**Type**
string

**Properties**
Create, Group, Nillable, Sort

**Description**
This field is required if `Type` is `ContentPost` . The name of the file uploaded to
the feed. Setting `ContentFileName` automatically sets `Type` to
`ContentPost` .

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
This field is the size of the file (in bytes) uploaded to the feed. This field is read-only
and is automatically determined during insert.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
This field is the MIME type of the file uploaded to the feed. This field is read-only and
is automatically determined during insert.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the feed containing the FeedPost.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects FeedPost

**Field** **Details**

**Description**
ID of the user who added this item to the feed. For example, if an application migrates
posts and comments from another application into a feed, the `InsertedBy` value
is set to the ID of the context user.

```
IsDeleted

LinkUrl

ParentId

Title

Type

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not
( `false` ). This field is a standard system field.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort

**Description**
The URL of a `LinkPost` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the object type to which the FeedPost is related. For example, set this field to a
`UserId` to post to someone’s profile feed, or an `AccountId` to post to a specific
account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The title of the FeedPost. When the `Type` is `LinkPost`, the `Body` is the URL and
the `Title` is the label for the link.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects FeedRevision

**Field** **Details**

**Description**
The type of FeedPost:

**•** `UserStatus` —automatically generated when a user updates their status

**•** `TrackedChange` —ignore

**•** `TextPost` —a direct text entry on a feed

**•** `LinkPost` —a URL posting on a feed

**•** `ContentPost` —an uploaded file on a feed

Note: If you set `Type` to `ContentPost`, you must specify
`ContentData` and `ContentFileName` .

Usage

**•** You can’t directly query for a FeedPost. FeedPosts are always associated with a feed item, so you can query for them through the
feeds. The following example returns all feed items for a given account, ordered by date descending:

```
     SELECT Id, Type, FeedPost.Body

     FROM AccountFeed

     WHERE ParentId = AccountId ORDER BY CreatedDate DESC

```

**•** A FeedPost of type `UserStatus` is automatically created when a user adds a post to update the current status. You can’t explicitly
create a FeedPost of type `UserStatus` .

**•** The size limit for an attachment on a profile, news, or record feed is 2 GB.

**•** You can’t use the content fields to update or delete the content.

**•** You can’t filter or update the content fields.

**•** Deleting a FeedPost via the API also deletes the associated content and FeedPost objects. Likewise, undeleting a FeedPost restores
associated content and FeedPost objects.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.

**•** After uploading to a feed, it is possible for an attachment or document to be deleted, marked private, or hidden by sharing rules. In
this case, all content fields in FeedPost appear as `null` in a SOQL query.

**•** You can’t explicitly create or delete a FeedTrackedChange record.

### FeedRevision

Holds the revision history of a specific feed item or comment, including a list of attributes that changed for each revision. This object is
available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects FeedRevision

Fields

**Field Name** **Details**

```
Action

EditedAttribute

FeedEntityId

IsDeleted

IsValueRichText

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Holds the type of modification to the underlying feed item or comment attribute.
`Action` can have the value `Changed` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Identifies the part of the feed item or comment which was modified. A single
revision can have many edited attributes.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifies the modified feed item or comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not
( `false` ). This field is a standard system field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text
feed comment using SOAP API, set `IsRichText` to `true` and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:


Standard Objects FeedRevision

**Field Name** **Details**

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use
`<p>&nbsp;</p>` to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`

```
                         src="sfdc://069B0000000omjh"></img>

```

Note: In API version 35.0 and later, the system replaces special characters
in rich text with escaped HTML. In API version 34.0 and prior, all rich text
appears as a plain-text representation.

```
OriginNetworkId

Revision

Value

```

**Type**

reference

**Properties**

Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site in which a user modified the feed item or
comment. This field is only available, if digital experiences is enabled for your
org.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item or comment.

**Type**
textarea

**Properties**
Nillable


### Standard Objects feedSignal

**Field Name** **Details**

**Description**
Identifies the value of the `EditedAttribute` field before the update.

Usage

This object tracks the changes made to a feed item or feed comment and stores a list of attributes that changed for each revision.

**•** To query the FeedRevision object, users need the View All Data permission or supply a WHERE clause on the `FeedEntityId` .

### feedSignal

Attach feed signals, like `UpDownVote`, `UserVerified`, and `Verified`, to a feed post or comment. This object is available in
API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`

Fields

**Field** **Details**

```
FeedEntityId

FeedItemId

InsertedById

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Feed entity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the feed post or comment.

Possible values are:

**•** `FeedItem`

**•** `FeedComment`

**Type**
reference


### Standard Objects FeedTrackedChange

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of user who inserted the signal.

This is a relationship field.

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

```
SignalType

SignalValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of signal.

Possible values are:

**•** `UpDownVote`

**•** `UserVerified`

**•** `Verified`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The value of the signal. For example, for `UpDownVote`, the value specifies whether the
signal is an upvote or a downvote.

### FeedTrackedChange

Represents an individual field change or set of field changes. A FeedTrackedChange is a child object of a record feed, such as AccountFeed.
This object is available in API version 18.0 and later.

Supported Calls

```
describeSObjects()

```


Standard Objects FeedTrackedChange

Fields

**Field** **Details**

```
CurrencyIsoCode

FeedItemId

FieldName

NewValue

OldCurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
currency code for the field, if `FieldName` is a currency field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent feed that tracks the field change.

**Type**
string

**Properties**
Group, Sort

**Description**
The name of the field that was changed.

Note: This field also tracks other events that are not related to an individual field for
a parent feed. These events occur as the parent record advances through its pipeline.
For example, a value of `leadConverted` indicates that a lead has been converted
to an opportunity. For a full list of values, see Tracking of Special Events.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
currency code for the `OldValue` field, if `FieldName` is a currency field.


Standard Objects FeedTrackedChange

**Field** **Details**

```
OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The last value of the field before it was changed.

A user can subscribe to a record or to another user. Changes to the record and updates from the users are displayed in the Chatter feed
on the user's home page, which is a useful way to stay up-to-date with other users and with changes made to records in Salesforce.
Feeds are available in API version 18.0 and later.

If you move a custom field to the Recycle Bin, all FeedTrackedChange records that track historical changes to the custom field are
automatically deleted and are not restored if the custom-field is undeleted.

The following sections outline the difference between standard feeds and custom feeds.

Standard Feeds

A standard feed is a record feed, such as AccountFeed. FeedTrackedChange records for standard feeds can only be queried via the parent
feed object.

Note the following when working with standard feed items:

**•** Feed items for standard feeds are read only in the API.

**•** A FeedTrackedChange record is visible when you have read access on the record feed, and when the field is visible in the field-level
security settings.

Custom Feeds

If you want more control over the information provided in a record feed, such as AccountFeed, you can create a custom feed. A custom
feed can replace or augment an existing record feed. For example, you might want to:

**•** Disable the standard account record feed and use an Apex trigger to generate FeedTrackedChange records for the events that you
want to track in the feed instead.

**•** Augment the standard contact record feed by writing an API client that inserts feed items for events that are not tracked in the
standard feed.

Tracking of Special Events

The `FieldName` field also tracks other events that are not related to an individual field for a parent feed. These events occur as the
parent record advances through its pipeline. For example, a value of `leadConverted` indicates that a lead has been converted to
an opportunity.

Valid values for the `FieldName` field for multiple objects:

**•** `created`


### Standard Objects FieldHistoryArchive

**•** `ownerAccepted`

**•** `ownerAssignment`

Additional valid values for the `FieldName` field for individual objects:

**Account**

**•** `accountCreatedFromLead`

**•** `accountMerged`

**•** `accountUpdatedByLead`

**•** `personAccountUpdatedByLead`

**Case**

**•** `closed`

**•** `ownerEscalated`

**Contact**

**•** `contactCreatedFromLead`

**•** `contactMerged`

**•** `contactUpdatedByLead`

**Contract**

**•** `contractActivation`

**•** `contractApproval`

**•** `contractConversion`

**•** `contractExpiration`

**•** `contractTermination`

**Lead**

**•** `leadConverted`

**•** `leadMerged`

**Opportunity**

**•** `opportunityCreatedFromLead`

SEE ALSO:

Custom Object __Feed __Feed

### FieldHistoryArchive Represents field history values for all objects that retain field history. FieldHistoryArchive is a big object, available only to users

with the “Retain Field History” permission. This object is available in API version 29.0 and later.

### Each instance of the FieldHistoryArchive object represents a single change in the value of a field. FieldHistoryArchive

stores history for both standard and custom fields.

### The Field field returns the name of the field unless the parent field or object is deleted, in which case it returns the field ID. You can

use the ID to retrieve the old field and object name from the `FieldNameAfterArchival` and `ParentNameAfterArchival`
fields, respectively.


Standard Objects FieldHistoryArchive

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
ArchiveFieldName

ArchiveParentName

ArchiveParentType

ArchiveTimestamp

CreatedById

```

**Type**
string

**Properties**
Nillable

**Description**
The name of the field at the time the data was archived. If the field name changed,
the name is sometimes not the same for all records related to a single field.

**Type**
string

**Properties**
Nillable

**Description**
The name of the parent object at the time the data was archived. If the object
name changed, the name is sometimes not the same for all records related to a
single field.

**Type**
string

**Properties**
Nillable

**Description**
The type of the field at the time the data was archived. If the field type changed,
the type is sometimes not the same for all records related to a single field.

**Type**
dateTime

**Properties**
Nillable

**Description**
The date and time at which the data was archived.

**Type**
reference

**Properties**
Nillable


Standard Objects FieldHistoryArchive

**Field Name** **Details**

**Description**
The user ID of the user who created the original record.

```
CreatedDate

Field

FieldHistoryType

```

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**
The date and time at which the original record was created.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The name of the field that was changed. If the field is deleted from the parent
object, the `Field` field contains the field ID instead.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The name of the object that contains the field history. Possible values are:

**•** `Account`

**•** `Article`

**•** `Asset`

**•** `AuthorizationFormConsent`  - Available in version 58.0 and later.

**•** `Case`

**•** `CommSubscriptionConsent`  - Available in version 58.0 and later.

**•** `Contact`

**•** `ContactPointConsent`  - Available in version 58.0 and later.

**•** `ContactPointTypeConsent`  - Available in version 58.0 and later.

**•** `Contract`

**•** `ContractLineItem`

**•** `Crisis`

**•** `Employee`

**•** `EmployeeCrisisAssessment`

**•** `Entitlement`

**•** `Individual`


Standard Objects FieldHistoryArchive

**Field Name** **Details**

**•** `InternalOrganizationUnit`

**•** `Knowledge`

**•** `Lead`

**•** `Opportunity`

**•** `Order`

**•** `OrderItem`

**•** `PartyConsent`                       - Available in version 58.0 and later.

**•** `Pricebook2`

**•** `PricebookEntry`

**•** `Product2`

**•** `ServiceAppointment`

**•** `ServiceContract`

**•** `Solution`

**•** `WorkOrder`

**•** `WorkOrderLineItem`

```
HistoryId

Id

NewValue

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the relevant history object (for example, AccountHistory). This field is
available in versions 42.0 and later.

**Type**
ID

**Properties**
Defaulted on create, Filter, idLookup

**Description**
The ID of the archived record. It’s useful to have a field’s ID for fields that you’ve
deleted. (Field names aren’t retained in history when you delete fields from
Salesforce.)

**Type**
anyType

**Properties**
Nillable

**Description**
The new value of the modified field.


### Standard Objects FieldChangeSnapshot

**Field Name** **Details**

```
OldValue

ParentId

```

Usage

When sorting fields, order them as follows:

**1.** `FieldHistoryType ASC`

**2.** `ParentID ASC`

**3.** `CreatedDate DESC`

SEE ALSO:

**Type**
anyType

**Properties**
Nillable

**Description**
The previous value of the modified field.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the object that contains the field (the parent object).

_Developer Guide:_ [Big Objects Implementation Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.bigobjects.meta/bigobjects/big_object.htm)

### FieldChangeSnapshot

Use this virtual object to learn which opportunities' close dates changed during the specified time period. This object is available in API
version 52.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To use FieldChangeSnapshot, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.


Standard Objects FieldChangeSnapshot

Fields

**Field** **Details**

```
CurrentValueDateOnly

FieldName

ParentId

ValidFrom

ValidTo

```

**Type**
date

**Properties**
Filter, Group, Nillable

**Description**
The current value of a date field on the opportunity.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the field to get the change history for. Possible values are:

**•** `CloseDate`

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity to get the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time that specifies the beginning of the time period.

**Type**
dateTime


### Standard Objects FieldPermissions **Field Details**

**Properties**
Filter

**Description**
The date and time that specifies the end of the time period.

Usage

Use FieldChangeSnapshot to learn about the first change made to the specified opportunity during the specified time period. Subsequent
changes are not returned.

Example: Suppose that last week you changed an opportunity's close date to June 1, 2021. Assuming the opportunity had the
ID '006R0000XXXXXXXXXX', the following query would return the `CurrentValueDateOnly` of June 1, 2021:

```
      Select CurrentValueDateOnly from FieldChangeSnapshot where ParentID =

      '006R0000XXXXXXXXXX' and FieldName = 'CloseDate' and ValidTo = LAST_WEEK AND ValidFrom

      = LAST_WEEK and CurrentValueDateOnly < 2021-07-01

### FieldPermissions

```

Represents the enabled field permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

To grant a user access to a field, associate a FieldPermissions record with a PermissionSet that’s assigned to a user. FieldPermissions
records are only supported in PermissionSet, not in Profile.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

In API version 49.0 and later, only users with the View Setup and Configuration permission can access this object.

Fields

In API version 50.0 and later, for lookup field inserts and queries, you can leave off the Id in the field name or include it. The rows returned
always use the API name. For example:

```
   SELECT SobjectType, Field

   FROM FieldPermissions

   WHERE Field='Contact.Account'

```

and

```
   SELECT SobjectType, Field

   FROM FieldPermissions

   WHERE Field='Contact.Account Id '

```


Standard Objects FieldPermissions

both return

```
   Contact, Contact.AccountId

```

**Field Name** **Details**

```
Field

ParentId

PermissionsEdit

PermissionsRead

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field’s API name. This name must be prefixed with the `SobjectType` . For example,

```
  Merchandise__c.Description__c

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The `Id` of the field’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit this field. Requires
`PermissionsRead` for the same field to be `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view this field. A FieldPermissions
record must have at minimum `PermissionsRead` set to `true`, or it will be deleted.


Standard Objects FieldPermissions

**Field Name** **Details**

```
SobjectType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object’s API name. For example, `Merchandise__c` .

FieldPermissions work similarly to ObjectPermissions. However, FieldPermissions includes a `Field` attribute to return the name of the
field.

For example, the following query returns all FieldPermissions records that have at least the “Read” permission. The results include the
field, object, and permission set names.

```
SELECT SobjectType, Field, PermissionsRead, Parent.Name

FROM FieldPermissions

WHERE PermissionsRead = True

```

Include the field’s parent object when querying FieldPermissions. For example, to find all rows that match the Account object’s `Type`
field, create the following query:

```
SELECT Id, SobjectType, Field

FROM FieldPermissions

WHERE Field = 'Account.Type' AND SobjectType = 'Account'

```

To find which permission sets are backed by profiles with the Account object, you can use a query like the following example:

```
SELECT Id, ParentId, SobjectType, Field, PermissionsEdit, PermissionsRead, Parent.Name

FROM FieldPermissions

WHERE SobjectType = 'Account' and Parent.IsOwnedByProfile = true

ORDER BY SObjectType, Field

```

Both `SobjectType` and `Field` must be included in the `SELECT` line of the query. Provide the full API name of the field in the
form of `SobjectType.Field` when querying for a field.

Note: When using the FieldPermission object to download records, depending on the SOQL query you use, you might not receive
all expected records. Results can also appear incomplete. However, all records do download; fields that don't support field security
and rows for entities not visible to the org are hidden.

Special Properties for Field Permissions

The auto-number and formula fields have special rules for how field permissions work. Both have FieldPermissions records, but inserting
and updating is limited to `PermissionsRead` . `PermissionsEdit` isn’t allowed for either field type, since these fields must be
read-only for users.

The following field types don’t return a FieldPermissions record because they are assumed to always be readable.

**•** `Id`

**•** `CreatedById`


Standard Objects FieldPermissions

**•** `CreatedDate`

**•** `IsDeleted`

**•** `LastModifiedById`

**•** `LastModifiedDate`

**•** `SystemModStamp`

The following field types don’t return a FieldPermissions record because they are assumed to always be readable and writable.

**•** `OwnerId`

**•** Master-detail custom (relationship) fields

**•** Universally required custom fields

As a result, the following query returns no records, even though users do have some access to some of the fields.

```
   SELECT Field, SobjectType, PermissionsRead

   FROM FieldPermissions

   WHERE Field='Id'

```

To determine if a field can return a FieldPermissions record, you can call a `describeSObject()` on the field. For example,
`describeSObject('Merchandise__c')`, returns all the properties of the Merchandise custom object, including field properties.
If you use a field whose `permissionable` property is `false` (like the field types listed in this section), you can’t query, insert,
update, or delete field permissions records, because they don’t exist.

If the View All Fields object permission is enabled for an object in the permission set, the `PermissionsRead` field equals `true`
for all queried fields for that object.

Working with Custom Activity Fields

While tasks and events are considered separate objects, they share a common set of activity custom fields. As a result, when a custom
task field is created, a custom event field is also created, and vice versa. You can display the custom field on the event layout, task layout,
or both event and task layouts.

Although custom activity fields are shared between tasks and events, you see separate FieldPermissions records for the task and event.
However, changes made to one field permission record are automatically made to the other. For example, if you create a custom activity
field, assign field permissions to it in a permission set, and run the following query, the query returns two records with the same permission
value.

```
   SELECT Field, Id, ParentId, PermissionsEdit, PermissionsRead, SobjectType

   FROM FieldPermissions

   WHERE SobjectType = 'event' OR SobjectType ='task'

```

If you then update one of the records with another set of field permission values and run the query, the same permission values for both
records are returned.

Nesting Field Permissions

You can nest FieldPermissions in a PermissionSet query. For example, the following returns any permission sets where “Edit Read Only
Fields” is `true` . Also, the result set includes both the “Read” and “Edit” field permission on the Merchandise object. Get similar results
by nesting the SOQL with a field permission query using the relationship name for field permissions: `FieldPerms` .

```
   SELECT PermissionsEditReadonlyFields,

   (SELECT SobjectType, Field, PermissionsRead, PermissionsEdit

   FROM FieldPerms

```


Standard Objects FieldPermissions

```
   WHERE SobjectType = 'Merchandise__c')

   FROM PermissionSet

   WHERE PermissionsEditReadonlyFields = true

```

As a result, it’s possible to traverse the relationship between the PermissionSet and any child-related objects (in this case, FieldPermissions).
You can do this from the PermissionSet object by using the child relationship ( `ObjectPerms`, `FieldPerms`, and so on) or from
the child object by referencing the PermissionSet with `Parent.` _**`permission_set_attribute`**_ .

It’s important to consider when to use a conditional `WHERE` statement to restrict the result set. To query based on an attribute on the
permission set object, nest the SOQL with the child relationship. However, to query based on an attribute on the child object, you must
reference the permission set parent attribute in your query.

The following two queries return the same columns with different results, based on whether you use the child relationship or parent
notation.

```
   SELECT PermissionsEditReadonlyFields,

   (SELECT SobjectType, Field, PermissionsRead, PermissionsEdit

   FROM FieldPerms

   WHERE SobjectType = 'Merchandise__c')

   FROM PermissionSet

   WHERE PermissionsEditReadonlyFields = true

```

Versus:

```
   SELECT SobjectType, Field, PermissionsRead, PermissionsEdit, Parent.Name,

     Parent.PermissionsEditReadonlyFields

   FROM FieldPermissions

   WHERE SObjectType='Merchandise__c'

```

Muting Permissions

Field permissions with a parent muting permission set act differently than those enabled in a regular permission set. For a regular
permission set, if a FieldPermissions record grants full access to a field (for example, granting read and edit access), users have full access
to that field.

With muting permission sets, a FieldPermissions record defines the muting of access. So if a muting permission set is set for read and
edit, the read and edit access is muted.

For example, we have a permission set and a muting permission set that controls access to the Account object’s fields. Each permission
set has settings for the Website field.

Regular Permission Set

**Field** **PermissionsRead** **PermissionsEdit** **Result**

Account.Website `true` `false` The Account.Website field is
read only.

Account.Website `true` `true` The Account.Website field has
both read and edit permissions.

Muting Permission Set


### Standard Objects FieldSecurityClassification **Field PermissionsRead PermissionsEdit Result**

Account.Website `false` `true`

Account.Website `true` `true`

Edit permissions on the
Account.Website fields are
muted.

Read and edit permissions on
the Account.Website field are
muted.

Field permissions are aggregated by combining the permissions granted by the permission set and the permissions muted by the muting
permission set. For example, if you have a permission set that grants read and edit permissions for a field, and a muting permission that
mutes the same field’s edit permission, the result is that only the read permission is enabled.

SEE ALSO:

PermissionSet

ObjectPermissions

### FieldSecurityClassification

Represents a field’s data sensitivity value selected from the SecurityClassification picklist. This object is available in API version 46.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To view this object, you need the Customize Application or Modify Data Classification permission.

Fields

**Field Name** **Details**

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential


Standard Objects FieldSecurityClassification

**Field Name** **Details**

**•** Restricted

**•** MissionCritical

```
Description

IsHighRiskLevel

MasterLabel

SortOrder

```

Usage

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the data sensitivity picklist value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your
company.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential

**•** Restricted

**•** MissionCritical

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the picklist.

Use this object to return information about data sensitivity values in the SecurityClassification picklist. This object is read-only, but you
[can update the SecurityClassification picklist using the StandardValueSet Metadata API type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_standardvalueset.htm)


### Standard Objects FieldServiceMobileSettings FieldServiceMobileSettings

Represents a configuration of settings that control the Field Service iOS and Android mobile app experience. This object is available in
API version 38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AscAutomaticMode

```

AscCancellationTimerInSec

AscCompletedStatus

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes how status changes are handled. Possible values are:

**•** `Off` —No automatic status changes.

**•** `Manual` —The mobile worker can cancel or update the status change.

**•** `Timed` —The mobile worker has a time period to prevent the status change.
When the timer ends, the status changes.

**•** `Automated` —The mobile worker is notified that the status has changed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
For the Timed mode only. Time that the user has to cancel the appointment
status change.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
Status that indicates that a mobile worker completed a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

```
AscOnSiteStatus

AscRadiusInMeters

AscTimeLimitationInMin

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is at a service appointment. Possible
values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Service appointment radius that can trigger a status change.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
A time period when status changes can occur, before an appointment’s scheduled
start time and after the scheduled end time. The time is applied only if
IsAscTimeLimitEnabled is `true` .

```
AscTravelStatus

BgGeoLocationAccuracy

BgGeoLocationMinUpdateFreqMins

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is traveling to a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of geolocation tracking of services resources while the app is running
in the background. Lowering accuracy reduces battery consumption for mobile
devices. Available in API version 41.0 and later. Picklist options:

**•** `Medium` —Accurate to within about 100 meters.

**•** `Coarse` —Accurate to within about 1 kilometer.

**•** `Very Coarse` —Accurate to within about 3 kilometers.

The default value is `Coarse` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The frequency of geolocation poling of services resources while the app is running
in the background. Less frequent poling decreases battery consumption for


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

mobile devices. The label in the UI is **Minimum Update Frequency of Geo**
**Location in Minutes (Background)** . Available in API version 41.0 and later.

```
BrandInvertedColor

ContrastInvertedColor

ContrastPrimaryColor

ContrastQuaternaryColor

ContrastQuinaryColor

ContrastSecondaryColor

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of toasts and the contrast color of the floating action button.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary text.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary lines that delineate different areas of the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
The color of secondary text.

```
ContrastTertiaryColor

DaysBeforeCurrentServiceDate

DayAfterCurrentServiceDate

DefaultListViewDeveloperName

```

DestinationType

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the icons on the settings screen and of primary lines that delineate
different areas of the UI.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days before the current service date during which to prime service documents
for offline use.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days after the current service date during which to prime service documents for
offline use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the default service appointment list view on the schedule screen.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines if the mobile worker navigates to the destination based on the address
or based on the latitude and longitude. Possible values are:

**•** `Address`


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**•** `Latitude and Longitude`

The default value is `Address` .

```
DeveloperName

FeedbackPrimaryColor

FeedbackSecondaryColor

FeedbackSelectedColor

FutureDaysInDatePicker

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the set of field service mobile settings.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of error messages.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of success messages.

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The color indicating the user’s current selection.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the future that a user can select from the date picker
on the schedule screen.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
GeoLocationAccuracy

GeoLocationMinUpdateFreqMins

IsAscTimeLimitEnabled

IsAssignmentNotification

IsDefault

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of service resource geolocation tracking. Lowering accuracy reduces
battery consumption for mobile devices. Picklist values:

**•** `Fine` —Accurate to within 10 meters.

**•** `Medium` —Accurate to within 100 meters.

**•** `Coarse` —Accurate to within 1 kilometer.

The default value is `Medium` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to poll geolocation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether AscTimeLimitationInMin is applied. Default is `true`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is assigned the appointment. Default is `false` . This field is available
in API version 46.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

**Description**
Indicates that the set of field service mobile settings is the default set that is
automatically assigned to users. You can’t make a different settings record the
default, but you can modify the default settings record. Default is `false` .
Available in API version 41.0 and later.

```
IsDispatchNotification

```

IsLimitedLocTrackingEnabled

IsOptimizedImageUploadEnabled

```
IsScheduleViewResourceAbsences

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is dispatched for the appointment. Default is `false` . This field is
available in API version 46.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When limited tracking for Appointment Assistant is enabled, the mobile worker’s
location is shown only on the way to a service appointment. The default value
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to configure the size of images uploaded by your mobile
workers. To optimize upload speeds, you can limit your file size to a defined
maximum size using the OptimizeImageSizeInMb field. Resizing your images
affects the resolution of your images. The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether resource absences appear in the Schedule tab of the mobile
app. This field is available in API version 55.0 and later.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
IsSendLocationHistory

IsShowEditFullRecord

IsTimeSheetEnabled

IsTimeZoneEnabled

IsUseSalesforceMobileActions

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether geolocation tracking of services resources is enabled. Default
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can edit records with the field service mobile app. Default
is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can access time sheets on their mobile devices (Beta).
Default is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether the time zone of timesheet entries on the mobile app is
recorded. The current time zone is recorded in the `LocationTimeZone` field
of the TimeSheetEntry object. Default is `false` . Available in API version 50.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
Language

MasterLabel

MaxNumberOfServiceAppointments

MetadataCacheTimeDays

NavbarBackgroundColor

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The localization preference for a user. The format is a two letter language code
and, if there’s a dialect, followed by the two letter dialect, for example, `fr` for
French, and `fr_BE` for Belgian French

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label in the UI for the set of field service mobile settings. Available in API
version 41.0 and later.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Sets the maximum number of service appointments to use for offline priming
of service documents. If you don’t have dates on your service appointments, this
setting helps to optimize offline priming in place of
`DaysBeforeCurrentServiceDate` and
`DaysBeforeCurrentServiceDate` fields.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days that org metadata, such as layouts, is kept in the app’s local
cache of memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the top bar in the app.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
NavbarInvertedColor

```

OptimizeImageSizeInMb

```
PastDaysInDatePicker

PrimaryBrandColor

QuickStatusChangeFlowName

```

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The secondary color of the tap bar in the app.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Configure the size of images uploaded by your mobile workers. To optimize
upload speeds, you can limit your file size to a defined maximum size. Resizing
your images affects the resolution of your images. Enter 0.2 or higher. Used only
if IsOptimizedImageUploadEnabled is `true` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the past that a user can select from the date picker on
the schedule screen.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The main branding color used throughout the UI.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of an existing Field Service flow with a Quick Status Change action to
change the work order or service appointment status or both. This applies to
flows invoked on the mobile app only. This field is available in API version 51.0
and later.


Standard Objects FieldServiceMobileSettings

**Field Name** **Details**

```
RecordDataCacheTimeMins

SecondaryBrandColor

TimeIntervalSetupMins

UpdateScheduleTimeMins

```

Usage

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of minutes that record data is kept in the app’s local cache of
memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of action buttons.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls the spacing of picklist options for time values such as when creating
resource absences.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to update a user’s
schedule.The user’s schedule might not refresh on this cadence if the user’s
device isn’t connected to a network or doesn’t have adequate battery life.

Field Service Mobile settings allow you to create sets of settings to apply to different field service mobile users. The settings apply to
both the Android and iOS versions of the app.

For example, suppose you want to accommodate workers that are color blind, or who work in dark or bright conditions. You can choose
different branding options for different workers to suit their needs, and assign them to their profiles.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects FieldServiceOrgSettings

**FieldServiceMobileSettingsChangeEvent (API version 55.0)**
Change events are available for the object.

### FieldServiceOrgSettings

Represents the org settings for Field Service, such as Appointment Assistant settings. If Field Service is enabled, the org contains one
read-only record of this object. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, Field Service must be enabled. For specified fields in the table, Appointment Assistant must also be enabled.

Fields

### **Field Details**

```
ApptAssistantExpiration

ApptAssistantInfoUrl

ApptAssistantRadiusUnit

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expiry time in minutes of when the customer stops seeing the mobile worker’s location.
Appointment Assistant must also be enabled to see this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The page URL that enables Appointment Assistant. Appointment Assistant must also be
enabled to see this field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of the radius of the service appointment that prompts the Last Mile event for
Appointment Assistant. Appointment Assistant must also be enabled to see this field.


Standard Objects FieldServiceOrgSettings

**Field** **Details**

Possible values are:

**•** `Kilometer`

**•** `Meter`

**•** `Mile`

**•** `Yard`

```
ApptAssistantRadiusValue

ApptAssistantStatus

CanPopulateGoogleAddress

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The radius of the service appointment that prompts the Last Mile event for Appointment
Assistant. Appointment Assistant must also be enabled to see this field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The value that prompts the En Route event for Appointment Assistant. Appointment Assistant
must also be enabled to see this field.

Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**•** `TestSharing`

The default value is 'None'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows desktop and mobile to send geolocation and map data to Google and Apple. Available
in API version 57.0 and later.

The default value is `true` .


Standard Objects FieldServiceOrgSettings

**Field** **Details**

```
CanSendAppCenterCrashReports

CanStoreMobileAnalytics

DeveloperName

DoesAvlCalcInclOvertime

DoesAvlCalcInclPrimOnly

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows Salesforce to send crash reports to Microsoft App Center. Available in API version 57.0
and later.

The default value is `true` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows third parties to store mobile analytics. Available in API version 57.0 and later.

The default value is `true` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether overtime is included in work capacity availability calculations. Available
in API version 59.0 and later.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects FileSearchActivity

**Field** **Details**

**Description**
Specifies if primary members only are included in work capacity availability calculations. If
the value is `false` both primary and secondary members of the service territory are
included. Available in API version 59.0 and later.

The default value is `false` .

```
Language

MasterLabel

### FileSearchActivity

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the field service org settings.

The format for the values is a two-letter language code in small letters, for example, `fr` for
French. If the language has regional dialects, add the two-letter country code in capital
letters, for example, use `fr_BE` for Belgian French.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the field service org settings.

Represents search activity on a file. This object is available in API version 38.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AvgNumResults

```

**Type**
double

**Properties**
Filter, Sort


Standard Objects FileSearchActivity

**Field** **Details**

**Description**
The number of search results returned for the search term. If Period is also included, this
value is aggregated based on the time period specified.

```
ClickRank

CountQueries

CountUsers

Name

Period

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that the file appeared in the search results when users clicked it from the list of
results.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of searches for the period (day, month, or year).

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of individual users who clicked the file.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of search activity.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The time period that the search count is applied to. For example, a record where the Count
is 70 and the Period is Monthly indicates that 70 searches took place over the past month.
Totals are aggregated daily for the current month, monthly from the past full month through
the past full year, and yearly beyond that.


### Standard Objects FiscalYearSettings

**Field** **Details**

Possible values are:

**•** `DAY`

**•** `MONTH`

**•** `YEAR`

```
QueryDate

QueryLanguage

SearchTerm

### FiscalYearSettings

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date of the search.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language filter that’s applied to the user’s search.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first 100 characters of the search term that was used to search published files.

Settings to define a custom or standard fiscal year for your organization. This object has a parent-child relationship with the Period object.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only partner users and standard users can access this object.


Standard Objects FiscalYearSettings

Fields

**Field** **Details**

```
Description

EndDate

IsStandardYear

Name

PeriodId

PeriodLabelScheme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the setting.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the fiscal year.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fiscal year is a standard calendar year ( `true` ) or a custom fiscal year
( `false` ).

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A name for the fiscal year. Limit: 80 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated fiscal period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects FiscalYearSettings

**Field** **Details**

**Description**
The numbering scheme used for fiscal periods.

```
PeriodPrefix

QuarterLabelScheme

QuarterPrefix

StartDate

WeekLabelScheme

WeekStartDay

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal periods. For example, if `p` is the prefix, then the first period is “P1.”

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for fiscal quarters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal quarters. For example, if “Q” is the prefix, then the fourth quarter would
be “Q4.”

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**

Start date of the fiscal year.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for weeks.

**Type**
int


### Standard Objects FldSvcObjChg

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the day that starts the week, for example `Monday` or `Sunday`

```
YearType

```

SEE ALSO:

Period

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates one of two types of fiscal years, Standard or Custom. Standard denotes the standard
Gregorian calendar, while Custom means a fiscal year with a custom structure.

Overview of Salesforce Objects and Fields

### FldSvcObjChg

Represents a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Field Service must be enabled.

**•** The Field Service managed package must be installed.

**•** The **Track the lifecycle of service appointments** setting in **Setup** - **Field Service Settings** must be enabled.

**•** The Platform Integration User must have the Manage Service Appointment Lifecycle and the View Service Appointment Lifecycle
permissions.

**•** To view this object, users must have the View Service Appointment Lifecycle user permission.

Fields

**Field** **Details**

```
Activity

```

**Type**
picklist


Standard Objects FldSvcObjChg

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The available scheduling activities for the service appointment.

Possible values are:

**•** `AddedToBundle` —Currently not supported

**•** `BundleMemberAdded` —Currently not supported

**•** `BundleMemberRemoved` —Currently not supported

**•** `Created`

**•** `Deleted`

**•** `RemovedFromBundle` —Currently not supported

**•** `Rescheduled` —An appointment is considered rescheduled if a change is made to
its assigned service resource or to its scheduled start time.

**•** `Scheduled`

**•** `ServiceResourceAssigned`

**•** `StatusChanged` —The service appointment status was changed. The manual activities
of scheduling, rescheduling, and unscheduling are also reported as status changes
because they change the status of an appointment.

**•** `Unscheduled`

**•** `Updated` —Captures changes made to one or more of the tracked scheduling fields
that aren’t associated with another activity.

```
ActivityDetails

ActivityTimeStamp

IsPrimary

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Details about the scheduling activity such as the scheduling policy that was used and the
unscheduling reason (when applicable).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time of when the change to the service appointment was made.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FldSvcObjChg

**Field** **Details**

**Description**
Indicates whether the change was made directly to the service appointment or indirectly. If
the change was made directly to the appointment, it’s flagged as Primary. If it was made to
another appointment and affected this one, it’s flagged as Secondary.

```
OriginalSvcAppointment

ServiceAppointmentId

TimeZone

Transaction

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the service appointment that was changed. The field value isn’t deleted when the
Service Appointment object is deleted.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the service appointment that was changed. Because this is a relationship field, the
field value is deleted when the Service Appointment object is deleted.

This field is a relationship field.

**Relationship Name**
ServiceAppointment

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time zone of the service appointment or the assigned resource.

**Type**
string

**Properties**
Filter, Nillable, Sort


### Standard Objects FldSvcObjChgDtl

**Field** **Details**

**Description**
The last transaction ID of the scheduling and optimization request that updated this object.
The transaction ID is automatically generated and populated by the Enhanced Scheduling
and Optimization engine.

```
UserId

```

SEE ALSO:

### FldSvcObjChgDtl FldSvcObjChgDtl

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who made the change to the service appointment. If an activity is a scheduled job,
it’s registered with the System Administrator user who configured it.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents the details of a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0 and
later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Field Service must be enabled.

**•** The Field Service managed package must be installed.

**•** The **Track the lifecycle of service appointments** setting in **Setup** - **Field Service Settings** must be enabled.

**•** The Platform Integration User must have the Manage Service Appointment Lifecycle and the View Service Appointment Lifecycle
permissions.

**•** To view this object, users must have the View Service Appointment Lifecycle user permission.


### Standard Objects FlexQueueItem

Fields

**Field** **Details**

```
FieldChangedName

FieldChangedValue

FldSvcObjChgId

```

SEE ALSO:

FldSvcObjChg

### FlexQueueItem

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the field that was changed.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The updated value of the field that was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The parent record associated with the details of the change. The parent record has multiple
detail records associated with it. Each record includes the name and the current value of the
tracked fields.

This field is a relationship field.

**Relationship Name**
FldSvcObjChg

**Relationship Type**
Lookup

**Refers To**
FldSvcObjChg

Represents an asynchronous Apex job in the Apex flex queue. Provides information about the job type and flex queue position of the
AsyncApexJob. This object is available in API version 36.0 and later.


Standard Objects FlexQueueItem

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

In API version 49.0 and later, users must have the View Setup and Configuration permission to access this object.

Fields

**Field Name** **Description**

```
AsyncApexJobId

FlexQueueItemId

JobPosition

JobType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of an AsyncApexJob that’s waiting in the flex queue.

This is a relationship field.

**Relationship Name**
AsyncApexJob

**Relationship Type**
Lookup

**Refers To**
AsyncApexJob

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary key for this FlexQueueItem.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The position in the flex queue of the waiting job. The highest-priority job in the
queue is at position 0.

**Type**
picklist


### Standard Objects FlowDefinitionView

**Field Name** **Description**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of the job. Valid values are:

**•** `ApexToken`

**•** `BatchApex`

**•** `BatchApexWorker`

**•** `Future`

**•** `Queueable`

**•** `ScheduledApex`

**•** `SharingRecalculation`

**•** `TestRequest`

**•** `TestWorker`

Currently, queries are supported only on `BatchApex` jobs.

Usage

To find the position of an AsyncApexJob in the flex queue, query `JobPosition` . For example:

```
   SELECT JobPosition FROM FlexQueueItem WHERE JobType = 'BatchApex' AND AsyncApexJobId =

   '707xx000000DABC'

```

To find the job at a given position, query `AsyncApexJobId` . For example:

```
   SELECT AsyncApexJobId FROM FlexQueueItem WHERE JobType = 'BatchApex' AND JobPosition = '2'

```

To find all batch jobs in the flex queue, query `JobType` . To get other information about the jobs, include AsyncApexJob in your query.
For example:

```
   SELECT JobType, JobPosition, AsyncApexJob.ApexClass.Name, AsyncApexJob.CreatedDate,

      AsyncApexJob.CreatedById FROM FlexQueueItem WHERE JobType='BatchApex' AND

      AsyncApexJob.ApexClass.Name LIKE '%BatchAJob%' ORDER BY JobPosition DESC

### FlowDefinitionView

```

Represents the description of a flow definition. This object is available in API version 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects FlowDefinitionView

Fields

**Field** **Details**

```
ActiveVersionId

ApiName

ApiVersion

AreMetricsLoggedToDataCloud

Builder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow definition.

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Possible values are:

**•** Cloud Flow Designer

**•** Flow Builder

**•** Swing Designer


Standard Objects FlowDefinitionView

**Field** **Details**

This field is available in API version 47.0 and later.

```
CapacityCategory

Description

DurableId

Environments

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow definition information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow definition.

**Type**
multipicklist

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default` —The flow can run from a Visualforce component, Lightning page,
flow action, or custom Aura component.

**•** `Offline` —The flow can run only offline. Flow types that support offline flows
must set this value. This value is available in API version 62.0 and later.

**•** `Slack` —The flow can run in Slack and the default environment. You specify
the Slack flow environment when you save the flow.

This field is available in API version 55.0 to 62.0. This field is deprecated in API version
63.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

```
HasAsyncAfterCommitPath

InstalledPackageName

IsActive

IsOutOfDate

IsOverridable

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the scheduled path runs asynchronously after a save. The default
value is false. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the installed package that includes this flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the latest version of the flow definition is the active flow version.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the active flow version is the latest version of the flow definition.

This field is available in API version 47.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is overridable. The default value is false. This field is available
in API version 53.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

```
IsSwingFlow

IsTemplate

Label

LastModifiedBy

LatestVersionId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. The default value is `false` .
When installed from managed packages, subscribers can’t view or clone processes
or flows because of intellectual property (IP) protection. But when those processes
and flows are templates, subscribers can open them in a builder, clone them, and
customize the clones.

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who last updated this flow definition.

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the latest flow version, regardless of the flow’s status.


Standard Objects FlowDefinitionView

**Field** **Details**

```
ManageableState

NamespacePrefix

OverriddenById

OverriddenFlowId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the flow that is contained in a package. Possible
values are:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 47.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow definition.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The flow that’s overriding the current flow. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string


Standard Objects FlowDefinitionView

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The flow that the current flow is overriding. This is a relationship field. This field is
available in API version 53.0 and later.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

```
ProcessType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s executed when a
user completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This
value is available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API
version 44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for an approval process.
This value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request to be contacted
by customer support. This flow is used to create contact request records. This
value is available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate
survey questions with different stages in customer lifecycles. This value is available


Standard Objects FlowDefinitionView

**Field** **Details**

in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent` —A process that is invoked when it receives a platform event
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow`                     - In the UI, Data Capture flows configure the Form tab
in the Field Service mobile app. When the Data Capture flow is launched, its Flow
metadata is publicly available in JavaScript format. This value is available in API
version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `EvaluationFlow` —A flow for evaluating custom entry and exit conditions
in an orchestration. Uses the `isOrchestrationConditionMet` output
variable and discards values from any other output variables. This value is available
in API version 54.0 and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value
is available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more
screens or local actions, choices, or dynamic choices. In the UI and Salesforce
Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is
available in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration
and updates for single sign-on with the authentication provider framework.
Available in API version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow` —A flow that associates individuals
with interactions such as voice calls, messaging sessions, or case-related emails.
This value is available in API version 58.0 and later.

**•** `InvocableProcess` —A process that another process or the Invocable
Actions resource in REST API invokes. This value is available in API version 38.0
and later.

**•** `Journey` —An audience-driven flow for Marketing Cloud. This value is available
in API version 57.0 and later.


Standard Objects FlowDefinitionView

**Field** **Details**

**•** `LoginFlow` —A flow for login. This value is available in API version 51.0 and
later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app that’s
invokable by loyalty program processes. This value is available in API version 54.0
and later.

**•** `Orchestrator` —An orchestration that organizes flows into groups of steps
contained in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder
and the flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy` —Build recommendations for your users. A
recommendation launches its assigned flow. This value is available in API version
[54.0 and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=platform.nba_building_flow_builder_strategy.htm&type=5&language=en_US)

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business
logic. This value is available in API version 52.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created
in Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper.
From the UI, this type of flow is created in the Survey Builder and requires an
associated survey flow type. This value is available in API version 49.0 or later and
only when the Customer Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In
the UI and Salesforce Help, it’s a record change process.

These values are reserved for future use:

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

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that


Standard Objects FlowDefinitionView

**Field** **Details**

the flow contains only the elements, resources, and functionality that the new flow type
supports.

```
RecordTriggerType

SourceTemplateId

SupportedEnvironments

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies what type of record changes can start the flow. Possible values are:

**•** `Create`

**•** `CreateAndUpdate`

**•** `Delete`

**•** `None`

**•** `Update`

Available only when `triggerType` is `RecordBeforeSave` . This field is
available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The template that the current flow was created from. This is a relationship field. This
field is available in API version 53.0 and later.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable

**Description**
The environment in which the flow can run. Valid values are:

**•** `Default` —The flow can run from a Visualforce component, Lightning page,
flow action, or custom Aura component.

**•** `Offline` —The flow can run only offline. Flow types that support offline flows
must set this value.


Standard Objects FlowDefinitionView

**Field** **Details**

**•** `Slack` —The flow can run in Slack and the default environment. You specify
the Slack flow environment when you save the flow.

This field is available in API version 63.0 and later.

```
TriggerObjectOrEventId

TriggerObjectOrEventLabel

TriggerOrder

TriggerType

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
ID of the object or platform event that triggers this flow. This field is available in API
version 53.0 and later.

This is a relationship field.

**Relationship Name**
TriggerObjectOrEvent

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is available
in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
[The run order of a record-triggered flow, from 1 to 2,000. See "Guidelines for Defining](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
[the Run Order of Record-Triggered Flows for an Object" in Salesforce Help. Available](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
in API version 54.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects FlowDefinitionView

**Field** **Details**

**Description**
Specifies what causes the flow to run. If you exclude this field, the flow has no trigger
and starts only when a user or app launches the flow. Valid values are:

**•** `AutomationEvent` —The flow starts when an automation event such as an
SMS subscription occurs. This value is available in API version 62.0 and later.

**•** `Capability` —The flow starts when the specified capability that the flow
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `DataCloudDataChange` —The flow starts when data model object (DMO)
or calculated insight object (CIO) conditions are met. This value is available in API
version 59.0 and later.

**•** `DataGraphDataChange` —The flow starts when conditions are met in the
specified data graph field. This value is available in API version 63.0 and later.

**•** `EventDrivenJourney` —Reserved for internal use.

**•** `ExternalSystemChange` —The flow starts when an external system change
event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent` —The flow runs when a user submits data via a
webform. In Flow Builder, this value corresponds to `Form` . This value is available
in API version 60.0 and later.

**•** `PlatformEvent` —The flow starts when a platform event message is received.
This value is available in API version 49.0 and later.

**•** `RecordAfterSave` —The flow starts after a record is saved. This value is
available in API version 49.0 and later.

**•** `RecordBeforeDelete` —Deleting a record triggers an autolaunched flow
before the record is deleted from the database. This value is available in API version
50.0 and later.

**•** `RecordBeforeSave` —Creating and/or updating a record triggers an
autolaunched flow to make additional updates to that record before it's saved to
the database. This value is available in API version 48.0 and later.

**•** `Scheduled` —The flow starts at the scheduled time. This value is available in
API version 47.0 and later.

**•** `Segment`                     - At the scheduled time, the flow send emails to individuals included
in the chosen segment. This value is available in API version 56.0 and later.

Available only when `processType` is `AutoLaunchedFlow` or `PromptFlow` .
This field is available in API version 47.0 and later.

```
VersionNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s version number. This field is available in API version 54.0 and later.


### Standard Objects FlowInterview

Usage

Use this object to query information about flow definitions.

### FlowInterview

Represents a flow interview. A _flow interview_ is a running instance of a flow. This object is available in API version 32.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To delete a flow interview, you must have the “Manage Flow” user permission. All other calls require the “Run Flows” user permission or
the `Flow User` field enabled on the user detail page. If **Override default behavior and restrict access to enabled profiles or**
**permission sets** is selected for an individual flow, access to that specific flow and its interviews is given to users by profile or permission
set.

Fields

**Field Name** **Details**

```
CurrentElement

EngineType

FlowVersionViewId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow element at which the interview is paused.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The engine type used to run the flow interview.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
This field is a relationship field. This field is available in API version 51.0 and later.


Standard Objects FlowInterview

**Field Name** **Details**

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

```
Guid

InterviewLabel

InterviewStatus

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Globally unique identifier for the interview.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the interview. This label helps users and administrators differentiate
interviews from the same flow.

In the user interface, this label appears in the Paused Flow Interviews component
on the user’s Home tab and in the list of paused flow interviews in Setup.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the interview. Valid values are:

**•** `Completed` —This flow is complete. There are no more records to process.

**•** `Error` —This flow has one or more errors. To resolve each error, check the
error code for instructions.

**•** `Paused` —This flow is paused. No new processes are added until the flow
is resumed.

**•** `Running` —This flow is running or is ready to run.

**•** `VersionPaused` —This flow version is paused. No more records are
processed until the flow is resumed. This value is available in API version 60.0
and later.

This field is available in API version 50.0 and later.


Standard Objects FlowInterview

**Field Name** **Details**

```
Name

OwnerId

PauseLabel

WasPausedFromScreen

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the interview.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the interview. Only this user or an admin can resume
the interview.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Information about why the interview was paused. This string is entered by the
user who paused the flow interview. The label is **Why Paused** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the flow interview was paused by a user from a flow Screen element
( `true` ) or not ( `false` ). This field is available in API version 46.0 and later.

This object has these associated objects. Unless noted, these objects are available in the same API version as this object.


### Standard Objects FlowInterviewLog

**FlowInterviewOwnerSharingRule**

Sharing rules are available for the object.

**FlowInterviewShare**

Sharing is available for the object.

### FlowInterviewLog

Represents the logs of a screen flow interview. An _interview_ is an instance of a running or previously run flow.This object is available in
API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

By default, only users with the View All Data permission can access the logs for flows that are run by other users. To let users access other
### users’ flow logs, set up sharing settings with the FlowInterviewLogOwnerSharingRule object.

Fields

**Field Name** **Details**

```
FlowDeveloperName

FlowInterviewGuid

FlowLabel

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow's API name.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Globally unique identifier for the interview.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowInterviewLog

**Field Name** **Details**

**Description**
The flow’s label. Only shows up in API results when users query FlowInterviewLog, or when
they include this field in a report.

```
FlowNamespace

FlowVersionNumber

InterviewDurationInMinutes

InterviewEndTimestamp

InterviewStartTimestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace of the flow interview logged in the FlowInterviewLog.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of the flow version for a flow definition. Flow versions are counted sequentially
from 1.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total number of minutes between InterviewStartTimestamp and InterviewEndTimestamp,
even if flow interview is paused.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the interview ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the interview started.


Standard Objects FlowInterviewLog

**Field Name** **Details**

```
InterviewStatus

Name

OwnerId

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the interview. Valid values are:

**•** `Autosaved` —This value is available in API version 62.0 and later.

**•** `Completed`

**•** `Error`

**•** `Expired` —This value is available in API version 62.0 and later.

**•** `Paused`

**•** `Running`

**•** `VersionPaused` —This value is available in API version 60.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated name of the flow interview log record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user who owns the FlowInterviewLog record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**FlowInterviewOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects FlowInterviewLogEntry FlowInterviewLogEntry

Represents the log of a specific element that’s executed by a screen flow interview. An _interview_ is an instance of a running or previously
run flow. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

By default, only users with the View All Data permission can access the log entries for flows that are run by other users.

Fields

**Field Name** **Details**

```
DurationSinceStartInMinutes

ElementApiName

ElementDurationInMinutes

ElementLabel

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of minutes that elapsed since the flow interview started, even if flow interview is
paused.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
API name of the flow element.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Number of minutes that elapsed since the element executed. For example, if a screen element
takes users a long time to complete, consider simplifying the screen.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowInterviewLogEntry

**Field Name** **Details**

**Description**
The flow element’s label.

```
FlowInterviewLogId

LogEntryTimestamp

LogEntryType

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
FlowInterviewLog

**Relationship Type**
Lookup

**Refers To**
FlowInterviewLog

**Type**
datetime

**Properties**
Filter, Sort

**Description**
Date and time when the flow element started to execute.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of screen flow user action triggered the log entry. Valid values are:

**•** `Error`

**•** `FlowFinish-Finished Flow`

**•** `FlowPause-Paused Flow`

**•** `FlowResume-Resumed Flow`

**•** `FlowStart-Started Flow`

**•** `ScreenFinish-Clicked Finish`

**•** `ScreenNext-Clicked Next`

**•** `ScreenPrevious-Clicked Previous`

**Type**
string


### Standard Objects FlowInterviewLogOwnerSharingRule

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Autogenerated name of the flow interview log entry.

### FlowInterviewLogOwnerSharingRule

Represents the rules for sharing a FlowInterviewLog with users other than the owner.This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed.

Possible values are:

**•** `Edit` —Read/Write

**•** `Read` —Read Only

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects FlowInterviewLogOwnerSharingRule

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
GroupId

Name

OptionsIncludeHVUOwnedRecords

OptionsIncludeRecordsOwnedByAll

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects FlowInterviewOwnerSharingRule

**Field** **Details**

**Description**
The ID representing the target user or group that’s given access.

Usage

Use this object to manage the sharing rules for FlowInterviewLog records. General sharing uses this object.

### FlowInterviewOwnerSharingRule

Represents the rules for sharing a FlowInterview with users other than the owner. This object is available in API version 33.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
AccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit` —In API version 42.0 and later, when **Let users resume shared flow**
**interviews** is enabled for your org, users can resume all flow interviews that they
have edit access to.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string


Standard Objects FlowInterviewOwnerSharingRule

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

```
GroupId

Name

UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group that’s given access.

Use this object to manage the sharing rules for FlowInterview records. General sharing uses this object.

In API version 42.0 and later, when **Let users resume shared flow interviews** is enabled for your org, users can resume all flow interviews
that they have edit access to. When that setting is disabled, only the owner or a flow admin can resume a flow interview. To disable this
setting, go to your org’s Process Automation Settings in Setup.


### Standard Objects FlowInterviewShare FlowInterviewShare

Represents a sharing entry on a FlowInterview. This object is available in API version 33.0 and later.

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

**Field** **Details**

```
AccessLevel

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the FlowInterview. The possible values are:

**•** `Read`

**•** `Edit` —In API version 42.0 and later, when **Let users resume shared flow interviews**
is enabled for your org, users can resume all flow interviews that they have edit access
to.

**•** `All` —This value is not valid for creating or deleting records.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FlowInterview associated with this sharing entry.

This is a relationship field.

**Relationship Name**
Parent


Standard Objects FlowInterviewShare

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowInterview

```
RowCause

UserOrGroupId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the FlowInterview with them.

**•** `Owner` —The User is the owner of the FlowInterview.

**•** `Rule` —The User or Group has access via a FlowInterview sharing rule.

**•** `GuestRule` —The User or Group has access via a FlowInterview guest user sharing
rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the FlowInterview. This field can't be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object lets you determine which users and groups can view and edit flow interviews that are owned by other users.


### Standard Objects FlowNavMetricEventLog

In API version 42.0 and later, when **Let users resume shared flow interviews** is enabled for your org, users can resume all flow interviews
that they have edit access to. When that setting is disabled, only the owner or a flow admin can resume a flow interview. To disable this
setting, go to your org’s Process Automation Settings in Setup.

### FlowNavMetricEventLog

Flow Navigation Metric event logs contain metric data for flow interviews such as total execution time, number of interviews, and number
of errors. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

ErrorCount

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

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of errors for all flow interviews after the flow version was executed.


Standard Objects FlowNavMetricEventLog

**Field** **Details**

```
FlowLoadTime

FlowVersionIdentifier

InterviewCount

PlannerIdentifier

ProcessType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds to load the flow’s metadata.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version that was executed.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of flow interviews that started after the flow version was executed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable event
orchestration process in the background and automatically executes different types of
actions based on the event type. This value is available in API version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s executed when a user
completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This value is
available in API version 56.0 and later.


Standard Objects FlowNavMetricEventLog

**Field** **Details**

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein Activity
Capture detects and captures a new activity, such as an email. This type of flow runs in
the background without user interaction. This value is available with Sync Email as
Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API version
44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for an approval process. This
value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.

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


Standard Objects FlowNavMetricEventLog

**Field** **Details**

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


### Standard Objects FlowOrchestration

**Field** **Details**

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

```
RequestIdentifier

Timestamp

TotalExecutionTime

UserIdentifier

### FlowOrchestration

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`TID:000000000000c00fff` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the flow was executed in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in milliseconds to start and finish all flow interviews.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who executed the flow through the UI or the API. For example:
`00530000009M943` .

Represents the details of an orchestration definition. This object is available in API version 62.0 and later.


Standard Objects FlowOrchestration

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`

Fields

**Field** **Details**

```
ActiveVersionId

ApiName

ApiVersion

AverageRunTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active orchestration version. This field is a relationship field.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Refers To**
FlowOrchestrationVersion

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the the orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the active orchestration or the last saved orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The average duration of an orchestration run that has completed without error.


Standard Objects FlowOrchestration

**Field** **Details**

```
CompletionRate

Description

FailedRunCount

InstalledPackageName

IsCitizenEnabled

IsOverridable

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the total number of orchestration runs that have completed without error.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
The description of the flow orchestration.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have failed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the installed package that the orchestration is a part of.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration can be modified by non-admins. Valid value is False.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects FlowOrchestration

**Field** **Details**

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false` .

```
IsTemplate

LastReferencedDate

LastViewedDate

ManageableState

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record is a template.

The default value is `false` .

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
The timestamp for when the current user last viewed this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the managable state of the orchestration that's contained in a package.

Valid values are:

**•** `beta` —Managed-Beta

**•** `deleted` —Managed-Proposed-Deleted

**•** `deprecated` —Managed-Proposed-Deprecated

**•** `deprecatedEditable` —SecondGen-Installed-Deprecated

**•** `installed` —Managed-Installed

**•** `installedEditable` —SecondGen-Installed-Editable

**•** `released` —Managed-Released


Standard Objects FlowOrchestration

**Field** **Details**

**•** `unmanaged` —Unmanaged

```
Name

NamespacePrefix

OrchestrationDefinition

OrchestrationLabel

OrchestrationType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The label of the orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the orchestration record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the orchestration definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The label of the orchestration.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The orchestration's flow type. FlowType consolidates ProcessType and TriggerType into one
field. FlowType is used with permissions, so admins can control access to each flow type.

Valid values are:

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration: Launches when invoked
by Apex, REST API, custom buttons, or custom links. An orchestration lets you create a
multi-step, multi-user process.


Standard Objects FlowOrchestration

**Field** **Details**

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration: Launches
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch` —CMS Workflow Orchestration Autolaunched: Launches when
invoked from the Workflows component in a CMS workspace. This type of orchestration
lets you create a multi-step, multi-user process to create, edit, organize, and manage
digital content from a centralized location

```
OverriddenById

OverriddenOrchestrationId

RunCount

SourceTemplateId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that's overriding the current orchestration.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Refers To**
FlowOrchestration

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.

**Relationship Name**
OverriddenOrchestration

**Refers To**
FlowOrchestration

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of orchestration runs that have been started across all orchestration versions.

**Type**
reference


Standard Objects FlowOrchestration

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template that the orchestration was created from.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

```
Status

TriggerType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the record.

Valid values are:

**•** `Active` —Active

**•** `Draft` —Inactive

**•** `InvalidDraft` —Draft

**•** `Obsolete` —Inactive

**•** `UnderReview` —Under Review

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the trigger type for a record-triggered orchestration.

Valid values are:

**•** `RecordAfterSave` —Record—Run After Save

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationChangeEvent on page 68**
Change events are available for the object.


### Standard Objects FlowOrchestrationInstance FlowOrchestrationInstance

Represents a run-time instance of an orchestration. This object is available in API version 53.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationInstance, they determine access to specific orchestration run records. Or the user must
have the View All Data permission.

Fields

**Field** **Details**

```
CurrentStage

Duration

InterviewId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage that was running when the orchestration run was paused or failed
because of an error in an action called by a step. This field is available in API version 62.0 and
later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The duration of the orchestration instance in seconds. Durations are incremented until the
orchestration is completed, canceled, or ends in an error. This field is available in API version
62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The globally unique flow interview ID associated with the orchestration instance.

This field is a relationship field.

**Relationship Name**
Interview


Standard Objects FlowOrchestrationInstance

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowInterview

```
LastReferencedDate

LastViewedDate

Name

OrchestrationDeveloperName

OrchestrationLabel

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration run. This field is
available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration run. This field is available in API version
55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the orchestration instance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name of the flow definition associated with the orchestration run. This field
is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the orchestration. This field is available in API version 63.0 and later.


Standard Objects FlowOrchestrationInstance

**Field** **Details**

```
OwnerId

Status

TriggeringRecord

TriggeringRecordType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the orchestration run. Valid values are:

**•** `Canceled` —The orchestration instance was canceled.

**•** `Completed` —The orchestration instance completed.

**•** `Error` —The orchestration instance, or a stage or step within the orchestration instance,
encountered an error.

**•** `InProgress` —The orchestration instance is in progress.

**•** `Suspended` —The orchestration instance was suspended.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that triggered the record-triggered orchestration. This field is available
in API version 62.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Salesforce object configured to trigger the orchestration. This field is available
in API version 64.0 and later.


### Standard Objects FlowOrchestrationLog

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object. This object is available in API version 56.0 and later.

**FlowOrchestrationInstanceShare on page 67**
Sharing is available for the object. This object is available in API version 56.0 and later.

### FlowOrchestrationLog

Represents logging data for a FlowOrchestrationInstance. This object is available in API version 54.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()update()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationInstance and the Inherit orchestration run sharing rules to control orchestration run log
record access setting is enabled, then orchestration run log record access is inherited from related orchestration run records. If the Inherit
orchestration run sharing rules to control orchestration run log record access setting isn’t enabled, a user must have the Manage Flow
permission. Or the user must have the View All Data permission.

Fields

**Field** **Details**

```
Actor

Assignee

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For an interactive step, the user that completed the work item.

For a background or MuleSoft step, the username of the user that the step ran as.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowOrchestrationLog

**Field** **Details**

**Description**
For an interactive step, the user, group, or queue assigned to a work item when the
FlowOrchestrationLog relates to an interactive FlowOrchestrationStep.

```
AssigneeType

Comments

Context

Duration

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For an interactive step, the assignee type associated with an interactive step's work item.
Valid values are:

**•** `Group`

**•** `Invalid`

**•** `Queue`

**•** `User`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string stored in an output variable with the API name of Comments from a flow called
by a completed orchestration step.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record where the assigned user completed the flow associated with an
interactive step in the Work Guide component.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
A long number that indicates the duration, in seconds, of the associated
FlowOrchestrationInstance, FlowOrchestrationStage, FlowOrchestrationStep, or
FlowOrchestrationWorkItem.


Standard Objects FlowOrchestrationLog

**Field** **Details**

```
Kind

Name

OrchestationInstanceId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The milestone associated with the FlowOrchestrationLog. Valid values are:

**•** `CancelInstance` —The associated FlowOrchestrationInstance was canceled.

**•** `DiscontinueStage` —The associated FlowOrchestrationStage was discontinued.

**•** `DiscontinueStep` —The associated FlowOrchestrationStep was discontinued.

**•** `EndInstance` —The associated FlowOrchestrationInstance was completed
successfully.

**•** `EndStage` —The associated FlowOrchestrationStage was exited successfully.

**•** `EndStep` —The associated FlowOrchestrationStep was exited successfully.

**•** `EndWorkItem` —The associated FlowOrchestrationWorkItem was completed
successfully.

**•** `FailInstance` —The associated FlowOrchestrationInstance encountered an error.

**•** `FailStage` —The associated FlowOrchestrationStage encountered an error.

**•** `FailStep` —The associated FlowOrchestrationStep encountered an error.

**•** `ResumeInstance` —A failed or paused orchestration instance was resumed.

**•** `ReassignWorkItem` —The associated FlowOrchestrationWorkItem was reassigned.

**•** `RunRecallPath` —The associated approval submission was recalled.

**•** `StartInstance` —The associated FlowOrchestrationInstance started.

**•** `StartStage` —The associated FlowOrchestrationStage started.

**•** `StartStep` —The associated FlowOrchestrationStep started.

**•** `StartWorkItem` —The associated FlowOrchestrationWorkItem started.

**•** `SuspendInstance` —The associated FlowOrchestrationInstance was suspended.

**•** `SuspendStage` —The associated FlowOrchestrationStage was suspended.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name for the FlowOrchestrationLog record.

**Type**
reference

**Properties**
Filter, Sort, Group


Standard Objects FlowOrchestrationLog

**Field** **Details**

**Description**
The FlowOrchestrationInstance associated with the FlowOrchestrationLog.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

```
OrchestrationName

OrchestrationVersion

StageName

StepName

Timestamp

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the orchestration.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
An integer for the FlowDefinitionVersion of the orchestration associated with the
FlowOrchestrationLog.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the stage in the associated orchestration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the step in the associated orchestration.

**Type**
dateTime


### Standard Objects FlowOrchestrationStageInstance

**Field** **Details**

**Properties**
Filter, Sort

**Description**
The date and time when the FlowOrchestrationLog milestone occured.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationLogFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationLogHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationLogOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationLogShare on page 67**
Sharing is available for the object.

### FlowOrchestrationStageInstance

Represents a run-time instance of a stage in a run-time instance of an orchestration. This read-only object is available in API version 53.0
and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationStageInstance, they determine access to specific orchestration stage run records. Or
the user must have the View All Data permission.

Fields

**Field** **Details**

```
Label

```

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects FlowOrchestrationStageInstance

**Field** **Details**

**Description**
The label for the flow orchestration stage instance. This label helps users and administrators
differentiate between step instances from the same orchestration.

```
Name

OrchestrationInstanceId

OwnerId

Position

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name for the flow orchestration stage instance.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration stage instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int


### Standard Objects FlowOrchestrationStepInstance

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
For internal use only.

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The run status of the orchestration stage instance. Valid values are:

**•** `Completed` —The stage instance completed.

**•** `Discontinued` —The stage was in progress or completed when the orchestration
instance encountered an error.

**•** `Error` —The stage instance encountered an error, an instance of a background step
within the stage encountered and error, or an autolaunched flow called by a background
step within the stage encountered an error.

**•** `InProgress` —The stage instance is in progress.

**•** `Suspended` —The stage was in progress when the orchestration instance was manually
suspended.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStageInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationStageInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationStageInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationStageInstanceShare on page 67**
Sharing is available for the object.

### FlowOrchestrationStepInstance

Represents a run-time instance of a step in a run-time instance of a stage of a run-time instance of an orchestration. This read-only object
is available in API version 53.0 and later.


Standard Objects FlowOrchestrationStepInstance

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

If sharing rules are defined for FlowOrchestrationStepInstance, they determine access to specific orchestration step run records. Or the
user must have the View All Data permission.

Fields

**Field** **Details**

```
Description

Label

Name

OrchestrationInstanceId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the step.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the step.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the step.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
OrchestrationInstance


Standard Objects FlowOrchestrationStepInstance

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstance

```
OwnerId

StageInstanceId

Status

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the automated process user. This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the FlowOrchestrationStageInstance associated with the orchestration step instance.

This field is a relationship field.

**Relationship Name**
StageInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationStageInstance

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the orchestration step instance. Valid values are:

**•** `Completed` —The step instance completed.


### Standard Objects FlowOrchestrationVersion

**Field** **Details**

**•** `Discontinued` —The step instance was in progress or completed when it’s associated
stage instance completed, or the step was in progress or completed when the
orchestration instance encountered an error.

**•** `Error` —The step instance encountered an error or the autolaunched flow associated
with a step instance encountered an error.

**•** `InProgress` —The step instance is running, the step instance was in progress when
its associated stage encountered an error, or the screen flow associated with the step
instance encountered an error.

**•** `NotStarted` —The step instance was created, but hasn’t met its entry condition.

```
StepType

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of step. Valid values are:

**•** `InteractiveStep` —Interactive Step

**•** `BackgroundStep` —Background Step

**•** `AynchronousBackgroundStep` —Asynchronous Background Step

This value is available in API version 54.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationStepInstanceFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationStepInstanceHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationStepInstanceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationStepInstanceShare on page 67**
Sharing is available for the object.

### FlowOrchestrationVersion

Represents the version of an orchestration. This object is available in API version 62.0 and later.


Standard Objects FlowOrchestrationVersion

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ActivatedById

ActivatedDate

ApiVersion

Description

FlowOrchestrationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that activated the orchestration.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the orchestration was activated.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version of this orchestration record version.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow orchestration version.

**Type**
reference


Standard Objects FlowOrchestrationVersion

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent orchestration running this version.

This field is a relationship field.

**Relationship Name**
FlowOrchestration

**Relationship Type**
Master-detail

**Refers To**
FlowOrchestration

```
IsOverridable

IsTemplate

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration that's part of a managed package is overridable.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the orchestration record version is a template.

The default value is `false` .

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
The timestamp for when the current user last viewed this record.


Standard Objects FlowOrchestrationVersion

**Field** **Details**

```
Name

OrchestrationType

OverriddenById

OverriddenOrchestrationId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the orchestration.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The orchestration's flow type. FlowType consolidates ProcessType and TriggerType into one
field. FlowType is used with permissions, so admins can control access to each flow type.

Valid values are:

**•** `OrchAutolnch` —Autolaunched No Trigger Orchestration: Launches when invoked
by Apex, REST API, custom buttons, or custom links. An orchestration lets you create a
multi-step, multi-user process.

**•** `OrchRecTrigAftSave` —Record-Triggered After Save Orchestration: Launches
when a record is created or updated. An orchestration lets you create a multi-step,
multi-user process. This type of flow runs in the background without user interaction.

**•** `CmsOrchAutolnch` —CMS Workflow Orchestration Autolaunched: Launches when
invoked from the Workflows component in a CMS workspace. This type of orchestration
lets you create a multi-step, multi-user process to create, edit, organize, and manage
digital content from a centralized location

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that's overriding the current orchestration.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Refers To**
FlowOrchestration

**Type**
reference


Standard Objects FlowOrchestrationVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the orchestration that the current orchestration is overriding.

This field is a relationship field.

**Relationship Name**
OverriddenOrchestration

**Refers To**
FlowOrchestration

```
RunInMode

SourceTemplateId

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the orchestration runs in.

Possible values are:

**•** `DefaultMode` —The orchestration version runs in system or user context, depending
on how the orchestration is launched.

**•** `SystemModeWithSharing` —The orchestration version always runs in system
mode with sharing. The orchestration respects org-wide default settings, role hierarchies,
sharing rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

**•** `SystemModeWithoutSharing` —The orchestration version can access all data.
In the UI, this value appears as System Context without Sharing—Access All Data.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Refers To**
FlowOrchestration

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**Description**
The ID of the template that the orchestration was created from. This is a relationship
field.(Refers to Orchestration Record).

Possible values are:

**•** `Active` —Active

**•** `Draft` —Inactive

**•** `InvalidDraft` —Draft

**•** `Obsolete` —Inactive

**•** `UnderReview` —Under Review

```
TriggerObjectOrEventLabel

VersionNumber

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the orchestration version.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationVersionChangeEvent on page 68**
Change events are available for the object.

### FlowOrchestrationWorkItem

Represents a work item associated with a run-time instance of an interactive step in a run-time instance of an orchestration. This object
is available in API version 54.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```


Standard Objects FlowOrchestrationWorkItem

Special Access Rules

An assignee can see all work item records assigned to them. If sharing rules are defined for FlowOrchestrationWorkItem, they determine
access to specific orchestration work item records for users other than the assignee. Or the user must have the View All Data permission.

Fields

**Field** **Details**

```
AssigneeId

Description

ElapsedTimeSinceAsgntInSec

ElapsedTimeSinceCreationInSec

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user, group, or queue assigned to the orchestration work item.

This field is a polymorphic relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
Group (Type = Regular), Group (Type = Queue), User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the orchestration work item.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
last assigned. When status is Completed, this value is null. This field is available in API version
63.0 and later.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**Description**
When status is Assigned, the number of seconds that have passed since the work item was
created. When status is Completed, this value is null. This field is available in API version 63.0
and later.

```
Label

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the orchestration work item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed a record related to the orchestration work item. This
field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent time a user viewed the orchestration work item. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the orchestration work item.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**

**•** When the assignee is an internal user: the ID of the internal user


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**•** When the assignee is a credentialed Experience Cloud site visitor: the ID of the
credentialed Experience Cloud site visitor

**•** When the assignee is a group or queue: the ID of the automated process user

This field is available in API version 56.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
RelatedRecordId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the context record, such as an account, case, or expense, that the orchestration
work item is related to. An assigned user completes the associated orchestration work item
on the page for this record.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
All objects except AccountContactRelation, AccountTeamMember, ActiveScratchOrg,
ActivityMetric, ActivityMetricRollup,CampaignMember, CartCheckoutSession,
CartDeliveryGroup, CartDeliveryGroupMethod, ChatterActivity,CollaborationGroupMember,
ContentDesignKit, ContentDesignKitVersion, ConversationBroadcastEntry,ConversationReason,
ConversationReasonExcerpt, ConversationReasonGroup,
CustomPersonDataTemplate,ElectronicMediaGroup, EngagementScore, Event, FeedItem,
FlowOrchestrationWorkItem, FtestDelPlatform1,FtestDelPlatform2,
FtestFormulaFieldRefSql,HighScaleSample, HighScaleSampleItem, LegalEntity, LocationWaitlist,
LocationWaitlistedParty,LocWaitlistMsgTemplate, ManagedContentVersion,
MessagingEndUser, MessagingSession, MLModel,MLModelFactor, MLModelFactorComponent,
NetworkMember, NetworkMemberChunk, OpportunityContactRole,OpportunityLineItem,
OpportunityScore, OpportunityTeamMember, OrgSnapshot,
PaymentTermItem,RequestsForAccessSIQ, ScoreIntelligence, ScratchOrgInfo,
SharingRecordCollection, SharingRecordCollectionItem,SharingRecordCollectionMember,
StreamActivityAccess, Survey, SurveyMessagingChannel, SurveyPage,SurveyQuestionChoice,
SurveyVersion, Task, TenantSecurityAlertRuleSelectedTenant,
TenantSecurityApiAnomaly,TenantSecurityConnectedApp, TenantSecurityCredentialStuffing,
TenantSecurityHealthCheckBaselineTrend,TenantSecurityHealthCheckDetail,


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

TenantSecurityHealthCheckTrend, TenantSecurityLogin,
TenantSecurityMetricDetail,TenantSecurityMetricDetailLink, TenantSecurityMobilePolicyTrend,
TenantSecurityMonitorMetric,TenantSecurityNotification, TenantSecurityNotificationRule,
TenantSecurityPackage, TenantSecurityPolicy,TenantSecurityPolicyChangeLog,
TenantSecurityPolicyDeployment,
TenantSecurityPolicySelectedTenant,TenantSecurityReportAnomaly,
TenantSecuritySessionHijacking, TenantSecurityTenantChangeLog,TenantSecurityTenantInfo,
TenantSecurityTrustedIpRangeTrend, TenantSecurityUserActivity,
TenantSecurityUserPerm,TenantSecurityWebsite, TopicAssignment, UserExternalCredential,
VoiceCall

```
ScreenFlow

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The screen flow associated with the orchestration work item.

Possible values are:

**•** `healthcloud_pm_flows__AcceptSlots`

**•** `industries_automotive__AutoIV`

**•** `industries_mfg_service__MfgIv`

**•** `omnichannel_chat__QueuesChat`

**•** `omnichannel_chat__SkillsChat`

**•** `omnichannel_messaging__MsgRouting`

**•** `omnichannel_voice__VoiceRouting`

**•** `opencti__SCV_Basic_Routing_Flow`

**•** `runtime_appointmentbooking__Flow`

**•** `runtime_appointmentbooking__Guest_Flow`

**•** `runtime_appointmentbooking__In_Cancel`

**•** `runtime_appointmentbooking__In_Modify`

**•** `runtime_appointmentbooking__In_New`

**•** `runtime_appointmentbooking__Inv_Book`

**•** `runtime_appointmentbooking__Inv_Gen`

**•** `runtime_appointmentbooking__Out_Modify`

**•** `runtime_commerce_adj__Discount_Item`

**•** `runtime_commerce_exc__Exchange_Flow`

**•** `runtime_commerce_oms__Cancel_Item`

**•** `runtime_commerce_oms__Create_OS`

**•** `runtime_commerce_oms__Create_PE`

**•** `runtime_commerce_oms__Return_Item`


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

**•** `runtime_commerce_rma__Create_CO`

**•** `runtime_commerce_rma__Return_Item_RMA`

**•** `runtime_commerce_rs__Reship_FO`

**•** `runtime_industries_recurrence__Orch`

**•** `runtime_industries_recurrence__Schdlr`

**•** `sales_channel__BroadcastArchive`

**•** `sales_channel__DealWon`

**•** `sales_channel__DealsToWatch`

**•** `sales_channel__HighPriorityCaseNotif`

**•** `sales_channel__NotificationsSubflow`

**•** `sales_channel__OpptyChgNotif`

**•** `sales_channel__OpptyCloseDateNotif`

**•** `sales_channel__OpptyCreateMatchAct`

**•** `sales_channel__OpptyNextStepNotif`

**•** `sales_channel__OpptyStageNotChgNotif`

**•** `sales_channel__SelectFeaturedChannels`

**•** `sales_channel__SetupBroadcastChannel`

**•** `sales_channel__filter_users`

**•** `sales_channel__get_single_user`

**•** `sales_channel__invite_to_channel`

**•** `sales_channel__slack_sales_AccountRoom`

**•** `sales_channel__slack_sales_DealRoom`

**•** `setup_bot__IntroBotAddCaseComment`

**•** `setup_bot__IntroBotCreateCase`

**•** `setup_bot__IntroBotCreateLead`

**•** `setup_bot__IntroBotLookupCase`

**•** `setup_bot__IntroBotPreChatContext`

**•** `setup_order_bot__IntroBotLookupOrder`

**•** `setup_service_experience__Create_Case`

**•** `setup_service_experience__Reset_Pwd`

**•** `setup_service_experience__Verify_Cust`

```
ScreenFlowInputs

```

**Type**
textarea

**Properties**
Nillable

**Description**
The input parameters required by the screen flow.


Standard Objects FlowOrchestrationWorkItem

**Field** **Details**

```
Status

StepInstanceId

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the work item.

Valid values are:

**•** `Assigned`

**•** `Completed`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow orchestration step associated with the orchestration work item.

This field is a relationship field.

**Relationship Name**
StepInstance

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationStepInstance

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowOrchestrationWorkItemFeed on page 55**
Feed tracking is available for the object.

**FlowOrchestrationWorkItemHistory on page 63**
History is available for tracked fields of the object.

**FlowOrchestrationWorkItemOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowOrchestrationWorkItemShare on page 67**
Sharing is available for the object.


### Standard Objects FlowRecord FlowRecord

Represents the details of a flow. This object is available in API version 58.0 and later.

Supported Calls

`delete()`, `query()`, `update()`

Fields

**Field Name** **Details**

```
ActivationId

ActiveVersionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the marketing segment activation. This field is available in API version
64.0 and later.

This field is a relationship field.

**Relationship Name**
Activation

**Relationship Type**
Lookup

**Refers To**
MarketSegmentActivation

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the active flow version. This field is available in API version 61.0 and
later.

This field is a relationship field.

**Relationship Name**
ActiveVersion

**Relationship Type**
Lookup

**Refers To**
### FlowRecordVersion


Standard Objects FlowRecord

**Field Name** **Details**

```
ApiVersion

AreMetricsLoggedToDataCloud

AssociatedRecordId

Builder

```

**Type**
double

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API version of the flow record. This field is available in API version 61.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value
is false. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record the flow is associated with.

This field is a polymorphic relationship field.

**Relationship Name**
AssociatedRecord

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Valid values are:

**•** `Cloud Flow Designer`

**•** `Flow Builder`

**•** `Swing Designer`

This field is available in API version 61.0 and later.


Standard Objects FlowRecord

**Field Name** **Details**

```
CapacityCategory

Description

ErrorCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the flow.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The error code if the flow element run encountered an error. Valid values are:

**•** `ACTIVATING_USER_ACCOUNT_DEACTIVATED` —We can't run this
flow because the user who activated it has a deactivated user record.

**•** `ACTIVATING_USER_LOST_PERMISSIONS` —We can't run this flow
because the user that activated it no longer has permission to it.

**•** `CANNOT_PUBLISH_SEGMENT` —We can't run this flow because we can't
publish the segment it's using. Contact Salesforce Customer Support and
ask for help with the error ID.

**•** `CANNOT_QUERY_SEGMENT_MEMBER_DATA` —We can't run this flow
because we can't query the segment membership data it's using. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_RUN_ACTIVATION_TRIGGERED_FLOW` —Something went
wrong with your automation. Contact Salesforce Customer Support and ask
for help with the error ID.

**•** `CANNOT_REFRESH_DATA_STREAM` —We can't run this flow because
we can't refresh your data stream metadata. Contact Salesforce Customer
Support and ask for help with the error ID.

**•** `CANNOT_REFRESH_IDENTITY_RES_DATA` —We can't run this flow
because we can't refresh your identity resolution data. Contact Salesforce
Customer Support and ask for help with the error ID.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `CANNOT_REFRESH_IDENTITY_RES_METADATA` —We can't run this
flow because we can't refresh your identity resolution metadata. Contact
Salesforce Customer Support and ask for help with the error ID.

**•** `CANNOT_UPDATE_DATASTREAM_METADATA` —We can't run this flow
because we can't update your DataStream metadata. Contact Salesforce
Customer Support and ask for help with the error ID.

**•** `CREATE_EXPERIMENT_ERROR` —We can't run this flow because an
error occurred while executing the Path Experiment element. To try again,
save and activate a new version of the flow.

**•** `DATA_ACTION_STATUS_ERROR` —We can’t run this flow because we
couldn’t create the data action. To try again, save and activate a new version
of the flow.

**•** `FLOW_FAILED_TO_START` —This flow failed to start. Contact Salesforce
Customer Support and ask for help with the error ID.

This field is available in API version 59.0 and later.

```
ErrorDetails

FlowCategory

FlowDefinition

FlowSubcategory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error ID. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a category. Sharing rules assign permissions to view and edit
flows by category and subcategory. This field is available in API version 60.0 and
later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the flow definition.

**Type**
string


Standard Objects FlowRecord

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The API name of a subcategory. Sharing rules assign permissions to view and
edit flows by category and subcategory. This field is available in API version 60.0
and later.

```
FlowType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The label of a flow type. `FlowType` consolidates `ProcessType` and
`TriggerType` into one field. `FlowType` is used with permissions, so admins
can control access to each flow type. Valid values are:

**•** `Action Cadence Step Screen Flow` —Launches from a cadence
step. This type of flow collects or displays information and requires user
interaction.

**•** `Action Plan Autolaunched Flow` —Launches an action plan
task from an action plan when conditions in the associated action plan
template process are met. This type of flow runs in the background without
user interaction.

**•** `Activity-Object Matching No Trigger Flow` —Launches
when Einstein Activity Capture detects and captures a new activity, such as
an email. This type of flow runs in the background without user interaction.
Requires Sync Email as Salesforce Activity to be enabled.

**•** `Activation-Triggered Autolaunched Flow` —Launches
when an activation is published. This type of flow runs in the background
without user interaction.

**•** `Admin Automation Event-Triggered Flow` —Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction.

**•** `Autolaunched Approval Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An approval
orchestration lets you create a multi-step, multi-user approval process.

**•** `Autolaunched No Trigger Flow` —Launches when invoked by
processes or code such as Apex and REST API. This type of flow runs in the
background without user interaction.

**•** `Autolaunched No Trigger Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An orchestration
lets you create a multi-step, multi-user process.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Automation Event-Triggered Autolaunched`
`Flow` —Launches when invoked by Apex, processes, REST API, and more.
This type of flow runs in the background without user interaction.

**•** `Automation Event-Triggered Flow` —Launches when a user
performs an automation event, like subscribing to SMS messages. This type
of flow runs in the background without user interaction.

**•** `Automation Event-Triggered Flow v0` —Deprecated. Launches
when a user performs an automation event, like subscribing to SMS messages.
This type of flow runs in the background without user interaction.

**•** `Cart Async Autolaunched Flow` —Launches when invoked by
a cart change, such as an Add to Cart. This type of flow runs in the background
without user interaction.

**•** `Checkout Screen Flow` —Create a screen flow that implements a
Commerce Cloud checkout process. This type of flow collects or displays
information and requires user interaction.

**•** `CMS Workflow Orchestration Autolaunched` —Launches
when invoked from the Workflows component in a CMS workspace. This
type of orchestration lets you create a multi-step, multi-user process to create,
edit, organize, and manage digital content from a centralized location.

**•** `Contact Request Screen Flow` —Launches when invoked by a
customer, allowing them to enter contact details into a self-service form. This
type of flow collects or displays information and requires user interaction.

**•** `Customer Lifecycle Record-Triggered After Save`
`Flow` —Launches after a customer lifecycle map is saved and changes
records related to the triggering record. This type of flow runs in the
background without user interaction.

**•** `Data Cloud Data Change Flow` —Launches when a record from
a Data Cloud data model object or a calculated insight object is changed and
meets the specified conditions. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Autolaunched Flow` —Launches
when invoked by Apex, processes, REST API, and more. This type of flow runs
in the background without user interaction.

**•** `Data Graph-Triggered Flow` —Launches when invoked by Apex,
processes, REST API, and more. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Flow v0` —Deprecated. Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction.

**•** `Digital Form Screen Flow` —Launches from app extensions. This
type of flow collects or displays information and requires user interaction.

**•** `Discovery Framework Data Capture Screen Flow`
`(Beta)` —Launches when invoked by a user on a mobile device and


Standard Objects FlowRecord

**Field Name** **Details**

presents assessment questions from Discovery Framework. This type of flow
collects or displays information and requires user interaction.

**•** `Employee Service Catalog Item Screen Flow` —Launches
when invoked by a user and allows them to browse and order items from
the Employee Service Catalog. This type of flow collects or displays information
and requires user interaction.

**•** `Evaluation Autolaunched Flow` —Launches when invoked by
an orchestration to evaluate custom criteria for a stage or step. To indicate
that the criteria are met, set the output variable
`isOrchestrationConditionMet` to `true` . This type of flow runs
in the background without user interaction.

**•** `External System Change-Triggered Flow` —Launches when
an event is received from an external system. This type of flow runs in the
background without user interaction.

**•** `Event-Driven Flow` —Launches when an event is received. This type
of flow runs in the background without user interaction.

**•** `Field Service Mobile Screen Flow` —Launches when invoked
by a user in the Field Service mobile app. This type of flow collects or displays
information and requires user interaction.

**•** `Field Service Web Screen Flow` —Launches from the Field
Service app and lets users schedule, modify, or cancel an appointment in a
web browser. This type of flow requires user interaction.

**•** `Form-Triggered Autolaunched Flow` —Launches when a web
visitor submits a marketing form. This type of flow runs in the background
without user interaction.

**•** `Form-Triggered Flow` —Launches when a web visitor submits a
marketing form. This type of flow runs in the background without user
interaction.

**•** `Form-Triggered Flow v0` —Deprecated. Launches when a web
visitor submits a marketing form. This type of flow runs in the background
without user interaction.

**•** `Identity User Registration Flow` —Launches when a user
logs in via a single sign-on process that uses the authentication provider
framework. After the third-party identity provider authenticates the user, the
flow creates a user or updates an existing user. This type of flow runs in the
background without user interaction.

**•** `Indicator Result Screen Flow` —Launches a screen flow when
initiated by a user to calculate and create indicator results for a selected
indicator performance period.

**•** `Individual-Object Linking Screen Flow` —Launches when
invoked by an agent to link a record like a case or messaging session to a
contact, lead, person account, or employee. This type of flow collects or
displays information and requires user interaction.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Login Screen Flow` —Launches when a user tries to log in to
Salesforce. This type of flow extends Salesforce's default authentication
process by sending users with certain profiles through a flow when they log
in and requires user interaction.

**•** `Loyalty Management Autolaunched Flow` —Launches when
invoked by a loyalty program process, and contains Assignment, Decision,
and Action elements. The Action element in this type of flow supports Apex
and quick actions. This type of flow runs in the background without user
interaction.

**•** `Managed Content Autolaunched Flow` —Launches when
invoked by the ManagedContentRelease translator. This type of flow runs in
the background without user interaction.

**•** `Mortgage Lending Screen Flow` —Launches when invoked by
a user and allows them to provide Financial Service Cloud mortgage
application details. This type of flow requires user interaction.

**•** `Platform Event Triggered Flow` —Launches when a platform
event occurs. This type of flow runs in the background without user
interaction.

**•** `Process Builder Autolaunched Process` —Launched when
invoked from a Process Builder process. This type of flow runs in the
background without user interaction.

**•** `Process Builder Custom Event Process` —A process created
in Process Builder that launches when a custom event message is received.
This type of process runs in the background without user interaction.

**•** `Process Builder Workflow` —Launches when a record is created
or updated. This type of process runs in the background without user
interaction.

**•** `Prompt Template Capability-Triggered Flow` —Launches
from a prompt template. This type of flow adds prompt instructions to the
associated prompt template and runs in the background without user
interaction.

**•** `Recommendation Strategy Autolaunched Flow` —Build a
personalized list of recommendations. When a recommendation is selected,
it launches its assigned flow. Used by Einstein Next Best Action. Show
recommendations in Lightning App Builder with the Einstein Next Best Action
component and in Experience Builder with the Suggested Actions component.

**•** `Record-Triggered After Save Flow` —Launches after a record
is created or updated and has been saved. This type of flow can make changes
only to records related to the triggering record and runs in the background
without user interaction.

**•** `Record-Triggered After Save Approval`
`Orchestration` —Launches when a record is created or updated. An
approval orchestration lets you create a multi-step, multi-user approval
process.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered Before Delete Flow` —Launches when a
record is deleted. This type of flow runs in the background without user
interaction.

**•** `Record-Triggered Before Save Flow` —Launches after a record
is created or updated, but hasn't been saved. This type of flow can make
changes only to the triggering record and runs in the background without
user interaction.

**•** `Routing Autolaunched Flow` —Launches when a customer initiates
a chat, voice, or messaging conversation and routes the work item to a queue,
skill, agent, or bot. This type of flow runs in the background without user
interaction.

**•** `Schedule-Triggered Flow` —Launches at a specified time and
frequency for each record that meets the flow criteria. This type of flow runs
in the background without user interaction.

**•** `Scheduler Appointments Screen Flow` —Launches when
invoked by a user and lets them schedule appointments in Salesforce
Scheduler. This type of flow collects or displays information and requires user
interaction.

**•** `Screen Flow` —Launches from Lightning pages, Experience Cloud sites,
quick actions and more. This type of flow collects or displays information and
requires user interaction.

**•** `Segment-Triggered Autolaunched Flow` —Launches when
activated or when scheduled for qualified Data Cloud segment members.
This type of flow runs in the background without user interaction.

**•** `Segment-Triggered Flow` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction.

**•** `Segment-Triggered Flow v0` —Deprecated. Launches when
activated or when scheduled for qualified Data Cloud segment members.
This type of flow runs in the background without user interaction.

**•** `Stage Management Evaluation Autolaunched`
`Flow` —Launches when invoked by a stage transition in Stage Management
to evaluate custom criteria for a stage or step. To indicate that the criteria are
met, set the output variable isCriteriaMet to True.

**•** `Survey Enrich Autolaunched Flow` —Launches in the context
of a survey response and can't execute without a corresponding survey. Use
it to conditionally map a response to a record, create records, or send
notifications. This type of flow runs in the background without user
interaction.


Standard Objects FlowRecord

**Field Name** **Details**

**•** `Survey Screen Flow` —Launches when invoked by an internal or
external survey participant. This type of flow saves participant feedback as
survey response records and requires user interaction.

**•** `Transaction Security Autolaunched Flow` —Used by
Condition Builder to declaratively build customized security policies to protect
data. This type of flow runs in the background without user interaction.

**•** `User Provisioning Screen Flow` —Launches when invoked by
a user and allows them to create a user account and link it to a third-party
service or app. This type of flow requires user interaction.

This field is available in API version 60.0 and later.

```
Id

IsLightningAppEnabled

IsOverridable

IsPaused

```

**Type**
text

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s flow type has been enabled in Lightning Experience
apps. The default value is `false` . This field is available in API version 61.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is overridable. The default value is
`false` . This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment-triggered flow is paused ( `true` ) or not ( `false` ).
When the value is `true`, no additional records are processed until the flow is


Standard Objects FlowRecord

**Field Name** **Details**

resumed. The default value is `false` . This field is available in API version 60.0
and later.

```
IsTemplate

LogsEnabledFlowVersion

Manageable State

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is a template. Template flow record
versions are automatically shared with all users in your Salesforce org. The default
value is `false` . This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the flow that enabled persistent logging. This field is
available in API version 66.0 and later.

**Type**
boolean

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates the manageable state of the flow record that is contained in a package.
Valid values are:

**•** beta

**•** deleted

**•** deprecated

**•** deprecatedEditable

**•** installed

**•** installedEditable

**•** released

**•** unmanaged

This field is available in API version 60.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects FlowRecord

**Field Name** **Details**

**Description**
The label of the flow.

```
NamespacePrefix

OverriddenById

OverriddenFlowId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the flow record. This field is available in
API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that’s overriding the current flow. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that the current flow is overriding. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowRecord


Standard Objects FlowRecord

**Field Name** **Details**

```
OwnerId

ProgressStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the user who owns the flow.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The progress status of the flow. Valid values are:

**•** `Canceled`  - Indicates a flow that has been deactivated by a user who
doesn’t process previously added records. No additional records are added
to this flow.

**•** `Completed`  - Indicates a flow that is complete. No additional records are
eligible to be processed in this flow.

**•** `Draft` —Indicates a flow that is under construction and isn’t active yet. This
status can be invalid because it needs additional information before it can
be activated by the user.

**•** `Error` —Indicates a flow that has been deactivated because it encountered
an error. When the error occurs, the error details are emailed to up to 5 users
with the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`  - Indicates a flow that has been deactivated by a user, but is
finishing previously added records that are eligible to run to completion. No
additional records are added to this flow.

**•** `InProgress`  - Indicates a flow that is running or ready to run.

**•** `PreparingData`  - Indicates a flow that is preparing the necessary data
to run. This process can take up to 2 hours.

**•** `Scheduled`  - Indicates a flow scheduled to start on the date and time
selected by the user.

**•** `UnderReview` —Indicates a flow that is under review before it is activated.
This value is available in API version 64.0 and later.


Standard Objects FlowRecord

**Field Name** **Details**

```
ScheduledStartDate

SegmentId

SourceTemplateId

TriggerObjectOrEventLabel

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow is scheduled to start.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the segment used in the flow.

This field is a relationship field.

**Relationship Name**
Segment

**Relationship Type**
Lookup

**Refers To**
MarketSegment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template from which the current flow was created. This field is
available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowRecord

**Field Name** **Details**

**Description**
The label of the object or platform event that triggers this flow. This field is
available in API version 61.0 and later.

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The trigger type of the flow. Specifies what causes the flow to run. Valid values
are:

**•** `Activation` —The flow starts when an activation is published. This type
of flow runs in the background without user interaction. This value is available
in API version 64.0 and later.

**•** `AdminAutomationEvent` —The flow starts when an automation event
is received. This type of flow runs in the background without user interaction.
This value is available in API version 64.0 and later.

**•** `Automation Event` —The flow starts when an automation event such
as an SMS subscription occurs. This value is available in API version 62.0 and
later.

**•** `Capability` —The flow starts when the specified capability that the flow
integrates with is invoked. This value is available in API version 60.0 and later.

**•** `DataCloudDataChange` —The flow starts when data model object
(DMO) or calculated insight object (CIO) conditions are met. This value is
available in API version 59.0 and later.

**•** `DataGraphDataChange` —The flow starts when conditions are met in
the specified data graph field. This value is available in API version 63.0 and
later.

**•** `EventDrivenJourney` —Reserved for internal use.

**•** `ExternalSystemChange` —The flow starts when an external system
change event is received. This value is available in API version 61.0 and later.

**•** `FormSubmissionEvent` —The flow runs when a user submits data via
a webform. In Flow Builder, this value corresponds to `Form` . This value is
available in API version 60.0 and later.

**•** `PlatformEvent` —The flow starts when a platform event message is
received. This value is available in API version 49.0 and later.

**•** `RecordAfterSave` —The flow starts after a record is saved. This value
is available in API version 49.0 and later.

**•** `RecordBeforeDelete` —Deleting a record triggers an autolaunched
flow before the record is deleted from the database. This value is available
in API version 50.0 and later.


### Standard Objects FlowRecordElement

**Field Name** **Details**

**•** `RecordBeforeSave` —Creating and/or updating a record triggers an
autolaunched flow to make additional updates to that record before it's saved
to the database. This value is available in API version 48.0 and later.

**•** `Scheduled` —The flow starts at the scheduled time. This value is available
in API version 47.0 and later.

**•** `Segment` —The flow runs at the scheduled time of a segment.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**FlowRecordChangeEvent (API version 62.0)**
Change events are available for the object.

**FlowRecordOwnerSharingRule**

Sharing rules are available for the object.

**FlowRecordShare**

Sharing is available for the object.

### FlowRecordElement

Represents a single element within a flow version. This object is available in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ElementName

FlowRecordVersionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow element.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects FlowRecordElementOccurrence

**Field Name** **Details**

**Description**
The ID of the flow version the flow element is part of.

This field is a relationship field.

**Relationship Name**
FlowRecordVersion

**Relationship Type**
Master-detail

**Refers To**
FlowRecordVersion (the master object)

```
LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow element was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the flow element was last viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The label of the flow element.

**FlowRecordElementChangeEvent (API version 62.0)**
Change events are available for the object.

### FlowRecordElementOccurrence

Represents the execution metrics for a single element within a flow version. This object is available in API version 62.0 and later.


Standard Objects FlowRecordElementOccurrence

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Fields

**Field** **Details**

```
CurrencyIsoCode

Entries

Errors

Exits

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency associated with the flow.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was initiated in all flow interviews after the flow version
was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of errors for the element in all flow interviews after the flow version was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was executed to completion in all flow interviews after
the flow version was executed.


Standard Objects FlowRecordElementOccurrence

**Field** **Details**

```
FlowRecordElementId

FlowRecordId

FlowRecordVersionId

FlowRecordVersionOccurrenceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow element.

This field is a relationship field.

**Relationship Name**
FlowRecordElement

**Refers To**
FlowRecordElement

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow.

This field is a relationship field.

**Relationship Name**
FlowRecord

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version.

This field is a relationship field.

**Relationship Name**
FlowRecordVersion

**Refers To**
FlowRecordVersion

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects FlowRecordElementOccurrence

**Field** **Details**

**Description**
The ID of the flow occurrence.

This field is a relationship field.

**Relationship Name**
FlowRecordVersionOccurrence

**Relationship Type**
Master-detail

**Refers To**
FlowRecordVersionOccurrence (the master object)

```
Name

Stopped

TotalDuration

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the flow element.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times execution of the element was stopped in all flow interviews after the
flow version was executed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total time in milliseconds spent executing the element in all flow interviews.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowRecordElementOccurrenceChangeEvent on page 68**
Change events are available for the object.

**FlowRecordElementOccurrenceFeed on page 55**
Feed tracking is available for the object.


### Standard Objects FlowRecordRelation

**FlowRecordElementOccurrenceHistory on page 63**
History is available for tracked fields of the object.

**FlowRecordElementOccurrenceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FlowRecordElementOccurrenceShare on page 67**
Sharing is available for the object.

### FlowRecordRelation

Represents a relationship between a record and a flow interview. When a flow interview is paused, Salesforce uses the $Flow.CurrentRecord
global variable in the flow to associate the interview with a record. Available in API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

ParentId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview


Standard Objects FlowRecordRelation

**Field Name** **Details**

```
RelatedRecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that the flow interview is related to. Make sure that this field contains
only one ID, and that the ID is for a valid object.

Custom objects and most standard objects are supported.

This is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, AccountContactRole, AccountPartner, Accreditation, ActivationTarget,
ActivationTrgtIntOrgAccess, Address, AlternativePaymentMethod, Announcement,
ApexTestQueueItem, AppAnalyticsQueryRequest, AppUsageAssignment,
AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, AssociatedLocation, AsyncApexJob, Attachment,
AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, Award, BackgroundOperation, BoardCertification,
BusinessLicense, BusinessMilestone, BusinessProfile, CalendarView, Campaign,
CampaignMember, CardPaymentMethod, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth,
CarePreauthItem, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct,
CareProgramProvider, CareProgramTeamMember, CareProviderAdverseAction,
CareProviderFacilitySpecialty, CareProviderSearchableField, CareRegisteredDevice,
CareRequest, CareRequestDrug, CareRequestExtension, CareRequestItem,
CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CaseContactRole,
CaseSolution, CodeSet, CodeSetBundle, CollaborationGroup,
CollaborationGroupMember, CollaborationGroupMemberRequest,
CollaborationGroupRecord, CollaborationInvitation, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConferenceNumber, ConsumptionRate,
ConsumptionSchedule, Contact, ContactEncounter, ContactEncounterParticipant,
ContactPointAddress, ContactPointConsent, ContactPointEmail,
ContactPointPhone, ContactPointTypeConsent, ContactRequest,
ContentDistribution, ContentDocument, ContentDocumentLink,
ContentDocumentSubscription, ContentFolder, ContentFolderLink,


Standard Objects FlowRecordRelation

**Field Name** **Details**

ContentFolderMember, ContentNotification, ContentVersion,
ContentVersionComment, ContentVersionRating, ContentWorkspaceDoc,
Contract, ContractContactRole, ConversationEntry, CoverageBenefit,
CoverageBenefitItem, CreditMemo, CreditMemoLine, Dashboard,
DashboardComponent, DataAssessmentFieldMetric, DataAssessmentMetric,
DataAssessmentValueMetric, DataStream, DataUseLegalBasis, DataUsePurpose,
DelegatedAccount, DeleteEvent, DialerCallUsage, DigitalSignature, DigitalWallet,
Document, DocumentChecklistItem, DuplicateRecordItem, DuplicateRecordSet,
EmailMessage, EmailMessageRelation, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, EntitySubscription, Event,
EventRelation, ExternalEvent, ExternalEventMapping, FeedAttachment,
FeedComment, FeedItem, FeedPollChoice, FeedPollVote, FeedRevision,
FileSearchActivity, FlowInterviewLog, FlowInterviewLogEntry, FlowStageRelation,
HealthCareDiagnosis, HealthCareProcedure, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Idea, Identifier, IdentityDocument, Image, Individual,
IndividualApplication, InstalledMobileApp, Invoice, InvoiceLine, Lead, ListEmail,
ListEmailIndividualRecipient, ListEmailRecipientSource, Location,
LocationTrustMeasure, MarketSegment, MarketSegmentActivation,
MatchingInformation, MemberPlan, MessagingDeliveryError, MessagingEndUser,
MktCalculatedInsight, MktSgmntActvtnAudAttribute,
MktSgmntActvtnContactPoint, Note, OperatingHours, Opportunity,
OpportunityContactRole, OpportunityLineItem, OpportunityPartner, Order,
OrderItem, OrgMetric, OrgMetricScanResult, OrgMetricScanSummary,
OtherComponentTask, Partner, PartyConsent, Payment, PaymentAuthAdjustment,
PaymentAuthorization, PaymentGateway, PaymentGatewayLog, PaymentGroup,
PaymentLineInvoice, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Pricebook2, PricebookEntry,
ProcessException, ProcessInstance, ProcessInstanceNode, Product2,
ProductConsumptionSchedule, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, PromptAction, ProviderSearchSyncLog, PurchaserPlan,
PurchaserPlanAssn, PushTopic, QuickText, QuickTextUsage, ReceivedDocument,
Recommendation, RecordAction, Refund, RefundLinePayment, ReplyText, Report,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderItemAdjustment,
ReturnOrderItemTax, ReturnOrderLineItem, SearchPromotionRule,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SetupAssistantStep,
SharingRecordCollection, SharingRecordCollectionItem,
SharingRecordCollectionMember, Shift, Shipment, ShipmentItem,
SkillRequirement, SocialPersona, SocialPost, Solution, StreamingChannel, Task,
ThreatDetectionFeedback, TimeSlot, TodayGoal, Topic, TopicAssignment,
UnitOfMeasure, UserAppInfo, UserAppMenuCustomization,
UserEmailPreferredPerson, UserProvAccount, UserProvAccountStaging,
UserProvMockTarget, UserProvisioningLog, UserProvisioningRequest, VideoCall,


### Standard Objects FlowRecordVersion

**Field Name** **Details**

VideoCallParticipant, VideoCallRecording, Visit, VisitedParty, Visitor, VoiceCall,
VoiceCallRecording, VoiceVendorLine, VolunteerProject, WaveAutoInstallRequest,
WaveCompatibilityCheckItem, WorkAccess, WorkBadge, WorkBadgeDefinition,
WorkOrder, WorkOrderLineItem, WorkThanks, WorkType, WorkTypeGroup,
WorkTypeGroupMember

### FlowRecordVersion

Represents the version of a flow. This object is available in API version 58.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Fields

**Field Name** **Details**

```
ActivatedById

ActivatedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that activated the flow. This field is available in API version 60.0
and later.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow was activated. This field is available in API
version 60.0 and later.


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
ApiVersion

AreMetricsLoggedToDataCloud

Builder

CapacityCategory

DataSpaceId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version of the flow record version. This field is available in API version
61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value
is false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the tool that created this flow. Valid values are:

**•** `Cloud Flow Designer`

**•** `Flow Builder`

**•** `Swing Designer`

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Description**
The ID of the data space for this flow record version. This field is available in API
version 65.0 and later.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Description

Entries

Errors

Exits

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow record version. This field is available in API version
61.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of entries in this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of errors in this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Description**
The number of exits from this flow. To use this field, your org must use Salesforce
Enterprise and Unlimited Editions with Marketing Cloud Growth Edition. This
field is available in API version 60.0 and later.

```
FlowRecordId

FlowType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent flow running this version.

This field is a relationship field.

**Relationship Name**
FlowRecord

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The label of a flow type. `FlowType` consolidates `ProcessType` and
`TriggerType` into one field. `FlowType` is used with permissions, so admins
can control access to each flow type. Valid values are:

**•** `Action Cadence Step Screen Flow` —Launches from a cadence
step. This type of flow collects or displays information and requires user
interaction.

**•** `Activation-Triggered Autolaunched Flow` —Launches
when an activation is published. This type of flow runs in the background
without user interaction. This value is available in API version 64.0 and later.

**•** `Action Plan Autolaunched Flow` —Launches an action plan
task from an action plan when conditions in the associated action plan
template process are met. This type of flow runs in the background without
user interaction.

**•** `Admin Automation Event-Triggered Flow` —Launches when
invoked by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction. This value is available in API version
64.0 and later.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Agentic Guided Experience Background Flow` —Creates,
retrieves, updates, or deletes records. This autolaunched flow runs in the
background. This value is available in API version 65.0 and later.

**•** `Agentic Guided Experience Orchestration`
`Flow` —Launches when a mobile worker invokes it from the Field Service
mobile app. With Agentic Guided Experience, configure the mobile experience
to follow a tailored work completion process. This value is available in API
version 65.0 and later.

**•** `Agentic Guided Experience Screen Data Flow` —Retrieve
records for use throughout AGX Screen and AGX Orchestration flows. This
autolaunched flow runs in the background. This value is available in API
version 65.0 and later.

**•** `Agentic Guided Experience Screen Flow` —A screen flow
that can launch from an interactive step on an AGX orchestration flow. This
value is available in API version 65.0 and later.

**•** `Autolaunched Approval Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An approval
orchestration lets you create a multi-step, multi-user approval process.

**•** `Autolaunched No Trigger Flow` —Launches when invoked by
processes or code such as Apex and REST API. This type of flow runs in the
background without user interaction.

**•** `Autolaunched No Trigger Orchestration` —Launches when
invoked by Apex, REST API, custom buttons, or custom links. An orchestration
lets you create a multi-step, multi-user process.

**•** `Automation Event-Triggered Flow` —Launches when invoked
by Apex, processes, REST API, and more. This type of flow runs in the
background without user interaction. This value is available in API version
64.0 and later.

**•** `Automation Event-Triggered Flow` —Launches when an
automation event is received. This type of flow runs in the background
without user interaction.

**•** `Broadcast Flow` —Launches when referenced by Apex, REST API, or
subflow element. This value is available in API version 65.0 and later.

**•** `Cart Async Autolaunched Flow` —Launches when invoked by
a cart change, such as an Add to Cart. This type of flow runs in the background
without user interaction.

**•** `Checkout Screen Flow` —Create a screen flow that implements a
Commerce Cloud checkout process. This type of flow collects or displays
information and requires user interaction.

**•** `CMS Workflow Orchestration Autolaunched` —Launches
when invoked from the Workflows component in a CMS workspace. This
type of orchestration lets you create a multi-step, multi-user process to create,
edit, organize, and manage digital content from a centralized location.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Contact Request Screen Flow` —Launches when invoked by a
customer, allowing them to enter contact details into a self-service form. This
type of flow collects or displays information and requires user interaction.

**•** `Customer Lifecycle Record-Triggered After Save`
`Flow` —Launches after a customer lifecycle map is saved and changes
records related to the triggering record. This type of flow runs in the
background without user interaction.

**•** `Data Cloud Data Change Flow` —Launches when a record from
a Data Cloud data model object or a calculated insight object is changed and
meets the specified conditions. This type of flow runs in the background
without user interaction.

**•** `Data Graph-Triggered Flow` —Launches when conditions are
met in the specified data graph field. This type of flow runs in the background
without user interaction. This value is available in API version 64.0 and later.

**•** `Data Graph-Triggered Flow v0` —Launches when conditions
are met in the specified data graph field. This type of flow runs in the
background without user interaction.

**•** `Digital Form Screen Flow` —Launches from app extensions. This
type of flow collects or displays information and requires user interaction.

**•** `Discovery Framework Data Capture Screen Flow`
`(Beta)` —Launches when invoked by a user on a mobile device and
presents assessment questions from Discovery Framework. This type of flow
collects or displays information and requires user interaction.

**•** `Employee Service Catalog Item Screen Flow` —Launches
when invoked by a user and allows them to browse and order items from
the Employee Service Catalog. This type of flow collects or displays information
and requires user interaction.

**•** `Evaluation Autolaunched Flow` —Launches when invoked by
an orchestration to evaluate custom criteria for a stage or step. To indicate
that the criteria are met, set the output variable
`isOrchestrationConditionMet` to `true` . This type of flow runs
in the background without user interaction.

**•** `External System Change-Triggered Flow Approval`
`Process` —Launches when data changes in a supported external system.
A flow approval process lets you create a multi-step, multi-user approval
process. This value is available in API version 65.0 and later.

**•** `External System Change-Triggered`
`Orchestration` —Launches when data changes in a supported external
system. An orchestration lets you create a multi-step, multi-user process. This
value is available in API version 65.0 and later.

**•** `External System Change-Triggered Flow` —Launches when
an event is received from an external system. This type of flow runs in the
background without user interaction.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Event-Driven Flow` —Launches when an event is received. This type
of flow runs in the background without user interaction.

**•** `Field Service Mobile Screen Flow` —Launches when invoked
by a user in the Field Service mobile app. This type of flow collects or displays
information and requires user interaction.

**•** `Field Service Web Screen Flow` —Launches from the Field
Service app and lets users schedule, modify, or cancel an appointment in a
web browser. This type of flow requires user interaction.

**•** `Form-Triggered Flow` —Launches when a web visitor submits a
marketing form. This type of flow runs in the background without user
interaction. This value is available in API version 64.0 and later.

**•** `Form-Triggered Flow v0` —Launches when a web visitor submits
a marketing form. This type of flow runs in the background without user
interaction.

**•** `Identity User Registration Autolaunched`
`Flow` —Launches when a user logs in via a single sign-on process that uses
the authentication provider framework. After the third-party identity provider
authenticates the user, the flow creates a user or updates an existing user.
This type of flow runs in the background without user interaction. This value
is available in API version 64.0 and later.

**•** `Indicator Result Screen Flow` —Launches a screen flow when
initiated by a user to calculate and create indicator results for a selected
indicator performance period.

**•** `Individual-Object Linking Screen Flow` —Launches when
invoked by an agent to link a record like a case or messaging session to a
contact, lead, person account, or employee. This type of flow collects or
displays information and requires user interaction.

**•** `Login Screen Flow` —Launches when a user tries to log in to
Salesforce. This type of flow extends Salesforce's default authentication
process by sending users with certain profiles through a flow when they log
in and requires user interaction.

**•** `Loyalty Management Autolaunched Flow` —Launches when
invoked by a loyalty program process, and contains Assignment, Decision,
and Action elements. The Action element in this type of flow supports Apex
and quick actions. This type of flow runs in the background without user
interaction.

**•** `Managed Content Autolaunched Flow` —Launches when
invoked by the ManagedContentRelease translator. This type of flow runs in
the background without user interaction.

**•** `Mortgage Lending Screen Flow` —Launches when invoked by
a user and allows them to provide Financial Service Cloud mortgage
application details. This type of flow requires user interaction.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `On-Demand Flow` —Launches when referenced by the REST API. This
autolaunched flow runs asynchronously in the background. This value is
available in API version 65.0 and later.

**•** `Platform Event Triggered Flow` —Launches when a platform
event occurs. This type of flow runs in the background without user
interaction.

**•** `Process Builder Autolaunched Process` —Launched when
invoked from a Process Builder process. This type of flow runs in the
background without user interaction.

**•** `Process Builder Custom Event Process` —A process created
in Process Builder that launches when a custom event message is received.
This type of process runs in the background without user interaction.

**•** `Process Builder Workflow` —Launches when a record is created
or updated. This type of process runs in the background without user
interaction.

**•** `Prompt Template Capability-Triggered Flow` —Launches
from a prompt template. This type of flow adds prompt instructions to the
associated prompt template and runs in the background without user
interaction.

**•** `Recommendation Strategy Autolaunched Flow` —Build a
personalized list of recommendations. When a recommendation is selected,
it launches its assigned flow. Used by Einstein Next Best Action. Show
recommendations in Lightning App Builder with the Einstein Next Best Action
component and in Experience Builder with the Suggested Actions component.

**•** `Record-Triggered After Save Flow` —Launches after a record
is created or updated and has been saved. This type of flow can make changes
only to records related to the triggering record and runs in the background
without user interaction.

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered After Save Orchestration` —Launches
when a record is created or updated. An orchestration lets you create a
multi-step, multi-user process. This type of flow runs in the background
without user interaction.

**•** `Record-Triggered Before Delete Flow` —Launches when a
record is deleted. This type of flow runs in the background without user
interaction.

**•** `Record-Triggered Before Save Flow` —Launches after a record
is created or updated, but hasn't been saved. This type of flow can make
changes only to the triggering record and runs in the background without
user interaction.


Standard Objects FlowRecordVersion

**Field Name** **Details**

**•** `Routing Autolaunched Flow` —Launches when a customer initiates
a chat, voice, or messaging conversation and routes the work item to a queue,
skill, agent, or bot. This type of flow runs in the background without user
interaction.

**•** `Schedule-Triggered Flow` —Launches at a specified time and
frequency for each record that meets the flow criteria. This type of flow runs
in the background without user interaction.

**•** `Scheduler Appointments Screen Flow` —Launches when
invoked by a user and lets them schedule appointments in Salesforce
Scheduler. This type of flow collects or displays information and requires user
interaction.

**•** `Screen Flow` —Launches from Lightning pages, Experience Cloud sites,
quick actions and more. This type of flow collects or displays information and
requires user interaction.

**•** `Segment-Triggered Flow` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction. This value is available in API
version 64.0 and later.

**•** `Segment-Triggered Flow v0` —Launches when activated or when
scheduled for qualified Data Cloud segment members. This type of flow runs
in the background without user interaction.

**•** `Survey Enrich Autolaunched Flow` —Launches in the context
of a survey response and can't execute without a corresponding survey. Use
it to conditionally map a response to a record, create records, or send
notifications. This type of flow runs in the background without user
interaction.

**•** `Survey Screen Flow` —Launches when invoked by an internal or
external survey participant. This type of flow saves participant feedback as
survey response records and requires user interaction.

**•** `Transaction Security Autolaunched Flow` —Used by
Condition Builder to declaratively build customized security policies to protect
data. This type of flow runs in the background without user interaction.

**•** `User Provisioning Screen Flow` —Launches when invoked by
a user and allows them to create a user account and link it to a third-party
service or app. This type of flow requires user interaction.

This field is available in API version 60.0 and later.

```
Id

```

**Type**
text

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow version.


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
IsOverridable

IsPaused

IsTemplate

OverriddenById

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is overridable. The default value is
`false` . This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the segment-triggered flow is paused ( `true` ) or not ( `false` ).
When the value is `true`, no additional records are processed until the flow is
resumed. The default value is `false` . This field is available in API version 60.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow record version is a template. Template flow record
versions are automatically shared with all users in your Salesforce org. The default
value is `false` . This field is available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that’s overriding the current flow. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenBy

**Relationship Type**
Lookup

**Refers To**
FlowRecord


Standard Objects FlowRecordVersion

**Field Name** **Details**

```
OverriddenFlowId

PausedDate

PausingUserId

ProgressStatus

```

**Type**
text

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow that the current flow is overriding. This field is available in API
version 61.0 and later.

This field is a relationship field.

**Relationship Name**
OverriddenFlow

**Relationship Type**
Lookup

**Refers To**
FlowRecord

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the segment-triggered flow was paused. This field is available
in API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who paused the segment-triggered flow. This field is available
in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
PausingUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The running status of the flow. Valid values are:

**•** `Canceled`                       - Specifies a flow that was deactivated by a user. The flow
doesn’t process previously added records and no additional records are added
to this flow.

**•** `Completed`                       - Indicates a flow that is complete. No additional records are
eligible to be processed in this flow.

**•** `Draft`                       - Indicates a flow that is under construction and isn’t active yet.
This status can be invalid because it needs additional information before a
user can activate it.

**•** `Error`                       - Indicates a flow that has been deactivated because it encountered
an error. When the error occurs, the error details are emailed to up to 5 users
with the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`                       - Indicates a flow that was deactivated by a user, but is
finishing records previously added that are eligible to run to completion. No
additional records are added to this flow.

**•** `InProgress`                       - Indicates a flow that is running or ready to run.

**•** `PreparingData`                       - Indicates a flow that is preparing the resources it
requires to run. This process can take up to 2 hours.

**•** `Scheduled`                       - Indicates a flow scheduled to start on the date and time
selected by the user.

```
ReasonPaused

ResumedDate

ResumingUserId

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason the segment-triggered flow was paused. This field is available in API
version 60.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the segment-triggered flow resumed. This field is available in
API version 60.0 and later.

**Type**
reference


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who resumed the segment-triggered flow. This field is available
in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ResumingUser

**Relationship Type**
Lookup

**Refers To**
User

```
RunInMode

ScheduledStartDate

SourceTemplateId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the flow runs in. Valid values are:

**•** `DefaultMode` —The flow record version runs in system or user context,
depending on how the flow is launched.

**•** `SystemModeWithSharing` —The flow record version always runs in
system mode with sharing. The flow respects org-wide default settings, role
hierarchies, sharing rules, manual sharing, teams, and territories. But it doesn’t
respect object permissions, field-level access, or other permissions of the
running user.

**•** `SystemModeWithoutSharing` —The flow record version can access
all data. In the UI, this value appears as System Context without
Sharing—Access All Data. This value is available in API version 49.0 and later.

This field is available in API version 61.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the flow started. This field is available in API version 60.0 and
later.

**Type**
reference


Standard Objects FlowRecordVersion

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the template from which the current flow was created. This field is
available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
SourceTemplate

**Relationship Type**
Lookup

**Refers To**
FlowRecord

```
Status

TriggerObjectOrEventLabel

VersionNumber

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The flow’s status. Valid values are:

**•** `Active`

**•** `Draft`

**•** `InvalidDraft`

**•** `Obsolete`

**•** `UnderReview`  - This value is available in API version 64.0 and later.

This field is available in API version 61.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the object or platform event that triggers this flow. This field is
available in API version 61.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the flow version.


### Standard Objects FlowRecordVersionOccurrence FlowRecordVersionOccurrence

Represents an instance of a recurring flow that runs on a schedule. For example, a flow that runs weekly on Wednesdays creates an
occurrence each time it runs. This object is available in API version 60.0 and later.

Supported Calls

`describe()`, `read()`

Fields

**Field** **Details**

```
DataSpaceId

Entries

Errors

ErrorDetail

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the data space for this occurence. This field is available in API version 65.0
and later.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of entries for this occurrence.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of errors for this occurrence.

**Type**
string


Standard Objects FlowRecordVersionOccurrence

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the error. This field is available in API version 63.0 and later.

```
Exits

FlowRecordId

FlowRecordVersionId

ProgressStatus

```

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of exits for this occurrence.

**Type**
string

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated flow record.

**Type**
string

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated version of the flow record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The running status of the flow interview.

Valid values are:

**•** `Canceled`

Specifies a flow interview that was deactivated by a user. The flow doesn’t process
previously added records and no additional records are added to this flow.

**•** `Completed`

Indicates a flow interview that is complete. No additional records are eligible to
be processed in this flow.

**•** `Error`


### Standard Objects FlowTestResult

**Field** **Details**

Indicates a flow interview that has been deactivated because it encountered an
error. When the error occurs, the error details are emailed to up to 5 users with
the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`

Indicates a flow interview that was deactivated by a user, but is finishing records
previously added that are eligible to run to completion. No additional records are
added to this flow.

**•** `InProgress`

Indicates a flow interview that is running or ready to run.

**•** `PreparingData`

Indicates a flow interview that is preparing the resources it requires to run. This
process can take up to 2 hours.

```
ScheduledDate

Stopped

### FlowTestResult

```

**Type**
dateTime

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The scheduled time and date of the occurrence.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of flows that were stopped for this occurrence.

Represents the results for a flow test associated with a flow version. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To view test run details, you must have the View All Data user permission. You can view flow tests and test results without the View All
Data permission.


Standard Objects FlowTestResult

Fields

**Field** **Details**

```
FlowDefinitionViewId

FlowTestViewId

FlowVersionNumber

FlowVersionViewId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow test associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowTestView

**Relationship Type**
Lookup

**Refers To**
FlowTestView

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number for the flow.

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects FlowTestResult

**Field** **Details**

**Description**
The ID of the flow version associated with the flow test result.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

```
Name

OwnerId

Result

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the flow test result.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns this test result.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the flow test result.

Possible values are:

**•** `Error`

**•** `Fail`


### Standard Objects FlowTestView

**Field** **Details**

**•** `Pass`

```
TestEndDateTime

TestStartDateTime

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the flow test started.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowTestResultShare**

Sharing is available for the object.

### FlowTestView

Represents the description of a flow test associated with a flow definition. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
Description

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the flow test associated with the flow test view.


### Standard Objects FlowStageRelation

**Field** **Details**

```
DurableId

FlowDefinitionViewId

FlowTestApiName

FlowTestLabel

### FlowStageRelation

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow test associated with this flow test view.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test view.

This is a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow test associated with the flow test view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow test associated with the flow test view.

Represents a relationship between a paused flow interview and its stages. When a flow interview is paused, Salesforce creates a
### FlowStageRelation record for each stage that’s set to the $Flow.CurrentStage or $Flow.ActiveStages global variable.

Available in API version 43.0 and later.


Standard Objects FlowStageRelation

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Fields

**Field** **Details**

```
Name

ParentId

StageLabel

StageOrder

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the stage. If the stage is translated, the label respects the language of the user who
is querying the label.

**Type**
int

**Properties**
Filter, Group, Sort


### Standard Objects FlowVariableView

**Field** **Details**

**Description**
The order of this stage when the flow interview was paused. This order may differ from the
order in the stage definition.

**•** If the type is Active, the order corresponds to the order of the stage in
`$Flow.ActiveStages` .

**•** If the type is Current and corresponds to an active stage, the order matches the order of
the active stage.

**•** If the type is Current and doesn't correspond to an active stage, the order is 0.

```
 StageType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of stage. The valid values are:

**•** Current: Identifies that the stage is set to `$Flow.CurrentStage` .

**•** Active: Identifies that the stage is set to `$Flow.ActiveStages` .

You can use the FlowStageRelation records to represent the paused interview and its active and current stages visually.

For example, an Online Purchasing flow interview starts with several stages in $Flow.ActiveStages. If the interview is paused, Salesforce
creates a FlowStageRelation record for each stage in `$Flow.ActiveStages` or `$Flow.CurrentStage` .

### FlowVariableView

Represents a variable within the flow version. This object is available in API version 46.0 and later.


Standard Objects FlowVariableView

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApiName

DataType

Description

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow variable.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data type of the flow variable. Valid values are:

**•** `Apex` —This value is available in API version 46.0 and later.

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —This value is available in API version 30.0 and later.

**•** `Number`

**•** `Multipicklist` —This value is available in API version 34.0 and later.

**•** `Picklist` —This value is available in API version 34.0 and later.

**•** `String`

**•** `sObject`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow variable information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowVariableView

**Field** **Details**

**Description**
The Id of the flow variable.

```
FlowVersionViewId

IsCollection

IsInput

IsOutput

ObjectType

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Id of the flow version.

This is a relationship field.

**Relationship Name**
FlowVersionView

**Relationship Type**
Lookup

**Refers To**
FlowVersionView

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is a collection of values.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicated whether or not the flow variable is available for input.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether or not the flow variable is available for output.

**Type**
string


### Standard Objects FlowVersionView

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the data type is sObject, this field indicates which object.

Usage

### Use this object to query information about flow variables. A query must be filtered by FlowVersionViewId to get results. Only

variables with IsInput or IsOutput marked as true are visible.

### FlowVersionView

Represents the version of a flow definition. This object is available in API version 46.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ApiVersion

ApiVersionRuntime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for the flow definition. Every flow version has an API version specified
at creation.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The API version for running the flow. This value determines which versioned run-time
behavior improvements are adopted by the flow version.

If not specified when the flow or flow version is created, the latest available API version
is used as the API version for running the flow. When an existing flow is saved as a


Standard Objects FlowVersionView

**Field** **Details**

new flow or flow version, the existing flow’s run-time API version is used in the new
flow or flow version.

This field is available in API version 50.0 and later.

```
AreMetricsLoggedToDataCloud

CapabilityType

CapacityCategory

Description

DurableId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this flow’s metrics are logged in Data Cloud. The default value is
false. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The capability that integrates with the flow. An example value is
`PromptTemplateType://SalesEmail` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that determines the usage limits of the flow. Possible values are:

**•** Marketing Cloud Flow

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Flow version information, specified by the org’s admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FlowVersionView

**Field** **Details**

**Description**
The ID of the flow version.

```
FlowDefinitionViewId

IsSwingFlow

IsTemplate

Label

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition.

This field s a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the flow is built with Desktop Flow Designer.

This field is available in API version 49.0 and later.

Default: false

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the process or flow is a template. When installed from managed
packages, processes and flows can’t be viewed or cloned by subscribers because of
intellectual property (IP) protection. But when those processes and flows are templates,
subscribers can open them in a builder, clone them, and customize the clones.
Available in API version 46.0 and later.

Default: false

**Type**
string


Standard Objects FlowVersionView

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow version.

```
ProcessType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable
event orchestration process in the background and automatically executes
different types of actions based on the event type. This value is available in API
version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow executed when a user
completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This
value is available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API
version 44.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein
Activity Capture detects and captures a new activity, such as an email. This type
of flow runs in the background without user interaction. This value is available
with Sync Email as Salesforce Activity in API version 63.0 and later.

**•** `ApprovalWorkflow` —An orchestration for approvals. This value is available
in API version 62.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout
in a store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request that customer
support get back to them. This flow is used to create contact request records.
This value is available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate
survey questions with different stages in customer lifecycles. This value is available
in API version 49.0 and later and only when the Customer Lifecycle Designer
license is enabled.


Standard Objects FlowVersionView

**Field** **Details**

**•** `CustomEvent` —A process that is invoked when it receives a platform event
message. In the UI, it’s an event process. This value is available in API version 41.0
and later.

**•** `DataCaptureFlow` —A flow that configures the Form tab on Work Order
Overview or the related list for a service appointment or a work order line item.
This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents
assessment questions from Discovery Framework. Launches when invoked by a
user on a mobile device. This type of flow collects or displays information, requires
user interaction, and works offline or online. This value is available in API version
62.0 and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value
is available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI
label is Field Service Embedded Flow. This value is available in API version 41.0
and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more
screens or local actions, choices, or dynamic choices. In the UI and Salesforce
Help, it’s a screen flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is
available in API version 46.0 and later.

**•** `FSCLending` —A flow for login. This value is available in API version 51.0 and
later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration
and updates for single sign-on with the authentication provider framework.
Available in API version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates
and creates indicator results for a selected indicator performance period. This
value is available with the Outcome Management license in API version 60.0 and
later.

**•** `IndividualObjectLinkingFlow` —A screen flow that helps search for
contacts, leads, person accounts, and employees and links them to support
interactions. This value is available in API version 58.0 and later.

**•** `InvocableProcess` —A process that can be invoked by another process or
the Invocable Actions resource in REST API. This value is available in API version
38.0 and later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app and
can be invoked by loyalty program processes. This value is available in API version
54.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder
and the flow. This value is available in API version 60.0 and later.

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business
logic. This value is available in API version 52.0 and later.


Standard Objects FlowVersionView

**Field** **Details**

**•** `StageManagementEvaluationFlow` —A flow for evaluating custom
criteria for a stage or step in Stage Management. This value is available in API
version 63.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created
in Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper.
From the UI, this type of flow is created in the Survey Builder and requires an
associated survey flow type. This value is available in API version 49.0 or later and
only when the Customer Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In
the UI and Salesforce Help, it’s a record change process.

These values are reserved for future use.

**•** `ActionCadenceFlow`

**•** `ActionPlan`

**•** `ActivitySmartMatchingFlow`

**•** `AppProcess`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `Journey`

**•** `JourneyBuilderIntegration`

**•** `LoginFlow`

**•** `ManagedContentFlow`

**•** `OrchestrationFlow`

**•** `RecommendationStrategy`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

This value has significant impact on validation when saving the flow and on the flow’s
runtime behavior. Don’t change this value unless you understand the flow properties
of the specified type.

Across flow versions, you can change the type only from `Flow` to
`AutoLaunchedFlow` or vice versa. Before you change the flow type, make sure that
the flow contains only elements, resources, and functionality that the new flow type
supports.

```
RunInMode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mode that the flow runs in. Valid values are:


### Standard Objects Folder

**Field** **Details**

**•** DefaultMode — The flow version runs in system or user context, depending on
how the flow is launched.

**•** SystemModeWithSharing — The flow version always runs in system mode with
sharing. The flow respects org-wide default settings, role hierarchies, sharing
rules, manual sharing, teams, and territories. But it doesn’t respect object
permissions, field-level access, or other permissions of the running user.

```
Status

VersionNumber

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The flow’s status.

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow’s version number.

Use this object to query information about flow versions. A query must be filtered by `DurableId` or `FlowDefinitionViewId`
to get results.

### Folder

Represents a repository for a Dashboard, Document, EmailTemplate, Macro, QuickText, or Report. Only one type of item can be contained
in a folder.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects Folder

Special Access Rules

**•** You must have the “Modify All Data” permission to create, update, or delete document folders and email template folders.

**•** Guest and Customer Portal users can’t access this object.

**•** To query this object, no special permissions are needed.

**•** As of API version 35.0, when a folder is shared with a role, it is only visible to users in that role. Superior roles in the role hierarchy
don’t gain visibility.

**•** If analytics folder sharing is turned on, then users need these permissions to create and manage report folders and dashboard folders:

**–** “ `Create Dashboard Folders` ”

**–** “ `Create Report Folders` ”

**•** To use folders for macros and quick text, enable folders for these objects in Setup on the Macro Settings and Quick Text Settings
pages.

Fields

**Field** **Details**

```
AccessType

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Indicates who can access the Folder. Available values include:

**•** `Hidden` —Folder is hidden from everyone.

**•** `Public` —Folder is accessible by all users.

**•** `Shared` —Folder is accessible only by a User in a particular Group or UserRole. The API
doesn’t allow you to view, insert, or update which group or Role the Folder is shared
with.

Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Folder Unique Name** .


Standard Objects Folder

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
IsReadonly

Name

NamespacePrefix

ParentId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this Folder is read-only ( `true` ) or editable ( `false` ). Label is _`Read`_
_`Only`_ .

Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the folder as it appears in the user interface. Label is **Document Folder Label** .

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
reference


### Standard Objects FolderedContentDocument

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the parent object, if any.

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of objects contained in the Folder. This field can’t be updated. Available values
include:

**•** `Dashboard`

**•** `Document`

**•** `Email` (for Salesforce Classic email templates)

**•** `EmailTemplate` (for Lightning email templates)

**•** `Macro`

**•** `QuickText`

**•** `Report`

Only one type of item can be contained in a folder, either Dashboard, Document, EmailTemplate, Macro, QuickText, or Report.

SEE ALSO:

Overview of Salesforce Objects and Fields

### FolderedContentDocument

Represents the relationship between a parent and child ContentFolderItem in a ContentWorkspace.

Supported Calls

```
describeSObjects()

```


Standard Objects FolderedContentDocument

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentSize

ContentSizeLong

FileExtension

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the ContentDocument that can be in a folder.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for files smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for documents smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the ContentDocument.


Standard Objects FolderedContentDocument

**Field Name** **Details**

```
FileType

IsFolder

ParentContentFolderId

Title

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File type of the ContentDocument.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the FolderedContentDocument is a folder, rather than a file.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the ContentFoldr the ContentDocument resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Name of the file or folder in a ContentFolder.


### Standard Objects ForecastingAdjustment ForecastingAdjustment

This object represents an individual forecast manager’s adjustment for a subordinate’s or child territory’s forecast via a ForecastingItem.
Available in API versions 26.0 and later. This object is different from the ForecastingOwnerAdjustment object, which represents forecast
users’ adjustments of their _own_ forecasts, including territory forecasts they own.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
AdjustedAmount

AdjustedQuantity

AdjustmentNote

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment. This
field is available in API version 28.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field doesn’t appear in reports.


Standard Objects ForecastingAdjustment

**Field Name** **Details**

```
CurrencyIsoCode

ForecastCategoryName

ForecastingGroupItemId

ForecastingItemCategory

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the user’s personal
currency.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category within the sales cycle that an opportunity is assigned to based on
its opportunity stage. The standard forecast categories are Pipeline, Best Case,
Commit, Omitted, and Closed. You can add a Most Likely category and can
customize forecast category names in single category rollups. The forecast
categories display information for that specific category; for example, Best Case
only reflects amounts in the Best Case category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the manager adjustment belongs to. This field is a relationship field. Available in
API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.


Standard Objects ForecastingAdjustment

**Field Name** **Details**

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly` —Rollup from Pipeline opportunities only.

**•** `BestCaseOnly` —Rollup from Best Case opportunities only. The value
in this category is adjustable.

**•** `MostLikelyOnly` —Rollup from Most Likely opportunities only. The
value in this category is adjustable.

**•** `CommitOnly` —Rollup from Commit opportunities only. The value in
this category is adjustable.

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline` —Rollup from Pipeline, Best Case, Most Likely, and
Commit opportunities.

**•** `BestCaseForecast` —Rollup from Best Case, Most Likely, Commit,
and Closed opportunities. The value in this category is adjustable.

**•** `MostLikelyForecast` —Rollup from Most Likely, Commit, and
Closed opportunities. The value in this category is adjustable.

**•** `CommitForecast` —Rollup from Commit and Closed opportunities.
The value in this category is adjustable.

**For either cumulative or individual forecast category rollups, the possible**
**values are:**

**•** `ClosedOnly` —Rollup from Closed opportunities only.

```
ForecastingItemId

ForecastingTypeId

IsAmount

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ForecastingAdjustment

**Field Name** **Details**

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` . This field is available in API version 28.0 and
later.

```
IsQuantity

OwnerId

PeriodId

ProductFamily

StartDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` . This field is available in API version 28.0 and later.

**Type**
reference

**Properties**
Create,Defaulted on create, Filter, Group, Sort

**Description**

The ID of the forecast owner.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the adjustment. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only. This field is available in API
version 29.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Sort


Standard Objects ForecastingAdjustment

**Field Name** **Details**

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.

```
Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to obtain a manager’s adjustment detail for a specified ForecastingItem. The ForecastingAdjustment object is visible to
all users, but only forecast managers and users above them in the forecast hierarchy can read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

The `ForecastingItemCategory` field differs from the `ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category of the _underlying opportunities_ rolling up to forecast
amounts. In organizations using cumulative forecast rollups, the `ForecastCategoryName` field can be null because the
cumulative forecast amounts include opportunities from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of rollup_ a forecast amount or adjustment is from. In
organizations using individual forecast category columns, it contains the individual forecast rollup categories. In organizations using
cumulative forecast rollups, it contains the cumulative rollup categories.

When inserting manager adjustments, the values you insert for `ForecastCategoryName` and `ForecastingItemCategory`
must be compatible with each other. In organizations using cumulative forecast rollups, the `ForecastCategoryName` is nillable.
The following pairs are valid.

**For individual forecast category rollups:**

**•** `ForecastCategoryName` : `BestCase`, `ForecastingItemCategory` : `BestCaseOnly`

**•** `ForecastCategoryName` : `MostLikely`, `ForecastingItemCategory` : `MostLikelyOnly`

**•** `ForecastCategoryName` : `Commit`, `ForecastingItemCategory` : `CommitOnly`

**For cumulative forecast category rollups:**

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `BestCaseForecast`

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `MostLikelyForecast`


### Standard Objects ForecastingColumnDefinition

**•** `ForecastCategoryName` : `null`, `ForecastingItemCategory` : `CommitForecast`

SEE ALSO:

ForecastingFact

ForecastingItem

ForecastingQuota

### ForecastingColumnDefinition

Represents a custom calculated column or a custom reference data column in a forecast type. This object is available in API version 56.0
and later.

For a custom calculated column, a `Formula` field value is required. For a custom reference data column, a `ReferenceField` field
value is required.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DeveloperName

ForecastingTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer (API) name of the custom calculated column or custom reference data column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup


Standard Objects ForecastingColumnDefinition

**Field** **Details**

**Refers To**
ForecastingType

```
Formula

Language

MasterLabel

ReferenceField

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for custom calculated columns. The formula for the custom calculated column.
Use API column names in your formula (such as ForecastAmount0), not column header
names (such as Closed or Closed Only). For details on API column names, operators, and
functions to use in formulas, see ForecastingColumnDefinition Formula Field Details.

**Example**
The following formula calculates the gap to quota: `ForecastingQuotaAmount -`

```
  ForecastAmount0

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the custom calculated column or custom reference data column.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object, which displays in Setup and in the column header on the forecasts
page. The label is in the default language locale for the organization. If there’s no default
language locale, the label is in en_US.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required for custom reference data columns. The number or currency custom field from the
ForecastingCustomData object. For example,
`ForecastingCustomData.Realized_Revenue__c` . Data from this field appears
in a column in the forecasts summary. This field is available in API version 58.0 and later.


Standard Objects ForecastingColumnDefinition

**Field** **Details**

```
ResultField

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The field name to represent the custom calculated column or custom reference data column
result. Possible values are:

**Custom Calculated Column Result**

**•** CalculatedAmount0 or CalculatedQuantity0

**•** CalculatedAmount1 or CalculatedQuantity1

**•** CalculatedAmount2 or CalculatedQuantity2

**•** CalculatedAmount3 or CalculatedQuantity3

**•** CalculatedAmount4 or CalculatedQuantity4

If the formula’s result is null or invalid, “-” is the value. For example, if the formula divided by
0. If you want to show “-” for 0 or negative values in your forecast, use the IF function in your
formula to detect 0 or negative numbers.

**Custom Reference Data Column Result** Use the appropriate field based on whether your
column output is of Currency or Number type.

**•** ExtensionCurrency0 or ExtensionNumber0

**•** ExtensionCurrency1 or ExtensionNumber1

**•** ExtensionCurrency2 or ExtensionNumber2

**•** ExtensionCurrency3 or ExtensionNumber3

**•** ExtensionCurrency4 or ExtensionNumber4

Each forecast type can include any combination of custom calculated columns and reference data columns, as long as they don’t exceed
five in number. For example, a forecast type can have two custom calculated columns and three custom reference data columns.

Custom calculated columns can’t be adjusted and aren’t included in rollups. In the UI, custom calculated columns can’t indicate changes
in the last 7 days.

If you have at least one custom calculated column in an active or inactive forecast type, you can’t do the following until you’ve removed
the column.

**•** Switch from single category to cumulative rollups in Forecast Settings

**•** Enable the Most Likely category

**•** Disable Show Quotas (only if your custom calculated column’s formula refers to a quota value)


#### Standard Objects ForecastingColumnDefinition Formula Field Details ForecastingColumnDefinition Formula Field Details

Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

#### ForecastingColumnDefinition Formula Field Details

Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

**API Column Names – General**

**•** ForecastingQuotaAmount – Quota (currency)

**•** ForecastingQuotaQuantity – Quota quantity (double)

**•** _`DeveloperName`_ of any custom calculated column or custom reference data column shown in the forecasts page

**API Column Names for Forecast Category Columns**

If the Most Likely category isn’t enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Best Case

**•** ForecastAmount3 or ForecastQuantity3 – Pipeline

If the Most Likely category is enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – Best Case

**•** ForecastAmount4 or ForecastQuantity4 – Pipeline

**API Column Names for Adjustment Columns – Original Forecast Value Without Adjustments**

If your org shows adjustments in columns, use these API column names for the original forecast value without adjustments. Adjustment
columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Most Likely

**•** AmountWithoutAdjustments3 or QuantityWithoutAdjustments3 – Best Case

**API Column Names for Adjustment Columns – Team Adjustment Value**

If your org shows adjustments in columns, use these API column names for the team’s adjusted value that includes a subordinate’s
owner and manager adjustments, but not a forecast manager’s owner and manager adjustments. These adjustment columns are
available in API version 61.0 and later.


Standard Objects ForecastingColumnDefinition Formula Field Details

If the Most Likely category isn’t enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Best Case

If the Most Likely category is enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Most Likely

**•** SubordinateOverrideAmount3 or SubordinateOverrideQuantity3 - Best Case

Use these API column names for the team’s adjusted value that includes owner adjustments without manager adjustments. The
adjustment value includes a subordinate’s manager adjustments that they made. These adjustment columns are available in API
version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Most Likely

**•** AmountWithoutManagerAdjustment3 or QuantityWithoutManagerAdjustment3 – Best Case

**API Column Names for Adjustment Columns – My Adjusted Value**

The column that represents the adjusted value from the forecast user viewing the page is the same as the API column name for the
standard forecast category. Adjustment columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Best Case

If the Most Likely category is enabled:

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – My Best Case

**API Column Names for Custom Reference Data**

Use the appropriate field based on whether the custom reference data is of Currency or Number type.

**•** ExtensionCurrency0

**•** ExtensionCurrency1

**•** ExtensionCurrency2

**•** ExtensionCurrency3

**•** ExtensionCurrency4

**•** ExtensionNumber0

**•** ExtensionNumber1

**•** ExtensionNumber2

**•** ExtensionNumber3

**•** ExtensionNumber4


### Standard Objects ForecastingColumnDefinitionLocalization

**Supported Math Operators**

**•** + (Add) – Calculates the sum of two values.

**•**     - (Subtract) – Calculates the difference of two values.

**•**     - (Multiply) – Multiplies its values.

**•** / (Divide) – Divides its values.

**•** () (Open Parenthesis and Closed Parenthesis) – Specifies that the expressions within the open parenthesis and close parenthesis
are evaluated first. All other expressions are evaluated using standard operator precedence.

**Supported Logical Operators**

**•** = and == (Equal) – Evaluates if two values are equivalent. The = and == operators are interchangeable.

**•** <> and != (Not Equal) – Evaluates if two values aren’t equivalent.

**•** < (Less Than) – Evaluates if a value is less than the value that follows this symbol.

**•**     - (Greater Than) – Evaluates if a value is greater than the value that follows this symbol.

**•** <= (Less Than or Equal) – Evaluates if a value is less than or equal to the value that follows this symbol.

**•** >= (Greater Than or Equal) – Evaluates if a value is greater than or equal to the value that follows this symbol.

**Supported Functions**

**•** IF – Determines if expressions are true or false. Returns a given value if true and another value if false.

**•** NULL can be used as a constant. For example, `IF((expression) < 0, NULL, (expression)).`

### ForecastingColumnDefinitionLocalization

Represents the translated value of a custom calculated column or custom reference data column label when the Translation Workbench
is enabled for your organization. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Translation Workbench must be enabled for your org.

Fields

**Field** **Details**

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language of the translated label.


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

Possible values are:

**•** `af` —Afrikaans

**•** `am` —Amharic

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)

**•** `ar_EG` —Arabic (Egypt)

**•** `ar_IQ` —Arabic (Iraq)

**•** `ar_JO` —Arabic (Jordan)

**•** `ar_KW` —Arabic (Kuwait)

**•** `ar_LB` —Arabic (Lebanon)

**•** `ar_LY` —Arabic (Libya)

**•** `ar_MA` —Arabic (Morocco)

**•** `ar_OM` —Arabic (Oman)

**•** `ar_QA` —Arabic (Qatar)

**•** `ar_SA` —Arabic (Saudi Arabia)

**•** `ar_SD` —Arabic (Sudan)

**•** `ar_SY` —Arabic (Syria)

**•** `ar_TN` —Arabic (Tunisia)

**•** `ar_YE` —Arabic (Yemen)

**•** `bg` —Bulgarian

**•** `bn` —Bengali

**•** `bs` —Bosnian

**•** `ca` —Catalan

**•** `cs` —Czech

**•** `cy` —Welsh

**•** `da` —Danish

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `el_CY` —Greek (Cyprus)

**•** `en_AE` —English (United Arab Emirates)

**•** `en_AU` —English (Australian)

**•** `en_BE` —English (Belgium)


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `en_CA` —English (Canadian)

**•** `en_CY` —English (Cyprus)

**•** `en_DE` —English (Germany)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IL` —English (Israel)

**•** `en_IN` —English (Indian)

**•** `en_MT` —English (Malta)

**•** `en_MY` —English (Malaysian)

**•** `en_NL` —English (Netherlands)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English

**•** `en_ZA` —English (South Africa)

**•** `eo` —Esperanto (Pseudo)

**•** `es` —Spanish

**•** `es_AR` —Spanish (Argentina)

**•** `es_BO` —Spanish (Bolivia)

**•** `es_CL` —Spanish (Chile)

**•** `es_CO` —Spanish (Colombia)

**•** `es_CR` —Spanish (Costa Rica)

**•** `es_DO` —Spanish (Dominican Republic)

**•** `es_EC` —Spanish (Ecuador)

**•** `es_GT` —Spanish (Guatemala)

**•** `es_HN` —Spanish (Honduras)

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)

**•** `es_PA` —Spanish (Panama)

**•** `es_PE` —Spanish (Peru)

**•** `es_PR` —Spanish (Puerto Rico)

**•** `es_PY` —Spanish (Paraguay)

**•** `es_SV` —Spanish (El Salvador)

**•** `es_US` —Spanish (United States)

**•** `es_UY` —Spanish (Uruguay)

**•** `es_VE` —Spanish (Venezuela)

**•** `et` —Estonian


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `eu` —Basque

**•** `fa` —Farsi

**•** `fi` —Finnish

**•** `fr` —French

**•** `fr_BE` —French (Belgium)

**•** `fr_CA` —French (Canadian)

**•** `fr_CH` —French (Switzerland)

**•** `fr_LU` —French (Luxembourg)

**•** `fr_MA` —French (Morocco)

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `haw` —Hawaiian

**•** `hi` —Hindi

**•** `hmn` —Hmong

**•** `hr` —Croatian

**•** `ht` —Haitian Creole

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `iw_EO` —Esperanto RTL (Pseudo)

**•** `ja` —Japanese

**•** `ji` —Yiddish

**•** `ka` —Georgian

**•** `kk` —Kazakh

**•** `kl` —Greenlandic

**•** `km` —Khmer

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo

**•** `mk` —Macedonian

**•** `ml` —Malayalam


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pa` —Punjabi

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `ru_AM` —Russian (Armenia)

**•** `ru_BY` —Russian (Belarus)

**•** `ru_KG` —Russian (Kyrgyzstan)

**•** `ru_KZ` —Russian (Kazakhstan)

**•** `ru_LT` —Russian (Lithuania)

**•** `ru_MD` —Russian (Moldova)

**•** `ru_PL` —Russian (Poland)

**•** `ru_UA` —Russian (Ukraine)

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sm` —Samoan

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian


Standard Objects ForecastingColumnDefinitionLocalization

**Field** **Details**

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_MY` —Chinese (Malaysia)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
NamespacePrefix

ParentId

```

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
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related custom column definition. This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ForecastingColumnDefinition


### Standard Objects ForecastingCustomCategory

**Field** **Details**

```
Value

```

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The translated label of the custom calculated column or custom reference data column.

### ForecastingCustomCategory

Represents a custom forecasting category used for forecast rollups. This object is available in API version 62.0 and later.

In API version 62.0, this object is available for rollup of Manager Judgments only.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CanHaveQuotas

Description

DeveloperName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecasts in the custom category can have quotas. The default value is
`false` . Available in API version 63.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user-defined description of the custom category.

**Type**
string


Standard Objects ForecastingCustomCategory

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The developer name of the custom category.

```
DisplayPosition

ForecastingSourceDefinitionId

ForecastingTypeId

IsAdjustable

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the placement of the custom category column among the other columns on the
forecasts page.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the forecasting source definition.

This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition

**Refers To**
ForecastingSourceDefinition

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ForecastingType.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ForecastingCustomCategory

**Field** **Details**

**Description**
Indicates whether forecast managers can adjust forecasts in the custom category. The default
value is `false` .

```
IsAmount

IsHidden

IsOwnerAdjustable

IsQuantity

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, then `IsQuantity`
must be `true` . The default value is `false` . Available in API version 63.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom category is hidden. The default value is `false` . Available in
API version 63.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether all forecast users can adjust their own forecasts in the custom category,
including the territory forecasts that they own. The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then `IsAmount`
must be `true` . The default value is `false` . Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom category.


### Standard Objects ForecastingCustomData

**Field** **Details**

```
MasterLabel

MeasureFieldOverride

UnitOfMeasure

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for this column. The label is in the default language locale for the organization. If
there’s no default language locale, the label is in en_US.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The measure that this custom category supports.

Possible values are:

**•** `Opportunity.Amount`

**•** `Opportunity.AmountCustom__c`

**•** `Opportunity.AmountRSF__c`

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItem.oliCustomAmount__c`

**•** `OpportunityLineItemSplit.SplitAmount`

**•** `OpportunitySplit.SplitAmount`

**•** `OpportunitySplit.customAmount__c`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unit of measure for the specified custom category measure. Available in API version 63.0
and later.

### ForecastingCustomData

Represents forecast data from external sources to display in the forecasts page. For example, risk or last year’s revenue. This object is
available in API version 58.0 and later.

This object doesn’t support forecast rollups or adjustments. Number and currency columns are supported only.


Standard Objects ForecastingCustomData

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Available in Enterprise Edition and above, and in Professional Edition with an add-on license. Access to this object requires the Manage
Forecasts Custom Data user permission.

Fields

**Field** **Details**

```
ForecastOwnerId

ForecastingGroupItemId

ForecastingTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast owner. This field is a relationship field.

**Relationship Name**
ForecastOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that the custom
data belongs to. This field is a relationship field. Available in API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
reference


Standard Objects ForecastingCustomData

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

```
PeriodId

ProductFamily

StartDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Period ID for the custom data. This field is a relationship field.

**Relationship Name**
Period

**Relationship Type**
Lookup

**Refers To**
Period

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The user-defined product family available to forecast on. Each product family is unique.
Possible values are:

**•** _`[user-defined]`_ –For example, `Electronics` or `Appliances` .

**•** `None`

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The start of the custom data, expressed as month and year. The date can include any day in
a given month. Stored using the first date of the month.


### Standard Objects ForecastingDisplayedFamily

**Field** **Details**

```
Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.

Each record displays as a custom column on the forecasts summary page.

### ForecastingDisplayedFamily

Represents the table in Forecasts Settings where an admin selects the product families that users can forecast on in Lightning Experience.
This object is available in API version 40.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
DisplayPosition

ProductFamily

```

**Type**
int

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The order in which product families are displayed on the forecasts page. Each
value is unique to a product family.

**Type**
picklist

**Properties**
Filter, Group, Sort


### Standard Objects ForecastingFact

**Field Name** **Details**

**Description**
The product family available to forecast on. Each product family is unique.

### ForecastingFact

This object is read-only and links a ForecastingItem with its opportunities, such as opportunities that share the same owner or forecast
category and have a closing date within the period of the forecasting item. Available in API versions 26 and greater.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
ForecastCategoryName

ForecastedObjectId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

A forecast category is the category within the sales cycle to which an opportunity
is assigned based on its opportunity stage. The standard forecast categories are
Pipeline, Best Case, Commit, Omitted (not included in forecasts), and Closed.
Salesforce admins can customize the forecast category names.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the Split ID of the forecasted OpportunitySplit object if the forecast data
source is opportunity splits or the OpportunityLineItem ID of the forecasted
opportunity if the data source is product families. If the data source is product
families and the opportunity has no line item, this field is null. If the forecast data


Standard Objects ForecastingFact

**Field Name** **Details**

source is opportunities, this field is null. This field is available in API version 29
and later. Read-only.

```
ForecastedSubObjectId

ForecastingItemId

ForecastingTypeId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Possible values:

**•** If the forecast data source is OpportunityLineItemSplit, and the opportunity
has line items and line item splits, then this field contains the ID of the
forecasted OpportunityLineItemSplit object.

**•** If the forecast data source is OpportunityLineItemSplit, and the opportunity
has line items but no line item splits, this field contains the ID of the forecasted
OpportunitySplit object.

**•** If the forecast data source is OpportunityLineItemSchedule, this field contains
the OpportunityLineItemSchedule ID of the forecasted opportunity.

**•** If the forecast data source is OpportunityLineItemSplit and the opportunity
has no line item, this field is null.

**•** If the forecast data source is OpportunityLineItemSchedule and the
opportunity has no line item, this field is null.

This field is available in API version 58.0 and later. Read-only. This field is a
polymorphic relationship field.

**Relationship Name**
null

**Relationship Type**
Lookup

**Refers To**
OpportunityLineItem, OpportunityLineItemSplit

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ForecastingItem.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ForecastingFact

**Field Name** **Details**

**Description**

The ID of the related ForecastingType.

```
OpportunityId

OwnerId

PeriodId

TargetValue

Territory2Id

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The opportunity ID.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the opportunity owner.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the forecast.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

Target value of the forecast amount.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43 and later.


### Standard Objects ForecastingFilter

Usage

Use this object to get information about opportunities linked to forecasting items.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingItem

ForecastingQuota

### ForecastingFilter

Represents the custom filter for including or excluding data from opportunity forecasts. This object is available in API version 54.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts permission OR Allow Forecasting permission OR delegated
forecast manager status can access this object.

Fields

**Field Name** **Details**

```
DeveloperName

FilterLogic

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The developer name of the forecast filter.

**Type**
string


Standard Objects ForecastingFilter

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The logic that controls the evaluation of conditions. Only `AND` is supported. For
example, `1 AND 2 AND 3` .

```
ForecastingTypeId

ForecastingTypeSourceId

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast type. Can be linked only to forecast types created in Summer
’21 and later. This is a relationship field.

**Relationship Name**

ForecastingType

**Relationship Type**

Lookup

**Refers To**

ForecastingType

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast type source. Can be linked only to forecast type sources
created in Summer ’21 or later and with a forecast source definition with source
object of 'Opportunity.' This is a relationship field.

**Relationship Name**

ForecastingTypeSource

**Relationship Type**

Lookup

**Refers To**

ForecastingTypeSource

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ForecastingFilterCondition

**Field Name** **Details**

**Description**

The language of the forecast filter.

```
MasterLabel

### ForecastingFilterCondition

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this object, which displays in Setup. The label is in the default
language locale for the organization. If there’s no default language locale, the
label is in en_US.

Represents the custom filter condition logic for including or excluding data from opportunity forecasts. This object is available in API
version 54.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts permission OR Allow Forecasting permission OR delegated
forecast manager status can access this object.

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The developer name of the forecast filter condition.


Standard Objects ForecastingFilterCondition

**Field Name** **Details**

```
FieldName

ForecastingFilterId

Language

MasterLabel

Operation

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The name of the opportunity field to be filtered.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast filter. This is a relationship field.

**Relationship Name**

ForecastingFilter

**Relationship Type**

Lookup

**Refers To**

ForecastingFilter

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the forecast filter condition.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this object, which displays in Setup. The label is in the default
language locale for the organization. If there’s no default language locale, the
label is in en_US.

**Type**
string


### Standard Objects ForecastingGroup

**Field Name** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The operator in the filter condition. Possible values are:

**•** equals

**•** greaterOrEqual – greater than or equal to

**•** greaterThan

**•** lessOrEqual – less than or equal to

**•** lessThan

**•** notEqual

```
SortOrder

Value

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**

The index value for the condition. This value represents the condition in the
FilterLogic field in the ForecastingFilter object. For example, 1.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The value of the filter condition. If multiple values are specified, they must be
separated by a comma delimiter.

Note: If you have multiple currencies enabled, and add a custom filter
on a currency field as part of your forecast type definition, the corporate
currency at the time the filter was created is used. If you have a single
currency enabled, the absolute value is used in your filter condition.

A forecast type can contain up to three filter conditions.

### ForecastingGroup

Represents groups used to roll up forecast totals on the forecasts page. For example, group forecasts by industry or sales type. This object
is available in API version 60.0 and later.


Standard Objects ForecastingGroup

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Available for forecast types created in Spring ‘24 or later and that are based on the Opportunity and Opportunity Product objects.

You can only add groups to new forecast types.

Fields

**Field** **Details**

```
DeveloperName

DisplayPosition

ForecastingTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer (API) name of the forecast group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which forecasting dimensions are displayed on the forecasts page. Each value
is unique to a dimension.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the forecast type associated with the forecasting group.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType


Standard Objects ForecastingGroup

**Field** **Details**

```
GroupField

Language

MasterLabel

SourceObject

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field name of the custom picklist used as a group. Possible values include custom,
single-selection picklists available in `SourceObject` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the custom picklist identified as the group.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object, which displays in Setup. The label is in the default language locale
for the organization. If there’s no default language locale, the label is in en_US.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The entity the picklist used for the forecast group is on.

Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `Product2`

Each forecast group can apply to only one forecast type.


### Standard Objects ForecastingGroupItem ForecastingGroupItem

Represents the value within the picklist that is specified as the forecasting group for a forecast type. For example, if you have a forecasting
group that identifies the industry an opportunity is part of, this object represents the value in the the industry picklist that’s chosen to
be part of the group. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DisplayPosition

ForecastingGroupId

SourceValueApiName

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates the order in which the value displays among other values in the group on the
forecasts page.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
### ForecastingGroup

**Relationship Type**
Lookup

**Refers To**
### ForecastingGroup

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The API name that’s derived from the group value.


### Standard Objects ForecastingItem

**Field** **Details**

```
SourceValueLabel

SourceValueTranslatedLabel

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The label that’s derived from the group value.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
If one exists, the translated version of the group value.

New forecast types based on opportunities or opportunity products can include a forecasting group. This group is based on a custom,
single-selection picklist that’s defined on the Opportunity, OpportunityLineItem, or Product2 objects. The picklist that’s chosen for the
group can contain more values than are needed for the type.

### ForecastingItem

This object is read-only used for individual forecast amounts. Users see amounts based on their perspectives and forecast roles. The
amounts users see include one of these values when forecasting in revenue: `AmountWithoutAdjustments`,
`AmountWithoutManagerAdjustment`, `ForecastAmount`, `OwnerOnlyAmount` . The amounts users see include one of
these values when forecasting in quantity: `QuantityWithoutAdjustments`, `QuantityWithoutManagerAdjustment`,
`ForecastQuantity`, `OwnerOnlyQuantity` . Available in API version 26.0 and later.

Other users can see the ForecastingItem object, but not its records. See these access guidelines.

**•** Users with the “View All Forecasts” permission have access to all ForecastingItem fields.

**•** Users without the “View All Forecasts” permission have access to all fields for their own subordinates and child territories.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.


Standard Objects ForecastingItem

Fields

**Field Name** **Details**

```
AmountWithoutAdjustments

AmountWithoutManagerAdjustment

AmountWithoutOwnerAdjustment

ForecastAmount

```

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s owned revenue opportunities and the person's
subordinates’ and child territories’ opportunities, without adjustments.
Subordinates include everyone reporting up to a person in the role-based forecast
hierarchy. This amount is visible only on reports.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The forecast number as seen by the forecast owner. This number is the sum of
the owner’s revenue opportunities and the owner’s subordinates’ and child
territories’ opportunities, including adjustments made by the forecast owner on
the owner's or subordinates’ and child territories’ forecasts. It doesn’t include
adjustments made by forecast managers above the owner in the forecast
hierarchy.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The forecast amount as seen by the forecast owner without the owner's
adjustment. This amount is the sum of the subordinate's and child territories’
opportunities, including adjustments made by their manager or by the
subordinate themselves, plus the rollup of the owner's own opportunities. _It_
_doesn’t include adjustments made by the forecast owner._

**Type**
double

**Properties**
Filter, Sort, Nillable


Standard Objects ForecastingItem

**Field Name** **Details**

**Description**

The revenue forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ and child territories’ opportunities, including all
forecast adjustments.

```
ForecastCategoryName

ForecastQuantity

ForecastingGroupItemId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A forecast category is the category within the sales cycle to which an opportunity
is assigned based on its opportunity stage. The standard forecast categories are
Pipeline, Best Case, Commit, Omitted (not included in forecasts), and Closed.
Salesforce admins can add a Most Likely category and can customize the forecast
category names in single category rollups. Change the forecast category name
only. Changing a forecast category’s API name can have unintended results.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The quantity forecast from the forecast manager’s perspective and the sum of
the owner’s and subordinates’ opportunities, including all forecast adjustments.
This field is available in API version 28 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the forecast total belongs to. This field is a relationship field. Available in API
version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem


Standard Objects ForecastingItem

**Field Name** **Details**

```
ForecastingItemCategory

ForecastingTypeId

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
This field indicates which type of forecast rollup the forecasting item belongs to.
Depending on whether your organization uses individual forecast category rollups
or cumulative forecast rollups, you have these possible values for the
`ForecastingItemCategory` field.

_**Individual forecast category rollups:**_

**•** PipelineOnly - Rollup from Pipeline opportunities only.

**•** BestCaseOnly - Rollup from Best Case opportunities only. Adjustable.

**•** MostLikelyOnly - Rollup from Most Likely opportunities only. Adjustable.

**•** CommitOnly - Rollup from Commit opportunities only. Adjustable.

_**Cumulative forecast rollups:**_

**•** OpenPipeline - Rollup from Pipeline + Best Case + Most Likely + Commit
opportunities.

**•** BestCaseForecast - Rollup from Best Case + Most Likely + Commit +
Closed opportunities. Adjustable.

**•** MostLikelyForecast - Rollup from Most Likely + Commit + Closed
opportunities. Adjustable.

**•** CommitForecast - Rollup from Commit + Closed opportunities.
Adjustable.

_**Either cumulative or individual forecast category rollups:**_

**•** ClosedOnly - Rollup from Closed opportunities only.

The `ForecastingItemCategory` field differs from the
`ForecastCategoryName` field.

**•** The `ForecastCategoryName` field represents the forecast category
of the _underlying opportunities_ rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the `ForecastCategoryName` field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of_
_rollup_ a forecast amount or adjustment is from. In organizations using
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

**Type**
reference


Standard Objects ForecastingItem

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

```
HasAdjustment

HasOwnerAdjustment

IsAmount

IsQuantity

IsUpToDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes a _manager_ adjustment. This
flag is true only when the item includes an adjustment and the user performing
the query has read access to the adjustment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag that indicates the forecasting item includes an _owner_ adjustment. This flag
is true only when the item includes an adjustment and the user performing the
query has read access to the adjustment. Available in API version 33.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a revenue amount. If false, then
`IsQuantity` must be true. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

True indicates that the adjustment is made in a quantity amount. If false, then
`IsAmount` must be true. This field is available in API version 28.0 and later.

**Type**
boolean


Standard Objects ForecastingItem

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

A flag indicating whether a specific forecasting item reflects current information.
For example, if users are making adjustments that are in process, the item isn’t
up to date.

```
OwnerId

OwnerOnlyAmount

OwnerOnlyQuantity

ParentForecastingItemId

PeriodId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the forecast owner.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s revenue opportunities, without adjustments.

**Type**
double

**Properties**
Filter, Sort, Nillable

**Description**

The sum of a person’s quantity opportunities, without adjustments. This field is
available in API version 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ForecastingItem that the current item rolls up to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ForecastingItem

**Field Name** **Details**

**Description**

Period ID for the forecast.

```
ProductFamily

QuantityWithoutAdjustments

QuantityWithoutManagerAdjustment

QuantityWithoutOwnerAdjustment

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product family of the forecast item. This field is available in API version 29.0
and later. Read only.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The sum of a person’s owned quantity opportunities and also his or her
subordinates’ opportunities, without adjustments. Subordinates include everyone
reporting up to a person in the forecast hierarchy. This field is available in API
version 28.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast number as seen by the forecast owner. This number is the sum of
the owner’s quantity opportunities and subordinates’ opportunities, including
adjustments made on the subordinates’ forecasts. It doesn’t include adjustments
made by forecast managers above the owner in the forecast hierarchy. This field
is available in API version 28 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

The forecast quantity as seen by the forecast owner without the owner's
adjustment. This number is the sum of the subordinate's opportunities, including
adjustments made by their manager or by the subordinate themselves, plus the
rollup of the owner's own opportunities. _It doesn’t include adjustments made by_
_the forecast owner._ This field is available in API version 38.0 and later.


### Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

```
SubordinateOverrides

Territory2Id

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of adjustments made to a forecast down the hierarchical chain.
For example, User A has a forecast without adjustments. If User A adjusts User
B’s forecast, User A’s `SubordinateOverrides` value is 1. Then if User B
adjusts User C’s forecast, User A’s `SubordinateOverrides` value is 2. If
User A removes his adjustment from User B’s forecast, User A’s
`SubordinateOverrides` value is 1.

This field is available in API version 38.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to obtain individual forecast amounts, either with or without adjustments, based on a user’s perspective and forecast
role. The ForecastingItem object is visible to all users, but only forecast managers and users above them in the forecast hierarchy can
read or write ForecastingAdjustment records.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
### ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingQuota

### ForecastingOwnerAdjustment

This object represents an individual forecast user’s adjustment of their _own_ forecast, including territory forecasts they own, via a
ForecastingItem. Available in API versions 33.0 and later. This object is different from the ForecastingAdjustment object, which represents
managers’ adjustments of _subordinates’_ and child territories’ forecasts.


Standard Objects ForecastingOwnerAdjustment

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

ForecastCategoryName

ForecastOwnerId

ForecastingGroupItemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the adjustment. If omitted, the default is the importing
user’s personal currency.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category within the sales cycle that an opportunity is assigned to based on
its opportunity stage. The standard forecast categories are Pipeline, Best Case,
Commit, Omitted, and Closed. You can add a Most Likely category and can
customize forecast category names in single category rollups. The forecast
categories display information for that specific category; for example, Best Case
only reflects amounts in the Best Case category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the forecast owner.

**Type**
reference


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the owner adjustment belongs to. This field is a relationship field. Available in
API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

```
ForecastingItemCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
This field indicates which type of forecast rollup the owner adjustment belongs
to. Depending on whether your organization uses individual forecast category
rollups or cumulative forecast rollups, you have these possible values for the
`ForecastingItemCategory` field.

_**Individual forecast category rollups:**_

**•** PipelineOnly - Rollup from Pipeline opportunities only.

**•** BestCaseOnly - Rollup from Best Case opportunities only. Adjustable.

**•** MostLikelyOnly - Rollup from Most Likely opportunities only. Adjustable.

**•** CommitOnly - Rollup from Commit opportunities only. Adjustable.

_**Cumulative forecast rollups:**_

**•** OpenPipeline - Rollup from Pipeline + Best Case + Most Likely + Commit
opportunities.

**•** BestCaseForecast - Rollup from Best Case + Most Likely + Commit +
Closed opportunities. Adjustable.

**•** MostLikelyForecast - Rollup from Most Likely + Commit + Closed
opportunities. Adjustable.

**•** CommitForecast - Rollup from Commit + Closed opportunities.
Adjustable.

_**Either cumulative or individual forecast category rollups:**_

**•** ClosedOnly - Rollup from Closed opportunities only.

The `ForecastingItemCategory` field differs from the
`ForecastCategoryName` field.


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**•** The `ForecastCategoryName` field represents the forecast category
of the _underlying opportunities_ rolling up to forecast amounts. In organizations
using cumulative forecast rollups, the `ForecastCategoryName` field
can be null because the cumulative forecast amounts include opportunities
from multiple forecast categories.

**•** The new `ForecastingItemCategory` field represents the _type of_
_rollup_ a forecast amount or adjustment is from. In organizations using
individual forecast category columns, it contains the individual forecast rollup
categories. In organizations using cumulative forecast rollups, it contains the
cumulative rollup categories.

When inserting owner adjustments, the values you insert for
`ForecastCategoryName` and `ForecastingItemCategory` must
be compatible with each other. In organizations using cumulative forecast rollups,
the `ForecastCategoryName` is nillable. These pairs are the valid pairs.

**Individual forecast category rollups:**

**•** `ForecastCategoryName` : BestCase,
`ForecastingItemCategory` : BestCaseOnly

**•** `ForecastCategoryName` : Commit,
`ForecastingItemCategory` : CommitOnly

**Cumulative forecast category rollups:**

**•** `ForecastCategoryName` : null, `ForecastingItemCategory` :
BestCaseForecast

**•** `ForecastCategoryName` : null, `ForecastingItemCategory` :
CommitForecast

```
ForecastingItemId

ForecastingTypeId

IsAmount

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the related ForecastingItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` .

```
IsQuantity

OwnerAdjustedAmount

OwnerAdjustedQuantity

OwnerAdjustmentNote

PeriodId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A text note providing information about the adjustment. The maximum length
is 255 characters. This field does not appear in reports.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ForecastingOwnerAdjustment

**Field Name** **Details**

**Description**

Period ID for the adjustment. Read only.

```
ProductFamily

StartDate

Territory2Id

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The Product Family for the adjustment. Read only.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The start of the adjustment, expressed as month and year. The date can include
any day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to obtain a user’s adjustment details for a specified ForecastingItem in their own forecast.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

**ForecastingOwnerAdjustmentChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ForecastingQuota ForecastingQuota

This object represents an individual user’s or territory’s quota for a specified time period. The Managed Quotas user permission is required
for creating, updating, or deleting quotas. (Users can only edit their subordinates’ or child territories’ quotas, not their own.) The View
All Forecasts permission is required to view any user's forecast, regardless of the forecast hierarchy. Available in API versions 25.0 and
later. Forecast managers can view the forecasts of subordinates and territories below them in the forecast hierarchy.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CurrencyIsoCode

ForecastingGroupItemId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The currency code of the quota. If omitted, the default is the importing user’s
personal currency.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that
the quota belongs to. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroupItem

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem


Standard Objects ForecastingQuota

**Field Name** **Details**

```
ForecastingTypeId

IsAmount

IsQuantity

PeriodId

ProductFamily

QuotaAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the related ForecastingType.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a revenue amount. If `false`, then
`IsQuantity` must be `true` . This field is available in API version 28.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

If `true`, then the adjustment is made in a quantity amount. If `false`, then
`IsAmount` must be `true` . This field is available in API version 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the quota. Read only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product family for the quota. This field is available in API version 29.0 and
later.

**Type**
currency


Standard Objects ForecastingQuota

**Field Name** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**

The revenue quota amount for an individual user or territory and for a specific
period.

```
QuotaOwnerId

QuotaQuantity

StartDate

Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

ID that identifies the quota owner.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**

The quantity quota amount for an individual user and for a specific period. This
field is available in API version 28.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The start of the quota, expressed as month and year. The date can include any
day in a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43.0 and later.

Use this object to get an individual user’s or territory’s quota for a specified time period.


### Standard Objects ForecastingShare

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
`ForecastingQuota`, `ForecastingAdjustment`, `ForecastingOwnerAdjustment`, `ForecastingItem`,
and `ForecastingFact` objects can all have records with different `ForecastingTypeId` values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota`, `ForecastingAdjustment`,
`ForecastingItem`, or `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingFact

ForecastingItem

### ForecastingShare

Represents forecasts shared between a forecast manager and a user. Available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
AccessLevel

SharedForecastManagerRoleId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

Whether the user you’re sharing your forecasts with can view and adjust the
forecasts or view only. This field is new since the pilot.

Picklist values:

**•** `ViewAndEdit`

**•** `ViewOnly`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ForecastingSourceDefinition

**Field Name** **Details**

**Description**

The ID of either:

**•** The role of the manager whose forecasts you want to share.

**•** The territory whose forecasts you want to share.

```
RoleType

UserOrGroupId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of hierarchy associated with the forecast share.

**•** `R`  - Role-based

**•** `T`  - Territory-based

**•** `Y`  - Territory2-based

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the user with whom the forecast is shared.

Use this object to let any stakeholder at your company view and adjust forecast managers’ forecasts.

### ForecastingSourceDefinition

Represents the object, measure, date type, and hierarchy that a forecast uses to project sales. This object is available in API version 52.0
and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ForecastingSourceDefinition

Fields

**Field** **Details**

```
CategoryField

DateField

DeveloperName

FamilyField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Name of the forecast category that is associated with the forecast type.

Possible values are:

**•** `Opportunity.ForecastCategoryName`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Field that is used for the forecast type’s date type. For example, the CloseDate field on
Opportunity is used for opportunity close date-based forecast types.

Possible values are:

**•** `Opportunity.CloseDate`

**•** `OpportunityLineItem.ServiceDate`

**•** `OpportunityLineItemSchedule.ScheduleDate`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting source definition.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Use this field to group forecasts by product family. Possible values are:

**•** `Product2.Family`


Standard Objects ForecastingSourceDefinition

**Field** **Details**

```
Language

MasterLabel

MeasureField

SourceObject

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting source definition. For example, English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting source definition.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Field that is used for the forecast type’s measure. For example, the Amount field on
Opportunity is associated with revenue-based forecast types.

Possible values are*:

**•** `Opportunity.Amount`

**•** `Opportunity.` _**`Custom`**_

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.` _**`Custom`**_

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItemSchedule.` _**`Custom`**_

**•** `OpportunityLineItemSchedule.Quantity`

**•** `OpportunityLineItemSchedule.Revenue`

**•** `OpportunitySplit.` _**`Custom`**_

**•** `OpportunitySplit.SplitAmount`

*Where _**`Custom`**_ represents the name of the custom field that a forecast type’s measure is
based on. Example: Use `Megawatts__c` to forecast energy consumption.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ForecastingSourceDefinition

**Field** **Details**

**Description**
Object associated with this forecasting source definition.

Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `OpportunityLineItemSchedule`

**•** `OpportunitySplit`

**•** `Product2`

```
Territory2Field

UserField

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For a territory-based forecast type, indicates the field that is used for territory information.

Possible values are:

**•** `Opportunity.Territory2Id`

For user role-based forecast types, this value is `null` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies who owns the forecast.

Possible values are:

**•** `Opportunity.OwnerId`

**•** `OpportunitySplit.SplitOwnerId`

Use ForecastingSourceDefinition to define a forecast type’s structure. A forecasting source definition is joined via
`ForecastingTypeSource` to `ForecastingType` .

In this example, a user role-based forecast type called Custom Amount Forecast is based on the Amount and Close Date fields on
opportunities.

```
ForecastingType type = new sforce.SObject("ForecastingType");

type.DeveloperName = "Custom_Amount_Forecast";

type.MasterLabel = "Custom Amount Forecast";

type.IsAmount = true;

```


### Standard Objects ForecastingSrcRecJudgment

```
   type.IsQuantity = false;

   type.RoleType = "R";

   type.DateType = "OpportunityCloseDate";

   String typeId = insert(type);

   ForecastingSourceDefinition sourceDefinition = new

   sforce.SObject("ForecastingSourceDefinition")

   sourceDefinition.DeveloperName = "Custom Amount Source";

   sourceDefinition.MasterLabel = "Custom_Amount_Source";

   sourceDefinition.SourceObject = "Opportunity";

   sourceDefinition.MeasureField = "Opportunity.Amount";

   sourceDefinition.DateField = "Opportunity.CloseDate";

   sourceDefinition.UserField = "Opportunity.OwnerId";

   sourceDefinition.CategoryField = "Opportunity.ForecastCategoryName";

   String sourceDefinitionId = insert(sourceDefinition);

   ForecastingTypeSource typeSource = new sforce.SObject("ForecastingTypeSource");

   typeSource.MasterLabel = "Custom Amount Type Source";

   typeSource.DeveloperName = "Custom_Amount_Type_Source";

   typeSource.ForecastingTypeId = typeId;

   typeSource.ForecastingSourceDefinitionId = sourceDefinitionId;

   typeSource.SourceGroup = 1;

   insert(typeSource);

### ForecastingSrcRecJudgment

```

Represents forecast managers’ judgment of whether they consider an opportunity-related deal to be certain to close. This object is
available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
CurrencyIsoCode

JudgmentOwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the judgment. If omitted, the default is USD.

**Type**
reference


Standard Objects ForecastingSrcRecJudgment

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast manager.

This field is a relationship field.

**Relationship Name**
JudgmentOwner

**Relationship Type**
Lookup

**Refers To**
User

```
JudgmentValue

ReferenceObjectId

Territory2Id

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Whether the deal is likely to close ( `IN` ) or not ( `OUT` ).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the opportunity-related object.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory that the judgment is on.

This field is a polymorphic relationship field.


### Standard Objects ForecastingSubmission

**Field** **Details**

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Territory2

### ForecastingSubmission

Represents a submitted forecast. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available for forecast types that aren’t grouped by product family forecast.

Fields

**Field** **Details**

```
CurrencyIsoCode

ForecastOwnerId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast owner.

This field is a relationship field.

**Relationship Name**
ForecastOwner


Standard Objects ForecastingSubmission

**Field** **Details**

**Refers To**
User

```
ForecastingGroupItemId

ForecastingTypeId

IsLatest

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use. Forecast submissions aren't supported in forecast types with groups.

**Relationship Name**
ForecastingGroupItem

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the forecast submission is the most recent submission.

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. ID of this record.


Standard Objects ForecastingSubmission

**Field** **Details**

```
Note

PeriodId

PeriodStartDate

ProductFamily

SubmissionDateTime

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The note attached to the submitted forecast.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the period to which the submission applies.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Indicates the start date of the forecast period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Must be set to `none` . Forecast submissions aren't supported in forecast types grouped by
product families.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the forecast submission was made. Calculated internally.


### Standard Objects ForecastingSubmissionItem

**Field** **Details**

```
Territory2Id

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2

ForecastingSubmission is a detail object that contains the submitted item category values. Each record represents the values for a single
item category. ForecastingSubmission is always used as a detail object for the submission, and inserted only as part of a transaction that
includes all detail objects.

### ForecastingSubmissionItem

Represents the values for each forecast category in a submitted forecast. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Amount as the measure, the amount for the forecast category.
Amounts must be provided in the corporate currency.

**Type**
picklist


Standard Objects ForecastingSubmissionItem

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

```
ForecastingItemCategory

ForecastingSubmissionId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort

**Description**
The category the forecast belongs to.

**For individual forecast category rollups, the possible values are:**

**•** `PipelineOnly` —Rollup from Pipeline opportunities only.

**•** `BestCaseOnly` —Rollup from Best Case opportunities only.

**•** `MostLikelyOnly` —Rollup from Most Likely opportunities only.

**•** `CommitOnly` —Rollup from Commit opportunities only.

**For cumulative forecast rollups, the possible values are:**

**•** `OpenPipeline` —Rollup from Pipeline, Best Case, Most Likely, and Commit
opportunities.

**•** `BestCaseForecast` —Rollup from Best Case, Most Likely, Commit, and Closed
opportunities.

**•** `MostLikelyForecast` —Rollup from Most Likely, Commit, and Closed
opportunities.

**•** `CommitForecast` —Rollup from Commit and Closed opportunities.

**For either cumulative or individual forecast category rollups, the possible values**
**are:**

**•** `ClosedOnly` —Rollup from Closed opportunities only.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast submission.

This field is a relationship field.

**Relationship Name**
ForecastingSubmission

**Relationship Type**
Master-detail


### Standard Objects ForecastingType

**Field** **Details**

**Refers To**
ForecastingSubmission (the master object)

```
Name

Quantity

### ForecastingType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. The ID of this record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Quantity as the measure, the quantity for the forecast category.
Quantities must be provided in the corporate currency.

Used to identify the forecast type associated with `ForecastingAdjustment`, `ForecastingOwnerAdjustment`,
`ForecastingQuota`, `ForecastingFact`, and `ForecastingItem` objects. Available in API version 30.0 and greater.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()` . `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
CanDisplayQuotas

```

**Type**
boolean


Standard Objects ForecastingType

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a forecast type can show quota information. The default value
is `false` . Available in API version 38.0 and later.

```
DateType

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The date type that forecast amounts are based on. These values are available for
forecast types that were available before Summer ’21.

**•** `OpportunityCloseDate` : Base forecasts on opportunity close dates.

**•** `ProductDate` : Base forecasts on opportunity product line item dates, if
available.

**•** `ScheduleDate` : Base forecasts on opportunity product schedule dates,
if available.

These values are available in API version 52.0 and later in Performance Edition
and in Unlimited Edition with the Sales Cloud.

**•** `OLIMeasureCloseDateOnly` : Base forecasts on opportunity close
dates.

**•** `ProductDateOnly` : Base forecasts on opportunity product line item
dates, if available.

**•** `ScheduleDateOnly` : Base forecasts on opportunity product schedule
dates, if available.

These values to create forecasts on custom date fields are available in API version
57.0 and later in Performance, Professional, Enterprise, and Unlimited Edition
with the Sales Cloud.

**•** `OLIMeasureOppCustomDateOnly` : Base forecasts on custom
opportunity dates, if available.

**•** `OpportunityCustomDate` : Base forecasts on custom opportunity
dates.

The custom date field used must be on the opportunity object and based on the
date type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ForecastingType

**Field Name** **Details**

**Description**
The name of the forecasting type. The `DeveloperName` is called `name` in
the Metadata API and Forecasting Type in custom reports.

```
ForecastingGroupID

HasAdjustments

HasOwnerAdjustments

HasProductFamily

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a group assignment, and if so, the
name of the group. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroup

**Relationship Type**
Lookup

**Refers To**
ForecastingGroup

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecast managers can adjust forecasts of their immediate
subordinates and child territories. The default value is `false` . Available in API
version 60.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether all forecast users can adjust their own forecasts, including the
territory forecasts that they own. The default value is `false` . Available in API
version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group


Standard Objects ForecastingType

**Field Name** **Details**

**Description**
Indicates whether a forecasts view includes product families. The default value
is `false` . Available in API version 40.0 and later.

```
IsActive

IsAmount

IsPlatformType

IsQuantity

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecasting type is enabled. The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the revenue measure. The
default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a legacy forecast type that wasn’t available before Summer ’21. The
default value is `false` . Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the quantity measure. The
default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the forecasting type.


Standard Objects ForecastingType

**Field Name** **Details**

```
LastActivatedDate

MasterLabel

OpportunitySplitTypeId

OpptyLineItemSplitTypeId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date when a forecast type was activated. Read only. Available in API version
53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Controlling label for this forecasting type value. This display value is the internal
label that doesn’t get translated.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a split type, and if so, the name of the
split type. This field is a relationship field. Available in API version 41.0 and later.

**Relationship Name**
OpportunitySplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a product split type, and if so, the
name of the product split type. This field is a relationship field. Available in API
version 58.0 and later.

**Relationship Name**
OpptyLineItemSplitType

**Relationship Type**
Lookup


### Standard Objects ForecastingTypeSource

**Field Name** **Details**

**Refers To**
OpptyLineItemSplitType

```
RoleType

Territory2ModelId

### ForecastingTypeSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the role type has a forecasting type, and if so, which forecasting
type. Available in API version 41.0 and later.

Possible values are:

**•** `R` —User role-based forecasting type

**•** `T` —Territory1-based forecasting type; not used

**•** `Y` —Territory2-based forecasting type

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a Territory2 model, and if so, the name
of the Territory2 model. Available in API version 41.0 and later.

Maps a forecasting source definition to a forecast type. This object is available in API version 52.0 and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ForecastingTypeSource

Fields

**Field** **Details**

```
DeveloperName

ForecastingSourceDefinitionId

ForecastingTypeId

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting type source.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecasting source definition. This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition

**Relationship Type**
Lookup

**Refers To**
ForecastingSourceDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecast type. Can be linked only to forecast types created in Summer ’21 and later.
This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
picklist


Standard Objects ForecastingTypeSource

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting type source.

```
MasterLabel

ParentSourceDefinitionId

RelationField

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting type source.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For forecast types not based on the opportunity object and not based on a custom measure,
this value represents the parent ForecastingSourceDefinition of the linked
ForecastingSourceDefinition. This field is a relationship field.

**•** Opportunity Product is the parent of Opportunity.

**•** Opportunity Split is the parent of Opportunity.

**•** Line Item Schedule is the parent of Opportunity Product.

**Relationship Name**
ParentSourceDefinition

**Relationship Type**
Lookup

**Refers To**
ForecastingSourceDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the field linking the source objects of the parent ForecastingSourceDefinition to
the child ForecastingSourceDefinition.

Possible values are:

**•** `OpportunityLineItem.OpportunityId`

**•** `OpportunityLineItem.Product2Id`

**•** `OpportunityLineItemSchedule.OpportunityLineItemId`


### Standard Objects ForecastingUserPreference

**Field** **Details**

**•** `OpportunitySplit.OpportunityId`

```
SourceGroup

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Represents a grouping of forecasting source definitions.

Use this object to define a forecast type’s structure. This junction object links `ForecastingSourceDefinition` to
`ForecastingType` .

For an example, see ForecastingSourceDefinition.

### ForecastingUserPreference

Represents the forecasting selections that a user has made, such as display options, date range, forecasting type, and currency.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

Fields

**Field Name** **Details**

```
ExternalId

ForecastingDisplayedTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A unique system-generated numerical identifier for the user.

**Type**
reference


Standard Objects ForecastingUserPreference

**Field Name** **Details**

**Properties**
Create, Group, Sort, Update

**Description**

An identifier for the forecasting type that’s displayed.

```
ForecastingPeriodDuration

ForecastingPeriodType

ForecastingStartPeriod

ForecastingViewCurrency

IsForecastingHideZeroRows

```

**Type**
int

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

How long the forecasting period lasts.

**Type**
picklist

**Properties**
Create, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The forecasting period’s type. Valid values include: Month, Quarter, Week, or Year

**Type**
int

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The date when the forecasting period begins.

**Type**
string

**Properties**
Create, Group, Nillable, Sort, Update

**Description**

The currency shown on the forecasts page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows zero-value rows.


### Standard Objects FormulaFunction

**Field Name** **Details**

```
IsForecastingShowQuantity

IsHideForecastingGuidedTour

IsHideForecastingQuotaColumn

IsShowForecastingChangeSignals

IsShowForecastingQuotaAttainment

### FormulaFunction

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows forecast quantity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows the guided tour.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows a quota column.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows changes in the last 7 days.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**

Whether the forecasts page shows quota attainment information.

Represents a function used when building a formula, including examples and uses. This object is available in API version 47.0 and later.


Standard Objects FormulaFunction

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
CategoryId

Description

DurableId

ExampleString

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FormulaFunctionCategory.

This is a relationship field.

**Relationship Name**
Category

**Relationship Type**
Lookup

**Refers To**
FormulaFunctionCategory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the formula function.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the function and what arguments you can use with it.


Standard Objects FormulaFunction

**Field** **Details**

```
IsAllowedInEntityContext

IsAllowedInFlowContext

IsAllowedInVisualforceContext

Label

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether you can use the formula function on an Entity ( `true` ) or not ( `false` ).
For example, you cannot use the PRIORVALUE function in a custom Account formula field.
The default value is `false` . This field is removed in API version 48.0 and later. Use the
FormulaFunctionAllowedType on page 2789 object instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in a Flow ( `true` ) or not ( `false` ). The
default value is `false` . This field is removed in API version 48.0 and later. Use the
FormulaFunctionAllowedType on page 2789 object instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the formula function is allowed in Visualforce ( `true` ) or not ( `false` ).
The default value is `false` . This field is removed in API version 48.0 and later. Use the
FormulaFunctionAllowedType on page 2789 object instead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The formula function label that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the formula function.


### Standard Objects FormulaFunctionAllowedType

Usage

Query FormulaFunction to search for available formula functions, such as `AND()`, `ISBLANK()`, `MAX()`, `MIN()`, and others.

### FormulaFunctionAllowedType

Represents the functions that are supported in the given formula context. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DurableId

FunctionId

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the supported function.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
### FormulaFunction

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects FormulaFunctionCategory

**Field** **Details**

**Description**
The name of the formula type in which the function is supported.

Possible values are:

**•** `FLOW`

**•** `VALIDATION`

**•** `VISUALFORCE`

### FormulaFunctionCategory

Represents the category to which a formula belongs when building a formula. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
DurableId

Label

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the field. Always retrieve this value before using it, as the value isn’t
guaranteed to stay the same from one release to the next. To simplify queries, use this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label of the FormulaFunctionCategory that appears in the user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the FormulaFunctionCategory.


### Standard Objects FrcstCustmCatgRampRateSrc

Usage

Query FormulaFunctionCategory to search for categories of available formula functions, such as `Math`, `Logical`, `Date and Time`,
and others.

### FrcstCustmCatgRampRateSrc

Represents the total contract value used for custom bulk adjustments. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BaseValueFrcstSrcDefinitionId

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The DMO that contains the field in which the total contract value exists. This field is a
relationship field.

**Relationship Name**
BaseValueFrcstSrcDefinition

**Refers To**
ForecastingSourceDefinition

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


### Standard Objects FrcstCustmzAdjustment

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
ForecastingCustomCategoryId

Language

MasterLabel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the
FrcstCustmCatgRampRateSrc.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this FrcstCustmCatgRampRateSrc value. This display value is the internal label that
doesn't get translated.

### FrcstCustmzAdjustment

Represents an individual forecast manager’s adjustment of a subordinate’s consumption forecast. Available in API version 63.0 and later.
This object is different from the ForecastingAdjustment object, which represents managers’ adjustments of subordinates’ pipeline
forecasts.


Standard Objects FrcstCustmzAdjustment

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdjustedAmount

AdjustedQuantity

AdjustmentNote

ForecastingCustomCategoryId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text note providing information about the adjustment. The maximum length is 255
characters.

This field doesn’t appear in reports.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory


Standard Objects FrcstCustmzAdjustment

**Field** **Details**

```
ForecastingTypeId

IsAmount

IsQuantity

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related forecasting type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, IsQuantity must be
set to `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the adjustment is made in a quantity amount. If `false`, IsAmount must be set to
`true` .

The default value is `false` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the forecast owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


### Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

```
PeriodId

Territory2Id

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Period ID for the adjustment.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period

**Type**
reference

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FrcstCustmzAdjustmentChangeEvent on page 68**
Change events are available for the object.

**FrcstCustmzAdjustmentFeed on page 55**
Feed tracking is available for the object.

**FrcstCustmzAdjustmentHistory on page 63**
History is available for tracked fields of the object.

**FrcstCustmzAdjustmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FrcstCustmzAdjustmentShare on page 67**
Sharing is available for the object.

### FrcstCustmzOwnerAdjustment

Represents an individual forecast user’s adjustment of their own consumption forecast. Available in API version 63.0 and later. This object
is different from the ForecastingOwnerAdjustment object, which represents users’ adjustments of their pipeline forecasts.


Standard Objects FrcstCustmzOwnerAdjustment

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AdjustedAmount

AdjustedQuantity

AdjustmentNote

CustomDimension

ForecastingCustomCategoryId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue amount of an individual forecast item, after an adjustment.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity amount of an individual forecast item, after an adjustment.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text note providing information about the adjustment. The maximum length is 255
characters.

This field doesn’t appear in reports.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the additional dimension of the forecasting adjustment. For example, account ID,
use case ID.

Any data imported from an external source must be exactly 15 characters.

**Type**
reference


Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the forecasting custom category.

This field is a relationship field.

**Relationship Name**
ForecastingCustomCategory

**Refers To**
ForecastingCustomCategory

```
ForecastingTypeId

IsAmount

IsQuantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related forecasting type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, then the adjustment is made in a revenue amount. If `false`, IsQuantity must be
set to `true` .

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the adjustment is made in a quantity amount. If `false`, IsAmount must be set to
`true` .

The default value is `false` .


Standard Objects FrcstCustmzOwnerAdjustment

**Field** **Details**

```
OwnerId

PeriodId

Territory2Id

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the forecast owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Period ID for the adjustment.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period

**Type**
reference

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FrcstCustmzOwnerAdjustmentChangeEvent on page 68**
Change events are available for the object.

**FrcstCustmzOwnerAdjustmentFeed on page 55**
Feed tracking is available for the object.


### Standard Objects FulfillmentOrder

**FrcstCustmzOwnerAdjustmentHistory on page 63**
History is available for tracked fields of the object.

**FrcstCustmzOwnerAdjustmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**FrcstCustmzOwnerAdjustmentShare on page 67**
Sharing is available for the object.

### FulfillmentOrder

Represents a group of products, fees, and delivery charges on a single order that share the same fulfillment location, delivery method,
and recipient. The FulfillmentOrderLineItems belonging to a FulfillmentOrder are associated with OrderItemSummary objects belonging
to a single OrderSummary. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
AccountId

ActiveDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Account or Person Account associated with the FulfillmentOrder. It represents the
shopper in the storefront.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
datetime


Standard Objects FulfillmentOrder

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the FulfillmentOrder becomes active.

This field is available in API version 61.0 and later.

```
BillToContactId

ClosedDate

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with the FulfillmentOrder. It represents the shopper in the
storefront when not using person accounts.

This field is available in API version 49.0 and later.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
datetime

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the FulfillmentOrder closed. Automatically entered.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the OrderSummary associated with the FulfillmentOrder.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro


Standard Objects FulfillmentOrder

**Field** **Details**

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.

```
DeliveryDate

DeliveryMethodId

FulfilledFromLocationId

```

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the FulfillmentOrder was delivered.

This field is a relationship field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the DeliveryMethod used for this FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location handling this FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
FulfilledFromLocation

**Relationship Type**
Lookup

**Refers To**
Location


Standard Objects FulfillmentOrder

**Field** **Details**

```
FulfilledToAddress

FulfilledToCity

FulfilledToCountry

FulfilledToEmailAddress

FulfilledTo

GeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Address of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address country.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the recipient.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy of the geocode for the recipient address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`


Standard Objects FulfillmentOrder

**Field** **Details**

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
FulfilledToLatitude

FulfilledToLongitude

FulfilledToName

FulfilledToPhone

FulfilledToPostalCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLongitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLatitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name on the recipient address.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Recipient address postal code.

```
FulfilledToState

FulfilledToStreet

FulfillmentOrderNumber

GrandTotalAmount

InvoiceId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address street.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrder.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the products, fees, and delivery charges on the
FulfillmentOrder. This amount includes all FulfillmentOrderLineItems associated with the
FulfillmentOrder. This amount is equal to TotalAmount + TotalTaxAmount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Invoice associated with the FulfillmentOrder.

This field is a relationship field.


Standard Objects FulfillmentOrder

**Field** **Details**

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

```
IsReship

IsSuspended

ItemCount

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the FulfillmentOrder is for a reshipment. The default value is false.

This field is available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the FulfillmentOrder is suspended. The default value is false.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the quantities of the FulfillmentOrderLineItems included in the FulfillmentOrder.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Timestamp for when the current user last viewed this record. A null value can mean that this
record has only been referenced (LastReferencedDate) and not viewed.

```
OrderId

OrderSummaryId

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original Order that generated the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderSummary associated with the FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this FulfillmentOrder. Default value is the User logged in
to the API to perform the create.

This field is a polymorphic relationship field.


Standard Objects FulfillmentOrder

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ProcessingTimeInMinutes

StartFulfillmentDate

Status

```

**Type**
long

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
How many minutes it took to process the FulfillmentOrder, from the start of processing to
completion.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the fulfillment process was started for the FulfillmentOrder.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Status of the FulfillmentOrder. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes,
but the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.

Default values are:

**•** `Allocated` (Activated)

**•** `Assigned` (Fulfilling)

**•** `Cancelled` (Cancelled)

**•** `Draft` (Draft)

**•** `Fulfilled` (Closed)

**•** `Pick Complete` (Fulfilling) This value is available in API v56.0 and later.

**•** `Pickpack` (Fulfilling)

**•** `Printed` (Fulfilling) This value is available in API v56.0 and later.

**•** `Rejected` (Rejected) This value is available in API v56.0 and later.


Standard Objects FulfillmentOrder

**Field** **Details**

```
StatusCategory

TaxLocaleType

TotalAdjustmentAmount

TotalAdjustment

AmtWithTax

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each status category corresponds to one or more statuses.

Possible values are:

**•** `ACTIVATED` —Activated

**•** `CANCELLED` —Cancelled

**•** `CLOSED` —Closed

**•** `DRAFT` —Draft

**•** `FULFILLING` —Fulfilling

**•** `REJECTED` —Rejected This value is available in API v56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system used to handle tax on the original Order associated with the FulfillmentOrder.
Gross usually applies to taxes like value-added tax (VAT), and Net usually applies to taxes like
sales tax.

Possible values are:

**•** `Gross` (displays most prices and taxes as combined values)

**•** `Net` (displays most prices and taxes as separate values)

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the FulfillmentOrder. This
value only includes adjustments to FulfillmentOrderLineItems of type code Product, not
adjustments to delivery charges or fees.

**Type**
currency


Standard Objects FulfillmentOrder

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the products on the Fulfillment Order,
inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of type
code Product. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.

```
TotalAdjustmentTaxAmount

TotalAmount

TotalDelivery

AdjustAmount

TotalDeliveryAdjust

AmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Adjusted total, not including tax, of the FulfillmentOrderLineItems, including products, fees,
and delivery charges, on the Fulfillment Order.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the Fulfillment
Order. This value only includes adjustments to FulfillmentOrderLineItems of type Delivery
Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges on the Fulfillment
Order, inclusive of tax. This value only includes adjustments to FulfillmentOrderLineItems of
type Delivery Charge. This amount is equal to TotalDeliveryAdjustAmount +
TotalDeliveryAdjustTaxAmount.


Standard Objects FulfillmentOrder

**Field** **Details**

This field is available in API version 49.0 and later.

```
TotalDelivery

AdjustTaxAmount

TotalDeliveryAmount

TotalDeliveryAmtWithTax

TotalDeliveryTaxAmount

TotalFeeAdjustAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAdjustAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges on the FulfillmentOrder. This value only includes
FulfillmentOrderLineItems of type Delivery Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the delivery charges on the FulfillmentOrder, inclusive of tax. This value only
includes FulfillmentOrderLineItems of type Delivery Charge. This amount is equal to
TotalDeliveryAmount + TotalDeliveryTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalDeliveryAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the fees on the FulfillmentOrder. This value
only includes adjustments to FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.


Standard Objects FulfillmentOrder

**Field** **Details**

```
TotalFeeAdjustAmtWithTax

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
Total amount of the price adjustments applied to the fees on the FulfillmentOrder, inclusive
of tax. This value only includes adjustments to FulfillmentOrderLineItems of type Fee. This
amount is equal to TotalFeeAdjustAmount + TotalFeeAdjustTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalFeeAdjustAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the fees on the FulfillmentOrder, excluding adjustments and tax. This value
only includes FulfillmentOrderLineItems of type Fee.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the fees on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type Fee. This amount is equal to TotalFeeAmount +
TotalFeeTaxAmount.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Tax on the TotalFeeAmount.

This field is available in API version 56.0 and later.

```
TotalProductAmount

TotalProductAmtWithTax

TotalProductTaxAmount

TotalTaxAmount

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the products on the FulfillmentOrder, excluding order adjustments, delivery
charges, and fees. This value only includes FulfillmentOrderLineItems of type code Product.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the products on the FulfillmentOrder, inclusive of tax. This value only includes
FulfillmentOrderLineItems of type code Product. This amount is equal to TotalProductAmount
+ TotalProductTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalProductAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects FulfillmentOrder

**Field** **Details**

**Description**
Type of the FulfillmentOrder. Each type corresponds to one type category, shown here in
parentheses. You can customize the type picklist to represent your business processes, but
the type category picklist is fixed because processing is based on those values. If you customize
the type picklist, include at least one type value for each type category.

Default values are:

**•** `Download` (Digital)

**•** `Email` (Digital)

**•** `In Store Pickup` (Physical)

**•** `Retail Store` (Physical)

**•** `Supplier` (Drop Ship)

**•** `Warehouse` (Physical)

```
TypeCategory

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type category of the FulfillmentOrder. Processing of the FulfillmentOrder depends on this
value. Each type category corresponds to one or more types.

Possible values are:

**•** `DIGITAL` —Digital

**•** `DROPSHIP` —Drop Ship

**•** `PHYSICAL` —Physical

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[FulFillmentOrderChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[FulfillmentOrderFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[FulfillmentOrderOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.


### Standard Objects FulfillmentOrderItemAdjustment

**[FulfillmentOrderShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

SEE ALSO:

FulfillmentOrderLineItem

Order

OrderSummary

### FulfillmentOrderItemAdjustment

Represents a price adjustment on a FulfillmentOrderLineItem. Corresponds to an OrderItemAdjustmentLineSummary associated with
the corresponding OrderItemSummary. This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
Amount

CampaignName

CouponName

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount, not including tax, of the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Campaign associated with the adjustment.

**Type**
string


Standard Objects FulfillmentOrderItemAdjustment

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon associated with the adjustment.

```
CurrencyIsoCode

Description

FulfillmentOrderId

FulfillmentOrderItem

AdjustmentNumber

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the adjustment applies.
The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem to which the
adjustment applies.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItemAdjustment.


Standard Objects FulfillmentOrderItemAdjustment

**Field** **Details**

```
FulfillmentOrder

LineItemId

OrderItemAdjust

LineSummaryId

PromotionName

TotalAmtWithTax

TotalTaxAmount

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrderLineItem to which this adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemAdjustmentLineSummary associated with the adjustment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Promotion associated with the adjustment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects FulfillmentOrderItemTax

**Field** **Details**

**Description**
Tax on the Amount.

SEE ALSO:

### FulfillmentOrder FulfillmentOrderItemTax

FulfillmentOrderLineItem

OrderItemAdjustmentLineSummary

### FulfillmentOrderItemTax

Represents the tax on a FulfillmentOrderLineItem or FulfillmentOrderItemAdjustment. Corresponds to an OrderItemTaxLineItemSummary.
This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
Amount

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Sort

**Description**
Amount of tax represented by the FulfillmentOrderItemTax.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects FulfillmentOrderItemTax

**Field** **Details**

**Description**
ISO code for the currency of the FulfillmentOrderLineItem to which the tax applies. The
default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

```
Description

FulfillmentOrderId

FulfillmentOrder

ItemAdjustId

FulfillmentOrderItem

TaxNumber

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the FulfillmentOrderItemTax.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated FulfillmentOrder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this object represents tax on an adjustment, this value is the ID of the
FulfillmentOrderItemAdjustment to which the tax applies. If this value is null, the adjustment
applies to a FulfillmentOrderLineItem.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderItemTax.


Standard Objects FulfillmentOrderItemTax

**Field** **Details**

```
FulfillmentOrder

LineItemId

OrderItemTaxLineItem

SummaryId

Rate

TaxEffectiveDate

Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If this object represents tax on a FulfillmentOrderLineItem, this value is the ID of that
FulfillmentOrderLineItem. If this object represents tax on an adjustment, this value is the ID
of the FulfillmentOrderLineItem to which the adjustment applies.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemTaxLineItemSummary associated with the OrderItemSummary that
corresponds to the FulfillmentOrderLineItem to which the tax applies.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tax rate used to calculate the Amount.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date on which the Amount was calculated. Important due to tax rate changes over time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the Amount is actual or estimated.

Possible values are:

**•** `Actual`

**•** `Estimated`


### Standard Objects FulfillmentOrderLineItem

**FulFillmentOrderItemTaxChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

### FulfillmentOrder

FulfillmentOrderItemAdjustment

### FulfillmentOrderLineItem

OrderItemTaxLineItemSummary

### FulfillmentOrderLineItem

Represents a product or delivery charge belonging to a FulfillmentOrder. Corresponds to an OrderItemSummary. This object is available
in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the FulfillmentOrder associated with the FulfillmentOrderLineItem.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

This field is available in API version 49.0 and later.


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
Description

EndDate

FulfillmentOrderId

FulfillmentOrder

LineItemNumber

GrossUnitPrice

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the FulfillmentOrderLineItem.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
End date of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the FulfillmentOrder associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
FulfillmentOrder

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Description**
Unit price, including tax, of the FulfillmentOrderLineItem. This value is equal to TotalPrice +
TotalTaxAmount.

This field is available in API version 49.0 and later.

```
IsReship

MainFulfillmentOrderLineItemId

OrderItemId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the FulfillmentOrderLineItem belongs to a reshipment. The default value
is false.

This field is available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original FulfillmentOrderLineItem.

This field is a relationship field.

This field is available in API version 63.0 and later.

**Relationship Name**
FulfillmentOrderLineItem

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrderLineItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the original OrderItem for the OrderItemSummary associated with the
FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItem

**Relationship Type**
Lookup


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Refers To**
OrderItem

```
OrderItemSummaryId

OriginalQuantity

Product2Id

Quantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the OrderItemSummary associated with the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
OrderItemSummary

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Original quantity of the FulfillmentOrderLineItem.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the product represented by the FulfillmentOrderLineItem.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
Current quantity of the FulfillmentOrderLineItem. Equal to the original quantity minus any
canceled quantity.

```
QuantityUnitOfMeasure

RejectedQuantity

RejectReason

ReshipReason

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unit of measure of the quantity, for example: unit, gallon, ton, or case.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used by the Distributed Order Management package and Store Fulfillment app to store the
quantity that has been rejected by a fulfillment location.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the FulfillmentOrderLineItem was rejected by a fulfillment location, the reason for the
rejection.

Default values are:

**•** `Damaged`

**•** `Just Sold`

**•** `Other`

**•** `Out of Packing Supplies`

**•** `Out of Stock`

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Description**
If the FulfillmentOrderLineItem belongs to a reshipment, the reason for the reshipment.

Default values are:

**•** `Damaged`

**•** `Lost`

**•** `Unknown`

**•** `Wrong Item`

This field is available in API version 53.0 and later.

```
ServiceDate

ScopeIdentifierText

TotalAdjustmentAmount

TotalAdjustment

AmountWithTax

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Service or start date of the FulfillmentOrderLineItem.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unique identifier used to identify the scope in which this fulfillment order line item record
is created.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of any price adjustments applied to the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the FulfillmentOrderLineItem, inclusive of
tax. This amount is equal to TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

```
TotalAdjustment

TaxAmount

TotalAmount

TotalLineAmount

TotalLineAmountWithTax

TotalLineTaxAmount

TotalPrice

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the FulfillmentOrderLineItem.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the FulfillmentOrderLineItem, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects FulfillmentOrderLineItem

**Field** **Details**

**Description**
Total, including adjustments but not tax, of the FulfillmentOrderLineItem. Equal to UnitPrice
times Quantity.

```
TotalTaxAmount

Type

TypeCode

UnitPrice

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalPrice.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of the FulfillmentOrderLineItem. Matches the type of the associated OrderItemSummary.
Delivery Charge indicates that the FulfillmentOrderLineItem represents a delivery charge.
Fee indicates that it represents another type of fee, such as a return fee. Order Product
indicates that it represents any other type of product, service, or charge. Each type corresponds
to one type code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge` (Charge)

**•** `Fee` (Charge) This value is available in API v56.0 and later.

**•** `Order Product` (Product)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type code of the FulfillmentOrderLineItem. Matches the type code of the associated
OrderItemSummary. Processing depends on this value. Charge indicates that the
FulfillmentOrderLineItem represents a charge or fee. Product indicates that it represents any
other type of product, service, or charge. A type code can be associated with one or more
types.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
currency


### Standard Objects FunctionConnection

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
Unit price of the FulfillmentOrderLineItem.

**[FulFillmentOrderChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

SEE ALSO:

FulfillmentOrder

FulfillmentOrderItemAdjustment

FulfillmentOrderItemTax

OrderItemSummary

### FunctionConnection

Represents a connection between an org and Salesforce Functions. This object is available in API version 52.0 and later.

In API version 53.0, the name of this object was changed from SfFunctionsConnection to FunctionConnection.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Error

FunctionsAccountLoginOrg

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error string, if any, for the connection between the org and Salesforce Functions.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects FunctionConnection

**Field** **Details**

**Description**
The Salesforce Functions account login org.

```
FunctionsAccountName

FunctionsAccountUuid

Sequence

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce Functions account name.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique Salesforce Functions account UUID. This is a generated ID that is not in Salesforce
object ID format.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Sequence number for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the connection between the org and Salesforce Functions.

Possible values are:

**•** `Attempted`

**•** `None`

**•** `TrustedBiDirection`

**•** `TrustedUniDirection`

The default value is 'None'. `TrustedBiDirection` indicates the connection is fully
established.


### Standard Objects FunctionInvocationRequest

Usage

FunctionConnection is not intended for direct use and should be treated as a read-only object that represents the current connection
information between your org and Salesforce Functions. To create and manage connections between your org and Salesforce Functions
[use the steps and commands described in the Salesforce Functions developer documentation.](https://developer.salesforce.com/docs/platform/functions/guide/index.html)

FunctionConnection is not supported in Trialforce templates or org snapshots.

### FunctionInvocationRequest

Represents invocation information for a Salesforce Function. This object is available in API version 51.0 and later.

When a Salesforce Function is invoked using the Apex `functions.Function` invoke methods, a FunctionInvocationRequest
record is created that contains information on the status and results of the invocation.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`, `update()`

Fields

**Field** **Details**

```
CallbackStatus

ExecutionTime

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the callback for asynchronous invocations. This field is new in API version 52.0.

Possible values are:

**•** `Completed`  - Not used for the Salesforce Functions beta.

**•** `Enqueued`  - The Function has completed (either successfully or unsuccessfully), and
the callback has been enqueued for asynchronous execution in the Salesforce org.

**•** `Failed`  - Not used for the Salesforce Functions beta.

**•** `PendingResponse`  - The Function has not yet completed, so the callback has not
been called yet.

The default value is 'PendingResponse'.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The execution time of the Function in milliseconds.


Standard Objects FunctionInvocationRequest

**Field** **Details**

```
ExtendedResponse

FunctionName

InvokingNamespacePrefix

NamespacePrefix

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
JSON object with additional information about the result of the Function execution.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the Function that was invoked. This name is case-sensitive and uses the format
“ `project name`   - `function name` ”

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Prefix of the namespace that invokes the function. A namespace can invoke the global
function using an installed package via Apex.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. This object is available in API version
53.0 and later. Each Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component in a managed package
by using the `namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


Standard Objects FunctionInvocationRequest

**Field** **Details**

```
OwnerId

ResponseBody

ResponseContentType

ResponseLength

ResponseName

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The owner of the FunctionInvocationRequest.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
base64

**Properties**
Nillable, Update

**Description**
Response body of the invoked Function.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Content type of the response body of the invoked Function. For example, the content type
could be `application/json`, `text/csv`, or various other values depending on what
the Function returned.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the response body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects FunctionInvocationRequest

**Field** **Details**

**Description**
Name of response, not currently used.

```
ResponseUncompressedLength

StackTrace

Status

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Uncompressed length of the Function response, if the response content was compressed.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
If there was an error invoking the function, this field contains the Function stack trace.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the invoked Function. Functions that are invoked asynchronously can be in a queued
`InProgress` state before they are invoked.

Possible values are:

**•** `Dispatched`  - Not used for the Salesforce Functions beta.

**•** `Error`  - The Function failed to execute due to either an error starting the Function, or
an error while the Function was running.

**•** `FunctionInProgress`  - The Function invocation has been sent to the Salesforce
Functions compute environment, and is running.

**•** `InProgress`  - The Function invocation request has been enqueued.

**•** `New`  - The Function invocation request has been created, but not enqueued yet.

**•** `Success`  - The Function has completed execution. For status on whether the callback
has been called, see the CallbackStatus field.

The default value is 'New'.

Treat FunctionInvocationRequest records as read-only records used to get information about a specific Function invocation. To invoke
Functions, use the Apex `functions.Function` class invoke methods.


### Standard Objects FunctionReference

FunctionInvocationRequest is not supported in Trialforce templates or org snapshots.

### FunctionReference

Represents a deployed Salesforce Function associated with an org. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Access

Description

FunctionName

ImageReference

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The label for whether managed components can access across namespaces.

Possible values are:

**•** `Global` —The managed components can access across namespaces.

**•** `Public` —The managed components can access within the same namespace.

The default value is `Public` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Function.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The developer name of the Function. This name is case sensitive and uses the format
“ `project name`   - `function name` ”. This field is unique within your organization.

**Type**
reference


Standard Objects FunctionReference

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Stores details about an image associated with a function. This is internal only, used by
packaging only, and should not be editable or set by the customer.

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
The language code for the Function, such as “en_US”.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the Function.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. This object is available in API version
53.0 and later. Each Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component in a managed package
by using the `namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


### Standard Objects GenAIConversationSummary

Usage

Treat FunctionReference records as read-only records used to get information about a specific Function associated with your org. To
invoke Functions, use the Apex `functions.Function` class invoke methods. To deploy and associate Functions with your org,
[use Salesforce CLI commands associated with Functions, as described in the Salesforce Functions developer documentation.](https://developer.salesforce.com/docs/platform/functions/guide/index.html)

FunctionReference is not supported in Trialforce templates or org snapshots.

### GenAIConversationSummary

Represents a generated summary of a voice or video call. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, Einstein Conversation Insights and Einstein for Sales must be enabled in your org.

Fields

**Field** **Details**

```
ConversationRecordId

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the related voice or video call record.

This field is a polymorphic relationship field.

**Relationship Name**
ConversationRecord

**Relationship Type**
Master-detail

**Refers To**
VideoCall, VoiceCall (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects GenAIConversationSummary

**Field** **Details**

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

Possible values are:

**•** `MXN` —Mexican Peso

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
ErrorMessage

Source

Status

Summary

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An error message when there is a problem with sharing the conversation summary.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Whether the summary shown is content generated by Einstein or subsequently edited by a
user.

Possible values are:

**•** `EINSTEIN_GPT` —Einstein

**•** `USER_EDITED` —User Edited

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the summary.

Possible values are:

**•** `ERROR` —Error

**•** `GENERATING` —Generating

**•** `SUCCESS` —Success

**Type**
textarea


### Standard Objects GenAiFunctionDefinition

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The summary text content.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**GenAIConversationSummaryChangeEvent on page 68**
Change events are available for the object.

**GenAIConversationSummaryFeed on page 55**
Feed tracking is available for the object.

**GenAIConversationSummaryHistory on page 63**
History is available for tracked fields of the object.

**GenAIConversationSummaryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**GenAIConversationSummaryShare on page 67**
Sharing is available for the object.

### GenAiFunctionDefinition

Represents an agent action. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea

**Properties**
Create, Update


Standard Objects GenAiFunctionDefinition

**Field** **Details**

**Description**
A description explaining the general purpose and domain of the action.

```
DeveloperName

InvocationTarget

InvocationTargetType

IsConfirmationRequired

IsLocal

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target invocation used by invocation operations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Invocable action types used by invocation operations.

Possible values are:

**•** `apex`

**•** `flow`

**•** `generatePromptResponse`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether confirmation is required for this action.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects GenAiFunctionDefinition

**Field** **Details**

**Description**
This field is a calculated field and is set to `true` if this action is an edited version of a standard
action.

The default value is `false` .

```
Language

LocalDeveloperName

MasterLabel

NamespacePrefix

ParentId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the GenAiFunctionDefinition. The value for this field is the language value
of the org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name for this action within a topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the generative AI action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiFunctionDefinition.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the action.

This field is a relationship field.


Standard Objects GenAiFunctionDefinition

**Field** **Details**

**Relationship Name**
Parent

**Refers To**
GenAiPlannerFunctionDef

```
PlannerId

PluginId

Source

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent planner service for this action.

This field is a relationship field.

**Relationship Name**
Planner

**Refers To**
GenAiPlannerDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent topic for this agent action.

This field is a relationship field.

**Relationship Name**
Plugin

**Refers To**
GenAiPluginDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The optional source standard or custom action from which this action's configuration,
including description, input, and output, is copied. If there's no value, the action is used only
within the parent topic.


### Standard Objects GenAiPlannerDefinition GenAiPlannerDefinition

Represents an agent planner service that uses a large language model (LLM) and a reasoning strategy to decompose a given task into
smaller subtasks, identify the most suitable actions for each subtask, and invoke them. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
Capabilities

Description

DeveloperName

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A set of tags associated with the agent planner service definition.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description explaining the general purpose and domain of the agent planner service
definition.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects GenAiPlannerFunctionDef

**Field** **Details**

**Description**
The language of the GenAiPlannerDefinition. The value for this field is the language value
of the org.

```
MasterLabel

NamespacePrefix

PlannerType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the agent planner service definition.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiPlannerDefinition.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A particular approach to problem solving that is given as prompt instructions to a large
language model (LLM).

Possible values are:

**•** `AiCopilot__ReAct` —Uses a reactive planning strategy to solve problems with the
LLM. This strategy consists of prompting the LLM to generate the next step in response
to an event and the current context. It differs from a sequential planner in that it doesn’t
plan more than one step ahead of time.

**•** `AiCopilot__SequentialPlannerIntentClassifier` —Uses an intent
classifier prompt and a sequential planner prompt. With each text input, the planner
asks the LLM to generate a step-by-step plan to finish the goal. It plans first, then executes.

### GenAiPlannerFunctionDef

Represents a relationship between the agent planner service and agent actions. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects GenAiPluginDefinition

Special Access Rules

To access this object, Agents must be enabled in your org.

Fields

**Field** **Details**

```
PlannerId

Plugin

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
Planner

**Relationship Type**
Lookup

**Refers To**
GenAiPlannerDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A set of actions that contextualize the agent planner service.

### GenAiPluginDefinition

Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents. This object is available in
API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Agents must be enabled in your org.


Standard Objects GenAiPluginDefinition

Fields

**Field** **Details**

```
CanEscalate

Description

DeveloperName

IsLocal

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this topic is eligible for escalation to a rep.

The default value is `false` .

**Type**
textarea

**Properties**
Create, Update

**Description**
The description of the topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the API name of the topic. Can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is a calculated field and is set to `true` if this topic is an edited version of a standard
topic.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the topic.


Standard Objects GenAiPluginDefinition

**Field** **Details**

```
LocalDeveloperName

MasterLabel

NamespacePrefix

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name for this topic within an agent.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of these values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the topic.

This field is a polymorphic relationship field.

**Relationship Name**
Parent


Standard Objects GenAiPluginDefinition

**Field** **Details**

**Refers To**
GenAiPlannerDefinition, GenAiPlannerFunctionDef

```
PlannerId

PluginType

Scope

Source

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent planner service for this topic.

This field is a relationship field.

**Relationship Name**
Planner

**Refers To**
GenAiPlannerDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `APICustomTopic`

**•** `Topic`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A specific job description for a topic.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The optional source standard or custom topic from which this topic's configuration, including
description, instructions, and utterances, is copied. If there's no value, the topic is used only
within this agent version.


### Standard Objects GeoCountry GeoCountry

Represents a country. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The GeoCountry object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
Description

IsoCode

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Two-letter ISO code of the country as defined in the org’s State-Country picklist. This field is
unique within your organization

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


Standard Objects GeoCountry

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.

```
Name

OwnerId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the country that corresponds with the ISO code.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the GeoCountry record. By default, the asset owner is the user who created
the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**GeoCountryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**GeoCountryShare on page 67**
Sharing is available for the object.

SEE ALSO:

GeoState

TaxGeoConfig


### Standard Objects GeolocationBasedAction GeolocationBasedAction

Represents a geolocation-based action, which is an action that’s triggered when a user enters, exits, or is within the area of the associated
object. Available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field** **Details**

```
ActionData

ActionType

Description

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the selected action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action.

Possible values are:

**•** `PlatformAlert`

**•** `QuickAction`

**•** `ViewRecord`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the action.


Standard Objects GeolocationBasedAction

**Field** **Details**

```
InitialTimeInvoked

LastReferencedDate

LastTimeInvoked

LastViewedDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the first time the mobile worker invoked this action.

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
Create, Filter, Nillable, Sort, Update

**Description**
Captures the last time the mobile worker invoked this action.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the action.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects GeolocationBasedAction

**Field** **Details**

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
Radius

ReferenceRecordId

TriggerType

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distance in meters from the location of the associated object that triggers the action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record that the action is associated with.

This field is a relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The event that triggered this action.

Possible values are:

**•** `GeoFenceEnter` —Enter

**•** `GeoFenceExit` —Exit


### Standard Objects GeoState GeoState

Represents a state. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The GeoState object is available if B2B Commerce or D2C Commerce is enabled.

Fields

**Field** **Details**

```
Description

GeoCountryId

IsoCode

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the GeoCountry associated with this GeoState.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
string

**Properties**
Create, Filter, Group, Sort


### Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**Description**
Two-letter ISO code of the state as defined in the org’s State-Country picklist. This field is
unique within your organization

```
LastReferencedDate

LastViewedDate

Name

```

SEE ALSO:

GeoCountry

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
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the state that corresponds with the ISO code.

### GtwyProvPaymentMethodType

The gateway provider payment method type allows integrators and payment providers to choose an active payment to receive an
order's payment data rather than allowing the Salesforce Order Management platform to select a default payment method. This object
is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`


Standard Objects GtwyProvPaymentMethodType

Fields

**Field** **Details**

```
Comments

DeveloperName

GtwyProviderPaymentMethodType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Users can provide additional details about the gateway provider payment method type
record. Supports a maximum of 1000 characters.

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

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, Salesforce generates one for
each record, which slows performance.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links the Salesforce payment method to the payment method used in the Salesforce Order
Management storefront. Your payment gateway integration uses this field when finding a
payment method to link to a payment.

The value of `GtwyProviderPaymentMethodType` must match the payment method
value sent to the order's Payment Instrument in Salesforce Order Management.

Listed below are several examples of payment method values that Salesforce could receive
from Salesforce Order Management.

**•** `CREDIT_CARD`

**•** `BASIC_CREDIT`

**•** `CreditCard`

**•** `GooglePay`


Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**•** `ApplePay`

```
Language

LastViewedDate

MasterLabel

NamespacePrefix

PaymentGatewayProviderId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the payment gateway integration.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view `(LastReferencedDate)`
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The gateway provider payment method type name that appears in the user
interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace of the payment gateway integration classes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the payment gateway provider that Salesforce Order Management should use
when processing payments. One payment gateway provider can be related to multiple
payment method types.

This is a relationship field.


Standard Objects GtwyProvPaymentMethodType

**Field** **Details**

**Relationship Name**
PaymentGatewayProvider

**Relationship Type**
Lookup

**Refers To**
PaymentGatewayProvider

```
PaymentMethodType

RecordTypeId

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of payment method used on an order in Salesforce Order Management.

Possible values are:

**•** `AlternativePaymentMethod`

**•** `CardPaymentMethod`

**•** `DigitalWallet`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type entity related to the gateway provider payment method type.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

The Salesforce Order Management payment record must have a `ProcessorId` field with the same value as the payment gateway's
`ExternalReferenceId` field. The gateway provider payment method type record must have a `PaymentMethodType` field
that looks up to the payment method that you want to associate to your payment. Finally, the payment gateway and gateway provider
payment method type must have matching `PaymentGatewayProviderId` fields. When you've established these relationships,
the payment record can infer your payment method from the gateway provider payment method type record.


### Standard Objects Goal Goal

The Goal object represents the components of a goal such as its name, description, and status.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CompletionDate

Description

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the goal.

**Type**
textarea


Standard Objects Goal

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the goal. The maximum length is 65,535 characters.

```
DueDate

ImageUrl

IsKeyCompanyGoal

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the goal is due.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the goal image. The image must be stored in Documents and set as
externally available. Applicable only to Goal objects of `Type` : Goal.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the goal is a key company goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this goal.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Goal

**Field Name** **Details**

**Description**
The timestamp that indicates when a user last viewed this goal. If this value is
null, this record might have been only referenced ( `LastReferencedDate` )
and not viewed.

```
Name

OwnerId

Progress

StartDate

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the goal. The maximum length is 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the goal.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The progress of the goal measured as a percentage.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the goal.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the goal.

Possible values:

**•** Draft


### Standard Objects GoalLink

**Field Name** **Details**

**•** Published

**•** Completed

**•** Canceled

**•** Not Completed

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**GoalFeed**

Feed tracking is available for the object.

**GoalHistory**

History is available for tracked fields of the object.

**GoalOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**GoalShare**

Sharing is available for the object.

### GoalLink

Represents the relationship between two goals. This is a many-to-many relationship, meaning that each goal can link to many other
goals.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated name of the goal link.


### Standard Objects GoogleDoc

**Field Name** **Details**

```
ParentGoalId

SubgoalId

### GoogleDoc

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the parent goal.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the subgoal.

Represents a link to a Google Document. This object is available in API version 14.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available in **All** Editions except **Database.com** for Google Apps Premier Edition accounts. See the Salesforce online help
for more information.

Fields

**Field** **Details**

```
Name

Owner

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the Google document.

**Type**
reference


### Standard Objects Group

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The ID of the user who currently owns this Google Document. Default value is the
user logged in to the API to perform the create.

```
ParentId

Url

### Group

```

A set of User records.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the attachment's parent object. The following objects are supported
as parents of Google documents: Account, Asset, Campaign, Case, Contact, Contract,
Custom Object Behavior, Lead, Opportunity, Product2, and Solution.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The URL of the Google document.

### Groups are sets of users. They can contain individual users, other groups, the users in a particular role or territory, or the users in a particular

role or territory plus all the users below that role or territory in the hierarchy.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `search()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Authenticated internal and external users can access this object.


Standard Objects Group

Fields

**Field** **Details**

```
Description

DefaultDivision

DeveloperName

DoesIncludeBosses

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the group. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. This name is unique
by group type and corresponds to **Group Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Only your Salesforce org’s internal users can access this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether records shared with users in this group are also shared with users
higher in the role hierarchy ( `true` ) or not ( `false` ). This field is only available for public


Standard Objects Group

**Field** **Details**

groups. This field corresponds to the Grant Access Using Hierarchies checkbox in Setup.
This field is available in API version 18.0 and later.

```
DoesSendEmailToMembers

Email

Name

OwnerId

QueueRoutingConfigId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is sent ( `true` ) or not sent ( `false` ) to the group members.
The email is sent to queue members as well.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address for a group of type Case. Applies only for a case queue.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the group. Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the group.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Organization, User

**Type**
reference


Standard Objects Group

**Field** **Details**

**Properties**
Create, Delete, Query, Retrieve, Update

**Description**
The ID of the queue routing configuration associated with the queue.

```
RelatedId

Type

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the associated groups. For groups of type “Role,” the ID of the
associated UserRole. The `RelatedId` field is polymorphic.

This is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
User, UserRole

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of the group. One of the following values:

**•** `AllCustomerPortal` —Public group that includes all Customer Portal or
Customer Community Plus users. This type is only available when a Customer Portal
or a Customer Site is enabled for your org.

**•** `ChannelProgramGroup` —Public group for partners in a channel program.

**•** `CollaborationGroup` —Chatter group.

**•** `Manager` —Public group that includes a user’s direct and indirect managers. This
group is read-only.

**•** `ManagerAndSubordinatesInternal` —Public group that includes a user
and the user’s direct and indirect reports. This group is read-only.

**•** `Organization` —Public group that includes all the User records in the
organization. This group is read-only.

**•** `Participant` —Compliant Data Sharing group that includes internal users who
have the Use Compliant Data Sharing permission. A group can contain other
participant groups only, or a group can contain both internal users with the Use


Standard Objects Group

**Field** **Details**

Compliant Data Sharing permission and other participant groups. This value is only
available when Compliant Data Sharing is enabled for your org.

**•** `PRMOrganization` —Public group that includes all the partners in an organization
that has the partner site or portal feature enabled.

**•** `Queue` —Public group that includes all the User records that are members of a
queue.

**•** `Regular` —Standard public group. When you `create()` a group, its type must
be `Regular`, unless a partner site or portal is enabled for the organization, in which
case the type can be `Regular` or `PRMOrganization` .

**•** `Role` —Public group that includes all the User records in a particular UserRole.

**•** `RoleAndSubordinates` —Public group that includes all the User records in a
particular UserRole and all the User records in any subordinate UserRole. Only available
when digital experiences is enabled for your org and Experience Cloud site users are
created with external account roles other than a shared person account role.

**•** `RoleAndSubordinatesInternal` —Public group that includes all the User
records in an internal UserRole, excluding customer and partner roles, and all the
User records in any subordinate internal UserRole.

**•** `SharingRecordCollGroup` —Public group that has access to a
SharingRecordCollection.

**•** `Territory` —Public group that includes all the User records in an organization
that has the territory feature enabled.

**•** `TerritoryAndSubordinates` —Public group that includes all the User records
in a particular UserRole and all the User records in any subordinateUserRole in an
organization that has the territory feature enabled.

Only `Personal`, `Regular`, and `Queue` can be used when creating a group. The
other values are reserved.

Usage

Unlike users, this object can be deleted.

Only public groups are accessible via the API. Personal groups are not available.

In API version 34.0 and later, you can query a group using `Related.Name` to retrieve the group’s name. `Related.Name` is
supported for public groups, user roles, territories, manager groups, and user names.

In API version 13.0 and later, if you delete a public group, it is deleted even if it has been used in sharing, consistent with the behavior
for UserRole. In versions before 13.0, such sharing prevents the record from being deleted.

SEE ALSO:

GroupMember

Overview of Salesforce Objects and Fields


### Standard Objects GroupMember GroupMember

Represents a User or Group that is a member of a public group.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
GroupId

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Group.

This is a relationship field.

**Relationship Name**
### Group

**Relationship Type**
Lookup

**Refers To**
### Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the User or Group that is a direct member of the group.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects GroupMembershipEventLog

Usage

If your group contains more than 10,000 members, for improved performance, you can adjust group membership using the GroupMember
API object instead of the group's detail page in Setup. You can also adjust membership using the public group's access summary or user
access policies in Setup.

A record exists for every User or Group who is a direct member of a public group whose `Type` field is set to Regular. User records that
are indirect members of Regular public groups aren't listed as group members. A User can be an indirect member of a group if he or
she is in a UserRole above the direct group member in the hierarchy, or if he or she is a member of a group that is included as a subgroup
in that group.

If you attempt to create a record that matches an existing record, the system simply returns the existing record.

SEE ALSO:

Overview of Salesforce Objects and Fields

### GroupMembershipEventLog

Group Membership events capture details about changes to public group and queue membership, such as when members are added
to or removed from the public group or queue. This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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
IP address of the client employing salesforce.com services.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects GroupMembershipEventLog

**Field** **Details**

**Description**
Amount of cpu cycles used by the request

```
GroupIdentifier

GroupType

LoginKey

MemberIdentifier

OperationType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the group whose membership changed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of group being updated.

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
The ID of the member added to or removed from the group. Public groups can contain
individual users, other groups, or users in a specified role or territory. Queues can contain
individual users, roles, public groups, territories, connections, or partner users.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of operation that occurred, such as a group member being added or removed from
a group.


Standard Objects GroupMembershipEventLog

**Field** **Details**

```
RequestIdentifier

RunTime

SessionKey

Timestamp

Uri

UserIdentifier

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
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects GuestBuyerProfile

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

### GuestBuyerProfile

Represents a store's guest buyer profile, which allows unauthenticated buyers to browse the store. This object is available in API version
51.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency displayed to the guest buyer when they’re viewing the store.

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Detailed description of the profile. Includes information like which store the profile is used
in.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were modified


### Standard Objects HashtagDefinition

**Field** **Details**

```
LastViewedDate

Name

### HashtagDefinition

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last date and time when one or more of the fields were viewed

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the guest buyer profile. Including a reference to the store helps with later
identification.

### HashtagDefinition represents hashtag (#) topics in public Chatter posts and comments. Public posts and comments include those on

profiles and in public groups, but not those on records or in private groups. This object is available in API version 26.0 and later.

Important: Starting in Spring ’16, API access to HashtagDefinition is disabled across all API versions. Any integrations relying on
API queries to this object stop working. You can continue to use hashtags in posts and comments, and the hashtags continue to
create corresponding topics. We recommend that you redirect all API queries and reports using the HashtagDefinition object to
[use the Topic object instead. For more information, see Retiring the Legacy HashtagDefinition Object—FAQs.](https://help.salesforce.com/apex/HTViewSolution?urlname=Retiring-the-Legacy-HashtagDefinition-Object)

Supported Calls

`delete(), describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
HashtagCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times a hashtag topic is used.


### Standard Objects HealthCareDiagnosis

**Field Name** **Details**

```
Name

NameNorm

NetworkId

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The string of characters following the hashtag (#) in a hashtag topic, normalized
to remove capitalization and punctuation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the HashtagDefinition belongs. This field
is available only if digital experiences is enabled in your org.

Use this object to identify public hashtag topics and see how often they’re used.

SEE ALSO:

Topic

### HealthCareDiagnosis

Represents information related to industry-standard healthcare diagnosis codes. Before the Spring ’21 release, the Healthcare Procedure
and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used for
prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set Bundle
objects for this purpose instead.


Standard Objects HealthCareDiagnosis

Example: The Code Set and Code Set Bundle objects improve on the old objects by adding support for terminology system
information. This added support comes in the form of the Source System and Version fields.

Note: Objects, flows, and apps that previously used Healthcare Diagnosis and Healthcare Procedure have been or will be
extended to support the use of Code Set and Code Set Bundle. Healthcare Diagnosis and Healthcare Procedure are to be
gradually phased out with future releases.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Code

CodeDescription

CodeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates the category for this diagnosis such as newborn, pediatric, maternity,
or adult.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry-standard diagnosis code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Description of the diagnosis code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

**Description**

Type of diagnosis code represented in the record such as ICD-9 or ICD-10.

```
EffectiveDate

EndDate

Gender

IsActive

IsComplicationOrComorbidity

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Start date for the code.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

End date for the code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether this diagnosis is for males, females, or all genders.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the diagnosis code is available for use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a complication or
comorbidity.


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

```
IsHospitalAcquiredCondition

IsMajorComplicationOrComorbidity

IsPresentOnAdmissionExempt

IsPrimaryDiagnosis

IsUnacceptablePrincipalDxIpAdmit

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis represents a condition acquired while in the
hospital.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a major complication or
comorbidity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is exempt from the diagnosis present on
admission requirement.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code can be used as primary diagnosis only, or can
be used in any diagnosis sequence.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is an unacceptable principal diagnosis for
inpatient admission per Medicare Code Edits.


Standard Objects HealthCareDiagnosis

**Field Name** **Details**

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
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the code that displays in search and lookup fields. Salesforce
recommends using the code along with the description to populate this field.
For example, use <Code>: <Description> or <Code>-<Description> such as
(E08.37X9 - Diabetes mellitus due to underlying condition).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects HealthCareProcedure

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[HealthCareDiagnosisChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareDiagnosisHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareDiagnosisOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareDiagnosisShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### HealthCareProcedure

Represents information related to industry-standard healthcare procedure codes. Before the Spring ’21 release, the Healthcare Procedure
and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used for
prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set Bundle
objects for this purpose instead.

Example: The Code Set and Code Set Bundle objects improve on the old objects by adding support for terminology system
information. This added support comes in the form of the Source System and Version fields.

Note: Objects, flows, and apps that previously used Healthcare Diagnosis and Healthcare Procedure have been or will be
extended to support the use of Code Set and Code Set Bundle. Healthcare Diagnosis and Healthcare Procedure are to be
gradually phased out with future releases.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Code

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Category of the procedure code such as anesthesia, surgery, radiology, and so
on.

**Type**
string


Standard Objects HealthCareProcedure

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry standard procedure code such as CPT or HCPCS.

```
CodeDescription

CodeShortDescription

CodeType

EffectiveDate

EndDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Description of the procedure code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Short description of the procedure code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Type of procedure code represented in the record such as CPT or HCPCS.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Start date for the code.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

End date for the code.


Standard Objects HealthCareProcedure

**Field Name** **Details**

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

Indicates whether the diagnosis code is available for use.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the code that displays in search and lookup fields. Salesforce
recommends using the code along with the description to populate this field.
For example, use <Code>: <Description> or <Code>-<Description> such as
95115: Allergy injection.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this record.


### Standard Objects Holiday

**Field Name** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[HealthCareProcedureChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareProcedureHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareProcedureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareProcedureShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

### Holiday

Represents a period of time during which your customer support team is unavailable. Business hours and escalation rules associated
with business hours are suspended during any holidays with which they are affiliated.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can’t access this object.

All users, even those without the “View Setup and Configuration” user permission, can view holidays via the API.

Fields

**Field** **Details**

```
ActivityDate

```

**Type**
date


Standard Objects Holiday

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the Holiday `IsAllDay` flag is set to `true` (indicating that it is an all-day holiday), then
the holiday due date information is contained in the `ActivityDate` field. This field is a
date field with a timestamp that is always set to midnight in the Coordinated Universal Time
(UTC) time zone. The timestamp is not relevant, and you should not attempt to alter it to
account for any time zone differences.

```
Description

EndTimeInMinutes

IsAllDay

IsRecurrence

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the holiday.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end time of the holiday in minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the duration of the holiday is all day ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the holiday is scheduled to repeat itself ( `true` ) or only occurs once
( `false` ). This is a read only field on update, but not on create. If this field value is `true`,
then any recurrence fields associated with the given recurrence type must be populated.

**Type**
string


Standard Objects Holiday

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the holiday.

```
NextOccurrenceDate

RecurrenceDayOfMonth

RecurrenceDayOfWeekMask

```

**Type**
date

**Properties**
Filter, Group, Nillable

**Description**

The next date of the holiday. Applies to recurring holidays only. Available in API version 58.0
and later. To access this field, you must have Field Service enabled and the Field Service
Standard permission.

This field isn't sortable. To compare this date to other dates, you must parse the string into
a date value to compare it to other dates.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day of the month on which the holiday repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the holiday repeats. This field contains a bitmask. For
each day of the week, the values are as follows:

**•** Sunday = `1`

**•** Monday = `2`

**•** Tuesday = `4`

**•** Wednesday = `8`

**•** Thursday = `16`

**•** Friday = `32`

**•** Saturday = `64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.


Standard Objects Holiday

**Field** **Details**

```
RecurrenceEndDateOnly

RecurrenceInstance

RecurrenceInterval

RecurrenceMonthOfYear

RecurrenceStartDate

RecurrenceType

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the holiday repeats. For multiday recurring events, this is the day on
which the last occurrence starts.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring holiday. For example, `2nd` or `3rd` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring holidays.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year on which the event repeats.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the recurring holiday begins. Must be a date and time before
`RecurrenceEndDateOnly` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects IconDefinition

**Field** **Details**

**Description**
Indicates how often the holiday repeats. For example, daily, weekly, or every Nth month
(where “Nth” is defined in `RecurrenceInstance` ).

```
StartTimeInMinutes

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start time of the holiday in minutes.

Use this object to view and update holidays, which specify dates and times at which associated business hours and escalation rules are
suspended.

### IconDefinition

Represents the icon-related metadata for a custom tab. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
ContentType

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s content type, for example, “image/png.”

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects IconDefinition

**Field Name** **Details**

**Description**

A unique virtual Salesforce ID for the icon.

```
Height

TabDefinitionId

Theme

Url

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s height in pixels. If the icon content type is an SVG type, height and
width values are not used.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The `TabDefinition` ID.

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

The icon’s theme.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified URL for this icon.


### Standard Objects Idea

**Field Name** **Details**

```
Width

### Idea

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s width in pixels. If the icon content type is an SVG type, height and
width values are not used.

Represents an idea on which users are allowed to comment and vote, for example, a suggestion for an enhancement to an existing
product or process. This object is available in API version 12 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Note: For other standard objects, the `describeLayout()` call returns the `recordTypeMappings` section that contains
the layout ID and picklist values for each record type. However, the `recordTypeMappings` section and the fields it includes
are not available for the Idea object.

When performing a SOSL search on Idea objects, IdeaComment objects are also searched.

Fields

**Field** **Details**

```
AttachmentBody

AttachmentContentType

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**

File data for the attachment. This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Type of the attachment. This field is available in API version 28.0 and later.


Standard Objects Idea

**Field** **Details**

```
AttachmentLength

AttachmentName

Body

Categories

Category

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the attachment in bytes. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of the attachment. This field is available in API version 28.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the Idea.

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize Ideas into logical groupings.

Note: This field is only available if your organization has the `Categories` field
enabled. This field is enabled by default in organizations created after API version 14
was released. If the `Categories` field is enabled, API versions 13 and earlier do
not have access to either the `Categories` or `Category` fields.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable picklist of values used to organize Ideas into logical groupings.

Note: This field is not available if your organization has the multi-select
`Categories` field enabled.


Standard Objects Idea

**Field** **Details**

```
CommunityId

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

This is a relationship field.

**Relationship Name**
Community

**Relationship Type**
Lookup

**Refers To**
Community

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who posted the idea or commented on the idea.

This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.


Standard Objects Idea

**Field** **Details**

```
CurrencyIsoCode

IdeaThemeID

IsDeleted

IsHtml

IsMerged

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the idea theme associated with the idea.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. If this value is `true`, your organization has the Ideas HTML editor enabled, and
the Idea `Body` may contain HTML. If this value is `false`, the HTML editor is disabled and
the Idea `Body` only contains regular text.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether the idea has been merged with a parent idea ( `true` ) or not
( `false` ). You can’t vote for or add comments to a merged idea.

Note: In API version 27, `IsMerged` replaces `IsLocked` . Existing formula fields
that use `IsLocked` must be edited to use `IsMerged` .


Standard Objects Idea

**Field** **Details**

```
LastCommentDate

LastCommentId

LastReferencedDate

LastViewedDate

NumComments

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last comment (child IdeaComment object) was added.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last comment (child IdeaComment object).

This is a relationship field.

**Relationship Name**
LastComment

**Relationship Type**
Lookup

**Refers To**
IdeaComment

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects Idea

**Field** **Details**

**Description**
The number of comments (child IdeaComment objects) that users have submitted for the
given idea.

```
ParentIdeaId

RecordTypeId

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID associated with this idea's parent idea. When multiple ideas are merged together,
one idea becomes the parent (master) of the other ideas. The `ParentIdeaId` is
automatically set when you merge ideas.

This is a relationship field.

**Relationship Name**
ParentIdea

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record type assigned to this object.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customizable picklist of values used to specify the status of an idea.


Standard Objects Idea

**Field** **Details**

```
Title

VoteScore

VoteTotal

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The descriptive title of the idea.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the Idea, used to sort Ideas on the Popular tab in the application user
interface. The internal algorithm that determines the score gives older votes less weight than
newer votes, simulating exponential decay. The score itself does not display in the application
user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
An Idea's total number of points. Each vote a user makes is worth ten points, therefore the
value of this field is ten times the number of votes an idea has received.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.

Note: If you are importing Idea data and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Audit fields are automatically updated during API operations unless you request to set these fields yourself..

Usage

Use this object to track ideas, which are written suggestions on which users can vote and comment.

SEE ALSO:

IdeaComment

Vote


### Standard Objects IdeaComment IdeaComment

Represents a comment that a user has submitted in response to an idea.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Note: When performing a SOSL search on IdeaComment objects, Idea objects are also searched.

Fields

**Field** **Field Type**

```
CommentBody

CommunityId

CreatorFullPhotoUrl

CreatorName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Body of the submitted comment.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo. This field is available in API version 28.0 and later.

**Type**
string


Standard Objects IdeaComment

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who posted the idea or commented on the idea. This field is available in
API version 28.0 and later.

```
CreatorSmallPhotoUrl

IdeaId

IsHtml

UpVotes

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the idea on which this comment was made.

This is a relationship field.

**Relationship Name**
Idea

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. If this value is `true`, your organization has the Ideas HTML editor enabled, and
the `CommentBody` field may contain HTML. If this value is `false`, the HTML editor is
disabled and the `CommentBody` field only contains regular text.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects IdeaReputation

**Field** **Field Type**

**Description**

Total number of up votes for the question.

Note: If you import these records, and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

Use this object to track comments on ideas, which are users' text responses to ideas.

SEE ALSO:

### Idea

Vote

### IdeaReputation

Represents a collection of statistics and scores derived from a user’s activity within an Ideas zone or internal organization. This object is
available in API version 28.0 and later.

Supported Calls

`query()`, `retrieve()`,

Fields

**Field** **Details**

```
CommentCount

CommentsReceivedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments a user has created in a zone or the internal organization. This
number excludes comments the user creates on his or her own idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects IdeaReputation

**Field** **Details**

**Description**
The number of comments a user has received in a zone or the internal organization.

```
ContextId

DownVotesGivenCount

DownVotesReceivedCount

IdeaCount

ReputationLevel

Score

```

**Type**
reference

**Properties**
Filter, Group, Namepointing, Nillable, Sort

**Description**
The ID of the zone or internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has given in a zone or the internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of down votes a user has received in a zone or the internal organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of ideas a user has created in a zone or the internal organization.

**Type**
string

**Properties**
Nillable

**Description**
The reputation level that a user has achieved based on their score in a zone or within an
organization.

**Type**
double


### Standard Objects IdeaReputationLevel

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The total score of a user’s activity within a zone or within an organization.

```
UpVotesGivenCount

UpVotesReceivedCount

UserId

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes a user has given in a zone or the internal organization. This number
doesn’t include the default vote the system applies when the user creates the idea.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes a user has received in a zone or the internal organization.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID associated with the reputation.

Use to query a user’s reputation within a zone.

### IdeaReputationLevel

Represents a reputation level within an Ideas zone or internal organization and is used by the system to calculate reputation. You can
create up to 25 levels per zone or internal organization. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects IdeaTheme

Fields

**Field Name** **Details**

```
ContextId

Name

Threshold

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Namepointing, Sort, Update

**Description**

The ID of the zone or internal organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level. The name must be unique within the zone or
internal organization. Maximum size is 50 characters.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level. The threshold must be unique within
the zone or internal organization and must be greater than or equal to zero.

Use to create or edit reputation levels for an Ideas zone or internal organization.

### IdeaTheme

Represents an invitation to zone members to submit ideas that are focused on a specific topic. This object is available in API version 26
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`,


Standard Objects IdeaTheme

Fields

**Field Name** **Details**

```
Categories

CommunityId

CurrencyIsoCode

Description

EndDate

LastReferencedDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize ideas and idea themes into
logical groupings.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort,

**Description**
The zone ID associated with the idea theme.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Description of the idea theme.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date marking the end of the idea theme.

**Type**
date


### Standard Objects IdpEventLog

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

```
StartDate

Status

Title

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date that the idea theme begins.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Customizable picklist of values used to specify the status of the idea theme.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**

Title of the idea theme.

Use the object to track ideas that are submitted to an idea theme.

### IdpEventLog

Represents the Identity Provider Event Log. This log records both problems and successes with inbound SAML or OpenID Connect
authentication requests from another app provider. It also records outbound SAML responses when Salesforce is acting as an identity
provider. This object is available in API version 39.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects IdpEventLog

Fields

**Field** **Details**

```
AppId

AuthSessionId

ErrorCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the app provider seeking authentication.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the authentication session.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The error code for the authentication issue.

Possible values are:

**•** `AppAccessDenied` —Error: App access denied

**•** `AppBlocked` —Error: App blocked

**•** `ClientUnapproved` —Error: Invalid grant

**•** `CodeExpired` —Error: Expired authorization code

**•** `ForceAuthNLogout` —User logged out due to forced authentication request

**•** `InternalError` —Error: Internal Error

**•** `InvalidAuthnRequest` —Error: Unable to parse AuthnRequest from service
provider

**•** `InvalidClientCredentials` —Error: Invalid client credentials

**•** `InvalidCode` —Error: Invalid authorization code

**•** `InvalidDeviceId` —Error: Invalid device ID

**•** `InvalidIdpEndpoint` —Error: Invalid Identity Provider Endpoint URL

**•** `InvalidIssuer` —Error: Invalid Issuer

**•** `InvalidScope` —Error: Invalid scope(s)

**•** `InvalidSessionLevel` —Error: Invalid session level

**•** `InvalidSettings` —Error: IdP certificate is invalid or does not exist

**•** `InvalidSignature` —Error: Invalid Signature


Standard Objects IdpEventLog

**Field** **Details**

**•** `InvalidSp` —Error: Misconfigured or invalid service provider

**•** `InvalidSpokeSp` —Error: Invalid spoke SP settings

**•** `InvalidUserCredentials` —Error: Invalid user credentials

**•** `NoAccess` —Error: User does not have access to this service provider

**•** `NoCustomAttrValue` —Error: User does not have a value for the subject custom
attribute

**•** `NoCustomField` —Error: Custom field not found

**•** `NoSpokeId` —Error: No Spoke ID found

**•** `NoSubdomain` —Error: No My Domain deployed in the org

**•** `NoUserFedId` —Error: User does not have a Federation Identifier selected

**•** `OauthError` —OAuth Error

**•** `Success`

**•** `UnableToResolve` —Error: Unable to resolve request into a Service Provider

**•** `UnknownError` —Unknown Error

```
IdentityUsed

InitiatedBy

OptionsHasLogoutUrl

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The identity (username) of the user being authenticated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The code describing how the authentication request was initiated.

Possible values are:

**•** `IdP` —IdP-Initiated SAML

**•** `OauthAuthorize` —OAuth Authorization

**•** `OauthTokenExchange` —OAuth Token Exchange

**•** `SP` —SP-Initiated SAML

**Type**
boolean

**Properties**
Filter


### Standard Objects IframeWhiteListUrl

**Field** **Details**

**Description**
Whether a logout URL has been assigned to the app. This URL is where users are redirected
when they log out.

```
 SamlEntityUrl

 SsoType

 Timestamp

 UserId

### IframeWhiteListUrl

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The authentication URL of the SAML provider.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of SSO. Options are:

**•** 0–SAML

**•** 1–OpenID Connect

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time on which the event occurred.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user seeking authentication.

Represents a list of trusted external domains that you allow to frame your Embedded Service, Surveys, and Visualforce pages. This object
is available in API version 45.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.


### Standard Objects Image

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Context

Url

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of content in the iframe.

Valid values are:

**•** `Surveys`

**•** `VisualforcePages`

**•** `DisclosureAndComplianceHubConnector`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique domain that is allowed to frame your Visualforce pages, surveys, or
Disclosure and Compliance Hub Connector. Accepts these formats: example.com,
*example.com, and https://example.com.

To use this object for framing Visualforce pages, on Session Settings in Setup, select **Enable clickjack protection for customer**
**Visualforce pages** either **with headers disabled** or **with standard headers** . These options both allow framing of Visualforce pages
on trusted external domains and provide clickjack protection.

Alternatively, you can customize session settings via the SecuritySettings Metadata API type. To use the IframeWhiteListUrl object, set
either the `enableClickjackNonsetupUser` or `enableClickjackNonsetupUserHeaderless` field to `true` . For
[more information, see SecuritySettings in the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_securitysettings.htm)

### Image

Represents the details of an image. This object is available in API version 47.0 and later.


Standard Objects Image

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AlternateText

CapturedAngle

ContentDocumentId

ImageClass

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Accessibility text to explain the image in words.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Angle at which the image was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of the content document where image is stored.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The image category.


Standard Objects Image

**Field** **Details**

Possible values are:

**•** `FOOD`

**•** `LOGOS`

**•** `OBJECTS`

**•** `SCENES`

```
ImageClassObjectType

ImageViewType

IsActive

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of image. Used in Einstein Object Detection to identify whether the image is used
to detect objects or build a model.

Possible values are:

**•** `DETECTION` —Actual Image

**•** `FEEDBACK`

**•** `TRAINING`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Orientation of the image.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if an image is active. The default value is False. An active image can be used for
building or updating a model in Einstein Object Detection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the image was last referenced.


Standard Objects Image

**Field** **Details**

```
LastViewedDate

Name

OwnerId

Title

Url

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the image was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Unique identifier of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the image.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Public URL of the image file.


### Standard Objects Incident Incident

An Incident is any unplanned business interruption that has wide-sweeping impacts and requires an urgent fix. This object contains the
details of the incident, documenting the history of the incident from registration to closure. This object is available in API version 53.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Category

Description

DetectedDateTime

EndDateTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident. This field can store up to 32 KB of data, but only the first 255
characters appear in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was first detected.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident ended.


Standard Objects Incident

**Field** **Details**

```
Impact

IncidentNumber

IsMajorIncident

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The incident's impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated number for the incident.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the incident is business-critical. If set to `true`, the incident is widespread
and business-critical. The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the current user last accessed this record, a list view, or
another related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Incident

**Field** **Details**

**Description**
The date and time (in UTC) when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

```
OwnerId

ParentIncidentId

Priority

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned to resolve the
incident.

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
The unique ID of an incident above one or more related incidents in an incident hierarchy.

This is a relationship field.

**Relationship Name**
ParentIncident

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of the incident.

Possible values are:

**•** `Critical`


Standard Objects Incident

**Field** **Details**

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
PriorityOverrideReason

ReportedMethod

ResolutionDateTime

ResolutionSummary

ResolvedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why a priority should be changed or edited.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates how the incident was reported to customer service.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident was resolved.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of possible steps to resolve the incident.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the user who resolved the incident.

This is a relationship field.


Standard Objects Incident

**Field** **Details**

**Relationship Name**
ResolvedBy

**Relationship Type**
Lookup

**Refers To**
User

```
StartDateTime

Status

StatusCode

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the incident began.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any custom or granular stages a customer may want to track.

Possible values are:

**•** `Completed`

**•** `In Progress`

**•** `New`

**•** `Open`

**•** `Problem Created`

**•** `Resolved`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The incident's status.

Possible values are:

**•** `Completed`

**•** `InProgress`

**•** `New`

**•** `Open`


Standard Objects Incident

**Field** **Details**

**•** `ProblemCreated`

**•** `Resolved`

The default value is 'New'.

```
SubCategory

Subject

Type

Urgency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident. One level deeper than Category. Administrators set field values.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the incident.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of incident, for example, question or problem. Administrators set field values.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A measure of how long the resolution can be delayed until an incident, problem, or change
has a significant business impact.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.


### Standard Objects IncidentRelatedItem

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentChangeEvent on page 68**
Change events are available for the object.

**IncidentFeed on page 55**
Feed tracking is available for the object.

**IncidentHistory on page 63**
History is available for tracked fields of the object.

**IncidentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**IncidentShare on page 67**
Sharing is available for the object.

### IncidentRelatedItem

Represents a junction object that relates an Incident to an Asset or Product. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Asset ID that's linked to the Incident.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


Standard Objects IncidentRelatedItem

**Field** **Details**

```
Comment

ImpactLevel

ImpactType

IncidentId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the incident.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The effect of the related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Incident ID that's linked to the Asset.

This field is a relationship field.


Standard Objects IncidentRelatedItem

**Field** **Details**

**Relationship Name**
Incident

**Relationship Type**
Lookup

**Refers To**
Incident

```
Name

Product2Id

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident-related item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product (Product2) ID that's linked to the Incident..

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentRelatedItemChangeEvent on page 68**
Change events are available for the object.

**IncidentRelatedItemFeed on page 55**
Feed tracking is available for the object.

**IncidentRelatedItemHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects Individual Individual

Represents a customer’s data privacy and protection preferences. Data privacy records based on the Individual object store your customers’
preferences. Data privacy records are associated with related leads, contacts, person accounts, and users. This object is available in API
version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
BirthDate

CanStorePiiElsewhere

ChildrenCount

ConsumerCreditScore

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s birthdate.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indication that you can store the customer’s personally identifiable information
(PII) outside of their legislation area. For example, you could store an EU citizen’s
PII data in the US.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of children the customer has.

**Type**
int


Standard Objects Individual

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person's credit score (for example, 740).

```
ConsumerCreditScoreProviderName

ConvictionsCount

DeathDate

FirstName

HasOptedOutGeoTracking

HasOptedOutProcessing

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that provided the credit score.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of convictions for the customer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s death date.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s first name. Maximum size is 40 characters.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track geolocation on mobile devices.

**Type**
boolean


Standard Objects Individual

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process personal data, which can include collecting, storing,
and sharing personal data.

```
HasOptedOutProfiling

HasOptedOutSolicit

HasOptedOutTracking

HasPrivacyHold

IndividualsAge

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process data for predicting personal attributes, such as interests,
behavior, and location.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not solicit products and services.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track customer web activity and whether the customer opens
email sent through Salesforce.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates the Privacy Hold status.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer is considered to be a minor.


Standard Objects Individual

**Field Name** **Details**

```
InfluencerRating

IsHomeOwner

LastName

LastViewedDate

MasterRecordId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A measure of the person's influence, irrespective of how we do business with
them.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the customer owns a home.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The customer’s last name. Maximum size is 80 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the
record that was kept. If this object was deleted for any other reason, or hasn’t
been deleted, the value is `null` .

This is a relationship field.

**Relationship Name**
MasterRecord


Standard Objects Individual

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
Individual

```
MilitaryService

Name

Occupation

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer has served in the military.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName` . Maximum size is 203
characters, including whitespaces.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s occupation. Maximum size is 150 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects Individual

**Field Name** **Details**

```
Salutation

SendIndividualData

ShouldForget

Website

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title for addressing the customer, such as Dr. or Mrs.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to export personal data for delivery to the customer.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to delete records and personal data related to this customer.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the customer’s website.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IndividualChangeEvent (API version 47.0)**
Change events are available for the object.

**IndividualHistory**

History is available for tracked fields of the object.

**IndividualShare**

Sharing is available for the object.


### Standard Objects IndividualApplicationItem IndividualApplicationItem

Captures individual application input data that is used during run-time. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only with the EAndU Cloud Program Access permission set.

Fields

**Field** **Details**

```
IndividualApplicationId

Name

RelatedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Individual Application parent object associated with the Individual Application Item.

This field is a relationship field.

**Relationship Name**
### IndividualApplication

**Relationship Type**
Lookup

**Refers To**
### IndividualApplication

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the object related to the Individual Application.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects IndividualApplicationItem

**Field** **Details**

**Description**
The related object associated with the Individual Application Item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedItem

**Relationship Type**
Lookup

**Refers To**
Benefit, ProgramProduct

```
Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the approval status of the Individual Application.

Possible values are:

**•** `Approved`

**•** `Declined`

**•** `In Progress`

**•** `Pending`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[IndividualApplicationItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[IndividualApplicationItemFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[IndividualApplicationItemHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[IndividualApplicationItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[IndividualApplicationItemShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects IndividualHistory IndividualHistory

Represents the history of changes to values in the fields of a data privacy record, based on the Individual object. This object is available
in versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.

Fields

**Field Name** **Details**

```
DataType

Field

IndividualId

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
The name of the changed field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the data privacy record. Label is **Individual ID** .

This is a relationship field.

**Relationship Name**
### Individual


### Standard Objects IndividualShare

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
### Individual

```
NewValue

OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

Use this object to identify changes to data privacy records.

This object respects field-level security on the parent object.

### IndividualShare

Represents a list of access levels to a data privacy record along with an explanation of the access level. For example, if you have access
to a record because you own it, the `IndividualAccessLevel` is `All` and `RowCause` is Owner. This object is available in API
version 42.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects IndividualShare

Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.

Fields

**Field Name** **Details**

```
IndividualAccessLevel

IndividualId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the data privacy record. The possible
values include:

**•** `Read`

**•** `Edit`

**•** `All` (Except for create or update.)

Set this field to an access level that’s higher than your default access level for
individuals.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Individual associated with this sharing entry. This field isn’t available for
updates.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects InsufficientAccessEventLog

**Field Name** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited. Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the data privacy record with them.

**•** `Owner` —The User is the owner of the data privacy record.

**•** `Rule` —The User or Group has access to the data privacy record via an
Individual sharing rule.

**•** `LpuImplicit` —The User has access to records owned by high-volume
Experience Cloud site users via a share group.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the data privacy record.
This field isn’t available for updates.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object lets you determine which users and groups can view or edit Individual records owned by other users.

### InsufficientAccessEventLog

Insufficient Access event logs contain details about errors relating to insufficient account, case, contact, and opportunity record access.
This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Note: The Insufficient Access event type is disabled by default. You can enable this event type for a period of 24 hours by contacting
Salesforce Customer Support.

These insufficient access error scenarios are logged:


Standard Objects InsufficientAccessEventLog

**•** The user can’t share a case, contact, or opportunity because the user doesn’t have permission to share the parent account or the
recipient of the share doesn’t currently have read access to the parent account.

**•** The user can’t change ownership of a case, contact, or opportunity because the user doesn’t have permission to share the parent
account or the new owner doesn’t currently have read access to the parent account.

**•** The user can’t change the parent account of a case, contact, or opportunity because the user doesn’t have permission to share the
new parent account or the owner of the case, contact, or opportunity doesn’t have read access to the new parent account.

Insufficient access errors resulting from bulk operations involving two or more records aren’t logged.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
AccessError

ActualLoggedInUserIdentifier

ErrorDescription

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
The ID of the user who initiated the action that caused the insufficient access error. For
example, a user attempts to transfer ownership of a record to a teammate, but the operation
fails because the teammate doesn’t have the required access.

**Example**

```
  005XXXXXXXXXXXX

```

**Type**
String


Standard Objects InsufficientAccessEventLog

**Field** **Details**

**Description**
Description of the insufficient access error that the user received.

**Example**
User 005XXXXXXXXXXXX doesn't have full access for the record 001XXXXXXXXXXXX.

```
ObjectType

RecordIdentifier

RequestIdentifier

RequestedAccessLevel

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object for which the user received the insufficient access error.

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
The unique ID of a single transaction. A transaction can contain one or more events.

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

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
dateTime


### Standard Objects InternalOrganizationUnit

**Field** **Details**

**Description**
The access time of Salesforce services in GMT.

**Example**

```
                   20130715233322.670

```

```
UserIdentifier

```

**Type**
Id

**Description**
The ID of the user for whom the insufficient access error occurred, either when the user
couldn’t access a record, the user couldn’t complete an operation, or the user was the
intended recipient of a record transfer that failed because the user didn’t have the required
access.

**Example**

```
  005XXXXXXXXXXXX

```

### InternalOrganizationUnit

Represents an organization that an Employee belongs to. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you have either a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission, or the Employee Management and Employee User add-on licenses. This object is also
available with the Referral Marketing license.

Fields

**Field** **Details**

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects InternalOrganizationUnit

**Field** **Details**

**Description**
A description of the organization the Employee is working in.

```
LastReferencedDate

LastViewedDate

OrganizationCode

OrganizationName

OwnerId

ParentOrganizationId

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
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The code of the organization the Employee is working in.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the organization the Employee is working in.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
reference


### Standard Objects InventoryItemReservation

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the parent organization.

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether the record is for an internal or an external organization. This field is available
in API version 60.0 and later.

Possible values are:

**•** `EXTERNAL_BUSINESS_UNIT`

**•** `INTERNAL_ORGANIZATION`

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**InternalOrganizationUnitHistory (API version 49.0)**
History is available for tracked fields of the object.

**InternalOrganizationUnitOwnerSharingRule**

Sharing rules are available for the object.

**InternalOrganizationUnitShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### InventoryItemReservation

Used to store inventory item reservation information for a specific product and location. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects InventoryItemReservation

Special Access Rules

This object is available only if a B2B Commerce, D2C Commerce, B2C Commerce or Salesforce Order Management license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

ErrorCode

ErrorMessage

InventoryItemReservationName

InventoryReservationId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. ISO code for the currency of
the inventory items.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the reservation isn’t successful.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
If an error occurred, this field contains the error message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the inventory item reservation (autogenerated, for example: PIR-0033).

**Type**
reference


Standard Objects InventoryItemReservation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the inventory reservation.

This field is a relationship field.

**Relationship Name**
InventoryReservation

**Relationship Type**
Lookup

**Refers To**
InventoryReservation

```
ItemReservationSourceId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity associated with the inventory item reservation.

This field is a relationship field.

**Relationship Name**
ItemReservationSource

**Relationship Type**
Lookup

**Refers To**
CartItem

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


Standard Objects InventoryItemReservation

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
ProductId

Quantity

ReservedAtLocationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the product on the inventory item reservation. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Number of products on the inventory item reservation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location or location group where the inventory item reservation originated.

This field is a polymorphic relationship field.

**Relationship Name**
ReservedAtLocation

**Relationship Type**
Lookup

**Refers To**
Location, LocationGroup


### Standard Objects InventoryReservation

**Field** **Details**

```
StockKeepingUnit

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The stock keeping unit (SKU) of the reserved item.

### InventoryReservation

Stores information about the status of cart inventory reservations in B2B and D2C Commerce. This object is available in API version 60.0
and later.

This object only applies to cart inventory reservation APIs in B2B and D2C Commerce. It isn't related to inventory reservation Connect
APIs used with Omnichannel Inventory and Order Management.

If your org is using Omnichannel Inventory as its inventory system, the inventory reservation record related to the cart also represents a
reservation in Omnichannel Inventory. If the org uses a different inventory system, the inventory reservation record related to the cart
represents a reservation in that inventory system.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if a B2B Commerce, D2C Commerce, B2C Commerce, or Salesforce Order Management license is enabled.

Fields

**Field** **Details**

```
ErrorCode

ErrorMessage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the reservation isn’t successful.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects InventoryReservation

**Field** **Details**

**Description**
If an error occurred, this field contains the error message.

```
InventoryReservationName

IsAsyncOperationInProgress

IsSuccess

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the inventory reservation (autogenerated, for example: PIR-0033).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if there’s an async operation in progress that could affect the reservation.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the most recent inventory system operation was successful.

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


Standard Objects InventoryReservation

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user could have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
OwnerId

ReservationDate

ReservationDurationInSeconds

ReservationIdentifier

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the inventory reservation.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The timestamp when the inventory reservation was created.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total duration of the inventory reservation in seconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier (text value) for the reservation.


### Standard Objects InvocableActionEventLog

**Field** **Details**

```
ReservationSourceId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity associated with the inventory reservation.

This field is a polymorphic relationship field.

**Relationship Name**
ReservationSource

**Relationship Type**
Lookup

**Refers To**
Export_FOI__c, WebCart

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**InventoryReservationOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InventoryReservationShare on page 67**
Sharing is available for the object.

### InvocableActionEventLog

Invocable Action events capture the calls to Salesforce Invocable Actions.This is particularly useful to monitor actions invoked during
Agentforce flows. This object is available in API version 64.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects InvocableActionEventLog

Fields

**Field** **Details**

```
ActionName

ActionType

ActionVersion

ApiCaller

BotIdentifier

BotSessionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
InvocableActionType being referenced.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The invocable action version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifier of the API caller. This is only populated when the action is invoked from a REST API
call

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


Standard Objects InvocableActionEventLog

**Field** **Details**

**Description**
The bot session ID.

```
Duration

FlowProcessType

FlowVersionIdentifier

PlannerIdentifier

RequestCount

RequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Time (in nanos) taken to process this set of requests.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The process type of the calling flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the version of the calling flow.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of invoked requests.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Invoice

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
Timestamp

UserIdentifier

### Invoice

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user employing salesforce.com services, whether through the user interface or API.

Represents a financial document describing the total amount a buyer must pay for goods or services provided. This object is available
in API version 48.0 and later.

Users can edit non-posted invoices. Posted invoices can’t be deleted. After an invoice is posted, users can make payments against it to
reduce its balance.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Salesforce Order Management or D2C Commerce license, and Billing (Revenue Cloud). A few fields require
Commerce Subscriptions to be enabled. These fields are available only in Lightning Experience.

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoice.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoice.htm)


Standard Objects Invoice

Fields

**Field** **Details**

```
Balance

BillToContactId

BillingAccountId

CurrencyIsoCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for this invoice. Equal to the invoice’s total amount with tax, ignoring
payments and adjustments.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The customer account for this invoice.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist


Standard Objects Invoice

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The three-letter ISO 4217 currency code associated with the invoice.

The default value is `USD` .

This field is available in API version 55.0 and later.

```
DaysInvoiceOpen

DaysInvoiceOverdue

Description

DocumentNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the invoice was created before it was paid.

This field is a calculated field.

This field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days since the date when payment was due.

This field is a calculated field.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Users can add more information about this invoice. Maximum of 1,000 characters.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The system-generated number that is used to organize financial documents. The number
can be sequential or random.


Standard Objects Invoice

**Field** **Details**

```
DueDate

FullSettlementDate

InvoiceBatchRunId

InvoiceDate

```

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The customer must pay the invoice by the due date. Unpaid invoices past the due date can
be sent to collections.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the invoice is paid in full.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Id of the invoice batch run that generated this invoice.

This field is a relationship field.

This field is available in API version 55.0 and later.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
The date that the invoice was posted. Used with payment terms to determine the invoice’s
`DueDate` . For example, an invoice with an `InvoiceDate` of 04/01 and Net 30 payment
terms has a `DueDate` of 05/01.


Standard Objects Invoice

**Field** **Details**

```
InvoiceNumber

LastReferencedDate

LastViewedDate

NetCreditsApplied

NetPaymentsApplied

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
System-created unique ID for this invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

This field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. If this value is null, it's possible the user accessed this record or list view
( `LastReferencedDate` ) but didn't view it.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Represents the net credits applied to an invoice. Calculated by subtracting the sum of all
unapplied lines from the sum of all applied lines.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
Represents net payments applied to an invoice. Calculated by subtracting the sum of
unapplied payments from the sum of payments applied to the invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

```
OwnerId

PaymentExclusionReason

PaymentTermId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns an invoice record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason for skipping creation of payment schedules and payment schedule items for the
invoice. This field is only available if Commerce Subscriptions is enabled for your org. Available
in API version 63.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the payment term used on this invoice.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm


Standard Objects Invoice

**Field** **Details**

```
PostedDate

ReferenceEntityId

SettlementStatus

ShouldExcludePayment

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the invoice was posted.

This field is available in API version 60.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the order or order summary that created this invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Order, OrderSummary

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the invoice's payment.

Possible values are:

**•** `Not Applicable`

**•** `Not Settled`

**•** `Partially Settled`

**•** `Settled`

This field is available when Subscription Management is enabled.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
Required. Indicates whether to skip creating payment schedules and payment schedule
items for the invoice ( `true` ) or not ( `false` ). The default value is `false` . This field is only
available if Commerce Subscriptions is enabled for your org. Available in API Version 63.0
and later.

```
Status

TaxLocaleType

TotalAdjustmentAmount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice.

Possible values are:

**•** `Canceled`  - Indicates that the invoice was generated and later canceled.

**•** `Draft`  - Indicates that the invoice is a draft. Available in API version 60.0 and later.

**•** `Draft In Progress`  - Indicates that the draft invoice is in progress. Available in
API version 60.0 and later.

**•** `Error`  - Indicates that an error occurred when processing the invoice.

**•** `Pending`  - Indicates that the invoice is being processed.

**•** `Posted`  - Indicates that the invoice has been generated and sent to the customer.

**•** `Posting In Progress` —Indicates that the invoice posting is in progress. Available
in API version 60.0 and later.

**•** `Void In Progress`  - Indicates that the invoice is pending a status change.

**•** `Voided`  - The invoice’s status after the API successfully voids the invoice.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The system used to handle tax on the original Order associated with the Invoice. Gross usually
applies to taxes like value-added tax (VAT), and Net usually applies to taxes like sales tax. This
field is available when Order Management or B2B Commerce is enabled.

Possible values are:

**•** Gross: Displays most prices and taxes as combined values

**•** Net: Displays most prices and taxes as separate values

This field is available in API version 56.0 and later.

**Type**
currency


Standard Objects Invoice

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice’s adjustment line amounts.

```
TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

TotalAmount

TotalAmountWithTax

TotalChargeAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's adjustment-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the invoice line's adjustment lines.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum `TotalAmount` values on the invoice’s lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TotalAmountWithTax` values on the invoice’s lines.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects Invoice

**Field** **Details**

**Description**
The sum of the invoice’s charges.

This field is a calculated field.

```
TotalChargeAmountWithTax

TotalChargeTaxAmount

TotalConvertedNegAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the amount fields on the invoice's charge-type invoice lines, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the invoice's charge lines.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all negative invoice lines that were converted to a credit memo. For example, if
one negative invoice line was for -$10 and one was for -$15, the total amount that’s converted
to a credit memo is -$25.

This field is a calculated field.

This field is available when Subscription Management is enabled.

This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of `TaxAmount` values on the invoice lines.

This field is a calculated field.


### Standard Objects InvoiceAddressGroup

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceFeed on page 55**
Feed tracking is available for the object.

**InvoiceHistory on page 63**
History is available for tracked fields of the object.

**InvoiceOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceShare on page 67**
Sharing is available for the object.

### InvoiceAddressGroup

Stores the buyer's address information. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceaddressgroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceaddressgroup.htm)

Fields

**Field** **Details**

```
Address

City

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer's address. Compound field that summarizes the invoice address group's address
component fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceAddressGroup

**Field** **Details**

**Description**
The buyer's city.

```
Country

GeocodeAccuracy

InvoiceAddressGroupNumber

InvoiceId

Latitude

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's country.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. The accuracy rating contains
information about the location of a latitude and longitude.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as DOC-000001.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice associated with the address group.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
double


Standard Objects InvoiceAddressGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's latitude.

```
Longitude

PostalCode

State

Street

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's longitude.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's postal code or ZIP code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's street.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceAddressGroupHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects InvoiceBatchRun InvoiceBatchRun

Represents a batch processing job in Subscription Management or Billing (Revenue Cloud). During an invoice batch run, all billing
schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version
55.0 and later.

An invoice batch run, controlled by a scheduler, tells the system to start the run at a scheduled date and time. The scheduler also includes
matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are included for
processing in the invoice batch run.

When an invoice batch run is started, Subscription Management or Billing (Revenue Cloud):

**•** Evaluates the billing schedule to see if it meets the criteria for inclusion in the batch invoice run.

**•** Generates an invoice record with a pending state.

**•** Makes calls to an external tax provider.

**•** Adds the tax to the invoice.

**•** Summarizes information about the billing schedules that were included in the invoice batch run and displays this information in
the Invoice Batch Run record.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrun.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrun.htm)

Fields

**Field** **Details**

```
BillingBatchSchedulerId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related billing batch scheduler.

This field is a relationship field.

**Relationship Name**
BillingBatchScheduler

**Relationship Type**
Lookup


Standard Objects InvoiceBatchRun

**Field** **Details**

**Refers To**
BillingBatchScheduler

```
Comments

CompletionTime

InvoiceBatchRunNumber

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the invoice batch run finished processing.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last modified. Its UI label is Last Modified
Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run was last viewed.

**Type**
reference


Standard Objects InvoiceBatchRun

**Field** **Details**

**Properties**
Filter, Group, Sort, Update

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is Owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RecoveryStatus

StartTime

Status

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the state of the invoice batch run recovery process. This field is available in API
version 56.0 and later.

Possible values are:

**•** `CompletelyRecovered` —All billing schedules included in the recovery run were
reset to _`Ready for Invoicing`_ . These billing schedules are included in the next
scheduled invoice batch run.

**•** `PartiallyRecovered` —Some, but not all, billing schedules that were part of the
recovery run were reset to _`Ready for Invoicing`_ . The billing schedules that
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to _`Ready for`_
_`Invoicing`_ so they can be processed.

**•** `RecoveryFailed` —The recovery job was unsuccessful. This value is available in API
version 57.0 and later.

**•** `RecoveryStarted` —The recovery job is in process.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Timestamp when the invoice batch run started processing.

**Type**
picklist


Standard Objects InvoiceBatchRun

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The state of the invoice batch run.

Possible values are:

**•** `Canceled` —This value is available in API version 57.0 and later.

**•** `Completed`

**•** `Failed`

**•** `Started`

**•** `Stopped` —This value is available in API version 57.0 and later.

The default value is `Started` .

```
TotalBillSchedRecovered

TotalBillSchedUnrecovered

TotalBillingSchedulesFailed

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that were reset to _`Ready`_
_`for Invoicing`_ . These billing schedules are included in the next scheduled invoice
batch run.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of billing schedules that were part of the recovery run that weren't reset to
_`Ready for Invoicing`_ . These billing schedules that weren’t successfully recovered
must be manually reset to _`Ready for Invoicing`_ so they can be processed.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that weren’t successfully processed. When a billing
schedule isn’t successfully processed, then the system doesn’t generate an invoice for it. For
details about errors, check the Revenue Transaction Error Log. This field is available in API
version 56.0 and later.


Standard Objects InvoiceBatchRun

**Field** **Details**

```
TotalBsSuccessfullyProcessed

TotalDraftInvoiceAmount

TotalDraftInvoices

TotalFilteredBillingSchedules

TotalInvSuccessfullyProcessed

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules for which the system was able to generate and process
invoices. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the invoice amounts for invoices in `Draft` status.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices in `Draft` status generated in the batch run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of billing schedules that met the invoice run scheduler’s matching criteria.
The matching criteria specify which billing schedules are included in the invoice batch run.
Its field label is Total Matching Billing Schedules. This field is available in API version 56.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceBatchRun

**Field** **Details**

**Description**
The total number of invoices that were successfully processed.

When Billing (Revenue Cloud) is enabled, the field's value is either the same as
`TotalPostedInvoices` or `TotalDraftInvoices` based on the Invoice Status
selected when the Invoice Scheduler is set up.

This field is available in API version 56.0 and later.

```
TotalInvoicedAmount

TotalInvoicesCanceled

TotalInvoicesFailed

TotalInvoicesGenerated

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of income including taxes represented by the successfully processed
invoices. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren't processed. To find out what went wrong, check
the Revenue Transaction Error Log. Fix the errors, then run the invoice batch run recovery
process.

This field is available in API version 57.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that weren’t processed successfully. To find out what went
wrong, check the Revenue Transaction Error Log. Then fix the errors and run the invoice
batch run recovery process. This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices that were generated from the billing schedules processed by
the invoice batch run. This field is available in API version 56.0 and later.


### Standard Objects InvoiceBatchRunCriteria

**Field** **Details**

```
TotalPostedInvoices

TotBillSchdUpdtDurDrftToPost

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of invoices in `Posted` status generated during the batch run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total billing schedules updated during the draft to posted run.

This field is available when Billing (Revenue Cloud) is enabled.

This field is available in API version 62.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceBatchRunChangeEvent on page 68**
Change events are available for the object.

**InvoiceBatchRunFeed on page 55**
Feed tracking is available for the object.

**InvoiceBatchRunHistory on page 63**
History is available for tracked fields of the object.

**InvoiceBatchRunOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceBatchRunShare on page 67**
Sharing is available for the object.

### InvoiceBatchRunCriteria

Represents a batch processing job and its required criteria in Subscription Management. During an invoice batch run, all billing schedules
that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version 55.0 and later.

A scheduled invoice batch run tells the system to start the run at a scheduled date and time by using certain criteria. The scheduler
includes the matching criteria, which are used to evaluate the billing schedules. Billing schedules that meet the specified criteria are
included for processing in the invoice batch run.


Standard Objects InvoiceBatchRunCriteria

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchruncriteria.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchruncriteria.htm)

Fields

**Field** **Details**

```
Comments

CriteriaExpression

CriteriaMatchType

ExpectedInvoiceStatus

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined information about the batch run criteria.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The formula that specifies criteria for filtering the billing schedules. For example, we can filter
billing schedules by currency code.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of matching criteria required for the batch.

Valid value is `MatchAll` .

The default value is `MatchAll` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects InvoiceBatchRunRecovery

**Field** **Details**

**Description**
The type of invoice a batch run generates.

Valid values are:

**•** `Draft`

**•** `Posted`

This field is available in API version 60.0 and later.

```
InvoiceBatchRunCriteriaNumber

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated sequential number.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
System-generated field. The ID of the user who created the BillingBatchScheduler record. Its
UI label is `Owner` .

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

### InvoiceBatchRunRecovery

Provides information about an invoice batch run recovery procedure. This object is available in API version 57.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).


Standard Objects InvoiceBatchRunRecovery

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrunrecovery.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicebatchrunrecovery.htm)

Fields

**Field** **Details**

```
Comments

CompletionTime

InvoiceBatchRunId

InvoiceBatchRunRecoveryNumber

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run recovery procedure was completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique identifier of the invoice batch run related to this recovery run.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique identifier of the invoice batch run recovery process.


Standard Objects InvoiceBatchRunRecovery

**Field** **Details**

```
LastReferencedDate

LastViewedDate

StartTime

Status

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
it’s possible that the user indirectly accessed this record ( `LastReferencedDate` ), but
did not view it.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The timestamp when the invoice batch run recovery started.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The final state of the invoice batch run recovery process.

Possible values are:

**•** `Completed` —The recovery run successfully reset all billing schedules to _`Ready for`_
_`Invoicing`_ .

**•** `CompletedWithErrors` —Some, but not all, billing schedules included in the
recovery run were reset to _`Ready for Invoicing`_ . The billing schedules that
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to _`Ready for`_
_`Invoicing`_ so they can be processed.

**•** `Failed` —The recovery run was unable to complete the reset process.

**•** `Started` —Indicates that the recovery run reset process began, is ongoing, and has
not yet produced a result.

The default value is `Started` .


### Standard Objects InvoiceDocument

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceBatchRunRecoveryChangeEvent on page 68**
Change events are available for the object.

**InvoiceBatchRunRecoveryFeed on page 55**
Feed tracking is available for the object.

**InvoiceBatchRunRecoveryHistory on page 63**
History is available for tracked fields of the object.

**InvoiceBatchRunRecoveryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceBatchRunRecoveryShare on page 67**
Sharing is available for the object.

### InvoiceDocument

Tracks and displays the status of documents generated for invoices. Invoice documents are available in the related lists of invoice entity
records. This object is available in API version 61.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

This object is available with Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicedocument.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoicedocument.htm)

Fields

**Field** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the generated PDF document.

This field is a relationship field.

**Relationship Name**
ContentDocument


Standard Objects InvoiceDocument

**Field** **Details**

**Refers To**
ContentDocument

```
DateGenerated

DocumentGenerationProcessId

DocumentNumber

ErrorMessage

InvoiceId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date on which the PDF is generated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the entity that contains the information used to create the PDF invoice.

This field is a relationship field.

**Relationship Name**
DocumentGenerationProcess

**Refers To**
DocumentGenerationProcess

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the generated document.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Errors that occur during PDF generation.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects InvoiceLine

**Field** **Details**

**Description**
The ID of the invoice entity to which the invoice document is attached.

This field is a relationship field.

**Relationship Name**
### Invoice

**Relationship Type**
Master-detail

**Refers To**
Invoice (the master object)

```
Status

### InvoiceLine

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the PDF generation process.

Possible values are:

**•** `Blocked`

**•** `Cancelled`

**•** `Failure`

**•** `Pending`

**•** `Success`

Represents the amount that a buyer must pay for a product, service, or fee. Invoice lines are created based on the amount of an order
line. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceline.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_invoiceline.htm)


Standard Objects InvoiceLine

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentAmountWithTax

AdjustmentTaxAmount

Balance

BillingAddressId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustments made to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustment amounts, including associated taxes related to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of tax adjustments to the invoice line.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for an invoice line. This is equal to the invoice’s total amount with
tax after deducting the payments made.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field to an InvoiceAddressGroup containing the billing address for the invoice line.
Assign one InvoiceAddressGroup to the invoiceLine's BillingAddressID, and another
InvoiceAddressGroup to the invoiceLine's ShippingAddressId.

This field is a relationship field. This field is available in API version 55.0 and later.


Standard Objects InvoiceLine

**Field** **Details**

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup

```
BillingScheduleGroupId

BillingScheduleId

ChargeAmount

ChargeAmountWithTax

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Refers To**
BillingScheduleGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the billing schedule for the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Sum of charges made to the invoice line.

**Type**
currency


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Amount on a charge invoice line, including tax.

This field is available in API version 55.0 and later.

```
ChargeTaxAmount

ConvertedNegAmount

Description

GroupReferenceEntityItemId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax to be applied on a charge invoice line.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount from an invoice line that is converted to credit.

This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the invoice line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Grouping field for adjustment line items.

This field is a polymorphic relationship field.

**Relationship Name**
GroupReferenceEntityItem

**Relationship Type**
Lookup


Standard Objects InvoiceLine

**Field** **Details**

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

```
HasMultipleItems

InvoiceId

InvoiceLineEndDate

InvoiceLineStartDate

InvoiceStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this field merges items from the same billing period.

The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The invoice that contains this invoice line.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the end date of the billing for the service.

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the first date of the billing for the service.

**Type**
string


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the invoice line. Inherited from the invoice’s status.

```
LegalEntityAccountingPeriodId

LegalEntityId

LineAmount

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntityAccountingPeriod

**Refers To**
LegalEntyAccountingPeriod

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntity

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the invoice line.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the invoice line.


Standard Objects InvoiceLine

**Field** **Details**

```
NetCreditsApplied

NetPaymentsApplied

Product2Id

Quantity

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total credit memo line amount applied to the invoice line. This amount is calculated by
subtracting the unapplied credit memo line amount from the applied credit memo line
amount.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total payment applied to the invoice line. This amount is calculated by subtracting the
unapplied payment amount from the applied payment amount.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The product that was charged or ordered to create the invoice line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Number of units of the order product that created the invoice line.


Standard Objects InvoiceLine

**Field** **Details**

```
ReferenceEntityItemId

ReferenceEntityItemType

ReferenceEntityItemTypeCode

RelatedLineId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order item or adjustment item that created the invoice line.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of transaction that created the invoice line.

Possible values are:

**•** `DeliveryCharge` —Charge

**•** `Fee` —Charge. This value is available in API version 56.0 and later.

**•** `OrderProduct` —Product

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that created the invoice line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects InvoiceLine

**Field** **Details**

**Description**
The original invoice line that was adjusted or taxed.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

```
ShippingAddressId

TaxAmount

TaxCode

TaxDocumentNumber

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address associated with the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
ShippingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate tax rate for the invoice line.

**Type**
string


Standard Objects InvoiceLine

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the latest record in the external tax engine in which this invoice line item is
included.

This field is available in API version 55.0 and later.

```
TaxEffectiveDate

TaxName

TaxRate

TaxTransactionNumber

TaxTreatmentId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the invoice line’s `TaxAmount` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for the applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update

**Description**
Percentage value used for calculating tax.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the transaction in the external tax engine in which the taxes for the line were
calculated for the invoice line.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects InvoiceLine

**Field** **Details**

**Description**
The tax treatment used on this invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

```
 Type

 UnitPrice

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of transaction for the invoice line.

Possible values are:

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Price for one unit of the item on the invoice line.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceLineFeed on page 55**
Feed tracking is available for the object.

**InvoiceLineHistory on page 63**
History is available for tracked fields of the object.

**InvoiceLineOwnerSharingRule on page 65**
Sharing rules are available for the object.

**InvoiceLineShare on page 67**
Sharing is available for the object.


### Standard Objects JobProfile JobProfile

Represents a job profile used for shift scheduling. This object is available in API versions 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service or Workforce Engagement must be enabled.

Fields

**Field** **Details**

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
The date and time when the current user last viewed a related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the job profile.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects JobProfileQueueGroup

**Field** **Details**

**Description**
The ID of the owner of the job profile.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**JobProfileFeed**

Feed tracking is available for the object.

**JobProfileHistory**

History is available for tracked fields of the object.

**JobProfileOwnerSharingRule**

Sharing rules are available for the object.

**JobProfileShare**

Sharing is available for the object.

### JobProfileQueueGroup JobProfileQueueGroup defines the mapping between Queue and JobProfile and configurations for capacity plans in Workforce Engagement.

This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`

Special Access Rules

Org must have the Workforce Engagement, Workforce Engagement Configuration, and Omni org preferences enabled. User must have
the Workforce Engagement Analyst or Planner user permission set.

Fields

**Field** **Details**

```
AnswerTime

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The answer time (in seconds) for a specific group.


Standard Objects JobProfileQueueGroup

**Field** **Details**

```
CapacityPerJobProfile

GroupCapacity

GroupId

JobProfileId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The max number of work units that an agent can handle for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distributed number of work units among groups to which a specific job profile is
associated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the group or queue record.

This is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Identifies the job profile record.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup


### Standard Objects Knowledge__Feed

**Field** **Details**

**Refers To**
JobProfile

```
JobProfileShrinkage

Priority

ServiceLevelAgreementPerc

WorkType

### Knowledge__Feed

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The shrinkage for a specific job profile.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority of a group per job profile.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The expected SLA percentage for a specific group.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A type of group, indicating whether a queue is synchronous or asynchronous.

Possible values are:

**•** `A` —Async

**•** `S` —Sync

The default value is 'S'.

Represents the feed for a knowledge article. This object is available in API version 39.0 and later.

For additional information about feeds, see FeedItem on page 2526.


Standard Objects Knowledge__Feed

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Lightning Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
BestCommentId

Body

CommentCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

**Type**
textarea

**Properties**
Nillable, Sort

**Description**
The body of the feed item. Required when `Type` is `TextPost` or `AdvancedTextPost` .
Optional when `Type` is `ContentPost` or `LinkPost` .

Although a value for `Body` is not required for the `ContentPost` type, an attachment
is required. If an attachment isn’t present, the type changes to `TextPost` or
`AdvancedTextPost`, depending on the API version. `TextPost` and
`AdvancedTextPost` do require a value for `Body` .

Tip: See the `IsRichText` field for a list of HTML tags supported in the body of
rich text posts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.


Standard Objects Knowledge__Feed

**Field** **Details**

Tip: In a feed that supports pre-moderation, `CommentCount` isn’t updated until a
comment is published. For example, say that you comment on a post that already has
one published comment and your comment triggers moderation. Now there are two
comments on the post, but the count says there's only one. In a moderated feed,
comments aren’t counted until approved by an admin or someone with Can Approve
Feed Post and Comment or Modify All Data.

Feed moderation has implications on how you retrieve feed comments. In a moderated
feed, rather than retrieving comments by looping through `CommentCount`, go through
pagination until the end of comments is returned.

```
InsertedById

IsRichText

```

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application migrates posts
and comments from another application into a feed, the `InsertedBy` value is set to the
ID of the context user.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text feed comment
using SOAP API, set `IsRichText` to `true` and escape HTML entities from the body.
Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use `<p>&nbsp;</p>`
to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`


Standard Objects Knowledge__Feed

**Field** **Details**

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files in Salesforce
similar to this example: `<img src="sfdc://069B0000000omjh"></img>`

Note: In API version 35.0 and later, the system replaces special characters in rich text
with escaped HTML. In API version 34.0 and prior, all rich text appears as a plain-text
representation.

```
LikeCount

LinkUrl

ParentId

RelatedRecordId

Title

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Nillable, Sort

**Description**
The URL of a `LinkPost` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Knowledge article to which the feed item is related.

**Type**
reference

**Properties**
Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost` . For WDC thanks posts,
it’s the ID of the WorkThanks object associated with a `RypplePost` . This field is typically
null for all posts except `ContentPost` and `RypplePost` .

For example, set this field to an existing ContentVersion ID and post it to a feed with `Type`
set to `ContentPost` .

**Type**
string


Standard Objects Knowledge__Feed

**Field** **Details**

**Properties**
Group, Nillable, Sort

**Description**
The title of the feed item. When the `Type` is `LinkPost`, the `LinkUrl` is the URL and
this field is the link name. The `Title` field can be updated on posts of `Type`
`QuestionPost` .

```
Type

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost`, `LinkPost`, and `TextPost`, don’t
create feed items of other types directly from the API.

**•** `ActivityEvent` —indirectly generated event when a user or the API adds a Task
associated with a feed-enabled parent record (excluding email tasks on cases). Also
occurs when a user or the API adds or updates a Task or Event associated with a case
record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the series only.
For a recurring Task with CaseFeed enabled, events are generated for the series and each
occurrence.

**•** `AdvancedTextPost` —created when a user posts a group announcement and, in
Lightning Experience as of API version 39.0 and later, when a user shares a post.

**•** `AnnouncementPost` —Not used.

**•** `ApprovalPost` —generated when a user submits an approval.

**•** `BasicTemplateFeedItem` —Not used.

**•** `CanvasPost` —a post made by a canvas app posted on a feed.

**•** `CollaborationGroupCreated` —generated when a user creates a public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —a post with an attached file.

**•** `CreatedRecordEvent` —generated when a user creates a record from the publisher.

**•** `DashboardComponentAlert` —generated when a dashboard metric or gauge
exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot` —created when a user posts a dashboard
snapshot on a feed.

**•** `LinkPost` —a post with an attached URL.

**•** `PollPost` —a poll posted on a feed.

**•** `ProfileSkillPost` —generated when a skill is added to a user’s Chatter profile.

**•** `QuestionPost` —generated when a user posts a question.

**•** `ReplyPost` —generated when Chatter Answers posts a reply.


### Standard Objects Knowledge__ka

**Field** **Details**

**•** `RypplePost` —generated when a user creates a Thanks badge in WDC.

**•** `TextPost` —a direct text entry on a feed.

**•** `TrackedChange` —a change or group of changes to a tracked field.

**•** `UserStatus` —automatically generated when a user adds a post. Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply only to
CaseFeed:

**•** `AttachArticleEvent` —generated event when a user attaches an article to a case.

**•** `CallLogPost` —generated event when a user logs a call for a case through the user
interface. CTI calls also generate this event.

**•** `CaseCommentPost` —generated event when a user adds a case comment for a case
object.

**•** `ChangeStatusPost` —generated event when a user changes the status of a case.

**•** `ChatTranscriptPost` —generated event when Chat transcript is saved to a case.

**•** `EmailMessageEvent` —generated event when an email related to a case object is
sent or received.

**•** `FacebookPost` —generated when a Facebook post is created from a case. Deprecated.

**•** `MilestoneEvent` —generated when a case milestone is completed or reaches
violation status.

**•** `SocialPost` —generated when a social post is created from a case.

Note: If you set `Type` to `ContentPost`, also specify `ContentData` and
`ContentFileName` .

### Knowledge__ka

Provides access to the concrete object that represents a Knowledge article, the parent object for article versions. This object is available
in API version 39.0 and later.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticle on page 3004.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.


Standard Objects Knowledge__ka

Fields

**Field** **Details**

```
ArchivedById

ArchivedDate

ArticleNumber

CaseAssociationCount

FirstPublishedDate

LastPublishedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was archived.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of cases attached to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Knowledge__ka

**Field** **Details**

**Description**
The date when the article was last published.

```
LastReferencedDate

LastViewedDate

MasterLanguage

MigratedToFromArticle

TotalViewCount

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
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The article's original language. Only accessible if your knowledge base supports multiple
languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article. Contains values only in orgs that
migrate from Knowledge in Salesforce Classic to Lightning Knowledge. This field is available
in API version 45.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Knowledge__kav

**Field** **Details**

**Description**
Total number of views for this article. This field is available in API version 39.0 and later.

### Knowledge__kav

Provides access to the concrete object that represents a Knowledge article version. This object is available in API version 39.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

This object is derived from KnowledgeArticleVersion on page 3016.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

This object doesn’t retrieve `<ActionOverrides>` .

Special Access Rules

Lightning Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users,
unlike customer and partner users, must also be granted the `Knowledge User` feature license.

Fields

**Field** **Details**

```
ArchivedById

ArchivedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article version was archived.


Standard Objects Knowledge__kav

**Field** **Details**

```
ArticleArchivedById

ArticleArchivedDate

ArticleCaseAttachCount

ArticleCreatedById

ArticleCreatedDate

ArticleMasterLanguage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was archived.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cases where this article is attached.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who created the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects Knowledge__kav

**Field** **Details**

**Description**
The article's original language. Only accessible if your knowledge base supports multiple
languages.

```
ArticleNumber

ArticleTotalViewCount

AssignedById

AssignedToId

AssignmentDate

AssignmentDueDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't change
the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of views for the article.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who assigned the article.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user assigned to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the article was assigned to a user.

**Type**
dateTime


Standard Objects Knowledge__kav

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The due date when an article is assigned.

```
AssignmentNote

ExternalRef

ExternalSourceId

ExternalUrl

FirstPublishedDate

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Notes to the assignee from the user who assigned the article.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the item being referenced on the external system. For example, the ID of a document
on a Google Drive or a page on Confluence.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reference to the external Knowledge data source object.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL of the knowledge content referenced in an external system. For example, the ID of
a document in Google Drive or a page in Confluence.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.


Standard Objects Knowledge__kav

**Field** **Details**

```
IsExternalData

IsLatestVersion

IsMasterLanguage

IsOutOfDate

IsVisibleInApp

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the data is external to the customer’s knowledge base ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article is the most current version. ( `true` ) or not ( `false` ). This field
can be `true` on the online or published version, a draft version in the primary language, a
draft version in a translation, and the latest archived version. However, you can’t filter by
(PublishState=’Online’) and (IsLatestVersion=false) because the online version is also the
latest version. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the article has one or more translations associated with it ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the source article has been updated since this translated version was
created ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the article is visible in the Articles tab ( `true` ) or not ( `false` ).


Standard Objects Knowledge__kav

**Field** **Details**

```
IsVisibleInCsp

IsVisibleInPkb

IsVisibleInPrm

KnowledgeArticleId

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the Customer Portal ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the public knowledge base ( `true` ) or
not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the article is visible in the partner portal ( `true` ) or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article independent from its version. The value for this field is retrieved from
the `Id` field of the KnowledgeArticle object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
`(Traditional)` .

Querying or searching articles in SOSL require that you specify the `Language` field in the
WHERE clause. The language must be the same for all article types.


Standard Objects Knowledge__kav

**Field** **Details**

Before API version 47.0, you must include the `Language` field to filter queries on Knowledge
article versions. In API version 47.0 and later, you can filter queries on Knowledge article
versions with or without `Language` depending on what you are querying.

```
LastPublishedDate

MasterVersionId

MigratedToFromArticleVersion

NextReviewDate

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was last published.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source article, if the article is the translation of a source article. Only accessible if
your knowledge base supports multiple languages.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the corresponding pre- or post-migration article version. Contains values only in
orgs that migrate from Classic to Lightning Knowledge. Available in API version 43.0 and
later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article must next be reviewed for accuracy. Available in API version 58.0
and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the article's owner.


Standard Objects Knowledge__kav

**Field** **Details**

```
PublishStatus

RecordTypeId

SourceId

Summary

Title

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The publication status for the article:

**•** `Draft` : any draft articles.

**•** `Online` : articles published in Salesforce Knowledge.

**•** `Archived` : archived articles.

A user must have the “Manage Articles” permission enabled to use `Online` .

Article queries and searches in SOQL or SOSL require that you specify either the
`PublishStatus` or the `Id` field in the WHERE clause. You can search for only one
publication status per article type in a single SOSL query. When searching for articles with a
`PublishStatus` of `Archived`, also check that `IsLatestVersion` equals `false`
in your WHERE clause.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the API Name that describes the type of article. Use the record type to determine
the article structure and other settings for different types of content.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the source from which the article was created (Case or Reply). This field is only accessible
from the API and isn’t visible in the Salesforce UI.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Summary of the article. Maximum size is 1000 characters.

**Type**
string


Standard Objects Knowledge__kav

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Article's title. Maximum size is 255 characters.

```
TranslationCompletedDate

TranslationExportedDate

TranslationImportedDate

UrlName

ValidationStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last translated. Only accessible if your knowledge base
supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last exported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the article was last imported for translation. Only accessible if your
knowledge base supports multiple languages.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Represents the article's URL. Can contain alphanumeric characters and hyphens
but can't begin or end with a hyphen. Use a unique value regardless of context. (For example,
a unique value allows you to get expected results when running an Apex test with
`SeeAllData` set to `false` .) `UrlName` is case-sensitive and its maximum size is 255
characters.

**Type**
picklist


### Standard Objects Knowledge__DataCategorySelection

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group

**Description**

Shows whether the content of the article has been validated. Possible values are
`Validated` and `Not Validated` . The default value is `Not Validated` . This field
is available in API version 24.0 or later.

```
VersionNumber

```

**Type**
int

**Properties**
Group, Sort

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.

### Knowledge__DataCategorySelection

Represents a data category that classifies an article. This object is available in API version 39.0 and later.

### Note: By default, the prefix for this object name is Knowledge and that is the value shown in this reference. However, this

prefix can be modified by changing the **Object Name** for the Knowledge__kav object in Object Manager.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Lightning Knowledge must be enabled in your org.

Fields

**Field** **Details**

```
DataCategoryGroupName

```

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category group which has categories associated with the article.


### Standard Objects KnowledgeableUser

**Field** **Details**

```
 DataCategoryName

 ParentId

```

Usage

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the article associated with the data category selection.

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use this object to query and manage article categorization in your organization. Client applications can create
a categorization for an article with a Draft status. They can also delete and query article categorizations.

Note: When using this object to classify an article, you can't select both a category (for example USA) and one of its descendants
(California) or ascendant categories (North America). In this case, only the first category is selected.

### KnowledgeableUser

Represents a user identified as knowledgeable about a specific topic, and ranks them relative to other knowledgeable users. This object
is available in API version 31.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
NetworkId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects KnowledgeArticle

**Field Name** **Details**

**Description**
ID of the Experience Cloud site the topic exists in. This field is available only if
digigal experiences is enabled for your org.

```
RawRank

TopicId

UserId

### KnowledgeArticle

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank of this user’s knowledge on the topic relative to other users.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the topic in Salesforce.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique ID for the user in Salesforce.

Provides read-only access to an article and the ability to delete the primary article. This object is available in API version 19.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Unlike KnowledgeArticleVersion, the ID of a KnowledgeArticle record is identical irrespective of the article's version (status).

Knowledge__ka on page 2990 is derived from this object.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects KnowledgeArticle

Special Access Rules

Knowledge must be enabled in your org. A user must have the View Articles permission enabled. Salesforce Knowledge users, unlike
customer and partner users, must also be granted the `Knowledge User` feature license.

Fields

**Field Name** **Details**

```
ArchivedById

ArchivedDate

ArticleNumber

CaseAssociationCount

FirstPublishedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was archived.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique number automatically assigned to the article when it's created. You can't
change the format or value for this field.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of cases attached to the article.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the article was first published.


Standard Objects KnowledgeArticle

**Field Name** **Details**

```
IsGeneratedByLlm

LastPublishedDate

LastReferencedDate

LastViewedDate

MasterLanguage

MigratedToFromArticle

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the first version of an article was created with an LLM. This object is available
in API version 59.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

