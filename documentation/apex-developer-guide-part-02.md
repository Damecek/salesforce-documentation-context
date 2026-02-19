The Apex class returns a JSON response that contains the attachment ID such as the following:

```
     "00PD0000001y7BfMAI"

```

**3.** To verify that the attachment and the image were added to the case, navigate to **Cases** and select the **All Open Cases** view. Click
on the case and then scroll down to the Attachments related list. You should see the attachment you just created.

#### Apex Email Service

You can use email services to process the contents, headers, and attachments of inbound email. For example, you can create an email
service that automatically creates contact records based on contact information in messages.

You can associate each email service with one or more Salesforce-generated email addresses to which users can send messages for
processing. To give multiple users access to a single email service, you can:

**•** Associate multiple Salesforce-generated email addresses with the email service and allocate those addresses to users.

**•** Associate a single Salesforce-generated email address with the email service, and write an Apex class that executes according to the
user accessing the email service. For example, you can write an Apex class that identifies the user based on the user's email address
and creates records on behalf of that user.

To use email services, from Setup, enter _`Email Services`_ in the `Quick Find` box, then select **Email Services** .

**•** Click **New Email Service** to define a new email service.

**•** Select an existing email service to view its configuration, activate or deactivate it, and view or specify addresses for that email service.

**•** Click **Edit** to make changes to an existing email service.

**•** Click **Delete** to delete an email service.


Apex Developer Guide Invoking Apex

Note: Before deleting email services, you must delete all associated email service addresses.

When defining email services, note the following:

**•** An email service only processes messages it receives at one of its addresses.

**•** Salesforce limits the total number of messages that all email services combined, including On-Demand Email-to-Case, can process
daily. Messages that exceed this limit are bounced, discarded, or queued for processing the next day, depending on how you
configure the failure response settings for each email service. Salesforce calculates the limit by multiplying the number of user
licenses by 1,000; maximum 1,000,000. For example, if you have 10 licenses, your org can process up to 10,000 email messages a
day.

**•** Email service addresses that you create in your sandbox can’t be copied to your production org.

**•** For each email service, you can tell Salesforce to send error email messages to a specified address instead of the sender's email
address.

**•** Email services reject email messages and notify the sender if the email (combined body text, body HTML, and attachments) exceeds
approximately 25 MB (varies depending on language and character set).

#### Using the InboundEmail Object

For every email the Apex email service domain receives, Salesforce creates a separate InboundEmail object that contains the contents
and attachments of that email. You can use Apex classes that implement the `Messaging.InboundEmailHandler` interface
to handle an inbound email message. Using the `handleInboundEmail` method in that class, you can access an InboundEmail
object to retrieve the contents, headers, and attachments of inbound email messages, as well as perform many functions.

Example 1: Create Tasks for Contacts

The following is an example of how you can look up a contact based on the inbound email address and create a new task.

```
   public with sharing class CreateTaskEmailExample implements Messaging.InboundEmailHandler

    {

     public Messaging.InboundEmailResult handleInboundEmail(Messaging.inboundEmail email,

                                    Messaging.InboundEnvelope env){

      // Create an InboundEmailResult object for returning the result of the

      // Apex Email Service

      Messaging.InboundEmailResult result = new Messaging.InboundEmailResult();

      String myPlainText= '';

      // Add the email plain text into the local variable

      myPlainText = email.plainTextBody;

      // New Task object to be created

      Task[] newTask = new Task[0];

      // Try to look up any contacts based on the email from address

      // If there is more than one contact with the same email address,

      // an exception will be thrown and the catch statement will be called.

      try {

       Contact vCon = [SELECT Id, Name, Email

        FROM Contact

```


Apex Developer Guide Invoking Apex

```
        WHERE Email = :email.fromAddress

        WITH USER_MODE

        LIMIT 1];

       // Add a new Task to the contact record we just found above.

       newTask.add(new Task(Description = myPlainText,

          Priority = 'Normal',

          Status = 'Inbound Email',

          Subject = email.subject,

          IsReminderSet = true,

          ReminderDateTime = System.now()+1,

          WhoId = vCon.Id));

      // Insert the new Task

      insert as user newTask;

      System.debug('New Task Object: ' + newTask );

      }

      // If an exception occurs when the query accesses

      // the contact record, a QueryException is called.

      // The exception is written to the Apex debug log.

     catch (QueryException e) {

        System.debug('Query Issue: ' + e);

     }

     // Set the result to true. No need to send an email back to the user

     // with an error message

     result.success = true;

     // Return the result for the Apex Email Service

     return result;

     }

   }

```

Example 2: Handle Unsubscribe Email

Companies that send marketing email to their customers and prospects must provide a way to let the recipients unsubscribe. The
following is an example of how an email service can process unsubscribe requests. The code searches the subject line of inbound email
for the word “unsubscribe.” If the word is found, the code finds all contacts and leads that match the From email address and sets the
`Email Opt Out` field ( `HasOptedOutOfEmail` ) to True.

```
   public with sharing class unsubscribe implements Messaging.inboundEmailHandler{

      public Messaging.InboundEmailResult handleInboundEmail(Messaging.InboundEmail email,

                  Messaging.InboundEnvelope env ) {

        // Create an inboundEmailResult object for returning

        // the result of the email service.

        Messaging.InboundEmailResult result = new Messaging.InboundEmailResult();

        // Create contact and lead lists to hold all the updated records.

        List<Contact> lc = new List <contact>();

        List<Lead> ll = new List <lead>();

```


Apex Developer Guide Invoking Apex

```
        // Convert the subject line to lower case so the program can match on lower case.

        String mySubject = email.subject.toLowerCase();

        // The search string used in the subject line.

        String s = 'unsubscribe';

        // Check the variable to see if the word "unsubscribe" was found in the subject

   line.

        Boolean unsubMe;

        // Look for the word "unsubcribe" in the subject line.

        // If it is found, return true; otherwise, return false.

        unsubMe = mySubject.contains(s);

         // If unsubscribe is found in the subject line, enter the IF statement.

        if (unsubMe == true) {

           try {

           // Look up all contacts with a matching email address.

           for (Contact c : [SELECT Id, Name, Email, HasOptedOutOfEmail

                   FROM Contact

                   WHERE Email = :env.fromAddress

                   AND hasOptedOutOfEmail = false

                   WITH USER_MODE

                   LIMIT 100]) {

             // Add all the matching contacts into the list.

             c.hasOptedOutOfEmail = true;

             lc.add(c);

           }

           // Update all of the contact records.

           update as user lc;

        }

        catch (System.QueryException e) {

           System.debug('Contact Query Issue: ' + e);

        }

        try {

           // Look up all leads matching the email address.

           for (Lead l : [SELECT Id, Name, Email, HasOptedOutOfEmail

                FROM Lead

                WHERE Email = :env.fromAddress

                AND isConverted = false

                AND hasOptedOutOfEmail = false

                WITH USER_MODE

                LIMIT 100]) {

             // Add all the leads to the list.

             l.hasOptedOutOfEmail = true;

             ll.add(l);

             System.debug('Lead Object: ' + l);

```


Apex Developer Guide Invoking Apex

```
           }

           // Update all lead records in the query.

           update as user ll;

        }

        catch (System.QueryException e) {

           System.debug('Lead Query Issue: ' + e);

        }

        System.debug('Found the unsubscribe word in the subject line.');

         }

         else {

           System.debug('No Unsuscribe word found in the subject line.' );

         }

        // Return True and exit.

        // True confirms program is complete and no emails

        // should be sent to the sender of the unsubscribe request.

        result.success = true;

        return result;

      }

   }

   @isTest

   private class unsubscribeTest {

      // The following test methods provide adequate code coverage

      // for the unsubscribe email class.

      // There are two methods, one that does the testing

      // with a valid "unsubcribe" in the subject line

      // and one the does not contain "unsubscribe" in the

      // subject line.

      static testMethod void testUnsubscribe() {

        // Create a new email and envelope object.

        Messaging.InboundEmail email = new Messaging.InboundEmail() ;

        Messaging.InboundEnvelope env = new Messaging.InboundEnvelope();

        // Create a new test lead and insert it in the test method.

        Lead l = new lead(firstName='John',

             lastName='Smith',

             Company='Salesforce',

             Email='user@acme.com',

             HasOptedOutOfEmail=false);

        insert l;

        // Create a new test contact and insert it in the test method.

        Contact c = new Contact(firstName='john',

               lastName='smith',

               Email='user@acme.com',

               HasOptedOutOfEmail=false);

        insert c;

        // Test with the subject that matches the unsubscribe statement.

        email.subject = 'test unsubscribe test';

        env.fromAddress = 'user@acme.com';

```


Apex Developer Guide Invoking Apex

```
        // Call the class and test it with the data in the testMethod.

        unsubscribe unsubscribeObj = new unsubscribe();

        unsubscribeObj.handleInboundEmail(email, env );

      }

      static testMethod void testUnsubscribe2() {

        // Create a new email and envelope object.

        Messaging.InboundEmail email = new Messaging.InboundEmail();

        Messaging.InboundEnvelope env = new Messaging.InboundEnvelope();

        // Create a new test lead and insert it in the test method.

        Lead l = new lead(firstName='john',

             lastName='smith',

             Company='Salesforce',

             Email='user@acme.com',

             HasOptedOutOfEmail=false);

        insert l;

        // Create a new test contact and insert it in the test method.

        Contact c = new Contact(firstName='john',

               lastName='smith',

               Email='user@acme.com',

               HasOptedOutOfEmail=false);

        insert c;

        // Test with a subject that does not contain "unsubscribe."

        email.subject = 'test';

        env.fromAddress = 'user@acme.com';

        // Call the class and test it with the data in the test method.

        unsubscribe unsubscribeObj = new unsubscribe();

        unsubscribeObj.handleInboundEmail(email, env );

        // Assert that the Lead and Contact have been unsubscribed

        Lead updatedLead = [Select Id, HasOptedOutOfEmail from Lead where Id = :l.Id];

        Contact updatedContact = [Select Id, HasOptedOutOfEmail from Contact where Id =

   :c.Id];

        Assert.isTrue(l.HasOptedOutOfEmail);

        Assert.isTrue(c.HasOptedOutOfEmail);

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: InboundEmail Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_inbound_inbound.htm)

_Apex Reference Guide_ [: InboundEnvelope Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_inbound_envelope.htm)

_Apex Reference Guide_ [: InboundEmailResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_inbound_result.htm)


Apex Developer Guide Invoking Apex

#### Visualforce Classes

In addition to giving developers the ability to add business logic to Salesforce system events such as button clicks and related record
updates, Apex can also be used to provide custom logic for Visualforce pages through custom Visualforce controllers and controller
extensions.

**•** A custom controller is a class written in Apex that implements all of a page's logic, without leveraging a standard controller. If you
use a custom controller, you can define new navigation elements or behaviors, but you must also reimplement any functionality
that was already provided in a standard controller.

Like other Apex classes, custom controllers execute entirely in system mode, in which the object and field-level permissions of the
current user are ignored. You can specify whether a user can execute methods in a custom controller based on the user's profile.

**•** A controller extension is a class written in Apex that adds to or overrides behavior in a standard or custom controller. Extensions
allow you to leverage the functionality of another controller while adding your own custom logic.

Because standard controllers execute in user mode, in which the permissions, field-level security, and sharing rules of the current
user are enforced, extending a standard controller allows you to build a Visualforce page that respects user permissions. Although
the extension class executes in system mode, the standard controller executes in user mode. As with custom controllers, you can
specify whether a user can execute methods in a controller extension based on the user's profile.

You can use these system-supplied Apex classes when building custom Visualforce controllers and controller extensions.

**•** Action

**•** Dynamic Component

**•** IdeaStandardController

**•** IdeaStandardSetController

**•** KnowledgeArticleVersionStandardController

**•** Message

**•** PageReference

**•** SelectOption

**•** StandardController

**•** StandardSetController

In addition to these classes, the `transient` keyword can be used when declaring methods in controllers and controller extensions.
For more information, see Using the `transient` Keyword on page 88.

For more information on Visualforce, see the _[Visualforce Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)_ .

#### JavaScript Remoting

Use JavaScript remoting in Visualforce to call methods in Apex controllers from JavaScript. Create pages with complex, dynamic behavior
that isn’t possible with the standard Visualforce AJAX components.

Features implemented using JavaScript remoting require three elements:

**•** The remote method invocation you add to the Visualforce page, written in JavaScript.

**•** The remote method definition in your Apex controller class. This method definition is written in Apex, but there are some important
differences from normal action methods.

**•** The response handler callback function you add to or include in your Visualforce page, written in JavaScript.


Apex Developer Guide Invoking Apex

In your controller, your Apex method declaration is preceded with the `@RemoteAction` annotation like this:

```
   @RemoteAction

   global static String getItemId(String objectName) { ... }

#### Apex @RemoteAction methods must be static and either global or public .

```

Add the Apex class as a custom controller or a controller extension to your page.

```
   <apex:page controller="MyController" extension="MyExtension">

```

Warning: Adding a controller or controller extension grants access to all `@RemoteAction` methods in that Apex class, even
if those methods aren’t used in the page. Anyone who can view the page can execute all `@RemoteAction` methods and
provide fake or malicious data to the controller.

Then, add the request as a JavaScript function call. A simple JavaScript remoting invocation takes the following form.

```
   [ namespace .] MyController . method (

      [parameters...,]

     callbackFunction,

      [configuration]

   );

```

**Table 7: Remote Request Elements**

For more information, see _JavaScript Remoting for Apex Controllers_ in the _Visualforce Developer's Guide_ .

#### Apex in AJAX

The AJAX toolkit includes built-in support for invoking Apex through anonymous blocks or public `webservice` methods.

To invoke Apex through anonymous blocks or public `webservice` methods, include the following lines in your AJAX code:

```
<script src="/soap/ajax/66.0/connection.js" type="text/javascript"></script>

<script src="/soap/ajax/66.0/apex.js" type="text/javascript"></script>

```

Note: For AJAX buttons, use the alternate forms of these includes.


### Apex Developer Guide Apex Transactions and Governor Limits

To invoke Apex, use one of the following two methods:

**•** Execute anonymously via `sforce.apex.executeAnonymous (` _**`script`**_ `)` . This method returns a result similar to the API's
result type, but as a JavaScript structure.

**•** Use a class WSDL. For example, you can call the following Apex class:

```
     global class myClass {

      webservice static Id makeContact(String lastName, Account a) {

          Contact c = new Contact(LastName = lastName, AccountId = a.Id);

          return c.id;

       }

     }

```

By using the following JavaScript code:

```
     var account = sforce.sObject("Account");

     var id = sforce.apex.execute("myClass","makeContact",

                      {lastName:"Smith",

                       a:account});

```

The `execute` method takes primitive data types, sObjects, and lists of primitives or sObjects.

To call a webservice method with no parameters, use `{}` as the third parameter for `sforce.apex.execute` . For example, to
call the following Apex class:

```
     global class myClass{

       webservice static String getContextUserName() {

          return UserInfo.getFirstName();

       }

     }

```

Use the following JavaScript code:

```
     var contextUser = sforce.apex.execute("myClass", "getContextUserName", {});

```

Note: If a namespace has been defined for your organization, you must include it in the JavaScript code when you invoke
the class. For example, to call the _`myClass`_ class, the JavaScript code from above would be rewritten as follows:

```
       var contextUser = sforce.apex.execute("myNamespace.myClass", "getContextUserName",

        {});

```

To verify whether your organization has a namespace, log in to your Salesforce organization and from Setup, enter _`Packages`_
in the `Quick Find` box, then select **Packages** . If a namespace is defined, it’s listed under Developer Settings.

[For more information on the return datatypes, see Data Types in AJAX Toolkit](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/ajax/sforce_api_ajax_datatypes.htm)

Use the following line to display a window with debugging information:

```
   sforce.debug.trace=true;

### Apex Transactions and Governor Limits

```

Apex Transactions ensure the integrity of data. Apex code runs as part of atomic transactions. Governor execution limits ensure the
efficient use of resources on the Lightning Platform multitenant platform.

Most of the governor limits are per transaction, and some aren’t, such as 24-hour limits.


#### Apex Developer Guide Apex Transactions and Governor Limits

To make sure Apex adheres to governor limits, certain design patterns should be used, such as bulk calls and foreign key relationships
in queries.

#### Apex Transactions

An _Apex transaction_ represents a set of operations that are executed as a single unit. All DML operations in a transaction must complete
successfully. If an error occurs in one operation, the entire transaction is rolled back and no data is committed to the database. The
boundary of a transaction can be a trigger, a class method, an anonymous block of code, a Visualforce page, or a custom Web service
method.

Execution Governors and Limits
Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces limits so that runaway Apex code or
processes don’t monopolize shared resources. If some Apex code exceeds a limit, the associated governor issues a runtime exception
that can’t be handled.

Set Up Governor Limit Email Warnings
You can specify users in your organization to receive an email notification when they invoke Apex code that surpasses 50% of
allocated governor limits. Only per-request limits are checked for sending email warnings; per-org limits like concurrent long-running
requests are not checked. These email notifications do not count against the daily single email limit.

Running Apex within Governor Execution Limits
When you develop software in a multitenant cloud environment such as the Lightning platform, you don’t have to scale your code,
because the Lightning platform does it for you. Because resources are shared in a multitenant platform, the Apex runtime engine
enforces some limits to ensure that no one transaction monopolizes shared resources.

#### Apex Transactions

An _Apex transaction_ represents a set of operations that are executed as a single unit. All DML operations in a transaction must complete
successfully. If an error occurs in one operation, the entire transaction is rolled back and no data is committed to the database. The
boundary of a transaction can be a trigger, a class method, an anonymous block of code, a Visualforce page, or a custom Web service
method.

Note: Payments transactions are the exception to DML operation errors. Even if an error occurs, data is committed and payment
records are generated because the transaction has already happened at the payment gateway.

All operations that occur inside the transaction boundary represent a single unit of operations, including calls to external code, such as
classes or triggers that run in the transaction boundary. For example: a custom Apex Web service method causes a trigger to fire, which
in turn calls a method in a class. In this case, all changes are committed to the database only after all operations in the transaction finish
executing and don’t cause any errors. If an error occurs in any of the intermediate steps, all database changes are rolled back and the
transaction isn’t committed.

An Apex transaction is sometimes referred to as an execution context. This guide uses the term Apex transaction.

How are Transactions Useful?

Transactions are useful when several operations are related, and either all or none of the operations are committed. The goal is to keep
the database in a consistent state. There are many business scenarios that benefit from transaction processing. For example, transferring
funds from one bank account to another is a common scenario. It involves debiting the first account and crediting the second account
with the amount to transfer. These two operations must be committed together to the database. If the debit operation succeeds and
the credit operation fails, the account balances become inconsistent.


Apex Developer Guide Apex Transactions and Governor Limits

Example

This example shows how all DML `insert` operations in a method are rolled back when the last operation causes a validation rule
failure. In this example, the `invoice` method is the transaction boundary—all code that runs within this method either commits all
changes to the platform database or rolls back all changes. In this case, we add an invoice statement with a line item for the pencils
merchandise. The Line Item is for a purchase of 5,000 pencils specified in the Units_Sold__c field, which is more than the entire pencils
inventory of 1,000. This example assumes a validation rule has been set up to check that the total inventory of the merchandise item is
enough to cover new purchases.

Since this example attempts to purchase more pencils (5,000) than items in stock (1,000), the validation rule fails and throws an exception.
Code execution halts at this point and all DML operations processed before this exception are rolled back. The invoice statement and
the line item aren’t added to the database, and their `insert` DML operations are rolled back.

In the Developer Console, execute the static `invoice` method.

```
   // Only 1,000 pencils are in stock.

   // Purchasing 5,000 pencils cause the validation rule to fail,

   // which results in an exception in the invoice method.

   Id invoice = MerchandiseOperations.invoice('Pencils', 5000, 'test 1');

```

This definition is the `invoice` method. The update of total inventory causes an exception due to the validation rule failure. As a result,
the invoice statements and line items are rolled back and aren’t inserted into the database.

```
   public class MerchandiseOperations {

      public static Id invoice( String pName, Integer pSold, String pDesc) {

        // Retrieve the pencils sample merchandise

        Merchandise__c m = [SELECT Price__c,Total_Inventory__c

           FROM Merchandise__c WHERE Name = :pName LIMIT 1];

        // break if no merchandise is found

        System.assertNotEquals(null, m);

        // Add a new invoice

        Invoice_Statement__c i = new Invoice_Statement__c(

           Description__c = pDesc);

        insert i;

        // Add a new line item to the invoice

        Line_Item__c li = new Line_Item__c(

           Name = '1',

           Invoice_Statement__c = i.Id,

           Merchandise__c = m.Id,

           Unit_Price__c = m.Price__c,

           Units_Sold__c = pSold);

        insert li;

        // Update the inventory of the merchandise item

        m.Total_Inventory__c -= pSold;

        // This causes an exception due to the validation rule

        // if there is not enough inventory.

        update m;

        return i.Id;

      }

   }

```


Apex Developer Guide Apex Transactions and Governor Limits

#### Execution Governors and Limits

Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces limits so that runaway Apex code or processes
don’t monopolize shared resources. If some Apex code exceeds a limit, the associated governor issues a runtime exception that can’t
be handled.

The Apex limits, or _governors_, track, and enforce the statistics outlined in the following tables and sections.

**•** Per-Transaction Apex Limits

**•** Per-Transaction Certified Managed Package Limits

**•** Lightning Platform Apex Limits

**•** Static Apex Limits

**•** Size-Specific Apex Limits

**•** Miscellaneous Apex Limits

In addition to the core Apex governor limits, email limits and push notification limits are also included later in this topic for your
convenience.

Per-Transaction Apex Limits

These limits count for each Apex transaction. For Batch Apex, these limits are reset for each execution of a batch of records in the
`execute` method.

This table lists limits for synchronous Apex and asynchronous Apex (Batch Apex and future methods) when they’re different. Otherwise,
this table lists only one limit that applies to both synchronous and asynchronous Apex.

Note:

**•** Although scheduled Apex is an asynchronous feature, synchronous limits apply to scheduled Apex jobs.

**•** For Bulk API and Bulk API 2.0 transactions, the effective limit is the higher of the synchronous and asynchronous limits. For
example, the maximum number of Bulk Apex jobs added to the queue with `System.enqueueJob` is the synchronous
limit (50), which is higher than the asynchronous limit (1).

**Description** **Synchronous** **Asynchronous**
**Limit** **Limit**

Total number of SOQL queries issued [1] 100 200

Total number of records retrieved by SOQL queries 50,000 50,000

Total number of records retrieved by `Database.getQueryLocator` 10,000 10,000

Total number of SOSL queries issued 20 20

Total number of records retrieved by a single SOSL query 2,000 2,000

Total number of DML statements issued [2] 150 150

Total number of records processed as a result of DML statements, `Approval.process`, 10,000 10,000
or `database.emptyRecycleBin`

Total stack depth for any Apex invocation that recursively fires triggers due to `insert`, 16 16

`update`, or `delete` statements [3]

Total number of callouts (HTTP requests or web services calls) in a transaction 100 100


Apex Developer Guide Apex Transactions and Governor Limits

**Description** **Synchronous** **Asynchronous**
**Limit** **Limit**

Maximum cumulative timeout for all callouts (HTTP requests or Web services calls) in a 120 seconds 120 seconds
transaction

Maximum number of methods with the `future` annotation allowed per Apex invocation 50 0 in batch and
future contexts; 50

in queueable
context

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

Maximum number of cursor fetch calls per transaction 10 10

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


Apex Developer Guide Apex Transactions and Governor Limits

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
statements your org’s native code can execute. This limit increase means more than 150 DML statements can execute during a single
transaction if code from the managed package and your native org both executes. Similarly, the certified managed package gets its own
100-SOQL-query limit for synchronous Apex, in addition to the org’s native code limit of 100 SOQL queries.


Apex Developer Guide Apex Transactions and Governor Limits

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

Lightning Platform Apex Limits

The limits in this table aren't specific to an Apex transaction; Lightning Platform enforces these limits.


Apex Developer Guide Apex Transactions and Governor Limits

**Description** **Limit**

The maximum number of asynchronous Apex method executions (batch Apex, future methods,
Queueable Apex, and scheduled Apex) per a 24-hour period [1,6,7]

250,000 or the number of user
licenses in your org multiplied
by 200, whichever is greater

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
`OrgLimits.getAll()` or `OrgLimits.getMap()` [. See List Organization Limits in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/dome_limits.htm) _REST API Developer Guide_ [and OrgLimits](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_OrgLimits.htm)
[Class in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_OrgLimits.htm) _Apex Reference Guide_ .


Apex Developer Guide Apex Transactions and Governor Limits

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


Apex Developer Guide Apex Transactions and Governor Limits

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
`ConnectApi` method calls are also subject to rate limits. `ConnectApi` rate limits match Connect REST API rate limits, and
have a per user, per namespace, per hour rate limit. When you exceed the rate limit, a `ConnectApi.RateLimitException`
is thrown. Your Apex code must catch and handle this exception.

For migrated orgs and orgs created in Summer ’24 and later, only `ConnectApi` method calls that require Chatter are subject to
the per user, per namespace, per hour rate limit. The documentation for every `ConnectApi` method indicates whether Chatter
is required. `ConnectApi` [method calls that don’t require Chatter count toward the Salesforce Platform total API request allocations,](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
which are per org and span a 24-hour period.

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
[For best performance, use selective SOQL queries. This is especially important for queries inside triggers. See More Efficient SOQL](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_VLSQ.htm)
[Queries.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_VLSQ.htm)

Email Limits

**Inbound Email Limits**

Email Services: Maximum Number of Email Messages Processed Number of user licenses multiplied by
1,000; maximum 1,000,000

(Includes limit for On-Demand Email-to-Case)

Email Services: Maximum Size of Email Message (Body and Attachments) 25 MB [1]

On-Demand Email-to-Case: Maximum Email Attachment Size 25 MB


Apex Developer Guide Apex Transactions and Governor Limits

On-Demand Email-to-Case: Maximum Number of Email Messages Processed Number of user licenses multiplied by
1,000; maximum 1,000,000

(Counts toward limit for Email Services)

1 The maximum size of email messages for Email Services varies depending on character set and transfer encoding of the body parts.
The size of an email message includes the email headers, body, attachments, and encoding. As a result, an email with a 35-MB
attachment likely exceeds the 25-MB size limit for an email message after accounting for the headers, body, and encoding.

When defining email services, note the following:

**•** An email service only processes messages it receives at one of its addresses.

**•** Salesforce limits the total number of messages that all email services combined, including On-Demand Email-to-Case, can
process daily. Messages that exceed this limit are bounced, discarded, or queued for processing the next day, depending on
how you configure the failure response settings for each email service. Salesforce calculates the limit by multiplying the number
of user licenses by 1,000; maximum 1,000,000. For example, if you have 10 licenses, your org can process up to 10,000 email
messages a day.

**•** Email service addresses that you create in your sandbox can’t be copied to your production org.

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
a trial period, you can send to a maximum of 50 recipients per day, and each single email can have up to 15 recipients..

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


Apex Developer Guide Apex Transactions and Governor Limits

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

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

#### Set Up Governor Limit Email Warnings

You can specify users in your organization to receive an email notification when they invoke Apex code that surpasses 50% of allocated
governor limits. Only per-request limits are checked for sending email warnings; per-org limits like concurrent long-running requests
are not checked. These email notifications do not count against the daily single email limit.

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


Apex Developer Guide Apex Transactions and Governor Limits

Maximum number of Apex jobs added to the queue with `System.enqueueJob`

Total number of records retrieved by `Database.getQueryLocator`

Total number of mobile Apex push calls

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

```


Apex Developer Guide Apex Transactions and Governor Limits

```
   // Once DML call for the entire list of line items

   update updatedList;

```

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


### Apex Developer Guide Using Salesforce Features with Apex

**Example:** Query without a for loop

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

Data Cloud In Apex
You can use Apex with Data Cloud objects, with constraints and considerations that are detailed in this topic . Further, you can mock
SOQL query responses for Data Cloud data model objects (DMOs) in Apex testing by using SOQL stub methods and a test class.

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
Flow Builder lets admins build applications, known as _flows_, that automate a business process by collecting data and doing something
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

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_system_quickaction.htm)_ : QuickAction Class

_Apex Reference Guide_ [: QuickActionRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_quickactionrequest.htm)

_Apex Reference Guide_ [: QuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_quickactionresult.htm)

_Apex Reference Guide_ [: DescribeQuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describequickactionresult.htm)

_Apex Reference Guide_ [: DescribeQuickActionDefaultValue Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describequickactiondefaultvalue.htm)

_Apex Reference Guide_ [: DescribeLayoutSection Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describelayoutsection.htm)

_Apex Reference Guide_ [: DescribeLayoutRow Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describelayoutrow.htm)

_Apex Reference Guide_ [: DescribeLayoutItem Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describelayoutitem.htm)

_Apex Reference Guide_ [: DescribeLayoutComponent Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describelayoutcomponent.htm)

_Apex Reference Guide_ [: DescribeAvailableQuickActionResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_quickaction_describeavailablequickactionresult.htm)

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
row limit.

Apex cursors throw these new System exceptions: `System.FatalCursorException` and
`System.TransientCursorException` . Transactions that fail with `System.TransientCursorException` can be
retried.

Apex Cursor Example

```
   public class QueryChunkingQueuable implements Queueable {

      private Database.Cursor locator;

      private integer position;

      public QueryChunkingQueuable() {

        locator = Database.getCursor

              ('SELECT Id FROM Contact WHERE LastActivityDate = LAST_N_DAYS:400');

        position = 0;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      public void execute(QueueableContext ctx) {

        List<Contact> scope = locator.fetch(position, 200);

        position += scope.size();

        // do something, like archive or delete the scope list records

        if(position < locator.getNumRecords() ) {

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

**•** To retrieve the number of deleted rows that the cursor skipped in the `fetchPage()` operation, call
`CursorFetchResult.getDeletedRows()` .

**•** To retrieve the next page of results, first call `CursorFetchResult.getNextIndex()`, and then use the return value as the
_`start`_ parameter in the next `fetchPage()` call.

**•** To determine whether to make subsequent calls to `fetchPage()`, use the `CursorFetchResult.isDone()` method.
The method returns `true` if the specified _`pageSize`_ is reached, which indicates that a full page of results is retrieved. It also
returns `true` if the pagination cursor reaches the end of a result set before the specified _`pageSize`_ is reached, which indicates
that a partial, final page of results is retrieved.


Apex Developer Guide Using Salesforce Features with Apex

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

[To view transaction and daily limits for Apex cursors and Apex pagination cursors, see Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

[Apex cursors and pagination cursors have the same expiration limits as API Query cursors. See API Query Cursor Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apicursors.htm)

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

   Limits.getLimitApexPaginationCursorRows());

   // Fetch a page

   Database.CursorFetchResult page = pagCursor.fetchPage(0, 5);

   // Check shared fetch call limit

   System.debug('Fetch Calls: ' + Limits.getFetchCallsOnApexCursor() + '/' +

   Limits.getLimitFetchCallsOnApexCursor());

   // Get daily limits map

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

_[Apex Reference Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Database_Cursor.htm)_ Cursor Class

_Apex Reference Guide:_ [PaginationCursor Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Database_PaginationCursor.htm)

#### Approval Processing

An approval process automates how records are approved in Salesforce. An approval process specifies each step of approval, including
from whom to request approval and what to do at each point of the process.

**•** Use the Apex process classes to create approval requests and process the results of those requests:

**–** [ProcessRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ProcessRequest.htm)

**–** [ProcessResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ProcessResult.htm)

**–** [ProcessSubmitRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ProcessSubmitRequest.htm)

**–** [ProcessWorkItemRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ProcessWorkitemRequest.htm)

**•** Use the `Approval.process` method to submit an approval request and approve or reject existing approval requests. For more
[information, see Approval Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_approval.htm)

Note: The `process` method counts against the DML limits for your organization. See Execution Governors and Limits.

For more information about approval processes, see “Set Up an Approval Process” in the Salesforce online help.

##### Apex Approval Processing Example Apex Approval Processing Example

The following sample code initially submits a record for approval, then approves the request. This example assumes that a pre-existing
approval process on Account exists and is valid for the Account record created.

```
   public class TestApproval {

      void submitAndProcessApprovalRequest() {

        // Insert an account

        Account a = new Account(Name='Test',annualRevenue=100.0);

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

        // Verify the results

        System.assert(result2.isSuccess(), 'Result Status:'+result2.isSuccess());

        System.assertEquals(

           'Approved', result2.getInstanceStatus(),

           'Instance Status'+result2.getInstanceStatus());

      }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

#### Authentication

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

               dom.XmlNode xroot = docx.getrootelement() ;

               if(xroot != null){

                 ret = xroot.getChildElement(token, ns).getText();

               }

               return ret;

             }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

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

      }

      static testMethod void testInitiateMethod() {

          String stateToPropogate = 'mocktestState';

          Map<String,String> authProviderConfiguration = setupAuthProviderConfig();

          Concur concurCls = new Concur();

          concurCls.redirectUrl = authProviderConfiguration.get('Redirect_Url__c');

          PageReference expectedUrl = new

   PageReference(authProviderConfiguration.get('Auth_Url__c') + '?client_id='+

                                authProviderConfiguration.get('Key__c')

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

          Test.setMock(HttpCalloutMock.class, new ConcurMockHttpResponseGenerator());

          Auth.AuthProviderTokenResponse response = new

   Auth.AuthProviderTokenResponse(PROVIDER, OAUTH_TOKEN,'sampleOauthSecret', STATE);

         Auth.UserData actualUserData = concurCls.getUserInfo(authProviderConfiguration,

    response) ;

          Map<String,String> provMap = new Map<String,String>();

          provMap.put('key1', 'value1');

          provMap.put('key2', 'value2');

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

     }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: AuthProviderPlugin Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_Auth_AuthProviderPlugin.htm)

[Salesforce Help: Create a Custom External Authentication Provider](https://help.salesforce.com/HTViewHelpDoc?id=sso_provider_plugin_custom.htm&language=en_US)


Apex Developer Guide Using Salesforce Features with Apex

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

In this example, the `[OAuth2TokenExchangeType](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)` enum specifies that the token is a JSON Web Token (JWT). The first method,
`validateIncomingToken`, uses a method in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm#apex_Auth_JWTUtil_methods)` class to validate the token by calling an endpoint on the
external identity provider.

Validating the token returns an instance of the `[Auth.TokenValidationResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)` class with information about the token and the
user.

With the second method, `getUserForTokenSubject`, the handler gets information about the user from the token validation
result. The example shows two ways to bundle the user data—either by creating a class with a custom data structure or by using the
`[Auth.UserData](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_UserData.htm)` class.

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

        //If it’s an ID Token or JWT, try using our JWT validation methods

        //This example assumes that the incoming token is a JWT and that there is a public

    keys endpoint on the identity provider

        //Be very careful with any logic in this method, and test carefully before using

        Boolean isValid = false;

        Auth.JWT jwt;

        //Custom data structure

        CustomStructuredUserData customData;

        //Standard user data structure

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

      }

      public override User getUserForTokenSubject(Id networkId, Auth.TokenValidationResult

   result, Boolean canCreateUser, String appDeveloperName, Auth.IntegratingAppType appType)

   {

        //If you passed data from the validation method, grab it now. Remember to cast

   back for the custom data

        CustomStructuredUserData customData = (CustomStructuredUserData)result.data;

        Auth.UserData userData = result.userData;

        //If you don’t have any data from the token, you can perform a callout using the

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

**•** For JWTs and ID tokens, use methods in the `[Auth.JWTUtil](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)` class.

**•** For opaque tokens, such as opaque access and refresh tokens, call out to the identity provider’s introspection or user info endpoints.

**•** For SAML assertions, write code to parse the XML from the assertion.

In this example, the handler validates a JWT from the identity provider. The handler determines the token type and uses the
`validateJWTWithKey` method in the `Auth.JWTUtil` class to validate the JWT with a public key.

```
   global override Auth.TokenValidationResult validateIncomingToken(String appDeveloperName,

    Auth.IntegratingAppType appType, String incomingToken, Auth.OAuth2TokenExchangeType

   tokenType) {

        if (tokenType == Auth.OAuth2TokenExchangeType.JWT) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

                    if (fieldName == 'active') {

                       parser.nextToken();

                       active = parser.getBooleanValue();

                       if (!active) {

                        return new Auth.TokenValidationResult(false);

                       }

                    }

                    if (fieldName == 'username') {

```


Apex Developer Guide Using Salesforce Features with Apex

```
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
`isUserCreationAllowed` field on your `[OauthTokenExchangeHandler](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_oauthtokenexchangehandler.htm)` metadata definition must be set to `true` . When
you set this metadata field to `true`, the `CanCreateUser` parameter in the `getUserForTokenSubject` Apex method is
also set to `true` .

If necessary, to get more information about the incoming subject, the handler can call out to the external identity provider or another
external system.

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

      }

   }

```

SEE ALSO:

_Salesforce Help:_ [OAuth 2.0 Token Exchange Flow](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_token_exchange_overview.htm&type=5&language=en_US)

_Apex Reference Guide:_ [Oauth2TokenExchangeHandler Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm)

_Apex Reference Guide:_ [TokenValidationResult Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_TokenValidationResult.htm)

_Apex Reference Guide:_ [OAuth2TokenExchangeType Enum](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_OAuth2TokenExchangeType.htm)

_Apex Reference Guide:_ [IntegratingAppType Enum](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_Auth_IntegratingAppType.htm)

_[Apex Reference Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Auth_JWTUtil.htm)_ JWTUtil Class

#### Chatter Answers and Ideas

In Chatter Answers and Ideas, use zones to organize ideas and answers into groups. Each zone can have its own focus, with unique ideas
and answers topics to match that focus.


Apex Developer Guide Using Salesforce Features with Apex

To work with zones in Apex, use the `Answers`, `Ideas`, and `ConnectApi.Zones` classes.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_answers.htm)_ : Answers Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_ideas.htm)_ : Ideas Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Zones_static_methods.htm)_ : Zones Class

#### Use Cases for the CommercePayments Namespace

Review walkthroughs, use cases, and reference material for the `CommercePayments` platform.

To review `CommercePayments` [class reference docs, go to CommercePayments Namespace.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_commercepayments.htm)

##### Payment Gateway Adapters

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


Apex Developer Guide Using Salesforce Features with Apex

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

A synchronous gateway adapter implements the `[PaymentGatewayAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAdapter.htm#apex_interface_commerce_payments_PaymentGatewayAdapter)` . In this topic, we examine a sample
synchronous adapter by looking at `PaymentGatewayAdapter`, and then the `processRequest` method, which drives most
of the communication between the payment platform and the payment gateway.

Note: Payment gateway adapters can’t make future calls, external callouts using `System.Http`, asynchronous calls, queueable
calls, or execute DMLs using SOQL.

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


Apex Developer Guide Using Salesforce Features with Apex

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

   } else if ( requestType == commercepayments.RequestType.ReferencedRefund) {

      response = createRefundResponse(res);

   }

   return response;

```

Using Custom Data

[To transfer additional, custom data from the frontend to your payment gateway adapter, use the Checkout Payments Connect API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
Sending custom data to the adapter supports use cases like implementing conditional logic based on specific data or mapping
asynchronous webhook events to a cart by passing an identifier.

To send custom data to your payment gateway adapter, use the `paymentsData` [parameter in the Checkout Payments Connect API](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
input payload. This parameter is a serialized map of type `<String, String>` that supports up to four key-value pairs. Each key
and each value can contain up to 255 characters. `paymentsData` is only applicable to Auth and PostAuth payment requests. Simple
purchase orders don’t support `paymentsData` .

[Similarly, the Post Authorization input payload has an](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_payment_post_auth.htm) `additionalData` property, which is also a map of type `<String, String>` .
The `paymentsData` property is accepted for Auth and PostAuth requests and is transferred to the Payment APIs through the
`additionalData` property.


Apex Developer Guide Using Salesforce Features with Apex

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

**a.** [Generate an access token according to the instructions in Connect to Connect REST API Using OAuth.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/quickstart_connecting.htm)

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

**4.** Create a payment gateway record. The PaymentGateway object stores information about the connection to the external payment
gateway. The record requires these field values.

**•** Payment Gateway Name: Name of the external payment gateway.

**•** Merchant Credential ID: ID of the named credential that you created.

**•** Payment Gateway Provider ID: ID of the payment gateway provider that you created.


Apex Developer Guide Using Salesforce Features with Apex

**•** Status: Active

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_paymentgateway.htm)_ : PaymentGateway

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewayprovider.htm)_ : PaymentGatewayProvider

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

An asynchronous gateway adapter class must implement both the `[PaymentGatewayAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAdapter.htm#apex_interface_commerce_payments_PaymentGatewayAdapter)` and the
`[PaymentGatewayAsyncAdapter Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_commercepayments_PaymentGatewayAsyncAdapter.htm#apex_interface_commercepayments_PaymentGatewayAsyncAdapter)` . The adapter class must also implement the `processRequest` method for
PaymentGatewayAdapter and the `processNotification` method for PaymentGatewayAsyncAdapter.

```
   global with sharing class SampleAdapter implements

   commercepayments.PaymentGatewayAsyncAdapter, commercepayments.PaymentGatewayAdapter {

      global SampleAdapter() {}

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


Apex Developer Guide Using Salesforce Features with Apex

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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


Apex Developer Guide Using Salesforce Features with Apex

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

[To transfer additional, custom data from the frontend to your payment gateway adapter, use the Checkout Payments Connect API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
Sending custom data to the adapter supports use cases like implementing conditional logic based on specific data or mapping
asynchronous webhook events to a cart by passing an identifier.

To send custom data to your payment gateway adapter, use the `paymentsData` [parameter in the Checkout Payments Connect API](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_checkouts_payments.htm)
input payload. This parameter is a serialized map of type `<String, String>` that supports up to four key-value pairs. Each key
and each value can contain up to 255 characters. `paymentsData` is only applicable to Auth and PostAuth payment requests. Simple
purchase orders don’t support `paymentsData` .

[Similarly, the Post Authorization input payload has an](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_payment_post_auth.htm) `additionalData` property, which is also a map of type `<String, String>` .
The `paymentsData` property is accepted for Auth and PostAuth requests and is transferred to the Payment APIs through the
`additionalData` property.

Debugging

Usually, Apex debug logs are available in the developer console. However, Salesforce doesn’t store debug logs from the
`processNotification` method in the developer console. To view this part of the method flow using system.debug, review the
[Collect Debug Logs for Guest Users section of Set Up Debug Logging.](https://help.salesforce.com/articleView?id=code_add_users_debug_log.htm&type=5&language=en_US)

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


Apex Developer Guide Using Salesforce Features with Apex

**4.** Create a payment gateway provider. The PaymentGatewayProvider object stores details about the payment gateway that Salesforce
Payments communicates with when processing a transaction.

**a.** [Generate an access token according to the instructions in Connect to Connect REST API Using OAuth.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/quickstart_connecting.htm)

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


Apex Developer Guide Using Salesforce Features with Apex

**c.** Enter the webhook in your external payment gateway’s standard notification settings.

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_paymentgatewayprovider.htm)_ : PaymentGatewayProvider

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_paymentgateway.htm)_ : PaymentGateway

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

###### Authorization Reversal Apex Class Implementation

The Authorization Reversal Service uses the `AuthorizationReversalRequest` and
`AuthorizationReversalResponse` classes to manage the creation and storage of authorization reversal information.
Implement these classes in your payment gateway adapter.

##### Payment Authorization Reversal Service API

An authorization reversal is a transaction that negates an authorization by releasing the hold on funds in a customer’s payment
method. Use the authorization reversal service to provide users with the ability to reverse an outstanding payment authorization.

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


Apex Developer Guide Using Salesforce Features with Apex

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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


Apex Developer Guide Using Salesforce Features with Apex

The service accepts one authorization reversal request per call. The following payment authorization adjustment API parameters are
accepted.

**Table 8: Reversal Service Input Parameters**

Sample Request and Response

This request calls a $150 reversal against an authorization.

```
{

```

```
"accountId":"",

"amount": "150",* "comments": "authorization reversal request",

"effectiveDate":"2020-10-18T11:32:27.000Z",

"ipAddress": "202.95.77.70",

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

**Sample Response - Error**

```
   {

      "errorCode":"",

      "errorMessage":""

   }

```


Apex Developer Guide Using Salesforce Features with Apex

##### Tokenization Service

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
[field, available in API v48.0 and later. Both fields store gateway token values. However, GatewayTokenEncrypted uses Salesforce Classic](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/fields_about_encrypted_fields.htm)
[Encryption for Custom Fields to securely encrypt the token. GatewayToken doesn't use encryption. To ensure secure tokenization, we](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/fields_about_encrypted_fields.htm)
recommend using GatewayTokenEncrypted on your DigitalWallets and CardPaymentMethods. The AlternativePaymentMethod object
uses a GatewayToken field for token storage, however, this field is encrypted on AlternativePaymentMethods.

In API version 52.0 and later, CardPaymentMethods and DigitalWallets can’t store values for GatewayTokenEncryption and GatewayToken
at the same time on the same record. If you try to assign one while the other exists, Salesforce throws an error.

Your payment gateway adapter uses the `PaymentMethodTokenizationRequest` and
`PaymentMethodTokenizationResponse` classes to retrieve a gateway token from the payment gateway, encrypt it in
Salesforce, and store the value on a payment method entity. Let's see how we can configure these classes in our payment gateway
adapter.

Implementing Tokenization Classes in Your Gateway Adapter

The following code is used within your `PaymentGatewayAdapter` Apex class.

Gateway tokens are created and encrypted when the `GatewayResponse` class's `processRequest` method receives a tokenization
request. If the request type is `Tokenize`, `GatewayResponse` calls the `createTokenizeResponse` method and passes an
instance of the `PaymentMethodTokenizationRequest` class. The passed `PaymentMethodTokenizationRequest`


Apex Developer Guide Using Salesforce Features with Apex

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
and then build an instance of `[PaymentMethodTokenizationResponse](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentMethodTokenizationResponse.htm#apex_class_commercepayments_PaymentMethodTokenizationResponse)` based on the values that it receives from the payment
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

The `setGatewayTokenEncrypted` method is available in Salesforce API v52.0 and later. It uses Salesforce classic encryption to
set the encrypted token value that you can store in GatewayTokenEncrypted on a CardPaymentMethod or DigitalWallet, or in GatewayToken
on an AlternativePaymentMethod. We recommend using `setGatewayTokenEncrypted` to ensure your tokenized payment
method values are encrypted and secure.

```
      /** @description Method to set Gateway token to persist in Encrypted Text */

      global void setGatewayTokenEncrypted(String gatewayTokenEncrypted) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
         if (gatewayTokenSet) {

           throwTokenError();

         }

         this.delegate.setGatewayTokenEncrypted(gatewayTokenEncrypted);

         gatewayTokenEncryptedSet = true;

      }

```

If the instantiated class already has a gateway token, `setGatewayTokenEncrypted` throws an error.

Note: While the PaymentMethodTokenizationResponse's `[setGatewayToken](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentMethodTokenizationResponse.htm#apex_commercepayments_PaymentMethodTokenizationResponse_setGatewayToken)` method (available in API v48.0 and later) also
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
token in `[CardPaymentMethod](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_cardpaymentmethod.htm)` .

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

        "key2":"value2",

        "key3":"value3",

        "key4":"value4",

        "key5":"value5"

      }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

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

Example: Let's say you wanted to make an alternative payment method for GiroPay. First, create an
`AlternativePaymentMethod` record type.

**New RecordType**

```
   /services/data/v51.0/sobjects/RecordType

   {

   "Name" : "Giro Pay",

   "DeveloperName" : "GiroPay",

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

**1.** Get the payment capture request object from the `[PaymentGatewayContext Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)` .

EDITIONS

Available in: Salesforce
Spring ’20

```
  commercepayments.CaptureRequest =

  (commercepayments.CaptureRequest)gatewayContext.getPaymentRequest()

```

**2.** Set the HTTP request object.

```
  HttpRequest req = new HttpRequest();

  req.setHeader('Content-Type', 'application/json');

```

**3.** Read the parameters from the `[CaptureRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_CaptureRequest.htm#apex_class_commerce_payments_CaptureRequest)` object and prepare the HTTP request body.

**4.** Make the HTTP call to the gateway using the `[PaymentsHttp Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentsHttp.htm#apex_class_commerce_payments_PaymentsHttp)` .

```
  commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

  HttpResponse res = http.send(req);

```


Apex Developer Guide Using Salesforce Features with Apex

**5.** Parse the `httpResponse` and prepare the `[CaptureResponse](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_CaptureResponse.htm#apex_class_commerce_payments_CaptureResponse)` object.

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

**1.** Get the referenced refund request object from the `[PaymentGatewayContext Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentGatewayContext.htm#apex_class_commerce_payments_PaymentGatewayContext)` .

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

**3.** Read the parameters from the `[ReferencedRefundRequest object](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_ReferencedRefundRequest.htm#apex_class_commerce_payments_ReferencedRefundRequest)` and prepare the HTTP request body.

**4.** Make the HTTP call to the gateway using the `[PaymentsHttp Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_PaymentsHttp.htm#apex_class_commerce_payments_PaymentsHttp)` .

```
  commercepayments.PaymentsHttp http = new commercepayments.PaymentsHttp();

  HttpResponse res = http.send(req);

```

**5.** Parse the `httpResponse` and prepare the `[ReferencedRefundResponse](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_commercepayments_ReferencedRefundResponse.htm#apex_class_commerce_payments_ReferencedRefundResponse)` object.

```
  commercepayments.ReferencedRefundResponse referencedRefundResponse = new

  commercepayments.ReferencedRefundResponse();

  referencedRefundResponse.setGatewayResultCode(“”);

  referencedRefundResponse.setGatewayResultCodeDescription(“”);

  referencedRefundResponse.setGatewayReferenceNumber(“”);

  referencedRefundResponse.setSalesforceResultCodeInfo(getSalesforceResultCodeInfo(commercepayments.SalesforceResultCode.SUCCESS.name()));

  referencedRefundResponse.setGatewayReferenceDetails(“”);

  referencedRefundResponse.setAmount(double.valueOf(100);

```

**6.** Return the `referencedRefundResponse` .


Apex Developer Guide Using Salesforce Features with Apex

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

has access to. It doesn’t run in system mode like other Apex code.

[For Connect in Apex reference information, see ConnectApi Namespace.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_connect_api.htm)

#### Connect in Apex Examples

Use these examples to perform common tasks with Connect in Apex.

#### Connect in Apex Features

This topic describes which classes and methods to use to work with common Connect in Apex features.

Using ConnectApi Input and Output Classes
Some classes in the `ConnectApi` namespace contain static methods that access Connect REST API data. The `ConnectApi`
namespace also contains input classes to pass as parameters and output classes that calls to the static methods return.


Apex Developer Guide Using Salesforce Features with Apex

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

Post a Rich-Text Feed Element with Inline Image
Call a method or use the ConnectApiHelper repository to post a feed element with an already uploaded, inline image.

Post a Rich-Text Feed Element with a Code Block
Call a method to post a feed element with a code block.

Post a Feed Element with a New File (Binary) Attachment
Call a method to post a feed element with a new file.


Apex Developer Guide Using Salesforce Features with Apex

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

Edit a Comment
Call a method to edit a comment.

Follow a Record
Call a method to follow a record.

Unfollow a Record
Call a method to stop following a record.


Apex Developer Guide Using Salesforce Features with Apex

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

###### Get Feed Elements From a Feed

Call a method to get feed elements from a feed.

Call `[getFeedElementsFromFeed(communityId, feedType, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_2)` to get the first page of feed elements
from the context user’s news feed.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.News, 'me');

```


Apex Developer Guide Using Salesforce Features with Apex

The `getFeedElementsFromFeed` method is overloaded, which means that the method name has many different signatures. A
signature is the name of the method and its parameters in order.

Each signature lets you send different inputs. For example, one signature may specify the feed type and the subject ID. Another signature
could have those parameters and an additional parameter to specify the maximum number of comments to return for each feed element.

Tip: Each signature operates on certain feed types. Use the signatures that operate on the `ConnectApi.FeedType.Record`
to get group feeds, since a group is a record type.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

###### Get Feed Elements From Another User’s Feed

Call a method to get feed elements from another user’s feed.

Call `[getFeedElementsFromFeed(communityId, feedType, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_2)` to get the first page of feed elements
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

This example calls `[getFeedElementsFromFeed(communityId, feedType, subjectId, recentCommentCount,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_7a)`
`[density, pageParam, pageSize, sortParam, filter)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_7a)` to get only site-specific feed elements.

```
   ConnectApi.FeedElementPage fep =

   ConnectApi.ChatterFeeds.getFeedElementsFromFeed(Network.getNetworkId(),

   ConnectApi.FeedType.UserProfile, 'me', 3, ConnectApi.FeedDensity.FewerUpdates, null, null,

    ConnectApi.FeedSortOrder.LastModifiedDateDesc, ConnectApi.FeedFilter.CommunityScoped );

###### Post a Feed Element

```

Make a call to post a feed element.


Apex Developer Guide Using Salesforce Features with Apex

Call `[postFeedElement(communityId, subjectId, feedElementType, text)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_1)` to post a string of text.

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
use this example, which calls `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` .

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

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed item with files that have already been uploaded.

```
   // Define the FeedItemInput object to pass to postFeedElement

   ConnectApi.FeedItemInput feedItemInput = new ConnectApi.FeedItemInput();

   feedItemInput.subjectId = 'me';

   ConnectApi.TextSegmentInput textSegmentInput = new ConnectApi.TextSegmentInput();

   textSegmentInput.text = 'Would you please review these docs?';

   // The MessageBodyInput object holds the text in the post

   ConnectApi.MessageBodyInput messageBodyInput = new ConnectApi.MessageBodyInput();

   messageBodyInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

   messageBodyInput.messageSegments.add(textSegmentInput);

   feedItemInput.body = messageBodyInput;

   // The FeedElementCapabilitiesInput object holds the capabilities of the feed item.

```


Apex Developer Guide Using Salesforce Features with Apex

```
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
write a single line of code, or use this example, which calls `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` . In this
example, the image file is existing content that has already been uploaded to Salesforce as a content document (069). The post also
includes text and a mention.

```
   String communityId = null;

   String imageId = '069D00000001INA';

   String mentionedUserId = '005D0000001QNpr';

   String targetUserOrGroupOrRecordId = '005D0000001Gif0';

   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = targetUserOrGroupOrRecordId;

   input.feedElementType = ConnectApi.FeedElementType.FeedItem;

   ConnectApi.MessageBodyInput messageInput = new ConnectApi.MessageBodyInput();

   ConnectApi.TextSegmentInput textSegment;

   ConnectApi.MentionSegmentInput mentionSegment;

   ConnectApi.MarkupBeginSegmentInput markupBeginSegment;

   ConnectApi.MarkupEndSegmentInput markupEndSegment;

   ConnectApi.InlineImageSegmentInput inlineImageSegment;

   messageInput.messageSegments = new List<ConnectApi.MessageSegmentInput>();

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

_Apex Reference Guide_ [: ConnectApi.MarkupBeginSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_markup_begin_segment.htm)

_Apex Reference Guide_ [: ConnectApi.MarkupEndSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_markup_end_segment.htm)

_Apex Reference Guide_ [: ConnectApi.InlineImageSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_inline_image_segment.htm)

###### Post a Rich-Text Feed Element with a Code Block

Call a method to post a feed element with a code block.

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed item with a code block.

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

_Apex Reference Guide_ [: ConnectApi.MarkupBeginSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_markup_begin_segment.htm)

_Apex Reference Guide_ [: ConnectApi.MarkupEndSegmentInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_markup_end_segment.htm)

###### Post a Feed Element with a New File (Binary) Attachment

Call a method to post a feed element with a new file.

Important: In version 36.0 and later, you can’t post a feed element with a new file in the same call. Upload files to Salesforce first,
and then specify existing files when posting a feed element.

This example calls `[postFeedElement(communityId, feedElement, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_2)` to post a feed
item with a new file (binary) attachment.

```
   ConnectApi.FeedItemInput input = new ConnectApi.FeedItemInput();

   input.subjectId = 'me';

   ConnectApi.ContentCapabilityInput contentInput = new ConnectApi.ContentCapabilityInput();

   contentInput.title = 'Title';

   ConnectApi.FeedElementCapabilitiesInput capabilities = new

   ConnectApi.FeedElementCapabilitiesInput();

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


Apex Developer Guide Using Salesforce Features with Apex

This trigger calls `[postFeedElementBatch(communityId, feedElements)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElementBatch_1)` to bulk post to the feeds of newly inserted
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

This trigger calls `[postFeedElementBatch(communityId, feedElements)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElementBatch_1)` to bulk post to the feeds of newly inserted
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

This example calls `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`
`[actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` to create an action link group definition.

It saves the action link group ID from that call and associates it with a feed element in a call to
`[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` .

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

This example calls `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`
`[actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` to create an action link group definition.

It calls `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to associate the action
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

Call `[updateFeedElement(communityId, feedElementId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElement)` to edit a feed element. Feed items are
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

Call `[updateFeedElement(communityId, feedElementId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElement)` to edit a question title and post.

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

Call `[likeFeedElement(communityId, feedElementId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_likeFeedElement)` to like a feed element.

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

###### Bookmark a Feed Element

```

Call a method to bookmark a feed element.

Call `[updateFeedElementBookmarks(communityId, feedElementId, isBookmarkedByCurrentUser)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateFeedElementBookmarks_2)` to
bookmark a feed element.

```
   ConnectApi.BookmarksCapability bookmark =

   ConnectApi.ChatterFeeds.updateFeedElementBookmarks(null, '0D5D0000000KuGh', true);

###### Share a Feed Element (prior to Version 39.0)

```

Call a method to share a feed element.

Important: In API version 39.0 and later, `shareFeedElement(communityId, subjectId, feedElementType,`
`originalFeedElementId)` isn’t supported. See Share a Feed Element (in Version 39.0 and Later).

Call `[shareFeedElement(communityId, subjectId, feedElementType, originalFeedElementId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_shareFeedElement)` to
share a feed item (which is a type of feed element) with a group.

```
   ConnectApi.ChatterLike chatterLike = ConnectApi.ChatterFeeds.likeFeedElement(null,

   '0D5D0000000KuGh');

###### Share a Feed Element (in Version 39.0 and Later)

```

Call a method to share a feed element.

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to share a feed element.

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

Call `[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to send a direct message to two people.

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

Call `[postCommentToFeedElement(communityId, feedElementId, text)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_1)` to post a plain text comment to a feed
element.

```
   ConnectApi.Comment comment = ConnectApi.ChatterFeeds.postCommentToFeedElement(null,

   '0D5D0000000KuGh', 'I agree with the proposal.' );

###### Post a Comment with a Mention

```

Make call or use the ConnectApiHelper repository to post a comment with a mention.

[You can post comments with mentions two ways. Use the ConnectApiHelper repository on GitHub to write a single line of code, or use](https://github.com/forcedotcom/ConnectApiHelper)
this example, which calls `[postCommentToFeedElement(communityId, feedElementId, comment,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` .

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
`ConnectApi.CommentInput` object to pass to `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` .

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
`ConnectApi.BinaryInput` object to pass to the `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` method.

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
a single line of code, or use this example, which calls `[postCommentToFeedElement(communityId, feedElementId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[comment, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` . In this example, the image file is existing content that has already been uploaded to
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

This example calls `[postCommentToFeedElement(communityId, feedElementId, comment,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)`
`[feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postCommentToFeedElement_2)` to post a comment with a code block.

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

Call `[updateComment(communityId, commentId, comment)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updateComment)` to edit a comment.

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

Call `[follow(communityId, userId, subjectId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_follow)` to follow a record.

```
   ChatterUsers.ConnectApi.Subscription subscriptionToRecord =

   ConnectApi.ChatterUsers.follow(null, 'me', '001RR000002G4Y0');

```

SEE ALSO:

###### Unfollow a Record Unfollow a Record

Call a method to stop following a record.

When you follow a record such as a user, the call to `ConnectApi.ChatterUsers.follow` returns a
`ConnectApi.Subscription` object. To unfollow a record, pass the `id` property of that object to
`[deleteSubscription(communityId, subscriptionId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Chatter_static_methods.htm#apex_ConnectAPI_Chatter_deleteSubscription)` .

```
   ConnectApi.Chatter.deleteSubscription(null, '0E8RR0000004CnK0AU');

```

SEE ALSO:

Follow a Record

###### Get a Repository

Call a method to get a repository.

Call `[getRepository(repositoryId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepository_1)` to get a repository.

```
   final string repositoryId = '0XCxx0000000123GAA';

   final ConnectApi.ContentHubRepository repository =

   ConnectApi.ContentHub.getRepository(repositoryId);

###### Get Repositories

```

Call a method to get all repositories.

Call `[getRepositories()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositories_1)` to get all repositories and get the first SharePoint online repository found.

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

Call `[getAllowedItemTypes(repositoryId, repositoryFolderId, filter)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getAllowedItemTypes_2)` with a `filter` of `FilesOnly`
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

Call `[getPreviews(repositoryId, repositoryFileId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getPreviews_1)` to get all supported preview formats and their respective URLs
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

Call `[getFilePreview(repositoryId, repositoryFileId, formatType)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getFilePreview_1)` with a `formatType` of `Thumbnail`
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

Call `[getRepositoryFolderItems(repositoryId, repositoryFolderId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFolderItems_1)` to get the collection of items in a
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

Call `[getRepositoryFolder(repositoryId, repositoryFolderId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFolder_3)` to get a repository folder.

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

Call `[getRepositoryFile(repositoryId, repositoryFileId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFile_3)` to get a repository file without permissions information.

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

Call `[getRepositoryFile(repositoryId, repositoryFileId, includeExternalFilePermissionsInfo)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_getRepositoryFile_4)`
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

Call `[addRepositoryItem(repositoryId, repositoryFolderId, file)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_addRepositoryItem_5)` to create a file without binary content
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

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

###### Create a Repository File with Content

Call a method to create a file with binary content in a Google Drive repository folder.

Call `[addRepositoryItem(repositoryId, repositoryFolderId, file, filedata)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_addRepositoryItem_7)` to create a file with binary
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

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

_Apex Reference Guide_ [: ConnectApi.BinaryInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_binary.htm)

###### Update a Repository File Without Content (Metadata Only)

Call a method to update the metadata of a repository file.

Call `[updateRepositoryFile(repositoryId, repositoryFileId, file)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_updateRepositoryFile_7)` to update the metadata of a file in a
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

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

###### Update a Repository File with Content

Call a method to update a repository file with content.

Call `[updateRepositoryFile(repositoryId, repositoryFileId, file, fileData)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ContentHub_static_methods.htm#apex_ConnectAPI_ContentHub_updateRepositoryFile_8)` to update the content
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

_Apex Reference Guide_ [: ConnectApi.ContentHubItemInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_item.htm)

_Apex Reference Guide_ [: ConnectApi.ContentHubFieldValueInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_content_hub_field_value.htm)

_Apex Reference Guide_ [: ConnectApi.BinaryInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_binary.htm)

###### Get an Authentication URL

Call a method to get an authentication URL.


Apex Developer Guide Using Salesforce Features with Apex

Call `[getOAuthCredentialAuthUrl(requestBody)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_NamedCredentials_static_methods.htm#apex_ConnectAPI_NamedCredentials_getOAuthCredentialAuthUrl_1)` to retrieve the URL that a user must visit to begin an authentication
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

_Apex Reference Guide_ [: NamedCredentials Methods](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_NamedCredentials_static_methods.htm)

###### Resolve a Prompt Template

Call a method to resolve a prompt template.

Call `[generateMessagesForPromptTemplate(promptTemplateDevName,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_EinsteinLLM_static_methods.htm)`
`[promptTemplateGenerationsInput)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_EinsteinLLM_static_methods.htm)` to resolve a prompt template.

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

To create a cart with custom fields, call `[createCart(webstoreId, cartInput)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_createCart_1)` . Specify your custom fields using the
`customFields` property of `cartInput` . The type for `customFields` is `List<SObject>`, where the sObject is a WebCart.

Then, to add an item to the cart, call `[addItemToCart(webstoreId, effectiveAccountId, activeCartOrId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_9)`
`[cartItemInput, currencyIsoCode)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_9)` . You can specify custom fields using the `customFields` property of
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

[You can also go directly to the ConnectApi Namespace reference content.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_connect_api.htm)

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

**2.** Call `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`

to define an action link group that contains at least one action link.

**3.** Call `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed element
and associate the action link with it.

Use these methods to work with action links.

**ConnectApi Method** **Task**

`[ActionLinks.createActionLinkGroupDefinition](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` Create an action link group definition. To associate an action link
`[(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)` group with a feed element, first create an action link group

```
ActionLinks.deleteActionLinkGroupDefinition(communityId,

actionLinkGroupId)

ActionLinks.getActionLinkGroupDefinition(communityId,

actionLinkGroupId)

```

definition. Then post a feed element with an associated actions
capability.

`[ChatterFeeds.postFeedElement(communityId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` Post a feed element with an associated actions capability. Associate
`[feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` up to 10 action link groups with a feed element.

`[ActionLinks.getActionLink(communityId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLink_1)` Get information about an action link, including state for the context
`[actionLinkId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLink_1)` user.

`[ActionLinks.getActionLinkGroup(communityId,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkGroup_1)` Get information about an action link group including state for the
`[actionLinkGroupId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkGroup_1)` context user.

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

**2.** Call `[ConnectApi.ActionLinks.createActionLinkGroupDefinition(communityId, actionLinkGroup)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_createActionLinkGroupDefinition_1)`

to define an action link group that contains at least one action link.


Apex Developer Guide Using Salesforce Features with Apex

**3.** Call `[ConnectApi.ChatterFeeds.postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)` to post a feed element
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
example, the `actionUrl` property in the `[ConnectApi.ActionLinkDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_action_link_definition.htm)` looks like
`https://www.example.com/api/v1/exampleResource` .

You can use templates to change the values of the `actionUrl`, `headers`, or `requestBody` properties, even after a template is
distributed in a package. Let’s say you release a new API version that requires new inputs. An admin can change the inputs in the action
link template in Setup and even action links already associated with a feed element use the new inputs. However, you can’t add new
binding variables to a published action link template.

If your API isn’t versioned, you can use the `expirationDate` property of the
`[ConnectApi.ActionLinkGroupDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_action_link_group_definition.htm)` to avoid issues due to upgrades or changing functionality in your API.
[See Set the Action Link Group Expiration Time in Design Action Link Templates.](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template_design.htm&type=5&language=en_US)

**Errors**

Use the Action Link Diagnostic Information method
( `[ConnectApi.ActionLinks.getActionLinkDiagnosticInfo(communityId, actionLinkId)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ActionLinks_static_methods.htm#apex_ConnectAPI_ActionLinks_getActionLinkDiagnosticInfo_1)` ) to return
status codes and errors from executing `Api` action links. Diagnostic info is given only for users who can access the action link.

**Localized Labels**

Action links use a predefined set of localized labels specified in the `labelKey` property of the
`[ConnectApi.ActionLinkDefinitionInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_action_link_definition.htm)` request body and the `Label` field of an action link template.

[For a list of labels, see Actions Links Labels.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)


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

The `[ConnectApi.FeedElement.capabilities](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_feed_element.htm)` property holds a set of capabilities.

A capability includes both an indication that a feature is possible and data associated with that feature. If a capability property exists on
a feed element, that capability is available, even if there isn’t any data associated with the capability yet. For example, if the
`chatterLikes` capability property exists on a feed element, the context user can like that feed element. If the capability property
doesn’t exist on a feed element, it isn’t possible to like that feed element.

When posting a feed element, specify its characteristics in the `[ConnectApi.FeedElementInput.capabilities](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_feed_element.htm)` property.

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

The feed item ( `[ConnectApi.FeedItem](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_Feed_Item.htm)` ) layout elements are:

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

**`[postFeedElement(communityId, feedElement, feedElementFileUpload)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_2)`** **(version 35.0 and earlier)**
Post a rich-text feed element. Include mentions and hashtag topics, attach a file to a feed element, and associate action link groups
with a feed element. You can also use this method to share a feed element and add a comment.

**`[postFeedElement(communityId, feedElement)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_postFeedElement_3)`** **(version 36.0 and later)**
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

_Apex Reference Guide_ [: ChatterFavorites Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFavorites_static_methods.htm)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

_Apex Reference Guide_ [: ConnectApi Output Classes](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output.htm)

_Apex Reference Guide_ [: ConnectApi Input Classes](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input.htm)

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

**–** `[getAnnouncements()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Announcements_static_methods.htm#apex_ConnectAPI_Announcements_getAnnouncements_1)`

**•** `ChatterFeeds` methods:

**–** `[getComment()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getComment)`

**–** `[getCommentInContext()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getCommentInContext_1)`

**–** `[getCommentsForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getCommentsForFeedElement_1)`

**–** `[getExtensions()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getExtensions_1)`

**–** `[getFeed()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeed)`

**–** `[getFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElement_1)`

**–** `[getFeedElementBatch()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementBatch_1)`

**–** `[getFeedElementPoll()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementPoll_1)`

**–** `[getFeedElementsFromFeed()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsFromFeed_1)`

**–** `[getFeedElementsUpdatedSince()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedElementsUpdatedSince_1)`

**–** `[getFeedWithFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getFeedWithFeedElements_5)`


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getLike()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLike)`

**–** `[getLikesForComment()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLikesForComment)`

**–** `[getLikesForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLikesForFeedElement_1)`

**–** `[getLinkMetadata()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getLinkMetadata_1)`

**–** `[getPinnedFeedElementsFromFeed()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getPinnedFeedElementsFromFeed_1)`

**–** `[getRelatedPosts()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getRelatedPosts_1)`

**–** `[getThreadsForFeedComment()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getThreadsForFeedComment_1)`

**–** `[getVotesForComment()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getVotesForComment_1)`

**–** `[getVotesForFeedElement()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_getVotesForFeedElement_1)`

**–** `[searchFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_searchFeedElements_1)`

**–** `[searchFeedElementsInFeed()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_searchFeedElementsInFeed_1)`

**–** `[updatePinnedFeedElements()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm#apex_ConnectAPI_ChatterFeeds_updatePinnedFeedElements_2)`

**•** `ChatterGroups` methods:

**–** `[getGroup()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getGroup)`

**–** `[getGroups()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getGroups)`

**–** `[getMembers()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_getMembers)`

**–** `[searchGroups()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterGroups_static_methods.htm#apex_ConnectAPI_ChatterGroups_searchGroups)`

**•** `ChatterUsers` methods:

**–** `[getFollowers()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getFollowers)`

**–** `[getFollowings()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getFollowings)`

**–** `[getReputation()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getReputation_1)`

**–** `[getUser()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUser)`

**–** `[getUserBatch()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUserBatch)`

**–** `[getUserGroups()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getGroups_3)`

**–** `[getUsers()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_getUsers)`

**–** `[searchUserGroupDetails()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_searchUserGroups_3)`

**–** `[searchUsers()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterUsers_static_methods.htm#apex_ConnectAPI_ChatterUsers_searchUsers)`

**•** `CommerceCart` methods:

**–** `[addItemsToCart()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemsToCart_1)`

**–** `[addItemToCart()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_addItemToCart_1)`

**–** `[applyCartCoupon()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_applyCartCoupon_1)`

**–** `[calculateCart()](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_calculateCart_1)`

**–** `[cloneCart()](https://developer.salesforce.com/docs/atlas.en-us.246.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_Commerce_cloneCart_1)`

**–** `[copyCartToWishlist()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_copyCartToWishlist_1)`

**–** `[createCart()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_createCart_1)`

**–** `[deleteCart()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCart_1)`

**–** `[deleteCartCoupon()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCartCoupon_1)`

**–** `[deleteCartItem()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteCartItem_1)`

**–** `[deleteInventoryReservation()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_deleteInventoryReservation_1)` (developer preview)


Apex Developer Guide Using Salesforce Features with Apex

**–** `[evaluateShipping()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_evaluateShipping_1)`

**–** `[evaluateTaxes()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_evaluateTaxes_1)`

**–** `[getCartCoupons()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartCoupons_1)`

**–** `[getCartItems()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartItems_6)`

**–** `[getCartCompactSummary()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartCompactSummary_1)`

**–** `[getCartSummary()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getCartSummary_1)`

**–** `[getOrCreateActiveCartSummary()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_getOrCreateActiveCartSummary_2)`

**–** `[makeCartPrimary()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_makeCartPrimary_1)`

**–** `[setCartMessagesVisibility()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_setCartMessagesVisibility_1)`

**–** `[updateCartItem()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_updateCartItem_2)`

**–** `[upsertInventoryReservation()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCart_static_methods.htm#apex_ConnectAPI_CommerceCart_upsertInventoryReservation_2.htm)` (developer preview)

**•** `CommerceCatalog` methods:

**–** `[getCategoryMenuItems()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getCategoryMenuItems_1)`

**–** `[getProduct()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProduct_6)`

**–** `[getProducts()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProducts_4)`

**–** `[getProductCategory()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductCategory_2)`

**–** `[getProductCategoryChildren()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductCategoryChildren_1)`

**–** `[getProductCategoryPath()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getStorefrontCategoryPath_1)`

**–** `[getProductChildCollection()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceCatalog_static_methods.htm#apex_ConnectAPI_CommerceCatalog_getProductChildCollection_5)`

**•** `CommercePromotions` methods:

**–** `decreaseRedemption()`

**–** `[evaluate()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommercePromotions_static_methods.htm#apex_ConnectAPI_CommercePromotions_evaluate_1.xml)`

**–** `increaseRedemption()`

**•** `CommerceSearch` methods:

**–** `[getSortRules()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_getSortRules_1)`

**–** `[getSuggestions()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_getSuggestions_1)`

**–** `[searchProducts()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceSearch_static_methods.htm#apex_ConnectAPI_CommerceSearch_productSearch_1)`

**•** `CommerceStorePricing` methods:

**–** `[getProductPrice()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceStorePricing_static_methods.htm#apex_ConnectAPI_CommerceStorePricing_getProductPrice_1)`

**–** `[getProductPrices()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CommerceStorePricing_static_methods.htm#apex_ConnectAPI_CommerceStorePricing_getProductPrices_1)`

**•** `Communities` methods:

**–** `[getCommunity()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Communities_static_methods.htm#apex_ConnectAPI_Communities_getCommunity)`

**•** `EmployeeProfiles` methods:

**–** `[getPhoto()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_EmployeeProfiles_static_methods.htm#apex_ConnectAPI_EmployeeProfiles_getPhoto_2)`

**•** `ExtendedCommerceDelivery` methods:

**–** `[estimateDeliveryDate()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ExtendedCommerceDelivery_static_methods.htm#apex_ConnectAPI_ExtendedCommerceDelivery_estimateDeliveryDate_1)`

**•** `Knowledge` methods:


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getTopViewedArticlesForTopic()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTopicTopViewedArticles_1)`

**–** `[getTrendingArticles()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTrendingArticles_1)`

**–** `[getTrendingArticlesForTopic()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Knowledge_static_methods.htm#apex_ConnectAPI_Knowledge_getTrendingArticlesForTopic_1)`

**•** `ManagedContent` methods:

**–** `[getAllContent()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllContent_1)`

**–** `[getAllDeliveryChannels()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllDeliveryChannels_1)`

**–** `[getAllManagedContent()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getAllManagedContent_1)`

**–** `[getContentByContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getContentByContentKeys_2)`

**–** `[getContentByIds()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getContentByIds_2)`

**–** `[getManagedContentByContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByContentKeys_2)`

**–** `[getManagedContentByIds()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByIds_2)`

**–** `[getManagedContentByTopics()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopics_3)`

**–** `[getManagedContentByTopicsAndContentKeys()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopicsAndContentKeys_3a)`

**–** `[getManagedContentByTopicsAndIds()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContent_static_methods.htm#apex_ConnectAPI_ManagedContent_getManagedContentByTopicsAndIds_4)`

**•** `ManagedContentDelivery` methods:

**–** `[getChannel()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getChannel_1)`

**–** `[getChannels()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getChannels_1)`

**–** `[getCollectionItemsForChannel()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getCollectionItemsForChannel_1)`

**–** `[getCollectionItemsForSite()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getCollectionItemsForSite_2)`

**–** `[getManagedContentChannel()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentChannel_1)`

**–** `[getManagedContentForChannel()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentForChannel_1)`

**–** `[getManagedContentForSite()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentForSite_4)`

**–** `[getManagedContentsForChannel()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentsForChannel_2)`

**–** `[getManagedContentsForSite()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedContentDelivery_static_methods.htm#apex_ConnectAPI_ManagedContentDelivery_getManagedContentsForSite_4)`

**•** `ManagedTopics` methods:

**–** `[getManagedTopic()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedTopics_static_methods.htm#apex_ConnectAPI_ManagedTopics_getManagedTopic)`

**–** `[getManagedTopics()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ManagedTopics_static_methods.htm#apex_ConnectAPI_ManagedTopics_getManagedTopics_1)`

**•** `MarketingIntegration` methods:

**–** `[submitForm()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_MarketingIntegration_static_methods.htm#apex_ConnectAPI_MarketingIntegration_submitForm_1)`

**•** `NavigationMenu` methods:

**–** `[getCommunityNavigationMenu()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_NavigationMenu_static_methods.htm#apex_ConnectAPI_NavigationMenu_getCommunityNavigationMenu_1)`

**•** `NextBestActions` methods:

**–** `[executeStrategy()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_executeStrategy_1)`

**–** `[setRecommendationReaction()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_NextBestAction_static_methods.htm#apex_ConnectAPI_NextBestAction_setRecommendationReaction_1)`

**•** `Personalization` methods:

**–** `[getAudience()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudience_2)`

**–** `[getAudienceBatch()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudienceBatch_1)`


Apex Developer Guide Using Salesforce Features with Apex

**–** `[getAudiences()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getAudiences_1)`

**–** `[getTarget()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTarget_2)`

**–** `[getTargetBatch()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTargetBatch_1)`

**–** `[getTargets()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Personalization_static_methods.htm#apex_ConnectAPI_Personalization_getTargets_1)`

**•** `Recommendations` methods:

**–** `[getRecommendationsForUser()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Recommendations_static_methods.htm#apex_ConnectAPI_Recommendations_getRecommendationsForUser_1a)`

Note: Only article and file recommendations are available to guest users.

**•** `RecordUi` methods.

**–** `[getPicklistValuesByRecordType()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_RecordUi_static_methods.htm#apex_ConnectAPI_RecordUi_getPicklistValuesByRecordType_1)`

**•** `Search` methods.

**–** `[answer()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_answer_objects_1)`

**–** `[find()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_find_object_1)`

**–** `[findAndGroup()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Search_static_methods.htm#apex_ConnectAPI_Search_find_objects_1)`

**•** `Sites` methods:

**–** `[searchSite()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Sites_static_methods.htm#apex_ConnectAPI_Sites_searchSite_1)`

**•** `Topics` methods:

**–** `[getGroupsRecentlyTalkingAboutTopic()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getGroupsRecentlyTalkingAboutTopic)`

**–** `[getRecentlyTalkingAboutTopicsForGroup()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRecentlyTalkingAboutTopicsForGroup)`

**–** `[getRecentlyTalkingAboutTopicsForUser()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRecentlyTalkingAboutTopicsForUser)`

**–** `[getRelatedTopics()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getRelatedTopics)`

**–** `[getTopic()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTopic)`

**–** `[getTopics()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTopics)`

**–** `[getTrendingTopics()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_Topics_static_methods.htm#apex_ConnectAPI_Topics_getTrendingTopics)`

**•** `UserProfiles` methods:

**–** `[getPhoto()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_UserProfiles_static_methods.htm#apex_ConnectAPI_UserProfiles_getPhoto)`

SEE ALSO:

_Salesforce Help_ [: Give Secure Access to Unauthenticated Users with the Guest User Profile](https://help.salesforce.com/HTViewHelpDoc?id=networks_public_access.htm&language=en_US)

###### Supported Validations for DBT Segments

When creating or updating a segment, the ConnectApi.CdpSegmentInput class is subject to some SQL validations.

You can create a segment using the `[createSegment(input)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm#apex_ConnectAPI_CdpSegment_createSegment_4)` method with the `ConnectApi.CdpSegmentInput` class.
Similarly, you can update a segment using the `[updateSegment(segmentApiName, input)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm#apex_ConnectAPI_CdpSegment_updateSegment_4)` method with the same input
class. The `[ConnectApi.CdpSegmentDbtModelInput](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input_cdp_segment_dbt_model.htm)` input class, which is nested in the `ConnectApi.CdpSegmentInput`
class, provides validation for the SQL.

The `sql` property of the `ConnectApi.CdpSegmentDbtModelInput` is subject to these validations.


Apex Developer Guide Using Salesforce Features with Apex

##### Using ConnectApi Input and Output Classes

Some classes in the `ConnectApi` namespace contain static methods that access Connect REST API data. The `ConnectApi`
namespace also contains input classes to pass as parameters and output classes that calls to the static methods return.

`ConnectApi` methods take either simple or complex types. Simple types are primitive Apex data like integers and strings. Complex
types are `ConnectApi` input objects.

The successful execution of a `ConnectApi` method can return an output object from the `ConnectApi` namespace. `ConnectApi`
output objects can be made up of other output objects. For example, the `[ConnectApi.ActorWithId](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_actorWithIdOutput.htm)` output object contains
properties such as `id` and `url`, which contain primitive data types. It also contains a `mySubscription` property, which contains
a `ConnectApi.Reference` object.

Note: All Salesforce IDs in `ConnectApi` output objects are 18 character IDs. Input objects can use 15 character IDs or 18
character IDs.

SEE ALSO:

_Apex Reference Guide_ [: ConnectApi Input Classes](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_input.htm)

_Apex Reference Guide_ [: ConnectApi Output Classes](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output.htm)

##### Understanding Limits for ConnectApi Classes

Limits for methods in the `ConnectApi` namespace are different than the limits for other Apex classes.

For classes in the `ConnectApi` namespace, every write operation costs one DML statement against the Apex governor limit.
`ConnectApi` method calls are also subject to rate limiting. `ConnectApi` rate limits match Connect REST API rate limits. Both have
a per user, per namespace, per hour rate limit. When you exceed the rate limit, a `ConnectApi.RateLimitException` is thrown.
Your Apex code must catch and handle this exception.

For migrated orgs and orgs created in Summer ’24 and later, only `ConnectApi` method calls that require Chatter are subject to the
per user, per namespace, per hour rate limit. The documentation for every `ConnectApi` method indicates whether Chatter is required.
`ConnectApi` [method calls that don’t require Chatter count toward the Salesforce Platform total API request allocations, which are](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
per org and span a 24-hour period.

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


Apex Developer Guide Using Salesforce Features with Apex

##### Serializing and Deserializing ConnectApi Objects When ConnectApi output objects are serialized into JSON, the structure is similar to the JSON returned from Connect REST API. When ConnectApi input objects are deserialized from JSON, the format is also similar to Connect REST API.

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

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ConnectAPI_ChatterFeeds_static_methods.htm)_ : ChatterFeeds Class

_Apex Reference Guide_ [: ConnectApi.FeedElementCapabilities](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_feed_element_capabilities.htm)

_Apex Reference Guide_ [: ConnectApi.MessageSegment](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_msg_seg.htm)

_Apex Reference Guide_ [: ConnectApi.AbstractRecordView](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_connectapi_output_abstractRecordView.htm)

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

Connect in Apex methods don’t run in system mode, they run in the context of the current user (also called the _context user_ ). The methods
have access to whatever the context user has access to. Connect in Apex doesn’t support the `runAs` system method.

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

**System mode and context user**
Connect in Apex methods don’t run in system mode, they run in the context of the current user (also called the _context user_ ). The
methods have access to whatever the context user has access to. Connect in Apex doesn’t support the `runAs` system method.
When a method takes a _`subjectId`_ argument, often that subject must be the context user. In these cases, you can use the string
`me` to specify the context user instead of an ID.

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

To save Apex triggers for
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

#### Data Cloud In Apex

You can use Apex with Data Cloud objects, with constraints and considerations that are detailed in this topic . Further, you can mock
SOQL query responses for Data Cloud data model objects (DMOs) in Apex testing by using SOQL stub methods and a test class.

Using SOQL in Apex with Data Cloud Objects

Static SOQL is supported with Data Cloud data model objects (DMOs) as a more direct alternative to using either dynamic SOQL or
ConnectAPI. Additionally, SOQL queries against DMOs using Apex `Database.QueryLocator` or in FOR loops is supported in API
version 61.0 and later. In versions earlier than 61.0, only the first 201 records are returned. Batch Apex is blocked against DMOs when
using `QueryLocators`, but is supported when using `Iterable` .

Warning: Running SOQL queries against DMOs can result in Data Services credits being consumed from your Data Cloud
[subscription. For more information on how usage is billed, see Data Cloud Billable Usage Types. Use caution when using FOR loops,](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&type=5&language=en_US)
query locators, recursion, or any mechanism that can result in multiple queries to Data Cloud.

A static SOQL query against Data Cloud from Apex is considered a callout and is subject to the same restrictions as HTTP callouts from
Apex. For example, if there is pending DML, this sample code can result in an unexpected exception with this message:

```
   UnexpectedException: A callout was unsuccessful because of pending uncommitted work

   related to a process, flow, or Apex operation. Commit or roll back the work, and then

   try again.

   insert new Account(Name='Test');

   List<ssot_Account_dlm> dmo1 = [Select Id from ssot_Account_dlm];

```

Security Considerations

You must consider field- and record-level access when using Apex with Data Cloud data model objects (DMOs). DMOs in all data spaces
are accessible from Apex in system mode, even when a permission set for the data space isn’t explicitly assigned. Read-only object-level
access checks are supported if the user has access to the data space. There’s currently no support for field-level security or for record-level
access control. Apex features, such as WITH USER_MODE, WITH SECURITY_ENFORCED, describe calls, and
`Security.stripInaccessible()`, can check only object-level access for DMOs.

Starting with API version 61.0, you can get information on a specific DMO using `SObjectType.getDescribe()` . There’s no
field-level security to be enforced because all fields on DMOs that are accessed by field describes and security model checks are read
only. You can’t use `Schema.getGlobalDescribe()` to discover exposed DMOs. Instead, use the
`Schema.describeSObjects(List<String>)` method with the known DMO API names.

This example uses static SOQL with the _`UnifiedIndividual__dlm`_ Data Cloud object.

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

##### Mock SOQL Tests for Data Cloud Data Model Objects

You can mock SOQL query responses for Data Cloud data model objects (DMOs) in Apex testing by using the new SOQL stub methods
and a new test class. Use static or dynamic SOQL queries against DMOs and return mock records in a testing context.

##### Mock SOQL Tests for Data Cloud Data Model Objects

You can mock SOQL query responses for Data Cloud data model objects (DMOs) in Apex testing by using the new SOQL stub methods
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

_Apex Reference Guide:_ [SoqlStubProvider Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_SoqlStubProvider.htm)

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

_Apex Reference Guide_ [: DataWeave Namespace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_dataweave.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_dataweaveresource.htm)_ : DataWeaveResource

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/packaging_packageable_components.htm#mdc_dataweaveresource)_ : DataWeaveResource

##### Implementing DataWeave in Apex

Create DataWeave scripts as metadata and invoke them directly from Apex. Use class methods and exceptions in the DataWeave
namespace to load and execute the scripts.

DataWeave Namespace

The DataWeave namespace provides classes and methods to support the invocation of DataWeave scripts from Apex. The `Script`
class contains the `createScript()` method to load DataWeave scripts from `.dwl` metadata files that have been deployed to an
org. The resulting script can then be run with a payload using the `execute()` method to obtain script output in a
`DataWeave.Result` object. The `Result` class contains methods to retrieve script output using `Script` class methods. For
[more information on these classes and methods, see DataWeave Namespace.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_DataWeave.htm)

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

[Limitations of DataWeave in Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/DataWeaveInApex_limitations.htm)

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

#### Experience Cloud Sites

```

Experience Cloud sites are branded spaces for your employees, customers, and partners to connect. You can customize and create sites
to meet your business needs, then transition seamlessly between them.

Interact with Experience Cloud sites in Apex using the `Network` class and using Connect in Apex classes in the `ConnectApi`
namespace.

Connect in Apex has a `ConnectApi.Communities` class with methods that return information about sites. Many Connect in
Apex methods take a _`communityId`_ argument, and some Connect in Apex methods take a _`siteId`_ argument

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_network.htm)_ : Network Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_connect_api.htm)_ : Connect in Apex

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

You can use Apex to send individual and mass email. The email can include all standard email attributes (such as subject line and blind
carbon copy address), use Salesforce email templates, and be in plain text or HTML format, or those generated by Visualforce.

Note: Visualforce email templates cannot be used for mass email.

You can use Salesforce to track the status of email in HTML format, including the date the email was sent, first opened and last opened,
and the total number of times it was opened.


Apex Developer Guide Using Salesforce Features with Apex

To send individual and mass email with Apex, use the following classes:

**[SingleEmailMessage](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_outbound_single.htm)**

Instantiates an email object used for sending a single email message. The syntax is:

```
     Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

```

**[MassEmailMessage](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_outbound_mass.htm)**

Instantiates an email object used for sending a mass email message. The syntax is:

```
     Messaging.MassEmailMessage mail = new Messaging.MassEmailMessage();

```

**[Messaging](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_email_outbound_messaging.htm)**

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

**•** Maximum of 10 `sendEmail` [methods per transaction. Use the Limits methods to verify the number of](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_limits.htm) `sendEmail` methods
in a transaction.

**•** Single email messages sent with the `sendEmail` method count against the sending organization's daily single email limit. When
this limit is reached, calls to the `sendEmail` method using `SingleEmailMessage` are rejected, and the user receives a
`SINGLE_EMAIL_LIMIT_EXCEEDED` error code. However, single emails sent through the application are allowed.

**•** Mass email messages sent with the `sendEmail` method count against the sending organization's daily mass email limit. When
this limit is reached, calls to the `sendEmail` method using `MassEmailMessage` are rejected, and the user receives a
`MASS_MAIL_LIMIT_EXCEEDED` error code.

**•** Any error returned in the SendEmailResult object indicates that no email was sent.

`Messaging.SingleEmailMessage` has a method called `setOrgWideEmailAddressId` . It accepts an object ID to an
`OrgWideEmailAddress` object. If `setOrgWideEmailAddressId` is passed a valid ID, the
`OrgWideEmailAddress.DisplayName` field is used in the email header, instead of the logged-in user's `Display Name` .
The sending email address in the header is also set to the field defined in `OrgWideEmailAddress.Address` .


Apex Developer Guide Using Salesforce Features with Apex

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

    here.</a>');

   // Send the email you have created.

   Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

```


Apex Developer Guide Using Salesforce Features with Apex

#### External Services External Services connect your Salesforce org to a service outside of Salesforce, such as an employee banking service. After you register

the external service, you can call it natively in your Apex code. Objects and operations defined in the external service's registered API
specification become Apex classes and methods in the `ExternalService` namespace. The registered service's schema types map
to Apex types, and are strongly typed, making the Apex compiler do the heavy lifting for you. For example, you can make a type safe
callout to an external service from Apex without needing to use the `Http` class or perform transforms on JSON strings.

SEE ALSO:

_Salesforce Help_ [: Invoke External Service Callouts Using Apex](https://help.salesforce.com/s/articleView?id=platform.external_services_apex_invoking.htm&type=5&language=en_US)

#### Flows

Flow Builder lets admins build applications, known as _flows_, that automate a business process by collecting data and doing something
in your Salesforce org or an external system.

For example, you can create a flow to script calls for a customer support center or to generate real-time quotes for a sales team. You can
embed a flow in a Visualforce page or Aura component and access it in an Apex controller.

[For more information about using Apex to start a flow, see Apex Reference Guide: Interview Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/flow_interview_class.htm#flow_interview_class)

##### Getting Flow Variables

You can retrieve flow variables for a specific flow in Apex.

Making Callouts to External Systems from Invocable Actions
When you define a method that runs as an invocable action in a screen flow and makes a callout to an external system, use the

`callout` modifier.

Customize Invocable Action Input Order in Flow Builder
Control the display order and grouping of input parameters for your Apex invocable actions in Flow Builder using the
InvocableActionExtension metadata file.

Passing Data to a Flow Using the Process.Plugin Interface

`Process.Plugin` is a built-in interface that lets you process data within your org and pass it to a specified flow. The interface
exposes Apex as a service, which accepts input values and returns output back to the flow.

##### Getting Flow Variables

You can retrieve flow variables for a specific flow in Apex.

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
       if (myFlow==null) { return 'Home';}

       else aBreadCrumb = (String) myFlow.getVariableValue('vaBreadCrumb');

       return(aBreadCrumb==null ? 'Home': aBreadCrumb);

     }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/flow_interview_class.htm)_ : Interview Class

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

##### Customize Invocable Action Input Order in Flow Builder

Control the display order and grouping of input parameters for your Apex invocable actions in Flow Builder using the
InvocableActionExtension metadata file.

Example: Sorting Booking Request Inputs

An Apex class for a travel application, `BookingAction`, uses a custom input type, `BookingRequest`, to manage two required
dates: `startDate` and `endDate` . By default, the flow displays inputs alphabetically. Use the InvocableActionExtension metadata
file to define the logical order and group the fields under a relevant section header to improve the user experience.

Create the Apex Invocable Action

This section shows the Apex class structure required for the invocable action that exposes configurable input parameters to a flow.


Apex Developer Guide Using Salesforce Features with Apex

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


Apex Developer Guide Using Salesforce Features with Apex

`BookingRequest` use the `@InvocableVariable` annotation, which allows them to be exposed as configurable fields in Flow
Builder.

Define Input Order with Invocable Action Extension

Use the InvocableActionExtension metadata file to specify the sort order of the input fields and organize them into collapsible groups
for improved usability in Flow Builder.

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


Apex Developer Guide Using Salesforce Features with Apex

The `<targets>` elements identify the specific input parameters to be customized. The `<key>Order</key>` attribute explicitly
controls the vertical display sequence of the input parameters in Flow Builder. The `<key>Group</key>` attribute is used to create
the collapsible Booking Dates section, improving the organization and scannability of the action's inputs.

SEE ALSO:

InvocableMethod Annotation

InvocableVariable Annotation

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_invocableactionextension.htm)_ : InvocableActionExtension

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

When you define an Apex class that implements the `Process.Plugin` interface in your org, it's available in Flow Builder as a legacy
Apex action.

`Process.Plugin` has these top-level classes.

**•** `[Process.PluginRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginRequest.htm)` passes input parameters from the class that implements the interface to the flow.

**•** `[Process.PluginResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginResult.htm)` returns output parameters from the class that implements the interface to the flow.

**•** `[Process.PluginDescribeResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult.htm)` passes input parameters from a flow to the class that implements the interface. This
class determines the input parameters and output parameters needed by the `Process.PluginResult` plug-in.

When you write Apex unit tests, instantiate a class and pass it into the interface `invoke` method. To pass in the parameters that the
system needs, create a map and use it in the constructor. For more information, see Using the Process.PluginRequest Class on page 482.

Implementing the Process.Plugin Interface

`Process.Plugin` is a built-in interface that allows you to pass data between your organization and a specified flow.


Apex Developer Guide Using Salesforce Features with Apex

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

The class that implements the `Process.Plugin` interface must call these methods.

**Name** **Arguments** **Return Type** **Description**

```
describe Process.PluginDescribeResult

invoke Process.PluginRequest Process.PluginResult

```

Example Implementation

```
global class flowChat implements Process.Plugin {

```

Returns a

```
Process.PluginDescribeResult
```

object that describes this method call.

Primary method that the system invokes
when the class that implements the
interface is instantiated.

```
// The main method to be implemented. The Flow calls this at runtime.

global Process.PluginResult invoke(Process.PluginRequest request) {

     // Get the subject of the Chatter post from the flow

     String subject = (String) request.inputParameters.get('subject');

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

        plugin.invoke(request);

      }

   }

###### Using the Process.PluginRequest Class

```

The `Process.PluginRequest` class passes input parameters from the class that implements the interface to the flow.


Apex Developer Guide Using Salesforce Features with Apex

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

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

```


Apex Developer Guide Using Salesforce Features with Apex

###### Using the Process.PluginResult Class

The `Process.PluginResult` class returns output parameters from the class that implements the interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

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

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

The `Process.PluginDescribeResult` class doesn’t support the following functions.

**•** Queries

**•** Data modification

**•** Email

**•** Apex nested callouts


Apex Developer Guide Using Salesforce Features with Apex

**`Process.PluginDescribeResult`** Class and Subclass Properties

Here’s the constructor for the `Process.PluginDescribeResult` class.

```
   Process.PluginDescribeResult classname = new Process.PluginDescribeResult();

```

**•** [PluginDescribeResult Class Properties](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult.htm)

**•** [PluginDescribeResult.InputParameter Class Properties](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult_InputParameter.htm)

**•** [PluginDescribeResult.OutputParameter Class Properties](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Process_PluginDescribeResult_OutputParameter.htm)

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

###### Process.Plugin Data Type Conversions Understand how data types are converted between Apex and the values returned to the Process.Plugin . For example, text data
```

in a flow converts to string data in Apex.

###### Tip: We recommend using the @InvocableMethod annotation instead of the Process.Plugin interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

**Flow Data Type** **Data Type**

Number Decimal

Date Datetime/Date

DateTime Datetime/Date


Apex Developer Guide Using Salesforce Features with Apex

**Flow Data Type** **Data Type**

Boolean Boolean and numeric with 1 or 0 values only

Text String

###### Sample Process.Plugin Implementation for Lead Conversion

In this example, an Apex class implements the `Process.Plugin` interface and converts a lead into an account, contact, and
optionally, an opportunity. Test methods for the plug-in are also included. This implementation can be called from a flow via a legacy
Apex action.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

```
   // Converts a lead as an action in a flow.

   global class VWFConvertLead implements Process.Plugin {

      // This method runs when called by a flow's legacy Apex action.

      global Process.PluginResult invoke(

        Process.PluginRequest request) {

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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

```


Apex Developer Guide Using Salesforce Features with Apex

```
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

#### Formula Evaluation in Apex

```

Formula evaluation in Apex helps avoid unnecessary DML statements to recalculate formula field values and evaluate dynamic formula
expressions. Dynamic formulas in Apex support SObjects and Apex objects as context objects. The context type that corresponds to the
Apex class used in the `FormulaBuilder.withType()` method must be a global, user-defined Apex class. Any fields, properties,
or methods that the formula references must also be global.

Note: If formula fields on the input SObjects require a round-trip request to the database, use the
`[Formula.recalculateFormulas()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Formula.htm#apex_System_Formula_recalculateFormulas)` method.

Formulas in Apex support these features.

**•** Reference Apex types in formula fields. The values contained in individual components of such Apex types are accessed and evaluated
[by the formula. Address, Location, URL, and UUID System types are supported.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_system_Address.htm#topic-title)

**•** Reference standard lookups and custom lookups in formula fields.

**•** Access polymorphic relationship fields.

**•** Access the return value from the `toString()` method in formula fields.

[Formula evaluation in Apex is bound by the formula field character limit, but not the compile size limit. A formula can contain up to](https://help.salesforce.com/s/articleView?id=platform.formula_field_limits.htm&type=5&language=en_US)
3,900 characters including spaces, return characters, and comments.

[Formula functions that are available to use in Apex are ones that can be used in validation rules. For details, see Formula Operators and](https://help.salesforce.com/s/articleView?id=platform.customize_functions.htm&type=5&language=en_US)
[Functions by Context.](https://help.salesforce.com/s/articleView?id=platform.customize_functions.htm&type=5&language=en_US)

SEE ALSO:

_Apex Reference Guide:_ [FormulaEval Namespace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_formulaeval.htm)


Apex Developer Guide Using Salesforce Features with Apex

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

##### Retrieving and Deploying Metadata
#### Retrieve and deploy metadata by using the Metadata.Operations class.

Supported Metadata Types
Apex supports a subset of metadata types and components.

Security Considerations
Be aware of security considerations when using Apex to access metadata.

Testing Metadata Deployments
Apex code that accesses metadata must be properly tested.

SEE ALSO:

_Apex Reference Guide_ [: Metadata Namespace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_Metadata.htm)

##### Retrieving and Deploying Metadata

#### Retrieve and deploy metadata by using the Metadata.Operations class. Use the Metadata.Operations.retrieve() method to synchronously retrieve metadata from the current org. Provide a list

of metadata component names that you want to retrieve. Salesforce returns a list of matching component data, represented by component
#### classes that derive from Metadata.Metadata . Use the Metadata.Operations.enqueueDeployment() method to asynchronously deploy metadata to the current org.

Deployment is queued for asynchronous processing. When deploying metadata, you can create and update components but not delete
them. There are limitations on which components that apps and packages can deploy and which types of apps and packages can deploy
to which types of orgs. There are also service protection limitations on how many deployments that you can enqueue at one time from
Apex. For more information, see Security Considerations.

Use the full name of the metadata component when retrieving and deploying metadata. The full name can include the namespace,
metadata type, and component name. If you’re updating components in a namespace, you must qualify the namespace for the component
in the full name. For example, the full name for a custom metadata MDType1__mdt component named Component1 that is contained
in the myPackage namespace is myPackage__MDType1__mdt.myPackage__Component1. For more information on the metadata
#### component full name syntax, see Metadata base type in the Metadata API Developer Guide .


Apex Developer Guide Using Salesforce Features with Apex

You can retrieve and deploy metadata in post install scripts. In uninstall scripts, you can only retrieve, not deploy, metadata from Apex
code.

[See Metadata.Operations for code examples for retrieving and deploying metadata.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Metadata_Operations.htm)

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

[Salesforce verifies the notice during the security review. For more information, see the ISVforce Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_guidelines.htm)

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


Apex Developer Guide Using Salesforce Features with Apex

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

The `[calculatePermissionSetGroup()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_System_Test_class.htm)` method forces an immediate calculation of aggregate permissions for a specified
permission set group. As the forced calculation counts against Apex CPU limits, and can require complex data setup, it’s a best practice
to minimize the number of times you perform this operation. Recalculating complex permission set groups with a large number of
included permission sets or overall enabled permissions can cause Apex test failures because Apex CPU limits are exceeded. Apex CPU
limits can also be exceeded if the included permission sets in the permission set group aren’t licensed and the permission set group is
assigned to many users.

Set this test to run once in a Test setup method, then reuse the data in subsequent tests.

```
   @isTest public class PSGTest {

     @isTest static void testPSG() {

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

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm)_ : Test Class


Apex Developer Guide Using Salesforce Features with Apex

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

#### Platform Cache Best Practices Platform Cache can greatly improve performance in your applications. However, it’s important to follow these guidelines to get the

best cache performance. In general, it’s more efficient to cache a few large items than to cache many small items separately. Also
be mindful of cache limits to prevent unexpected cache evictions.


Apex Developer Guide Using Salesforce Features with Apex

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


Apex Developer Guide Using Salesforce Features with Apex

Note: Platform Cache isn’t supported in Professional Edition.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Session.htm)_ : Session Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Org.htm)_ : Org Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Partition.htm)_ : Partition Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_OrgPartition.htm)_ : OrgPartition Class

_Apex Reference Guide_ [: SessionPartition Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_SessionPartition.htm)

_Apex Reference Guide_ [: CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

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
[Alternatively, use the CacheBuilder Interface, which checks for cache misses.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

**•** All platform cache statistical methods: `getAvgGetSize()`, `getAvgGetTime()`, `getMaxGetSize()`,
`getMaxGetTime()`, and `getMissRate()` report data starting from the time the cache server was restarted, and do not
include data prior to the restart.

**•** Partitions must adhere to the limits within Salesforce.

**•** The session cache can store values up to eight hours. The org cache can store values up to 48 hours.

**•** For orgs that use Salesforce Flow:

**–** When a process contains a scheduled action, make sure that later actions in the process don't invoke Apex code that stores or
retrieves values from the session cache. The session-cache restriction applies to Apex actions and to changes that the process
makes to the database that cause Apex triggers to fire.

**–** When a flow contains a Pause element, make sure that later elements in the flow don't invoke Apex code that stores or retrieves
values from the session cache. The session-cache restriction applies to Apex actions and to changes that the flow makes to the
database that cause Apex triggers to fire.

##### Platform Cache Limits

These limits apply when using Platform Cache.


Apex Developer Guide Using Salesforce Features with Apex

Platform Cache Limits

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

Maximum session cache time-to-live 28,800 seconds (8 hours)

Org Cache Limits

**Limit** **Value**

Maximum size of a single cached item (for `put()` methods) 100 KB

Maximum local cache size for a partition, per-request [1] 1,000 KB

Minimum developer-assigned time-to-live 300 seconds (5 minutes)

Maximum developer-assigned time-to-live 172,800 seconds (48 hours)


Apex Developer Guide Using Salesforce Features with Apex

**Limit** **Value**

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
data that any users in an org can access. You can distribute your org’s cache space across any number of partitions. Session and org
cache allocations can be zero, or five or greater, and they must be whole numbers. The sum of all partition allocations, including the
default partition, equals the Platform Cache total allocation. The total allocated capacity of all cache segments must be less than or equal
to the org’s overall capacity.

You can define any partition as the default partition, but you can have only one default partition. When a partition has no allocation,
cache operations (such as get and put) are not invoked, and no error is returned.

When performing cache operations within the default partition, you can omit the partition name from the key.

After you set up partitions, you can use Apex code to perform cache operations on a partition. For example, use the
`Cache.SessionPartition` and `Cache.OrgPartition` classes to put, retrieve, or remove values on a specific partition’s
cache. Use `Cache.Session` and `Cache.Org` to get a partition or perform cache operations by using a fully qualified key.

Packaging Platform Cache Partitions

When packaging an application that uses Platform Cache, add any referenced partitions to your packages explicitly. Partitions aren’t
pulled into packages automatically, as other dependencies are. Partition validation occurs during run time, rather than compile time.
Therefore, if a partition is missing from a package, you don’t receive an error message at compile time.


Apex Developer Guide Using Salesforce Features with Apex

Note: If platform cache code is intended for a package, don’t use the default partition in the package. Instead, explicitly reference
and package a non-default partition. Any package containing the default partition can’t be deployed.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Partition.htm)_ : Partition Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_OrgPartition.htm)_ : OrgPartition Class

_Apex Reference Guide_ [: SessionPartition Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_SessionPartition.htm)

[Metadata API Developer’s Guide: Platform Cache Partition Type](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_platformcachepartition.htm)

##### Platform Cache Internals

Platform Cache uses local cache and a least recently used (LRU) algorithm to improve performance.

Local Cache

Platform Cache uses local cache to improve performance, ensure efficient use of the network, and support atomic transactions. Local
cache is the application server’s in-memory container that the client interacts with during a request. Cache operations don’t interact
with the caching layer directly, but instead interact with local cache.

For session cache, all cached items are loaded into local cache upon first request. All subsequent interactions use the local cache. Similarly,
an org cache get operation retrieves a value from the caching layer and stores it in the local cache. Subsequent requests for this value
are retrieved from the local cache. All mutable operations, such as put and remove, are also performed against the local cache. Upon
successful completion of the request, mutable operations are committed.

Note: Local cache doesn’t support concurrent operations. Mutable operations, such as put and remove, are performed against
the local cache and are only committed when the entire Apex request is successful. Therefore, other simultaneous requests don’t
see the results of the mutable operations.

Atomic Transactions

Each cache operation depends on the Apex request that it runs in. If the entire request fails, all cache operations in that request are rolled
back. Behind the scenes, the use of local cache supports these atomic transactions.

Eviction Algorithm

When possible, Platform Cache uses an LRU algorithm to evict keys from the cache. When cache limits are reached, keys are evicted
until the cache is reduced to 100-percent capacity. If session cache is used, the system removes cache evenly from all existing session
cache instances. Local cache also uses an LRU algorithm. When the maximum local cache size for a partition is reached, the least recently
used items are evicted from the local cache.

SEE ALSO:

Platform Cache Limits

##### Store and Retrieve Values from the Session Cache

Use the `Cache.Session` and `Cache.SessionPartition` classes to manage values in the session cache. To manage values
in any partition, use the methods in the `Cache.Session` class. If you’re managing cache values in one partition, use the
`Cache.SessionPartition` methods instead.


Apex Developer Guide Using Salesforce Features with Apex

**`Cache.Session`** Methods

To store a value in the session cache, call the `Cache.Session.put()` method and supply a key and value. The key name is in the
format `namespace.partition.key` . For example, for namespace **ns1**, partition **partition1**, and key **orderDate**, the fully qualified
key name is `ns1.partition1.orderDate` .

This example stores a `DateTime` cache value with the key `orderDate` . Next, the snippet checks if the `orderDate` key is in the
cache, and if so, retrieves the value from the cache.

```
   // Add a value to the cache

   DateTime dt = DateTime.parse('06/16/2015 11:46 AM');

   Cache.Session.put('ns1.partition1.orderDate', dt);

   if (Cache.Session.contains('ns1.partition1.orderDate')) {

      DateTime cachedDt = (DateTime)Cache.Session.get('ns1.partition1.orderDate');

   }

```

To refer to the default partition and the namespace of the invoking class, omit the `namespace.partition` prefix and specify the
key name.

```
   Cache.Session.put('orderDate', dt);

   if (Cache.Session.contains('orderDate')) {

      DateTime cachedDt = (DateTime)Cache.Session.get('orderDate');

   }

```

The `local` prefix refers to the namespace of the current org where the code is running, regardless of whether the org has a namespace
defined. If the org has a namespace defined as ns1, the following two statements are equivalent.

```
   Cache.Session.put('local.myPartition.orderDate', dt);

   Cache.Session.put('ns1.myPartition.orderDate', dt);

```

Note: The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls are not allowed in a partition that the invoking class doesn’t own.

The `put()` method has multiple versions (or overloads), and each version takes different parameters. For example, to specify that your
cached value can’t be overwritten by another namespace, set the last parameter of this method to `true` . The following example also
sets the lifetime of the cached value (3600 seconds or 1 hour) and makes the value available to any namespace.

```
   // Add a value to the cache with options

   Cache.Session.put('ns1.partition1.totalSum', '500', 3600, Cache.Visibility.ALL, true);

```

To retrieve a cached value from the session cache, call the `Cache.Session.get()` method. Because `Cache.Session.get()`
returns an object, we recommend that you cast the returned value to a specific type.

```
   // Get a cached value

   Object obj = Cache.Session.get('ns1.partition1.orderDate');

   // Cast return value to a specific data type

   DateTime dt2 = (DateTime)obj;

```

**`Cache.SessionPartition`** Methods

If you’re managing cache values in one partition, use the `Cache.SessionPartition` methods instead. After the partition object
is obtained, the process of adding and retrieving cache values is similar to using the `Cache.Session` methods. The
`Cache.SessionPartition` methods are easier to use because you specify only the key name without the namespace and
partition prefix.

First, get the session partition and specify the desired partition. The partition name includes the namespace prefix:
`namespace.partition` . You can manage the cached values in that partition by adding and retrieving cache values on the obtained


Apex Developer Guide Using Salesforce Features with Apex

partition object. The following example obtains the partition named myPartition in the myNs namespace. Next, if the cache contains a
value with the key `BookTitle`, this cache value is retrieved. A new value is added with key `orderDate` and today’s date.

```
   // Get partition

   Cache.SessionPartition sessionPart = Cache.Session.getPartition('myNs.myPartition');

   // Retrieve cache value from the partition

   if (sessionPart.contains('BookTitle')) {

      String cachedTitle = (String)sessionPart.get('BookTitle');

   }

   // Add cache value to the partition

   sessionPart.put('OrderDate', Date.today());

```

This example calls the `get` method on a partition in one expression without assigning the partition instance to a variable.

```
   // Or use dot notation to call partition methods

   String cachedAuthor =

   (String)Cache.Session.getPartition('myNs.myPartition').get('BookAuthor');

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Session.htm)_ : Session Class

_Apex Reference Guide_ [: SessionPartition Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_SessionPartition.htm)

##### Store and Retrieve Values from the Org Cache

Use the `Cache.Org` and `Cache.OrgPartition` classes to manage values in the org cache. To manage values in any partition,
use the methods in the `Cache.Org` class. If you’re managing cache values in one partition, use the `Cache.OrgPartition`
methods instead.

**`Cache.Org`** Methods

To store a value in the org cache, call the `Cache.Org.put()` method and supply a key and value. The key name is in the format
`namespace.partition.key` . For example, for namespace **ns1**, partition **partition1**, and key **orderDate**, the fully qualified key
name is `ns1.partition1.orderDate` .

This example stores a `DateTime` cache value with the key `orderDate` . Next, the snippet checks if the `orderDate` key is in the
cache, and if so, retrieves the value from the cache.

```
   // Add a value to the cache

   DateTime dt = DateTime.parse('06/16/2015 11:46 AM');

   Cache.Org.put('ns1.partition1.orderDate', dt);

   if (Cache.Org.contains('ns1.partition1.orderDate')) {

      DateTime cachedDt = (DateTime)Cache.Org.get('ns1.partition1.orderDate');

   }

```

To refer to the default partition and the namespace of the invoking class, omit the `namespace.partition` prefix and specify the
key name.

```
   Cache.Org.put('orderDate', dt);

   if (Cache.Org.contains('orderDate')) {

      DateTime cachedDt = (DateTime)Cache.Org.get('orderDate');

   }

```


Apex Developer Guide Using Salesforce Features with Apex

The `local` prefix refers to the namespace of the current org where the code is running. The `local` prefix refers to the namespace
of the current org where the code is running, regardless of whether the org has a namespace defined. If the org has a namespace defined
as ns1, the following two statements are equivalent.

```
   Cache.Org.put('local.myPartition.orderDate', dt);

   Cache.Org.put('ns1.myPartition.orderDate', dt);

```

Note: The `local` prefix in an installed managed package refers to the namespace of the subscriber org and not the package’s
namespace. The cache `put` calls are not allowed in a partition that the invoking class doesn’t own.

The `put()` method has multiple versions (or overloads), and each version takes different parameters. For example, to specify that your
cached value can’t be overwritten by another namespace, set the last parameter of this method to `true` . The following example also
sets the lifetime of the cached value (3600 seconds or 1 hour) and makes the value available to any namespace.

```
   // Add a value to the cache with options

   Cache.Org.put('ns1.partition1.totalSum', '500', 3600, Cache.Visibility.ALL, true);

```

To retrieve a cached value from the org cache, call the `Cache.Org.get()` method. Because `Cache.Org.get()` returns an
object, we recommend that you cast the returned value to a specific type.

```
   // Get a cached value

   Object obj = Cache.Org.get('ns1.partition1.orderDate');

   // Cast return value to a specific data type

   DateTime dt2 = (DateTime)obj;

```

**`Cache.OrgPartition`** Methods

If you’re managing cache values in one partition, use the `Cache.OrgPartition` methods instead. After the partition object is
obtained, the process of adding and retrieving cache values is similar to using the `Cache.Org` methods. The `Cache.OrgPartition`
methods are easier to use because you specify only the key name without the namespace and partition prefix.

First, get the org partition and specify the desired partition. The partition name includes the namespace prefix:
`namespace.partition` . You can manage the cached values in that partition by adding and retrieving cache values on the obtained
partition object. The following example obtains the partition named myPartition in the myNs namespace. If the cache contains a value
with the key `BookTitle`, this cache value is retrieved. A new value is added with key `orderDate` and today’s date.

```
   // Get partition

   Cache.OrgPartition orgPart = Cache.Org.getPartition('myNs.myPartition');

   // Retrieve cache value from the partition

   if (orgPart.contains('BookTitle')) {

      String cachedTitle = (String)orgPart.get('BookTitle');

   }

   // Add cache value to the partition

   orgPart.put('OrderDate', Date.today());

```

This example calls the `get` method on a partition in one expression without assigning the partition instance to a variable.

```
   // Or use dot notation to call partition methods

   String cachedAuthor = (String)Cache.Org.getPartition('myNs.myPartition').get('BookAuthor');

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_Org.htm)_ : Org Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_cache_OrgPartition.htm)_ : OrgPartition Class


Apex Developer Guide Using Salesforce Features with Apex

##### Use a Visualforce Global Variable for the Platform Cache

You can access cached values stored in the session or org cache from a Visualforce page with global variables.

You can use either the `$Cache.Session` or `$Cache.Org` global variable. Include the global variable’s fully qualified key name
with the namespace and partition name.

This output text component retrieves a session cache value using the global variable’s namespace, partition, and key.

```
   <apex:outputText value="{!$Cache.Session.myNamespace.myPartition.key1}"/>

```

This example is similar but uses the `$Cache.Org` global variable to retrieve a value from the org cache.

```
   <apex:outputText value="{!$Cache.Org.myNamespace.myPartition.key1}"/>

```

Note: The remaining examples show how to access the session cache using the `$Cache.Session` global variable. The
equivalent org cache examples are the same except that you use the `$Cache.Org` global variable instead.

Unlike with Apex methods, you can’t omit the `myNamespace.myPartition` prefix to reference the default partition in the org.

If a namespace isn’t defined for the org, use `local` to refer to the org’s namespace.

```
   <apex:outputText value="{!$Cache.Session.local.myPartition.key1}"/>

```

The cached value is sometimes a data structure that has properties or methods, like an Apex list or a custom class. In this case, you can
access the properties in the `$Cache.Session` or `$Cache.Org` expression by using dot notation. For example, this markup
invokes the `List.size()` Apex method if the value of `numbersList` is declared as a `List` .

```
   <apex:outputText value="{!$Cache.Session.local.myPartition.numbersList.size}"/>

```

This example accesses the value property on the myData cache value that is declared as a custom class.

```
   <apex:outputText value="{!$Cache.Session.local.myPartition.myData.value}"/>

```

If you’re using `CacheBuilder`, qualify the key name with the class that implements the `CacheBuilder` interface and the literal
string _`_B_`_, in addition to the namespace and partition name. In this example, the class that implements `CacheBuilder` is called
`CacheBuilderImpl` .

```
   <apex:outputText value="{!$Cache.Session.myNamespace.myPartition.CacheBuilderImpl_B_key1}"/>

##### Safely Cache Values with the CacheBuilder Interface

```

A Platform Cache best practice is to ensure that your Apex code handles cache misses by testing for cache requests that return null. You
can write this code yourself. Or, you can use the `Cache.CacheBuilder` interface, which makes it easy to safely store and retrieve
values to a session or org cache.

Rather than just declaring what you want to cache in your Apex class, create an inner class that implements the `CacheBuilder`
interface. The interface has a single method, `doLoad(String var)`, which you override by coding the logic that builds the cached
value based on the `doLoad(String var)` method’s argument.

To retrieve a value that you’ve cached with `CacheBuilder`, you don’t call the `doLoad(String var)` method directly. Instead,
it’s called indirectly by Salesforce the first time you reference the class that implements `CacheBuilder` . Subsequent calls get the
value from the cache, as long as the value exists. If the value doesn’t exist, the `doLoad(String var)` method is called again to
build the value and then return it. As a result, you don’t execute `put()` methods when using the `CacheBuilder` interface. And
because the `doLoad(String var)` method checks for cache misses, you don’t have to write the code to check for nulls yourself.

Let’s look at an example. Suppose you’re coding an Apex controller class for a Visualforce page. In the Apex class, you often run a SOQL
query that looks up a User record based on a user ID. SOQL queries can be expensive, and Salesforce user records don’t typically change
much, so the User information is a good candidate for `CacheBuilder` .


Apex Developer Guide Using Salesforce Features with Apex

In your controller class, create an inner class that implements the `CacheBuilder` interface and overrides the `doLoad(String`

`var)` method. Then add the SOQL code to the `doLoad(String var)` method with the user ID as its parameter.

```
   class UserInfoCache implements Cache.CacheBuilder {

      public Object doLoad(String userid) {

        User u = (User)[SELECT Id, IsActive, username FROM User WHERE id =: userid];

        return u;

      }

   }

```

To retrieve the User record from the org cache, execute the `Org.get(cacheBuilder, key)` method, passing it the
`UserInfoCache` class and the user ID. Similarly, use `Session.get(cacheBuilder, key)` and
`Partition.get(cacheBuilder, key)` to retrieve the value from the session or partition cache, respectively.

```
   User batman = (User) Cache.Org.get(UserInfoCache.class, ‘00541000000ek4c');

```

When you run the `get()` method, Salesforce searches the cache using a unique key that consists of the strings 00541000000ek4c and
UserInfoCache. If Salesforce finds a cached value, it returns it. For this example, the cached value is a User record associated with the ID
00541000000ek4c. If Salesforce doesn’t find a value, it executes the `doLoad(String var)` method of `UserInfoCache` again
(and reruns the SOQL query), caches the User record, and then returns it.

CacheBuilder Coding Requirements

Follow these requirements when you code a class that implements the `CacheBuilder` interface.

**•** The `doLoad(String var)` method must take a `String` parameter, even if you do not use the parameter in the method’s
code. Salesforce uses the string, along with the class name, to build a unique key for the cached value.

**•** The `doLoad(String var)` method can return any value, including null. If a null value is returned, it is delivered directly to the
CacheBuilder consumer and **not** cached. CacheBuilder consumers are expected to handle null values gracefully. We recommend
using null values to reflect a temporary failure to re-build the cache key.

**•** The class that implements `CacheBuilder` must be non-static because Salesforce instantiates a new instance of the class and
runs the `doLoad(String var)` method to create the cached value.

SEE ALSO:

_Apex Reference Guide_ [: CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

##### Platform Cache Best Practices

Platform Cache can greatly improve performance in your applications. However, it’s important to follow these guidelines to get the best
cache performance. In general, it’s more efficient to cache a few large items than to cache many small items separately. Also be mindful
of cache limits to prevent unexpected cache evictions.

Evaluate the Performance Impact

To test whether Platform Cache improves performance in your application, calculate the elapsed time with and without using the cache.
Don’t rely on the Apex debug log timestamp for the execution time. Use the `System.currentTimeMillis()` method instead.
For example, first call `System.currentTimeMillis()` to get the start time. Perform application logic, fetching the data from
either the cache or another data source. Then calculate the elapsed time.

```
   long startTime = System.currentTimeMillis();

   // Your code here

```


Apex Developer Guide Using Salesforce Features with Apex

```
   long elapsedTime = System.currentTimeMillis() - startTime;

   System.debug(elapsedTime);

```

Handle Cache Misses Gracefully

Ensure that your code handles cache misses by testing cache requests that return null. To help with debugging, add logging information
for cache operations.

Alternatively, use the `Cache.CacheBuilder` interface, which checks for cache misses.

```
   public class CacheManager {

      private Boolean cacheEnabled;

      public void CacheManager() {

        cacheEnabled = true;

      }

      public Boolean toggleEnabled() { // Use for testing misses

        cacheEnabled = !cacheEnabled;

        return cacheEnabled;

      }

      public Object get(String key) {

        if (!cacheEnabled) return null;

        Object value = Cache.Session.get(key);

        if (value != null) System.debug(LoggingLevel.DEBUG, 'Hit for key ' + key);

        return value;

      }

      public void put(String key, Object value, Integer ttl) {

        if (!cacheEnabled) return;

        Cache.Session.put(key, value, ttl);

        // for redundancy, save to DB

        System.debug(LoggingLevel.DEBUG, 'put() for key ' + key);

      }

      public Boolean remove(String key) {

        if (!cacheEnabled) return false;

        Boolean removed = Cache.Session.remove(key);

        if (removed) {

           System.debug(LoggingLevel.DEBUG, 'Removed key ' + key);

           return true;

        } else return false;

      }

   }

```

Group Cache Requests

When possible, group cache requests, but be aware of caching limits. To help improve performance, perform cache operations on a list
of keys rather than on individual keys. For example, if you know which keys are necessary to invoke a Visualforce page or perform a task
in Apex, retrieve all keys at once. To retrieve multiple keys, call `get(keys)` in an initialization method.


Apex Developer Guide Using Salesforce Features with Apex

Cache Larger Items

It’s more efficient to cache a few large items than to cache many small items separately. Caching many small items decreases performance
and increases overhead, including total serialization size, serialization time, cache commit time, and cache capacity usage.

Don’t add many small items to the Platform Cache within one request. Instead, wrap data in larger items, such as lists. If a list is large,
consider breaking it into multiple items. Here’s an example of what to avoid.

```
   // Don't do this!

   public class MyController {

      public void initCache() {

        List<Account> accts = [SELECT Id, Name, Phone, Industry, Description FROM

           Account limit 1000];

        for (Integer i=0; i<accts.size(); i++) {

           Cache.Org.put('acct' + i, accts.get(i));

        }

      }

   }

```

Instead, wrap the data in a few reasonably large items without exceeding the limit on the size of single cached items.

```
   // Do this instead.

   public class MyController {

   public void initCache() {

      List<Account> accts = [SELECT Id, Name, Phone, Industry, Description FROM

        Account limit 1000];

      Cache.Org.put('accts', accts);

      }

   }

```

Another good example of caching larger items is to encapsulate data in an Apex class. For example, you can create a class that wraps
session data, and cache an instance of the class rather than the individual data items. Caching the class instance improves overall
serialization size and performance.

Be Aware of Cache Limits

When you add items to the cache, be aware of the following limits.

**Cache Partition Size Limit**
When the cache partition limit is reached, keys are evicted until the cache is reduced to 100% capacity. Platform Cache uses a least
recently used (LRU) algorithm to evict keys from the cache.

**Local Cache Size Limit**

When you add items to the cache, make sure that you are not exceeding local cache limits within a request. The local cache limit
for the session cache is 500 KB and 1,000 KB for the org cache. If you exceed the local cache limit, items can be evicted from the local
cache before the request has been committed. This eviction can cause unexpected misses and long serialization time and can waste
resources.

**Single Cached Item Size Limit**
The size of individual cached items is limited to 100 KB. If the serialized size of an item exceeds this limit, the
`Cache.ItemSizeLimitExceededException` exception is thrown. It’s a good practice to catch this exception and reduce
the size of the cached item.


Apex Developer Guide Using Salesforce Features with Apex

Use the Cache Diagnostics Page (Sparingly)

To determine how much of the cache is used, check the Platform Cache Diagnostics page. To reach the Diagnostics page:

**1.** Make sure that Cache Diagnostics is enabled for the user (on the User Detail page).

**2.** On the Platform Cache Partition page, click the partition name.

**3.** Click the link to the Diagnostics page for the partition.

The Diagnostics page provides valuable information, including the capacity usage, keys, and serialized and compressed sizes of the
cached items. The session cache and org cache have separate diagnostics pages. The session cache diagnostics are per session, and they
don’t provide insight across all active sessions.

Note: Generating the diagnostics page gathers all partition-related information and is an expensive operation. Use it sparingly.

Minimize Expensive Operations

Consider the following guidelines to minimize expensive operations.

**•** Use `Cache.Org.getKeys()` and `Cache.Org.getCapacity()` sparingly. Both methods are expensive, because they
traverse all partition-related information looking for or making calculations for a given partition.

Note: `Cache.Session` usage is not expensive.

**•** Avoid calling the `contains(key)` method followed by the `get(key)` method. If you intend to use the key value, simply call
the `get(key)` method and make sure that the value is not equal to null.

**•** Clear the cache only when necessary. Clearing the cache traverses all partition-related cache space, which is expensive. After clearing
the cache, your application will likely regenerate the cache by invoking database queries and computations. This regeneration can
be complex and extensive and impact your application’s performance.

SEE ALSO:

Platform Cache Limits

_Apex Reference Guide_ [: CacheBuilder Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_cache_CacheBuilder.htm)

#### Salesforce Knowledge Salesforce Knowledge is a knowledge base where users can easily create and manage content, known as articles, and quickly find and

view the articles they need.

Use Apex to access these Salesforce Knowledge features:

Knowledge Management
Users can write, publish, archive, and manage articles using Apex in addition to the Salesforce user interface.

Promoted Search Terms
Promoted search terms are useful for promoting a Salesforce Knowledge article that you know is commonly used to resolve a support
issue when an end user’s search contains certain keywords. Users can promote an article in search results by associating keywords
with the article in Apex (by using the SearchPromotionRule sObject) in addition to the Salesforce user interface.

Suggest Salesforce Knowledge Articles
Provide users with shortcuts to navigate to relevant articles before they perform a search. Call `Search.suggest(searchText,`
`objectType, options)` to return a list of Salesforce Knowledge articles whose titles match a user’s search query string.


Apex Developer Guide Using Salesforce Features with Apex

##### Knowledge Management

Users can write, publish, archive, and manage articles using Apex in addition to the Salesforce user interface.

Use the methods in the `KbManagement.PublishingService` class to manage the following parts of the lifecycle of an article
and its translations:

**•** Publishing

**•** Updating

**•** Retrieving

**•** Deleting

**•** Submitting for translation

**•** Setting a translation to complete or incomplete status

**•** Archiving

**•** Assigning review tasks for draft articles or translations

Note: Date values are based on GMT.

[To use the methods in this class, you must enable Salesforce Knowledge. See Salesforce Knowledge Implementation Guide for more](https://resources.docs.salesforce.com/260/latest/en-us/sfdc/pdf/salesforce_knowledge_implementation_guide.pdf)
information on setting up Salesforce Knowledge.

SEE ALSO:

_Apex Reference Guide_ [: PublishingService Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_knowledge_kbManagement.htm)

##### Promoted Search Terms

Promoted search terms are useful for promoting a Salesforce Knowledge article that you know is commonly used to resolve a support
issue when an end user’s search contains certain keywords. Users can promote an article in search results by associating keywords with
the article in Apex (by using the SearchPromotionRule sObject) in addition to the Salesforce user interface.

Articles must be in published status (with a `PublishSatus` field value of `Online` ) for you to manage their promoted terms.

Example: This code sample shows how to add a search promotion rule. This sample performs a query to get published articles
of type MyArticle__kav. Next, the sample creates a SearchPromotionRule sObject to promote articles that contain the word
“Salesforce” and assigns the first returned article to it. Finally, the sample inserts this new sObject.

```
      // Identify the article to promote in search results

      List<MyArticle__kav> articles = [SELECT Id FROM MyArticle__kav WHERE

      PublishStatus='Online' AND Language='en_US' AND Id=' Article Id '];

      // Define the promotion rule

      SearchPromotionRule s = new SearchPromotionRule(

        Query='Salesforce',

        PromotedEntity=articles[0]);

      // Save the new rule

      insert s;

```

To perform DML operations on the SearchPromotionRule sObject, you must enable Salesforce Knowledge.


Apex Developer Guide Using Salesforce Features with Apex

##### Suggest Salesforce Knowledge Articles

Provide users with shortcuts to navigate to relevant articles before they perform a search. Call `Search.suggest(searchText,`
`objectType, options)` to return a list of Salesforce Knowledge articles whose titles match a user’s search query string.

[To return suggestions, enable Salesforce Knowledge. See Salesforce Knowledge Implementation Guide for more information on setting](https://resources.docs.salesforce.com/260/latest/en-us/sfdc/pdf/salesforce_knowledge_implementation_guide.pdf)
up Salesforce Knowledge.

This Visualforce page has an input field for searching articles or accounts. When the user presses the Suggest button, suggested records
are displayed. If there are more than five results, the More results button appears. To display more results, click the button.

```
   <apex:page controller="SuggestionDemoController">

      <apex:form >

        <apex:pageBlock mode="edit" id="block">

           <h1>Article and Record Suggestions</h1>

           <apex:pageBlockSection >

             <apex:pageBlockSectionItem >

               <apex:outputPanel >

                  <apex:panelGroup >

                    <apex:selectList value="{!objectType}" size="1">

                      <apex:selectOption itemLabel="Account" itemValue="Account"

    />

                       <apex:selectOption itemLabel="Article"

   itemValue="KnowledgeArticleVersion" />

                       <apex:actionSupport event="onchange" rerender="block"/>

                    </apex:selectList>

                  </apex:panelGroup>

                  <apex:panelGroup >

                    <apex:inputHidden id="nbResult" value="{!nbResult}" />

                  <apex:outputLabel for="searchText">Search Text</apex:outputLabel>

                    &nbsp;

                    <apex:inputText id="searchText" value="{!searchText}"/>

                    <apex:commandButton id="suggestButton" value="Suggest"

   action="{!doSuggest}"

                                rerender="block"/>

                    <apex:commandButton id="suggestMoreButton" value="More

   results..." action="{!doSuggestMore}"

                              rerender="block" style="{!IF(hasMoreResults,

    '', 'display: none;')}"/>

                  </apex:panelGroup>

               </apex:outputPanel>

             </apex:pageBlockSectionItem>

           </apex:pageBlockSection>

           <apex:pageBlockSection title="Results" id="results" columns="1"

   rendered="{!results.size>0}">

             <apex:dataList value="{!results}" var="w" type="1">

               Id: {!w.SObject['Id']}

               <br />

               <apex:panelGroup rendered="{!objectType=='KnowledgeArticleVersion'}">

                  Title: {!w.SObject['Title']}

               </apex:panelGroup>

               <apex:panelGroup rendered="{!objectType!='KnowledgeArticleVersion'}">

                  Name: {!w.SObject['Name']}

```


Apex Developer Guide Using Salesforce Features with Apex

```
               </apex:panelGroup>

               <hr />

             </apex:dataList>

           </apex:pageBlockSection>

           <apex:pageBlockSection id="noresults" rendered="{!results.size==0}">

             No results

           </apex:pageBlockSection>

           <apex:pageBlockSection rendered="{!LEN(searchText)>0}">

             Search text: {!searchText}

           </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

This code is the custom Visualforce controller for the page:

```
   public class SuggestionDemoController {

      public String searchText;

      public String language = 'en_US';

      public String objectType = 'Account';

      public Integer nbResult = 5;

      public Transient Search.SuggestionResults suggestionResults;

      public String getSearchText() {

        return searchText;

      }

      public void setSearchText(String s) {

        searchText = s;

      }

      public Integer getNbResult() {

        return nbResult;

      }

      public void setNbResult(Integer n) {

        nbResult = n;

      }

      public String getLanguage() {

        return language;

      }

      public void setLanguage(String language) {

        this.language = language;

      }

      public String getObjectType() {

        return objectType;

      }

      public void setObjectType(String objectType) {

        this.objectType = objectType;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      public List<Search.SuggestionResult> getResults() {

        if (suggestionResults == null) {

           return new List<Search.SuggestionResult>();

        }

        return suggestionResults.getSuggestionResults();

      }

      public Boolean getHasMoreResults() {

        if (suggestionResults == null) {

           return false;

        }

        return suggestionResults.hasMoreResults();

      }

      public PageReference doSuggest() {

        nbResult = 5;

        suggestAccounts();

        return null;

      }

      public PageReference doSuggestMore() {

        nbResult += 5;

        suggestAccounts();

        return null;

      }

      private void suggestAccounts() {

        Search.SuggestionOption options = new Search.SuggestionOption();

        Search.KnowledgeSuggestionFilter filters = new Search.KnowledgeSuggestionFilter();

        if (objectType=='KnowledgeArticleVersion') {

           filters.setLanguage(language);

           filters.setPublishStatus('Online');

        }

        options.setFilter(filters);

        options.setLimit(nbResult);

        suggestionResults = Search.suggest(searchText, objectType, options);

      }

   }

```

SEE ALSO:

[Search.suggest(searchQuery,sObjectType,suggestions)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_search.htm)

#### Salesforce Files

Use Apex to customize the behavior of Salesforce Files.


Apex Developer Guide Using Salesforce Features with Apex

##### Customize File Downloads

You can customize the behavior of files when users attempt to download them using an Apex callback. ContentVersion supports
modified file behavior, such as antivirus scanning and information rights management (IRM), after the download operation. File
download customization is available in API version 39.0 and later.

##### Custom File Download Examples

You can use Apex to customize the behavior of files upon attempted download. These examples assume that only one file is being
downloaded. File download customization is available in API version 39.0 and later.

##### Customize File Downloads

You can customize the behavior of files when users attempt to download them using an Apex callback. ContentVersion supports modified
file behavior, such as antivirus scanning and information rights management (IRM), after the download operation. File download
customization is available in API version 39.0 and later.

Customization code runs before download and determines whether the download can proceed.

The `Sfc` namespace contains Apex objects for customizing the behavior of Salesforce Files before they are downloaded.
`ContentDownloadHandlerFactory` provides an interface for customizing file downloads. The `ContentDownloadHandler`
class defines values related to whether download is allowed, and what to do otherwise. The `ContentDownloadContext` enum
is the context in which the download takes place.

You can use Apex to customize multiple-file downloads from the Content tab in Salesforce Classic. The Apex function parameter List<ID>
handles a list of ContentVersion IDs.

Customization also works on content packs and content deliveries. List<ID> is a list of the version IDs in a ContentPack. Setting
`isDownloadAllowed = false` on a multi-file or ContentPack download causes the entire download to fail. You can pass a list
of the problem files back to an error page via URL parameters in `redirectUrl` .

Example:

**•** Prevent a file from downloading based on the user profile, device being used, or file type and size.

**•** Apply IRM control to track information, such as the number of times a file has been downloaded.

**•** Flag suspicious files before download, and redirect them for antivirus scanning.

Flow Execution

When a download is triggered either from the UI, Connect API, or an sObject call retrieving `ContentVersion.VersionData`,
implementations of the `Sfc.ContentDownloadHandlerFactory` are looked up. If no implementation is found, download
proceeds. Otherwise, the user is redirected to what has been defined in the `ContentDownloadHandler#redirectUrl`
property. If several implementations are found, they are cascade handled (ordered by name) and the first one for which the download
isn’t allowed is considered.

Note: If a SOAP API operation triggers a download, it goes through the Apex class that checks whether the download is allowed.
If a download isn’t allowed, a redirection can’t be handled, and an exception containing an error message is returned instead.

##### Custom File Download Examples

You can use Apex to customize the behavior of files upon attempted download. These examples assume that only one file is being
downloaded. File download customization is available in API version 39.0 and later.


Apex Developer Guide Using Salesforce Features with Apex

Example: This example demonstrates a system that requires downloads to go through IRM control for some users. For a Modify
All Data (MAD) user who’s allowed to download files, and whose user ID is `005xx` :

```
      // Allow customization of the content Download experience

      public class ContentDownloadHandlerFactoryImpl implements

      Sfc.ContentDownloadHandlerFactory {

      public Sfc.ContentDownloadHandler getContentDownloadHandler(List<ID> ids,

      Sfc.ContentDownloadContext context) {

        Sfc.ContentDownloadHandler contentDownloadHandler = new Sfc.ContentDownloadHandler();

        if(UserInfo.getUserId() == '005xx') {

           contentDownloadHandler.isDownloadAllowed = true;

           return contentDownloadHandler;

        }

        contentDownloadHandler.isDownloadAllowed = false;

        contentDownloadHandler.downloadErrorMessage = 'This file needs to be IRM controlled.

      You're not allowed to download it';

        contentDownloadHandler.redirectUrl ='/apex/IRMControl?Id='+ids.get(0);

        return contentDownloadHandler;

      }

      }

```

Note: To refer to a MAD user profile, you can use `UserInfo.getProfileId()` instead of
`UserInfo.getUserId()` .

In this example, `IRMControl` is a Visualforce page created for displaying a link to download a file from the IRM system. You
need a controller for this page that calls your IRM system. As it’s processing the file, it gives an endpoint to download the file when
it’s controlled. Your IRM system uses the sObject API to get the `VersionData` of this `ContentVersion` . Therefore, the IRM
system needs the VersionID and must retrieve the VersionData using the MAD user.

Your IRM system is at `http://irmsystem` and is expecting the VersionID as a query parameter. The IRM system returns a
JSON response with the download endpoint in a `downloadEndpoint` value.

```
      public class IRMController {

      private String downloadEndpoint;

      public IRMController() {

        downloadEndpoint = '';

      }

      public void applyIrmControl() {

        String versionId = ApexPages.currentPage().getParameters().get('id');

        Http h = new Http();

        //Instantiate a new HTTP request, specify the method (GET) as well as the endpoint

        HttpRequest req = new HttpRequest();

        req.setEndpoint('http://irmsystem?versionId=' + versionId);

        req.setMethod('GET');

        // Send the request, and retrieve a response

```


Apex Developer Guide Using Salesforce Features with Apex

```
        HttpResponse r = h.send(req);

        JSONParser parser = JSON.createParser(r.getBody());

         while (parser.nextToken() != null) {

           if ((parser.getCurrentToken() == JSONToken.FIELD_NAME) &&

             (parser.getText() == 'downloadEndpoint')) {

               parser.nextToken();

               downloadEndpoint = parser.getText();

               break;

           }

        }

      }

      public String getDownloadEndpoint() {

        return downloadEndpoint;

      }

      }

```

Example: The following example creates a class that implements the `ContentDownloadHandlerFactory` interface
and returns a download handler that prevents downloading a file to a mobile device.

```
      // Allow customization of the content Download experience

      public class ContentDownloadHandlerFactoryImpl implements

      Sfc.ContentDownloadHandlerFactory {

      public Sfc.ContentDownloadHandler getContentDownloadHandler(List<ID> ids,

      Sfc.ContentDownloadContext context) {

        Sfc.ContentDownloadHandler contentDownloadHandler = new Sfc.ContentDownloadHandler();

        if(context == Sfc.ContentDownloadContext.MOBILE) {

           contentDownloadHandler.isDownloadAllowed = false;

          contentDownloadHandler.downloadErrorMessage = 'Downloading a file from a mobile

      device isn't allowed.';

           return contentDownloadHandler;

        }

        contentDownloadHandler.isDownloadAllowed = true;

        return contentDownloadHandler;

      }

```

Example: You can also prevent downloading a file from a mobile device and require that a file must go through IRM control.

```
      // Allow customization of the content Download experience

      public class ContentDownloadHandlerFactoryImpl implements

      Sfc.ContentDownloadHandlerFactory {

      public Sfc.ContentDownloadHandler getContentDownloadHandler(List<ID> ids,

      Sfc.ContentDownloadContext context) {

        Sfc.ContentDownloadHandler contentDownloadHandler = new Sfc.ContentDownloadHandler();

        if(UserInfo.getUserId() == '005xx000001SvogAAC') {

           contentDownloadHandler.isDownloadAllowed = true;

           return contentDownloadHandler;

```


Apex Developer Guide Using Salesforce Features with Apex

```
        }

        if(context == Sfc.ContentDownloadContext.MOBILE) {

           contentDownloadHandler.isDownloadAllowed = false;

          contentDownloadHandler.downloadErrorMessage = 'Downloading a file from a mobile

      device isn't allowed.';

           return contentDownloadHandler;

        }

        contentDownloadHandler.isDownloadAllowed = false;

        contentDownloadHandler.downloadErrorMessage = 'This file needs to be IRM controlled.

      You're not allowed to download it';

        contentDownloadHandler.redirectUrl ='/apex/IRMControl?Id='+id.get(0);

        return contentDownloadHandler;

      }

      }

#### Salesforce Connect

```

Apex code can access external object data via any Salesforce Connect adapter. Use the Apex Connector Framework to develop a custom
adapter for Salesforce Connect. The custom adapter can retrieve data from external systems and synthesize data locally. Salesforce
Connect represents that data in Salesforce external objects, enabling users and the Lightning Platform to seamlessly interact with data
that’s stored outside the Salesforce org.

Apex Considerations for Salesforce Connect External Objects
Apex code can access external object data via any Salesforce Connect adapter, but some requirements and limitations apply.

Writable External Objects
By default, external objects are read only, but you can make them writable. Doing so lets Salesforce users and APIs create, update,
and delete data that’s stored outside the org by interacting with external objects within the org. For example, users can see all the
orders that reside in an SAP system that are associated with an account in Salesforce. Then, without leaving the Salesforce user
interface, they can place a new order or route an existing order. The relevant data is automatically created or updated in the SAP
system.

External Change Data Capture Packaging and Testing
You can distribute External Change Data Capture components in managed packages, including a framework for testing your Apex
triggers. Special behaviors and limitations apply to packaging and package installation.

Mock SOQL Tests for External Objects
You can mock SOQL query responses for external objects in Apex testing by using SOQL stub methods and a new test class. Use
basic and joined SOQL queries against external objects and return mock records in a testing context.

Get Started with the Apex Connector Framework
To get started with your first custom adapter for Salesforce Connect, create two Apex classes: one that extends the
`DataSource.Connection` class, and one that extends the `DataSource.Provider` class.

Key Concepts About the Apex Connector Framework
The `DataSource` namespace provides the classes for the Apex Connector Framework. Use the Apex Connector Framework to
develop a custom adapter for Salesforce Connect. Then connect your Salesforce org to any data anywhere via the Salesforce Connect
custom adapter.

Considerations for the Apex Connector Framework
Understand the limits and considerations for creating Salesforce Connect custom adapters with the Apex Connector Framework.


Apex Developer Guide Using Salesforce Features with Apex

Apex Connector Framework Examples
These examples illustrate how to use the Apex Connector Framework to create custom adapters for Salesforce Connect.

SEE ALSO:

_Salesforce Help_ [: Access External Data With Salesforce Connect](https://help.salesforce.com/s/articleView?id=platform.salesforce_connect.htm&type=5&language=en_US)

[Salesforce Connect Learning Map](https://salesforceconnect-learningmap.herokuapp.com/)

##### Apex Considerations for Salesforce Connect External Objects

Apex code can access external object data via any Salesforce Connect adapter, but some requirements and limitations apply.

**•** These features aren’t available for external objects.

**–** Apex-managed sharing

**–** Apex triggers (However, you can create triggers on external change data capture events from OData 4.0 connections.)

**•** When developers use Apex to manipulate external object records, asynchronous timing and an active background queue minimize
potential save conflicts. A specialized set of Apex methods and keywords handles potential timing issues with write execution. Apex
also lets you retrieve the results of delete and upsert operations. Use the BackgroundOperation object to monitor job progress for
write operations via the API or SOQL.

**•** `Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a
community member. To add external object records via Apex, use `Database.insertImmediate()` methods.

Important: When running an iterable batch Apex job against an external data source, the external records are stored in Salesforce
while the job is running. The data is removed from storage when the job completes, whether or not the job was successful. No
external data is stored during batch Apex jobs that use `Database.QueryLocator` .

**•** If you use batch Apex with `Database.QueryLocator` to access external objects via an OData adapter for Salesforce Connect:

**–** Enable Request Row Counts on the external data source, and each response from the external system must include the total
row count of the result set.

**–** We recommend enabling Server Driven Pagination on the external data source and having the external system determine page
sizes and batch boundaries for large result sets. Typically, server-driven paging can adjust batch boundaries to accommodate
changing datasets more effectively than client-driven paging.

When Server Driven Pagination is disabled on the external data source, the OData adapter controls the paging behavior
(client-driven). If external object records are added to the external system while a job runs, other records can be processed twice.
If external object records are deleted from the external system while a job runs, other records can be skipped.

**–** When Server Driven Pagination is enabled on the external data source, the batch size at runtime is the smaller of the following:

**•** Batch size specified in the `scope` parameter of `Database.executeBatch` . Default is 200 records.

**•** Page size returned by the external system. We recommend that you set up your external system to return page sizes of 200
or fewer records.

SEE ALSO:

Use Batch Apex

_Salesforce Help_ [: Client-driven and Server-driven Paging for Salesforce Connect—OData 2.0 and 4.0 Adapters](https://help.salesforce.com/articleView?id=odata_paging.htm&language=en_US)

_Salesforce Help_ [: Define an External Data Source for Salesforce Connect—OData 2.0 or 4.0 Adapter](https://help.salesforce.com/articleView?id=platform_connect_add_external_data_source.htm&language=en_US)


Apex Developer Guide Using Salesforce Features with Apex

##### Writable External Objects

By default, external objects are read only, but you can make them writable. Doing so lets Salesforce users and APIs create, update, and
delete data that’s stored outside the org by interacting with external objects within the org. For example, users can see all the orders
that reside in an SAP system that are associated with an account in Salesforce. Then, without leaving the Salesforce user interface, they
can place a new order or route an existing order. The relevant data is automatically created or updated in the SAP system.

Access to external data depends on the connections between Salesforce and the external systems that store the data. Network latency
and the availability of the external systems can introduce timing issues with Apex write or delete operations on external objects.

Because of the complexity of these connections, Apex can’t execute standard `insert()`, `update()`, or `create()` operations
on external objects. Instead, Apex provides a specialized set of database methods and keywords to work around potential issues with
write execution. DML insert, update, create, and delete operations on external objects are either asynchronous or executed when specific
criteria are met.

This example uses the `Database.insertAsync()` method to insert a new order into a database table asynchronously. It returns
a `SaveResult` object that contains a unique identifier for the insert job.

```
   public void createOrder () {

      SalesOrder__x order = new SalesOrder__x ();

      Database.SaveResult sr = Database.insertAsync (order);

      if (! sr.isSuccess ()) {

        String locator = Database.getAsyncLocator ( sr );

        completeOrderCreation(locator);

      }

   }

```

Note: Writes performed on external objects through the Salesforce user interface or the API are synchronous and work the same
way as for standard and custom objects.

You can perform the following DML operations on external objects, either asynchronously or based on criteria: insert records, update
records, upsert records, or delete records. Use classes in the `DataSource` namespace to get the unique identifiers for asynchronous
jobs, or to retrieve results lists for upsert, delete, or save operations.

When you initiate an Apex method on an external object, a job is scheduled and placed in the background jobs queue. The
BackgroundOperation object lets you view the job status for write operations via the API or SOQL. Monitor job progress and related
errors in the org, extract statistics, process batch jobs, or see how many errors occur in a specified time period.

[For usage information and examples, see Database Namespace and DataSource Namespace.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_Database.htm)

SEE ALSO:

_Salesforce Help_ [: Writable External Objects Considerations for Salesforce Connect—All Adapters](https://help.salesforce.com/HTViewHelpDoc?id=platform_connect_considerations_writable_external_objects.htm&language=en_US)

##### External Change Data Capture Packaging and Testing

You can distribute External Change Data Capture components in managed packages, including a framework for testing your Apex
triggers. Special behaviors and limitations apply to packaging and package installation.

**•** Include External Change Data Tracking components in a managed package by selecting your test from the Apex Class Component
Type list. The trigger, test, external data source, external object, and other related assets are brought into the package for distribution.

**•** Certificates aren’t packageable. If you package an external data source that specifies a certificate, make sure that the subscriber org
has a valid certificate with the same name.

To help you test your External Change Data Capture–triggered Apex classes, here is a unit test code example of a trigger reacting to a
simulated external change.


Apex Developer Guide Using Salesforce Features with Apex

**Example Trigger**

```
   trigger OnExternalProductChangeEventForAudit on Products__ChangeEvent (after insert) {

      if (Trigger.new.size() != 1) return;

      for (Products__ChangeEvent event: Trigger.new) {

         Product_Audit__c audit = new Product_Audit__c();

         audit.Name = 'ProductChangeOn' + event.ExternalId;

         audit.Change_Type__c = event.ChangeEventHeader.getChangeType();

         audit.Audit_Price__c = event.Price__c;

         audit.Product_Name__c = event.Name__c;

         insert(audit);

      }

   }

```

**Apex Test**

```
   @isTest

   public class testOnExternalProductChangeEventForAudit {

      static testMethod void testExternalProductChangeTrigger() {

           // Create Change Event

          Products__ChangeEvent event = new Products__ChangeEvent();

           // Set Change Event Header Fields

          EventBus.ChangeEventHeader header = new EventBus.ChangeEventHeader();

          header.changeType='CREATE';

          header.entityName='Products__x';

          header.changeOrigin='here';

          header.transactionKey = 'some';

          header.commitUser = 'me';

          event.changeEventHeader = header;

          event.put('ExternalId', 'ParentExternalId');

          event.put('Price__c', 5500);

          event.put('Name__c', 'Coat');

           // Publish the event to the EventBus

          EventBus.publish(event);

          Test.getEventBus().deliver();

           // Perform assertion that the trigger was run

          Product_Audit__c audit = [SELECT name, Audit_Price__c, Product_Name__c FROM

   Product_Audit__c WHERE name = : 'ProductChangeOn'+ event.ExternalId LIMIT 1];

          System.assertEquals('ProductChangeOn'+ event.ExternalId, audit.Name);

          System.assertEquals(5500, audit.Audit_Price__c);

          System.assertEquals('Coat', audit.Product_Name__c);

      }

   }

##### Mock SOQL Tests for External Objects

```

You can mock SOQL query responses for external objects in Apex testing by using SOQL stub methods and a new test class. Use basic
and joined SOQL queries against external objects and return mock records in a testing context.

Create mock test classes by extending the new `System.SoqlStubProvider` class and overriding the `handleSoqlQuery()`
class method. Create external object records using either `Test.createStubQueryRow()` or
`Test.createStubQueryRows()` . Register the mock provider in the test using `Test.createSoqlStub()` and execute
the test code.

Note: Apex governor limits apply to the stubbed records.


Apex Developer Guide Using Salesforce Features with Apex

The SOQL query must be against an external object, either directly with a FROM clause or via a subquery. These features aren’t allowed
within a stub implementation.

**•** SOQL

**•** SOSL

**•** Callouts

**•** Future methods

**•** Queueable Jobs

**•** Batch Jobs

**•** DML

**•** Platform events

This example shows a mock test class for the _`GithubIssueTest`_ class with joined and basic queries.

```
   /**

    * Test class that utilizes the SoqlStubProvider classes.

    * Each test sets the appropriate SoqlStubProvider

    * and runs validation against the mocked query results.

    **/

   @isTest

   public class GithubIssueTest {

      @isTest

      static void testGithubIssueQuery() {

        QueryIssueUtil queryIssueUtil = new QueryIssueUtil();

        SObjectType type = queryIssueUtil.getSObjectTypeForDynamicSoql('GithubIssues__x');

        Test.createSoqlStub(type, new IssueStubProvider());

        Test.startTest();

        Assert.isTrue(Test.isSoqlStubDefined(type));

        Assert.isTrue(queryIssueUtil.queryGithubIssuesAndCheckForId());

        Assert.areEqual(Limits.getQueries(), 1);

        Assert.areEqual(Limits.getQueryRows(), 1);

        Assert.areEqual(Limits.getAggregateQueries(), 0);

        Assert.isTrue(queryIssueUtil.queryGithubIssuesAndVerifyResultSize(1));

        Assert.areEqual(Limits.getQueries(), 2);

        Assert.areEqual(Limits.getQueryRows(), 2);

        Assert.areEqual(Limits.getAggregateQueries(), 0);

        Test.stopTest();

      }

      @isTest

      static void testIssueToCommentJoinQuery() {

        QueryIssueUtil queryIssueUtil = new QueryIssueUtil();

       Test.createSoqlStub(GithubIssues__x.SObjectType, new IssueCommentJoinStubProvider());

        Test.startTest();

        Assert.isTrue(Test.isSoqlStubDefined(GithubIssues__x.SObjectType));

        Assert.isTrue(queryIssueUtil.queryIssueToCommentJoinAndCheckForCommentId());

        Assert.areEqual(Limits.getQueries(), 1);

        Assert.areEqual(Limits.getQueryRows(), 3);

        Assert.areEqual(Limits.getAggregateQueries(), 1);

        Assert.isTrue(queryIssueUtil.queryIssueToCommentJoinAndVerifyResultSize(1, 2));

```


Apex Developer Guide Using Salesforce Features with Apex

```
        Assert.areEqual(Limits.getQueries(), 2);

        Assert.areEqual(Limits.getQueryRows(), 6);

        Assert.areEqual(Limits.getAggregateQueries(), 2);

        Test.stopTest();

      }

   }

   /**

    * SoqlStubProvider class that returns a mocked query result

    * for joined queries between the Github Issues object and

    * the associated Comments object.

    **/

   public class IssueCommentJoinStubProvider extends SoqlStubProvider {

     public override List<SObject> handleSoqlQuery(SObjectType sobjectType, String rawQuery,

    Map<String,Object> binds) {

        if (sobjectType.equals(GithubIssues__x.SObjectType)) {

           Assert.areEqual(binds.size(), 0);

           List<GithubIssues__x> issues = new List<GithubIssues__x>();

           List<Map<String,Object>> commentMaps = new List<Map<String,Object>>();

           Map<String, Object> comment1 = new Map<String, Object> {

             'Id' => 'x09xx000000brk9AAA'

           };

           Map<String, Object> comment2 = new Map<String, Object> {

             'Id' => 'x09xx000001brk9AAA'

           };

           commentMaps.add(comment1);

           commentMaps.add(comment2);

           List<IssueComments__x> comments = (List<IssueComments__x>)

   Test.createStubQueryRows(IssueComments__x.SObjectType, commentMaps);

           Map<String, Object> issueMap = new Map<String, Object> {

             'Id' => 'x08xx000002HNZ6AAO',

             'Title__c' => 'Sample Issue 1',

             'IssueComments__r' => comments

           };

          GithubIssues__x obj = (GithubIssues__x) Test.createStubQueryRow(sobjectType,

   issueMap);

           issues.add(obj);

           return issues;

        }

        return null;

      }

   }

   /**

    * SoqlStubProvider class that returns a mocked query result

    * for queries against the Github Issues object.

```


Apex Developer Guide Using Salesforce Features with Apex

```
    **/

   public class IssueStubProvider extends SoqlStubProvider {

     public override List<SObject> handleSoqlQuery(SObjectType sobjectType, String rawQuery,

    Map<String,Object> binds) {

        if (sobjectType.equals(GithubIssues__x.SObjectType)) {

        Assert.areEqual(binds.size(), 1);

        Assert.areEqual(binds.get('tmpVar1'), 'x08xx000002HNZ6AAO');

           List<SObject> objs = new List<SObject>();

           Map<String, Object> individualMap = new Map<String, Object> {

             'Id' => 'x08xx000002HNZ6AAO'

           };

          GithubIssues__x obj = (GithubIssues__x) Test.createStubQueryRow(sobjectType,

   individualMap);

           objs.add(obj);

           return objs;

        }

        return null;

      }

   }

   /**

    * Utility class that runs queries to be mocked

    * in the Apex tests.

    **/

   public class QueryIssueUtil {

      public boolean queryGithubIssuesAndCheckForId() {

        // BINDS WITH USER_MODE DYNAMIC QUERY

        Map<String, Object> binds = new Map<String, Object>{'tmpVar1' =>

   'x08xx000002HNZ6AAO'};

        List<GithubIssues__x> issues = Database.queryWithBinds('SELECT Id FROM

   GithubIssues__x WHERE Id = :tmpVar1', binds, AccessLevel.USER_MODE);

        for (GithubIssues__x issue : issues ) {

           if (issue.Id.equals('x08xx000002HNZ6AAO')) {

             return true;

           }

        }

        return false;

      }

      public boolean queryGithubIssuesAndVerifyResultSize(Integer size) {

        // BINDS WITH SYSTEM_MODE STATIC QUERY

        String issueId = 'x08xx000002HNZ6AAO';

       List<GithubIssues__x> issues = [SELECT Id FROM GithubIssues__x WHERE Id = :issueId];

        if(issues.size() == size) {

           return true;

        }

           return false;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      public boolean queryIssueToCommentJoinAndCheckForCommentId() {

        // DYNAMIC QUERY

        List<GithubIssues__x> issues = Database.query('SELECT Id, Title__c, (SELECT Id

   FROM IssueComments__r) FROM GithubIssues__x WHERE Id = \'003000000000000\'');

        for (GithubIssues__x issue : issues) {

           List<IssueComments__x> comments = issue.IssueComments__r;

           System.debug(comments);

           if(!comments.get(0).Id.equals('x09xx000000brk9AAA') &&

   !comments.get(1).Id.equals('x09xx000001brk9AAA'))return false;

        }

        return true;

      }

      public boolean queryIssueToCommentJoinAndVerifyResultSize(Integer parentSize, Integer

    childSize) {

        // STATIC QUERY

        List<GithubIssues__x> issues = [SELECT Id, Title__c, (SELECT Id FROM

   IssueComments__r) FROM GithubIssues__x WHERE Id = '003000000000000'];

       if(issues.size() == parentSize && issues.get(0).IssueComments__r.size() == childSize)

    {

           return true;

        }

        return false;

      }

      public SObjectType getSObjectTypeForDynamicSoql(String name) {

        Schema.DescribeSObjectResult[] descResult = Schema.describeSobjects(new

   List<String>{name});

        SObjectType type = descResult.get(0).getSobjectType();

        return type;

      }

   }

##### Get Started with the Apex Connector Framework

```

To get started with your first custom adapter for Salesforce Connect, create two Apex classes: one that extends the
`DataSource.Connection` class, and one that extends the `DataSource.Provider` class.

Note: The `DataSource.Connection` class requires a Salesforce Connect add-on license. For more information, see
[Salesforce Connect Adapters Included per Add-On License.](https://help.salesforce.com/s/articleView?id=sf.platform_connect_license.htm&language=en_US)

Let’s step through the code of a sample custom adapter.

1. Create a Sample DataSource.Connection Class Class
First, create a `DataSource.Connection` class to enable Salesforce to obtain the external system’s schema and to handle
queries and searches of the external data.

2. Create a Sample DataSource.Provider Class Class
Now you need a class that extends and overrides a few methods in `DataSource.Provider` .


Apex Developer Guide Using Salesforce Features with Apex

3. Set Up Salesforce Connect to Use Your Custom Adapter
After you create your `DataSource.Connection` and `DataSource.Provider` classes, the Salesforce Connect custom
adapter becomes available in Setup.

###### Create a Sample DataSource.Connection Class Class

First, create a `DataSource.Connection` class to enable Salesforce to obtain the external system’s schema and to handle queries
and searches of the external data.

```
   global class SampleDataSourceConnection

      extends DataSource.Connection {

      global SampleDataSourceConnection(DataSource.ConnectionParams

        connectionParams) {

      }

   // Add implementation of abstract methods

   // ...

```

The `DataSource.Connection` class contains these methods.

**•** query

**•** search

**•** sync

**•** upsertRows

**•** deleteRows

```
   sync

```

The `sync()` method is invoked when an administrator clicks the **Validate and Sync** button on the external data source detail page.
It returns information that describes the structural metadata on the external system.

Note: Changing the `sync` method on the `DataSource.Connection` class doesn’t automatically resync any external
objects.

```
   // ...

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

           new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('Name', 255));

        columns.add(DataSource.Column.text('ExternalId', 255));

        columns.add(DataSource.Column.url('DisplayUrl'));

        tables.add(DataSource.Table.get('Sample', 'Title',

           columns));

        return tables;

      }

   // ...

   query

```

The `query` method is invoked when a SOQL query is executed on an external object. A SOQL query is automatically generated and
executed when a user opens an external object’s list view or detail page in Salesforce. The `DataSource.QueryContext` is always
only for a single table.


Apex Developer Guide Using Salesforce Features with Apex

This sample custom adapter uses a helper method in the `DataSource.QueryUtils` class to filter and sort the results based on
the `WHERE` and `ORDER BY` clauses in the SOQL query.

The `DataSource.QueryUtils` class and its helper methods can process query results locally within your Salesforce org. This class
is provided for your convenience to simplify the development of your Salesforce Connect custom adapter for initial tests. However, the
`DataSource.QueryUtils` class and its methods aren’t supported for use in production environments that use callouts to retrieve
data from external systems. Complete the filtering and sorting on the external system before sending the query results to Salesforce.
When possible, use server-driven paging or another technique to have the external system determine the appropriate data subsets
according to the limit and offset clauses in the query.

```
   // ...

      override global DataSource.TableResult query(

        DataSource.QueryContext context) {

        if (context.tableSelection.columnsSelected.size() == 1 &&

           context.tableSelection.columnsSelected.get(0).aggregation ==

             DataSource.QueryAggregation.COUNT) {

             List<Map<String,Object>> rows = getRows(context);

             List<Map<String,Object>> response =

               DataSource.QueryUtils.filter(context, getRows(context));

             List<Map<String, Object>> countResponse =

               new List<Map<String, Object>>();

             Map<String, Object> countRow =

               new Map<String, Object>();

             countRow.put(

               context.tableSelection.columnsSelected.get(0).columnName,

               response.size());

             countResponse.add(countRow);

             return DataSource.TableResult.get(context,

               countResponse);

        } else {

           List<Map<String,Object>> filteredRows =

             DataSource.QueryUtils.filter(context, getRows(context));

           List<Map<String,Object>> sortedRows =

             DataSource.QueryUtils.sort(context, filteredRows);

           List<Map<String,Object>> limitedRows =

             DataSource.QueryUtils.applyLimitAndOffset(context,

               sortedRows);

           return DataSource.TableResult.get(context, limitedRows);

        }

      }

   // ...

   search

```

The `search` method is invoked by a SOSL query of an external object or when a user performs a Salesforce global search that also
searches external objects. Because search can be federated over multiple objects, the `DataSource.SearchContext` can have
multiple tables selected. In this example, however, the custom adapter knows about only one table.

```
   // ...

      override global List<DataSource.TableResult> search(

           DataSource.SearchContext context) {

        List<DataSource.TableResult> results =

           new List<DataSource.TableResult>();

        for (DataSource.TableSelection tableSelection :

```


Apex Developer Guide Using Salesforce Features with Apex

```
           context.tableSelections) {

           results.add(DataSource.TableResult.get(tableSelection,

             getRows(context)));

        }

        return results;

      }

   // ...

```

The following is the `getRows` helper method that the search sample calls to get row values from the external system. The `getRows`
method makes use of other helper methods:

**•** `makeGetCallout` makes a callout to the external system.

**•** `foundRow` populates a row based on values from the callout result. The `foundRow` method is used to make any modifications
to the returned field values, such as changing a field name or modifying a field value.

[These methods aren’t included in this snippet but are available in the full example included in Connection Class. Typically, the filter from](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Connection.htm)
`SearchContext` or `QueryContext` would be used to reduce the result set, but for simplicity this example doesn’t make use of
the context object.

```
   // ...

      // Helper method to get record values from the external system for the Sample table.

      private List<Map<String, Object>> getRows () {

       // Get row field values for the Sample table from the external system via a callout.

        HttpResponse response = makeGetCallout();

        // Parse the JSON response and populate the rows.

        Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

             response.getBody());

        Map<String, Object> error = (Map<String, Object>)m.get('error');

        if (error != null) {

           throwException(string.valueOf(error.get('message')));

        }

        List<Map<String,Object>> rows = new List<Map<String,Object>>();

        List<Object> jsonRows = (List<Object>)m.get('value');

        if (jsonRows == null) {

           rows.add(foundRow(m));

        } else {

           for (Object jsonRow : jsonRows) {

             Map<String,Object> row = (Map<String,Object>)jsonRow;

             rows.add(foundRow(row));

           }

        }

        return rows;

      }

   // ...

   upsertRows

```

The `upsertRows` method is invoked when external object records are created or updated. You can create or update external object
records through the Salesforce user interface or DML. The following example provides a sample implementation for the `upsertRows`
method. The example uses the passed-in `UpsertContext` to determine what table was selected and performs the upsert only if
the name of the selected table is `Sample` . The upsert operation is broken up into either an insert of a new record or an update of an
existing record. These operations are performed in the external system using callouts. An array of `DataSource.UpsertResult`


Apex Developer Guide Using Salesforce Features with Apex

is populated from the results obtained from the callout responses. Note that because a callout is made for each row, this example might
hit the Apex callouts limit.

```
   // ...

      global override List<DataSource.UpsertResult> upsertRows(DataSource.UpsertContext

           context) {

        if (context.tableSelected == 'Sample') {

          List<DataSource.UpsertResult> results = new List<DataSource.UpsertResult>();

          List<Map<String, Object>> rows = context.rows;

          for (Map<String, Object> row : rows){

            // Make a callout to insert or update records in the external system.

            HttpResponse response;

            // Determine whether to insert or update a record.

            if (row.get('ExternalId') == null){

              // Send a POST HTTP request to insert new external record.

              // Make an Apex callout and get HttpResponse.

              response = makePostCallout(

                '{"name":"' + row.get('Name') + '","ExternalId":"' +

                row.get('ExternalId') + '"');

            }

            else {

              // Send a PUT HTTP request to update an existing external record.

              // Make an Apex callout and get HttpResponse.

              response = makePutCallout(

                '{"name":"' + row.get('Name') + '","ExternalId":"' +

                row.get('ExternalId') + '"',

                String.valueOf(row.get('ExternalId')));

            }

            // Check the returned response.

            // Deserialize the response.

            Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

                 response.getBody());

            if (response.getStatusCode() == 200){

              results.add(DataSource.UpsertResult.success(

                   String.valueOf(m.get('id'))));

            }

            else {

              results.add(DataSource.UpsertResult.failure(

                  String.valueOf(m.get('id')),

                  'The callout resulted in an error: ' +

                  response.getStatusCode()));

            }

          }

          return results;

        }

        return null;

      }

   // ...

```


Apex Developer Guide Using Salesforce Features with Apex

```
   deleteRows

```

The `deleteRows` method is invoked when external object records are deleted. You can delete external object records through the
Salesforce user interface or DML. The following example provides a sample implementation for the `deleteRows` method. The example
uses the passed-in `DeleteContext` to determine what table was selected and performs the deletion only if the name of the selected
table is `Sample` . The deletion is performed in the external system using callouts for each external ID. An array of
`DataSource.DeleteResult` is populated from the results obtained from the callout responses. Note that because a callout is
made for each ID, this example might hit the Apex callouts limit.

```
   // ...

      global override List<DataSource.DeleteResult> deleteRows(DataSource.DeleteContext

           context) {

        if (context.tableSelected == 'Sample'){

          List<DataSource.DeleteResult> results = new List<DataSource.DeleteResult>();

          for (String externalId : context.externalIds){

            HttpResponse response = makeDeleteCallout(externalId);

            if (response.getStatusCode() == 200){

              results.add(DataSource.DeleteResult.success(externalId));

            }

            else {

              results.add(DataSource.DeleteResult.failure(externalId,

                  'Callout delete error:'

                  + response.getBody()));

            }

          }

          return results;

        }

        return null;

      }

   // ...

```

SEE ALSO:

Execution Governors and Limits

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Connection.htm)_ : Connection Class

Filters in the Apex Connector Framework

###### Create a Sample DataSource.Provider Class Class

Now you need a class that extends and overrides a few methods in `DataSource.Provider` .

Your `DataSource.Provider` class informs Salesforce of the authentication and functional capabilities that are supported by or
required to connect to the external system.

```
   global class SampleDataSourceProvider extends DataSource.Provider {

```

If the external system requires authentication, Salesforce can provide the authentication credentials from the external data source
definition or users’ personal settings. This example specifies that the external system doesn’t require authentication, but also supports
OAuth authentication. To do so, it returns `AuthenticationCapability.ANONYMOUS` and
`AuthenticationCapability.OAUTH` in the list of authentication capabilities.


Apex Developer Guide Using Salesforce Features with Apex

The `getAuthenticationCapabilities` method should always return the same list of authentication types regardless of user,
org, or context.

```
   global override List<DataSource.AuthenticationCapability>

        getAuthenticationCapabilities() {

        // Best Practice: Always return a static list of authentication types

        // Don't query the database, make callouts, or use dynamic logic

        List<DataSource.AuthenticationCapability> capabilities =

           new List<DataSource.AuthenticationCapability>();

        capabilities.add(DataSource.AuthenticationCapability.ANONYMOUS);

        capabilities.add(DataSource.AuthenticationCapability.OAUTH);

        return capabilities;

      }

```

This example also specifies that the external system allows SOQL queries, SOSL queries, Salesforce searches, upserting data, and deleting
data.

**•** To allow SOQL, the example declares the `DataSource.Capability.ROW_QUERY` capability.

**•** To allow SOSL and Salesforce searches, the example declares the `DataSource.Capability.SEARCH` capability.

**•** To allow upserting external data, the example declares the `DataSource.Capability.ROW_CREATE` and
`DataSource.Capability.ROW_UPDATE` capabilities.

**•** To allow deleting external data, the example declares the `DataSource.Capability.ROW_DELETE` capability.

The `getCapabilities` method should always return the same list of capabilities regardless of configuration or data.The returned
capabilities should never change based on runtime conditions, user context, dynamic queries, or any other conditions.

```
   global override List<DataSource.Capability> getCapabilities() {

        // Best Practice: Return a static list of functional capabilities

        // Don't query the database, make callouts, or use dynamic logic

        List<DataSource.Capability> capabilities = new

        List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        capabilities.add(DataSource.Capability.SEARCH);

        capabilities.add(DataSource.Capability.ROW_CREATE);

        capabilities.add(DataSource.Capability.ROW_UPDATE);

        capabilities.add(DataSource.Capability.ROW_DELETE);

        return capabilities;

      }

```

Warning: When you call the `getAuthenticationCapabilities` or `getCapabilities` methods, be sure the
returned list always contains the same values. Never use a SOQL query, callout, or any conditional logic that changes the returned
values based on runtime conditions. Returning varying lists of authentication capabilities or capabilities for an external system can
lead to errors that are difficult to troubleshoot.

Lastly, the example identifies the `SampleDataSourceConnection` class that obtains the external system’s schema and handles
the queries and searches of the external data.

```
   global override DataSource.Connection getConnection(

        DataSource.ConnectionParams connectionParams) {

        return new SampleDataSourceConnection(connectionParams);

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Provider.htm)_ : Provider Class

###### Set Up Salesforce Connect to Use Your Custom Adapter

After you create your `DataSource.Connection` and `DataSource.Provider` classes, the Salesforce Connect custom
adapter becomes available in Setup.

[Complete the tasks that are described in “Set Up Salesforce Connect to Access External Data with a Custom Adapter” in the Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=apex_adapter_setup.htm&language=en_US)
Help.

To add write capability for external objects to your adapter:

**1.** [Make the external data source for this adapter writable. See “Define an External Data Source for Salesforce Connect—Custom Adapter”](https://help.salesforce.com/articleView?id=apex_add_external_data_source.htm&language=en_US)
in the Salesforce Help.

**2.** Implement the `DataSource.Connection.upsertRows()` and `DataSource.Connection.deleteRows()`
[methods for the adapter. For details, see Connection Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Connection.htm)

##### Key Concepts About the Apex Connector Framework

The `DataSource` namespace provides the classes for the Apex Connector Framework. Use the Apex Connector Framework to develop
a custom adapter for Salesforce Connect. Then connect your Salesforce org to any data anywhere via the Salesforce Connect custom
adapter.

We recommend that you learn about some key concepts to help you use the Apex Connector Framework effectively.

External IDs for Salesforce Connect External Objects
When you access external data with a custom adapter for Salesforce Connect, the values of the External ID standard field on an
external object come from the `DataSource.Column` named `ExternalId` .

Authentication for Salesforce Connect Custom Adapters
Your `DataSource.Provider` class declares what types of credentials can be used to authenticate to the external system.

Callouts for Salesforce Connect Custom Adapters
Just like any other Apex code, a Salesforce Connect custom adapter can make callouts. If the connection to the external system
requires authentication, incorporate the authentication parameters into the callout.

Paging with the Apex Connector Framework
When displaying a large set of records in the user interface, Salesforce breaks the set into batches and displays one batch. You can
then page through those batches. However, custom adapters for Salesforce Connect don’t automatically support paging of any
kind. To support paging through external object data that’s obtained by a custom adapter, implement server-driven or client-driven
paging.

queryMore with the Apex Connector Framework with the Apex Connector Framework
Custom adapters for Salesforce Connect don’t automatically support the `queryMore` method in API queries. However, your
implementation must be able to break up large result sets into batches and iterate over them by using the `queryMore` method
in the SOAP API. The default batch size is 500 records, but the query developer can adjust that value programmatically in the query
call.


Apex Developer Guide Using Salesforce Features with Apex

Aggregation for Salesforce Connect Custom Adapters
If you receive a `COUNT()` query, the selected column has the value `QueryAggregation.COUNT` in its `aggregation`
property. The selected column is provided in the `columnsSelected` property on the `tableSelection` for the
`DataSource.QueryContext` .

Filters in the Apex Connector Framework
The `DataSource.QueryContext` contains one `DataSource.TableSelection` . The
`DataSource.SearchContext` can have more than one `TableSelection` . Each `TableSelection` has a `filter`
property that represents the `WHERE` clause in a SOQL or SOSL query.

###### External IDs for Salesforce Connect External Objects

When you access external data with a custom adapter for Salesforce Connect, the values of the External ID standard field on an external
object come from the `DataSource.Column` named `ExternalId` .

###### Each external object has an External ID standard field. Its values uniquely identify each external object record in your org. When

the external object is the parent in an external lookup relationship, the External ID standard field is used to identify the child records.

Important:

**•** The custom adapter’s Apex code must declare the `DataSource.Column` named `ExternalId` and provide its values.

**•** Don’t use sensitive data as the values of the External ID standard field or fields designated as name fields, because Salesforce
sometimes stores those values.

**–** External lookup relationship fields on child records store and display the External ID values of the parent records.

**–** For internal use only, Salesforce stores the External ID value of each row that’s retrieved from the external system. This
behavior doesn’t apply to external objects that are associated with high-data-volume external data sources.

Example: This excerpt from a sample `DataSource.Connection` class shows the `DataSource.Column` named
`ExternalId` .

```
        override global List<DataSource.Table> sync() {

           List<DataSource.Table> tables =

           new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('title', 255));

        columns.add(DataSource.Column.text('description',255));

        columns.add(DataSource.Column.text('createdDate',255));

        columns.add(DataSource.Column.text('modifiedDate',255));

        columns.add(DataSource.Column.url('selfLink'));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text(' ExternalId ',255));

        tables.add(DataSource.Table.get('googleDrive','title',

           columns));

        return tables;

        }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Column.htm)_ : Column Class


Apex Developer Guide Using Salesforce Features with Apex

###### Authentication for Salesforce Connect Custom Adapters

Your `DataSource.Provider` class declares what types of credentials can be used to authenticate to the external system.

If your extension of the `[DataSource.Provider](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Provider.htm)` class returns `[DataSource.AuthenticationCapability](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_enum_DataSource_AuthenticationCapability.htm)` values that
indicate support for authentication, the `[DataSource.Connection](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Connection.htm)` class is instantiated with a
`[DataSource.ConnectionParams](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_ConnectionParams.htm)` instance in the constructor.

The authentication credentials in the `DataSource.ConnectionParams` instance depend on the `Identity Type` field of
the external data source definition in Salesforce.

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

####### OAuth for Salesforce Connect Custom Adapters

If you use OAuth 2.0 to access external data, learn how to avoid access interruptions caused by expired access tokens.

SEE ALSO:

####### OAuth for Salesforce Connect Custom Adapters OAuth for Salesforce Connect Custom Adapters

If you use OAuth 2.0 to access external data, learn how to avoid access interruptions caused by expired access tokens.

Some external systems use OAuth access tokens that expire and need to be refreshed. We can automatically refresh access tokens as
needed when:

**•** The user or external data source has a valid refresh token from a previous OAuth flow.

**•** The sync, query, or search method in your `DataSource.Connection` class throws a
`DataSource.OAuthTokenExpiredException` .

We use the relevant OAuth credentials for the user or external data source to negotiate with the remote service and refresh the token.
The `DataSource.Connection` class is reconstructed with the new OAuth token in the `DataSource.ConnectionParams`
that we supply to the constructor. The search or query is then reinvoked.

If the authentication provider doesn’t provide a refresh token, access to the external system is lost when the current access token expires.
If a warning message appears on the external data source detail page, consult your OAuth provider for information about requesting
offline access or a refresh token.

For some authentication providers, requesting offline access is as simple as adding a scope. For example, to request offline access from
a Salesforce authentication provider, add _`refresh_token`_ to the `Default Scopes` field on the authentication provider definition
in your Salesforce organization.

For other authentication providers, you must request offline access in the authentication URL as a query parameter. For example, with
Google, append _`?access_type=offline`_ to the `Authorize Endpoint URL` field on the authentication provider definition


Apex Developer Guide Using Salesforce Features with Apex

in your Salesforce organization. To edit the authorization endpoint, select **Open ID Connect** in the `Provider Type` field of the
authentication provider. For details, see “Configure an OpenID Connect Authentication Provider” in the Salesforce Help.

SEE ALSO:

Authentication for Salesforce Connect Custom Adapters

###### Callouts for Salesforce Connect Custom Adapters

Just like any other Apex code, a Salesforce Connect custom adapter can make callouts. If the connection to the external system requires
authentication, incorporate the authentication parameters into the callout.

Authentication parameters are encapsulated in a `ConnectionParams` object and provided to your `DataSource.Connection`
class’s constructor.

For example, if your connection requires an OAuth access token, use code similar to the following.

```
   public HttpResponse getResponse(String url) {

      Http httpProtocol = new Http();

      HttpRequest request = new HttpRequest();

      request.setEndPoint(url);

      request.setMethod('GET');

      request.setHeader('Authorization', 'Bearer ' +

           this.connectionInfo.oauthToken);

      HttpResponse response = httpProtocol.send(request);

      return response;

   }

```

If your connection requires basic password authentication, use code similar to the following.

```
   public HttpResponse getResponse(String url) {

      Http httpProtocol = new Http();

      HttpRequest request = new HttpRequest();

      request.setEndPoint(url);

      request.setMethod('GET');

      string encodedHeaderValue = EncodingUtil.base64Encode(Blob.valueOf(

           this.connectioninfo.username + ':' +

           this.connectionInfo.password));

      request.setHeader('Authorization', 'Basic ' + encodedHeaderValue);

      HttpResponse response = httpProtocol.send(request);

      return response;

   }

```

Named Credentials as Callout Endpoints for Salesforce Connect Custom Adapters

A Salesforce Connect custom adapter obtains the relevant credentials that are stored in Salesforce whenever they’re needed. However,
your Apex code must apply those credentials to all callouts, except those that specify named credentials as the callout endpoints. A
named credential lets Salesforce handle the authentication logic for you so that your code doesn’t have to.


Apex Developer Guide Using Salesforce Features with Apex

If all your custom adapter’s callouts use named credentials, you can set the external data source’s `Authentication Protocol`
field to **No Authentication** . The named credentials add the appropriate certificates and can add standard authorization headers to the
callouts. You also don’t need to define a remote site for an Apex callout endpoint that’s defined as a named credential.

SEE ALSO:

Named Credentials as Callout Endpoints

###### Paging with the Apex Connector Framework

When displaying a large set of records in the user interface, Salesforce breaks the set into batches and displays one batch. You can then
page through those batches. However, custom adapters for Salesforce Connect don’t automatically support paging of any kind. To
support paging through external object data that’s obtained by a custom adapter, implement server-driven or client-driven paging.

With server-driven paging, the external system controls the paging and ignores any batch boundaries or page sizes that are specified
in queries. To enable server-driven paging, declare the `QUERY_PAGINATION_SERVER_DRIVEN` capability in your
`DataSource.Provider` class. Also, your Apex code must generate a query token and use it to determine and fetch the next batch
of results.

With client-driven paging, you use `LIMIT` and `OFFSET` clauses to page through result sets. Factor in the `offset` and `maxResults`
properties in the `DataSource.QueryContext` to determine which rows to return. For example, suppose that the result set has
20 rows with numeric `ExternalID` values from 1 to 20. If we ask for an `offset` of `5` and `maxResults` of `5`, we expect to get
the rows with IDs `6`     - `10` . We recommend that you do all filtering in the external system, outside of Apex, using methods that the external
system supports.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_QueryContext.htm)_ : QueryContext Class

###### queryMore with the Apex Connector Framework with the Apex Connector Framework Custom adapters for Salesforce Connect don’t automatically support the queryMore method in API queries. However, your implementation must be able to break up large result sets into batches and iterate over them by using the queryMore method in

the SOAP API. The default batch size is 500 records, but the query developer can adjust that value programmatically in the query call.

###### To support queryMore, your implementation must indicate whether more data exists than what’s in the current batch. When the

Lightning Platform knows that more data exists, your API queries return a `QueryResult` object that’s similar to the following.

```
   {

         "totalSize" => -1,

            "done" => false,

      "nextRecordsUrl" => "/services/data/v32.0/query/01gxx000000B5OgAAK-2000",

          "records" => [

        [ 0] {

           "attributes" => {

             "type" => "Sample__x",

              "url" =>

                "/services/data/v32.0/sobjects/Sample__x/x06xx0000000001AAA"

           },

           "ExternalId" => "id0"

        },

        [ 1] {

           "attributes" => {

             "type" => "Sample__x",

```


Apex Developer Guide Using Salesforce Features with Apex

```
              "url" =>

                "/services/data/v32.0/sobjects/Sample__x/x06xx0000000002AAA"

           },

   …

   }

####### Support queryMore by Using Server-Driven Paging by Using Server-Driven Paging
```

With server-driven paging, the external system controls the paging and ignores any batch boundaries or page sizes that are specified
in queries. To enable server-driven paging, declare the `QUERY_PAGINATION_SERVER_DRIVEN` capability in your
`DataSource.Provider` class.

####### Support queryMore by Using Client-Driven Paging

With client-driven paging, you use `LIMIT` and `OFFSET` clauses to page through result sets.

####### Support queryMore by Using Server-Driven Paging by Using Server-Driven Paging

With server-driven paging, the external system controls the paging and ignores any batch boundaries or page sizes that are specified
in queries. To enable server-driven paging, declare the `QUERY_PAGINATION_SERVER_DRIVEN` capability in your
`DataSource.Provider` class.

When the returned `DataSource.TableResult` doesn’t contain the entire result set, the `TableResult` must provide a
`queryMoreToken` value. The query token is an arbitrary string that we store temporarily. When we request the next batch of results,
we pass the query token back to your custom adapter in the `DataSource.QueryContext` . Your Apex code must use that query
token to determine which rows belong to the next batch of results.

When your custom adapter returns the final batch, it must not return a `queryMoreToken` value in the `TableResult` .

The Apex Connector Framework doesn't support server-driven pagination for list views.

SEE ALSO:

queryMore with the Apex Connector Framework with the Apex Connector Framework

####### Support queryMore by Using Client-Driven Paging

With client-driven paging, you use `LIMIT` and `OFFSET` clauses to page through result sets.

If the external system can return the total size of the result set for each query, declare the `QUERY_TOTAL_SIZE` capability in your
`DataSource.Provider` class. Make sure that each search or query returns the `totalSize` value in the
`DataSource.TableResult` . If the total size is larger than the number of rows that are returned in the batch, we generate a
`nextRecordsUrl` link and set the `done` flag to `false` . We also set the `totalSize` in the `TableResult` to the value that
you supply.

If the external system can’t return the total size for each query, don’t declare the `QUERY_TOTAL_SIZE` capability in your
`DataSource.Provider` class. Whenever we do a query through your custom adapter, we ask for one extra row. For example, if
you run the query `SELECT ExternalId FROM Sample LIMIT 5`, we call the `query` method on the
`DataSource.Connection` object with a `DataSource.QueryContext` that has the `maxResults` property set to 6.
The presence or absence of that sixth row in the result set indicates whether more data is available. We assume, however, that the data
set we query against doesn’t change between queries. If the data set changes between queries, you might see repeated rows or not
get all results.


Apex Developer Guide Using Salesforce Features with Apex

Ultimately, accessing external data works most efficiently when you retrieve small amounts of data and the data set that you query
against changes infrequently.

SEE ALSO:

queryMore with the Apex Connector Framework with the Apex Connector Framework

###### Aggregation for Salesforce Connect Custom Adapters

If you receive a `COUNT()` query, the selected column has the value `QueryAggregation.COUNT` in its `aggregation` property.
The selected column is provided in the `columnsSelected` property on the `tableSelection` for the
`DataSource.QueryContext` .

The following example illustrates how to apply the value of the `aggregation` property to handle `COUNT()` queries.

```
   // Handle COUNT() queries

   if (context.tableSelection.columnsSelected.size() == 1 &&

      context.tableSelection.columnsSelected.get(0).aggregation ==

        QueryAggregation.COUNT) {

      List<Map<String, Object>> countResponse = new List<Map<String, Object>>();

      Map<String, Object> countRow = new Map<String, Object>();

      countRow.put(context.tableSelection.columnsSelected.get(0).columnName,

      response.size());

      countResponse.add(countRow);

      return countResponse;

   }

```

An aggregate query can still have filters, so your query method can be implemented like the following example to support basic
`aggregation` queries, with or without filters.

```
   override global DataSource.TableResult query(DataSource.QueryContext context) {

      List<Map<String,Object>> rows = retrieveData(context);

      List<Map<String,Object>> response = postFilterRecords(

           context.tableSelection.filter, rows);

      if (context.tableSelection.columnsSelected.size() == 1 &&

        context.tableSelection.columnsSelected.get(0).aggregation ==

             DataSource.QueryAggregation.COUNT) {

        List<Map<String, Object>> countResponse = new List<Map<String,

             Object>>();

        Map<String, Object> countRow = new Map<String, Object>();

        countRow.put(context.tableSelection.columnsSelected.get(0).columnName,

             response.size());

        countResponse.add(countRow);

        return DataSource.TableResult.get(context, countResponse);

      }

      return DataSource.TableResult.get(context, response);

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_QueryContext.htm)_ : QueryContext Class

Create a Sample DataSource.Connection Class Class


Apex Developer Guide Using Salesforce Features with Apex

###### Filters in the Apex Connector Framework

The `DataSource.QueryContext` contains one `DataSource.TableSelection` . The `DataSource.SearchContext`
can have more than one `TableSelection` . Each `TableSelection` has a `filter` property that represents the `WHERE`
clause in a SOQL or SOSL query.

For example, when a user goes to an external object’s record detail page, your `DataSource.Connection` is executed. Behind
the scenes, we generate a SOQL query similar to the following.

```
   SELECT columnNames

   FROM externalObjectApiName

   WHERE ExternalId = ' selectedExternalObjectExternalId '

```

This SOQL query causes the `query` method on your `DataSource.Connection` class to be invoked. The following code can
detect this condition.

```
   if (context.tableSelection.filter != null) {

      if (context.tableSelection.filter.type == DataSource.FilterType.EQUALS

        && 'ExternalId' == context.tableSelection.filter.columnName

        && context.tableSelection.filter.columnValue instanceOf String) {

        String selection = (String)context.tableSelection.filter.columnValue;

        return DataSource.TableResult.get(true, null,

             tableSelection.tableSelected, findSingleResult(selection));

      }

   }

```

This code example assumes that you implemented a `findSingleResult` method that returns a single record, given the selected
`ExternalId` . Make sure that your code obtains the record that matches the requested `ExternalId` .

####### Evaluating Filters in the Apex Connector Framework

A filter evaluates to true for a row if that row matches the conditions that the filter describes.

Compound Filters in the Apex Connector Framework
Filters can have child filters, which are stored in the `subfilters` property.

####### Evaluating Filters in the Apex Connector Framework

A filter evaluates to true for a row if that row matches the conditions that the filter describes.

For example, suppose that a `DataSource.Filter` has `columnName` set to `meaningOfLife`, `columnValue` set to `42`,
and `type` set to `EQUALS` . Any row in the remote table whose `meaningOfLife` column entry equals 42 is returned.

Suppose, instead, that the filter has `type` set to `LESS_THAN`, `columnValue` set to `3`, and `columnName` set to `numericCol` .
We’d construct a `DataSource.TableResult` object that contains all the rows that have a `numericCol` value less than 3.

###### To improve performance, do all the filtering in the external system. You can, for example, translate the Filter object into a SQL or

OData query, or map it to parameters on a SOAP query. If the external system returns a large set of data, and you do the filtering in your
Apex code, you quickly exceed your governor limits.

If you can’t do all the filtering in the external system, do as much as possible there and return as little data as possible. Then filter the
smaller collection of data in your Apex code.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Filter.htm)_ : Filter Class


Apex Developer Guide Using Salesforce Features with Apex

####### Compound Filters in the Apex Connector Framework

Filters can have child filters, which are stored in the `subfilters` property.

If a filter has children, the filter `type` must be one of the following.

**Filter Type** **Description**

`AND_` We return all rows that match _all_ of the subfilters.

`OR_` We return all rows that match _any_ of the subfilters.

`NOT_` The filter reverses how its child filter evaluates rows. Filters of this type can have only one subfilter.

This code example illustrates how to deal with compound filters.

```
   override global DataSource.TableResult query(DataSource.QueryContext context) {

      // Call out to an external data source and retrieve a set of records.

      // We should attempt to get as much information as possible about the

      // query from the QueryContext, to minimize the number of records

      // that we return.

      List<Map<String,Object>> rows = retrieveData(context);

      // This only filters the results. Anything in the query that we don’t

      // currently support, such as aggregation or sorting, is ignored.

      return DataSource.TableResult.get(context, postFilterRecords(

        context.tableSelection.filter, rows));

   }

   private List<Map<String,Object>> retrieveData(DataSource.QueryContext context) {

      // Call out to an external data source. Form the callout so that

      // it filters as much as possible on the remote site,

      // based on the parameters in the QueryContext.

      return ...;

   }

   private List<Map<String,Object>> postFilterRecords(

      DataSource.Filter filter, List<Map<String,Object>> rows) {

      if (filter == null) {

        return rows;

      }

      DataSource.FilterType type = filter.type;

      List<Map<String,Object>> retainedRows = new List<Map<String,Object>>();

      if (type == DataSource.FilterType.NOT_) {

        // We expect one Filter in the subfilters.

        DataSource.Filter subfilter = filter.subfilters.get(0);

        for (Map<String,Object> row : rows) {

           if (!evaluate(filter, row)) {

             retainedRows.add(row);

           }

        }

        return retainedRows;

      } else if (type == DataSource.FilterType.AND_) {

        // For each filter, find all matches; anything that matches ALL filters

        // is returned.

```


Apex Developer Guide Using Salesforce Features with Apex

```
        retainedRows = rows;

        for (DataSource.Filter subfilter : filter.subfilters) {

           retainedRows = postFilterRecords(subfilter, retainedRows);

        }

        return retainedRows;

      } else if (type == DataSource.FilterType.OR_) {

        // For each filter, find all matches. Anything that matches

        // at least one filter is returned.

        for (DataSource.Filter subfilter : filter.subfilters) {

           List<Map<String,Object>> matchedRows = postFilterRecords(

             subfilter, rows);

           retainedRows.addAll(matchedRows);

        }

        return retainedRows;

      } else {

        // Find all matches for this filter in our collection of records.

        for (Map<String,Object> row : rows) {

           if (evaluate(filter, row)) {

             retainedRows.add(row);

           }

        }

        return retainedRows;

      }

   }

   private Boolean evaluate(DataSource.Filter filter, Map<String,Object> row) {

      if (filter.type == DataSource.FilterType.EQUALS) {

        String columnName = filter.columnName;

        Object expectedValue = filter.columnValue;

        Object foundValue = row.get(columnName);

        return expectedValue.equals(foundValue);

      } else {

        // Throw an exception; implementing other filter types is left

        // as an exercise for the reader.

        throwException('Unexpected filter type: ' + filter.type);

      }

      return false;

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_DataSource_Filter.htm)_ : Filter Class

##### Considerations for the Apex Connector Framework

Understand the limits and considerations for creating Salesforce Connect custom adapters with the Apex Connector Framework.

**•** If you change and save a `DataSource.Connection` class, resave the corresponding `DataSource.Provider` class.
Otherwise, when you define the external data source, the custom adapter doesn’t appear as an option for the `Type` field. Also, the
associated external objects’ custom tabs no longer appear in the Salesforce UI.

**•** DML operations aren’t allowed in the Apex code that comprises the custom adapter.

**•** Make sure that you understand the limits of the external system’s APIs. For example, some external systems accept only requests
for up to 40 rows.


Apex Developer Guide Using Salesforce Features with Apex

**•** Apex data type limitations:

**–** Double—The value loses precision beyond 18 significant digits. For higher precision, use decimals instead of doubles.

**–** String—If the length is greater than 255 characters, the string is mapped to a long text area field in Salesforce.

**•** Custom adapters for Salesforce Connect are subject to the same limitations as any other Apex code. For example:

**–** All Apex governor limits apply.

**–** Test methods don’t support web service callouts. Tests that perform web service callouts fail. For an example that shows how
to avoid these failing tests by returning mock responses, see Google Drive [™] Custom Adapter for Salesforce Connect on page
558.

**•** In Apex tests, use dynamic SOQL to query external objects. Tests that perform static SOQL queries of external objects fail.

SEE ALSO:

Dynamic SOQL

##### Apex Connector Framework Examples

These examples illustrate how to use the Apex Connector Framework to create custom adapters for Salesforce Connect.

###### GitHub Issues Custom Adapter for Salesforce Connect

This example creates a custom adapter that links GitHub Issues to products in Salesforce using an indirect lookup relationship. An
external lookup relationship also links GitHub Issues to the comments on each issue.

GitHub Custom Adapter for Salesforce Connect
This example illustrates how to support indirect lookup relationships. An indirect lookup relationship links a child external object to
a parent standard or custom object.

Google Drive [™] Custom Adapter for Salesforce Connect
This example illustrates how to use callouts and OAuth to connect to an external system, which in this case is the Google Drive [™]

online storage service. The example also shows how to avoid failing tests from web service callouts by returning mock responses
for test methods.

Google Books [™] Custom Adapter for Salesforce Connect
This example illustrates how to work around the requirements and limits of an external system’s APIs: in this case, the Google Books
API Family.

Loopback Custom Adapter for Salesforce Connect
This example illustrates how to handle filtering in queries. For simplicity, this example connects the Salesforce org to itself as the
external system.

Stack Overflow Custom Adapter for Salesforce Connect
This example illustrates how to support external lookup relationships and multiple tables. An external lookup relationship links a
child standard, custom, or external object to a parent external object. Each table can become an external object in the Salesforce
org.

###### GitHub Issues Custom Adapter for Salesforce Connect

This example creates a custom adapter that links GitHub Issues to products in Salesforce using an indirect lookup relationship. An external
lookup relationship also links GitHub Issues to the comments on each issue.

This example illustrates a range of common use cases for custom adapters, including how to:


Apex Developer Guide Using Salesforce Features with Apex

**•** Query external data.

**•** Work with a range of external object field types, such as Date and Picklist fields.

**•** Use indirect lookup relationships, which link a child external object to a parent standard or custom object.

**•** Use external lookup relationships, which link a child standard, custom, or external object to a parent external object.

**•** Use Data Manipulation Language (DML) operations to insert, update, and delete external data.

To improve unit tests for the Apex code in this example, you can also return mock records in a testing context. See Mock SOQL Tests for
External Objects on page 522.

DataSource.Connection Class

This example creates a class named `GitHubDataSourceConnection` . For this example to work, create a custom field on the
Product2 standard object. Specify the name of the custom text field as Repository, and select the External ID and Unique attributes.

```
   /**

    * Defines the connection to GitHub REST API v3 to support

    * querying of GitHub profiles.

    * Extends the DataSource.Connection class to enable

    * Salesforce to sync the external system’s schema

    * and to handle queries and searches of the external data.

    **/

   global class GitHubDataSourceConnection extends DataSource.Connection {

      private DataSource.ConnectionParams connectionInfo;

      /**

      * Constructor for GitHubDataSourceConnection

      **/

      global GitHubDataSourceConnection(DataSource.ConnectionParams connectionInfo) {

        this.connectionInfo = connectionInfo;

      }

      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages

      * for an external object that’s associated with the

      * external data source.

      *

      * The queryContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult query(DataSource.QueryContext context) {

        DataSource.Filter filter = context.tableSelection.filter;

        String url, tableName;

        if(context.tableSelection.tableSelected.equals('GithubIssues')) {

           tableName = 'GithubIssues';

           if (filter != null) {

             String thisColumnName = filter.columnName;

             if (thisColumnName != null &&

               (thisColumnName.equals('ExternalId') ||

               thisColumnName.equals('number')))

```


Apex Developer Guide Using Salesforce Features with Apex

```
               url = 'callout:GithubNC/issues/' + filter.columnValue;

             else

               url = 'callout:GithubNC/issues';

           } else {

             url = 'callout:GithubNC/issues';

           }

        } else if(context.tableSelection.tableSelected.equals('IssueComments')) {

           tableName = 'IssueComments';

           if (filter != null) {

             String thisColumnName = filter.columnName;

             if (thisColumnName != null &&

               (thisColumnName.equals('ExternalId') ||

               thisColumnName.equals('id')))

               url = 'callout:GithubNC/issues/comments/' + filter.columnValue;

             else

               url = 'callout:GithubNC/issues/comments';

           } else {

             url = 'callout:GithubNC/issues/comments';

           }

        }

        /**

         * Filters, sorts, and applies limit and offset clauses.

         **/

       List<Map<String, Object>> rows = DataSource.QueryUtils.process(context, getData(url,

    tableName));

        return DataSource.TableResult.get(true, null, context.tableSelection.tableSelected,

    rows);

      }

      /**

      * Defines the schema for the external system.

      * Called when the Salesforce admin clicks “Validate and Sync”

      * in the user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =new List<DataSource.Table>();

        List<DataSource.Column> columns, commentsColumns;

        columns = new List<DataSource.Column>();

        commentsColumns = new List<DataSource.Column>();

        // Defines the external lookup field.

        commentsColumns.add(DataSource.Column.externalLookup('issue_number',

   'GithubIssues__x'));

        commentsColumns.add(DataSource.Column.text('ExternalId', 255));

        commentsColumns.add(DataSource.Column.url('DisplayUrl'));

        commentsColumns.add(DataSource.Column.text('Body'));

        commentsColumns.add(DataSource.Column.text('Created_By'));

        commentsColumns.add(DataSource.Column.datetime('Created'));

        commentsColumns.add(DataSource.Column.datetime('Updated'));

        tables.add(DataSource.Table.get('IssueComments','id', commentsColumns));

       //================================================================================

```


Apex Developer Guide Using Salesforce Features with Apex

```
        // Defines the indirect lookup field. (For this to work,

        // make sure your Product2 standard object has a

        // custom unique, external ID field called Repository.)

        columns.add(DataSource.Column.indirectLookup( 'repository_url', 'Product2',

   'Repository__c'));

        columns.add(DataSource.Column.text('ExternalId',255));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text('Title',255));

        columns.add(DataSource.Column.text('Description'));

        columns.add(DataSource.Column.text('Repo_Name'));

        columns.add(DataSource.Column.url('Repo_URL'));

        List<Map<String,String>> stateList = new List<Map<String, String>>();

        Map<String, String> open = new Map<String,String>();

        open.put('Open', 'Open');

        stateList.add(open);

        Map<String, String> closed = new Map<String,String>();

        closed.put('Closed', 'Closed');

        stateList.add(closed);

        columns.add(DataSource.Column.picklist('State',stateList));

        List<Map<String,String>> stateReasonList = new List<Map<String, String>>();

        Map<String, String> completed = new Map<String,String>();

        completed.put('Completed', 'completed');

        stateReasonList.add(completed);

        Map<String, String> reopened = new Map<String,String>();

        reopened.put('Reopened', 'reopened');

        stateReasonList.add(reopened);

        Map<String, String> notPlanned = new Map<String,String>();

        notPlanned.put('Not Planned', 'not_planned');

        stateReasonList.add(notPlanned);

        columns.add(DataSource.Column.picklist('State_Reason',stateReasonList));

        columns.add(DataSource.Column.boolean('Locked'));

        columns.add(DataSource.Column.text('Lock_Reason', 255));

        columns.add(DataSource.Column.datetime('Created'));

        columns.add(DataSource.Column.datetime('Updated'));

        columns.add(DataSource.Column.datetime('Closed_At'));

        tables.add(DataSource.Table.get('GithubIssues','repository_url', columns));

        return tables;

      }

      /**

      * Called to do a full text search and get results from

      * the external system for SOSL queries and Salesforce

      * global searches.

      *

      * The SearchContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns results for each table that the SearchContext

      * requested to be searched.

      **/

```


Apex Developer Guide Using Salesforce Features with Apex

```
      override global List<DataSource.TableResult> search(

           DataSource.SearchContext context) {

        List<DataSource.TableResult> results =

             new List<DataSource.TableResult>();

        for (Integer i =0;i< context.tableSelections.size();i++) {

           String entity = context.tableSelections[i].tableSelected;

           String url = 'callout:GithubNC/issues/' + context.searchPhrase;

           results.add(DataSource.TableResult.get(true, null, entity, getData(url,

   entity)));

        }

        return results;

      }

      global override List<DataSource.UpsertResult> upsertRows(DataSource.UpsertContext

   context) {

        List<DataSource.UpsertResult> results = new List<DataSource.UpsertResult>();

        String tableName = context.tableSelected;

        // Calls the GitHub API to create and update issues.

        List<Map<String, Object>> rows = context.rows;

        for(Integer i = 0; i < rows.size(); i++) {

           Map<String,Object> row = rows[i];

           Map<String,Object> obj = new Map<String,Object>();

           String externalId = (String) row.get('ExternalId');

           String url, httpMethod;

           if(tableName.equals('GithubIssues')) {

             url = 'callout:GithubNC/issues';

             httpMethod = 'POST';

             if(!String.isBlank(externalId)){

               httpMethod = 'PATCH';

               url = url+'/'+externalId;

             }

             obj.put('title', row.get('Title'));

             obj.put('body', row.get('Description'));

             obj.put('state', row.get('State'));

             obj.put('state_reason', String.isBlank((String) row.get('State_Reason'))?

    null: row.get('State_Reason'));

             obj.put('closed_at', row.get('Closed_At'));

           }

           else if(tableName.equals('IssueComments')) {

             url = 'callout:GithubNC/issues';

             if(!String.isBlank(externalId)){

               httpMethod = 'PATCH';

               url = url+'/comments/'+externalId;

             } else {

               httpMethod = 'POST';

               url = url+'/' + row.get('issue_number') + '/comments';

             }

             obj.put('body', row.get('Body'));

```


Apex Developer Guide Using Salesforce Features with Apex

```
           }

           HttpResponse response = getResponse(url, httpMethod, obj);

           if (response.getStatusCode() != 200){

             results.add(DataSource.UpsertResult.failure(

               String.valueOf(row.get('ExternalId')), 'The callout resulted in an

   error: ' + response.getStatusCode()+' - '+response.getBody()));

           }

           System.debug(response.getBody());

           if(tableName.equals('GithubIssues')) {

             HttpResponse responseForLock = null;

             if(!String.isBlank(externalId)) {

               Boolean currentlyLocked = isIssueLockedCurrently(url);

               Boolean isLocked = (Boolean) row.get('Locked');

               Boolean lockStatusChanged = currentlyLocked != isLocked;

               if(lockStatusChanged) {

                  url = url + '/lock';

                  if(isLocked) {

                    Map<String, Object> lockReasonObj = new Map<String, Object>();

                    lockReasonObj.put('lock_reason', row.get('Lock_Reason'));

                    responseForLock = getResponse(url, 'PUT', lockReasonObj);

                  }

                  else {

                    responseForLock = getResponse(url, 'DELETE', null);

                  }

                  if (responseForLock.getStatusCode() != 200) {

                    results.add(DataSource.UpsertResult.failure(

                     String.valueOf(row.get('ExternalId')), 'The callout resulted

    in an error: ' + responseForLock.getStatusCode()+' - '+responseForLock.getBody()));

                  }

                  System.debug(responseForLock.getBody());

               }

             }

           }

           results.add(DataSource.UpsertResult.success(String.valueOf(externalId)));

        }

        return results;

      }

      global override List<DataSource.DeleteResult> deleteRows(DataSource.DeleteContext

   context) {

        List<DataSource.DeleteResult> results = new List<DataSource.DeleteResult>();

        String tableName = context.tableSelected;

        // Calls the GitHub API to delete issues.

        if(tableName.equals('IssueComments')) {

           for(String externalId: context.externalIds) {

             String httpMethod = 'DELETE';

             String url = 'callout:GithubNC/issues/comments/'+externalId;

```


Apex Developer Guide Using Salesforce Features with Apex

```
             HttpResponse response = getResponse(url, httpMethod, null);

             if (response.getStatusCode() != 204){

               results.add(DataSource.DeleteResult.failure(

                  externalId, 'The callout resulted in an error: ' +

   response.getStatusCode()+' - '+response.getBody()));

             }

             System.debug(response.getBody());

             results.add(DataSource.DeleteResult.success(String.valueOf(externalId)));

           }

        } else if(tableName.equals('GithubIssues')) {

           System.debug('Deletion not supported for GitHub Issues.');

          results.add(DataSource.DeleteResult.failure(String.valueOf(context.externalIds),

    'Deletion not supported for GitHub Issues.'));

        }

        return results;

      }

      /**

      * Helper method to parse the data.

      * The url argument is the URL of the external system.

      * Returns a list of rows from the external system.

      **/

      public List<Map<String, Object>> getData(String url, String tableName) {

        String response = getResponse(url, 'GET', null).getBody();

        // Standardize response string

        if (!response.contains('"items":')) {

           if (response.substring(0,1).equals('{')) {

             response = '[' + response + ']';

           }

           response = '{"items": ' + response + '}';

        }

        List<Map<String, Object>> rows = new List<Map<String, Object>>();

        Map<String, Object> responseBodyMap = (Map<String, Object>)

   JSON.deserializeUntyped(response);

        /**

         * Checks errors.

         **/

        Map<String, Object> error = (Map<String, Object>)responseBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList = (List<Object>)error.get('errors');

           Map<String, Object> errors = (Map<String, Object>)errorsList[0];

           String errorMessage = (String)errors.get('message');

           throw new DataSource.OAuthTokenExpiredException(errorMessage);

        }

        List<Object> fileItems = (List<Object>)responseBodyMap.get('items');

        if (fileItems != null) {

           for (Integer i=0; i < fileItems.size(); i++) {

             Map<String, Object> item = (Map<String, Object>)fileItems[i];

```


Apex Developer Guide Using Salesforce Features with Apex

```
             rows.add(createRow(item, tableName));

           }

        } else {

           rows.add(createRow(responseBodyMap, tableName));

        }

        return rows;

      }

      /**

      * Helper method to populate the External ID and Display

      * URL fields on external object records based on the 'id'

      * value that’s sent by the external system.

      *

      * The Map<String, Object> item parameter maps to the data

      * that represents a row.

      *

      * Returns an updated map with the External ID and

      * Display URL values.

      **/

      public Map<String, Object> createRow(Map<String, Object> item, String tableName) {

        Map<String, Object> row = new Map<String, Object>();

        for ( String key : item.keySet() ) {

           if(tableName.equals('GithubIssues')) {

             if (key == 'number') {

               row.put('ExternalId', item.get(key));

             } else if (key=='title') {

               row.put('Title', item.get(key));

             } else if (key=='body') {

               row.put('Description', item.get(key));

             } else if (key=='url') {

               row.put('DisplayUrl', item.get(key));

             } else if (key=='repository_url') {

               String repoUrl = (String) item.get(key);

               row.put('Repo_URL', repoUrl);

               //extract repository name from the URL and add it to the Repo_Name

   field

               String repoName = repoUrl.substring(repoUrl.lastIndexOf('/')+1);

               row.put('Repo_Name', repoName);

               row.put(key, item.get(key));

             } else if (key=='state') {

               row.put('State', item.get(key));

             } else if (key=='state_reason') {

               row.put('State_Reason', item.get(key));

             } else if (key=='locked') {

               row.put('Locked', item.get(key));

             } else if (key=='active_lock_reason') {

               row.put('Lock_Reason', item.get(key));

             } else if (key=='created_at' && item.get(key) != null) {

               DateTime createdDateTime =

   (DateTime)Json.deserialize('"'+item.get(key)+'"', DateTime.class);

               row.put('Created', createdDateTime);

             } else if (key=='updated_at' && item.get(key) != null) {

               DateTime updatedDateTime =

```


Apex Developer Guide Using Salesforce Features with Apex

```
   (DateTime)Json.deserialize('"'+item.get(key)+'"', DateTime.class);

               row.put('Updated', updatedDateTime);

             } else if (key=='closed_at' && item.get(key) != null) {

               DateTime closedDateTime =

   (DateTime)Json.deserialize('"'+item.get(key)+'"', DateTime.class);

               row.put('Closed_At', closedDateTime);

             } else {

               row.put(key, item.get(key));

             }

           }

           else if (tableName.equals('IssueComments')) {

             if (key=='id') {

               row.put('ExternalId', item.get(key));

             } else if (key=='url') {

               row.put('DisplayUrl', item.get(key));

             } else if (key == 'body') {

               row.put('Body', item.get(key));

             } else if (key=='user') {

               Map<String, Object> ownerMap = (Map<String, Object>)item.get(key);

               row.put('Created_By', ownerMap.get('login'));

             } else if (key=='created_at' && item.get(key) != null) {

               DateTime createdDateTime =

   (DateTime)Json.deserialize('"'+item.get(key)+'"', DateTime.class);

               row.put('Created', createdDateTime);

             } else if (key=='updated_at' && item.get(key) != null) {

               DateTime updatedDateTime =

   (DateTime)Json.deserialize('"'+item.get(key)+'"', DateTime.class);

               row.put('Updated', updatedDateTime);

             } else if (key=='issue_url') {

               String issueUrl = (String) item.get(key);

              row.put('issue_number', issueUrl.substring(issueUrl.lastIndexOf('/')+1));

             } else {

              row.put(key, item.get(key));

             }

           }

        }

        return row;

      }

      public Boolean isIssueLockedCurrently(String url) {

        String existingIssue = getResponse(url, 'GET', null).getBody();

        Map<String, Object> existingIssueBodyMap = (Map<String, Object>)

   JSON.deserializeUntyped(existingIssue);

        /**

         * Checks errors.

         **/

       Map<String, Object> error = (Map<String, Object>) existingIssueBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList = (List<Object>)error.get('errors');

           Map<String, Object> errors = (Map<String, Object>)errorsList[0];

           String errorMessage = (String)errors.get('message');

```


Apex Developer Guide Using Salesforce Features with Apex

```
           throw new DataSource.OAuthTokenExpiredException(errorMessage);

        }

        return (Boolean) existingIssueBodyMap.get('locked');

      }

      /**

      * The url argument is the URL of the external system.

      * Returns the response from the external system.

      **/

      public HttpResponse getResponse(String url, String httpMethod, Map<String,Object>

   issue) {

        // Perform callouts for production (non-test) results.

        Http httpProtocol = new Http();

        HttpRequest request = new HttpRequest();

        request.setEndpoint(url);

        request.setMethod(httpMethod);

        if(issue != null)

           request.setBody(JSON.serialize(issue));

        return httpProtocol.send(request);

      }

   }

```

DataSource.Provider Class

This example creates a class named `GitHubDataSourceProvider` .

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class GitHubDataSourceProvider extends DataSource.Provider {

      /**

      * For simplicity, this example declares that the external

      * system doesn’t require authentication by returning

      * AuthenticationCapability.ANONYMOUS as the sole entry

      * in the list of authentication capabilities.

      **/

     override global List<DataSource.AuthenticationCapability> getAuthenticationCapabilities()

    {

        List<DataSource.AuthenticationCapability> capabilities = new

   List<DataSource.AuthenticationCapability>();

        capabilities.add(DataSource.AuthenticationCapability.ANONYMOUS);

        return capabilities;

      }

      /**

      * Declares the functional capabilities that the

      * external system supports, in this case

```


Apex Developer Guide Using Salesforce Features with Apex

```
      * only SOQL queries.

      **/

      override global List<DataSource.Capability> getCapabilities() {

        List<DataSource.Capability> capabilities = new List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        capabilities.add(DataSource.Capability.ROW_CREATE);

        capabilities.add(DataSource.Capability.ROW_UPDATE);

        capabilities.add(DataSource.Capability.ROW_DELETE);

        capabilities.add(DataSource.Capability.PICKLIST);

        capabilities.add(DataSource.Capability.MULTI_PICKLIST);

        capabilities.add(DataSource.Capability.SEARCH);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection getConnection(DataSource.ConnectionParams

   connectionParams) {

        return new GitHubDataSourceConnection(connectionParams);

      }

   }

###### GitHub Custom Adapter for Salesforce Connect

```

This example illustrates how to support indirect lookup relationships. An indirect lookup relationship links a child external object to a
parent standard or custom object.

For this example to work, create a custom field on the Contact standard object. Name the custom field _`github_username`_, make
it a text field of length 39, and select the `External ID` and `Unique` attributes. Also, add https://api.github.com to your remote
site settings.

GitHubDataSourceConnection Class

```
   /**

    * Defines the connection to GitHub REST API v3 to support

    * querying of GitHub profiles.

    * Extends the DataSource.Connection class to enable

    * Salesforce to sync the external system’s schema

    * and to handle queries and searches of the external data.

    **/

   global class GitHubDataSourceConnection extends

        DataSource.Connection {

      private DataSource.ConnectionParams connectionInfo;

      /**

      * Constructor for GitHubDataSourceConnection

      **/

      global GitHubDataSourceConnection(

           DataSource.ConnectionParams connectionInfo) {

        this.connectionInfo = connectionInfo;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages

      * for an external object that’s associated with the

      * external data source.

      *

      * The queryContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult query(

           DataSource.QueryContext context) {

        DataSource.Filter filter = context.tableSelection.filter;

        String url;

        if (filter != null) {

           String thisColumnName = filter.columnName;

           if (thisColumnName != null &&

            (thisColumnName.equals('ExternalId') ||

             thisColumnName.equals('login')))

             url = 'https://api.github.com/users/'

                  + filter.columnValue;

           else

               url = 'https://api.github.com/users';

        } else {

           url = 'https://api.github.com/users';

        }

        /**

         * Filters, sorts, and applies limit and offset clauses.

         **/

        List<Map<String, Object>> rows =

             DataSource.QueryUtils.process(context, getData(url));

        return DataSource.TableResult.get(true, null,

             context.tableSelection.tableSelected, rows);

      }

      /**

      * Defines the schema for the external system.

      * Called when the administrator clicks “Validate and Sync”

      * in the user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

             new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        // Defines the indirect lookup field. (For this to work,

        // make sure your Contact standard object has a

        // custom unique, external ID field called github_username.)

        columns.add(DataSource.Column.indirectLookup(

             'login', 'Contact', 'github_username__c'));

```


Apex Developer Guide Using Salesforce Features with Apex

```
        columns.add(DataSource.Column.text('id', 255));

        columns.add(DataSource.Column.text('name',255));

        columns.add(DataSource.Column.text('company',255));

        columns.add(DataSource.Column.text('bio',255));

        columns.add(DataSource.Column.text('followers',255));

        columns.add(DataSource.Column.text('following',255));

        columns.add(DataSource.Column.url('html_url'));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text('ExternalId',255));

        tables.add(DataSource.Table.get('githubProfile','login',

             columns));

        return tables;

      }

      /**

      * Called to do a full text search and get results from

      * the external system for SOSL queries and Salesforce

      * global searches.

      *

      * The SearchContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns results for each table that the SearchContext

      * requested to be searched.

      **/

      override global List<DataSource.TableResult> search(

           DataSource.SearchContext context) {

        List<DataSource.TableResult> results =

             new List<DataSource.TableResult>();

        for (Integer i =0;i< context.tableSelections.size();i++) {

           String entity = context.tableSelections[i].tableSelected;

           // Search usernames

           String url = 'https://api.github.com/users/'

                    + context.searchPhrase;

           results.add(DataSource.TableResult.get(

               true, null, entity, getData(url)));

        }

        return results;

      }

      /**

      * Helper method to parse the data.

      * The url argument is the URL of the external system.

      * Returns a list of rows from the external system.

      **/

      public List<Map<String, Object>> getData(String url) {

        String response = getResponse(url);

        // Standardize response string

        if (!response.contains('"items":')) {

           if (response.substring(0,1).equals('{')) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
             response = '[' + response + ']';

           }

           response = '{"items": ' + response + '}';

        }

        List<Map<String, Object>> rows =

             new List<Map<String, Object>>();

        Map<String, Object> responseBodyMap = (Map<String, Object>)

             JSON.deserializeUntyped(response);

        /**

         * Checks errors.

         **/

        Map<String, Object> error =

             (Map<String, Object>)responseBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList =

               (List<Object>)error.get('errors');

           Map<String, Object> errors =

               (Map<String, Object>)errorsList[0];

           String errorMessage = (String)errors.get('message');

           throw new

               DataSource.OAuthTokenExpiredException(errorMessage);

        }

        List<Object> fileItems =

           (List<Object>)responseBodyMap.get('items');

        if (fileItems != null) {

           for (Integer i=0; i < fileItems.size(); i++) {

             Map<String, Object> item =

                  (Map<String, Object>)fileItems[i];

             rows.add(createRow(item));

           }

        } else {

           rows.add(createRow(responseBodyMap));

        }

        return rows;

      }

      /**

      * Helper method to populate the External ID and Display

      * URL fields on external object records based on the 'id'

      * value that’s sent by the external system.

      *

      * The Map<String, Object> item parameter maps to the data

      * that represents a row.

      *

      * Returns an updated map with the External ID and

      * Display URL values.

      **/

      public Map<String, Object> createRow(

           Map<String, Object> item){

```


Apex Developer Guide Using Salesforce Features with Apex

```
        Map<String, Object> row = new Map<String, Object>();

        for ( String key : item.keySet() ) {

           if (key == 'login') {

             row.put('ExternalId', item.get(key));

           } else if (key=='html_url') {

             row.put('DisplayUrl', item.get(key));

           }

           row.put(key, item.get(key));

        }

        return row;

      }

      /**

      * Helper method to make the HTTP GET call.

      * The url argument is the URL of the external system.

      * Returns the response from the external system.

      **/

      public String getResponse(String url) {

        // Perform callouts for production (non-test) results.

        Http httpProtocol = new Http();

        HttpRequest request = new HttpRequest();

        request.setEndPoint(url);

        request.setMethod('GET');

        HttpResponse response = httpProtocol.send(request);

        return response.getBody();

      }

   }

```

GitHubDataSourceProvider Class

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class GitHubDataSourceProvider

        extends DataSource.Provider {

      /**

      * For simplicity, this example declares that the external

      * system doesn’t require authentication by returning

      * AuthenticationCapability.ANONYMOUS as the sole entry

      * in the list of authentication capabilities.

      **/

      override global List<DataSource.AuthenticationCapability>

      getAuthenticationCapabilities() {

        List<DataSource.AuthenticationCapability> capabilities =

             new List<DataSource.AuthenticationCapability>();

        capabilities.add(

             DataSource.AuthenticationCapability.ANONYMOUS);

        return capabilities;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      /**

      * Declares the functional capabilities that the

      * external system supports, in this case

      * only SOQL queries.

      **/

      override global List<DataSource.Capability>

      getCapabilities() {

        List<DataSource.Capability> capabilities =

             new List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection getConnection(

           DataSource.ConnectionParams connectionParams) {

        return new GitHubDataSourceConnection(connectionParams);

      }

   }

```

SEE ALSO:

Adding Remote Site Settings

###### Google Drive [™] Custom Adapter for Salesforce Connect

This example illustrates how to use callouts and OAuth to connect to an external system, which in this case is the Google Drive [™] online
storage service. The example also shows how to avoid failing tests from web service callouts by returning mock responses for test
methods.

For this example to work reliably, request offline access when setting up OAuth so that Salesforce can obtain and maintain a refresh
token for your connections.

DriveDataSourceConnection Class

```
   /**

    * Extends the DataSource.Connection class to enable

    * Salesforce to sync the external system’s schema

    * and to handle queries and searches of the external data.

    **/

   global class DriveDataSourceConnection extends

      DataSource.Connection {

      private DataSource.ConnectionParams connectionInfo;

      /**

      * Constructor for DriveDataSourceConnection.

      **/

      global DriveDataSourceConnection(

        DataSource.ConnectionParams connectionInfo) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
        this.connectionInfo = connectionInfo;

      }

      /**

      * Called when an external object needs to get a list of

      * schema from the external data source, for example when

      * the administrator clicks “Validate and Sync” in the

      * user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

           new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('title', 255));

        columns.add(DataSource.Column.text('description',255));

        columns.add(DataSource.Column.text('createdDate',255));

        columns.add(DataSource.Column.text('modifiedDate',255));

        columns.add(DataSource.Column.url('selfLink'));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text('ExternalId',255));

        tables.add(DataSource.Table.get('googleDrive','title',

           columns));

        return tables;

      }

      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages

      * for an external object that’s associated with the

      * external data source.

      *

      * The QueryContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult query(

        DataSource.QueryContext context) {

        DataSource.Filter filter = context.tableSelection.filter;

        String url;

        if (filter != null) {

           String thisColumnName = filter.columnName;

           if (thisColumnName != null &&

               thisColumnName.equals('ExternalId'))

             url = 'https://www.googleapis.com/drive/v2/'

             + 'files/' + filter.columnValue;

           else

             url = 'https://www.googleapis.com/drive/v2/'

             + 'files';

        } else {

           url = 'https://www.googleapis.com/drive/v2/'

           + 'files';

        }

```


Apex Developer Guide Using Salesforce Features with Apex

```
        /**

         * Filters, sorts, and applies limit and offset clauses.

         **/

        List<Map<String, Object>> rows =

           DataSource.QueryUtils.process(context, getData(url));

        return DataSource.TableResult.get(true, null,

           context.tableSelection.tableSelected, rows);

      }

      /**

      * Called to do a full text search and get results from

      * the external system for SOSL queries and Salesforce

      * global searches.

      *

      * The SearchContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns results for each table that the SearchContext

      * requested to be searched.

      **/

      override global List<DataSource.TableResult> search(

        DataSource.SearchContext context) {

        List<DataSource.TableResult> results =

           new List<DataSource.TableResult>();

        for (Integer i =0;i< context.tableSelections.size();i++) {

           String entity = context.tableSelections[i].tableSelected;

           String url =

             'https://www.googleapis.com/drive/v2/files'+

             '?q=fullText+contains+\''+context.searchPhrase+'\'';

           results.add(DataSource.TableResult.get(

             true, null, entity, getData(url)));

        }

        return results;

      }

      /**

      * Helper method to parse the data.

      * The url argument is the URL of the external system.

      * Returns a list of rows from the external system.

      **/

      public List<Map<String, Object>> getData(String url) {

        String response = getResponse(url);

        List<Map<String, Object>> rows =

           new List<Map<String, Object>>();

        Map<String, Object> responseBodyMap = (Map<String, Object>)

           JSON.deserializeUntyped(response);

        /**

         * Checks errors.

```


Apex Developer Guide Using Salesforce Features with Apex

```
         **/

        Map<String, Object> error =

           (Map<String, Object>)responseBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList =

             (List<Object>)error.get('errors');

           Map<String, Object> errors =

             (Map<String, Object>)errorsList[0];

           String errorMessage = (String)errors.get('message');

           throw new DataSource.OAuthTokenExpiredException(errorMessage);

        }

        List<Object> fileItems=(List<Object>)responseBodyMap.get('items');

        if (fileItems != null) {

           for (Integer i=0; i < fileItems.size(); i++) {

             Map<String, Object> item =

               (Map<String, Object>)fileItems[i];

             rows.add(createRow(item));

           }

        } else {

           rows.add(createRow(responseBodyMap));

        }

        return rows;

      }

      /**

      * Helper method to populate the External ID and Display

      * URL fields on external object records based on the 'id'

      * value that’s sent by the external system.

      *

      * The Map<String, Object> item parameter maps to the data

      * that represents a row.

      *

      * Returns an updated map with the External ID and

      * Display URL values.

      **/

      public Map<String, Object> createRow(

        Map<String, Object> item){

        Map<String, Object> row = new Map<String, Object>();

        for ( String key : item.keySet() ) {

           if (key == 'id') {

             row.put('ExternalId', item.get(key));

           } else if (key=='selfLink') {

             row.put(key, item.get(key));

             row.put('DisplayUrl', item.get(key));

           } else {

             row.put(key, item.get(key));

           }

        }

        return row;

      }

      static String mockResponse = '{' +

```


Apex Developer Guide Using Salesforce Features with Apex

```
       ' "kind": "drive#file",' +

       ' "id": "12345",' +

       ' "selfLink": "files/12345",' +

       ' "title": "Mock File",' +

       ' "mimeType": "application/text",' +

       ' "description": "Mock response that’s used during tests",' +

       ' "createdDate": "2016-04-20",' +

       ' "modifiedDate": "2016-04-20",' +

       ' "version": 1' +

       '}';

      /**

      * Helper method to make the HTTP GET call.

      * The url argument is the URL of the external system.

      * Returns the response from the external system.

      **/

      public String getResponse(String url) {

        if (System.Test.isRunningTest()) {

         // Avoid callouts during tests. Return mock data instead.

         return mockResponse;

        } else {

         // Perform callouts for production (non-test) results.

         Http httpProtocol = new Http();

         HttpRequest request = new HttpRequest();

         request.setEndPoint(url);

         request.setMethod('GET');

         request.setHeader('Authorization', 'Bearer '+

            this.connectionInfo.oauthToken);

         HttpResponse response = httpProtocol.send(request);

         return response.getBody();

        }

      }

   }

```

DriveDataSourceProvider Class

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class DriveDataSourceProvider

      extends DataSource.Provider {

      /**

      * Declares the types of authentication that can be used

      * to access the external system.

      **/

      override global List<DataSource.AuthenticationCapability>

        getAuthenticationCapabilities() {

        List<DataSource.AuthenticationCapability> capabilities =

           new List<DataSource.AuthenticationCapability>();

```


Apex Developer Guide Using Salesforce Features with Apex

```
        capabilities.add(

           DataSource.AuthenticationCapability.OAUTH);

        capabilities.add(

           DataSource.AuthenticationCapability.ANONYMOUS);

        return capabilities;

      }

      /**

      * Declares the functional capabilities that the

      * external system supports.

      **/

      override global List<DataSource.Capability>

        getCapabilities() {

        List<DataSource.Capability> capabilities =

           new List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        capabilities.add(DataSource.Capability.SEARCH);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection getConnection(

        DataSource.ConnectionParams connectionParams) {

        return new DriveDataSourceConnection(connectionParams);

      }

   }

###### Google Books [™] Custom Adapter for Salesforce Connect

```

This example illustrates how to work around the requirements and limits of an external system’s APIs: in this case, the Google Books API
Family.

To integrate with the Google Books [™] service, we set up Salesforce Connect as follows.

**•** The Google Books API allows a maximum of 40 returned results, so we develop our custom adapter to handle result sets with more
than 40 rows.

**•** The Google Books API can sort only by search relevance and publish dates, so we develop our custom adapter to disable sorting on
columns.

**•** To support OAuth, we set up our authentication settings in Salesforce so that the requested scope of permissions for access tokens
includes _`https://www.googleapis.com/auth/books`_ .

**•** To allow Apex callouts, we define these remote sites in Salesforce:

**–** https://www.googleapis.com

**–** https://books.google.com

BooksDataSourceConnection Class

```
   /**

    * Extends the DataSource.Connection class to enable

    * Salesforce to sync the external system metadata

```


Apex Developer Guide Using Salesforce Features with Apex

```
    * schema and to handle queries and searches of the external

    * data.

    **/

   global class BooksDataSourceConnection extends

      DataSource.Connection {

      private DataSource.ConnectionParams connectionInfo;

      // Constructor for BooksDataSourceConnection.

      global BooksDataSourceConnection(DataSource.ConnectionParams

                         connectionInfo) {

        this.connectionInfo = connectionInfo;

      }

      /**

      * Called when an external object needs to get a list of

      * schema from the external data source, for example when

      * the administrator clicks “Validate and Sync” in the

      * user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

           new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(getColumn('title'));

        columns.add(getColumn('description'));

        columns.add(getColumn('publishedDate'));

        columns.add(getColumn('publisher'));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text('ExternalId', 255));

        tables.add(DataSource.Table.get('googleBooks', 'title',

                           columns));

        return tables;

      }

      /**

      * Google Books API v1 doesn't support sorting,

      * so we create a column with sortable = false.

      **/

      private DataSource.Column getColumn(String columnName) {

        DataSource.Column column = DataSource.Column.text(columnName,

                                     255);

        column.sortable = false;

        return column;

      }

      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages

      * for an external object that's associated with the

      * external data source.

      *

      * The QueryContext argument represents the query to run

```


Apex Developer Guide Using Salesforce Features with Apex

```
      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult query(

               DataSource.QueryContext contexts) {

        DataSource.Filter filter = contexts.tableSelection.filter;

        String url;

        if (contexts.tableSelection.columnsSelected.size() == 1 &&

        contexts.tableSelection.columnsSelected.get(0).aggregation ==

           DataSource.QueryAggregation.COUNT) {

           return getCount(contexts);

        }

        if (filter != null) {

           String thisColumnName = filter.columnName;

           if (thisColumnName != null &&

             thisColumnName.equals('ExternalId')) {

             url = 'https://www.googleapis.com/books/v1/' +

               'volumes?q=' + filter.columnValue +

               '&maxResults=1&id=' + filter.columnValue;

             return DataSource.TableResult.get(true, null,

                    contexts.tableSelection.tableSelected,

                    getData(url));

           }

           else {

             url = 'https://www.googleapis.com/books/' +

               'v1/volumes?q=' + filter.columnValue +

               '&id=' + filter.columnValue +

               '&maxResults=40' + '&startIndex=';

           }

        } else {

           url = 'https://www.googleapis.com/books/v1/' +

             'volumes?q=america&' + '&maxResults=40' +

             '&startIndex=';

        }

        /**

         * Google Books API v1 supports maxResults of 40

         * so we handle pagination explicitly in the else statement

         * when we handle more than 40 records per query.

         **/

        if (contexts.maxResults < 40) {

           return DataSource.TableResult.get(true, null,

               contexts.tableSelection.tableSelected,

               getData(url + contexts.offset));

        }

        else {

           return fetchData(contexts, url);

        }

      }

      /**

      * Helper method to fetch results when maxResults is

      * greater than 40 (the max value for maxResults supported

```


Apex Developer Guide Using Salesforce Features with Apex

```
      * by Google Books API v1).

      **/

      private DataSource.TableResult fetchData(

        DataSource.QueryContext contexts, String url) {

        Integer fetchSlot = (contexts.maxResults / 40) + 1;

        List<Map<String, Object>> data =

           new List<Map<String, Object>>();

        Integer startIndex = contexts.offset;

        for(Integer count = 0; count < fetchSlot; count++) {

           data.addAll(getData(url + startIndex));

           if(count == 0)

             contexts.offset = 41;

           else

             contexts.offset += 40;

        }

        return DataSource.TableResult.get(true, null,

                  contexts.tableSelection.tableSelected, data);

      }

      /**

      * Helper method to execute count() query.

      **/

      private DataSource.TableResult getCount(

        DataSource.QueryContext contexts) {

        String url = 'https://www.googleapis.com/books/v1/' +

               'volumes?q=america&projection=full';

        List<Map<String,Object>> response =

           DataSource.QueryUtils.filter(contexts, getData(url));

        List<Map<String, Object>> countResponse =

           new List<Map<String, Object>>();

        Map<String, Object> countRow =

           new Map<String, Object>();

        countRow.put(

           contexts.tableSelection.columnsSelected.get(0).columnName,

           response.size());

        countResponse.add(countRow);

        return DataSource.TableResult.get(contexts, countResponse);

      }

      /**

      * Called to do a full text search and get results from

      * the external system for SOSL queries and Salesforce

      * global searches.

      *

      * The SearchContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns results for each table that the SearchContext

      * requested to be searched.

      **/

      override global List<DataSource.TableResult> search(

        DataSource.SearchContext contexts) {

        List<DataSource.TableResult> results =

```


Apex Developer Guide Using Salesforce Features with Apex

```
           new List<DataSource.TableResult>();

        for (Integer i =0; i< contexts.tableSelections.size();i++) {

           String entity = contexts.tableSelections[i].tableSelected;

           String url = 'https://www.googleapis.com/books/v1' +

                  '/volumes?q=' + contexts.searchPhrase;

           results.add(DataSource.TableResult.get(true, null,

                                entity,

                                getData(url)));

        }

        return results;

      }

      /**

      * Helper method to parse the data.

      * Returns a list of rows from the external system.

      **/

      public List<Map<String, Object>> getData(String url) {

        HttpResponse response = getResponse(url);

        String body = response.getBody();

        List<Map<String, Object>> rows =

           new List<Map<String, Object>>();

        Map<String, Object> responseBodyMap =

           (Map<String, Object>)JSON.deserializeUntyped(body);

      /**

      * Checks errors.

      **/

        Map<String, Object> error =

           (Map<String, Object>)responseBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList =

             (List<Object>)error.get('errors');

           Map<String, Object> errors =

             (Map<String, Object>)errorsList[0];

           String messages = (String)errors.get('message');

           throw new DataSource.OAuthTokenExpiredException(messages);

        }

        List<Object> sItems = (List<Object>)responseBodyMap.get('items');

        if (sItems != null) {

           for (Integer i=0; i< sItems.size(); i++) {

             Map<String, Object> item =

               (Map<String, Object>)sItems[i];

             rows.add(createRow(item));

           }

        } else {

           rows.add(createRow(responseBodyMap));

        }

        return rows;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      /**

      * Helper method to populate a row based on source data.

      *

      * The item argument maps to the data that

      * represents a row.

      *

      * Returns an updated map with the External ID and

      * Display URL values.

      **/

      public Map<String, Object> createRow(

        Map<String, Object> item) {

        Map<String, Object> row = new Map<String, Object>();

        for ( String key : item.keySet() ){

           if (key == 'id') {

             row.put('ExternalId', item.get(key));

           } else if (key == 'volumeInfo') {

             Map<String, Object> volumeInfoMap =

               (Map<String, Object>)item.get(key);

             row.put('title', volumeInfoMap.get('title'));

             row.put('description',

                  volumeInfoMap.get('description'));

             row.put('DisplayUrl',

                  volumeInfoMap.get('infoLink'));

             row.put('publishedDate',

                  volumeInfoMap.get('publishedDate'));

             row.put('publisher',

                  volumeInfoMap.get('publisher'));

           }

        }

        return row;

      }

      /**

      * Helper method to make the HTTP GET call.

      * The url argument is the URL of the external system.

      * Returns the response from the external system.

      **/

      public HttpResponse getResponse(String url) {

        Http httpProtocol = new Http();

        HttpRequest request = new HttpRequest();

        request.setEndPoint(url);

        request.setMethod('GET');

        request.setHeader('Authorization', 'Bearer '+

                  this.connectionInfo.oauthToken);

        HttpResponse response = httpProtocol.send(request);

        return response;

      }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

BooksDataSourceProvider Class

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class BooksDataSourceProvider extends

      DataSource.Provider {

      /**

      * Declares the types of authentication that can be used

      * to access the external system.

      **/

      override global List<DataSource.AuthenticationCapability>

        getAuthenticationCapabilities() {

        List<DataSource.AuthenticationCapability> capabilities =

           new List<DataSource.AuthenticationCapability>();

        capabilities.add(

           DataSource.AuthenticationCapability.OAUTH);

        capabilities.add(

           DataSource.AuthenticationCapability.ANONYMOUS);

        return capabilities;

      }

      /**

      * Declares the functional capabilities that the

      * external system supports.

      **/

      override global List<DataSource.Capability>

        getCapabilities() {

        List<DataSource.Capability> capabilities = new

           List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        capabilities.add(DataSource.Capability.SEARCH);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection getConnection(

        DataSource.ConnectionParams connectionParams) {

        return new BooksDataSourceConnection(connectionParams);

      }

   }

###### Loopback Custom Adapter for Salesforce Connect

```

This example illustrates how to handle filtering in queries. For simplicity, this example connects the Salesforce org to itself as the external
system.


Apex Developer Guide Using Salesforce Features with Apex

LoopbackDataSourceConnection Class

```
   /**

    * Extends the DataSource.Connection class to enable
    * Salesforce to sync the external systemâ€ [™] s schema

    * and to handle queries and searches of the external data.

    **/

   global class LoopbackDataSourceConnection

      extends DataSource.Connection {

      /**

      * Constructors.

      **/

      global LoopbackDataSourceConnection(

        DataSource.ConnectionParams connectionParams) {

      }

      global LoopbackDataSourceConnection() {}

      /**

      * Called when an external object needs to get a list of

      * schema from the external data source, for example when

      * the administrator clicks â€œValidate and Syncâ€ � in the

      * user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

           new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('ExternalId', 255));

        columns.add(DataSource.Column.url('DisplayUrl'));

        columns.add(DataSource.Column.text('Name', 255));

        columns.add(

           DataSource.Column.number('NumberOfEmployees', 18, 0));

        tables.add(

           DataSource.Table.get('Looper', 'Name', columns));

        return tables;

      }

      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages
      * for an external object thatâ€ [™] s associated with the

      * external data source.

      *

      * The QueryContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult

        query(DataSource.QueryContext context) {

        if (context.tableSelection.columnsSelected.size() == 1 &&

           context.tableSelection.columnsSelected.get(0).aggregation ==

             DataSource.QueryAggregation.COUNT) {

```


Apex Developer Guide Using Salesforce Features with Apex

```
           integer count = execCount(getCountQuery(context));

           List<Map<String, Object>> countResponse =

             new List<Map<String, Object>>();

           Map<String, Object> countRow =

             new Map<String, Object>();

           countRow.put(

             context.tableSelection.columnsSelected.get(0).columnName,

             count);

           countResponse.add(countRow);

           return DataSource.TableResult.get(context,countResponse);

        } else {

           List<Map<String,Object>> rows = execQuery(

             getSoqlQuery(context));

           return DataSource.TableResult.get(context,rows);

        }

      }

      /**

      * Called to do a full text search and get results from

      * the external system for SOSL queries and Salesforce

      * global searches.

      *

      * The SearchContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns results for each table that the SearchContext

      * requested to be searched.

      **/

      override global List<DataSource.TableResult>

        search(DataSource.SearchContext context) {

        return DataSource.SearchUtils.searchByName(context, this);

      }

      /**

      * Helper method to execute the SOQL query and

      * return the results.

      **/

      private List<Map<String,Object>>

        execQuery(String soqlQuery) {

        List<Account> objs = Database.query(soqlQuery);

        List<Map<String,Object>> rows =

           new List<Map<String,Object>>();

        for (Account obj : objs) {

           Map<String,Object> row = new Map<String,Object>();

           row.put('Name', obj.Name);

           row.put('NumberOfEmployees', obj.NumberOfEmployees);

           row.put('ExternalId', obj.Id);

           row.put('DisplayUrl',

             URL.getOrgDomainUrl().toExternalForm() +

               obj.Id);

           rows.add(row);

        }

        return rows;

      }

```


Apex Developer Guide Using Salesforce Features with Apex

```
      /**

      * Helper method to get aggregate count.

      **/

      private integer execCount(String soqlQuery) {

        integer count = Database.countQuery(soqlQuery);

        return count;

      }

      /**

      * Helper method to create default aggregate query.

      **/

      private String getCountQuery(DataSource.QueryContext context) {

        String baseQuery = 'SELECT COUNT() FROM Account';

        String filter = getSoqlFilter('',

           context.tableSelection.filter);

        if (filter.length() > 0)

           return baseQuery + ' WHERE ' + filter;

        return baseQuery;

      }

      /**

      * Helper method to create default query.

      **/

      private String getSoqlQuery(DataSource.QueryContext context) {

        String baseQuery =

           'SELECT Id,Name,NumberOfEmployees FROM Account';

        String filter = getSoqlFilter('',

           context.tableSelection.filter);

        if (filter.length() > 0)

           return baseQuery + ' WHERE ' + filter;

        return baseQuery;

      }

      /**

      * Helper method to handle query filter.

      **/

      private String getSoqlFilter(String query,

        DataSource.Filter filter) {

        if (filter == null) {

           return query;

        }

        String append;

        DataSource.FilterType type = filter.type;

        List<Map<String,Object>> retainedRows =

           new List<Map<String,Object>>();

        if (type == DataSource.FilterType.NOT_) {

           DataSource.Filter subfilter = filter.subfilters.get(0);

           append = getSoqlFilter('NOT', subfilter);

        } else if (type == DataSource.FilterType.AND_) {

           append =

             getSoqlFilterCompound('AND', filter.subfilters);

        } else if (type == DataSource.FilterType.OR_) {

           append =

```


Apex Developer Guide Using Salesforce Features with Apex

```
             getSoqlFilterCompound('OR', filter.subfilters);

        } else {

           append = getSoqlFilterExpression(filter);

        }

        return query + ' ' + append;

      }

      /**

      * Helper method to handle query subfilters.

      **/

      private String getSoqlFilterCompound(String operator,

        List<DataSource.Filter> subfilters) {

        String expression = ' (';

        boolean first = true;

        for (DataSource.Filter subfilter : subfilters) {

           if (first)

             first = false;

           else

             expression += ' ' + operator + ' ';

           expression += getSoqlFilter('', subfilter);

        }

        expression += ') ';

        return expression;

      }

      /**

      * Helper method to handle query filter expressions.

      **/

      private String getSoqlFilterExpression(

        DataSource.Filter filter) {

        String columnName = filter.columnName;

        String operator;

        Object expectedValue = filter.columnValue;

        if (filter.type == DataSource.FilterType.EQUALS) {

           operator = '=';

        } else if (filter.type ==

           DataSource.FilterType.NOT_EQUALS) {

           operator = '<>';

        } else if (filter.type ==

           DataSource.FilterType.LESS_THAN) {

           operator = '<';

        } else if (filter.type ==

           DataSource.FilterType.GREATER_THAN) {

           operator = '>';

        } else if (filter.type ==

           DataSource.FilterType.LESS_THAN_OR_EQUAL_TO) {

           operator = '<=';

        } else if (filter.type ==

           DataSource.FilterType.GREATER_THAN_OR_EQUAL_TO) {

           operator = '>=';

        } else if (filter.type ==

           DataSource.FilterType.STARTS_WITH) {

           return mapColumnName(columnName) +

           ' LIKE \'' + String.valueOf(expectedValue) + '%\'';

```


Apex Developer Guide Using Salesforce Features with Apex

```
        } else if (filter.type ==

           DataSource.FilterType.ENDS_WITH) {

           return mapColumnName(columnName) +

           ' LIKE \'%' + String.valueOf(expectedValue) + '\'';

        } else if (filter.type ==

           DataSource.FilterType.LIKE_) {

           return mapColumnName(columnName) +

           ' LIKE \'' + String.valueOf(expectedValue) + '\'';

        } else {

           throwException(

           'Implementing other filter types is left as an exercise for the reader: '

           + filter.type);

        }

        return mapColumnName(columnName) +

           ' ' + operator + ' ' + wrapValue(expectedValue);

      }

      /**

      * Helper method to map column names.

      **/

      private String mapColumnName(String apexName) {

        if (apexName.equalsIgnoreCase('ExternalId'))

           return 'Id';

        if (apexName.equalsIgnoreCase('DisplayUrl'))

           return 'Id';

        return apexName;

      }

      /**

      * Helper method to wrap expression Strings with quotes.

      **/

      private String wrapValue(Object foundValue) {

        if (foundValue instanceof String)

           return '\'' + String.valueOf(foundValue) + '\'';

        return String.valueOf(foundValue);

      }

   }

```

LoopbackDataSourceProvider Class

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class LoopbackDataSourceProvider

      extends DataSource.Provider {

      /**

      * Declares the types of authentication that can be used

      * to access the external system.

      **/

```


Apex Developer Guide Using Salesforce Features with Apex

```
      override global List<DataSource.AuthenticationCapability>

        getAuthenticationCapabilities() {

        List<DataSource.AuthenticationCapability> capabilities =

           new List<DataSource.AuthenticationCapability>();

        capabilities.add(

           DataSource.AuthenticationCapability.ANONYMOUS);

        capabilities.add(

           DataSource.AuthenticationCapability.BASIC);

        return capabilities;

      }

      /**

      * Declares the functional capabilities that the

      * external system supports.

      **/

      override global List<DataSource.Capability>

        getCapabilities() {

        List<DataSource.Capability> capabilities =

           new List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        capabilities.add(DataSource.Capability.SEARCH);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection

        getConnection(DataSource.ConnectionParams connectionParams) {

        return new LoopbackDataSourceConnection();

      }

   }

###### Stack Overflow Custom Adapter for Salesforce Connect

```

This example illustrates how to support external lookup relationships and multiple tables. An external lookup relationship links a child
standard, custom, or external object to a parent external object. Each table can become an external object in the Salesforce org.

For this example to work, create a custom field on the Contact standard object. Name the custom field “github_username” and select
the `External ID` and `Unique` attributes.

StackOverflowDataSourceConnection Class

```
   /**

    * Defines the connection to Stack Exchange API v2.2 to support

    * querying of Stack Overflow users (stackoverflowUser)

    * and posts (stackoverflowPost).

    * Extends the DataSource.Connection class to enable

    * Salesforce to sync the external system’s schema

    * and to handle queries of the external data.

    **/

   global class StackOverflowDataSourceConnection extends

        DataSource.Connection {

      private DataSource.ConnectionParams connectionInfo;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      /**

      * Constructor for StackOverflowDataSourceConnection

      **/

      global StackOverflowDataSourceConnection(

           DataSource.ConnectionParams connectionInfo) {

        this.connectionInfo = connectionInfo;

      }

      /**

      * Defines the schema for the external system.

      * Called when the administrator clicks “Validate and Sync”

      * in the user interface for the external data source.

      **/

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables =

             new List<DataSource.Table>();

        // Defines columns for the table of Stack OverFlow posts

        List<DataSource.Column> postColumns =

         new List<DataSource.Column>();

        // Defines the external lookup field.

        postColumns.add(DataSource.Column.externalLookup(

         'owner_id', 'stackoverflowUser__x'));

        postColumns.add(DataSource.Column.text('title', 255));

        postColumns.add(DataSource.Column.text('view_count', 255));

        postColumns.add(DataSource.Column.text('question_id',255));

        postColumns.add(DataSource.Column.text('creation_date',255));

        postColumns.add(DataSource.Column.text('score',255));

        postColumns.add(DataSource.Column.url('link'));

        postColumns.add(DataSource.Column.url('DisplayUrl'));

        postColumns.add(DataSource.Column.text('ExternalId',255));

        tables.add(DataSource.Table.get('stackoverflowPost','title',

         postColumns));

        // Defines columns for the table of Stack OverFlow users

        List<DataSource.Column> userColumns =

         new List<DataSource.Column>();

        userColumns.add(DataSource.Column.text('user_id', 255));

        userColumns.add(DataSource.Column.text('display_name', 255));

        userColumns.add(DataSource.Column.text('location',255));

        userColumns.add(DataSource.Column.text('creation_date',255));

        userColumns.add(DataSource.Column.url('website_url',255));

        userColumns.add(DataSource.Column.text('reputation',255));

        userColumns.add(DataSource.Column.url('link'));

        userColumns.add(DataSource.Column.url('DisplayUrl'));

        userColumns.add(DataSource.Column.text('ExternalId',255));

        tables.add(DataSource.Table.get('stackoverflowUser',

             'Display_name', userColumns));

        return tables;

```


Apex Developer Guide Using Salesforce Features with Apex

```
      }

      /**

      * Called to query and get results from the external

      * system for SOQL queries, list views, and detail pages

      * for an external object that’s associated with the

      * external data source.

      *

      * The QueryContext argument represents the query to run

      * against a table in the external system.

      *

      * Returns a list of rows as the query results.

      **/

      override global DataSource.TableResult query(

           DataSource.QueryContext context) {

        DataSource.Filter filter = context.tableSelection.filter;

        String url;

        // Sets the URL to query Stack Overflow posts

        if (context.tableSelection.tableSelected

   .equals('stackoverflowPost')) {

           if (filter != null) {

             String thisColumnName = filter.columnName;

             if (thisColumnName != null &&

                  thisColumnName.equals('ExternalId'))

               url = 'https://api.stackexchange.com/2.2/'

                    + 'questions/' + filter.columnValue

                    + '?order=desc&sort=activity'

                    + '&site=stackoverflow';

             else

                  url = 'https://api.stackexchange.com/2.2/'

                       + 'questions'

                       + '?order=desc&sort=activity'

                       + '&site=stackoverflow';

           } else {

             url = 'https://api.stackexchange.com/2.2/'

                  + 'questions'

                  + '?order=desc&sort=activity'

                  + '&site=stackoverflow';

           }

        // Sets the URL to query Stack Overflow users

        } else if (context.tableSelection.tableSelected

   .equals('stackoverflowUser')) {

           if (filter != null) {

             String thisColumnName = filter.columnName;

             if (thisColumnName != null &&

                  thisColumnName.equals('ExternalId'))

               url = 'https://api.stackexchange.com/2.2/'

                    + 'users/' + filter.columnValue

                    + '?order=desc&sort=reputation'

                    + '&site=stackoverflow';

             else

               url = 'https://api.stackexchange.com/2.2/'

                    + 'users' +

```


Apex Developer Guide Using Salesforce Features with Apex

```
   '?order=desc&sort=reputation&site=stackoverflow';

           } else {

             url = 'https://api.stackexchange.com/2.2/'

                  + 'users' + '?order=desc&sort=reputation'

                  + '&site=stackoverflow';

           }

        }

        /**

         * Filters, sorts, and applies limit and offset clauses.

         **/

        List<Map<String, Object>> rows =

             DataSource.QueryUtils.process(context, getData(url));

        return DataSource.TableResult.get(true, null,

             context.tableSelection.tableSelected, rows);

      }

      /**

      * Helper method to parse the data.

      * The url argument is the URL of the external system.

      * Returns a list of rows from the external system.

      **/

      public List<Map<String, Object>> getData(String url) {

        String response = getResponse(url);

        List<Map<String, Object>> rows =

             new List<Map<String, Object>>();

        Map<String, Object> responseBodyMap = (Map<String, Object>)

             JSON.deserializeUntyped(response);

        /**

         * Checks errors.

         **/

        Map<String, Object> error =

             (Map<String, Object>)responseBodyMap.get('error');

        if (error!=null) {

           List<Object> errorsList =

               (List<Object>)error.get('errors');

           Map<String, Object> errors =

               (Map<String, Object>)errorsList[0];

           String errorMessage = (String)errors.get('message');

           throw new

               DataSource.OAuthTokenExpiredException(errorMessage);

        }

        List<Object> fileItems=

           (List<Object>)responseBodyMap.get('items');

        if (fileItems != null) {

           for (Integer i=0; i < fileItems.size(); i++) {

             Map<String, Object> item =

                  (Map<String, Object>)fileItems[i];

             rows.add(createRow(item));

           }

```


Apex Developer Guide Using Salesforce Features with Apex

```
        } else {

           rows.add(createRow(responseBodyMap));

        }

        return rows;

      }

      /**

      * Helper method to populate the External ID and Display

      * URL fields on external object records based on the 'id'

      * value that’s sent by the external system.

      *

      * The Map<String, Object> item parameter maps to the data

      * that represents a row.

      *

      * Returns an updated map with the External ID and

      * Display URL values.

      **/

      public Map<String, Object> createRow(

           Map<String, Object> item) {

        Map<String, Object> row = new Map<String, Object>();

        for ( String key : item.keySet() ) {

           if (key.equals('question_id') || key.equals('user_id')) {

             row.put('ExternalId', item.get(key));

           } else if (key.equals('link')) {

             row.put('DisplayUrl', item.get(key));

           } else if (key.equals('owner')) {

             Map<String, Object> ownerMap =

             (Map<String, Object>)item.get(key);

             row.put('owner_id', ownerMap.get('user_id'));

           }

           row.put(key, item.get(key));

        }

        return row;

      }

      /**

      * Helper method to make the HTTP GET call.

      * The url argument is the URL of the external system.

      * Returns the response from the external system.

      **/

      public String getResponse(String url) {

        // Perform callouts for production (non-test) results.

        Http httpProtocol = new Http();

        HttpRequest request = new HttpRequest();

        request.setEndPoint(url);

        request.setMethod('GET');

        HttpResponse response = httpProtocol.send(request);

        return response.getBody();

      }

   }

```


Apex Developer Guide Using Salesforce Features with Apex

StackOverflowPostDataSourceProvider Class

```
   /**

    * Extends the DataSource.Provider base class to create a

    * custom adapter for Salesforce Connect. The class informs

    * Salesforce of the functional and authentication

    * capabilities that are supported by or required to connect

    * to an external system.

    **/

   global class StackOverflowPostDataSourceProvider

        extends DataSource.Provider {

      /**

      * For simplicity, this example declares that the external

      * system doesn’t require authentication by returning

      * AuthenticationCapability.ANONYMOUS as the sole entry

      * in the list of authentication capabilities.

      **/

      override global List<DataSource.AuthenticationCapability>

      getAuthenticationCapabilities() {

        List<DataSource.AuthenticationCapability> capabilities =

             new List<DataSource.AuthenticationCapability>();

        capabilities.add(

             DataSource.AuthenticationCapability.ANONYMOUS);

        return capabilities;

      }

      /**

      * Declares the functional capabilities that the

      * external system supports, in this case

      * only SOQL queries.

      **/

      override global List<DataSource.Capability>

      getCapabilities() {

        List<DataSource.Capability> capabilities =

             new List<DataSource.Capability>();

        capabilities.add(DataSource.Capability.ROW_QUERY);

        return capabilities;

      }

      /**

      * Declares the associated DataSource.Connection class.

      **/

      override global DataSource.Connection getConnection(

           DataSource.ConnectionParams connectionParams) {

        return new

           StackOverflowDataSourceConnection(connectionParams);

      }

   }

#### Salesforce Reports and Dashboards API via Apex

```

The Salesforce Reports and Dashboards API via Apex gives you programmatic access to your report data as defined in the report builder.


Apex Developer Guide Using Salesforce Features with Apex

The API enables you to integrate report data into any web or mobile application, inside or outside the Salesforce platform. For example,
you might use the API to trigger a Chatter post with a snapshot of top-performing reps each quarter.

The Salesforce Reports and Dashboards API via Apex revolutionizes the way that you access and visualize your data. You can:

**•** Integrate report data into custom objects.

**•** Integrate report data into rich visualizations to animate the data.

**•** Build custom dashboards.

**•** Automate reporting tasks.

At a high level, the API resources enable you to query and filter report data. You can:

**•** Run tabular, summary, or matrix reports synchronously or asynchronously.

**•** Filter for specific data on the fly.

**•** Query report data and metadata.

##### Requirements and Limitations

The Salesforce Reports and Dashboards API via Apex is available for organizations that have API enabled.

Run Reports
You can run a report synchronously or asynchronously through the Salesforce Reports and Dashboards API via Apex.

List Asynchronous Runs of a Report
You can retrieve up to 2,000 instances of a report that you ran asynchronously.

Get Report Metadata
You can retrieve report metadata to get information about a report and its report type.

Get Report Data
You can use the `ReportResults` class to get the fact map, which contains data that’s associated with a report.

Filter Reports
To get specific results on the fly, you can filter reports through the API.

Decode the Fact Map
The fact map contains the summary and record-level data values for a report.

Test Reports
Like all Apex code, Salesforce Reports and Dashboards API via Apex code requires test coverage.

SEE ALSO:

_Apex Reference Guide_ [: Reports Namespace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_Reports.htm)

##### Requirements and Limitations

The Salesforce Reports and Dashboards API via Apex is available for organizations that have API enabled.

The following restrictions apply to the Reports and Dashboards API via Apex, in addition to general API limits.

**•** Cross filters, standard report filters, and filtering by row limit are unavailable when filtering data.

**•** Historical tracking reports are only supported for matrix reports.

**•** Subscriptions aren't supported for historical tracking reports.

**•** The API can process only reports that contain up to 100 fields selected as columns.

**•** A list of up to 200 recently viewed reports can be returned.


Apex Developer Guide Using Salesforce Features with Apex

**•** Your org can request up to 500 synchronous report runs per hour.

**•** The API supports up to 20 synchronous report run requests at a time.

**•** A list of up to 2,000 instances of a report that was run asynchronously can be returned.

**•** The API supports up to 200 requests at a time to get results of asynchronous report runs.

**•** Your organization can request up to 1,200 asynchronous requests per hour.

**•** Asynchronous report run results are available within a 24-hour rolling period.

**•** The API returns up to the first 2,000 report rows. You can narrow results using filters.

**•** You can add up to 20 custom field filters when you run a report.

**•** If a report is run on a standard or custom object as an automated process user from an Apex test class, only the required custom
fields are returned. Non-required custom fields aren’t shown in the results.

**•** **–** Your org can request up to 200 dashboard refreshes per hour.

**–** Your org can request results for up to 5,000 dashboards per hour.

In addition, the following restrictions apply to the Reports and Dashboards API via Apex.

**•** Asynchronous report calls are not allowed in batch Apex.

**•** Report calls are not allowed in Apex triggers.

**•** There is no Apex method to list recently run reports.

**•** The number of report rows processed during a synchronous report run count towards the governor limit that restricts the total
number of rows retrieved by SOQL queries to 50,000 rows per transaction. This limit is not imposed when reports are run
asynchronously.

**•** In Apex tests, report runs always ignore the `SeeAllData` annotation, regardless of whether the annotation is set to `true` or

`false` . This means that report results will include pre-existing data that the test didn’t create. There is no way to disable the
`SeeAllData` annotation for a report execution. To limit results, use a filter on the report.

**•** In Apex tests, asynchronous report runs will execute only after the test is stopped using the `Test.stopTest` method.

Note: All limits that apply to reports created in the report builder also apply to the API. For more information, see “Analytics Limits”
in the Salesforce online help.

##### Run Reports

You can run a report synchronously or asynchronously through the Salesforce Reports and Dashboards API via Apex.

Reports can be run with or without details and can be filtered by setting report metadata. When you run a report, the API returns data
for the same number of records that are available when the report is run in the Salesforce user interface.

Run a report synchronously if you expect it to finish running quickly. Otherwise, we recommend that you run reports through the
Salesforce API asynchronously for these reasons:

**•** Long-running reports have a lower risk of reaching the timeout limit when they are run asynchronously.

**•** The Salesforce Reports and Dashboards API via Apex can handle a higher number of asynchronous run requests at a time.

**•** Because the results of an asynchronously run report are stored for a 24-hour rolling period, they’re available for recurring access.

Example: **Run a Report Synchronously**

To run a report synchronously, use one of the `ReportManager.runReport()` methods. For example:

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

```


Apex Developer Guide Using Salesforce Features with Apex

```
        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Run the report

      Reports.ReportResults results = Reports.ReportManager.runReport(reportId, true);

      System.debug('Synchronous results: ' + results);

```

Example: **Run a Report Asynchronously**

To run a report asynchronously, use one of the `ReportManager.runAsyncReport()` methods. For example:

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Run the report

      Reports.ReportInstance instance = Reports.ReportManager.runAsyncReport(reportId, true);

      System.debug('Asynchronous instance: ' + instance);

##### List Asynchronous Runs of a Report

```

You can retrieve up to 2,000 instances of a report that you ran asynchronously.

The instance list is sorted by the date and time when the report was run. Report results are stored for a rolling 24-hour period. During
this time, based on your user access level, you can access results for each instance of the report that was run.

Example: You can get the instance list by calling the `ReportManager.getReportInstances` method. For example:

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Run a report asynchronously

      Reports.ReportInstance instance = Reports.ReportManager.runAsyncReport(reportId, true);

      System.debug('List of asynchronous runs: ' +

        Reports.ReportManager.getReportInstances(reportId));

##### Get Report Metadata

```

You can retrieve report metadata to get information about a report and its report type.

Metadata includes information about fields that are used in the report for filters, groupings, detailed data, and summaries. You can use
the metadata to do several things:

**•** Find out what fields and values you can filter on in the report type.

**•** Build custom chart visualizations by using the metadata information on fields, groupings, detailed data, and summaries.

**•** Change filters in the report metadata when you run a report.

Use the `ReportResults.getReportMetadata` method to retrieve report metadata. You can then use the “get” methods on
the `ReportMetadata` class to access metadata values.


Apex Developer Guide Using Salesforce Features with Apex

Example: The following example retrieves metadata for a report.

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Run a report

      Reports.ReportResults results = Reports.ReportManager.runReport(reportId);

      // Get the report metadata

      Reports.ReportMetadata rm = results.getReportMetadata();

      System.debug('Name: ' + rm.getName());

      System.debug('ID: ' + rm.getId());

      System.debug('Currency code: ' + rm.getCurrencyCode());

      System.debug('Developer name: ' + rm.getDeveloperName());

      // Get grouping info for first grouping

      Reports.GroupingInfo gInfo = rm.getGroupingsDown()[0];

      System.debug('Grouping name: ' + gInfo.getName());

      System.debug('Grouping sort order: ' + gInfo.getSortOrder());

      System.debug('Grouping date granularity: ' + gInfo.getDateGranularity());

      // Get aggregates

      System.debug('First aggregate: ' + rm.getAggregates()[0]);

      System.debug('Second aggregate: ' + rm.getAggregates()[1]);

      // Get detail columns

      System.debug('Detail columns: ' + rm.getDetailColumns());

      // Get report format

      System.debug('Report format: ' + rm.getReportFormat());

##### Get Report Data

```

You can use the `ReportResults` class to get the fact map, which contains data that’s associated with a report.

Example: To access data values of the fact map, you can map grouping value keys to the corresponding fact map keys. In the
following example, imagine that you have an opportunity report that’s grouped by close month, and you’ve summarized the
amount field. To get the value for the summary amount for the first grouping in the report:

**1.** Get the first down-grouping in the report by using the `ReportResults.getGroupingsDown` method and accessing
the first `GroupingValue` object.

**2.** Get the grouping key value from the `GroupingValue` object by using the `getKey` method.

**3.** Construct a fact map key by appending `'!T'` to this key value. The resulting fact map key represents the summary value for
the first down-grouping.

**4.** Get the fact map from the report results by using the fact map key.

**5.** Get the first summary amount value by using the `ReportFact.getAggregates` method and accessing the first
`SummaryValue` object.

**6.** Get the field value from the first data cell of the first row of the report by using the `ReportFactWithDetails.getRows`
method.


Apex Developer Guide Using Salesforce Features with Apex

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Run a report synchronously

      Reports.reportResults results = Reports.ReportManager.runReport(reportId, true);

      // Get the first down-grouping in the report

      Reports.Dimension dim = results.getGroupingsDown();

      Reports.GroupingValue groupingVal = dim.getGroupings()[0];

      System.debug('Key: ' + groupingVal.getKey());

      System.debug('Label: ' + groupingVal.getLabel());

      System.debug('Value: ' + groupingVal.getValue());

      // Construct a fact map key, using the grouping key value

      String factMapKey = groupingVal.getKey() + '!T';

      // Get the fact map from the report results

      Reports.ReportFactWithDetails factDetails =

        (Reports.ReportFactWithDetails)results.getFactMap().get(factMapKey);

      // Get the first summary amount from the fact map

      Reports.SummaryValue sumVal = factDetails.getAggregates()[0];

      System.debug('Summary Value: ' + sumVal.getLabel());

      // Get the field value from the first data cell of the first row of the report

      Reports.ReportDetailRow detailRow = factDetails.getRows()[0];

      System.debug(detailRow.getDataCells()[0].getLabel());

##### Filter Reports

```

To get specific results on the fly, you can filter reports through the API.

Changes to filters that are made through the API don’t affect the source report definition. Using the API, you can filter with up to 20
custom field filters and add filter logic (such as AND and OR). But standard filters (such as range), filtering by row limit, and cross filters
are unavailable.

Before you filter a report, it’s helpful to check the following filter values in the metadata.

**•** The `ReportTypeColumn.getFilterable` method tells you whether a field can be filtered.

**•** The `ReportTypeColumn.filterValues` method returns all filter values for a field.

**•** The `ReportManager.dataTypeFilterOperatorMap` method lists the field data types that you can use to filter the
report.

**•** The `ReportMetadata.getReportFilters` method lists all filters that exist in the report.

You can filter reports during synchronous or asynchronous report runs.

Example: To filter a report, set filter values in the report metadata and then run the report. The following example retrieves the
report metadata, overrides the filter value, and runs the report. The example:

**1.** Retrieves the report filter object from the metadata by using the `ReportMetadata.getReportFilters` method.

**2.** Sets the value in the filter to a specific date by using the `ReportFilter.setValue` method and runs the report.


Apex Developer Guide Using Salesforce Features with Apex

**3.** Overrides the filter value to a different date and runs the report again.

The output for the example shows the differing grand total values, based on the date filter that was applied.

```
      // Get the report ID

      List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

        DeveloperName = 'Closed_Sales_This_Quarter'];

      String reportId = (String)reportList.get(0).get('Id');

      // Get the report metadata

      Reports.ReportDescribeResult describe = Reports.ReportManager.describeReport(reportId);

      Reports.ReportMetadata reportMd = describe.getReportMetadata();

      // Override filter and run report

      Reports.ReportFilter filter = reportMd.getReportFilters()[0];

      filter.setValue('2013-11-01');

      Reports.ReportResults results = Reports.ReportManager.runReport(reportId, reportMd);

      Reports.ReportFactWithSummaries factSum =

        (Reports.ReportFactWithSummaries)results.getFactMap().get('T!T');

      System.debug('Value for November: ' + factSum.getAggregates()[0].getLabel());

      // Override filter and run report

      filter = reportMd.getReportFilters()[0];

      filter.setValue('2013-10-01');

      results = Reports.ReportManager.runReport(reportId, reportMd);

      factSum = (Reports.ReportFactWithSummaries)results.getFactMap().get('T!T');

      System.debug('Value for October: ' + factSum.getAggregates()[0].getLabel());

##### Decode the Fact Map

```

The fact map contains the summary and record-level data values for a report.

Depending on how you run a report, the fact map in the report results can contain values for only summary or both summary and
detailed data. The fact map values are expressed as keys, which you can programmatically use to visualize the report data. Fact map
keys provide an index into each section of a fact map, from which you can access summary and detailed data.

The pattern for the fact map keys varies by report format as shown in this table.

**Report** **Fact map key pattern**
**format**

Tabular
`T!T` : The grand total of a report. Both record data values and the grand total are represented by this key.

Summary

Matrix

```
<First level row grouping_second level row grouping_third level row
```

_**`grouping>`**_ `!T` : T refers to the row grand total.

```
<First level row grouping_second level row grouping>!<First level column
```

_**`grouping_second level column grouping>`**_ .

Each item in a row or column grouping is numbered starting with `0` . Here are some examples of fact map keys:


Apex Developer Guide Using Salesforce Features with Apex

**Fact Map** **Description**
**Key**

`0!T` The first item in the first-level grouping.

`1!T` The second item in the first-level grouping.

`0_0!T` The first item in the first-level grouping and the first item in the second-level grouping.

`0_1!T` The first item in the first-level grouping and the second item in the second-level grouping.

Let’s look at examples of how fact map keys represent data as it appears in a Salesforce tabular, summary, or matrix report.

Tabular Report Fact Map

Here’s an example of an opportunities report in tabular format. Since tabular reports don’t have groupings, all of the record level data
and summaries are expressed by the `T!T` key, which refers to the grand total.

Summary Report Fact Map

This example shows how the values in a summary report are represented in the fact map.


Apex Developer Guide Using Salesforce Features with Apex

**Fact Map Key** **Description**

`0!T` Summary for the value of opportunities in the Prospecting stage.

`1_0!T` Summary of the probabilities for the Manufacturing opportunities in the Needs Analysis stage.

Matrix Report Fact Map

Here’s an example of some fact map keys for data in a matrix opportunities report with a couple of row and column groupings.

**Fact Map Key** **Description**

`0!0` Total opportunity amount in the Prospecting stage in Q4 2010.

`0_0!0_0` Total opportunity amount in the Prospecting stage in the Manufacturing sector in October 2010.

`2_1!1_1` Total value of opportunities in the Value Proposition stage in the Technology sector in February 2011.

`T!T` Grand total summary for the report.

##### Test Reports

Like all Apex code, Salesforce Reports and Dashboards API via Apex code requires test coverage.

The Reporting Apex methods don’t run in system mode, they run in the context of the current user (also called the _context user_ or the
_logged-in_ user). The methods have access to whatever the current user has access to.


Apex Developer Guide Using Salesforce Features with Apex

In Apex tests, report runs always ignore the `SeeAllData` annotation, regardless of whether the annotation is set to `true` or `false` .
This means that report results will include pre-existing data that the test didn’t create. There is no way to disable the `SeeAllData`
annotation for a report execution. To limit results, use a filter on the report.

Example: **Create a Reports Test Class**

The following example tests asynchronous and synchronous reports. Each method:

**•** Creates a new Opportunity object and uses it to set a filter on the report.

**•** Runs the report.

**•** Calls assertions to validate the data.

Note: In Apex tests, asynchronous reports execute only after the test is stopped using the `Test.stopTest` method.

```
      @isTest

      public class ReportsInApexTest{

        @isTest(SeeAllData='true')

        public static void testAsyncReportWithTestData() {

         List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

            DeveloperName = 'Closed_Sales_This_Quarter'];

         String reportId = (String)reportList.get(0).get('Id');

         // Create an Opportunity object.

         Opportunity opp = new Opportunity(Name='ApexTestOpp', StageName='stage',

            Probability = 95, CloseDate=system.today());

         insert opp;

         Reports.ReportMetadata reportMetadata =

            Reports.ReportManager.describeReport(reportId).getReportMetadata();

         // Add a filter.

         List<Reports.ReportFilter> filters = new List<Reports.ReportFilter>();

         Reports.ReportFilter newFilter = new Reports.ReportFilter();

         newFilter.setColumn('OPPORTUNITY_NAME');

         newFilter.setOperator('equals');

         newFilter.setValue('ApexTestOpp');

         filters.add(newFilter);

         reportMetadata.setReportFilters(filters);

         Test.startTest();

         Reports.ReportInstance instanceObj =

            Reports.ReportManager.runAsyncReport(reportId,reportMetadata,false);

         String instanceId = instanceObj.getId();

         // Report instance is not available yet.

         Test.stopTest();

         // After the stopTest method, the report has finished executing

         // and the instance is available.

         instanceObj = Reports.ReportManager.getReportInstance(instanceId);

         System.assertEquals(instanceObj.getStatus(),'Success');

         Reports.ReportResults result = instanceObj.getReportResults();

```


Apex Developer Guide Using Salesforce Features with Apex

```
         Reports.ReportFact grandTotal = (Reports.ReportFact)result.getFactMap().get('T!T');

         System.assertEquals(1,(Decimal)grandTotal.getAggregates().get(1).getValue());

        }

        @isTest(SeeAllData='true')

        public static void testSyncReportWithTestData() {

         // Create an Opportunity Object.

         Opportunity opp = new Opportunity(Name='ApexTestOpp', StageName='stage',

            Probability = 95, CloseDate=system.today());

         insert opp;

         List <Report> reportList = [SELECT Id,DeveloperName FROM Report where

            DeveloperName = 'Closed_Sales_This_Quarter'];

         String reportId = (String)reportList.get(0).get('Id');

         Reports.ReportMetadata reportMetadata =

            Reports.ReportManager.describeReport(reportId).getReportMetadata();

         // Add a filter.

         List<Reports.ReportFilter> filters = new List<Reports.ReportFilter>();

         Reports.ReportFilter newFilter = new Reports.ReportFilter();

         newFilter.setColumn('OPPORTUNITY_NAME');

         newFilter.setOperator('equals');

         newFilter.setValue('ApexTestOpp');

         filters.add(newFilter);

         reportMetadata.setReportFilters(filters);

         Reports.ReportResults result =

            Reports.ReportManager.runReport(reportId,reportMetadata,false);

         Reports.ReportFact grandTotal = (Reports.ReportFact)result.getFactMap().get('T!T');

         System.assertEquals(1,(Decimal)grandTotal.getAggregates().get(1).getValue());

        }

      }

#### Salesforce Sites Salesforce Sites lets you build custom pages and Web applications by inheriting Lightning Platform capabilities including analytics,
```

workflow and approvals, and programmable logic.

You can manage your Salesforce sites in Apex using the methods of the `Site` and `Cookie` classes.


Apex Developer Guide Using Salesforce Features with Apex

##### Rewrite URLs for Salesforce Sites

Sites provides built-in logic that helps you display user-friendly URLs and links to site visitors. Create rules to rewrite URL requests
typed into the address bar, launched from bookmarks, or linked from external websites. You can also create rules to rewrite the URLs
for links within site pages. URL rewriting not only makes URLs more descriptive and intuitive for users, it allows search engines to
better index your site pages.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_sites.htm)_ : Site Class

##### Rewrite URLs for Salesforce Sites

Sites provides built-in logic that helps you display user-friendly URLs and links to site visitors. Create rules to rewrite URL requests typed
into the address bar, launched from bookmarks, or linked from external websites. You can also create rules to rewrite the URLs for links
within site pages. URL rewriting not only makes URLs more descriptive and intuitive for users, it allows search engines to better index
your site pages.

For example, let's say that you have a blog site. Without URL rewriting, a blog entry's URL might look like this:

```
   https://myblog.my.salesforce-sites.com/posts?id=003D000000Q0PcN

```

With URL rewriting, your users can access blog posts by date and title, say, instead of by record ID. The URL for one of your New Year's
Eve posts might be: `https://myblog.my.salesforce-sites.com/posts/2019/12/31/auld-lang-syne`

You can also rewrite URLs for links shown within a site page. If your New Year's Eve post contained a link to your Valentine's Day post,
the link URL might show: `https://myblog.my.salesforce-sites.com/posts/2019/02/14/last-minute-roses`

To rewrite URLs for a site, create an Apex class that maps the original URLs to user-friendly URLs, and then add the Apex class to your
site.

To learn about the methods in the `Site.UrlRewriter interface` [, see UrlRewriter Interface.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_site_urlRewriter_reference.htm)

Creating the Apex Class

The Apex class that you create must implement the provided interface `Site.UrlRewriter` . In general, it must have the following
form:

```
   global class yourClass implements Site.UrlRewriter {

      global PageReference mapRequestUrl(PageReference

           yourFriendlyUrl)

      global PageReference[] generateUrlFor(PageReference[]

           yourSalesforceUrls);

   }

```

Consider the following restrictions and recommendations as you create your Apex class:

**Class and Methods Must Be Global**
The Apex class and methods must all be `global` .

**Class Must Include Both Methods**
The Apex class must implement both the `mapRequestUrl` and `generateUrlFor` methods. If you don't want to use one
of the methods, simply have it return `null` .

**Rewriting Only Works for Visualforce Site Pages**
Incoming URL requests can only be mapped to Visualforce pages associated with your site. You can't map to standard pages, images,
or other entities.


Apex Developer Guide Using Salesforce Features with Apex

To rewrite URLs for links on your site's pages, use the `!URLFOR` function with the `$Page` merge variable. For example, the
following links to a Visualforce page named myPage:

```
     <apex:outputLink value="{!URLFOR($Page.myPage)}"></apex:outputLink>

```

Note: Visualforce `<apex:form>` elements with `forceSSL=”true”` aren't affected by the `urlRewriter` .

See the “Functions” appendix of the _[Visualforce Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)_ .

**Encoded URLs**
The URLs you get from using the `Site.urlRewriter` interface are encoded. If you need to access the unencoded values of
your URL, use the `urlDecode` [method of the EncodingUtil Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_encodingUtil.htm)

**Restricted Characters**
User-friendly URLs must be distinct from Salesforce URLs. URLs with a 3-character entity prefix or a 15- or 18-character ID aren’t
rewritten.

You can’t use periods in your user-friendly or rewritten URLs, except for the `.well-known` path component, which can’t be used
at the end of a URL.

**Restricted Strings**
You can’t use the following reserved strings as the first path component after a site’s base URL in either a user-friendly URL or a
rewritten URL. Some examples of the first past component after a site’s base URL are baseURL in
https:// _`MyDomainName`_ .my.salesforce-sites.com/baseURL, https:// _`MyDomainName`_ .my.salesforce-sites.com/pathPrefix/baseURL,
https://custom-domain/pathPrefix/baseURL, and https:// _`MyDomainName`_ .my.salesforce-sites.com/pathPrefix/baseURL/another/path.

**•** `apexcomponent`

**•** `apexpages`

**•** `aura`

**•** `chatter`

**•** `chatteranswers`

**•** `chatterservice`

**•** `cometd`

**•** `ex`

**•** `faces`

**•** `flash`

**•** `flex`

**•** `google`

**•** `home`

**•** `id`

**•** `ideas`

**•** `idp`

**•** `images`

**•** `img`

**•** `javascript`

**•** `js`

**•** `knowledge`

**•** `lightning`


Apex Developer Guide Using Salesforce Features with Apex

**•** `login`

**•** `m`

**•** `mobile`

**•** `ncsphoto`

**•** `nui`

**•** `push`

**•** `resource`

**•** `saml`

**•** `sccommunities`

**•** `search`

**•** `secur`

**•** `services`

**•** `servlet`

**•** `setup`

**•** `sfc`

**•** `sfdc`

**•** `sfdc_ns`

**•** `sfsites`

**•** `site`

**•** `style`

**•** `vote`

**•** `WEB-INF`

**•** `widg`

You can't use the following reserved strings at the end of a rewritten URL path:

**•** /aura

**•** /auraFW

**•** /auraResource

**•** /AuraJLoggingRPCService

**•** /AuraJLVRPCService

**•** /AuraJRPCService

**•** /dbcthumbnail

**•** /HelpAndTrainingDoor

**•** /htmldbcthumbnail

**•** /l

**•** /m

**•** /mobile

**Relative Paths Only**
[The PageReference.getUrl() method only returns the part of the URL immediately following the host name or site prefix (if any). For](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_System_PageReference_getUrl.htm)
example, if your URL is `https://mycompany.my.salesforce-sites.com/sales/MyPage?id=12345`, where
“sales” is the site prefix, only `/MyPage?id=12345` is returned.


Apex Developer Guide Using Salesforce Features with Apex

You can't rewrite the domain or site prefix.

**Unique Paths Only**
You can't map a URL to a directory that has the same name as your site prefix. For example, if your site URL is
`https://acme.my.salesforce-sites.com/help`, where “help” is the site prefix, you can't point the URL to
`help/page` . The resulting path, `https://acme.my.salesforce-sites.com/help/help/page`, would be
returned instead as `https://acme.my.salesforce-sites.com/help/page` .

**Query in Bulk**
For better performance with page generation, perform tasks in bulk rather than one at a time for the `generateUrlFor` method.

**Enforce Field Uniqueness**
Make sure the fields you choose for rewriting URLs are unique. Using unique or indexed fields in SOQL for your queries may improve
performance.

Adding URL Rewriting to a Site

Once you've created the URL rewriting Apex class, follow these steps to add it to your site:

**1.** From Setup, enter _`Sites`_ in the `Quick Find` box, then select **Sites** .

**2.** Click **New** or click **Edit** for an existing site.

**3.** On the Site Edit page, choose an Apex class for `URL Rewriter Class` .

**4.** Click **Save** .

Note: If you have URL rewriting enabled on your site, all PageReferences are passed through the URL rewriter. PageReferences
with `redirect` set to `true` and a `redirectCode` other than 0 return redirected URLs instead of rewritten URLs.

Code Example

In this example, we have a simple site consisting of two Visualforce pages: mycontact and myaccount. Be sure you have “Read” permission
enabled for both before trying the sample. Each page uses the standard controller for its object type. The contact page includes a link
to the parent account, plus contact details.

Before implementing rewriting, the address bar and link URLs showed the record ID (a random 15-digit string), illustrated in the “before”
figure. Once rewriting was enabled, the address bar and links show more user-friendly rewritten URLs, illustrated in the “after” figure.

The Apex class used to rewrite the URLs for these pages is shown in Example URL Rewriting Apex Class, with detailed comments.

Example Site Pages

This section shows the Visualforce for the account and contact pages used in this example.

The account page uses the standard controller for accounts and is nothing more than a standard detail page. This page should be named
myaccount.

```
   <apex:page standardController="Account">

      <apex:detail relatedList="false"/>

   </apex:page>

```

The contact page uses the standard controller for contacts and consists of two parts. The first part links to the parent account using the
`URLFOR` function and the `$Page` merge variable; the second simply provides the contact details. Notice that the Visualforce page
doesn't contain any rewriting logic except `URLFOR` . This page should be named mycontact.

```
   <apex:page standardController="contact">

      <apex:pageBlock title="Parent Account">

```


Apex Developer Guide Using Salesforce Features with Apex

```
        <apex:outputLink value="{!URLFOR($Page.mycontact,null,

             [id=contact.account.id])}">{!contact.account.name}

             </apex:outputLink>

      </apex:pageBlock>

      <apex:detail relatedList="false"/>

   </apex:page>

```

Example URL Rewriting Apex Class

The Apex class used as the URL rewriter for the site uses the `mapRequestUrl` method to map incoming URL requests to the right
Salesforce record. It also uses the `generateUrlFor` method to rewrite the URL for the link to the account page in a more user-friendly
form.

```
   global with sharing class myRewriter implements Site.UrlRewriter {

      //Variables to represent the user-friendly URLs for

      //account and contact pages

      String ACCOUNT_PAGE = '/myaccount/';

      String CONTACT_PAGE = '/mycontact/';

      //Variables to represent my custom Visualforce pages

      //that display account and contact information

      String ACCOUNT_VISUALFORCE_PAGE = '/myaccount?id=';

      String CONTACT_VISUALFORCE_PAGE = '/mycontact?id=';

      global PageReference mapRequestUrl(PageReference

           myFriendlyUrl){

        String url = myFriendlyUrl.getUrl();

        if(url.startsWith(CONTACT_PAGE)){

           //Extract the name of the contact from the URL

           //For example: /mycontact/Ryan returns Ryan

           String name = url.substring(CONTACT_PAGE.length(),

               url.length());

           //Select the ID of the contact that matches

           //the name from the URL

           Contact con = [SELECT Id FROM Contact WHERE Name =:

               name LIMIT 1];

           //Construct a new page reference in the form

           //of my Visualforce page

           return new PageReference(CONTACT_VISUALFORCE_PAGE + con.id);

        }

        if(url.startsWith(ACCOUNT_PAGE)){

           //Extract the name of the account

           String name = url.substring(ACCOUNT_PAGE.length(),

               url.length());

           //Query for the ID of an account with this name

           Account acc = [SELECT Id FROM Account WHERE Name =:name LIMIT 1];

          //Return a page in Visualforce format

           return new PageReference(ACCOUNT_VISUALFORCE_PAGE + acc.id);

        }

```


Apex Developer Guide Using Salesforce Features with Apex

```
        //If the URL isn't in the form of a contact or

        //account page, continue with the request

        return null;

      }

      global List<PageReference> generateUrlFor(List<PageReference>

           mySalesforceUrls){

        //A list of pages to return after all the links

        //have been evaluated

        List<PageReference> myFriendlyUrls = new List<PageReference>();

        //a list of all the ids in the urls

        List<id> accIds = new List<id>();

        // loop through all the urls once, finding all the valid ids

        for(PageReference mySalesforceUrl : mySalesforceUrls){

        //Get the URL of the page

        String url = mySalesforceUrl.getUrl();

           //If this looks like an account page, transform it

           if(url.startsWith(ACCOUNT_VISUALFORCE_PAGE)){

             //Extract the ID from the query parameter

             //and store in a list

             //for querying later in bulk.

                  String id= url.substring(ACCOUNT_VISUALFORCE_PAGE.length(),

                  url.length());

                  accIds.add(id);

           }

        }

      // Get all the account names in bulk

      List <account> accounts = [SELECT Name FROM Account WHERE Id IN :accIds];

      // make the new urls

      Integer counter = 0;

      // it is important to go through all the urls again, so that the order

      // of the urls in the list is maintained.

      for(PageReference mySalesforceUrl : mySalesforceUrls) {

        //Get the URL of the page

        String url = mySalesforceUrl.getUrl();

        if(url.startsWith(ACCOUNT_VISUALFORCE_PAGE)){

        myFriendlyUrls.add(new PageReference(ACCOUNT_PAGE + accounts.get(counter).name));

         counter++;

        } else {

         //If this doesn't start like an account page,

         //don't do any transformations

         myFriendlyUrls.add(mySalesforceUrl);

        }

      }

      //Return the full list of pages

```


Apex Developer Guide Using Salesforce Features with Apex

```
      return myFriendlyUrls;

     }

   }

```

Before and After Rewriting

Here is a visual example of the results of implementing the Apex class to rewrite the original site URLs. Notice the ID-based URLs in the
first figure, and the user-friendly URLs in the second.

**Site URLs Before Rewriting**

The numbered elements in this figure are:

**1.** The original URL for the contact page before rewriting

**2.** The link to the parent account page from the contact page

**3.** The original URL for the link to the account page before rewriting, shown in the browser's status bar


Apex Developer Guide Using Salesforce Features with Apex

**Site URLs After Rewriting**

The numbered elements in this figure are:

**1.** The rewritten URL for the contact page after rewriting

**2.** The link to the parent account page from the contact page

**3.** The rewritten URL for the link to the account page after rewriting, shown in the browser's status bar

#### Support Classes

Support classes allow you to interact with records commonly used by support centers, such as business hours and cases.

Working with Business Hours

Business hours are used to specify the hours at which your customer support team operates, including multiple business hours in multiple
time zones.

This example finds the time one business hour from startTime, returning the Datetime in the local time zone. It gets the default business
hours by querying BusinessHours. Also, it calls the `BusinessHours add` method.

```
   // Get the default business hours

   BusinessHours bh = [SELECT Id FROM BusinessHours WHERE IsDefault=true];

   // Create Datetime on May 28, 2008 at 1:06:08 AM in local timezone.

   Datetime startTime = Datetime.newInstance(2008, 5, 28, 1, 6, 8);

   // Find the time it will be one business hour from May 28, 2008, 1:06:08 AM using the

   // default business hours. The returned Datetime will be in the local timezone.

   Datetime nextTime = BusinessHours.add(bh.id, startTime, 60 * 60 * 1000L);

```

This example finds the time one business hour from startTime, returning the Datetime in GMT:

```
   // Get the default business hours

   BusinessHours bh = [SELECT Id FROM BusinessHours WHERE IsDefault=true];

```


Apex Developer Guide Using Salesforce Features with Apex

```
   // Create Datetime on May 28, 2008 at 1:06:08 AM in local timezone.

   Datetime startTime = Datetime.newInstance(2008, 5, 28, 1, 6, 8);

   // Find the time it will be one business hour from May 28, 2008, 1:06:08 AM using the

   // default business hours. The returned Datetime will be in GMT.

   Datetime nextTimeGmt = BusinessHours.addGmt(bh.id, startTime, 60 * 60 * 1000L);

```

The next example finds the difference between startTime and nextTime:

```
   // Get the default business hours

   BusinessHours bh = [select id from businesshours where IsDefault=true];

   // Create Datetime on May 28, 2008 at 1:06:08 AM in local timezone.

   Datetime startTime = Datetime.newInstance(2008, 5, 28, 1, 6, 8);

   // Create Datetime on May 28, 2008 at 4:06:08 PM in local timezone.

   Datetime endTime = Datetime.newInstance(2008, 5, 28, 16, 6, 8);

   // Find the number of business hours milliseconds between startTime and endTime as

   // defined by the default business hours. Will return a negative value if endTime is

   // before startTime, 0 if equal, positive value otherwise.

   Long diff = BusinessHours.diff(bh.id, startTime, endTime);

```

Working with Cases

Incoming and outgoing email messages can be associated with their corresponding cases using the `Cases` class
`getCaseIdFromEmailThreadId` method. This method is used with Email-to-Case, which is an automated process that turns
emails received from customers into customer service cases.

The following example uses an email thread ID to retrieve the related case ID.

```
   public class GetCaseIdController {

     public static void getCaseIdSample() {

        // Get email thread ID

        String emailThreadId = '_00Dxx1gEW._500xxYktg';

        // Call Apex method to retrieve case ID from email thread ID

        ID caseId = Cases.getCaseIdFromEmailThreadId(emailThreadId);

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: BusinessHours Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_businesshours.htm)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_system_cases.htm)_ : Cases Class

#### Territory Management 2.0

With trigger support for the Territory2 and UserTerritory2Association standard objects, you can automate actions and processes related
to changes in these territory management records.


Apex Developer Guide Using Salesforce Features with Apex

Sample Trigger for Territory2

This example trigger fires after Territory2 records have been created or deleted. This example trigger assumes that an organization has
a custom field called `TerritoryCount__c` defined on the Territory2Model object to track the net number of territories in each
territory model. The trigger code increments or decrements the value in the `TerritoryCount__c` field each time a territory is
created or deleted.

```
   trigger maintainTerritoryCount on Territory2 (after insert, after delete) {

      // Track the effective delta for each model

      Map<Id, Integer> modelMap = new Map<Id, Integer>();

      for(Territory2 terr : (Trigger.isInsert ? Trigger.new : Trigger.old)) {

        Integer offset = 0;

        if(modelMap.containsKey(terr.territory2ModelId)) {

          offset = modelMap.get(terr.territory2ModelId);

        }

        offset += (Trigger.isInsert ? 1 : -1);

        modelMap.put(terr.territory2ModelId, offset);

      }

      // We have a custom field on Territory2Model called TerritoryCount__c

      List<Territory2Model> models = [SELECT Id, TerritoryCount__c FROM

                    Territory2Model WHERE Id IN :modelMap.keySet()];

      for(Territory2Model tm : models) {

        // In case the field is not defined with a default of 0

        if(tm.TerritoryCount__c == null) {

          tm.TerritoryCount__c = 0;

        }

        tm.TerritoryCount__c += modelMap.get(tm.Id);

      }

      // Bulk update the field on all the impacted models

      update(models);

   }

```

Sample Trigger for UserTerritory2Association

This example trigger fires after UserTerritory2Association records have been created. This example trigger sends an email notification to
the Sales Operations group letting them know that users have been added to territories. It identifies the user who added users to
territories. Then, it identifies each added user along with which territory the user was added to and which territory model the territory
belongs to.

```
   trigger notifySalesOps on UserTerritory2Association (after insert) {

      // Query the details of the users and territories involved

      List<UserTerritory2Association> utaList = [SELECT Id, User.FirstName, User.LastName,

        Territory2.Name, Territory2.Territory2Model.Name

        FROM UserTerritory2Association WHERE Id IN :Trigger.New];

      // Email message to send

      Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

      mail.setToAddresses(new String[]{'salesOps@acme.com'});

      mail.setSubject('Users added to territories notification');

      // Build the message body

      List<String> msgBody = new List<String>();

      String addedToTerrStr = '{0}, {1} added to territory {2} in model {3} \n';

```


### Apex Developer Guide Integration and Apex Utilities

```
      msgBody.add('The following users were added to territories by ' +

        UserInfo.getFirstName() + ', ' + UserInfo.getLastName() + '\n');

      for(UserTerritory2Association uta : utaList) {

        msgBody.add(String.format(addedToTerrStr,

          new String[]{uta.User.FirstName, uta.User.LastName,

                  uta.Territory2.Name, uta.Territory2.Territory2Model.Name}));

      }

      // Set the message body and send the email

      mail.setPlainTextBody(String.join(msgBody,''));

      Messaging.sendEmail(new Messaging.Email[] { mail });

   }

### Integration and Apex Utilities

```

Apex allows you to integrate with external SOAP and REST Web services using callouts. You can use utilities for JSON, XML, data security,
and encoding. A general-purpose utility for regular expressions with text strings is also provided.

#### Invoking Callouts Using Apex

JSON Support
JavaScript Object Notation (JSON) support in Apex enables the serialization of Apex objects into JSON format and the deserialization
of serialized JSON content.

XML Support
Apex provides utility classes that enable the creation and parsing of XML content using streams and the DOM.

ZIP Support
Take advantage of a native Apex Zip library to create and extract ZIP archive files by using the class methods in the `Compression`
namespace.

Securing Your Data
You can secure your data by using the methods provided by the `Crypto` class.

Encoding Your Data
You can encode and decode URLs and convert strings to hexadecimal format by using the methods provided by the `EncodingUtil`
class.

Using Patterns and Matchers
Apex provides patterns and matchers that enable you to search text using regular expressions.

#### Invoking Callouts Using Apex

An Apex callout enables you to tightly integrate your Apex with an external service by making a call to an external Web service or sending
a HTTP request from Apex code and then receiving the response. Apex provides integration with Web services that utilize SOAP and
WSDL, or HTTP services (RESTful services).

Note: Before any Apex callout can call an external site, that site must be registered in the Remote Site Settings page, or the callout
fails. Salesforce prevents calls to unauthorized network addresses.

If the callout specifies a named credential as the endpoint, you don’t need to configure remote site settings. A named credential
specifies the URL of a callout endpoint and its required authentication parameters in one definition. To set up named credentials,
see “Define a Named Credential” in the Salesforce Help.


Apex Developer Guide Integration and Apex Utilities

To learn more about the types of callouts, see:

**•** SOAP Services: Defining a Class from a WSDL Document on page 607

**•** Invoking HTTP Callouts on page 620

**•** Asynchronous Callouts for Long-Running Requests on page 632

Tip: Callouts enable Apex to invoke external web or HTTP services. Apex Web services allow an external application to invoke
Apex methods through Web services.

##### 1. Adding Remote Site Settings

2. Named Credentials as Callout Endpoints
A named credential specifies the URL of a callout endpoint and its required authentication parameters in one definition. Salesforce
manages all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have
to. You can also skip remote site settings, which are otherwise required for callouts to external sites, for the site defined in the named
credential.

3. SOAP Services: Defining a Class from a WSDL Document

4. Invoking HTTP Callouts

5. Using Certificates

6. Callout Limits and Limitations

7. Make Long-Running Callouts with Continuations
Use asynchronous callouts to make long-running requests from a Visualforce page or a Lightning component to an external Web
service and process responses in callback methods.

##### Adding Remote Site Settings

Before any Apex callout can call an external site, that site must be registered in the Remote Site Settings page, or the callout fails. Salesforce
prevents calls to unauthorized network addresses.

Note: If the callout specifies a named credential as the endpoint, you don’t need to configure remote site settings. A named
credential specifies the URL of a callout endpoint and its required authentication parameters in one definition. To set up named
credentials, see “Define a Named Credential” in the Salesforce Help.

To add a remote site setting:

**1.** From Setup, enter _`Remote Site Settings`_ in the `Quick Find` box, then select **Remote Site Settings** .

**2.** Click **New Remote Site** .

**3.** Enter a descriptive term for the `Remote Site Name` .

**4.** Enter the URL for the remote site.

**5.** Optionally, enter a description of the site.

**6.** Click **Save** .

Tip: For best performance, verify that your remote HTTPS encrypted sites have OCSP (Online Certificate Status Protocol) stapling
turned on.


Apex Developer Guide Integration and Apex Utilities

##### Named Credentials as Callout Endpoints

A named credential specifies the URL of a callout endpoint and its required authentication parameters in one definition. Salesforce
manages all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to.
You can also skip remote site settings, which are otherwise required for callouts to external sites, for the site defined in the named
credential.

Named Credentials also include an OutboundNetworkConnection field that you can use to route callouts through a private connection.
By separating the endpoint URL and authentication from the callout definition, named credentials make callouts easier to maintain. For
example, if an endpoint URL changes, you update only the named credential. All callouts that reference the named credential simply
continue to work.

If you have multiple orgs, you can create a named credential with the same name but with a different endpoint URL in each org. You
can then package and deploy—on all the orgs—one callout definition that references the shared name of those named credentials.
For example, the named credential in each org can have a different endpoint URL to accommodate differences in development and
production environments. If an Apex callout specifies the shared name of those named credentials, the Apex class that defines the callout
can be packaged and deployed on all those orgs without programmatically checking the environment.

To reference a named credential from a callout definition, use the named credential URL. A named credential URL contains the scheme
`callout:`, the name of the named credential, and an optional path. For example:
`callout:` _`My_Named_Credential`_ `/` _`some_path`_ .

You can append a query string to a named credential URL. Use a question mark (?) as the separator between the named credential URL
and the query string. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ `?format=json` .

Example: In the following Apex code, a named credential and an appended path specify the callout’s endpoint.

```
      HttpRequest req = new HttpRequest();

      req.setEndpoint( ' callout: My_Named_Credential / some_path ' );

      req.setMethod('GET');

      Http http = new Http();

      HTTPResponse res = http.send(req);

      System.debug(res.getBody());

```

The referenced named credential specifies the endpoint URL and an external credential that specifies authentication settings.


Apex Developer Guide Integration and Apex Utilities

The Apex code remains the same no matter what authentication you use. The authentication settings differ in the external credential,
which references an authentication provider that’s defined in the org.


Apex Developer Guide Integration and Apex Utilities

In contrast, let’s see what the Apex code looks like without a named credential. Notice that the code becomes more complex to
handle authentication, even if we stick with basic password authentication. Coding OAuth is even more complex and is an ideal
use case for named credentials.

```
      HttpRequest req = new HttpRequest();

      req.setEndpoint( ' https://my_endpoint.example.com/some_path ' );

      req.setMethod('GET');

      // Because we didn't set the endpoint as a named credential,

      // our code has to specify:

      // - The required username and password to access the endpoint

      // - The header and header information

      String username = ' myname ';

      String password = ' mypwd ';

      Blob headerValue = Blob.valueOf(username + ':' + password);

      String authorizationHeader = 'BASIC ' +

      EncodingUtil.base64Encode(headerValue);

      req.setHeader('Authorization', authorizationHeader);

      // Create a new http object to send the request object

      // A response object is generated as a result of the request

      Http http = new Http();

      HTTPResponse res = http.send(req);

      System.debug(res.getBody());

###### 1. Custom Headers and Bodies of Apex Callouts That Use Named Credentials
```

Salesforce generates a standard authorization header for each callout to a named-credential-defined endpoint, but you can disable
this option. Your Apex code can also use merge fields to construct each callout’s HTTP header and body.

2. Merge Fields for Apex Callouts That Use Named Credentials
To construct the HTTP headers and request bodies of callouts to endpoints that are specified as named credentials, use these merge
fields in your Apex code.

SEE ALSO:

Invoking Callouts Using Apex

_Salesforce Help:_ [Named Credentials](https://help.salesforce.com/HTViewHelpDoc?id=named_credentials_about.htm&language=en_US)

_Salesforce Help:_ [Authentication Providers](https://help.salesforce.com/apex/HTViewHelpDoc?id=sso_authentication_providers.htm&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

###### Custom Headers and Bodies of Apex Callouts That Use Named Credentials

Salesforce generates a standard authorization header for each callout to a named-credential-defined endpoint, but you can disable this
option. Your Apex code can also use merge fields to construct each callout’s HTTP header and body.


Apex Developer Guide Integration and Apex Utilities

This flexibility enables you to use named credentials in special situations. For example, some remote endpoints require security tokens
or encrypted credentials in request headers. Some remote endpoints expect usernames and passwords in XML or JSON message bodies.
Customize the callout headers and bodies as needed.

The Salesforce admin must set up the named credential to allow Apex code to construct headers or use merge fields in HTTP headers
or bodies. The following table describes these callout options for the named credential.

**Field** **Description**

```
Generate Authorization Header

Allow Merge Fields in HTTP Header

Allow Merge Fields in HTTP Body

```

SEE ALSO:

By default, Salesforce generates an authorization header and applies it to
each callout that references the named credential.

Deselect this option only if one of the following statements applies.

**•** The remote endpoint doesn’t support authorization headers.

**•** The authorization headers are provided by other means. For example, in
Apex callouts, the developer can have the code construct a custom
authorization header for each callout.

This option is required if you reference the named credential from an external
data source.

In each Apex callout, the code specifies how the HTTP header and request
body are constructed. For example, the Apex code can set the value of a
cookie in an authorization header.

These options enable the Apex code to use merge fields to populate the
HTTP header and request body with org data when the callout is made.

These options aren’t available if you reference the named credential from an
external data source.

###### Merge Fields for Apex Callouts That Use Named Credentials

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/HTViewHelpDoc?id=named_credentials_about.htm&language=en_US)

###### Merge Fields for Apex Callouts That Use Named Credentials

To construct the HTTP headers and request bodies of callouts to endpoints that are specified as named credentials, use these merge
fields in your Apex code.

###### **Merge Field Description**

```
{!$Credential.Username}

{!$Credential.Password}

```

Username and password of the running user. Available only if the named
credential uses password authentication.

```
// non-standard authentication

req.setHeader('X-Username',

'{!$Credential.Username}');

req.setHeader('X-Password',

'{!$Credential.Password}');

```


Apex Developer Guide Integration and Apex Utilities

**Merge Field** **Description**

```
{!$Credential.OAuthToken}

```

OAuth token of the running user. Available only if the named credential uses
OAuth authentication.

```
req.setHeader('Authorization',

'{!$Credential.OAuthToken}');

```

`{!$Credential.AuthorizationMethod}` Valid values depend on the authentication protocol of the named credential.

**•** `Basic` —password authentication

**•** `Bearer` —OAuth 2.0

**•** `null` —no authentication

`{!$Credential.AuthorizationHeaderValue}` Valid values depend on the authentication protocol of the named credential.

**•** _**`Base-64 encoded username and password`**_ —password
authentication

**•** _**`OAuth token`**_ —OAuth 2.0

**•** `null` —no authentication

`{!$Credential.OAuthConsumerKey}` Consumer key. Available only if the named credential uses OAuth
authentication.

When you use merge fields to construct HTTP headers and request bodies, keep these considerations in mind.

**•** To allow Apex code to use merge fields to populate the HTTP header and request body with org data when the callout is made, a
Salesforce admin must enable **Allow Merge Fields in HTTP Header** and **Allow Merge Fields in HTTP Body** on the named
[credential. See Create or Edit a Named Credential in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.nc_create_edit_named_credential.htm&language=en_US)

**•** [To access or input custom headers, use Connect REST API. See Named Credentials Resources in the Connect REST API Developer](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_named_credentials_resources.htm)
Guide.

**•** When you use these merge fields in HTTP request bodies of callouts, you can apply the `HTMLENCODE` formula function to escape
special characters. The formula must start with HTMLENCODE, and other formula functions aren't supported. `HTMLENCODE` can’t
be used on merge fields in HTTP headers. This example escapes special characters that are in the credentials.

```
  req.setBody('Username:{!HTMLENCODE($Credential.Username)}')

  req.setBody('Password:{!HTMLENCODE($Credential.Password)}')

```

**•** When you use these merge fields in SOAP API calls, OAuth access tokens aren’t refreshed.

SEE ALSO:

Custom Headers and Bodies of Apex Callouts That Use Named Credentials

Named Credentials as Callout Endpoints

_Knowledge Article_ [: Named credential OAuth token doesn't get automatically refreshed with Salesforce SOAP API endpoint](https://help.salesforce.com/articleView?id=Named-credential-oauth-token-doesn-t-get-automatically-refreshed-with-Salesforce-SOAP-API-end-point&type=1&language=en_US)

##### SOAP Services: Defining a Class from a WSDL Document

Classes can be automatically generated from a WSDL document that is stored on a local hard drive or network. Creating a class by
consuming a WSDL document allows developers to make callouts to the external Web service in their Apex code.


Apex Developer Guide Integration and Apex Utilities

Note: Use Outbound Messaging to handle integration solutions when possible. Use callouts to third-party Web services only
when necessary.

To generate an Apex class from a WSDL:

**1.** In the application, from Setup, enter _`Apex Classes`_ in the `Quick Find` box, then select **Apex Classes** .

**2.** Click **Generate from WSDL** .

**3.** Click **Browse** to navigate to a WSDL document on your local hard drive or network, or type in the full path. This WSDL document is
the basis for the Apex class you are creating.

Note: The WSDL document that you specify might contain a SOAP endpoint location that references an outbound port.

For security reasons, Salesforce restricts the outbound ports you can specify to one of the following:

**•** 80: This port only accepts HTTP connections.

**•** 443: This port only accepts HTTPS connections.

**•** 1024–66535 (inclusive): These ports accept HTTP or HTTPS connections.

**4.** Click **Parse WSDL** to verify the WSDL document contents. The application generates a default class name for each namespace in
the WSDL document and reports any errors. Parsing fails if the WSDL contains schema types or constructs that aren’t supported by
Apex classes, or if the resulting classes exceed the 1 million character limit on Apex classes. For example, the Salesforce SOAP API
WSDL cannot be parsed.

**5.** Modify the class names as desired. While you can save more than one WSDL namespace into a single class by using the same class
name for each namespace, Apex classes can be no more than 1 million characters total.

**6.** Click **Generate Apex** . The final page of the wizard shows which classes were successfully generated, along with any errors from
other classes. The page also provides a link to view successfully generated code.

The successfully generated Apex classes include stub and type classes for calling the third-party Web service represented by the WSDL
document. These classes allow you to call the external Web service from Apex. For each generated class, a second class is created with
the same name and with a prefix of `Async` . The first class is for synchronous callouts. The second class is for asynchronous callouts. For
more information about asynchronous callouts, see Make Long-Running Callouts with Continuations.

Note the following about the generated Apex:

**•** If a WSDL document contains an Apex reserved word, the word is appended with `_x` when the Apex class is generated. For example,
`limit` in a WSDL document converts to `limit_x` in the generated Apex class. See Reserved Keywords. For details on handling
characters in element names in a WSDL that are not supported in Apex variable names, see Considerations Using WSDLs.

**•** If an operation in the WSDL has an output message with more than one element, the generated Apex wraps the elements in an
inner class. The Apex method that represents the WSDL operation returns the inner class instead of the individual elements.

**•** Since periods ( `.` ) are not allowed in Apex class names, any periods in WSDL names used to generate Apex classes are replaced by
underscores ( `_` ) in the generated Apex code.

After you have generated a class from the WSDL, you can invoke the external service referenced by the WSDL.

Note: Before you can use the samples in the rest of this topic, you must copy the Apex class `docSampleClass` from Generated
WSDL2Apex Code and add it to your organization.


Apex Developer Guide Integration and Apex Utilities

Invoking an External Service

To invoke an external service after using its WSDL document to generate an Apex class, create an instance of the stub in your Apex code
[and call the methods on it. For example, to invoke the StrikeIron IP address lookup service from Apex, you could write code similar to](http://ws.strikeiron.com/relauto/iplookup?WSDL)
the following:

```
     // Create the stub

     strikeironIplookup.DNSSoap dns = new strikeironIplookup.DNSSoap();

     // Set up the license header

     dns.LicenseInfo = new strikeiron.LicenseInfo();

     dns.LicenseInfo.RegisteredUser = new strikeiron.RegisteredUser();

     dns.LicenseInfo.RegisteredUser.UserID = 'you@company.com';

     dns.LicenseInfo.RegisteredUser.Password = 'your-password';

     // Make the Web service call

     strikeironIplookup.DNSInfo info = dns.DNSLookup('www.myname.com');

```

HTTP Header Support

You can set the HTTP headers on a Web service callout. For example, you can use this feature to set the value of a cookie in an authorization
header. To set HTTP headers, add `inputHttpHeaders_x` and `outputHttpHeaders_x` to the stub.

Note: In API versions 16.0 and earlier, HTTP responses for callouts are always decoded using UTF-8, regardless of the Content-Type
header. In API versions 17.0 and later, HTTP responses are decoded using the encoding specified in the Content-Type header.

The following samples work with the sample WSDL file in Generated WSDL2Apex Code on page 613:

Sending HTTP Headers on a Web Service Callout

```
   docSample.DocSamplePort stub = new docSample.DocSamplePort();

   stub.inputHttpHeaders_x = new Map<String, String>();

   //Setting a basic authentication header

   // Tip: Use named credentials instead.

   stub.inputHttpHeaders_x.put('Authorization', 'Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==');

   //Setting a cookie header

   stub.inputHttpHeaders_x.put('Cookie', 'name=value');

   //Setting a custom HTTP header

   stub.inputHttpHeaders_x.put('myHeader', 'myValue');

   String input = 'This is the input string';

   String output = stub.EchoString(input);

```

If a value for `inputHttpHeaders_x` is specified, it overrides the standard headers set.

Tip: Instead of hardcoding the `Authorization` header value, use named credentials. Named credentials offer a declarative
and secure way to store and manage the credentials needed for HTTP callouts so that Salesforce can authenticate with external
[APIs. For more information, see Named Credentials in](https://help.salesforce.com/s/articleView?id=sf.named_credentials_about.htm&language=en_US) _Salesforce Help_ .


Apex Developer Guide Integration and Apex Utilities

Accessing HTTP Response Headers from a Web Service Callout Response

```
   docSample.DocSamplePort stub = new docSample.DocSamplePort();

   stub.outputHttpHeaders_x = new Map<String, String>();

   String input = 'This is the input string';

   String output = stub.EchoString(input);

   //Getting cookie header

   String cookie = stub.outputHttpHeaders_x.get('Set-Cookie');

   //Getting custom header

   String myHeader = stub.outputHttpHeaders_x.get('My-Header');

```

The value of `outputHttpHeaders_x` is null by default. You must set `outputHttpHeaders_x` before you have access to the
content of headers in the response.

Supported WSDL Features

Apex supports only the document literal wrapped WSDL style and the following primitive and built-in datatypes:

**Schema Type** **Apex Type**

`xsd:anyURI` String

`xsd:boolean` Boolean

`xsd:date` Date

`xsd:dateTime` Datetime

`xsd:double` Double

`xsd:float` Double

`xsd:int` Integer

`xsd:integer` Integer

`xsd:language` String

`xsd:long` Long

`xsd:Name` String

`xsd:NCName` String

`xsd:nonNegativeInteger` Integer

`xsd:NMTOKEN` String

`xsd:NMTOKENS` String

`xsd:normalizedString` String

`xsd:NOTATION` String

`xsd:positiveInteger` Integer

`xsd:QName` String


Apex Developer Guide Integration and Apex Utilities

**Schema Type** **Apex Type**

`xsd:short` Integer

`xsd:string` String

`xsd:time` Datetime

`xsd:token` String

`xsd:unsignedInt` Integer

`xsd:unsignedLong` Long

`xsd:unsignedShort` Integer

Note: The Salesforce datatype anyType is not supported in WSDLs used to generate Apex code that is saved using API version
15.0 and later. For code saved using API version 14.0 and earlier, anyType is mapped to String.

Apex also supports the following schema constructs:

**•** `xsd:all`, in Apex code saved using API version 15.0 and later

**•** `xsd:annotation`, in Apex code saved using API version 15.0 and later

**•** `xsd:attribute`, in Apex code saved using API version 15.0 and later

**•** `xsd:choice`, in Apex code saved using API version 15.0 and later

**•** `xsd:element` . In Apex code saved using API version 15.0 and later, the `ref` attribute is also supported with the following
restrictions:

**–** You cannot call a `ref` in a different namespace.

**–** A global element cannot use `ref` .

**–** If an element contains `ref`, it cannot also contain `name` or `type` .

**•** `xsd:sequence`

The following data types are only supported when used as _call ins_, that is, when an external Web service calls an Apex Web service
method. These data types are not supported as _callouts_, that is, when an Apex Web service method calls an external Web service.

**•** blob

**•** decimal

**•** enum

Apex does not support any other WSDL constructs, types, or services, including:

**•** RPC/encoded services

**•** WSDL files with multiple `portTypes`, multiple services, or multiple bindings

**•** WSDL files that import external schemas. For example, the following WSDL fragment imports an external schema, which is not
supported:

```
      <wsdl:types>

       <xsd:schema

        elementFormDefault="qualified"

        targetNamespace="http://s3.amazonaws.com/doc/2006-03-01/">

         <xsd:include schemaLocation="AmazonS3.xsd"/>

```


Apex Developer Guide Integration and Apex Utilities

```
       </xsd:schema>

      </wsdl:types>

```

However, an import within the same schema is supported. In the following example, the external WSDL is pasted into the WSDL
you are converting:

```
      <wsdl:types>

       <xsd:schema

         xmlns:tns="http://s3.amazonaws.com/doc/2006-03-01/"

         xmlns:xsd="http://www.w3.org/2001/XMLSchema"

         elementFormDefault="qualified"

         targetNamespace="http://s3.amazonaws.com/doc/2006-03-01/">

         <xsd:element name="CreateBucket">

          <xsd:complexType>

           <xsd:sequence>

        [...]

       </xsd:schema>

      </wsdl:types>

```

**•** Any schema types not documented in the previous table

**•** WSDLs that exceed the size limit, including the Salesforce WSDLs

**•** WSDLs that don’t use the document literal wrapped style. The following WSDL snippet doesn’t use document literal wrapped style
and results in an “Unable to find complexType” error when imported.

```
      <wsdl:types>

       <xsd:schema targetNamespace="http://test.org/AccountPollInterface/"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

         <xsd:element name="SFDCPollAccountsResponse" type="tns:SFDCPollResponse"/>

         <xsd:simpleType name="SFDCPollResponse">

           <xsd:restriction base="xsd:string" />

         </xsd:simpleType>

       </xsd:schema>

      </wsdl:types>

```

This modified version wraps the `simpleType` element as a `complexType` that contains a sequence of elements. This follows
the document literal style and is supported.

```
      <wsdl:types>

       <xsd:schema targetNamespace="http://test.org/AccountPollInterface/"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

         <xsd:element name="SFDCPollAccountsResponse" type="tns:SFDCPollResponse" />

         <xsd:complexType name="SFDCPollResponse">

          <xsd:sequence>

           <xsd:element name="SFDCOutput" type="xsd:string" />

          </xsd:sequence>

         </xsd:complexType>

       </xsd:schema>

      </wsdl:types>

```

1. Generated WSDL2Apex Code
You can generate Apex classes from a WSDL document using the WSDL2Apex tool. The WSDL2Apex tool is open source and available
on GitHub.


Apex Developer Guide Integration and Apex Utilities

2. Test Web Service Callouts
Generated code is saved as an Apex class containing the methods you can invoke for calling the web service. To deploy or package
this Apex class and other accompanying code, 75% of the code must have test coverage, including the methods in the generated
class. By default, test methods don’t support web service callouts, and tests that perform web service callouts fail. To prevent tests
from failing and to increase code coverage, Apex provides the built-in `WebServiceMock` interface and the `Test.setMock`
method. Use `WebServiceMock` and `Test.setMock` to receive fake responses in a test method.

3. Performing DML Operations and Mock Callouts

4. Considerations Using WSDLs

###### Generated WSDL2Apex Code

You can generate Apex classes from a WSDL document using the WSDL2Apex tool. The WSDL2Apex tool is open source and available
on GitHub.

[You can find and contribute to the WSDL2Apex source code in the WSDL2Apex repository on GitHub.](https://github.com/forcedotcom/WSDL2Apex)

The following example shows how an Apex class is created from a WSDL document. The Apex class is auto-generated for you when you
import the WSDL.

The following code shows a sample WSDL document.

```
   <wsdl:definitions xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"

   xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"

   xmlns:s="http://www.w3.org/2001/XMLSchema"

   xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"

   xmlns:tns="http://doc.sample.com/docSample"

   targetNamespace="http://doc.sample.com/docSample"

   xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">

   <!-- Above, the schema targetNamespace maps to the Apex class name. -->

   <!-- Below, the type definitions for the parameters are listed.

      Each complexType and simpleType parameteris mapped to an Apex class inside the parent

    class for the WSDL. Then, each element in the complexType is mapped to a public field

   inside the class. -->

   <wsdl:types>

   <s:schema elementFormDefault="qualified"

   targetNamespace="http://doc.sample.com/docSample">

   <s:element name="EchoString">

   <s:complexType>

   <s:sequence>

   <s:element minOccurs="0" maxOccurs="1" name="input" type="s:string" />

   </s:sequence>

   </s:complexType>

   </s:element>

   <s:element name="EchoStringResponse">

   <s:complexType>

   <s:sequence>

   <s:element minOccurs="0" maxOccurs="1" name="EchoStringResult"

   type="s:string" />

   </s:sequence>

   </s:complexType>

```


Apex Developer Guide Integration and Apex Utilities

```
   </s:element>

   </s:schema>

   </wsdl:types>

   <!--The stub below defines operations. -->

   <wsdl:message name="EchoStringSoapIn">

   <wsdl:part name="parameters" element="tns:EchoString" />

   </wsdl:message>

   <wsdl:message name="EchoStringSoapOut">

   <wsdl:part name="parameters" element="tns:EchoStringResponse" />

   </wsdl:message>

   <wsdl:portType name="DocSamplePortType">

   <wsdl:operation name="EchoString">

   <wsdl:input message="tns:EchoStringSoapIn" />

   <wsdl:output message="tns:EchoStringSoapOut" />

   </wsdl:operation>

   </wsdl:portType>

   <!--The code below defines how the types map to SOAP. -->

   <wsdl:binding name="DocSampleBinding" type="tns:DocSamplePortType">

   <wsdl:operation name="EchoString">

   <soap:operation soapAction="urn:dotnet.callouttest.soap.sforce.com/EchoString"

   style="document" />

   <wsdl:input>

   <soap:body use="literal" />

   </wsdl:input>

   <wsdl:output>

   <soap:body use="literal" />

   </wsdl:output>

   </wsdl:operation>

   </wsdl:binding>

   <!-- Finally, the code below defines the endpoint, which maps to the endpoint in the class

    -->

   <wsdl:service name="DocSample">

   <wsdl:port name="DocSamplePort" binding="tns:DocSampleBinding">

   <soap:address location="http://YourServer/YourService" />

   </wsdl:port>

   </wsdl:service>

   </wsdl:definitions>

```

From this WSDL document, the following Apex class is auto-generated. The class name `docSample` is the name you specify when
importing the WSDL.

```
   //Generated by wsdl2apex

   public class docSample {

      public class EchoStringResponse_element {

        public String EchoStringResult;

        private String[] EchoStringResult_type_info = new String[]{

                    'EchoStringResult',

```


Apex Developer Guide Integration and Apex Utilities

```
                    'http://doc.sample.com/docSample',

                     null,'0','1','false'};

        private String[] apex_schema_type_info = new String[]{

                     'http://doc.sample.com/docSample',

                     'true','false'};

        private String[] field_order_type_info = new String[]{

                     'EchoStringResult'};

      }

      public class EchoString_element {

        public String input;

        private String[] input_type_info = new String[]{

                     'input',

                     'http://doc.sample.com/docSample',

                      null,'0','1','false'};

        private String[] apex_schema_type_info = new String[]{

                      'http://doc.sample.com/docSample',

                      'true','false'};

        private String[] field_order_type_info = new String[]{'input'};

      }

      public class DocSamplePort {

        public String endpoint_x = 'http://YourServer/YourService';

        public Map<String,String> inputHttpHeaders_x;

        public Map<String,String> outputHttpHeaders_x;

        public String clientCertName_x;

        public String clientCert_x;

        public String clientCertPasswd_x;

        public Integer timeout_x;

        private String[] ns_map_type_info = new String[]{

                   'http://doc.sample.com/docSample', 'docSample'};

        public String EchoString(String input) {

           docSample.EchoString_element request_x = new

                             docSample.EchoString_element();

           request_x.input = input;

           docSample.EchoStringResponse_element response_x;

           Map<String, docSample.EchoStringResponse_element> response_map_x =

                 new Map<String, docSample.EchoStringResponse_element>();

           response_map_x.put('response_x', response_x);

           WebServiceCallout.invoke(

            this,

            request_x,

            response_map_x,

            new String[]{endpoint_x,

            'urn:dotnet.callouttest.soap.sforce.com/EchoString',

            'http://doc.sample.com/docSample',

            'EchoString',

            'http://doc.sample.com/docSample',

            'EchoStringResponse',

            'docSample.EchoStringResponse_element'}

           );

           response_x = response_map_x.get('response_x');

           return response_x.EchoStringResult;

        }

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

Note the following mappings from the original WSDL document:

**•** The WSDL target namespace maps to the Apex class name.

**•** Each complex type becomes a class. Each element in the type is a public field in the class.

**•** The WSDL port name maps to the stub class.

**•** Each operation in the WSDL maps to a public method.

You can use the auto-generated `docSample` class to invoke external Web services. The following code calls the `echoString`
method on the external server.

```
   docSample.DocSamplePort stub = new docSample.DocSamplePort();

   String input = 'This is the input string';

   String output = stub.EchoString(input);

###### Test Web Service Callouts

```

Generated code is saved as an Apex class containing the methods you can invoke for calling the web service. To deploy or package this
Apex class and other accompanying code, 75% of the code must have test coverage, including the methods in the generated class. By
default, test methods don’t support web service callouts, and tests that perform web service callouts fail. To prevent tests from failing
and to increase code coverage, Apex provides the built-in `WebServiceMock` interface and the `Test.setMock` method. Use
`WebServiceMock` and `Test.setMock` to receive fake responses in a test method.

Specify a Mock Response for Testing Web Service Callouts

When you create an Apex class from a WSDL, the methods in the auto-generated class call `WebServiceCallout.invoke`, which
performs the callout to the external service. When testing these methods, you can instruct the Apex runtime to generate a fake response
whenever `WebServiceCallout.invoke` is called. To do so, implement the `WebServiceMock` interface and specify a fake
response for the Apex runtime to send. Here are the steps in more detail.

First, implement the `WebServiceMock` interface and specify the fake response in the `doInvoke` method.

```
   global class YourWebServiceMockImpl implements WebServiceMock {

     global void doInvoke(

          Object stub,

          Object request,

          Map<String, Object> response,

          String endpoint,

          String soapAction,

          String requestName,

          String responseNS,

          String responseName,

          String responseType) {

        // Create response element from the autogenerated class.

        // Populate response element.

        // Add response element to the response parameter, as follows:

        response.put('response_x', responseElement );

     }

   }

```

Note:

**•** The class implementing the `WebServiceMock` interface can be either global or public.


Apex Developer Guide Integration and Apex Utilities

**•** You can annotate this class with `@isTest` because it is used only in a test context. In this way, you can exclude it from your
org’s code size limit of 6 MB.

Now that you have specified the values of the fake response, instruct the Apex runtime to send this fake response by calling
`Test.setMock` in your test method. For the first argument, pass `WebServiceMock.class`, and for the second argument,
pass a new instance of your interface implementation of `WebServiceMock`, as follows:

```
   Test.setMock(WebServiceMock.class, new YourWebServiceMockImpl ());

```

After this point, if a web service callout is invoked in test context, the callout is not made. You receive the mock response specified in
your `doInvoke` method implementation.

Note: To mock a callout if the code that performs the callout is in a managed package, call `Test.setMock` from a test method
in the same package with the same namespace.

This example shows how to test a web service callout. The implementation of the `WebServiceMock` interface is listed first. This
example implements the `doInvoke` method, which returns the response you specify. In this case, the response element of the
auto-generated class is created and assigned a value. Next, the response Map parameter is populated with this fake response. This
example is based on the WSDL listed in Generated WSDL2Apex Code. Import this WSDL and generate a class called `docSample`
before you save this class.

```
   @isTest

   global class WebServiceMockImpl implements WebServiceMock {

     global void doInvoke(

          Object stub,

          Object request,

          Map<String, Object> response,

          String endpoint,

          String soapAction,

          String requestName,

          String responseNS,

          String responseName,

          String responseType) {

        docSample.EchoStringResponse_element respElement =

          new docSample.EchoStringResponse_element();

        respElement.EchoStringResult = 'Mock response';

        response.put('response_x', respElement);

     }

   }

```

This method makes a web service callout.

```
   public class WebSvcCallout {

      public static String callEchoString(String input) {

        docSample.DocSamplePort sample = new docSample.DocSamplePort();

        sample.endpoint_x = 'https://example.com/example/test';

        // This invokes the EchoString method in the generated class

        String echo = sample.EchoString(input);

        return echo;

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

This test class contains the test method that sets the mock callout mode. It calls the `callEchoString` method in the previous class
and verifies that a mock response is received.

```
   @isTest

   private class WebSvcCalloutTest {

      @isTest static void testEchoString() {

        // This causes a fake response to be generated

        Test.setMock(WebServiceMock.class, new WebServiceMockImpl());

        // Call the method that invokes a callout

        String output = WebSvcCallout.callEchoString('Hello World!');

        // Verify that a fake result is returned

        System.assertEquals('Mock response', output);

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: WebServiceMock Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_webservicemock.htm)

###### Performing DML Operations and Mock Callouts

By default, callouts aren’t allowed after DML operations in the same transaction because DML operations result in pending uncommitted
work that prevents callouts from executing. Sometimes, you might want to insert test data in your test method using DML before making
a callout. To enable this, enclose the portion of your code that performs the callout within `Test.startTest` and `Test.stopTest`
statements. The `Test.startTest` statement must appear before the `Test.setMock` statement. Also, the calls to DML operations
must not be part of the `Test.startTest` / `Test.stopTest` block.

DML operations that occur after mock callouts are allowed and don’t require any changes in test methods.

Performing DML Before Mock Callouts

This example is based on the previous example. The example shows how to use `Test.startTest` and `Test.stopTest`
statements to allow DML operations to be performed in a test method before mock callouts. The test method ( `testEchoString` )
first inserts a test account, calls `Test.startTest`, sets the mock callout mode using `Test.setMock`, calls a method that performs
the callout, verifies the mock response values, and finally, calls `Test.stopTest` .

```
   @isTest

   private class WebSvcCalloutTest {

      @isTest static void testEchoString() {

        // Perform some DML to insert test data

        Account testAcct = new Account('Test Account');

        insert testAcct;

        // Call Test.startTest before performing callout

        // but after setting test data.

        Test.startTest();

        // Set mock callout class

        Test.setMock(WebServiceMock.class, new WebServiceMockImpl());

        // Call the method that invokes a callout

        String output = WebSvcCallout.callEchoString('Hello World!');

```


Apex Developer Guide Integration and Apex Utilities

```
        // Verify that a fake result is returned

        System.assertEquals('Mock response', output);

        Test.stopTest();

      }

   }

```

Asynchronous Apex and Mock Callouts

Similar to DML, asynchronous Apex operations result in pending uncommitted work that prevents callouts from being performed later
in the same transaction. Examples of asynchronous Apex operations are calls to future methods, batch Apex, or scheduled Apex. These
asynchronous calls are typically enclosed within `Test.startTest` and `Test.stopTest` statements in test methods so that
they execute after `Test.stopTest` . In this case, mock callouts can be performed after the asynchronous calls and no changes are
necessary. But if the asynchronous calls aren’t enclosed within `Test.startTest` and `Test.stopTest` statements, you’ll get
an exception because of uncommitted work pending. To prevent this exception, do either of the following:

**•** Enclose the asynchronous call within `Test.startTest` and `Test.stopTest` statements.

```
     Test.startTest();

     MyClass.asyncCall();

     Test.stopTest();

     Test.setMock(..); // Takes two arguments

     MyClass.mockCallout();

```

**•** Follow the same rules as with DML calls: Enclose the portion of your code that performs the callout within `Test.startTest`
and `Test.stopTest` statements. The `Test.startTest` statement must appear before the `Test.setMock` statement.
Also, the asynchronous calls must not be part of the `Test.startTest` / `Test.stopTest` block.

```
     MyClass.asyncCall();

     Test.startTest();

     Test.setMock(..); // Takes two arguments

     MyClass.mockCallout();

     Test.stopTest();

```

Asynchronous calls that occur after mock callouts are allowed and don’t require any changes in test methods.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm)_ : Test Class

###### Considerations Using WSDLs

Be aware of the following when generating Apex classes from a WSDL.

SOAP Web Service Callout

For WSDLs that require namespace changes within the SOAP requests, you must manually construct the HTTP request body and invoke
the endpoint as a POST request from Apex.


Apex Developer Guide Integration and Apex Utilities

Mapping Headers

Headers defined in the WSDL document become public fields on the stub in the generated class. This is similar to how the AJAX Toolkit
and .NET works.

Understanding Runtime Events

The following checks are performed when Apex code is making a callout to an external service.

**•** For information on the timeout limits when making an HTTP request or a Web services call, see Callout Limits and Limitations on
page 631.

**•** Circular references in Apex classes are not allowed.

**•** More than one loopback connection to Salesforce domains is not allowed.

**•** To allow an endpoint to be accessed, register it from Setup by entering _`Remote Site Settings`_ in the `Quick Find` box,
then selecting **Remote Site Settings** .

**•** To prevent database connections from being held up, no transactions can be open.

Understanding Unsupported Characters in Variable Names

A WSDL file can include an element name that is not allowed in an Apex variable name. The following rules apply when generating
Apex variable names from a WSDL file:

**•** If the first character of an element name is not alphabetic, an `x` character is prepended to the generated Apex variable name.

**•** If the last character of an element name is not allowed in an Apex variable name, an `x` character is appended to the generated Apex
variable name.

**•** If an element name contains a character that is not allowed in an Apex variable name, the character is replaced with an underscore
( `_` ) character.

**•** If an element name contains two characters in a row that are not allowed in an Apex variable name, the first character is replaced
with an underscore ( `_` ) character and the second one is replaced with an `x` character. This avoids generating a variable name with
two successive underscores, which is not allowed in Apex.

**•** Suppose you have an operation that takes two parameters, `a_` and `a_x` . The generated Apex has two variables, both named `a_x` .
The class doesn’t compile. Manually edit the Apex and change one of the variable names.

Debugging Classes Generated from WSDL Files

Salesforce tests code with SOAP API, .NET, and Axis. If you use other tools, you can encounter issues.

You can use the debugging header to return the XML in request and response SOAP messages to help you diagnose problems. For more
information, see _SOAP API Developer Guide_ [: DebuggingHeader.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_header_debuggingheader.htm)

##### Invoking HTTP Callouts

Apex provides several built-in classes to work with HTTP services and create HTTP requests like GET, POST, PUT, and DELETE.

You can use these HTTP classes to integrate to REST-based services. They also allow you to integrate to SOAP-based web services as an
alternate option to generating Apex code from a WSDL. By using the HTTP classes, instead of starting with a WSDL, you take on more
responsibility for handling the construction of the SOAP message for the request and response.

1. HTTP Classes


Apex Developer Guide Integration and Apex Utilities

2. Testing HTTP Callouts
To deploy or package Apex, 75% of your code must have test coverage. By default, test methods don’t support HTTP callouts, so
tests that perform callouts fail. Enable HTTP callout testing by instructing Apex to generate mock responses in tests, using
`Test.setMock` .

###### HTTP Classes

These classes expose the HTTP request and response functionality.

**•** `[Http Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_http.htm)` . Use this class to initiate an HTTP request and response.

**•** [HttpRequest Class: Use this class to programmatically create HTTP requests like GET, POST, PATCH, PUT, and DELETE.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm)

###### • HttpResponse Class: Use this class to handle the HTTP response returned by HTTP .

The `HttpRequest` and `HttpResponse` classes support these elements.

**•** HttpRequest

**–** HTTP request types, such as GET, POST, PATCH, PUT, DELETE, TRACE, CONNECT, HEAD, and OPTIONS

**–** Request headers if needed

**–** Read and connection timeouts

**–** Redirects if needed

**–** Content of the message body

**•** `HttpResponse`

**–** The HTTP status code

**–** Response headers if needed

**–** Content of the response body

This example makes an HTTP GET request to the external server passed to the `getCalloutResponseContents` method in the
_`url`_ parameter. This example also accesses the body of the returned response.

```
   public class HttpCalloutSample {

     // Pass in the endpoint to be used using the string url

     public String getCalloutResponseContents(String url) {

      // Instantiate a new Http object

      Http h = new Http();

      // Instantiate a new HTTP request, specify the method (GET) as well as the endpoint

      HttpRequest req = new HttpRequest();

      req.setEndpoint(url);

      req.setMethod('GET');

      // Send the request, and return a response

      HttpResponse res = h.send(req);

      return res.getBody();

     }

   }

```

The previous example runs synchronously, meaning no further processing happens until the external web service returns a response.
Alternatively, you can use the @future annotation to make the callout run asynchronously.


Apex Developer Guide Integration and Apex Utilities

This example makes an HTTP POST request to the external server passed to the `getPostCalloutResponseContents` method
in the _`url`_ parameter. Replace _`Your_JSON_Content`_ with the JSON content that you want to send in the callout.

```
   public class HttpPostCalloutSample {

     // Pass in the endpoint to be used using the string url

     public String getPostCalloutResponseContents(String url) {

      // Instantiate a new Http object

      Http h = new Http();

      // Instantiate a new HTTP request

      // Specify request properties such as the endpoint, the POST method, etc.

      HttpRequest req = new HttpRequest();

      req.setEndpoint(url);

      req.setMethod('POST');

      req.setHeader('Content-Type', 'application/json');

      req.setBody('{ Your_JSON_Content }');

      // Send the request, and return a response

      HttpResponse res = h.send(req);

      return res.getBody();

     }

   }

```

To access an external server from an endpoint or a redirect endpoint, add the remote site to a list of authorized remote sites. Log in to
Salesforce and from Setup, in the Quick Find box, enter _`Remote Site Settings`_, and then select **Remote Site Settings** .

Use the XML classes or JSON classes to parse XML or JSON content in the body of a request created by `[HttpRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm)`, or a response
accessed by `[HttpResponse](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httpresponse.htm)` .

Considerations

**•** The AJAX proxy handles redirects and authentication challenges (401/407 responses) automatically. For more information about
[the AJAX proxy, see AJAX Toolkit documentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/ajax/sforce_api_ajax_queryresultiterator.htm#ajax_proxy)

**•** You can set the endpoint as a named credential URL. A named credential URL contains the scheme `callout:`, the name of the
named credential, and an optional path. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ . A named credential
specifies the URL of a callout endpoint and its required authentication parameters in one definition. Salesforce manages all
authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to. You can
also skip remote site settings, which are otherwise required for callouts to external sites, for the site defined in the named credential.
[See Named Credentials as Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

**•** When you set a request body in the callout, set the method to `POST` . If you set a request body and the request method is `GET`, a
`POST` request is performed.

**•** Callouts are blocked if you have pending uncommitted transactions from DML operations, queueable jobs (that are queued with
`System.enqueueJob` ), `Database.executeBatch`, or future methods.

###### Testing HTTP Callouts

To deploy or package Apex, 75% of your code must have test coverage. By default, test methods don’t support HTTP callouts, so tests
that perform callouts fail. Enable HTTP callout testing by instructing Apex to generate mock responses in tests, using `Test.setMock` .

Specify the mock response in one of the following ways.

**•** By implementing the `HttpCalloutMock` interface


Apex Developer Guide Integration and Apex Utilities

**•** By using Static Resources with `StaticResourceCalloutMock` or `MultiStaticResourceCalloutMock`

To enable running DML operations before mock callouts in your test methods, see Performing DML Operations and Mock Callouts.

####### Testing HTTP Callouts by Implementing the HttpCalloutMock Interface Interface

Testing HTTP Callouts Using Static Resources

Performing DML Operations and Mock Callouts

####### Testing HTTP Callouts by Implementing the HttpCalloutMock Interface Interface

Provide an implementation for the `HttpCalloutMock` interface to specify the response sent in the `respond` method, which the
Apex runtime calls to send a response for a callout.

```
   global class YourHttpCalloutMockImpl implements HttpCalloutMock {

      global HTTPResponse respond(HTTPRequest req) {

        // Create a fake response.

        // Set response values, and

        // return response.

      }

   }

```

Note:

**•** The class that implements the `HttpCalloutMock` interface can be either global or public.

**•** You can annotate this class with `@isTest` since it will be used only in test context. In this way, you can exclude it from your
organization’s code size limit of 6 MB.

Now that you have specified the values of the fake response, instruct the Apex runtime to send this fake response by calling
`Test.setMock` in your test method. For the first argument, pass `HttpCalloutMock.class`, and for the second argument,
pass a new instance of your interface implementation of `HttpCalloutMock`, as follows:

```
   Test.setMock(HttpCalloutMock.class, new YourHttpCalloutMockImpl ());

```

After this point, if an HTTP callout is invoked in test context, the callout is not made and you receive the mock response you specified in
the _`respond`_ method implementation.

Note: To mock a callout if the code that performs the callout is in a managed package, call `Test.setMock` from a test method
in the same package with the same namespace.

This is a full example that shows how to test an HTTP callout. The interface implementation ( `MockHttpResponseGenerator` ) is
listed first. It is followed by a class containing the test method and another containing the method that the test calls. The `testCallout`
test method sets the mock callout mode by calling `Test.setMock` before calling `getInfoFromExternalService` . It then
verifies that the response returned is what the implemented `respond` method sent. Save each class separately and run the test in
`CalloutClassTest` .

```
   @isTest

   global class MockHttpResponseGenerator implements HttpCalloutMock {

      // Implement this interface method

      global HTTPResponse respond(HTTPRequest req) {

        // Optionally, only send a mock response for a specific endpoint

        // and method.

        System.assertEquals('https://example.com/example/test', req.getEndpoint());

        System.assertEquals('GET', req.getMethod());

```


Apex Developer Guide Integration and Apex Utilities

```
        // Create a fake response

        HttpResponse res = new HttpResponse();

        res.setHeader('Content-Type', 'application/json');

        res.setBody('{"example":"test"}');

        res.setStatusCode(200);

        return res;

      }

   }

   public class CalloutClass {

      public static HttpResponse getInfoFromExternalService() {

        HttpRequest req = new HttpRequest();

        req.setEndpoint('https://example.com/example/test');

        req.setMethod('GET');

        Http h = new Http();

        HttpResponse res = h.send(req);

        return res;

      }

   }

   @isTest

   private class CalloutClassTest {

      @isTest static void testCallout() {

        // Set mock callout class

        Test.setMock(HttpCalloutMock.class, new MockHttpResponseGenerator());

        // Call method to test.

        // This causes a fake response to be sent

        // from the class that implements HttpCalloutMock.

        HttpResponse res = CalloutClass.getInfoFromExternalService();

        // Verify response received contains fake values

        String contentType = res.getHeader('Content-Type');

        System.assert(contentType == 'application/json');

        String actualValue = res.getBody();

        String expectedValue = '{"example":"test"}';

        System.assertEquals(actualValue, expectedValue);

        System.assertEquals(200, res.getStatusCode());

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: HttpCalloutMock Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_httpcalloutmock.htm)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm)_ : Test Class

####### Testing HTTP Callouts Using Static Resources

You can test HTTP callouts by specifying the body of the response you’d like to receive in a static resource and using one of two built-in
classes— `StaticResourceCalloutMock` or `MultiStaticResourceCalloutMock` .


Apex Developer Guide Integration and Apex Utilities

**Testing HTTP Callouts Using** **`StaticResourceCalloutMock`**

Apex provides the built-in `StaticResourceCalloutMock` class that you can use to test callouts by specifying the response
body in a static resource. When using this class, you don’t have to provide your own implementation of the `HttpCalloutMock`
interface. Instead, just create an instance of `StaticResourceCalloutMock` and set the static resource to use for the response
body, along with other response properties, like the status code and content type.

First, you must create a static resource from a text file to contain the response body:

**1.** Create a text file that contains the response body to return. The response body can be an arbitrary string, but it must match the
content type, if specified. For example, if your response has no content type specified, the file can include the arbitrary string _`abc`_ .
If you specify a content type of application/json for the response, the file content should be a JSON string, such as {"hah":"fooled
you"}.

**2.** Create a static resource for the text file:

**a.** From Setup, enter _`Static Resources`_ in the `Quick Find` box, then select **Static Resources** .

**b.** Click **New** .

**c.** Name your static resource.

**d.** Choose the file to upload.

**e.** Click **Save** .

To learn more about static resources, see “Defining Static Resources” in the Salesforce online help.

Next, create an instance of `StaticResourceCalloutMock` and set the static resource, and any other properties.

```
   StaticResourceCalloutMock mock = new StaticResourceCalloutMock();

   mock.setStaticResource('myStaticResourceName');

   mock.setStatusCode(200);

   mock.setHeader('Content-Type', 'application/json');

```

In your test method, call `Test.setMock` to set the mock callout mode and pass it `HttpCalloutMock.class` as the first
argument, and the variable name that you created for `StaticResourceCalloutMock` as the second argument.

```
   Test.setMock(HttpCalloutMock.class, mock );

```

After this point, if your test method performs a callout, the callout is not made and the Apex runtime sends the mock response you
specified in your instance of `StaticResourceCalloutMock` .

Note: To mock a callout if the code that performs the callout is in a managed package, call `Test.setMock` from a test method
in the same package with the same namespace.

This is a full example containing the test method ( `testCalloutWithStaticResources` ) and the method it is testing
( `getInfoFromExternalService` ) that performs the callout. Before running this example, create a static resource named
_`mockResponse`_ based on a text file with the content _`{"hah":"fooled you"}`_ . Save each class separately and run the test in
`CalloutStaticClassTest` .

```
   public class CalloutStaticClass {

      public static HttpResponse getInfoFromExternalService(String endpoint) {

        HttpRequest req = new HttpRequest();

        req.setEndpoint(endpoint);

        req.setMethod('GET');

        Http h = new Http();

        HttpResponse res = h.send(req);

        return res;

```


Apex Developer Guide Integration and Apex Utilities

```
      }

   }

   @isTest

   private class CalloutStaticClassTest {

      @isTest static void testCalloutWithStaticResources() {

        // Use StaticResourceCalloutMock built-in class to

        // specify fake response and include response body

        // in a static resource.

        StaticResourceCalloutMock mock = new StaticResourceCalloutMock();

        mock.setStaticResource('mockResponse');

        mock.setStatusCode(200);

        mock.setHeader('Content-Type', 'application/json');

        // Set the mock callout mode

        Test.setMock(HttpCalloutMock.class, mock);

        // Call the method that performs the callout

        HTTPResponse res = CalloutStaticClass.getInfoFromExternalService(

           'https://example.com/example/test');

        // Verify response received contains values returned by

        // the mock response.

        // This is the content of the static resource.

        System.assertEquals('{"hah":"fooled you"}', res.getBody());

        System.assertEquals(200,res.getStatusCode());

        System.assertEquals('application/json', res.getHeader('Content-Type'));

      }

   }

```

**Testing HTTP Callouts Using** **`MultiStaticResourceCalloutMock`**

Apex provides the built-in `MultiStaticResourceCalloutMock` class that you can use to test callouts by specifying the
response body in a static resource for each endpoint. This class is similar to `StaticResourceCalloutMock` except that it allows
you to specify multiple response bodies. When using this class, you don’t have to provide your own implementation of the
`HttpCalloutMock` interface. Instead, just create an instance of `MultiStaticResourceCalloutMock` and set the static
resource to use per endpoint. You can also set other response properties like the status code and content type.

First, you must create a static resource from a text file to contain the response body. See the procedure outlined in Testing HTTP Callouts
Using `StaticResourceCalloutMock` .

Next, create an instance of `MultiStaticResourceCalloutMock` and set the static resource, and any other properties.

```
   MultiStaticResourceCalloutMock multimock = new MultiStaticResourceCalloutMock();

   multimock.setStaticResource('https://example.com/example/test', 'mockResponse');

   multimock.setStaticResource('https://example.com/example/sfdc', 'mockResponse2');

   multimock.setStatusCode(200);

   multimock.setHeader('Content-Type', 'application/json');

```

In your test method, call `Test.setMock` to set the mock callout mode and pass it `HttpCalloutMock.class` as the first
argument, and the variable name that you created for `MultiStaticResourceCalloutMock` as the second argument.

```
   Test.setMock(HttpCalloutMock.class, multimock );

```


Apex Developer Guide Integration and Apex Utilities

After this point, if your test method performs an HTTP callout to one of the endpoints `https://example.com/example/test`
or `https://example.com/example/sfdc`, the callout is not made and the Apex runtime sends the corresponding mock
response you specified in your instance of `MultiStaticResourceCalloutMock` .

This is a full example containing the test method ( `testCalloutWithMultipleStaticResources` ) and the method it is
testing ( `getInfoFromExternalService` ) that performs the callout. Before running this example, create a static resource named
_`mockResponse`_ based on a text file with the content _`{"hah":"fooled you"}`_ and another named _`mockResponse2`_
based on a text file with the content _`{"hah":"fooled you twice"}`_ . Save each class separately and run the test in
`CalloutMultiStaticClassTest` .

```
   public class CalloutMultiStaticClass {

      public static HttpResponse getInfoFromExternalService(String endpoint) {

        HttpRequest req = new HttpRequest();

        req.setEndpoint(endpoint);

        req.setMethod('GET');

        Http h = new Http();

        HttpResponse res = h.send(req);

        return res;

      }

   }

   @isTest

   private class CalloutMultiStaticClassTest {

      @isTest static void testCalloutWithMultipleStaticResources() {

        // Use MultiStaticResourceCalloutMock to

        // specify fake response for a certain endpoint and

        // include response body in a static resource.

        MultiStaticResourceCalloutMock multimock = new MultiStaticResourceCalloutMock();

        multimock.setStaticResource(

           'https://example.com/example/test', 'mockResponse');

        multimock.setStaticResource(

           'https://example.com/example/sfdc', 'mockResponse2');

        multimock.setStatusCode(200);

        multimock.setHeader('Content-Type', 'application/json');

        // Set the mock callout mode

        Test.setMock(HttpCalloutMock.class, multimock);

        // Call the method for the first endpoint

        HTTPResponse res = CalloutMultiStaticClass.getInfoFromExternalService(

           'https://example.com/example/test');

        // Verify response received

        System.assertEquals('{"hah":"fooled you"}', res.getBody());

        // Call the method for the second endpoint

        HTTPResponse res2 = CalloutMultiStaticClass.getInfoFromExternalService(

           'https://example.com/example/sfdc');

        // Verify response received

        System.assertEquals('{"hah":"fooled you twice"}', res2.getBody());

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

####### Performing DML Operations and Mock Callouts

By default, callouts aren’t allowed after DML operations in the same transaction because DML operations result in pending uncommitted
work that prevents callouts from executing. Sometimes, you might want to insert test data in your test method using DML before making
a callout. To enable this, enclose the portion of your code that performs the callout within `Test.startTest` and `Test.stopTest`
statements. The `Test.startTest` statement must appear before the `Test.setMock` statement. Also, the calls to DML operations
must not be part of the `Test.startTest` / `Test.stopTest` block.

DML operations that occur after mock callouts are allowed and don’t require any changes in test methods.

The DML operations support works for all implementations of mock callouts using: the `HttpCalloutMock` interface and static
resources ( `StaticResourceCalloutMock` or `MultiStaticResourceCalloutMock` ). The following example uses an
implemented `HttpCalloutMock` interface but you can apply the same technique when using static resources.

**Performing DML Before Mock Callouts**

This example is based on the HttpCalloutMock example provided earlier. The example shows how to use `Test.startTest` and
`Test.stopTest` statements to allow DML operations to be performed in a test method before mock callouts. The test method
( `testCallout` ) first inserts a test account, calls `Test.startTest`, sets the mock callout mode using `Test.setMock`, calls a
method that performs the callout, verifies the mock response values, and finally, calls `Test.stopTest` .

```
   @isTest

   private class CalloutClassTest {

      @isTest static void testCallout() {

        // Perform some DML to insert test data

        Account testAcct = new Account('Test Account');

        insert testAcct;

        // Call Test.startTest before performing callout

        // but after setting test data.

        Test.startTest();

        // Set mock callout class

        Test.setMock(HttpCalloutMock.class, new MockHttpResponseGenerator());

        // Call method to test.

        // This causes a fake response to be sent

        // from the class that implements HttpCalloutMock.

        HttpResponse res = CalloutClass.getInfoFromExternalService();

        // Verify response received contains fake values

        String contentType = res.getHeader('Content-Type');

        System.assert(contentType == 'application/json');

        String actualValue = res.getBody();

        String expectedValue = '{"example":"test"}';

        System.assertEquals(actualValue, expectedValue);

        System.assertEquals(200, res.getStatusCode());

        Test.stopTest();

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

**Asynchronous Apex and Mock Callouts**

Similar to DML, asynchronous Apex operations result in pending uncommitted work that prevents callouts from being performed later
in the same transaction. Examples of asynchronous Apex operations are calls to future methods, batch Apex, or scheduled Apex. These
asynchronous calls are typically enclosed within `Test.startTest` and `Test.stopTest` statements in test methods so that
they execute after `Test.stopTest` . In this case, mock callouts can be performed after the asynchronous calls and no changes are
necessary. But if the asynchronous calls aren’t enclosed within `Test.startTest` and `Test.stopTest` statements, you’ll get
an exception because of uncommitted work pending. To prevent this exception, do either of the following:

**•** Enclose the asynchronous call within `Test.startTest` and `Test.stopTest` statements.

```
     Test.startTest();

     MyClass.asyncCall();

     Test.stopTest();

     Test.setMock(..); // Takes two arguments

     MyClass.mockCallout();

```

**•** Follow the same rules as with DML calls: Enclose the portion of your code that performs the callout within `Test.startTest`
and `Test.stopTest` statements. The `Test.startTest` statement must appear before the `Test.setMock` statement.
Also, the asynchronous calls must not be part of the `Test.startTest` / `Test.stopTest` block.

```
     MyClass.asyncCall();

     Test.startTest();

     Test.setMock(..); // Takes two arguments

     MyClass.mockCallout();

     Test.stopTest();

```

Asynchronous calls that occur after mock callouts are allowed and don’t require any changes in test methods.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm)_ : Test Class

##### Using Certificates

To use two-way SSL authentication, send a certificate with your callout that was either generated in Salesforce or signed by a certificate
authority (CA). Sending a certificate enhances security because the target of the callout receives the certificate and can use it to authenticate
the request against its keystore.

To enable two-way SSL authentication for a callout:

**1.** Generate a certificate.

**2.** Integrate the certificate with your code. See Using Certificates with SOAP Services and Using Certificates with HTTP Requests.

**3.** If you’re connecting to a third party and using a self-signed certificate, share the Salesforce certificate with them so that they can
add the certificate to their keystore. If you’re connecting to another application, generate and integrate the certificate with your
code, and then ensure that the Web or application server is configured to accept the certificate. This process depends on the type
of Web or application server you use.

**4.** Configure the remote site settings for the callout. Before any Apex callout can call an external site, that site must be registered in
the Remote Site Settings page, or the callout fails.

If the callout specifies a named credential as the endpoint, you don’t need to configure remote site settings. To set up named
[credentials, see Named Credentials and External Credentials in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.nc_named_creds_and_ext_creds.htm&language=en_US)


Apex Developer Guide Integration and Apex Utilities

###### 1. Generating Certificates 2. Using Certificates with SOAP Services

To support two-way authentication for a callout to a SOAP web service, generate a certificate in Salesforce or import a key pair from
a keystore into Salesforce. Then integrate the certificate with your Apex.

###### 3. Using Certificates with HTTP Requests Generating Certificates

You can use a self-signed certificate generated in Salesforce or a certificate signed by a certificate authority (CA). To generate a certificate
[for a callout, see Generate a Certificate.](https://help.salesforce.com/apex/HTViewHelpDoc?id=security_keys_creating.htm&language=en_US)

After you successfully save a Salesforce certificate, the certificate and corresponding keys are automatically generated.

After you create a CA-signed certificate, you must upload the signed certificate before you can use it. See “Generate a Certificate Signed
by a Certificate Authority” in the Salesforce online help.

###### Using Certificates with SOAP Services

To support two-way authentication for a callout to a SOAP web service, generate a certificate in Salesforce or import a key pair from a
keystore into Salesforce. Then integrate the certificate with your Apex.

Important: We recommend storing mutual authentication certificates for external web services in a Java keystore. For more
[information, see Certificates and Keys.](https://help.salesforce.com/articleView?id=security_keys_about.htm&language=en_US)

To integrate the certificate with your Apex:

**1.** Receive the WSDL for the web service from the third party, or generate it from the application you want to connect to.

**2.** Generate Apex classes from the WSDL for the web service. See SOAP Services: Defining a Class from a WSDL Document.

**3.** The generated Apex classes include a stub for calling the third-party web service represented by the WSDL document. Edit the Apex
classes, and assign a value to a `clientCertName_x` variable on an instance of the stub class. The value must match the `Unique`
`Name` of the certificate that you generated on the Certificate and Key Management page.

This example illustrates editing the Apex classes and works with the sample WSDL file in Generated WSDL2Apex Code. The example
assumes that you generated a certificate with the `Unique Name` of `DocSampleCert` .

```
   docSample.DocSamplePort stub = new docSample.DocSamplePort();

   stub.clientCertName_x = 'DocSampleCert';

   String input = 'This is the input string';

   String output = stub.EchoString(input);

###### Using Certificates with HTTP Requests

```

After you have generated a certificate in Salesforce, you can use it to support two-way authentication for a callout to an HTTP request.

To integrate the certificate with your Apex:

**1.** Generate a certificate. Note the `Unique Name` of the certificate.

**2.** In your Apex, use the `setClientCertificateName` method of the `HttpRequest` class. The value used for the argument
for this method must match the `Unique Name` of the certificate that you generated in the previous step.


Apex Developer Guide Integration and Apex Utilities

The following example illustrates the last step of the previous procedure. This example assumes that you previously generated a certificate
with a `Unique Name` of `DocSampleCert` .

```
   HttpRequest req = new HttpRequest();

   req.setClientCertificateName('DocSampleCert');

##### Callout Limits and Limitations

```

The following limits and limitations apply when Apex code makes a callout to an HTTP request or a web services call. The web services
call can be a SOAP API call or any external web services call.

**•** A single Apex transaction can make a maximum of 100 callouts to an HTTP request or an API call.

**•** In Developer Edition orgs, you can only make up to 20 concurrent callouts to endpoints outside of your Salesforce org’s domain.
This limit doesn’t apply to non-Developer Edition orgs.

**•** The default timeout is 10 seconds. A custom timeout can be defined for each callout. The minimum is 1 millisecond and the maximum
is 120,000 milliseconds. See the examples in the next section for how to set custom timeouts for Web services or HTTP callouts.

**•** The maximum cumulative timeout for callouts by a single Apex transaction is 120 seconds. This time is additive across all callouts
invoked by the Apex transaction.

**•** Every org has a limit on long-running requests that run for more than 5 seconds (total execution time). HTTP callout processing time
is not included when calculating this limit. We pause the timer for the callout and resume it when the callout completes. See Execution
Governors and Limits for Lightning Platform Apex limits.

**•** You can’t make a callout when there are pending operations in the same transaction. Things that result in pending operations are
DML statements, asynchronous Apex (such as future methods and batch Apex jobs), scheduled Apex, or sending email. You can
make callouts before performing these types of operations.

**•** Pending operations can occur before mock callouts in the same transaction. See Performing DML Operations and Mock Callouts for
WSDL-based callouts or Performing DML Operations and Mock Callouts for HTTP callouts.

**•** When the header `Expect: 100-Continue` is added to a callout request and a `HTTP/1.1 100 Continue` response
isn’t returned by the external server, a timeout occurs.

Apex Callouts in Read-Only Mode

During read-only mode, Apex callouts to external services execute and aren’t blocked by the system. Typically, you execute some
follow-up operations in the same transaction after receiving a response from a callout. For example, you can make a DML call to update
a Salesforce record. But write operations in Salesforce, such as record updates, are blocked during read-only mode. This inconsistency
in behavior in read-only mode can break your program flow and causes issues. To avoid incorrect program behavior, we recommend
that you prevent making callouts in read-only mode. To check whether the org is in read-only mode, call
`System.getApplicationReadWriteMode()` .

The following example checks the return value of `System.getApplicationReadWriteMode()` . If the return value is equal
to `ApplicationReadWriteMode.READ_ONLY` enum value, the org is in read-only mode and the callout is skipped. Otherwise
( `ApplicationReadWriteMode.DEFAULT` value), the callout is performed.

Note: This class uses Apex HTTP classes to make a callout as an example. You can also make a callout using an imported WSDL
through WSDL2Apex. The process for checking for read-only mode is the same in either case.

```
   public class HttpCalloutSampleReadOnly {

      public class MyReadOnlyException extends Exception {}

      // Pass in the endpoint to be used using the string url

      public String getCalloutResponseContents(String url) {

```


Apex Developer Guide Integration and Apex Utilities

```
        // Get Read-only mode status

        ApplicationReadWriteMode mode = System.getApplicationReadWriteMode();

        String returnValue = '';

        if (mode == ApplicationReadWriteMode.READ_ONLY) {

           // Prevent the callout

           throw new MyReadOnlyException('Read-only mode. Skipping callouts!');

        } else if (mode == ApplicationReadWriteMode.DEFAULT) {

           // Instantiate a new http object

           Http h = new Http();

           // Instantiate a new HTTP request, specify the method (GET)

           // as well as the endpoint.

           HttpRequest req = new HttpRequest();

           req.setEndpoint(url);

           req.setMethod('GET');

           // Send the request, and return a response

           HttpResponse res = h.send(req);

           returnValue = res.getBody();

        }

        return returnValue;

      }

   }

```

Your Salesforce org is in read-only mode during some Salesforce maintenance activities, such as planned site switches and instance
refreshes. As part of Continuous Site Switching, your Salesforce org is switched to its ready site approximately once every six months.
[For more information about site switching, see Continuous Site Switching.](https://help.salesforce.com/articleView?id=Continuous-Site-Switching&type=1&language=en_US)

To test read-only mode in sandbox, contact Salesforce to enable the read-only mode test option. Once the test option is enabled, you
can toggle read-only mode on and verify your apps.

Setting Callout Timeouts

The following example sets a custom timeout for Web services callouts. The example works with the sample WSDL file and the generated
`DocSamplePort` class described in Generated WSDL2Apex Code on page 613. Set the timeout value in milliseconds by assigning a
value to the special `timeout_x` variable on the stub.

```
   docSample.DocSamplePort stub = new docSample.DocSamplePort();

   stub.timeout_x = 2000; // timeout in milliseconds

```

The following is an example of setting a custom timeout for HTTP callouts:

```
   HttpRequest req = new HttpRequest();

   req.setTimeout(2000); // timeout in milliseconds

##### Make Long-Running Callouts with Continuations

```

Use asynchronous callouts to make long-running requests from a Visualforce page or a Lightning component to an external Web service
and process responses in callback methods.

An asynchronous callout is a callout that is made from a Visualforce page or a Lightning component for which the response is returned
through a callback method. An asynchronous callout is also referred to as a _continuation_ .


Apex Developer Guide Integration and Apex Utilities

Visualforce Example

This diagram shows the execution path of an asynchronous callout, starting from a Visualforce page. A user invokes an action on a
Visualforce page that requests information from a Web service (step 1). The app server hands the callout request to the Continuation
server before returning to the Visualforce page (steps 2–3). The Continuation server sends the request to the Web service and receives
the response (steps 4–7), then hands the response back to the app server (step 8). Finally, the response is returned to the Visualforce
page (step 9).

**Execution Flow of an Asynchronous Callout**

A typical Salesforce application that benefits from asynchronous callouts contains a Visualforce page with a button. Users click that
button to get data from an external Web service. For example, a Visualforce page that gets warranty information for a certain product
from a Web service. Thousands of agents in the organization can use this page. Therefore, a hundred of those agents can click the same
button to process warranty information for products at the same time. These hundred simultaneous actions exceed the limit of concurrent
long-running requests on page 349 . But by using asynchronous callouts, the requests aren’t subjected to this limit and can be executed.

In the following example application, the button action is implemented in an Apex controller method. The action method creates a
`Continuation` and returns it. After the request is sent to the service, the Visualforce request is suspended. The user must wait for
the response to be returned before proceeding with using the page and invoking new actions. When the external service returns a
response, the Visualforce request resumes and the page receives this response.

This is the Visualforce page of our sample application. This page contains a button that invokes the `startRequest` method of the
controller that’s associated with this page. After the continuation result is returned and the callback method is invoked, the button
renders the `outputText` component again to display the body of the response.

```
   <apex:page controller="ContinuationController" showChat="false" showHeader="false">

     <apex:form >

       <!-- Invokes the action method when the user clicks this button. -->

       <apex:commandButton action="{!startRequest}"

            value="Start Request" reRender="result"/>

     </apex:form>

     <!-- This output text component displays the callout response body. -->

     <apex:outputText id="result" value="{!result}" />

   </apex:page>

```

The following is the Apex controller that’s associated with the Visualforce page. This controller contains the action and callback methods.


Apex Developer Guide Integration and Apex Utilities

Note: Before you can call an external service, you must add the remote site to a list of authorized remote sites in the Salesforce
user interface. From Setup, enter _`Remote Site Settings`_ in the `Quick Find` box, then select **Remote Site Settings**,
and then click **New Remote Site** .

If the callout specifies a named credential as the endpoint, you don’t need to configure remote site settings. A named credential
specifies the URL of a callout endpoint and its required authentication parameters in one definition. To set up named credentials,
see Define a Named Credential in Salesforce Help. In your code, specify the named credential URL instead of the long-running
service URL. A named credential URL contains the scheme `callout:`, the name of the named credential, and an optional path.
For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ .

```
   public with sharing class ContinuationController {

      // Unique label corresponding to the continuation

      public String requestLabel;

      // Result of callout

      public String result {get;set;}

      // Callout endpoint as a named credential URL

      // or, as shown here, as the long-running service URL

      private static final String LONG_RUNNING_SERVICE_URL =

        '<Insert your service URL>';

     // Action method

      public Object startRequest() {

       // Create continuation with a timeout

       Continuation con = new Continuation(40);

       // Set callback method

       con.continuationMethod='processResponse';

       // Create callout request

       HttpRequest req = new HttpRequest();

       req.setMethod('GET');

       req.setEndpoint(LONG_RUNNING_SERVICE_URL);

       // Add callout request to continuation

       this.requestLabel = con.addHttpRequest(req);

       // Return the continuation

       return con;

      }

      // Callback method

      public Object processResponse() {

       // Get the response by using the unique label

       HttpResponse response = Continuation.getResponse(this.requestLabel);

       // Set the result variable that is displayed on the Visualforce page

       this.result = response.getBody();

       // Return null to re-render the original Visualforce page

       return null;

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

Note:

**•** You can make up to three asynchronous callouts in a single continuation. Add these callout requests to the same continuation
by using the `addHttpRequest` method of the `Continuation` class. The callouts run in parallel for this continuation
and suspend the Visualforce request. Only after the external service returns all callouts, the Visualforce process resumes.

**•** Asynchronous callouts are supported only through a Visualforce page. Making an asynchronous callout by invoking the action
method outside a Visualforce page, such as in the Developer Console, isn’t supported.

**•** Asynchronous callouts are available for Apex controllers and Visualforce pages saved in version 30.0 and later. If JavaScript
remoting is used, version 31.0 or later is required.

**•** Asynchronous callouts, including callouts that specify named credentials as the callout endpoint, aren’t supported over Private
Connect.

###### Process for Using Asynchronous Callouts

To use asynchronous callouts, create a `Continuation` object in an action method of a controller, and implement a callback
method.

Testing Asynchronous Callouts
Write tests to test your controller and meet code coverage requirements for deploying or packaging Apex. Because Apex tests don’t
support making callouts, you can simulate callout requests and responses. When you’re simulating a callout, the request doesn’t
get sent to the external service, and a mock response is used.

Asynchronous Callout Limits
When a continuation is executing, the continuation-specific limits apply. When the continuation returns and the request resumes,
a new Apex transaction starts. All Apex and Visualforce limits apply and are reset in the new transaction, including the Apex callout
limits.

Making Multiple Asynchronous Callouts
To make multiple callouts to a long-running service simultaneously from a Visualforce page, you can add up to three requests to
the Continuation instance. An example of when to make simultaneous callouts is when you’re making independent requests to a
service, such as getting inventory statistics for two products.

Chaining Asynchronous Callouts
If the order of the callouts matters, or when a callout is conditional on the response of another callout, you can chain callout requests.
Chaining callouts means that the next callout is made only after the response of the previous callout returns. For example, you might
need to chain a callout to get warranty extension information after the warranty service response indicates that the warranty expired.
You can chain up to three callouts.

Making an Asynchronous Callout from an Imported WSDL
In addition to `HttpRequest` -based callouts, asynchronous callouts are supported in Web service calls that are made from
WSDL-generated classes. The process of making asynchronous callouts from a WSDL-generated class is similar to the process for
using the `HttpRequest` class.

SEE ALSO:

Named Credentials as Callout Endpoints

_Lightning Web Components Developer Guide_ [: Make Long-Running Callouts with Continuations](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.apex_continuations)

###### Process for Using Asynchronous Callouts

To use asynchronous callouts, create a `Continuation` object in an action method of a controller, and implement a callback method.


Apex Developer Guide Integration and Apex Utilities

Invoking an Asynchronous Callout in an Action Method

To invoke an asynchronous callout, call the external service by using a `Continuation` instance in your Visualforce action method.
When you create a continuation, you can specify a timeout value and the name of the callback method. For example, the following
creates a continuation with a 60-second timeout and a callback method name of `processResponse` .

```
   Continuation cont = new Continuation(60);

   cont.continuationMethod = 'processResponse';

```

Next, associate the `Continuation` object to an external callout. To do so, create the HTTP request, and then add this request to the
continuation as follows:

```
   String requestLabel = cont.addHttpRequest(request);

```

Note: This process is based on making callouts with the HttpRequest class. For an example that uses a WSDL-based class, see
Making an Asynchronous Callout from an Imported WSDL.

The method that invokes the callout (the action method) must return the `Continuation` object to instruct Visualforce to suspend
the current request after the system sends the callout and waits for the callout response. The `Continuation` object holds the details
of the callout to be executed.

This is the signature of the method that invokes the callout. The Object return type represents a `Continuation` .

```
   public Object calloutActionMethodName ()

```

Defining a Callback Method

The response is returned after the external service finishes processing the callout. You can specify a callback method for asynchronous
execution after the callout returns. This callback method must be defined in the controller class where the callout invocation method is
defined. You can define a callback method to process the returned response, such as retrieving the response for display on a Visualforce
page.

The callback method doesn’t take any arguments and has this signature.

```
   public Object callbackMethodName ()

```

The Object return type represents a `Continuation`, a `PageReference`, or `null` . To render the original Visualforce page and
finish the Visualforce request, return `null` in the callback method.

If the action method uses JavaScript remoting (is annotated with `@RemoteAction` ), the callback method must be static and has the
following supported signatures.

```
   public static Object callbackMethodName (List< String> labels, Object state )

```

Or:

```
   public static Object callbackMethodName (Object state )

```

The _`labels`_ parameter is supplied by the system when it invokes the callback method and holds the labels associated with the callout
requests made. The _`state`_ [parameter is supplied by setting the Continuation.state property in the controller.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Continuation.htm#apex_System_Continuation_state)

This table lists the return values for the callback method. Each return value corresponds to a different behavior.

**Table 10: Possible Return Values for the Callback Method**


Apex Developer Guide Integration and Apex Utilities

Note: If the `continuationMethod` property isn’t set for a continuation, the same action method that made the callout is
called again when the callout response returns.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Continuation.htm)_ : Continuation Class

###### Testing Asynchronous Callouts

Write tests to test your controller and meet code coverage requirements for deploying or packaging Apex. Because Apex tests don’t
support making callouts, you can simulate callout requests and responses. When you’re simulating a callout, the request doesn’t get
sent to the external service, and a mock response is used.

The following example shows how to invoke a mock asynchronous callout in a test for a Web service call that uses `HTTPRequest` .
###### To simulate callouts in continuations, call these methods of the Test class: Test.setContinuationResponse() and

[Test.invokeContinuationMethod().](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm#apex_System_Test_invokeContinuationMethod)

The controller class to test is listed first, followed by the test class. The controller class from Make Long-Running Callouts with Continuations
is reused here.

```
public with sharing class ContinuationController {

   // Unique label corresponding to the continuation request

   public String requestLabel;

   // Result of callout

   public String result {get;set;}

   // Endpoint of long-running service

   private static final String LONG_RUNNING_SERVICE_URL =

     '<Insert your service URL>';

  // Action method

   public Object startRequest() {

    // Create continuation with a timeout

    Continuation con = new Continuation(40);

    // Set callback method

    con.continuationMethod='processResponse';

    // Create callout request

    HttpRequest req = new HttpRequest();

    req.setMethod('GET');

    req.setEndpoint(LONG_RUNNING_SERVICE_URL);

```


Apex Developer Guide Integration and Apex Utilities

```
       // Add callout request to continuation

       this.requestLabel = con.addHttpRequest(req);

       // Return the continuation

       return con;

      }

      // Callback method

      public Object processResponse() {

       // Get the response by using the unique label

       HttpResponse response = Continuation.getResponse(this.requestLabel);

       // Set the result variable that is displayed on the Visualforce page

       this.result = response.getBody();

       // Return null to re-render the original Visualforce page

       return null;

      }

   }

```

This example shows the test class corresponding to the controller. This test class contains a test method for testing an asynchronous
callout. In the test method, `Test.setContinuationResponse` sets a mock response, and
`Test.invokeContinuationMethod` causes the callback method for the continuation to be executed. The test ensures that
the callback method processed the mock response by verifying that the controller’s result variable is set to the expected response.

```
   @isTest

   public class ContinuationTestingForHttpRequest {

      public static testmethod void testWebService() {

        ContinuationController controller = new ContinuationController();

        // Invoke the continuation by calling the action method

        Continuation conti = (Continuation)controller.startRequest();

        // Verify that the continuation has the proper requests

        Map<String, HttpRequest> requests = conti.getRequests();

        system.assert(requests.size() == 1);

        system.assert(requests.get(controller.requestLabel) != null);

        // Perform mock callout

        // (i.e. skip the callout and call the callback method)

        HttpResponse response = new HttpResponse();

        response.setBody('Mock response body');

        // Set the fake response for the continuation

        Test.setContinuationResponse(controller.requestLabel, response);

        // Invoke callback method

        Object result = Test.invokeContinuationMethod(controller, conti);

        // result is the return value of the callback

        System.assertEquals(null, result);

        // Verify that the controller's result variable

        // is set to the mock response.

        System.assertEquals('Mock response body', controller.result);

      }

   }

```


Apex Developer Guide Integration and Apex Utilities

###### Asynchronous Callout Limits

When a continuation is executing, the continuation-specific limits apply. When the continuation returns and the request resumes, a
new Apex transaction starts. All Apex and Visualforce limits apply and are reset in the new transaction, including the Apex callout limits.

Continuation-Specific Limits

The following are Apex and Visualforce limits that are specific to a continuation.

**Description** **Limit**

Maximum number of parallel Apex callouts in a single continuation 3

Maximum number of chained Apex callouts 3

Maximum timeout for a single continuation [1] 120 seconds

Maximum Visualforce controller-state size [2] 80 KB

Maximum HTTP response size 1 MB

Maximum HTTP POST form size—the size of all keys and values in the form [3] 1 MB

Maximum number of keys in the HTTP POST form [3] 500

1 The timeout that is specified in the autogenerated Web service stub and in the HttpRequest objects is ignored. Only this timeout limit
is enforced for a continuation.

2 When the continuation is executed, the Visualforce controller is serialized. When the continuation is completed, the controller is
deserialized and the callback is invoked. Use the Apex `transient` modifier to designate a variable that is not to be serialized. The
framework uses only serialized members when it resumes. The controller-state size limit is separate from the view state limit. See
Differences Between Continuation Controller State and Visualforce View State.

3 This limit is for HTTP POST forms with the following content type headers:
`content-type='application/x-www-form-urlencoded'` and `content-type='multipart/form-data'`

Differences Between Continuation Controller State and Visualforce View State

Controller state and view state are distinct. Controller state for a continuation consists of the serialization of all controllers that are involved
in the request, not only the controller that invokes the continuation. The serialized controllers include controller extensions, and custom
and internal component controllers. The controller state size is logged in the debug log as a `USER_DEBUG` event.

View state holds more data than the controller state and has a higher maximum size (170KB). The view state contains state and component
structure. State is serialization of all controllers and all the attributes of each component on a page, including subpages and subcomponents
. Component structure is the parent-child relationship of components that are in the page. You can monitor the view state size in the
Developer Console or in the footer of a Visualforce page when development mode is enabled. For more information, see “View State
[Tab” in the Salesforce Help or refer to the Visualforce Developer’s Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

###### Making Multiple Asynchronous Callouts

To make multiple callouts to a long-running service simultaneously from a Visualforce page, you can add up to three requests to the
Continuation instance. An example of when to make simultaneous callouts is when you’re making independent requests to a service,
such as getting inventory statistics for two products.


Apex Developer Guide Integration and Apex Utilities

When you’re making multiple callouts in the same continuation, the callout requests run in parallel and suspend the Visualforce request.
Only after all callout responses are returned does the Visualforce process resume.

The following Visualforce and Apex examples show how to make two asynchronous callouts simultaneously by using a single continuation.
The Visualforce page is shown first. The Visualforce page contains a button that invokes the action method
`startRequestsInParallel` in the controller. When the Visualforce process resumes, the `outputPanel` component is
rendered again. This panel displays the responses of the two asynchronous callouts.

```
   <apex:page controller="MultipleCalloutController" showChat="false" showHeader="false">

     <apex:form >

       <!-- Invokes the action method when the user clicks this button. -->

       <apex:commandButton action="{!startRequestsInParallel}" value="Start Request"

   reRender="panel"/>

     </apex:form>

     <apex:outputPanel id="panel">

        <!-- Displays the response body of the initial callout. -->

        <apex:outputText value="{!result1}" />

        <br/>

        <!-- Displays the response body of the chained callout. -->

        <apex:outputText value="{!result2}" />

     </apex:outputPanel>

   </apex:page>

```

This example shows the controller class for the Visualforce page. The `startRequestsInParallel` method adds two requests
to the Continuation. After all callout responses are returned, the callback method ( `processAllResponses` ) is invoked and processes
the responses.

```
   public with sharing class MultipleCalloutController {

      // Unique label for the first request

      public String requestLabel1;

      // Unique label for the second request

      public String requestLabel2;

      // Result of first callout

      public String result1 {get;set;}

     // Result of second callout

      public String result2 {get;set;}

      // Endpoints of long-running service

      private static final String LONG_RUNNING_SERVICE_URL1 =

        '<Insert your first service URL>';

      private static final String LONG_RUNNING_SERVICE_URL2 =

        '<Insert your second service URL>';

      // Action method

      public Object startRequestsInParallel() {

       // Create continuation with a timeout

       Continuation con = new Continuation(60);

       // Set callback method

       con.continuationMethod='processAllResponses';

       // Create first callout request

       HttpRequest req1 = new HttpRequest();

```


Apex Developer Guide Integration and Apex Utilities

```
       req1.setMethod('GET');

       req1.setEndpoint(LONG_RUNNING_SERVICE_URL1);

       // Add first callout request to continuation

       this.requestLabel1 = con.addHttpRequest(req1);

       // Create second callout request

       HttpRequest req2 = new HttpRequest();

       req2.setMethod('GET');

       req2.setEndpoint(LONG_RUNNING_SERVICE_URL2);

       // Add second callout request to continuation

       this.requestLabel2 = con.addHttpRequest(req2);

       // Return the continuation

       return con;

      }

      // Callback method.

      // Invoked only when responses of all callouts are returned.

      public Object processAllResponses() {

       // Get the response of the first request

       HttpResponse response1 = Continuation.getResponse(this.requestLabel1);

       this.result1 = response1.getBody();

       // Get the response of the second request

       HttpResponse response2 = Continuation.getResponse(this.requestLabel2);

       this.result2 = response2.getBody();

       // Return null to re-render the original Visualforce page

       return null;

      }

   }

###### Chaining Asynchronous Callouts

```

If the order of the callouts matters, or when a callout is conditional on the response of another callout, you can chain callout requests.
Chaining callouts means that the next callout is made only after the response of the previous callout returns. For example, you might
need to chain a callout to get warranty extension information after the warranty service response indicates that the warranty expired.
You can chain up to three callouts.

The following Visualforce and Apex examples show how to chain one callout to another. The Visualforce page is shown first. The Visualforce
page contains a button that invokes the action method `invokeInitialRequest` in the controller. The Visualforce process is
suspended each time a continuation is returned. The Visualforce process resumes after each response is returned and renders each
response in the `outputPanel` component.

```
   <apex:page controller="ChainedContinuationController" showChat="false" showHeader="false">

     <apex:form >

       <!-- Invokes the action method when the user clicks this button. -->

       <apex:commandButton action="{!invokeInitialRequest}" value="Start Request"

   reRender="panel"/>

     </apex:form>

```


Apex Developer Guide Integration and Apex Utilities

```
     <apex:outputPanel id="panel">

        <!-- Displays the response body of the initial callout. -->

        <apex:outputText value="{!result1}" />

        <br/>

        <!-- Displays the response body of the chained callout. -->

        <apex:outputText value="{!result2}" />

     </apex:outputPanel>

   </apex:page>

```

This example show the controller class for the Visualforce page. The `invokeInitialRequest` method creates the first continuation.
The callback method ( `processInitialResponse` ) processes the response of the first callout. If this response meets a certain
condition, the method chains another callout by returning a second continuation. After the response of the chained continuation is
returned, the second callback method ( `processChainedResponse` ) is invoked and processes the second response.

```
   public with sharing class ChainedContinuationController {

      // Unique label for the initial callout request

      public String requestLabel1;

      // Unique label for the chained callout request

      public String requestLabel2;

      // Result of initial callout

      public String result1 {get;set;}

      // Result of chained callout

      public String result2 {get;set;}

      // Endpoint of long-running service

      private static final String LONG_RUNNING_SERVICE_URL1 =

        '<Insert your first service URL>';

      private static final String LONG_RUNNING_SERVICE_URL2 =

        '<Insert your second service URL>';

      // Action method

      public Object invokeInitialRequest() {

       // Create continuation with a timeout

       Continuation con = new Continuation(60);

       // Set callback method

       con.continuationMethod='processInitialResponse';

       // Create first callout request

       HttpRequest req = new HttpRequest();

       req.setMethod('GET');

       req.setEndpoint(LONG_RUNNING_SERVICE_URL1);

       // Add initial callout request to continuation

       this.requestLabel1 = con.addHttpRequest(req);

       // Return the continuation

       return con;

      }

      // Callback method for initial request

      public Object processInitialResponse() {

       // Get the response by using the unique label

```


Apex Developer Guide Integration and Apex Utilities

```
       HttpResponse response = Continuation.getResponse(this.requestLabel1);

       // Set the result variable that is displayed on the Visualforce page

       this.result1 = response.getBody();

       Continuation chainedContinuation = null;

       // Chain continuation if some condition is met

       if (response.getBody().toLowerCase().contains('expired')) {

         // Create a second continuation

         chainedContinuation = new Continuation(60);

         // Set callback method

         chainedContinuation.continuationMethod='processChainedResponse';

         // Create callout request

         HttpRequest req = new HttpRequest();

         req.setMethod('GET');

         req.setEndpoint(LONG_RUNNING_SERVICE_URL2);

         // Add callout request to continuation

         this.requestLabel2 = chainedContinuation.addHttpRequest(req);

       }

       // Start another continuation

       return chainedContinuation;

      }

      // Callback method for chained request

      public Object processChainedResponse() {

       // Get the response for the chained request

       HttpResponse response = Continuation.getResponse(this.requestLabel2);

       // Set the result variable that is displayed on the Visualforce page

       this.result2 = response.getBody();

       // Return null to re-render the original Visualforce page

       return null;

      }

   }

```

Note: The response of a continuation must be retrieved before you create a new continuation and before the Visualforce request
is suspended again. You can’t retrieve an old response from an earlier continuation in the chain of continuations.

###### Making an Asynchronous Callout from an Imported WSDL

In addition to `HttpRequest` -based callouts, asynchronous callouts are supported in Web service calls that are made from
WSDL-generated classes. The process of making asynchronous callouts from a WSDL-generated class is similar to the process for using
the `HttpRequest` class.

When you import a WSDL in Salesforce, Salesforce autogenerates two Apex classes for each namespace in the imported WSDL. One
class is the service class for the synchronous service, and the other is a modified version for the asynchronous service. The autogenerated
asynchronous class name starts with the `Async` prefix and has the format `Async` _`ServiceName`_ . _`ServiceName`_ is the name of
the original unmodified service class. The asynchronous class differs from the standard class in the following ways.

**•** The public service methods contain an extra `Continuation` parameter as the first parameter.

**•** The Web service operations are invoked asynchronously and their responses are obtained with the `getValue` method of the
response element.


Apex Developer Guide Integration and Apex Utilities

**•** The `WebServiceCallout.beginInvoke` and `WebServiceCallout.endInvoke` are used to invoke the service
and get the response respectively.

You can generate Apex classes from a WSDL in the Salesforce user interface. From Setup, enter **Apex Classes** in the `Quick Find`
box, then select **Apex Classes** .

To make asynchronous Web service callouts, call the methods on the autogenerated asynchronous class by passing your `Continuation`
instance to these methods. The following example is based on a hypothetical stock-quote service. This example assumes that the
organization has a class, called `AsyncSOAPStockQuoteService`, that was autogenerated via a WSDL import. The example shows
how to make an asynchronous callout to the service by using the autogenerated `AsyncSOAPStockQuoteService` class. First,
this example creates a continuation with a 60-second timeout and sets the callback method. Next, the code example invokes the
`beginStockQuote` method by passing it the Continuation instance. The `beginStockQuote` method call corresponds to an
asynchronous callout execution.

```
   public Continuation startRequest() {

     Integer TIMEOUT_INT_SECS = 60;

     Continuation cont = new Continuation(TIMEOUT_INT_SECS);

     cont.continuationMethod = 'processResponse';

     AsyncSOAPStockQuoteService.AsyncStockQuoteServiceSoap

       stockQuoteService =

        new AsyncSOAPStockQuoteService.AsyncStockQuoteServiceSoap();

     stockQuoteFuture = stockQuoteService.beginStockQuote(cont,'CRM');

     return cont;

   }

```

When the external service returns the response of the asynchronous callout (the `beginStockQuote` method), this callback method
is executed. It gets the response by calling the `getValue` method on the response object.

```
   public Object processResponse() {

     result = stockQuoteFuture.getValue();

     return null;

   }

```

The following is the entire controller with the action and callback methods.

```
   public class ContinuationSOAPController {

      AsyncSOAPStockQuoteService.GetStockQuoteResponse_elementFuture

          stockQuoteFuture;

      public String result {get;set;}

      // Action method

      public Continuation startRequest() {

        Integer TIMEOUT_INT_SECS = 60;

        Continuation cont = new Continuation(TIMEOUT_INT_SECS);

        cont.continuationMethod = 'processResponse';

        AsyncSOAPStockQuoteService.AsyncStockQuoteServiceSoap

         stockQuoteService =

           new AsyncSOAPStockQuoteService.AsyncStockQuoteServiceSoap();

          stockQuoteFuture = stockQuoteService.beginGetStockQuote(cont,'CRM');

        return cont;

      }

```


Apex Developer Guide Integration and Apex Utilities

```
      // Callback method

      public Object processResponse() {

        result = stockQuoteFuture.getValue();

        // Return null to re-render the original Visualforce page

        return null;

      }

   }

```

This example shows the corresponding Visualforce page that invokes the `startRequest` method and displays the result field.

```
   <apex:page controller="ContinuationSOAPController" showChat="false" showHeader="false">

     <apex:form >

       <!-- Invokes the action method when the user clicks this button. -->

       <apex:commandButton action="{!startRequest}"

            value="Start Request" reRender="result"/>

     </apex:form>

     <!-- This output text component displays the callout response body. -->

     <apex:outputText value="{!result}" />

   </apex:page>

```

Testing WSDL-Based Asynchronous Callouts

Testing asynchronous callouts that are based on Apex classes from a WSDL is similar to the process that’s used with callouts that are
based on the `HttpRequest` class. Before you test `ContinuationSOAPController.cls`, create a class that implements
`WebServiceMock` . This class enables safe testing for `ContinuationTestForWSDL.cls`, which we'll create in a moment,
by enabling a mock continuation and making sure that the test has no real effect.

```
   public class AsyncSOAPStockQuoteServiceMockImpl implements WebServiceMock {

      public void doInvoke(

        Object stub,

        Object request,

        Map<String, Object> response,

        String endpoint,

        String soapAction,

        String requestName,

        String responseNS,

        String responseName,

        String responseType) {

        // do nothing

      }

   }

```

This example is the test class that corresponds to the `ContinuationSOAPController` controller. The test method in the class
sets a fake response and invokes a mock continuation. The callout isn’t sent to the external service. To perform a mock callout, the test
calls these methods of the `Test` [class: Test.setContinuationResponse() and Test.invokeContinuationMethod().](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm#apex_System_Test_setContinuationResponse)

```
   @isTest

   public class ContinuationTestingForWSDL {

      public static testmethod void testWebService() {

        ContinuationSOAPController demoWSDLClass =

           new ContinuationSOAPController();

        // Invoke the continuation by calling the action method

```


Apex Developer Guide Integration and Apex Utilities

```
        Continuation conti = demoWSDLClass.startRequest();

        // Verify that the continuation has the proper requests

        Map<String, HttpRequest> requests = conti.getRequests();

        System.assertEquals(requests.size(), 1);

        // Perform mock callout

        // (i.e. skip the callout and call the callback method)

        HttpResponse response = new HttpResponse();

        response.setBody('<SOAP:Envelope'

           + ' xmlns:SOAP="http://schemas.xmlsoap.org/soap/envelope/">'

           + '<SOAP:Body>'

           + '<m:getStockQuoteResponse '

           + 'xmlns:m="http://soap.sforce.com/schemas/class/StockQuoteServiceSoap">'

           + '<m:result>Mock response body</m:result>'

           + '</m:getStockQuoteResponse>'

           + '</SOAP:Body>'

           + '</SOAP:Envelope>');

        // Set the fake response for the continuation

        String requestLabel = requests.keyset().iterator().next();

        Test.setContinuationResponse(requestLabel, response);

        // Invoke callback method

        Object result = Test.invokeContinuationMethod(demoWSDLClass, conti);

        System.debug(demoWSDLClass);

        // result is the return value of the callback

        System.assertEquals(null, result);

        // Verify that the controller's result variable

        // is set to the mock response.

        System.assertEquals('Mock response body', demoWSDLClass.result);

      }

   }

#### JSON Support

```

JavaScript Object Notation (JSON) support in Apex enables the serialization of Apex objects into JSON format and the deserialization of
serialized JSON content.

Apex provides a set of classes that expose methods for JSON serialization and deserialization. The following table describes the classes
available.

**Class** **Description**

```
System.JSON

```

Contains methods for serializing Apex objects into JSON format
and deserializing JSON content that was serialized using the
`serialize` method in this class.

`[System.JSONGenerator](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_JsonGenerator.htm)` Contains methods used to serialize objects into JSON content using
the standard JSON encoding.

`[System.JSONParser](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_JsonParser.htm)` Represents a parser for JSON-encoded content.


Apex Developer Guide Integration and Apex Utilities

The `System.JSONToken` enumeration contains the tokens used for JSON parsing.

Methods in these classes throw a `JSONException` if an issue is encountered during execution.

**JSON Support Considerations**

**•** JSON serialization and deserialization support is available for sObjects (standard objects and custom objects), Apex primitive
and collection types, return types of Database methods (such as SaveResult and DeleteResult), and instances of your Apex classes.

**•** Only custom objects, which are `sObject` types of managed packages can be serialized from code that is external to the
managed package. Objects that are instances of Apex classes defined in the managed package can't be serialized.

**•** A Map object is serializable into JSON only if it uses one of the following data types as a key.

**–** [Boolean](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_boolean.htm)

**–** [Date](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_date.htm)

**–** [DateTime](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_datetime.htm)

**–** [Decimal](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_decimal.htm)

**–** [Double](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_double.htm)

**–** [Enum](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_enum.htm)

**–** [Id](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_id.htm)

**–** [Integer](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_integer.htm)

**–** [Long](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_long.htm)

**–** [String](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_string.htm)

**–** [Time](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_time.htm)

**•** When an object is declared as the parent type but is set to an instance of the subtype, some data can be lost. The object gets
serialized and deserialized as the parent type and any fields that are specific to the subtype are lost.

**•** An object that has a reference to itself won’t get serialized and causes a `JSONException` to be thrown.

**•** Reference graphs that reference the same object twice are deserialized and cause multiple copies of the referenced object to
be generated.

**•** The `System.JSONParser` data type isn’t serializable. If you try to create an instance of a serializable class, such as a Visualforce
controller, that has a member variable of type `System.JSONParser`, you receive an exception. To use `JSONParser` in
a serializable class, use a local variable instead in your method.

Versioned Behavior Changes

In API version 63.0 and later, JSON serialization of custom exceptions and most built-in exceptions isn't supported. Attempting to serialize
an exception throws an error: `Type unsupported in JSON: MyException` .

In API version 53.0 and later, DateTime format and processing has been updated. The API correctly handles DateTime values in JSON
requests that use more than 3 digits after the decimal point. Requests that use an unsupported DateTime format (such as `123456000` )
[result in an error. Salesforce recommends that you strictly adhere to DateTime formats specified in Valid Date and DateTime Formats.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_valid_date_formats.htm)

Roundtrip Serialization and Deserialization
Use the `JSON` class methods to perform roundtrip serialization and deserialization of your JSON content. These methods enable
you to serialize objects into JSON-formatted strings and to deserialize JSON strings back into objects.

JSON Generator
Using the `JSONGenerator` class methods, you can generate standard JSON-encoded content.


Apex Developer Guide Integration and Apex Utilities

JSON Parsing
Use the `JSONParser` class methods to parse JSON-encoded content. These methods enable you to parse a JSON-formatted
response that's returned from a call to an external service, such as a web service callout.

##### Roundtrip Serialization and Deserialization

Use the `JSON` class methods to perform roundtrip serialization and deserialization of your JSON content. These methods enable you
to serialize objects into JSON-formatted strings and to deserialize JSON strings back into objects.

Example: Serialize and Deserialize a List of Invoices

This example creates a list of `InvoiceStatement` objects and serializes the list. Next, the serialized JSON string is used to deserialize
the list again and the sample verifies that the new list contains the same invoices that were present in the original list.

```
   public class JSONRoundTripSample {

      public class InvoiceStatement {

        Long invoiceNumber;

        Datetime statementDate;

        Decimal totalPrice;

        public InvoiceStatement(Long i, Datetime dt, Decimal price)

        {

           invoiceNumber = i;

           statementDate = dt;

           totalPrice = price;

        }

      }

      public static void SerializeRoundtrip() {

        Datetime dt = Datetime.now();

        // Create a few invoices.

        InvoiceStatement inv1 = new InvoiceStatement(1,Datetime.valueOf(dt),1000);

        InvoiceStatement inv2 = new InvoiceStatement(2,Datetime.valueOf(dt),500);

        // Add the invoices to a list.

        List<InvoiceStatement> invoices = new List<InvoiceStatement>();

        invoices.add(inv1);

        invoices.add(inv2);

        // Serialize the list of InvoiceStatement objects.

        String JSONString = JSON.serialize(invoices);

        System.debug('Serialized list of invoices into JSON format: ' + JSONString);

        // Deserialize the list of invoices from the JSON string.

        List<InvoiceStatement> deserializedInvoices =

        (List<InvoiceStatement>)JSON.deserialize(JSONString, List<InvoiceStatement>.class);

        System.assertEquals(invoices.size(), deserializedInvoices.size());

        Integer i=0;

        for (InvoiceStatement deserializedInvoice :deserializedInvoices) {

           system.debug('Deserialized:' + deserializedInvoice.invoiceNumber + ','

           + deserializedInvoice.statementDate.formatGmt('MM/dd/yyyy HH:mm:ss.SSS')

           + ', ' + deserializedInvoice.totalPrice);

```


Apex Developer Guide Integration and Apex Utilities

```
           system.debug('Original:' + invoices[i].invoiceNumber + ','

           + invoices[i].statementDate.formatGmt('MM/dd/yyyy HH:mm:ss.SSS')

           + ', ' + invoices[i].totalPrice);

           i++;

        }

      }

   }

```

JSON Serialization Considerations

The behavior of the `serialize` method differs depending on the Salesforce API version of the Apex code saved.

**Serialization of queried sObject with additional fields set**
For Apex saved using Salesforce API version 27.0 and earlier, if queried sObjects have additional fields set, these fields aren’t included
in the serialized JSON string returned by the `serialize` method. Starting with Apex saved using Salesforce API version 28.0, the
additional fields are included in the serialized JSON string.

This example adds a field to a contact after it has been queried, and then serializes the contact. The assertion statement verifies that
the JSON string contains the additional field. The assertion passes for Apex saved using Salesforce API version 28.0 and later.

```
     Contact con = [SELECT Id, LastName, AccountId FROM Contact LIMIT 1];

     // Set additional field

     con.FirstName = 'Joe';

     String jsonstring = Json.serialize(con);

     System.debug(jsonstring);

     System.assert(jsonstring.contains('Joe') == true);

```

**Serialization of aggregate query result fields**
For Apex saved using Salesforce API version 27.0, results of aggregate queries don’t include the fields in the SELECT statement when
serialized using the `serialize` method. For earlier API versions or for API version 28.0 and later, serialized aggregate query results
include all fields in the SELECT statement.

This aggregate query returns two fields: the count of ID fields and the account name.

```
     String jsonString = JSON.serialize(

       Database.query('SELECT Count(Id),Account.Name FROM Contact WHERE Account.Name !=

     null GROUP BY Account.Name LIMIT 1'));

       System.debug(jsonString);

     // Expected output in API v 26 and earlier or v28 and later

     // [{"attributes":{"type":"AggregateResult"},"expr0":2,"Name":"acct1"}]

```

**Serialization of empty fields**
Starting with API version 28.0, null fields aren’t serialized and aren’t included in the JSON string, unlike in earlier versions. This change
[doesn’t affect deserializing JSON strings with JSON methods, such as Json.deserialize(). This change is noticeable when you inspect](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm#apex_System_Json_deserialize)
the JSON string. For example:

```
     String jsonString = JSON.serialize(

               [SELECT Id, Name, Website FROM Account WHERE Website = null LIMIT 1]);

     System.debug(jsonString);

     // In v27.0 and earlier, the string includes the null field and looks like the following.

     // {"attributes":{...},"Id":"001D000000Jsm0WIAR","Name":"Acme","Website":null}

     // In v28.0 and later, the string doesn’t include the null field and looks like

```


Apex Developer Guide Integration and Apex Utilities

```
     // the following.

     // {"attributes":{...},"Name":"Acme","Id":"001D000000Jsm0WIAR"}}

```

**Serialization of IDs**
In API version 34.0 and earlier, ID comparison using `==` fails for IDs that have been through roundtrip JSON serialization and
deserialization.

JSON Deserialization Considerations

JSON from aggregate results can’t be deserialized back into Apex AggregateResult objects because they have no named fields.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Json.htm)_ : JSON Class

##### JSON Generator

Using the `JSONGenerator` class methods, you can generate standard JSON-encoded content.

You can construct JSON content, element by element, using the standard JSON encoding. To do so, use the methods in the
`JSONGenerator` class.

JSONGenerator Sample

This example generates a JSON string in pretty print format by using the methods of the `JSONGenerator` class. The example first
adds a number field and a string field, and then adds a field to contain an object field of a list of integers, which gets deserialized properly.
Next, it adds the `A` object into the `Object A` field, which also gets deserialized.

```
   public class JSONGeneratorSample{

      public class A {

        String str;

        public A(String s) { str = s; }

      }

      static void generateJSONContent() {

        // Create a JSONGenerator object.

        // Pass true to the constructor for pretty print formatting.

        JSONGenerator gen = JSON.createGenerator(true);

        // Create a list of integers to write to the JSON string.

        List<integer> intlist = new List<integer>();

        intlist.add(1);

        intlist.add(2);

        intlist.add(3);

        // Create an object to write to the JSON string.

        A x = new A('X');

        // Write data to the JSON string.

        gen.writeStartObject();

        gen.writeNumberField('abc', 1.21);

        gen.writeStringField('def', 'xyz');

```


Apex Developer Guide Integration and Apex Utilities

```
        gen.writeFieldName('ghi');

        gen.writeStartObject();

        gen.writeObjectField('aaa', intlist);

        gen.writeEndObject();

        gen.writeFieldName('Object A');

        gen.writeObject(x);

        gen.writeEndObject();

        // Get the JSON string.

        String pretty = gen.getAsString();

        System.assertEquals('{\n' +

        ' "abc" : 1.21,\n' +

        ' "def" : "xyz",\n' +

        ' "ghi" : {\n' +

        ' "aaa" : [ 1, 2, 3 ]\n' +

        ' },\n' +

        ' "Object A" : {\n' +

        ' "str" : "X"\n' +

        ' }\n' +

        '}', pretty);

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: JSONGenerator Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_JsonGenerator.htm)

##### JSON Parsing

Use the `JSONParser` class methods to parse JSON-encoded content. These methods enable you to parse a JSON-formatted response
that's returned from a call to an external service, such as a web service callout.

The following are samples that show how to parse JSON strings.

Example: Parsing a JSON Response from a Web Service Callout

This example parses a JSON-formatted response using `JSONParser` methods. It makes a callout to a web service that returns a
response in JSON format. Next, the response is parsed to build up a map from api version numbers to the release labels.

```
   public class JSONParserUtil {

      public static void parseJSONResponse() {

        // Create HTTP request to send.

        HttpRequest request = new HttpRequest();

        // Set the endpoint URL.

        String endpoint = URL.getOrgDomainUrl().toExternalForm() + '/services/data';

        request.setEndPoint(endpoint);

        // Set the HTTP verb to GET.

```


Apex Developer Guide Integration and Apex Utilities

```
        request.setMethod('GET');

        // Set the request header for JSON content type

        request.setHeader('Accept', 'application/json');

        // Send the HTTP request and get the response.

        // The response is in JSON format.

        Http httpProtocol = new Http();

        HttpResponse response = httpProtocol.send(request);

        System.debug(response.getBody());

        /* The JSON response returned is the following:

           {"label":"Summer '14","url":"/services/data/v31.0","version":"31.0"},

           {"label":"Winter '15","url":"/services/data/v32.0","version":"32.0"},

           {"label":"Spring '15","url":"/services/data/v33.0","version":"33.0"},

        */

        // Parse JSON response to build a map from API version numbers to labels

        JSONParser parser = JSON.createParser(response.getBody());

        Map<double, string> apiVersionToReleaseNameMap = new Map<double, string>();

        string label = null;

        double version = null;

        while (parser.nextToken() != null) {

           if (parser.getCurrentToken() == JSONToken.FIELD_NAME) {

             switch on parser.getText() {

               when 'label' {

               // Advance to the label value.

               parser.nextToken();

                  label = parser.getText();

               }

               when 'version' {

                  // Advance to the version value.

                  parser.nextToken();

                  version = Double.valueOf(parser.getText());

               }

             }

           }

           if(version != null && String.isNotEmpty(label)) {

             apiVersionToReleaseNameMap.put(version, label);

             version = null;

             label = null;

           }

        }

        system.debug('Release with Rainbow logo = ' +

           apiVersionToReleaseNameMap.get(39.0D));

      }

   }

```

Example: Parse a JSON String and Deserialize It into Objects

This example uses a hardcoded JSON string, which is the same JSON string returned by the callout in the previous example. In this
example, the entire string is parsed into `Invoice` objects using the `readValueAs` method. This code also uses the `skipChildren`
method to skip the child array and child objects and parse the next sibling invoice in the list. The parsed objects are instances of the


Apex Developer Guide Integration and Apex Utilities

`Invoice` class that is defined as an inner class. Because each invoice contains line items, the class that represents the corresponding
line item type, the `LineItem` class, is also defined as an inner class. Add this sample code to a class to use it.

```
   public static void parseJSONString() {

      String jsonStr =

        '{"invoiceList":[' +

        '{"totalPrice":5.5,"statementDate":"2011-10-04T16:58:54.858Z","lineItems":[' +

           '{"UnitPrice":1.0,"Quantity":5.0,"ProductName":"Pencil"},' +

           '{"UnitPrice":0.5,"Quantity":1.0,"ProductName":"Eraser"}],' +

             '"invoiceNumber":1},' +

        '{"totalPrice":11.5,"statementDate":"2011-10-04T16:58:54.858Z","lineItems":[' +

           '{"UnitPrice":6.0,"Quantity":1.0,"ProductName":"Notebook"},' +

           '{"UnitPrice":2.5,"Quantity":1.0,"ProductName":"Ruler"},' +

           '{"UnitPrice":1.5,"Quantity":2.0,"ProductName":"Pen"}],"invoiceNumber":2}' +

        ']}';

      // Parse entire JSON response.

      JSONParser parser = JSON.createParser(jsonStr);

      while (parser.nextToken() != null) {

        // Start at the array of invoices.

        if (parser.getCurrentToken() == JSONToken.START_ARRAY) {

           while (parser.nextToken() != null) {

             // Advance to the start object marker to

             // find next invoice statement object.

             if (parser.getCurrentToken() == JSONToken.START_OBJECT) {

               // Read entire invoice object, including its array of line items.

               Invoice inv = (Invoice)parser.readValueAs(Invoice.class);

               system.debug('Invoice number: ' + inv.invoiceNumber);

               system.debug('Size of list items: ' + inv.lineItems.size());

               // For debugging purposes, serialize again to verify what was parsed.

               String s = JSON.serialize(inv);

               system.debug('Serialized invoice: ' + s);

               // Skip the child start array and start object markers.

               parser.skipChildren();

             }

           }

        }

      }

   }

   // Inner classes used for serialization by readValuesAs().

   public class Invoice {

      public Double totalPrice;

      public DateTime statementDate;

      public Long invoiceNumber;

      List<LineItem> lineItems;

      public Invoice(Double price, DateTime dt, Long invNumber, List<LineItem> liList) {

        totalPrice = price;

        statementDate = dt;

        invoiceNumber = invNumber;

        lineItems = liList.clone();

```


Apex Developer Guide Integration and Apex Utilities

```
      }

   }

   public class LineItem {

      public Double unitPrice;

      public Double quantity;

      public String productName;

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_JsonParser.htm)_ : JSONParser Class

#### XML Support

Apex provides utility classes that enable the creation and parsing of XML content using streams and the DOM.

This section contains details about XML support.

##### Reading and Writing XML Using Streams

Apex provides classes for reading and writing XML content using streams.

Reading and Writing XML Using the DOM
Apex provides classes that enable you to work with XML content using the DOM (Document Object Model).

##### Reading and Writing XML Using Streams

Apex provides classes for reading and writing XML content using streams.

The XMLStreamReader class enables you to read XML content and the XMLStreamWriter class enables you to write XML content.

###### Reading XML Using Streams

The XMLStreamReader class methods enable forward, read-only access to XML data.

Writing XML Using Streams
The XmlStreamWriter class methods enable the writing of XML data.

###### Reading XML Using Streams

The XMLStreamReader class methods enable forward, read-only access to XML data.

Those methods are used in conjunction with HTTP callouts to parse XML data or skip unwanted events. You can parse nested XML
content that’s up to 50 nodes deep. The following example shows how to instantiate a new XmlStreamReader object:

```
   String xmlString = '<books><book>My Book</book><book>Your Book</book></books>';

   XmlStreamReader xsr = new XmlStreamReader(xmlString);

```

These methods work on the following XML events:

**•** An _attribute_ event is specified for a particular element. For example, the element `<book>` has an attribute `title` : `<book`

`title="Salesforce.com for Dummies">` .

**•** A _start element_ event is the opening tag for an element, for example `<book>` .

**•** An _end element_ event is the closing tag for an element, for example `</book>` .


Apex Developer Guide Integration and Apex Utilities

**•** A _start document_ event is the opening tag for a document.

**•** An _end document_ event is the closing tag for a document.

**•** An _entity reference_ is an entity reference in the code, for example `!ENTITY title = "My Book Title"` .

**•** A _characters_ event is a text character.

**•** A _comment_ event is a comment in the XML file.

Use the `next` and `hasNext` methods to iterate over XML data. Access data in XML using `get` methods such as the `getNamespace`
method.

When iterating over the XML data, always check that stream data is available using `hasNext` before calling `next` to avoid attempting
to read past the end of the XML data.

XmlStreamReader Example

The following example processes an XML string.

```
   public class XmlStreamReaderDemo {

      // Create a class Book for processing

      public class Book {

        String name;

        String author;

      }

      public Book[] parseBooks(XmlStreamReader reader) {

        Book[] books = new Book[0];

        boolean isSafeToGetNextXmlElement = true;

        while(isSafeToGetNextXmlElement) {

           // Start at the beginning of the book and make sure that it is a book

           if (reader.getEventType() == XmlTag.START_ELEMENT) {

             if ('Book' == reader.getLocalName()) {

               // Pass the book to the parseBook method (below)

               Book book = parseBook(reader);

               books.add(book);

             }

           }

           // Always use hasNext() before calling next() to confirm

           // that we have not reached the end of the stream

           if (reader.hasNext()) {

             reader.next();

           } else {

             isSafeToGetNextXmlElement = false;

             break;

           }

        }

        return books;

      }

      // Parse through the XML, determine the author and the characters

      Book parseBook(XmlStreamReader reader) {

        Book book = new Book();

        book.author = reader.getAttributeValue(null, 'author');

        boolean isSafeToGetNextXmlElement = true;

        while(isSafeToGetNextXmlElement) {

```


Apex Developer Guide Integration and Apex Utilities

```
           if (reader.getEventType() == XmlTag.END_ELEMENT) {

             break;

           } else if (reader.getEventType() == XmlTag.CHARACTERS) {

             book.name = reader.getText();

           }

           // Always use hasNext() before calling next() to confirm

           // that we have not reached the end of the stream

           if (reader.hasNext()) {

             reader.next();

           } else {

             isSafeToGetNextXmlElement = false;

             break;

           }

        }

        return book;

      }

   }

   @isTest

   private class XmlStreamReaderDemoTest {

      // Test that the XML string contains specific values

      static testMethod void testBookParser() {

        XmlStreamReaderDemo demo = new XmlStreamReaderDemo();

        String str = '<books><book author="Chatty">Alpha beta</book>' +

           '<book author="Sassy">Baz</book></books>';

        XmlStreamReader reader = new XmlStreamReader(str);

        XmlStreamReaderDemo.Book[] books = demo.parseBooks(reader);

        System.debug(books.size());

        for (XmlStreamReaderDemo.Book book : books) {

           System.debug(book);

        }

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: XmlStreamReader Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_xml_XmlStream_reader.htm)

###### Writing XML Using Streams

The XmlStreamWriter class methods enable the writing of XML data.

Those methods are used in conjunction with HTTP callouts to construct an XML document to send in the callout request to an external
service. The following example shows how to instantiate a new XmlStreamReader object:

```
   String xmlString = '<books><book>My Book</book><book>Your Book</book></books>';

   XmlStreamReader xsr = new XmlStreamReader(xmlString);

```


Apex Developer Guide Integration and Apex Utilities

XML Writer Methods Example

The following example writes an XML document and tests its validity.

This Hello World sample requires custom objects. You can either create these objects on your own, or download the objects and Apex
[code as an unmanaged package from AppExchange. To obtain the sample assets in your org, install the Apex Tutorials Package. This](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000001saDCEAY)
package also contains sample code and objects for the Shipping Invoice example.

```
   public class XmlWriterDemo {

      public String getXml() {

         XmlStreamWriter w = new XmlStreamWriter();

         w.writeStartDocument(null, '1.0');

         w.writeProcessingInstruction('target', 'data');

         w.writeStartElement('m', 'Library', 'http://www.book.com');

         w.writeNamespace('m', 'http://www.book.com');

         w.writeComment('Book starts here');

         w.setDefaultNamespace('http://www.defns.com');

         w.writeCData('<Cdata> I like CData </Cdata>');

         w.writeStartElement(null, 'book', null);

         w.writedefaultNamespace('http://www.defns.com');

         w.writeAttribute(null, null, 'author', 'Manoj');

         w.writeCharacters('This is my book');

         w.writeEndElement(); //end book

         w.writeEmptyElement(null, 'ISBN', null);

         w.writeEndElement(); //end library

         w.writeEndDocument();

         String xmlOutput = w.getXmlString();

         w.close();

         return xmlOutput;

        }

   }

   @isTest

   private class XmlWriterDemoTest {

      static TestMethod void basicTest() {

        XmlWriterDemo demo = new XmlWriterDemo();

        String result = demo.getXml();

        String expected = '<?xml version="1.0"?><?target data?>' +

           '<m:Library xmlns:m="http://www.book.com">' +

           '<!--Book starts here-->' +

           '<![CDATA[<Cdata> I like CData </Cdata>]]>' +

   '<book xmlns="http://www.defns.com" author="Manoj">This is my

   book</book><ISBN/></m:Library>';

        System.assert(result == expected);

      }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: XmlStreamWriter Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_xml_XmlStream_writer.htm)


Apex Developer Guide Integration and Apex Utilities

##### Reading and Writing XML Using the DOM

Apex provides classes that enable you to work with XML content using the DOM (Document Object Model).

DOM classes help you parse or generate XML content. You can use these classes to work with any XML content. One common application
[is to use the classes to generate the body of a request created by HttpRequest or to parse a response accessed by HttpResponse. The](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm)
DOM represents an XML document as a hierarchy of nodes. Some nodes may be branch nodes and have child nodes, while others are
leaf nodes with no children. You can parse nested XML content that’s up to 50 nodes deep.

The DOM classes are contained in the `Dom` namespace.

[Use the Document Class to process the content in the body of the XML document.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_xml_dom_document.htm)

[Use the XmlNode Class to work with a node in the XML document.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_xml_dom_xmlnode.htm)

[Use the Document Class class to process XML content. One common application is to use it to create the body of a request for HttpRequest](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httprequest.htm)
[or to parse a response accessed by HttpResponse.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_http_httpresponse.htm)

XML Namespaces

An XML namespace is a collection of names identified by a URI reference and used in XML documents to uniquely identify element types
and attribute names. Names in XML namespaces may appear as qualified names, which contain a single colon, separating the name
into a namespace prefix and a local part. The prefix, which is mapped to a URI reference, selects a namespace. The combination of the
universally managed URI namespace and the document's own namespace produces identifiers that are universally unique.

The following XML element has a namespace of `http://my.name.space` and a prefix of `myprefix` .

```
   <sampleElement xmlns:myprefix="http://my.name.space" />

```

In the following example, the XML element has two attributes:

**•** The first attribute has a key of `dimension` ; the value is `2` .

**•** The second attribute has a key namespace of `http://ns1` ; the value namespace is `http://ns2` ; the key is `example` ; the
value is `test` .

```
   <square dimension="2" ns1:example="ns2:test" xmlns:ns1="http://ns1" xmlns:ns2="http://ns2"

    />

```

**`Document`** Example

For the purposes of the sample below, assume that the `url` argument passed into the `parseResponseDom` method returns this
XML response:

```
   <address>

      <name>Kirk Stevens</name>

      <street1>808 State St</street1>

      <street2>Apt. 2</street2>

      <city>Palookaville</city>

      <state>PA</state>

      <country>USA</country>

   </address>

```

The following example illustrates how to use DOM classes to parse the XML response returned in the body of a `GET` request:

```
   public class DomDocument {

      // Pass in the URL for the request

      // For the purposes of this sample,assume that the URL

```


Apex Developer Guide Integration and Apex Utilities

```
      // returns the XML shown above in the response body

      public void parseResponseDom(String url){

        Http h = new Http();

        HttpRequest req = new HttpRequest();

        // url that returns the XML in the response body

        req.setEndpoint(url);

        req.setMethod('GET');

        HttpResponse res = h.send(req);

        Dom.Document doc = res.getBodyDocument();

        //Retrieve the root element for this document.

        Dom.XMLNode address = doc.getRootElement();

        String name = address.getChildElement('name', null).getText();

        String state = address.getChildElement('state', null).getText();

        // print out specific elements

        System.debug('Name: ' + name);

        System.debug('State: ' + state);

        // Alternatively, loop through the child elements.

        // This prints out all the elements of the address

        for(Dom.XMLNode child : address.getChildElements()) {

          System.debug(child.getText());

        }

      }

   }

```

Using XML Nodes

Use the `XmlNode` class to work with a node in an XML document. The DOM represents an XML document as a hierarchy of nodes.
Some nodes may be branch nodes and have child nodes, while others are leaf nodes with no children.

There are different types of DOM nodes available in Apex. `XmlNodeType` is an enum of these different types. The values are:

**•** COMMENT

**•** ELEMENT

**•** TEXT

It is important to distinguish between elements and nodes in an XML document. The following is a simple XML example:

```
   <name>

      <firstName>Suvain</firstName>

      <lastName>Singh</lastName>

   </name>

```

This example contains three XML elements: `name`, `firstName`, and `lastName` . It contains five nodes: the three `name`, `firstName`,
and `lastName` element nodes, as well as two text nodes— `Suvain` and `Singh` . Note that the text within an element node is
considered to be a separate text node.

[For more information about the methods shared by all enums, see Enum Methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_enum.htm)


Apex Developer Guide Integration and Apex Utilities

**`XmlNode`** Example

This example shows how to use `XmlNode` methods and namespaces to create an XML request.

```
   public class DomNamespaceSample

   {

      public void sendRequest(String endpoint)

      {

        // Create the request envelope

        DOM.Document doc = new DOM.Document();

        String soapNS = 'http://schemas.xmlsoap.org/soap/envelope/';

        String xsi = 'http://www.w3.org/2001/XMLSchema-instance';

        String serviceNS = 'http://www.myservice.com/services/MyService/';

        dom.XmlNode envelope

           = doc.createRootElement('Envelope', soapNS, 'soapenv');

        envelope.setNamespace('xsi', xsi);

        envelope.setAttributeNS('schemaLocation', soapNS, xsi, null);

        dom.XmlNode body

           = envelope.addChildElement('Body', soapNS, null);

        body.addChildElement('echo', serviceNS, 'req').

          addChildElement('category', serviceNS, null).

          addTextNode('classifieds');

        System.debug(doc.toXmlString());

        // Send the request

        HttpRequest req = new HttpRequest();

        req.setMethod('POST');

        req.setEndpoint(endpoint);

        req.setHeader('Content-Type', 'text/xml');

        req.setBodyDocument(doc);

        Http http = new Http();

        HttpResponse res = http.send(req);

        System.assertEquals(200, res.getStatusCode());

        dom.Document resDoc = res.getBodyDocument();

        envelope = resDoc.getRootElement();

        String wsa = 'http://schemas.xmlsoap.org/ws/2004/08/addressing';

        dom.XmlNode header = envelope.getChildElement('Header', soapNS);

        System.assert(header != null);

        String messageId

           = header.getChildElement('MessageID', wsa).getText();

        System.debug(messageId);

```


Apex Developer Guide Integration and Apex Utilities

```
        System.debug(resDoc.toXmlString());

        System.debug(resDoc);

        System.debug(header);

        System.assertEquals(

         'http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous',

         header.getChildElement(

          'ReplyTo', wsa).getChildElement('Address', wsa).getText());

        System.assertEquals(

         envelope.getChildElement('Body', soapNS).

            getChildElement('echo', serviceNS).

            getChildElement('something', 'http://something.else').

            getChildElement(

             'whatever', serviceNS).getAttribute('bb', null),

             'cc');

        System.assertEquals('classifieds',

         envelope.getChildElement('Body', soapNS).

            getChildElement('echo', serviceNS).

            getChildElement('category', serviceNS).getText());

      }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_xml_dom_document.htm)_ : Document Class

#### ZIP Support

Take advantage of a native Apex Zip library to create and extract ZIP archive files by using the class methods in the `Compression`
namespace.

You can compress multiple attachments or documents into an Apex blob that contains the ZIP archive. You can also specify the data to
be extracted from the zip archive, without uncompressing the entire ZIP archive. To optimize compression, you can specify a compression
method and compression level.

This example code extracts a JSON translation file from a callout response containing a ZIP archive by getting and extracting the specified
entry from the ZIP archive.

```
   HttpRequest request = new HttpRequest();

   request.setEndpoint('callout:My_Named_Credential/translationService');

   request.setMethod('POST');

   // Set request payload to translate...

   HttpResponse response = new Http().send(request);

   Blob translationZip = response.getBodyAsBlob();

   ZipReader reader = new ZipReader(translationZip);

```


Apex Developer Guide Integration and Apex Utilities

```
   ZipEntry frTranslation = reader.getEntry('translations/fr.json');

   Blob frTranslationData = reader.extractEntry(frTranslation);

```

SEE ALSO:

_Apex Reference Guide_ [: Compression NameSpace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_Compression.htm)

#### Securing Your Data

You can secure your data by using the methods provided by the `Crypto` class.

The methods in the `Crypto` class provide standard algorithms for creating digests, message authentication codes, and signatures, as
well as encrypting and decrypting information. These alogorithms can be used for securing content in Salesforce or for integrating with
external services such as Google or Amazon WebServices (AWS).

Note: The code excerpts on this page are written to highlight the use of the Crypto class. A production-level implementation
would incorporate more plaintext key security. Refer to Strengthen Your Data’s Security with Shield Platform Encryption in Salesforce
Help.

Example Integrating Amazon WebServices

This example demonstrates an integration of Amazon WebServices with Salesforce.

```
   public class HMacAuthCallout {

     public void testAlexaWSForAmazon() {

     // The date format is yyyy-MM-dd'T'HH:mm:ss.SSS'Z'

       DateTime d = System.now();

       String timestamp = ''+ d.year() + '-' +

       d.month() + '-' +

       d.day() + '\'T\'' +

       d.hour() + ':' +

       d.minute() + ':' +

       d.second() + '.' +

       d.millisecond() + '\'Z\'';

       String timeFormat = d.formatGmt(timestamp);

       String urlEncodedTimestamp = EncodingUtil.urlEncode(timestamp, 'UTF-8');

       String action = 'UrlInfo';

       String inputStr = action + timeFormat;

       String algorithmName = 'HMacSHA1';

       Blob mac = Crypto.generateMac(algorithmName, Blob.valueOf(inputStr),

                                   Blob.valueOf('your_signing_key'));

       String macUrl = EncodingUtil.urlEncode(EncodingUtil.base64Encode(mac), 'UTF-8');

       String urlToTest = 'amazon.com';

       String version = '2005-07-11';

       String endpoint = 'http://awis.amazonaws.com/';

       String accessKey = 'your_key';

       HttpRequest req = new HttpRequest();

       req.setEndpoint(endpoint +

                 '?AWSAccessKeyId=' + accessKey +

```


Apex Developer Guide Integration and Apex Utilities

```
                 '&Action=' + action +

                 '&ResponseGroup=Rank&Version=' + version +

                 '&Timestamp=' + urlEncodedTimestamp +

                 '&Url=' + urlToTest +

                 '&Signature=' + macUrl);

       req.setMethod('GET');

       Http http = new Http();

       try {

         HttpResponse res = http.send(req);

         System.debug('STATUS:'+res.getStatus());

         System.debug('STATUS_CODE:'+res.getStatusCode());

         System.debug('BODY: '+res.getBody());

       } catch(System.CalloutException e) {

         System.debug('ERROR: '+ e);

       }

     }

   }

```

Example Encrypting and Decrypting

This example uses the `encryptWithManagedIV` and `decryptWithManagedIV` methods and the `generateAesKey`
method of the `Crypto` class.

```
   // Use generateAesKey to generate the private key

   Blob cryptoKey = Crypto.generateAesKey(256);

   // Generate the data to be encrypted.

   Blob data = Blob.valueOf('Test data to encrypted');

   // Encrypt the data and have Salesforce generate the initialization vector

   Blob encryptedData = Crypto.encryptWithManagedIV('AES256', cryptoKey, data);

   // Decrypt the data

   Blob decryptedData = Crypto.decryptWithManagedIV('AES256', cryptoKey, encryptedData);

```

This example shows how to write a unit test for the `encryptWithManagedIV` and `decryptWithManagedIV` Crypto methods.

```
   @isTest

   private class CryptoTest {

      static testMethod void testValidDecryption() {

        // Use generateAesKey to generate the private key

        Blob key = Crypto.generateAesKey(128);

        // Generate the data to be encrypted.

        Blob data = Blob.valueOf('Test data');

        // Generate an encrypted form of the data using base64 encoding

        String b64Data = EncodingUtil.base64Encode(data);

        // Encrypt and decrypt the data

        Blob encryptedData = Crypto.encryptWithManagedIV('AES128', key, data);

        Blob decryptedData = Crypto.decryptWithManagedIV('AES128', key, encryptedData);

        String b64Decrypted = EncodingUtil.base64Encode(decryptedData);

        // Verify that the strings still match

        System.assertEquals(b64Data, b64Decrypted);

```


Apex Developer Guide Integration and Apex Utilities

```
      }

      static testMethod void testInvalidDecryption() {

        // Verify that you must use the same key size for encrypting data

        // Generate two private keys, using different key sizes

        Blob keyOne = Crypto.generateAesKey(128);

        Blob keyTwo = Crypto.generateAesKey(256);

        // Generate the data to be encrypted.

        Blob data = Blob.valueOf('Test data');

        // Encrypt the data using the first key

        Blob encryptedData = Crypto.encryptWithManagedIV('AES128', keyOne, data);

        try {

         // Try decrypting the data using the second key

           Crypto.decryptWithManagedIV('AES256', keyTwo, encryptedData);

           System.assert(false);

        } catch(SecurityException e) {

          System.assertEquals('Given final block not properly padded', e.getMessage());

        }

      }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_crypto.htm)_ : Crypto Class

_Salesforce Help_ [: Strengthen Your Data’s Security with Shield Platform Encryption](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_overview.htm&type=5&language=en_US)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_encodingUtil.htm)_ : EncodingUtil Class

#### Encoding Your Data

You can encode and decode URLs and convert strings to hexadecimal format by using the methods provided by the `EncodingUtil`
class.

This example shows how to URL encode a timestamp value in UTF-8 by calling `urlEncode` .

```
   DateTime d = System.now();

   String timestamp = ''+ d.year() + '-' +

      d.month() + '-' +

      d.day() + '\'T\'' +

      d.hour() + ':' +

      d.minute() + ':' +

      d.second() + '.' +

      d.millisecond() + '\'Z\'';

   System.debug(timestamp);

   String urlEncodedTimestamp = EncodingUtil.urlEncode(timestamp, 'UTF-8');

   System.debug(urlEncodedTimestamp);

```

This next example shows how to use `convertToHex` to compute a client response for HTTP Digest Authentication (RFC2617).

```
   @isTest

   private class SampleTest {

     static testmethod void testConvertToHex() {

       String myData = 'A Test String';

       Blob hash = Crypto.generateDigest('SHA1',Blob.valueOf( myData ));

       String hexDigest = EncodingUtil.convertToHex(hash);

```


Apex Developer Guide Integration and Apex Utilities

```
       System.debug(hexDigest);

      }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_restful_encodingUtil.htm)_ : EncodingUtil Class

#### Using Patterns and Matchers

Apex provides patterns and matchers that enable you to search text using regular expressions.

A pattern is a compiled representation of a regular expression. Patterns are used by matchers to perform match operations on a character
string.

A _regular expression_ is a string that is used to match another string, using a specific syntax. Apex supports the use of regular expressions
through its _Pattern_ and _Matcher_ classes.

Note: In Apex, Patterns and Matchers, as well as regular expressions, are based on their counterparts in Java. See
`[http://java.sun.com/j2se/1.5.0/docs/api/index.html?java/util/regex/Pattern.html](http://java.sun.com/j2se/1.5.0/docs/api/index.html?java/util/regex/Pattern.html)` .

Many Matcher objects can share the same Pattern object, as shown in the following illustration:

**Many Matcher objects can be created from the same Pattern object**

Regular expressions in Apex follow the standard syntax for regular expressions used in Java. Any Java-based regular expression strings
can be easily imported into your Apex code.

Note: Salesforce limits the number of times an input sequence for a regular expression can be accessed to 1,000,000 times. If you
reach that limit, you receive a runtime error.

All regular expressions are specified as strings. Most regular expressions are first compiled into a Pattern object: only the String `split`
method takes a regular expression that isn't compiled.

Generally, after you compile a regular expression into a Pattern object, you only use the Pattern object once to create a Matcher object.
All further actions are then performed using the Matcher object. For example:

```
   // First, instantiate a new Pattern object "MyPattern"

   Pattern MyPattern = Pattern.compile('a*b');

```


Apex Developer Guide Integration and Apex Utilities

```
   // Then instantiate a new Matcher object "MyMatcher"

   Matcher MyMatcher = MyPattern.matcher('aaaaab');

   // You can use the system static method assert to verify the match

   System.assert(MyMatcher.matches());

```

If you are only going to use a regular expression once, use the `Pattern` class `matches` method to compile the expression and
match a string against it in a single invocation. For example, the following is equivalent to the code above:

```
   Boolean Test = Pattern.matches('a*b', 'aaaaab');

##### Using Regions Using Match Operations

```

Using Bounds

Understanding Capturing Groups

Pattern and Matcher Example

##### Using Regions

A Matcher object finds matches in a subset of its input string called a _region_ . The default region for a Matcher object is always the entirety
of the input string. However, you can change the start and end points of a region by using the `region` method, and you can query
the region's end points by using the `regionStart` and `regionEnd` methods.

The `region` method requires both a start and an end value. The following table provides examples of how to set one value without
setting the other.

**Start of the Region** **End of the Region** **Code Example**

Specify explicitly Leave unchanged
```
                         MyMatcher.region(start, MyMatcher.regionEnd());

```

Leave unchanged Specify explicitly
```
                         MyMatcher.region(MyMatcher.regionStart(), end);

```

Reset to the default Specify explicitly
```
                         MyMatcher.region(0, end);

##### Using Match Operations

```

A _Matcher object_ performs match operations on a character sequence by interpreting a Pattern.

A Matcher object is instantiated from a Pattern by the Pattern's `matcher` method. Once created, a Matcher object can be used to
perform the following types of match operations:

**•** Match the Matcher object's entire input string against the pattern using the `matches` method

**•** Match the Matcher object's input string against the pattern, starting at the beginning but without matching the entire region, using
the `lookingAt` method

**•** Scan the Matcher object's input string for the next substring that matches the pattern using the `find` method

Each of these methods returns a Boolean indicating success or failure.


Apex Developer Guide Integration and Apex Utilities

After you use any of these methods, you can find out more information about the previous match, that is, what was found, by using the
following Matcher class methods:

**•** `end` : Once a match is made, this method returns the position in the match string after the last character that was matched.

**•** `start` : Once a match is made, this method returns the position in the string of the first character that was matched.

**•** `group` : Once a match is made, this method returns the subsequence that was matched.

##### Using Bounds

By default, a region is delimited by _anchoring bounds_, which means that the line anchors (such as `^` or `$` ) match at the region boundaries,
even if the region boundaries have been moved from the start and end of the input string. You can specify whether a region uses
anchoring bounds with the `useAnchoringBounds` method. By default, a region always uses anchoring bounds. If you set
`useAnchoringBounds` to `false`, the line anchors match only the true ends of the input string.

By default, all text located outside of a region is not searched, that is, the region has _opaque bounds_ . However, using _transparent bounds_
it is possible to search the text outside of a region. Transparent bounds are only used when a region no longer contains the entire input
string. You can specify which type of bounds a region has by using the `useTransparentBounds` method.

Suppose you were searching the following string, and your region was only the word “STRING”:

```
   This is a concatenated STRING of cats and dogs.

```

If you searched for the word “cat”, you wouldn't receive a match unless you had transparent bounds set.

##### Understanding Capturing Groups

During a matching operation, each substring of the input string that matches the pattern is saved. These matching substrings are called
_capturing groups_ .

Capturing groups are numbered by counting their opening parentheses from left to right. For example, in the regular expression string
`((A)(B(C)))`, there are four capturing groups:

**1.** `((A)(B(C)))`

**2.** `(A)`

**3.** `(B(C))`

**4.** `(C)`

Group zero always stands for the entire expression.

The captured input associated with a group is always the substring of the group most recently matched, that is, that was returned by
one of the Matcher class match operations.

If a group is evaluated a second time using one of the match operations, its previously captured value, if any, is retained if the second
evaluation fails.

##### Pattern and Matcher Example

The Matcher class `end` method returns the position in the match string after the last character that was matched. You would use this
when you are parsing a string and want to do additional work with it after you have found a match, such as find the next match.

In regular expression syntax, `?` means match once or not at all, and `+` means match 1 or more times.


Apex Developer Guide Integration and Apex Utilities

In the following example, the string passed in with the Matcher object matches the pattern since `(a(b)?)` matches the string `'ab'`

      - `'a'` followed by `'b'` once. It then matches the last `'a'`      - `'a'` followed by `'b'` not at all.

```
   pattern myPattern = pattern.compile('(a(b)?)+');

   matcher myMatcher = myPattern.matcher('aba');

   System.assert(myMatcher.matches() && myMatcher.hitEnd());

   // We have two groups: group 0 is always the whole pattern, and group 1 contains

   // the substring that most recently matched--in this case, 'a'.

   // So the following is true:

   System.assert(myMatcher.groupCount() == 2 &&

            myMatcher.group(0) == 'aba' &&

            myMatcher.group(1) == 'a');

   // Since group 0 refers to the whole pattern, the following is true:

   System.assert(myMatcher.end() == myMatcher.end(0));

   // Since the offset after the last character matched is returned by end,

   // and since both groups used the last input letter, that offset is 3

   // Remember the offset starts its count at 0. So the following is also true:

   System.assert(myMatcher.end() == 3 &&

            myMatcher.end(0) == 3 &&

            myMatcher.end(1) == 3);

```

In the following example, email addresses are normalized and duplicates are reported if there is a different top-level domain name or
subdomain for similar email addresses. For example, `john@fairway.smithco` is normalized to `john@smithco` .

```
   class normalizeEmailAddresses{

      public void hasDuplicatesByDomain(Lead[] leads) {

          // This pattern reduces the email address to 'john@smithco'

          // from 'john@*.smithco.com' or 'john@smithco.*'

        Pattern emailPattern = Pattern.compile('(?<=@)((?![\\w]+\\.[\\w]+$)

                                [\\w]+\\.)|(\\.[\\w]+$)');

          // Define a set for emailkey to lead:

        Map<String,Lead> leadMap = new Map<String,Lead>();

             for(Lead lead:leads) {

               // Ignore leads with a null email

               if(lead.Email != null) {

                    // Generate the key using the regular expression

                 String emailKey = emailPattern.matcher(lead.Email).replaceAll('');

                    // Look for duplicates in the batch

                 if(leadMap.containsKey(emailKey))

                    lead.email.addError('Duplicate found in batch');

                 else {

                    // Keep the key in the duplicate key custom field

                    lead.Duplicate_Key__c = emailKey;

                    leadMap.put(emailKey, lead);

                 }

              }

           }

```


## Apex Developer Guide Debugging, Testing, and Deploying Apex

```
             // Now search the database looking for duplicates

             for(Lead[] leadsCheck:[SELECT Id, duplicate_key__c FROM Lead WHERE

             duplicate_key__c IN :leadMap.keySet()]) {

            for(Lead lead:leadsCheck) {

            // If there's a duplicate, add the error.

               if(leadMap.containsKey(lead.Duplicate_Key__c))

                leadMap.get(lead.Duplicate_Key__c).email.addError('Duplicate found

                  in salesforce(Id: ' + lead.Id + ')');

           }

        }

      }

    }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_pattern_and_matcher_pattern_methods.htm)_ : Pattern Class

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_pattern_and_matcher_matcher_methods.htm)_ : Matcher Class

## Debugging, Testing, and Deploying Apex

Develop your Apex code in a sandbox and debug it with the Developer Console and debug logs. Unit-test your code, then distribute it
to customers using packages.

### Debugging Apex

Apex provides debugging support. You can debug your Apex code using the Developer Console and debug logs.

Testing Apex
Apex provides a testing framework that allows you to write unit tests, run your tests, check test results, and have code coverage
results.

Deploying Apex
You can't develop Apex in your Salesforce production org. Your development work is done in a sandbox, in a scratch org, or in a
Developer Edition org.

Apex in Managed Packages
Learn how to develop, distribute, and use managed Apex. Apex in managed packages can behave differently than Apex in unmanaged
packages or Apex deployed directly to an org. Managed package developers and subscribers must understand these differences so
that they can safely evolve their packages and integrations.

### Debugging Apex

Apex provides debugging support. You can debug your Apex code using the Developer Console and debug logs.

To aid debugging in your code, Apex supports exception statements and custom exceptions. Also, Apex sends emails to developers for
unhandled exceptions.

1. Debug Log


Apex Developer Guide Debugging Apex

2. Exceptions in Apex
_Exceptions_ note errors and other events that disrupt the normal flow of code execution. `throw` statements are used to generate
exceptions, while `try`, `catch`, and `finally` statements are used to gracefully recover from exceptions.

#### Debug Log

A debug log can record database operations, system processes, and errors that occur when executing a transaction or running unit tests.
Debug logs can contain information about:

**•** Database changes

**•** HTTP callouts

**•** Apex errors

**•** Resources used by Apex

**•** Automated workflow processes, such as:

**–** Workflow rules

**–** Assignment rules

**–** Approval processes

**–** Validation rules

Note: The debug log doesn’t include information from actions triggered by time-based workflows. It also doesn’t include
information from standard or custom controllers used in Visualforce email templates.

You can retain and manage debug logs for specific users, including yourself, and for classes and triggers. Setting class and trigger trace
flags doesn’t cause logs to be generated or saved. Class and trigger trace flags override other logging levels, including logging levels set
by user trace flags, but they don’t cause logging to occur. If logging is enabled when classes or triggers execute, logs are generated at
the time of execution.

#### To view a debug log from Setup, enter Debug Logs in the Quick Find box, then select Debug Logs . Then click View next to

the debug log that you want to examine. Click **Download** to download the debug log as a log file.

#### Debug Log Limits

Debug logs have the following limits.

**•** Each debug log must be 20 MB or smaller. Debug logs that are larger than 20 MB are reduced in size by removing older log lines,
such as log lines for earlier `System.debug` statements. The log lines can be removed from any location, not just the start of the
debug log.

**•** System debug logs are retained for 24 hours. Monitoring debug logs are retained for seven days.

**•** If you generate more than 1,000 MB of debug logs in a 15-minute window, your trace flags are disabled. We send an email to the
users who last modified the trace flags, informing them that they can re-enable the trace flag in 15 minutes.

Warning: If the debug log trace flag is enabled on a frequently accessed Apex class or for a user executing requests often,
the request can result in failure, regardless of the time window and the size of the debug logs.

**•** When your org accumulates more than 1,000 MB of debug logs, we prevent users in the org from adding or editing trace flags. To
add or edit trace flags so that you can generate more logs after you reach the limit, delete some debug logs.


Apex Developer Guide Debugging Apex

Inspecting the Debug Log Sections

After you generate a debug log, the type and amount of information listed depends on the filter values you set for the user. However,
the format for a debug log is always the same.

Note: Session IDs are replaced with "SESSION_ID_REMOVED" in Apex debug logs

A debug log has the following sections.

**Header**
The header contains the following information.

**•** The version of the API used during the transaction.

**•** The log category and level used to generate the log. For example:

The following is an example of a header.

```
     66.0

     APEX_CODE,DEBUG;APEX_PROFILING,INFO;CALLOUT,INFO;DB,INFO;SYSTEM,DEBUG;VALIDATION,INFO;VISUALFORCE,INFO;

     WORKFLOW,INFO

```

