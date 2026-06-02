Maximum number of Apex jobs added to the queue with `System.enqueueJob` 50 1

Total number of `sendEmail` methods allowed 10 10

Total heap size [4] 6 MB 12 MB

Maximum CPU time on the Salesforce servers [5] 10,000 milliseconds 60,000 milliseconds

Maximum execution time for each Apex transaction 10 minutes 10 minutes

Maximum number of push notification method calls allowed per Apex transaction 10 10

Maximum number of push notifications that can be sent in each push notification method 2,000 2,000
call

Maximum number of `EventBus.publish` calls for platform events configured to 150 150
publish immediately

Maximum number of rows across all Apex cursors per transaction 50 million 50 million

Maximum number of Apex cursors per day 10,000 10,000

Maximum number of `Cursor.fetch` calls per transaction 100 100


Apex Developer Guide Apex Transactions and Governor Limits

**Description** **Synchronous** **Asynchronous**
**Limit** **Limit**

Maximum cumulative number of new cursor rows and pagination cursor rows per 24-hour 100 million 100 million
period

Maximum number of rows across all Apex pagination cursors per transaction 100,000 100,000

Maximum number of Apex pagination cursor instances per transaction 50 50

Maximum number of Apex pagination cursor instances per 24-hour period 200,000 200,000

Maximum number of rows retrieved per page from an Apex pagination cursor 2000 2000

1 In a SOQL query with parent-child relationship subqueries, each parent-child relationship counts as an extra query. These types of
queries have a limit of three times the number for top-level queries. The limit for subqueries corresponds to the value that
`Limits.getLimitAggregateQueries()` returns. The row counts from these relationship queries contribute to the row
counts of the overall code execution. This limit doesn’t apply to custom metadata types. In a single Apex transaction, custom metadata
records can have unlimited SOQL queries. In addition to static SOQL statements, calls to the following methods count against the number
of SOQL statements issued in a request.

**•** `Database.countQuery`, `Database.countQueryWithBinds`

**•** `Database.getQueryLocator`, `Database.getQueryLocatorWithBinds`

**•** `Database.query`, `Database.queryWithBinds`

2 Calls to the following methods count against the number of DML statements issued in a request.

**•** `Approval.process`

**•** `Database.convertLead`

**•** `Database.emptyRecycleBin`

**•** `Database.rollback`

**•** `Database.setSavePoint`

**•** `delete` and `Database.delete`

**•** `insert` and `Database.insert`

**•** `merge` and `Database.merge`

**•** `undelete` and `Database.undelete`

**•** `update` and `Database.update`

**•** `upsert` and `Database.upsert`

**•** `EventBus.publish` for platform events configured to publish after commit

**•** `System.runAs`

Recursive Apex that doesn’t fire any triggers with `insert`, `update`, or `delete` statements, exists in a single invocation, with a
single stack. Conversely, recursive Apex that fires a trigger spawns the trigger in a new Apex invocation. The new invocation is separate
from the invocation of the code that caused it to fire. Spawning a new invocation of Apex is a more expensive operation than a recursive
call in a single invocation. Therefore, there are tighter restrictions on the stack depth of these types of recursive calls.

4 Email services heap size is 50 MB.

5 CPU time is calculated for all executions on the Salesforce application servers occurring in one Apex transaction. CPU time is calculated
for the executing Apex code, and for any processes that are called from this code, such as package code and workflows. CPU time is
private for a transaction and is isolated from other transactions. Application server CPU time spent in DML operations is counted towards


Apex Developer Guide Apex Transactions and Governor Limits

the Apex CPU limit. Operations that don't consume application server CPU time aren't counted toward CPU time. For example, the
portion of execution time spent in the database for DML, SOQL, and SOSL isn't counted, nor is waiting time for Apex callouts. Bulk API
and Bulk API 2.0 consume a unique governor limit for CPU time on Salesforce Servers, with a maximum value of 60,000 milliseconds.

Note:

**•** Limits apply individually to each `testMethod` .

**•** To determine the code execution limits for your code while it’s running, use the Limits methods. For example, you can use
the `getDMLStatements` method to determine the number of DML statements that have already been called by your
program. Or, you can use the `getLimitDMLStatements` method to determine the total number of DML statements
available to your code.

Per-Transaction Certified Managed Package Limits

Certified managed packages—managed packages that have passed the security review for AppExchange—get their own set of limits
for most per-transaction limits. Salesforce ISV Partners develop certified managed packages, which are installed in your org from
AppExchange and have unique namespaces.

Here’s an example that illustrates the separate certified managed package limits for DML statements. If you install a certified managed
package, all the Apex code in that package gets its own 150 DML statements. These DML statements are in addition to the 150 DML
statements your org’s native code can execute. This limit increase means that more than 150 DML statements can execute during a
single transaction if code from the managed package and your native org both executes. Similarly, the certified managed package gets
its own 100-SOQL-query limit for synchronous Apex, in addition to the org’s native code limit of 100 SOQL queries.

There’s no limit on the number of certified namespaces that can be invoked in a single transaction. However, the number of operations
that can be performed in each namespace must not exceed the per-transaction limits. There’s also a limit on the cumulative number of
operations that can be made across namespaces in a transaction. This cumulative limit is 11 times the per-namespace limit. For example,
if the per-namespace limit for SOQL queries is 100, a single transaction can perform up to 1,100 SOQL queries. In this case, the cumulative
limit is 11 times the per-namespace limit of 100. These queries can be performed across an unlimited number of namespaces, as long
as any one namespace doesn't have more than 100 queries. The cumulative limit doesn’t affect limits that are shared across all namespaces,
such as the limit on maximum CPU time.

Note:

**•** These cross-namespace limits apply only to namespaces in certified managed packages.

**•** Namespaces in non-certified packages don’t have their own separate governor limits. The resources that they use continue
to count against the same governor limits used by the org's custom code.

This table lists the cumulative cross-namespace limits.

**Description** **Cumulative**
**Cross-Namespace Limit**

Total number of SOQL queries issued 1,100

Total number of records retrieved by `Database.getQueryLocator` 110,000

Total number of SOSL queries issued 220

Total number of DML statements issued 1,650

Total number of callouts (HTTP requests or web services calls) in a transaction 1,100

Total number of `sendEmail` methods allowed 110


Apex Developer Guide Apex Transactions and Governor Limits

All per-transaction limits count separately for certified managed packages except for:

**•** The total heap size

**•** The maximum CPU time

**•** The maximum transaction execution time

**•** The maximum number of unique namespaces

These limits count for the entire transaction, regardless of how many certified managed packages are running in the same transaction.

The code from a package from AppExchange, not created by a Salesforce ISV Partner and not certified, doesn’t have its own separate
governor limits. Any resources used by the package count against the total org governor limits. Cumulative resource messages and
warning emails are also generated based on managed package namespaces.

[For more information on Salesforce ISV Partner packages, see Salesforce Partner Programs.](http://sites.force.com/partners/PP2Page?p=P_PartnerPrograms)

Salesforce Platform Apex Limits

The limits in this table aren't specific to an Apex transaction; the Salesforce Platform enforces these limits.

**Description** **Limit**

The maximum number of asynchronous Apex method executions (batch Apex, future methods, 250,000 or the number of
Queueable Apex, and scheduled Apex) per a 24-hour period. This licensed daily limit is the applicable user licenses in your
`DailyAsyncApexExecutions` org limit. [1,6,7] org multiplied by 200, whichever
is greater

The total number of Queueable Apex and future method executions that can be enqueued during The org’s daily asynchronous
a 24-hour period, including elastic executions processed at a throttled rate (beta). This limit is the Apex method executions limit
`DailyAsyncApexElasticExecutions` org limit. [6] plus either the org’s licensed
daily asynchronous Apex
method executions limit or 10
million executions, whichever is
less.

In other words, the extra elastic
executions added to the daily
asynchronous Apex method
executions limit is capped at a
maximum of 10 million
additional executions.

Number of synchronous concurrent transactions for long-running transactions that last longer than Based on the number of
5 seconds for each org. [2] applicable licenses [8] in an org,

the limit is calculated as a ratio
of 100 licenses to one
concurrent long-running Apex
transaction [9] .

**•** Minimum limit is 10

**•** Maximum limit is 50

Maximum number of Apex classes scheduled concurrently 100. In Developer Edition orgs,
the limit is 5.


Apex Developer Guide Apex Transactions and Governor Limits

**Description** **Limit**

Maximum number of batch Apex jobs in the Apex flex queue that are in `Holding` status 100

Maximum number of batch Apex jobs queued or active concurrently [3] 5

Maximum number of batch Apex job `start` method concurrent executions [4] 1

Maximum number of batch jobs that can be submitted in a running test 5

Maximum number of test classes that can be queued per 24-hour period (production orgs other
than Developer Edition) [5,6]

Maximum number of test classes that can be queued per 24-hour period (sandbox and Developer
Edition orgs) [5,6]

The greater of 500 or 10
multiplied by the number of test
classes in the org

The greater of 500 or 20
multiplied by the number of test
classes in the org

For Batch Apex, method executions include executions of the `start`, `execute`, and `finish` methods. This limit is for your entire
org and is shared with all asynchronous Apex: Batch Apex, Queueable Apex, scheduled Apex, and future methods. The license types
that count toward this limit include full Salesforce and Salesforce Platform user licenses, App Subscription user licenses, Chatter Only
users, Identity users, and Company Communities users.

2 If more transactions are started while the default number of long-running transactions are still running, they’re denied. HTTP callout
processing time isn’t included when calculating this limit.

3 When batch jobs are submitted, they’re held in the flex queue before the system queues them for processing.

4 Batch jobs that haven’t started yet remain in the queue until they’re started. If more than one job is running, this limit doesn’t cause
any batch job to fail. `execute` methods of batch Apex jobs still run in parallel.

5 This limit applies to tests running asynchronously. This group of tests includes tests started through the Salesforce user interface
including the Developer Console or by inserting `ApexTestQueueItem` objects using SOAP API.

To check how many asynchronous Apex executions are available, make a request to REST API `limits` resource or use Apex methods
`OrgLimits.getAll()` or `OrgLimits.getMap()` [. See List Organization Limits in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm) _REST API Developer Guide_ [and OrgLimits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_OrgLimits.htm)
[Class in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_OrgLimits.htm) _Apex Reference Guide_ .

7 If the number of asynchronous Apex executions needed by a job exceeds the available number that’s calculated using the 24-hour
rolling limit, an exception is thrown. Batch Apex preemptively checks the required asynchronous job capacity when
`Database.executeBatch` is called and the `start` method has returned the workload. The batch won’t start unless there is
sufficient capacity for the entire job available. For example, if the batch requires 10,000 executions and the remaining asynchronous
limit is 9,500 executions, an `AsyncApexExecutions Limit exceeded` exception is thrown, and the remaining executions
are left unchanged.

8 The license types that count toward this limit include full Salesforce and Salesforce Platform user licenses, App Subscription user licenses,
Chatter Only users, Identity users, and Company Communities users.

9 For example, if your org has 4,000 licenses, the concurrent long-running Apex requests limit is set at 40. If your org has 5,000 or more
licenses, the concurrent long-running Apex requests limit is set at 50, which is the maximum capped limit. If your org has 1,000 or fewer
licenses, the concurrent long-running Apex requests limit is set at 10, which is the minimum floor limit.


Apex Developer Guide Apex Transactions and Governor Limits

Static Apex Limits

**Description** **Limit**

Default timeout of callouts (HTTP requests or Web services calls) in a transaction 10 seconds

Maximum size of callout request or response (HTTP request or Web services call) [1] 6 MB for synchronous Apex or
12 MB for asynchronous Apex

Maximum SOQL query run time before Salesforce cancels the transaction 120 seconds

Maximum number of class and trigger code units in a deployment of Apex 7500

Apex trigger batch size [2] 200

For loop list batch size 200

Maximum number of records returned for a Batch Apex query in `Database.QueryLocator` 50 million

1 The HTTP request and response sizes count towards the total heap size.

2 The Apex trigger batch size for platform events and Change Data Capture events is 2,000. The trigger batch size doesn’t apply when
[using Mass Transfer Records.](https://help.salesforce.com/s/articleView?id=platform.admin_transfer.htm&type=5&language=en_US)

Size-Specific Apex Limits

**Description** **Limit**

Maximum number of characters for a class 1 million

Maximum number of characters for a trigger 1 million

Maximum amount of code used by all Apex code in an org [1,3,4] 6 MB

Method size limit [2] 65,535 bytecode instructions in
compiled form

1 This limit doesn’t apply to Apex code in first generation(1GP) or second generation(2GP) managed packages. The code in those types
of packages belongs to a namespace unique from the code in your org. This limit also doesn’t apply to any code included in a class
defined with the `@isTest` annotation.

2 Large methods that exceed the allowed limit cause an exception to be thrown during the execution of your code.

[3 The default 6 MB limit can be increased by opening a support case for your org. Before you apply for a limit increase, ensure that you’re](https://help.salesforce.com/s/)
[following best practices outlined in Increase Apex Code Character Limit.](https://help.salesforce.com/s/articleView?id=000382172&type=1&language=en_US)

[4 For scratch orgs, the limit is 10MB. The limit can be increased by opening a support case for your org. Before you apply for a limit](https://help.salesforce.com/s/)
[increase, ensure that you’re following the best practices.](https://help.salesforce.com/s/articleView?id=000382172&type=1&language=en_US)

Miscellaneous Apex Limits

**Connect in Apex**

For classes in the `ConnectApi` namespace, every write operation costs one DML statement against the Apex governor limit.
`ConnectApi` method calls are also subject to rate limits. Most `ConnectApi` [method calls count toward the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)


Apex Developer Guide Apex Transactions and Governor Limits

[total API request allocations, which are per org and span a 24-hour period. Only](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) `ConnectApi` method calls that require Chatter
are subject to a per user, per namespace, per hour rate limit. The documentation for every `ConnectApi` method indicates whether
Chatter is required. When you exceed the rate limit, a `ConnectApi.RateLimitException` is thrown. Your Apex code must
catch and handle this exception.

**Data.com Clean**
If you use the Data.com Clean product and its automated jobs, consider how you use Apex triggers. If you have Apex triggers on
account, contact, or lead records that run SOQL queries, the SOQL queries can interfere with Clean jobs for those objects. Your Apex
triggers (combined) must not exceed 200 SOQL queries per batch. If they do, your Clean job for that object fails. In addition, if your
triggers call `future` methods, they’re subject to a limit of 10 `future` calls per batch.

**Event Reports**
The maximum number of records that an event report returns for a user who isn’t a system administrator is 20,000; for system
administrators, 100,000.

**MAX_DML_ROWS limit in Apex testing**
The maximum number of rows that can be inserted, updated, or deleted, in a single, synchronous Apex test execution context, is
limited to 450,000. For example, an Apex class can have 45 methods that insert 10,000 rows each. If the limit is reached, you see this
error: `Your runallTests is consuming too many DB resources` .

**SOQL Query Performance**
[For best performance, use selective SOQL queries. This is especially important for queries inside triggers. See More Efficient SOQL](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_VLSQ.htm)
[Queries.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_VLSQ.htm)

Email Limits

**Inbound Email Limits**

Email Services: Maximum Number of Email Messages Processed Number of user licenses multiplied by
1,000; maximum 1,000,000

(Includes limit for On-Demand Email-to-Case)

Email Services: Maximum Size of Email Message (Body and Attachments) 25 MB [1]

On-Demand Email-to-Case: Maximum Email Attachment Size 25 MB

On-Demand Email-to-Case: Maximum Number of Email Messages Processed Number of user licenses multiplied by
1,000; maximum 1,000,000

(Counts toward limit for Email Services)

1 The maximum size of email messages for Email Services varies depending on the character set and transfer encoding of the body
parts. The size of an email message includes the email headers, body, attachments, and encoding. As a result, an email with a 35-MB
attachment likely exceeds the 25-MB size limit for an email message after accounting for the headers, body, and encoding.

When defining email services, note the following:

**•** An email service only processes messages it receives at one of its addresses.

**•** Salesforce limits the total number of messages that all email services combined, including On-Demand Email-to-Case, can
process daily. Messages that exceed this limit are bounced, discarded, or queued for processing the next day, depending on
how you configure the failure response settings for each email service. Salesforce calculates the limit by multiplying the number
of user licenses by 1,000; maximum 1,000,000. For example, if you have 10 licenses, your org can process up to 10,000 email
messages a day.

**•** Email service addresses that you create in your sandbox can’t be copied to your production org.


Apex Developer Guide Apex Transactions and Governor Limits

**•** For each email service, you can tell Salesforce to send error email messages to a specified address instead of the sender's email
address.

**•** Email services reject email messages and notify the sender if the email (combined body text, body HTML, and attachments)
exceeds approximately 25 MB (varies depending on language and character set).

**Outbound Email: Limits for Single and Mass Email Sent Using Apex**

Each licensed org can send single emails to a maximum of 5,000 external email addresses per day based on Greenwich Mean Time
(GMT). For orgs created before Spring ’19, the daily limit is enforced only for emails sent via Apex and Salesforce APIs except for REST
API. For orgs created in Spring ’19 and later, the daily limit is also enforced for email alerts, simple email actions, Send Email actions
in flows, and REST API. If one of the newly counted emails can’t be sent because your org has reached the limit, we notify you by
email and add an entry to the debug logs. Single emails sent using the email author or composer in Salesforce don't count toward
this limit. There’s no limit on sending single emails to contacts, leads, person accounts, and users in your org directly from account,
contact, lead, opportunity, case, campaign, or custom object pages. In Developer Edition orgs and orgs evaluating Salesforce during
a trial period, you can send to a maximum of 50 recipients per day, and each single email can have up to 15 recipients.

Keep these considerations in mind when sending emails:

**•** When sending single emails, you can specify up to 150 recipients across the `To`, `CC`, and `BCC` fields in each
`SingleEmailMessage` . Each field is also limited to 4,000 bytes.

**•** If you use `SingleEmailMessage` to email your org’s internal users, specifying the user’s ID in `setTargetObjectId`
means the email doesn’t count toward the daily limit. However, specifying internal users’ email addresses in `setToAddresses`
means the email does count toward the limit.

**•** You can send mass email and list email to a maximum of 5,000 external email addresses per day per licensed Salesforce org. A
day is calculated based on Greenwich Mean Time (GMT).

**•** The single email, mass email, and list email limits count duplicate email addresses. For example, if you have
`johndoe@example.com` in your email 10 times that counts as 10 against the limit.

**•** API or Apex single emails can be sent to a maximum of 5,000 external email addresses per day.

**•** You can send an unlimited amount of email through the UI to your org’s internal users, which include portal users.

**•** You can send mass emails and list emails only to contacts, person accounts, leads, and your org’s internal users.

**•** In Developer Edition orgs and orgs evaluating Salesforce during a trial period, you can send to no more than 10 external email
recipients per org per day using mass email and list email.

**•** You can’t send mass email using a Visualforce email template.

Push Notification Limits

An org can send up to 20,000 iOS and 10,000 Android push notifications per hour (for example, 4:00 to 4:59 UTC).

Only _deliverable_ notifications count toward this limit. For example, a notification is sent to 1,000 employees in your company, but 100
employees haven’t installed the mobile app yet. Only the notifications sent to the 900 employees who have installed the mobile app
count toward this limit.

Each test push notification that is generated through the Test Push Notification page is limited to a single recipient. Test push notifications
count toward an org’s hourly push notification limit.

When an org's hourly push notification limit is met, any additional notifications are still created for in-app display and retrieval via REST
API.

SEE ALSO:

Asynchronous Callout Limits

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_


Apex Developer Guide Apex Transactions and Governor Limits

#### Elastic Limits for Asynchronous Apex Jobs (Beta)

To help avoid disruptions to your workflow, enable elastic limits for asynchronous Apex jobs (beta). The setting supports throttled
processing of asynchronous jobs above the standard daily limit, which prevents execution failures and limit exceptions if your org reaches
or exceeds this limit.

Important: Elastic Limits for Queueable Apex and Future Methods is a pilot or beta service that is subject to the Beta Services
[Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the](https://www.salesforce.com/company/legal/agreements/)
[Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)

Elastic Limits Overview

Important: Elastic limits for asynchronous Apex jobs (beta) applies to only Queueable Apex and future methods in production
and demo orgs. Batch Apex and scheduled jobs currently remain capped at the daily asynchronous job limit.

If you enable the “Use elastic limits for asynchronous Apex jobs (Beta)” setting, you can enqueue Queueable Apex and future method
jobs up to an increased elastic asynchronous job limit. This elastic limit is the org’s daily asynchronous job limit plus either the org’s
licensed daily asynchronous job limit (defined as 250,000 jobs or 200 times the number of applicable user licenses, whichever is greater)
or 10 million jobs, whichever is less.

In other words, the `DailyAsyncApexElasticExecutions` limit is calculated according to this formula:

```
   // DailyAsyncApexElasticExecutions limit calculation (pseudocode)

   DailyAsyncApexElasticExecutions = DailyAsyncApexExecutions + min(licensed

   DailyAsyncApexExecutions, 10000000)

```

For example, if an org’s daily asynchronous Apex job limit is 250,000 and the org’s licensed daily asynchronous job limit is 250,000, then
the org’s elastic limit is 500,000 jobs (250,000 + 250,000). However, if an org’s daily asynchronous Apex job limit is 12 million and the
org’s licensed daily asynchronous job limit is 12 million, then the org’s elastic limit is 22 million jobs (12 million + 10 million).

If an org reaches both the daily asynchronous Apex job limit and the elastic asynchronous job limit, exceptions are thrown for enqueued
jobs that exceed the elastic limit.

If the number of asynchronous Apex jobs processed over a rolling 24-hour period exceeds the daily limit, Salesforce processes any
additional enqueued asynchronous jobs at a throttled rate of one concurrent job per asynchronous Apex type. Processing resumes the
regular, non-throttled concurrency rate only after the number of executed asynchronous jobs in the past 24 hours falls below the daily
limit.

Enable Elastic Limits

To enable elastic limits for asynchronous Apex:

**1.** In Setup, in the Quick Find box, enter _`Apex Settings`_, and then select **Apex Settings** .

**2.** Select **Use elastic limits for asynchronous Apex jobs (Beta)** .

**3.** Save your changes.

Monitor Asynchronous Job Usage

To check your asynchronous job usage against the daily and elastic limits, see the Apex Jobs page in Setup. A banner shows the number
of asynchronous jobs processed in the past 24 hours, along with the org’s daily and elastic limits. It also indicates whether asynchronous
processing is currently being throttled.


Apex Developer Guide Apex Transactions and Governor Limits

You can also use these methods on the `[OrgLimits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_OrgLimits.htm)` class to check asynchronous job usage.

```
   // Map of OrgLimit instances

   Map<String,System.OrgLimit> limitsMap = OrgLimits.getMap();

   // Daily Limit Methods

   System.OrgLimit asyncApexDailyLimit = limitsMap.get('DailyAsyncApexExecutions');

   System.debug('Limit Name: ' + asyncApexDailyLimit.getName());

   // The total async jobs enqueued in the past 24 hours.

   // Gives the same value as asyncApexElasticLimit.getValue()

   System.debug('Usage Value: ' + asyncApexDailyLimit.getValue());

   // The daily async job limit

   System.debug('Maximum Limit: ' + asyncApexRequestsLimit.getLimit());

   // ------------------------------------------------
   // Elastic Limit Methods

   System.OrgLimit asyncApexElasticLimit = limitsMap.get('DailyAsyncApexElasticExecutions');

   System.debug('Limit Name: ' + asyncApexElasticLimit.getName());

   // The total async jobs enqueued in the past 24 hours.

   // Gives the same value as the asyncApexDailyLimit.getValue()

   System.debug('Usage Value: ' + asyncApexElasticLimit.getValue());

   // The sum of the daily limit and the additional jobs allowed up to the elastic limit

   System.debug('Maximum Limit: ' + asyncApexElasticLimit.getLimit());

```

For example, let’s say an org’s daily limit is 400,000 asynchronous jobs, and it enqueues 700,000 asynchronous jobs within a 24-hour
period. Here’s the org’s `DailyAsyncApexExecutions` and `DailyAsyncApexElasticExecutions` OrgLimits instance
values.

```
   // Example Org Limits for Async Jobs

   // Daily Limit Methods

   Limit Name: DailyAsyncApexExecutions

   Usage Value: 700000

   Maximum Limit: 400000

   // Elastic Limit Methods

   Limit Name: DailyAsyncApexElasticExecutions

```


Apex Developer Guide Apex Transactions and Governor Limits

```
   Usage Value: 700000

   Maximum Limit: 800000

```

When you use the `OrgLimits` class, keep these considerations in mind.

**•** If the “Use elastic limits for asynchronous Apex jobs (Beta)” setting isn’t enabled, the `OrgLimits.getMap()` method doesn’t
return a `DailyAsyncApexElasticExecutions` key-value pair.

**•** The `getValue()` method returns the total number of asynchronous jobs _enqueued_ over the last 24 hours, not the number
_executed_ . Because asynchronous jobs are throttled only when actual executions exceed the daily limit, the enqueued jobs count
may surpass the daily limit when asynchronous jobs are still being processed at the regular concurrency rate.

#### Set Up Governor Limit Email Warnings

You can specify users in your organization to receive an email notification when they invoke Apex code that surpasses 50% of allocated
governor limits. Only per-request limits are checked for sending email warnings; per-org limits like concurrent long-running requests
are not checked. These email notifications do not count against the daily single email limit.

Important: System-generated emails from an unverified email-sending domain aren’t delivered, even if the From email address
[is verified. See Requirements to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

**1.** Log in to Salesforce as an administrator user.

**2.** From Setup, enter _`Users`_ in the `Quick Find` box, then select **Users** .

**3.** Click **Edit** next to the name of the user to receive the email notifications.

Note: Only users with Author Apex permission can receive email notifications.

**4.** Select the `Send Apex Warning Emails` option.

Note: Only users with Author Apex permission can view and update this option.

**5.** Click **Save** .

Note: These limits are currently checked for sending email warnings.

Total number of SOQL queries issued

Total number of records retrieved by SOQL queries

Total number of SOSL queries issued

Total number of DML statements issued

Total number of records processed as a result of DML statements, `Approval.process`, or `database.emptyRecycleBin`

Total heap size

Total number of callouts (HTTP requests or Web services calls) in a transaction

Total number of `sendEmail` methods allowed

Maximum number of methods with the `future` annotation allowed per Apex invocation

Maximum number of Apex jobs added to the queue with `System.enqueueJob`

Total number of records retrieved by `Database.getQueryLocator`

Total number of mobile Apex push calls


Apex Developer Guide Apex Transactions and Governor Limits

#### Running Apex within Governor Execution Limits

When you develop software in a multitenant cloud environment such as the Lightning platform, you don’t have to scale your code,
because the Lightning platform does it for you. Because resources are shared in a multitenant platform, the Apex runtime engine enforces
some limits to ensure that no one transaction monopolizes shared resources.

Your Apex code must execute within these predefined execution limits. If a governor limit is exceeded, a run-time exception that can’t
be handled is thrown. By following best practices in your code, you can avoid hitting these limits. Imagine you had to wash 100 T-shirts.
Would you wash them one by one—one per load of laundry, or would you group them in batches for just a few loads? The benefit of
coding in the cloud is that you learn how to write more efficient code and waste fewer resources.

The governor execution limits are per transaction. For example, one transaction can issue up to 100 SOQL queries and up to 150 DML
statements. There are some other limits that aren’t transaction bound, such as the number of batch jobs that can be queued or active
at one time.

The following are some best practices for writing code that doesn’t exceed certain governor limits.

Bulkifying DML Calls

Making DML calls on lists of sObjects instead of each individual sObject makes it less likely to reach the DML statements limit. The
following is an example that doesn’t bulkify DML operations, and the next example shows the recommended way of calling DML
statements.

**Example:** DML calls on single sObjects

The for loop iterates over line items contained in the `liList` List variable. For each line item, it sets a new value for the Description__c
field and then updates the line item. If the list contains more than 150 items, the 151st update call returns a run-time exception for
exceeding the DML statement limit of 150. How do we fix this? Check the second example for a simple solution.

```
   for(Line_Item__c li : liList) {

      if (li.Units_Sold__c > 10) {

        li.Description__c = 'New description';

      }

      // Not a good practice since governor limits might be hit.

      update li;

   }

```

**Recommended Alternative:** DML calls on sObject lists

This enhanced version of the DML call performs the update on an entire list that contains the updated line items. It starts by creating a
new list and then, inside the loop, adds every update line item to the new list. It then performs a bulk update on the new list.

```
   List<Line_Item__c> updatedList = new List<Line_Item__c>();

   for(Line_Item__c li : liList) {

      if (li.Units_Sold__c > 10) {

        li.Description__c = 'New description';

        updatedList.add(li);

      }

   }

   // Once DML call for the entire list of line items

   update updatedList;

```


Apex Developer Guide Apex Transactions and Governor Limits

More Efficient SOQL Queries

Placing SOQL queries inside `for` loop blocks isn’t a good practice because the SOQL query executes once for each iteration and may
surpass the 100 SOQL queries limit per transaction. The following is an example that runs a SOQL query for every item in `Trigger.new`,
which isn’t efficient. An alternative example is given with a modified query that retrieves child items using only one SOQL query.

**Example:** Inefficient querying of child items

The `for` loop in this example iterates over all invoice statements that are in `Trigger.new` . The SOQL query performed inside the
loop retrieves the child line items of each invoice statement. If more than 100 invoice statements were inserted or updated, and thus
contained in `Trigger.new`, this results in a run-time exception because of reaching the SOQL limit. The second example solves this
problem by creating another SOQL query that can be called only once.

```
   trigger LimitExample on Invoice_Statement__c (before insert, before update) {

      for(Invoice_Statement__c inv : Trigger.new) {

        // This SOQL query executes once for each item in Trigger.new.

        // It gets the line items for each invoice statement.

        List<Line_Item__c> liList = [SELECT Id,Units_Sold__c,Merchandise__c

                          FROM Line_Item__c

                          WHERE Invoice_Statement__c = :inv.Id];

        for(Line_Item__c li : liList) {

           // Do something

        }

      }

   }

```

**Recommended Alternative:** Querying of child items with one SOQL query

This example bypasses the problem of having the SOQL query called for each item. It has a modified SOQL query that retrieves all invoice
statements that are part of `Trigger.new` and also gets their line items through the nested query. In this way, only one SOQL query
is performed and we’re still within our limits.

```
   trigger EnhancedLimitExample on Invoice_Statement__c (before insert, before update) {

      // Perform SOQL query outside of the for loop.

      // This SOQL query runs once for all items in Trigger.new.

      List<Invoice_Statement__c> invoicesWithLineItems =

       [SELECT Id,Description__c,(SELECT Id,Units_Sold__c,Merchandise__c from Line_Items__r)

         FROM Invoice_Statement__c WHERE Id IN :Trigger.newMap.KeySet()];

      for(Invoice_Statement__c inv : invoicesWithLineItems) {

        for(Line_Item__c li : inv.Line_Items__r) {

           // Do something

        }

      }

   }

```

SOQL For Loops

Use SOQL for loops to operate on records in batches of 200. This helps avoid the heap size limit of 6 MB. Note that this limit is for code
running synchronously and it is higher for asynchronous code execution.

**Example:** Query without a for loop


### Apex Developer Guide Using Salesforce Features with Apex

The following is an example of a SOQL query that retrieves all merchandise items and stores them in a List variable. If the returned
merchandise items are large in size and a large number of them was returned, the heap size limit might be hit.

```
   List<Merchandise__c> ml = [SELECT Id,Name FROM Merchandise__c];

```

**Recommended Alternative:** Query within a for loop

To prevent this from happening, this second version uses a SOQL for loop, which iterates over the returned results in batches of 200
records. This reduces the size of the `ml` list variable which now holds 200 items instead of all items in the query results, and gets recreated
for every batch.

```
   for (List<Merchandise__c> ml : [SELECT Id,Name FROM Merchandise__c]){

      // Do something.

   }

### Using Salesforce Features with Apex

```

Many features of the Salesforce user interface are exposed in Apex so that you can access them programmatically in the Lightning
Platform. For example, you can write Apex code to post to a Chatter feed, or use the approval methods to submit and approve process
requests.

Actions
Create quick actions, and add them to your Salesforce Classic home page, to the Chatter tab, to Chatter groups, and to record detail
pages. Choose from standard quick actions, such as create and update actions, or create custom actions based on your company’s
needs.

Apex Cursors
Use Apex cursors to break up the processing of a SOQL query result into pieces that can be processed within the bounds of a single
transaction. Cursors provide you with the ability to work with large query result sets, while not actually returning the entire result
set. You can traverse a query result in parts, with the flexibility to navigate forward and back in the result set. Package developers
and advanced developers can use cursors to work with high-volume and high-resource processing jobs. Cursors combined with
chained queueable Apex jobs are a powerful alternative to batch Apex and address some of batch Apex’s limitations.

Approval Processing
An approval process automates how records are approved in Salesforce. An approval process specifies each step of approval, including
from whom to request approval and what to do at each point of the process.

Authentication
Salesforce provides various ways to authenticate users. Build a combination of authentication methods to fit the needs of your org
and your users’ use patterns.

Chatter Answers and Ideas
In Chatter Answers and Ideas, use zones to organize ideas and answers into groups. Each zone can have its own focus, with unique
ideas and answers topics to match that focus.

Use Cases for the CommercePayments Namespace
Review walkthroughs, use cases, and reference material for the `CommercePayments` platform.

Connect in Apex
Use Connect in Apex to develop custom experiences in Salesforce. Connect in Apex provides programmatic access to B2B Commerce,
CMS managed content, Experience Cloud sites, topics, and more. Create Apex pages that display Chatter feeds, post feed items with
mentions and topics, and update user and group photos. Create triggers that update Chatter feeds.


Apex Developer Guide Using Salesforce Features with Apex

Moderate Chatter Private Messages with Triggers
Write a trigger for ChatterMessage to automate the moderation of private messages in an org or Experience Cloud site. Use triggers
to ensure that messages conform to your company’s messaging policies and don’t contain blocklisted words.

Data 360 In Apex
You can use Apex with Data 360 objects, with constraints and considerations that are detailed in this topic . Further, you can mock
SOQL query responses for Data 360 data model objects (DMOs) in Apex testing by using SOQL stub methods and a test class.

DataWeave in Apex
DataWeave in Apex uses the Mulesoft DataWeave library to read and parse data from one format, transform it, and export it in a
different format. You can create DataWeave scripts as metadata and invoke them directly from Apex. Like Apex, DataWeave scripts
are run within Salesforce application servers, enforcing the same heap and CPU limits on the executing code.

Moderate Feed Items with Triggers
Write a trigger for FeedItem to automate the moderation of posts in an org or Experience Cloud site. Use triggers to ensure that
posts conform to your company’s communication policies and don’t contain unwanted words or phrases.

Experience Cloud Sites
Experience Cloud sites are branded spaces for your employees, customers, and partners to connect. You can customize and create
sites to meet your business needs, then transition seamlessly between them.

Email
You can use Apex to work with inbound and outbound email.

External Services
External Services connect your Salesforce org to a service outside of Salesforce, such as an employee banking service. After you
register the external service, you can call it natively in your Apex code. Objects and operations defined in the external service's
registered API specification become Apex classes and methods in the `ExternalService` namespace. The registered service's
schema types map to Apex types, and are strongly typed, making the Apex compiler do the heavy lifting for you. For example, you
can make a type safe callout to an external service from Apex without needing to use the `Http` class or perform transforms on
JSON strings.

Flows
Flow Builder lets admins build applications, known as _flows_, that automate a business process. Flows collect data and perform actions
in your Salesforce org or an external system.

Formula Evaluation in Apex
Formula evaluation in Apex helps avoid unnecessary DML statements to recalculate formula field values and evaluate dynamic
formula expressions. Dynamic formulas in Apex support SObjects and Apex objects as context objects. The context type that
corresponds to the Apex class used in the `FormulaBuilder.withType()` method must be a global, user-defined Apex
class. Any fields, properties, or methods that the formula references must also be global.

Metadata
Salesforce uses metadata types and components to represent org configuration and customization. Metadata is used for org settings
that admins control, or configuration information applied by installed apps and packages.

Permission Set Groups
To provide Apex test coverage for permission set groups, write tests using the `calculatePermissionSetGroup()` method
in the `System.Test` class.

Platform Cache
The Lightning Platform Cache layer provides faster performance and better reliability when caching Salesforce session and org data.
Specify what to cache and for how long without using custom objects and settings or overloading a Visualforce view state. Platform
Cache improves performance by distributing cache space so that some applications or operations don’t steal capacity from others.


Apex Developer Guide Using Salesforce Features with Apex

Salesforce Knowledge
Salesforce Knowledge is a knowledge base where users can easily create and manage content, known as articles, and quickly find
and view the articles they need.

Salesforce Files
Use Apex to customize the behavior of Salesforce Files.

Salesforce Connect
Apex code can access external object data via any Salesforce Connect adapter. Use the Apex Connector Framework to develop a
custom adapter for Salesforce Connect. The custom adapter can retrieve data from external systems and synthesize data locally.
Salesforce Connect represents that data in Salesforce external objects, enabling users and the Lightning Platform to seamlessly
interact with data that’s stored outside the Salesforce org.

Salesforce Reports and Dashboards API via Apex
The Salesforce Reports and Dashboards API via Apex gives you programmatic access to your report data as defined in the report
builder.

Salesforce Sites
Salesforce Sites lets you build custom pages and Web applications by inheriting Lightning Platform capabilities including analytics,
workflow and approvals, and programmable logic.

Support Classes
Support classes allow you to interact with records commonly used by support centers, such as business hours and cases.

Territory Management 2.0
With trigger support for the Territory2 and UserTerritory2Association standard objects, you can automate actions and processes
related to changes in these territory management records.

#### Actions

Create quick actions, and add them to your Salesforce Classic home page, to the Chatter tab, to Chatter groups, and to record detail
pages. Choose from standard quick actions, such as create and update actions, or create custom actions based on your company’s needs.

**•** _Create actions_ let users create records—like New Contact, New Opportunity, and New Lead.

**•** _Custom actions_ invoke Lightning components, flows, Visualforce pages, or canvas apps with functionality that you define.Use a
Visualforce page, Lightning component, or a canvas app to create global custom actions for tasks that don’t require users to use
records that have a relationship to a specific object. Object-specific custom actions invoke Lightning components, flows, Visualforce
pages, or canvas apps that let users interact with or create records that have a relationship to an object record.

For create, Log a Call, and custom actions, you can create either object-specific actions or global actions. Update actions must be
object-specific.


Apex Developer Guide Using Salesforce Features with Apex

For more information on actions, see the online help.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_system_quickaction.htm)_ : QuickAction Class

_Apex Reference Guide_ [: QuickActionRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_quickactionrequest.htm)

_Apex Reference Guide_ [: QuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_quickactionresult.htm)

_Apex Reference Guide_ [: DescribeQuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describequickactionresult.htm)

_Apex Reference Guide_ [: DescribeQuickActionDefaultValue Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describequickactiondefaultvalue.htm)

_Apex Reference Guide_ [: DescribeLayoutSection Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describelayoutsection.htm)

_Apex Reference Guide_ [: DescribeLayoutRow Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describelayoutrow.htm)

_Apex Reference Guide_ [: DescribeLayoutItem Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describelayoutitem.htm)

_Apex Reference Guide_ [: DescribeLayoutComponent Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describelayoutcomponent.htm)

_Apex Reference Guide_ [: DescribeAvailableQuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_quickaction_describeavailablequickactionresult.htm)

#### Apex Cursors

Use Apex cursors to break up the processing of a SOQL query result into pieces that can be processed within the bounds of a single
transaction. Cursors provide you with the ability to work with large query result sets, while not actually returning the entire result set.
You can traverse a query result in parts, with the flexibility to navigate forward and back in the result set. Package developers and advanced
developers can use cursors to work with high-volume and high-resource processing jobs. Cursors combined with chained queueable
Apex jobs are a powerful alternative to batch Apex and address some of batch Apex’s limitations.

Apex cursors are stateless and generate results from the offset position that is specified in the `Cursor.fetch(integer`
`position, integer count)` method. You must track the offsets or positions of the results within your particular processing
scenario.

A cursor is created when a SOQL query is executed on a `Database.getCursor()` or `Database.getCursorWithBinds()`
call. When a `Cursor.fetch(integer position, integer count)` method is invoked with an offset position and the
count of records to fetch, the corresponding rows are returned from the cursor. The maximum number of rows per cursor is 50 million,
regardless of whether the operation is synchronous or asynchronous. To get the number of cursor rows returned from the SOQL query,
use `Cursor.getNumRecords()` .

Calling the `Cursor.fetch()` method counts against the SOQL query limit, and the rows fetched count against the SOQL query
row limit. You can make a maximum of 100 `Cursor.fetch()` calls per transaction.

Apex cursors throw these new System exceptions: `System.FatalCursorException` and
`System.TransientCursorException` . Transactions that fail with `System.TransientCursorException` can be
retried.

Apex Cursor Example

```
   public with sharing class QueryChunkingQueueable implements Queueable {

      private Database.Cursor locator;

      private Integer position;

      public QueryChunkingQueueable() {

        locator = Database.getCursor(

           'SELECT Id FROM Contact WHERE LastActivityDate = LAST_N_DAYS:400',

           AccessLevel.USER_MODE);

```


Apex Developer Guide Using Salesforce Features with Apex

```
        position = 0;

      }

      public void execute(QueueableContext ctx) {

        Integer remainingRows = locator.getNumRecords() - position;

        if (remainingRows == 0) {

           return; // Nothing to do

        }

        // Take the minimum of batch size and remaining rows to avoid over-fetching

        Integer fetchSize = Math.min(200, remainingRows);

        List<Contact> scope = locator.fetch(position, 200);

        position += scope.size();

        // do something, like archive or delete the scope list records

        if (position < locator.getNumRecords()) {

           // process the next chunk

           System.enqueueJob(this);

        }

      }

   }

```

Pagination Cursors

Like a standard Apex cursor, an Apex pagination cursor provides a pointer to a large SOQL query result set. However, an Apex pagination
cursor is designed for UI-based pagination, such as multipage record lists.

To create a pagination cursor, call `Database.getPaginationCursor()` or
`Database.getPaginationCursorWithBinds()` with a SOQL query as an argument. A single
`Database.PaginationCursor` instance can have a maximum of 100,000 rows, regardless of whether the operation is synchronous
or asynchronous. This size limit is lower than that of a regular Apex cursor, as pagination cursors are designed for human-readable data.

However, pagination cursors have a higher instance daily limit than that of regular Apex cursors. Whereas standard cursors are limited
to 10,000 instances per org per 24-hour period, pagination cursors are limited to 200,000 instances per org per 24-hour period. This
higher instance limit supports many users accessing records lists that rely on smaller pagination cursors.

To retrieve a page of rows from a pagination cursor, call `PaginationCursor.fetchPage(integer start, integer`
`pageSize)` . The _`start`_ parameter is the zero-based index from which to begin fetching rows, and the _`pageSize`_ is the maximum
number of rows to retrieve for this page. The maximum _`pageSize`_ value is 2000 rows.

Unlike a standard Apex cursor, a pagination cursor retrieves a complete page of records, where record rows deleted after the creation
of the cursor are skipped over by default. This way, the number of rows displayed per page is consistent.

For example, let’s say that you create a standard cursor and a pagination cursor on the same SOQL query, where the result set is 100
rows. After the cursors are created, you delete the first five rows in the set, indexed 0-4. If you then call `Cursor.fetch(0, 20)`,
only 15 rows are retrieved—rows indexed 5-19. However, if you call `PaginationCursor.fetchPage(0, 20)`, 20 rows are
retrieved—rows indexed 5-24. The `fetchPage()` method automatically skips over the five deleted records so that a complete page
is retrieved.

To manage this handling of deleted records, the `fetchPage()` method returns a `Database.CursorFetchResult` object
instead of only the list of results. The `Database.CursorFetchResult` object encapsulates the rows retrieved and information
for the next pagination call.

**•** To retrieve the rows as a list of sObjects, call `CursorFetchResult.getRecords()` .


Apex Developer Guide Using Salesforce Features with Apex

**•** To retrieve the number of deleted rows that the cursor skipped in the `fetchPage()` operation, call
`CursorFetchResult.getDeletedRows()` .

**•** To retrieve the next page of results, first call `CursorFetchResult.getNextIndex()`, and then use the return value as the
_`start`_ parameter in the next `fetchPage()` call.

**•** To determine whether to make subsequent calls to `fetchPage()`, use the `CursorFetchResult.isDone()` method.
The method returns `true` if the specified _`pageSize`_ is reached, which indicates that a full page of results is retrieved. It also
returns `true` if the pagination cursor reaches the end of a result set before the specified _`pageSize`_ is reached, which indicates
that a partial, final page of results is retrieved.

Calling the `PaginationCursor.fetchPage()` and `PaginationCursor.fetchDeleted()` methods count against
the SOQL query limit, and the rows fetched count against the SOQL query row limit.

Apex pagination cursors throw these System exceptions: `System.FatalCursorException` and
`System.TransientCursorException` . Transactions that fail with `System.TransientCursorException` can be
retried.

Cursors and Pagination Cursor Limits

To get limits on Apex cursors and Apex pagination cursors, use these methods in the `Limits` class.

**•** `Limits.getApexCursorRows()` and its upper bound `Limits.getLimitApexCursorRows()` method

**•** `Limits.getFetchCallsOnApexCursor()` and its upper bound
`Limits.getLimitFetchCallsOnApexCursor()` method

**•** `Limits.getApexCursors()` and its upper bound `Limits.getLimitApexCursors()` method

**•** `Limits.getApexPaginationCursors()` and its upper bound `Limits.getLimitApexPaginationCursors()`
method

**•** `Limits.getApexPaginationCursorRows()` and its upper bound
`Limits.getLimitApexPaginationCursorRows()` method

[To view transaction and daily limits for Apex cursors and Apex pagination cursors, see Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

[Apex cursors and pagination cursors have the same expiration limits as API Query cursors. See API Query Cursor Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apicursors.htm)

Apex Cursor and Pagination Cursor Limits Example

```
   // Create a standard cursor

   Database.Cursor cursor = Database.getCursor('SELECT Id, Name FROM Account LIMIT 20');

   System.debug('Standard Cursors: ' + Limits.getApexCursors() + '/' +

   Limits.getLimitApexCursors());

   System.debug('Standard Cursor Rows: ' + Limits.getApexCursorRows() + '/' +

   Limits.getLimitApexCursorRows());

   // Fetch records

   List<Account> batch1 = cursor.fetch(0, 10);

   List<Account> batch2 = cursor.fetch(10, 10);

   // Create a pagination cursor

   Database.PaginationCursor pagCursor = Database.getPaginationCursor('SELECT Id, Name FROM

   Account LIMIT 15');

   System.debug('Pagination Cursors: ' + Limits.getApexPaginationCursors() + '/' +

   Limits.getLimitApexPaginationCursors());

   System.debug('Pagination Cursor Rows: ' + Limits.getApexPaginationCursorRows() + '/' +

```


Apex Developer Guide Using Salesforce Features with Apex

```
   Limits.getLimitApexPaginationCursorRows());

   // Fetch a page

   Database.CursorFetchResult page = pagCursor.fetchPage(0, 5);

   // Check shared fetch call limit

   System.debug('Fetch Calls: ' + Limits.getFetchCallsOnApexCursor() + '/' +

   Limits.getLimitFetchCallsOnApexCursor());

   // Get daily limits map

   Map<String, System.OrgLimit> limitMap = OrgLimits.getMap();

   // Standard cursor daily limit

   System.OrgLimit dailyCursorLimit = limitMap.get('DailyApexCursorLimit');

   System.debug('Daily Cursors: ' + dailyCursorLimit.getValue() + '/' +

   dailyCursorLimit.getLimit());

   // Pagination cursor daily limit

   System.OrgLimit dailyPCursorLimit = limitMap.get('DailyApexPCursorLimit');

   System.debug('Daily Pagination Cursors: ' + dailyPCursorLimit.getValue() + '/' +

   dailyPCursorLimit.getLimit());

   // Shared daily rows limit

   System.OrgLimit dailyRowsLimit = limitMap.get('DailyApexCursorRowsLimit');

   System.debug('Daily Cursor Rows: ' + dailyRowsLimit.getValue() + '/' +

   dailyRowsLimit.getLimit());

```

SEE ALSO:

_[Apex Reference Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Database_Cursor.htm)_ Cursor Class

_Apex Reference Guide:_ [PaginationCursor Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Database_PaginationCursor.htm)

#### Approval Processing

An approval process automates how records are approved in Salesforce. An approval process specifies each step of approval, including
from whom to request approval and what to do at each point of the process.

**•** Use the Apex process classes to create approval requests and process the results of those requests:

**–** [ProcessRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ProcessRequest.htm)

**–** [ProcessResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ProcessResult.htm)

**–** [ProcessSubmitRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ProcessSubmitRequest.htm)

**–** [ProcessWorkItemRequest Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ProcessWorkitemRequest.htm)

**•** Use the `Approval.process` method to submit an approval request and approve or reject existing approval requests. For more
[information, see Approval Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_approval.htm)

Note: The `process` method counts against the DML limits for your organization. See Execution Governors and Limits.

For more information about approval processes, see “Set Up an Approval Process” in the Salesforce online help.

Apex Approval Processing Example


Apex Developer Guide Using Salesforce Features with Apex

##### Apex Approval Processing Example

The following sample code initially submits a record for approval, then approves the request. This example assumes that a pre-existing
approval process on Account exists and is valid for the Account record created.

```
   public class TestApproval {

      void submitAndProcessApprovalRequest() {

        // Insert an account

        Account a = new Account(Name='Test',annualRevenue=100.0);

        insert a;

        User user1 = [SELECT Id FROM User WHERE Alias='SomeStandardUser'];

        // Create an approval request for the account

        Approval.ProcessSubmitRequest req1 =

           new Approval.ProcessSubmitRequest();

        req1.setComments('Submitting request for approval.');

        req1.setObjectId(a.id);

        // Submit on behalf of a specific submitter

        req1.setSubmitterId(user1.Id);

        // Submit the record to the existing process named PTO_Request_Process

        req1.setProcessDefinitionNameOrId('PTO_Request_Process');

        // Skip the criteria evaluation for the specified process

        req1.setSkipEntryCriteria(true);

        // Submit the approval request for the account

        Approval.ProcessResult result = Approval.process(req1);

        // Verify the result

        System.assert(result.isSuccess());

        System.assertEquals(

           'Pending', result.getInstanceStatus(),

           'Instance Status'+result.getInstanceStatus());

        // Approve the submitted request

        // First, get the ID of the newly created item

        List<Id> newWorkItemIds = result.getNewWorkitemIds();

        // Instantiate the new ProcessWorkitemRequest object and populate it

        Approval.ProcessWorkitemRequest req2 =

           new Approval.ProcessWorkitemRequest();

        req2.setComments('Approving request.');

        req2.setAction('Approve');

        req2.setNextApproverIds(new Id[] {UserInfo.getUserId()});

        // Use the ID from the newly created item to specify the item to be worked

        req2.setWorkitemId(newWorkItemIds.get(0));

        // Submit the request for approval

        Approval.ProcessResult result2 = Approval.process(req2);

```


Apex Developer Guide Using Salesforce Features with Apex

```
        // Verify the results

        System.assert(result2.isSuccess(), 'Result Status:'+result2.isSuccess());

        System.assertEquals(

           'Approved', result2.getInstanceStatus(),

           'Instance Status'+result2.getInstanceStatus());

      }

   }

#### Authentication

```

Salesforce provides various ways to authenticate users. Build a combination of authentication methods to fit the needs of your org and
your users’ use patterns.

##### Create a Custom Authentication Provider Plug-in

You can use Apex to create a custom OAuth-based authentication provider plug-in for single sign-on (SSO) to Salesforce.

OAuth 2.0 Token Exchange Handler Examples
Sometimes you want to integrate Salesforce into a complex system where you have a primary app, a central identity provider, and
multiple other apps and microservices. In this model, users log in to the primary app via the identity provider and access data provided
by the other apps and microservices. To fit Salesforce into this model as one of the apps providing data, use the OAuth 2.0 token
exchange flow, which implements an Apex token exchange handler.

##### Create a Custom Authentication Provider Plug-in

You can use Apex to create a custom OAuth-based authentication provider plug-in for single sign-on (SSO) to Salesforce.

Out of the box, Salesforce supports several external authentication providers for single sign-on, including Facebook, Google, LinkedIn,
and service providers that implement the OpenID Connect protocol. By creating a plug-in with Apex, you can add your own OAuth-based
authentication provider. Your users can then use the SSO credentials they already use for non-Salesforce applications with your Salesforce
orgs.

[Before you create your Apex class, you create a custom metadata type record for your authentication provider. For details, see Create a](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)
[Custom External Authentication Provider.](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)

Sample Classes

This example extends the abstract class `Auth.AuthProviderPluginClass` to configure an external authentication provider
called Concur. Build the sample classes and sample test classes in the following order.

**1.** Concur

**2.** ConcurTestStaticVar

**3.** MockHttpResponseGenerator

**4.** ConcurTestClass

Note: The `Auth.AuthProviderPluginClass` class doesn't include a method for single logout. You can easily configure
[single logout in Setup. For steps, see Configure OpenID Connect Single Logout with Salesforce as the Relying Party in](https://help.salesforce.com/s/articleView?id=xcloud.security_auth_slo_oidc_rp_configuring.htm&language=en_US) _Salesforce_
_Help_ . Alternatively, create custom methods for single logout.

```
   global class Concur extends Auth.AuthProviderPluginClass {

```


Apex Developer Guide Using Salesforce Features with Apex

```
            public String redirectUrl; // use this URL for the endpoint that the

   authentication provider calls back to for configuration

            private String key;

            private String secret;

            private String authUrl; // application redirection to the Concur website

    for authentication and authorization

            private String accessTokenUrl; // uri to get the new access token from

   concur using the GET verb

           private String customMetadataTypeApiName; // api name for the custom metadata

    type created for this auth provider

            private String userAPIUrl; // api url to access the user in concur

            private String userAPIVersionUrl; // version of the user api url to access

    data from concur

            global String getCustomMetadataType() {

               return customMetadataTypeApiName;

            }

            global PageReference initiate(Map<string,string> authProviderConfiguration,

    String stateToPropagate) {

               authUrl = authProviderConfiguration.get('Auth_Url__c');

               key = authProviderConfiguration.get('Key__c');

               //Here the developer can build up a request of some sort

               //Ultimately they’ll return a URL where we will redirect the user

               String url = authUrl + '?client_id='+ key

   +'&scope=USER,EXPRPT,LIST&redirect_uri='+ redirectUrl + '&state=' + stateToPropagate;

               return new PageReference(url);

             }

            global Auth.AuthProviderTokenResponse handleCallback(Map<string,string>

   authProviderConfiguration, Auth.AuthProviderCallbackState state ) {

               //Here, the developer will get the callback with actual protocol.

             //Their responsibility is to return a new object called AuthProviderToken

               //This will contain an optional accessToken and refreshToken

               key = authProviderConfiguration.get('Key__c');

               secret = authProviderConfiguration.get('Secret__c');

               accessTokenUrl = authProviderConfiguration.get('Access_Token_Url__c');

               Map<String,String> queryParams = state.queryParameters;

               String code = queryParams.get('code');

               String sfdcState = queryParams.get('state');

               HttpRequest req = new HttpRequest();

               String url = accessTokenUrl+'?code=' + code + '&client_id=' + key +

   '&client_secret=' + secret;

               req.setEndpoint(url);

               req.setHeader('Content-Type','application/xml');

               req.setMethod('GET');

               Http http = new Http();

               HTTPResponse res = http.send(req);

```


Apex Developer Guide Using Salesforce Features with Apex

```
               String responseBody = res.getBody();

               String accessToken = getTokenValueFromResponse(responseBody,

   'AccessToken', null);

               //Parse access token value

               String refreshToken = getTokenValueFromResponse(responseBody,

   'RefreshToken', null);

               //Parse refresh token value

               return new Auth.AuthProviderTokenResponse('Concur', accessToken,

   'refreshToken', sfdcState);

               //don’t hard-code the refresh token value!

             }

              global Auth.UserData getUserInfo(Map<string,string>

   authProviderConfiguration, Auth.AuthProviderTokenResponse response) {

               //Here the developer is responsible for constructing an Auth.UserData

    object

                String token = response.oauthToken;

                HttpRequest req = new HttpRequest();

                userAPIUrl = authProviderConfiguration.get('API_User_Url__c');

                userAPIVersionUrl =

   authProviderConfiguration.get('API_User_Version_Url__c');

                req.setHeader('Authorization', 'OAuth ' + token);

                req.setEndpoint(userAPIUrl);

                req.setHeader('Content-Type','application/xml');

                req.setMethod('GET');

                Http http = new Http();

                HTTPResponse res = http.send(req);

                String responseBody = res.getBody();

                String id = getTokenValueFromResponse(responseBody,

   'LoginId',userAPIVersionUrl);

                String fname = getTokenValueFromResponse(responseBody, 'FirstName',

   userAPIVersionUrl);

                String lname = getTokenValueFromResponse(responseBody, 'LastName',

   userAPIVersionUrl);

                String flname = fname + ' ' + lname;

               String uname = getTokenValueFromResponse(responseBody, 'EmailAddress',

    userAPIVersionUrl);

               String locale = getTokenValueFromResponse(responseBody, 'LocaleName',

    userAPIVersionUrl);

                Map<String,String> provMap = new Map<String,String>();

                provMap.put('what1', 'noidea1');

                provMap.put('what2', 'noidea2');

                return new Auth.UserData(id, fname, lname, flname, uname,

                   'what', locale, null, 'Concur', null, provMap);

             }

             private String getTokenValueFromResponse(String response, String token,

   String ns) {

               Dom.Document docx = new Dom.Document();

               docx.load(response);

               String ret = null;

```


Apex Developer Guide Using Salesforce Features with Apex

```
               dom.XmlNode xroot = docx.getrootelement() ;

               if(xroot != null){

                 ret = xroot.getChildElement(token, ns).getText();

               }

               return ret;

             }

   }

```

Sample Test Classes

The following example contains test classes for the Concur class.

```
   @IsTest

   public class ConcurTestClass {

      private static final String OAUTH_TOKEN = 'testToken';

      private static final String STATE = 'mocktestState';

      private static final String REFRESH_TOKEN = 'refreshToken';

      private static final String LOGIN_ID = 'testLoginId';

      private static final String USERNAME = 'testUsername';

      private static final String FIRST_NAME = 'testFirstName';

      private static final String LAST_NAME = 'testLastName';

      private static final String EMAIL_ADDRESS = 'testEmailAddress';

      private static final String LOCALE_NAME = 'testLocalName';

      private static final String FULL_NAME = FIRST_NAME + ' ' + LAST_NAME;

      private static final String PROVIDER = 'Concur';

      private static final String REDIRECT_URL =

   'http://localhost/services/authcallback/orgId/Concur';

      private static final String KEY = 'testKey';

      private static final String SECRET = 'testSecret';

      private static final String STATE_TO_PROPOGATE = 'testState';

     private static final String ACCESS_TOKEN_URL = 'http://www.dummyhost.com/accessTokenUri';

     private static final String API_USER_VERSION_URL = 'http://www.dummyhost.com/user/20/1';

      private static final String AUTH_URL = 'http://www.dummy.com/authurl';

      private static final String API_USER_URL = 'www.concursolutions.com/user/api';

     // in the real world scenario, the key and value would be read from the (custom fields

    in) custom metadata type record

      private static Map<String,String> setupAuthProviderConfig () {

           Map<String,String> authProviderConfiguration = new Map<String,String>();

          authProviderConfiguration.put('Key__c', KEY);

          authProviderConfiguration.put('Auth_Url__c', AUTH_URL);

          authProviderConfiguration.put('Secret__c', SECRET);

          authProviderConfiguration.put('Access_Token_Url__c', ACCESS_TOKEN_URL);

          authProviderConfiguration.put('API_User_Url__c',API_USER_URL);

          authProviderConfiguration.put('API_User_Version_Url__c',API_USER_VERSION_URL);

          authProviderConfiguration.put('Redirect_Url__c',REDIRECT_URL);

          return authProviderConfiguration;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      static testMethod void testInitiateMethod() {

          String stateToPropogate = 'mocktestState';

          Map<String,String> authProviderConfiguration = setupAuthProviderConfig();

          Concur concurCls = new Concur();

          concurCls.redirectUrl = authProviderConfiguration.get('Redirect_Url__c');

          PageReference expectedUrl = new

   PageReference(authProviderConfiguration.get('Auth_Url__c') + '?client_id='+

                                authProviderConfiguration.get('Key__c')

   +'&scope=USER,EXPRPT,LIST&redirect_uri='+

   authProviderConfiguration.get('Redirect_Url__c') + '&state=' +

                                STATE_TO_PROPOGATE);

          PageReference actualUrl = concurCls.initiate(authProviderConfiguration,

   STATE_TO_PROPOGATE);

          System.assertEquals(expectedUrl.getUrl(), actualUrl.getUrl());

        }

      static testMethod void testHandleCallback() {

          Map<String,String> authProviderConfiguration = setupAuthProviderConfig();

          Concur concurCls = new Concur();

          concurCls.redirectUrl = authProviderConfiguration.get('Redirect_Url_c');

          Test.setMock(HttpCalloutMock.class, new ConcurMockHttpResponseGenerator());

          Map<String,String> queryParams = new Map<String,String>();

          queryParams.put('code','code');

          queryParams.put('state',authProviderConfiguration.get('State_c'));

          Auth.AuthProviderCallbackState cbState = new

   Auth.AuthProviderCallbackState(null,null,queryParams);

          Auth.AuthProviderTokenResponse actualAuthProvResponse =

   concurCls.handleCallback(authProviderConfiguration, cbState);

          Auth.AuthProviderTokenResponse expectedAuthProvResponse = new

   Auth.AuthProviderTokenResponse('Concur', OAUTH_TOKEN, REFRESH_TOKEN, null);

          System.assertEquals(expectedAuthProvResponse.provider,

   actualAuthProvResponse.provider);

          System.assertEquals(expectedAuthProvResponse.oauthToken,

   actualAuthProvResponse.oauthToken);

          System.assertEquals(expectedAuthProvResponse.oauthSecretOrRefreshToken,

   actualAuthProvResponse.oauthSecretOrRefreshToken);

         System.assertEquals(expectedAuthProvResponse.state, actualAuthProvResponse.state);

      }

      static testMethod void testGetUserInfo() {

          Map<String,String> authProviderConfiguration = setupAuthProviderConfig();

          Concur concurCls = new Concur();

```


Apex Developer Guide Using Salesforce Features with Apex

```
          Test.setMock(HttpCalloutMock.class, new ConcurMockHttpResponseGenerator());

          Auth.AuthProviderTokenResponse response = new

   Auth.AuthProviderTokenResponse(PROVIDER, OAUTH_TOKEN,'sampleOauthSecret', STATE);

         Auth.UserData actualUserData = concurCls.getUserInfo(authProviderConfiguration,

    response) ;

          Map<String,String> provMap = new Map<String,String>();

          provMap.put('key1', 'value1');

          provMap.put('key2', 'value2');

          Auth.UserData expectedUserData = new Auth.UserData(LOGIN_ID, FIRST_NAME,

   LAST_NAME, FULL_NAME, EMAIL_ADDRESS,

                   null, LOCALE_NAME, null, PROVIDER, null, provMap);

          System.assertNotEquals(expectedUserData,null);

          System.assertEquals(expectedUserData.firstName, actualUserData.firstName);

          System.assertEquals(expectedUserData.lastName, actualUserData.lastName);

          System.assertEquals(expectedUserData.fullName, actualUserData.fullName);

          System.assertEquals(expectedUserData.email, actualUserData.email);

          System.assertEquals(expectedUserData.username, actualUserData.username);

          System.assertEquals(expectedUserData.locale, actualUserData.locale);

          System.assertEquals(expectedUserData.provider, actualUserData.provider);

         System.assertEquals(expectedUserData.siteLoginUrl, actualUserData.siteLoginUrl);

      }

     // implementing a mock http response generator for concur

     public class ConcurMockHttpResponseGenerator implements HttpCalloutMock {

      public HTTPResponse respond(HTTPRequest req) {

        String namespace = API_USER_VERSION_URL;

        String prefix = 'mockPrefix';

        Dom.Document doc = new Dom.Document();

       Dom.XmlNode xmlNode = doc.createRootElement('mockRootNodeName', namespace, prefix);

        xmlNode.addChildElement('LoginId', namespace, prefix).addTextNode(LOGIN_ID);

        xmlNode.addChildElement('FirstName', namespace, prefix).addTextNode(FIRST_NAME);

        xmlNode.addChildElement('LastName', namespace, prefix).addTextNode(LAST_NAME);

        xmlNode.addChildElement('EmailAddress', namespace,

   prefix).addTextNode(EMAIL_ADDRESS);

        xmlNode.addChildElement('LocaleName', namespace, prefix).addTextNode(LOCALE_NAME);

        xmlNode.addChildElement('AccessToken', null, null).addTextNode(OAUTH_TOKEN);

        xmlNode.addChildElement('RefreshToken', null, null).addTextNode(REFRESH_TOKEN);

        System.debug(doc.toXmlString());

        // Create a fake response

        HttpResponse res = new HttpResponse();

        res.setHeader('Content-Type', 'application/xml');

        res.setBody(doc.toXmlString());

        res.setStatusCode(200);

        return res;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
     }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: AuthProviderPlugin Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_Auth_AuthProviderPlugin.htm)

[Salesforce Help: Create a Custom External Authentication Provider](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)

##### OAuth 2.0 Token Exchange Handler Examples

Sometimes you want to integrate Salesforce into a complex system where you have a primary app,
a central identity provider, and multiple other apps and microservices. In this model, users log in
to the primary app via the identity provider and access data provided by the other apps and
microservices. To fit Salesforce into this model as one of the apps providing data, use the OAuth
2.0 token exchange flow, which implements an Apex token exchange handler.

EDITIONS

Available in: **Enterprise**,
**Unlimited**, **Performance**,
and **Developer** Editions

During the OAuth 2.0 token exchange flow, when a user logs in to the primary app via the identity
provider, the identity provider issues a token to the primary app. The primary app can’t use this
token to directly access Salesforce data, but it can exchange the token for a Salesforce access token. To complete this exchange, the
primary app uses an Apex token exchange handler. With the token exchange handler, Salesforce can issue its own access token by
validating the identity provider’s token and mapping the token’s subject, which identifies the end user, to a Salesforce user.

To build an Apex token exchange handler, create a class that extends the `Auth.Oauth2TokenExchangeHandler` abstract
class and customize its validation logic and subject mapping.

Token Exchange Handler Abstract Class

The `Auth.Oauth2TokenExchangeHandler` abstract class contains two methods. Use the first method,
`validateIncomingToken`, to validate the identity provider’s token. Use the second method, `getUserForTokenSubject`,
to map the token’s subject to a Salesforce user.

```
global abstract class Oauth2TokenExchangeHandler {

   //First method called in the handler

  global virtual Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

 Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

tokenType) {

     //This method must be overridden by the extending class

     //Validate the identity provider’s token. Depending on your use case and token

type, write validation logic that does these things:

     // Use the token to make a callout to the identity provider’s User Info endpoint

     // Use the token to make a callout to identity provider’s Introspection endpoint

     // Validate a SAML response

     // Validate a JWT locally

     // The appDeveloperName is the developer name of the Connected App or External

Client App

     //The IntegratingAppType is an ENUM that is either a Connected App or External

Client App

     // After you validate the token, return true or false

     return null;

   }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      //Second method called in the handler

      global virtual User getUserForTokenSubject(Id networkId, Auth.TokenValidationResult

   result, Boolean canCreateUser, String appDeveloperName, Auth.IntegratingAppType appType)

   {

         //This method must be overridden by the extending class

        //To map the subject of the token to a Salesforce user, write code that does these

    things:

        // Get data directly from the token, and query for the user in Salesforce

        // Get data from the identity provider’s User Info endpoint using the token and

   query for the user in Salesforce

        // Get data from the SAML assertion and query for the user in Salesforce

        // If the user is not in Salesforce, and canCreateUser is true, set up a User

   object

        // This includes external users, so it can include an account and contact

        // If the user Id is null, Salesforce automatically inserts the user(assuming that

    canCreateUser is true)

        return null;

      }

   }

```

The way you build your validation and subject mapping processes depends on your use case, identity provider, and token type. Use
these examples to get started.

Important: These example implementations and code snippets are for demonstration only. Use them as a starting point, but
make sure you evaluate, customize, and test them carefully.

Token Exchange Handler Example Implementation

This example implementation extends the `Auth.Oauth2TokenExchangeHandler` abstract class.

In this example, the `[OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)` enum specifies that the token is a JSON Web Token (JWT). The first method,
`validateIncomingToken`, uses a method in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm#apex_Auth_JWTUtil_methods)` class to validate the token by calling an endpoint on the
external identity provider.

Validating the token returns an instance of the `[Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)` class with information about the token and the
user.

With the second method, `getUserForTokenSubject`, the handler gets information about the user from the token validation
result. The example shows two ways to bundle the user data—either by creating a class with a custom data structure or by using the
`[Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)` class.

After the handler gets the user data from the token, it looks for a Salesforce user matching the token subject. In this example, the handler
doesn’t find a user, so it creates a User object. To finish creating the user, Salesforce automatically inserts the User object for you.

```
   /*Token Exchange Handler Implementation Example*/

   public class MyTokenExchangeClass extends Auth.Oauth2TokenExchangeHandler{

     public override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

    Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType) {

        //Depending on your incoming token, you validate it in different ways

        //If the incoming token is an opaque access token or refresh token, validate it

   with a callout to the identity provider

        //If it’s a SAML assertion, validate it by checking the XML

```


Apex Developer Guide Using Salesforce Features with Apex

```
        //If it’s an ID Token or JWT, try using our JWT validation methods

        //This example assumes that the incoming token is a JWT and that there is a public

    keys endpoint on the identity provider

        //Be very careful with any logic in this method, and test carefully before using

        Boolean isValid = false;

        Auth.JWT jwt;

        //Custom data structure

        CustomStructuredUserData customData;

        //Standard user data structure

        Auth.UserData userData;

        if (tokenType == Auth.OAuth2TokenExchangeType.JWT || tokenType ==

   Auth.OAuth2TokenExchangeType.ID_TOKEN) {

           try {

             jwt = Auth.JWTUtil.validateJWTWithKeysEndpoint(incomingToken,

   'https://your-idp.com/keys', true);

             isValid = true;

             //These values are sourced from the JWT or ID Token

             userData = new Auth.UserData('identifier', 'firstName', 'lastName',

   'fullName', 'customer@email.com', 'link url', 'remote username', 'local', 'Provider (IDP

   Name)', '', new Map<String,String>());

             //You can also pass data as generic object

             customData = new CustomStructuredUserData();

           } catch (Exception e) {

             isValid = false;

           }

        } else if (tokenType == Auth.OAuth2TokenExchangeType.ACCESS_TOKEN || tokenType ==

    Auth.OAuth2TokenExchangeType.REFRESH_TOKEN) {

           //Putlogic for validating an opaque access token or refresh token here

          //This validation typically involves a callout to the introspect or user info

    endpoints

           //If you call out to the user info endpoint, make sure to pass the data from

   the validation into the getUserForTokenSubject method using an Apex class or the user data

    class

           isValid = false;

        } else if (tokenType == Auth.OAuth2TokenExchangeType.SAML_2) {

           //Put logic for validating a SAML assertion here

           //This validation involves XML parsing

           isValid = false;

        } else {

           //You can add new token types. If you don’t know how to validate the token,

   always check the type and return false

           isValid = false;

        }

        if(isValid){

           return new Auth.TokenValidationResult(true, (object)customData, userData,

   incomingToken, tokenType, 'CustomErrorMessage');

        } else {

           return new Auth.TokenValidationResult(isValid);

        }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      public override User getUserForTokenSubject(Id networkId, Auth.TokenValidationResult

   result, Boolean canCreateUser, String appDeveloperName, Auth.IntegratingAppType appType)

   {

        //If you passed data from the validation method, grab it now. Remember to cast

   back for the custom data

        CustomStructuredUserData customData = (CustomStructuredUserData)result.data;

        Auth.UserData userData = result.userData;

        //If you don’t have any data from the token, you can perform a callout using the

   incoming token

        String userToken = result.token;

        //Now, search for a user

        User u;

        try {

           u = [SELECT Id, IsActive FROM User WHERE email =: userData.email];

        } catch (Exception e) {

           //No user existed for this email address, or there were too many. Try looking

    harder

        }

        // If you didn’t find a user, check to see if you can create one

        if (canCreateUser && (u == null)) {

           u = new User();

           u.firstName = userData.firstName;

           u.lastName = userData.lastName;

          //Finish setting user attributes. For external users, make sure you set up the

    contact/account/person account

           //If you assign permission sets, do it in a future method to avoid mixed DML

           //Returning the user from this method handles the insertion, so it’s not

   necessary to manually insert

        }

        return u;

      }

      //This class gives you a way to pass structured data between the validateIncomingToken

    and getUserForTokenSubject methods

      //This example is for demonstration only. Implement this class in a way that matches

   the data that you are passing

      private class CustomStructuredUserData {

        public String customAttribute1;

        public Integer customAttribute2;

        public Map<String,Object> customAttribute3;

      }

   }

```

Examples for Validating Different Token Types

The custom logic for your implementation of the `validateIncomingToken` method depends on the token type. Here’s an
overview of the options for different token types.


Apex Developer Guide Using Salesforce Features with Apex

**•** For JWTs and ID tokens, use methods in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)` class.

**•** For opaque tokens, such as opaque access and refresh tokens, call out to the identity provider’s introspection or user info endpoints.

**•** For SAML assertions, write code to parse the XML from the assertion.

In this example, the handler validates a JWT from the identity provider. The handler determines the token type and uses the
`validateJWTWithKey` method in the `Auth.JWTUtil` class to validate the JWT with a public key.

```
   global override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

    Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType) {

        if (tokenType == Auth.OAuth2TokenExchangeType.JWT) {

          // Validates the JWT with a public key, but we also provide methods to validate

    it with a certificate (Auth.JWTUtil.validateJWTWithCert) or with a keys endpoint

   (Auth.JWTUtil.validateJWTWithKeysEndpoint)

          Auth.JWT jwt =

   Auth.JWTUtil.validateJWTWithKey(incomingToken,'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMI...');

          return new Auth.TokenValidationResult(true);

        }

        return new Auth.TokenValidationResult(false); // Returns a general 'Token handler

    validation failed' message that you can customize

   }

```

For opaque access tokens, which can’t be introspected locally on your app, call out to the introspection or user info endpoints on the
external identity provider. In this example for validating an opaque token, the handler sends a POST request to the identity provider’s
introspection endpoint and parses the identity provider’s JSON response so that Salesforce can understand it. It then validates the
response using the `validateIncomingToken` method.

```
   global override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

    Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType) {

        if (tokenType == Auth.OAuth2TokenExchangeType.ACCESS_TOKEN) {

          // Validate the token with a callout to the introspection endpoint

          String body =

   'client_id=3MVG9AOp4kbriZ...&client_secret=71E147927AC...&token=00Dxx0000006H5T!AQEA...';

          HttpRequest req = new HttpRequest();

          req.setMethod('POST');

          req.setEndpoint('https://<MyCompanyDomain>/services/oauth2/introspect');

          req.setHeader('Content-Type', 'application/x-www-form-urlencoded');

          req.setBody(body);

          Http http = new Http();

          HttpResponse res = http.send(req);

          Boolean active;

          String username;

          Auth.UserData userData;

          if(res.getStatusCode() == 200) {

             System.JSONParser parser = System.JSON.createParser(res.getBody());

             try {

               while((active == null || username == null) && parser.nextToken() !=

   null) {

                  if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

                    String fieldName = parser.getText();

```


Apex Developer Guide Using Salesforce Features with Apex

```
                    if (fieldName == 'active') {

                       parser.nextToken();

                       active = parser.getBooleanValue();

                       if (!active) {

                        return new Auth.TokenValidationResult(false);

                       }

                    }

                    if (fieldName == 'username') {

                       parser.nextToken();

                       username = parser.getText();

                    }

                  }

               }

             if (active != null && username != null) {

               userData = new Auth.UserData(null, null, null, null, null, null,

   username, null, null, null, null);

             }

             } catch(JSONException e) {

               return new Auth.TokenValidationResult(false); // Returns a general

   'Token handler validation failed' message that you can customize

             }

          } else {

             return new Auth.TokenValidationResult(false); // Returns a general 'Token

    handler validation failed' message that you can customize

          }

          return new Auth.TokenValidationResult(true, null, userData, incomingToken,

   tokenType, null);

        }

        return new Auth.TokenValidationResult(false); // Returns a general 'Token handler

    validation failed' message that you can customize

      }

```

Example for Finding and Creating a User

During subject mapping, your handler finds the subject (end user) of the incoming token and tries to link it to a Salesforce user. Optionally,
you can configure your handler to help create a Salesforce user if it can’t find one. The handler doesn’t technically create the user—instead,
it returns a User object. Salesforce then automatically inserts the new user into the User object for you. To create the User object, the
`isUserCreationAllowed` field on your `[OauthTokenExchangeHandler](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_oauthtokenexchangehandler.htm)` metadata definition must be set to `true` . When
you set this metadata field to `true`, the `CanCreateUser` parameter in the `getUserForTokenSubject` Apex method is
also set to `true` .

If necessary, to get more information about the incoming subject, the handler can call out to the external identity provider or another
external system.


Apex Developer Guide Using Salesforce Features with Apex

In this example implementation, the handler gets information about the user from the identity provider’s token and looks for an existing
Salesforce user. If no user exists, it creates a User object.

```
   global class MyTokenExchangeHandler extends Auth.Oauth2TokenExchangeHandler {

     global override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

    Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType) {

        // Validates the incoming token

        Auth.UserData userData = new Auth.UserData('someIdentifier', 'someFirstName',

   'someLastName', 'someFullName', 'someEmail', 'someLink', 'someUsername@my.org', 'en_US',

   'someProvider', 'someSiteLoginUrl', null);

       return new Auth.TokenValidationResult(true, null, userData, incomingToken, tokenType,

    null);

      }

     global override User getUserForTokenSubject(Id networkId, Auth.TokenValidationResult

   result, Boolean canCreateUser, String appDeveloperName, Auth.IntegratingAppType appType)

   {

        String username = result.getUserData().username;

        List<User> existingUser = [SELECT Id, Username, Email, FirstName, LastName, Alias,

    ProfileId FROM User WHERE Username=:username LIMIT 1];

        if (!existingUser.isEmpty()) {

           return existingUser[0];

        }

        User u = new User();

        u.Username = username;

        u.Email = 'some@email.com';

        u.LastName = 'SomeLastName';

        u.Alias = 'MyAlias';

        u.TimeZoneSidKey = 'America/Los_Angeles';

        u.LocaleSidKey = 'en_US';

        u.EmailEncodingKey = 'UTF-8';

        Profile p = [SELECT Id FROM profile WHERE name='Standard User'];

        u.ProfileId = p.Id;

        u.LanguageLocaleKey = 'en_US';

        return u;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

   }

```

SEE ALSO:

_Salesforce Help:_ [OAuth 2.0 Token Exchange Flow](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_token_exchange_overview.htm&type=5&language=en_US)

_Apex Reference Guide:_ [Oauth2TokenExchangeHandler Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm)

_Apex Reference Guide:_ [TokenValidationResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

_Apex Reference Guide:_ [OAuth2TokenExchangeType Enum](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

_Apex Reference Guide:_ [IntegratingAppType Enum](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

_[Apex Reference Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)_ JWTUtil Class

#### Chatter Answers and Ideas

In Chatter Answers and Ideas, use zones to organize ideas and answers into groups. Each zone can have its own focus, with unique ideas
and answers topics to match that focus.

To work with zones in Apex, use the `Answers`, `Ideas`, and `ConnectApi.Zones` classes.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_answers.htm)_ : Answers Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_ideas.htm)_ : Ideas Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Zones_static_methods.htm)_ : Zones Class

#### Use Cases for the CommercePayments Namespace

Review walkthroughs, use cases, and reference material for the `CommercePayments` platform.

To review `CommercePayments` [class reference docs, go to CommercePayments Namespace.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)

Payment Gateway Adapters
Payment gateway adapters represent the bridge between your payments platform in Salesforce and an external payment gateway.

Payment Authorization Reversal Service
An authorization reversal is a transaction that negates an authorization by releasing the hold on funds in a customer’s payment
method.

Tokenization Service
The credit card tokenization process replaces sensitive customer information with a one-time algorithmically generated number,
called a token, used during the payment transaction. Salesforce stores the token and then uses that token as a representation of the
credit card used for transactions. The token lets you store information about the credit card without storing sensitive customer data,
such as credit card numbers, in Salesforce.

Alternative Payment Methods
An alternative payment method allows customers to store and represent payment method information not represented by another
pre-defined payment method such as `CardPaymentMethod` or `DigitalWallet` . Common examples of alternative payment
methods include CashOnDeliver, Klarna, and Direct Debit. Alternative payment methods are available in API v51.0 and later.

Process Payments
Process a payment in the payment gateway.


Apex Developer Guide Using Salesforce Features with Apex

Process Refund
Process a refund in the payment gateway.

Idempotency Guidelines
Idempotency represents the ability of a payment gateway to recognize duplicate requests submitted either in error or maliciously,
and then process the duplicate requests accordingly. When working with an idempotent gateway, consider these important
guidelines.

Sample Payment Gateway Implementation for CommercePayments
We’ve created a GitHub repository containing code samples for a sample Payeezy payment gateway implementation with the
CommercePayments namespace. Review the sample code if you need help with configuring your payment gateway implementation.

##### Payment Gateway Adapters

Payment gateway adapters represent the bridge between your payments platform in Salesforce and an external payment gateway.

###### Building a Synchronous Gateway Adapter

In synchronous payment configurations, the Salesforce payment platform sends transaction information to the gateway, and then
waits for a gateway response that contains the final transaction status. Salesforce creates a transaction only if the transaction is
successful in the gateway.

Set Up a Synchronous Payment Gateway Adapter
For payments transactions, you can configure Salesforce to interface with a synchronous payment gateway adapter.

Building an Asynchronous Gateway Adapter
In an asynchronous payments configuration, the payments platform first sends transaction information to the gateway. The gateway
responds with an acknowledgment that it received the transaction, and then the platform creates a pending transaction. The gateway
sends a notification, which contains the final transaction status. The platform then updates the transaction’s status accordingly.

Set Up an Asynchronous Payment Gateway Adapter
For payments transactions, you can configure Salesforce to interface with an asynchronous payment gateway adapter.

Builder Examples for Payment Gateway Adapters
The final sections of a payment gateway adapter should define how the adapter creates requests and responses. The implementation
of these classes can vary widely based on your gateway and platform requirements. We’ve provided several generics examples for
review.

###### Building a Synchronous Gateway Adapter

In synchronous payment configurations, the Salesforce payment platform sends transaction information to the gateway, and then waits
for a gateway response that contains the final transaction status. Salesforce creates a transaction only if the transaction is successful in
the gateway.

A synchronous gateway adapter implements the `[PaymentGatewayAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAdapter.htm#apex_interface_commerce_payments_PaymentGatewayAdapter)` . In this topic, we examine a sample
synchronous adapter by looking at `PaymentGatewayAdapter`, and then the `processRequest` method, which drives most
of the communication between the payment platform and the payment gateway.

Note: Payment gateway adapters can’t make future calls, external callouts using `System.Http`, asynchronous calls, queueable
calls, or execute DMLs using SOQL.


Apex Developer Guide Using Salesforce Features with Apex

PaymentGatewayAdapter

All synchronous gateways must implement the `PaymentGatewayAdapter` interface. All PaymentGatewayAdapters are required
to implement the `processRequest` method.

```
   global with sharing class SampleAdapter implements commercepayments.PaymentGatewayAdapter

    {

      global SampleAdapter() {}

      global commercepayments.GatewayResponse

   processRequest(commercepayments.paymentGatewayContext gatewayContext) {

      }

   }

```

Processing an Initial Payment Request

When the payments platform receives a payments API request, it passes the request to your gateway adapter for further evaluation. The
adapter begins the request evaluation process by calling the `processRequest` method, which represents the first step in a
synchronous payment flow. We can break the `processRequest` implementation into three parts.

First, it builds a payment request object that the gateway can understand.

```
   commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

   if (requestType == commercepayments.RequestType.Capture) {

     req.setEndpoint('/pal/servlet/Payment/v52/capture');

      body =

   buildCaptureRequest((commercepayments.CaptureRequest)gatewayContext.getPaymentRequest());

   } else if (requestType == commercepayments.RequestType.ReferencedRefund) {

      req.setEndpoint('/pal/servlet/Payment/v52/refund');

      body =

   buildRefundRequest((commercepayments.ReferencedRefundRequest)gatewayContext.getPaymentRequest());

   }

```

Note: We don't recommend encoding the request body, which contains the merge fields, including the card number and CVV.
This can cause the request to fail to read the encoded request body and to fail to replace the merge field values.

Then, the adapter sends the request to the payment gateway.

```
   req.setBody(body);

   req.setMethod('POST');

   commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

   HttpResponse res = null;

   try {

      res = http.send(req);

   } catch(CalloutException ce) {

      commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('500', ce.getMessage());

      return error;

   }

```

Finally, the adapter creates a response object to store data from the gateway’s response. The type of response object varies based on
whether you originally made a payment capture request or a refund request.

```
   if ( requestType == commercepayments.RequestType.Capture) {

     // Refer to the end of this doc for sample createCaptureResponse implementation

      response = createCaptureResponse(res);

```


Apex Developer Guide Using Salesforce Features with Apex

```
   } else if ( requestType == commercepayments.RequestType.ReferencedRefund) {

      response = createRefundResponse(res);

   }

   return response;

```

Using Custom Data

[To transfer additional, custom data from the frontend to your payment gateway adapter, use the Checkout Payments Connect API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
Sending custom data to the adapter supports use cases like implementing conditional logic based on specific data or mapping
asynchronous webhook events to a cart by passing an identifier.

To send custom data to your payment gateway adapter, use the `paymentsData` [parameter in the Checkout Payments Connect API](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
input payload. This parameter is a serialized map of type `<String, String>` that supports up to four key-value pairs. Each key
and each value can contain up to 255 characters. `paymentsData` is only applicable to Auth and PostAuth payment requests. Simple
purchase orders don’t support `paymentsData` .

[Similarly, the Post Authorization input payload has an](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_payment_post_auth.htm) `additionalData` property, which is also a map of type `<String, String>` .
The `paymentsData` property is accepted for Auth and PostAuth requests and is transferred to the Payment APIs through the
`additionalData` property.

###### Set Up a Synchronous Payment Gateway Adapter

For payments transactions, you can configure Salesforce to interface with a synchronous payment
gateway adapter.

To access the `commercepayments` API, you need the PaymentPlatform org permission.

**1.** Create your payment gateway adapter Apex classes. For instructions, see Building a Synchronous
Gateway Adapter.

**2.** Create a named credential.

**a.** From Setup, in the Quick Find box, enter _`Named Credentials`_, and then select **New.** .

**b.** Complete the required fields, including the URL for your payment gateway.

EDITIONS

Available in: Salesforce
Summer ’20 and later

Available in: API 49.0 and
later

**3.** Create a payment gateway provider. The PaymentGatewayProvider object stores details about the payment gateway that Salesforce
Payments communicates with when processing a transaction.

**a.** [Generate an access token according to the instructions in Connect to Connect REST API Using OAuth.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/quickstart_connecting.htm)

The response includes the access token, specified in the `access_token` property, and the server instance, specified in the
`instance_url` property. Use this information to make API calls to build the payment gateway provider.

**b.** Execute a POST call to the resource using the domain in the `instance_url` . For example,
`https://` _**`instance_name`**_ `.my.salesforce.com/services/data/v` _**`api_version`**_ `/tooling/sobjects/PaymentGatewayProvider` .

Use this payload as the request body, replacing _`value`_ with the correct data.

```
    {

        "ApexAdapterId": " value ",

        "DeveloperName": " value ",

        "MasterLabel": " value ",

        "IdempotencySupported": " value ",

        "Comments": " value "

        }

        Example:

```


Apex Developer Guide Using Salesforce Features with Apex

```
           {

           "ApexAdapterId": "01pxx0000004UU8AAM",

           "DeveloperName": "MyNewGatewayProvider",

           "MasterLabel": "My New Gateway Provider",

           "IdempotencySupported": "Yes",

           "Comments": "Custom made gateway provider."

           }

```

**4.** Create a payment gateway record. The PaymentGateway object stores information about the connection to the external payment
gateway. The record requires these field values.

**•** Payment Gateway Name: Name of the external payment gateway.

**•** Merchant Credential ID: ID of the named credential that you created.

**•** Payment Gateway Provider ID: ID of the payment gateway provider that you created.

**•** Status: Active

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_paymentgateway.htm)_ : PaymentGateway

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewayprovider.htm)_ : PaymentGatewayProvider

###### Building an Asynchronous Gateway Adapter

In an asynchronous payments configuration, the payments platform first sends transaction information to the gateway. The gateway
responds with an acknowledgment that it received the transaction, and then the platform creates a pending transaction. The gateway
sends a notification, which contains the final transaction status. The platform then updates the transaction’s status accordingly.

The asynchronous process differs from synchronous transactions, where the platform does not create a pending transaction after the
initial gateway request. Instead, the platform creates a transaction only after the gateway sends a response containing the final transaction
status. For information on building a synchronous adapter, review Building a Synchronous Gateway Adapter.

An asynchronous configuration requires both a synchronous gateway adapter and an asynchronous adapter. In this topic, we’ll break
down a sample asynchronous adapter by looking at several important areas.

**•** Defining an asynchronous payment gateway adapter

**•** Processing the initial payment request

**•** Processing a notification from the payment gateway

**•** Debugging gateway responses using system debug logs.

Note: Payment gateway adapters can’t make future calls, external callouts using `System.Http`, asynchronous calls, queueable
calls, or execute DMLs using SOQL.

Asynchronous Payment Gateway Adapter Definition

An asynchronous gateway adapter class must implement both the `[PaymentGatewayAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAdapter.htm#apex_interface_commerce_payments_PaymentGatewayAdapter)` and the
`[PaymentGatewayAsyncAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAsyncAdapter.htm#apex_interface_commercepayments_PaymentGatewayAsyncAdapter)` . The adapter class must also implement the `processRequest` method for
PaymentGatewayAdapter and the `processNotification` method for PaymentGatewayAsyncAdapter.

```
   global with sharing class SampleAdapter implements

   commercepayments.PaymentGatewayAsyncAdapter, commercepayments.PaymentGatewayAdapter {

      global SampleAdapter() {}

```


Apex Developer Guide Using Salesforce Features with Apex

```
      global commercepayments.GatewayResponse

   processRequest(commercepayments.paymentGatewayContext gatewayContext) {

      }

      global commercepayments.GatewayNotificationResponse

   processNotification(commercepayments.PaymentGatewayNotificationContext

   gatewayNotificationContext) {

      }

   }

```

Processing an Initial Payment Request

When the payments platform receives a payments API request, it passes the request to your gateway adapter for further evaluation. The
adapter begins the request evaluation process by calling the **processRequest** method, which represents the first step in an asynchronous
payment flow. We can break the processRequest implementation into three parts.

First, it builds a payment request object that the gateway can understand.

```
   commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

   if (requestType == commercepayments.RequestType.Capture) {

     req.setEndpoint('/pal/servlet/Payment/v52/capture');

      body =

   buildCaptureRequest((commercepayments.CaptureRequest)gatewayContext.getPaymentRequest());

   } else if (requestType == commercepayments.RequestType.ReferencedRefund) {

      req.setEndpoint('/pal/servlet/Payment/v52/refund');

      body =

   buildRefundRequest((commercepayments.ReferencedRefundRequest)gatewayContext.getPaymentRequest());

   }

```

Then, the adapter sends the request to the payment gateway.

```
   req.setBody(body);

   req.setMethod('POST');

   commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

   HttpResponse res = null;

   try {

      res = http.send(req);

   } catch(CalloutException ce) {

      commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('500', ce.getMessage());

      return error;

   }

```

Finally, the adapter creates a response object to store data from the gateway’s response. The type of response object will vary based on
whether you originally made a payment capture request or a refund request.

```
   if ( requestType == commercepayments.RequestType.Capture) {

     // Refer to the end of this doc for sample createCaptureResponse implementation

      response = createCaptureResponse(res);

   } else if ( requestType == commercepayments.RequestType.ReferencedRefund) {

      response = createRefundResponse(res);

   }

   return response;

```


Apex Developer Guide Using Salesforce Features with Apex

Processing a Notification from the Payment Gateway

After the customer bank processes the transaction and sends the results to the gateway, the gateway sends the adapter a notification
indicating that it’s ready to provide the final transaction status. For this part of an asynchronous transaction flow, the adapter needs to
call the processNotification class. We can split the processNotification implementation into four parts.

[First, the adapter verifies the signature in the notification request. For more information on verifying signatures, review Encryption and](https://developer.salesforce.com/blogs/2023/12/encryption-and-signature-techniques-in-apex)
[Signature Techniques in Apex.](https://developer.salesforce.com/blogs/2023/12/encryption-and-signature-techniques-in-apex)

```
   private Boolean verifySignature(NotificationRequest requestItem) {

      String payload = requestItem.pspReference + ':'

        + (requestItem.originalReference == null ? '' : requestItem.originalReference) +

   ':'

        + requestItem.merchantAccountCode + ':'

        + requestItem.merchantReference + ':'

        + requestItem.amount.value.intValue() + ':'

        + requestItem.amount.currencyCode + ':'

        + requestItem.eventCode + ':'

        + requestItem.success;

      String myHMacKey = getHMacKey();

      String generatedSign = EncodingUtil.base64Encode(Crypto.generateMac('hmacSHA256',

   Blob.valueOf(payload),

                       EncodingUtil.convertFromHex(myHMacKey)));

      return generatedSign.equals(requestItem.additionalData.hmacSignature);

   }

```

Next, the adapter parses the gateway’s notification request and builds a notification object. The
`getPaymentGatewayNotificationRequest` method evaluates data from the gateway’s notification request items, which
include status, referenceNumber, event, and amount. The `notificationStatus` object is set to Success or Failed based on
whether the platform successfully received the notification. If the notification’s event code indicates that the gateway processed a
payment capture transaction, the adapter builds a notification object using the `CaptureNotification` class. If the event code
indicates that the gateway processed a refund transaction, the adapter builds a notification object using the
`ReferencedRefundNotification` class.

```
   commercepayments.PaymentGatewayNotificationRequest gatewayNotificationRequest =

   gatewayNotificationContext.getPaymentGatewayNotificationRequest();

   Blob request = gatewayNotificationRequest.getRequestBody();

   SampleNotificationRequest notificationRequest =

   SampleNotificationRequest.parse(request.toString().replace('currency', 'currencyCode'));

   List<SampleNotificationRequest.NotificationItems> notificationItems =

   notificationRequest.notificationItems;

   SampleNotificationRequest.NotificationRequestItem notificationRequestItem =

   notificationItems[0].NotificationRequestItem;

   Boolean success = Boolean.valueOf(notificationRequestItem.success);

   String pspReference = notificationRequestItem.pspReference;

   String eventCode = notificationRequestItem.eventCode;

   Double amount = notificationRequestItem.amount.value;

   commercepayments.NotificationStatus notificationStatus = null;

   if (success) {

      notificationStatus = commercepayments.NotificationStatus.Success;

   } else {

      notificationStatus = commercepayments.NotificationStatus.Failed;

```


Apex Developer Guide Using Salesforce Features with Apex

```
   }

   commercepayments.BaseNotification notification = null;

   if ('CAPTURE'.equals(eventCode)) {

      notification = new commercepayments.CaptureNotification();

   } else if ('REFUND'.equals(eventCode)) {

      notification = new commercepayments.ReferencedRefundNotification();

   }

   notification.setStatus(notificationStatus);

   notification.setGatewayReferenceNumber(pspReference);

   notification.setAmount(amount);

```

The adapter then requests that the payments platform records the results of the notification.

```
   commercepayments.NotificationSaveResult saveResult =

   commercepayments.NotificationClient.record(notification);

```

All asynchronous gateways require that the platform acknowledges that it received the notification, regardless of whether the platform
successfully saved the notification’s data. The platform calls the `GatewayNotificationResponse` class to send the
acknowledgment.

```
   commercepayments.GatewayNotificationResponse gnr = new

   commercepayments.GatewayNotificationResponse();

   if (saveResult.isSuccess()) {

      system.debug('Notification accepted by platform');

   } else {

      system.debug('Errors in the result '+ Blob.valueOf(saveResult.getErrorMessage()));

   }

   gnr.setStatusCode(200);

   gnr.setResponseBody(Blob.valueOf('[accepted]'));

   return gnr;

```

Using Custom Data

[To transfer additional, custom data from the frontend to your payment gateway adapter, use the Checkout Payments Connect API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
Sending custom data to the adapter supports use cases like implementing conditional logic based on specific data or mapping
asynchronous webhook events to a cart by passing an identifier.

To send custom data to your payment gateway adapter, use the `paymentsData` [parameter in the Checkout Payments Connect API](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
input payload. This parameter is a serialized map of type `<String, String>` that supports up to four key-value pairs. Each key
and each value can contain up to 255 characters. `paymentsData` is only applicable to Auth and PostAuth payment requests. Simple
purchase orders don’t support `paymentsData` .

[Similarly, the Post Authorization input payload has an](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_payment_post_auth.htm) `additionalData` property, which is also a map of type `<String, String>` .
The `paymentsData` property is accepted for Auth and PostAuth requests and is transferred to the Payment APIs through the
`additionalData` property.

Debugging

Usually, Apex debug logs are available in the developer console. However, Salesforce doesn’t store debug logs from the
`processNotification` method in the developer console. To view this part of the method flow using system.debug, review the
[Collect Debug Logs for Guest Users section of Set Up Debug Logging.](https://help.salesforce.com/articleView?id=code_add_users_debug_log.htm&type=5&language=en_US)


Apex Developer Guide Using Salesforce Features with Apex

###### Set Up an Asynchronous Payment Gateway Adapter

For payments transactions, you can configure Salesforce to interface with an asynchronous payment
gateway adapter.

To access the `commercepayments` API, you need the PaymentPlatform org permission.

**1.** Create a Salesforce site. From Setup, in the Quick Find box, enter _`Sites`_ . Under Sites and
Domains, select **Sites** [see Set Up Salesforce Sites.](https://help.salesforce.com/s/articleView?language=en_US&id=sf.sites_setup_overview.htm)

Set the site’s public access settings to **Guest Access to the Payments API** .

EDITIONS

Available in: Salesforce
Summer ’20 and later

Available in: API 49.0 and
later

**2.** Create your payment gateway adapter Apex classes. Asynchronous payment gateways require
that you implement an asynchronous and a synchronous adapter. For information about building gateway adapters in Apex, see
Building an Asynchronous Gateway Adapter and Building a Synchronous Gateway Adapter.

**3.** Create a named credential in the UI.

**a.** From Setup, in the Quick Find box, enter _`Named Credentials`_, and then select **New** .

**b.** Complete the required fields. For the URL, enter the URL of your payment gateway.

**4.** Create a payment gateway provider. The PaymentGatewayProvider object stores details about the payment gateway that Salesforce
Payments communicates with when processing a transaction.

**a.** [Generate an access token according to the instructions in Connect to Connect REST API Using OAuth.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/quickstart_connecting.htm)

The response includes the access token, specified in the `access_token` property, and the server instance, specified in the
`instance_url` property. Use this information to make API calls to build the payment gateway provider.

**b.** Execute a POST call to the resource using the domain in the `instance_url` . For example,
`https://` _**`instance_name`**_ `.my.salesforce.com/services/data/v` _**`api_version`**_ `/tooling/sobjects/PaymentGatewayProvider` .

Use this payload as the request body, replacing _`value`_ with the correct data.

```
    {

     "ApexAdapterId": " value ",

     "DeveloperName": " value ",

     "MasterLabel": " value ",

     "IdempotencySupported": " value ",

     "Comments": " value "

    }

    Example:

    {

     "ApexAdapterId": "01pxx0000004UU8AAM",

     "DeveloperName": "MyNewGatewayProvider",

     "MasterLabel": "My New Gateway Provider",

     "IdempotencySupported": "Yes",

     "Comments": "Custom made gateway provider."

    }

```

**5.** Create a payment gateway record. The PaymentGateway object stores information about the connection to an external payment
gateway. The record requires these field values.

**•** Payment Gateway Name: Name of the external payment gateway.

**•** Merchant Credential ID: ID of the named credential that you created.

**•** Payment Gateway Provider ID: ID of the payment gateway provider that you created.

**•** Status: Active


Apex Developer Guide Using Salesforce Features with Apex

**6.** Create a webhook by providing a URL in the standard notification transport settings of your external payment gateway. The external
payment gateway uses the webhook to send notifications, as HTTP POST messages, to your asynchronous payment gateway adapter.

The webhook is a combination of your site endpoint with the ID of the payment gateway provider.

**a.** Use the following URL for your site’s endpoint, replacing `domain` with your site's domain and URL. For example:

```
      https:// MyDomainName .my.salesforce-sites.com/solutions/services/data/v58.0/commerce/payments/notify

```

Note: If you’re not using enhanced domains, your org’s Salesforce Sites URL is different. For details, see My Domain URL
Formats in Salesforce Help.

**b.** Find the ID of your payment gateway provider, and append the `?provider=ID` query parameter to the endpoint. For
example,

```
      https:// MyDomainName .my.salesforce-sites.com/solutions/services/data/v58.0/commerce/payments/notify?provider=0cJR00000004CEhMAM

```

**c.** Enter the webhook in your external payment gateway’s standard notification settings.

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewayprovider.htm)_ : PaymentGatewayProvider

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_paymentgateway.htm)_ : PaymentGateway

###### Builder Examples for Payment Gateway Adapters

The final sections of a payment gateway adapter should define how the adapter creates requests and responses. The implementation
of these classes can vary widely based on your gateway and platform requirements. We’ve provided several generics examples for review.

Example:

**buildCaptureRequest**

```
       private String buildCaptureRequest(commercepayments.CaptureRequest captureRequest)

        {

         Boolean IS_MULTICURRENCY_ORG = UserInfo.isMultiCurrencyOrganization();

          QueryUtils qBuilderForAuth = new QueryUtils(PaymentAuthorization.SObjectType);

          qBuilderForAuth.getSelectClause().addField('GatewayRefNumber', false);

          qBuilderForAuth.setWhereClause(' WHERE Id =' + '\'' +

       captureRequest.paymentAuthorizationId + '\'');

          PaymentAuthorization authObject =

       (PaymentAuthorization)Database.query(qBuilderForAuth.buildSOQL())[0];

          JSONGenerator jsonGeneratorInstance = JSON.createGenerator(true);

          jsonGeneratorInstance.writeStartObject();

          jsonGeneratorInstance.writeStringField('merchantAccount',

       '{!$Credential.Username}');

          jsonGeneratorInstance.writeStringField('originalReference',

       authObject.GatewayRefNumber);

          jsonGeneratorInstance.writeFieldName('modificationAmount');

          jsonGeneratorInstance.writeStartObject();

          jsonGeneratorInstance.writeStringField('value',

       String.ValueOf((captureRequest.amount * 100.0).intValue()));

          jsonGeneratorInstance.writeEndObject();

          jsonGeneratorInstance.writeEndObject();

```


Apex Developer Guide Using Salesforce Features with Apex

```
          return jsonGeneratorInstance.getAsString();

       }

```

Example:

**createCaptureResponse**

```
       private commercepayments.GatewayResponse createCaptureResponse(HttpResponse response)

        {

          Map<String, Object> mapOfResponseValues = (Map

                    <String, Object>) JSON.deserializeUntyped(response.getBody());

          Integer statusCode = response.getStatusCode();

          String responceValue = (String)mapOfResponseValues.get('response');

          if(statusCode == 200) {

            system.debug('Response - success - Capture received');

            commercepayments.CaptureResponse captureResponse = new

       commercepayments.CaptureResponse();

            captureResponse.setAsync(true); // Very important to treat this as an

       asynchronous transaction

       captureResponse.setGatewayReferenceNumber((String)mapOfResponseValues.get('pspReference'));

            captureResponse.setSalesforceResultCodeInfo(new

       commercepayments.SalesforceResultCodeInfo(commercepayments.SalesforceResultCode.Success));

            return captureResponse;

          } else {

            system.debug('Response - error - Capture not received by Gateway');

            String message = (String)mapOfResponseValues.get('message');

            commercepayments.GatewayErrorResponse error = new

       commercepayments.GatewayErrorResponse(String.valueOf(statusCode), message);

            return error;

          }

       }

##### Payment Authorization Reversal Service

```

An authorization reversal is a transaction that negates an authorization by releasing the hold on funds in a customer’s payment method.

Authorization Reversal Apex Class Implementation
The Authorization Reversal Service uses the `AuthorizationReversalRequest` and
`AuthorizationReversalResponse` classes to manage the creation and storage of authorization reversal information.
Implement these classes in your payment gateway adapter.

##### Payment Authorization Reversal Service API

An authorization reversal is a transaction that negates an authorization by releasing the hold on funds in a customer’s payment
method. Use the authorization reversal service to provide users with the ability to reverse an outstanding payment authorization.


Apex Developer Guide Using Salesforce Features with Apex

###### Authorization Reversal Apex Class Implementation

The Authorization Reversal Service uses the `AuthorizationReversalRequest` and `AuthorizationReversalResponse`
classes to manage the creation and storage of authorization reversal information. Implement these classes in your payment gateway
adapter.

**AuthorizationReversalRequest**
Represents the authorization reversal request. Extends `BaseRequest` and inherits all its methods.

`AuthorizationReversalRequest` uses a constructor to build an authorization reversal request record in Salesforce. The
`AuthorizationReversalRequest` constructor takes no arguments. You can invoke it as follows.

```
     CommercePayments.AuthorizationReversalRequest arr = new

     CommercePayments.AuthorizationReversalRequest();

```

If you want to build a sample authorization reversal, you can also invoke a constructor with arguments for the reversal amount and
payment authorization ID. However, the constructor would only work for test usage and would throw an exception if used outside
of the Apex test context.

```
     commercepayments.AuthorizationReversalRequest authorizationReversalRequest =

     new commercepayments.AuthorizationReversalRequest(80, authObj.id);

```

**AuthorizationReversalResponse**
The payment gateway adapter sends this class as a response for an Authorization Reversal request type. Extends
`AbstractResponse` and inherits its methods.

`AuthorizationReversalResponse` uses a constructor to build an authorization reversal request record in Salesforce. The
`AuthorizationReversalResponse` constructor takes no arguments. You can invoke it as follows:

```
     CommercePayments.AuthorizationReversalResponse arp = new

     CommercePayments.AuthorizationReversalResponse();

```

Note: Salesforce doesn't support bulk operations or custom fields in the authorization reversal process.

Implementing Reversal Classes in Your Gateway Adapter

Add your reversal classes to your payment gateway adapter. We recommend adding `AuthorizationReversal` as a possible
`requestType` value when calling `processRequest` on the gateway’s response.

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

        commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

        commercepayments.GatewayResponse response;

        try {

        //add conditions for other requestType values here

        //..

        else if (requestType == commercepayments.RequestType.AuthorizationReversal) {

             response =

   createAuthReversalResponse((commercepayments.AuthorizationReversalRequest)gatewayContext.getPaymentRequest());}

        return response;

```


Apex Developer Guide Using Salesforce Features with Apex

Then, add a class that sets the amount of the authorization reversal request, gateway information, and the Salesforce result code.

```
   global commercepayments.GatewayResponse

   createAuthReversalResponse(commercepayments.AuthorizationReversalRequest authReversalRequest)

    {

        commercepayments.AuthorizationReversalResponse authReversalResponse = new

   commercepayments.AuthorizationReversalResponse();

        if(authReversalRequest.amount!=null )

        {

           authReversalResponse.setAmount(authReversalRequest.amount);

        }

        else

        {

           throw new SalesforceValidationException('Required Field Missing : Amount');

        }

        system.debug('Response - success');

        authReversalResponse.setGatewayDate(system.now());

        authReversalResponse.setGatewayResultCode('00');

        authReversalResponse.setGatewayResultCodeDescription('Transaction Normal');

        //Replace 'xxxxx' with the gateway reference number.

        authReversalResponse.setGatewayReferenceNumber('SF'+xxxxx);

   authReversalResponse.setSalesforceResultCodeInfo(SUCCESS_SALESFORCE_RESULT_CODE_INFO);

        return authReversalResponse;

      }

```

**Sample Apex Request**

```
   String authorizationId = '0XcxXXXXXXXXXXXXXXX';

   ConnectApi.AuthorizationReversalRequest authorizationReversalRequest = new

   ConnectApi.AuthorizationReversalRequest();

   authorizationReversalRequest.amount = 1.0;

   authorizationReversalRequest.comments = 'Captured from custom action';

   authorizationReversalRequest.ipAddress = '192.162.10.3';

   authorizationReversalRequest.email = 'testuser@example.com';

   ConnectApi.AuthorizationReversalResponse authorizationReversalResponse =

   ConnectApi.Payments.reverseAuthorization(authorizationReversalRequest, authorizationId);

   String authReversalId = authorizationReversalResponse.paymentAuthAdjustment.id;

   System.debug(authorizationReversalResponse);

   System.debug(authReversalId);

###### Payment Authorization Reversal Service API

```

An authorization reversal is a transaction that negates an authorization by releasing the hold on funds in a customer’s payment method.
Use the authorization reversal service to provide users with the ability to reverse an outstanding payment authorization.

Sometimes, a customer performs a payment authorization but then needs to cancel all or part of the authorization later. For example,
the customer bought three items, and then realized that the first item is already in their stock. Commerce Payments API allows you to
reverse all or part of an outstanding payment authorization.

After the customer payment gateway authorizes a payment, Commerce Payments creates a payment authorization record to store
information about the authorization. When a user or process performs a reversal against the authorization, the authorization reversal
service creates a payment authorization adjustment to store information. The adjustment is related to the authorization.


Apex Developer Guide Using Salesforce Features with Apex

If the payment authorization is associated with an order payment summary, then the reversal amount is added to the order payment
summary’s `AuthorizationReversalAmount` and subtracted from its `AvailableToCaptureAmount` . But the
`AvailableToCaptureAmount` is never below 0, even if a reversal makes its calculation a negative amount.

Note: For an authorization reversal, the payment gateway log’s `OrderPaymentSummaryId` always defaults to null. If there’s
an associated order payment summary, your code can set the value.

Call the authorization reversal service by making a POST request to the following endpoint.

**Endpoint**

```
   /commerce/payments/authorizations/${*authorizationId*}/reversals

```

The service accepts one authorization reversal request per call. The following payment authorization adjustment API parameters are
accepted.

**Table 8: Reversal Service Input Parameters**


Apex Developer Guide Using Salesforce Features with Apex

Sample Request and Response

This request calls a $150 reversal against an authorization.

```
   {

     "accountId":"",

     "amount": "150",* "comments": "authorization reversal request",

     "effectiveDate":"2020-10-18T11:32:27.000Z",

     "ipAddress": "202.95.77.70",

     "macAddress": "00-14-22-01-23-45",

     "phone": "100-456-67",

     "email": "test@example.org",

     "additionalData":{

        //add additional parameters if needed

       "key1":"value1",

       "key2":"value2",

       "key3":"value3",

       "key4":"value4",

       "key5":"value5"

      }

   }

```

**Sample Response - Success**

A successful authorization reversal response provides information about the gateway’s response and the values to construct a payment
authorization adjustment entity.

```
   HPP Status Code: 201

   {

     "gatewayResponse" : {

      "gatewayDate" : "2020-10-23T15:21:58.833Z",

      "gatewayReferenceNumber" : "439XXXXXXX",

      "gatewayResultCode" : "00",

      "gatewayResultCodeDescription" : "Transaction Normal",

      "salesforceResultCode" : "Success"

     },

     "paymentAuthAdjustment" : {

      "amount" : "150.0",

      "currencyIsoCode" : "USD",

      "effectiveDate" : "2020-10-18T11:32:27.000Z",

      "id" : "9tvR00000004Cf1MAE",

      "paymentAuthAdjustmentNumber" : "PAA-00XXXXXXX",

      "requestDate" : "2020-10-23T15:21:58.000Z",

      "status" : "Processed"

     },

     "paymentGatewayLogs" : [ {

      "createdDate" : "2020-10-23T15:21:58.000Z",

      "gatewayResultCode" : "00",

      "id" : "0XtXXXXXXXXXXXXXXX",

      "interactionStatus" : "Success"

     } ]

   }

```

The resulting payment authorization adjustment in Salesforce would look like this.

If an error is returned, the response contains the gateway's error code and error message.


Apex Developer Guide Using Salesforce Features with Apex

**Sample Response - Error**

```
   {

      "errorCode":"",

      "errorMessage":""

   }

##### Tokenization Service

```

The credit card tokenization process replaces sensitive customer information with a one-time algorithmically generated number, called
a token, used during the payment transaction. Salesforce stores the token and then uses that token as a representation of the credit card
used for transactions. The token lets you store information about the credit card without storing sensitive customer data, such as credit
card numbers, in Salesforce.

##### Tokenization Service Apex Class Implementation

Use the tokenization service to hide sensitive customer payment method data. The Tokenization service uses
`PaymentMethodTokenizationRequest`, `PaymentMethodTokenizationResponse`, and
`CardPaymentMethodRequest` . Implement these classes in your payment gateway adapter.

##### Tokenization Service API

The credit card tokenization process replaces sensitive customer information with a one-time algorithmically generated number,
called a token, to use during the payment transaction. Salesforce stores the token and then uses that token as a representation of
the credit card used for transactions. The token stores information about the credit card without storing sensitive customer data
such as credit card numbers. To add tokenization capabilities to your payment services, implement our Tokenization API.

##### Tokenization Service Apex Class Implementation

Use the tokenization service to hide sensitive customer payment method data. The Tokenization
service uses `PaymentMethodTokenizationRequest`,
`PaymentMethodTokenizationResponse`, and `CardPaymentMethodRequest` .
Implement these classes in your payment gateway adapter.

Encryption for Tokenized Payment Methods

EDITIONS

Available in: Salesforce
Spring '21 and later

CommercePayments uses Salesforce field encryption to securely store gateway token values on customer payment method entities
such as DigitalWallet, CardPaymentMethod, and AlternativePaymentMethod.

CardPaymentMethod and DigitalWallet contain the GatewayTokenEncrypted field, available in API v52.0 and later, and the GatewayToken
[field, available in API v48.0 and later. Both fields store gateway token values. However, GatewayTokenEncrypted uses Salesforce Classic](https://help.salesforce.com/s/articleView?id=platform.fields_about_encrypted_fields&type=5&language=en_US)
[Encryption for Custom Fields to securely encrypt the token. GatewayToken doesn't use encryption. To ensure secure tokenization, we](https://help.salesforce.com/s/articleView?id=platform.fields_about_encrypted_fields&type=5&language=en_US)
recommend using GatewayTokenEncrypted on your DigitalWallets and CardPaymentMethods. The AlternativePaymentMethod object
uses a GatewayToken field for token storage, however, this field is encrypted on AlternativePaymentMethods.

In API version 52.0 and later, CardPaymentMethods and DigitalWallets can’t store values for GatewayTokenEncryption and GatewayToken
at the same time on the same record. If you try to assign one while the other exists, Salesforce throws an error.

Your payment gateway adapter uses the `PaymentMethodTokenizationRequest` and
`PaymentMethodTokenizationResponse` classes to retrieve a gateway token from the payment gateway, encrypt it in
Salesforce, and store the value on a payment method entity. Let's see how we can configure these classes in our payment gateway
adapter.


Apex Developer Guide Using Salesforce Features with Apex

Implementing Tokenization Classes in Your Gateway Adapter

The following code is used within your `PaymentGatewayAdapter` Apex class.

Gateway tokens are created and encrypted when the `GatewayResponse` class's `processRequest` method receives a tokenization
request. If the request type is `Tokenize`, `GatewayResponse` calls the `createTokenizeResponse` method and passes an
instance of the `PaymentMethodTokenizationRequest` class. The passed `PaymentMethodTokenizationRequest`
object contains the address and cardPaymentMethod information that the payment gateway needs to manage the tokenization process.
For example:

```
   global commercepayments.GatewayResponse processRequest(commercepayments.paymentGatewayContext

    gatewayContext) {

        commercepayments.RequestType requestType = gatewayContext.getPaymentRequestType();

         commercepayments.GatewayResponse response;

         try

         {

           if (requestType == commercepayments.RequestType.Tokenize) {

                response =

   createTokenizeResponse((commercepayments.PaymentMethodTokenizationRequest)gatewayContext.getPaymentRequest());

           }

           //Add other else if statements for different request types as needed.

           return response;

         }

         catch(SalesforceValidationException e)

         {

            commercepayments.GatewayErrorResponse error = new

   commercepayments.GatewayErrorResponse('400', e.getMessage());

            return error;

         }

      }

```

Configure the `createTokenizeResponse` method to accept an instance of `PaymentMethodTokenizationRequest`
and then build an instance of `[PaymentMethodTokenizationResponse](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentMethodTokenizationResponse.htm#apex_class_commercepayments_PaymentMethodTokenizationResponse)` based on the values that it receives from the payment
gateway. The tokenizeResponse contains the results of the gateway's tokenization process, and if successful, the tokenized value. In this
example, we call the `setGatewayTokenEncrypted` method to set the tokenized value in our tokenization response.

```
   public commercepayments.GatewayResponse

   createTokenizeResponse(commercepayments.PaymentMethodTokenizationRequest tokenizeRequest)

    {

         commercepayments.PaymentMethodTokenizationResponse tokenizeResponse = new

   commercepayments.PaymentMethodTokenizationResponse();

         tokenizeResponse.setGatewayTokenEncrypted(encryptedValue);

         tokenizeResponse.setGatewayTokenDetails(tokenDetails);

         tokenizeResponse.setGatewayAvsCode(avsCode);

         tokenizeResponse.setGatewayMessage(gatewayMessage);

         tokenizeResponse.setGatewayResultCode(resultcode);

         tokenizeResponse.setGatewayResultCodeDescription(resultCodeDescription);

         tokenizeResponse.setSalesforceResultCodeInfo(resultCodeInfo);

         tokenizeResponse.setGatewayDate(system.now());

         return tokenizeResponse;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

The `setGatewayTokenEncrypted` method is available in Salesforce API v52.0 and later. It uses Salesforce classic encryption to
set the encrypted token value that you can store in GatewayTokenEncrypted on a CardPaymentMethod or DigitalWallet, or in GatewayToken
on an AlternativePaymentMethod. We recommend using `setGatewayTokenEncrypted` to ensure your tokenized payment
method values are encrypted and secure.

```
      /** @description Method to set Gateway token to persist in Encrypted Text */

      global void setGatewayTokenEncrypted(String gatewayTokenEncrypted) {

         if (gatewayTokenSet) {

           throwTokenError();

         }

         this.delegate.setGatewayTokenEncrypted(gatewayTokenEncrypted);

         gatewayTokenEncryptedSet = true;

      }

```

If the instantiated class already has a gateway token, `setGatewayTokenEncrypted` throws an error.

Note: While the PaymentMethodTokenizationResponse's `[setGatewayToken](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentMethodTokenizationResponse.htm#apex_commercepayments_PaymentMethodTokenizationResponse_setGatewayToken)` method (available in API v48.0 and later) also
returns a payment method token, the tokenized value isn't encrypted.

###### Tokenization Service API

The credit card tokenization process replaces sensitive customer information with a one-time algorithmically generated number, called
a token, to use during the payment transaction. Salesforce stores the token and then uses that token as a representation of the credit
card used for transactions. The token stores information about the credit card without storing sensitive customer data such as credit
card numbers. To add tokenization capabilities to your payment services, implement our Tokenization API.

In a typical tokenization process, the payments platform accepts customer payment method data and passes it to a remote token service
server on the payment gateway, outside of Salesforce. The server provides the tokenized value for storage on the platform. For example,
a customer provides a credit card number of _`4111 1111 1111 1234`_ . The token server stores this value, associates it with a token
of _`2537446225198291`_, and sends that token for storage on the platform.

During communication with the merchant, the merchant sends the _`2537446225198291`_ token to the token server. The token
server confirms that it matches the customer’s token, and authorizes the merchant to perform the transaction against the customer’s
card.

The Commerce Payments Tokenization API accepts credit card information and uses the external payment gateway configured through
the customer's Salesforce org to tokenize the card information. It then returns the tokenization representation. The API then saves the
token in `[CardPaymentMethod](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_cardpaymentmethod.htm)` .

Call the tokenization service by making a POST request to this endpoint.

```
   /commerce/payments/payment-methods

```

The Tokenization Service accepts these request parameters from payment and related entities.


Apex Developer Guide Using Salesforce Features with Apex

Sample Request and Response

This sample request provides a customer's credit card information for tokenization. Some optional parameters are left blank.

```
   {

      "cardPaymentMethod": {

        "cardHolderName":"Carol Smith",

        "expiryMonth": "05",

        "expiryYear": "2025",

        "startMonth": "",

        "startYear": "",

        "cvv": "000",

        "cardNumber": "4111111111111111",

        "cardCategory": "Credit",

        "cardType": "Visa",

        "nickName": "",

        "cardHolderFirstName": "Carol",

        "cardHolderLastName": "Smith",

        "email" : "csmith@example.com",

        "comments" : "",

        "accountId": "000XXXXXXXX"

      },

      "address":{

        "street": "128 1st Street",

        "city": "San Francisco",

        "state": "CA",

        "country": "USA",

        "postalCode": "94015",

        "companyName": "Salesforce"

      },

      "paymentGatewayId" : "000XXXXXXXX",

      "email": ""

      "ipAddress": "",

      "macAddress": "",

      "phone": "",

      "additionalData":{

         //add additional information if needed

        "key1":"value1",

```


Apex Developer Guide Using Salesforce Features with Apex

```
        "key2":"value2",

        "key3":"value3",

        "key4":"value4",

        "key5":"value5"

      }

   }

```

A successful tokenization response updates the payment method and provides information about the gateway response and any
payment gateway logs.

```
   {

     "paymentMethod": {

      "id": "03OR0000000xxxxxxx",

      "accountId" : "001xx000000xxxxxxx",

      "status" : "Active"

     },

     "gatewayResponse" : {

      "gatewayResultCode": "00",

      "gatewayResultCodeDescription": "Transaction Normal",

      "gatewayDate": "2020-12-08T04:03:20.000Z",

      "gatewayAvsCode" : "7638788018713617",

      "gatewayMessage" : "8313990738208498",

      "salesforceResultCode": "Success",

      "gatewayTokenEncrypted" : "SF701252"

     }

     "paymentGatewayLogs" : [ {

      "createdDate" : "2020-12-08T04:03:20.000Z",

      "gatewayResultCode" : "00",

      "id" : "0XtR0000000xxxxxxx",

      "interactionStatus" : "NoOp"

     } ],

   }

##### Alternative Payment Methods

```

An alternative payment method allows customers to store and represent payment method
information not represented by another pre-defined payment method such as
`CardPaymentMethod` or `DigitalWallet` . Common examples of alternative payment
methods include CashOnDeliver, Klarna, and Direct Debit. Alternative payment methods are available
in API v51.0 and later.

EDITIONS

Available in: Salesforce
Spring '21 and later

Create a unique record type for each type of alternative payment method in your org. This way,
each of your alternative payment methods can show different picklist values and page layouts based on the method provider and
gateway provider’s requirements. For example, you could have one alternative payment method record type for direct debit and a
different record type for cash on deliver.

We also recommend creating a `GtwyProviderPaymentMethodType` for each of your unique alternative payment method
record types.

AlternativePaymentMethod has the private sharing model enabled as default for both internal and external users. Only the record owner
and users with higher ownership have Read, Edit, and Delete access.


Apex Developer Guide Using Salesforce Features with Apex

Example: Let's say you wanted to make an alternative payment method for GiroPay. First, create an
`AlternativePaymentMethod` record type.

**New RecordType**

```
      /services/data/v51.0/sobjects/RecordType

      {

      "Name" : "Giro Pay",

      "DeveloperName" : "GiroPay",

      "SobjectType" : "AlternativePaymentMethod"

      }

```

Next, create an alternative payment method record for the `AlternativePaymentMethod` record type.

**New AlternativePaymentMethod**

```
      /services/data/v51.0/sobjects/AlternativePaymentMethod

      {

      "ProcessingMode": "External",

      "status":"Active",

      "GatewayToken":"mHkDsh0oIA3mnWjo9UL",

      "NickName" : "MyGiroPay",

      "RecordTypeId" : "{record_type_id}"

      }

```

You can also create a gateway provider payment method type.

**New GtwyProvPaymentMethodType**

```
      {

      "PaymentGatewayProviderId": "XXXXXXXXXXXXXXX",

      "PaymentMethodType":"AlternativePaymentMethod",

      "GtwyProviderPaymentMethodType" : "PM_Giro",

      "DeveloperName" : "DevName",

      "MasterLabel" : "MasterLabel",

      "RecordTypeId" : "{record_type_id}"

      }

##### Process Payments

```

Process a payment in the payment gateway.

To access `commercepayments` API, you need the PaymentPlatform org permission.

**1.** Get the payment capture request object from the `[PaymentGatewayContext Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)` .

EDITIONS

Available in: Salesforce
Spring ’20

```
commercepayments.CaptureRequest =

(commercepayments.CaptureRequest)gatewayContext.getPaymentRequest()

```


Apex Developer Guide Using Salesforce Features with Apex

**2.** Set the HTTP request object.

```
     HttpRequest req = new HttpRequest();

     req.setHeader('Content-Type', 'application/json');

```

**3.** Read the parameters from the `[CaptureRequest](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_CaptureRequest.htm#apex_class_commerce_payments_CaptureRequest)` object and prepare the HTTP request body.

**4.** Make the HTTP call to the gateway using the `[PaymentsHttp Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentsHttp.htm#apex_class_commerce_payments_PaymentsHttp)` .

```
     commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

     HttpResponse res = http.send(req);

```

**5.** Parse the `httpResponse` and prepare the `[CaptureResponse](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_CaptureResponse.htm#apex_class_commerce_payments_CaptureResponse)` object.

```
     commercepayments.CaptureResponse captureResponse = new commercepayments.CaptureResponse();

     captureResponse.setGatewayResultCode(“”);

     captureResponse.setGatewayResultCodeDescription(“”);

     captureResponse.setGatewayReferenceNumber(“”);

     captureResponse.setSalesforceResultCodeInfo(getSalesforceResultCodeInfo(commercepayments.SalesforceResultCode.SUCCESS.name()));

     captureResponse.setGatewayReferenceDetails(“”);

     captureResponse.setAmount(double.valueOf(100);

```

**6.** Return the `captureResponse` .

##### Process Refund

Process a refund in the payment gateway.

To access the `commercepayments` API, you need the PaymentPlatform org permission.

**1.** Get the referenced refund request object from the `[PaymentGatewayContext Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)` .

EDITIONS

Available in: Salesforce
Spring ’20

```
  commercepayments.ReferencedRefundRequest =

  (commercepayments.ReferencedRefundRequest)gatewayContext.getPaymentRequest();

```

**2.** Set the HTTP request object.

```
  HttpRequest req = new HttpRequest();

  req.setHeader('Content-Type', 'application/json');

```

**3.** Read the parameters from the `[ReferencedRefundRequest object](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_ReferencedRefundRequest.htm#apex_class_commerce_payments_ReferencedRefundRequest)` and prepare the HTTP request body.

**4.** Make the HTTP call to the gateway using the `[PaymentsHttp Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_PaymentsHttp.htm#apex_class_commerce_payments_PaymentsHttp)` .

```
  commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

  HttpResponse res = http.send(req);

```

**5.** Parse the `httpResponse` and prepare the `[ReferencedRefundResponse](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_commercepayments_ReferencedRefundResponse.htm#apex_class_commerce_payments_ReferencedRefundResponse)` object.

```
  commercepayments.ReferencedRefundResponse referencedRefundResponse = new

  commercepayments.ReferencedRefundResponse();

  referencedRefundResponse.setGatewayResultCode(“”);

  referencedRefundResponse.setGatewayResultCodeDescription(“”);

  referencedRefundResponse.setGatewayReferenceNumber(“”);

```


Apex Developer Guide Using Salesforce Features with Apex

```
     referencedRefundResponse.setSalesforceResultCodeInfo(getSalesforceResultCodeInfo(commercepayments.SalesforceResultCode.SUCCESS.name()));

     referencedRefundResponse.setGatewayReferenceDetails(“”);

     referencedRefundResponse.setAmount(double.valueOf(100);

```

**6.** Return the `referencedRefundResponse` .

##### Idempotency Guidelines

Idempotency represents the ability of a payment gateway to recognize duplicate requests submitted
either in error or maliciously, and then process the duplicate requests accordingly. When working
with an idempotent gateway, consider these important guidelines.

To access the `commercepayments` API, you need the PaymentPlatform org permission.

EDITIONS

Available in: Salesforce
Spring ’20

The payment gateway adapter class is linked to a paymentGatewayProvider object record. CCS
Payments provides its own layer of idempotency for its own service request. Each payment gateway
can also specify their `idempotencySupported` value in the paymentGatewayProvider object record. If Salesforce CCS Payment
APIs detects a duplicate request and the gateway provider supports idempotency, the request body’s `duplicate` parameter becomes
_`True`_ .

```
commercepayments.CaptureRequest request =

(commercepayments.CaptureRequest)paymentGatewayContext.getPaymentRequest();

Boolean isDuplicate = requestObject.duplicate

```

The idempotency key can be fetched from the request object.

```
String idempotencyKey = request.idempotencyKey

##### Sample Payment Gateway Implementation for CommercePayments

```

We’ve created a GitHub repository containing code samples for a sample Payeezy payment gateway implementation with the
CommercePayments namespace. Review the sample code if you need help with configuring your payment gateway implementation.

[Review our code samples in the CommercePayments Gateway Reference Implementation for Payeezy repository.](https://github.com/forcedotcom/Core-Payments-Reference-Gateway-Integration-Adapters)

#### Connect in Apex

Use Connect in Apex to develop custom experiences in Salesforce. Connect in Apex provides programmatic access to B2B Commerce,
CMS managed content, Experience Cloud sites, topics, and more. Create Apex pages that display Chatter feeds, post feed items with
mentions and topics, and update user and group photos. Create triggers that update Chatter feeds.

Many Connect REST API resource actions are exposed as static methods on Apex classes in the `ConnectApi` namespace. These
#### methods use other ConnectApi classes to input and return information. The ConnectApi namespace is referred to as Connect

_in Apex._

In Apex, you can access some Connect data using SOQL queries and objects. However, it’s simpler to expose data in `ConnectApi`
classes, and data is localized and structured for display. For example, instead of making several calls to access and assemble a feed, you
can do it with a single call.

#### Connect in Apex methods execute in the context of the user executing the methods. The code has access to whatever the context user

has access to. It doesn’t run in system mode.

[For Connect in Apex reference information, see ConnectApi Namespace.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_connect_api.htm)


Apex Developer Guide Using Salesforce Features with Apex

##### Connect in Apex Examples

Use these examples to perform common tasks with Connect in Apex.

Connect in Apex Features
This topic describes which classes and methods to use to work with common Connect in Apex features.

Using ConnectApi Input and Output Classes
Some classes in the `ConnectApi` namespace contain static methods that access Connect REST API data. The `ConnectApi`
namespace also contains input classes to pass as parameters and output classes that calls to the static methods return.

Understanding Limits for ConnectApi Classes
Limits for methods in the `ConnectApi` namespace are different than the limits for other Apex classes.

Packaging ConnectApi Classes
If you include `ConnectApi` classes in a package, be aware of Chatter dependencies.

Serializing and Deserializing ConnectApi Objects
When `ConnectApi` output objects are serialized into JSON, the structure is similar to the JSON returned from Connect REST API.
When `ConnectApi` input objects are deserialized from JSON, the format is also similar to Connect REST API.

ConnectApi Versioning and Equality Checking
Versioning in `ConnectApi` classes follows specific rules that are different than the rules for other Apex classes.

Casting ConnectApi Objects
It may be useful to downcast some `ConnectApi` output objects to a more specific type.

Wildcards
Use wildcard characters to match text patterns in Connect REST API and Connect in Apex searches.

Testing ConnectApi Code
Like all Apex code, Connect in Apex code requires test coverage.

Differences Between ConnectApi Classes and Other Apex Classes
Note these additional differences between `ConnectApi` classes and other Apex classes.

##### Connect in Apex Examples

Use these examples to perform common tasks with Connect in Apex.

Get Feed Elements From a Feed
Call a method to get feed elements from a feed.

Get Feed Elements From Another User’s Feed
Call a method to get feed elements from another user’s feed.

Get Site-Specific Feed Elements from a Feed
Call a method to display a user profile feed that contains only feed elements that are scoped to a specific Experience Cloud site.

Post a Feed Element
Make a call to post a feed element.

Post a Feed Element with a Mention
Call a method or use the ConnectApiHelper repository to post a feed.

Post a Feed Element with Existing Files
Call a method to post a feed element with already uploaded files.


Apex Developer Guide Using Salesforce Features with Apex

Post a Rich-Text Feed Element with Inline Image
Call a method or use the ConnectApiHelper repository to post a feed element with an already uploaded, inline image.

Post a Rich-Text Feed Element with a Code Block
Call a method to post a feed element with a code block.

Post a Feed Element with a New File (Binary) Attachment
Call a method to post a feed element with a new file.

Post a Batch of Feed Elements
Use a trigger to call a method to bulk post to the feeds of accounts.

Post a Batch of Feed Elements with a New (Binary) File
Use a trigger to call a method to bulk post a new file to the feeds of accounts.

Define an Action Link and Post with a Feed Element
Create one action link in an action link group, associate the action link group with a feed item, and post the feed item.

Define an Action Link in a Template and Post with a Feed Element
Create an action link and action link group and instantiate the action link group from a template.

Edit a Feed Element
Call a method to edit a feed element.

Edit a Question Title and Post
Call a method to edit a question title and post.

Like a Feed Element
Call a method to like a feed element.

Bookmark a Feed Element
Call a method to bookmark a feed element.

Share a Feed Element (prior to Version 39.0)
Call a method to share a feed element.

Share a Feed Element (in Version 39.0 and Later)
Call a method to share a feed element.

Send a Direct Message
Call a method to send a direct message.

Post a Comment
Call a method to post a comment.

Post a Comment with a Mention
Make call or use the ConnectApiHelper repository to post a comment with a mention.

Post a Comment with an Existing File
Make a call to post a comment with an already uploaded file.

Post a Comment with a New File
Call a method to post a comment with a new file.

Post a Rich-Text Comment with Inline Image
Make a call or use the ConnectApiHelper repository to post a comment with an already uploaded, inline image.

Post a Rich-Text Feed Comment with a Code Block
Call a method to post a comment with a code block.


Apex Developer Guide Using Salesforce Features with Apex

Edit a Comment
Call a method to edit a comment.

Follow a Record
Call a method to follow a record.

Unfollow a Record
Call a method to stop following a record.

Get a Repository
Call a method to get a repository.

Get Repositories
Call a method to get all repositories.

Get Allowed Item Types
Call a method to get allowed item types.

Get Previews
Call a method to get all supported preview formats and their respective URLs.

Get a File Preview
Call a method to get a file preview.

Get Repository Folder Items
Call a method to get a collection of repository folder items.

Get a Repository Folder
Call a method to get a repository folder.

Get a Repository File Without Permissions Information
Call a method to get a repository file without permission information.

Get a Repository File with Permissions Information
Call a method to get a repository file with permission information.

Create a Repository File Without Content (Metadata Only)
Call a method to create a file without binary content (metadata only) in a Google Drive repository folder.

Create a Repository File with Content
Call a method to create a file with binary content in a Google Drive repository folder.

Update a Repository File Without Content (Metadata Only)
Call a method to update the metadata of a repository file.

Update a Repository File with Content
Call a method to update a repository file with content.

Get an Authentication URL
Call a method to get an authentication URL.

Resolve a Prompt Template
Call a method to resolve a prompt template.

Create a Cart and Cart Item with Custom Fields in a Commerce Store
Create a cart with a cart item using custom fields for a buyer or guest user in your Commerce store.


Apex Developer Guide Using Salesforce Features with Apex

###### Get Feed Elements From a Feed

Call a method to get feed elements from a feed.

Call `[getFeedElementsFromFeed(communityId, feedType, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_2)` to get the first page of feed elements
from the context user’s news feed.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.News, 'me');

```

The `getFeedElementsFromFeed` method is overloaded, which means that the method name has many different signatures. A
signature is the name of the method and its parameters in order.

Each signature lets you send different inputs. For example, one signature may specify the feed type and the subject ID. Another signature
could have those parameters and an additional parameter to specify the maximum number of comments to return for each feed element.

Tip: Each signature operates on certain feed types. Use the signatures that operate on the `ConnectApi.FeedType.Record`
to get group feeds, since a group is a record type.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

###### Get Feed Elements From Another User’s Feed

Call a method to get feed elements from another user’s feed.

Call `[getFeedElementsFromFeed(communityId, feedType, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_2)` to get the first page of feed elements
from another user’s feed.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, '005R0000000HwMA');

```

This example calls the same method to get the first page of feed elements from another user’s record feed.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.Record, '005R0000000HwMA');

```

The `getFeedElementsFromFeed` method is overloaded, which means that the method name has many different signatures. A
signature is the name of the method and its parameters in order.

Each signature lets you send different inputs. For example, one signature can specify the feed type and the subject ID. Another signature
could have those parameters and an extra parameter to specify the maximum number of comments to return for each feed element.

###### Get Site-Specific Feed Elements from a Feed

Call a method to display a user profile feed that contains only feed elements that are scoped to a specific Experience Cloud site.

Feed elements that have a User or a Group parent record are scoped to sites. Feed elements whose parents are record types other than
User or Group are always visible in all sites. Other parent record types could be scoped to sites in the future.


Apex Developer Guide Using Salesforce Features with Apex

This example calls `[getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_7a)`
`[density, pageParam, pageSize, sortParam, filter)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_7a)` to get only site-specific feed elements.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, 'me', 3, ConnectApi.FeedDensity.FewerUpdates, null, null,

    ConnectApi.FeedSortOrder.LastModifiedDateDesc, ConnectApi.FeedFilter.CommunityScoped );

###### Post a Feed Element

```

Make a call to post a feed element.

Call `[postFeedElement(communityId, subjectId, feedElementType, text)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_1)` to post a string of text.

```
   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), '0F9d0000000TreH',

   ConnectApi.FeedElementType.FeedItem, 'On vacation this week.');

```

The second parameter, `subjectId` is the ID of the parent this feed element is posted to. The value can be the ID of a user, group, or
record, or the string `me` to indicate the context user.

###### Post a Feed Element with a Mention

Call a method or use the ConnectApiHelper repository to post a feed.

[You can post feed elements with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or](https://github.com/forcedotcom/ConnectApiHelper)
use this example, which calls `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` .

```
   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   mentionSegmentInput.id = '005RR000000Dme9';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

   textSegmentInput.text = 'Could you take a look?';

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   feedItemInput.feedElementType = ConnectApi.FeedElementType.FeedItem;

   feedItemInput.subjectId = '0F9RR0000004CPw';

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

###### Post a Feed Element with Existing Files

```

Call a method to post a feed element with already uploaded files.

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed item with files that have already been uploaded.

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Would you please review these docs?';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a files capability to hold the file(s).

   List<String> fileIds = new List<String>();

   fileIds.add('069xx00000000QO');

   fileIds.add('069xx00000000QT');

   fileIds.add('069xx00000000Qn');

   fileIds.add('069xx00000000Qi');

   fileIds.add('069xx00000000Qd');

   ConnectApi.FilesCapabilityInput filesInput = new ConnectApi.FilesCapabilityInput();

   filesInput.items = new List<ConnectApi.FileIdInput>();

   for (String fileId : fileIds) {

      ConnectApi.FileIdInput idInput = new ConnectApi.FileIdInput();

      idInput.id = fileId;

      filesInput.items.add(idInput);

   }

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.files = filesInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

###### Post a Rich-Text Feed Element with Inline Image

```

Call a method or use the ConnectApiHelper repository to post a feed element with an already uploaded, inline image.

[You can post rich-text feed elements with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to](https://github.com/forcedotcom/ConnectApiHelper)
write a single line of code, or use this example, which calls `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` . In this
example, the image file is existing content that has already been uploaded to Salesforce as a content document (069). The post also
includes text and a mention.

```
   String communityId = null;

   String imageId = '069D00000001INA';

   String mentionedUserId = '005D0000001QNpr';

   String targetUserOrGroupOrRecordId = '005D0000001Gif0';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.MarkupBeginSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_markup_begin_segment.htm)

_Apex Reference Guide_ [: ConnectApi.MarkupEndSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_markup_end_segment.htm)

_Apex Reference Guide_ [: ConnectApi.InlineImageSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_inline_image_segment.htm)

###### Post a Rich-Text Feed Element with a Code Block

Call a method to post a feed element with a code block.


Apex Developer Guide Using Salesforce Features with Apex

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed item with a code block.

```
   String communityId = null;

   String targetUserOrGroupOrRecordId = 'me';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postFeedElement(communityId, input);

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.MarkupBeginSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_markup_begin_segment.htm)

_Apex Reference Guide_ [: ConnectApi.MarkupEndSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_markup_end_segment.htm)

###### Post a Feed Element with a New File (Binary) Attachment

Call a method to post a feed element with a new file.

Important: In version 36.0 and later, you can’t post a feed element with a new file in the same call. Upload files to Salesforce first,
and then specify existing files when posting a feed element.

This example calls `[postFeedElement(communityId, feedElement, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_2)` to post a feed
item with a new file (binary) attachment.

```
   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = 'me';

   ConnectApi.ContentCapabilityInput contentInput = new ConnectApi.ContentCapabilityInput();

   contentInput.title = 'Title';

   ConnectApi.FeedElementCapabilitiesInput capabilities = new

   ConnectApi.FeedElementCapabilitiesInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   capabilities.content = contentInput;

   input.capabilities = capabilities;

   String text = 'These are the contents of the new file.';

   Blob myBlob = Blob.valueOf(text);

   ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

   'fileName');

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), input, binInput);

###### Post a Batch of Feed Elements

```

Use a trigger to call a method to bulk post to the feeds of accounts.

This trigger calls `[postFeedElementBatch(communityId, feedElements)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElementBatch_1)` to bulk post to the feeds of newly inserted
accounts.

```
   trigger postFeedItemToAccount on Account (after insert) {

      Account[] accounts = Trigger.new;

      // Bulk post to the account feeds.

      List<ConnectApi.BatchInput> batchInputs = new List<ConnectApi.BatchInput>();

      for (Account a : accounts) {

        ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

        input.subjectId = a.id;

        ConnectApi.MessageBodyInput body = new ConnectApi.MessageBodyInput();

        body.messageSegments = new List<ConnectApi.MessageSegmentInput>();

        ConnectApi.TextSegmentInput textSegment = new ConnectApi.TextSegmentInput();

        textSegment.text = 'Let\'s win the ' + a.name + ' account.';

        body.messageSegments.add(textSegment);

        input.body = body;

        ConnectApi.BatchInput batchInput = new ConnectApi.BatchInput(input);

        batchInputs.add(batchInput);

      }

      ConnectApi.ChatterFeeds.postFeedElementBatch(Network.getNetworkId(), batchInputs);

   }

###### Post a Batch of Feed Elements with a New (Binary) File

```

Use a trigger to call a method to bulk post a new file to the feeds of accounts.

Important: This example is valid in version 32.0–35.0. In version 36.0 and later, you can’t post a batch of feed elements with a
new file in the same call. Upload the file to Salesforce first, and then specify the uploaded file when posting a batch of feed elements.


Apex Developer Guide Using Salesforce Features with Apex

This trigger calls `[postFeedElementBatch(communityId, feedElements)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElementBatch_1)` to bulk post to the feeds of newly inserted
accounts. Each post has a new file (binary) attachment.

```
   trigger postFeedItemToAccountWithBinary on Account (after insert) {

      Account[] accounts = Trigger.new;

      // Bulk post to the account feeds.

      List<ConnectApi.BatchInput> batchInputs = new List<ConnectApi.BatchInput>();

      for (Account a : accounts) {

        ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

        input.subjectId = a.id;

        ConnectApi.MessageBodyInput body = new ConnectApi.MessageBodyInput();

        body.messageSegments = new List<ConnectApi.MessageSegmentInput>();

        ConnectApi.TextSegmentInput textSegment = new ConnectApi.TextSegmentInput();

        textSegment.text = 'Let\'s win the ' + a.name + ' account.';

        body.messageSegments.add(textSegment);

        input.body = body;

        ConnectApi.ContentCapabilityInput contentInput = new

   ConnectApi.ContentCapabilityInput();

        contentInput.title = 'Title';

        ConnectApi.FeedElementCapabilitiesInput capabilities = new

   ConnectApi.FeedElementCapabilitiesInput();

        capabilities.content = contentInput;

        input.capabilities = capabilities;

        String text = 'We are words in a file.';

        Blob myBlob = Blob.valueOf(text);

        ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

    'fileName');

        ConnectApi.BatchInput batchInput = new ConnectApi.BatchInput(input, binInput);

        batchInputs.add(batchInput);

      }

      ConnectApi.ChatterFeeds.postFeedElementBatch(Network.getNetworkId(), batchInputs);

###### Define an Action Link and Post with a Feed Element

```

Create one action link in an action link group, associate the action link group with a feed item, and post the feed item.


Apex Developer Guide Using Salesforce Features with Apex

When a user clicks the action link, the action link requests the Connect REST API resource `/chatter/feed-elements`, which
posts a feed item to the user’s feed. After the user clicks the action link and it executes successfully, its status changes to successful and
the feed item UI is updated.


Apex Developer Guide Using Salesforce Features with Apex

Refresh the user’s feed to see the new post.

This simple example shows you how to use action links to call a Salesforce resource.

Think of an action link as a button on a feed item. Like a button, an action link definition includes a label ( `labelKey` ). An action link
group definition also includes other properties like a URL ( `actionUrl` ), an HTTP method ( `method` ), and an optional request body
( `requestBody` ) and HTTP headers ( `headers` ).

When a user clicks this action link, an HTTP POST request is made to a Connect REST API resource, which posts a feed item to Chatter.
The `requestBody` property holds the request body for the `actionUrl` resource, including the text of the new feed item. In this
example, the new feed item includes only text, but it could include other capabilities such as a file attachment, a poll, or even action
links.

Just like radio buttons, action links must be nested in a group. Action links within a group share the properties of the group and are
mutually exclusive (you can click only one action link within a group). Even if you define only one action link, it must be part of an action
link group.

This example calls `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`
`[actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` to create an action link group definition.

It saves the action link group ID from that call and associates it with a feed element in a call to
`[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` .

To use this code, substitute an OAuth value for your own Salesforce org. Also, verify that the `expirationDate` is in the future. Look
for the “To Do” comments in the code.

```
   ConnectApi.ActionLinkGroupDefinitionInput actionLinkGroupDefinitionInput = new

   ConnectApi.ActionLinkGroupDefinitionInput();

   ConnectApi.ActionLinkDefinitionInput actionLinkDefinitionInput = new

   ConnectApi.ActionLinkDefinitionInput();

   ConnectApi.RequestHeaderInput requestHeaderInput1 = new ConnectApi.RequestHeaderInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   ConnectApi.RequestHeaderInput requestHeaderInput2 = new ConnectApi.RequestHeaderInput();

   // Create the action link group definition.

   actionLinkGroupDefinitionInput.actionLinks = New

   List<ConnectApi.ActionLinkDefinitionInput>();

   actionLinkGroupDefinitionInput.executionsAllowed =

   ConnectApi.ActionLinkExecutionsAllowed.OncePerUser;

   actionLinkGroupDefinitionInput.category = ConnectApi.PlatformActionGroupCategory.Primary;

   // To Do : Verify that the date is in the future.

   // Action link groups are removed from feed elements on the expiration date.

   datetime myDate = datetime.newInstance(2016, 3, 1);

   actionLinkGroupDefinitionInput.expirationDate = myDate;

   // Create the action link definition.

   actionLinkDefinitionInput.actionType = ConnectApi.ActionLinkType.Api;

   actionLinkDefinitionInput.actionUrl = '/services/data/v33.0/chatter/feed-elements';

   actionLinkDefinitionInput.headers = new List<ConnectApi.RequestHeaderInput>();

   actionLinkDefinitionInput.labelKey = 'Post';

   actionLinkDefinitionInput.method = ConnectApi.HttpRequestMethod.HttpPost;

   actionLinkDefinitionInput.requestBody = '{\"subjectId\": \"me\",\"feedElementType\":

   \"FeedItem\",\"body\": {\"messageSegments\": [{\"type\": \"Text\",\"text\": \"This is a

   test post created via an API action link.\"}]}}';

   actionLinkDefinitionInput.requiresConfirmation = true;

   // To Do : Substitute an OAuth value for your Salesforce org.

   requestHeaderInput1.name = 'Authorization';

   requestHeaderInput1.value = 'OAuth

   00DD00000007WNP!ARsAQCwoeV0zzAV847FTl4zF.85w.EwsPbUgXR4SAjsp ';

   actionLinkDefinitionInput.headers.add(requestHeaderInput1);

   requestHeaderInput2.name = 'Content-Type';

   requestHeaderInput2.value = 'application/json';

   actionLinkDefinitionInput.headers.add(requestHeaderInput2);

   // Add the action link definition to the action link group definition.

   actionLinkGroupDefinitionInput.actionLinks.add(actionLinkDefinitionInput);

   // Instantiate the action link group definition.

   ConnectApi.ActionLinkGroupDefinition actionLinkGroupDefinition =

   ConnectApi.ActionLinks.createActionLinkGroupDefinition(Network.getNetworkId(),

   actionLinkGroupDefinitionInput);

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   ConnectApi.AssociatedActionsCapabilityInput associatedActionsCapabilityInput = new

   ConnectApi.AssociatedActionsCapabilityInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   // Set the properties of the feedItemInput object.

   feedItemInput.body = messageBodyInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   feedItemInput.subjectId = 'me';

```


Apex Developer Guide Using Salesforce Features with Apex

```
   // Create the text for the post.

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Click to post a feed item.';

   messageBodyInput.messageSegments.add(textSegmentInput);

   // The feedElementCapabilitiesInput object holds the capabilities of the feed item.

   // Define an associated actions capability to hold the action link group.

   // The action link group ID is returned from the call to create the action link group

   definition.

   feedElementCapabilitiesInput.associatedActions = associatedActionsCapabilityInput;

   associatedActionsCapabilityInput.actionLinkGroupIds = new List<String>();

   associatedActionsCapabilityInput.actionLinkGroupIds.add(actionLinkGroupDefinition.id);

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

Note: If the post fails, check the OAuth ID.

###### Define an Action Link in a Template and Post with a Feed Element

Create an action link and action link group and instantiate the action link group from a template.

This example creates the same action link and action link group as the example Define an Action Link and Post with a Feed Element,
but this example instantiates the action link group from a template.

Step 1: Create the Action Link Templates

**1.** From Setup, enter _`Action Link Templates`_ in the `Quick Find` box, then select **Action Link Templates** .

**2.** Use these values in a new Action Link Group Template:

**3.** Use these values in a new Action Link Template:


Apex Developer Guide Using Salesforce Features with Apex

**4.** Go back to the Action Link Group Template and select `Published` . Click **Save** .

Step 2: Instantiate the Action Link Group, Associate it with a Feed Item, and Post it

This example calls `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`
`[actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` to create an action link group definition.

It calls `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to associate the action
link group with a feed item and post it.

```
// Get the action link group template Id.

ActionLinkGroupTemplate template = [SELECT Id FROM ActionLinkGroupTemplate WHERE

DeveloperName='Doc_Example'];

// Add binding name-value pairs to a map.

// The names are defined in the action link template(s) associated with the action link

group template.

// Get them from Setup UI or SOQL.

Map<String, String> bindingMap = new Map<String, String>();

bindingMap.put('ApiVersion', 'v33.0');

bindingMap.put('Text', 'This post was created by an API action link.');

bindingMap.put('SubjectId', 'me');

// Create ActionLinkTemplateBindingInput objects from the map elements.

List<ConnectApi.ActionLinkTemplateBindingInput> bindingInputs = new

List<ConnectApi.ActionLinkTemplateBindingInput>();

for (String key : bindingMap.keySet()) {

   ConnectApi.ActionLinkTemplateBindingInput bindingInput = new

ConnectApi.ActionLinkTemplateBindingInput();

   bindingInput.key = key;

   bindingInput.value = bindingMap.get(key);

   bindingInputs.add(bindingInput);

}

// Set the template Id and template binding values in the action link group definition.

ConnectApi.ActionLinkGroupDefinitionInput actionLinkGroupDefinitionInput = new

ConnectApi.ActionLinkGroupDefinitionInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   actionLinkGroupDefinitionInput.templateId = template.id;

   actionLinkGroupDefinitionInput.templateBindings = bindingInputs;

   // Instantiate the action link group definition.

   ConnectApi.ActionLinkGroupDefinition actionLinkGroupDefinition =

    ConnectApi.ActionLinks.createActionLinkGroupDefinition(Network.getNetworkId(),

   actionLinkGroupDefinitionInput);

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   ConnectApi.AssociatedActionsCapabilityInput associatedActionsCapabilityInput = new

   ConnectApi.AssociatedActionsCapabilityInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   // Define the FeedItemInput object to pass to postFeedElement

   feedItemInput.body = messageBodyInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   feedItemInput.subjectId = 'me';

   // The MessageBodyInput object holds the text in the post

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Click to post a feed item.';

   messageBodyInput.messageSegments.add(textSegmentInput);

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define an associated actions capability to hold the action link

    group.

   // The action link group ID is returned from the call to create the action link group

   definition.

   feedElementCapabilitiesInput.associatedActions = associatedActionsCapabilityInput;

   associatedActionsCapabilityInput.actionLinkGroupIds = new List<String>();

   associatedActionsCapabilityInput.actionLinkGroupIds.add(actionLinkGroupDefinition.id);

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

###### Edit a Feed Element

```

Call a method to edit a feed element.

Call `[updateFeedElement(communityId, feedElementId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElement)` to edit a feed element. Feed items are
the only type of feed element that can be edited.

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited post.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

###### Edit a Question Title and Post

```

Call a method to edit a question title and post.

Call `[updateFeedElement(communityId, feedElementId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElement)` to edit a question title and post.

```
   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isFeedElementEditableByMe(communityId, feedElementId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

      ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

      ConnectApi.QuestionAndAnswersCapabilityInput questionAndAnswersCapabilityInput = new

   ConnectApi.QuestionAndAnswersCapabilityInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

```


Apex Developer Guide Using Salesforce Features with Apex

```
      textSegmentInput.text = 'This is my edited question.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      feedItemInput.body = messageBodyInput;

      feedItemInput.capabilities = feedElementCapabilitiesInput;

      feedElementCapabilitiesInput.questionAndAnswers = questionAndAnswersCapabilityInput;

      questionAndAnswersCapabilityInput.questionTitle = 'Where is my edited question?';

      ConnectApi.FeedElement editedFeedElement =

   ConnectApi.ChatterFeeds.updateFeedElement(communityId, feedElementId, feedItemInput);

   }

###### Like a Feed Element

```

Call a method to like a feed element.

Call `[likeFeedElement(communityId, feedElementId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_likeFeedElement)` to like a feed element.

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

###### Bookmark a Feed Element

```

Call a method to bookmark a feed element.

Call `[updateFeedElementBookmarks(communityId, feedElementId, isBookmarkedByCurrentUser)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElementBookmarks_2)` to
bookmark a feed element.

```
   ConnectApi.BookmarksCapability bookmark =

   ConnectApi.ChatterFeeds.updateFeedElementBookmarks(null, '0D5D0000000KuGh', true);

###### Share a Feed Element (prior to Version 39.0)

```

Call a method to share a feed element.

Important: In API version 39.0 and later, `shareFeedElement(communityId, subjectId, feedElementType,`
`originalFeedElementId)` isn’t supported. See Share a Feed Element (in Version 39.0 and Later).

Call `[shareFeedElement(communityId, subjectId, feedElementType, originalFeedElementId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_shareFeedElement)` to
share a feed item (which is a type of feed element) with a group.

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

###### Share a Feed Element (in Version 39.0 and Later)

```

Call a method to share a feed element.

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to share a feed element.

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

```


Apex Developer Guide Using Salesforce Features with Apex

```
   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Look at this post I'm sharing.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   ConnectApi.FeedEntityShareCapabilityInput shareInput = new

   ConnectApi.FeedEntityShareCapabilityInput();

   shareInput.feedEntityId = '0D5R0000000SEbc';

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.feedEntityShare = shareInput;

   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

###### Send a Direct Message

```

Call a method to send a direct message.

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to send a direct message to two people.

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Thanks for attending my presentation test run this morning. Send

    me any feedback.';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

   // For this feed item, we define a direct message capability to hold the member(s) and the

    subject.

   List<String> memberIds = new List<String>();

   memberIds.add('005B00000016OUQ');

   memberIds.add('005B0000001rIN6');

   ConnectApi.DirectMessageCapabilityInput dmInput = new

   ConnectApi.DirectMessageCapabilityInput();

   dmInput.subject = 'Thank you!';

   dmInput.membersToAdd = memberIds;

   ConnectApi.FeedElementCapabilitiesInput feedElementCapabilitiesInput = new

   ConnectApi.FeedElementCapabilitiesInput();

   feedElementCapabilitiesInput.directMessage = dmInput;

```


Apex Developer Guide Using Salesforce Features with Apex

```
   feedItemInput.capabilities = feedElementCapabilitiesInput;

   // Post the feed item.

   ConnectApi.FeedElement feedElement =

   ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

###### Post a Comment

```

Call a method to post a comment.

Call `[postCommentToFeedElement(communityId, feedElementId, text)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_1)` to post a plain text comment to a feed
element.

```
   ConnectApi.Comment comment = ConnectApi.ChatterFeeds.postCommentToFeedElement(null,

   '0D5D0000000KuGh', 'I agree with the proposal.' );

###### Post a Comment with a Mention

```

Make call or use the ConnectApiHelper repository to post a comment with a mention.

[You can post comments with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or use](https://github.com/forcedotcom/ConnectApiHelper)
this example, which calls `[postCommentToFeedElement(communityId, feedElementId, comment,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` .

```
   String communityId = null;

   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   textSegmentInput.text = 'Does anyone in this group have an idea? ';

   messageBodyInput.messageSegments.add(textSegmentInput);

   mentionSegmentInput.id = '005D00000000oOT';

   messageBodyInput.messageSegments.add(mentionSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.Comment commentRep = ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId,

    feedElementId, commentInput, null);

###### Post a Comment with an Existing File

```

Make a call to post a comment with an already uploaded file.


Apex Developer Guide Using Salesforce Features with Apex

To post a comment and attach an existing file (already uploaded to Salesforce) to the comment, create a
`ConnectApi.CommentInput` object to pass to `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` .

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'I attached this file from Salesforce Files.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.contentDocumentId = '069D00000001rNJ';

   commentInput.capabilities = commentCapabilitiesInput;

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, null);

###### Post a Comment with a New File

```

Call a method to post a comment with a new file.

To post a comment and upload and attach a new file to the comment, create a `ConnectApi.CommentInput` object and a
`ConnectApi.BinaryInput` object to pass to the `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` method.

```
   String feedElementId = '0D5D0000000KtW3';

   ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Enjoy this new file.';

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   commentInput.body = messageBodyInput;

   ConnectApi.CommentCapabilitiesInput commentCapabilitiesInput = new

   ConnectApi.CommentCapabilitiesInput();

```


Apex Developer Guide Using Salesforce Features with Apex

```
   ConnectApi.ContentCapabilityInput contentCapabilityInput = new

   ConnectApi.ContentCapabilityInput();

   commentCapabilitiesInput.content = contentCapabilityInput;

   contentCapabilityInput.title = 'Title';

   commentInput.capabilities = commentCapabilitiesInput;

   String text = 'These are the contents of the new file.';

   Blob myBlob = Blob.valueOf(text);

   ConnectApi.BinaryInput binInput = new ConnectApi.BinaryInput(myBlob, 'text/plain',

   'fileName');

   ConnectApi.Comment commentRep =

   ConnectApi.ChatterFeeds.postCommentToFeedElement(Network.getNetworkId(), feedElementId,

   commentInput, binInput);

###### Post a Rich-Text Comment with Inline Image

```

Make a call or use the ConnectApiHelper repository to post a comment with an already uploaded, inline image.

[You can post rich-text comments with inline images and mentions two ways. Use the ConnectApiHelper repository on GitHub to write](https://github.com/forcedotcom/ConnectApiHelper)
a single line of code, or use this example, which calls `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` . In this example, the image file is existing content that has already been uploaded to
Salesforce.

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String imageId = '069R00000000IgQ';

   String mentionedUserId = '005R0000000DiMz';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = 'Hello ';

   messageInput.messageSegments.add(textSegment);

   mentionSegment = new ConnectApi.MentionSegmentInput();

   mentionSegment.id = mentionedUserId;

   messageInput.messageSegments.add(mentionSegment);

```


Apex Developer Guide Using Salesforce Features with Apex

```
   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = '!';

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Bold;

   messageInput.messageSegments.add(markupEndSegment);

   inlineImageSegment = new ConnectApi.InlineImageSegmentInput();

   inlineImageSegment.altText = 'image one';

   inlineImageSegment.fileId = imageId;

   messageInput.messageSegments.add(inlineImageSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

###### Post a Rich-Text Feed Comment with a Code Block

```

Call a method to post a comment with a code block.

This example calls `[postCommentToFeedElement(communityId, feedElementId, comment,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` to post a comment with a code block.

```
   String communityId = null;

   String feedElementId = '0D5R0000000SBEr';

   String codeSnippet = '<html>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>';

   ConnectApi.CommentInput input = new ConnectApi.CommentInput();

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   markupBeginSegment = new ConnectApi.MarkupBeginSegmentInput();

   markupBeginSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupBeginSegment);

   textSegment = new ConnectApi.TextSegmentInput();

   textSegment.text = codeSnippet;

   messageInput.messageSegments.add(textSegment);

   markupEndSegment = new ConnectApi.MarkupEndSegmentInput();

   markupEndSegment.markupType = ConnectApi.MarkupType.Code;

   messageInput.messageSegments.add(markupEndSegment);

   input.body = messageInput;

   ConnectApi.ChatterFeeds.postCommentToFeedElement(communityId, feedElementId, input, null);

```


Apex Developer Guide Using Salesforce Features with Apex

###### Edit a Comment

Call a method to edit a comment.

Call `[updateComment(communityId, commentId, comment)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateComment)` to edit a comment.

```
   String commentId;

   String communityId = Network.getNetworkId();

   // Get the last feed item created by the context user.

   List<FeedItem> feedItems = [SELECT Id FROM FeedItem WHERE CreatedById = :UserInfo.getUserId()

    ORDER BY CreatedDate DESC];

   if (feedItems.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   String feedElementId = feedItems[0].id;

   ConnectApi.CommentPage commentPage =

   ConnectApi.ChatterFeeds.getCommentsForFeedElement(communityId, feedElementId);

   if (commentPage.items.isEmpty()) {

      // Return null within anonymous apex.

      return null;

   }

   commentId = commentPage.items[0].id;

   ConnectApi.FeedEntityIsEditable isEditable =

   ConnectApi.ChatterFeeds.isCommentEditableByMe(communityId, commentId);

   if (isEditable.isEditableByMe == true){

      ConnectApi.CommentInput commentInput = new ConnectApi.CommentInput();

      ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

      ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

      messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

      textSegmentInput.text = 'This is my edited comment.';

      messageBodyInput.messageSegments.add(textSegmentInput);

      commentInput.body = messageBodyInput;

      ConnectApi.Comment editedComment = ConnectApi.ChatterFeeds.updateComment(communityId,

    commentId, commentInput);

   }

###### Follow a Record

```

Call a method to follow a record.


Apex Developer Guide Using Salesforce Features with Apex

Call `[follow(communityId, userId, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_follow)` to follow a record.

```
   ChatterUsers.ConnectApi.Subscription subscriptionToRecord =

   ConnectApi.ChatterUsers.follow(null, 'me', '001RR000002G4Y0');

```

SEE ALSO:

###### Unfollow a Record Unfollow a Record

Call a method to stop following a record.

When you follow a record such as a user, the call to `ConnectApi.ChatterUsers.follow` returns a
`ConnectApi.Subscription` object. To unfollow a record, pass the `id` property of that object to
`[deleteSubscription(communityId, subscriptionId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Chatter_static_methods.htm#apex_ConnectAPI_Chatter_deleteSubscription)` .

```
   ConnectApi.Chatter.deleteSubscription(null, '0E8RR0000004CnK0AU');

```

SEE ALSO:

Follow a Record

###### Get a Repository

Call a method to get a repository.

Call `[getRepository(repositoryId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepository_1)` to get a repository.

```
   final string repositoryId = '0XCxx0000000123GAA';

   final ConnectApi.ContentHubRepository repository =

   ConnectApi.ContentHub.getRepository(repositoryId);

###### Get Repositories

```

Call a method to get all repositories.

Call `[getRepositories()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositories_1)` to get all repositories and get the first SharePoint online repository found.

```
   final string sharePointOnlineProviderType ='ContentHubSharepointOffice365';

   final ConnectApi.ContentHubRepositoryCollection repositoryCollection =

   ConnectApi.ContentHub.getRepositories();

   ConnectApi.ContentHubRepository sharePointOnlineRepository = null;

   for(ConnectApi.ContentHubRepository repository : repositoryCollection.repositories){

     if(sharePointOnlineProviderType.equalsIgnoreCase(repository.providerType.type)){

       sharePointOnlineRepository = repository;

       break;

     }

   }

###### Get Allowed Item Types

```

Call a method to get allowed item types.


Apex Developer Guide Using Salesforce Features with Apex

Call `[getAllowedItemTypes(repositoryId, repositoryFolderId, filter)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getAllowedItemTypes_2)` with a `filter` of `FilesOnly`
to get the first `ConnectApi.ContentHubItemTypeSummary.id` of a file. The context user can create allowed files in a
repository folder in the external system.

```
   final ConnectApi.ContentHubAllowedItemTypeCollection allowedItemTypesColl =

   ConnectApi.ContentHub.getAllowedItemTypes(repositoryId, repositoryFolderId,

   ConnectApi.ContentHubItemType.FilesOnly);

   final List<ConnectApi.ContentHubItemTypeSummary> allowedItemTypes =

   allowedItemTypesColl.allowedItemTypes;

   string allowedFileItemTypeId = null;

   if(allowedItemTypes.size() > 0){

     ConnectApi.ContentHubItemTypeSummary allowedItemTypeSummary = allowedItemTypes.get(0);

     allowedFileItemTypeId = allowedItemTypeSummary.id;

   }

###### Get Previews

```

Call a method to get all supported preview formats and their respective URLs.

Call `[getPreviews(repositoryId, repositoryFileId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getPreviews_1)` to get all supported preview formats and their respective URLs
and number of renditions. For each supported preview format, we show every rendition URL available.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'document:1-zcA1BaeoQbo2_yNFiHCcK6QJTPmOke-kHFC4TYg3rk';

   final ConnectApi.FilePreviewCollection previewsCollection =

   ConnectApi.ContentHub.getPreviews(gDriveRepositoryId, gDriveFileId);

   for(ConnectApi.FilePreview filePreview : previewsCollection.previews){

     System.debug(String.format('Preview - URL: \'\'{0}\'\', format: \'\'{1}\'\', nbr of

   renditions for this format: {2}', new String[]{ filePreview.url,

   filePreview.format.name(),String.valueOf(filePreview.previewUrls.size())}));

     for(ConnectApi.FilePreviewUrl filePreviewUrl : filePreview.previewUrls){

       System.debug('-----> Rendition URL: ' + filePreviewUrl.previewUrl);

       }

   }

###### Get a File Preview

```

Call a method to get a file preview.

Call `[getFilePreview(repositoryId, repositoryFileId, formatType)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getFilePreview_1)` with a `formatType` of `Thumbnail`
to get the thumbnail format preview along with its respective URL and number of thumbnail renditions. For each thumbnail format, we
show every rendition URL available.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'document:1-zcA1BaeoQbo2_yNFiHCcK6QJTPmOke-kHFC4TYg3rk';

   final ConnectApi.FilePreviewCollection previewsCollection =

   ConnectApi.ContentHub.getPreviews(gDriveRepositoryId, gDriveFileId);

   for(ConnectApi.FilePreview filePreview : previewsCollection.previews){

     System.debug(String.format('Preview - URL: \'\'{0}\'\', format: \'\'{1}\'\', nbr of

   renditions for this format: {2}', new String[]{ filePreview.url,

   filePreview.format.name(),String.valueOf(filePreview.previewUrls.size())}));

     for(ConnectApi.FilePreviewUrl filePreviewUrl : filePreview.previewUrls){

       System.debug('-----> Rendition URL: ' + filePreviewUrl.previewUrl);

```


Apex Developer Guide Using Salesforce Features with Apex

```
       }

   }

###### Get Repository Folder Items

```

Call a method to get a collection of repository folder items.

Call `[getRepositoryFolderItems(repositoryId, repositoryFolderId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFolderItems_1)` to get the collection of items in a
repository folder. For files, we show the file’s name, size, external URL, and download URL. For folders, we show the folder’s name,
description, and external URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.RepositoryFolderItemsCollection folderItemsColl =

   ConnectApi.ContentHub.getRepositoryFolderItems(gDriveRepositoryId,gDriveFolderId);

   final List<ConnectApi.RepositoryFolderItem> folderItems = folderItemsColl.items;

   System.debug('Number of items in repository folder: ' + folderItems.size());

   for(ConnectApi.RepositoryFolderItem item : folderItems){

     ConnectApi.RepositoryFileSummary fileSummary = item.file;

     if(fileSummary != null){

       System.debug(String.format('File item - name: \'\'{0}\'\', size: {1}, external URL:

    \'\'{2}\'\', download URL: \'\'{3}\'\'', new String[]{ fileSummary.name,

   String.valueOf(fileSummary.contentSize), fileSummary.externalDocumentUrl,

   fileSummary.downloadUrl}));

       }else{

         ConnectApi.RepositoryFolderSummary folderSummary = item.folder;

         System.debug(String.format('Folder item - name: \'\'{0}\'\', description:

   \'\'{1}\'\'', new String[]{ folderSummary.name, folderSummary.description}));

       }

   }

###### Get a Repository Folder

```

Call a method to get a repository folder.

Call `[getRepositoryFolder(repositoryId, repositoryFolderId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFolder_3)` to get a repository folder.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.RepositoryFolderDetail folder =

   ConnectApi.ContentHub.getRepositoryFolder(gDriveRepositoryId, gDriveFolderId);

   System.debug(String.format('Folder - name: \'\'{0}\'\', description: \'\'{1}\'\', external

    URL: \'\'{2}\'\', folder items URL: \'\'{3}\'\'',

     new String[]{ folder.name, folder.description, folder.externalFolderUrl,

   folder.folderItemsUrl}));

###### Get a Repository File Without Permissions Information

```

Call a method to get a repository file without permission information.

Call `[getRepositoryFile(repositoryId, repositoryFileId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFile_3)` to get a repository file without permissions information.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'file:0B0lTys1KmM3sTmxKNjVJbWZja00';

   final ConnectApi.RepositoryFileDetail file =

```


Apex Developer Guide Using Salesforce Features with Apex

```
   ConnectApi.ContentHub.getRepositoryFile(gDriveRepositoryId, gDriveFileId);

   System.debug(String.format('File - name: \'\'{0}\'\', size: {1}, external URL: \'\'{2}\'\',

    download URL: \'\'{3}\'\'',

     new String[]{ file.name, String.valueOf(file.contentSize), file.externalDocumentUrl,

   file.downloadUrl}));

###### Get a Repository File with Permissions Information

```

Call a method to get a repository file with permission information.

Call `[getRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFile_4)`
to get a repository file with permissions information.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFileId =

   'file:0B0lTys1KmM3sTmxKNjVJbWZja00';

   final ConnectApi.RepositoryFileDetail file =

   ConnectApi.ContentHub.getRepositoryFile(gDriveRepositoryId, gDriveFileId, true);

   System.debug(String.format('File - name: \'\'{0}\'\', size: {1}, external URL: \'\'{2}\'\',

    download URL: \'\'{3}\'\'', new String[]{ file.name, String.valueOf(file.contentSize),

   file.externalDocumentUrl, file.downloadUrl}));

   final ConnectApi.ExternalFilePermissionInformation externalFilePermInfo =

   file.externalFilePermissionInformation;

   //permission types

   final List<ConnectApi.ContentHubPermissionType> permissionTypes =

   externalFilePermInfo.externalFilePermissionTypes;

   for(ConnectApi.ContentHubPermissionType permissionType : permissionTypes){

     System.debug(String.format('Permission type - id: \'\'{0}\'\', label: \'\'{1}\'\'', new

    String[]{ permissionType.id, permissionType.label}));

   }

   //permission groups

   final List<ConnectApi.RepositoryGroupSummary> groups =

   externalFilePermInfo.repositoryPublicGroups;

   for(ConnectApi.RepositoryGroupSummary ggroup : groups){

     System.debug(String.format('Group - id: \'\'{0}\'\', name: \'\'{1}\'\', type:

   \'\'{2}\'\'', new String[]{ ggroup.id, ggroup.name, ggroup.type.name()}));

   }

###### Create a Repository File Without Content (Metadata Only)

```

Call a method to create a file without binary content (metadata only) in a Google Drive repository folder.

Call `[addRepositoryItem(repositoryId, repositoryFolderId, file)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_addRepositoryItem_5)` to create a file without binary content
(metadata only) in a Google Drive repository folder. After the file is created, we show the file’s ID, name, description, external URL, and
download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.ContentHubItemInput newItem = new ConnectApi.ContentHubItemInput();

   newItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

   for creation/update

```


Apex Developer Guide Using Salesforce Features with Apex

```
   newItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   final ConnectApi.ContentHubFieldValueInput fieldValueInput = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInput.name = 'name';

   fieldValueInput.value = 'new folder item name.txt';

   newItem.fields.add(fieldValueInput);

   //Metadata: description field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputDesc = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputDesc.name = 'description';

   fieldValueInputDesc.value = 'It does describe it';

   newItem.fields.add(fieldValueInputDesc);

   final ConnectApi.RepositoryFolderItem newFolderItem =

   ConnectApi.ContentHub.addRepositoryItem(gDriveRepositoryId, gDriveFolderId, newItem);

   final ConnectApi.RepositoryFileSummary newFile = newFolderItem.file;

   System.debug(String.format('New file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

   \'\'{2}\'\' \n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   newFile.id, newFile.name, newFile.description, newFile.externalDocumentUrl,

   newFile.downloadUrl}));

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

###### Create a Repository File with Content

Call a method to create a file with binary content in a Google Drive repository folder.

Call `[addRepositoryItem(repositoryId, repositoryFolderId, file, filedata)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_addRepositoryItem_7)` to create a file with binary
content in a Google Drive repository folder. After the file is created, we show the file’s ID, name, description, external URL, and download
URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs';

   final ConnectApi.ContentHubItemInput newItem = new ConnectApi.ContentHubItemInput();

   newItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

   for creation/update

   newItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   Final String newFileName = 'new folder item name.txt';

   final ConnectApi.ContentHubFieldValueInput fieldValueInput = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInput.name = 'name';

   fieldValueInput.value = newFileName;

   newItem.fields.add(fieldValueInput);

   //Metadata: description field

```


Apex Developer Guide Using Salesforce Features with Apex

```
   final ConnectApi.ContentHubFieldValueInput fieldValueInputDesc = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputDesc.name = 'description';

   fieldValueInputDesc.value = 'It does describe it';

   newItem.fields.add(fieldValueInputDesc);

   //Binary content

   final Blob newFileBlob = Blob.valueOf('awesome content for brand new file');

   final String newFileMimeType = 'text/plain';

   final ConnectApi.BinaryInput fileBinaryInput = new ConnectApi.BinaryInput(newFileBlob,

   newFileMimeType, newFileName);

   final ConnectApi.RepositoryFolderItem newFolderItem =

   ConnectApi.ContentHub.addRepositoryItem(gDriveRepositoryId, gDriveFolderId, newItem,

   fileBinaryInput);

   final ConnectApi.RepositoryFileSummary newFile = newFolderItem.file;

   System.debug(String.format('New file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

   \'\'{2}\'\' \n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   newFile.id, newFile.name, newFile.description, newFile.externalDocumentUrl,

   newFile.downloadUrl}));

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

_Apex Reference Guide_ [: ConnectApi.BinaryInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_binary.htm)

###### Update a Repository File Without Content (Metadata Only)

Call a method to update the metadata of a repository file.

Call `[updateRepositoryFile(repositoryId, repositoryFileId, file)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_updateRepositoryFile_7)` to update the metadata of a file in a
repository folder. After the file is updated, we show the file’s ID, name, description, external URL, download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs', gDriveFileId =

   'document:1q9OatVpcyYBK-JWzp_PhR75ulQghwFP15zhkamKrRcQ';

   final ConnectApi.ContentHubItemInput updatedItem = new ConnectApi.ContentHubItemInput();

   updatedItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

    for creation/update

   updatedItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputName = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputName.name = 'name';

   fieldValueInputName.value = 'updated file name.txt';

   updatedItem.fields.add(fieldValueInputName);

   final ConnectApi.RepositoryFileDetail updatedFile =

   ConnectApi.ContentHub.updateRepositoryFile(gDriveRepositoryId, gDriveFileId, updatedItem);

   System.debug(String.format('Updated file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

    \'\'{2}\'\',\n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

```


Apex Developer Guide Using Salesforce Features with Apex

```
   updatedFile.id, updatedFile.name, updatedFile.description, updatedFile.externalDocumentUrl,

    updatedFile.downloadUrl}));

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

###### Update a Repository File with Content

Call a method to update a repository file with content.

Call `[updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_updateRepositoryFile_8)` to update the content
and metadata of a file in a repository. After the file is updated, we show the file’s ID, name, description, external URL, and download URL.

```
   final String gDriveRepositoryId = '0XCxx00000000ODGAY', gDriveFolderId =

   'folder:0B0lTys1KmM3sSVJ2bjIzTGFqSWs', gDriveFileId =

   'document:1q9OatVpcyYBK-JWzp_PhR75ulQghwFP15zhkamKrRcQ';

   final ConnectApi.ContentHubItemInput updatedItem = new ConnectApi.ContentHubItemInput();

   updatedItem.itemTypeId = 'document'; //see getAllowedTypes for any file item types available

    for creation/update

   updatedItem.fields = new List<ConnectApi.ContentHubFieldValueInput>();

   //Metadata: name field

   final ConnectApi.ContentHubFieldValueInput fieldValueInputName = new

   ConnectApi.ContentHubFieldValueInput();

   fieldValueInputName.name = 'name';

   fieldValueInputName.value = 'updated file name.txt';

   updatedItem.fields.add(fieldValueInputName);

   //Binary content

   final Blob updatedFileBlob = Blob.valueOf('even more awesome content for updated file');

   final String updatedFileMimeType = 'text/plain';

   final ConnectApi.BinaryInput fileBinaryInput = new ConnectApi.BinaryInput(updatedFileBlob,

    updatedFileMimeType, updatedFileName);

   final ConnectApi.RepositoryFileDetail updatedFile =

   ConnectApi.ContentHub.updateRepositoryFile(gDriveRepositoryId, gDriveFileId, updatedItem);

   System.debug(String.format('Updated file - id: \'\'{0}\'\', name: \'\'{1}\'\', description:

    \'\'{2}\'\',\n external URL: \'\'{3}\'\', download URL: \'\'{4}\'\'', new String[]{

   updatedFile.id, updatedFile.name, updatedFile.description, updatedFile.externalDocumentUrl,

    updatedFile.downloadUrl}));

```

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

_Apex Reference Guide_ [: ConnectApi.BinaryInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_binary.htm)

###### Get an Authentication URL

Call a method to get an authentication URL.


Apex Developer Guide Using Salesforce Features with Apex

Call `[getOAuthCredentialAuthUrl(requestBody)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_NamedCredentials_static_methods.htm#apex_ConnectAPI_NamedCredentials_getOAuthCredentialAuthUrl_1)` to retrieve the URL that a user must visit to begin an authentication
flow, ultimately returning authentication tokens to Salesforce. Accepts input parameters representing a specific external credential and,
optionally, a named principal. Use this method as part of building a customized or branded user interface to help users initiate
authentication.

```
   ConnectApi.OAuthCredentialAuthUrlInput input = new ConnectApi.OAuthCredentialAuthUrlInput();

   input.externalCredential = 'MyExternalCredentialDeveloperName';

   input.principalType = ConnectApi.CredentialPrincipalType.PerUserPrincipal;

   input.principalName = 'MyPrincipal'; // Only required when principalType = NamedPrincipal

   ConnectApi.OAuthCredentialAuthUrl output =

   ConnectApi.NamedCredentials.getOAuthCredentialAuthUrl(input);

   String authenticationUrl = output.authenticationUrl; // Redirect users to this URL to

   authenticate in the browser

```

SEE ALSO:

_Apex Reference Guide_ [: NamedCredentials Methods](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_NamedCredentials_static_methods.htm)

###### Resolve a Prompt Template

Call a method to resolve a prompt template.

Call `[generateMessagesForPromptTemplate(promptTemplateDevName,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_EinsteinLLM_static_methods.htm)`
`[promptTemplateGenerationsInput)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_EinsteinLLM_static_methods.htm)` to resolve a prompt template.

To resolve a prompt template, create an input object, build input maps, configure additional settings, call the service, and handle the
resolution and response.

To create an input object, create an instance of `ConnectApi.EinsteinPromptTemplateGenerationsInput` .

To store input parameters for the prompt template, build input maps using `Map<String, ConnectApi.WrappedValue>` .
Wrap the input maps in `ConnectApi.WrappedValue` and add them to a `ConnectApi.WrappedValue` map with identifying
keys. You can also wrap a string input in `ConnectApi.WrappedValue` and add it to a map.

To configure additional settings, create an instance of `ConnectApi.EinsteinLlmAdditionalConfigInput` and assign
it to the `additionalConfig` property of the input object.

To generate messages based on the prompt template and input parameters, call the `generateMessagesForPromptTemplate`
method of the `ConnectApi.EinsteinLLM` class with the prompt template ID and the input object.

To access the prompt resolution, use `generationsOutput.prompt` and, to access the first generated response, use
`generationsOutput.generations[0].text` .

Resolve a Flex Prompt Template with Apex and Flow Resources

```
   // Create input

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptGenerationsInput = new

   ConnectApi.EinsteinPromptTemplateGenerationsInput();

   promptGenerationsInput.isPreview = false;

   // Build input map

   Map<String,ConnectApi.WrappedValue> valueMap = new

```


Apex Developer Guide Using Salesforce Features with Apex

```
   Map<String,ConnectApi.WrappedValue>();

   Map<String, String> account1RecordIdMap = new Map<String, String>();

   account1RecordIdMap.put('id', '001xx000003H9cuAAC'); // Account ID

   Map<String, String> account2RecordIdMap = new Map<String, String>();

   account2RecordIdMap.put('id', '001xx000003H9ctAAC'); // Account ID

   Map<String, String> case1RecordIdMap = new Map<String, String>();

   case1RecordIdMap.put('id', '500xx000000cJ7rAAE'); // Case ID

   // Add wrapped values to map

   ConnectApi.WrappedValue account1WrappedValue = new ConnectApi.WrappedValue();

   account1WrappedValue.value = account1RecordIdMap;

   ConnectApi.WrappedValue account2WrappedValue = new ConnectApi.WrappedValue();

   account2WrappedValue.value = account2RecordIdMap;

   ConnectApi.WrappedValue case1WrappedValue = new ConnectApi.WrappedValue();

   case1WrappedValue.value = case1RecordIdMap;

   valueMap.put('Input:Account_1', account1WrappedValue);

   valueMap.put('Input:Account_2', account2WrappedValue);

   valueMap.put('Input:Case_1', case1WrappedValue);

   // Add string input

   ConnectApi.WrappedValue strWrappedValue = new ConnectApi.WrappedValue();

   strWrappedValue.value = 'My string input';

   valueMap.put('Input:My_Free_Text1', strWrappedValue);

   promptGenerationsInput.inputParams = valueMap;

   // Set additional configuration values

   promptGenerationsInput.additionalConfig = new ConnectApi.EinsteinLlmAdditionalConfigInput();

   promptGenerationsInput.additionalConfig.applicationName =

   'PromptTemplateGenerationsInvocable';

   // Call the service using the prompt template ID

   ConnectApi.EinsteinPromptTemplateGenerationsRepresentation generationsOutput =

   ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate('0hfxx0000000KQ9AAM',

   promptGenerationsInput);

   // Consume resolution

   System.debug('Prompt resolution: ' + generationsOutput.prompt);

   // Consume response

   System.debug('Prompt response: ' + generationsOutput.generations[0].text);

```

Resolve a Sales Email Prompt Template

```
   // Create input

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptGenerationsInput = new

```


Apex Developer Guide Using Salesforce Features with Apex

```
   ConnectApi.EinsteinPromptTemplateGenerationsInput();

   promptGenerationsInput.isPreview = false;

   // Build input map

   Map<String,ConnectApi.WrappedValue> valueMap = new Map<String,ConnectApi.WrappedValue>();

   Map<String, String> recipientEntityRecordIdMap = new Map<String, String>();

   recipientEntityRecordIdMap.put('id', '00Qxx000002ToPvEAK');

   Map<String, String> senderEntityRecordIdMap = new Map<String, String>();

   senderEntityRecordIdMap.put('id', '005xx000001XiWLAA0');

   ConnectApi.WrappedValue recipientEntityWrappedValue = new ConnectApi.WrappedValue();

   recipientEntityWrappedValue.value = recipientEntityRecordIdMap;

   ConnectApi.WrappedValue senderEntityWrappedValue = new ConnectApi.WrappedValue();

   senderEntityWrappedValue.value = senderEntityRecordIdMap;

   valueMap.put('Input:Account', recipientEntityWrappedValue);

   valueMap.put('Input:Recipient', recipientEntityWrappedValue);

   valueMap.put('Input:Sender', senderEntityWrappedValue);

   promptGenerationsInput.inputParams = valueMap;

   // Set additional configuration values

   promptGenerationsInput.additionalConfig = new ConnectApi.EinsteinLlmAdditionalConfigInput();

   promptGenerationsInput.additionalConfig.applicationName =

   'PromptTemplateGenerationsInvocable';

   // Call the service

   ConnectApi.EinsteinPromptTemplateGenerationsRepresentation generationsOutput =

   ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate('0hfxx0000000KTNAA2',

   promptGenerationsInput);

   // Consume response

   System.debug('Prompt Testing: ' + generationsOutput.prompt);

```

Resolve a Field Generation Prompt Template

```
   // Create input

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptGenerationsInput = new

   ConnectApi.EinsteinPromptTemplateGenerationsInput();

   promptGenerationsInput.isPreview = false;

   // Build input map

   Map<String,ConnectApi.WrappedValue> valueMap = new Map<String,ConnectApi.WrappedValue>();

   Map<String, String> relatedEntityRecordIdMap = new Map<String, String>();

   relatedEntityRecordIdMap.put('id', '001xx000003H9cuAAC');

   ConnectApi.WrappedValue relatedEntityWrappedValue = new ConnectApi.WrappedValue();

   relatedEntityWrappedValue.value = relatedEntityRecordIdMap;

   valueMap.put('Input:Account', relatedEntityWrappedValue);

```


Apex Developer Guide Using Salesforce Features with Apex

```
   promptGenerationsInput.inputParams = valueMap;

   // Set additional configuration values

   promptGenerationsInput.additionalConfig = new ConnectApi.EinsteinLlmAdditionalConfigInput();

   promptGenerationsInput.additionalConfig.applicationName =

   'PromptTemplateGenerationsInvocable';

   // Call the service

   ConnectApi.EinsteinPromptTemplateGenerationsRepresentation generationsOutput =

   ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate('0hfxx0000000KRlAAM',

   promptGenerationsInput);

   // Consume response

   System.debug('Prompt Testing: ' + generationsOutput.prompt);

```

Resolve a Summary Prompt Template

```
   // Create input

   ConnectApi.EinsteinPromptTemplateGenerationsInput promptGenerationsInput = new

   ConnectApi.EinsteinPromptTemplateGenerationsInput();

   promptGenerationsInput.isPreview = false;

   // Build input map

   Map<String,ConnectApi.WrappedValue> valueMap = new Map<String,ConnectApi.WrappedValue>();

   Map<String, String> recipientEntityRecordIdMap = new Map<String, String>();

   recipientEntityRecordIdMap.put('id', '00Qxx000002ToPvEAK');

   ConnectApi.WrappedValue recipientEntityWrappedValue = new ConnectApi.WrappedValue();

   recipientEntityWrappedValue.value = recipientEntityRecordIdMap;

   valueMap.put('Input:Account', recipientEntityWrappedValue);

   promptGenerationsInput.inputParams = valueMap;

   // Set additional configuration values

   promptGenerationsInput.additionalConfig = new ConnectApi.EinsteinLlmAdditionalConfigInput();

   promptGenerationsInput.additionalConfig.applicationName =

   'PromptTemplateGenerationsInvocable';

   // Call the service

   ConnectApi.EinsteinPromptTemplateGenerationsRepresentation generationsOutput =

   ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate('0hfxx0000000KUzAAM',

   promptGenerationsInput);

   // Consume response

   System.debug('Prompt Testing: ' + generationsOutput.prompt);

###### Create a Cart and Cart Item with Custom Fields in a Commerce Store

```

Create a cart with a cart item using custom fields for a buyer or guest user in your Commerce store.


Apex Developer Guide Using Salesforce Features with Apex

[Custom fields are optional and must be previously defined for the WebCart and CartItem sObjects. See Create Custom Fields. Field-level](https://help.salesforce.com/s/articleView?id=platform.adding_fields.htm&type=5&language=en_US)
[security rules from the shopper profile are applied to the WebCart and CartItem custom fields. The rules are applied for registered](https://help.salesforce.com/s/articleView?id=commerce.comm_create_shopper_profile.htm&type=5&language=en_US)
shoppers and for the guest shopper profile.

To create a cart with custom fields, call `[createCart(webstoreId, cartInput)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_createCart_1)` . Specify your custom fields using the
`customFields` property of `cartInput` . The type for `customFields` is `List<SObject>`, where the sObject is a WebCart.

Then, to add an item to the cart, call `[addItemToCart(webstoreId, effectiveAccountId, activeCartOrId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_9)`
`[cartItemInput, currencyIsoCode)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_9)` . You can specify custom fields using the `customFields` property of
`cartItemInput` . Again, the type of `customFields` is `List<SObject>`, but the sObject must be a CartItem.

[In this scenario we assume that further customization sets a custom field within the Cart Calculate API flow onto the cart item for further](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/cart-calculate-api.html)
use.

```
   ID webStoreId = '0ZEOL000000063r4AA';

      ID accountId = '001OL000002LC0qYAG';

      ID productId = '01tOL000000ETzuYAG';

      List<SObject> webCartList = new List<SObject>();

      WebCart webCart = new WebCart();

      webCart.webCartCustomTextField__c = 'webCartCustomFieldValue';

      webCartList.add(webCart);

      final ConnectApi.CartInput cartInput = new ConnectApi.CartInput();

      cartInput.effectiveAccountId = accountId;

      cartInput.name = 'Cart With Custom Fields';

      cartInput.customFields = webCartList;

      // create a cart

      ConnectApi.CartSummary cartSummary = ConnectApi.CommerceCart.createCart(webStoreId,

   cartInput);

      ID cartId = cartSummary.cartId;

      // Given

      List<SObject> cartItemList = new List<SObject>();

      CartItem cartItem = new CartItem();

      cartItem.cartItemCustomNumberField__c = 12.34;

      cartItemList.add(cartItem);

      final ConnectApi.CartItemInput input = new ConnectApi.CartItemInput();

      input.productId = productId;

      input.quantity = '2';

      input.type = ConnectApi.CartItemType.Product;

      input.customFields = cartItemList;

      // add an item to the previously created cart

      ConnectApi.CartItem itemResult = ConnectApi.CommerceCart.addItemToCart(webStoreId,

   accountId, cartId, input, 'USD');

      // response contains all (accessible) custom fields for which data was set

      CartItem cartItemResult = (CartItem)itemResult.customFields[0];

      // the value from request (if not changed during flow)

      Double valueFromRequest = cartItemResult.cartItemCustomNumberField__c;

      // an additional customization value, e.g. set by the cart calculation flow

      String valueForCustomization = cartItemResult.additionalCustomField__c;

```


Apex Developer Guide Using Salesforce Features with Apex

##### Connect in Apex Features

This topic describes which classes and methods to use to work with common Connect in Apex features.

[You can also go directly to the ConnectApi Namespace reference content.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_connect_api.htm)

###### Working with Action Links

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke
an API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body
and header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services
into the feed so that users can drive productivity and accelerate innovation.

Working with Feeds and Feed Elements
The Chatter feed is a container of feed elements. The abstract class `ConnectApi.FeedElement` is a parent class to the
`ConnectApi.FeedItem` class, representing feed posts, and the `ConnectApi.GenericFeedElement` class, representing
bundles and recommendations in the feed.

Accessing ConnectApi Data in Experience Cloud Sites
Many `ConnectApi` methods work within the context of a single Experience Cloud site.

Methods Available to Experience Cloud Guest Users
If your Experience Cloud site allows access without logging in, guest users have access to many Apex methods. These methods
return information the guest user has access to.

Supported Validations for DBT Segments
When creating or updating a segment, the ConnectApi.CdpSegmentInput class is subject to some SQL validations.

###### Working with Action Links

An action link is a button on a feed element. Clicking an action link can take a user to a Web page, initiate a file download, or invoke an
API call to Salesforce or to an external server. An action link includes a URL and an HTTP method, and can include a request body and
header information, such as an OAuth token for authentication. Use action links to integrate Salesforce and third-party services into the
feed so that users can drive productivity and accelerate innovation.

Workflow

This feed item contains one action link group with one visible action link, **Join** .


Apex Developer Guide Using Salesforce Features with Apex

The workflow to create and post action links with a feed element:

**1.** (Optional) Create an action link template.

**2.** Call `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`

to define an action link group that contains at least one action link.

**3.** Call `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed element
and associate the action link with it.

Use these methods to work with action links.

**ConnectApi Method** **Task**

`[ActionLinks.createActionLinkGroupDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` Create an action link group definition. To associate an action link
`[(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` group with a feed element, first create an action link group

```
ActionLinks.deleteActionLinkGroupDefinition(communityId,

actionLinkGroupId)

ActionLinks.getActionLinkGroupDefinition(communityId,

actionLinkGroupId)

```

definition. Then post a feed element with an associated actions
capability.

`[ChatterFeeds.postFeedElement(communityId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` Post a feed element with an associated actions capability. Associate
`[feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` up to 10 action link groups with a feed element.

`[ActionLinks.getActionLink(communityId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLink_1)` Get information about an action link, including state for the context
`[actionLinkId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLink_1)` user.

`[ActionLinks.getActionLinkGroup(communityId,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkGroup_1)` Get information about an action link group including state for the
`[actionLinkGroupId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkGroup_1)` context user.

```
ActionLinks.getActionLinkDiagnosticInfo(communityId,

actionLinkId)

```

Get diagnostic information returned when an action link executes.
Diagnostic information is given only for users who can access the
action link.


Apex Developer Guide Using Salesforce Features with Apex

**ConnectApi Method** **Task**

```
ChatterFeeds.getFeedElementsFromFeed()

```

Get the feed elements from a specified feed type. If a feed element
has action links associated with it, the action links data is returned
in the feed element’s associated actions capability.

####### Action Links Overview, Authentication, and Security

Learn about Apex action links security, authentication, labels, and errors.

Action Links Use Case
Use action links to integrate Salesforce and third-party services with a feed. An action link can make an HTTP request to a Salesforce
or third-party API. An action link can also download a file or open a web page. This topic contains an example use case.

SEE ALSO:

Define an Action Link and Post with a Feed Element

Define an Action Link in a Template and Post with a Feed Element

####### Action Links Overview, Authentication, and Security

Learn about Apex action links security, authentication, labels, and errors.

**Workflow**

This feed item contains one action link group with one visible action link, **Join** .

The workflow to create and post action links with a feed element:

**1.** (Optional) Create an action link template.

**2.** Call `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`

to define an action link group that contains at least one action link.


Apex Developer Guide Using Salesforce Features with Apex

**3.** Call `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed element
and associate the action link with it.

**Action Link Templates**

Create action link templates in Setup to instantiate action link groups with common properties. You can package templates and distribute
them to other Salesforce orgs.

Specify binding variables in the template and set the values of the variables when you instantiate the action link group. For example,
use a binding variable for the API version number, a user ID, or an OAuth token.

You can also specify context variables in the templates. When a user executes the action link, Salesforce provides values for these variables,
such as who executed the link and in which organization.

To instantiate the action link group, call the

```
   ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId, actionLinkGroup)
```

method. Specify the template ID and the values for any binding variables defined in the template.

[See Design Action Link Templates.](https://help.salesforce.com/articleView?id=action_link_group_template_design.htm&type=5&language=en_US)

**Type of Action Links**

Specify the action link type in the `actionType` property when you define an action link.

There are four types of action links:

**•** `Api` —The action link calls a synchronous API at the action URL. Salesforce sets the status to `SuccessfulStatus` or
`FailedStatus` based on the HTTP status code returned by your server.

**•** `ApiAsync` —The action link calls an asynchronous API at the action URL. The action remains in a `PendingStatus` state until
a third party makes a request to `/connect/action-links/` _**`actionLinkId`**_ to set the status to `SuccessfulStatus`
or `FailedStatus` when the asynchronous operation is complete.

**•** `Download` —The action link downloads a file from the action URL.

**•** `Ui` —The action link takes the user to a web page at the action URL.

**Authentication**

When you define an action link, specify a URL ( `actionUrl` ) and the HTTP headers ( `headers` ) required to make a request to that
URL.

If an external resource requires authentication, include the information wherever the resource requires.

If a Salesforce resource requires authentication, you can include OAuth information in the HTTP headers or you can include a bearer
token in the URL.

Salesforce automatically authenticates these resources.

**•** Relative URLs in templates

**•** Relative URLs beginning with `/services/apexrest` when the action link group is instantiated from Apex

Don’t use these resources for sensitive operations.

**Security**

**HTTPS**
The action URL in an action link must begin with `https://` or be a relative URL that matches one of the rules in the previous
Authentication section.


Apex Developer Guide Using Salesforce Features with Apex

**Encryption**
API details are stored with encryption, and obfuscated for clients.

The `actionURL`, `headers`, and `requestBody` data for action links that are not instantiated from a template are encrypted
with the organization’s encryption key. The `Action URL`, `HTTP Headers`, and `HTTP Request Body` for an action link
template are not encrypted. The binding values used when instantiating an action link group from a template are encrypted with
the organization’s encryption key.

**Action Link Templates**
Only users with Customize Application user permission can create, edit, delete, and package action link templates in Setup.

Don’t store sensitive information in templates. Use binding variables to add sensitive information when you instantiate the action
link group. After the action link group is instantiated, the values are stored in an encrypted format. See Define Binding Variables in
[Design Action Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)

**Client Apps**
When creating action links via a client app, it's a good idea to use a client app with a consumer key that never leaves your control.
The client app is used for server-to-server communication and is not compiled into mobile apps that could be decompiled.

**Expiration Date**
When you define an action link group, specify an expiration date ( `expirationDate` ). After that date, the action links in the group
can’t be executed and disappear from the feed. If your action link group definition includes an OAuth token, set the group’s expiration
date to the same value as the expiration date of the OAuth token.

[Action link templates use a slightly different mechanism for excluding a user. See Set the Action Link Group Expiration Time in Design](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)
[Action Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)

**Exclude a User or Specify a User**
Use the `excludeUserId` property of the action link definition input to exclude a single user from executing an action.

Use the `userId` property of the action link definition input to specify the ID of a user who alone can execute the action. If you
don’t specify a `userId` property or if you pass `null`, any user can execute the action. You can’t specify both `excludeUserId`
and `userId` for an action link

[Action link templates use a slightly different mechanism for excluding a user. See Set Who Can See the Action Link in Design Action](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)
[Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)

**Read, Modify, or Delete an Action Link Group Definition**
There are two views of an action link and an action link group: the definition, and the context user’s view. The definition includes
potentially sensitive information, such as authentication information. The context user’s view is filtered by visibility options and the
values reflect the state of the context user.

Action link group definitions can contain sensitive information (such as OAuth tokens). For this reason, to read, modify, or delete a
definition, the user must have created the definition or have View All Data permission. In addition, in Connect REST API, the request
must be made via the same client app that created the definition. In Apex, the call must be made from the same namespace that
created the definition.

**Context Variables**

Use context variables to pass information about the user who executed the action link and the context in which it was invoked into the
HTTP request made by invoking an action link. You can use context variables in the `actionUrl`, `headers`, and `requestBody`
properties of the Action Link Definition Input request body or `ConnectApi.ActionLinkDefinitionInput` object. You can
also use context variables in the `Action URL`, `HTTP Request Body`, and `HTTP Headers` fields of action link templates. You
can edit these fields, including adding and removing context variables, after a template is published.

The context variables are:


Apex Developer Guide Using Salesforce Features with Apex

**Versioning**

To avoid issues due to upgrades or changing functionality in your API, we recommend using versioning when defining action links. For
example, the `actionUrl` property in the `[ConnectApi.ActionLinkDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_action_link_definition.htm)` looks like
`https://www.example.com/api/v1/exampleResource` .

You can use templates to change the values of the `actionUrl`, `headers`, or `requestBody` properties, even after a template is
distributed in a package. Let’s say you release a new API version that requires new inputs. An admin can change the inputs in the action
link template in Setup and even action links already associated with a feed element use the new inputs. However, you can’t add new
binding variables to a published action link template.

If your API isn’t versioned, you can use the `expirationDate` property of the
`[ConnectApi.ActionLinkGroupDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_action_link_group_definition.htm)` to avoid issues due to upgrades or changing functionality in your API.
[See Set the Action Link Group Expiration Time in Design Action Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)

**Errors**

Use the Action Link Diagnostic Information method
( `[ConnectApi.ActionLinks.getActionLinkDiagnosticInfo(communityId, actionLinkId)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkDiagnosticInfo_1)` ) to return
status codes and errors from executing `Api` action links. Diagnostic info is given only for users who can access the action link.

**Localized Labels**

Action links use a predefined set of localized labels specified in the `labelKey` property of the
`[ConnectApi.ActionLinkDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_action_link_definition.htm)` request body and the `Label` field of an action link template.

[For a list of labels, see Actions Links Labels.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)


Apex Developer Guide Using Salesforce Features with Apex

Note: If none of the label key values make sense for your action link, specify a custom label in the `Label` field of an action link
template and set `Label Key` to None. However, custom labels aren’t localized.

SEE ALSO:

Define an Action Link and Post with a Feed Element

Define an Action Link in a Template and Post with a Feed Element

Define an Action Link and Post with a Feed Element

Define an Action Link in a Template and Post with a Feed Element

####### Action Links Use Case

Use action links to integrate Salesforce and third-party services with a feed. An action link can make an HTTP request to a Salesforce or
third-party API. An action link can also download a file or open a web page. This topic contains an example use case.

**Start a Video Chat from the Feed**

Suppose that you work as a Salesforce developer for a company that has a Salesforce org and an account with a fictional company called
“VideoChat.” Users have been saying they want to do more from their mobile devices. You’re asked to create an app that lets users create
and join video chats directly from their mobile device.

When a user opens the VideoChat app in Salesforce, they’re asked to name the video chat room and invite either a group or individual
users to the video chat room. When the user clicks **OK**, the VideoChat app launches the video chat room and posts a feed item to the
selected group or users asking them to **Please join the video chat** by clicking an action link labeled **Join** . When an invitee clicks **Join**,
the action link opens a web page containing the video chat room.

As a developer thinking about how to create the action link URL, you come up with these requirements:

**1.** When a user clicks **Join**, the action link URL has to open the video chat room they were invited to.

**2.** The action link URL has to tell the video chat room who’s joining.

To dynamically create the action link URLs, you create an action link template in Setup.


Apex Developer Guide Using Salesforce Features with Apex

For the first requirement, you create a `{!Bindings.roomId}` binding variable in the `Action URL` template field. When the
user clicks **OK** to create the video chat room, your Apex code generates a unique room ID. The Apex code uses that unique room ID as
the binding variable value when it instantiates the action link group, associates it with the feed item, and posts the feed item.

For the second requirement, the action link must include the user ID. Action links support a predefined set of context variables. When
an action link is invoked, Salesforce substitutes the variables with values. Context variables include information about who clicked the
action link and in what context it was invoked. You decide to include a `{!userId}` context variable in the `Action URL` so that
when a user clicks the action link in the feed, Salesforce substitutes the user’s ID and the video chat room knows who’s entering.

This is the action link template for the **Join** action link.

Every action link must be associated with an action link group. The group defines properties shared by all the action links associated
with it. Even if you’re using a single action link (as in this example) it must be associated with a group. The first field of the action link
template is `Action Link Group Template`, which in this case is **Video Chat**, which is the action link group template the
action link template is associated with.


Apex Developer Guide Using Salesforce Features with Apex

.

###### Working with Feeds and Feed Elements

The Chatter feed is a container of feed elements. The abstract class `ConnectApi.FeedElement` is a parent class to the
`ConnectApi.FeedItem` class, representing feed posts, and the `ConnectApi.GenericFeedElement` class, representing
bundles and recommendations in the feed.

Note: Salesforce Help refers to feed items as posts and bundles as bundled posts.

Capabilities

As part of the effort to diversify the feed, pieces of functionality found in feed elements have been broken out into capabilities. Capabilities
provide a consistent way to interact with the feed. Don’t inspect the feed element type to determine which functionality is available for
a feed element. Inspect the capability, which tells you explicitly what’s available. Check for the presence of a capability to determine
what a client can do to a feed element.

The `[ConnectApi.FeedElement.capabilities](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_feed_element.htm)` property holds a set of capabilities.

A capability includes both an indication that a feature is possible and data associated with that feature. If a capability property exists on
a feed element, that capability is available, even if there isn’t any data associated with the capability yet. For example, if the
`chatterLikes` capability property exists on a feed element, the context user can like that feed element. If the capability property
doesn’t exist on a feed element, it isn’t possible to like that feed element.

When posting a feed element, specify its characteristics in the `[ConnectApi.FeedElementInput.capabilities](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_feed_element.htm)` property.

How the Salesforce UI Displays Feed Items

A client can use the `ConnectApi.FeedElement.capabilities` property to determine what it can do with a feed element
and how to render the feed element. For all feed element subclasses other than `ConnectApi.FeedItem`, the client doesn’t have
to know the subclass type. Instead, the client can look at the capabilities. Feed items do have capabilities, but they also have a few
properties, such as `actor`, that aren’t exposed as capabilities. For this reason, clients must handle feed items a bit differently than other
feed elements.

The Salesforce UI uses one layout to display every feed item. This single layout gives customers a consistent view of feed items and gives
developers an easy way to create UI. The layout always contains the same pieces and the pieces are always in the same position. Only
the content of the layout pieces changes.


Apex Developer Guide Using Salesforce Features with Apex

The feed item ( `[ConnectApi.FeedItem](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_Feed_Item.htm)` ) layout elements are:

**1.** Actor ( `ConnectApi.FeedItem.actor` )—A photo or icon of the creator of the feed item. (You can override the creator at
the feed item type level. For example, the dashboard snapshot feed item type shows the dashboard as the creator.)

**2.** Header ( `ConnectApi.FeedElement.header` )—Context for the feed item. The same feed item can have a different header
depending on who posted it and where it was posted. For example, Ted posted this feed item to a group.

Timestamp ( `ConnectApi.FeedElement.relativeCreatedDate` )—The date and time when the feed item was posted.
If the feed item is less than two days old, the date and time are formatted as a relative, localized string, such as “17m ago”. Otherwise,
the date and time are formatted as an absolute, localized string.

**3.** Body ( `ConnectApi.FeedElement.body` )—All feed items have a body. The body can be `null`, which is the case when
the user doesn’t provide text for the feed item. Because the body can be `null`, you can’t use it as the default case for rendering
text. Instead, use the `ConnectApi.FeedElement.header.text` property, which always contains a value.

**4.** Auxiliary Body ( `ConnectApi.FeedElement.capabilities` )—The visualization of the capabilities. See Capabilities.

How the Salesforce Displays Feed Elements Other Than Feed Items

A client can use the `ConnectApi.FeedElement.capabilities` property to determine what it can do with a feed element
and how to render the feed element. This section uses bundles as an example of how to render a feed element, but these properties
are available for every feed element. Capabilities allow you to handle all content in the feed consistently.

Note: Bundled posts contain feed-tracked changes and are in record feeds only.

To give customers a clean, organized feed, Salesforce aggregates feed-tracked changes into a bundle. To see individual feed elements,
click the bundle.

A bundle is a `ConnectApi.GenericFeedElement` object (which is a concrete subclass of `ConnectApi.FeedElement` )
with a `ConnectApi.BundleCapability` . The bundle layout elements are:

**•** Header ( `ConnectApi.FeedElement.header` )—For feed-tracked change bundles, this text is “ _`User Name`_ updated this
record.”

**•** Timestamp ( `ConnectApi.FeedElement.relativeCreatedDate` )—The date and time when the feed item was posted.
If the feed item is less than two days old, the date and time are formatted as a relative, localized string, such as “17m ago”. Otherwise,
the date and time are formatted as an absolute, localized string.

**•** Auxiliary Body ( `ConnectApi.FeedElement.capabilities.bundle.changes` )—The bundle displays the
`fieldName` and the `oldValue` and `newValue` properties for the first two feed-tracked changes in the bundle. If there are
more than two feed-tracked changes, the bundle displays a “Show All Updates” link.


Apex Developer Guide Using Salesforce Features with Apex

Feed Element Visibility

The feed elements a user sees depend on how the administrator has configured feed tracking, sharing rules, and field-level security. For
example, if a user doesn’t have access to a record, they don’t see updates for that record. If a user can see the parent of the feed element,
the user can see the feed element. Typically, a user sees feed updates for:

**•** Feed elements that @mention the user (if the user can access the feed element’s parent)

**•** Feed elements that @mention groups the user is a member of

**•** Record field changes on records whose parent is a record the user can see, including User, Group, and File records

**•** Feed elements posted to the user

**•** Feed elements posted to groups that the user owns or is a member of

**•** Feed elements for standard and custom records, for example, tasks, events, leads, accounts, files

Feed Types

There are many types of feeds. Each feed type defines a collection of feed elements.

Important: The collection of feed elements can change between releases.

All feed types except Favorites are exposed in the `ConnectApi.FeedType` enum and passed to one of the
`ConnectApi.ChatterFeeds.getFeedElementsFromFeed` methods. This example gets the feed elements from the
context user’s news feed and topics feed.

```
   ConnectApi.FeedElementPage newsFeedElementPage =

     ConnectApi.ChatterFeeds.getFeedElementsFromFeed(null,

       ConnectApi.FeedType.News, 'me');

   ConnectApi.FeedElementPage topicsFeedElementPage =

     ConnectApi.ChatterFeeds.getFeedElementsFromFeed(null,

       ConnectApi.FeedType.Topics, '0TOD00000000cld');

```

To get a filter feed, call one of the `ConnectApi.ChatterFeeds.getFeedElementsFromFilterFeed` methods. To get
a favorites feed, call one of the `ConnectApi.ChatterFavorites.getFeedElements` methods.

The feed types and their descriptions are:

**•** `Bookmarks` —Contains all feed items saved as bookmarks by the context user.

**•** `Company` —Contains all feed items except feed items of type `TrackedChange` . To see the feed item, the user must have sharing
access to its parent.

**•** `DirectMessageModeration` —Contains all direct messages that are flagged for moderation. The Direct Message Moderation
feed is available only to users with Moderate Experiences Chatter Messages permissions.

**•** `DirectMessages` —Contains all feed items of the context user’s direct messages.

**•** `Draft` —Contains all the feed items that the context user drafted.

**•** `Files` —Contains all feed items that contain files posted by people or groups that the context user follows.

**•** `Filter` —Contains the news feed filtered to contain feed items whose parent is a specified object type.

**•** `Groups` —Contains all feed items from all groups the context user either owns or is a member of.

**•** `Home` —Contains all feed items associated with any managed topic in an Experience Cloud site.

**•** `Landing` —Contains all feed items that best drive user engagement when the feed is requested. Allows clients to avoid an empty
feed when there aren’t many personalized feed items.

**•** `Moderation` —Contains all feed items that are flagged for moderation, except direct messages. The moderation feed is available
only to users with Moderate Experiences Feeds permissions.


Apex Developer Guide Using Salesforce Features with Apex

**•** `Mute` —Contains all feed items that the context user muted.

**•** `News` —Contains all updates for people the context user follows, groups the user is a member of, and files and records the user is
following. Contains all updates for records whose parent is the context user.

**•** `PendingReview` —Contains all feed items and comments that are pending review.

**•** `People` —Contains all feed items posted by all people the context user follows.

**•** `Record` —Contains all feed items whose parent is a specified record, which could be a group, user, object, file, or any other standard
or custom object. When the record is a group, the feed also contains feed items that mention the group. When the record is a user,
the feed contains only feed items on that user. You can get another user’s record feed.

**•** `Streams` —Contains all feed items for any combination of up to 25 feed-enabled entities that the context user subscribes to in a
stream. Examples of feed-enabled entities include people, groups, and records,

**•** `To` —Contains all feed items with mentions of the context user. Contains feed items the context user commented on and feed items
created by the context user that are commented on.

**•** `Topics` —Contains all feed items that include the specified topic.

**•** `UserProfile` —Contains feed items created when a user changes records that can be tracked in a feed. Contains feed items
whose parent is the user and feed items that @mention the user. This feed is different than the news feed, which returns more feed
items, including group updates. You can get another user’s user profile feed.

**•** `Favorites` —Contains favorites saved by the context user. Favorites are feed searches, list views, and topics.

Post a Feed Item Using **`postFeedElement`**

Tip: The `postFeedElement` methods are the simplest, most efficient way to post feed items because, unlike the
`postFeedItem` methods, they don’t require you to pass a feed type. Feed items are the only feed element type you can post.

Use these methods to post feed items.

```
   postFeedElement(communityId, subjectId, feedElementType, text)
```

Post a plain-text feed element.

**`[postFeedElement(communityId, feedElement, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_2)`** **(version 35.0 and earlier)**
Post a rich-text feed element. Include mentions and hashtag topics, attach a file to a feed element, and associate action link groups
with a feed element. You can also use this method to share a feed element and add a comment.

**`[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)`** **(version 36.0 and later)**
Post a rich-text feed element. Include mentions and hashtag topics, attach already uploaded files to a feed element, and associate
action link groups with a feed element. You can also use this method to share a feed element and add a comment.

When you post a feed item, you create a child of a standard or custom object. Specify the parent object in the _**`subjectId`**_ parameter
or in the _**`subjectId`**_ property of the `ConnectApi.FeedElementInput` object you pass in the _**`feedElement`**_ parameter.
The value of the _**`subjectId`**_ parameter determines the feeds in which the feed item is displayed. The `parent` property in the
returned `ConnectApi.FeedItem` object contains information about the parent object.

Use these methods to complete these tasks.

**Post to yourself**
This code posts a feed item to the context user. The _**`subjectId`**_ specifies `me`, which is an alias for the context user’s ID. It could
also specify the context user’s ID.

```
     ConnectApi.FeedElement feedElement = ConnectApi.ChatterFeeds.postFeedElement(null, 'me',

      ConnectApi.FeedElementType.FeedItem, 'Working from home today.');

```

The `parent` property of the newly posted feed item contains the `ConnectApi.UserSummary` of the context user.


Apex Developer Guide Using Salesforce Features with Apex

**Post to another user**
This code posts a feed item to a user other than the context user. The _**`subjectId`**_ specifies the user ID of the target user.

```
     ConnectApi.FeedElement feedElement = ConnectApi.ChatterFeeds.postFeedElement(null,

     '005D00000016Qxp', ConnectApi.FeedElementType.FeedItem, 'Kevin, do you have information

      about the new categories?');

```

The `parent` property of the newly posted feed item contains the `ConnectApi.UserSummary` of the target user.

**Post to a group**
This code posts a feed item to a group. The _**`subjectId`**_ specifies the group ID.

```
     ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

     ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

     ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

     ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

     messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

     mentionSegmentInput.id = '005RR000000Dme9';

     messageBodyInput.messageSegments.add(mentionSegmentInput);

     textSegmentInput.text = 'Could you take a look?';

     messageBodyInput.messageSegments.add(textSegmentInput);

     feedItemInput.body = messageBodyInput;

     feedItemInput.feedElementType = ConnectApi.FeedElementType.FeedItem;

     feedItemInput.subjectId = '0F9RR0000004CPw';

     ConnectApi.FeedElement feedElement =

     ConnectApi.ChatterFeeds.postFeedElement(Network.getNetworkId(), feedItemInput);

```

The `parent` property of the newly posted feed item contains the `ConnectApi.ChatterGroupSummary` of the specified
group.

**Post to a record (such as a file or an account)**
This code posts a feed item to a record and mentions a group. The _**`subjectId`**_ specifies the record ID.

```
     ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

     ConnectApi.MentionSegmentInput mentionSegmentInput = new ConnectApi.MentionSegmentInput();

     ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

     ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

     messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

     textSegmentInput.text = 'Does anyone know anyone with contacts here?';

     messageBodyInput.messageSegments.add(textSegmentInput);

     // Mention a group.

     mentionSegmentInput.id = '0F9D00000000oOT';

     messageBodyInput.messageSegments.add(mentionSegmentInput);

     feedItemInput.body = messageBodyInput;

     feedItemInput.feedElementType = ConnectApi.FeedElementType.FeedItem;

     // Use a record ID for the subject ID.

```


Apex Developer Guide Using Salesforce Features with Apex

```
     feedItemInput.subjectId = '001D000000JVwL9';

     ConnectApi.FeedElement feedElement = ConnectApi.ChatterFeeds.postFeedElement(null,

     feedItemInput);

```

The `parent` property of the new feed item depends on the record type specified in _**`subjectId`**_ . If the record type is File, the
parent is `ConnectApi.FileSummary` . If the record type is Group, the parent is `ConnectApi.ChatterGroupSummary` .
If the record type is User, the parent is `ConnectApi.UserSummary` . For all other record types, as in this example that uses an
Account, the parent is `ConnectApi.RecordSummary` .

Get Feed Elements from a Feed

Tip: To return a feed that includes feed elements, call these methods. Feed element types include feed item, bundle, and
recommendation.

Getting feed items from a feed is similar, but not identical, for each feed type.

**Get feed elements from the** **`Company`** **,** **`DirectMessageModeration`** **,** **`DirectMessages`** **,** **`Home`** **,** **`Moderation`** **, and**
**`PendingReview`** **feeds**
To get the feed elements from these feeds, use these methods that don’t require a _`subjectId`_ .

**•** `getFeedElementsFromFeed(communityId, feedType)`

**•** `getFeedElementsFromFeed(communityId, feedType, pageParam, pageSize, sortParam)`

**•** `getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`

```
      pageParam, pageSize, sortParam)

```

**•** `getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`

```
      pageParam, pageSize, sortParam, filter)

```

**•** `getFeedElementsFromFeed(communityId, feedType, recentCommentCount, density,`

```
      pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

**Get feed elements from the** **`Favorites`** **feed**
To get the feed elements from the favorites feed, specify a _`favoriteId`_ . For these feeds, the _`subjectId`_ must be the ID of
the context user or the alias `me` .

**•** `getFeedElements(communityId, subjectId, favoriteId)`

**•** `getFeedElements(communityId, subjectId, favoriteId, pageParam, pageSize, sortParam)`

**•** `getFeedElements(communityId, subjectId, favoriteId, recentCommentCount,`

```
      elementsPerBundle, pageParam, pageSize, sortParam)

```

**Get feed elements from the** **`Filter`** **feed**
To get the feed elements from the filters feed, specify a _`keyPrefix`_ . The _`keyPrefix`_ indicates the object type and is the first
three characters of the object ID. The _`subjectId`_ must be the ID of the context user or the alias `me` .

**•** `getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix)`

**•** `getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, pageParam,`

```
      pageSize, sortParam)

```

**•** `getFeedElementsFromFilterFeed(communityId, subjectId, keyPrefix, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam)

```

**Get feed elements from the** **`Bookmarks`** **,** **`Files`** **,** **`Groups`** **,** **`Mute`** **,** **`News`** **,** **`People`** **,** **`Record`** **,** **`Streams`** **,** **`To`** **,** **`Topics`** **,**
**and** **`UserProfile`** **feeds**
To get the feed elements from these feed types, specify a subject ID. If _`feedType`_ is `Record`, _`subjectId`_ can be any record
ID, including a group ID. If _`feedType`_ is `Streams`, _`subjectId`_ must be a stream ID. If _`feedType`_ is `Topics`, _`subjectId`_


Apex Developer Guide Using Salesforce Features with Apex

must be a topic ID. If _`feedType`_ is `UserProfile`, _`subjectId`_ can be any user ID. If the _`feedType`_ is any other value,
_`subjectId`_ must be the ID of the context user or the alias `me` .

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId)`

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, pageParam, pageSize,`

```
      sortParam)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      density, pageParam, pageSize, sortParam)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      density, pageParam, pageSize, sortParam, filter)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      density, pageParam, pageSize, sortParam, filter, threadedCommentsCollapsed)

```

**Get feed elements from a** **`Record`** **feed**
For _`subjectId`_, specify a record ID.

Tip: The record can be a record of any type that supports feeds, including group. The feed on the group page in the Salesforce
UI is a record feed.

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      density, pageParam, pageSize, sortParam, showInternalOnly)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      density, pageParam, pageSize, sortParam, customFilter)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

      filter)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

      customFilter)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

      filter, threadedCommentsCollapsed)

```

**•** `getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,`

```
      elementsPerBundle, density, pageParam, pageSize, sortParam, showInternalOnly,

      customFilter, threadedCommentsCollapsed)

```

SEE ALSO:

_Apex Reference Guide_ [: ChatterFavorites Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFavorites_static_methods.htm)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

_Apex Reference Guide_ [: ConnectApi Output Classes](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output.htm)

_Apex Reference Guide_ [: ConnectApi Input Classes](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input.htm)

###### Accessing ConnectApi Data in Experience Cloud Sites

Many `ConnectApi` methods work within the context of a single Experience Cloud site.


Apex Developer Guide Using Salesforce Features with Apex

Many `ConnectApi` methods include _**`communityId`**_ as the first argument. If you don’t have digital experiences enabled, use
`internal` or `null` for this argument.

If you have digital experiences enabled, the _`communityId`_ argument specifies whether to execute a method in the context of the
default Experience Cloud site (by specifying `internal` or `null` ) or in the context of a specific site (by specifying an ID). Any entity,
such as a comment or a feed item, referred to by other arguments in the method must be in the specified site. The ID is included in URLs
returned in the output.

Some `ConnectApi` methods include _**`siteId`**_ as an argument. Unlike _**`communityId`**_, if you don’t have digital experiences
enabled, you can’t use these methods. The site ID is included in URLs returned in the output.

Most URLs returned in `ConnectApi` output objects are Connect REST API resources.

If you specify an ID, URLs returned in the output use the following format:

```
   /connect/communities/ communityId / resource

```

If you specify `internal`, URLs returned in the output use the same format:

```
   /connect/communities/internal/ resource

```

If you specify `null`, URLs returned in the output use one of these formats:

```
   /chatter/ resource

   /connect/ resource

###### Methods Available to Experience Cloud Guest Users

```

If your Experience Cloud site allows access without logging in, guest users have access to many Apex methods. These methods return
information the guest user has access to.

All overloads of these methods are available to guest users.

[Important: If an overload of a method listed here indicates that Chatter is required, you must also enable public access to your](https://help.salesforce.com/articleView?id=community_builder_page_access_settings.htm&type=5&language=en_US)
Experience Cloud site to make the method available to guest users. If you don’t enable public access, data retrieved by methods
that require Chatter doesn’t load correctly on public site pages.

**•** `Announcements` methods:

**–** `[getAnnouncements()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Announcements_static_methods.htm#apex_ConnectAPI_Announcements_getAnnouncements_1)`

**•** `ChatterFeeds` methods:

**–** `[getComment()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getComment)`

**–** `[getCommentInContext()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getCommentInContext_1)`

**–** `[getCommentsForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getCommentsForFeedElement_1)`

**–** `[getExtensions()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getExtensions_1)`

**–** `[getFeed()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeed)`

**–** `[getFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElement_1)`

**–** `[getFeedElementBatch()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementBatch_1)`

**–** `[getFeedElementPoll()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementPoll_1)`

**–** `[getFeedElementsFromFeed()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_1)`

**–** `[getFeedElementsUpdatedSince()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsUpdatedSince_1)`

**–** `[getFeedWithFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedWithFeedElements_5)`


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getLike()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLike)`

**–** `[getLikesForComment()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLikesForComment)`

**–** `[getLikesForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLikesForFeedElement_1)`

**–** `[getLinkMetadata()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLinkMetadata_1)`

**–** `[getPinnedFeedElementsFromFeed()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getPinnedFeedElementsFromFeed_1)`

**–** `[getRelatedPosts()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getRelatedPosts_1)`

**–** `[getThreadsForFeedComment()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getThreadsForFeedComment_1)`

**–** `[getVotesForComment()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getVotesForComment_1)`

**–** `[getVotesForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getVotesForFeedElement_1)`

**–** `[searchFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_searchFeedElements_1)`

**–** `[searchFeedElementsInFeed()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_searchFeedElementsInFeed_1)`

**–** `[updatePinnedFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updatePinnedFeedElements_2)`

**•** `ChatterGroups` methods:

**–** `[getGroup()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getGroup)`

**–** `[getGroups()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getGroups)`

**–** `[getMembers()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getMembers)`

**–** `[searchGroups()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_searchGroups)`

**•** `ChatterUsers` methods:

**–** `[getFollowers()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getFollowers)`

**–** `[getFollowings()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getFollowings)`

**–** `[getReputation()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getReputation_1)`

**–** `[getUser()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUser)`

**–** `[getUserBatch()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUserBatch)`

**–** `[getUserGroups()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getGroups_3)`

**–** `[getUsers()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUsers)`

**–** `[searchUserGroupDetails()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_searchUserGroups_3)`

**–** `[searchUsers()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_searchUsers)`

**•** `CommerceCart` methods:

**–** `[addItemsToCart()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemsToCart_1)`

**–** `[addItemToCart()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_1)`

**–** `[applyCartCoupon()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_applyCartCoupon_1)`

**–** `[calculateCart()](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_calculateCart_1)`

**–** `[cloneCart()](https://developer.salesforce.com/docs/atlas.en-us.246.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_cloneCart_1)`

**–** `[copyCartToWishlist()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_copyCartToWishlist_1)`

**–** `[createCart()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_createCart_1)`

**–** `[deleteCart()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCart_1)`

**–** `[deleteCartCoupon()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCartCoupon_1)`

**–** `[deleteCartItem()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCartItem_1)`

**–** `[deleteInventoryReservation()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteInventoryReservation_1)` (developer preview)


Apex Developer Guide Using Salesforce Features with Apex

**–** `[evaluateShipping()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_evaluateShipping_1)`

**–** `[evaluateTaxes()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_evaluateTaxes_1)`

**–** `[getCartCoupons()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartCoupons_1)`

**–** `[getCartItems()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartItems_6)`

**–** `[getCartCompactSummary()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartCompactSummary_1)`

**–** `[getCartSummary()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartSummary_1)`

**–** `[getOrCreateActiveCartSummary()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getOrCreateActiveCartSummary_2)`

**–** `[makeCartPrimary()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_makeCartPrimary_1)`

**–** `[setCartMessagesVisibility()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_setCartMessagesVisibility_1)`

**–** `[updateCartItem()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_updateCartItem_2)`

**–** `[upsertInventoryReservation()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_upsertInventoryReservation_2.htm)` (developer preview)

**•** `CommerceCatalog` methods:

**–** `[getCategoryMenuItems()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getCategoryMenuItems_1)`

**–** `[getProduct()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProduct_7)`

**–** `[getProducts()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProducts_4)`

**–** `[getProductCategory()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductCategory_2)`

**–** `[getProductCategoryChildren()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductCategoryChildren_1)`

**–** `[getProductCategoryPath()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getStorefrontCategoryPath_1)`

**–** `[getProductChildCollection()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductChildCollection_5)`

**•** `CommercePromotions` methods:

**–** `decreaseRedemption()`

**–** `[evaluate()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommercePromotions_static_methods.htm#apex_ConnectAPI_CommercePromotions_evaluate_1.xml)`

**–** `increaseRedemption()`

**•** `CommerceSearch` methods:

**–** `[getSortRules()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_getSortRules_1)`

**–** `[getSuggestions()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_getSuggestions_4)`

**–** `[searchProducts()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_productSearch_1)`

**•** `CommerceStorePricing` methods:

**–** `[getProductPrice()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceStorePricing_static_methods.htm#apex_ConnectAPI_CommerceStorePricing_getProductPrice_1)`

**–** `[getProductPrices()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CommerceStorePricing_static_methods.htm#apex_ConnectAPI_CommerceStorePricing_getProductPrices_1)`

**•** `Communities` methods:

**–** `[getCommunity()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Communities_static_methods.htm#apex_ConnectAPI_Communities_getCommunity)`

**•** `EmployeeProfiles` methods:

**–** `[getPhoto()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_EmployeeProfiles_static_methods.htm#apex_ConnectAPI_EmployeeProfiles_getPhoto_2)`

**•** `ExtendedCommerceDelivery` methods:

**–** `[estimateDeliveryDate()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ExtendedCommerceDelivery_static_methods.htm#apex_ConnectAPI_ExtendedCommerceDelivery_estimateDeliveryDate_1)`

**•** `Knowledge` methods:


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getTopViewedArticlesForTopic()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTopicTopViewedArticles_1)`

**–** `[getTrendingArticles()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTrendingArticles_1)`

**–** `[getTrendingArticlesForTopic()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTrendingArticlesForTopic_1)`

**•** `ManagedContent` methods:

**–** `[getAllContent()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllContent_1)`

**–** `[getAllDeliveryChannels()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllDeliveryChannels_1)`

**–** `[getAllManagedContent()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllManagedContent_1)`

**–** `[getContentByContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getContentByContentKeys_2)`

**–** `[getContentByIds()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getContentByIds_2)`

**–** `[getManagedContentByContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByContentKeys_2)`

**–** `[getManagedContentByIds()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByIds_2)`

**–** `[getManagedContentByTopics()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopics_3)`

**–** `[getManagedContentByTopicsAndContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopicsAndContentKeys_3a)`

**–** `[getManagedContentByTopicsAndIds()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopicsAndIds_4)`

**•** `ManagedContentDelivery` methods:

**–** `[getChannel()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getChannel_1)`

**–** `[getChannels()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getChannels_1)`

**–** `[getCollectionItemsForChannel()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getCollectionItemsForChannel_1)`

**–** `[getCollectionItemsForSite()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getCollectionItemsForSite_2)`

**–** `[getManagedContentChannel()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentChannel_1)`

**–** `[getManagedContentForChannel()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentForChannel_1)`

**–** `[getManagedContentForSite()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentForSite_4)`

**–** `[getManagedContentsForChannel()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentsForChannel_2)`

**–** `[getManagedContentsForSite()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentsForSite_4)`

**•** `ManagedTopics` methods:

**–** `[getManagedTopic()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedTopics_static_methods.htm#apex_ConnectAPI_ManagedTopics_getManagedTopic)`

**–** `[getManagedTopics()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ManagedTopics_static_methods.htm#apex_ConnectAPI_ManagedTopics_getManagedTopics_1)`

**•** `MarketingIntegration` methods:

**–** `[submitForm()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_MarketingIntegration_static_methods.htm#apex_ConnectAPI_MarketingIntegration_submitForm_1)`

**•** `NavigationMenu` methods:

**–** `[getCommunityNavigationMenu()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_NavigationMenu_static_methods.htm#apex_ConnectAPI_NavigationMenu_getCommunityNavigationMenu_1)`

**•** `NextBestActions` methods:

**–** `[executeStrategy()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_executeStrategy_1)`

**–** `[setRecommendationReaction()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_setRecommendationReaction_1)`

**•** `Personalization` methods:

**–** `[getAudience()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudience_2)`

**–** `[getAudienceBatch()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudienceBatch_1)`


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getAudiences()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudiences_1)`

**–** `[getTarget()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTarget_2)`

**–** `[getTargetBatch()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTargetBatch_1)`

**–** `[getTargets()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTargets_1)`

**•** `Recommendations` methods:

**–** `[getRecommendationsForUser()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Recommendations_static_methods.htm#apex_ConnectAPI_Recommendations_getRecommendationsForUser_1a)`

Note: Only article and file recommendations are available to guest users.

**•** `RecordUi` methods.

**–** `[getPicklistValuesByRecordType()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_RecordUi_static_methods.htm#apex_ConnectAPI_RecordUi_getPicklistValuesByRecordType_1)`

**•** `Search` methods.

**–** `[answer()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_answer_objects_1)`

**–** `[find()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_find_object_1)`

**–** `[findAndGroup()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_find_objects_1)`

**•** `Sites` methods:

**–** `[searchSite()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Sites_static_methods.htm#apex_ConnectAPI_Sites_searchSite_1)`

**•** `Topics` methods:

**–** `[getGroupsRecentlyTalkingAboutTopic()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getGroupsRecentlyTalkingAboutTopic)`

**–** `[getRecentlyTalkingAboutTopicsForGroup()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRecentlyTalkingAboutTopicsForGroup)`

**–** `[getRecentlyTalkingAboutTopicsForUser()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRecentlyTalkingAboutTopicsForUser)`

**–** `[getRelatedTopics()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRelatedTopics)`

**–** `[getTopic()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTopic)`

**–** `[getTopics()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTopics)`

**–** `[getTrendingTopics()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTrendingTopics)`

**•** `UserProfiles` methods:

**–** `[getPhoto()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_UserProfiles_static_methods.htm#apex_ConnectAPI_UserProfiles_getPhoto)`

SEE ALSO:

_Salesforce Help_ [: Give Secure Access to Unauthenticated Users with the Guest User Profile](https://help.salesforce.com/HTViewHelpDoc?id=networks_public_access.htm&language=en_US)

###### Supported Validations for DBT Segments

When creating or updating a segment, the ConnectApi.CdpSegmentInput class is subject to some SQL validations.

You can create a segment using the `[createSegment(input)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm#apex_ConnectAPI_CdpSegment_createSegment_4)` method with the `ConnectApi.CdpSegmentInput` class.
Similarly, you can update a segment using the `[updateSegment(segmentApiName, input)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm#apex_ConnectAPI_CdpSegment_updateSegment_4)` method with the same input
class. The `[ConnectApi.CdpSegmentDbtModelInput](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input_cdp_segment_dbt_model.htm)` input class, which is nested in the `ConnectApi.CdpSegmentInput`
class, provides validation for the SQL.

The `sql` property of the `ConnectApi.CdpSegmentDbtModelInput` is subject to these validations.


Apex Developer Guide Using Salesforce Features with Apex

##### Using ConnectApi Input and Output Classes

Some classes in the `ConnectApi` namespace contain static methods that access Connect REST API data. The `ConnectApi`
namespace also contains input classes to pass as parameters and output classes that calls to the static methods return.

`ConnectApi` methods take either simple or complex types. Simple types are primitive Apex data like integers and strings. Complex
types are `ConnectApi` input objects.

The successful execution of a `ConnectApi` method can return an output object from the `ConnectApi` namespace. `ConnectApi`
output objects can be made up of other output objects. For example, the `[ConnectApi.ActorWithId](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_actorWithIdOutput.htm)` output object contains
properties such as `id` and `url`, which contain primitive data types. It also contains a `mySubscription` property, which contains
a `ConnectApi.Reference` object.

Note: All Salesforce IDs in `ConnectApi` output objects are 18 character IDs. Input objects can use 15 character IDs or 18
character IDs.

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi Input Classes](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_input.htm)

_Apex Reference Guide_ [: ConnectApi Output Classes](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output.htm)

##### Understanding Limits for ConnectApi Classes

Limits for methods in the `ConnectApi` namespace are different than the limits for other Apex classes.

For classes in the `ConnectApi` namespace, every write operation costs one DML statement against the Apex governor limit.
`ConnectApi` method calls are also subject to rate limits. Most `ConnectApi` [method calls count toward the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
[total API request allocations, which are per org and span a 24-hour period. Only](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) `ConnectApi` method calls that require Chatter are
subject to a per user, per namespace, per hour rate limit. The documentation for every `ConnectApi` method indicates whether
Chatter is required. When you exceed the rate limit, a `ConnectApi.RateLimitException` is thrown. Your Apex code must
catch and handle this exception.

When testing code, a call to the Apex `Test.startTest` method starts a new rate limit count. A call to the `Test.stopTest`
method sets your rate limit count to the value it was before you called `Test.startTest` .

##### Packaging ConnectApi Classes

If you include `ConnectApi` classes in a package, be aware of Chatter dependencies.

If a `ConnectApi` class has a dependency on Chatter, the code can be compiled and installed in orgs that don’t have Chatter enabled.
However, if Chatter isn’t enabled, the code throws an error at run time.

```
   System.NoAccessException: Insufficient Privileges: This feature is not currently enabled

   for this user.

```

In its reference documentation, every `ConnectApi` method indicates whether or not it supports Chatter.

SEE ALSO:

Develop and Distribute Apex for Managed Packages

##### Serializing and Deserializing ConnectApi Objects

When `ConnectApi` output objects are serialized into JSON, the structure is similar to the JSON returned from Connect REST API.
When `ConnectApi` input objects are deserialized from JSON, the format is also similar to Connect REST API.


Apex Developer Guide Using Salesforce Features with Apex

Connect in Apex supports serialization and deserialization in these Apex contexts.

**•** `JSON` and `JSONParser` classes—serialize Connect in Apex outputs to JSON and deserialize Connect in Apex inputs from JSON.

**•** Apex REST with `@RestResource` —serialize Connect in Apex outputs to JSON as return values and deserialize Connect in Apex
inputs from JSON as parameters.

**•** JavaScript Remoting with `@RemoteAction` —serialize Connect in Apex outputs to JSON as return values and deserialize Connect
in Apex inputs from JSON as parameters.

Connect in Apex follows these rules for serialization and deserialization.

**•** Only output objects can be serialized.

**•** Only top-level input objects can be deserialized.

**•** Enum values and exceptions cannot be serialized or deserialized.

##### ConnectApi Versioning and Equality Checking Versioning in ConnectApi classes follows specific rules that are different than the rules for other Apex classes. Versioning for ConnectApi classes follows these rules. • A ConnectApi method call executes in the context of the version of the class that contains the method call. The use of version

is analogous to the `/v` _**`XX`**_ `.` _**`X`**_ section of a Connect REST API URL.

##### • Each ConnectApi output object exposes a getBuildVersion method. This method returns the version under which the

method that created the output object was invoked.

**•** When interacting with input objects, Apex can access only properties supported by the version of the enclosing Apex class.

##### • Input objects passed to a ConnectApi method may contain only non-null properties that are supported by the version of the

Apex class executing the method. If the input object contains version-inappropriate properties, an exception is thrown.

**•** The output of the `toString` method only returns properties that are supported in the version of the code interacting with the
object. For output objects, the returned properties must also be supported in the build version.

**•** Apex REST, `JSON.serialize`, and `@RemoteAction` serialization include only version-appropriate properties.

**•** Apex REST, `JSON.deserialize`, and `@RemoteAction` deserialization reject properties that are version-inappropriate.

**•** Enums are not versioned. Enum values are returned in all API versions. Clients should handle values they don't understand gracefully.

##### Equality checking for ConnectApi classes follows these rules.

**•** Input objects—properties are compared.

**•** Output objects—properties and build versions are compared. For example, if two objects have the same properties with the same
values but have different build versions, the objects are not equal. To get the build version, call `getBuildVersion` .

##### Casting ConnectApi Objects It may be useful to downcast some ConnectApi output objects to a more specific type.

This technique is especially useful for message segments, feed item capabilities, and record fields. Message segments in a feed item are
typed as `ConnectApi.MessageSegment` . Feed item capabilities are typed as `ConnectApi.FeedItemCapability` .
Record fields are typed as `ConnectApi.AbstractRecordField` . These classes are all abstract and have several concrete
subclasses. At runtime you can use `instanceof` to check the concrete types of these objects and then safely proceed with the
corresponding downcast. When you downcast, you must have a default case that handles unknown subclasses.


Apex Developer Guide Using Salesforce Features with Apex

The following example downcasts a `ConnectApi.MessageSegment` to a `ConnectApi.MentionSegment` :

```
   if(segment instanceof ConnectApi.MentionSegment) {

    ConnectApi.MentionSegment = (ConnectApi.MentionSegment)segment;

   }

```

Important: The composition of a feed can change between releases. Write your code to handle instances of unknown subclasses.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

_Apex Reference Guide_ [: ConnectApi.FeedElementCapabilities](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_feed_element_capabilities.htm)

_Apex Reference Guide_ [: ConnectApi.MessageSegment](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_msg_seg.htm)

_Apex Reference Guide_ [: ConnectApi.AbstractRecordView](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_connectapi_output_abstractRecordView.htm)

##### Wildcards

Use wildcard characters to match text patterns in Connect REST API and Connect in Apex searches.

A common use for wildcards is searching a feed. Pass a search string and wildcards in the `q` parameter. This example is a Connect REST
API request:

```
   /chatter/feed-elements?q=chat*

```

This example is a Connect in Apex method call:

```
   ConnectApi.ChatterFeeds.searchFeedElements(null, 'chat*');

```

You can specify the following wildcard characters to match text patterns in your search:

##### **Wildcard Description**

Asterisks match zero or more characters at the middle or end of your search term. For example, a search for _john*_
finds items that start with _john_, such as, _john_, _johnson_, or _johnny_ . A search for _mi* meyers_ finds items with _mike_
_meyers_ or _michael meyers_ .

If you are searching for a literal asterisk in a word or phrase, then escape the asterisk (precede it with the `\` character).

? Question marks match only one character in the middle or end of your search term. For example, a search for _jo?n_
finds items with the term _john_ or _joan_ but not _jon_ or _johan_ . You can't use a ? in a lookup search.

When using wildcards, consider the following notes:

**•** The more focused your wildcard search, the faster the search results are returned, and the more likely the results will reflect your
intention. For example, to search for all occurrences of the word `prospect` (or `prospects`, the plural form), it is more efficient
to specify `prospect*` in the search string than to specify a less restrictive wildcard search (such as `prosp*` ) that could return
extraneous matches (such as `prosperity` ).

**•** Tailor your searches to find all variations of a word. For example, to find `property` and `properties`, you would specify
`propert*` .

**•** Punctuation is indexed. To find `*` or `?` inside a phrase, you must enclose your search string in quotation marks and you must escape
the special character. For example, `"where are you\?"` finds the phrase `where are you?` . The escape character ( `\` ) is
required in order for this search to work correctly.


Apex Developer Guide Using Salesforce Features with Apex

##### Testing ConnectApi Code

Like all Apex code, Connect in Apex code requires test coverage.

Connect in Apex methods run in the context of the current user (also called the _context user_ ). The methods have access to whatever the
context user has access to. Connect in Apex doesn’t support the `runAs` system method.

Most Connect in Apex methods require access to real org data, and fail unless used in test methods marked

`@IsTest(SeeAllData=true)` .

However, some Connect in Apex methods, such as `getFeedElementsFromFeed`, are not permitted to access org data in tests
and must be used with special test methods that register outputs to be returned in a test context. If a method requires a `setTest`
method, the requirement is stated in the method’s “Usage” section.

A test method name is the regular method name with a `setTest` prefix. The test method signature (combination of parameters)
matches a signature of the regular method. For example, if the regular method has three overloads, the test method has three overloads.

Using Connect in Apex test methods is similar to testing web services in Apex. First, build the data you expect the method to return. To
build data, create output objects and set their properties. To create objects, you can use no-argument constructors for any non-abstract
output classes. If you’re testing binary input parameters, use the same instance for creating and executing data.

After you build the data, call the test method to register the data. Call the test method that has the same signature as the regular method
you’re testing.

After you register the test data, run the regular method. When you run the regular method, the registered data is returned.

Important: Use the test method signature that matches the regular method signature. If data wasn't registered with the matching
set of parameters when you call the regular method, you receive an exception.

This example shows a test that constructs an `ConnectApi.FeedElementPage` and registers it to be returned when
`getFeedElementsFromFeed` is called with a particular combination of parameters.

```
   global class NewsFeedClass {

      global static Integer getNewsFeedCount() {

        ConnectApi.FeedElementPage elements =

           ConnectApi.ChatterFeeds.getFeedElementsFromFeed(null,

             ConnectApi.FeedType.News, 'me');

        return elements.elements.size();

      }

   }

   @isTest

   private class NewsFeedClassTest {

      @IsTest

      static void doTest() {

        // Build a simple feed item

        ConnectApi.FeedElementPage testPage = new ConnectApi.FeedElementPage();

        List<ConnectApi.FeedItem> testItemList = new List<ConnectApi.FeedItem>();

        testItemList.add(new ConnectApi.FeedItem());

        testItemList.add(new ConnectApi.FeedItem());

        testPage.elements = testItemList;

        // Set the test data

        ConnectApi.ChatterFeeds.setTestGetFeedElementsFromFeed(null,

           ConnectApi.FeedType.News, 'me', testPage);

        // The method returns the test page, which we know has two items in it.

        Test.startTest();

```


Apex Developer Guide Using Salesforce Features with Apex

```
        System.assertEquals(2, NewsFeedClass.getNewsFeedCount());

        Test.stopTest();

      }

   }

```

SEE ALSO:

Testing Apex

##### Differences Between ConnectApi Classes and Other Apex Classes

Note these additional differences between `ConnectApi` classes and other Apex classes.

**User mode**
Connect in Apex methods run in the context of the current user (also called the _context user_ ). The methods have access to whatever
the context user has access to. Connect in Apex doesn’t support the `runAs` system method. When a method takes a _`subjectId`_
argument, often that subject must be the context user. In these cases, you can use the string `me` to specify the context user instead
of an ID.

Connect in Apex isn’t available to Automated Process users by default. Connect in Apex is available to these users:

**•** Chatter-only users

**•** Guest users

**•** Portal users

**•** Standard users

**`with sharing`** **and** **`without sharing`**
Connect in Apex ignores the `with sharing` and `without sharing` keywords. Instead, the context user controls all security,
field level sharing, and visibility. For example, if the context user is a member of a private group, `ConnectApi` classes can post
to that group. If the context user is not a member of a private group, the code can’t see the feed items for that group and can’t post
to the group.

**Asynchronous operations**
Some Connect in Apex operations are asynchronous, that is, they don’t occur immediately. For example, if your code adds a feed
item for a user, it isn’t immediately available in the news feed. Another example: when you add a photo, it’s not available immediately.
For testing, if you add a photo, you can’t retrieve it immediately.

**No XML support in Apex REST**
Apex REST doesn’t support XML serialization and deserialization of Connect in Apex objects. Apex REST does support JSON serialization
and deserialization of Connect in Apex objects.

**Empty log entries**
Information about Connect in Apex objects doesn’t appear in `VARIABLE_ASSIGNMENT` log events.

**No Apex SOAP web services support**
Connect in Apex objects can’t be used in Apex SOAP web services indicated with the keyword `webservice` .


Apex Developer Guide Using Salesforce Features with Apex

#### Moderate Chatter Private Messages with Triggers

Write a trigger for ChatterMessage to automate the moderation of private messages in an org or
Experience Cloud site. Use triggers to ensure that messages conform to your company’s messaging
policies and don’t contain blocklisted words.

Write an Apex _before insert_ trigger to review the private message body and information about the
sender. You can add validation messages to the record or the Body field, which causes the message
to fail and an error to be returned to the user.

Although you can create an _after insert_ trigger, ChatterMessage is not updatable, and consequently
any _after insert_ trigger that modifies ChatterMessage will fail at run time with an appropriate error
message.

To create a trigger for private messages from Setup, enter _`ChatterMessage Triggers`_ in
the `Quick Find` box, then select **ChatterMessage Triggers** . Alternatively, you can create a
trigger from the Developer Console by clicking **File** - **New** - **Apex Trigger** and selecting
ChatterMessage from the **sObject** drop-down list.

This table lists the fields that are exposed on ChatterMessage.

**Table 9: Available Fields in ChatterMessage**

EDITIONS

Available in: Salesforce
Classic

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

USER PERMISSIONS

User permissions needed to
save Apex triggers for
ChatterMessage:

**•** Author Apex

AND

Manage Chatter
Messages and Direct
Messages

This example shows a _before insert_ trigger on ChatterMessage that is used to review each new message. This trigger calls a class method,
`moderator.review()`, to review each new message before it is inserted.

```
trigger PrivateMessageModerationTrigger on ChatterMessage (before insert) {

   ChatterMessage[] messages = Trigger.new;

   // Instantiate the Message Moderator using the factory method

   MessageModerator moderator = MessageModerator.getInstance();

   for (ChatterMessage currentMessage : messages) {

     moderator.review(currentMessage);

   }

}

```

If a message violates your policy, for example when the message body contains blocklisted words, you can prevent the message from
being sent by calling the Apex `addError` method. You can call `addError` to add a custom error message on a field or on the


Apex Developer Guide Using Salesforce Features with Apex

entire message. The following snippet shows a portion of the `reviewContent` method that adds an error to the message `Body`
field.

```
         if (proposedMsg.contains(nextBlockListedWord)) {

           theMessage.Body.addError(

              'This message does not conform to the acceptable use policy');

           System.debug('moderation flagged message with word: '

              + nextBlockListedWord);

           problemsFound=true;

           break;

         }

```

The following is the full `MessageModerator` class, which contains methods for reviewing the sender and the content of messages.
Part of the code in this class has been deleted for brevity.

```
   public class MessageModerator {

     private Static List<String> blocklistedWords=null;

     private Static MessageModerator instance=null;

     /**

      Overall review includes checking the content of the message,

      and validating that the sender is allowed to send messages.

     **/

     public void review(ChatterMessage theMessage) {

      reviewContent(theMessage);

      reviewSender(theMessage);

     }

     /**

      This method is used to review the content of the message. If the content

      is unacceptable, field level error(s) are added.

     **/

     public void reviewContent(ChatterMessage theMessage) {

       // Forcing to lower case for matching

       String proposedMsg=theMessage.Body.toLowerCase();

       boolean problemsFound=false; // Assume it's acceptable

       // Iterate through the blocklist looking for matches

       for (String nextBlockListedWord : blocklistedWords) {

         if (proposedMsg.contains(nextBlockListedWord)) {

           theMessage.Body.addError(

              'This message does not conform to the acceptable use policy');

           System.debug('moderation flagged message with word: '

              + nextBlockListedWord);

           problemsFound=true;

           break;

         }

         }

        // For demo purposes, we're going to add a "seal of approval" to the

        // message body which is visible.

        if (!problemsFound) {

         theMessage.Body = theMessage.Body +

           ' *** approved, meets conduct guidelines';

        }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

     /**

      Is the sender allowed to send messages in this context?

      -- Moderators -- always allowed to send

      -- Internal Members -- always allowed to send

      -- Site Members -- in general only allowed to send if they have

          a sufficient Reputation

      -- Site Members -- with insufficient reputation may message the

          moderator(s)

     **/

     public void reviewSender(ChatterMessage theMessage) {

       // Are we in a Site Context?

       boolean isSiteContext = (theMessage.SendingNetworkId != null);

       // Get the User

       User sendingUser = [SELECT Id, Name, UserType, IsPortalEnabled

                   FROM User where Id = :theMessage.SenderId ];

       // ...

     }

     /**

      Enforce a singleton pattern to improve performance

     **/

     public static MessageModerator getInstance() {

      if (instance==null) {

        instance = new MessageModerator();

      }

      return instance;

     }

     /**

      Default contructor is private to prevent others from instantiating this class

      without using the factory.

      Initializes the static members.

     **/

     private MessageModerator() {

       initializeBlockList();

     }

     /**

      Helper method that does the "heavy lifting" to load up the dictionaries

      from the database.

      Should only run once to initialize the static member which is used for

      subsequent validations.

     **/

     private void initializeBlockList() {

       if (blocklistedWords==null) {

         // Fill list of blocklisted words

         // ...

       }

     }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

#### Data 360 In Apex

You can use Apex with Data 360 objects, with constraints and considerations that are detailed in this topic . Further, you can mock SOQL
query responses for Data 360 data model objects (DMOs) in Apex testing by using SOQL stub methods and a test class.

Using SOQL in Apex with Data 360 Objects

Static SOQL is supported with Data 360 data model objects (DMOs) as a more direct alternative to using either dynamic SOQL or
ConnectAPI. Additionally, SOQL queries against DMOs using Apex `Database.QueryLocator` or in FOR loops is supported in API
version 61.0 and later. In versions earlier than 61.0, only the first 201 records are returned. Batch Apex is blocked against DMOs when
using `QueryLocators`, but is supported when using `Iterable` .

Warning: Running SOQL queries against DMOs can result in Data Services credits being consumed from your Data 360 subscription.
[For more information on how usage is billed, see Data 360 Billable Usage Types. Use caution when using FOR loops, query locators,](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US)
recursion, or any mechanism that can result in multiple queries to Data 360.

A static SOQL query against Data 360 from Apex is considered a callout and is subject to the same restrictions as HTTP callouts from
Apex. For example, if there is pending DML, this sample code can result in an unexpected exception with this message:

```
   UnexpectedException: A callout was unsuccessful because of pending uncommitted work

   related to a process, flow, or Apex operation. Commit or roll back the work, and then

   try again.

   insert new Account(Name='Test');

   List<ssot_Account_dlm> dmo1 = [Select Id from ssot_Account_dlm];

```

Security Considerations

You must consider field- and record-level access when using Apex with Data 360 data model objects (DMOs). DMOs in all data spaces
are accessible from Apex in system mode, even when a permission set for the data space isn’t explicitly assigned. Read-only object-level
access checks are supported if the user has access to the data space. There’s currently no support for field-level security or for record-level
access control. Apex features, such as WITH USER_MODE, WITH SECURITY_ENFORCED, describe calls, and
`Security.stripInaccessible()`, can check only object-level access for DMOs.

Starting with API version 61.0, you can get information on a specific DMO using `SObjectType.getDescribe()` . There’s no
field-level security to be enforced because all fields on DMOs that are accessed by field describes and security model checks are read
only. You can’t use `Schema.getGlobalDescribe()` to discover exposed DMOs. Instead, use the
`Schema.describeSObjects(List<String>)` method with the known DMO API names.

This example uses static SOQL with the _`UnifiedIndividual__dlm`_ Data 360 object.

```
   //Static SOQL example

   List<UnifiedIndividual__dlm> unifiedIndividuals = [

       SELECT

        Id,

        ssot__FirstName__c,

        ssot__LastName__c,

        ssot__Email__c,

        ssot__SkyMilesBalance__c,

        ssot__MedallionStatus__c

       FROM UnifiedIndividual__dlm

       WHERE ssot__CompanyId__c = :companyId

      ];

```


Apex Developer Guide Using Salesforce Features with Apex

##### Mock SOQL Tests for Data 360 Data Model Objects

You can mock SOQL query responses for Data 360 data model objects (DMOs) in Apex testing by using the new SOQL stub methods
and a new test class. Use static or dynamic SOQL queries against DMOs and return mock records in a testing context.

##### Mock SOQL Tests for Data 360 Data Model Objects

You can mock SOQL query responses for Data 360 data model objects (DMOs) in Apex testing by using the new SOQL stub methods
and a new test class. Use static or dynamic SOQL queries against DMOs and return mock records in a testing context.

Create mock test classes by extending the new `System.SoqlStubProvider` class and overriding the `handleSoqlQuery()`
class method. Create DMO instances using either `Test.createStubQueryRow()` or `Test.createStubQueryRows()` .
Register the mock provider in the test using `Test.createSoqlStub()` and execute the test code.

Note: Apex governor limits apply to the stubbed records.

The SOQL query must be against a DMO or an external object, either directly with a FROM clause or via a subquery. If you query against
a stubbed object type that doesn’t include a DMO or an external object, the error `Stubbed query invocations can't be`
`used without a participating query stub set.` is thrown.

These features are not allowed within a stub implementation:

**•** SOQL

**•** SOSL

**•** Callouts

**•** Future methods

**•** Queueable Jobs

**•** Batch Jobs

**•** DML

**•** Platform Events

This example shows a mock test class for the _`SkyMilesForBusinessOptInController`_ class.

```
   @IsTest

   public class SkyMilesForBusinessOptInController_Test {

      @IsTest

      public static void mockSoql() {

        SoqlStubProvider stub = new UnifiedIndividualSoqlStub();

        Test.createSoqlStub(UnifiedIndividual__dlm.sObjectType, stub);

        Assert.isTrue(Test.isSoqlStubDefined(UnifiedIndividual__dlm.sObjectType));

        Test.startTest();

        string companyId = 'SampleCompanyId';

        // Performs SOQL query against Data Model Object

        List<SkyMilesMember> members =

   SkyMilesForBusinessOptInController.getSkyMilesProfilesFromDataCloud(companyId);

        Test.stopTest();

        Assert.areEqual(1, members.size());

```


Apex Developer Guide Using Salesforce Features with Apex

```
        SkyMilesMember member = members[0];

        Assert.areEqual(companyId, member.CompanyId);

        Assert.areEqual(5000, member.SkyMilesBalance);

      }

      class UnifiedIndividualSoqlStub extends SoqlStubProvider {

       public override List<sObject> handleSoqlQuery(sObjectType sot, string stubbedQuery,

    Map<string, object> bindVars) {

           Assert.areEqual(UnifiedIndividual__dlm.sObjectType, sot);

          // Stub assumes that the SOQL query is searching for a single record by company

    id

           string companyId = 'Default';

           if(bindVars.containsKey('tmpVar1')) {

             companyId = (string)bindVars.get('tmpVar1');

           }

          UnifiedIndividual__dlm dmo = (UnifiedIndividual__dlm)Test.createStubQueryRow(

             sot,

             new Map<string, object> {

               'ssot__FirstName__c' => 'Codey',

               'ssot__LastName__c' => 'Bear',

               'ssot__Email__c' => 'developer@salesforce.com',

               'ssot__SkyMilesBalance__c' => 5000,

               'ssot__MedallionStatus__c' => 'Gold',

               'ssot__CompanyId__c' => companyId

              }

           );

           return new List<sObject> { dmo };

        }

      }

   }

   public with sharing class SkyMilesForBusinessOptInController {

      public static List<SkyMilesMember> getSkyMilesProfilesFromDataCloud(String companyId)

    {

        List<UnifiedIndividual__dlm> unifiedIndividuals = [

         SELECT

           Id,

           ssot__FirstName__c,

           ssot__LastName__c,

           ssot__Email__c,

           ssot__SkyMilesBalance__c,

           ssot__MedallionStatus__c,

           ssot__CompanyId__c

         FROM UnifiedIndividual__dlm

         WHERE ssot__CompanyId__c = :companyId

        ];

        List<SkyMilesMember> skyMilesMembers = new List<SkyMilesMember>();

```


Apex Developer Guide Using Salesforce Features with Apex

```
        for (UnifiedIndividual__dlm individual : unifiedIndividuals) {

         skyMilesMembers.add(

           new SkyMilesMember(

            individual.Id,

            individual.ssot__FirstName__c,

            individual.ssot__LastName__c,

            individual.ssot__Email__c,

            individual.ssot__SkyMilesBalance__c,

            individual.ssot__MedallionStatus__c,

            individual.ssot__CompanyId__c

           )

         );

        }

        return skyMilesMembers;

      }

   }

```

SEE ALSO:

_Apex Reference Guide:_ [SoqlStubProvider Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_SoqlStubProvider.htm)

#### DataWeave in Apex DataWeave in Apex uses the Mulesoft DataWeave library to read and parse data from one format, transform it, and export it in a different

format. You can create DataWeave scripts as metadata and invoke them directly from Apex. Like Apex, DataWeave scripts are run within
Salesforce application servers, enforcing the same heap and CPU limits on the executing code.

Enterprise applications often require transformation of data between formats such as CSV, JSON, XML, and Apex objects. DataWeave in
Apex complements native Apex support for JSON and XML processing, and makes data transformation easier to code, more scalable,
and efficient. Apex developers can focus more on solving business problems and less on addressing the specifics of file formats.

DataWeave is the MuleSoft expression language for accessing, parsing, and transforming data that travels through a Mule application.
[For detailed information, see DataWeave Overview.](https://docs.mulesoft.com/mule-runtime/4.3/dataweave)

Note: You don’t have to be a MuleSoft customer or have any specific Salesforce license to use DataWeave in Apex.

The following are some use-cases for DataWeave in Apex.

**•** Serializing Apex objects with custom date formats

**•** Serializing and deserializing JSON with Apex reserved keywords

**•** Performing custom transformations like removing or adding namespaces or removing `__c` suffixes

**•** Parsing and transforming RFC 4180-compliant CSV (Comma-Separated Values) data

You can create a listview for DataWeave resources in your org and view deployed DataWeave scripts within your namespace. From
#### Setup, in the Quick Find box, enter DataWeave, and then select DataWeave Resources . Select the fields that you want to monitor,

such as the DataWeave Resource ID, Name, Namespace Prefix, and API Version.

Implementing DataWeave in Apex
Create DataWeave scripts as metadata and invoke them directly from Apex. Use class methods and exceptions in the DataWeave
namespace to load and execute the scripts.


Apex Developer Guide Using Salesforce Features with Apex

Examples of DataWeave in Apex
Here are code samples that demonstrate DataWeave in Apex.

Limitations of DataWeave in Apex
DataWeave in Apex has these limitations.

SEE ALSO:

_Apex Reference Guide_ [: DataWeave Namespace](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_dataweave.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_dataweaveresource.htm)_ : DataWeaveResource

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/packaging_packageable_components.htm#mdc_dataweaveresource)_ : DataWeaveResource

##### Implementing DataWeave in Apex

Create DataWeave scripts as metadata and invoke them directly from Apex. Use class methods and exceptions in the DataWeave
namespace to load and execute the scripts.

DataWeave Namespace

The DataWeave namespace provides classes and methods to support the invocation of DataWeave scripts from Apex. The `Script`
class contains the `createScript()` method to load DataWeave scripts from `.dwl` metadata files that have been deployed to an
org. The resulting script can then be run with a payload using the `execute()` method to obtain script output in a
`DataWeave.Result` object. The `Result` class contains methods to retrieve script output using `Script` class methods. For
[more information on these classes and methods, see DataWeave Namespace.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_DataWeave.htm)

For every DataWeave script, an inner class of type `DataWeaveScriptResource.ScriptName` is generated. The inner class
extends the `DataWeave.Script` class. You can use the generated `DataWeaveScriptResource.ScriptName` class
instead of using the actual script name via the `createScript()` method. DataWeave scripts that are currently being referenced
via this inner class can't be deleted. To make the generated DataWeaveScriptResource class global, set the `isGlobal` field in the
`DataWeaveResource` metadata object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataWeaveResource xmlns="http://soap.sforce.com/2006/04/metadata">

   <apiVersion>58.0</apiVersion>

   <isGlobal>true</isGlobal>

   </DataWeaveResource>

```

The catchable `System.DataWeaveScriptException` exception is available for error handling. Runtime script exceptions that
occur within DataWeave are exposed to Apex with this exception type.

DataWeave scripts support logging using the `log(string, value)` function. Log messages that originate from DataWeave are
reflected in Apex debug logs as `DATAWEAVE_USER_DEBUG` events, under the Apex Code log category at the DEBUG log level.

Supporting Information

These tools support the development of DataWeave scripts.

**•** [DataWeave Interactive Learning is an online interactive playground that you can use to test your DataWeave scripts.](https://sfdc.co/dwlangfun)

**•** [DataWeave 2.0 VSCode marketplace extension adds code highlighting and other feature support for editing DataWeave scripts.](https://marketplace.visualstudio.com/items?itemName=MuleSoftInc.dataweave)

Versioned Behavior Changes

These versions of DataWeave script syntax are supported in Apex.


Apex Developer Guide Using Salesforce Features with Apex

**•** [API version 61.0 and earlier: DataWeave 2.5](https://docs.mulesoft.com/dataweave/2.5/)

**•** [API version 62.0: DataWeave 2.8](https://docs.mulesoft.com/dataweave/2.8/)

**•** [API version 63.0 and later: DataWeave 2.9](https://docs.mulesoft.com/dataweave/2.9/)

SEE ALSO:

[Limitations of DataWeave in Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex_limitations.htm)

##### Examples of DataWeave in Apex

Here are code samples that demonstrate DataWeave in Apex.

To use DataWeave in Apex, follow these instructions with associated examples.

**•** Create a DataWeave script source file.

For example: `csvToContacts.dwl` .

```
     %dw 2.0

     input records application/csv

     output application/apex

     --
     records map(record) -> {

      FirstName: record.first_name,

      LastName: record.last_name,

      Email: record.email

     } as Object {class: "Contact"}

```

**•** Create the associated metadata file.

For example: `csvToContacts.dwl-meta.xml` .

```
     <?xml version="1.0" encoding="UTF-8"?>

     <DataWeaveResource xmlns="http://soap.sforce.com/2006/04/metadata">

       <apiVersion>58.0</apiVersion>

       <isGlobal>false</isGlobal>

     </DataWeaveResource>

```

**•** [Push the source to the scratch org using Salesforce CLI version v7.151.9 or higher. See Salesforce CLI Release Notes.](https://github.com/forcedotcom/cli/blob/main/releasenotes/sfdx/README.md#71511-may-19-2022)

**•** Invoke the DataWeave script from Apex and check the results from anonymous Apex.

This example invokes the `csvToContacts.dwl` script.

```
     // CSV data for Contacts

     String inputCsv = 'first_name,last_name,email\nCodey,"The Bear",codey@salesforce.com';

     DataWeave.Script dwscript = new DataWeaveScriptResource.csvToContacts();

     DataWeave.Result dwresult = dwscript.execute(new Map<String, Object>{'records' =>

     inputCsv});

     List<Contact> results = (List<Contact>)dwresult.getValue();

     Assert.areEqual(1, results.size());

     Contact codeyContact = results[0];

     Assert.areEqual('Codey',codeyContact.FirstName);

     Assert.areEqual('The Bear',codeyContact.LastName);

```

[Note: Extensive code samples that demonstrate the DataWeave in Apex feature are available on Developerforce.](https://github.com/developerforce/DataWeaveInApex)


Apex Developer Guide Using Salesforce Features with Apex

##### Limitations of DataWeave in Apex

DataWeave in Apex has these limitations.

**•** [The DataWeave Java bridge, that is, the ability to bind to static Java methods is disabled. See Introduction to Mule 4. Features that](https://docs.mulesoft.com/mule-runtime/4.2/intro-java-integration)
interact with the environment such as the `readURL` and `envVar` functions are also disabled. These checks are done at script
creation time instead of at runtime.

**•** You must specify an encoding for binary input (Apex Blobs) to be coerced to strings: `binaryVariable as String`
`{encoding: 'utf8' }"` .

**•** DataWeave is constrained to disallow the loading of additional libraries. Therefore, scripts must be self-contained.

**•** DataWeave modules and importing other scripts aren’t supported. For example, `import modules::MyMapping` as per
[Using a Mapping File in a DataWeave Script isn’t supported.](https://docs.mulesoft.com/dataweave/2.4/dataweave-create-module#using-a-mapping-file-in-a-dataweave-script)

[Note: The feature supports built-in modules. See DataWeave Reference.](https://docs.mulesoft.com/dataweave/2.3/dw-functions)

**•** DataWeave in Apex doesn’t support these content types.

**–** [Flat File Format (](https://docs.mulesoft.com/dataweave/2.4/dataweave-formats-flatfile) `application/flatfile` )

**–** [Excel (](https://docs.mulesoft.com/dataweave/2.4/dataweave-formats-excel) `application/xlsx` )

**–** [Avro (](https://docs.mulesoft.com/dataweave/2.4/dataweave-formats-avro) `application/avro` )

**•** Apex classes must be at API version 53.0 or later to access DataWeave integration methods.

**•** There’s a maximum of 50 DataWeave scripts per org.

**•** The maximum body size of one DataWeave script is 100,000 (one hundred thousand) characters.

Note: XML Entity Expansion isn’t supported, either currently or in the future, as a guard against denial of service attacks.

#### Moderate Feed Items with Triggers


Apex Developer Guide Using Salesforce Features with Apex

```
        }

      }

   }

#### Experience Cloud Sites

```

Experience Cloud sites are branded spaces for your employees, customers, and partners to connect. You can customize and create sites
to meet your business needs, then transition seamlessly between them.

Interact with Experience Cloud sites in Apex using the `Network` class and using Connect in Apex classes in the `ConnectApi`
namespace.

Connect in Apex has a `ConnectApi.Communities` class with methods that return information about sites. Many Connect in
Apex methods take a _`communityId`_ argument, and some Connect in Apex methods take a _`siteId`_ argument.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_network.htm)_ : Network Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_connect_api.htm)_ : Connect in Apex

#### Email

You can use Apex to work with inbound and outbound email.

Use Apex with these email features:

##### Inbound Email

Use Apex to work with email sent to Salesforce.

##### Outbound Email

Use Apex to work with email sent from Salesforce.

##### Inbound Email

Use Apex to work with email sent to Salesforce.

You can use Apex to receive and process email and attachments. The email is received by the Apex email service, and processed by
Apex classes that utilize the InboundEmail object.

Note: The Apex email service is only available in Developer, Enterprise, Unlimited, and Performance Edition organizations.

See Apex Email Service.

##### Outbound Email

Use Apex to work with email sent from Salesforce.

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

You can use Apex to send individual and mass email. The email can include all standard email attributes (such as subject line and blind
carbon copy address), use Salesforce email templates, and be in plain text or HTML format, or those generated by Visualforce.


Apex Developer Guide Using Salesforce Features with Apex

Note: Visualforce email templates cannot be used for mass email.

You can use Salesforce to track the status of email in HTML format, including the date the email was sent, first opened and last opened,
and the total number of times it was opened.

To send individual and mass email with Apex, use the following classes:

**[SingleEmailMessage](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_outbound_single.htm)**

Instantiates an email object used for sending a single email message. The syntax is:

```
     Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

```

**[MassEmailMessage](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_outbound_mass.htm)**

Instantiates an email object used for sending a mass email message. The syntax is:

```
     Messaging.MassEmailMessage mail = new Messaging.MassEmailMessage();

```

**[Messaging](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_outbound_messaging.htm)**

Includes the static `sendEmail` method, which sends the email objects you instantiate with either the `SingleEmailMessage`
or `MassEmailMessage` classes, and returns a SendEmailResult object.

The syntax for sending an email is:

```
     Messaging.sendEmail(new Messaging. Email [] { mail }, opt_allOrNone );

```

where `Email` is either `Messaging.SingleEmailMessage` or `Messaging.MassEmailMessage` .

The optional _`opt_allOrNone`_ parameter specifies whether `sendEmail` prevents delivery of all other messages when any of
the messages fail due to an error ( `true` ), or whether it allows delivery of the messages that don't have errors ( `false` ). The default
is `true` .

Includes the static `reserveMassEmailCapacity` and `reserveSingleEmailCapacity` methods, which can be
called before sending any emails to ensure that the sending organization doesn’t exceed its daily email limit when the transaction
is committed and emails are sent. The syntax is:

```
     Messaging.reserveMassEmailCapacity( count );

```

and

```
     Messaging.reserveSingleEmailCapacity( count );

```

where _**`count`**_ indicates the total number of addresses that emails will be sent to.

Note the following:

**•** The email is not sent until the Apex transaction is committed.

**•** The email address of the user calling the `sendEmail` method is inserted in the `From Address` field of the email header. All
email that is returned, bounced, or received out-of-office replies goes to the user calling the method.

**•** Maximum of 10 `sendEmail` [methods per transaction. Use the Limits methods to verify the number of](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_limits.htm) `sendEmail` methods
in a transaction.

**•** Single email messages sent with the `sendEmail` method count against the sending organization's daily single email limit. When
this limit is reached, calls to the `sendEmail` method using `SingleEmailMessage` are rejected, and the user receives a
`SINGLE_EMAIL_LIMIT_EXCEEDED` error code. However, single emails sent through the application are allowed.

**•** Mass email messages sent with the `sendEmail` method count against the sending organization's daily mass email limit. When
this limit is reached, calls to the `sendEmail` method using `MassEmailMessage` are rejected, and the user receives a
`MASS_MAIL_LIMIT_EXCEEDED` error code.

**•** Any error returned in the SendEmailResult object indicates that no email was sent.


Apex Developer Guide Using Salesforce Features with Apex

`Messaging.SingleEmailMessage` has a method called `setOrgWideEmailAddressId` . It accepts an object ID to an
`OrgWideEmailAddress` object. If `setOrgWideEmailAddressId` is passed a valid ID, the
`OrgWideEmailAddress.DisplayName` field is used in the email header, instead of the logged-in user's `Display Name` .
The sending email address in the header is also set to the field defined in `OrgWideEmailAddress.Address` .

Note: If both `OrgWideEmailAddress.DisplayName` and `setSenderDisplayName` are defined, the user receives
a `DUPLICATE_SENDER_DISPLAY_NAME` error.

For more information, see _Organization-Wide Email Addresses_ in the Salesforce Help .

Example

```
   // First, reserve email capacity for the current Apex transaction to ensure

   // that we won't exceed our daily email limits when sending email after

   // the current transaction is committed.

   Messaging.reserveSingleEmailCapacity(2);

   // Processes and actions involved in the Apex transaction occur next,

   // which conclude with sending a single email.

   // Now create a new single email message object

   // that will send out a single email to the addresses in the To, CC & BCC list.

   Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

   // Strings to hold the email addresses to which you are sending the email.

   String[] toAddresses = new String[] {'user@acme.com'};

   String[] ccAddresses = new String[] {'smith@gmail.com'};

   // Assign the addresses for the To and CC lists to the mail object.

   mail.setToAddresses(toAddresses);

   mail.setCcAddresses(ccAddresses);

   // Specify the address used when the recipients reply to the email.

   mail.setReplyTo('support@acme.com');

   // Specify the name used as the display name.

   mail.setSenderDisplayName('Salesforce Support');

   // Specify the subject line for your email address.

   mail.setSubject('New Case Created : ' + case.Id);

   // Set to True if you want to BCC yourself on the email.

   mail.setBccSender(false);

   // Optionally append the Salesforce email signature to the email.

   // The email address of the user executing the Apex Code will be used.

   mail.setUseSignature(false);

   // Specify the text content of the email.

   mail.setPlainTextBody('Your Case: ' + case.Id +' has been created.');

   mail.setHtmlBody('Your case:<b> ' + case.Id +' </b>has been created.<p>'+

      'To view your case <a href=https:// MyDomainName .my.salesforce.com/'+case.Id+'>click

```


Apex Developer Guide Using Salesforce Features with Apex

```
    here.</a>');

   // Send the email you have created.

   Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

#### External Services External Services connect your Salesforce org to a service outside of Salesforce, such as an employee banking service. After you register
```

the external service, you can call it natively in your Apex code. Objects and operations defined in the external service's registered API
specification become Apex classes and methods in the `ExternalService` namespace. The registered service's schema types map
to Apex types, and are strongly typed, making the Apex compiler do the heavy lifting for you. For example, you can make a type safe
callout to an external service from Apex without needing to use the `Http` class or perform transforms on JSON strings.

SEE ALSO:

_Salesforce Help_ [: Invoke External Service Callouts Using Apex](https://help.salesforce.com/s/articleView?id=platform.external_services_apex_invoking.htm&type=5&language=en_US)

#### Flows

Flow Builder lets admins build applications, known as _flows_, that automate a business process. Flows collect data and perform actions
in your Salesforce org or an external system.

For example, you can create a flow to script calls for a customer support center or to generate real-time quotes for a sales team. You can
embed a flow in a Visualforce page or Aura component and access it in an Apex controller.

[For more information about how to start a flow from Apex, see Apex Reference Guide: Interview Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/flow_interview_class.htm#flow_interview_class)

You can customize how your Apex invocable actions appear and behave in Flow Builder by using the InvocableActionExtension metadata
file. Control input parameter order and grouping, provide picklist values, add custom headers, and create partial custom property editors
for improved configuration experiences. For more information, see Extend Invocable Action Configuration in Flow Builder on page 483.

##### Getting Flow Variables

You can retrieve flow variables for a specific flow in Apex.

Making Callouts to External Systems from Invocable Actions
When you define a method that runs as an invocable action in a screen flow and makes a callout to an external system, use the

`callout` modifier.

Extend Invocable Action Configuration in Flow Builder
Simplify the configuration of Apex invocable actions in Flow Builder by using the InvocableActionExtension metadata file. Create
partial custom property editors for one or more input parameters that don't require updates when you introduce new versions of
your action. Define dynamic or static picklists for input parameters and control input parameter display order and grouping. You
can also add a custom header to your property editor.

Passing Data to a Flow Using the Process.Plugin Interface

`Process.Plugin` is a built-in interface that lets you process data within your org and pass it to a specified flow. The interface
exposes Apex as a service, which accepts input values and returns output back to the flow.

##### Getting Flow Variables

You can retrieve flow variables for a specific flow in Apex.


Apex Developer Guide Using Salesforce Features with Apex

The `Flow.Interview` Apex class provides the `getVariableValue` method for retrieving a flow variable, which can be in the
flow embedded in the Visualforce page, or in a separate flow that is called by a subflow element. This example shows how to use this
method to obtain breadcrumb (navigation) information from the flow embedded in the Visualforce page. If that flow contains subflow
elements, and each of the referenced flows also contains a _`vaBreadCrumb`_ variable, the Visualforce page can provide users with
breadcrumbs regardless of which flow the interview is running.

```
   public class SampleContoller {

     // Instance of the flow

     public Flow.Interview.Flow_Template_Gallery myFlow {get; set;}

     public String getBreadCrumb() {

       String aBreadCrumb;

       if (myFlow==null) { return 'Home';}

       else aBreadCrumb = (String) myFlow.getVariableValue('vaBreadCrumb');

       return(aBreadCrumb==null ? 'Home': aBreadCrumb);

     }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/flow_interview_class.htm)_ : Interview Class

##### Making Callouts to External Systems from Invocable Actions

When you define a method that runs as an invocable action in a screen flow and makes a callout to an external system, use the `callout`
modifier.

When the method is executed as an invocable action, screen flows use this modifier to determine whether the action can be executed
safely in the current transaction. Flow admins can configure the action to let the flow decide whether to execute the action in a new
transaction or the current one.

When all of these conditions are met, the flow commits the current transaction, starts a new transaction, and makes the call to an external
system safely.

**•** The method's callout modifier is `true` .

**•** The action's Transaction Control setting in a screen flow is configured to let the flow decide.

**•** The current transaction has uncommitted work.

If any of these conditions are true, the flow executes the action in the current transaction.

**•** The callout modifier is `false` .

**•** The action is executed by a non-screen flow.

**•** The current transaction doesn’t have uncommitted work.

SEE ALSO:

InvocableMethod Annotation


Apex Developer Guide Using Salesforce Features with Apex

##### Extend Invocable Action Configuration in Flow Builder

Simplify the configuration of Apex invocable actions in Flow Builder by using the InvocableActionExtension metadata file. Create partial
custom property editors for one or more input parameters that don't require updates when you introduce new versions of your action.
Define dynamic or static picklists for input parameters and control input parameter display order and grouping. You can also add a
custom header to your property editor.

Example: Sorting Booking Request Inputs

An Apex class for a travel application, `BookingAction`, uses a custom input type, `BookingRequest`, to manage two required
dates: `startDate` and `endDate` . By default, the flow shows inputs alphabetically. Use the InvocableActionExtension metadata file
to define the logical order and group the fields under a relevant section header to improve the user experience.

Create the Apex Invocable Action

This section shows the Apex class structure required for the invocable action that exposes configurable input parameters to a flow.

This Apex class creates an invocable action, `BookingAction`, designed to send a booking request to an external system. Note that
the method accepts a `List` input to support bulk processing, a best practice for Apex development.

Note: Users who invoke the action from a flow must have the appropriate Apex class access set in their profile or permission set.

```
   public class BookingAction {

      @InvocableMethod(

        label='Booking Request'

        description='Sends a booking reservation request to booking system'

        category='Booking Integrations'

        callout=true // Indicates this action makes an external callout

      )

      public static List<BookingResult> invoke(List<BookingRequest> request) {

        // Apex business logic goes here to process the booking requests.

        // This process must be designed to handle multiple requests (bulkified).

        // Example mock logic:

        List<BookingResult> results = new List<BookingResult>();

        for (BookingRequest req : request) {

           BookingResult result = new BookingResult();

           result.status = 'Booking request received for dates: ' + req.startDate + ' to

    ' + req.endDate;

           results.add(result);

        }

        return results;

      }

      public class BookingRequest {

        @InvocableVariable(

           label='Requested Start Date'

           description='The start date for the booking.'

           required=true

        )

        public Date startDate;

        @InvocableVariable(

```


Apex Developer Guide Using Salesforce Features with Apex

```
           label='Requested End Date'

           description='The end date for the booking.'

           required=true

        )

        public Date endDate;

      }

      public class BookingResult {

        @InvocableVariable(

           label='Status Message'

        )

        public String status;

        // Include other output variables as needed.

      }

   }

```

The `invoke` method uses the `@InvocableMethod` annotation to be callable from a flow. Input and output are defined by the
inner classes, `BookingRequest` and `BookingResult`, ensuring data integrity. The individual input variables within
`BookingRequest` use the `@InvocableVariable` annotation, which allows them to be exposed as configurable fields in Flow
Builder.

Define Input Order with Invocable Action Extension

Use the InvocableActionExtension metadata file to specify the sort order of input fields. You can also organize them into collapsible
groups for improved usability in Flow Builder.

The file must have the suffix .invocableactionextension-meta.xml and the filename corresponds to the Apex class name, for example,
BookingAction.invocableactionextension-meta.xml. Add the metadata file to the invocableactionextensions directory.

This metadata file targets each input parameter and uses the `<key>Order</key>` attribute so the start date appears before the
end date. It also uses the `<key>Group</key>` attribute to organize both inputs under a single collapsible section named Booking
Dates.

Important: To sort the order of input fields, define an `Order` for all input parameters for the action. If you define an `Order`
for at least one parameter, you must define an `Order` for all parameters within the action to avoid unexpected behavior.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <InvocableActionExtension xmlns="http://soap.sforce.com/2006/04/metadata">

      <targets>

        <targetType>ActionParameter</targetType>

        <targetName>BookingAction.BookingRequest.startDate</targetName>

        <attributes>

           <key>Order</key>

           <dataType>Integer</dataType>

           <value>1</value> </attributes>

```


Apex Developer Guide Using Salesforce Features with Apex

```
        <attributes>

           <key>Group</key>

           <dataType>String</dataType>

           <value>Booking Dates</value> </attributes>

      </targets>

      <targets>

        <targetType>ActionParameter</targetType>

        <targetName>BookingAction.BookingRequest.endDate</targetName>

        <attributes>

           <key>Order</key>

           <dataType>Integer</dataType>

           <value>2</value> </attributes>

        <attributes>

           <key>Group</key>

           <dataType>String</dataType>

           <value>Booking Dates</value> </attributes>

      </targets>

   </InvocableActionExtension>

```

The `<targets>` elements identify the specific input parameters to be customized. The `<key>Order</key>` attribute explicitly
controls the vertical display sequence of the input parameters in Flow Builder. The `<key>Group</key>` attribute is used to create
the collapsible Booking Dates section, improving the organization and scannability of the action's inputs.

Define Static Picklist Values for Input Parameters

Use the `ProvidedValuesList` standard additional attribute to provide picklist options for input parameters. Users select from
predefined values, which reduces configuration errors. Each input parameter supports up to 500 total picklist values.

For a fixed set of values, use a comma-separated list. Optionally include display labels for one or more values by using a pipe delimiter.

First, add a new input parameter to the `BookingRequest` class:

```
   @InvocableVariable(

      label='Booking Type'

      description='The type of booking to create.'

      required=true

   )

   public String bookingType;

```

Then define the static picklist values in the InvocableActionExtension metadata file:

```
   <targets>

      <targetName>BookingAction.BookingRequest.bookingType</targetName>

```


Apex Developer Guide Using Salesforce Features with Apex

```
      <attributes>

        <key>ProvidedValuesList</key>

        <value>hotel|Hotel Reservation, flight|Flight Booking, car|Car Rental</value>

      </attributes>

   </targets>

```

In this example, the values `hotel`, `flight`, and `car` are stored in the flow. The labels `Hotel Reservation`, `Flight`
`Booking`, and `Car Rental` appear to users in Flow Builder.

Define Dynamic Picklist Values for Input Parameters

For picklist values that change based on org data or business logic, create an Apex class that extends
`VisualEditor.DynamicPicklist` . The class's `getValues()` method defines the picklist logic and returns the values.

```
   public class BookingTypeDynamicPicklist extends VisualEditor.DynamicPicklist {

      public override VisualEditor.DataRow getDefaultValue() {

        VisualEditor.DataRow defaultValue = new VisualEditor.DataRow('hotel', 'Hotel

   Reservation');

        return defaultValue;

      }

      public override VisualEditor.DynamicPicklistRows getValues() {

        VisualEditor.DynamicPicklistRows picklistValues = new

   VisualEditor.DynamicPicklistRows();

        // Query available booking types from custom metadata or other source

        List<BookingType__mdt> types = [SELECT Value__c, Label__c FROM BookingType__mdt];

        for (BookingType__mdt type : types) {

           VisualEditor.DataRow row = new VisualEditor.DataRow(type.Value__c,

   type.Label__c);

           picklistValues.addRow(row);

        }

        return picklistValues;

      }

   }

```

Reference the Apex class in the InvocableActionExtension metadata file by using the `apex://` URI format:

```
   <targets>

      <targetName>BookingAction.BookingRequest.bookingType</targetName>

      <attributes>

        <key>ProvidedValuesList</key>

        <value>apex://BookingTypeDynamicPicklist</value>

      </attributes>

   </targets>

```

Important: Dynamic picklist logic runs when users configure the action in Flow Builder. Efficient logic prevents timeouts during
action configuration.


Apex Developer Guide Using Salesforce Features with Apex

Add a Custom Header to an Action

Use the `CustomHeaderLwcName` standard additional attribute to add a custom header to your Apex action's standard property
editor. The header appears at the top of the property panel in Flow Builder. It provides context, instructions, or additional information
to improve the configuration experience.

First, create a Lightning web component that shows the header content. A Lightning web component consists of a JavaScript file and
an HTML template file.

Create the JavaScript controller file:

```
   // bookingActionHeader.js

   import { LightningElement } from 'lwc';

   export default class BookingActionHeader extends LightningElement {}

```

Create the HTML template file that defines the header's content and appearance:

```
   <codeblock otherprops="xml"><!-- bookingActionHeader.html -->

   <template>

      <div class="slds-box slds-theme_info slds-m-bottom_small">

        <p class="slds-text-heading_small">Booking Action Configuration</p>

        <p>Configure the booking request parameters below. Ensure you have enabled external

    callouts before using this action.</p>

      </div>

   </template>

   </codeblock>

```

Then reference the Lightning web component in the InvocableActionExtension metadata file. Use `ActionDefinition` as the
target type to apply the header to the entire action:

```
   <targets>

      <targetType>ActionDefinition</targetType>

      <targetName>BookingAction</targetName>

      <attributes>

        <key>CustomHeaderLwcName</key>

        <value>c:bookingActionHeader</value>

      </attributes>

   </targets>

```

When users configure the action in Flow Builder, the custom header appears at the top of the property panel before the input parameters.

Create Partial Custom Property Editors for Input Parameters

Use partial custom property editors (CPEs) to create custom configuration interfaces for one or more related input parameters. Full
custom property editors replace the entire action configuration interface. Partial CPEs customize specific parameters while other parameters
use the standard property editor.

With partial CPEs, you can add new input parameters to your action without updating the CPE code. The new parameters automatically
use the standard property editor. Full CPEs require code updates whenever you modify the action's parameters. This flexibility makes
partial CPEs easier to maintain as your action evolves.

First, add related input parameters to the `BookingRequest` class that benefit from coordinated configuration:

```
   @InvocableVariable(

      label='Assignee Type'

      description='The type of assignee for this booking.'

      required=true

```


Apex Developer Guide Using Salesforce Features with Apex

```
   )

   public String assigneeType;

   @InvocableVariable(

      label='Assignee'

      description='The user or queue to assign this booking to.'

      required=true

   )

   public String assignee;

```

Create a Lightning web component that serves as the partial CPE. The component can control how both parameters are configured
together.

Create the JavaScript controller file:

```
   // bookingAssigneeCpe.js

   import { LightningElement, api } from 'lwc';

   export default class BookingAssigneeCpe extends LightningElement {

      @api inputVariables;

      @api genericTypeMappings;

      // Logic to handle assigneeType and assignee coordination

      handleAssigneeTypeChange(event) {

        // Update available assignee options based on selected type

      }

   }

```

Create the HTML template file:

```
   <!-- bookingAssigneeCpe.html -->

   <template>

      <lightning-combobox

        label="Assignee Type"

        value={assigneeType}

        options={assigneeTypeOptions}

        onchange={handleAssigneeTypeChange}>

      </lightning-combobox>

      <lightning-combobox

        label="Assignee"

        value={assignee}

        options={assigneeOptions}>

      </lightning-combobox>

   </template>

```

Configure the partial CPE in the InvocableActionExtension metadata file. First, assign the CPE to the primary parameter by using the
`CpeName` attribute:

```
   <targets>

      <targetType>ActionParameter</targetType>

      <targetName>BookingAction.BookingRequest.assigneeType</targetName>

      <attributes>

        <key>CpeName</key>

        <value>c:bookingAssigneeCpe</value>

```


Apex Developer Guide Using Salesforce Features with Apex

```
      </attributes>

   </targets>

```

Then link the related parameter to the same CPE using the `ConfiguredBy` attribute:

```
   <targets>

      <targetType>ActionParameter</targetType>

      <targetName>BookingAction.BookingRequest.assignee</targetName>

      <attributes>

        <key>ConfiguredBy</key>

        <value>assigneeType</value>

      </attributes>

   </targets>

```

When users configure the action in Flow Builder, the partial CPE manages both the `assigneeType` and `assignee` parameters.
Other input parameters in the action continue to use the standard property editor. Each parameter can belong to only one partial CPE.
When a CPE controls multiple input parameters, the primary parameter's `Order` attribute determines where the CPE appears in the
property panel.

SEE ALSO:

InvocableMethod Annotation

InvocableVariable Annotation

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_invocableactionextension.htm)_ : InvocableActionExtension

_Apex Reference Guide_ [: DynamicPicklist Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_VisualEditor_DynamicPicklist.htm)

##### Passing Data to a Flow Using the Process.Plugin Interface

`Process.Plugin` is a built-in interface that lets you process data within your org and pass it to a specified flow. The interface exposes
Apex as a service, which accepts input values and returns output back to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

When you define an Apex class that implements the `Process.Plugin` interface in your org, it's available in Flow Builder as a legacy
Apex action.

`Process.Plugin` has these top-level classes.

**•** `[Process.PluginRequest](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginRequest.htm)` passes input parameters from the class that implements the interface to the flow.

**•** `[Process.PluginResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginResult.htm)` returns output parameters from the class that implements the interface to the flow.

**•** `[Process.PluginDescribeResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult.htm)` passes input parameters from a flow to the class that implements the interface. This
class determines the input parameters and output parameters needed by the `Process.PluginResult` plug-in.


Apex Developer Guide Using Salesforce Features with Apex

When you write Apex unit tests, instantiate a class and pass it into the interface `invoke` method. To pass in the parameters that the
system needs, create a map and use it in the constructor. For more information, see Using the Process.PluginRequest Class on page 492.

###### Implementing the Process.Plugin Interface

`Process.Plugin` is a built-in interface that allows you to pass data between your organization and a specified flow.

Using the Process.PluginRequest Class
The `Process.PluginRequest` class passes input parameters from the class that implements the interface to the flow.

Using the Process.PluginResult Class
The `Process.PluginResult` class returns output parameters from the class that implements the interface to the flow.

Using the Process.PluginDescribeResult Class
Use the `Process.Plugin` interface `describe` method to dynamically provide both input and output parameters for the
flow. This method returns the `Process.PluginDescribeResult` class.

Process.Plugin Data Type Conversions
Understand how data types are converted between Apex and the values returned to the `Process.Plugin` . For example, text
data in a flow converts to string data in Apex.

Sample Process.Plugin Implementation for Lead Conversion
In this example, an Apex class implements the `Process.Plugin` interface and converts a lead into an account, contact, and
optionally, an opportunity. Test methods for the plug-in are also included. This implementation can be called from a flow via a legacy
Apex action.

###### Implementing the Process.Plugin Interface

`Process.Plugin` is a built-in interface that allows you to pass data between your organization and a specified flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

The class that implements the `Process.Plugin` interface must call these methods.

**Name** **Arguments** **Return Type** **Description**

```
describe Process.PluginDescribeResult

invoke Process.PluginRequest Process.PluginResult

```


Returns a

```
Process.PluginDescribeResult
```

object that describes this method call.

Primary method that the system invokes
when the class that implements the
interface is instantiated.

Apex Developer Guide Using Salesforce Features with Apex

Example Implementation

```
   global class flowChat implements Process.Plugin {

   // The main method to be implemented. The Flow calls this at runtime.

   global Process.PluginResult invoke(Process.PluginRequest request) {

        // Get the subject of the Chatter post from the flow

        String subject = (String) request.inputParameters.get('subject');

        // Use the Chatter APIs to post it to the current user's feed

        FeedItem fItem = new FeedItem();

        fItem.ParentId = UserInfo.getUserId();

        fItem.Body = 'Flow Update: ' + subject;

        insert fItem;

        // return to Flow

        Map<String,Object> result = new Map<String,Object>();

        return new Process.PluginResult(result);

      }

      // Returns the describe information for the interface

      global Process.PluginDescribeResult describe() {

        Process.PluginDescribeResult result = new Process.PluginDescribeResult();

        result.Name = 'flowchatplugin';

        result.Tag = 'chat';

        result.inputParameters = new

          List<Process.PluginDescribeResult.InputParameter>{

            new Process.PluginDescribeResult.InputParameter('subject',

            Process.PluginDescribeResult.ParameterType.STRING, true)

           };

        result.outputParameters = new

          List<Process.PluginDescribeResult.OutputParameter>{ };

        return result;

      }

   }

```

Test Class

The following is a test class for the preceding class.

```
   @isTest

   private class flowChatTest {

      static testmethod void flowChatTests() {

        flowChat plugin = new flowChat();

        Map<String,Object> inputParams = new Map<String,Object>();

        string feedSubject = 'Flow is alive';

        InputParams.put('subject', feedSubject);

        Process.PluginRequest request = new Process.PluginRequest(inputParams);

```


Apex Developer Guide Using Salesforce Features with Apex

```
        plugin.invoke(request);

      }

   }

###### Using the Process.PluginRequest Class

```

The `Process.PluginRequest` class passes input parameters from the class that implements the interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

This class has no methods.

Constructor signature:

```
   Process.PluginRequest (Map<String,Object>)

```

Here’s an example of instantiating the `Process.PluginRequest` class with one input parameter.

```
    Map<String,Object> inputParams = new Map<String,Object>();

           string feedSubject = 'Flow is alive';

           InputParams.put('subject', feedSubject);

           Process.PluginRequest request = new Process.PluginRequest(inputParams);

```

Code Example

In this example, the code returns the subject of a Chatter post from a flow and posts it to the current user's feed.

```
   global Process.PluginResult invoke(Process.PluginRequest request) {

        // Get the subject of the Chatter post from the flow

        String subject = (String) request.inputParameters.get('subject');

        // Use the Chatter APIs to post it to the current user's feed

        FeedPost fpost = new FeedPost();

        fpost.ParentId = UserInfo.getUserId();

        fpost.Body = 'Flow Update: ' + subject;

        insert fpost;

        // return to Flow

        Map<String,Object> result = new Map<String,Object>();

        return new Process.PluginResult(result);

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      // describes the interface

      global Process.PluginDescribeResult describe() {

        Process.PluginDescribeResult result = new Process.PluginDescribeResult();

        result.inputParameters = new List<Process.PluginDescribeResult.InputParameter>{

           new Process.PluginDescribeResult.InputParameter('subject',

           Process.PluginDescribeResult.ParameterType.STRING, true)

           };

        result.outputParameters = new List<Process.PluginDescribeResult.OutputParameter>{

    };

        return result;

      }

   }

###### Using the Process.PluginResult Class

```

The `Process.PluginResult` class returns output parameters from the class that implements the interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

You can instantiate the `Process.PluginResult` class using one of the following formats:

**•** `Process.PluginResult (Map<String,Object>)`

**•** `Process.PluginResult (String, Object)`

Use the map when you have more than one result or when you don't know how many results are returned.

The following is an example of instantiating a `Process.PluginResult` class.

```
        string url = 'https://docs.google.com/document/edit?id=abc';

             String status = 'Success';

             Map<String,Object> result = new Map<String,Object>();

             result.put('url', url);

             result.put('status',status);

             new Process.PluginResult(result);

###### Using the Process.PluginDescribeResult Class

```

Use the `Process.Plugin` interface `describe` method to dynamically provide both input and output parameters for the flow.
This method returns the `Process.PluginDescribeResult` class.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.


Apex Developer Guide Using Salesforce Features with Apex

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

The `Process.PluginDescribeResult` class doesn’t support the following functions.

**•** Queries

**•** Data modification

**•** Email

**•** Apex nested callouts

**`Process.PluginDescribeResult`** Class and Subclass Properties

Here’s the constructor for the `Process.PluginDescribeResult` class.

```
   Process.PluginDescribeResult classname = new Process.PluginDescribeResult();

```

**•** [PluginDescribeResult Class Properties](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult.htm)

**•** [PluginDescribeResult.InputParameter Class Properties](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult_InputParameter.htm)

**•** [PluginDescribeResult.OutputParameter Class Properties](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult_OutputParameter.htm)

Here’s the constructor for the `Process.PluginDescribeResult.InputParameter` class.

```
   Process.PluginDescribeResult.InputParameter ip = new

      Process.PluginDescribeResult.InputParameter( Name, Optional_description_string,

       Process.PluginDescribeResult.ParameterType. Enum, Boolean_required );

```

Here’s the constructor for the `Process.PluginDescribeResult.OutputParameter` class.

```
   Process.PluginDescribeResult.OutputParameter op = new

      new Process.PluginDescribeResult.OutputParameter( Name, Optional description string,

        Process.PluginDescribeResult.ParameterType. Enum );

```

To use the `Process.PluginDescribeResult` class, create instances of these subclasses.

**•** `Process.PluginDescribeResult.InputParameter`

**•** `Process.PluginDescribeResult.OutputParameter`

`Process.PluginDescribeResult.InputParameter` is a list of input parameters and has the following format.

```
   Process.PluginDescribeResult.inputParameters =

       new List<Process.PluginDescribeResult.InputParameter>{

        new Process.PluginDescribeResult.InputParameter( Name, Optional_description_string,

       Process.PluginDescribeResult.ParameterType. Enum, Boolean_required )

```

For example:

```
   Process.PluginDescribeResult result = new Process.PluginDescribeResult();

   result.setDescription('this plugin gets the name of a user');

```


Apex Developer Guide Using Salesforce Features with Apex

```
   result.setTag ('userinfo');

   result.inputParameters = new List<Process.PluginDescribeResult.InputParameter>{

      new Process.PluginDescribeResult.InputParameter('FullName',

        Process.PluginDescribeResult.ParameterType.STRING, true),

      new Process.PluginDescribeResult.InputParameter('DOB',

        Process.PluginDescribeResult.ParameterType.DATE, true),

      };

```

`Process.PluginDescribeResult.OutputParameter` is a list of output parameters and has the following format.

```
   Process.PluginDescribeResult.outputParameters = new

   List<Process.PluginDescribeResult.OutputParameter>{

      new Process.PluginDescribeResult.OutputParameter( Name, Optional description string,

        Process.PluginDescribeResult.ParameterType. Enum )

```

For example:

```
   Process.PluginDescribeResult result = new Process.PluginDescribeResult();

   result.setDescription('this plugin gets the name of a user');

   result.setTag ('userinfo');

   result.outputParameters = new List<Process.PluginDescribeResult.OutputParameter>{

      new Process.PluginDescribeResult.OutputParameter('URL',

        Process.PluginDescribeResult.ParameterType.STRING),

```

Both classes take the `Process.PluginDescribeResult.ParameterType` Enum. Valid values are:

**•** BOOLEAN

**•** DATE

**•** DATETIME

**•** DECIMAL

**•** DOUBLE

**•** FLOAT

**•** ID

**•** INTEGER

**•** LONG

**•** STRING

**•** TIME

For example:

```
   Process.PluginDescribeResult result = new Process.PluginDescribeResult();

        result.outputParameters = new List<Process.PluginDescribeResult.OutputParameter>{

           new Process.PluginDescribeResult.OutputParameter('URL',

           Process.PluginDescribeResult.ParameterType.STRING, true),

           new Process.PluginDescribeResult.OutputParameter('STATUS',

           Process.PluginDescribeResult.ParameterType. STRING ),

           };

```


Apex Developer Guide Using Salesforce Features with Apex

###### Process.Plugin Data Type Conversions Understand how data types are converted between Apex and the values returned to the Process.Plugin . For example, text data

in a flow converts to string data in Apex.

###### Tip: We recommend using the @InvocableMethod annotation instead of the Process.Plugin interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

**Flow Data Type** **Data Type**

Number Decimal

Date Datetime/Date

DateTime Datetime/Date

Boolean Boolean and numeric with 1 or 0 values only

Text String

###### Sample Process.Plugin Implementation for Lead Conversion In this example, an Apex class implements the Process.Plugin interface and converts a lead into an account, contact, and

optionally, an opportunity. Test methods for the plug-in are also included. This implementation can be called from a flow via a legacy
Apex action.

###### Tip: We recommend using the @InvocableMethod annotation instead of the Process.Plugin interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**•** You can customize how invocable actions created with `@InvocableMethod` appear in Flow Builder by using the
InvocableActionExtension metadata file. Control parameter order, add picklists, create custom headers, and build partial custom
property editors.

```
   // Converts a lead as an action in a flow.

   global class VWFConvertLead implements Process.Plugin {

      // This method runs when called by a flow's legacy Apex action.

      global Process.PluginResult invoke(

        Process.PluginRequest request) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
        // Set up variables to store input parameters from

        // the flow.

        String leadID = (String) request.inputParameters.get(

           'LeadID');

        String contactID = (String)

           request.inputParameters.get('ContactID');

        String accountID = (String)

           request.inputParameters.get('AccountID');

        String convertedStatus = (String)

           request.inputParameters.get('ConvertedStatus');

        Boolean overWriteLeadSource = (Boolean)

           request.inputParameters.get('OverwriteLeadSource');

        Boolean createOpportunity = (Boolean)

           request.inputParameters.get('CreateOpportunity');

        String opportunityName = (String)

           request.inputParameters.get('ContactID');

        Boolean sendEmailToOwner = (Boolean)

           request.inputParameters.get('SendEmailToOwner');

        // Set the default handling for booleans.

        if (overWriteLeadSource == null)

           overWriteLeadSource = false;

        if (createOpportunity == null)

           createOpportunity = true;

        if (sendEmailToOwner == null)

           sendEmailToOwner = false;

        // Convert the lead by passing it to a helper method.

        Map<String,Object> result = new Map<String,Object>();

        result = convertLead(leadID, contactID, accountID,

           convertedStatus, overWriteLeadSource,

           createOpportunity, opportunityName,

           sendEmailToOwner);

        return new Process.PluginResult(result);

      }

      // This method describes the plug-in and its inputs from

      // and outputs to the flow.

      // Implementing this method makes the class available

      // in Flow Builder as a legacy Apex action.

      global Process.PluginDescribeResult describe() {

        // Set up plugin metadata

        Process.PluginDescribeResult result = new

           Process.PluginDescribeResult();

        result.description =

           'The LeadConvert Flow Plug-in converts a lead into ' +

           'an account, a contact, and ' +

           '(optionally)an opportunity.';

        result.tag = 'Lead Management';

        // Create a list that stores both mandatory and optional

        // input parameters from the flow.

```


Apex Developer Guide Using Salesforce Features with Apex

```
        // NOTE: Only primitive types (STRING, NUMBER, etc.) are

        // supported. Collections aren't supported.

        result.inputParameters = new

           List<Process.PluginDescribeResult.InputParameter>{

           // Lead ID (mandatory)

           new Process.PluginDescribeResult.InputParameter(

             'LeadID',

             Process.PluginDescribeResult.ParameterType.STRING,

             true),

           // Account Id (optional)

           new Process.PluginDescribeResult.InputParameter(

             'AccountID',

             Process.PluginDescribeResult.ParameterType.STRING,

             false),

           // Contact ID (optional)

           new Process.PluginDescribeResult.InputParameter(

             'ContactID',

             Process.PluginDescribeResult.ParameterType.STRING,

             false),

           // Status to use once converted

           new Process.PluginDescribeResult.InputParameter(

             'ConvertedStatus',

             Process.PluginDescribeResult.ParameterType.STRING,

             true),

           new Process.PluginDescribeResult.InputParameter(

             'OpportunityName',

             Process.PluginDescribeResult.ParameterType.STRING,

             false),

           new Process.PluginDescribeResult.InputParameter(

             'OverwriteLeadSource',

             Process.PluginDescribeResult.ParameterType.BOOLEAN,

             false),

           new Process.PluginDescribeResult.InputParameter(

             'CreateOpportunity',

             Process.PluginDescribeResult.ParameterType.BOOLEAN,

             false),

           new Process.PluginDescribeResult.InputParameter(

             'SendEmailToOwner',

             Process.PluginDescribeResult.ParameterType.BOOLEAN,

             false)

        };

        // Create a list that stores output parameters sent

        // to the flow.

        result.outputParameters = new List<

           Process.PluginDescribeResult.OutputParameter>{

           // Account ID of the converted lead

           new Process.PluginDescribeResult.OutputParameter(

             'AccountID',

             Process.PluginDescribeResult.ParameterType.STRING),

           // Contact ID of the converted lead

           new Process.PluginDescribeResult.OutputParameter(

             'ContactID',

             Process.PluginDescribeResult.ParameterType.STRING),

```


Apex Developer Guide Using Salesforce Features with Apex

```
           // Opportunity ID of the converted lead

           new Process.PluginDescribeResult.OutputParameter(

             'OpportunityID',

             Process.PluginDescribeResult.ParameterType.STRING)

        };

        return result;

      }

      /**

      * Implementation of the LeadConvert plug-in.

      * Converts a given lead with several options:

      * leadID - ID of the lead to convert

      * contactID 
      * accountID - ID of the Account to attach the converted

      * Lead/Contact/Opportunity to.

      * convertedStatus 
      * overWriteLeadSource 
      * createOpportunity - true if you want to create a new

      * Opportunity upon conversion

      * opportunityName - Name of the new Opportunity.

      * sendEmailtoOwner - true if you are changing owners upon

      * conversion and want to notify the new Opportunity owner.

      *

      * returns: a Map with the following output:

      * AccountID - ID of the Account created or attached

      * to upon conversion.

      * ContactID - ID of the Contact created or attached

      * to upon conversion.

      * OpportunityID - ID of the Opportunity created

      * upon conversion.

      */

      public Map<String,String> convertLead (

                      String leadID,

                      String contactID,

                      String accountID,

                      String convertedStatus,

                      Boolean overWriteLeadSource,

                      Boolean createOpportunity,

                      String opportunityName,

                      Boolean sendEmailToOwner

        ) {

        Map<String,String> result = new Map<String,String>();

        if (leadId == null) throw new ConvertLeadPluginException(

           'Lead Id cannot be null');

        // check for multiple leads with the same ID

        Lead[] leads = [Select Id, FirstName, LastName, Company

           From Lead where Id = :leadID];

        if (leads.size() > 0) {

           Lead l = leads[0];

           // CheckAccount = true, checkContact = false

           if (accountID == null && l.Company != null) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
             Account[] accounts = [Select Id, Name FROM Account

               where Name = :l.Company LIMIT 1];

             if (accounts.size() > 0) {

               accountId = accounts[0].id;

             }

           }

           // Perform the lead conversion.

           Database.LeadConvert lc = new Database.LeadConvert();

           lc.setLeadId(leadID);

           lc.setOverwriteLeadSource(overWriteLeadSource);

           lc.setDoNotCreateOpportunity(!createOpportunity);

           lc.setConvertedStatus(convertedStatus);

           if (sendEmailToOwner != null) lc.setSendNotificationEmail(

             sendEmailToOwner);

           if (accountId != null && accountId.length() > 0)

             lc.setAccountId(accountId);

           if (contactId != null && contactId.length() > 0)

             lc.setContactId(contactId);

           if (createOpportunity) {

             lc.setOpportunityName(opportunityName);

           }

           Database.LeadConvertResult lcr = Database.convertLead(

             lc, true);

           if (lcr.isSuccess()) {

             result.put('AccountID', lcr.getAccountId());

             result.put('ContactID', lcr.getContactId());

             if (createOpportunity) {

               result.put('OpportunityID',

                  lcr.getOpportunityId());

             }

           } else {

             String error = lcr.getErrors()[0].getMessage();

             throw new ConvertLeadPluginException(error);

           }

        } else {

           throw new ConvertLeadPluginException(

             'No leads found with Id : "' + leadId + '"');

        }

        return result;

      }

      // Utility exception class

      class ConvertLeadPluginException extends Exception {}

   }

   // Test class for the lead convert Apex plug-in.

   @isTest

   private class VWFConvertLeadTest {

      static testMethod void basicTest() {

        // Create test lead

        Lead testLead = new Lead(

          Company='Test Lead',FirstName='John',LastName='Doe');

```


Apex Developer Guide Using Salesforce Features with Apex

```
        insert testLead;

        LeadStatus convertStatus =

          [Select Id, MasterLabel from LeadStatus

          where IsConverted=true limit 1];

        // Create test conversion

        VWFConvertLead aLeadPlugin = new VWFConvertLead();

        Map<String,Object> inputParams = new Map<String,Object>();

        Map<String,Object> outputParams = new Map<String,Object>();

        inputParams.put('LeadID',testLead.ID);

        inputParams.put('ConvertedStatus',

          convertStatus.MasterLabel);

        Process.PluginRequest request = new

          Process.PluginRequest(inputParams);

        Process.PluginResult result;

        result = aLeadPlugin.invoke(request);

        Lead aLead = [select name, id, isConverted

                 from Lead where id = :testLead.ID];

        System.Assert(aLead.isConverted);

      }

      /*

       * This tests lead conversion with

       * the Account ID specified.

       */

      static testMethod void basicTestwithAccount() {

        // Create test lead

        Lead testLead = new Lead(

           Company='Test Lead',FirstName='John',LastName='Doe');

        insert testLead;

        Account testAccount = new Account(name='Test Account');

        insert testAccount;

          // System.debug('ACCOUNT BEFORE' + testAccount.ID);

        LeadStatus convertStatus = [Select Id, MasterLabel

               from LeadStatus where IsConverted=true limit 1];

        // Create test conversion

        VWFConvertLead aLeadPlugin = new VWFConvertLead();

        Map<String,Object> inputParams = new Map<String,Object>();

        Map<String,Object> outputParams = new Map<String,Object>();

        inputParams.put('LeadID',testLead.ID);

        inputParams.put('AccountID',testAccount.ID);

        inputParams.put('ConvertedStatus',

           convertStatus.MasterLabel);

```


Apex Developer Guide Using Salesforce Features with Apex

```
        Process.PluginRequest request = new

           Process.PluginRequest(inputParams);

        Process.PluginResult result;

        result = aLeadPlugin.invoke(request);

        Lead aLead =

           [select name, id, isConverted, convertedAccountID

           from Lead where id = :testLead.ID];

        System.Assert(aLead.isConverted);

        //System.debug('ACCOUNT AFTER' + aLead.convertedAccountID);

        System.AssertEquals(testAccount.ID, aLead.convertedAccountID);

      }

      /*

      * This tests lead conversion with the Account ID specified.

      */

      static testMethod void basicTestwithAccounts() {

        // Create test lead

        Lead testLead = new Lead(

           Company='Test Lead',FirstName='John',LastName='Doe');

        insert testLead;

        Account testAccount1 = new Account(name='Test Lead');

        insert testAccount1;

        Account testAccount2 = new Account(name='Test Lead');

        insert testAccount2;

          // System.debug('ACCOUNT BEFORE' + testAccount.ID);

        LeadStatus convertStatus = [Select Id, MasterLabel

           from LeadStatus where IsConverted=true limit 1];

        // Create test conversion

        VWFConvertLead aLeadPlugin = new VWFConvertLead();

        Map<String,Object> inputParams = new Map<String,Object>();

        Map<String,Object> outputParams = new Map<String,Object>();

        inputParams.put('LeadID',testLead.ID);

        inputParams.put('ConvertedStatus',

           convertStatus.MasterLabel);

        Process.PluginRequest request = new

           Process.PluginRequest(inputParams);

        Process.PluginResult result;

        result = aLeadPlugin.invoke(request);

        Lead aLead =

           [select name, id, isConverted, convertedAccountID

           from Lead where id = :testLead.ID];

        System.Assert(aLead.isConverted);

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      /*

       * -ve Test

       */

      static testMethod void errorTest() {

        // Create test lead

        // Lead testLead = new Lead(Company='Test Lead',

        // FirstName='John',LastName='Doe');

        LeadStatus convertStatus = [Select Id, MasterLabel

           from LeadStatus where IsConverted=true limit 1];

        // Create test conversion

        VWFConvertLead aLeadPlugin = new VWFConvertLead();

        Map<String,Object> inputParams = new Map<String,Object>();

        Map<String,Object> outputParams = new Map<String,Object>();

        inputParams.put('LeadID','00Q7XXXXxxxxxxx');

        inputParams.put('ConvertedStatus',convertStatus.MasterLabel);

        Process.PluginRequest request = new

           Process.PluginRequest(inputParams);

        Process.PluginResult result;

        try {

           result = aLeadPlugin.invoke(request);

        }

        catch (Exception e) {

         System.debug('EXCEPTION' + e);

         System.AssertEquals(1,1);

        }

      }

      /*

       * This tests the describe() method

       */

      static testMethod void describeTest() {

        VWFConvertLead aLeadPlugin =

           new VWFConvertLead();

        Process.PluginDescribeResult result =

           aLeadPlugin.describe();

        System.AssertEquals(

           result.inputParameters.size(), 8);

        System.AssertEquals(

           result.OutputParameters.size(), 3);

      }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

#### Formula Evaluation in Apex

Formula evaluation in Apex helps avoid unnecessary DML statements to recalculate formula field values and evaluate dynamic formula
expressions. Dynamic formulas in Apex support SObjects and Apex objects as context objects. The context type that corresponds to the
Apex class used in the `FormulaBuilder.withType()` method must be a global, user-defined Apex class. Any fields, properties,
or methods that the formula references must also be global.

Note: If formula fields on the input SObjects require a round-trip request to the database, use the
`[Formula.recalculateFormulas()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Formula.htm#apex_System_Formula_recalculateFormulas)` method.

Formulas in Apex support these features.

**•** Reference Apex types in formula fields. The values contained in individual components of such Apex types are accessed and evaluated
[by the formula. Address, Location, URL, and UUID System types are supported.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_system_Address.htm#topic-title)

**•** Reference standard lookups and custom lookups in formula fields.

**•** Access polymorphic relationship fields.

**•** Access the return value from the `toString()` method in formula fields.

[Formula evaluation in Apex is bound by the formula field character limit, but not the compile size limit. A formula can contain up to](https://help.salesforce.com/s/articleView?id=platform.formula_field_limits.htm&type=5&language=en_US)
3,900 characters including spaces, return characters, and comments.

[Formula functions that are available to use in Apex are ones that can be used in validation rules. For details, see Formula Operators and](https://help.salesforce.com/s/articleView?id=platform.customize_functions.htm&type=5&language=en_US)
[Functions by Context.](https://help.salesforce.com/s/articleView?id=platform.customize_functions.htm&type=5&language=en_US)

SEE ALSO:

_Apex Reference Guide:_ [FormulaEval Namespace](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_formulaeval.htm)

#### Metadata

Salesforce uses metadata types and components to represent org configuration and customization. Metadata is used for org settings
that admins control, or configuration information applied by installed apps and packages.

#### Use the classes in the Metadata namespace to access metadata from within Apex code for tasks that include:

**•** Customizing app installs or upgrades—During or after an install (or upgrade), your app can create or update metadata to let users
configure your app.

**•** Customizing apps after installation—After your app is installed, you can use metadata in Apex to let admins configure your app
using the UI that your app provides rather than having admins manually use the standard Salesforce setup UI.

**•** Securely accessing protected metadata—Update metadata that your app uses internally without exposing these types and components
to your users.

**•** Creating custom configuration tools—Use metadata in Apex to provide custom tools for admins to customize apps and packages.

#### Metadata access in Apex is available for Apex classes using API version 40.0 and later. For more information on metadata types and components, see the Metadata API Developer Guide and Custom Metadata Types.

Retrieving and Deploying Metadata
#### Retrieve and deploy metadata by using the Metadata.Operations class.

Supported Metadata Types
Apex supports a subset of metadata types and components.

Security Considerations
Be aware of security considerations when using Apex to access metadata.


Apex Developer Guide Using Salesforce Features with Apex

Testing Metadata Deployments
Apex code that accesses metadata must be properly tested.

SEE ALSO:

_Apex Reference Guide_ [: Metadata Namespace](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_namespace_Metadata.htm)

##### Retrieving and Deploying Metadata

Retrieve and deploy metadata by using the `Metadata.Operations` class.

Use the `Metadata.Operations.retrieve()` method to synchronously retrieve metadata from the current org. Provide a list
of metadata component names that you want to retrieve. Salesforce returns a list of matching component data, represented by component
classes that derive from `Metadata.Metadata` .

Use the `Metadata.Operations.enqueueDeployment()` method to asynchronously deploy metadata to the current org.
Deployment is queued for asynchronous processing. When deploying metadata, you can create and update components but not delete
them. There are limitations on which components that apps and packages can deploy and which types of apps and packages can deploy
to which types of orgs. There are also service protection limitations on how many deployments that you can enqueue at one time from
Apex. For more information, see Security Considerations.

Use the full name of the metadata component when retrieving and deploying metadata. The full name can include the namespace,
metadata type, and component name. If you’re updating components in a namespace, you must qualify the namespace for the component
in the full name. For example, the full name for a custom metadata MDType1__mdt component named Component1 that is contained
in the myPackage namespace is myPackage__MDType1__mdt.myPackage__Component1. For more information on the metadata
[component full name syntax, see Metadata base type in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) _Metadata API Developer Guide_ .

You can retrieve and deploy metadata in post install scripts. In uninstall scripts, you can only retrieve, not deploy, metadata from Apex
code.

[See Metadata.Operations for code examples for retrieving and deploying metadata.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Metadata_Operations.htm)

##### Supported Metadata Types

Apex supports a subset of metadata types and components.

Metadata access in Apex is limited to types and components that support the use cases described in Metadata. Apps and packages can
use the metadata feature in Apex to retrieve and deploy the following metadata types and components:

**•** Records of custom metadata types

**•** Layouts

##### Security Considerations

Be aware of security considerations when using Apex to access metadata.

Generally, Apex classes installed in the subscriber org can access any public, supported metadata type or component in the subscriber
org. Protected metadata, such as a custom metadata type that’s been marked protected, can only be accessed by Apex classes in the
same namespace as the protected metadata.

Additionally, for managed packages, if the managed package isn’t approved by Salesforce via security review, Apex classes in the package
can’t access public or protected metadata unless the **Deploy Metadata from Non-Certified Package Versions via Apex** org preference
is enabled. This preference, located under **Setup**     - **Apex Settings**, must be enabled if admins or developers are installing managed
packages that haven’t passed security review for app testing or pilot purposes.


Apex Developer Guide Using Salesforce Features with Apex

For deployments, because `Metadata.Operations.enqueueDeployment()` uses asynchronous Apex, queued deployment
jobs and deployment callbacks are counted as asynchronous jobs in the current org. Queued deployment jobs and callbacks are subject
to governor limits. See Lightning Platform Apex Limits. To preserve service function, we limit the number of Metadata API deployments
originating from Apex that can be enqueued at a time. See Limit on Enqueued Deployments from Apex.

Apps that access metadata via Apex must notify users that the app can retrieve or deploy metadata in the subscriber org. For installs
that access metadata, notify users in the description of your package. You can write your own notice, or use this sample:

```
   This package can access and change metadata outside its namespace in the Salesforce

   org where it’s installed.

```

[Salesforce verifies the notice during the security review. For more information, see the ISVforce Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/security_guidelines.htm)

##### Testing Metadata Deployments

Apex code that accesses metadata must be properly tested.

To provide Apex test coverage for metadata deployments, write tests that verify both the set up of the deployment request and handling
of the deployment results.

Tests for deployment request code verify the metadata components and component values that get created and assert that the
`DeployContainer` contains exactly what needs to be deployed.

Tests for deployment result code verify that your `DeployCallback` handles expected and unexpected results. Your
`DeployCallback` is normally called by Salesforce as part of the asynchronous deployment process. Therefore, to test your callback
outside of the deployment process, create tests that use your callback class directly. You also must create test `DeployResults` and
`DeployCallbackContext` instances to test your `DeployCallback.handleResults()` method.

When creating a test instance of `DeployCallbackContext`, subclass `DeployCallbackContext` and provide your own
implementation of `getCallbackJobId()` .

```
   // DeployCallbackContext subclass for testing that returns myJobId

   public class TestingDeployCallbackContext extends Metadata.DeployCallbackContext {

     private Id myJobId = '000000000000000000'; // replace value with a job ID that you can

   use for testing

     public override Id getCallbackJobId() {

      return myJobId;

     }

   }

#### Permission Set Groups

```

To provide Apex test coverage for permission set groups, write tests using the `calculatePermissionSetGroup()` method
in the `System.Test` class.

The `[calculatePermissionSetGroup()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_System_Test_class.htm)` method forces an immediate calculation of aggregate permissions for a specified
permission set group. As the forced calculation counts against Apex CPU limits, and can require complex data setup, it’s a best practice
to minimize the number of times you perform this operation. Recalculating complex permission set groups with a large number of
included permission sets or overall enabled permissions can cause Apex test failures because Apex CPU limits are exceeded. Apex CPU
limits can also be exceeded if the included permission sets in the permission set group aren’t licensed and the permission set group is
assigned to many users.

Set this test to run once in a Test setup method, then reuse the data in subsequent tests.

```
   @isTest public class PSGTest {

     @isTest static void testPSG() {

```


Apex Developer Guide Using Salesforce Features with Apex

```
      // get the PSG by name (may have been modified in deployment)

      PermissionSetGroup psg = [select Id, Status from PermissionSetGroup where

   DeveloperName='MyPSG'];

      // force calculation of the PSG if it is not already Updated

      if (psg.Status != 'Updated') {

       Test.calculatePermissionSetGroup(psg.Id);

      }

      // assign PSG to current user (this fails if PSG is Outdated)

      insert new PermissionSetAssignment(PermissionSetGroupId = psg.Id, AssigneeId =

   UserInfo.getUserId());

      // additional tests to validate permissions granted by PSG

     }

   }

```

SEE ALSO:

[Salesforce Help: Permission Set Groups](https://help.salesforce.com/s/articleView?id=platform.perm_set_groups.htm&type=5&language=en_US)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_test.htm)_ : Test Class

#### Platform Cache

The Lightning Platform Cache layer provides faster performance and better reliability when caching Salesforce session and org data.
Specify what to cache and for how long without using custom objects and settings or overloading a Visualforce view state. Platform
Cache improves performance by distributing cache space so that some applications or operations don’t steal capacity from others.

Because Apex runs in a multi-tenant environment with cached data living alongside internally cached data, caching involves minimal
disruption to core Salesforce processes.

#### Platform Cache Features

The Platform Cache API lets you store and retrieve data that’s tied to Salesforce sessions or shared across your org. Put, retrieve, or
remove cache values by using the `Session`, `Org`, `SessionPartition`, and `OrgPartition` classes in the Cache
namespace. Use the Platform Cache Partition tool in Setup to create or remove org partitions and allocate their cache capacities to
balance performance across apps.

#### Platform Cache Considerations

Review these considerations when working with Platform Cache.

#### Platform Cache Limits

These limits apply when using Platform Cache.

#### Platform Cache Partitions

Use Platform Cache partitions to improve the performance of your applications. Partitions allow you to distribute cache space in the
way that works best for your applications. Caching data to designated partitions ensures that it’s not overwritten by other applications
or less-critical data.

#### Platform Cache Internals Platform Cache uses local cache and a least recently used (LRU) algorithm to improve performance.


Apex Developer Guide Using Salesforce Features with Apex

Store and Retrieve Values from the Session Cache
Use the `Cache.Session` and `Cache.SessionPartition` classes to manage values in the session cache. To manage
values in any partition, use the methods in the `Cache.Session` class. If you’re managing cache values in one partition, use the
`Cache.SessionPartition` methods instead.

Store and Retrieve Values from the Org Cache
Use the `Cache.Org` and `Cache.OrgPartition` classes to manage values in the org cache. To manage values in any partition,
use the methods in the `Cache.Org` class. If you’re managing cache values in one partition, use the `Cache.OrgPartition`
methods instead.

Use a Visualforce Global Variable for the Platform Cache
You can access cached values stored in the session or org cache from a Visualforce page with global variables.

Safely Cache Values with the CacheBuilder Interface
A Platform Cache best practice is to ensure that your Apex code handles cache misses by testing for cache requests that return null.
You can write this code yourself. Or, you can use the `Cache.CacheBuilder` interface, which makes it easy to safely store and
retrieve values to a session or org cache.

Platform Cache Best Practices
Platform Cache can greatly improve performance in your applications. However, it’s important to follow these guidelines to get the
best cache performance. In general, it’s more efficient to cache a few large items than to cache many small items separately. Also
be mindful of cache limits to prevent unexpected cache evictions.

##### Platform Cache Features

The Platform Cache API lets you store and retrieve data that’s tied to Salesforce sessions or shared across your org. Put, retrieve, or remove
cache values by using the `Session`, `Org`, `SessionPartition`, and `OrgPartition` classes in the Cache namespace. Use
the Platform Cache Partition tool in Setup to create or remove org partitions and allocate their cache capacities to balance performance
across apps.

There are two types of cache:

**•** **Session cache** —Stores data for individual user sessions. For example, in an app that finds customers within specified territories,
the calculations that run while users browse different locations on a map are reused.

Session cache lives alongside a user session. The maximum life of a session is eight hours. Session cache expires when its specified
time-to-live ( _`ttlsecs`_ value) is reached or when the session expires after eight hours, whichever comes first.

**•** **Org cache** —Stores data that any user in an org reuses. For example, the contents of navigation bars that dynamically display menu
items based on user profile are reused.

Unlike session cache, org cache is accessible across sessions, requests, and org users and profiles. Org cache expires when its specified
time-to-live ( _`ttlsecs`_ value) is reached.

Additionally, Salesforce provides 3 MB of free Platform Cache capacity for security-reviewed managed packages through a capacity type
called Provider Free capacity. You can allocate capacities to session cache and org cache from the Provider Free capacity.

The best data to cache is:

**•** Reused throughout a session

**•** Static (not rapidly changing)

**•** Otherwise expensive to retrieve

For both session and org caches, you can construct calls so that cached data in one namespace isn’t overwritten by similar data in
another. Optionally use the _`Cache.Visibility`_ enumeration to specify whether Apex code can access cached data in a namespace
outside of the invoking namespace.


Apex Developer Guide Using Salesforce Features with Apex

Each cache operation depends on the Apex transaction within which it runs. If the entire transaction fails, all cache operations in that
transaction are rolled back.

Try Platform Cache

To test performance improvements by using Platform Cache in your own org, you can request trial cache for your production org.
Enterprise, Unlimited, and Performance editions come with some cache, but adding more cache often provides greater performance.
When your trial request is approved, you can allocate capacity to partitions and experiment with using the cache for different scenarios.
Testing the cache on a trial basis lets you make an informed decision about whether to purchase cache.

For more information about trial cache, see “Request a Platform Cache Trial” in Salesforce Help.

You can request additional cache space to improve the performance of your application. For more information about requesting additional
cache, see "Request Additional Platform Cache" in Salesforce Help.

For more information about Provider Free capacity cache, see “Set Up a Platform Cache partition using Provider Free Capacity” in Salesforce
Help.

Note: Platform Cache isn’t supported in Professional Edition.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_cache_Session.htm)_ : Session Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_cache_Org.htm)_ : Org Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_cache_Partition.htm)_ : Partition Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_cache_OrgPartition.htm)_ : OrgPartition Class

_Apex Reference Guide_ [: SessionPartition Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_cache_SessionPartition.htm)

_Apex Reference Guide_ [: CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

##### Platform Cache Considerations

Review these considerations when working with Platform Cache.

**•** Cache isn’t persisted. There’s no guarantee against data loss.

**•** Some or all cache is invalidated when you modify an Apex class in your org.

**•** Data in the cache isn’t encrypted.

**•** Org cache supports concurrent reads and writes across multiple simultaneous Apex transactions. For example, a transaction updates
the key `PetName` with the value `Fido` . At the same time, another transaction updates the same key with the value `Felix` . Both
writes succeed, but one of the two values is chosen arbitrarily as the winner, and later transactions read that one value. However,
this arbitrary choice is per key rather than per transaction. For example, suppose one transaction writes `PetType="Cat"` and
`PetName="Felix"` . Then, at the same moment, another transaction writes `PetType="Dog"` and `PetName="Fido"` .
In this case, the `PetType` winning value could be from the first transaction, and the `PetName` winning value could be from the
second transaction. Subsequent `get()` calls on those keys would return `PetType="Cat"` and `PetName="Fido"` .

**•** Cache misses can happen. We recommend constructing your code to consider a case where previously cached items aren’t found.
[Alternatively, use the CacheBuilder Interface, which checks for cache misses.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

**•** All platform cache statistical methods: `getAvgGetSize()`, `getAvgGetTime()`, `getMaxGetSize()`,
`getMaxGetTime()`, and `getMissRate()` report data starting from the time the cache server was restarted, and do not
include data prior to the restart.

**•** Partitions must adhere to the limits within Salesforce.

**•** The session cache can store values up to eight hours. The org cache can store values up to 48 hours.


Apex Developer Guide Using Salesforce Features with Apex

**•** For orgs that use Salesforce Flow:

**–** When a process contains a scheduled action, make sure that later actions in the process don't invoke Apex code that stores or
retrieves values from the session cache. The session-cache restriction applies to Apex actions and to changes that the process
makes to the database that cause Apex triggers to fire.

**–** When a flow contains a Pause element, make sure that later elements in the flow don't invoke Apex code that stores or retrieves
values from the session cache. The session-cache restriction applies to Apex actions and to changes that the flow makes to the
database that cause Apex triggers to fire.

##### Platform Cache Limits

These limits apply when using Platform Cache.

##### Platform Cache Limits

Key Size Limits

**Limit** **Value**

Maximum key size 50 characters

Edition-specific Limits

This table shows the amount of Platform Cache available for different types of orgs. To purchase more cache, contact your Salesforce
representative.

**Edition** **Cache Size**

Enterprise 10 MB

Unlimited and Performance 30 MB

All others 0 MB

Partition Size Limits

**Limit** **Value**

Minimum partition size 1 MB

Session Cache Limits

**Limit** **Value**

Maximum size of a single cached item (for `put()` methods) 100 KB

Maximum local cache size for a partition, per-request [1] 500 KB

Minimum developer-assigned time-to-live 300 seconds (5 minutes)

Maximum developer-assigned time-to-live 28,800 seconds (8 hours)


Apex Developer Guide Using Salesforce Features with Apex

**Limit** **Value**

Maximum session cache time-to-live 28,800 seconds (8 hours)

Org Cache Limits

**Limit** **Value**

Maximum size of a single cached item (for `put()` methods) 100 KB

Maximum local cache size for a partition, per-request [1] 1,000 KB

Minimum developer-assigned time-to-live 300 seconds (5 minutes)

Maximum developer-assigned time-to-live 172,800 seconds (48 hours)

Default org cache time-to-live 86,400 seconds (24 hours)

1 Local cache is the application server’s in-memory container that the client interacts with during a request.

##### Platform Cache Partitions

Use Platform Cache partitions to improve the performance of your applications. Partitions allow you to distribute cache space in the way
that works best for your applications. Caching data to designated partitions ensures that it’s not overwritten by other applications or
less-critical data.

To use Platform Cache, first set up partitions using the Platform Cache Partition tool in Setup. Once you’ve set up partitions, you can add,
access, and remove data from them using the Platform Cache Apex API.

##### To access the Partition tool in Setup, enter Platform Cache in the Quick Find box, then select Platform Cache .

Use the Partition tool to:

**•** Setup a Platform Cache partition with Provider Free capacity.

**•** Request trial cache.

**•** Create, edit, or delete cache partitions.

**•** Allocate the session cache and org cache capacities of each partition to balance performance across apps.

**•** View a snapshot of the org’s current cache capacity, breakdown, and partition allocations (in KB or MB).

**•** View details about each partition.

**•** Make any partition the default partition.

To use Platform Cache, create at least one partition. Each partition has one session cache and one org cache segment and you can
allocate separate capacity to each segment. Session cache can be used to store data for individual user sessions, and org cache is for
