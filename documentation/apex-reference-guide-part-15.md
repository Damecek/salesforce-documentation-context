If the redirect code contains an invalid integer, an error message is displayed when `PageReference` is used by Salesforce for
redirection.

Return Value

Type: System.PageReference

### Packaging Class

Contains a method for obtaining information about managed and unlocked packages.


### Apex Reference Guide Pattern Class

Namespace

System

Usage

In the context of a package, use the getCurrentPackageId method to retrieve the packageID.

IN THIS SECTION:

#### Packaging Methods Packaging Methods The following are methods for Packaging .

IN THIS SECTION:

##### getCurrentPackageId()

Returns the context `packageID` in managed and unlocked packages.

##### getCurrentPackageId()

Returns the context `packageID` in managed and unlocked packages.

Signature

```
   public String getCurrentPackageId()

```

Return Value

Type: String

Usage

For managed packages, this method can be combined with isCurrentUserLicensedForPackage(packageId) to retrieve the `packageId`
at runtime. Then, use `packageId` to confirm that the contextual user is licensed to use that managed package.

### Pattern Class

Represents a compiled representation of a regular expression.

Namespace

System

#### Pattern Methods

### The following are methods for Pattern .


Apex Reference Guide Pattern Class

IN THIS SECTION:

##### compile(regExp)

Compiles the regular expression into a Pattern object.

##### matcher(stringtoMatch)

Creates a Matcher object that matches the input string _`stringtoMatch`_ against this Pattern object.

matches(regExp, stringtoMatch)
Compiles the regular expression _`regExp`_ and tries to match it against the specified string. This method returns `true` if the
specified string matches the regular expression, `false` otherwise.

pattern()
Returns the regular expression from which this Pattern object was compiled.

quote(yourString)
Returns a string that can be used to create a pattern that matches the string _`yourString`_ as if it were a literal pattern.

split(regExp)
Returns a list that contains each substring of the String that matches this pattern.

split(regExp, limit)
Returns a list that contains each substring of the String that is terminated either by the regular expression _`regExp`_ that matches
this pattern, or by the end of the String.

##### compile(regExp)

Compiles the regular expression into a Pattern object.

Signature

```
   public static Pattern compile(String regExp)

```

Parameters

```
   regExp
```

Type: String

Return Value

Type: System.Pattern

##### matcher(stringtoMatch)

Creates a Matcher object that matches the input string _`stringtoMatch`_ against this Pattern object.

Signature

```
   public Matcher matcher(String stringtoMatch)

```

Parameters

```
   stringtoMatch
```

Type: String


Apex Reference Guide Pattern Class

Return Value

Type: Matcher

##### matches(regExp, stringtoMatch)

Compiles the regular expression _`regExp`_ and tries to match it against the specified string. This method returns `true` if the specified
string matches the regular expression, `false` otherwise.

Signature

```
   public static Boolean matches(String regExp, String stringtoMatch)

```

Parameters

```
   regExp
```

Type: String

```
   stringtoMatch
```

Type: String

Return Value

Type: Boolean

Usage

If a pattern is to be used multiple times, compiling it once and reusing it is more efficient than invoking this method each time.

Example

Note that the following code example:

```
   Pattern.matches(regExp, input);

```

produces the same result as this code example:

```
   Pattern.compile(regex).

   matcher(input).matches();

##### pattern()

```

Returns the regular expression from which this Pattern object was compiled.

Signature

```
   public String pattern()

```

Return Value

Type: String


Apex Reference Guide Pattern Class

##### quote(yourString)

Returns a string that can be used to create a pattern that matches the string _`yourString`_ as if it were a literal pattern.

Signature

```
   public static String quote(String yourString)

```

Parameters

```
   yourString
```

Type: String

Return Value

Type: String

Usage

Metacharacters (such as `$` or `^` ) and escape sequences in the input string are treated as literal characters with no special meaning.

##### split(regExp)

Returns a list that contains each substring of the String that matches this pattern.

Signature

```
   public String[] split(String regExp)

```

Parameters

```
   regExp
```

Type: String

Return Value

Type: String[]

Note: In API version 34.0 and earlier, a zero-width _`regExp`_ value produces an empty list item at the beginning of the method’s
output.

Usage

The substrings are placed in the list in the order in which they occur in the String. If _`regExp`_ does not match the pattern, the resulting
list has just one element containing the original String.

##### split(regExp, limit)

Returns a list that contains each substring of the String that is terminated either by the regular expression _`regExp`_ that matches this
pattern, or by the end of the String.


### Apex Reference Guide ParentJobResult Enum

Signature

```
   public String[] split(String regExp, Integer limit)

```

Parameters

```
   regExp
```

Type: String

```
   limit
```

Type: Integer

(Optional) Controls the number of times the pattern is applied and therefore affects the length of the list.

**•** If _`limit`_ is greater than zero:

**–** The pattern is applied a maximum of ( _`limit`_      - 1) times.

**–** The list’s length is no greater than _`limit`_ .

**–** The list’s last entry contains all input beyond the last matched delimiter.

**•** If _`limit`_ is non-positive, the pattern is applied as many times as possible, and the list can have any length.

**•** If _`limit`_ is zero, the pattern is applied as many times as possible, the list can have any length, and trailing empty strings are
discarded.

Return Value

Type: String[]

Note: In API version 34.0 and earlier, a zero-width _`regExp`_ value produces an empty list item at the beginning of the method’s
output.

### ParentJobResult Enum

Specifies the success or exception status of the parent Queueable job to which a Transaction Finalizer is attached.

Enum Values

The following are the values of the `System.ParentJobResult` enum.

**Value** **Description**

`SUCCESS` Queueable job succeeded.

`UNHANDLED_EXCEPTION` Queueable job resulted in an exception.

### Queueable Interface

Enables the asynchronous execution of Apex jobs that can be monitored.

Namespace

System


Apex Reference Guide Queueable Interface

Usage

#### To execute Apex as an asynchronous job, implement the Queueable interface and add the processing logic in your implementation
##### of the execute method.

#### To implement the Queueable interface, you must first declare a class with the implements keyword as follows:

```
   public class MyQueueableClass implements Queueable {

```

Next, your class must provide an implementation for the following method:

```
   public void execute(QueueableContext context) {

      // Your code here

   }

```

Your class and method implementation must be declared as `public` or `global` .

To submit your class for asynchronous execution, call the `System.enqueueJob` by passing it an instance of your class implementation
#### of the Queueable interface as follows:

```
   ID jobID = System.enqueueJob(new MyQueueableClass());

```

IN THIS SECTION:

#### Queueable Methods

Queueable Example Implementation

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

#### Queueable Methods The following are methods for Queueable .

IN THIS SECTION:

##### execute(context)

Executes the queueable job.

##### execute(context)

Executes the queueable job.

Signature

```
   public void execute(QueueableContext context)

```

Parameters

```
   context
```

Type: QueueableContext

Contains the job ID.


Apex Reference Guide Queueable Interface

Return Value

Type: Void

#### Queueable Example Implementation This example is an implementation of the Queueable interface. The execute method in this example inserts a new account.

```
   public class AsyncExecutionExample implements Queueable {

      public void execute(QueueableContext context) {

        Account a = new Account(Name='Acme',Phone='(415) 555-1212');

        insert a;

      }

   }

```

To add this class as a job on the queue, call this method:

```
   ID jobID = System.enqueueJob(new AsyncExecutionExample());

```

After you submit your queueable class for execution, the job is added to the queue and will be processed when system resources become
available. You can monitor the status of your job programmatically by querying AsyncApexJob or through the user interface in Setup
by entering _`Apex Jobs`_ in the `Quick Find` box, then selecting **Apex Jobs** .

To query information about your submitted job, perform a SOQL query on AsyncApexJob by filtering on the job ID that the
`System.enqueueJob` method returns. This example uses the jobID variable that was obtained in the previous example.

```
   AsyncApexJob jobInfo = [SELECT Status,NumberOfErrors FROM AsyncApexJob WHERE Id=:jobID];

```

Similar to future jobs, queueable jobs don’t process batches, and so the number of processed batches and the number of total batches
are always zero.

Testing Queueable Jobs

This example shows how to test the execution of a queueable job in a test method. A queueable job is an asynchronous process. To
ensure that this process runs within the test method, the job is submitted to the queue between the `Test.startTest` and
`Test.stopTest` block. The system executes all asynchronous processes started in a test method synchronously after the
`Test.stopTest` statement. Next, the test method verifies the results of the queueable job by querying the account that the job
created.

```
   @isTest

   public class AsyncExecutionExampleTest {

      static testmethod void test1() {

        // startTest/stopTest block to force async processes

        // to run in the test.

        Test.startTest();

        System.enqueueJob(new AsyncExecutionExample());

        Test.stopTest();

        // Validate that the job has run

        // by verifying that the record was created.

        // This query returns only the account created in test context by the

        // Queueable class method.

        Account acct = [SELECT Name,Phone FROM Account WHERE Name='Acme' LIMIT 1];

        System.assertNotEquals(null, acct);

        System.assertEquals('(415) 555-1212', acct.Phone);

```


### Apex Reference Guide QueueableContext Interface

```
      }

   }

```

Note: The ID of a queueable Apex job isn’t returned in test context— `System.enqueueJob` returns `null` in a running test.

### QueueableContext Interface Represents the parameter type of the execute() method in a class that implements the Queueable interface and contains the

job ID. This interface is implemented internally by Apex.

Namespace

System

#### QueueableContext Methods

### The following are methods for QueueableContext .

IN THIS SECTION:

##### getJobId()
### Returns the ID of the submitted job that uses the Queueable interface.

##### getJobId()

### Returns the ID of the submitted job that uses the Queueable interface.

Signature

```
   public ID getJobId()

```

Return Value

Type: ID

The ID of the submitted job.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

### QueueableDuplicateSignature Class

Used in the `AsyncOptions` class to store the queueable job signature in the `DuplicateSignature` property.

Namespace

System


### Apex Reference Guide QueueableDuplicateSignature.Builder Class

IN THIS SECTION:

#### QueueableDuplicateSignature Methods

SEE ALSO:

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)

#### QueueableDuplicateSignature Methods The following are methods for QueueableDuplicateSignature .

IN THIS SECTION:

##### toString()

Returns the duplicate signature as a string value.

##### **`toString()`**

Returns the duplicate signature as a string value.

Signature

```
   public String toString()

```

Return Value

Type: String

### QueueableDuplicateSignature.Builder Class

Build a unique signature for your queueable job using this inner builder class. The `build()` class method builds a
#### QueueableDuplicateSignature object, with input from the addId(), addInteger(), and addString() methods.

Use the `DuplicateSignature` property in the `AsyncOptions` class to store the queueable job signature. Enqueue your job
by using the `System.enqueueJob()` with the `AsyncOptions` parameter.

Namespace

System

Examples

This example builds the async job signature with UserId and the string `MyQueueable` .

```
   AsyncOptions options = new AsyncOptions();

   options.DuplicateSignature = new System.QueueableDuplicateSignature.Builder()

                       .addId(UserInfo.getUserId())

                       .addString('MyQueueable')

                       .build();

   try {

      System.enqueueJob(new MyQueueable(), options);

```


Apex Reference Guide QueueableDuplicateSignature.Builder Class

```
   } catch (DuplicateMessageException ex) {

      //Exception is thrown if there is already an enqueued job with the same signature

      Assert.areEqual('Attempt to enqueue job with duplicate queueable signature',

        ex.getMessage());

   }

```

This example builds the async job signature using ApexClass Id and the hash value of an sObject.

```
   AsyncOptions options = new AsyncOptions();

   options.DuplicateSignature = new QueueableDuplicateSignature.Builder()

                       .addInteger(System.hashCode(someAccount))

                       .addId([SELECT Id FROM ApexClass

                          WHERE Name='MyQueueable'].Id)

                       .build();

   System.enqueueJob(new MyQueueable(), options);

```

IN THIS SECTION:

#### QueueableDuplicateSignature.Builder Methods

SEE ALSO:

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)

#### QueueableDuplicateSignature.Builder Methods The following are methods for QueueableDuplicateSignature.Builder .

IN THIS SECTION:

addId(inputId)
Adds an ID to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the
`AsyncOptions` parameter to `System.enqueueJob()` .

addInteger(inputInteger)
Adds an integer to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the
`AsyncOptions` parameter to `System.enqueueJob()` .

addString(inputString)
Adds a string to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the
`AsyncOptions` parameter to `System.enqueueJob()` .

build()
Builds a unique signature for a queueable job. You can then enqueue the job by using the signature as the `AsyncOptions`
parameter to `System.enqueueJob()` .

getMaxSize()
Gets the maximum size of the queueable job signature in bytes.

getRemainingSize()
Gets the remaining size of the queueable job signature in bytes, after subtracting what is already used by the signature from the
maximum allowed number.

getSize()
Gets the size of the queueable job signature in bytes.


Apex Reference Guide QueueableDuplicateSignature.Builder Class

##### **`addId(inputId)`**

Adds an ID to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the `AsyncOptions`
parameter to `System.enqueueJob()` .

Signature

```
   public System.QueueableDuplicateSignature.Builder addId(Id id)

```

Parameters

```
   inputId
```

Type: Id

Return Value

Type: QueueableDuplicateSignature.Builder

##### **`addInteger(inputInteger)`**

Adds an integer to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the
`AsyncOptions` parameter to `System.enqueueJob()` .

Signature

```
   public System.QueueableDuplicateSignature.Builder addInteger(Integer i)

```

Parameters

```
   inputInteger
```

Type: Integer

Return Value

Type: QueueableDuplicateSignature.Builder

##### **`addString(inputString)`**

Adds a string to build a unique signature for a queueable job. You can then enqueue the job by using the signature as the
`AsyncOptions` parameter to `System.enqueueJob()` .

Signature

```
   public System.QueueableDuplicateSignature.Builder addString(String s)

```

Parameters

```
   inputString
```

Type: String


Apex Reference Guide QueueableDuplicateSignature.Builder Class

Return Value

Type: QueueableDuplicateSignature.Builder

##### **`build()`**

Builds a unique signature for a queueable job. You can then enqueue the job by using the signature as the `AsyncOptions` parameter
to `System.enqueueJob()` .

Signature

```
   public System.QueueableDuplicateSignature build()

```

Return Value

Type: QueueableDuplicateSignature Class

##### **`getMaxSize()`**

Gets the maximum size of the queueable job signature in bytes.

Signature

```
   public Integer getMaxSize()

```

Return Value

Type: Integer

##### **`getRemainingSize()`**

Gets the remaining size of the queueable job signature in bytes, after subtracting what is already used by the signature from the maximum
allowed number.

Signature

```
   public Integer getRemainingSize()

```

Return Value

Type: Integer

##### **`getSize()`**

Gets the size of the queueable job signature in bytes.

Signature

```
   public Integer getSize()

```


### Apex Reference Guide QuickAction Class

Return Value

Type: Integer

### QuickAction Class

Use Apex to request and process actions on objects that allow custom fields, on objects that appear in a Chatter feed, or on objects that
are available globally.

Namespace

System

Example

In this sample, the trigger determines if the new contacts to be inserted are created by a quick action. If so, it sets the `WhereFrom__c`
custom field to a value that depends on whether the quick action is global or local to the contact. Otherwise, if the inserted contacts
don’t originate from a quick action, the `WhereFrom__c` field is set to `'NoAction'` .

```
   trigger accTrig2 on Contact (before insert) {

      for (Contact c : Trigger.new) {

        if (c.getQuickActionName() == QuickAction.CreateContact) {

           c.WhereFrom__c = 'GlobaActionl';

        } else if (c.getQuickActionName() == Schema.Account.QuickAction.CreateContact) {

           c.WhereFrom__c = 'AccountAction';

        } else if (c.getQuickActionName() == null) {

           c.WhereFrom__c = 'NoAction';

        } else {

           System.assert(false);

        }

      }

   }

```

This sample performs a global action— `QuickAction.CreateContact` –on the passed-in contact object.

```
   public Id globalCreate(Contact c) {

      QuickAction.QuickActionRequest req = new QuickAction.QuickActionRequest();

      req.quickActionName = QuickAction.CreateContact;

      req.record = c;

      QuickAction.QuickActionResult res = QuickAction.performQuickAction(req);

      return c.id;

   }

```

SEE ALSO:

QuickActionRequest Class

QuickActionResult Class

#### QuickAction Methods

### The following are methods for QuickAction . All methods are static.


Apex Reference Guide QuickAction Class

IN THIS SECTION:

##### describeAvailableQuickActions(parentType)

Returns metadata information for the available quick actions of the provided parent object.

describeQuickActions(sObjectNames)
Returns the metadata information for the provided quick actions.

performQuickAction(quickActionRequest)
Performs the quick action specified in the quick action request and returns the action result.

performQuickAction(quickActionRequest, allOrNothing)
Performs the quick action specified in the quick action request with the option for partial success, and returns the result.

performQuickActions(quickActionRequests)
Performs the quick actions specified in the quick action request list and returns action results.

performQuickActions(quickActionRequests, allOrNothing)
Performs the quick actions specified in the quick action request list with the option for partial success, and returns action results.

##### describeAvailableQuickActions(parentType)

Returns metadata information for the available quick actions of the provided parent object.

Signature

```
   public static List<QuickAction.DescribeAvailableQuickActionResult>

   describeAvailableQuickActions(String parentType)

```

Parameters

```
   parentType
```

Type: String

The parent object type. This can be an object type name ('Account') or 'Global' (meaning that this method is called at a global level
and not an entity level).

Return Value

Type: List<QuickAction.DescribeAvailableQuickActionResult>

The metadata information for the available quick actions of the parent object.

Example

```
   // Called for Account entity.

   List<QuickAction.DescribeAvailableQuickActionResult> result1 =

      QuickAction.DescribeAvailableQuickActions('Account');

   // Called at global level, not entity level.

   List<QuickAction.DescribeAvailableQuickActionResult> result2 =

      QuickAction.DescribeAvailableQuickActions('Global');

```


Apex Reference Guide QuickAction Class

##### describeQuickActions(sObjectNames)

Returns the metadata information for the provided quick actions.

Signature

```
   public static List<QuickAction.DescribeQuickActionResult>

   describeQuickActions(List<String> sObjectNames)

```

Parameters

```
   sObjectNames
```

Type: List<String>

The names of the quick actions. The quick action name can contain the entity name if it is at the entity level
('Account.QuickCreateContact'), or 'Global' if used for the action at the global level ('Global.CreateNewContact').

Return Value

Type: List<QuickAction.DescribeQuickActionResult>

The metadata information for the provided quick actions.

Example

```
   // First 3 parameter values are for actions at the entity level.

   // Last parameter is for an action at the global level.

   List<QuickAction.DescribeQuickActionResult> result =

      QuickAction.DescribeQuickActions(new List<String> {

        'Account.QuickCreateContact', 'Opportunity.Update1',

        'Contact.Create1', 'Global.CreateNewContact' });

##### performQuickAction(quickActionRequest)

```

Performs the quick action specified in the quick action request and returns the action result.

Signature

```
   public static QuickAction.QuickActionResult

   performQuickAction(QuickAction.QuickActionRequest quickActionRequest)

```

Parameters

```
   quickActionRequest
```

Type: QuickAction.QuickActionRequest

Return Value

Type: QuickAction.QuickActionResult


Apex Reference Guide QuickAction Class

##### performQuickAction(quickActionRequest, allOrNothing)

Performs the quick action specified in the quick action request with the option for partial success, and returns the result.

Signature

```
   public static QuickAction.QuickActionResult

   performQuickAction(QuickAction.QuickActionRequest quickActionRequest, Boolean

   allOrNothing)

```

Parameters

```
   quickActionRequest
```

Type: QuickAction.QuickActionRequest

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` for this argument and a record fails, the remainder of
the DML operation can still succeed. This method returns a result object that can be used to verify which records succeeded, which
failed, and why.

Return Value

Type: QuickAction.QuickActionResult

##### performQuickActions(quickActionRequests)

Performs the quick actions specified in the quick action request list and returns action results.

Signature

```
   public static List<QuickAction.QuickActionResult>

   performQuickActions(List<QuickAction.QuickActionRequest> quickActionRequests)

```

Parameters

```
   quickActionRequests
```

Type: List<QuickAction.QuickActionRequest>

Return Value

Type: List<QuickAction.QuickActionResult>

##### performQuickActions(quickActionRequests, allOrNothing)

Performs the quick actions specified in the quick action request list with the option for partial success, and returns action results.


### Apex Reference Guide Quiddity Enum

Signature

```
   public static List<QuickAction.QuickActionResult>

   performQuickActions(List<QuickAction.QuickActionRequest> quickActionRequests, Boolean

   allOrNothing)

```

Parameters

```
   quickActionRequests
```

Type: List<QuickAction.QuickActionRequest>

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` for this argument and a record fails, the remainder of
the DML operation can still succeed. This method returns a result object that can be used to verify which records succeeded, which
failed, and why.

Return Value

Type: List<QuickAction.QuickActionResult>

### Quiddity Enum

Specifies a Quiddity value used by the methods in the System.Request class

Enum Values

The following are the values of the `System.Quiddity` enum.

**Value** **Description**

`ANONYMOUS` Execution event is an anonymous Apex block.

`AURA` Execution event is an Aura component.

`BATCH_ACS` Execution event is an API Query Cursor driven batch Apex.

`BATCH_APEX` Execution event is a batch Apex job.

`BATCH_CHUNK_PARALLEL` Not used in API version 63.0 and later.

`BATCH_CHUNK_SERIAL` Execution event is chunks of a batch Apex job running in serial.

`BULK_API` Execution event is a bulk API request.

`COMMERCE_INTEGRATION` Execution event is an Apex integration for B2B Commerce.

`DISCOVERABLE_LOGIN` Execution event is Login Discoverable login page used by external users to log in
to an Experience Cloud site.

`EXTERNAL_SERVICE_CALLBACK` Execution event is an External Services asynchronous callback function.

`FUNCTION_CALLBACK` Execution event is a callback function.

`FUTURE` Execution event is a future method.


### Apex Reference Guide RemoteObjectController

**Value** **Description**

`INBOUND_EMAIL_SERVICE` Execution event is an Apex inbound email service.

`INVOCABLE_ACTION` Execution event is an invocable action.

`PLATFORM_EVENT_PUBLISH_CALLBACK` Execution event is an Apex publish callback for platform events.

`POST_INSTALL_SCRIPT` Execution event is a managed package install or upgrade.

`QUEUEABLE` Execution event is a queueable Apex operation.

`QUICK_ACTION` Execution event is a quick action.

`REMOTE_ACTION` Execution event is a remote action.

`REST` Execution event is an Apex RESTful Web service.

`RUNTEST_ASYNC` Execution event is Apex tests running asynchronously.

`RUNTEST_DEPLOY` Execution event is Apex tests run during deployment.

`RUNTEST_SYNC` Execution event is Apex tests running synchronously.

`RUN_INTEGRATION_TESTS` Execution event is Apex integration tests running.

`SCHEDULED` Execution event is a scheduled Apex job.

`SOAP` Execution event is an Apex SOAP Web service.

`SYNCHRONOUS` Execution event is a synchronous Apex operation.

`TRANSACTION_FINALIZER_QUEUEABLE` Execution event is a queueable job with transaction finalizers attached.

`VF` Execution event is triggered by a Visualforce page.

### RemoteObjectController Use RemoteObjectController to access the standard Visualforce Remote Objects operations in your Remote Objects override

methods.

Namespace

System

Usage

### RemoteObjectController is supported only for use within Remote Objects methods. See Overriding Default Remote Objects Operations in the Visualforce Developer’s Guide for examples of how to use RemoteObjectController with your Visualforce

pages.

### RemoteObjectController Methods The following are methods for RemoteObjectController . All methods are static.


Apex Reference Guide RemoteObjectController

IN THIS SECTION:

##### create(type, fields)

Create a record in the database.

##### del(type, recordIds)

Delete records from the database.

retrieve(type, fields, criteria)
Retrieve records from the database.

update(type, recordIds, fields)
Update records in the database.

##### create(type, fields)

Create a record in the database.

Signature

```
   public static Map<String,Object> create(String type, Map<String,Object> fields)

```

Parameters

```
   type
```

Type: String

The sObject type on which create is being called.

```
   fields
```

Type: Map<String,Object>

The fields and values to set on the new record.

Return Value

Type: Map<String,Object>

The return value is a map that represents the result of the Remote Objects operation. What is returned depends on the results of the
call.

**Success**
A map that contains a single element with the ID of the record created. For example, `{ id: '` _**`recordId`**_ `' }` .

**Failure**
A map that contains a single element with the error message for the overall operation. For example, `{ error:`

`'` _**`errorMessage`**_ `'` `}` .

##### del(type, recordIds)

Delete records from the database.

Signature

```
   public static Map<String,Object> del(String type, List<String> recordIds)

```


Apex Reference Guide RemoteObjectController

Parameters

```
   type
```

Type: String

The sObject type on which delete is being called.

```
   recordIds
```

Type: List<String>

The IDs of the records to be deleted.

Return Value

Type: Map<String,Object>

The return value is a map that represents the result of the Remote Objects operation. What is returned depends on how the method
was called and the results of the call.

**Single Delete—Success**
A map that contains a single element with the ID of the record that was deleted. For example, `{ id: '` _**`recordId`**_ `'` `}` .

**Batch Delete—Success**
A map that contains a single element, an array of Map<String,Object> elements. Each element contains the ID of a record that was
deleted and an array of errors, if there were any, for that record’s individual delete. For example, `{ results: [ { id:`

`'` _**`recordId`**_ `', errors:` `['` _**`errorMessage`**_ `', ...]}, ...] }` .

**Single and Batch Delete—Failure**
A map that contains a single element with the error message for the overall operation. For example, `{ error:`

`'` _**`errorMessage`**_ `' }` .

##### retrieve(type, fields, criteria)

Retrieve records from the database.

Signature

```
   public static Map<String,Object> retrieve(String type, List<String> fields,

   Map<String,Object> criteria)

```

Parameters

```
   type
```

Type: String

The sObject type on which retrieve is being called.

```
   fields
```

Type: List<String>

The fields to retrieve for each record.

```
   criteria
```

Type: Map<String,Object>

The criteria to use when performing the query.


Apex Reference Guide RemoteObjectController

Return Value

Type: Map<String,Object>

The return value is a map that represents the result of the Remote Objects operation. What is returned depends on the results of the
call.

**Success**
A map that contains the following elements.

**•** `records` : An array of records that match the query conditions.

**•** `type` : A string that indicates the type of the sObject that was retrieved.

**•** `size` : The number of records in the response.

**Failure**
A map that contains a single element with the error message for the overall operation. For example, `{ error:`

`'` _**`errorMessage`**_ `'` `}` .

##### update(type, recordIds, fields)

Update records in the database.

Signature

```
   public static Map<String,Object> update(String type, List<String> recordIds,

   Map<String,Object> fields)

```

Parameters

```
   type
```

Type: String

The sObject type on which update is being called.

```
   recordIds
```

Type: List<String>

The IDs of the records to be updated.

```
   fields
```

Type: Map<String,Object>

The fields to update, and the value to update each field with.

Return Value

Type: Map<String,Object>

The return value is a map that represents the result of the Remote Objects operation. What is returned depends on how the method
was called and the results of the call.

**Single Update—Success**
A map that contains a single element with the ID of the record that was updated. For example, `{ id: '` _**`recordId`**_ `'` `}` .

**Batch Update—Success**
A map that contains a single element, an array of Map<String,Object> elements. Each element contains the ID of the record updated
and an array of errors, if there were any, for that record’s individual update. For example, `{ results: [ { id: '` _**`recordId`**_ `',`
`errors:` `['` _**`errorMessage`**_ `', ...]}, ...] }` .


### Apex Reference Guide Request Class

**Single and Batch Update—Failure**
A map that contains a single element with the error message for the overall operation. For example, `{ error:`

`'` _**`errorMessage`**_ `'` `}` .

### Request Class

Contains methods to obtain the request ID and Quiddity value of the current Salesforce request.

Namespace

System

Usage

Use the Request class to detect the current Apex context at runtime. The methods in the Request class obtain a unique request ID and
the Quiddity value that represent the current Apex execution type. These values can also be used to correlate with debug and event
logs.

**•** The request ID represents an individual transaction, but may not be universally unique. The request ID is present in the debug logs
that are triggered by the request.

**•** The request ID and Quiddity values are the same as in the event log files of the Apex Execution event type used in Event Monitoring.

Example

This example code shows how to obtain current Apex code context by retrieving the request ID and Quiddity value of the current request.

```
   //Get info about the current request

   Request reqInfo = Request.getCurrent();

   //Get the identifier for this request, which is universally unique

   //Same as REQUEST_ID in event monitoring

   String currentRequestId = reqInfo.getRequestId();

   //Enum representing how Apex is running. e.g. BULK_API vs LIGHTNING

   Quiddity currentType = reqInfo.getQuiddity();

   //Use this with a switch statement,

   //instead of checking System.isFuture() || System.isQueueable() || ...

```

IN THIS SECTION:

#### Request Methods Request Methods

### The following are methods for Request .

IN THIS SECTION:

getCurrent()
Returns the current Request object that contains the request ID and Quiddity value.


### Apex Reference Guide ResetPasswordResult Class

##### getQuiddity()

Returns the Quiddity value of the current Request object.

##### getRequestId()

Returns the request ID of the current Request object.

##### getCurrent()

Returns the current Request object that contains the request ID and Quiddity value.

Signature

```
   public static System.Request getCurrent()

```

Return Value

Type: System.Request

##### getQuiddity()

Returns the Quiddity value of the current Request object.

Signature

```
   public System.Quiddity getQuiddity()

```

Return Value

Type: System.Quiddity

Uses the values from the Quiddity enum. This value identifies the type of execution event associated with the current request.

##### getRequestId()

Returns the request ID of the current Request object.

Signature

```
   public String getRequestId()

```

Return Value

Type: String

### ResetPasswordResult Class

Represents the result of a password reset.

Namespace

System


### Apex Reference Guide RestContext Class

#### ResetPasswordResult Methods The following are instance methods for ResetPasswordResult .

IN THIS SECTION:

##### getPassword()

Returns the password generated by the `System.resetPassword` method call.

##### getPassword()

Returns the password generated by the `System.resetPassword` method call.

Signature

```
   public String getPassword()

```

Return Value

Type: String

### RestContext Class

Contains the `RestRequest` and `RestResponse` objects.

Namespace

System

Usage

Use the `System.RestContext` class to access the `RestRequest` and `RestResponse` objects in your Apex REST methods.

Sample

### The following example shows how to use RestContext to access the RestRequest and RestResponse objects in an Apex

REST method.

```
   @RestResource(urlMapping='/MyRestContextExample/*')

   global with sharing class MyRestContextExample {

      @HttpGet

      global static Account doGet() {

        RestRequest req = RestContext.request;

        RestResponse res = RestContext.response;

        String accountId = req.requestURI.substring(req.requestURI.lastIndexOf('/')+1);

        Account result = [SELECT Id, Name, Phone, Website FROM Account WHERE Id =

   :accountId];

        return result;

      }

```


### Apex Reference Guide RestRequest Class

```
   }

#### RestContext Properties The following are properties for RestContext .

```

IN THIS SECTION:

##### request
### Returns the RestRequest for your Apex REST method.

##### response

Returns the `RestResponse` for your Apex REST method.

##### request

### Returns the RestRequest for your Apex REST method.

Signature

```
   public RestRequest request {get; set;}

```

Property Value

Type: System.RestRequest

##### response

Returns the `RestResponse` for your Apex REST method.

Signature

```
   public RestResponse response {get; set;}

```

Property Value

Type: System.RestResponse

### RestRequest Class

Use the `System.RestRequest` class to access and pass request data in a RESTful Apex method.

Namespace

System


Apex Reference Guide RestRequest Class

Usage

An Apex RESTful Web service method is defined using one of the REST annotations. For more information about Apex RESTful Web
[service, see Exposing Apex Classes as REST Web Services.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_rest.htm)

Example: An Apex Class with REST Annotated Methods

The following example shows you how to implement the Apex REST API in Apex. This class exposes three methods that each handle a
different HTTP request: GET, DELETE, and POST. You can call these annotated methods from a client by issuing HTTP requests.

```
   @RestResource(urlMapping='/Account/*')

   global with sharing class MyRestResource {

      @HttpDelete

      global static void doDelete() {

        RestRequest req = RestContext.request;

        RestResponse res = RestContext.response;

        String accountId = req.requestURI.substring(req.requestURI.lastIndexOf('/')+1);

        Account account = [SELECT Id FROM Account WHERE Id = :accountId];

        delete account;

      }

      @HttpGet

      global static Account doGet() {

        RestRequest req = RestContext.request;

        RestResponse res = RestContext.response;

        String accountId = req.requestURI.substring(req.requestURI.lastIndexOf('/')+1);

        Account result = [SELECT Id, Name, Phone, Website FROM Account WHERE Id =

   :accountId];

        return result;

      }

     @HttpPost

      global static String doPost(String name,

        String phone, String website) {

        Account account = new Account();

        account.Name = name;

        account.phone = phone;

        account.website = website;

        insert account;

        return account.Id;

      }

   }

```

IN THIS SECTION:

RestRequest Constructors

RestRequest Properties

RestRequest Methods


Apex Reference Guide RestRequest Class

#### RestRequest Constructors The following are constructors for RestRequest .

IN THIS SECTION:

##### RestRequest()

Creates a new instance of the `System.RestRequest` class.

##### RestRequest()

Creates a new instance of the `System.RestRequest` class.

Signature

```
   public RestRequest()

#### RestRequest Properties The following are properties for RestRequest . Note: Although the RestRequest Map properties are read-only, their contents are read-write. To modify a RestRequest
```

header or parameter, use the associated `addHeader` and `addParameter` methods instead of modifying the Map values
directly.

IN THIS SECTION:

##### headers

Returns the headers that are received by the request.

httpMethod
Returns one of the supported HTTP request methods.

params
Returns the parameters that are received by the request.

remoteAddress
Returns the IP address of the client making the request.

requestBody
Returns or sets the body of the request.

requestURI
Returns or sets everything after the host in the HTTP request string.

resourcePath
Returns the REST resource path for the request.

##### headers

Returns the headers that are received by the request.


Apex Reference Guide RestRequest Class

Signature

```
   public Map<String, String> headers {get; set;}

```

Property Value

Type: Map<String, String>

##### httpMethod

Returns one of the supported HTTP request methods.

Signature

```
   public String httpMethod {get; set;}

```

Property Value

Type: String

Possible values returned:

**•** DELETE

**•** GET

**•** HEAD

**•** PATCH

**•** POST

**•** PUT

##### params

Returns the parameters that are received by the request.

Signature

```
   public Map <String, String> params {get; set;}

```

Property Value

Type: Map<String, String>

##### remoteAddress

Returns the IP address of the client making the request.

Signature

```
   public String remoteAddress {get; set;}

```


Apex Reference Guide RestRequest Class

Property Value

Type: String

##### requestBody

Returns or sets the body of the request.

Signature

```
   public Blob requestBody {get; set;}

```

Property Value

Type: Blob

Usage

If the Apex method has no parameters, then Apex REST copies the HTTP request body into the `RestRequest.requestBody`
property. If there are parameters, then Apex REST attempts to deserialize the data into those parameters and the data won't be deserialized
into the `RestRequest.requestBody` property.

##### requestURI

Returns or sets everything after the host in the HTTP request string.

Signature

```
   public String requestURI {get; set;}

```

Property Value

Type: String

Example

For example, if the request string is _`https://instance.salesforce.com/services/apexrest/Account/`_ then
##### the requestURI is /Account/ . resourcePath

Returns the REST resource path for the request.

Signature

```
   public String resourcePath {get; set;}

```

Property Value

Type: String


Apex Reference Guide RestRequest Class

Example

For example, if the Apex REST class defines a `urlMapping` of `/MyResource/*`, the `resourcePath` property returns
`/services/apexrest/MyResource/*` .

#### RestRequest Methods The following are methods for RestRequest . All are instance methods. Note: At run time, you typically don't add a header or parameter to the RestRequest object manually because they are
##### automatically deserialized into the corresponding properties. The addHeader and addParameter methods are intended
#### for unit testing, so you can add header or parameter values to the RestRequest object without recreating the REST method

call. Use these methods instead of calling a Map method directly.

IN THIS SECTION:

##### addHeader(name, value)

Adds a header to the request header map in an Apex test.

addParameter(name, value)
Adds a parameter to the request params map in an Apex test.

##### addHeader(name, value)

Adds a header to the request header map in an Apex test.

Signature

```
   public Void addHeader(String name, String value)

```

Parameters

```
   name
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void

Usage

This method is intended for unit testing of Apex REST classes.

The following headers aren't allowed:

**•** cookie

**•** set-cookie

**•** set-cookie2

**•** content-length


### Apex Reference Guide RestResponse Class

**•** authorization

If any of these headers are used, an Apex exception is thrown.

##### addParameter(name, value)

Adds a parameter to the request params map in an Apex test.

Signature

```
   public Void addParameter(String name, String value)

```

Parameters

```
   name
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void

Usage

This method is intended for unit testing of Apex REST classes.

### RestResponse Class

Represents an object used to pass data from an Apex RESTful Web service method to an HTTP response.

Namespace

System

Usage

Use the `System.RestResponse` class to pass response data from an Apex RESTful web service method that is defined using one
[of the REST annotations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotations_rest.htm)

IN THIS SECTION:

#### RestResponse Constructors

RestResponse Properties

RestResponse Methods

#### RestResponse Constructors

### The following are constructors for RestResponse .


Apex Reference Guide RestResponse Class

IN THIS SECTION:

##### RestResponse()

Creates a new instance of the `System.RestResponse` class.

##### RestResponse()

Creates a new instance of the `System.RestResponse` class.

Signature

```
   public RestResponse()

#### RestResponse Properties

##### The following are properties for RestResponse . Note: Although the RestResponse Map properties are read-only, their contents are read-write. To modify a RestResponse
```

header, use the associated `addHeader` method instead of the modifying the Map values directly.

IN THIS SECTION:

##### responseBody

Returns or sets the body of the response.

headers
Returns the headers to be sent to the response.

statusCode
Returns or sets the response status code.

##### responseBody

Returns or sets the body of the response.

Signature

```
   public Blob responseBody {get; set;}

```

Property Value

Type: Blob

Usage

##### The response is either the serialized form of the method return value or it's the value of the responseBody property based on the

following rules:

##### • If the method returns void, then Apex REST returns the response in the responseBody property.

**•** If the method returns a value, then Apex REST serializes the return value as the response. If the return value contains fields with null
value, those fields are not serialized in the response.


Apex Reference Guide RestResponse Class

##### headers

Returns the headers to be sent to the response.

Signature

```
   public Map<String, String> headers {get; set;}

```

Property Value

Type: Map<String, String>

##### statusCode

Returns or sets the response status code.

Signature

```
   public Integer statuscode {get; set;}

```

Property Value

Type: Integer

Status Codes

The following are valid response status codes. The status code is returned by the `RestResponse.statusCode` property.

Note: If you set the `RestResponse.statusCode` property to a value that's not listed in the table, then an HTTP status of
500 is returned with the error message “Invalid status code for HTTP response: nnn” where nnn is the invalid status code value.

**Status Code** **Description**

200 OK

201 CREATED

202 ACCEPTED

204 NO_CONTENT

206 PARTIAL_CONTENT

300 MULTIPLE_CHOICES

301 MOVED_PERMANENTLY

302 FOUND

304 NOT_MODIFIED

400 BAD_REQUEST

401 UNAUTHORIZED

403 FORBIDDEN


Apex Reference Guide RestResponse Class

**Status Code** **Description**

404 NOT_FOUND

405 METHOD_NOT_ALLOWED

406 NOT_ACCEPTABLE

409 CONFLICT

410 GONE

412 PRECONDITION_FAILED

413 REQUEST_ENTITY_TOO_LARGE

414 REQUEST_URI_TOO_LARGE

415 UNSUPPORTED_MEDIA_TYPE

417 EXPECTATION_FAILED

500 INTERNAL_SERVER_ERROR

503 SERVER_UNAVAILABLE

#### RestResponse Methods The following are instance methods for RestResponse .

IN THIS SECTION:

##### addHeader(name, value)

Adds a header to the response header map.

##### addHeader(name, value)

Adds a header to the response header map.

Signature

```
   public Void addHeader(String name, String value)

```

Parameters

```
   name
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void


### Apex Reference Guide SandboxPostCopy Interface

Usage

The following headers aren't allowed:

**•** cookie

**•** set-cookie

**•** set-cookie2

**•** content-length

**•** authorization

**•** Header names that aren't RFC 7230 compliant

If any of these headers are used, an Apex exception is thrown.

### SandboxPostCopy Interface

To make your sandbox environment business ready, automate data manipulation or business logic tasks. Extend this interface and add
methods to perform post-copy tasks, then specify the class during sandbox creation.

Namespace

System

Usage

Create an Apex class that implements this interface. Specify your class during sandbox creation. After your sandbox is created, the
`runApexClass(context)` method in your class runs using the automated process user’s permissions.

Important: The SandboxPostCopy Apex class is executed at the end of the sandbox copy using a special Automated Process
user that isn’t visible within the org. This user doesn’t have access to all object and features; therefore, the Apex script cannot
access all objects and features. If the script fails, run the script after sandbox activation as a user with appropriate permissions.

IN THIS SECTION:

#### SandboxPostCopy Methods

SandboxPostCopy Example Implementation
These examples show a simple implementation of the SandboxPostCopy interface and a test for that implementation. To test your
SandboxPostCopy implementation, use the `System.Test.testSandboxPostCopyScript()` method.

SEE ALSO:

_Tooling API_ [: SandboxInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxinfo.htm)

_Tooling API_ [: SandboxProcess](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxprocess.htm)

#### SandboxPostCopy Methods

### The following method is for SandboxPostCopy .


Apex Reference Guide SandboxPostCopy Interface

IN THIS SECTION:

##### runApexClass(context)

Executes actions in a new sandbox to prepare it for use. For example, add logic to this method to create users, run sanitizing code
on records, and perform other setup tasks.

##### runApexClass(context)

Executes actions in a new sandbox to prepare it for use. For example, add logic to this method to create users, run sanitizing code on
records, and perform other setup tasks.

Signature

```
   public void runApexClass(System.SandboxContext context)

```

Parameters

```
   context
```

Type: System.SandboxContext

The org ID, sandbox ID, and sandbox name for your sandbox. To work with these values, reference
`context.organizationId()`, `context.sandboxId()`, and `context.sandboxName()` in your code.

Return Value

Type: void

#### SandboxPostCopy Example Implementation

These examples show a simple implementation of the SandboxPostCopy interface and a test for that implementation. To test your
SandboxPostCopy implementation, use the `System.Test.testSandboxPostCopyScript()` method.

Important: The SandboxPostCopy Apex class is executed at the end of the sandbox copy using a special Automated Process
user that isn’t visible within the org. This user doesn’t have access to all objects and features; therefore, the Apex script can’t access
all objects and features. If the script fails, run the script after sandbox activation as a user with appropriate permissions.

This example implements the `System.SandboxPostCopy` interface.

```
   global class PrepareMySandbox implements SandboxPostCopy {

      global PrepareMySandbox() {

        // Implementations of SandboxPostCopy must have a no-arg constructor.

        // This constructor is used during the sandbox copy process.

        // You can also implement constructors with arguments, but be aware that

        // they won’t be used by the sandbox copy process (unless as part of the

        // no-arg constructor).

        this(some_args);

      }

      global PrepareMySandbox(String some_args) {

        // Logic for constructor.

      }

```


### Apex Reference Guide Schedulable Interface

```
      global void runApexClass(SandboxContext context) {

        System.debug('Org ID: ' + context.organizationId());

        System.debug('Sandbox ID: ' + context.sandboxId());

        System.debug('Sandbox Name: ' + context.sandboxName());

        // Insert logic here to prepare the sandbox for use.

      }

   }

```

The following example tests the implementation using the `System.Test.testSandboxPostCopyScript()` method. This
method takes four parameters: a reference to a class that implements the SandboxPostCopy interface, and the three fields on the context
object that you pass to the `runApexClass(context)` method. An overload on the method takes an optional Boolean parameter
to indicate if the test must be performed as the Automated Process user.

```
   @isTest

   class PrepareMySandboxTest {

      @isTest

      static void testMySandboxPrep() {

        // Insert logic here to create records of the objects that the class you’re testing

        // manipulates.

        Test.startTest();

        // Replace '00D000000000000' with your sandboxId and

        // execute test script with RunAsAutoProcUser set to true.

        Test.testSandboxPostCopyScript(

           new PrepareMySandbox(), UserInfo.getOrganizationId(),

            '00D000000000000', UserInfo.getOrganizationName(), true);

        Test.stopTest();

        // Insert assert statements here to check that the records you created above have

        // the values you expect.

      }

   }

```

[For more information on testing, see Testing Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing.htm)

### Schedulable Interface

The class that implements this interface can be scheduled to run at different intervals.

Namespace

System

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_scheduler.htm)_ : Scheduler


### Apex Reference Guide SchedulableContext Interface

#### Schedulable Methods The following are methods for Schedulable .

IN THIS SECTION:

##### execute(context)

Executes the scheduled Apex job.

##### execute(context)

Executes the scheduled Apex job.

Signature

```
   public Void execute(SchedulableContext context)

```

Parameters

```
   context
```

Type: System.SchedulableContext

Contains the job ID.

Return Value

Type: Void

### SchedulableContext Interface

#### Represents the parameter type of a method in a class that implements the Schedulable interface and contains the scheduled job

ID. This interface is implemented internally by Apex.

Namespace

System

SEE ALSO:

Schedulable Interface

#### SchedulableContext Methods

### The following are methods for SchedulableContext .

IN THIS SECTION:

getTriggerId()
Returns the ID of the CronTrigger scheduled job.


### Apex Reference Guide Schema Class

##### getTriggerId()

Returns the ID of the CronTrigger scheduled job.

Signature

```
   public Id getTriggerId()

```

Return Value

Type: ID

### Schema Class

Contains methods for obtaining schema describe information.

Namespace

System

#### Schema Methods

### The following are methods for Schema . All methods are static.

IN THIS SECTION:

##### getGlobalDescribe()

Returns a map of all sObject names (keys) to sObject tokens (values) for the standard and custom objects defined in your organization.

describeDataCategoryGroups(sObjectNames)
Returns a list of the category groups associated with the specified objects.

describeSObjects(sObjectTypes)
Describes metadata (field list and object properties) for the specified sObject or array of sObjects.

describeSObjects(SObjectTypes, SObjectDescribeOptions)
Describes metadata such as field list and object properties for the specified list of SObjects. The default describe option for this
method is SObjectDescribeOptions.DEFERRED, which indicates lazy initialization of describe attributes on first use.

describeTabs()
Returns information about the standard and custom apps available to the running user.

describeDataCategoryGroupStructures(pairs,topCategoriesOnly)
Returns available category groups along with their data category structure for objects specified in the request.

##### getGlobalDescribe()

Returns a map of all sObject names (keys) to sObject tokens (values) for the standard and custom objects defined in your organization.

Signature

```
   public static Map<String, Schema.SObjectType> getGlobalDescribe()

```


Apex Reference Guide Schema Class

Return Value

Type: Map<String, Schema.SObjectType>

Usage

[For more information on accessing SObjects, see Accessing All sObjects.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_global_describe.htm)

Example

```
   Map<String, Schema.SObjectType> gd =

   Schema.getGlobalDescribe();

##### describeDataCategoryGroups(sObjectNames)

```

Returns a list of the category groups associated with the specified objects.

Signature

```
   public static List<Schema.DescribeDataCategoryGroupResult>

   describeDataCategoryGroups(List<String> sObjectNames)

```

Parameters

```
   sObjectNames
```

Type: List<String>

Return Value

Type: List<Schema.DescribeDataCategoryGroupResult>

Usage

You can specify one of the following sObject names:

**•** KnowledgeArticleVersion—to retrieve category groups associated with article types.

**•** Question—to retrieve category groups associated with questions.

[For more information and code examples using describeDataCategoryGroups, see Accessing All Data Categories Associated with an](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)
[sObject.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

For additional information about articles and questions, see “Work with Articles and Translations” in the Salesforce online help.

##### describeSObjects(sObjectTypes)

Describes metadata (field list and object properties) for the specified sObject or array of sObjects.

Signature

```
   public static List<Schema.DescribeSObjectResult> describeSObjects(List<String>

   sObjectTypes)

```


Apex Reference Guide Schema Class

Parameters

```
   sObjectTypes
```

Type: List<String>

The _`sObjectTypes`_ argument is a list of sObject type names you want to describe.

Return Value

Type: List<Schema.DescribeSObjectResult>

Usage

This method is similar to the `getDescribe` method on the `Schema.sObjectType` token. Unlike the `getDescribe` method,
this method allows you to specify the sObject type dynamically and describe more than one sObject at a time.

You can first call `getGlobalDescribe` to retrieve a list of all objects for your organization, then iterate through the list and use
##### describeSObjects to obtain metadata about individual objects.

Example

```
   Schema.DescribeSObjectResult[] descResult = Schema.describeSObjects(

                                            new

   String[]{'Account','Contact'});

##### **`describeSObjects(SObjectTypes, SObjectDescribeOptions)`**

```

Describes metadata such as field list and object properties for the specified list of SObjects. The default describe option for this method
is SObjectDescribeOptions.DEFERRED, which indicates lazy initialization of describe attributes on first use.

Signature

```
   public static List<Schema.DescribeSObjectResult> describeSObjects(List<String>

   SObjectTypes, Object SObjectDescribeOptions)

```

Parameters

```
   SObjectTypes
```

Type: List<String>

The list of SObject types to describe.

```
   SObjectDescribeOptions
```

Type: Object

The effective describe option used for the SObject.

Return Value

Type: List<Schema.DescribeSObjectResult>

##### describeTabs()

Returns information about the standard and custom apps available to the running user.


Apex Reference Guide Schema Class

Signature

```
   public static List<Schema.DescribeTabSetResult> describeTabs()

```

Return Value

Type: List<Schema.DescribeTabSetResult>

Usage

An app is a group of tabs that works as a unit to provide application functionality. For example, two of the standard Salesforce apps are
“Sales” and “Service.”

The `describeTabs` method returns the minimum required metadata that can be used to render apps in another user interface.
Typically, this call is used by partner applications to render Salesforce data in another user interface, such as in a mobile or connected
app.

In the Salesforce user interface, users have access to standard apps (and can also have access to custom apps) as listed in the Salesforce
app menu at the top of the page. Selecting an app name in the menu allows the user to switch between the listed apps at any time.

Note: The “All Tabs” tab isn’t included in the list of described tabs.

Example

This example shows how to call the `describeTabs` method.

```
   Schema.DescribeTabSetResult[] tabSetDesc = Schema.describeTabs();

```

This longer example shows how to obtain describe metadata information for the Sales app. For each tab, the example gets describe
information, such as the icon URL, whether the tab is custom or not, and colors. The describe information is written to the debug output.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(DescribeTabSetResult tsr : tabSetDesc) {

      String appLabel = tsr.getLabel();

      System.debug('Label: ' + appLabel);

      System.debug('Logo URL: ' + tsr.getLogoUrl());

      System.debug('isSelected: ' + tsr.isSelected());

      String ns = tsr.getNamespace();

      if (ns == '') {

        System.debug('The ' + appLabel + ' app has no namespace defined.');

      }

      else {

        System.debug('Namespace: ' + ns);

      }

      // Display tab info for the Sales app

      if (appLabel == 'Sales') {

        List<Schema.DescribeTabResult> tabDesc = tsr.getTabs();

        System.debug('-- Tab information for the Sales app --');

        for(Schema.DescribeTabResult tr : tabDesc) {

           System.debug('getLabel: ' + tr.getLabel());

           System.debug('getColors: ' + tr.getColors());

```


Apex Reference Guide Schema Class

```
           System.debug('getIconUrl: ' + tr.getIconUrl());

           System.debug('getIcons: ' + tr.getIcons());

           System.debug('getMiniIconUrl: ' + tr.getMiniIconUrl());

           System.debug('getSobjectName: ' + tr.getSobjectName());

           System.debug('getUrl: ' + tr.getUrl());

           System.debug('isCustom: ' + tr.isCustom());

        }

      }

   }

   // Example debug statement output

   // DEBUG|Label: Sales

   // DEBUG|Logo URL:

   https:// MyDomainName .my.salesforce.com/img/seasonLogos/2014_winter_aloha.png

   // DEBUG|isSelected: true

   // DEBUG|The Sales app has no namespace defined.// DEBUG|-- Tab information for the Sales

    app -
   // (This is an example debug output for the Accounts tab.)

   // DEBUG|getLabel: Accounts

   // DEBUG|getColors:

   (Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme4;],

   // Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme3;],

   // Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme2;])

   // DEBUG|getIconUrl: https:// MyDomainName .my.salesforce.com/img/icon/accounts32.png

   // DEBUG|getIcons:

   (Schema.DescribeIconResult[getContentType=image/png;getHeight=32;getTheme=theme3;

   //

   getUrl=https:// MyDomainName .my.salesforce.com/img/icon/accounts32.png;getWidth=32;],

   // Schema.DescribeIconResult[getContentType=image/png;getHeight=16;getTheme=theme3;

   //

   getUrl=https:// MyDomainName .my.salesforce.com/img/icon/accounts16.png;getWidth=16;])

   // DEBUG|getMiniIconUrl: https:// MyDomainName .my.salesforce.com/img/icon/accounts16.png

   // DEBUG|getSobjectName: Account

   // DEBUG|getUrl: https:// MyDomainName .my.salesforce.com/001/o

   // DEBUG|isCustom: false

##### **`describeDataCategoryGroupStructures(pairs,topCategoriesOnly)`**

```

Returns available category groups along with their data category structure for objects specified in the request.

Signature

```
   public static List<Schema.DescribeDataCategoryGroupStructureResult> describeDataCategory

   GroupStructures(List<Schema.DataCategoryGroupSobjectTypePair> pairs,Boolean

   topCategoriesOnly)

```

Parameters

```
   pairs
```

Type: List<Schema.DataCategoryGroupSobjectTypePair>


### Apex Reference Guide Search Class

The _`pairs`_ argument is one or more category groups and objects to query Schema.DataCategoryGroupSobjectTypePairs. Visible
data categories are retrieved for the specified object. For more information on data category group visibility, see “Data Category
Visibility” in Salesforce Help.

```
   topCategoriesOnly

```

Type: Boolean

Use `true` to return only the top visible category and `false` to return all the visible categories, depending on the user's data
category group visibility settings. For more information on data category group visibility, see Data Category Visibility in Salesforce
Help.

Return Value

Type: List<Schema.DescribeDataCategoryGroupStructureResult>

### Search Class

Use the methods of the Search class to perform dynamic SOSL queries.

Namespace

System

#### Search Methods

### The following are static methods for Search .

IN THIS SECTION:

find(searchQuery)
Performs a dynamic SOSL query that can include the SOSL `WITH SNIPPET` clause. Snippets provide more context for users in
Salesforce Knowledge article search results.

find(searchQuery, accessLevel)
Performs a dynamic SOSL query that can include the SOSL `WITH SNIPPET` clause. Snippets provide more context for users in
Salesforce Knowledge article search results.

query(query)
Performs a dynamic SOSL query.

query(query, accessLevel)
Performs a dynamic SOSL query.

suggest(searchQuery, sObjectType, suggestions)
Returns a list of records or Salesforce Knowledge articles whose names or titles match the user’s search query string. Use this method
to provide users with shortcuts to navigate to relevant records or articles before they perform a search.

suggest(searchQuery, sObjectType, suggestions, accessLevel)
Returns a list of records or Salesforce Knowledge articles whose names or titles match the user’s search query string. Use this method
to provide users with shortcuts to navigate to relevant records or articles before they perform a search.


Apex Reference Guide Search Class

##### find(searchQuery)

Performs a dynamic SOSL query that can include the SOSL `WITH SNIPPET` clause. Snippets provide more context for users in
Salesforce Knowledge article search results.

Signature

```
   public static Search.SearchResults find(String searchQuery)

```

Parameters

```
   searchQuery
```

Type: String

A SOSL query string.

Return Value

Type: Search.SearchResults

Usage

Use this method wherever a static SOSL query can be used, such as in regular assignment statements and `for` loops.

[See Use Dynamic SOSL to Return Snippets.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm#snippet_title)

SEE ALSO:

get(sObjectType)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### **`find(searchQuery, accessLevel)`**

Performs a dynamic SOSL query that can include the SOSL `WITH SNIPPET` clause. Snippets provide more context for users in
Salesforce Knowledge article search results.

Signature

```
   public static Search.SearchResults find(String searchQuery, System.AccessLevel

   accessLevel)

```

Parameters

```
   searchQuery
```

Type: String

A SOSL query string.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are


Apex Reference Guide Search Class

[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Search.SearchResults

Usage

Use this method wherever a static SOSL query can be used, such as in regular assignment statements and `for` loops.

[See Use Dynamic SOSL to Return Snippets.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm#snippet_title)

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### query(query)

Performs a dynamic SOSL query.

Signature

```
   public static sObject[sObject[]] query(String query)

```

Parameters

##### _`query`_

Type: String

A SOSL query string.

To create a SOSL query that includes the `WITH SNIPPET` clause, use the Search.find(String searchQuery) method instead.

Return Value

Type: sObject[sObject[]]

Usage

This method can be used wherever a static SOSL query can be used, such as in regular assignment statements and `for` loops.

[For more information, see Dynamic SOSL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)

##### **`query(query, accessLevel)`**

Performs a dynamic SOSL query.

Signature

```
   public static List<List<SObject>> query(String query, System.AccessLevel accessLevel)

```


Apex Reference Guide Search Class

Parameters

```
   query
```

Type: String

A SOSL query string.

To create a SOSL query that includes the `WITH SNIPPET` clause, use the Search.find(String searchQuery) method instead.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: sObject[sObject[]]

Usage

This method can be used wherever a static SOSL query can be used, such as in regular assignment statements and `for` loops.

[For more information, see Dynamic SOSL.](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)

##### suggest(searchQuery, sObjectType, suggestions)

Returns a list of records or Salesforce Knowledge articles whose names or titles match the user’s search query string. Use this method
to provide users with shortcuts to navigate to relevant records or articles before they perform a search.

Signature

```
   public static Search.SuggestionResults suggest(String searchQuery, String sObjectType,

   Search.SuggestionOption suggestions)

```

Parameters

```
   searchQuery
```

Type: String

A SOSL query string.

```
   sObjectType
```

Type: String

An sObject type.

```
   options
```

Type: Search.SuggestionOption

This object contains options that change the suggestion results.

If the _`searchQuery`_ returns KnowledgeArticleVersion objects, pass an _`options`_ parameter with a Search.SuggestionOption
object that contains a language KnowledgeSuggestionFilter and a publish status KnowledgeSuggestionFilter.


Apex Reference Guide Search Class

For suggestions for all other record types, the only supported option is a limit, which sets the maximum number of suggestions
returned.

Return Value

Type: SuggestionResults

Usage

Use this method to return:

**Suggestions for Salesforce Knowledge articles (KnowledgeArticleVersion)**
Salesforce Knowledge must be enabled in your organization. The user must have the “View Articles” permission enabled.

The articles suggested include only the articles the user can access, based on the data categories and article types the user has
permissions to view.

**Suggestions for other record types**
The records suggested include only the records the user can access.

This method returns a record if its name field starts with the text in the search string. This method automatically appends an asterisk
wildcard (*) at the end of the search string. Records that contain the search string within a word aren’t considered a match.

Records are suggested if the entire search string is found in the record name, in the same order as specified in the search string. For
example, the text string _`national u`_ is treated as _`national u*`_ and returns “National Utility” and “National Urban Company”
but not “National Company Utility” or “Urban National Company”.

Note: If the user’s search query contains quotation marks or wildcards, those symbols are automatically removed from the query
string in the URI.

SEE ALSO:

_Apex Developer Guide_ [: Suggest Salesforce Knowledge Articles](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_forcecom_kb_suggestions.htm)

##### **`suggest(searchQuery, sObjectType, suggestions, accessLevel)`**

Returns a list of records or Salesforce Knowledge articles whose names or titles match the user’s search query string. Use this method
to provide users with shortcuts to navigate to relevant records or articles before they perform a search.

Signature

```
   public static Search.SuggestionResults suggest(String searchQuery, String sObjectType,

   Search.SuggestionOption suggestions, System.AccessLevel accessLevel)

```

Parameters

```
   searchQuery
```

Type: String

A SOSL query string.

```
   sObjectType
```

Type: String

An sObject type.


### Apex Reference Guide Security Class

```
   suggestions
```

Type: Search.SuggestionOption

This object contains options that change the suggestion results.

If the _`searchQuery`_ returns KnowledgeArticleVersion objects, pass an _`options`_ parameter with a Search.SuggestionOption
object that contains a language KnowledgeSuggestionFilter and a publish status KnowledgeSuggestionFilter.

For suggestions for all other record types, the only supported option is a limit, which sets the maximum number of suggestions
returned.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: SuggestionResults

Usage

Use this method to return:

**Suggestions for Salesforce Knowledge articles (KnowledgeArticleVersion)**
Salesforce Knowledge must be enabled in your organization. The user must have the “View Articles” permission enabled.

The articles suggested include only the articles the user can access, based on the data categories and article types the user has
permissions to view.

**Suggestions for other record types**
The records suggested include only the records the user can access.

This method returns a record if its name field starts with the text in the search string. This method automatically appends an asterisk
wildcard (*) at the end of the search string. Records that contain the search string within a word aren’t considered a match.

Records are suggested if the entire search string is found in the record name, in the same order as specified in the search string. For
example, the text string _`national u`_ is treated as _`national u*`_ and returns “National Utility” and “National Urban Company”
but not “National Company Utility” or “Urban National Company”.

Note: If the user’s search query contains quotation marks or wildcards, those symbols are automatically removed from the query
string in the URI.

### Security Class

Contains methods to securely implement Apex applications.

Namespace

System


Apex Reference Guide Security Class

Usage

In the context of the current user’s create, read, update, or upsert access permission, use the Security class methods to:

**•** Strip fields that aren’t visible from query and subquery results

**•** Remove inaccessible fields before a DML operation without causing an exception

**•** Sanitize SObjects that have been deserialized from an untrusted source

IN THIS SECTION:

#### Security Methods Security Methods The following are methods for Security .

IN THIS SECTION:

##### stripInaccessible(accessCheckType, sourceRecords, enforceRootObjectCRUD)

Creates a list of sObjects from the source records, which are stripped of fields that fail the field-level security checks for the current
user. The method also provides an option to enforce an object-level access check.

stripInaccessible(accessCheckType, sourceRecords)
Creates a list of sObjects from the source records, which are stripped of fields that fail the field-level security checks for the current
user.

stripInaccessible(accessCheckType, sourceRecords, enforceRootObjectCRUD, permissionSetId)(Developer Preview)
Creates a list of sObjects from the source records, which are stripped of fields that fail field-level and object-level access checks. Apex
enforces field-level security (FLS) and object permissions as per the specified permission set, in addition to the running user’s
permissions.

##### **`stripInaccessible(accessCheckType, sourceRecords, enforceRootObjectCRUD)`**

Creates a list of sObjects from the source records, which are stripped of fields that fail the field-level security checks for the current user.
The method also provides an option to enforce an object-level access check.

Signature

```
   public static System.SObjectAccessDecision stripInaccessible(System.AccessType

   accessCheckType, List<SObject> sourceRecords, Boolean enforceRootObjectCRUD)

```

Parameters

```
   accessCheckType
```

Type: System.AccessType

Uses values from the AccessType enum. This parameter determines the type of field-level access check to be performed. To check
the current user's field-level access, use the Schema.DescribeFieldResult methods — `isCreatable()`, `isAccessible()`,
or `isUpdatable()` .

```
   sourceRecords
```

Type: List<SObject>


Apex Reference Guide Security Class

A list of sObjects to be checked for fields that aren’t accessible in the context of the current user’s operation.

```
   enforceRootObjectCRUD
```

Type: Boolean

Indicates whether an object-level access check is performed. If this parameter is set to `true` and the access check fails, the method
throws an exception. The default value of this optional parameter is `true` .

Return Value

Type: System.SObjectAccessDecision

Example

In this example, the user doesn’t have permission to create the `Probability` field of an Opportunity.

```
   List<Opportunity> opportunities = new List<Opportunity>{

      new Opportunity(Name='Opportunity1'),

      new Opportunity(Name='Opportunity2', Probability=95)

   };

   // Strip fields that are not creatable

   SObjectAccessDecision decision = Security.stripInaccessible(

      AccessType.CREATABLE,

      opportunities);

   // Print stripped records

   for (SObject strippedOpportunity : decision.getRecords()) {

      System.debug(strippedOpportunity);

   }

   // Print modified indexes

   System.debug(decision.getModifiedIndexes());

   // Print removed fields

   System.debug(decision.getRemovedFields());

   //Lines from output log

   //|DEBUG|Opportunity:{Name=Opportunity1}

   //|DEBUG|Opportunity:{Name=Opportunity2}

   //|DEBUG|{1}

   //|DEBUG|{Opportunity={Probability}}

##### **`stripInaccessible(accessCheckType, sourceRecords)`**

```

Creates a list of sObjects from the source records, which are stripped of fields that fail the field-level security checks for the current user.

Signature

```
   public static System.SObjectAccessDecision stripInaccessible(System.AccessType

   accessCheckType, List<SObject> sourceRecords)

```


Apex Reference Guide Security Class

Parameters

```
   accessCheckType
```

Type: System.AccessType

Uses values from the AccessType enum. This parameter determines the type of field-level access check to be performed. To check
the current user's field-level access, use the Schema.DescribeFieldResult methods — `isCreatable()`, `isAccessible()`,
or `isUpdatable()` .

```
   sourceRecords
```

Type: List<SObject>

A list of sObjects to be checked for fields that aren’t accessible in the context of the current user’s operation.

Return Value

Type: System.SObjectAccessDecision

Example

In this example, the user doesn’t have permission to read the `ActualCost` field of a Campaign.

```
   List<Campaign> campaigns = new List<Campaign>{

      new Campaign(Name='Campaign1', BudgetedCost=1000, ActualCost=2000),

      new Campaign(Name='Campaign2', BudgetedCost=4000, ActualCost=1500)

   };

   insert campaigns;

   // Strip fields that are not readable

   SObjectAccessDecision decision = Security.stripInaccessible(

      AccessType.READABLE,

      [SELECT Name, BudgetedCost, ActualCost from Campaign]);

   // Print stripped records

   for (SObject strippedCampaign : decision.getRecords()) {

      System.debug(strippedCampaign); // Does not display ActualCost

   }

   // Print modified indexes

   System.debug(decision.getModifiedIndexes());

   // Print removed fields

   System.debug(decision.getRemovedFields());

   //Lines from output log

   //|DEBUG|Campaign:{Name=Campaign1, BudgetedCost=1000, Id=701xx00000011nhAAA}

   //|DEBUG|Campaign:{Name=Campaign2, BudgetedCost=4000, Id=701xx00000011niAAA}

   //|DEBUG|{0, 1}

   //|DEBUG|{Campaign={ActualCost}}

##### **`stripInaccessible(accessCheckType, sourceRecords, enforceRootObjectCRUD,`**

  permissionSetId)(Developer Preview)

```

Creates a list of sObjects from the source records, which are stripped of fields that fail field-level and object-level access checks. Apex
enforces field-level security (FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.


### Apex Reference Guide SelectOption Class

Note: Feature is available as a developer preview. Feature isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don’t implement functionality developed with these commands or
tools in a production environment. You can provide feedback and suggestions for the “Permission Sets with User Mode” feature
[in the Trailblazer Community.](https://trailhead.salesforce.com/trailblazer-community/groups/0F94S000000GvrW)

This feature is available in scratch orgs where the `ApexUserModeWithPermset` feature is enabled. If the feature isn’t enabled,
Apex code with this feature can be compiled but not executed.

Signature

```
   public static System.SObjectAccessDecision stripInaccessible(System.AccessType

   accessCheckType, List<SObject> sourceRecords, Boolean enforceRootObjectCRUD, Id

   permissionSetId)

```

Parameters

```
   accessCheckType
```

Type: System.AccessType

Uses values from the AccessType enum. This parameter determines the type of field-level access check to be performed. To check
the current user's field-level access, use the Schema.DescribeFieldResult methods — `isCreatable()`, `isAccessible()`,
or `isUpdatable()` .

```
   sourceRecords
```

Type: List<SObject>

A list of sObjects to be checked for fields that aren’t accessible in the context of the current user’s operation.

```
   enforceRootObjectCRUD
```

Type: Boolean

Indicates whether an object-level access check is performed. If this parameter is set to `true` and the access check fails, the method
throws an exception. The default value of this optional parameter is `true` .

```
   permissionSetId
```

Type: Id

Permissions in the specified permission set are enforced in additon to the running user’s permissions.

Return Value

Type: System.SObjectAccessDecision

### SelectOption Class A SelectOption object specifies one of the possible values for a Visualforce selectCheckboxes, selectList, or

`selectRadio` component.

Namespace

System

### SelectOption consists of a label that is displayed to the end user, and a value that is returned to the controller if the option is selected. A SelectOption can also be displayed in a disabled state, so that a user cannot select it as an option, but can still view it.


Apex Reference Guide SelectOption Class

Instantiation

In a custom controller or controller extension, you can instantiate a SelectOption in one of the following ways:

**•** `SelectOption option = new SelectOption(` _**`value`**_ `,` _**`label`**_ `,` _**`isDisabled`**_ `);`

where _`value`_ is the String that is returned to the controller if the option is selected by a user, _`label`_ is the String that is displayed
to the user as the option choice, and _`isDisabled`_ is a Boolean that, if true, specifies that the user cannot select the option, but
can still view it.

**•** `SelectOption option = new SelectOption(` _**`value`**_ `,` _**`label`**_ `);`

where _`value`_ is the String that is returned to the controller if the option is selected by a user, and _`label`_ is the String that is
displayed to the user as the option choice. Because a value for _`isDisabled`_ is not specified, the user can both view and select
the option.

Example

The following example shows how a list of SelectOptions objects can be used to provide possible values for a `selectCheckboxes`
component on a Visualforce page. In the following custom controller, the `getItems` method defines and returns the list of possible
SelectOption objects:

```
   public class sampleCon {

     String[] countries = new String[]{};

     public PageReference test() {

      return null;

     }

     public List<SelectOption> getItems() {

      List<SelectOption> options = new List<SelectOption>();

      options.add(new SelectOption('US','US'));

      options.add(new SelectOption('CANADA','Canada'));

      options.add(new SelectOption('MEXICO','Mexico'));

      return options;

     }

     public String[] getCountries() {

      return countries;

     }

     public void setCountries(String[] countries) {

      this.countries = countries;

     }

   }

```

In the following page markup, the `<apex:selectOptions>` tag uses the `getItems` method from the controller above to
retrieve the list of possible values. Because `<apex:selectOptions>` is a child of the `<apex:selectCheckboxes>` tag,
the options are displayed as checkboxes:

```
    <apex:page controller="sampleCon">

     <apex:form>

```


Apex Reference Guide SelectOption Class

```
      <apex:selectCheckboxes value="{!countries}">

       <apex:selectOptions value="{!items}"/>

      </apex:selectCheckboxes><br/>

      <apex:commandButton value="Test" action="{!test}" rerender="out" status="status"/>

     </apex:form>

     <apex:outputPanel id="out">

      <apex:actionstatus id="status" startText="testing...">

       <apex:facet name="stop">

        <apex:outputPanel>

         <p>You have selected:</p>

         <apex:dataList value="{!countries}" var="c">{!c}</apex:dataList>

        </apex:outputPanel>

       </apex:facet>

      </apex:actionstatus>

     </apex:outputPanel>

   </apex:page>

```

IN THIS SECTION:

#### SelectOption Constructors

SelectOption Methods

#### SelectOption Constructors The following are constructors for SelectOption .

IN THIS SECTION:

##### SelectOption(value, label)
#### Creates a new instance of the SelectOption class using the specified value and label.

SelectOption(value, label, isDisabled)
#### Creates a new instance of the SelectOption class using the specified value, label, and disabled setting.

##### SelectOption(value, label)

#### Creates a new instance of the SelectOption class using the specified value and label.

Signature

```
   public SelectOption(String value, String label)

```

Parameters

```
   value
```

Type: String

The string that is returned to the Visualforce controller if the option is selected by a user.

```
   label
```

Type: String

The string that is displayed to the user as the option choice.


Apex Reference Guide SelectOption Class

##### SelectOption(value, label, isDisabled) Creates a new instance of the SelectOption class using the specified value, label, and disabled setting.

Signature

```
   public SelectOption(String value, String label, Boolean isDisabled)

```

Parameters

```
   value
```

Type: String

The string that is returned to the Visualforce controller if the option is selected by a user.

```
   label
```

Type: String

The string that is displayed to the user as the option choice.

```
   isDisabled
```

Type: Boolean

If set to true, the option can’t be selected by the user but can still be viewed.

#### SelectOption Methods

##### The following are methods for SelectOption . All are instance methods.

IN THIS SECTION:

getDisabled()
Returns the current value of the SelectOption object's `isDisabled` attribute.

getEscapeItem()
Returns the current value of the SelectOption object's `itemEscaped` attribute.

getLabel()
Returns the option label that is displayed to the user.

getValue()
Returns the option value that is returned to the controller if a user selects the option.

setDisabled(isDisabled)
Sets the value of the SelectOption object's `isDisabled` attribute.

setEscapeItem(itemsEscaped)
Sets the value of the SelectOption object's `itemEscaped` attribute.

setLabel(label)
Sets the value of the option label that is displayed to the user.

setValue(value)
Sets the value of the option value that is returned to the controller if a user selects the option.


Apex Reference Guide SelectOption Class

##### getDisabled()

Returns the current value of the SelectOption object's `isDisabled` attribute.

Signature

```
   public Boolean getDisabled()

```

Return Value

Type: Boolean

Usage

If `isDisabled` is set to `true`, the user can view the option, but cannot select it. If `isDisabled` is set to `false`, the user can
both view and select the option.

##### getEscapeItem()

Returns the current value of the SelectOption object's `itemEscaped` attribute.

Signature

```
   public Boolean getEscapeItem()

```

Return Value

Type: Boolean

Usage

If `itemEscaped` is set to `true`, sensitive HTML and XML characters are escaped in the HTML output generated by this component.
If `itemEscaped` is set to `false`, items are rendered as written.

##### getLabel()

Returns the option label that is displayed to the user.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the option value that is returned to the controller if a user selects the option.


Apex Reference Guide SelectOption Class

Signature

```
   public String getValue()

```

Return Value

Type: String

##### setDisabled(isDisabled)

Sets the value of the SelectOption object's `isDisabled` attribute.

Signature

```
   public Void setDisabled(Boolean isDisabled)

```

Parameters

```
   isDisabled
```

Type: Boolean

Return Value

Type: Void

Usage

If `isDisabled` is set to `true`, the user can view the option, but cannot select it. If `isDisabled` is set to `false`, the user can
both view and select the option.

##### setEscapeItem(itemsEscaped)

Sets the value of the SelectOption object's `itemEscaped` attribute.

Signature

```
   public Void setEscapeItem(Boolean itemsEscaped)

```

Parameters

```
   itemsEscaped
```

Type: Boolean

Return Value

Type: Void

Usage

If `itemEscaped` is set to `true`, sensitive HTML and XML characters are escaped in the HTML output generated by this component.
If `itemEscaped` is set to `false`, items are rendered as written.


### Apex Reference Guide Set Class

##### setLabel(label)

Sets the value of the option label that is displayed to the user.

Signature

```
   public Void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: Void

##### setValue(value)

Sets the value of the option value that is returned to the controller if a user selects the option.

Signature

```
   public Void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: Void

### Set Class

Represents a collection of unique elements with no duplicate values.

Namespace

System

Usage

##### The Set methods work on a set, that is, an unordered collection of elements that was initialized using the set keyword. Set elements

can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. Set methods are all instance
methods, that is, they all operate on a particular instance of a Set. The following are the instance methods for sets.


Apex Reference Guide Set Class

Note:

**•** Uniqueness of set elements of user-defined types is determined by the `equals` and `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)` methods, which you
provide in your classes. Uniqueness of all other non-primitive types is determined by comparing the objects’ fields.

**•** If the set contains String elements, the elements are case-sensitive. Two set elements that differ only by case are considered
distinct.

[For more information on sets, see Sets.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_sets.htm)

IN THIS SECTION:

#### Set Constructors

Set Methods

#### Set Constructors The following are constructors for Set .

IN THIS SECTION:

##### Set<T>()
#### Creates a new instance of the Set class. A set can hold elements of any data type T.

##### Set<T>(setToCopy)
#### Creates a new instance of the Set class by copying the elements of the specified set. T is the data type of the elements in both sets

and can be any data type.

Set<T>(listToCopy)
#### Creates a new instance of the Set class by copying the list elements. T is the data type of the elements in the set and list and can

be any data type.

##### Set<T>()

#### Creates a new instance of the Set class. A set can hold elements of any data type T.

Signature

```
   public Set<T>()

```

Example

```
   // Create a set of strings

   Set<String> s1 = new Set<String>();

   // Add two strings to it

   s1.add('item1');

   s1.add('item2');

##### Set<T>(setToCopy)

#### Creates a new instance of the Set class by copying the elements of the specified set. T is the data type of the elements in both sets
```

and can be any data type.


Apex Reference Guide Set Class

Signature

```
   public Set<T>(Set<T> setToCopy)

```

Parameters

```
   setToCopy
```

Type: Set<T>

The set to initialize this set with.

Example

```
   Set<String> s1 = new Set<String>();

   s1.add('item1');

   s1.add('item2');

   Set<String> s2 = new Set<String>(s1);

   // The set elements in s2 are copied from s1

   System.debug(s2);

##### Set<T>(listToCopy) Creates a new instance of the Set class by copying the list elements. T is the data type of the elements in the set and list and can be
```

any data type.

Signature

```
   public Set<T>(List<T> listToCopy)

```

Parameters

```
   listToCopy
```

Type: Integer

The list to copy the elements of into this set.

Example

```
   List<Integer> ls = new List<Integer>();

   ls.add(1);

   ls.add(2);

   // Create a set based on a list

   Set<Integer> s1 = new Set<Integer>(ls);

   // Elements are copied from the list to this set

   System.debug(s1);// DEBUG|{1, 2}

#### Set Methods

##### The following are methods for Set . All are instance methods.

```


Apex Reference Guide Set Class

IN THIS SECTION:

add(setElement)
Adds an element to the set if it is not already present.

addAll(fromList)
Adds all of the elements in the specified list to the set if they are not already present.

addAll(fromSet)
Adds all of the elements in the specified set to the set that calls the method if they are not already present.

clear()
Removes all of the elements from the set.

clone()
Makes a duplicate copy of the set.

contains(setElement)
Returns `true` if the set contains the specified element.

containsAll(listToCompare)
Returns `true` if the set contains all of the elements in the specified list. The list must be of the same type as the set that calls the
method.

containsAll(setToCompare)
Returns `true` if the set contains all of the elements in the specified set. The specified set must be of the same type as the original
set that calls the method.

equals(set2)
Compares this set with the specified set and returns `true` if both sets are equal; otherwise, returns `false` .

hashCode()
Returns the hashcode corresponding to this set and its contents.

isEmpty()
Returns `true` if the set has zero elements.

remove(setElement)
Removes the specified element from the set if it is present.

removeAll(listOfElementsToRemove)
Removes the elements in the specified list from the set if they are present.

removeAll(setOfElementsToRemove)
Removes the elements in the specified set from the original set if they are present.

retainAll(listOfElementsToRetain)
Retains only the elements in this set that are contained in the specified list.

retainAll(setOfElementsToRetain)
Retains only the elements in the original set that are contained in the specified set.

size()
Returns the number of elements in the set (its cardinality).

toString()
Returns the string representation of the set.


Apex Reference Guide Set Class

##### add(setElement)

Adds an element to the set if it is not already present.

Signature

```
   public Boolean add(Object setElement)

```

Parameters

```
   setElement
```

Type: Object

Return Value

Type: Boolean

Usage

This method returns true if the original set changed as a result of the call. For example:

```
   Set<String> myString = new Set<String>{'a', 'b', 'c'};

   Boolean result = myString.add('d');

   System.assertEquals(true, result);

##### addAll(fromList)

```

Adds all of the elements in the specified list to the set if they are not already present.

Signature

```
   public Boolean addAll(List<Object> fromList)

```

Parameters

```
   fromList
```

Type: List

Return Value

Type: Boolean

Returns `true` if the original set changed as a result of the call.

Usage

This method results in the _union_ of the list and the set. The list must be of the same type as the set that calls the method.

##### addAll(fromSet)

Adds all of the elements in the specified set to the set that calls the method if they are not already present.


Apex Reference Guide Set Class

Signature

```
   public Boolean addAll(Set<Object> fromSet)

```

Parameters

```
   fromSet
```

Type: Set<Object>

Return Value

Type: Boolean

This method returns `true` if the original set changed as a result of the call.

Usage

This method results in the _union_ of the two sets. The specified set must be of the same type as the original set that calls the method.

Example

```
   Set<String> myString = new Set<String>{'a', 'b'};

   Set<String> sString = new Set<String>{'c'};

   Boolean result1 = myString.addAll(sString);

   System.assertEquals(true, result1);

##### clear()

```

Removes all of the elements from the set.

Signature

```
   public Void clear()

```

Return Value

Type: Void

##### clone()

Makes a duplicate copy of the set.

Signature

```
   public Set<Object> clone()

```

Return Value

Type: Set (of same type)


Apex Reference Guide Set Class

##### contains(setElement)

Returns `true` if the set contains the specified element.

Signature

```
   public Boolean contains(Object setElement)

```

Parameters

```
   setElement
```

Type: Object

Return Value

Type: Boolean

Example

```
   Set<String> myString = new Set<String>{'a', 'b'};

   Boolean result = myString.contains('z');

   System.assertEquals(false, result);

##### containsAll(listToCompare)

```

Returns `true` if the set contains all of the elements in the specified list. The list must be of the same type as the set that calls the method.

Signature

```
   public Boolean containsAll(List<Object> listToCompare)

```

Parameters

```
   listToCompare
```

Type: List<Object>

Return Value

Type: Boolean

##### containsAll(setToCompare)

Returns `true` if the set contains all of the elements in the specified set. The specified set must be of the same type as the original set
that calls the method.

Signature

```
   public Boolean containsAll(Set<Object> setToCompare)

```


Apex Reference Guide Set Class

Parameters

```
   setToCompare
```

Type: Set<Object>

Return Value

Type: Boolean

Example

```
   Set<String> myString = new Set<String>{'a', 'b'};

   Set<String> sString = new Set<String>{'c'};

   Set<String> rString = new Set<String>{'a', 'b', 'c'};

   Boolean result1, result2;

   result1 = myString.addAll(sString);

   system.assertEquals(true, result1);

   result2 = myString.containsAll(rString);

   System.assertEquals(true, result2);

##### equals(set2)

```

Compares this set with the specified set and returns `true` if both sets are equal; otherwise, returns `false` .

Signature

```
   public Boolean equals(Set<Object> set2)

```

Parameters

```
   set2
```

Type: Set<Object>

The _`set2`_ argument is the set to compare this set with.

Return Value

Type: Boolean

Usage

Two sets are equal if their elements are equal, regardless of their order. The `==` operator is used to compare the elements of the sets.

##### The == operator is equivalent to calling the equals method, so you can call set1.equals(set2); instead of set1 ==

`set2;` .

##### hashCode()

Returns the hashcode corresponding to this set and its contents.


Apex Reference Guide Set Class

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### isEmpty()

Returns `true` if the set has zero elements.

Signature

```
   public Boolean isEmpty()

```

Return Value

Type: Boolean

Example

```
   Set<Integer> mySet = new Set<Integer>();

   Boolean result = mySet.isEmpty();

   System.assertEquals(true, result);

##### remove(setElement)

```

Removes the specified element from the set if it is present.

Signature

```
   public Boolean remove(Object setElement)

```

Parameters

```
   setElement
```

Type: Object

Return Value

Type: Boolean

Returns `true` if the original set changed as a result of the call.

##### removeAll(listOfElementsToRemove)

Removes the elements in the specified list from the set if they are present.

Signature

```
   public Boolean removeAll(List<Object> listOfElementsToRemove)

```


Apex Reference Guide Set Class

Parameters

```
   listOfElementsToRemove
```

Type: List<Object>

Return Value

Type: Boolean

Returns `true` if the original set changed as a result of the call.

Usage

This method results in the _relative complement_ of the two sets. The list must be of the same type as the set that calls the method.

Example

```
   Set<integer> mySet = new Set<integer>{1, 2, 3};

   List<integer> myList = new List<integer>{1, 3};

   Boolean result = mySet.removeAll(myList);

   System.assertEquals(true, result);

   Integer result2 = mySet.size();

   System.assertEquals(1, result2);

##### removeAll(setOfElementsToRemove)

```

Removes the elements in the specified set from the original set if they are present.

Signature

```
   public Boolean removeAll(Set<Object> setOfElementsToRemove)

```

Parameters

```
   setOfElementsToRemove
```

Type: Set<Object>

Return Value

Type: Boolean

This method returns `true` if the original set changed as a result of the call.

Usage

This method results in the _relative complement_ of the two sets. The specified set must be of the same type as the original set that calls
the method.

##### retainAll(listOfElementsToRetain)

Retains only the elements in this set that are contained in the specified list.


Apex Reference Guide Set Class

Signature

```
   public Boolean retainAll(List<Object> listOfElementsToRetain)

```

Parameters

```
   listOfElementsToRetain
```

Type: List<Object>

Return Value

Type: Boolean

This method returns `true` if the original set changed as a result of the call.

Usage

This method results in the _intersection_ of the list and the set. The list must be of the same type as the set that calls the method.

Example

```
   Set<integer> mySet = new Set<integer>{1, 2, 3};

   List<integer> myList = new List<integer>{1, 3};

   Boolean result = mySet.retainAll(myList);

   System.assertEquals(true, result);

##### retainAll(setOfElementsToRetain)

```

Retains only the elements in the original set that are contained in the specified set.

Signature

```
   public Boolean retainAll(Set setOfElementsToRetain)

```

Parameters

```
   setOfElementsToRetain
```

Type: Set

Return Value

Type: Boolean

Returns `true` if the original set changed as a result of the call.

Usage

This method results in the _intersection_ of the two sets. The specified set must be of the same type as the original set that calls the method.

##### size()

Returns the number of elements in the set (its cardinality).


### Apex Reference Guide Site Class

Signature

```
   public Integer size()

```

Return Value

Type: Integer

Example

```
   Set<Integer> mySet = new Set<Integer>{1, 2, 3};

   Set<Integer> retainSet = new Set<Integer>{1, 3};

   Boolean result = mySet.retainAll(retainSet);

   Assert.isTrue(result, 'Expected to have changed mySet');

   Integer retainedSetSize = mySet.size();

   Assert.areEqual(2, retainedSetSize);

##### toString()

```

Returns the string representation of the set.

Signature

```
   public String toString()

```

Return Value

Type: String

Usage

When used in cyclic references, the output is truncated to prevent infinite recursion. When used with large collections, the output is
truncated to avoid exceeding total heap size and maximum CPU time.

**•** Up to 10 items per collection are included in the output, followed by an ellipsis (…).

**•** If the same object is included multiple times in a collection, it’s shown in the output only once; subsequent references are shown
as `(already output)` .

### Site Class Use the Site Class to manage your sites. Change, reset, validate, and check the expiration of passwords. Create site users, person

accounts, and portal users. Get the admin email and ID. Get various URLs, the path prefix, the ID, the template, and the type of the site.
Log in to the site.

Namespace

System


Apex Reference Guide Site Class

#### Site Methods The following are methods for Site . All methods are static.

IN THIS SECTION:

changePassword(newPassword, verifyNewPassword, oldPassword)
Changes the password of the current user.

createExternalUser(user, accountId)
Creates a Salesforce Site or Experience Cloud site user for the given account and associates it with the site.

createExternalUser(user, accountId, password)
Creates a Salesforce Site or Experience Cloud site user for the given account and associates it with the site. This method sends an
email with the specified password to the user.

createExternalUser(user, accountId, password, sendEmailConfirmation)
Creates a Salesforce Site or Experience Cloud site user and associates it with the given account. This method sends the user an email
with the specified password and a new user confirmation email.

createPersonAccountPortalUser(user, ownerId, password)
Creates a person account using the default record type defined on the guest user's profile, then enables it for the site's portal.

createPersonAccountPortalUser(user, ownerId, recordTypeId, password)
Creates a person account using the specified _`recordTypeID`_, then enables it for the site's portal.

createPortalUser(user, accountId, password, sendEmailConfirmation)
Creates a portal user for the given account and associates it with the site's portal.

forgotPassword(username, emailTemplateName)
Resets the user's password and sends an email to the user with the user’s new password. You can specify a custom email template
or use the default email template. Returns a value indicating whether the password reset was successful.

forgotPassword(username)
Resets the user's password and sends an email to the user with the user’s new password. Returns a value indicating whether the
password reset was successful.

getAdminEmail()
Returns the email address of the site administrator.

getAdminId()
Returns the user ID of the site administrator.

getAnalyticsTrackingCode()
The tracking code associated with your site. Services such as Google Analytics can use this code to track page request data for your
site.

getCurrentSiteUrl()
Deprecated. This method was replaced by `getBaseUrl()` in API version 30.0. Returns the base URL of the current site that
references and links should use.

getBaseCustomUrl()
Returns a base URL for the current site that doesn’t use a force.com subdomain. The returned URL uses the same protocol (HTTP or
HTTPS) as the current request if at least one non-Force.com custom URL that supports HTTPS exists on the site. The returned value
never ends with a `/` character. If all the custom URLs in this site end in Force.com or this site has no custom URLs, then this returns
an empty string. If the current request is not a site request, then this method returns an empty string. This method replaced
getCustomWebAddress and includes the custom URL's path prefix..


Apex Reference Guide Site Class

getBaseInsecureUrl()
Deprecated. Returns a base URL for the current site that uses HTTP instead of HTTPS. The current request's domain is used. The
returned value includes the path prefix and never ends with a `/` character. If the current request is not a site request, then this
method returns an empty string.

getBaseRequestUrl()
Returns the base URL of the current site for the requested URL. This isn't influenced by the referring page's URL. The returned URL
uses the same protocol (HTTP or HTTPS) as the current request. The returned value includes the path prefix and never ends with a
`/` character. If the current request is not a site request, then this method returns an empty string.

getBaseSecureUrl()
Returns a base URL for the current site that uses HTTPS instead of HTTP. The current request's domain is preferred if it supports HTTPS.
Domains that are not Force.com subdomains are preferred over Force.com subdomains. A Force.com subdomain, if associated with
the site, is used if no other HTTPS domains exist in the current site. If no HTTPS custom URLs exist in the site, then this method returns
an empty string. The returned value includes the path prefix and never ends with a `/` character. If the current request is not a site
request, then this method returns an empty string.

getBaseUrl()
Returns the base URL of the current site that references and links should use. Note that this field may return the referring page's URL
instead of the current request's URL. The returned value includes the path prefix and never ends with a `/` character. If the current
request is not a site request, then this field returns an empty string. This field replaces getCurrentSiteUrl.

getCustomWebAddress()
Deprecated. This method was replaced by `getBaseCustomUrl()` in API version 30.0.

getDomain()
Returns your Salesforce Sites based URL.

getErrorDescription()
Returns the error description for the current page if it’s a designated error page for the site and an error exists; otherwise, returns an
empty string.

getErrorMessage()
Returns an error message for the current page if it’s a designated error page for the site and an error exists; otherwise, returns an
empty string.

getExperienceId()
Returns the value of the experience ID (expid). This expid value comes from a cookie in the user’s web browser.

getMasterLabel()
Returns the value of the Master Label field for the current site. If the current request is not a site request, then this field returns `null` .

getName()
Returns the API name of the current site.

getOriginalUrl()
Returns the original URL for this page if it’s a designated error page for the site; otherwise, returns `null` .

getPasswordPolicyStatement()
Returns the password requirements for a Salesforce Site or Experience Cloud site created with the Customer Service template.

getPathPrefix()
Returns the URL path prefix of the current site or an empty string if none. For example, if the requested site URL is
`https://myco.my.salesforce-sites.com/partners`, then `/partners` is the path prefix. If the current request
is not a site request, then this method returns an empty string. This method replaced getPrefix in API version 30.0.


Apex Reference Guide Site Class

getPrefix()
Deprecated. This method was replaced by `getPathPrefix()` in API version 30.0.

getSiteId()
Returns the ID of the current site. If the current request is not a site request, then this field returns `null` .

getTemplate()
Returns the template name associated with the current site; returns the default template if no template has been designated.

getSiteType()
Returns the API value of the site type field for the current site. This can be Visualforce for a Salesforce site, Siteforce for a Site.com
site, ChatterNetwork for an Experience Cloud site, or ChatterNetworkPicasso for an Experience Cloud site. If the current request is
not a site request, then this method returns `null` .

getSiteTypeLabel()
Returns the value of the Site Type field's label for the current site. If the current request is not a site request, then this method returns
`null` .

isLoginEnabled()
Returns `true` if the current site is associated with an active login-enabled portal; otherwise returns `false` .

isPasswordExpired()
For authenticated users, returns `true` if the currently logged-in user's password is expired. For non-authenticated users, returns
`false` .

isRegistrationEnabled()
Returns `true` if the current site is associated with an active self-registration-enabled Customer Portal; otherwise returns `false` .

isValidUsername(username)
Returns `true` if the given username is valid; otherwise, returns `false` .

login(username, password, startUrl)
Allows users to log in to the current site with the given username and password, then takes them to the `startUrl` . If `startUrl`
is not a relative path, it defaults to the site's designated index page.

passwordlessLogin(userId, methods, startUrl)
Logs in a user to a Salesforce Site or Experience Cloud site using an identity verification method, such as email or text, instead of a
password. Passwordless login is a convenient, mobile-centric way to welcome users into your site. Let your users log in with something
other than their password, like their email address or phone number.

setExperienceId(expIdValue)
Sets the experience ID for the current user. Use this method to populate the value of the experience ID (expid) cookie in the user’s
web browser.

setPortalUserAsAuthProvider(user, contactId)
Sets the specified user information within the site’s portal via an authentication provider.

validatePassword(user, password, confirmPassword)
Indicates whether a given password meets the requirements specified by org-wide or profile-based password policies in the current
user’s org.

##### changePassword(newPassword, verifyNewPassword, oldPassword)

Changes the password of the current user.


Apex Reference Guide Site Class

Signature

```
   public static System.PageReference changePassword(String newPassword, String

   verifyNewPassword, String oldPassword)

```

Parameters

```
   newPassword
```

Type: String

```
   verifyNewPassword
```

Type: String

```
   oldPassword
```

Type: String

Optional only if the current user’s password has expired; otherwise, required.

Return Value

Type: System.PageReference

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

The password reset process doesn't verify the external user's email address.

##### createExternalUser(user, accountId)

Creates a Salesforce Site or Experience Cloud site user for the given account and associates it with the site.

Signature

```
   public static Id createExternalUser(SObject user, String accountId)

```

Parameters

```
   user
```

Type: SObject

Information required to create a user.

The email address of the user is used to look for matching contacts associated with the specified _`accountId`_ . If a matching contact
is found and is already used by an external user, self-registration isn’t successful. If a matching contact is found but isn’t used by an
external user, it is used for the new external user. If there is no matching contact, a new contact is created for the new external user.

```
   accountId
```

Type: String

The ID of the account you want to associate the user with.

Return Value

Type: Id


Apex Reference Guide Site Class

The ID of the user that this method creates.

Usage

This method throws `Site.ExternalUserCreateException` when user creation fails.

##### The nickname field is required for the User sObject when using the createExternalUser method.

Note: This method is only valid when a site is associated with a Customer Portal.

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

##### createExternalUser(user, accountId, password)

Creates a Salesforce Site or Experience Cloud site user for the given account and associates it with the site. This method sends an email
with the specified password to the user.

Signature

```
   public static Id createExternalUser(SObject user, String accountId, String password)

```

Parameters

```
   user
```

Type: SObject

Information required to create a user.

The email address of the user is used to look for matching contacts associated with the specified _`accountId`_ . If a matching contact
is found and is already used by an external user, self-registration isn’t successful. If a matching contact is found but isn’t used by an
external user, it is used for the new external user. If there is no matching contact, a new contact is created for the new external user.

```
   accountId
```

Type: String

The ID of the account you want to associate the user with.

```
   password
```

Type: String

The password of the Salesforce Site or Experience Cloud site user. If not specified, or if set to `null` or an empty string, this method
sends a new password email to the portal user.

Return Value

Type: Id

The ID of the user that this method creates.

Usage

This method throws `Site.ExternalUserCreateException` when user creation fails.

##### The nickname field is required for the User sObject when using the createExternalUser method.

Note: This method is only valid when a site is associated with a Customer Portal.


Apex Reference Guide Site Class

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

##### createExternalUser(user, accountId, password, sendEmailConfirmation)

Creates a Salesforce Site or Experience Cloud site user and associates it with the given account. This method sends the user an email
with the specified password and a new user confirmation email.

Signature

```
   public static Id createExternalUser(SObject user, String accountId, String password,

   Boolean sendEmailConfirmation)

```

Parameters

```
   user
```

Type: SObject

Information required to create a user.

The email address of the user is used to look for matching contacts associated with the specified _`accountId`_ . If a matching contact
is found and is already used by an external user, self-registration isn’t successful. If a matching contact is found but isn’t used by an
external user, it is used for the new external user. If there is no matching contact, a new contact is created for the new external user.

```
   accountId
```

Type: String

The ID of the account you want to associate the user with.

```
   password
```

Type: String

The password of the Salesforce Site or Experience Cloud site user. If not specified, or if set to `null` or an empty string, this method
sends a new password email to the portal user.

```
   sendEmailConfirmation
```

Type: Boolean

Determines whether a new user email is sent to the portal user. Set it to `true` to send a new user email to the portal user. The
default is `false`, that is, the new user email isn't sent.

Return Value

Type: Id

The ID of the user that this method creates.

Usage

This method throws `Site.ExternalUserCreateException` when user creation fails.

##### The nickname field is required for the User sObject when using the createExternalUser method.

Note: This method is only valid when a site is associated with a Customer Portal.

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.


Apex Reference Guide Site Class

##### createPersonAccountPortalUser(user, ownerId, password)

Creates a person account using the default record type defined on the guest user's profile, then enables it for the site's portal.

Signature

```
   public static ID createPersonAccountPortalUser(sObject user, String ownerId, String

   password)

```

Parameters

```
   user
```

Type: sObject

```
   ownerId
```

Type: String

```
   password
```

Type: String

Return Value

Type: ID

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

Note: This method is only valid when a site is associated with a Customer Portal, and when the user license for the default new
user profile is a high-volume portal user.

##### createPersonAccountPortalUser(user, ownerId, recordTypeId, password)

Creates a person account using the specified _`recordTypeID`_, then enables it for the site's portal.

Signature

```
   public static ID createPersonAccountPortalUser(sObject user, String ownerId, String

   recordTypeId, String password)

```

Parameters

```
   user
```

Type: sObject

```
   ownerId
```

Type: String

```
   recordTypeId
```

Type: String

```
   password
```

Type: String


Apex Reference Guide Site Class

Return Value

Type: ID

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

Note: This method is only valid when a site is associated with a Customer Portal, and when the user license for the default new
user profile is a high-volume portal user.

##### createPortalUser(user, accountId, password, sendEmailConfirmation)

Creates a portal user for the given account and associates it with the site's portal.

Signature

```
   public static ID createPortalUser(sObject user, String accountId, String password,

   Boolean sendEmailConfirmation)

```

Parameters

```
   user
```

Type: sObject

```
   accountId
```

Type: String

```
   password
```

Type: String

(Optional) The password of the portal user. If not specified, or if set to `null` or an empty string, this method sends a new password
email to the portal user.

```
   sendEmailConfirmation
```

Type: Boolean

(Optional) Determines whether a new user email is sent to the portal user. Set it to `true` to send a new user email to the portal
user. The default is `false`, that is, the new user email isn't sent.

Return Value

Type: ID

Usage

If you’re using API version 34.0 or later, we recommend using the `createExternalUser()` methods because they offer better
error handling than this method.

##### The nickname field is required for the user sObject when using the createPortalUser method.

Note: This method is only valid when a site is associated with a Customer Portal.

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.


Apex Reference Guide Site Class

##### forgotPassword(username, emailTemplateName)

Resets the user's password and sends an email to the user with the user’s new password. You can specify a custom email template or
use the default email template. Returns a value indicating whether the password reset was successful.

Signature

```
   public static Boolean forgotPassword(String username,String emailTemplateName)

```

Parameters

```
   username
```

Type: String

```
   emailTemplateName
```

Type: String

If provided, the method applies the template to the email. Otherwise, the method applies the default system template. If an email
template that doesn’t exist is provided, the system logs an exception.

Return Value

Type: Boolean

Note: The return value is always true unless it’s called outside of a Visualforce page.

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

Calls to this method are subject to rate-limiting. If your rate of calls exceeds the limit, Salesforce doesn't send the password reset email.
If you experience this issue, try waiting for an hour before you send another call.

The password reset process doesn't verify the external user's email address.

Note: You can't use `Site.forgotPassword` with the `@future` method, which enables asynchronous execution.

##### forgotPassword(username)

Resets the user's password and sends an email to the user with the user’s new password. Returns a value indicating whether the password
reset was successful.

Signature

```
   public static Boolean forgotPassword(String username)

```

Parameters

```
   username
```

Type: String


Apex Reference Guide Site Class

Return Value

Type: Boolean

Note: The return value is always true unless it’s called outside of a Visualforce page.

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

Calls to this method are subject to rate-limiting. If your rate of calls exceeds the limit, Salesforce doesn't send the password reset email.
If you experience this issue, try waiting for an hour before you send another call.

The password reset process doesn't verify the external user's email address.

Note: You can't use `Site.forgotPassword` with the `@future` method, which enables asynchronous execution.

##### getAdminEmail()

Returns the email address of the site administrator.

Signature

```
   public static String getAdminEmail()

```

Return Value

Type: String

##### getAdminId()

Returns the user ID of the site administrator.

Signature

```
   public static ID getAdminId()

```

Return Value

Type: ID

##### getAnalyticsTrackingCode()

The tracking code associated with your site. Services such as Google Analytics can use this code to track page request data for your site.

Signature

```
   public static String getAnalyticsTrackingCode()

```

Return Value

Type: String


Apex Reference Guide Site Class

##### getCurrentSiteUrl()

Deprecated. This method was replaced by `getBaseUrl()` in API version 30.0. Returns the base URL of the current site that references
and links should use.

Note that this may return the referring page's URL instead of the current request's URL. The returned value includes the path prefix and
always ends with a `/` character. If the current request is not a site request, then this method returns `null` . If the current request is not
a site request, then this method returns `null` . This method was replaced by getBaseUrl in API version 30.0.

Signature

```
   public static String getCurrentSiteUrl()

```

Return Value

Type: String

Usage

Use `getBaseUrl()` instead.

##### getBaseCustomUrl()

Returns a base URL for the current site that doesn’t use a force.com subdomain. The returned URL uses the same protocol (HTTP or
HTTPS) as the current request if at least one non-Force.com custom URL that supports HTTPS exists on the site. The returned value never
ends with a `/` character. If all the custom URLs in this site end in Force.com or this site has no custom URLs, then this returns an empty
string. If the current request is not a site request, then this method returns an empty string. This method replaced getCustomWebAddress
and includes the custom URL's path prefix..

Signature

```
   public static String getBaseCustomUrl()

```

Return Value

Type: String

Usage

This method replaces `getCustomWebAddress()` and includes the custom URL's path prefix.

##### getBaseInsecureUrl()

Deprecated. Returns a base URL for the current site that uses HTTP instead of HTTPS. The current request's domain is used. The returned
value includes the path prefix and never ends with a `/` character. If the current request is not a site request, then this method returns
an empty string.

Signature

```
   public static String getBaseInsecureUrl()

```


Apex Reference Guide Site Class

Return Value

Type: String

##### getBaseRequestUrl()

Returns the base URL of the current site for the requested URL. This isn't influenced by the referring page's URL. The returned URL uses
the same protocol (HTTP or HTTPS) as the current request. The returned value includes the path prefix and never ends with a `/` character.
If the current request is not a site request, then this method returns an empty string.

Signature

```
   public static String getBaseRequestUrl()

```

Return Value

Type: String

##### getBaseSecureUrl()

Returns a base URL for the current site that uses HTTPS instead of HTTP. The current request's domain is preferred if it supports HTTPS.
Domains that are not Force.com subdomains are preferred over Force.com subdomains. A Force.com subdomain, if associated with the
site, is used if no other HTTPS domains exist in the current site. If no HTTPS custom URLs exist in the site, then this method returns an
empty string. The returned value includes the path prefix and never ends with a `/` character. If the current request is not a site request,
then this method returns an empty string.

Signature

```
   public static String getBaseSecureUrl()

```

Return Value

Type: String

##### getBaseUrl()

Returns the base URL of the current site that references and links should use. Note that this field may return the referring page's URL
instead of the current request's URL. The returned value includes the path prefix and never ends with a `/` character. If the current request
is not a site request, then this field returns an empty string. This field replaces getCurrentSiteUrl.

Signature

```
   public static String getBaseUrl()

```

Return Value

Type: String

Usage

This method replaces `getCurrentSiteUrl()` .


Apex Reference Guide Site Class

##### getCustomWebAddress()

Deprecated. This method was replaced by `getBaseCustomUrl()` in API version 30.0.

Returns the request's custom URL if it doesn't end in Lightning Platform or returns the site's primary custom URL. If neither exist, then
this returns null. Note that the URL's path is always the root, even if the request's custom URL has a path prefix. If the current request is
not a site request, then this method returns null. The returned value always ends with a `/` character.

Signature

```
   public static String getCustomWebAddress()

```

Return Value

Type: String

Usage

Use `getBaseCustomUrl()` instead.

##### getDomain()

Returns your Salesforce Sites based URL.

Signature

```
   public static String getDomain()

```

Return Value

Type: String

##### getErrorDescription()

Returns the error description for the current page if it’s a designated error page for the site and an error exists; otherwise, returns an
empty string.

Signature

```
   public static String getErrorDescription()

```

Return Value

Type: String

##### getErrorMessage()

Returns an error message for the current page if it’s a designated error page for the site and an error exists; otherwise, returns an empty
string.


Apex Reference Guide Site Class

Signature

```
   public static String getErrorMessage()

```

Return Value

Type: String

##### getExperienceId()

Returns the value of the experience ID (expid). This expid value comes from a cookie in the user’s web browser.

Signature

```
   public static String getExperienceId()

```

Return Value

Type: String

Usage

##### Use the getExperienceId and setExperienceId methods to implement dynamic login experiences. You can set the

experience ID with `setExperienceId` or by extending the following endpoints with `expid_` _**`value`**_ .

**•** _**`community-url`**_ `/services/oauth2/authorize/expid_` _**`value`**_

**•** _**`community-url`**_ `/idp/endpoint/HttpPost/expid_` _**`value`**_

**•** _**`community-url`**_ `/idp/endpoint/HttpRedirect/expid_` _**`value`**_

**•** _**`community-url_login_page`**_ `/expid=` _**`{value}`**_

**•** _**`community-url`**_ `/CommunitiesSelfReg?expid=` _**`{value}`**_

**•** _**`secur`**_ `/forgotpassword.jsp?expid=` _**`{value}`**_

The cookie is set when the browser loads the URLs with the expid values.

##### getMasterLabel()

Returns the value of the Master Label field for the current site. If the current request is not a site request, then this field returns `null` .

Signature

```
   public static String getMasterLabel()

```

Return Value

Type: String

##### getName()

Returns the API name of the current site.


Apex Reference Guide Site Class

Signature

```
   public static String getName()

```

Return Value

Type: String

##### getOriginalUrl()

Returns the original URL for this page if it’s a designated error page for the site; otherwise, returns `null` .

Signature

```
   public static String getOriginalUrl()

```

Return Value

Type: String

##### getPasswordPolicyStatement()

Returns the password requirements for a Salesforce Site or Experience Cloud site created with the Customer Service template.

Signature

```
   public static String getPasswordPolicyStatement()

```

Return Value

Type: String

##### getPathPrefix()

Returns the URL path prefix of the current site or an empty string if none. For example, if the requested site URL is
`https://myco.my.salesforce-sites.com/partners`, then `/partners` is the path prefix. If the current request is
not a site request, then this method returns an empty string. This method replaced getPrefix in API version 30.0.

Signature

```
   public static String getPathPrefix()

```

Return Value

Type: String

##### getPrefix() Deprecated. This method was replaced by getPathPrefix() in API version 30.0.


Apex Reference Guide Site Class

Returns the URL path prefix of the current site. For example, if your site URL is
_`MyDomainName`_ `.my.salesforce-sites.com/partners`, `/partners` is the path prefix. Returns `null` if the prefix
isn’t defined. If the current request is not a site request, then this method returns a `null` .

Signature

```
   public static String getPrefix()

```

Return Value

Type: String

##### getSiteId()

Returns the ID of the current site. If the current request is not a site request, then this field returns `null` .

Signature

```
   public static String getSiteId()

```

Return Value

Type: Id

##### getTemplate()

Returns the template name associated with the current site; returns the default template if no template has been designated.

Signature

```
   public static System.PageReference getTemplate()

```

Return Value

Type: System.PageReference

##### getSiteType()

Returns the API value of the site type field for the current site. This can be Visualforce for a Salesforce site, Siteforce for a Site.com site,
ChatterNetwork for an Experience Cloud site, or ChatterNetworkPicasso for an Experience Cloud site. If the current request is not a site
request, then this method returns `null` .

Signature

```
   public static String getSiteType()

```

Return Value

Type: String


Apex Reference Guide Site Class

##### getSiteTypeLabel()

Returns the value of the Site Type field's label for the current site. If the current request is not a site request, then this method returns
`null` .

Signature

```
   public static String getSiteTypeLabel()

```

Return Value

Type: String

##### isLoginEnabled()

Returns `true` if the current site is associated with an active login-enabled portal; otherwise returns `false` .

Signature

```
   public static Boolean isLoginEnabled()

```

Return Value

Type: Boolean

##### isPasswordExpired()

For authenticated users, returns `true` if the currently logged-in user's password is expired. For non-authenticated users, returns `false` .

Signature

```
   public static Boolean isPasswordExpired()

```

Return Value

Type: Boolean

##### isRegistrationEnabled()

Returns `true` if the current site is associated with an active self-registration-enabled Customer Portal; otherwise returns `false` .

Signature

```
   public static Boolean isRegistrationEnabled()

```

Return Value

Type: Boolean


Apex Reference Guide Site Class

##### isValidUsername(username)

Returns `true` if the given username is valid; otherwise, returns `false` .

Signature

```
   public static Boolean isValidUsername(String username)

```

Parameters

```
   username
```

Type: String

The username to test for validity.

Return Value

Type: Boolean

##### login(username, password, startUrl)

Allows users to log in to the current site with the given username and password, then takes them to the `startUrl` . If `startUrl`
is not a relative path, it defaults to the site's designated index page.

Signature

```
   public static System.PageReference login(String username, String password, String

   startUrl)

```

Parameters

```
   username
```

Type: String

```
   password
```

Type: String

```
   startUrl
```

Type: String

Return Value

Type: System.PageReference

Usage

All DML statements before the call to `Site.login` get committed. It’s not possible to roll back to a save point that was created before
a call to `Site.login` .

Note: Do not include `http://` or `https://` in the `startURL` .


Apex Reference Guide Site Class

##### passwordlessLogin(userId, methods, startUrl)

Logs in a user to a Salesforce Site or Experience Cloud site using an identity verification method, such as email or text, instead of a
password. Passwordless login is a convenient, mobile-centric way to welcome users into your site. Let your users log in with something
other than their password, like their email address or phone number.

Signature

```
   public static System.PageReference passwordlessLogin(Id userId,

   List<Auth.VerificationMethod> methods, String startUrl)

```

Parameters

```
   userId
```

Type: Id

ID of the user to log in.

```
   methods
```

Type: List<Auth.VerificationMethod>

List of identity verification methods available to the user for passwordless login.

```
   startUrl
```

Type: String

Path to the page that users see after they log in.

Return Value

Type: System.PageReference

Usage

Include this method in the Apex controller of a custom login page implementation.

PasswordlessLogin Example

##### This simple code example of an Apex controller contains the passwordlessLogin method. The PageReference returned by passwordlessLogin redirects the user to the Salesforce Verify page. When the user enters the correct code, the user is redirected

to the site page specified by the start URL.

```
   global with sharing class MFILoginController

   {

     //Input variables

     global String input {get; set;}

     public String startURL {get; set;}

     public List<Auth.VerificationMethod> methods;

     public String error;

     global MFILoginController()

     {

        // Add verification methods in priority order

        methods = new List<Auth.VerificationMethod>();

        methods.add(Auth.VerificationMethod.SMS);

```


Apex Reference Guide Site Class

```
        methods.add(Auth.VerificationMethod.EMAIL);

        methods.add(Auth.VerificationMethod.U2F);

        methods.add(Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

        methods.add(Auth.VerificationMethod.TOTP);

     }

     global PageReference login() {

        List<User> users = null;

        // Empty input

        if(input == null || input == '')

        {

           error = 'Enter Username';

           return null;

        }

        users = [select name, id, email from User where username=:input];

        if(users == null || users.isEmpty())

        {

           error = 'Can\'t find a user';

           return null;

        }

        if (startURL == null) startURL = '/';

        return Site.passwordlessLogin(users[0].id, methods, startURL);

      }

   }

##### setExperienceId(expIdValue)

```

Sets the experience ID for the current user. Use this method to populate the value of the experience ID (expid) cookie in the user’s web
browser.

Signature

```
   public static void setExperienceId(String expIdValue)

```

Parameters

```
   expIdValue
```

Type: String

A value that indicates the user’s login experience.

The value must contain alphanumeric characters only, up to 30 characters.

Usage

##### Use setExperienceId when you’re implementing dynamic login experiences. A login experience refers to a login page plus any

secondary pages associated with the login page (such as multi-factor authentication (MFA) or a login flow). You define different login
experiences depending on who users are or where they’re logging in from. For example, you can require a different registration process
based on the user’s location. In this case, `expIdValue` includes a state or country code. When the user logs in, the URL contains the


Apex Reference Guide Site Class

experience ID parameter, `{expid}` . The `{expid}` parameter is replaced by the value stored in `expIdValue`, such as `.jp` . Then
the user is redirected to the Japanese login experience.

Example

```
   String expid = ApexPages.currentPage().getParameters().get('expid');

     if (expId != null) {

     Site.setExperienceId(expId);

     }

##### setPortalUserAsAuthProvider(user, contactId)

```

Sets the specified user information within the site’s portal via an authentication provider.

Signature

```
   public static Void setPortalUserAsAuthProvider(sObject user, String contactId)

```

Parameters

```
   user
```

Type: sObject

```
   contactId
```

Type: String

Return Value

Type: Void

Usage

**•** This method is only valid when a site is associated with a Customer Portal.

**•** Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

**•** For more information on an authentication provider, see RegistrationHandler.

##### validatePassword(user, password, confirmPassword)

Indicates whether a given password meets the requirements specified by org-wide or profile-based password policies in the current
user’s org.

Signature

```
   public static void validatePassword(SObject user, String password, String

   confirmPassword)

```

Parameters

```
   user
```

Type: SObject


### Apex Reference Guide SObject Class

The user attempting to create a password during self-registration for a Salesforce Site or Experience Cloud site.

```
   password
```

Type: String

The password entered by the user.

```
   confirmPassword
```

Type: String

The password reentered by the user to confirm the password.

Return Value

Type: void

Usage

If validation fails when the method is run in a Lightning controller, this method throws an Apex exception describing the failed validation.
If validation fails when the method is run in a Visualforce controller, the method provides Visualforce error messages.

### SObject Class

Contains methods for the sObject data type.

Namespace

System

Usage

SObject methods are all instance methods: they are called by and operate on an sObject instance such as an account or contact. The
following are the instance methods for sObjects.

[For more information on sObjects, see Working with sObjects.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SObjects.htm)

#### SObject Methods

### The following are methods for SObject . All are instance methods.

IN THIS SECTION:

addError(errorMsg)
Marks a trigger record with a custom error message and prevents any DML operation from occurring.

addError(errorMsg, escape)
Marks a trigger record with a custom error message, specifies if the error message should be escaped, and prevents any DML operation
from occurring.

addError(exceptionError)
Marks a trigger record with a custom error message and prevents any DML operation from occurring.


Apex Reference Guide SObject Class

addError(exceptionError, escape)
Marks a trigger record with a custom exception error message, specifies whether or not the exception error message should be
escaped, and prevents any DML operation from occurring.

addError(errorMsg)
Places the specified error message on a trigger record field in the Salesforce user interface and prevents any DML operation from
occurring.

addError(errorMsg, escape)
Places the specified error message, which can be escaped or unescaped, on a trigger record field in the Salesforce user interface,
and prevents any DML operation from occurring.

addError(fieldName, errorMsg)
Dynamically add errors to fields of an SObject associated with the specified field name.

addError(fieldToken, errorMsg)
Dynamically add errors to an SObject instance associated with the specified field.

addError(fieldName, errorMsg, escape)
Dynamically add errors to fields of an SObject associated with the specified field name.

addError(fieldToken, errorMsg, escape)
Dynamically add errors to an SObject instance associated with the specified field.

clear()
Clears all field values

clone(preserveId)
Creates a copy of the SObject record.

clone(preserveId, isDeepClone)
Creates a copy of the SObject record.

clone(preserveId, isDeepClone, preserveReadonlyTimestamps)
Creates a copy of the SObject record.

clone(preserveId, isDeepClone, preserveReadonlyTimestamps, preserveAutonumber)
Creates a copy of the SObject record.

get(fieldName)
Returns the value for the field specified by _`fieldName`_, such as `AccountNumber` .

get(field)
Returns the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as,
`Schema.Account.AccountNumber` .

getCloneSourceId()
Returns the ID of the entity from which an object was cloned. You can use it for objects cloned through the Salesforce user interface.
You can also use it for objects created using the `System.SObject.clone(preserveId, isDeepClone,`
`preserveReadonlyTimestamps, preserveAutonumber)` method, provided that the _`preserveId`_ parameter
wasn’t used or was set to `false` . The `getCloneSourceId()` method can only be used within the transaction where the
entity is cloned, as clone information doesn’t persist in subsequent transactions.

getErrors()
Returns a list of `Database.Error` objects for an SObject instance. If the SObject has no errors, an empty list is returned.

getOptions()
Returns the database.DMLOptions object for the SObject.


Apex Reference Guide SObject Class

getPopulatedFieldsAsMap()
Returns a map of populated field names and their corresponding values. The map contains only the fields that have been populated
in memory for the SObject instance.

getSObject(fieldName)
Returns the value for the specified field. This method is primarily used with dynamic DML to access values for external IDs.

getSObject(field)
Returns the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as,
`Schema.MyObj.MyExternalId` . This method is primarily used with dynamic DML to access values for external IDs.

getSObjects(fieldName)
Returns the values for the specified field. This method is primarily used with dynamic DML to access values for associated objects,
such as child relationships.

getSObjects(fieldName)
Returns the value for the field specified by the field token `Schema.` _**`fieldName`**_, such as, `Schema.Account.Contact` .
This method is primarily used with dynamic DML to access values for associated objects, such as child relationships.

getSObjectType()
Returns the token for this SObject. This method is primarily used with describe information.

getQuickActionName()
Retrieves the name of a quick action associated with this SObject. Typically used in triggers.

hasErrors()
Returns true if an SObject instance has associated errors. The error message can be associated to the SObject instance by using
`SObject.addError()`, validation rules, or by other means.

isClone()
Returns `true` if an entity is cloned from something, even if the entity hasn’t been saved. The method can only be used within the
transaction where the entity is cloned, as clone information doesn’t persist in subsequent transactions.

isSet(fieldName)
Returns information about the queried sObject field. Returns `true` if the sObject field is populated, either by direct assignment or
by inclusion in a SOQL query. Returns `false` if the sObject field isn’t set. If an invalid field is specified, an SObjectException is
thrown.

isSet(field)
Returns information about the queried sObject field. Returns `true` if the sObject field is populated, either by direct assignment or
by inclusion in a SOQL query. Returns `false` if the sObject field isn’t set. If an invalid field is specified, an SObjectException is
thrown.

put(fieldName, value)
Sets the value for the specified field and returns the previous value for the field.

put(field, value)
Sets the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as,
`Schema.Account.AccountNumber` and returns the previous value for the field.

putSObject(fieldName, value)
Sets the value for the specified field. This method is primarily used with dynamic DML for setting external IDs. The method returns
the previous value of the field.

putSObject(fieldName, value)
Sets the value for the field specified by the token `Schema.SObjectType` . This method is primarily used with dynamic DML for
setting external IDs. The method returns the previous value of the field.


Apex Reference Guide SObject Class

recalculateFormulas()
**Deprecated as of API version 57.0. Use the** `recalculateFormulas()` **method in the** `System.Formula` **class**
**instead.**

setOptions(DMLOptions)
Sets the DMLOptions object for the SObject.

##### addError(errorMsg)

Marks a trigger record with a custom error message and prevents any DML operation from occurring.

Signature

```
   public Void addError(String errorMsg)

```

Parameters

```
   errorMsg
```

Type: String

The error message to mark the record with.

Return Value

Type: Void

Usage

When used on `Trigger.new` in `insert` and `update` triggers, and on `Trigger.old` in `delete` triggers, the error message
is displayed in the application interface.

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers.htm)

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

When used in Visualforce controllers, the generated message is added to the collection of errors for the page. For more information, see
[Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_std.htm) _Visualforce Developer's Guide_ .

Example

```
   Trigger.new[0].addError('bad');

##### addError(errorMsg, escape)

```

Marks a trigger record with a custom error message, specifies if the error message should be escaped, and prevents any DML operation
from occurring.

Signature

```
   public Void addError(String errorMsg, Boolean escape)

```


Apex Reference Guide SObject Class

Parameters

```
   errorMsg
```

Type: String

The error message to mark the record with.

```
   escape
```

Type: Boolean

Indicates whether any HTML markup in the custom error message should be escaped ( `true` ) or not ( `false` ). This parameter is
ignored in both Lightning Experience and the Salesforce mobile app, and the HTML is always escaped. The escape parameter only
applies in Salesforce Classic.

Return Value

Type: Void

Usage

The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead,
it is displayed as text in the Salesforce user interface.

Warning: Be cautious if you specify `false` for the _`escape`_ argument. Unescaped strings displayed in the Salesforce user
interface can represent a vulnerability in the system because these strings might contain harmful code. If you want to include
HTML markup in the error message, call this method with a `false` _`escape`_ argument. Make sure that you escape any dynamic
content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call `addError(String`
_**`errorMsg`**_ `)` instead.

Example

```
   Trigger.new[0].addError('Fix & resubmit', false);

##### addError(exceptionError)

```

Marks a trigger record with a custom error message and prevents any DML operation from occurring.

Signature

```
   public Void addError(Exception exceptionError)

```

Parameters

```
   exceptionError
```

Type: System.Exception

An Exception object or a custom exception object that contains the error message to mark the record with.

Return Value

Type: Void


Apex Reference Guide SObject Class

Usage

When used on `Trigger.new` in `insert` and `update` triggers, and on `Trigger.old` in `delete` triggers, the error message
is displayed in the application interface.

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers.htm)

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

When used in Visualforce controllers, the generated message is added to the collection of errors for the page. For more information, see
[Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_std.htm) _Visualforce Developer's Guide_ .

Example

```
   public class MyException extends Exception {}

   Trigger.new[0].addError(new myException('Invalid Id'));

##### addError(exceptionError, escape)

```

Marks a trigger record with a custom exception error message, specifies whether or not the exception error message should be escaped,
and prevents any DML operation from occurring.

Signature

```
   public Void addError(Exception exceptionError, Boolean escape)

```

Parameters

```
   exceptionError
```

Type: System.Exception

An Exception object or a custom exception object that contains the error message to mark the record with.

```
   escape
```

Type: Boolean

Indicates whether any HTML markup in the custom error message should be escaped ( `true` ) or not ( `false` ). This parameter is
ignored in both Lightning Experience and the Salesforce mobile app, and the HTML is always escaped. The escape parameter only
applies in Salesforce Classic.

Return Value

Type: Void

Usage

The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead,
it is displayed as text in the Salesforce user interface.

Warning: Be cautious if you specify `false` for the _`escape`_ argument. Unescaped strings displayed in the Salesforce user
interface can represent a vulnerability in the system because these strings might contain harmful code. If you want to include
HTML markup in the error message, call this method with a `false` _`escape`_ argument. Make sure that you escape any dynamic


Apex Reference Guide SObject Class

content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call `addError(Exception e)`
instead.

Example

```
   public class MyException extends Exception {}

   Trigger.new[0].addError(new myException('Invalid Id & other issues', false));

##### addError(errorMsg)

```

Places the specified error message on a trigger record field in the Salesforce user interface and prevents any DML operation from occurring.

Signature

```
   public Void addError(String errorMsg)

```

Parameters

```
   errorMsg
```

Type: String

Return Value

Type: Void

Usage

Note:

**•** When used on `Trigger.new` in `before insert` and `before update` triggers, and on `Trigger.old` in `before`

`delete` triggers, the error appears in the application interface.

**•** When used in Visualforce controllers, if there is an `inputField` component bound to field, the message is attached to the
[component. For more information, see Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_std_validation_rules.htm) _Visualforce Developer's Guide_ .

**•** This method is highly specialized because the field identifier is not actually the invoking object—the sObject record is the invoker.
The field is simply used to identify the field that should be used to display the error.

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers.htm)

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

Example

```
   Trigger.new[0].myField__c.addError('bad');

##### addError(errorMsg, escape)

```

Places the specified error message, which can be escaped or unescaped, on a trigger record field in the Salesforce user interface, and
prevents any DML operation from occurring.


Apex Reference Guide SObject Class

Signature

```
   public Void addError(String errorMsg, Boolean escape)

```

Parameters

```
   errorMsg
```

Type: String

The error message to mark the record with.

```
   escape
```

Type: Boolean

Indicates whether any HTML markup in the custom error message should be escaped ( `true` ) or not ( `false` ). This parameter is
ignored in both Lightning Experience and the Salesforce mobile app, and the HTML is always escaped. The escape parameter only
applies in Salesforce Classic.

Return Value

Type:

Usage

The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead,
it is displayed as text in the Salesforce user interface.

Warning: Be cautious if you specify `false` for the _`escape`_ argument. Unescaped strings displayed in the Salesforce user
interface can represent a vulnerability in the system because these strings might contain harmful code. If you want to include
HTML markup in the error message, call this method with a `false` _`escape`_ argument. Make sure that you escape any dynamic
content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call _`field`_ `.addError(String`
_**`errorMsg`**_ `)` instead.

Example

```
   Trigger.new[0].myField__c.addError('Fix & resubmit', false);

##### addError(fieldName, errorMsg)

```

Dynamically add errors to fields of an SObject associated with the specified field name.

Signature

```
   public void addError(String fieldName, String errorMsg)

```

Parameters

```
   fieldName
```

Type: String

The field name of the SObject .

```
   errorMsg
```

Type: String


Apex Reference Guide SObject Class

The error message to be added. HTML special characters in the error message string are always escaped.

Return Value

Type: void

Usage

If the field name is an empty string or null, the error is associated with the SObject and not with a specific field.

Example

```
   // Add an error to an SObject field using the addError() method.

   Account acct = new Account(name = 'TestAccount');

   acct.addError('name', 'error in name field');

   // Use the hasErrors() method to verify that the error is added, and then the getErrors()

    method to validate the error.

   System.Assert(acct.hasErrors());

   List<Database.Error> errors = acct.getErrors();

   System.AssertEquals(1, errors.size());

##### addError(fieldToken, errorMsg)

```

Dynamically add errors to an SObject instance associated with the specified field.

Signature

```
   public void addError(Schema.SObjectField fieldToken, String errorMsg

```

Parameters

```
   fieldToken
```

Type: Schema.SObjectField

The field of the SObject instance.

```
   errorMsg
```

Type: String

The error message to be added. HTML special characters in the error message string are always escaped.

Return Value

Type: void

Usage

Use this method to add errors to the specified field token of a standard or custom object. If `fieldToken` is null, the error is associated
with the SObject and not with a specific field.


Apex Reference Guide SObject Class

Example

```
   // Add an error to a field of an SObject instance using the addError() method.

   Account acct = new Account(name = 'TestAccount');

   Schema.DescribeFieldResult nameDesc = Account.name.getDescribe();

   Schema.sObjectField nameField = nameDesc.getSObjectField();

   acct.addError(nameField, 'error is name field');

   // Use the hasErrors() method to verify that the error is added, and then the getErrors()

    method to validate the error.

   System.Assert(acct.hasErrors());

   List<Database.Error> errors = acct.getErrors();

   System.AssertEquals(1, errors.size());

##### addError(fieldName, errorMsg, escape)

```

Dynamically add errors to fields of an SObject associated with the specified field name.

Signature

```
   public void addError(String fieldName, String errorMsg, Boolean escape)

```

Parameters

```
   fieldName
```

Type: String

The field name of the SObject .

```
   errorMsg
```

Type: String

The error message to be added.

```
   escape
```

Type: Boolean

Indicates whether any HTML markup in the custom error message should be escaped ( `true` ) or not ( `false` ). This parameter is
ignored in both Lightning Experience and the Salesforce mobile app, and the HTML is always escaped. The escape parameter only
applies in Salesforce Classic.

Return Value

Type: void

Usage

If the field name is an empty string or null, the error is associated with the SObject and not with a specific field.

The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead,
it is displayed as text in the Salesforce user interface.

Warning:

**•** The _`escape`_ parameter cannot be disabled in Lightning Experience and in the Salesforce mobile app, and will be ignored.

**•** Be cautious if you specify `false` for the _`escape`_ argument. Unescaped strings displayed in the Salesforce user interface
can represent a vulnerability in the system because these strings might contain harmful code. If you want to include HTML


Apex Reference Guide SObject Class

markup in the error message, call this method with a `false` _`escape`_ argument. Make sure that you escape any dynamic
content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call `addError(String`
`fieldName, String errorMsg)` instead.

Example

```
   // Add an error to an SObject field using the addError() method.

   Account acct = new Account(name = 'TestAccount');

   acct.addError('name', 'error in name field', false);

   // Use the hasErrors() method to verify that the error is added, and then the getErrors()

    method to validate the error.

   System.Assert(acct.hasErrors());

   List<Database.Error> errors = acct.getErrors();

   System.AssertEquals(1, errors.size());

##### addError(fieldToken, errorMsg, escape)

```

Dynamically add errors to an SObject instance associated with the specified field.

Signature

```
   public void addError(Schema.SObjectField fieldToken, String errorMsg, Boolean escape)

```

Parameters

```
   fieldToken
```

Type: Schema.SObjectField

The field of the SObject instance.

```
   errorMsg
```

Type: String

The error message to be added.

```
   escape
```

Type: Boolean

Indicates whether any HTML markup in the custom error message should be escaped ( `true` ) or not ( `false` ). This parameter is
ignored in both Lightning Experience and the Salesforce mobile app, and the HTML is always escaped. The escape parameter only
applies in Salesforce Classic.

Return Value

Type: void

Usage

Use this method to add errors to the specified field token of a standard or custom object. If `fieldToken` is null, the error is associated
with the SObject and not with a specific field.

The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead,
it is displayed as text in the Salesforce user interface.


Apex Reference Guide SObject Class

Warning:

**•** The _`escape`_ parameter cannot be disabled in Lightning Experience and in the Salesforce mobile app, and will be ignored.

**•** Be cautious if you specify `false` for the _`escape`_ argument. Unescaped strings displayed in the Salesforce user interface
can represent a vulnerability in the system because these strings might contain harmful code. If you want to include HTML
markup in the error message, call this method with a `false` _`escape`_ argument. Make sure that you escape any dynamic
content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call
`addError(Schema.SObjectField fieldToken, String errorMsg)` instead.

Example

```
   // Add an error to a field of an SObject instance using the addError() method.

   Account acct = new Account(name = 'TestAccount');

   Schema.DescribeFieldResult nameDesc = Account.name.getDescribe();

   Schema.sObjectField nameField = nameDesc.getSObjectField();

   acct.addError(nameField, 'error is name field', false);

   // Use the hasErrors() method to verify that the error is added, and then the getErrors()

    method to validate the error.

   System.Assert(acct.hasErrors());

   List<Database.Error> errors = acct.getErrors();

   System.AssertEquals(1, errors.size());

##### clear()

```

Clears all field values

Signature

```
   public Void clear()

```

Return Value

Type: Void

Example

```
   Account acc = new account(Name = 'Acme');

   acc.clear();

   Account expected = new Account();

   system.assertEquals(expected, acc);

##### clone(preserveId)

```

Creates a copy of the SObject record.

Signature

```
   public SObject clone(Boolean preserveId)

```


Apex Reference Guide SObject Class

Parameters

```
   preserveId
```

Type: Boolean

Determines whether the ID of the original object is preserved or cleared in the duplicate. If set to `true`, the ID is copied to the
duplicate. The default is `false`, that is, the ID is cleared.

Return Value

Type: SObject (of the same type)

Usage

Note: For Apex saved using Salesforce API version 22.0 or earlier, the default value for the _`preserveId`_ argument is `true`,
that is, the ID is preserved.

##### clone(preserveId, isDeepClone)

Creates a copy of the SObject record.

Signature

```
   public SObject clone(Boolean preserveId, Boolean isDeepClone)

```

Parameters

```
   preserveId
```

Type: Boolean

Determines whether the ID of the original object is preserved or cleared in the duplicate. If set to `true`, the ID is copied to the
duplicate. The default is `false`, that is, the ID is cleared.

```
   isDeepClone
```

Type: Boolean

Determines whether the method creates a full copy of the SObject field or just a reference:

**•** If set to `true`, the method creates a full copy of the SObject. All fields on the SObject are duplicated in memory, including
relationship fields. Consequently, if you change a field on the cloned SObject, the original SObject isn’t affected.

**•** If set to `false`, the method performs a shallow copy of the SObject fields. All copied relationship fields reference the original
SObjects. Consequently, if you change a relationship field on the cloned SObject, the corresponding field on the original SObject
is also affected, and vice versa. The default is `false` .

Return Value

Type: SObject (of the same type)

Usage

Note: For Apex saved using Salesforce API version 22.0 or earlier, the default value for the _`preserveId`_ argument is `true`,
that is, the ID is preserved.


Apex Reference Guide SObject Class

##### clone(preserveId, isDeepClone, preserveReadonlyTimestamps)

Creates a copy of the SObject record.

Signature

```
   public SObject clone(Boolean preserveId, Boolean isDeepClone, Boolean

   preserveReadonlyTimestamps)

```

Parameters

```
   preserveId
```

Type: Boolean

Determines whether the ID of the original object is preserved or cleared in the duplicate. If set to `true`, the ID is copied to the
duplicate. The default is `false`, that is, the ID is cleared.

```
   isDeepClone
```

Type: Boolean

Determines whether the method creates a full copy of the SObject field or just a reference:

**•** If set to `true`, the method creates a full copy of the SObject. All fields on the SObject are duplicated in memory, including
relationship fields. Consequently, if you change a field on the cloned SObject, the original SObject isn’t affected.

**•** If set to `false`, the method performs a shallow copy of the SObject fields. All copied relationship fields reference the original
SObjects. Consequently, if you change a relationship field on the cloned SObject, the corresponding field on the original SObject
is also affected, and vice versa. The default is `false` .

```
   preserveReadonlyTimestamps
```

Type: Boolean

Determines whether the read-only timestamp fields are preserved or cleared in the duplicate. If set to `true`, the read-only fields
`CreatedById`, `CreatedDate`, `LastModifiedById`, and `LastModifiedDate` are copied to the duplicate. The
default is `false`, that is, the values are cleared.

Note: Audit field values won’t be persisted to the database via DML on the cloned SObject instance.

Return Value

Type: SObject (of the same type)

Usage

Note: For Apex saved using Salesforce API version 22.0 or earlier, the default value for the _`preserveId`_ argument is `true`,
that is, the ID is preserved.

##### clone(preserveId, isDeepClone, preserveReadonlyTimestamps, preserveAutonumber)

Creates a copy of the SObject record.

Signature

```
   public SObject clone(Boolean preserveId, Boolean isDeepClone, Boolean

   preserveReadonlyTimestamps, Boolean preserveAutonumber)

```


Apex Reference Guide SObject Class

Parameters

```
   preserveId
```

Type: Boolean

Determines whether the ID of the original object is preserved or cleared in the duplicate. If set to `true`, the ID is copied to the
duplicate. The default is `false`, that is, the ID is cleared.

```
   isDeepClone
```

Type: Boolean

Determines whether the method creates a full copy of the SObject field or just a reference:

**•** If set to `true`, the method creates a full copy of the SObject. All fields on the SObject are duplicated in memory, including
relationship fields. Consequently, if you change a field on the cloned SObject, the original SObject isn’t affected.

**•** If set to `false`, the method performs a shallow copy of the SObject fields. All copied relationship fields reference the original
SObjects. Consequently, if you change a relationship field on the cloned SObject, the corresponding field on the original SObject
is also affected, and vice versa. The default is `false` .

```
   preserveReadonlyTimestamps
```

Type: Boolean

Determines whether the read-only timestamp fields are preserved or cleared in the duplicate. If set to `true`, the read-only fields
`CreatedById`, `CreatedDate`, `LastModifiedById`, and `LastModifiedDate` are copied to the duplicate. The
default is `false`, that is, the values are cleared.

Note: Audit field values won’t be persisted to the database via DML on the cloned SObject instance.

```
   preserveAutonumber
```

Type: Boolean

Determines whether auto number fields of the original object are preserved or cleared in the duplicate. If set to `true`, auto number
fields are copied to the cloned object. The default is `false`, that is, auto number fields are cleared.

Return Value

Type: SObject (of the same type)

Usage

Note: For Apex saved using Salesforce API version 22.0 or earlier, the default value for the _`preserveId`_ argument is `true`,
that is, the ID is preserved.

Example

```
   Account acc = new account(Name = 'Acme', Description = 'Acme Account');

   Account clonedAcc = acc.clone(false, false, false, false);

   System.assertEquals(acc, clonedAcc);

##### get(fieldName)

```

Returns the value for the field specified by _`fieldName`_, such as `AccountNumber` .


Apex Reference Guide SObject Class

Signature

```
   public Object get(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Return Value

Type: Object

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

Example

```
   Account acc = new account(Name = 'Acme', Description = 'Acme Account');

   String description = (String)acc.get('Description');

   System.assertEquals('Acme Account', description);

```

Versioned Behavior Changes

In API version 34.0 and later, you must include the namespace name to retrieve a field from a field Map using this method. For example,
to get the _`account__c`_ field in the _`MyNamespace`_ namespace from a _`fields`_ field Map, use:
`fields.get(‘MyNamespace__account__c’)` .

##### get(field)

Returns the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as,
`Schema.Account.AccountNumber` .

Signature

```
   public Object get(Schema.sObjectField field)

```

Parameters

```
   field
```

Type: Schema.SObjectField

Return Value

Type: Object

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)


Apex Reference Guide SObject Class

Note: Field tokens aren't available for person accounts. If you access `Schema.Account.` _**`fieldname`**_, you get an exception
error. Instead, specify the field name as a string.

Example

```
   Account acc = new account(Name = 'Acme', Description = 'Acme Account');

   String description = (String)acc.get(Schema.Account.Description);

   System.assertEquals('Acme Account', description);

##### getCloneSourceId()

```

Returns the ID of the entity from which an object was cloned. You can use it for objects cloned through the Salesforce user interface.
You can also use it for objects created using the `System.SObject.clone(preserveId, isDeepClone,`
`preserveReadonlyTimestamps, preserveAutonumber)` method, provided that the _`preserveId`_ parameter wasn’t
##### used or was set to false . The getCloneSourceId() method can only be used within the transaction where the entity is cloned,

as clone information doesn’t persist in subsequent transactions.

Signature

```
   public Id getCloneSourceId()

```

Return Value

Type: Id

Usage

If A is cloned to B, B is cloned to C, and C is cloned to D, then B, C, and D all point back to A as their clone source.

Example

```
   Account acc0 = new Account(Name = 'Acme');

   insert acc0;

   Account acc1 = acc0.clone();

   Account acc2 = acc1.clone();

   Account acc3 = acc2.clone();

   Account acc4 = acc3.clone();

   System.assert(acc0.Id != null);

   System.assertEquals(acc0.Id, acc1.getCloneSourceId());

   System.assertEquals(acc0.Id, acc2.getCloneSourceId());

   System.assertEquals(acc0.Id, acc3.getCloneSourceId());

   System.assertEquals(acc0.Id, acc4.getCloneSourceId());

   System.assertEquals(null, acc0.getCloneSourceId());

##### getErrors()

```

Returns a list of `Database.Error` objects for an SObject instance. If the SObject has no errors, an empty list is returned.

Signature

```
   public List<Database.Error> getErrors()

```


Apex Reference Guide SObject Class

Return Value

Type: List<Database.Error>

##### getOptions()

Returns the database.DMLOptions object for the SObject.

Signature

```
   public Database.DMLOptions getOptions()

```

Return Value

Type: Database.DMLOptions

Example

```
   Database.DMLOptions dmo = new Database.dmlOptions();

   dmo.assignmentRuleHeader.useDefaultRule = true;

   Account acc = new Account(Name = 'Acme');

   acc.setOptions(dmo);

   Database.DMLOptions accDmo = acc.getOptions();

##### getPopulatedFieldsAsMap()

```

Returns a map of populated field names and their corresponding values. The map contains only the fields that have been populated in
memory for the SObject instance.

Signature

```
   public Map<String,Object> getPopulatedFieldsAsMap()

```

Return Value

Type: Map<String,Object>

A map of field names and their corresponding values.

Usage

The returned map contains only the fields that have been populated in memory for the SObject instance, which makes it easy to iterate
over those fields. A field is populated in memory in the following cases.

**•** The field has been queried by a SOQL statement.

##### • The field has been explicitly set before the call to the getPopulatedFieldsAsMap() method.

Fields on related objects that are queried or set are also returned in the map.

##### The following example iterates over the map returned by the getPopulatedFieldsAsMap() method after a SOQL query.

```
   Account a = new Account();

   a.name = 'TestMapAccount1';

```


Apex Reference Guide SObject Class

```
   insert a;

   a = [select Id,Name from Account where id=:a.Id];

   Map<String, Object> fieldsToValue = a.getPopulatedFieldsAsMap();

   for (String fieldName : fieldsToValue.keySet()){

      System.debug('field name is ' + fieldName + ', value is ' +

        fieldsToValue.get(fieldName));

   }

   // Example debug statement output:

   // DEBUG|field name is Id, value is 001R0000003EPPkIAO

   // DEBUG|field name is Name, value is TestMapAccount1

```

This example iterates over the map returned by the `getPopulatedFieldsAsMap()` method after fields on the SObject are
explicitly set.

```
   Account a = new Account();

   a.name = 'TestMapAccount2';

   a.phone = '123-4567';

   insert a;

   Map<String, Object> fieldsToValue = a.getPopulatedFieldsAsMap();

   for (String fieldName : fieldsToValue.keySet()) {

      System.debug('field name is ' + fieldName + ', value is ' +

        fieldsToValue.get(fieldName));

   }

   // Example debug statement output:

   // DEBUG|field name is Name, value is TestMapAccount2

   // DEBUG|field name is Phone, value is 123-4567

   // DEBUG|field name is Id, value is 001R0000003EPPpIAO

```

The following example shows how to use the `getPopulatedFieldsAsMap()` method with related objects.

```
   Account a = new Account();

   a.name='TestMapAccount3';

   insert a;

   Contact c = new Contact();

   c.firstname='TestContactFirstName';

   c.lastName ='TestContactLastName';

   c.accountid = a.id;

   insert c;

   c = [SELECT id, Contact.Firstname, Contact.Account.Name FROM Contact

        where id=:c.id limit 1];

   Map<String, Object> fieldsToValue = c.getPopulatedFieldsAsMap();

   // To get the fields on Account, get the Account object

   // and call getMapPopulatedFieldsAsMap() on that object.

   a = (Account)fieldsToValue.get('Account');

   fieldsToValue = a.getPopulatedFieldsAsMap();

   for (String fieldName : fieldsToValue.keySet()) {

      System.debug('field name is ' + fieldName + ', value is ' +

```


Apex Reference Guide SObject Class

```
        fieldsToValue.get(fieldName));

   }

   // Example debug statement output:

   // DEBUG|field name is Id, value is 001R0000003EPPuIAO

   // DEBUG|field name is Name, value is TestMapAccount3

```

Versioned Behavior Changes

In API version 39.0 and later, getPopulatedFieldsAsMap returns all values set on the SObject, even if values were set after the record was
queried. This behavior is dependent on the version of the apex class calling this method and not on the version of the class that generated
the SObject. If you query an SObject at API version 20.0, and then call this method in a class with API version 40.0, you will get the full
set of fields.

##### getSObject(fieldName)

Returns the value for the specified field. This method is primarily used with dynamic DML to access values for external IDs.

Signature

```
   public SObject getSObject(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Return Value

Type: SObject

Example

```
   Account acc = new account(Name = 'Acme', Description = 'Acme Account');

   insert acc;

   Contact con = new Contact(Lastname = 'AcmeCon', AccountId = acc.id);

   insert con;

   SObject contactDB =

      [SELECT Id, AccountId, Account.Name FROM Contact WHERE id = :con.id LIMIT 1];

   Account a = (Account)contactDB.getSObject('Account');

   System.assertEquals('Acme', a.name);

##### getSObject(field)

```

Returns the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as, `Schema.MyObj.MyExternalId` .
This method is primarily used with dynamic DML to access values for external IDs.

Signature

```
   public SObject getSObject(Schema.SObjectField field)

```


Apex Reference Guide SObject Class

Parameters

```
   field
```

Type: Schema.SObjectField

Return Value

Type: SObject

Usage

[If the method references polymorphic fields, a Name object is returned. Use the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_name.htm) `TYPEOF` clause in the SOQL SELECT statement to
[directly get results that depend on the runtime object type referenced by the polymorphic field. See Working with Polymorphic](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_polymorphic_relationships.htm)
[Relationships in SOQL Queries.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_polymorphic_relationships.htm)

Example

```
   Account acc = new account(name = 'Acme', description = 'Acme Account');

   insert acc;

   Contact con = new contact(lastname = 'AcmeCon', accountid = acc.id);

   insert con;

   Schema.DescribeFieldResult fieldResult = Contact.AccountId.getDescribe();

   Schema.SObjectField field = fieldResult.getSObjectField();

   SObject contactDB =

      [SELECT Id, AccountId, Account.Name FROM Contact WHERE id = :con.id LIMIT 1];

   Account a = (Account)contactDB.getSObject(field);

   System.assertEquals('Acme', a.name);

##### getSObjects(fieldName)

```

Returns the values for the specified field. This method is primarily used with dynamic DML to access values for associated objects, such
as child relationships.

Signature

```
   public SObject[] getSObjects(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Return Value

Type: SObject[]

Usage

[For more information, see Dynamic DML.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_dml.htm)


Apex Reference Guide SObject Class

Example

```
   Account acc = new account(name = 'Acme', description = 'Acme Account');

   insert acc;

   Contact con = new contact(lastname = 'AcmeCon', accountid = acc.id);

   insert con;

   SObject[] a = [SELECT id, (SELECT Name FROM Contacts LIMIT 1) FROM Account WHERE id =

   :acc.id];

   SObject[] contactsDB = a.get(0).getSObjects('Contacts');

   String fieldValue = (String)contactsDB.get(0).get('Name');

   System.assertEquals('AcmeCon', fieldValue);

##### getSObjects(fieldName)

```

Returns the value for the field specified by the field token `Schema.` _**`fieldName`**_, such as, `Schema.Account.Contact` . This
method is primarily used with dynamic DML to access values for associated objects, such as child relationships.

Signature

```
   public SObject[] getSObjects(Schema.SObjectType fieldName)

```

Parameters

```
   fieldName
```

Type: Schema.SObjectType

Return Value

Type: SObject[]

##### getSObjectType()

Returns the token for this SObject. This method is primarily used with describe information.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Usage

For more information, see apex_dynamic_describe_objects_understanding.


Apex Reference Guide SObject Class

Example

```
   Account acc = new Account(name = 'Acme', description = 'Acme Account');

   Schema.SObjectType expected = Schema.Account.getSObjectType();

   System.assertEquals(expected, acc.getSObjectType());

##### getQuickActionName()

```

Retrieves the name of a quick action associated with this SObject. Typically used in triggers.

Signature

```
   public String getQuickActionName()

```

Return Value

Type: String

Example

```
   trigger accTrig2 on Contact (before insert) {

      for (Contact c : Trigger.new) {

        if (c.getQuickActionName() == QuickAction.CreateContact) {

           c.WhereFrom__c = 'GlobaActionl';

        } else if (c.getQuickActionName() == Schema.Account.QuickAction.CreateContact) {

           c.WhereFrom__c = 'AccountAction';

        } else if (c.getQuickActionName() == null) {

           c.WhereFrom__c = 'NoAction';

        } else {

           System.assert(false);

        }

      }

   }

##### hasErrors()

```

Returns true if an SObject instance has associated errors. The error message can be associated to the SObject instance by using
`SObject.addError()`, validation rules, or by other means.

Signature

```
   public Boolean hasErrors()

```

Return Value

Type: Boolean

##### isClone()

Returns `true` if an entity is cloned from something, even if the entity hasn’t been saved. The method can only be used within the
transaction where the entity is cloned, as clone information doesn’t persist in subsequent transactions.


Apex Reference Guide SObject Class

Signature

```
   public Boolean isClone()

```

Return Value

Type: Boolean

Example

```
   Account acc = new Account(Name = 'Acme');

   insert acc;

   Account acc2 = acc.clone();

   // Test before saving

   System.assertEquals(true, acc2.isClone());

   insert acc2;

   // Test after saving

   System.assertEquals(true, acc2.isClone());

##### isSet(fieldName)

```

Returns information about the queried sObject field. Returns `true` if the sObject field is populated, either by direct assignment or by
inclusion in a SOQL query. Returns `false` if the sObject field isn’t set. If an invalid field is specified, an SObjectException is thrown.

Signature

```
   public Boolean isSet(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Return Value

Type: Boolean

Usage

##### The isSet method doesn’t check if a field is accessible to a specific user via org permissions or other specialized access permissions.

Example

```
   Contact c = new Contact(LastName = 'Joyce');

   System.assertEquals(true, c.isSet('LastName'));

   System.assertEquals(false, c.isSet('FirstName')); // FirstName field is not written to

   c.firstName = null;

   System.assertEquals(true, c.isSet('FirstName')); //FirstName field is written to

```


Apex Reference Guide SObject Class

##### isSet(field)

Returns information about the queried sObject field. Returns `true` if the sObject field is populated, either by direct assignment or by
inclusion in a SOQL query. Returns `false` if the sObject field isn’t set. If an invalid field is specified, an SObjectException is thrown.

Signature

```
   public Boolean isSet(Schema.SObjectField field)

```

Parameters

```
   field
```

Type:SObjectField Class

Return Value

Type: Boolean

Usage

##### The isSet method doesn’t check if a field is accessible to a specific user via org permissions or other specialized access permissions.

Example

```
   Contact newContact = new Contact(LastName = 'Joyce');

   insert(newContact); //Insert a new contact with last name Joyce

   Contact c = [SELECT FirstName FROM Contact WHERE Id = :newContact.Id];

   System.assertEquals(true, c.isSet(Contact.FirstName)); //FirstName field in query

   System.assertEquals(false, c.isSet(Contact.LastName)); //LastName field not in query

##### put(fieldName, value)

```

Sets the value for the specified field and returns the previous value for the field.

Signature

```
   public Object put(String fieldName, Object value)

```

Parameters

```
   fieldName
```

Type: String

```
   value
```

Type: Object

Return Value

Type: Object


Apex Reference Guide SObject Class

Example

```
   Account acc = new Account(name = 'test', description = 'old desc');

   String oldDesc = (String)acc.put('description', 'new desc');

   System.assertEquals('old desc', oldDesc);

   System.assertEquals('new desc', acc.description);

##### put(field, value)

```

Sets the value for the field specified by the field token `Schema.` _**`sObjectField`**_, such as, `Schema.Account.AccountNumber`
and returns the previous value for the field.

Signature

```
   public Object put(Schema.SObjectField field, Object value)

```

Parameters

```
   field
```

Type: Schema.SObjectField

```
   value
```

Type: Object

Return Value

Type: Object

Example

```
   Account acc = new Account(name = 'test', description = 'old desc');

   String oldDesc = (String)acc.put(Schema.Account.Description, 'new desc');

   System.assertEquals('old desc', oldDesc);

   System.assertEquals('new desc', acc.description);

```

Note: Field tokens aren't available for person accounts. If you access `Schema.Account.` _**`fieldname`**_, you get an exception
error. Instead, specify the field name as a string.

##### putSObject(fieldName, value)

Sets the value for the specified field. This method is primarily used with dynamic DML for setting external IDs. The method returns the
previous value of the field.

Signature

```
   public SObject putSObject(String fieldName, SObject value)

```

Parameters

```
   fieldName
```

Type: String


Apex Reference Guide SObject Class

```
   value
```

Type: SObject

Return Value

Type: SObject

Example

```
   Account acc = new Account(name = 'Acme', description = 'Acme Account');

   insert acc;

   Contact con = new contact(lastname = 'AcmeCon', accountid = acc.id);

   insert con;

   Account acc2 = new account(name = 'Not Acme');

   Contact contactDB =

      (Contact)[SELECT Id, AccountId, Account.Name FROM Contact WHERE id = :con.id LIMIT 1];

   Account a = (Account)contactDB.putSObject('Account', acc2);

   System.assertEquals('Acme', a.name);

   System.assertEquals('Not Acme', contactDB.Account.name);

##### putSObject(fieldName, value)

```

Sets the value for the field specified by the token `Schema.SObjectType` . This method is primarily used with dynamic DML for
setting external IDs. The method returns the previous value of the field.

Signature

```
   public SObject putSObject(Schema.SObjectType fieldName, SObject value)

```

Parameters

```
   fieldName
```

Type: Schema.SObjectType

```
   value
```

Type: SObject

Return Value

Type: SObject

##### **`recalculateFormulas()`** Deprecated as of API version 57.0. Use the recalculateFormulas() method in the System.Formula class instead.

Signature

```
   public Void recalculateFormulas()

```


### Apex Reference Guide SObjectAccessDecision Class

Return Value

Type: Void

Usage

This method doesn’t recalculate cross-object formulas. If you call this method on objects that have both cross-object and non-cross-object
formula fields, only the non-cross-object formula fields are recalculated.

Each `recalculateFormulas` [call counts against the SOQL query limits. See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

SEE ALSO:

recalculateFormulas(sobjects)

[What Is a Cross-Object Formula?](https://help.salesforce.com/HTViewHelpDoc?id=customize_cross_object.htm&language=en_US)

##### setOptions(DMLOptions)

Sets the DMLOptions object for the SObject.

Signature

```
   public Void setOptions(database.DMLOptions DMLOptions)

```

Parameters

```
   DMLOptions
```

Type: Database.DMLOptions

Return Value

Type: Void

Example

```
   Database.DMLOptions dmo = new Database.dmlOptions();

   dmo.assignmentRuleHeader.useDefaultRule = true;

   Account acc = new Account(Name = 'Acme');

   acc.setOptions(dmo);

### SObjectAccessDecision Class

```

Contains the results of a call to the Security.stripInaccessible method and methods to retrieve those results.

Namespace

System


Apex Reference Guide SObjectAccessDecision Class

IN THIS SECTION:

#### SObjectAccessDecision Methods SObjectAccessDecision Methods The following are methods for SObjectAccessDecision .

IN THIS SECTION:

##### getModifiedIndexes()

Returns the indexes of sObjects that are modified by the stripInaccessible method.

getRecords()
Returns a list of new sObjects that are identical to the source records, except that they are stripped of fields that fail the field-level
security check for the current user.

getRemovedFields()
Returns a map of sObject types to their corresponding inaccessible fields. The map key is a string representation of the sObject type.
The map value is a set of strings, which denote the fields names that are inaccessible.

##### **`getModifiedIndexes()`**

Returns the indexes of sObjects that are modified by the stripInaccessible method.

Signature

```
   public Set<Integer> getModifiedIndexes()

```

Return Value

Type: Set<Integer>

A set of unsigned integers that represent the row indexes of the modified sObjects.

Example

In this example, the user doesn’t have permission to update the `AnnualRevenue` field of an Account.

```
   List<Account> accounts = new List<Account>{

      new Account(Name='Account1', AnnualRevenue=1000),

      new Account(Name='Account2')

   };

   // Strip fields that are not updatable

   SObjectAccessDecision decision = Security.stripInaccessible(

      AccessType.UPDATABLE,

      accounts);

   // Print stripped records

   for (SObject strippedAccount : decision.getRecords()) {

      System.debug(strippedAccount);

   }

```


Apex Reference Guide SObjectAccessDecision Class

```
   // Print modified indexes

   System.debug(decision.getModifiedIndexes());

##### **`getRecords()`**

```

Returns a list of new sObjects that are identical to the source records, except that they are stripped of fields that fail the field-level security
check for the current user.

Usage

The stripInaccessible method performs field-level access check for the source records in the context of the current user’s operation. The
##### getRecords() method returns the new records that contain only the fields that the current user has access to.

Signature

```
   public List<SObject> getRecords()

```

Return Value

Type: List<SObject>

Even if the result list contains only one sObject, the return type is still a list (of size one).

Example

In this example, the user doesn’t have permission to update the `AnnualRevenue` field of an Account.

```
   List<Account> accounts = new List<Account>{

      new Account(Name='Account1', AnnualRevenue=1000),

      new Account(Name='Account2')

   };

   // Strip fields that are not updatable

   SObjectAccessDecision decision = Security.stripInaccessible(

      AccessType.UPDATABLE,

      accounts);

   // Print stripped records

   for (SObject strippedAccount : decision.getRecords()) {

      System.debug(strippedAccount);

   }

##### getRemovedFields()

```

Returns a map of sObject types to their corresponding inaccessible fields. The map key is a string representation of the sObject type. The
map value is a set of strings, which denote the fields names that are inaccessible.

Signature

```
   public Map<String,Set<String>> getRemovedFields()

```


### Apex Reference Guide SoqlStubProvider Class

Return Value

Type: Map<String,Set<String>>

Example

In this example, the user doesn’t have permission to update the `AnnualRevenue` field of an Account.

```
   List<Account> accounts = new List<Account>{

      new Account(Name='Account1', AnnualRevenue=1000),

      new Account(Name='Account2')

   };

   // Strip fields that are not updatable

   SObjectAccessDecision decision = Security.stripInaccessible(

      AccessType.UPDATABLE,

      accounts);

   // Print stripped records

   for (SObject strippedAccount : decision.getRecords()) {

      System.debug(strippedAccount);

   }

   // Print removed fields

   System.debug(decision.getRemovedFields());

### SoqlStubProvider Class

```

Contains a method to create a mock test class for handling SOQL query responses for Data 360 data model objects (DMOs).

Namespace

System

Usage

### To create mock test classes, extend the SoqlStubProvider class and override the handleSoqlQuery() class method.

Note: SOQL `[For](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_loops_for_SOQL.htm)` Loops in Apex aren't supported for SOQL stubs in static or dynamic SOQL queries against DMOs.

[See Mock SOQL Tests for Data 360 Data Model Objects in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm) _Apex Developer Guide_ .

Example

This example shows a mock test class for the _`SkyMilesForBusinessOptInController`_ class.

```
   @IsTest

   public class SkyMilesForBusinessOptInController_Test {

      @IsTest

      public static void mockSoql() {

        SoqlStubProvider stub = new UnifiedIndividualSoqlStub();

        Test.createSoqlStub(UnifiedIndividual__dlm.sObjectType, stub);

```


Apex Reference Guide SoqlStubProvider Class

```
        Assert.isTrue(Test.isSoqlStubDefined(UnifiedIndividual__dlm.sObjectType));

        Test.startTest();

        string companyId = 'SampleCompanyId';

        // Performs SOQL query against Data Model Object

        List<SkyMilesMember> members =

   SkyMilesForBusinessOptInController.getSkyMilesProfilesFromDataCloud(companyId);

        Test.stopTest();

        Assert.areEqual(1, members.size());

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

```


Apex Reference Guide SoqlStubProvider Class

```
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

IN THIS SECTION:

#### SoqlStubProvider Methods SoqlStubProvider Methods The following are methods for SoqlStubProvider .

IN THIS SECTION:

##### handleSoqlQuery(targetType, stubbedQuery, bindMap)

Defines a mocked response for a SOQL query executed against the specified SObject type.

##### **`handleSoqlQuery(targetType, stubbedQuery, bindMap)`**

Defines a mocked response for a SOQL query executed against the specified SObject type.


### Apex Reference Guide StaticResourceCalloutMock Class

Signature

```
   public List<SObject> handleSoqlQuery(Schema.SObjectType targetType, String stubbedQuery,

   Map<String,Object> bindMap)

```

Parameters

```
   targetType
```

Type: Schema.SObjectType

The SObject type to be stubbed. This parameter can’t be null.

```
   stubbedQuery
```

Type: String

The SOQL query whose response is to be stubbed. Bind variables are replaced with placeholders.

```
   bindMap
```

Type: Map<String,Object>

A map that contains placeholder keys for each bind variable specified in the SOQL query string and its value.

Return Value

Type: List<SObject>

The list of stubbed SObjects resulting from the SOQL query.

SEE ALSO:

Test Class

_Apex Developer Guide:_ [Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)

### StaticResourceCalloutMock Class

Utility class used to specify a fake response for testing HTTP callouts.

Namespace

System

Usage

Use the methods in this class to set the response properties for testing HTTP callouts.

IN THIS SECTION:

#### StaticResourceCalloutMock Constructors

StaticResourceCalloutMock Methods

#### StaticResourceCalloutMock Constructors

### The following are constructors for StaticResourceCalloutMock .


Apex Reference Guide StaticResourceCalloutMock Class

IN THIS SECTION:

##### StaticResourceCalloutMock() Creates a new instance of the StaticResourceCalloutMock class. StaticResourceCalloutMock() Creates a new instance of the StaticResourceCalloutMock class.

Signature

```
   public StaticResourceCalloutMock()

#### StaticResourceCalloutMock Methods

##### The following are methods for StaticResourceCalloutMock . All are instance methods.

```

IN THIS SECTION:

##### setHeader(headerName, headerValue)

Sets the specified header name and value for the fake response.

setStaticResource(resourceName)
Sets the specified static resource, which contains the response body.

setStatus(httpStatus)
Sets the specified HTTP status for the response.

setStatusCode(httpStatusCode)
Sets the specified HTTP status for the response.

##### setHeader(headerName, headerValue)

Sets the specified header name and value for the fake response.

Signature

```
   public Void setHeader(String headerName, String headerValue)

```

Parameters

```
   headerName
```

Type: String

```
   headerValue
```

Type: String

Return Value

Type: Void


Apex Reference Guide StaticResourceCalloutMock Class

##### setStaticResource(resourceName)

Sets the specified static resource, which contains the response body.

Signature

```
   public Void setStaticResource(String resourceName)

```

Parameters

```
   resourceName
```

Type: String

Return Value

Type: Void

##### setStatus(httpStatus)

Sets the specified HTTP status for the response.

Signature

```
   public Void setStatus(String httpStatus)

```

Parameters

```
   httpStatus
```

Type: String

Return Value

Type: Void

##### setStatusCode(httpStatusCode)

Sets the specified HTTP status for the response.

Signature

```
   public Void setStatusCode(Integer httpStatusCode)

```

Parameters

```
   httpStatusCode
```

Type: Integer

Return Value

Type: Void


### Apex Reference Guide String Class String Class

Contains methods for the String primitive data type.

Namespace

System

Usage

[All string method definitions adhere to the Unicode Standard. For example, Unicode Roman numerals are classified as a type of number](https://www.unicode.org/standard/standard.html)
form, not a type of digit. Therefore, string methods such as `isAlphanumeric()` return `false` if used on a String that contains a
[Roman numeral. For Unicode classifications, see the Unicode Character Code Charts.](https://www.unicode.org/charts/)

[For more information on Strings, see String Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### String Methods

### The following are methods for String .

IN THIS SECTION:

abbreviate(maxWidth)
Returns an abbreviated version of the String, of the specified length and with ellipses appended if the current String is longer than
the specified length; otherwise, returns the original String without ellipses.

abbreviate(maxWidth, offset)
Returns an abbreviated version of the String, starting at the specified character offset and of the specified length. The returned String
has ellipses appended at the start and the end if characters have been removed at these locations.

capitalize()
Returns the current String with the first letter changed to title case.

center(size)
Returns a version of the current String of the specified size padded with spaces on the left and right, so that it appears in the center.
If the specified size is smaller than the current String size, the entire String is returned without added spaces.

center(size, paddingString)
Returns a version of the current String of the specified size padded with the specified String on the left and right, so that it appears
in the center. If the specified size is smaller than the current String size, the entire String is returned without padding.

charAt(index)
Returns the value of the character at the specified index.

codePointAt(index)
Returns the Unicode code point value at the specified index.

codePointBefore(index)
Returns the Unicode code point value that occurs before the specified index.

codePointCount(beginIndex, endIndex)
Returns the number of Unicode code points within the specified text range.

compareTo(secondString)
Compares two strings lexicographically, based on the Unicode value of each character in the Strings.


Apex Reference Guide String Class

contains(substring)
Returns `true` if and only if the String that called the method contains the specified sequence of characters in _`substring`_ .

containsAny(inputString)
Returns `true` if the current String contains any of the characters in the specified String; otherwise, returns `false` .

containsIgnoreCase(substring)
Returns `true` if the current String contains the specified sequence of characters without regard to case; otherwise, returns `false` .

containsNone(inputString)
Returns `true` if the current String doesn’t contain any of the characters in the specified String; otherwise, returns `false` .

containsOnly(inputString)
Returns `true` if the current String contains characters only from the specified sequence of characters and not any other characters;
otherwise, returns `false` .

containsWhitespace()
Returns `true` if the current String contains any white space characters; otherwise, returns `false` .

countMatches(substring)
Returns the number of times the specified substring occurs in the current String.

deleteWhitespace()
Returns a version of the current String with all white space characters removed.

difference(secondString)
Returns the difference between the current String and the specified String.

endsWith(suffix)
Returns `true` if the String that called the method ends with the specified _`suffix`_ .

endsWithIgnoreCase(suffix)
Returns `true` if the current String ends with the specified suffix; otherwise, returns `false` .

equals(secondString)
Deprecated. This method is replaced by `equals(stringOrId)` . Returns `true` if the passed-in string is not null and represents
the same binary sequence of characters as the current string. Use this method to perform case-sensitive comparisons.

equals(stringOrId)
Returns `true` if the passed-in object is not null and represents the same binary sequence of characters as the current string. Use
this method to compare a string to an object that represents a string or an ID.

equalsIgnoreCase(secondString)
Returns `true` if the _`secondString`_ isn’t null and represents the same sequence of characters as the String that called the
method, ignoring case.

escapeCsv()
Returns a String for a CSV column enclosed in double quotes, if required.

escapeEcmaScript()
Escapes the characters in the String using EcmaScript String rules.

escapeHtml3()
Escapes the characters in a String using HTML 3.0 entities.

escapeHtml4()
Escapes the characters in a String using HTML 4.0 entities.


Apex Reference Guide String Class

escapeJava()
Returns a String whose characters are escaped using Java String rules. Characters escaped include quotes and control characters,
such as tab, backslash, and carriage return characters.

escapeSingleQuotes(stringToEscape)
Returns a String with the escape character ( `\` ) added before any single quotation mark ( `'` ) or backslash ( `\` ) in the String _`s`_ .

escapeUnicode()
Returns a String whose Unicode characters are escaped to a Unicode escape sequence.

escapeXml()
Escapes the characters in a String using XML entities.

format(stringToFormat, formattingArguments)
Treat the first argument as a pattern and return a string using the second argument for substitution and formatting. The substitution
and formatting are the same as `apex:outputText` and the Java `MessageFormat` class. Non-string types in the second
argument’s List are implicitly converted to strings, respecting the toString() method overrides that exist on the type.

fromCharArray(charArray)
Returns a String from the values of the list of integers.

getChars()
Returns an array of character values that represent the characters in this string.

getCommonPrefix(strings)
Returns the initial sequence of characters as a String that is common to all the specified Strings.

getLevenshteinDistance(stringToCompare)
Returns the Levenshtein distance between the current String and the specified String.

getLevenshteinDistance(stringToCompare, threshold)
Returns the Levenshtein distance between the current String and the specified String if it is less than or equal than the given threshold;
otherwise, returns -1.

hashCode()
Returns a hash code value for this string.

indexOf(substring)
Returns the index of the first occurrence of the specified substring. If the substring does not occur, this method returns -1.

indexOf(substring, index)
Returns the zero-based index of the first occurrence of the specified substring from the point of the given index. If the substring
does not occur, this method returns -1.

indexOfAny(substring)
Returns the zero-based index of the first occurrence of any character specified in the substring. If none of the characters occur, returns
-1.

indexOfAnyBut(substring)
Returns the zero-based index of the first occurrence of a character that is not in the specified substring. Otherwise, returns -1.

indexOfChar(character)
Returns the index of the first occurrence of the character that corresponds to the specified character value.

indexOfChar(character, startIndex)
Returns the index of the first occurrence of the character that corresponds to the specified character value, starting from the specified
index.


Apex Reference Guide String Class

indexOfDifference(stringToCompare)
Returns the zero-based index of the character where the current String begins to differ from the specified String.

indexOfIgnoreCase(substring)
Returns the zero-based index of the first occurrence of the specified substring without regard to case. If the substring does not occur,
this method returns -1.

indexOfIgnoreCase(substring, startPosition)
Returns the zero-based index of the first occurrence of the specified substring from the point of index _`i`_, without regard to case. If
the substring does not occur, this method returns -1.

isAllLowerCase()
Returns `true` if all characters in the current String are lowercase; otherwise, returns `false` .

isAllUpperCase()
Returns `true` if all characters in the current String are uppercase; otherwise, returns `false` .

isAlpha()
Returns `true` if all characters in the current String are Unicode letters only; otherwise, returns `false` .

isAlphaSpace()
Returns `true` if all characters in the current String are Unicode letters or spaces only; otherwise, returns `false` .

isAlphanumeric()
Returns `true` if all characters in the current String are Unicode letters or digits only; otherwise, returns `false` .

isAlphanumericSpace()
Returns `true` if all characters in the current String are Unicode letters, digits, or spaces only; otherwise, returns `false` .

isAsciiPrintable()
Returns `true` if the current String contains only ASCII printable characters; otherwise, returns `false` .

isBlank(inputString)
Returns `true` if the specified String is white space, empty (''), or null; otherwise, returns `false` .

isEmpty(inputString)
Returns `true` if the specified String is empty ('') or null; otherwise, returns `false` .

isNotBlank(inputString)
Returns `true` if the specified String is not whitespace, not empty (''), and not null; otherwise, returns `false` .

isNotEmpty(inputString)
Returns `true` if the specified String is not empty ('') and not null; otherwise, returns `false` .

isNumeric()
Returns `true` if the current String contains only Unicode digits; otherwise, returns `false` .

isNumericSpace()
Returns `true` if the current String contains only Unicode digits or spaces; otherwise, returns `false` .

isWhitespace()
Returns `true` if the current String contains only white space characters or is empty; otherwise, returns `false` .

join(iterableObj, separator)
Joins the elements of the specified iterable object, such as a List, into a single String separated by the specified separator.

lastIndexOf(substring)
Returns the index of the last occurrence of the specified substring. If the substring does not occur, this method returns -1.


Apex Reference Guide String Class

lastIndexOf(substring, endPosition)
Returns the index of the last occurrence of the specified substring, starting from the character at index 0 and ending at the specified
index.

lastIndexOfChar(character)
Returns the index of the last occurrence of the character that corresponds to the specified character value.

lastIndexOfChar(character, endIndex)
Returns the index of the last occurrence of the character that corresponds to the specified character value, starting from the specified
index.

lastIndexOfIgnoreCase(substring)
Returns the index of the last occurrence of the specified substring regardless of case.

lastIndexOfIgnoreCase(substring, endPosition)
Returns the index of the last occurrence of the specified substring regardless of case, starting from the character at index 0 and
ending at the specified index.

left(length)
Returns the leftmost characters of the current String of the specified length.

leftPad(length)
Returns the current String padded with spaces on the left and of the specified length.

leftPad(length, padStr)
Returns the current String padded with String `padStr` on the left and of the specified length.

length()
Returns the number of 16-bit Unicode characters contained in the String.

mid(startIndex, length)
Returns a new String that begins with the character at the specified zero-based _`startIndex`_ with the number of characters
specified by _`length`_ .

normalizeSpace()
Returns the current String with leading, trailing, and repeating white space characters removed.

offsetByCodePoints(index, codePointOffset)
Returns the index of the Unicode code point that is offset by the specified number of code points, starting from the given index.

remove(substring)
Removes all occurrences of the specified substring and returns the String result.

removeEnd(substring)
Removes the specified substring only if it occurs at the end of the String.

removeEndIgnoreCase(substring)
Removes the specified substring only if it occurs at the end of the String using a case-insensitive match.

removeStart(substring)
Removes the specified substring only if it occurs at the beginning of the String.

removeStartIgnoreCase(substring)
Removes the specified substring only if it occurs at the beginning of the String using a case-insensitive match.

repeat(numberOfTimes)
Returns the current String repeated the specified number of times.


Apex Reference Guide String Class

repeat(separator, numberOfTimes)
Returns the current String repeated the specified number of times using the specified separator to separate the repeated Strings.

replace(target, replacement)
Replaces each substring of a string that matches the literal target sequence _`target`_ with the specified literal replacement sequence
_`replacement`_ .

replaceAll(regExp, replacement)
Replaces each substring of a string that matches the regular expression _`regExp`_ with the replacement sequence _`replacement`_ .

replaceFirst(regExp, replacement)
Replaces the first substring of a string that matches the regular expression _`regExp`_ with the replacement sequence _`replacement`_ .

reverse()
Returns a String with all the characters reversed.

right(length)
Returns the rightmost characters of the current String of the specified length.

rightPad(length)
Returns the current String padded with spaces on the right and of the specified length.

rightPad(length, padStr)
Returns the current String padded with String `padStr` on the right and of the specified length.

split(regExp)
Returns a list that contains each substring of the String that is terminated by either the regular expression _`regExp`_ or the end of
the String.

split(regExp, limit)
Returns a list that contains each substring of the String that is terminated by either the regular expression _`regExp`_ or the end of
the String.

splitByCharacterType()
Splits the current String by character type and returns a list of contiguous character groups of the same type as complete tokens.

splitByCharacterTypeCamelCase()
Splits the current String by character type and returns a list of contiguous character groups of the same type as complete tokens,
with the following exception: the uppercase character, if any, immediately preceding a lowercase character token belongs to the
following character token rather than to the preceding.

startsWith(prefix)
Returns `true` if the String that called the method begins with the specified _`prefix`_ .

startsWithIgnoreCase(prefix)
Returns `true` if the current String begins with the specified prefix regardless of the prefix case.

stripHtmlTags()
Removes HTML markup and returns plain text.

substring(startIndex)
Returns a new String that begins with the character at the specified zero-based _`startIndex`_ and extends to the end of the String.

substring(startIndex, endIndex)
Returns a new String that begins with the character at the specified zero-based _`startIndex`_ and extends to the character at
_`endIndex`_    - 1.


Apex Reference Guide String Class

substringAfter(separator)
Returns the substring that occurs after the first occurrence of the specified separator.

substringAfterLast(separator)
Returns the substring that occurs after the last occurrence of the specified separator.

substringBefore(separator)
Returns the substring that occurs before the first occurrence of the specified separator.

substringBeforeLast(separator)
Returns the substring that occurs before the last occurrence of the specified separator.

substringBetween(tag)
Returns the substring that occurs between two instances of the specified _`tag`_ String.

substringBetween(open, close)
Returns the substring that occurs between the two specified Strings.

swapCase()
Swaps the case of all characters and returns the resulting String by using the default (English US) locale.

toLowerCase()
Converts all of the characters in the String to lowercase using the rules of the default (English US) locale.

toLowerCase(locale)
Converts all of the characters in the String to lowercase using the rules of the specified locale.

toUpperCase()
Converts all of the characters in the String to uppercase using the rules of the default (English US) locale.

toUpperCase(locale)
Converts all of the characters in the String to the uppercase using the rules of the specified locale.

template(valueMap)
Substitutes variables in a string for their corresponding values in the `valueMap` parameter, and returns the updated string.

trim()
Returns a copy of the string that no longer contains any leading or trailing white space characters.

uncapitalize()
Returns the current String with the first letter in lowercase.

unescapeCsv()
Returns a String representing an unescaped CSV column.

unescapeEcmaScript()
Unescapes any EcmaScript literals found in the String.

unescapeHtml3()
Unescapes the characters in a String using HTML 3.0 entities.

unescapeHtml4()
Unescapes the characters in a String using HTML 4.0 entities.

unescapeJava()
Returns a String whose Java literals are unescaped. Literals unescaped include escape sequences for quotes (\\") and control characters,
such as tab (\\t), and carriage return (\\n).

unescapeUnicode()
Returns a String whose escaped Unicode characters are unescaped.


Apex Reference Guide String Class

unescapeXml()
Unescapes the characters in a String using XML entities.

valueOf(dateToConvert)
Returns a String that represents the specified Date in the standard “yyyy-MM-dd” format.

valueOf(datetimeToConvert)
Returns a String that represents the specified Datetime in the standard “yyyy-MM-dd HH:mm:ss” format for the local time zone.

valueOf(decimalToConvert)
Returns a String that represents the specified Decimal.

valueOf(doubleToConvert)
Returns a String that represents the specified Double.

valueOf(integerToConvert)
Returns a String that represents the specified Integer.

valueOf(longToConvert)
Returns a String that represents the specified Long.

valueOf(toConvert)
Returns a string representation of the specified object argument.

valueOfGmt(datetimeToConvert)
Returns a String that represents the specified Datetime in the standard “yyyy-MM-dd HH:mm:ss” format for the GMT time zone.

##### abbreviate(maxWidth)

Returns an abbreviated version of the String, of the specified length and with ellipses appended if the current String is longer than the
specified length; otherwise, returns the original String without ellipses.

Signature

```
   public String abbreviate(Integer maxWidth)

```

Parameters

```
   maxWidth
```

Type: Integer

If _`maxWidth`_ is less than four, this method throws a run-time exception.

Return Value

Type: String

Example

```
   String s = 'Hello Maximillian';

   String s2 = s.abbreviate(8);

   System.assertEquals('Hello...', s2);

   System.assertEquals(8, s2.length());

```


Apex Reference Guide String Class

##### abbreviate(maxWidth, offset)

Returns an abbreviated version of the String, starting at the specified character offset and of the specified length. The returned String
has ellipses appended at the start and the end if characters have been removed at these locations.

Signature

```
   public String abbreviate(Integer maxWidth, Integer offset)

```

Parameters

```
   maxWidth
```

Type: Integer

Note that the offset is not necessarily the leftmost character in the returned String or the first character following the ellipses, but it
##### appears somewhere in the result. Regardless, abbreviate won’t return a String of length greater than maxWidth .If maxWidth

is too small, this method throws a run-time exception.

```
   offset
```

Type: Integer

Return Value

Type: String

Example

```
   String s = 'Hello Maximillian';

   // Start at M

   String s2 = s.abbreviate(9,6);

   System.assertEquals('...Max...', s2);

   System.assertEquals(9, s2.length());

##### capitalize()

```

Returns the current String with the first letter changed to title case.

Signature

```
   public String capitalize()

```

Return Value

Type: String

Usage

This method is based on the `[Character.toTitleCase(char)](http://docs.oracle.com/javase/6/docs/api/java/lang/Character.html?is-external=true#toTitleCase%28char%29)` Java method.


Apex Reference Guide String Class

Example

```
   String s = 'hello maximillian';

   String s2 = s.capitalize();

   System.assertEquals('Hello maximillian', s2);

##### center(size)

```

Returns a version of the current String of the specified size padded with spaces on the left and right, so that it appears in the center. If
the specified size is smaller than the current String size, the entire String is returned without added spaces.

Signature

```
   public String center(Integer size)

```

Parameters

```
   size
```

Type: Integer

Return Value

Type: String

Example

```
   String s = 'hello';

   String s2 = s.center(9);

   System.assertEquals(

     ' hello ',

     s2);

##### center(size, paddingString)

```

Returns a version of the current String of the specified size padded with the specified String on the left and right, so that it appears in
the center. If the specified size is smaller than the current String size, the entire String is returned without padding.

Signature

```
   public String center(Integer size, String paddingString)

```

Parameters

```
   size
```

Type: Integer

```
   paddingString
```

Type: String

Return Value

Type: String


Apex Reference Guide String Class

Example

```
   String s = 'hello';

   String s2 = s.center(9, '-');

   System.assertEquals('--hello--', s2);

##### charAt(index)

```

Returns the value of the character at the specified index.

Signature

```
   public Integer charAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

The index of the character to get the value of.

Return Value

Type: Integer

The integer value of the character.

Usage

##### The charAt method returns the value of the character pointed to by the specified index. If the index points to the beginning of a

surrogate pair (the high-surrogate code point), this method returns only the high-surrogate code point. To return the supplementary
##### code point corresponding to a surrogate pair, call codePointAt instead.

Example

This example gets the value of the first character at index 0.

```
   String str = 'Ω is Omega.';

   System.assertEquals(937, str.charAt(0));

##### This example shows the difference between charAt and codePointAt . The example calls these methods on escaped supplementary
```

Unicode characters. `charAt(0)` returns the high surrogate value, which corresponds to `\uD835` . `codePointAt(0)` returns
the value for the entire surrogate pair.

```
   String str = '\uD835\uDD0A';

   System.assertEquals(55349, str.charAt(0),

      'charAt(0) didn\'t return the high surrogate.');

   System.assertEquals(120074, str.codePointAt(0),

      'codePointAt(0) didn\'t return the entire two-character supplementary value.');

##### codePointAt(index)

```

Returns the Unicode code point value at the specified index.


Apex Reference Guide String Class

Signature

```
   public Integer codePointAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

The index of the characters (Unicode code units) in the string. The index range is from zero to the string length minus one.

Return Value

Type: Integer

The Unicode code point value at the specified index.

Usage

If the _`index`_ points to the beginning of a surrogate pair (the high-surrogate code point), and the character value at the following index
points to the low-surrogate code point, this method returns the supplementary code point corresponding to this surrogate pair. Otherwise,
this method returns the character value at the given index.

[For more information on Unicode and surrogate pairs, see The Unicode Consortium.](http://www.unicode.org)

Example

This example gets the code point value of the first character at index 0, which is the escaped Omega character. Also, the example gets
the code point at index 20, which corresponds to the escaped supplementary Unicode characters (a pair of characters). Finally, it verifies
that the escaped and unescaped forms of Omega have the same code point values.

The supplementary characters in this example ( `\\uD835\\uDD0A` ) correspond to mathematical fraktur capital G:

```
   String str = '\u03A9 is Ω (Omega), and \uD835\uDD0A ' +

      ' is Fraktur Capital G.';

   System.assertEquals(937, str.codePointAt(0));

   System.assertEquals(120074, str.codePointAt(20));

   // Escaped or unescaped forms of the same character have the same code point

   System.assertEquals(str.codePointAt(0), str.codePointAt(5));

##### codePointBefore(index)

```

Returns the Unicode code point value that occurs before the specified index.

Signature

```
   public Integer codePointBefore(Integer index)

```

Parameters

```
   index
```

Type: Integer

The index before the Unicode code point that is to be returned. The index range is from one to the string length.


Apex Reference Guide String Class

Return Value

Type: Integer

The character or Unicode code point value that occurs before the specified index.

Usage

If the character value at _**`index`**_ `-1` is the low-surrogate code point, and _**`index`**_ `-2` is not negative and the character at this index
location is the high-surrogate code point, this method returns the supplementary code point corresponding to this surrogate pair. If the
character value at _**`index`**_ `-1` is an unpaired low-surrogate or high-surrogate code point, the surrogate value is returned.

[For more information on Unicode and surrogate pairs, see The Unicode Consortium.](http://www.unicode.org)

Example

This example gets the code point value of the first character (before index 1), which is the escaped Omega character. Also, the example
gets the code point at index 20, which corresponds to the escaped supplementary characters (the two characters before index 22).

```
   String str = '\u03A9 is Ω (Omega), and \uD835\uDD0A ' +

      ' is Fraktur Capital G.';

   System.assertEquals(937, str.codePointBefore(1));

   System.assertEquals(120074, str.codePointBefore(22));

##### codePointCount(beginIndex, endIndex)

```

Returns the number of Unicode code points within the specified text range.

Signature

```
   public Integer codePointCount(Integer beginIndex, Integer endIndex)

```

Parameters

```
   beginIndex
```

Type: Integer

The index of the first character in the range.

```
   endIndex
```

Type: Integer

The index after the last character in the range.

Return Value

Type: Integer

The number of Unicode code points within the specified range.

Usage

The specified range begins at _`beginIndex`_ and ends at _**`endIndex`**_ `—1` . Unpaired surrogates within the text range count as one
code point each.


Apex Reference Guide String Class

Example

This example writes the count of code points in a substring that contains an escaped Unicode character and another substring that
contains Unicode supplementary characters, which count as one code point.

```
   String str = '\u03A9 and \uD835\uDD0A characters.';

   System.debug('Count of code points for ' + str.substring(0,1)

           + ': ' + str.codePointCount(0,1));

   System.debug('Count of code points for ' + str.substring(6,8)

           + ': ' + str.codePointCount(6,8));

   // Output:

   // Count of code points for Ω: 1

   // Count of code points for ��: 1

##### compareTo(secondString)

```

Compares two strings lexicographically, based on the Unicode value of each character in the Strings.

Signature

```
   public Integer compareTo(String secondString)

```

Parameters

```
   secondString
```

Type: String

Return Value

Type: Integer

Usage

The result is:

**•** A negative Integer if the String that called the method lexicographically precedes _`secondString`_

**•** A positive Integer if the String that called the method lexicographically follows _`compsecondStringString`_

**•** Zero if the Strings are equal

If there is no index position at which the Strings differ, then the shorter String lexicographically precedes the longer String.

Note that this method returns 0 whenever the `equals` method returns true.

Example

```
   String myString1 = 'abcde';

   String myString2 = 'abcd';

   Integer result =

     myString1.compareTo(myString2);

   System.assertEquals(result, 1);

```


Apex Reference Guide String Class

##### contains(substring)

Returns `true` if and only if the String that called the method contains the specified sequence of characters in _`substring`_ .

Signature

```
   public Boolean contains(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Boolean

Example

```
   String myString1 = 'abcde';

   String myString2 = 'abcd';

   Boolean result =

     myString1.contains(myString2);

   System.assertEquals(result, true);

##### containsAny(inputString)

```

Returns `true` if the current String contains any of the characters in the specified String; otherwise, returns `false` .

Signature

```
   public Boolean containsAny(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean

Example

```
   String s = 'hello';

   Boolean b1 = s.containsAny('hx');

   Boolean b2 = s.containsAny('x');

   System.assertEquals(true, b1);

   System.assertEquals(false, b2);

```


Apex Reference Guide String Class

##### containsIgnoreCase(substring)

Returns `true` if the current String contains the specified sequence of characters without regard to case; otherwise, returns `false` .

Signature

```
   public Boolean containsIgnoreCase(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Boolean

Example

```
   String s = 'hello';

   Boolean b = s.containsIgnoreCase('HE');

   System.assertEquals(

     true,

     b);

##### containsNone(inputString)

```

Returns `true` if the current String doesn’t contain any of the characters in the specified String; otherwise, returns `false` .

Signature

```
   public Boolean containsNone(String inputString)

```

Parameters

```
   inputString
```

Type: String

If _`inputString`_ is an empty string or the current String is empty, this method returns `true` . If _`inputString`_ is null, this
method returns a run-time exception.

Return Value

Type: Boolean

Example

```
   String s1 = 'abcde';

   System.assert(s1.containsNone('fg'));

```


Apex Reference Guide String Class

##### containsOnly(inputString)

Returns `true` if the current String contains characters only from the specified sequence of characters and not any other characters;
otherwise, returns `false` .

Signature

```
   public Boolean containsOnly(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean

Example

```
   String s1 = 'abba';

   String s2 = 'abba xyz';

   Boolean b1 =

     s1.containsOnly('abcd');

   System.assertEquals(

     true,

     b1);

   Boolean b2 =

     s2.containsOnly('abcd');

   System.assertEquals(

     false,

     b2);

##### containsWhitespace()

```

Returns `true` if the current String contains any white space characters; otherwise, returns `false` .

Signature

```
   public Boolean containsWhitespace()

```

Return Value

Type: Boolean

Example

```
   String s = 'Hello Jane';

   System.assert(s.containsWhitespace()); //true

   s = 'HelloJane ';

   System.assert(s.containsWhitespace()); //true

   s = ' HelloJane';

```


Apex Reference Guide String Class

```
   System.assert(s.containsWhitespace()); //true

   s = 'HelloJane';

   System.assert(!s.containsWhitespace()); //false

##### countMatches(substring)

```

Returns the number of times the specified substring occurs in the current String.

Signature

```
   public Integer countMatches(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String s = 'Hello Jane';

   System.assertEquals(1, s.countMatches('Hello'));

   s = 'Hello Hello';

   System.assertEquals(2, s.countMatches('Hello'));

   s = 'Hello hello';

   System.assertEquals(1, s.countMatches('Hello'));

##### deleteWhitespace()

```

Returns a version of the current String with all white space characters removed.

Signature

```
   public String deleteWhitespace()

```

Return Value

Type: String

Example

```
   String s1 = ' Hello Jane ';

   String s2 = 'HelloJane';

   System.assertEquals(s2, s1.deleteWhitespace());

```


Apex Reference Guide String Class

##### difference(secondString)

Returns the difference between the current String and the specified String.

Signature

```
   public String difference(String secondString)

```

Parameters

```
   secondString
```

Type: String

If _`secondString`_ is an empty string, this method returns an empty string.If _`secondString`_ is null, this method throws a
run-time exception.

Return Value

Type: String

Example

```
   String s = 'Hello Jane';

   String d1 =

     s.difference('Hello Max');

   System.assertEquals(

     'Max',

     d1);

   String d2 =

     s.difference('Goodbye');

   System.assertEquals(

     'Goodbye',

     d2);

##### endsWith(suffix)

```

Returns `true` if the String that called the method ends with the specified _`suffix`_ .

Signature

```
   public Boolean endsWith(String suffix)

```

Parameters

```
   suffix
```

Type: String

Return Value

Type: Boolean


Apex Reference Guide String Class

Example

```
   String s = 'Hello Jason';

   System.assert(s.endsWith('Jason'));

##### endsWithIgnoreCase(suffix)

```

Returns `true` if the current String ends with the specified suffix; otherwise, returns `false` .

Signature

```
   public Boolean endsWithIgnoreCase(String suffix)

```

Parameters

```
   suffix
```

Type: String

Return Value

Type: Boolean

Example

```
   String s = 'Hello Jason';

   System.assert(s.endsWithIgnoreCase('jason'));

##### equals(secondString)

```

Deprecated. This method is replaced by `equals(stringOrId)` . Returns `true` if the passed-in string is not null and represents
the same binary sequence of characters as the current string. Use this method to perform case-sensitive comparisons.

Signature

```
   public Boolean equals(String secondString)

```

Parameters

```
   secondString
```

Type: String

Return Value

Type: Boolean

Usage

This method returns `true` when the `compareTo` method returns 0.

Use this method to perform case-sensitive comparisons. In contrast, the `==` operator performs case-insensitive string comparisons to
match Apex semantics.


Apex Reference Guide String Class

Example

```
   String myString1 = 'abcde';

   String myString2 = 'abcd';

   Boolean result = myString1.equals(myString2);

   System.assertEquals(result, false);

##### equals(stringOrId)

```

Returns `true` if the passed-in object is not null and represents the same binary sequence of characters as the current string. Use this
method to compare a string to an object that represents a string or an ID.

Signature

```
   public Boolean equals(Object stringOrId)

```

Parameters

```
   stringOrId
```

Type: Object

Return Value

Type: Boolean

Usage

If you compare ID values, the lengths of IDs don’t need to be equal. For example, if you compare a 15-character ID string to an object
that represents the equivalent 18-character ID value, this method returns `true` . For more information about 15-character and 18-character
[IDs, see the ID Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

Use this method to perform case-sensitive comparisons. In contrast, the `==` operator performs case-insensitive string comparisons to
match Apex semantics.

Example

These examples show comparisons between different types of variables with both equal and unequal values. The examples also show
how Apex automatically converts certain values before comparing them.

```
   // Compare a string to an object containing a string

   Object obj1 = 'abc';

   String str = 'abc';

   Boolean result1 = str.equals(obj1);

   System.assertEquals(true, result1);

   // Compare a string to an object containing a number

   Integer obj2 = 100;

   Boolean result2 = str.equals(obj2);

   System.assertEquals(false, result2);

   // Compare a string to an ID of the same length.

   // 15-character ID

   Id idValue15 = '001D000000Ju1zH';

```


Apex Reference Guide String Class

```
   // 15-character ID string value

   String stringValue15 = '001D000000Ju1zH';

   Boolean result3 = stringValue15.equals(IdValue15);

   System.assertEquals(true, result3);

   // Compare two equal ID values of different lengths:

   // 15-character ID and 18-character ID

   Id idValue18 = '001D000000Ju1zHIAR';

   Boolean result4 = stringValue15.equals(IdValue18);

   System.assertEquals(true, result4);

##### equalsIgnoreCase(secondString)

```

Returns `true` if the _`secondString`_ isn’t null and represents the same sequence of characters as the String that called the method,
ignoring case.

Signature

```
   public Boolean equalsIgnoreCase(String secondString)

```

Parameters

```
   secondString
```

Type: String

Return Value

Type: Boolean

Usage

The `String.equalsIgnoreCase()` method ignores the locale of the context user. If you want the string comparison to be
performed according to the locale, use the `==` operator instead. The `String.equalsIgnoreCase()` method typically executes
faster than the operator because the method ignores the locale.

Example

```
   String myString1 = 'abcd';

   String myString2 = 'ABCD';

   Boolean result =

   myString1.equalsIgnoreCase(myString2);

   System.assertEquals(result, true);

##### escapeCsv()

```

Returns a String for a CSV column enclosed in double quotes, if required.

Signature

```
   public String escapeCsv()

```


Apex Reference Guide String Class

Return Value

Type: String

Usage

If the String contains a comma, newline or double quote, the returned String is enclosed in double quotes. Also, any double quote
characters in the String are escaped with another double quote.

If the String doesn’t contain a comma, newline or double quote, it is returned unchanged.

Example

```
   String s1 = 'Max1, "Max2"';

   String s2 = s1.escapeCsv();

   System.assertEquals('"Max1, ""Max2"""', s2);

##### escapeEcmaScript()

```

Escapes the characters in the String using EcmaScript String rules.

Signature

```
   public String escapeEcmaScript()

```

Return Value

Type: String

Usage

The only difference between Apex strings and EcmaScript strings is that in EcmaScript, a single quote and forward-slash (/) are escaped.

Example

```
   String s1 = '"grade": 3.9/4.0';

   String s2 = s1.escapeEcmaScript();

   System.debug(s2);

   // Output is:

   // \"grade\": 3.9\/4.0

   System.assertEquals(

     '\\"grade\\": 3.9\\/4.0',

      s2);

##### escapeHtml3()

```

Escapes the characters in a String using HTML 3.0 entities.

Signature

```
   public String escapeHtml3()

```


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   String s1 =

     '"<Black&White>"';

   String s2 =

     s1.escapeHtml3();

   System.debug(s2);

   // Output:

   // &quot;&lt;Black&amp;

   // White&gt;&quot;

##### escapeHtml4()

```

Escapes the characters in a String using HTML 4.0 entities.

Signature

```
   public String escapeHtml4()

```

Return Value

Type: String

Example

```
   String s1 =

     '"<Black&White>"';

   String s2 =

     s1.escapeHtml4();

   System.debug(s2);

   // Output:

   // &quot;&lt;Black&amp;

   // White&gt;&quot;

##### escapeJava()

```

Returns a String whose characters are escaped using Java String rules. Characters escaped include quotes and control characters, such
as tab, backslash, and carriage return characters.

Signature

```
   public String escapeJava()

```

Return Value

Type: String

The escaped string.


Apex Reference Guide String Class

Example

```
   // Input string contains quotation marks

   String s = 'Company: "Salesforce.com"';

   String escapedStr = s.escapeJava();

   // Output string has the quotes escaped

   System.assertEquals('Company: \\"Salesforce.com\\"', escapedStr);

##### **`escapeSingleQuotes(stringToEscape)`**

```

Returns a String with the escape character ( `\` ) added before any single quotation mark ( `'` ) or backslash ( `\` ) in the String _`s`_ .

Signature

```
   public static String escapeSingleQuotes(String stringToEscape)

```

Parameters

```
   stringToEscape
```

Type: String

Return Value

Type: String

Usage

[This method is useful when creating a dynamic SOQL statement to help prevent SOQL injection. See Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

Example

```
   String s = '\'Hello Jason\'';

   system.debug(s); // Outputs 'Hello Jason'

   String escapedStr = String.escapeSingleQuotes(s);

   system.debug(escapedStr); // Outputs \'Hello Jason\'

   // In this assertEquals method, the first string is unescaped,

   // so each \ that precedes the ' and \ characters is removed.

   // Therefore, the string is equal to the value of escapedStr, or \'Hello Jason\'.

   system.assertEquals('\\\'Hello Jason\\\'', escapedStr);

##### escapeUnicode()

```

Returns a String whose Unicode characters are escaped to a Unicode escape sequence.

Signature

```
   public String escapeUnicode()

```

Return Value

Type: String


Apex Reference Guide String Class

The escaped string.

Example

```
   String s = 'De onde você é?';

   String escapedStr = s.escapeUnicode();

   System.assertEquals('De onde voc\\u00EA \\u00E9?', escapedStr);

##### escapeXml()

```

Escapes the characters in a String using XML entities.

Signature

```
   public String escapeXml()

```

Return Value

Type: String

Usage

Supports only the five basic XML entities (gt, lt, quot, amp, apos). Does not support DTDs or external entities. Unicode characters greater
than 0x7f are not escaped.

Example

```
   String s1 =

     '"<Black&White>"';

   String s2 =

     s1.escapeXml();

   System.debug(s2);

   // Output:

   // &quot;&lt;Black&amp;

   // White&gt;&quot;

##### format(stringToFormat, formattingArguments)

```

Treat the first argument as a pattern and return a string using the second argument for substitution and formatting. The substitution
and formatting are the same as `apex:outputText` and the Java `MessageFormat` class. Non-string types in the second
argument’s List are implicitly converted to strings, respecting the toString() method overrides that exist on the type.

Signature

```
   public static String format(String stringToFormat, List<Object> formattingArguments)

```

Parameters

```
   stringToFormat
```

Type: String


Apex Reference Guide String Class

```
   formattingArguments
```

Type: List<Object>

Return Value

Type: String

Versioned Behavior Changes

From version 51.0 and later, the `format()` method supports single quotes in the `stringToFormat` parameter and returns a
formatted string using the `formattingArguments` parameter. In version 50.0 and earlier, single quotes weren’t supported.

Example

```
   String template = '{0} was last updated {1}';

   List<Object> parameters = new List<Object> {'Universal Containers',

   DateTime.newInstance(2018, 11, 15) };

   String formatted = String.format(template, parameters);

   System.debug ('Newly formatted string is:' + formatted);

##### fromCharArray(charArray)

```

Returns a String from the values of the list of integers.

Signature

```
   public static String fromCharArray(List<Integer> charArray)

```

Parameters

```
   charArray
```

Type: List<Integer>

Return Value

Type: String

Example

```
   List<Integer> charArr= new Integer[]{74};

   String convertedChar = String.fromCharArray(charArr);

   System.assertEquals('J', convertedChar);

##### getChars()

```

Returns an array of character values that represent the characters in this string.

Signature

```
   public List<Integer> getChars()

```


Apex Reference Guide String Class

Return Value

Type: List<Integer>

A list of integers, each corresponding to a character value in the string.

Example

This sample converts a string to a character array and then gets the first array element, which corresponds to the value of 'J'.

```
   String str = 'Jane goes fishing.';

   Integer[] chars = str.getChars();

   // Get the value of 'J'

   System.assertEquals(74, chars[0]);

```

Usage

If a "/" (slash) character is present in the string, `String.getChars()` unescapes it in the returned character array. This example
uses the `String.escapeJava()` method to generate the desired value of "\\" in the returned string.

```
   String doubleSlash = '\\' + '\\'; //doubleSlash is set to "\\"

   System.debug(String.fromCharArray(doubleSlash.getChars())); //Returns "\"

   System.debug(String.fromCharArray(doubleSlash.escapeJava().getChars())); //Returns "\\”

##### getCommonPrefix(strings)

```

Returns the initial sequence of characters as a String that is common to all the specified Strings.

Signature

```
   public static String getCommonPrefix(List<String> strings)

```

Parameters

```
   strings
```

Type: List<String>

Return Value

Type: String

Example

```
   List<String> ls = new List<String>{'SFDCApex', 'SFDCVisualforce'};

   String prefix = String.getCommonPrefix(ls);

   System.assertEquals('SFDC', prefix);

##### getLevenshteinDistance(stringToCompare)

```

Returns the Levenshtein distance between the current String and the specified String.


Apex Reference Guide String Class

Signature

```
   public Integer getLevenshteinDistance(String stringToCompare)

```

Parameters

```
   stringToCompare
```

Type: String

Return Value

Type: Integer

Usage

The Levenshtein distance is the number of changes needed to change one String into another. Each change is a single character
modification (deletion, insertion or substitution).

Example

```
   String s = 'Hello Joe';

   Integer i = s.getLevenshteinDistance('Hello Max');

   System.assertEquals(3, i);

##### getLevenshteinDistance(stringToCompare, threshold)

```

Returns the Levenshtein distance between the current String and the specified String if it is less than or equal than the given threshold;
otherwise, returns -1.

Signature

```
   public Integer getLevenshteinDistance(String stringToCompare, Integer threshold)

```

Parameters

```
   stringToCompare
```

Type: String

```
   threshold
```

Type: Integer

Return Value

Type: Integer

Usage

The Levenshtein distance is the number of changes needed to change one String into another. Each change is a single character
modification (deletion, insertion or substitution).

Example:


Apex Reference Guide String Class

In this example, the Levenshtein distance is 3, but the threshold argument is 2, which is less than the distance, so this method returns
-1.

Example

```
   String s = 'Hello Jane';

   Integer i = s.getLevenshteinDistance('Hello Max', 2);

   System.assertEquals(-1, i);

##### hashCode()

```

Returns a hash code value for this string.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

Usage

This value is based on the hash code computed by the Java `[String.hashCode](http://docs.oracle.com/javase/6/docs/api/java/lang/String.html#hashCode%28%29)` counterpart method.

You can use this method to simplify the computation of a hash code for a custom type that contains String member variables. You can
compute your type’s hash code value based on the hash code of each String variable. For example:

[For more details about the use of hash code methods with custom types, see Using Custom Types in Map Keys and Sets.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)

Example

```
   public class MyCustomClass {

     String x,y;

     // Provide a custom hash code

     public Integer hashCode() {

      return

      (31*x.hashCode())^(y.hashCode());

     }

   }

##### indexOf(substring)

```

Returns the index of the first occurrence of the specified substring. If the substring does not occur, this method returns -1.

Signature

```
   public Integer indexOf(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String myString1 = 'abcde';

   String myString2 = 'cd';

   Integer result = myString1.indexOf(mystring2);

   System.assertEquals(2, result);

##### indexOf(substring, index)

```

Returns the zero-based index of the first occurrence of the specified substring from the point of the given index. If the substring does
not occur, this method returns -1.

Signature

```
   public Integer indexOf(String substring, Integer index)

```

Parameters

```
   substring
```

Type: String

##### _`index`_

Type: Integer

Return Value

Type: Integer

Example

```
   String myString1 = 'abcdabcd';

   String myString2 = 'ab';

   Integer result = myString1.indexOf(mystring2, 1);

   System.assertEquals(4, result);

##### indexOfAny(substring)

```

Returns the zero-based index of the first occurrence of any character specified in the substring. If none of the characters occur, returns
-1.

Signature

```
   public Integer indexOfAny(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String s1 = 'abcd';

   String s2 = 'xc';

   Integer result = s1.indexOfAny(s2);

   System.assertEquals(2, result);

##### indexOfAnyBut(substring)

```

Returns the zero-based index of the first occurrence of a character that is not in the specified substring. Otherwise, returns -1.

Signature

```
   public Integer indexOfAnyBut(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String s1 = 'abcd';

   String s2 = 'xc';

   Integer result = s1.indexOfAnyBut(s2);

   System.assertEquals(0, result);

##### indexOfChar(character)

```

Returns the index of the first occurrence of the character that corresponds to the specified character value.

Signature

```
   public Integer indexOfChar(Integer character)

```


Apex Reference Guide String Class

Parameters

```
   character
```

Type: Integer

The integer value of the character in the string.

Return Value

Type: Integer

The index of the first occurrence of the specified character, -1 if the character is not found.

Usage

The index that this method returns is in Unicode code units.

Example

```
   String str = '\\u03A9 is Ω (Omega)';

   // Returns 0, which is the first character.

   System.debug('indexOfChar(937)=' + str.indexOfChar(937));

   // Output:

   // indexOfChar(937)=0

##### indexOfChar(character, startIndex)

```

Returns the index of the first occurrence of the character that corresponds to the specified character value, starting from the specified
index.

Signature

```
   public Integer indexOfChar(Integer character, Integer startIndex)

```

Parameters

```
   character
```

Type: Integer

The integer value of the character to look for.

```
   startIndex
```

Type: Integer

The index to start the search from.

Return Value

Type: Integer

The index, starting from the specified start index, of the first occurrence of the specified character, -1 if the character is not found.


Apex Reference Guide String Class

Usage

The index that this method returns is in Unicode code units.

Example

This example shows different ways of searching for the index of the Omega character. The first call to `indexOfChar` doesn’t specify
a start index and therefore the returned index is 0, which is the first occurrence of Omega in the entire string. The subsequent calls specify
a start index to find the occurrence of Omega in substrings that start at the specified index.

```
   String str = 'Ω and \\u03A9 and Ω';

   System.debug('indexOfChar(937)=' + str.indexOfChar(937));

   System.debug('indexOfChar(937,1)=' + str.indexOfChar(937,1));

   System.debug('indexOfChar(937,10)=' + str.indexOfChar(937,10));

   // Output:

   // indexOfChar(937)=0

   // indexOfChar(937,1)=6, (corresponds to the escaped form \\u03A9)

   // indexOfChar(937,10)=12

##### indexOfDifference(stringToCompare)

```

Returns the zero-based index of the character where the current String begins to differ from the specified String.

Signature

```
   public Integer indexOfDifference(String stringToCompare)

```

Parameters

```
   stringToCompare
```

Type: String

Return Value

Type: Integer

Example

```
   String s1 = 'abcd';

   String s2 = 'abxc';

   Integer result = s1.indexOfDifference(s2);

   System.assertEquals(2, result);

##### indexOfIgnoreCase(substring)

```

Returns the zero-based index of the first occurrence of the specified substring without regard to case. If the substring does not occur,
this method returns -1.

Signature

```
   public Integer indexOfIgnoreCase(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String s1 = 'abcd';

   String s2 = 'BC';

   Integer result = s1.indexOfIgnoreCase(s2, 0);

   System.assertEquals(1, result);

##### indexOfIgnoreCase(substring, startPosition) Returns the zero-based index of the first occurrence of the specified substring from the point of index i, without regard to case. If the
```

substring does not occur, this method returns -1.

Signature

```
   public Integer indexOfIgnoreCase(String substring, Integer startPosition)

```

Parameters

```
   substring
```

Type: String

```
   startPosition
```

Type: Integer

Return Value

Type: Integer

##### isAllLowerCase()

Returns `true` if all characters in the current String are lowercase; otherwise, returns `false` .

Signature

```
   public Boolean isAllLowerCase()

```

Return Value

Type: Boolean


Apex Reference Guide String Class

Example

```
   String allLower = 'abcde';

   System.assert(allLower.isAllLowerCase());

##### isAllUpperCase()

```

Returns `true` if all characters in the current String are uppercase; otherwise, returns `false` .

Signature

```
   public Boolean isAllUpperCase()

```

Return Value

Type: Boolean

Example

```
   String allUpper = 'ABCDE';

   System.assert(allUpper.isAllUpperCase());

##### isAlpha()

```

Returns `true` if all characters in the current String are Unicode letters only; otherwise, returns `false` .

Signature

```
   public Boolean isAlpha()

```

Return Value

Type: Boolean

Example

```
   // Letters only

   String s1 = 'abc';

   // Returns true

   Boolean b1 =

     s1.isAlpha();

   System.assertEquals(

     true, b1);

   // Letters and numbers

   String s2 = 'abc 21';

   // Returns false

   Boolean b2 =

     s2.isAlpha();

   System.assertEquals(

     false, b2);

```


Apex Reference Guide String Class

##### isAlphaSpace()

Returns `true` if all characters in the current String are Unicode letters or spaces only; otherwise, returns `false` .

Signature

```
   public Boolean isAlphaSpace()

```

Return Value

Type: Boolean

Example

```
   String alphaSpace = 'aA Bb';

   System.assert(alphaSpace.isAlphaSpace());

   String notAlphaSpace = 'ab 12';

   System.assert(!notAlphaSpace.isAlphaSpace());

   notAlphaSpace = 'aA$Bb';

   System.assert(!notAlphaSpace.isAlphaSpace());

##### isAlphanumeric()

```

Returns `true` if all characters in the current String are Unicode letters or digits only; otherwise, returns `false` .

Signature

```
   public Boolean isAlphanumeric()

```

Return Value

Type: Boolean

Usage

##### Unicode Roman numerals are classified as a type of number form, not a type of digit. Therefore, the isAlphanumeric() method

returns `false` [if used on a String that contains a Roman numeral. For Unicode classifications, see the Unicode Character Code Charts.](https://www.unicode.org/charts/)

Example

```
   // Letters only

   String s1 = 'abc';

   // Returns true

   Boolean b1 =

     s1.isAlphanumeric();

   System.assertEquals(

     true, b1);

   // Letters and digits

   String s2 = 'abc021';

   // Returns true

   Boolean b2 =

```


Apex Reference Guide String Class

```
     s2.isAlphanumeric();

   System.assertEquals(

     true, b2);

##### isAlphanumericSpace()

```

Returns `true` if all characters in the current String are Unicode letters, digits, or spaces only; otherwise, returns `false` .

Signature

```
   public Boolean isAlphanumericSpace()

```

Return Value

Type: Boolean

Usage

##### Unicode Roman numerals are classified as a type of number form, not a type of digit. Therefore, the isAlphanumericSpace()

method returns `false` [if used on a String that contains a Roman numeral. For Unicode classifications, see the Unicode Character Code](https://www.unicode.org/charts/)
[Charts.](https://www.unicode.org/charts/)

Example

```
   String alphanumSpace = 'AE 86';

   System.assert(alphanumSpace.isAlphanumericSpace());

   String notAlphanumSpace = 'aA$12';

   System.assert(!notAlphanumSpace.isAlphanumericSpace());

##### isAsciiPrintable()

```

Returns `true` if the current String contains only ASCII printable characters; otherwise, returns `false` .

Signature

```
   public Boolean isAsciiPrintable()

```

Return Value

Type: Boolean

Example

```
   String ascii = 'abcd1234!@#$%^&*()`~-_+={[}]|:<,>.?';

   System.assert(ascii.isAsciiPrintable());
```

`String notAscii = '` √ `';`

```
   System.assert(!notAscii.isAsciiPrintable());

```


Apex Reference Guide String Class

##### isBlank(inputString)

Returns `true` if the specified String is white space, empty (''), or null; otherwise, returns `false` .

Signature

```
   public static Boolean isBlank(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean

Example

```
   String blank = '';

   String nullString = null;

   String whitespace = ' ';

   System.assert(String.isBlank(blank));

   System.assert(String.isBlank(nullString));

   System.assert(String.isBlank(whitespace));

   String alpha = 'Hello';

   System.assert(!String.isBlank(alpha));

##### isEmpty(inputString)

```

Returns `true` if the specified String is empty ('') or null; otherwise, returns `false` .

Signature

```
   public static Boolean isEmpty(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean

Example

```
   String empty = '';

   String nullString = null;

   System.assert(String.isEmpty(empty));

   System.assert(String.isEmpty(nullString));

```


Apex Reference Guide String Class

```
   String whitespace = ' ';

   String alpha = 'Hello';

   System.assert(!String.isEmpty(whitespace));

   System.assert(!String.isEmpty(alpha));

##### isNotBlank(inputString)

```

Returns `true` if the specified String is not whitespace, not empty (''), and not null; otherwise, returns `false` .

Signature

```
   public static Boolean isNotBlank(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean

Example

```
   String alpha = 'Hello world!';

   System.assert(String.isNotBlank(alpha));

   String blank = '';

   String nullString = null;

   String whitespace = ' ';

   System.assert(!String.isNotBlank(blank));

   System.assert(!String.isNotBlank(nullString));

   System.assert(!String.isNotBlank(whitespace));

##### isNotEmpty(inputString)

```

Returns `true` if the specified String is not empty ('') and not null; otherwise, returns `false` .

Signature

```
   public static Boolean isNotEmpty(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Boolean


Apex Reference Guide String Class

Example

```
   String whitespace = ' ';

   String alpha = 'Hello world!';

   System.assert(String.isNotEmpty(whitespace));

   System.assert(String.isNotEmpty(alpha));

   String empty = '';

   String nullString = null;

   System.assert(!String.isNotEmpty(empty));

   System.assert(!String.isNotEmpty(nullString));

##### isNumeric()

```

Returns `true` if the current String contains only Unicode digits; otherwise, returns `false` .

Signature

```
   public Boolean isNumeric()

```

Return Value

Type: Boolean

Usage

A decimal point (1.2) is not a Unicode digit.

Example

```
   String numeric = '1234567890';

   System.assert(numeric.isNumeric());

   String alphanumeric = 'R32';

   String decimalPoint = '1.2';

   System.assert(!alphanumeric.isNumeric());

   System.assert(!decimalpoint.isNumeric());

##### isNumericSpace()

```

Returns `true` if the current String contains only Unicode digits or spaces; otherwise, returns `false` .

Signature

```
   public Boolean isNumericSpace()

```

Return Value

Type: Boolean

Usage

A decimal point (1.2) is not a Unicode digit.


Apex Reference Guide String Class

Example

```
   String numericSpace = '1 2 3';

   System.assert(numericSpace.isNumericspace());

   String notNumericspace = 'FD3S FC3S';

   System.assert(!notNumericspace.isNumericspace());

##### isWhitespace()

```

Returns `true` if the current String contains only white space characters or is empty; otherwise, returns `false` .

Signature

```
   public Boolean isWhitespace()

```

Return Value

Type: Boolean

Example

```
   String whitespace = ' ';

   String blank = '';

   System.assert(whitespace.isWhitespace());

   System.assert(blank.isWhitespace());

   String alphanum = 'SIL80';

   System.assert(!alphanum.isWhitespace());

##### join(iterableObj, separator)

```

Joins the elements of the specified iterable object, such as a List, into a single String separated by the specified separator.

Signature

```
   public static String join(Object iterableObj, String separator)

```

Parameters

```
   iterableObj
```

Type: Object

```
   separator
```

Type: String

Return Value

Type: String


Apex Reference Guide String Class

Usage

```
   List<Integer> li = new

     List<Integer>

     {10, 20, 30};

   String s = String.join(

     li, '/');

   System.assertEquals(

     '10/20/30', s);

##### lastIndexOf(substring)

```

Returns the index of the last occurrence of the specified substring. If the substring does not occur, this method returns -1.

Signature

```
   public Integer lastIndexOf(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer

Example

```
   String s1 = 'abcdefgc';

   Integer i1 = s1.lastIndexOf('c');

   System.assertEquals(7, i1);

##### lastIndexOf(substring, endPosition)

```

Returns the index of the last occurrence of the specified substring, starting from the character at index 0 and ending at the specified
index.

Signature

```
   public Integer lastIndexOf(String substring, Integer endPosition)

```

Parameters

```
   substring
```

Type: String

```
   endPosition
```

Type: Integer


Apex Reference Guide String Class

Return Value

Type: Integer

Usage

If the substring doesn’t occur or _`endPosition`_ is negative, this method returns -1. If _`endPosition`_ is larger than the last index
in the current String, the entire String is searched.

Example

```
   String s1 = 'abcdaacd';

   Integer i1 = s1.lastIndexOf('c', 7);

   System.assertEquals(6, i1);

   Integer i2 = s1.lastIndexOf('c', 3);

   System.assertEquals(2, i2);

##### lastIndexOfChar(character)

```

Returns the index of the last occurrence of the character that corresponds to the specified character value.

Signature

```
   public Integer lastIndexOfChar(Integer character)

```

Parameters

```
   character
```

Type: Integer

The integer value of the character in the string.

Return Value

Type: Integer

The index of the last occurrence of the specified character, -1 if the character is not found.

Usage

The index that this method returns is in Unicode code units.

Example

```
   String str = '\u03A9 is Ω (Omega)';

   // Get the last occurrence of Omega.

   System.assertEquals(5, str.lastIndexOfChar(937));

##### lastIndexOfChar(character, endIndex)

```

Returns the index of the last occurrence of the character that corresponds to the specified character value, starting from the specified
index.


Apex Reference Guide String Class

Signature

```
   public Integer lastIndexOfChar(Integer character, Integer endIndex)

```

Parameters

```
   character
```

Type: Integer

The integer value of the character to look for.

```
   endIndex
```

Type: Integer

The index to end the search at.

Return Value

Type: Integer

The index, starting from the specified start index, of the last occurrence of the specified character. -1 if the character is not found.

Usage

The index that this method returns is in Unicode code units.

Example

This example shows different ways of searching for the index of the last occurrence of the Omega character. The first call to
`lastIndexOfChar` doesn’t specify an end index and therefore the returned index is 12, which is the last occurrence of Omega in
the entire string. The subsequent calls specify an end index to find the last occurrence of Omega in substrings.

```
   String str = 'Ω and \u03A9 and Ω';

   System.assertEquals(12, str.lastIndexOfChar(937));

   System.assertEquals(6, str.lastIndexOfChar(937,11));

   System.assertEquals(0, str.lastIndexOfChar(937,5));

##### lastIndexOfIgnoreCase(substring)

```

Returns the index of the last occurrence of the specified substring regardless of case.

Signature

```
   public Integer lastIndexOfIgnoreCase(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: Integer


Apex Reference Guide String Class

Usage

If the substring doesn’t occur, this method returns -1.

Example

```
   String s1 = 'abcdaacd';

   Integer i1 = s1.lastIndexOfIgnoreCase('DAAC');

   System.assertEquals(3, i1);

##### lastIndexOfIgnoreCase(substring, endPosition)

```

Returns the index of the last occurrence of the specified substring regardless of case, starting from the character at index 0 and ending
at the specified index.

Signature

```
   public Integer lastIndexOfIgnoreCase(String substring, Integer endPosition)

```

Parameters

```
   substring
```

Type: String

```
   endPosition
```

Type: Integer

Return Value

Type: Integer

Usage

If the substring doesn’t occur or _`endPosition`_ is negative, this method returns -1. If _`endPosition`_ is larger than the last index
in the current String, the entire String is searched.

Example

```
   String s1 = 'abcdaacd';

   Integer i1 = s1.lastIndexOfIgnoreCase('C', 7);

   System.assertEquals(6, i1);

##### left(length)

```

Returns the leftmost characters of the current String of the specified length.

Signature

```
   public String left(Integer length)

```


Apex Reference Guide String Class

Parameters

```
   length
```

Type: Integer

Return Value

Type: String

Usage

If _`length`_ is greater than the String size, the entire String is returned.

Example

```
   String s1 = 'abcdaacd';

   String s2 = s1.left(3);

   System.assertEquals('abc', s2);

##### leftPad(length)

```

Returns the current String padded with spaces on the left and of the specified length.

Signature

```
   public String leftPad(Integer length)

```

Parameters

```
   length
```

Type: Integer

Usage

If _`length`_ is less than or equal to the current String size, the entire String is returned without space padding.

Return Value

Type: String

Example

```
   String s1 = 'abc';

   String s2 = s1.leftPad(5);

   System.assertEquals(' abc', s2);

##### leftPad(length, padStr)

```

Returns the current String padded with String `padStr` on the left and of the specified length.


Apex Reference Guide String Class

Signature

```
   public String leftPad(Integer length, String padStr)

```

Parameters

##### _`length`_

Type: Integer

```
   padStr
```

Type: String

String to pad with; if null or empty treated as single blank.

Usage

##### If length is less than or equal to the current String size, the entire String is returned without space padding.

Return Value

Type: String

Example

```
   String s1 = 'abc';

   String s2 = 'xy';

   String s3 = s1.leftPad(7,s2);

   System.assertEquals('xyxyabc', s3);

##### length()

```

Returns the number of 16-bit Unicode characters contained in the String.

Signature

```
   public Integer length()

```

Return Value

Type: Integer

Example

```
   String myString = 'abcd';

   Integer result = myString.length();

   System.assertEquals(result, 4);

##### mid(startIndex, length)

```

Returns a new String that begins with the character at the specified zero-based _`startIndex`_ with the number of characters specified
##### by length .


Apex Reference Guide String Class

Signature

```
   public String mid(Integer startIndex, Integer length)

```

Parameters

```
   startIndex
```

Type: Integer

If _`startIndex`_ is negative, it is considered to be zero.

```
   length
```

Type: Integer

If _`length`_ is negative or zero, an empty String is returned. If _`length`_ is greater than the remaining characters, the remainder of
the String is returned.

Return Value

Type: String

Usage

This method is similar to the `substring(startIndex)` and `substring(startIndex, endIndex)` methods, except
that the second argument is the number of characters to return.

Example

```
   String s = 'abcde';

   String s2 = s.mid(2, 3);

   System.assertEquals(

     'cde', s2);

##### normalizeSpace()

```

Returns the current String with leading, trailing, and repeating white space characters removed.

Signature

```
   public String normalizeSpace()

```

Return Value

Type: String

Usage

This method normalizes the following white space characters: space, tab (\t), new line (\n), carriage return (\r), and form feed (\f).

Example

```
   String s1 =

     'Salesforce \t force.com';

```


Apex Reference Guide String Class

```
   String s2 =

     s1.normalizeSpace();

   System.assertEquals(

     'Salesforce force.com', s2);

##### offsetByCodePoints(index, codePointOffset)

```

Returns the index of the Unicode code point that is offset by the specified number of code points, starting from the given index.

Signature

```
   public Integer offsetByCodePoints(Integer index, Integer codePointOffset)

```

Parameters

```
   index
```

Type: Integer

The start index in the string.

```
   codePointOffset
```

Type: Integer

The number of code points to be offset.

Return Value

Type: Integer

The index that corresponds to the start index that is added to the offset.

Usage

Unpaired surrogates within the text range that is specified by _`index`_ and _`codePointOffset`_ count as one code point each.

Example

##### This example calls offsetByCodePoints on a string with a start index of 0 (to start from the first character) and an offset of three

code points. The string contains one sequence of supplementary characters in escaped form (a pair of characters). After an offset of three
code points when counting from the beginning of the string, the returned code point index is four.

```
   String str = 'A \uD835\uDD0A BC';

   System.assertEquals(4, str.offsetByCodePoints(0,3));

##### remove(substring)

```

Removes all occurrences of the specified substring and returns the String result.

Signature

```
   public String remove(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce and force.com';

   String s2 =

     s1.remove('force');

   System.assertEquals(

     'Sales and .com', s2);

##### removeEnd(substring)

```

Removes the specified substring only if it occurs at the end of the String.

Signature

```
   public String removeEnd(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce and force.com';

   String s2 =

     s1.removeEnd('.com');

   System.assertEquals(

     'Salesforce and force', s2);

##### removeEndIgnoreCase(substring)

```

Removes the specified substring only if it occurs at the end of the String using a case-insensitive match.

Signature

```
   public String removeEndIgnoreCase(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce and force.com';

   String s2 = s1.removeEndIgnoreCase('.COM');

   System.assertEquals('Salesforce and force', s2);

##### removeStart(substring)

```

Removes the specified substring only if it occurs at the beginning of the String.

Signature

```
   public String removeStart(String substring)

```

Parameters

```
   substring
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce and force.com';

   String s2 =

     s1.removeStart('Sales');

   System.assertEquals(

     'force and force.com', s2);

##### removeStartIgnoreCase(substring)

```

Removes the specified substring only if it occurs at the beginning of the String using a case-insensitive match.

Signature

```
   public String removeStartIgnoreCase(String substring)

```


Apex Reference Guide String Class

Parameters

```
   substring
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce and force.com';

   String s2 =

     s1.removeStartIgnoreCase('SALES');

   System.assertEquals(

     'force and force.com', s2);

##### repeat(numberOfTimes)

```

Returns the current String repeated the specified number of times.

Signature

```
   public String repeat(Integer numberOfTimes)

```

Parameters

```
   numberOfTimes
```

Type: Integer

Return Value

Type: String

Example

```
   String s1 = 'SFDC';

   String s2 = s1.repeat(2);

   System.assertEquals('SFDCSFDC', s2);

##### repeat(separator, numberOfTimes)

```

Returns the current String repeated the specified number of times using the specified separator to separate the repeated Strings.

Signature

```
   public String repeat(String separator, Integer numberOfTimes)

```


Apex Reference Guide String Class

Parameters

```
   separator
```

Type: String

```
   numberOfTimes
```

Type: Integer

Return Value

Type: String

Example

```
   String s1 = 'SFDC';

   String s2 =

     s1.repeat('-', 2);

   System.assertEquals(

     'SFDC-SFDC', s2);

##### replace(target, replacement)

```

Replaces each substring of a string that matches the literal target sequence _`target`_ with the specified literal replacement sequence
_`replacement`_ .

Signature

```
   public String replace(String target, String replacement)

```

Parameters

```
   target
```

Type: String

```
   replacement
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'abcdbca';

   String target = 'bc';

   String replacement = 'xy';

   String s2 = s1.replace(target, replacement);

   System.assertEquals('axydxya', s2);

##### replaceAll(regExp, replacement)

```

Replaces each substring of a string that matches the regular expression _`regExp`_ with the replacement sequence _`replacement`_ .


Apex Reference Guide String Class

Signature

```
   public String replaceAll(String regExp, String replacement)

```

Parameters

```
   regExp
```

Type: String

```
   replacement
```

Type: String

Return Value

Type: String

Usage

See the Java `[Pattern](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html)` class for information on regular expressions.

Example

```
   String s1 = 'a b c 5 xyz';

   String regExp = '[a-zA-Z]';

   String replacement = '1';

   String s2 = s1.replaceAll(regExp, replacement);

   System.assertEquals('1 1 1 5 111', s2);

##### replaceFirst(regExp, replacement)

```

Replaces the first substring of a string that matches the regular expression _`regExp`_ with the replacement sequence _`replacement`_ .

Signature

```
   public String replaceFirst(String regExp, String replacement)

```

Parameters

```
   regExp
```

Type: String

```
   replacement
```

Type: String

Return Value

Type: String

Usage

See the Java `[Pattern](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html)` class for information on regular expressions.


Apex Reference Guide String Class

Example

```
   String s1 = 'a b c 11 xyz';

   String regExp = '[a-zA-Z]{2}';

   String replacement = '2';

   String s2 = s1.replaceFirst(regExp, replacement);

   System.assertEquals('a b c 11 2z', s2);

##### reverse()

```

Returns a String with all the characters reversed.

Signature

```
   public String reverse()

```

Return Value

Type: String

##### right(length)

Returns the rightmost characters of the current String of the specified length.

Signature

```
   public String right(Integer length)

```

Parameters

```
   length
```

Type: Integer

If _`length`_ is greater than the String size, the entire String is returned.

Return Value

Type: String

Example

```
   String s1 = 'Hello Max';

   String s2 =

     s1.right(3);

   System.assertEquals(

     'Max', s2);

##### rightPad(length)

```

Returns the current String padded with spaces on the right and of the specified length.


Apex Reference Guide String Class

Signature

```
   public String rightPad(Integer length)

```

Parameters

```
   length
```

Type: Integer

If _`length`_ is less than or equal to the current String size, the entire String is returned without space padding.

Return Value

Type: String

Example

```
   String s1 = 'abc';

   String s2 =

     s1.rightPad(5);

   System.assertEquals(

     'abc ', s2);

##### rightPad(length, padStr)

```

Returns the current String padded with String `padStr` on the right and of the specified length.

Signature

```
   public String rightPad(Integer length, String padStr)

```

Parameters

```
   length
```

Type: Integer

```
   padStr
```

Type: String

String to pad with; if null or empty treated as single blank.

Usage

If _`length`_ is less than or equal to the current String size, the entire String is returned without space padding.

Return Value

Type: String

Example

```
   String s1 = 'abc';

   String s2 = 'xy';

```


Apex Reference Guide String Class

```
   String s3 = s1.rightPad(7, s2);

   System.assertEquals('abcxyxy', s3);

##### split(regExp)

```

Returns a list that contains each substring of the String that is terminated by either the regular expression _`regExp`_ or the end of the
String.

Signature

```
   public String[] split(String regExp)

```

Parameters

```
   regExp
```

Type: String

Return Value

Type: String[]

Note: In API version 34.0 and earlier, a zero-width _`regExp`_ value produces an empty list item at the beginning of the method’s
output.

Usage

See the Java `Pattern` class for information on regular expressions.

The substrings are placed in the list in the order in which they occur in the String. If _`regExp`_ does not match any part of the String,
the resulting list has just one element containing the original String.

Example

In the following example, a string is split using a backslash as a delimiter.

```
   public String splitPath(String filename) {

      if (filename == null)

        return null;

      List<String> parts = filename.split('\\\\');

      filename = parts[parts.size()-1];

      return filename;

   }

   // For example, if the file path is e:\\processed\\PPDSF100111.csv

   // This method splits the path and returns the last part.

   // Returned filename is PPDSF100111.csv

##### split(regExp, limit)

```

Returns a list that contains each substring of the String that is terminated by either the regular expression _`regExp`_ or the end of the
String.


Apex Reference Guide String Class

Signature

```
   public String[] split(String regExp, Integer limit)

```

Parameters

```
   regExp
```

Type: String

A regular expression.

```
   limit
```

Type: Integer

Return Value

Type: String[]

Note: In API version 34.0 and earlier, a zero-width _`regExp`_ value produces an empty list item at the beginning of the method’s
output.

Usage

The optional _`limit`_ parameter controls the number of times the pattern is applied and therefore affects the length of the list.

**•** If _`limit`_ is greater than zero:

**–** The pattern is applied a maximum of ( _`limit`_     - 1) times.

**–** The list’s length is no greater than _`limit`_ .

**–** The list’s last entry contains all input beyond the last matched delimiter.

**•** If _`limit`_ is non-positive, the pattern is applied as many times as possible, and the list can have any length.

**•** If _`limit`_ is zero, the pattern is applied as many times as possible, the list can have any length, and trailing empty strings are
discarded.

Example

For example, for `String s = 'boo:and:moo'` :

**•** `s.split(':', 2)` results in `{'boo', 'and:moo'}`

**•** `s.split(':', 5)` results in `{'boo', 'and', 'moo'}`

**•** `s.split(':', -2)` results in `{'boo', 'and', 'moo'}`

**•** `s.split('o', 5)` results in `{'b', '', ':and:m', '', ''}`

**•** `s.split('o', -2)` results in `{'b', '', ':and:m', '', ''}`

**•** `s.split('o', 0)` results in `{'b', '', ':and:m'}`

##### splitByCharacterType()

Splits the current String by character type and returns a list of contiguous character groups of the same type as complete tokens.

Signature

```
   public List<String> splitByCharacterType()

```


Apex Reference Guide String Class

Return Value

Type: List<String>

Usage

[For more information about the character types used, see java.lang.Character.getType(char).](http://docs.oracle.com/javase/7/docs/api/java/lang/Character.html#getType%28char%29)

Example

```
   String s1 = 'Lightning.platform';

   List<String> ls =

     s1.splitByCharacterType();

   System.debug(ls);

   // Writes this output:

   // (L, ightning, ., platform)

##### splitByCharacterTypeCamelCase()

```

Splits the current String by character type and returns a list of contiguous character groups of the same type as complete tokens, with
the following exception: the uppercase character, if any, immediately preceding a lowercase character token belongs to the following
character token rather than to the preceding.

Signature

```
   public List<String> splitByCharacterTypeCamelCase()

```

Return Value

Type: List<String>

Usage

[For more information about the character types used, see java.lang.Character.getType(char).](http://docs.oracle.com/javase/7/docs/api/java/lang/Character.html#getType%28char%29)

Example

```
   String s1 = 'Lightning.platform';

   List<String> ls =

     s1.splitByCharacterTypeCamelCase();

   System.debug(ls);

   // Writes this output:

   // (Lightning, ., platform)

##### startsWith(prefix)

```

Returns `true` if the String that called the method begins with the specified _`prefix`_ .

Signature

```
   public Boolean startsWith(String prefix)

```


Apex Reference Guide String Class

Parameters

```
   prefix
```

Type: String

Return Value

Type: Boolean

Example

```
   String s1 = 'AE86 vs EK9';

   System.assert(s1.startsWith('AE86'));

##### startsWithIgnoreCase(prefix)

```

Returns `true` if the current String begins with the specified prefix regardless of the prefix case.

Signature

```
   public Boolean startsWithIgnoreCase(String prefix)

```

Parameters

```
   prefix
```

Type: String

Return Value

Type: Boolean

Example

```
   String s1 = 'AE86 vs EK9';

   System.assert(s1.startsWithIgnoreCase('ae86'));

##### stripHtmlTags()

```

Removes HTML markup and returns plain text.

Signature

```
   public String stripHtmlTags()

```

Return Value

Type: String


Apex Reference Guide String Class

Usage

Warning: The stripHtmlTags function doesn’t recursively strip tags; therefore, tags can still exist in the returned string. Don’t use
the stripHtmlTags function to sanitize input for inclusion as a raw HTML page. The unescaped output isn’t considered safe to
include in an HTML document. The function will be deprecated in a future release.

Example

```
   String s1 = '<b>hello world</b>';

   String s2 = s1.stripHtmlTags();

   System.assertEquals(

     'hello world', s2);

##### substring(startIndex)

```

Returns a new String that begins with the character at the specified zero-based _`startIndex`_ and extends to the end of the String.

Signature

```
   public String substring(Integer startIndex)

```

Parameters

```
   startIndex
```

Type: Integer

Return Value

Type: String

Example

```
   String s1 = 'hamburger';

   System.assertEquals('burger', s1.substring(3));

##### substring(startIndex, endIndex)

```

Returns a new String that begins with the character at the specified zero-based _`startIndex`_ and extends to the character at
_`endIndex`_   - 1.

Signature

```
   public String substring(Integer startIndex, Integer endIndex)

```

Parameters

```
   startIndex
```

Type: Integer

```
   endIndex
```

Type: Integer


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   'hamburger'.substring(4, 8);

   // Returns "urge"

   'smiles'.substring(1, 5);

   // Returns "mile"

##### substringAfter(separator)

```

Returns the substring that occurs after the first occurrence of the specified separator.

Signature

```
   public String substringAfter(String separator)

```

Parameters

```
   separator
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce.Lightning.platform';

   String s2 =

     s1.substringAfter('.');

   System.assertEquals(

     'Lightning.platform', s2);

##### substringAfterLast(separator)

```

Returns the substring that occurs after the last occurrence of the specified separator.

Signature

```
   public String substringAfterLast(String separator)

```

Parameters

```
   separator
```

Type: String


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   String s1 = 'Salesforce.Lightning.platform';

   String s2 =

     s1.substringAfterLast('.');

   System.assertEquals(

     'platform', s2);

##### substringBefore(separator)

```

Returns the substring that occurs before the first occurrence of the specified separator.

Signature

```
   public String substringBefore(String separator)

```

Parameters

```
   separator
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'Salesforce.Lightning.platform';

   String s2 =

     s1.substringBefore('.');

   System.assertEquals(

     'Salesforce', s2);

##### substringBeforeLast(separator)

```

Returns the substring that occurs before the last occurrence of the specified separator.

Signature

```
   public String substringBeforeLast(String separator)

```

Parameters

```
   separator
```

Type: String


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   String s1 = 'Salesforce.Lightning.platform';

   String s2 =

     s1.substringBeforeLast('.');

   System.assertEquals(

     'Salesforce.Lightning', s2);

##### substringBetween(tag)

```

Returns the substring that occurs between two instances of the specified _`tag`_ String.

Signature

```
   public String substringBetween(String tag)

```

Parameters

```
   tag
```

Type: String

Return Value

Type: String

Example

```
   String s1 = 'tagYellowtag';

   String s2 = s1.substringBetween('tag');

   System.assertEquals('Yellow', s2);

##### substringBetween(open, close)

```

Returns the substring that occurs between the two specified Strings.

Signature

```
   public String substringBetween(String open, String close)

```

Parameters

```
   open
```

Type: String

```
   close
```

Type: String


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   String s1 = 'xYellowy';

   String s2 =

     s1.substringBetween('x','y');

   System.assertEquals(

     'Yellow', s2);

##### swapCase()

```

Swaps the case of all characters and returns the resulting String by using the default (English US) locale.

Signature

```
   public String swapCase()

```

Return Value

Type: String

Usage

Upper case and title case converts to lower case, and lower case converts to upper case.

Example

```
   String s1 = 'Force.com';

   String s2 = s1.swapCase();

   System.assertEquals('fORCE.COM', s2);

##### toLowerCase()

```

Converts all of the characters in the String to lowercase using the rules of the default (English US) locale.

Signature

```
   public String toLowerCase()

```

Return Value

Type: String

Example

```
   String s1 = 'ThIs iS hArD tO rEaD';

   System.assertEquals('this is hard to read',

     s1.toLowerCase());

```


Apex Reference Guide String Class

##### toLowerCase(locale)

Converts all of the characters in the String to lowercase using the rules of the specified locale.

Signature

```
   public String toLowerCase(String locale)

```

Parameters

```
   locale
```

Type: String

Return Value

Type: String

Example

```
   // Example in Turkish

   // An uppercase dotted "i", \u0304, which is İ

   // Note this contains both a İ as well as a I

   String s1 = 'KIYMETLİ';

   String s1Lower = s1.toLowerCase('tr');

   // Dotless lowercase "i", \u0131, which is ı

   // Note this has both a i and ı

   String expected = 'kıymetli';

   System.assertEquals(expected, s1Lower);

   // Note if this was done in toLowerCase(‘en’), it would output ‘kiymetli’

##### toUpperCase()

```

Converts all of the characters in the String to uppercase using the rules of the default (English US) locale.

Signature

```
   public String toUpperCase()

```

Return Value

Type: String

Example

```
   String myString1 = 'abcd';

   String myString2 = 'ABCD';

   myString1 =

     myString1.toUpperCase();

   Boolean result =

     myString1.equals(myString2);

   System.assertEquals(result, true);

```


Apex Reference Guide String Class

##### toUpperCase(locale)

Converts all of the characters in the String to the uppercase using the rules of the specified locale.

Signature

```
   public String toUpperCase(String locale)

```

Parameters

```
   locale
```

Type: String

Return Value

Type: String

Example

```
   // Example in Turkish

   // Dotless lowercase "i", \u0131, which is ı

   // Note this has both a i and ı

   String s1 = 'imkansız';

   String s1Upper = s1.toUpperCase('tr');

   // An uppercase dotted "i", \u0304, which is İ

   // Note this contains both a İ as well as a I

   String expected = 'İMKANSIZ';

   System.assertEquals(expected, s1Upper);

##### template(valueMap)

```

Substitutes variables in a string for their corresponding values in the `valueMap` parameter, and returns the updated string.

Signature

```
   public String template(Map<String, Object> valueMap)

```

Parameters

```
   valueMap
```

Type: Map<String,Object>

A map in which each key is the variable name specified in the string, and each value is the corresponding value to substitute into
the string.

Return Value

Type: String


Apex Reference Guide String Class

Usage

Both regular and multiline string literals are supported. In the string literal, use the syntax `${variableName}` to represent a
placeholder variable. For example:

```
   String formatted = '${name} was last updated ${date}'.template(new Map<String, Object> {

      'name' => 'My class',

      'date' => DateTime.newInstance(2018, 11, 15)

   });

```

To include literal text between `${}` in the string, use the `$` character to escape the variable reference. For example:

```
   String anotherStr = '''

      Escaped: $${hello}

      Unescaped: ${hello}

   '''.template(new Map<String, Object> {

        'hello' => 'hi'

   });

   Assert.areEqual('''

      Escaped: ${hello}

      Unescaped: hi

   ''', anotherStr);

```

Non-string values in the `valueMap` are implicitly converted to strings by using the `toString()` method overrides that exist on
the type.

Default values for missing variables aren’t supported. If a variable is present in the string but not as a key in the `valueMap`, a
`StringException` is thrown.

Implicit string formatting lookups, such as date formatting, also aren’t supported as values. Instead, first use the relevant Apex method
to apply the formatting, and then pass the result into the `valueMap` .

Example

In this example, the multiline string jsonBody has two variables: `sc` and `sn` . The `template` method sets the variables to the values
of `schoolCity` and `schoolName`, respectively, and returns the updated string.

```
   String schoolCity = ExampleClass.getschoolCity(); // "exampleCity"

   String schoolName = ExampleClass.getschoolName(); // "exampleSchool"

   String jsonBody = '''

   {

      "city" : "${sc}",

      "name" : "${sn}"

   }

   '''.template(new Map<String, Object> {

        'sc' => schoolCity,

        'sn' => schoolName

   });

   Assert.areEqual(

   '''

   {

      "city" : "exampleCity",

      "name" : "exampleSchool"

```


Apex Reference Guide String Class

```
   }

   ''', jsonBody);

##### trim()

```

Returns a copy of the string that no longer contains any leading or trailing white space characters.

Signature

```
   public String trim()

```

Return Value

Type: String

Usage

Leading and trailing ASCII control characters such as tabs and newline characters are also removed. White space and control characters
that aren’t at the beginning or end of the sentence aren’t removed.

Example

```
   String s1 = ' Hello! ';

   String trimmed = s1.trim();

   system.assertEquals('Hello!', trimmed);

##### uncapitalize()

```

Returns the current String with the first letter in lowercase.

Signature

```
   public String uncapitalize()

```

Return Value

Type: String

Example

```
   String s1 =

     'Hello max';

   String s2 =

     s1.uncapitalize();

   System.assertEquals(

     'hello max',

      s2);

```


Apex Reference Guide String Class

##### unescapeCsv()

Returns a String representing an unescaped CSV column.

Signature

```
   public String unescapeCsv()

```

Return Value

Type: String

Usage

If the String is enclosed in double quotes and contains a comma, newline or double quote, quotes are removed. Also, any double quote
escaped characters (a pair of double quotes) are unescaped to just one double quote.

If the String is not enclosed in double quotes, or is and does not contain a comma, newline or double quote, it is returned unchanged.

Example

```
   String s1 =

     '"Max1, ""Max2"""';

   String s2 =

     s1.unescapeCsv();

   System.assertEquals(

     'Max1, "Max2"',

      s2);

##### unescapeEcmaScript()

```

Unescapes any EcmaScript literals found in the String.

Signature

```
   public String unescapeEcmaScript()

```

Return Value

Type: String

Example

```
   String s1 =

     '\"3.8\",\"3.9\"';

   String s2 =

     s1.unescapeEcmaScript();

   System.assertEquals(

     '"3.8","3.9"',

     s2);

```


Apex Reference Guide String Class

##### unescapeHtml3()

Unescapes the characters in a String using HTML 3.0 entities.

Signature

```
   public String unescapeHtml3()

```

Return Value

Type: String

Example

```
   String s1 =

     '&quot;&lt;Black&amp;White&gt;&quot;';

   String s2 =

     s1.unescapeHtml3();

   System.assertEquals(

     '"<Black&White>"',

     s2);

##### unescapeHtml4()

```

Unescapes the characters in a String using HTML 4.0 entities.

Signature

```
   public String unescapeHtml4()

```

Return Value

Type: String

Usage

If an entity isn’t recognized, it is kept as is in the returned string.

Example

```
   String s1 =

     '&quot;&lt;Black&amp;White&gt;&quot;';

   String s2 =

     s1.unescapeHtml4();

   System.assertEquals(

     '"<Black&White>"',

     s2);

```


Apex Reference Guide String Class

##### unescapeJava()

Returns a String whose Java literals are unescaped. Literals unescaped include escape sequences for quotes (\\") and control characters,
such as tab (\\t), and carriage return (\\n).

Signature

```
   public String unescapeJava()

```

Return Value

Type: String

The unescaped string.

Example

```
   String s = 'Company: \\"Salesforce.com\\"';

   String unescapedStr = s.unescapeJava();

   System.assertEquals('Company: "Salesforce.com"', unescapedStr);

##### unescapeUnicode()

```

Returns a String whose escaped Unicode characters are unescaped.

Signature

```
   public String unescapeUnicode()

```

Return Value

Type: String

The unescaped string.

Example

```
   String s = 'De onde voc\u00EA \u00E9?';

   String unescapedStr = s.unescapeUnicode();

   System.assertEquals('De onde você é?', unescapedStr);

##### unescapeXml()

```

Unescapes the characters in a String using XML entities.

Signature

```
   public String unescapeXml()

```

Return Value

Type: String


Apex Reference Guide String Class

Usage

Supports only the five basic XML entities (gt, lt, quot, amp, apos). Does not support DTDs or external entities.

Example

```
   String s1 =

     '&quot;&lt;Black&amp;White&gt;&quot;';

   String s2 =

     s1.unescapeXml();

   System.assertEquals(

     '"<Black&White>"',

     s2);

##### valueOf(dateToConvert)

```

Returns a String that represents the specified Date in the standard “yyyy-MM-dd” format.

Signature

```
   public static String valueOf(Date dateToConvert)

```

Parameters

```
   dateToConvert
```

Type: Date

Return Value

Type: String

Example

```
   Date myDate = Date.Today();

   String sDate = String.valueOf(myDate);

##### valueOf(datetimeToConvert)

```

Returns a String that represents the specified Datetime in the standard “yyyy-MM-dd HH:mm:ss” format for the local time zone.

Signature

```
   public static String valueOf(Datetime datetimeToConvert)

```

Parameters

```
   datetimeToConvert
```

Type: Datetime


Apex Reference Guide String Class

Return Value

Type: String

Example

```
   DateTime dt = datetime.newInstance(1996, 6, 23);

   String sDateTime = String.valueOf(dt);

   System.assertEquals('1996-06-23 00:00:00', sDateTime);

##### valueOf(decimalToConvert)

```

Returns a String that represents the specified Decimal.

Signature

```
   public static String valueOf(Decimal decimalToConvert)

```

Parameters

```
   decimalToConvert
```

Type: Decimal

Return Value

Type: String

Example

```
   Decimal dec = 3.14159265;

   String sDecimal = String.valueOf(dec);

   System.assertEquals('3.14159265', sDecimal);

##### valueOf(doubleToConvert)

```

Returns a String that represents the specified Double.

Signature

```
   public static String valueOf(Double doubleToConvert)

```

Parameters

```
   doubleToConvert
```

Type: Double

Return Value

Type: String


Apex Reference Guide String Class

Example

```
   Double myDouble = 12.34;

   String myString =

     String.valueOf(myDouble);

   System.assertEquals(

     '12.34', myString);

##### valueOf(integerToConvert)

```

Returns a String that represents the specified Integer.

Signature

```
   public static String valueOf(Integer integerToConvert)

```

Parameters

```
   integerToConvert
```

Type: Integer

Return Value

Type: String

Example

```
   Integer myInteger = 22;

   String sInteger = String.valueOf(myInteger);

   System.assertEquals('22', sInteger);

##### valueOf(longToConvert)

```

Returns a String that represents the specified Long.

Signature

```
   public static String valueOf(Long longToConvert)

```

Parameters

```
   longToConvert
```

Type: Long

Return Value

Type: String


Apex Reference Guide String Class

Example

```
   Long myLong = 123456789;

   String sLong = String.valueOf(myLong);

   System.assertEquals('123456789', sLong);

##### valueOf(toConvert)

```

Returns a string representation of the specified object argument.

Signature

```
   public static String valueOf(Object toConvert)

```

Parameters

```
   toConvert
```

Type: Object

Return Value

Type: String

Usage

##### If the argument is not a String, the valueOf method converts it into a String by calling the toString method on the argument,

if available, or any overridden `toString` method if the argument is a user-defined type. Otherwise, if no `toString` method is
available, it returns a String representation of the argument.

Example

```
   List<Integer> ls =

     new List<Integer>();

   ls.add(10);

   ls.add(20);

   String strList =

     String.valueOf(ls);

   System.assertEquals(

     '(10, 20)', strList);

##### valueOfGmt(datetimeToConvert)

```

Returns a String that represents the specified Datetime in the standard “yyyy-MM-dd HH:mm:ss” format for the GMT time zone.

Signature

```
   public static String valueOfGmt(Datetime datetimeToConvert)

```


### Apex Reference Guide StubProvider Interface

Parameters

```
   datetimeToConvert
```

Type: Datetime

Return Value

Type: String

Example

```
   // For a PST timezone:

   DateTime dt = datetime.newInstance(2001, 9, 14);

   String sDateTime = String.valueOfGmt(dt);

   System.assertEquals('2001-09-14 07:00:00', sDateTime);

### StubProvider Interface StubProvider is a callback interface that you can use as part of the Apex stub API to implement a mocking framework. Use this
```

interface with the `Test.createStub()` method to create stubbed Apex objects for testing.

Namespace

System

Usage

### The StubProvider interface allows you to define the behavior of a stubbed Apex class. The interface specifies a single method that

requires implementing: `handleMethodCall()` . You specify the behavior of each method of the stubbed class in the
`handleMethodCall()` method.

In your Apex test, you create a stubbed object using the `Test.createStub()` method. When you invoke methods on the stubbed
object, `StubProvider.handleMethodCall()` is called, which performs the behavior that you’ve specified for each method.

IN THIS SECTION:

#### StubProvider Methods

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

createStub(parentType, stubProvider)

#### StubProvider Methods

### The following are methods for StubProvider .


Apex Reference Guide StubProvider Interface

IN THIS SECTION:

##### handleMethodCall(stubbedObject, stubbedMethodName, returnType, listOfParamTypes, listOfParamNames, listOfArgs)

Use this method to define the behavior of each method of a stubbed class.

##### handleMethodCall(stubbedObject, stubbedMethodName, returnType, listOfParamTypes,

listOfParamNames, listOfArgs)

Use this method to define the behavior of each method of a stubbed class.

Signature

```
   public Object handleMethodCall(Object stubbedObject, String stubbedMethodName,

   System.Type returnType, List<System.Type> listOfParamTypes, List<String>

   listOfParamNames, List<Object> listOfArgs)

```

Parameters

```
   stubbedObject
```

Type: Object

The stubbed object.

```
   stubbedMethodName
```

Type: String

The name of the invoked method.

```
   returnType
```

Type: System.Type

The return type of the invoked method.

```
   listOfParamTypes
```

Type: List<System.Type>

A list of the parameter types of the invoked method.

```
   listOfParamNames
```

Type: List<String>

A list of the parameter names of the invoked method.

```
   listOfArgs
```

Type: List<Object>

The actual argument values passed into this method at runtime.

Return Value

Type: Object


### Apex Reference Guide System Class

Usage

You can use the parameters passed into this method to identify which method on the stubbed object was invoked. Then you can define
the behavior for each identified method.

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

### System Class

Contains methods for system operations, such as writing debug messages and scheduling jobs.

Namespace

### System

#### System Methods

### The following are methods for System . All methods are static.

IN THIS SECTION:

abortJob(jobId)
Stops the specified job. If the job is currently executing, the stopped job is still visible in the job queue in the Salesforce user interface.
The specified job is stopped, but any code that is in progress will continue to execute until it completes.

assert(condition, msg)
Asserts that the specified condition is true. If it isn’t, a fatal error is returned that causes code execution to halt.

assertEquals(expected, actual, msg)
Asserts that the first two arguments are the same. If they aren’t, a fatal error is returned that causes code execution to halt.

assertNotEquals(expected, actual, msg)
Asserts that the first two arguments are different. If they’re the same, a fatal error is returned that causes code execution to halt.

attachFinalizer(finalizer)
Attach a finalizer for a Queueable job.

currentPageReference()
Returns a reference to the current page. This is used with Visualforce pages.

currentTimeMillis()
Returns the current time in milliseconds, which is expressed as the difference between the current time and midnight, January 1,
1970 UTC.

debug(msg)
Writes the specified message, in string format, to the execution debug log. The `DEBUG` log level is used.

debug(logLevel, msg)
Writes the specified message, in string format, to the execution debug log with the specified log level.

enqueueJob(queueableObj)
Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID.


Apex Reference Guide System Class

enqueueJob(queueable, delay)
Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. The job is scheduled
with a specified minimum delay (0–10 minutes). The delay is ignored during Apex testing.

enqueueJob(queueable, asyncOptions)
Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. Specify a unique signature
for your queueable job, the maximum stack depth or the minimum queue delay in the asyncOptions parameter.

equals(obj1, obj2)
Returns `true` if both arguments are equal. Otherwise, returns `false` .

getApplicationReadWriteMode()
Returns the read write mode set for an organization during Salesforce.com upgrades and downtimes.

getQuiddityShortCode(QuiddityValue)
Returns the short code for the Quiddity value of the current Request object.

hashCode(obj)
Returns the hash code of the specified object.

isBatch()
Returns `true` if a batch Apex job invoked the executing code, or `false` if not. In API version 35.0 and earlier, also returns `true`
if a queueable Apex job invoked the code.

isFunctionCallback()
Returns `true` if an asynchronous Salesforce Function callback invoked the executing code, or `false` if not. Available in API version
51.0 and later.

isFuture()
Returns `true` if the currently executing code is invoked by code contained in a method annotated with `future` ; `false`
otherwise.

isQueueable()
Returns `true` if a queueable Apex job invoked the executing code. Returns `false` if not, including if a batch Apex job or a future
method invoked the code.

isRunningElasticCompute()
Reserved for future use.

isScheduled()
Returns `true` if the currently executing code is invoked by a scheduled Apex job; `false` otherwise.

movePassword(targetUserId,sourceUserId)
Moves the specified user’s password to a different user.

now()
Returns the current date and time in the GMT time zone.

pauseJobById(cronTriggerId)
Pause a scheduled Apex job specified by its CronTrigger ID.

pauseJobByName(jobName)
Pause a scheduled Apex job specified by its name.

process(workItemIds, action, comments, nextApprover)
Processes the list of work item IDs.


Apex Reference Guide System Class

purgeOldAsyncJobs(dt)
Deletes asynchronous Apex job records for jobs that have finished execution before the specified date with a Completed, Aborted,
or Failed status, and returns the number of records deleted.

purgeOldAsyncJobs(dt, numOfJobs)
Deletes asynchronous Apex job records for the specified number of jobs that finished before the specified date and have a Completed,
Aborted, or Failed status. Returns the number of records deleted.

requestVersion()
Returns a two-part version that contains the major and minor version numbers of a package. Applies to first-generation managed
packages.

resetPassword(userId, sendUserEmail)
Resets the password for the specified user.

resetPasswordWithEmailTemplate(userId, sendUserEmail, emailTemplateName)
Resets the user's password and sends an email to the user with their new password. You specify the email template that is sent to
the specified user. Use this method for external users of Experience Cloud sites.

resumeJobById(cronTriggerId)
Resume a paused scheduled Apex job specified by its CronTrigger ID.

resumeJobByName(jobName)
Resumes a paused scheduled Apex job specified by its name.

runAs(version)
Changes the current package version to the package version specified in the argument.

runAs(userSObject)
Changes the current user to the specified user.

schedule(jobName, cronExpression, schedulableClass)
Use `schedule` with an Apex class that implements the `Schedulable` interface to schedule the class to run at the time specified
by a Cron expression.

scheduleBatch(batchable, jobName, minutesFromNow)
Schedules a batch job to run once in the future after the specified time interval and with the specified job name.

scheduleBatch(batchable, jobName, minutesFromNow, scopeSize)
Schedules a batch job to run once in the future after the specified the time interval, with the specified job name and scope size.
Returns the scheduled job ID (CronTrigger ID).

setPassword(userId, password)
Sets the password for the specified user.

submit(workItemIds, comments, nextApprover)
Submits the processed approvals. The current user is the submitter and the entry criteria is evaluated for all processes applicable to
the current user.

today()
Returns the current date in the current user's time zone.

##### **`abortJob(jobId)`**

Stops the specified job. If the job is currently executing, the stopped job is still visible in the job queue in the Salesforce user interface.
The specified job is stopped, but any code that is in progress will continue to execute until it completes.


Apex Reference Guide System Class

Signature

```
   public static Void abortJob(String jobId)

```

Parameters

```
   jobId
```

Type: String

The _`jobId`_ [is the ID associated with an AsyncApexJob ID for batch or future Apex jobs, or a CronTrigger ID for scheduled Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)
jobs. You can't abort a scheduled Apex job using an AsyncApexJob ID.

Return Value

Type: Void

Usage

The following methods return the job ID that can be passed to `abortJob` .

**•** `System.schedule` method—returns the CronTrigger object ID associated with the scheduled job as a string.

**•** `[SchedulableContext.getTriggerId](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_scheduler.htm)` method—returns the CronTrigger object ID associated with the scheduled job as
a string.

**•** `[getJobId](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)` method—returns the AsyncApexJob object ID associated with the batch job as a string.

**•** [Using Batch Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm) `[Database.executeBatch](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)` method—returns the AsyncApexJob object ID associated with the batch job as
a string.

##### assert(condition, msg)

Asserts that the specified condition is true. If it isn’t, a fatal error is returned that causes code execution to halt.

Important: We recommend that you use the methods of the Assert Class rather than this method. The `System.Assert`
class provides methods that handle all types of logical assertions and comparisons, which improve the clarity of your Apex code.

Signature

```
   public static Void assert(Boolean condition, Object msg)

```

Parameters

```
   condition
```

Type: Boolean

```
   msg
```

Type: Object

(Optional) Custom message returned as part of the error message.

Return Value

Type: Void


Apex Reference Guide System Class

Usage

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

##### assertEquals(expected, actual, msg)

Asserts that the first two arguments are the same. If they aren’t, a fatal error is returned that causes code execution to halt.

Important: We recommend that you use the methods of the Assert Class rather than this method. The `System.Assert`
class provides methods that handle all types of logical assertions and comparisons, which improve the clarity of your Apex code.

Signature

```
   public static Void assertEquals(Object expected, Object actual, Object msg)

```

Parameters

```
   expected
```

Type: Object

Specifies the expected value.

```
   actual
```

Type: Object

Specifies the actual value.

```
   msg
```

Type: Object

(Optional) Custom message returned as part of the error message.

Return Value

Type: Void

Usage

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

##### assertNotEquals(expected, actual, msg)

Asserts that the first two arguments are different. If they’re the same, a fatal error is returned that causes code execution to halt.

Important: We recommend that you use the methods of the Assert Class rather than this method. The `System.Assert`
class provides methods that handle all types of logical assertions and comparisons, which improve the clarity of your Apex code.

Signature

```
   public static Void assertNotEquals(Object expected, Object actual, Object msg)

```

Parameters

```
   expected
```

Type: Object


Apex Reference Guide System Class

Specifies the expected value.

```
   actual
```

Type: Object

Specifies the actual value.

```
   msg
```

Type: Object

(Optional) Custom message returned as part of the error message.

Return Value

Type: Void

Usage

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

##### **`attachFinalizer(finalizer)`**

Attach a finalizer for a Queueable job.

Signature

```
   public static void attachFinalizer(Object finalizer)

```

Parameters

```
   finalizer
```

Type: Object

The instantiated class that implements the `System.Finalizer` interface.

Return Value

Type: void

##### currentPageReference()

Returns a reference to the current page. This is used with Visualforce pages.

Signature

```
   public static System.PageReference currentPageReference()

```

Return Value

Type: System.PageReference

Usage

For more information, see PageReference Class.


Apex Reference Guide System Class

##### currentTimeMillis()

Returns the current time in milliseconds, which is expressed as the difference between the current time and midnight, January 1, 1970
UTC.

Signature

```
   public static Long currentTimeMillis()

```

Return Value

Type: Long

##### debug(msg)

Writes the specified message, in string format, to the execution debug log. The `DEBUG` log level is used.

Signature

```
   public static Void debug(Object msg)

```

Parameters

```
   msg
```

Type: Object

Return Value

Type: Void

Usage

##### If the msg argument is not a string, the debug method calls String.valueOf to convert it into a string. The String.valueOf

method calls the `toString` method on the argument, if available, or any overridden `toString` method if the argument is a
user-defined type. Otherwise, if no `toString` method is available, it returns a string representation of the argument.

If the log level for Apex Code is set to `DEBUG` or higher, the message of this debug statement will be written to the debug log.

Note that when a map or set is printed, the output is sorted in key order and is surrounded with square brackets ( `[]` ). When an array or
list is printed, the output is enclosed in parentheses ( `()` ).

Note: Calls to System.debug are not counted as part of Apex code coverage.Calls to `System.debug` are not counted as part
of Apex code coverage.

[For more information on log levels, see Debug Log Levels in the Salesforce online help.](https://help.salesforce.com/s/articleView?id=platform.code_setting_debug_log_levels.htm&type=5&language=en_US)

##### debug(logLevel, msg)

Writes the specified message, in string format, to the execution debug log with the specified log level.

Signature

```
   public static Void debug(LoggingLevel logLevel, Object msg)

```


Apex Reference Guide System Class

Parameters

```
   logLevel
```

Type: LoggingLevel Enum

The logging level to set for this method.

```
   msg
```

Type: Object

The message or object to write in string format to the execution debug log.

Return Value

Type: Void

Usage

If the _`msg`_ argument is not a string, the `debug` method calls `String.valueOf` to convert it into a string. The `String.valueOf`
method calls the `toString` method on the argument, if available, or any overridden `toString` method if the argument is a
user-defined type. Otherwise, if no `toString` method is available, it returns a string representation of the argument.

Note: Calls to `System.debug` are not counted as part of Apex code coverage.

[For more information on log levels, see Debug Log Levels in the Salesforce online help.](https://help.salesforce.com/s/articleView?id=platform.code_setting_debug_log_levels.htm&type=5&language=en_US)

##### enqueueJob(queueableObj)

Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID.

Signature

```
   public static ID enqueueJob(Object queueableObj)

```

Parameters

```
   queueableObj
```

Type: Object

An instance of the class that implements the Queueable Interface.

Return Value

Type: ID

The job ID, which corresponds to the ID of an AsyncApexJob record.

Usage

To add a job for asynchronous execution, call `System.enqueueJob` by passing in an instance of your class implementation of the
`Queueable` interface for execution as follows:

```
   ID jobID = System.enqueueJob(new MyQueueableClass());

```

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)


Apex Reference Guide System Class

##### **`enqueueJob(queueable, delay)`**

Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. The job is scheduled with a
specified minimum delay (0–10 minutes). The delay is ignored during Apex testing.

Signature

```
   public static Id enqueueJob(Object queueable, Integer delay)

```

Parameters

```
   queueable
```

Type: Object

An instance of the class that implements the Queueable Interface.

```
   delay
```

Type: Integer

The minimum delay (0–10 minutes) before the queueable job is scheduled for execution.

The delay is ignored during Apex testing.

Warning: When you set the delay to 0 (zero), the Queueable job is run as quickly as possible. With chained queueable jobs,
implement a mechanism to slow down or halt the job if necessary. Without such a fail-safe mechanism in place, you can rapidly
reach the daily async Apex limit.

Return Value

Type: Id

The job ID, which corresponds to the ID of an AsyncApexJob record.

Example

This example adds a job for delayed asynchronous execution by passing in an instance of your class implementation of the `Queueable`
interface for execution. There’s a minimum delay of 5 minutes before the job is executed.

```
   Integer delayInMinutes = 5;

   ID jobID = System.enqueueJob(new MyQueueableClass(), delayInMinutes);

```

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)

##### **`enqueueJob(queueable, asyncOptions)`**

Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. Specify a unique signature
for your queueable job, the maximum stack depth or the minimum queue delay in the asyncOptions parameter.

Signature

```
   public static Id enqueueJob(Object queueable, Object asyncoptions)

```


Apex Reference Guide System Class

Parameters

```
   queueable
```

Type: Object

An instance of the class that implements the Queueable Interface.

```
   asyncoptions
```

Type: AsyncOptions

Specify a unique signature for your queueable job, the maximum stack depth, or a minimum queue delay in the AsyncOptions class
properties.

Return Value

Type: Id

The job ID, which corresponds to the ID of an AsyncApexJob record.

Usage

The `[System.AsyncInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_AsyncInfo.htm)` class methods help you determine if maximum stack depth is set in your Queueable request and get the
stack depths and queue delay for queueables that are currently running. Use information about the current queueable execution to
make decisions on adjusting delays on subsequent calls.

These are methods in the `System.AsyncInfo` class.

**•** `hasMaxStackDepth()`

**•** `getCurrentQueueableStackDepth()`

**•** `getMaximumQueueableStackDepth()`

**•** `getMinimumQueueableDelayInMinutes()`

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)

##### equals(obj1, obj2)

Returns `true` if both arguments are equal. Otherwise, returns `false` .

Signature

```
   public static Boolean equals(Object obj1, Object obj2)

```

Parameters

```
   obj1
```

Type: Object

Object being compared.

```
   obj2
```

Type: Object

Object to compare with the first argument.

Return Value

Type: Boolean


Apex Reference Guide System Class

Usage

_`obj1`_ and _`obj2`_ can be of any type. They can be values, or object references, such as sObjects and user-defined types.

The comparison rules for `System.equals` are identical to the ones for the `==` operator. For example, string comparison is case
[insensitive. For information about the comparison rules, see the == operator.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_expressions_operators_understanding.htm)

##### getApplicationReadWriteMode()

Returns the read write mode set for an organization during Salesforce.com upgrades and downtimes.

Signature

```
   public static System.ApplicationReadWriteMode getApplicationReadWriteMode()

```

Return Value

Type: System.ApplicationReadWriteMode

Valid values are:

**•** `DEFAULT`

**•** `READ_ONLY`

Using the **`System.ApplicationReadWriteMode`** Enum

##### Use the System.ApplicationReadWriteMode enum returned by the getApplicationReadWriteMode to

programmatically determine if the application is in read-only mode during Salesforce upgrades and downtimes.

Valid values for the enum are:

**•** `DEFAULT`

**•** `READ_ONLY`

Example:

```
   public class myClass {

     public static void execute() {

      ApplicationReadWriteMode mode = System.getApplicationReadWriteMode();

      if (mode == ApplicationReadWriteMode.READ_ONLY) {

       // Do nothing. If DML operaton is attempted in readonly mode,

       // InvalidReadOnlyUserDmlException will be thrown.

      } else if (mode == ApplicationReadWriteMode.DEFAULT) {

       Account account = new Account(name = 'my account');

       insert account;

      }

     }

   }

##### getQuiddityShortCode(QuiddityValue)

```

Returns the short code for the Quiddity value of the current Request object.


Apex Reference Guide System Class

Signature

```
   public String getQuiddityShortCode(System.Quiddity QuiddityValue)

```

Parameters

```
   QuiddityValue
```

Type: System.Quiddity

The Quiddity enum value that has an associated short code. This short code is used in Event Monitoring logs. For more information,
[see Apex Execution Event Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_apexexecution.htm)

Return Value

Type: String

##### hashCode(obj)

Returns the hash code of the specified object.

Signature

```
   public static Integer hashCode(Object obj)

```

Parameters

```
   obj
```

Type: Object

The object to get the hash code for. This parameter can be of any type, including values or object references, such as sObjects or
user-defined types.

Return Value

Type: Integer

Versioned Behavior Changes

In API version 51.0 and later, the `hashCode()` method returns the same hashCode for identical Id values. In API version 50.0 and
earlier, identical Id values didn’t always generate the same hashCode value.

##### isBatch()

Returns `true` if a batch Apex job invoked the executing code, or `false` if not. In API version 35.0 and earlier, also returns `true` if
a queueable Apex job invoked the code.

Signature

```
   public static Boolean isBatch()

```

Return Value

Type: Boolean


Apex Reference Guide System Class

Usage

A batch Apex job can’t invoke a future method. Before invoking a future method, use `isBatch()` to check whether the executing
code is a batch Apex job.

##### isFunctionCallback()

Returns `true` if an asynchronous Salesforce Function callback invoked the executing code, or `false` if not. Available in API version
51.0 and later.

Signature

```
   public static Boolean isFunctionCallback()

```

Return Value

Type: Boolean

Usage

Use this method to determine if the Apex code is being invoked as part of a callback from an asynchronous Salesforce Functions invocation.
For more details on invoking Salesforce Functions from Apex, see Functions Namespace

##### isFuture()

Returns `true` if the currently executing code is invoked by code contained in a method annotated with `future` ; `false` otherwise.

Signature

```
   public static Boolean isFuture()

```

Return Value

Type: Boolean

Usage

Since a future method can't be invoked from another future method, use this method to check if the current code is executing within
the context of a future method before you invoke a future method.

##### isQueueable()

Returns `true` if a queueable Apex job invoked the executing code. Returns `false` if not, including if a batch Apex job or a future
method invoked the code.

Signature

```
   public static Boolean isQueueable()

```


Apex Reference Guide System Class

Return Value

Type: Boolean

Usage

```
   public class SimpleQueueable implements Queueable {

      String name;

      public SimpleQueueable(String name) {

        this.name = name;

        System.assert(!System.isQueueable()); //Should return false

      }

      public void execute(QueueableContext ctx) {

        Account testAccount = new Account();

        testAccount.name = 'testAcc';

        insert(testAccount);

        System.assert(System.isQueueable()); //Should return true

      }

   }

   global class ComplexBatch implements Database.Batchable<SObject> {

      global Database.QueryLocator start(Database.BatchableContext info) {

        System.assert(!System.isQueueable()); //Should return false

        return Database.getQueryLocator([SELECT Id, Name FROM Account LIMIT 1]);

      }

      global void execute(Database.BatchableContext info, SObject[] scope) {

        System.assert(!System.isQueueable()); //Should return false

        System.enqueueJob(new SimpleQueueable('CallingFromComplexBatch'));

        System.assert(!System.isQueueable()); //Should return false

      }

      global void finish(Database.BatchableContext info) {

        System.assert(!System.isQueueable()); //Should return false

      }

   }

##### isRunningElasticCompute()

```

Reserved for future use.

Signature

```
   public static Boolean isRunningElasticCompute()

```

Return Value

Type: Boolean


Apex Reference Guide System Class

##### isScheduled()

Returns `true` if the currently executing code is invoked by a scheduled Apex job; `false` otherwise.

Signature

```
   public static Boolean isScheduled()

```

Return Value

Type: Boolean

##### movePassword(targetUserId,sourceUserId)

Moves the specified user’s password to a different user.

Signature

```
   public static Void movePassword(ID targetUserId, ID sourceUserId)

```

Parameters

```
   targetUserId
```

Type: ID

The user that the password is moved to.

```
   sourceUserId
```

Type: ID

The user that the password is moved from.

Return Value

Type: Void

Usage

Moving a password simplifies converting a user to another type of user, such as when converting an external user to a user with less
##### restrictive access. If you require access to the movePassword method, contact Salesforce.

Keep in mind these requirements.

**•** The _`targetUserId`_, _`sourceUserId`_, and user performing the move operation must all belong to the same Salesforce org.

**•** The _`targetUserId`_ and the _`sourceUserId`_ cannot be the same as the user performing the move operation.

**•** A user without a password can’t be specified as the _`sourceUserId`_ . For example, a source user who has already had their
password moved is left without a password. That user can’t be a source user again.

After the password is moved:

**•** The target user can log in with the password.

**•** The source user no longer has a password. To enable logins for this user, a password reset is required.


Apex Reference Guide System Class

##### now()

Returns the current date and time in the GMT time zone.

Signature

```
   public static Datetime now()

```

Return Value

Type: Datetime

##### **`pauseJobById(cronTriggerId)`**

Pause a scheduled Apex job specified by its CronTrigger ID.

Signature

```
   public static void pauseJobById(String cronTriggerId)

```

Parameters

```
   cronTriggerId
```

Type: String

The scheduled job ID.

Return Value

Type: void

##### **`pauseJobByName(jobName)`**

Pause a scheduled Apex job specified by its name.

Signature

```
   public static void pauseJobByName(String jobName)

```

Parameters

```
   jobName
```

Type: String

Return Value

Type: void

##### process(workItemIds, action, comments, nextApprover)

Processes the list of work item IDs.


Apex Reference Guide System Class

Signature

```
   public static List<Id> process(List<Id> workItemIds, String action, String comments,

   String nextApprover)

```

Parameters

```
   workItemIds
```

Type: List<Id>

```
   action
```

Type: String

```
   comments
```

Type: String

```
   nextApprover
```

Type: String

Return Value

Type: List<Id>

##### purgeOldAsyncJobs(dt)

Deletes asynchronous Apex job records for jobs that have finished execution before the specified date with a Completed, Aborted, or
Failed status, and returns the number of records deleted.

Signature

```
   public static Integer purgeOldAsyncJobs(Date dt)

```

Parameters

```
   dt
```

Type: Date

Specifies the date up to which old records are deleted. The date comparison is based on the `CompletedDate` field of AsyncApexJob,
which is in the GMT time zone.

Return Value

Type: Integer

Usage

[Asynchronous Apex job records are records in AsyncApexJob.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)

The system cleans up asynchronous job records for jobs that have finished execution and are older than seven days. You can use this
method to further reduce the size of AsyncApexJob by cleaning up more records.

Each execution of this method counts as a single row against the governor limit for DML statements.


Apex Reference Guide System Class

Example

This example shows how to delete all job records for jobs that have finished before today’s date.

```
   Integer count = System.purgeOldAsyncJobs

     (Date.today());

   System.debug('Deleted ' +

     count + ' old jobs.');

##### purgeOldAsyncJobs(dt, numOfJobs)

```

Deletes asynchronous Apex job records for the specified number of jobs that finished before the specified date and have a Completed,
Aborted, or Failed status. Returns the number of records deleted.

Signature

```
   public static Integer purgeOldAsyncJobs(Date dt, Integer numOfJobs)

```

Parameters

```
   dt
```

Type: Date

Specifies the date up to which old records are deleted. The date comparison is based on the `CompletedDate` field of AsyncApexJob,
which is in the GMT time zone.

```
   numOfJobs
```

Type: Integer

Specifies the maximum number of async jobs to delete, starting from the oldest job that finished before the specified date.

Return Value

Type: Integer

Usage

[Asynchronous Apex job records are records in AsyncApexJob.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)

The system purges asynchronous job records for jobs that have finished execution and are older than seven days. You can use this
method to further reduce the size of AsyncApexJob by purging more records.

Each execution of this method counts as a single row against the governor limit for DML statements.

Example

This example shows how to delete up to 1000 job records for jobs that finished before today’s date.

```
   Integer maximumNumberOfJobsToDelete = 1000;

   Integer count = System.purgeOldAsyncJobs(

      Date.today(),

      maximumNumberOfJobsToDelete

   );

   System.debug('Deleted ' + count + ' old jobs.');

```


Apex Reference Guide System Class

##### **`requestVersion()`**

Returns a two-part version that contains the major and minor version numbers of a package. Applies to first-generation managed
packages.

Signature

```
   public static System.Version requestVersion()

```

Return Value

Type: System.Version

Usage

Using this method, you can determine the version of an installed instance of your package from which the calling code is referencing
[your package. Based on the version that the calling code has, you can customize the behavior of your package code. See Version Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm)
[Code Behavior in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm) _Apex Developer Guide_ .

##### The requestVersion method isn’t supported for unmanaged packages. If you call it from an unmanaged package, an exception

will be thrown.

##### resetPassword(userId, sendUserEmail)

Resets the password for the specified user.

Signature

```
   public static System.ResetPasswordResult resetPassword(ID userId, Boolean sendUserEmail)

```

Parameters

```
   userId
```

Type: ID

```
   sendUserEmail
```

Type: Boolean

Return Value

Type: System.ResetPasswordResult

Usage

When the user logs in with the new password, they are prompted to enter a new password, and to select a security question and answer
if they haven't already. If you specify `true` for _`sendUserEmail`_, the user is sent an email notifying them that their password was
reset. A link to sign onto Salesforce using the new password is included in the email. Use `setPassword(userId, password)`
if you don't want the user to be prompted to enter a new password when they log in.

Warning: Be careful with this method, and do not expose this functionality to end-users.


Apex Reference Guide System Class

##### resetPasswordWithEmailTemplate(userId, sendUserEmail, emailTemplateName)

Resets the user's password and sends an email to the user with their new password. You specify the email template that is sent to the
specified user. Use this method for external users of Experience Cloud sites.

Signature

```
   public static System.ResetPasswordResult resetPasswordWithEmailTemplate(Id userId,

   Boolean sendUserEmail, String emailTemplateName)

```

Parameters

```
   userId
```

Type: Id

The ID of the user whose password was reset.

```
   sendUserEmail
```

Type: Boolean

```
   emailTemplateName
```

Type: String

Name of the email template.

Return Value

Type: System.ResetPasswordResult

Usage

If you specify `true` for _`sendUserEmail`_, specify the email template that is sent to the user notifying them that their password was
reset. When the user logs in with the new password in the email, they are prompted to enter a new password. A link to sign onto
Salesforce using the new password is included in the email. Use `setPassword(userId, password)` if you don't want the user
to be prompted to enter a new password when they log in.

The password reset process doesn't verify an external user's email address.

Warning: Be careful with this method, and do not expose this functionality to end-users.

##### **`resumeJobById(cronTriggerId)`**

Resume a paused scheduled Apex job specified by its CronTrigger ID.

Signature

```
   public static void resumeJobById(String cronTriggerId)

```

Parameters

```
   cronTriggerId
```

Type: String

The scheduled job ID.


Apex Reference Guide System Class

Return Value

Type: void

Usage

If you resume a paused scheduled job, the job immediately runs one time. Subsequent executions of the job run according to the
established schedule. Any scheduled executions that were missed while the job was paused don’t run.

##### **`resumeJobByName(jobName)`**

Resumes a paused scheduled Apex job specified by its name.

Signature

```
   public static void resumeJobByName(String jobName)

```

Parameters

```
   jobName
```

Type: String

Return Value

Type: void

Usage

If you resume a paused scheduled job, the job immediately runs one time. Subsequent executions of the job run according to the
established schedule. Any scheduled executions that were missed while the job was paused don’t run.

##### runAs(version)

Changes the current package version to the package version specified in the argument.

Signature

```
   public static Void runAs(System.Version version)

```

Parameters

```
   version
```

Type: System.Version

Return Value

Type: Void


Apex Reference Guide System Class

Usage

A package developer can use Version methods to continue to support existing behavior in classes and triggers in previous package
versions while continuing to evolve the code. Apex classes and triggers are saved with the version settings for each installed managed
package that the class or trigger references.

This method is used for testing your component behavior in different package versions that you upload to the AppExchange. This method
effectively sets a two-part version consisting of major and minor numbers in a test method so that you can test the behavior for different
package versions.

##### You can only use runAs in a test method. There is no limitation to the number of calls to this method in a transaction. For sample

[usage of this method, see Testing Behavior in Package Versions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_manpkgs_behavior_testing.htm)

##### runAs(userSObject)

Changes the current user to the specified user.

Signature

```
   public static Void runAs(User userSObject)

```

Parameters

```
   userSObject
```

Type: User

Return Value

Type: Void

Usage

##### All of the specified user's record sharing is enforced during the execution of runAs . You can only use runAs in a test method. For

[more information, see Using the runAs() Method.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_tools_runas.htm)

##### Note: The runAs method ignores user license limits. You can create new users with runAs even if your organization has no

additional user licenses.

##### The runAs method implicitly inserts the user that is passed in as parameter if the user has been instantiated, but not inserted yet. You can also use runAs to perform mixed DML operations in your test by enclosing the DML operations within the runAs block. In

this way, you bypass the mixed DML error that is otherwise returned when inserting or updating setup objects together with other
[sObjects. See sObjects That Cannot Be Used Together in DML Operations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects.htm)

##### Note: Every call to runAs counts against the total number of DML statements issued in the process. schedule(jobName, cronExpression, schedulableClass) Use schedule with an Apex class that implements the Schedulable interface to schedule the class to run at the time specified

by a Cron expression.


Apex Reference Guide System Class

Signature

```
   public static String schedule(String jobName, String cronExpression, Object

   schedulableClass)

```

Parameters

```
   jobName
```

Type: String

```
   cronExpression
```

Type: String

```
   schedulableClass
```

Type: Object

Return Value

Type: String

Returns the scheduled job ID (CronTrigger ID).

Usage

Use extreme care if you’re planning to schedule a class from a trigger. You must be able to guarantee that the trigger won’t add more
scheduled classes than the limit. In particular, consider API bulk updates, import wizards, mass record changes through the user interface,
and all cases where more than one record can be updated at a time. Use the `abortJob` method to stop the job after it has been
scheduled.

Note: Salesforce schedules the class for execution at the specified time. Actual execution may be delayed based on service
availability.

Using the **`System.Schedule`** Method

After you implement a class with the `Schedulable` interface, use the `System.Schedule` method to execute it. The scheduler
runs as system—all classes are executed, whether or not the user has permission to execute the class.

Note: Use extreme care if you’re planning to schedule a class from a trigger. You must be able to guarantee that the trigger won’t
add more scheduled classes than the limit. In particular, consider API bulk updates, import wizards, mass record changes through
the user interface, and all cases where more than one record can be updated at a time.

The `System.Schedule` method takes three arguments: a name for the job, an expression used to represent the time and date the
job is scheduled to run, and the name of the class. This expression has the following syntax:

```
   Seconds Minutes Hours Day_of_month Month Day_of_week Optional_year

```

Note: Salesforce schedules the class for execution at the specified time. Actual execution may be delayed based on service
availability.

The `System.Schedule` method uses the user's timezone for the basis of all schedules.

The following are the values for the expression:

**Name** **Values** **Special Characters**

_`Seconds`_ 0–59 None


Apex Reference Guide System Class

**Name** **Values** **Special Characters**

_`Minutes`_ 0–59 None

_`Hours`_ 0–23 `, - * /`

_`Day_of_month`_ 1–31 `, - * ? / L W`

_`Month`_ 1–12 or the following: `, - * /`

**•** `JAN`

**•** `FEB`

**•** `MAR`

**•** `APR`

**•** `MAY`

**•** `JUN`

**•** `JUL`

**•** `AUG`

**•** `SEP`

**•** `OCT`

**•** `NOV`

**•** `DEC`

_`Day_of_week`_ 1–7 or the following: `, - * ? / L #`

**•** `SUN`

**•** `MON`

**•** `TUE`

**•** `WED`

**•** `THU`

**•** `FRI`

**•** `SAT`

_`optional_year`_ null or 1970–2099 `, - * /`

The special characters are defined as follows:

**Special Character** **Description**

`,` Delimits values. For example, use `JAN, MAR, APR` to specify more than one month.

`-` Specifies a range. For example, use `JAN-MAR` to specify more than one month.

`*` Specifies all values. For example, if _`Month`_ is specified as `*`, the job is scheduled for
every month.


Apex Reference Guide System Class

**Special Character** **Description**

```
?

```

Specifies no specific value. This is only available for _`Day_of_month`_ and
_`Day_of_week`_, and is generally used when specifying a value for one and not the
other.

`/` Specifies increments. The number before the slash specifies when the intervals will
begin, and the number after the slash is the interval amount. For example, if you specify

`1/5` for _`Day_of_month`_, the Apex class runs every fifth day of the month, starting
on the first of the month.

`L` Specifies the end of a range (last). This is only available for _`Day_of_month`_ and
_`Day_of_week`_ . When used with _`Day of month`_, `L` always means the last day

of the month, such as January 31, February 29 for leap years, and so on. When used
with _`Day_of_week`_ by itself, it always means `7` or `SAT` . When used with a
_`Day_of_week`_ value, it means the last of that type of day in the month. For example,
if you specify `2L`, you are specifying the last Monday of the month. Do not use a range
of values with `L` as the results might be unexpected.

`W` Specifies the nearest weekday (Monday-Friday) of the given day. This is only available
for _`Day_of_month`_ . For example, if you specify `20W`, and the 20th is a Saturday,

the class runs on the 19th. If you specify `1W`, and the first is a Saturday, the class does
not run in the previous month, but on the third, which is the following Monday.

Tip: Use the `L` and `W` together to specify the last weekday of the month.

`#` Specifies the _`nth`_ day of the month, in the format _**`weekday`**_ `#` _**`day_of_month`**_ .
This is only available for _`Day_of_week`_ . The number before the `#` specifies weekday

( `SUN-SAT` ). The number after the `#` specifies the day of the month. For example,
specifying `2#1` means the class runs on the first Monday of every month.

The following are some examples of how to use the expression.

**Expression** **Description**

`0 0 13 * * ?` Class runs every day at 1 PM.

`0 0 22 ? * 6L` Class runs the last Friday of every month at 10 PM.

`0 0 10 ? * MON-FRI` Class runs Monday through Friday at 10 AM.

`0 0 20 * * ? 2010` Class runs every day at 8 PM during the year 2010.

In the following example, the class `proschedule` implements the `Schedulable` interface. The class is scheduled to run at 8 AM,
on the 13 February.

```
proschedule p = new proschedule();

     String sch = '0 0 8 13 2 ?';

     system.schedule('One Time Pro', sch, p);

```


Apex Reference Guide System Class

##### scheduleBatch(batchable, jobName, minutesFromNow)

Schedules a batch job to run once in the future after the specified time interval and with the specified job name.

Signature

```
   public static String scheduleBatch(Database.Batchable batchable, String jobName, Integer

   minutesFromNow)

```

Parameters

```
   batchable
```

Type: Database.Batchable

An instance of a class that implements the `Database.Batchable` interface.

```
   jobName
```

Type: String

The name of the job that this method will start.

```
   minutesFromNow
```

Type: Integer

The time interval in minutes after which the job should start executing. This argument must be greater than zero.

Return Value

Type: String

The scheduled job ID (CronTrigger ID).

Usage

Note: Some things to note about `System.scheduleBatch` :

**•** When you call `System.scheduleBatch`, Salesforce schedules the job for execution at the specified time. Actual execution
occurs at or after that time, depending on service availability.

**•** The scheduler runs as system—all classes are executed, whether the user has permission to execute the class or not.

**•** When the job’s schedule is triggered, the system queues the batch job for processing. If Apex flex queue is enabled in your
org, the batch job is added at the end of the flex queue. For more information, see Holding Batch Jobs in the Apex Flex Queue.

**•** All scheduled Apex limits apply for batch jobs scheduled using `System.scheduleBatch` . After the batch job is queued
(with a status of `Holding` or `Queued` ), all batch job limits apply and the job no longer counts toward scheduled Apex
limits.

**•** After calling this method and before the batch job starts, you can use the returned scheduled job ID to abort the scheduled
job using the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

[For an example, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)

##### scheduleBatch(batchable, jobName, minutesFromNow, scopeSize)

Schedules a batch job to run once in the future after the specified the time interval, with the specified job name and scope size. Returns
the scheduled job ID (CronTrigger ID).


Apex Reference Guide System Class

Signature

```
   public static String scheduleBatch(Database.Batchable batchable, String jobName, Integer

   minutesFromNow, Integer scopeSize)

```

Parameters

```
   batchable
```

Type: Database.Batchable

The batch class that implements the `Database.Batchable` interface.

```
   jobName
```

Type: String

The name of the job that this method will start.

```
   minutesFromNow
```

Type: Integer

The time interval in minutes after which the job should start executing.

```
   scopeSize
```

Type: Integer

The number of records that should be passed to the batch `execute` method.

Return Value

Type: String

Usage

Note: Some things to note about `System.scheduleBatch` :

**•** When you call `System.scheduleBatch`, Salesforce schedules the job for execution at the specified time. Actual execution
occurs at or after that time, depending on service availability.

**•** The scheduler runs as system—all classes are executed, whether the user has permission to execute the class or not.

**•** When the job’s schedule is triggered, the system queues the batch job for processing. If Apex flex queue is enabled in your
org, the batch job is added at the end of the flex queue. For more information, see Holding Batch Jobs in the Apex Flex Queue.

**•** All scheduled Apex limits apply for batch jobs scheduled using `System.scheduleBatch` . After the batch job is queued
(with a status of `Holding` or `Queued` ), all batch job limits apply and the job no longer counts toward scheduled Apex
limits.

**•** After calling this method and before the batch job starts, you can use the returned scheduled job ID to abort the scheduled
job using the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

For an example, see Using the `[System.scheduleBatch](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)` Method.

##### setPassword(userId, password)

Sets the password for the specified user.

Signature

```
   public static Void setPassword(ID userId, String password)

```


Apex Reference Guide System Class

Parameters

```
   userId
```

Type: ID

```
   password
```

Type: String

Return Value

Type: Void

Usage

**•** If a security question hasn't been previously configured, a user who logs in with a new password that was set using `setPassword()`
is redirected to the "Change Your Password" page.

**•** Use `resetPassword(userId, sendUserEmail)` if you want the user to go through the reset process and create their
own password.

Warning: Be careful with this method, and don’t expose this functionality to end users.

##### submit(workItemIds, comments, nextApprover)

Submits the processed approvals. The current user is the submitter and the entry criteria is evaluated for all processes applicable to the
current user.

Signature

```
   public static List<ID> submit(List<ID> workItemIds, String comments, String nextApprover)

```

Parameters

```
   workItemIds
```

Type: List<ID>

```
   comments
```

Type: String

```
   nextApprover
```

Type: String

Return Value

Type: List<ID>

Usage

For enhanced submit and evaluation features, see the ProcessSubmitRequest class.

##### today()

Returns the current date in the current user's time zone.


### Apex Reference Guide Test Class

Signature

```
   public static Date today()

```

Return Value

Type: Date

### Test Class

Contains methods related to Apex tests.

Namespace

System

#### Test Methods

### The following are methods for Test . All methods are static.

IN THIS SECTION:

calculatePermissionSetGroup(psgIds)
Calculates aggregate permissions in specified permission set groups for testing.

calculatePermissionSetGroup(psgId)
Calculates aggregate permissions in a specified permission set group for testing.

clearApexPageMessages()
Clear the messages on a Visualforce page while executing Apex test methods.

createSoqlStub(targetType, soqlStub)
Creates a stub that will respond to SOQL queries against the specified SObject type you can use during testing.

createStub(parentType, stubProvider)
Creates a stubbed version of an Apex class that you can use for testing. This method is part of the Apex stub API. You can use it with
the `System.StubProvider` interface to create a mocking framework.

createStubQueryRow(targetType, fieldMapWithRelationshipKeys)
Creates an instance of a stubbed SObject type that you can use to provide testing results in the extended
`System.SoqlStubProvider` class.

createStubQueryRows(targetType, fieldMapWithRelationshipKeysForMultipleRows)
Creates instances of stubbed SObject types that you can use to provide testing results in the extended
`System.SoqlStubProvider` class.

enableChangeDataCapture()
Use this method in an Apex test so that change event notifications are generated for all supported Change Data Capture entities.
Call this method at the beginning of your test before performing DML operations and calling
`Test.getEventBus().deliver();` .


Apex Reference Guide Test Class

enqueueBatchJobs(numberOfJobs)
Adds the specified number of jobs with no-operation contents to the test-context queue. It first fills the test batch queue, up to the
maximum 5 jobs, and then places jobs in the test flex queue. It throws a limit exception when the number of jobs in the test flex
queue exceeds the allowed limit of 100 jobs.

getEventBus()
Returns an instance of the test event bus broker, which lets you operate on platform event or change event messages in an Apex
test. For example, you can call `Test.getEventBus().deliver()` to deliver event messages.

getFlexQueueOrder()
Returns an ordered list of job IDs for jobs in the test-context flex queue. The job at index `0` is the next job slated to run. This method
returns only test-context results, even if it’s annotated with `@IsTest(SeeAllData=true)` .

getStandardPricebookId()
Returns the ID of the standard price book in the organization.

invokeContinuationMethod(controller, request)
Invokes the callback method for the specified controller and continuation in a test method.

isRunningTest()
Returns `true` if the currently executing code was called by code contained in a test method, `false` otherwise. Use this method
if you need to run different code depending on whether it was being called from a test.

isSoqlStubDefined(targetType)
Returns `true` if a SOQL stub is defined for an SObject type; otherwise returns `false` .

loadData(sObjectToken, resourceName)
Inserts test records from the specified static resource .csv file and for the specified sObject type, and returns a list of the inserted
sObjects.

testNotificationActionHandler (handler, actionableNotification)
Tests a notification action handler implementation by simulating the execution of an action for a specific notification.

newSendEmailQuickActionDefaults(contextId, replyToId)
Creates a new QuickAction.SendEmailQuickActionDefaults instance for testing a class implementing the
QuickAction.QuickActionDefaultsHandler interface.

setContinuationResponse(requestLabel, mockResponse)
Sets a mock response for a continuation HTTP request in a test method.

setCreatedDate(recordId, createdDatetime)
Sets `CreatedDate` for a test-context sObject.

setCurrentPage(page)
A Visualforce test method that sets the current PageReference for the controller.

setCurrentPageReference(page)
A Visualforce test method that sets the current PageReference for the controller.

setFixedSearchResults(fixedSearchResults)
Defines a list of fixed search results to be returned by all subsequent SOSL statements in a test method.

setMock(interfaceType, instance)
Sets the response mock mode and instructs the Apex runtime to send a mock response whenever a callout is made through the
HTTP classes or the auto-generated code from WSDLs.


Apex Reference Guide Test Class

setReadOnlyApplicationMode(applicationMode)
Sets the application mode for an organization to read-only in an Apex test to simulate read-only mode during Salesforce upgrades
and downtimes. The application mode is reset to the default mode at the end of each Apex test run.

startTest()
Marks the point in your test code when your test actually begins. Use this method when you are testing governor limits.

stopTest()
Marks the point in your test code when your test ends. Use this method in conjunction with the `startTest` method.

testInstall(installImplementation, version, isPush)
Tests the implementation of the InstallHandler interface, which is used for specifying a post install script in packages. Tests run as
the test initiator in the development environment.

testSandboxPostCopyScript(script, organizationId, sandboxId, sandboxName)
Tests the implementation of the SandboxPostCopy Interface, which is used for specifying a script to run at the completion of a
Sandbox copy. Tests run as the test initiator in the development environment.

testSandboxPostCopyScript(script, organizationId, sandboxId, sandboxName, RunAsAutoProcUser)
Tests the implementation of the SandboxPostCopy Interface, which is used for specifying a script to run at the completion of a
Sandbox copy. When `RunAsAutoProcUser` is `true`, tests run as Automated Process user in the development environment.

testUninstall(uninstallImplementation)
Tests the implementation of the UninstallHandler interface, which is used for specifying an uninstall script in packages. Tests run as
the test initiator in the development environment.

##### **`calculatePermissionSetGroup(psgIds)`**

Calculates aggregate permissions in specified permission set groups for testing.

Signature

```
   public static void calculatePermissionSetGroup(List<String> psgIds)

```

Parameters

```
   psgIds
```

Type: List<String>

A list of IDs for permission set groups.

Return Value

Type: void

##### **`calculatePermissionSetGroup(psgId)`**

Calculates aggregate permissions in a specified permission set group for testing.

Signature

```
   public static void calculatePermissionSetGroup(String psgId)

```


Apex Reference Guide Test Class

Parameters

```
   psgId
```

Type: String

A single ID for a specified permission set group.

Return Value

Type: void

##### clearApexPageMessages()

Clear the messages on a Visualforce page while executing Apex test methods.

Signature

```
   public static void clearApexPageMessages()

```

Return Value

Type: void

Usage

This method may only be used in tests.

Example:

```
        @isTest

        static void clearMessagesTest() {

           Test.setCurrentPage(new PageReference('/'));

           ApexPages.addMessage(

             new ApexPages.Message(ApexPages.Severity.WARNING, 'Sample Warning')

           );

           System.assertEquals(1, ApexPages.getMessages().size());

           Test.clearApexPageMessages();

           System.assertEquals(0, ApexPages.getMessages().size());

        }

##### **`createSoqlStub(targetType, soqlStub)`**

```

Creates a stub that will respond to SOQL queries against the specified SObject type you can use during testing.

Signature

```
   public static void createSoqlStub(Schema.SObjectType targetType, System.SoqlStubProvider

   soqlStub)

```


Apex Reference Guide Test Class

Parameters

```
   targetType
```

Type: Schema.SObjectType

The SObject type to be stubbed. This parameter can’t be null.

```
   soqlStub
```

Type: System.SoqlStubProvider

An implementation of the `SoqlStubProvider` abstract class.

Return Value

Type: void

SEE ALSO:

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)

##### createStub(parentType, stubProvider)

Creates a stubbed version of an Apex class that you can use for testing. This method is part of the Apex stub API. You can use it with the
`System.StubProvider` interface to create a mocking framework.

Signature

```
   public static Object createStub(System.Type parentType, System.StubProvider stubProvider)

```

Parameters

```
   parentType
```

Type: System.Type

The type of the Apex class to be stubbed.

```
   stubProvider
```

System.StubProvider

An implementation of the `StubProvider` interface.

Return Value

Type: Object

Returns the stubbed object to use in testing.

Usage

The `createStub()` method works together with the `System.StubProvider` interface. You define the behavior of the stubbed
object by implementing the `StubProvider` interface. Then you create a stubbed object using the `createStub()` method.


Apex Reference Guide Test Class

When you invoke methods on the stubbed object, the `handleMethodCall()` method of the `StubProvider` interface is called
to perform the behavior of the stubbed method.

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

##### **`createStubQueryRow(targetType, fieldMapWithRelationshipKeys)`**

Creates an instance of a stubbed SObject type that you can use to provide testing results in the extended
`System.SoqlStubProvider` class.

Signature

```
   public static SObject createStubQueryRow(Schema.SObjectType targetType,

   Map<String,Object> fieldMapWithRelationshipKeys)

```

Parameters

```
   targetType
```

Type: Schema.SObjectType

The SObject type to be stubbed. This parameter can’t be null.

```
   fieldMapWithRelationshipKeys
```

Type: Map<String,Object>

The map contains the fields for a parent entity, keyed by the field name with a value for each field. Key and value pairs can also be
used for an aggregate relationship. The key holds the name of the aggregate relationship and the value is a list of SObjects.

Return Value

Type: SObject

Returns the stubbed SObject to use in testing.

Example

```
   ssot__EmailEngagement__dlm engagement =

   (ssot__EmailEngagement__dlm)Test.createStubQueryRow(ssot__EmailEngagement__dlm.SObjectType,

      new Map<string, object> {

        'ssot__Name__c' => 'My Email Engagement',

        'ssot__CityName__c' => 'San Francisco'

      }

   );

```

SEE ALSO:

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)


Apex Reference Guide Test Class

##### **`createStubQueryRows(targetType, fieldMapWithRelationshipKeysForMultipleRows)`**

Creates instances of stubbed SObject types that you can use to provide testing results in the extended `System.SoqlStubProvider`
class.

Signature

```
   public static List<SObject> createStubQueryRows(Schema.SObjectType targetType,

   List<Map<String,Object>> fieldMapWithRelationshipKeysForMultipleRows)

```

Parameters

```
   targetType
```

Type: Schema.SObjectType

The SObject type to be stubbed. This parameter can’t be null.

```
   fieldMapWithRelationshipKeysForMultipleRows
```

Type: List<Map<String,Object>>

The list of maps containing the fields for a parent entity, keyed by the field name with a value for each field. Key and value pairs can
also be used for an aggregate relationship used in the query. The key holds the name of the aggregate relationship and the value
is a list of SObjects.

Return Value

Type: List<SObject>

Returns a list of stubbed SObject types to use in testing.

Example

```
   List<Map<String, Object>> engagementMaps = new List<Map<String, Object>>();

   Map<String, Object> engagement = new Map<String, Object> {

        'ssot__Name__c' => 'My Email Engagement',

        'ssot__CityName__c' => 'San Francisco'

   };

   Map<String, Object> engagement2 = new Map<String, Object> {

        'ssot__Name__c' => 'My Other Email Engagement',

        'ssot__CityName__c' => 'New York'

   };

   engagementMaps.add(engagement);

   engagementMaps.add(engagement2);

   List<ssot__EmailEngagement__dlm> engagements =

   (List<ssot__EmailEngagement__dlm>)Test.createStubQueryRows(ssot__EmailEngagement__dlm.SObjectType,

      engagementMaps);

```

SEE ALSO:

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)


Apex Reference Guide Test Class

##### enableChangeDataCapture()

Use this method in an Apex test so that change event notifications are generated for all supported Change Data Capture entities. Call
this method at the beginning of your test before performing DML operations and calling `Test.getEventBus().deliver();` .

Signature

```
   public static void enableChangeDataCapture()

```

Return Value

Type: void

Usage

##### The enableChangeDataCapture() method ensures that Apex tests can fire change event triggers regardless of the entities selected in Setup in the Change Data Capture page. The enableChangeDataCapture() method doesn’t affect the entities

selected in Setup.

SEE ALSO:

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.change_data_capture.meta/change_data_capture/cdc_intro.htm)_

##### enqueueBatchJobs(numberOfJobs)

Adds the specified number of jobs with no-operation contents to the test-context queue. It first fills the test batch queue, up to the
maximum 5 jobs, and then places jobs in the test flex queue. It throws a limit exception when the number of jobs in the test flex queue
exceeds the allowed limit of 100 jobs.

Signature

```
   public static List<Id> enqueueBatchJobs(Integer numberOfJobs)

```

Parameters

```
   numberOfJobs
```

Type: Integer

Number of test jobs to enqueue.

Return Value

Type: List<Id>

A list of IDs of enqueued test jobs.

Usage

Use this method to reduce testing time. Instead of using your org's real batch jobs for testing, you can use this method to simulate
##### batch-job enqueueing. Using enqueueBatchJobs(numberOfJobs) is faster than enqueuing real batch jobs.


Apex Reference Guide Test Class

##### getEventBus()

Returns an instance of the test event bus broker, which lets you operate on platform event or change event messages in an Apex test.
For example, you can call `Test.getEventBus().deliver()` to deliver event messages.

Signature

```
   public static EventBus.TestBroker getEventBus()

```

Return Value

Type: EventBus.TestBroker

A broker for the test event bus.

Usage

Enclose `Test.getEventBus().deliver()` within the `Test.startTest()` and `Test.stopTest()` statement block.

```
   Test.startTest();

   // Create test events

   // ...

   // Publish test events with EventBus.publish()

   // ...

   // Deliver test events

   Test.getEventBus().deliver();

   // Perform validation

   // ...

   Test.stopTest();

```

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_

##### getFlexQueueOrder()

Returns an ordered list of job IDs for jobs in the test-context flex queue. The job at index `0` is the next job slated to run. This method
returns only test-context results, even if it’s annotated with `@IsTest(SeeAllData=true)` .

Signature

```
   public static List<Id> getFlexQueueOrder()

```

Return Value

Type: List<Id>

An ordered list of IDs of the jobs in the test’s flex queue.

##### getStandardPricebookId()

Returns the ID of the standard price book in the organization.


Apex Reference Guide Test Class

Signature

```
   public static Id getStandardPricebookId()

```

Return Value

Type: Id

The ID of the standard price book.

Usage

This method returns the ID of the standard price book in your organization regardless of whether the test can query organization data.
By default, tests can’t query organization data unless they’re annotated with `@isTest(SeeAllData=true)` .

Creating price book entries with a standard price requires the ID of the standard price book. Use this method to get the standard price
book ID so that you can create price book entries in your tests.

Example

This example creates some test data for price book entries. The test method in this example gets the standard price book ID and uses
this ID to create a price book entry for a product with a standard price. Next, the test creates a custom price book and uses the ID of this
custom price book to add a price book entry with a custom price.

```
   @isTest

   public class PriceBookTest {

      // Utility method that can be called by Apex tests to create price book entries.

      static testmethod void addPricebookEntries() {

        // First, set up test price book entries.

        // Insert a test product.

        Product2 prod = new Product2(Name = 'Laptop X200',

           Family = 'Hardware');

        insert prod;

        // Get standard price book ID.

        // This is available irrespective of the state of SeeAllData.

        Id pricebookId = Test.getStandardPricebookId();

        // 1. Insert a price book entry for the standard price book.

        // Standard price book entries require the standard price book ID we got earlier.

        PricebookEntry standardPrice = new PricebookEntry(

           Pricebook2Id = pricebookId, Product2Id = prod.Id,

           UnitPrice = 10000, IsActive = true);

        insert standardPrice;

        // Create a custom price book

        Pricebook2 customPB = new Pricebook2(Name='Custom Pricebook', isActive=true);

        insert customPB;

        // 2. Insert a price book entry with a custom price.

        PricebookEntry customPrice = new PricebookEntry(

           Pricebook2Id = customPB.Id, Product2Id = prod.Id,

           UnitPrice = 12000, IsActive = true);

        insert customPrice;

```


Apex Reference Guide Test Class

```
        // Next, perform some tests with your test price book entries.

      }

   }

##### invokeContinuationMethod(controller, request)

```

Invokes the callback method for the specified controller and continuation in a test method.

Signature

```
   public static Object invokeContinuationMethod(Object controller, Continuation request)

```

Parameters

```
   controller
```

Type: Object

An instance of the controller class that invokes the continuation request.

```
   request
```

Type: Continuation

The continuation that is returned by an action method in the controller class.

Return Value

Type: Object

The response of the continuation callback method.

Usage

Use the `Test.setContinuationResponse` and `Test.invokeContinuationMethod` methods to test continuations.
In test context, callouts of continuations aren’t sent to the external service. By using these methods, you can set a mock response and
cause the runtime to call the continuation callback method to process the mock response.

Call `Test.setContinuationResponse` before you call `Test.invokeContinuationMethod` . When you call
`Test.invokeContinuationMethod`, the runtime executes the callback method that is associated with the continuation. The
callback method processes the mock response that is set by `Test.setContinuationResponse` .

##### isRunningTest()

Returns `true` if the currently executing code was called by code contained in a test method, `false` otherwise. Use this method if
you need to run different code depending on whether it was being called from a test.

Signature

```
   public static Boolean isRunningTest()

```

Return Value

Type: Boolean


Apex Reference Guide Test Class

##### **`isSoqlStubDefined(targetType)`**

Returns `true` if a SOQL stub is defined for an SObject type; otherwise returns `false` .

Signature

```
   public static Boolean isSoqlStubDefined(Schema.SObjectType targetType)

```

Parameters

```
   targetType
```

Type: Schema.SObjectType

The SObject type to check. This parameter can’t be null.

Return Value

Type: Boolean

##### loadData(sObjectToken, resourceName)

Inserts test records from the specified static resource .csv file and for the specified sObject type, and returns a list of the inserted sObjects.

Signature

```
   public static List<sObject> loadData(Schema.SObjectType sObjectToken, String

   resourceName)

```

Parameters

```
   sObjectToken
```

Type: Schema.SObjectType

The sObject type for which to insert test records.

```
   resourceName
```

Type: String

The static resource that corresponds to the .csv file containing the test records to load. The name is case insensitive.

Return Value

Type: List<sObject>

Usage

You must create the static resource prior to calling this method. The static resource is a comma-delimited file ending with a .csv extension.
The file contains field names and values for the test records. The first line of the file must contain the field names and subsequent lines
are the field values. To learn more about static resources, see “Defining Static Resources” in the Salesforce online help.

Once you create a static resource for your .csv file, the static resource will be assigned a MIME type. Supported MIME types are:

**•** text/csv

**•** application/vnd.ms-excel


Apex Reference Guide Test Class

**•** application/octet-stream

**•** text/plain

##### testNotificationActionHandler (handler, actionableNotification)

Tests a notification action handler implementation by simulating the execution of an action for a specific notification.

Signature

```
   public static Messaging.ActionResult testNotificationActionHandler(

      Messaging.NotificationActionHandler handler,

      Messaging.ActionableNotification actionableNotification

   )

```

Return Value

Type: `Messaging.ActionResult`

The result object generated by the handler, typically containing success status and any relevant error messages or return data.

Usage

This method allows you to perform unit tests on custom notification logic without needing to trigger an actual push notification through
the platform. Use this in conjunction with `Assert` methods to verify that your handler processes inputs correctly and returns the
expected `ActionResult` .

##### Example: The following example demonstrates how to use testNotificationActionHandler to verify a custom

handler named `LeadAssignmentHandler` .

```
      @IsTest

      private with sharing class NotificationHandlerTest {

        @IsTest

        static void testNotificationSuccess() {

           // 1. Initialize your custom handler

           Messaging.NotificationActionHandler myHandler = new LeadAssignmentHandler();

           // 2. Set up the mock ActionableNotification

           Messaging.ActionableNotification mockNotification = new

      Messaging.ActionableNotification();

           // Assume 'AcceptLead' is a valid action ID for your handler logic

           mockNotification.setActionId('AcceptLead');

           // 3. Invoke the test method

           Test.startTest();

           Messaging.ActionResult result = Messaging.testNotificationActionHandler(

             myHandler,

             mockNotification

           );

           Test.stopTest();

           // 4. Verify the results

```


Apex Reference Guide Test Class

```
           Assert.isNotNull(result, 'The result should not be null.');

           Assert.isTrue(result.isSuccess(), 'The action should have succeeded.');

        }

      }

##### newSendEmailQuickActionDefaults(contextId, replyToId)

```

Creates a new QuickAction.SendEmailQuickActionDefaults instance for testing a class implementing the
QuickAction.QuickActionDefaultsHandler interface.

Signature

```
   public static QuickAction.SendEmailQuickActionDefaults newSendEmailQuickActionDefaults(ID

   contextId, ID replyToId)

```

Parameters

```
   contextId
```

Type: Id

Parent record of the email message.

```
   replyToId
```

Type: Id

Previous email message ID if this email message is a reply.

Return Value

Type: SendEmailQuickActionDefaults Class

The default values used for an email message quick action.

##### setContinuationResponse(requestLabel, mockResponse)

Sets a mock response for a continuation HTTP request in a test method.

Signature

```
   public static void setContinuationResponse(String requestLabel, System.HttpResponse

   mockResponse)

```

Parameters

```
   requestLabel
```

Type: String

The unique label that corresponds to the continuation HTTP request. This label is returned by
`Continuation.addHttpRequest` .

```
   mockResponse
```

Type: HttpResponse

The fake response to be returned by `Test.invokeContinuationMethod` .


Apex Reference Guide Test Class

Return Value

Type: void

Usage

Use the `Test.setContinuationResponse` and `Test.invokeContinuationMethod` methods to test continuations.
In test context, callouts of continuations aren’t sent to the external service. By using these methods, you can set a mock response and
cause the runtime to call the continuation callback method to process the mock response.

Call `Test.setContinuationResponse` before you call `Test.invokeContinuationMethod` . When you call
`Test.invokeContinuationMethod`, the runtime executes the callback method that is associated with the continuation. The
callback method processes the mock response that is set by `Test.setContinuationResponse` .

##### setCreatedDate(recordId, createdDatetime)

Sets `CreatedDate` for a test-context sObject.

Signature

```
   public static void setCreatedDate(Id recordId, Datetime createdDatetime)

```

Parameters

```
   recordId
```

Type: Id

The ID of an sObject.

```
   createdDatetime
```

Type: Datetime

The value to assign to the sObject’s `CreatedDate` field.

Return Value

Type: void

Usage

All database changes are rolled back at the end of a test. You can’t use this method on records that existed before your test executed.
##### You also can’t use setCreatedDate in methods annotated with @isTest(SeeAllData=true), because those methods

have access to all data in your org. If you set `CreatedDate` to a future value, it can cause unexpected results. This method takes two
parameters—an sObject ID and a Datetime value—neither of which can be null.

Insert your test record before you set its `CreatedDate`, as shown in this example.

```
   @isTest

   private class SetCreatedDateTest {

      static testMethod void testSetCreatedDate() {

        Account a = new Account(name='myAccount');

        insert a;

        Test.setCreatedDate(a.Id, DateTime.newInstance(2012,12,12));

        Test.startTest();

        Account myAccount = [SELECT Id, Name, CreatedDate FROM Account

```


Apex Reference Guide Test Class

```
                     WHERE Name ='myAccount' limit 1];

        System.assertEquals(myAccount.CreatedDate, DateTime.newInstance(2012,12,12));

        Test.stopTest();

      }

   }

##### setCurrentPage(page)

```

A Visualforce test method that sets the current PageReference for the controller.

Signature

```
   public static Void setCurrentPage(PageReference page)

```

Parameters

```
   page
```

Type: System.PageReference

Return Value

Type: Void

##### setCurrentPageReference(page)

A Visualforce test method that sets the current PageReference for the controller.

Signature

```
   public static Void setCurrentPageReference(PageReference page)

```

Parameters

```
   page
```

Type: System.PageReference

Return Value

Type: Void

##### setFixedSearchResults(fixedSearchResults)

Defines a list of fixed search results to be returned by all subsequent SOSL statements in a test method.

Signature

```
   public static Void setFixedSearchResults(ID[] fixedSearchResults)

```


Apex Reference Guide Test Class

Parameters

```
   fixedSearchResults
```

Type: ID[]

The list of record IDs specified by _`opt_set_search_results`_ replaces the results that would normally be returned by the
SOSL queries if they were not subject to any `WHERE` or `LIMIT` clauses. If these clauses exist in the SOSL queries, they are applied
to the list of fixed search results.

Return Value

Type: Void

Usage

If _`opt_set_search_results`_ is not specified, all subsequent SOSL queries return no results.

[For more information, see Dynamic SOSL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_SOSL.htm)

##### setMock(interfaceType, instance)

Sets the response mock mode and instructs the Apex runtime to send a mock response whenever a callout is made through the HTTP
classes or the auto-generated code from WSDLs.

Signature

```
   public static Void setMock(Type interfaceType, Object instance)

```

Parameters

```
   interfaceType
```

Type: System.Type

```
   instance
```

Type: Object

Return Value

Type: Void

Usage

Note: To mock a callout if the code that performs the callout is in a managed package, call `Test.setMock` from a test method
in the same package with the same namespace.

##### setReadOnlyApplicationMode(applicationMode)

Sets the application mode for an organization to read-only in an Apex test to simulate read-only mode during Salesforce upgrades and
downtimes. The application mode is reset to the default mode at the end of each Apex test run.

Signature

```
   public static Void setReadOnlyApplicationMode(Boolean applicationMode)

```


Apex Reference Guide Test Class

Parameters

```
   applicationMode
```

Type: Boolean

Return Value

Type: Void

Usage

Also see the `getApplicationReadWriteMode()` System method.

Do not use `setReadOnlyApplicationMode` for purposes unrelated to Read-Only Mode testing, such as simulating DML
exceptions.

Example

The following example sets the application mode to read-only and attempts to insert a new account record, which results in the exception.
It then resets the application mode and performs a successful insert.

```
   @isTest

   private class ApplicationReadOnlyModeTestClass {

     public static testmethod void test() {

      // Create a test account that is used for querying later.

      Account testAccount = new Account(Name = 'TestAccount');

      insert testAccount;

      // Set the application read only mode.

      Test.setReadOnlyApplicationMode(true);

      // Verify that the application is in read-only mode.

      System.assertEquals(

            ApplicationReadWriteMode.READ_ONLY,

            System.getApplicationReadWriteMode());

      // Create a new account object.

      Account testAccount2 = new Account(Name = 'TestAccount2');

      try {

       // Get the test account created earlier. Should be successful.

       Account testAccountFromDb =

        [SELECT Id, Name FROM Account WHERE Name = 'TestAccount'];

       System.assertEquals(testAccount.Id, testAccountFromDb.Id);

       // Inserts should result in the InvalidReadOnlyUserDmlException

       // being thrown.

       insert testAccount2;

       System.assertEquals(false, true);

      } catch (System.InvalidReadOnlyUserDmlException e) {

       // Expected

      }

      // Insertion should work after read only application mode gets disabled.

      Test.setReadOnlyApplicationMode(false);

```


Apex Reference Guide Test Class

```
      insert testAccount2;

      Account testAccount2FromDb =

        [SELECT Id, Name FROM Account WHERE Name = 'TestAccount2'];

      System.assertEquals(testAccount2.Id, testAccount2FromDb.Id);

     }

   }

##### startTest()

```

Marks the point in your test code when your test actually begins. Use this method when you are testing governor limits.

Signature

```
   public static Void startTest()

```

Return Value

Type: Void

Usage

##### You can also use this method with stopTest to ensure that all asynchronous calls that come after the startTest method are

run before doing any assertions or testing. Each test method is allowed to call this method only once. All of the code before this method
should be used to initialize variables, populate data structures, and so on, allowing you to set up everything you need to run your test.
##### Any code that executes after the call to startTest and before stopTest is assigned a new set of governor limits. stopTest() Marks the point in your test code when your test ends. Use this method in conjunction with the startTest method.

Signature

```
   public static Void stopTest()

```

Return Value

Type: Void

Usage

##### Each test method is allowed to call this method only once. Any code that executes after the stopTest method is assigned the original limits that were in effect before startTest was called. All asynchronous calls made after the startTest method are collected by the system. When stopTest is executed, all asynchronous processes are run synchronously. Note: Asynchronous calls, such as @future or executeBatch, called in a startTest, stopTest block, do not count

against your limits for the number of queued jobs.

##### testInstall(installImplementation, version, isPush)

Tests the implementation of the InstallHandler interface, which is used for specifying a post install script in packages. Tests run as the
test initiator in the development environment.


Apex Reference Guide Test Class

Signature

```
   public static Void testInstall(InstallHandler installImplementation, Version version,

   Boolean isPush)

```

Parameters

```
   installImplementation
```

Type: System.InstallHandler

A class that implements the `InstallHandler` interface.

```
   version
```

Type: System.Version

The version number of the existing package installed in the subscriber organization.

```
   isPush
```

Type: Boolean

(Optional) Specifies whether the upgrade is a push. The default value is `false` .

Return Value

Type: Void

Usage

This method throws a run-time exception if the test install fails.

Example

```
   @isTest static void test() {

     PostInstallClass postinstall =

      new PostInstallClass();

      Test.testInstall(postinstall,

       new Version(1,0));

     }

##### testSandboxPostCopyScript(script, organizationId, sandboxId, sandboxName)

```

Tests the implementation of the SandboxPostCopy Interface, which is used for specifying a script to run at the completion of a Sandbox
copy. Tests run as the test initiator in the development environment.

Signature

```
   public static void testSandboxPostCopyScript(System.SandboxPostCopy script, Id

   organizationId, Id sandboxId, String sandboxName)

```

Parameters

```
   script
```

Type: System.SandboxPostCopy

A class that implements the `SandboxPostCopy` interface.


Apex Reference Guide Test Class

```
   organizationId
```

Type: Id

The sandbox organization ID

```
   sandboxId
```

Type: Id

The sandbox ID to be provided to the SandboxPostCopy script.

```
   sandboxName
```

Type: String

The sandbox name to be provided to the SandboxPostCopy script.

Return Value

Type: void

Usage

This method throws a run-time exception if the test install fails.

##### Note: Salesforce recommends that you use the testSandboxPostCopyScript(script, organizationId,

`sandboxId, sandboxName, isRunAsAutoProcUser)` overload instead of this method. When

`isRunAsAutoProcUser` is `true`, the `SandboxPostCopy` script is tested with the same user access permissions as
used by post-copy tasks during sandbox creation. Using the same permissions enables the test to better simulate the actual usage
of the class, and to uncover potential issues.

Example

See SandboxPostCopy Example Implementation

##### **`testSandboxPostCopyScript(script, organizationId, sandboxId, sandboxName,`**

```
  RunAsAutoProcUser)

```

Tests the implementation of the SandboxPostCopy Interface, which is used for specifying a script to run at the completion of a Sandbox
copy. When `RunAsAutoProcUser` is `true`, tests run as Automated Process user in the development environment.

Signature

```
   public static void testSandboxPostCopyScript(System.SandboxPostCopy script, Id

   organizationId, Id sandboxId, String sandboxName, Boolean RunAsAutoProcUser)

```

Parameters

```
   script
```

Type: System.SandboxPostCopy

A class that implements the `SandboxPostCopy` interface.

```
   organizationId
```

Type: Id

The sandbox organization ID.


Apex Reference Guide Test Class

```
   sandboxId
```

Type: Id

The sandbox ID to be provided to the SandboxPostCopy script.

```
   sandboxName
```

Type: String

The sandbox name to be provided to the SandboxPostCopy script.

```
   RunAsAutoProcUser
```

Type: Boolean

When `true`, the `SandboxPostCopy` script is tested with the same user access permissions as used by post-copy tasks during
sandbox creation. Using the same permissions enables the test to better simulate the actual usage of the class, and to uncover
potential issues.

When `false`, the test runs as the test initiator. This option can alter the permissions with which the script is tested, such as the
ability to access objects and features.

Return Value

Type: void

Usage

This method throws a run-time exception if the test install fails.

Example

See SandboxPostCopy Example Implementation

##### testUninstall(uninstallImplementation)

Tests the implementation of the UninstallHandler interface, which is used for specifying an uninstall script in packages. Tests run as the
test initiator in the development environment.

Signature

```
   public static Void testUninstall(UninstallHandler uninstallImplementation)

```

Parameters

```
   uninstallImplementation
```

Type: System.UninstallHandler

A class that implements the `UninstallHandler` interface.

Return Value

Type: Void

Usage

This method throws a run-time exception if the test uninstall fails.


### Apex Reference Guide Time Class

Example

```
   @isTest static void test() {

     UninstallClass uninstall =

      new UninstallClass();

      Test.testUninstall(uninstall);

     }

### Time Class

```

Contains methods for the Time primitive data type.

Namespace

System

Usage

[For more information on time, see Time Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Time Methods

### The following are methods for Time .

IN THIS SECTION:

addHours(additionalHours)
Adds the specified number of hours to a Time.

addMilliseconds(additionalMilliseconds)
Adds the specified number of milliseconds to a Time.

addMinutes(additionalMinutes)
Adds the specified number of minutes to a Time.

addSeconds(additionalSeconds)
Adds the specified number of seconds to a Time.

hour()
Returns the hour component of a Time.

millisecond()
Returns the millisecond component of a Time.

minute()
Returns the minute component of a Time.

newInstance(hour, minutes, seconds, milliseconds)
Constructs a Time from Integer representations of the specified hour, minutes, seconds, and milliseconds. (UTC is assumed.)

second()
Returns the second component of a Time.


Apex Reference Guide Time Class

##### addHours(additionalHours)

Adds the specified number of hours to a Time.

Signature

```
   public Time addHours(Integer additionalHours)

```

Parameters

```
   additionalHours
```

Type: Integer

Return Value

Type: Time

Example

```
   Time myTime = Time.newInstance(1, 2, 3, 4);

   Time expected = Time.newInstance(4, 2, 3, 4);

   System.assertEquals(expected, myTime.addHours(3));

##### addMilliseconds(additionalMilliseconds)

```

Adds the specified number of milliseconds to a Time.

Signature

```
   public Time addMilliseconds(Integer additionalMilliseconds)

```

Parameters

```
   additionalMilliseconds
```

Type: Integer

Return Value

Type: Time

Example

```
   Time myTime = Time.newInstance(1, 2, 3, 0);

   Time expected = Time.newInstance(1, 2, 4, 400);

   System.assertEquals(expected, myTime.addMilliseconds(1400));

##### addMinutes(additionalMinutes)

```

Adds the specified number of minutes to a Time.


Apex Reference Guide Time Class

Signature

```
   public Time addMinutes(Integer additionalMinutes)

```

Parameters

```
   additionalMinutes
```

Type: Integer

Return Value

Type: Time

Example

```
   Time myTime = Time.newInstance(18, 30, 2, 20);

   Integer myMinutes = myTime.minute();

   myMinutes = myMinutes + 5;

   System.assertEquals(myMinutes, 35);

##### addSeconds(additionalSeconds)

```

Adds the specified number of seconds to a Time.

Signature

```
   public Time addSeconds(Integer additionalSeconds)

```

Parameters

```
   additionalSeconds
```

Type: Integer

Return Value

Type: Time

Example

```
   Time myTime = Time.newInstance(1, 2, 55, 0);

   Time expected = Time.newInstance(1, 3, 5, 0);

   System.assertEquals(expected, myTime.addSeconds(10));

##### hour()

```

Returns the hour component of a Time.

Signature

```
   public Integer hour()

```


Apex Reference Guide Time Class

Return Value

Type: Integer

Example

```
   Time myTime = Time.newInstance(18, 30, 2, 20);

   myTime = myTime.addHours(2);

   Integer myHour = myTime.hour();

   System.assertEquals(myHour, 20);

##### millisecond()

```

Returns the millisecond component of a Time.

Signature

```
   public Integer millisecond()

```

Return Value

Type: Integer

Example

```
   Time myTime = Time.newInstance(3, 14, 15, 926);

   System.assertEquals(926, myTime.millisecond());

##### minute()

```

Returns the minute component of a Time.

Signature

```
   public Integer minute()

```

Return Value

Type: Integer

Example

```
   Time myTime = Time.newInstance(3, 14, 15, 926);

   System.assertEquals(14, myTime.minute());

##### newInstance(hour, minutes, seconds, milliseconds)

```

Constructs a Time from Integer representations of the specified hour, minutes, seconds, and milliseconds. (UTC is assumed.)


### Apex Reference Guide TimeZone Class

Signature

```
   public static Time newInstance(Integer hour, Integer minutes, Integer seconds, Integer

   milliseconds)

```

Parameters

```
   hour
```

Type: Integer

```
   minutes
```

Type: Integer

```
   seconds
```

Type: Integer

```
   milliseconds
```

Type: Integer

Return Value

Type: Time

Example

The following example creates a time of 18:30:2:20 (UTC).

```
   Time myTime =

   Time.newInstance(18, 30, 2, 20);

##### second()

```

Returns the second component of a Time.

Signature

```
   public Integer second()

```

Return Value

Type: Integer

Example

```
   Time myTime = Time.newInstance(3, 14, 15, 926);

   System.assertEquals(15, myTime.second());

### TimeZone Class

```

Represents a time zone. Contains methods for creating a new time zone and obtaining time zone properties, such as the time zone ID,
offset, and display name.


Apex Reference Guide TimeZone Class

Namespace

System

Usage

You can use the methods in this class to get properties of a time zone, such as the properties of the time zone returned by
`UserInfo.getTimeZone`, or the time zone returned by `getTimeZone` of this class.

Example

This example shows how to get properties of the current user’s time zone and display them to the debug log. The output of the sample
varies based on the user's time zone.

```
   TimeZone tz = UserInfo.getTimeZone();

   System.debug('Display name: ' + tz.getDisplayName());

   System.debug('ID: ' + tz.getID());

   // During daylight saving time for the America/Los_Angeles time zone

   System.debug('Offset: ' + tz.getOffset(DateTime.newInstance(2012,10,23,12,0,0)));

   // Not during daylight saving time for the America/Los_Angeles time zone

   System.debug('Offset: ' + tz.getOffset(DateTime.newInstance(2012,11,23,12,0,0)));

   System.debug('String format: ' + tz.toString());

```

This second example shows how to create a time zone for the New York time zone and get the offset of this time zone to the GMT time
zone. The example uses two dates to get the offset from. One date is before DST (Daylight Saving Time), and one is after DST. In 2000,
DST ended on Sunday, October 29 for the New York time zone. Because the date occurs after DST ends, the offset on the first date is –5
hours to GMT. In 2012, DST ended on Sunday, November 4. Because the date is within DST, the offset on the second date is –4 hours.

```
   // Get the New York time zone

   Timezone tz = Timezone.getTimeZone('America/New_York');

   // Create a date before the 2007 shift of DST into November

   DateTime dtpre = DateTime.newInstanceGMT(2000, 11, 1, 0, 0, 0);

   system.debug(tz.getOffset(dtpre)); //-18000000 (= -5 hours = EST)

   // Create a date after the 2007 shift of DST into November

   DateTime dtpost = DateTime.newInstanceGMT(2012, 11, 1, 0, 0, 0);

   system.debug(tz.getOffset(dtpost)); //-14400000 (= -4 hours = EDT)

```

This next example is similar to the previous one except that it gets the offset around the boundary of DST. In 2014, DST ended on Sunday,
November 2 at 2:00 AM local time for the New York time zone. The first offset is obtained right before DST ends, and the second offset
is obtained right after DST ends. The dates are created by using the `DateTime.newInstanceGMT` method. This method expects
the passed-in date values to be based on the GMT time zone.

```
   // Get the New York time zone

   Timezone tz = Timezone.getTimeZone('America/New_York');

   // Before DST ends

   DateTime dtpre = DateTime.newInstanceGMT(2014, 11, 2, 5, 59, 59); //1:59:59AM local EDT

   system.debug(tz.getOffset(dtpre)); //-14400000 (= -4 hours = still on DST)

   // After DST ends

   DateTime dtpost = DateTime.newInstanceGMT(2014, 11, 2, 6, 0, 0); //1:00:00AM local EST

   system.debug(tz.getOffset(dtpost)); //-18000000 (= -5 hours = back one hour)

```


Apex Reference Guide TimeZone Class

#### TimeZone Methods The following are methods for TimeZone .

IN THIS SECTION:

##### getDisplayName()

Returns this time zone’s display name.

##### getID()

Returns this time zone’s ID.

##### getOffset(date)

Returns the time zone offset, in milliseconds, of the specified date to the GMT time zone.

getTimeZone(timeZoneIdString)
Returns the time zone corresponding to the specified time zone ID.

toString()
Returns the string representation of this time zone.

##### getDisplayName()

Returns this time zone’s display name.

Signature

```
   public String getDisplayName()

```

Return Value

Type: String

Versioned Behavior Changes

In API version 45.0 and later, getDisplayName displays Daylight Savings Time appropriately when daylight savings are in effect. For
example, British Summer Time is displayed for Europe/London and Pacific Daylight Time for America/Los_Angeles.

##### getID()

Returns this time zone’s ID.

Signature

```
   public String getID()

```

Return Value

Type: String

##### getOffset(date)

Returns the time zone offset, in milliseconds, of the specified date to the GMT time zone.


Apex Reference Guide TimeZone Class

Signature

```
   public Integer getOffset(Datetime date)

```

Parameters

```
   date
```

Type: Datetime

The _`date`_ argument is the date and time to evaluate.

Return Value

Type: Integer

Usage

Note: The returned offset is adjusted for daylight saving time if the _`date`_ argument falls within daylight saving time for this time
zone.

##### getTimeZone(timeZoneIdString)

Returns the time zone corresponding to the specified time zone ID.

Signature

```
   public static TimeZone getTimeZone(String timeZoneIdString)

```

Parameters

```
   timeZoneIdString
```

Type: String

The time zone values you can use for the _`Id`_ [argument are any valid time zone values that the Java TimeZone class supports.](http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html)

Return Value

Type: TimeZone

Example

```
   TimeZone tz = TimeZone.getTimeZone('America/Los_Angeles');

   String tzName = tz.getDisplayName();

   System.assert(tzName.equals('(GMT-08:00) Pacific Standard Time (America/Los_Angeles)') ||

            tzName.equals('(GMT-07:00) Pacific Daylight Time (America/Los_Angeles)'));

##### toString()

```

Returns the string representation of this time zone.


### Apex Reference Guide Trigger Class

Signature

```
   public String toString()

```

Return Value

Type: String

### Trigger Class Use the Trigger class to access run-time context information in a trigger, such as the type of trigger or the list of sObject records

that the trigger operates on.

Namespace

System

Trigger Context Variables

### The Trigger class provides the following context variables.

**Variable** **Usage**

`isExecuting` Returns `true` if the current context for the Apex code is a trigger, not a Visualforce page, a web
service, or an `executeanonymous()` API call.

`isInsert` Returns `true` if this trigger was fired due to an insert operation, from the Salesforce user interface,
Apex, or the API.

`isUpdate` Returns `true` if this trigger was fired due to an update operation, from the Salesforce user interface,
Apex, or the API.

`isDelete` Returns `true` if this trigger was fired due to a delete operation, from the Salesforce user interface,
Apex, or the API.

`isBefore` Returns `true` if this trigger was fired before any record was saved.

`isAfter` Returns `true` if this trigger was fired after all records were saved.

`isUndelete` Returns `true` if this trigger was fired after a record is recovered from the Recycle Bin. This recovery
can occur after an undelete operation from the Salesforce user interface, Apex, or the API.

```
new

newMap

old

```

Returns a list of the new versions of the sObject records.

This sObject list is only available in `insert`, `update`, and `undelete` triggers, and the records
can only be modified in `before` triggers.

A map of IDs to the new versions of the sObject records.

This map is only available in `before update`, `after insert`, `after update`, and
`after undelete` triggers.

Returns a list of the old versions of the sObject records.

This sObject list is only available in `update` and `delete` triggers.


Apex Reference Guide Trigger Class

**Variable** **Usage**

```
oldMap

operationType

```

A map of IDs to the old versions of the sObject records.

This map is only available in `update` and `delete` triggers.

Returns an enum of type `System.TriggerOperation` corresponding to the current operation.

Possible values of the System.TriggerOperation enum are: `BEFORE_INSERT`, `BEFORE_UPDATE`,
`BEFORE_DELETE`, `AFTER_INSERT`, `AFTER_UPDATE`, `AFTER_DELETE`, and

`AFTER_UNDELETE` . If you vary your programming logic based on different trigger types, consider
using the `switch` statement with different permutations of unique trigger execution enum states.

`size` The number of records processed in a trigger invocation. DML operations that include over 200
records are processed in batches, and the trigger is invoked for each batch. `Trigger.size`

includes only the number of records in the current batch, not the total number of records in the DML
operation.

Note: The record firing a trigger can include an invalid field value, such as a formula that divides by zero. In this case, the field
value is set to `null` in these variables:

**•** `new`

**•** `newMap`

**•** `old`

**•** `oldMap`

Example

For example, in this simple trigger, `Trigger.new` is a list of sObjects and can be iterated over in a `for` loop. It can also be used as
a bind variable in the `IN` clause of a SOQL query.

```
trigger SimpleTrigger on Account(after insert) {

  for (Account a : Trigger.new) {

   // Iterate over each sObject

  }

  // This single query finds every contact that is associated with any of the

  // triggering accounts. Note that although Trigger.new is a collection of

  // records, when used as a bind variable in a SOQL query, Apex automatically

  // transforms the list of records into a list of corresponding Ids.

  Contact[] cons = [

   SELECT LastName

   FROM Contact

   WHERE AccountId IN :Trigger.new

   WITH USER_MODE

  ];

}

```


Apex Reference Guide Trigger Class

This trigger uses Boolean context variables such as `Trigger.isBefore` and `Trigger.isDelete` to define code that only
executes for specific trigger conditions:

```
   trigger MyAccountTrigger on Account(

     before delete,

     before insert,

     before update,

     after delete,

     after insert,

     after update

   ) {

     if (Trigger.isBefore) {

      if (Trigger.isDelete) {

       // In a before delete trigger, the trigger accesses the records that will be

       // deleted with the Trigger.old list.

       for (Account a : Trigger.old) {

        if (a.name != 'okToDelete') {

         a.addError('You can\'t delete this record!');

        }

       }

      } else {

       // In before insert or before update triggers, the trigger accesses the new records

       // with the Trigger.new list.

       for (Account a : Trigger.new) {

        if (a.name == 'bad') {

         a.name.addError('Bad name');

        }

       }

       if (Trigger.isInsert) {

        for (Account a : Trigger.new) {

         Assert.areEqual('xxx', a.accountNumber);

         Assert.areEqual('industry', a.industry);

         Assert.areEqual(100, a.numberofemployees);

         Assert.areEqual(100.0, a.annualrevenue);

         a.accountNumber = 'yyy';

        }

        // If the trigger is not a before trigger, it must be an after trigger.

       } else {

        if (Trigger.isInsert) {

         List<Contact> contacts = new List<Contact>();

         for (Account a : Trigger.new) {

           if (a.Name == 'makeContact') {

            contacts.add(new Contact(LastName = a.Name, AccountId = a.Id));

           }

         }

         insert as user contacts;

        }

       }

      }

     }

   }

```


### Apex Reference Guide TriggerOperation Enum TriggerOperation Enum

System.TriggerOperation enum values are associated with trigger events.

Enum Values

Here are the values of the `System.TriggerOperation` enum listed by their ordinal value.

**•** 0: `BEFORE_INSERT`

**•** 1: `AFTER_INSERT`

**•** 2: `BEFORE_UPDATE`

**•** 3: `AFTER_UPDATE`

**•** 4: `BEFORE_DELETE`

**•** 5: `AFTER_DELETE`

**•** 6: `AFTER_UNDELETE`

### Type Class

Contains methods for getting the Apex type that corresponds to an Apex class and for instantiating new types.

Namespace

System

Usage

Use the `forName` methods to retrieve the type of an Apex class, which can be a built-in or a user-defined class. You can use these
methods to retrieve the type of public and global classes, and not private classes even if the context user has access. Also, use the
`newInstance` method if you want to instantiate a Type that implements an interface and call its methods while letting someone
else, such as a subscriber of your package, provide the methods’ implementations.

Note: A call to `Type.forName()` can cause the class to be compiled.

Example: Instantiating a Type Based on Its Name

The following sample shows how to use the Type methods to instantiate a Type based on its name. A typical application of this scenario
is when a package subscriber provides a custom implementation of an interface that is part of an installed package. The package can
get the name of the class that implements the interface through a custom setting in the subscriber’s org. The package can then instantiate
the type that corresponds to this class name and invoke the methods that the subscriber implemented.

In this sample, `Vehicle` represents the interface that the `VehicleImpl` class implements. The last class contains the code sample
that invokes the methods implemented in `VehicleImpl` .

This is the `Vehicle` interface.

```
   global interface Vehicle {

      Long getMaxSpeed();

      String getType();

   }

```


Apex Reference Guide Type Class

This is the implementation of the `Vehicle` interface.

```
   global class VehicleImpl implements Vehicle {

      global Long getMaxSpeed() { return 100; }

      global String getType() { return 'Sedan'; }

   }

```

The method in this class gets the name of the class that implements the `Vehicle` interface through a custom setting value. It then
instantiates this class by getting the corresponding type and calling the `newInstance` method. Next, it invokes the methods
implemented in `VehicleImpl` . This sample requires that you create a public list custom setting named _`CustomImplementation`_
with a text field named _`className`_ . Create one record for this custom setting with a data set name of _`Vehicle`_ and a class name
value of _`VehicleImpl`_ .

```
   public class CustomerImplInvocationClass {

      public static void invokeCustomImpl() {

        // Get the class name from a custom setting.

        // This class implements the Vehicle interface.

        CustomImplementation__c cs = CustomImplementation__c.getInstance('Vehicle');

        // Get the Type corresponding to the class name

        Type t = Type.forName(cs.className__c);

        // Instantiate the type.

        // The type of the instantiated object

        // is the interface.

        Vehicle v = (Vehicle)t.newInstance();

        // Call the methods that have a custom implementation

        System.debug('Max speed: ' + v.getMaxSpeed());

        System.debug('Vehicle type: ' + v.getType());

      }

   }

```

Class Property

The `class` property returns the `System.Type` of the type it is called on. It’s exposed on all Apex built-in types including primitive
data types and collections, sObject types, and user-defined classes. This property can be used instead of `forName` methods.

Call this property on the type name. For example:

```
   System.Type t = Integer.class;

```

You can use this property for the second argument of `JSON.deserialize`, `deserializeStrict`,
`JSONParser.readValueAs`, and `readValueAsStrict` methods to get the type of the object to deserialize. For example:

```
   Decimal n = (Decimal)JSON.deserialize('100.1', Decimal.class);

#### Type Methods The following are methods for Type .

```


Apex Reference Guide Type Class

IN THIS SECTION:

##### equals(typeToCompare)

Returns `true` if the specified type is equal to the current type; otherwise, returns `false` .

##### forName(fullyQualifiedName)

Returns the type that corresponds to the specified fully qualified class name.

forName(namespace, name)
Returns the type that corresponds to the specified namespace and class name.

getName()
Returns the name of the current type.

hashCode()
Returns a hash code value for the current type.

isAssignableFrom(sourceType)
Returns `true` if an object reference of the specified type can be assigned from the child type; otherwise, returns `false` .

newInstance()
Creates an instance of the current type and returns this new instance.

toString()
Returns a string representation of the current type, which is the type name.

##### equals(typeToCompare)

Returns `true` if the specified type is equal to the current type; otherwise, returns `false` .

Signature

```
   public Boolean equals(Object typeToCompare)

```

Parameters

```
   typeToCompare
```

Type: Object

The type to compare with the current type.

Return Value

Type: Boolean

Example

```
   Type t1 = Account.class;

   Type t2 = Type.forName('Account');

   System.assert(t1.equals(t2));

##### forName(fullyQualifiedName)

```

Returns the type that corresponds to the specified fully qualified class name.


Apex Reference Guide Type Class

Signature

```
   public static System.Type forName(String fullyQualifiedName)

```

Parameters

```
   fullyQualifiedName
```

Type: String

The fully qualified name of the class to get the type of. The fully qualified class name contains the namespace name, for example,
`MyNamespace.ClassName` .

Return Value

Type: `System.Type`

Usage

Note:

**•** This method returns `null` if called outside a managed package to get the type of a non-global class in a managed package.
This is because the non-global class isn’t visible outside the managed package. For Apex saved using Salesforce API version
27.0 and earlier, this method does return the corresponding class type for the non-global managed package class.

**•** When called from an installed managed package to get the name of a local type in an organization with no defined namespace,
##### the forName(fullyQualifiedName) method returns null . Instead, use the forName(namespace, name)

method and specify an empty string or `null` for the namespace argument.

**•** A call to `Type.forName()` can cause the class to be compiled.

##### forName(namespace, name)

Returns the type that corresponds to the specified namespace and class name.

Signature

```
   public static System.Type forName(String namespace, String name)

```

Parameters

```
   namespace
```

Type: String

The namespace of the class. If the class doesn't have a namespace, set the _`namespace`_ argument to `null` or an empty string.

```
   name
```

Type: String

The name of the class.

Return Value

Type: `System.Type`


Apex Reference Guide Type Class

Usage

Note:

**•** This method returns `null` if called outside a managed package to get the type of a non-global class in a managed package.
This is because the non-global class isn’t visible outside the managed package. For Apex saved using Salesforce API version
27.0 and earlier, this method does return the corresponding class type for the non-global managed package class.

**•** Use this method instead of `forName(fullyQualifiedName)` if it’s called from a managed package installed in an
organization with no defined namespace. To get the name of a local type, set the namespace argument to an empty string
or `null` . For example, `Type t = Type.forName('', 'ClassName');` .

**•** A call to `Type.forName()` can cause the class to be compiled.

Example

This example shows how to get the type that corresponds to the `ClassName` class and the `MyNamespace` namespace.

```
   Type myType =

     Type.forName('MyNamespace', 'ClassName');

```

Versioned Behavior Changes

In API version 60.0 and later, using an invalid namespace while calling this method returns null. Previously, Apex allowed you to specify
an invalid namespace such as `Type.forName('InvalidNamespace', 'OuterClass.InnerClass')` or use an outer
class as a namespace such as `Type.forName('OuterClass', 'InnerClass')` with indeterminate results.

##### getName()

Returns the name of the current type.

Signature

```
   public String getName()

```

Return Value

Type: String

Example

##### This example shows how to get a Type’s name. It first obtains a Type by calling forName, then calls getName on the Type object.

```
   Type t =

     Type.forName('MyClassName');

   String typeName =

     t.getName();

   System.assertEquals('MyClassName',

     typeName);

##### hashCode()

```

Returns a hash code value for the current type.


Apex Reference Guide Type Class

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

Usage

The returned hash code value corresponds to the type name hash code that `String.hashCode` returns.

##### isAssignableFrom(sourceType)

Returns `true` if an object reference of the specified type can be assigned from the child type; otherwise, returns `false` .

Signature

```
   public Boolean isAssignableFrom(Type sourceType)

```

Parameters

```
   sourceType
```

The type of the object with which you are checking compatibility.

Return Value

Type: Boolean

The method returns `true` when the method is invoked as parentType.isAssignableFrom(childType). When invoked in any of the
following ways, the method returns `false` :

**•** childType.isAssignableFrom(parentType)

**•** typeA.isAssignableFrom(TypeB) where TypeB is a sibling of TypeA

**•** typeA.isAssignableFrom(TypeB) where TypeB and TypeA are unrelated

Note: A childType is the child of a parentType when it implements an interface, extends a virtual or abstract class, or is the same
`System.Type` as the parentType.

Usage

Unlike the `instanceof` operator, this method allows you to check type compatibility without having to create a class instance. This
method eliminates static compile-time dependencies that `instanceof` requires.

The following code demonstrates how a typical ISV customer can use `isAssignableFrom()` to check compatibility between a
customer-defined type (customerProvidedPluginType) and a valid plugin type.

```
   //Scenario: Managed package code loading a “plugin” class that implements a managed

   interface; the implementation done outside of the package

   String pluginNameStr = Config__c.getInstance().PluginApexType__c;

   Type customerProvidedPluginType = Type.forName(pluginNameStr);

   Type pluginInterface = ManagedPluginInterface.class;

   // Constructors may have side-effects, including potentially unsafe DML/callouts.

```


Apex Reference Guide Type Class

```
   // We want to make sure the class is really designed to be a valid plugin before we

   instantiate it

   Boolean validPlugin = pluginInterface.isAssignableFrom(customerProvidedPluginType); //

   validate that it implements the right interface

   if(!validPlugin){

     throw new SecurityException('Cannot create instance of '+customerProvidedPluginType+'.

    Does not implement ManagedPluginInterface');

   }else{

      return Type.newInstance(validPlugin);

   }

```

Example

The following code snippet first defines sibling classes A and B that both implement the Callable interface and an unrelated class C.
Then, it explores several type comparisons using `isAssignableFrom()` .

```
   //Define classes A, B, and C

   global class A implements Database.Batchable<String>, Callable {

      global Iterable<String> start(Database.BatchableContext context) { return null; }

      global void execute(Database.BatchableContext context, String[] scope) { }

      global void finish(Database.BatchableContext context) { }

      global Object call(String action, Map<String, Object> args) { return null; }

   }

   global class B implements Callable {

      global Object call(String action, Map<String, Object> args) { return null; }

   }

   global class C { }

   Type listOfStrings = Type.forName('List<String>');

   Type listOfIntegers = Type.forName('List<Integer>');

   boolean flagListTypes = listOfIntegers.isAssignableFrom(listOfStrings); // false

   //Examples with stringType and idType

   Type stringType = Type.forName('String');

   Type idType = Type.forName('Id');

   boolean isId_assignableFromString = idType.isAssignableFrom(stringType); // true

   //isAssignableFrom respects that String can be assigned to Id without an explicit cast

   //Examples with typeA, typeB, and typeC

   Type typeA = Type.forName('A');

   Type typeB = Type.forName('B');

   Type typeC = Type.forName('C');

   boolean isTypeB_ofTypeA = typeB.isAssignableFrom( typeA ); // false - siblings

   boolean isTypeA_ofTypeC = typeA.isAssignableFrom( typeC ); // false - unrelated types

   boolean isTypeA_ofTypeA = typeA.isAssignableFrom(typeA); // true - identity

   //Examples with callableType and batchableType

   Type callableType = Type.forName('Callable');

```


Apex Reference Guide Type Class

```
   Type batchableType = Type.forName('Database.Batchable');

   boolean isTypeA_Callable = callableType.isAssignableFrom( typeA ); // true - type A is a

   child of Callable type

   boolean isTypeA_Batchable = batchableType.isAssignableFrom( typeA ); // true - type A is

   a child of Batchable type

   boolean isCallableOfTypeA = typeA.isAssignableFrom( callableType ); // false - Callable

   type is not a child of type A

   boolean isBatchableOfTypeA = typeA.isAssignableFrom( batchableType ); // false - Batchable

    type is not a child of type A

##### newInstance()

```

Creates an instance of the current type and returns this new instance.

Signature

```
   public Object newInstance()

```

Return Value

Type: Object

Usage

##### Because newInstance returns the generic object type, you should cast the return value to the type of the variable that will hold this

value.

This method enables you to instantiate a Type that implements an interface and call its methods while letting someone else provide
the methods’ implementation. For example, a package developer can provide an interface that a subscriber who installs the package
can implement. The code in the package calls the subscriber's implementation of the interface methods by instantiating the subscriber’s
Type.

Example

This example shows how to create an instance of a Type. It first gets a Type by calling `forName` with the name of a class ( `ShapeImpl` ),
##### then calls newInstance on this Type object. The newObj instance is declared with the interface type ( Shape ) that the ShapeImpl class implements. The return value of the newInstance method is cast to the Shape type.

```
   Type t =

     Type.forName('ShapeImpl');

   Shape newObj =

     (Shape)t.newInstance();

##### toString()

```

Returns a string representation of the current type, which is the type name.

Signature

```
   public String toString()

```


### Apex Reference Guide UninstallHandler Interface

Return Value

Type: String

Usage

This method returns the same value as `getName` . `String.valueOf` and `System.debug` use this method to convert their
Type argument into a String.

Example

This example calls `toString` on the Type corresponding to a list of Integers.

```
   Type t = List<Integer>.class;

   String s = t.toString();

   System.assertEquals('List<Integer>', s);

### UninstallHandler Interface

```

Enables custom code to run after a managed package is uninstalled.

Namespace

System

Usage

App developers can implement this interface to specify Apex code that runs automatically after a subscriber uninstalls a managed
package. This makes it possible to perform cleanup and notification tasks based on details of the subscriber’s organization.

The uninstall script is subject to default governor limits. It runs as a special system user that represents your package, so all operations
performed by the script will appear to be done by your package. You can access this user by using UserInfo. You will only see this user
at runtime, not while running tests.

If the script fails, the uninstall continues but none of the changes performed by the script are committed. Any errors in the script are
emailed to the user specified in the **Notify on Apex Error** field of the package. If no user is specified, the uninstall details will be
unavailable.

The uninstall script has the following restrictions. You can’t use it to initiate batch, scheduled, and future jobs, to access Session IDs, or
to perform callouts.

### The UninstallHandler interface has a single method called onUninstall, which specifies the actions to be performed on

uninstall.

```
   global interface UninstallHandler {

     void onUninstall(UninstallContext context)};

```

The `onUninstall` method takes a context object as its argument, which provides the following information.

**•** The org ID of the organization in which the uninstall takes place.

**•** The user ID of the user who initiated the uninstall.


Apex Reference Guide UninstallHandler Interface

The context argument is an object whose type is the `UninstallContext` interface. This interface is automatically implemented
by the system. The following definition of the `UninstallContext` interface shows the methods you can call on the context
argument.

```
   global interface UninstallContext {

     ID organizationId();

     ID uninstallerId();

   }

```

IN THIS SECTION:

#### UninstallHandler Methods UninstallHandler Example Implementation UninstallHandler Methods The following are methods for UninstallHandler .

IN THIS SECTION:

##### onUninstall(context)

Specifies the actions to be performed on uninstall.

##### onUninstall(context)

Specifies the actions to be performed on uninstall.

Signature

```
   public Void onUninstall(UninstallContext context)

```

Parameters

```
   context
```

Type: UninstallContext

Return Value

Type: Void

#### UninstallHandler Example Implementation

Example of an Uninstall Script

This sample uninstall script performs the following actions on package uninstall.

**•** Inserts an entry in the feed describing which user did the uninstall and in which organization


### Apex Reference Guide URL Class

**•** Creates and sends an email message confirming the uninstall to that user

```
   global class UninstallClass implements UninstallHandler {

     global void onUninstall(UninstallContext ctx) {

      FeedItem feedPost = new FeedItem();

      feedPost.parentId = ctx.uninstallerID();

      feedPost.body = 'Thank you for using our application!';

      insert feedPost;

      User u = [Select Id, Email from User where Id =:ctx.uninstallerID()];

      String toAddress= u.Email;

      String[] toAddresses = new String[] {toAddress};

      Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

      mail.setToAddresses(toAddresses);

      mail.setReplyTo('support@package.dev');

      mail.setSenderDisplayName('My Package Support');

      mail.setSubject('Package uninstall successful');

      mail.setPlainTextBody('Thanks for uninstalling the package.');

      Messaging.sendEmail(new Messaging.Email[] { mail });

     }

   }

```

You can test an uninstall script using the `testUninstall` method of the `Test` class. This method takes as its argument a class
that implements the `UninstallHandler` interface.

This sample shows how to test an uninstall script implemented in the `UninstallClass` Apex class.

```
   @isTest

   static void testUninstallScript() {

     Id UninstallerId = UserInfo.getUserId();

     List<FeedItem> feedPostsBefore =

      [SELECT Id FROM FeedItem WHERE parentId=:UninstallerId AND CreatedDate=TODAY];

     Test.testUninstall(new UninstallClass());

     List<FeedItem> feedPostsAfter =

      [SELECT Id FROM FeedItem WHERE parentId=:UninstallerId AND CreatedDate=TODAY];

     System.assertEquals(feedPostsBefore.size() + 1, feedPostsAfter.size(),

      'Post to uninstaller failed.');

   }

### URL Class

```

Represents a uniform resource locator (URL) and provides access to parts of the URL. Enables access to the base URL used to access your
Salesforce org.

Namespace

System


Apex Reference Guide URL Class

Usage

Use the methods of the `System.URL` class to create links to objects in your organization. Such objects can be files, images, logos, or
records that you want to include in external emails, in activities, or in Chatter posts. For example, you can create a link to a file uploaded
as an attachment to a Chatter post by concatenating the Salesforce base URL with the file ID:

```
   // Get a file uploaded through Chatter.

   ContentDocument doc = [SELECT Id FROM ContentDocument

         WHERE Title = 'myfile' WITH USER_MODE];

   // Create a link to the file.

   String fullFileURL = URL.getOrgDomainURL().toExternalForm() +

     '/' + doc.id;

   System.debug(fullFileURL);

```

The following example creates a link to a Salesforce record. The full URL is created by concatenating the Salesforce base URL with the
record ID.

```
   Account acct = [SELECT Id FROM Account WHERE Name = 'Acme' WITH USER_MODE LIMIT 1];

   String fullRecordURL = URL.getOrgDomainURL().toExternalForm() + '/' + acct.Id;

```

Example

In this example, the base URL and the full request URL of the current Salesforce server instance are retrieved. Next, a URL pointing to a
specific account object is created. Finally, components of the base and full URL are obtained. This example prints out all the results to
the debug log output.

```
   // Create a new account called Acme that we will create a link for later.

   Account myAccount = new Account(Name='Acme');

   insert as user myAccount;

   // Get the base URL.

   String sfdcBaseURL = URL.getOrgDomainURL().toExternalForm();

   System.debug('Base URL: ' + sfdcBaseURL );

   // Get the URL for the current request.

   String currentRequestURL = URL.getCurrentRequestUrl().toExternalForm();

   System.debug('Current request URL: ' + currentRequestURL);

   // Create the account URL from the base URL.

   String accountURL = URL.getOrgDomainURL().toExternalForm() +

                 '/' + myAccount.Id;

   System.debug('URL of a particular account: ' + accountURL);

   // Get some parts of the base URL.

   System.debug('Host: ' + URL.getOrgDomainURL().getHost());

   System.debug('Protocol: ' + URL.getOrgDomainURL().getProtocol());

   // Get the query string of the current request.

   System.debug('Query: ' + URL.getCurrentRequestUrl().getQuery());

```

Versioned Behavior Changes

In API version 41.0 and later, Apex URL objects are represented by the `java.net.URI` type, not the `java.net.URL` type. The
API version in which the URL object was instantiated determines the behavior of subsequent method calls to the specific instance.


Apex Reference Guide URL Class

Salesforce strongly encourages you to use API 41.0 and later versions for fully RFC-compliant URL parsing that includes proper handling
of edge cases of complex URL structures. API 41.0 and later versions also enforce that inputs are valid, RFC-compliant URL or URI strings.

IN THIS SECTION:

#### URL Constructors

URL Methods

SEE ALSO:

DomainCreator Class

#### URL Constructors The following are constructors for URL .

IN THIS SECTION:

##### Url(spec)
#### Creates a new instance of the URL class using the specified string representation of the URL.

##### Url(context, spec)
#### Creates a new instance of the URL class by parsing the specified spec within the specified context.

Url(protocol, host, file)
#### Creates a new instance of the URL class using the specified protocol, host, and file on the host. The default port for the specified

protocol is used.

Url(protocol, host, port, file)
#### Creates a new instance of the URL class using the specified protocol, host, port, and file on the host.

##### Url(spec)

#### Creates a new instance of the URL class using the specified string representation of the URL.

Signature

```
   public Url(String spec)

```

Parameters

```
   spec
```

Type: String

The string to parse as a URL.

##### Url(context, spec)

#### Creates a new instance of the URL class by parsing the specified spec within the specified context.


Apex Reference Guide URL Class

Signature

```
   public Url(Url context, String spec)

```

Parameters

```
   context
```

Type: URL on page 4376

The context in which to parse the specification.

```
   spec
```

Type: String

The string to parse as a URL.

Usage

The new URL is created from the given context URL and the spec argument as described in RFC2396 "Uniform Resource Identifiers :
Generic * Syntax" :

```
   <scheme>://<authority><path>?<query>#<fragment>

```

[For more information about the arguments of this constructor, see the corresponding URL(java.net.URL, java.lang.String) constructor for](http://download.oracle.com/javase/6/docs/api/java/net/URL.html#URL%28java.net.URL,%20java.lang.String%29)
Java.

##### Url(protocol, host, file)

Creates a new instance of the `URL` class using the specified protocol, host, and file on the host. The default port for the specified protocol
is used.

Signature

```
   public Url(String protocol, String host, String file)

```

Parameters

```
   protocol
```

Type: String

The protocol name for this URL.

```
   host
```

Type: String

The host name for this URL.

```
   file
```

Type: String

The file name for this URL.

##### Url(protocol, host, port, file)

Creates a new instance of the `URL` class using the specified protocol, host, port, and file on the host.


Apex Reference Guide URL Class

Signature

```
   public Url(String protocol, String host, Integer port, String file)

```

Parameters

```
   protocol
```

Type: String

The protocol name for this URL.

```
   host
```

Type: String

The host name for this URL.

```
   port
```

Type: Integer

The port number for this URL.

```
   file
```

Type: String

The file name for this URL.

#### URL Methods The following are methods for URL .

IN THIS SECTION:

getAuthority()
Returns the authority portion of the current URL.

getCurrentRequestUrl()
Returns the URL of an entire request on a Salesforce instance.

getDefaultPort()
Returns the default port number of the protocol associated with the current URL.

getFile()
Returns the file name of the current URL.

getFileFieldURL(entityId, fieldName)
Returns the download URL for a file attachment.

getHost()
Returns the host name of the current URL.

getOrgDomainUrl()
Returns the canonical URL for your org. For example, `https://` _`MyDomainName`_ `.my.salesforce.com` .

getPath()
Returns the path portion of the current URL.

getPort()
Returns the port of the current URL.


Apex Reference Guide URL Class

getProtocol()
Returns the protocol name of the current URL, such as, `https` .

getQuery()
Returns the query portion of the current URL.

getRef()
Returns the anchor of the current URL.

getSalesforceBaseUrl()
In API version 59.0 and later, this method is deprecated and versioned out. Use getOrgDomainUrl() to get the canonical URL for your
org or use getCurrentRequestUrl() to get the URL of an entire request on a Salesforce instance. Returns the URL of the current
connection to the Salesforce org.

getUserInfo()
Gets the UserInfo portion of the current URL.

sameFile(URLToCompare)
Compares the current URL with the specified URL object, excluding the fragment component.

toExternalForm()
Returns a string representation of the current URL.

##### getAuthority()

Returns the authority portion of the current URL.

Signature

```
   public String getAuthority()

```

Return Value

Type: String

##### getCurrentRequestUrl()

Returns the URL of an entire request on a Salesforce instance.

Signature

```
   public static System.URL getCurrentRequestUrl()

```

Return Value

Type: `System.URL`

Usage

An example of a URL for an entire request is `https://` _`yourInstance`_ `.salesforce.com/apex/myVfPage.apexp` .


Apex Reference Guide URL Class

##### getDefaultPort()

Returns the default port number of the protocol associated with the current URL.

Signature

```
   public Integer getDefaultPort()

```

Return Value

Type: Integer

Usage

Returns -1 if the URL scheme or the stream protocol handler for the URL doesn't define a default port number.

##### getFile()

Returns the file name of the current URL.

Signature

```
   public String getFile()

```

Return Value

Type: String

##### getFileFieldURL(entityId, fieldName)

Returns the download URL for a file attachment.

Signature

```
   public static String getFileFieldURL(String entityId, String fieldName)

```

Parameters

```
   entityId
```

Type: String

Specifies the ID of the entity that holds the file data.

```
   fieldName
```

Type: String

Specifies the API name of a file field component, such as `AttachmentBody` .

Return Value

Type: String


Apex Reference Guide URL Class

Usage

Example:

Example

```
   String fileURL =

     URL.getFileFieldURL(

      '087000000000123',

      'AttachmentBody');

##### getHost()

```

Returns the host name of the current URL.

Signature

```
   public String getHost()

```

Return Value

Type: String

##### getOrgDomainUrl()

Returns the canonical URL for your org. For example, `https://` _`MyDomainName`_ `.my.salesforce.com` .

Signature

```
   public static System.Url getOrgDomainUrl()

```

Return Value

Type: `System.URL`

##### getOrgDomainUrl() always returns the login URL for your org, regardless of context. Use that URL when making API calls to your

org.

Usage

##### Use getOrgDomainUrl() to interact with Salesforce REST and SOAP APIs in Apex code. Get endpoints for User Interface API calls,

for creating and customizing picklist value sets and custom fields, and more.

##### getOrgDomainUrl() can access the domain URL only for the org in which the Apex code is running.

You don't need a RemoteSiteSetting for your org to interact with the Salesforce APIs using domain URLs retrieved with this method.


Apex Reference Guide URL Class

Example

[This example uses the Salesforce REST API to get organization limit values. For information on limits, see Limits in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_limits.htm) _REST API Developer_
_Guide_ .

```
   Http h = new Http();

   HttpRequest req = new HttpRequest();

   req.setEndpoint(Url.getOrgDomainUrl().toExternalForm()

     + '/services/data/v44.0/limits');

   req.setMethod('GET');

   req.setHeader('Authorization', 'Bearer ' + UserInfo.getSessionId());

   HttpResponse res = h.send(req);

```

SEE ALSO:

_[Lightning Aura Components Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/apex_api_calls.htm)_ : Making API Calls from Apex

_User Interface API Developer Guide_ [: Get Default Values to Clone a Record](https://developer.salesforce.com/docs/atlas.en-us.262.0.uiapi.meta/uiapi/ui_api_resources_record_defaults_clone.htm)

_[User Interface API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.uiapi.meta/uiapi/ui_api_resources_picklist_values.htm)_ : Get Values for a Picklist Field

_[User Interface API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.uiapi.meta/uiapi/ui_api_resources_overview.htm)_ : User Inteface API Resources

##### getPath()

Returns the path portion of the current URL.

Signature

```
   public String getPath()

```

Return Value

Type: String

##### getPort()

Returns the port of the current URL.

Signature

```
   public Integer getPort()

```

Return Value

Type: Integer

##### getProtocol()

Returns the protocol name of the current URL, such as, `https` .

Signature

```
   public String getProtocol()

```


Apex Reference Guide URL Class

Return Value

Type: String

##### getQuery()

Returns the query portion of the current URL.

Signature

```
   public String getQuery()

```

Return Value

Type: String

Usage

Returns `null` if no query portion exists.

##### getRef()

Returns the anchor of the current URL.

Signature

```
   public String getRef()

```

Return Value

Type: String

Usage

Returns `null` if no query portion exists.

##### getSalesforceBaseUrl()

In API version 59.0 and later, this method is deprecated and versioned out. Use getOrgDomainUrl() to get the canonical URL for your org
or use getCurrentRequestUrl() to get the URL of an entire request on a Salesforce instance. Returns the URL of the current connection
to the Salesforce org.

Signature

```
   public static System.URL getSalesforceBaseUrl()

```

Return Value

Type: `System.URL`


Apex Reference Guide URL Class

Returns the URL for the current connection: for example, `https://` _`MyDomainName`_ `.my.salesforce.com` or
`https://` _`MyDomainName`_ `.lightning.force.com` .

SEE ALSO:

getOrgDomainUrl()

##### getUserInfo()

Gets the UserInfo portion of the current URL.

Signature

```
   public String getUserInfo()

```

Return Value

Type: String

Usage

Returns `null` if no UserInfo portion exists.

##### sameFile(URLToCompare)

Compares the current URL with the specified URL object, excluding the fragment component.

Signature

```
   public Boolean sameFile(System.URL URLToCompare)

```

Parameters

```
   URLToCompare
```

Type: System.URL

Return Value

Type: Boolean

Returns `true` if both URL objects reference the same remote resource; otherwise, returns `false` .

Usage

[For more information about the syntax of URIs and fragment components, see RFC3986.](http://tools.ietf.org/html/rfc3986)

##### toExternalForm()

Returns a string representation of the current URL.


### Apex Reference Guide UserInfo Class

Signature

```
   public String toExternalForm()

```

Return Value

Type: String

### UserInfo Class

Contains methods for obtaining information about the context user.

Namespace

System

#### UserInfo Methods

### The following are methods for UserInfo . All methods are static.

IN THIS SECTION:

getCurrentUvid()
Returns the context guest user’s unique visitor ID (UVID).

getDefaultCurrency()
Returns the context user's default currency code for multiple currency organizations or the organization's currency code for single
currency organizations.

getFirstName()
Returns the context user's first name

getLanguage()
Returns the context user's language

getLastName()
Returns the context user's last name

getLocale()
Returns the context user's locale.

getName()
Returns the context user's full name. The format of the name depends on the language preferences specified for the organization.

getOrganizationId()
Returns the context organization's ID.

getOrganizationName()
Returns the context organization's company name.

getProfileId()
Returns the context user's profile ID.

getSessionId()
Returns the session ID for the current session.


Apex Reference Guide UserInfo Class

getTimeZone()
Returns the current user’s local time zone.

getUiTheme()
Returns the preferred theme for the current user. Use `getUiThemeDisplayed` to determine the theme actually displayed to
the current user.

getUiThemeDisplayed()
Returns the theme being displayed for the current user.

getUserEmail()
Returns the current user’s email address.

getUserId()
Returns the context user's ID

getUserName()
Returns the context user's login name.

getUserRoleId()
Returns the context user's role ID.

getUserType()
Returns the context user's type.

hasPackageLicense(packageId)
Returns `true` if the context user has a license to the managed package via a package license only. Otherwise, returns `false` .

isCurrentUserLicensed(namespace)
Returns `true` if the context user has a license to any managed package denoted by the namespace. Otherwise, returns `false` .

isCurrentUserLicensedForPackage(packageID)
Returns `true` if the context user has a license to the managed package denoted by the package ID. Otherwise, returns `false` . If
the context user has access, it’s determined either via the package license or a namespace permission set license for the package
namespace.

isMultiCurrencyOrganization()
Specifies whether the organization uses multiple currencies.

##### **`getCurrentUvid()`**

Returns the context guest user’s unique visitor ID (UVID).

Signature

```
   public static String getCurrentUvid()

```

Return Value

Type: String

If a UVID isn’t available, returns `null` .


Apex Reference Guide UserInfo Class

##### getDefaultCurrency()

Returns the context user's default currency code for multiple currency organizations or the organization's currency code for single
currency organizations.

Signature

```
   public static String getDefaultCurrency()

```

Return Value

Type: String

Usage

##### Note: For Apex saved using Salesforce API version 22.0 or earlier, getDefaultCurrency returns null for single currency

organizations.

##### getFirstName()

Returns the context user's first name

Signature

```
   public static String getFirstName()

```

Return Value

Type: String

##### getLanguage()

Returns the context user's language

Signature

```
   public static String getLanguage()

```

Return Value

Type: String

##### getLastName()

Returns the context user's last name

Signature

```
   public static String getLastName()

```


Apex Reference Guide UserInfo Class

Return Value

Type: String

##### getLocale()

Returns the context user's locale.

Signature

```
   public static String getLocale()

```

Return Value

Type: String

Example

```
   String result = UserInfo.getLocale();

   System.assertEquals('en_US', result);

##### getName()

```

Returns the context user's full name. The format of the name depends on the language preferences specified for the organization.

Signature

```
   public static String getName()

```

Return Value

Type: String

Usage

The format is one of the following:

**•** FirstName LastName

**•** LastName, FirstName

##### getOrganizationId()

Returns the context organization's ID.

Signature

```
   public static String getOrganizationId()

```

Return Value

Type: String


Apex Reference Guide UserInfo Class

##### getOrganizationName()

Returns the context organization's company name.

Signature

```
   public static String getOrganizationName()

```

Return Value

Type: String

##### getProfileId()

Returns the context user's profile ID.

Signature

```
   public static String getProfileId()

```

Return Value

Type: String

##### getSessionId()

Returns the session ID for the current session.

Signature

```
   public static String getSessionId()

```

Return Value

Type: String

Usage

##### You can use getSessionId() both synchronously and asynchronously. In asynchronous Apex (Batch, Future, Queueable, or

Scheduled Apex), this method returns the session ID only when the code is run by an active, valid user. When the code is run by an
internal user, such as the automated process user or a proxy user, the method returns `null` .

As a best practice, ensure that your code handles both cases: when a session ID is or is not available.

Note: If you use a JWT-based access token for session authentication, you can’t use `UserInfo.getSessionId()` . To use
`UserInfo.getSessionId()`, use an opaque access token instead. Ensure that the “Issue JSON Web Token (JWT)-based
access tokens for named users” setting isn’t selected for your external client app or connected app.

##### getTimeZone()

Returns the current user’s local time zone.


Apex Reference Guide UserInfo Class

Signature

```
   public static System.TimeZone getTimeZone()

```

Return Value

Type: System.TimeZone

Example

```
   TimeZone tz =

     UserInfo.getTimeZone();

   System.debug(

     'Display name: ' +

     tz.getDisplayName());

   System.debug(

     'ID: ' +

     tz.getID());

##### getUiTheme() Returns the preferred theme for the current user. Use getUiThemeDisplayed to determine the theme actually displayed to the
```

current user.

Signature

```
   public static String getUiTheme()

```

Return Value

Type: String

The preferred theme for the current user.

Valid values include:

**•** `Theme1` —Obsolete Salesforce theme

**•** `Theme2` —Salesforce Classic 2005 user interface theme

**•** `Theme3` —Salesforce Classic 2010 user interface theme

**•** `Theme4d` —Modern “Lightning Experience” Salesforce theme

**•** `Theme4t` —Salesforce mobile app theme

**•** `Theme4u` —Lightning Console theme

**•** `PortalDefault` —Salesforce Customer Portal theme that applies to Customer Portals only and not to Experience Builder sites

**•** `Webstore` —AppExchange theme

##### getUiThemeDisplayed()

Returns the theme being displayed for the current user.


Apex Reference Guide UserInfo Class

Signature

```
   public static String getUiThemeDisplayed()

```

Return Value

Type: String

The theme being displayed for the current user

Valid values include:

**•** `Theme1` —Obsolete Salesforce theme

**•** `Theme2` —Salesforce Classic 2005 user interface theme

**•** `Theme3` —Salesforce Classic 2010 user interface theme

**•** `Theme4d` —Modern “Lightning Experience” Salesforce theme

**•** `Theme4t` —Salesforce mobile app theme

**•** `Theme4u` —Lightning Console theme

**•** `PortalDefault` —Salesforce Customer Portal theme that applies to Customer Portals only and not to Experience Builder sites

**•** `Webstore` —AppExchange theme

##### getUserEmail()

Returns the current user’s email address.

Signature

```
   public static String getUserEmail()

```

Return Value

Type: String

Example

```
   String emailAddress =

     UserInfo.getUserEmail();

   System.debug(

     'Email address: ' +

     emailAddress);

##### getUserId()

```

Returns the context user's ID

Signature

```
   public static String getUserId()

```


Apex Reference Guide UserInfo Class

Return Value

Type: String

##### getUserName()

Returns the context user's login name.

Signature

```
   public static String getUserName()

```

Return Value

Type: String

##### getUserRoleId()

Returns the context user's role ID.

Signature

```
   public static String getUserRoleId()

```

Return Value

Type: String

##### getUserType()

Returns the context user's type.

Signature

```
   public static String getUserType()

```

Return Value

Type: String

##### hasPackageLicense(packageId)

Returns `true` if the context user has a license to the managed package via a package license only. Otherwise, returns `false` .

Signature

```
   public static Boolean hasPackageLicense(ID packageID)

```


Apex Reference Guide UserInfo Class

Parameters

```
   packageID
```

Type: String

Return Value

Type: Boolean

##### isCurrentUserLicensed(namespace)

Returns `true` if the context user has a license to any managed package denoted by the namespace. Otherwise, returns `false` .

Signature

```
   public static Boolean isCurrentUserLicensed(String namespace)

```

Parameters

```
   namespace
```

Type: String

Return Value

Type: Boolean

Usage

A `TypeException` is thrown if _`namespace`_ is an invalid type.

##### isCurrentUserLicensedForPackage(packageID)

Returns `true` if the context user has a license to the managed package denoted by the package ID. Otherwise, returns `false` . If the
context user has access, it’s determined either via the package license or a namespace permission set license for the package namespace.

Signature

```
   public static Boolean isCurrentUserLicensedForPackage(ID packageID)

```

Parameters

```
   packageID
```

Type: String

Return Value

Type: Boolean


### Apex Reference Guide UserManagement Class

Usage

Retrieve _`packageID`_ at runtime, with the getCurrentPackageId() method. Then, use `packageId` to confirm that the contextual
user is licensed to use that managed package.

A `TypeException` is thrown if `packageID` is an invalid type or is the ID of an unlocked or unmanaged package.

SEE ALSO:

_[Set Up and Maintain Your Salesforce Organization](https://help.salesforce.com/s/articleView?id=xcloud.distribution_managing_licenses.htm&type=5&language=en_US)_ : Manage Licenses for Installed Packages

##### isMultiCurrencyOrganization()

Specifies whether the organization uses multiple currencies.

Signature

```
   public static Boolean isMultiCurrencyOrganization()

```

Return Value

Type: Boolean

### UserManagement Class

Contains methods to manage end users, for example, to register their verification methods, verify their identity, or remove their personal
information.

Namespace

System

Usage

Let users register and deregister identity verification methods. Create custom Login and Verify pages for passwordless login and
self-registration. Convert mobile phone numbers to the proper format before registering users. Scramble user data when users request
that Salesforce remove their personal information.

This class is available in API version 43.0 and later.

IN THIS SECTION:

#### UserManagement Methods UserManagement Methods

### The following are methods for UserManagement .

IN THIS SECTION:

clone()
Makes a duplicate copy of the System.UserManagement object.


Apex Reference Guide UserManagement Class

deregisterVerificationMethod(userId, method)
Deregisters an identity verification method. Use this method to let users delete an existing verification method.

formatPhoneNumber(countryCode, phoneNumber)
Formats a mobile phone number for a user. Call this method to ensure that the phone number is formatted properly before updating
a user’s mobile phone number.

initPasswordlessLogin(userId, method)
Invokes a verification challenge for passwordless login when creating custom (Visualforce) Login and Verify pages for customers
and partners.

initRegisterVerificationMethod(method)
Invokes a verification challenge for registering identity verification methods with a custom (Visualforce) page. Users can register
either their email address or phone number.

initSelfRegistration(method, user)
Invokes a verification challenge for self-registration when creating a custom (Visualforce) Verify page for Experience Cloud
self-registration.

initVerificationMethod(method)
Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

initVerificationMethod(method, actionName, extras)
Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

obfuscateUser(userId, username)
Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it. Use this method to set the username to a specific
value after it’s scrambled.

obfuscateUser(userId)
Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it.

registerVerificationMethod(method, startUrl)
Registers an identity verification method. Verification methods can be a time-based one-time password (TOTP), email or text
verification code, Salesforce Authenticator, or U2F-compatible security key. End users register verification methods for themselves.

sendAsyncEmailConfirmation(userId, emailTemplateId, networkId, startUrl)
Send an email message to a user’s email address for verification. The message contains a verification link (URL) that the user clicks
to verify the email address later on. You can send email verifications in bulk.

verifyPasswordlessLogin(userId, method, identifier, code, startUrl)
Completes a verification challenge during a passwordless login that uses a custom Verify page (Visualforce only). If the user who is
trying to log in enters the verification code successfully, the user is logged in.

verifyRegisterVerificationMethod(code, method)
Completes registering a user’s email address or phone number as a verification method when customizing the identity verification
process.

verifySelfRegistration(method, identifier, code, startUrl)
Completes a verification challenge when creating a custom (Visualforce) Verify page for Experience Cloud site self-registration. If the
person who is attempting to register enters the verification code successfully, the user is created and logged in.

verifyVerificationMethod(identifier, code, method)
Completes the verification service for email, phone (SMS), Salesforce Authenticator, password, or time-based one-time password
(TOTP) verification methods.


Apex Reference Guide UserManagement Class

##### clone()

Makes a duplicate copy of the System.UserManagement object.

Signature

```
   public Object clone()

```

Return Value

Type: User Management

##### deregisterVerificationMethod(userId, method)

Deregisters an identity verification method. Use this method to let users delete an existing verification method.

Signature

```
   public static void deregisterVerificationMethod(Id userId, Auth.VerificationMethod

   method)

```

Parameters

```
   userId
```

Type: Id

User ID of the user deregistering the verification method.

```
   method
```

Type: Auth.VerificationMethod

Verification method used to verify the identity of the user.

Return Value

Type: void

Usage

Use this method to deregister an existing identity verification method. For example, your users can deregister a phone number when
their phone number changes. While only end users can register an identity verification method, you and your users can deregister one.
Keep this behavior in mind when you implement a custom registration page.

This method is available in API version 43.0 and later.

Note: This method doesn't support deregistering built-in authenticators.

##### formatPhoneNumber(countryCode, phoneNumber)

Formats a mobile phone number for a user. Call this method to ensure that the phone number is formatted properly before updating
a user’s mobile phone number.


Apex Reference Guide UserManagement Class

Signature

```
   global static String formatPhoneNumber(String countryCode, String phoneNumber)

```

Parameters

```
   countryCode
```

Type: String

A valid country code.

```
   phoneNumber
```

Type: String

A mobile number that contains from 3 through 49 numeric characters, without the country code. For example, (415) 555-1234.

Return Value

Type: String

Returns a user’s mobile phone number in the proper format.

Usage

Use this method to ensure a user’s mobile phone number is formatted as required by Salesforce. Then use the method’s return value to
update the `mobile` field of the user’s record. This mobile number is used for SMS-based device activation. For example, mobile phone
numbers are stored along with other identity verification methods in Auth.VerificationMethod enum. This method is introduced in API
version 43.0. It isn't available in earlier versions.

Here are some acceptable ways that users can enter their mobile number:

**•** +1, (415) 555-1234 (with plus signs, parentheses, and dashes)

