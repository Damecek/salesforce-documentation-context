# Apex developer guide

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/salesforce_apex_developer_guide.pdf
> Fetched: 2026-06-02T08:15:48Z
Apex Developer Guide

Version 67.0, Summer ’26

Last updated: May 28, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

Apex Developer Guide **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**
Getting Started with Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Introducing Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2**
Apex Development Process **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11**
Apex Quick Start **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**
Writing Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**

Data Types and Variables **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
Control Flow Statements **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53**
Classes, Objects, and Interfaces **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61**
Working with Data in Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133**
Document Your Apex Code **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245**
Running Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263**

Invoking Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264**
Apex Transactions and Governor Limits **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347**
Using Salesforce Features with Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 363**
Integration and Apex Utilities **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 610**
Debugging, Testing, and Deploying Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678**

Debugging Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678**
Testing Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 720**
Deploying Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 764**
Apex in Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 766**
Apex Reference **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 794**
Appendices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 794**

Apex Versioned Behavior Changes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 794**
Shipping Invoice Example **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 805**
Reserved Keywords **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 816**
Documentation Typographical Conventions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 818**

APEX DEVELOPER GUIDE

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control
statements on the Salesforce Platform server, in conjunction with calls to the API. This guide introduces you to the Apex development
process and provides valuable information on learning, writing, deploying and testing Apex.

[For reference information on Apex classes, interfaces, exceptions and so on, see Apex Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ref_guide.htm)

Apex Release Notes
Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex.

## Getting Started with Apex

Learn about the Apex development lifecycle. Follow a step-by-step tutorial to create an Apex class and trigger, and deploy them to
a production organization.

Writing Apex
Apex is like Java for Salesforce. It enables you to add and interact with data in the Lightning Platform persistence layer. It uses classes,
data types, variables, and if-else statements. You can make it execute based on a condition, or have a block of code execute repeatedly.

Running Apex
You can access many features of the Salesforce user interface programmatically in Apex, and you can integrate with external SOAP
and REST Web services. You can run Apex code using a variety of mechanisms. Apex code runs in atomic transactions.

Debugging, Testing, and Deploying Apex
Develop your Apex code in a sandbox and debug it with the Developer Console and debug logs. Unit-test your code, then distribute
it to customers using packages.

Apex Reference
In Summer ’21 and later versions, Apex reference content is moved to a separate guide called the Apex Reference Guide.

Appendices

Apex Release Notes

Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex.

[For Apex updates and changes that impact the Salesforce Platform, see the Apex Release Notes.](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex.htm&language=en_US)

[For new and changed Apex classes, methods, exceptions and interfaces, see Apex: New and Changed Items in the Salesforce Release](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_nc.htm&language=en_US)
Notes.

## Getting Started with Apex

Learn about the Apex development lifecycle. Follow a step-by-step tutorial to create an Apex class and trigger, and deploy them to a
production organization.


### Apex Developer Guide Introducing Apex Introducing Apex

Apex code is the first multitenant, on-demand programming language for developers interested in building the next generation of
business applications. Apex revolutionizes the way developers create on-demand applications.

Apex Development Process
In this chapter, you’ll learn about the Apex development lifecycle, and which organization and tools to use to develop Apex. You’ll
also learn about testing and deploying Apex code.

Apex Quick Start
This step-by-step tutorial shows how to create a simple Apex class and trigger, and how to deploy these components to a production
organization.

### Introducing Apex

Apex code is the first multitenant, on-demand programming language for developers interested in building the next generation of
business applications. Apex revolutionizes the way developers create on-demand applications.

While many customization options are available through the Salesforce user interface, such as the ability to define new fields, objects,
workflow, and approval processes, developers can also use the SOAP API to issue data manipulation commands such as `delete()`,
`update()` or `upsert()`, from client-side programs.

These client-side programs, typically written in Java, JavaScript, .NET, or other programming languages, grant organizations more flexibility
in their customizations. However, because the controlling logic for these client-side programs is not located on Salesforce servers, they
are restricted by the performance costs of making multiple round-trips to the Salesforce site to accomplish common business transactions,
and by the cost and complexity of hosting server code, such as Java or .NET, in a secure and robust environment.

1. What is Apex?
Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control
statements on Salesforce servers in conjunction with calls to the API. Using syntax that looks like Java and acts like database stored
procedures, Apex enables developers to add business logic to most system events, including button clicks, related record updates,
and Visualforce pages. Apex code can be initiated by Web service requests and from triggers on objects.

2. Understanding Apex Core Concepts
Apex code typically contains many things that you're familiar with from other programming languages.

3. When Should I Use Apex?
Salesforce provides the ability to customize prebuilt apps to fit your organization. For complex business processes, you can implement
custom functionality and user interfaces with a variety of tools, including Apex and Lightning Components.

4. How Does Apex Work?
All Apex runs entirely on-demand on the Lightning Platform. Developers write and save Apex code to the platform, and end users
trigger the execution of the Apex code via the user interface.

5. Developing Code in the Cloud
The Apex programming language is saved and runs in the cloud—the multitenant platform. Apex is tailored for data access and
data manipulation on the platform, and it enables you to add custom business logic to system events. While it provides many benefits
for automating business processes on the platform, it is not a general purpose programming language.


Apex Developer Guide Introducing Apex

#### What is Apex?

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control
statements on Salesforce servers in conjunction with calls to the API. Using syntax that looks like Java and acts like database stored
procedures, Apex enables developers to add business logic to most system events, including button clicks, related record updates, and
Visualforce pages. Apex code can be initiated by Web service requests and from triggers on objects.

**You can add Apex to most system events.**

As a language, Apex is:

**Integrated**
Apex provides built-in support for common Lightning Platform idioms, including:

**•** Data manipulation language (DML) calls, such as `INSERT`, `UPDATE`, and `DELETE`, that include built-in `DmlException`
handling

**•** Inline Salesforce Object Query Language (SOQL) and Salesforce Object Search Language (SOSL) queries that return lists of sObject
records

**•** Looping that allows for bulk processing of multiple records at a time

**•** Locking syntax that prevents record update conflicts

**•** Custom public API calls that can be built from stored Apex methods

**•** Warnings and errors issued when a user tries to edit or delete a custom object or field that is referenced by Apex


Apex Developer Guide Introducing Apex

**Easy to use**
Apex is based on familiar Java idioms, such as variable and expression syntax, block and conditional statement syntax, loop syntax,
object and array notation. Where Apex introduces new elements, it uses syntax and semantics that are easy to understand and
encourage efficient use of the Lightning Platform. Therefore, Apex produces code that is both succinct and easy to write.

**Data focused**
Apex is designed to thread together multiple query and DML statements into a single unit of work on the Salesforce server. Developers
use database stored procedures to thread together multiple transaction statements on a database server in a similar way. Like other
database stored procedures, Apex does not attempt to provide general support for rendering elements in the user interface.

**Rigorous**
Apex is a strongly typed language that uses direct references to schema objects such as object and field names. It fails quickly at
compile time if any references are invalid. It stores all custom field, object, and class dependencies in metadata to ensure that they
are not deleted while required by active Apex code.

**Hosted**
Apex is interpreted, executed, and controlled entirely by the Lightning Platform.

**Multitenant aware**
Like the rest of the Lightning Platform, Apex runs in a multitenant environment. So, the Apex runtime engine is designed to guard
closely against runaway code, preventing it from monopolizing shared resources. Any code that violates limits fails with
easy-to-understand error messages.

**Easy to test**
Apex provides built-in support for unit test creation and execution. It includes test results that indicate how much code is covered,
and which parts of your code could be more efficient. Salesforce ensures that all custom Apex code works as expected by executing
all unit tests prior to any platform upgrades.

**Versioned**
You can save your Apex code against different versions of the API. This enables you to maintain behavior.

Apex is included in Performance Edition, Unlimited Edition, Developer Edition, Enterprise Edition, and Database.com.

#### Understanding Apex Core Concepts

Apex code typically contains many things that you're familiar with from other programming languages.


Apex Developer Guide Introducing Apex

**Programming elements in Apex**

The section describes the basic functionality of Apex, as well as some of the core concepts.

Using Version Settings

In the Salesforce user interface you can specify a version of the Salesforce API against which to save your Apex class or trigger. This setting
indicates not only the version of SOAP API to use, but which version of Apex as well. You can change the version after saving. Every class
or trigger name must be unique. You can’t save the same class or trigger against different versions.

You can also use version settings to associate a class or trigger with a particular version of a managed package that is installed in your
organization from AppExchange. This version of the managed package continues to be used by the class or trigger if later versions of
the managed package are installed, unless you manually update the version setting. To add an installed managed package to the settings
list, select a package from the list of available packages. The list is only displayed if you have an installed managed package that is not
already associated with the class or trigger.

For more information about using version settings with managed packages, see _About Package Versions_ in Salesforce Help.


Apex Developer Guide Introducing Apex

Naming Variables, Methods and Classes

You can’t use any of the Apex reserved keywords when naming variables, methods, or classes. These include words that are part of Apex
and the Lightning Platform, such as `list`, `test`, or `account`, as well as reserved keywords.

Using Variables and Expressions

Apex is a _strongly-typed_ language, that is, you must declare the data type of a variable when you first refer to it. Apex data types include
basic types such as Integer, Date, and Boolean, as well as more advanced types such as lists, maps, objects, and sObjects.

Variables are declared with a name and a data type. You can assign a value to a variable when you declare it. You can also assign values
later. Use the following syntax when declaring variables:

```
    datatype variable_name [ = value ];

```

Tip: The semi-colon at the end of preceding codeblock is _not_ optional. You must end all statements with a semi-colon.

The following are examples of variable declarations:

```
   // The following variable has the data type of Integer with the name Count,

   // and has the value of 0.

   Integer Count = 0;

   // The following variable has the data type of Decimal with the name Total. Note

   // that no value has been assigned to it.

   Decimal Total;

   // The following variable is an account, which is also referred to as an sObject.

   Account MyAcct = new Account();

```

In Apex, all primitive data type arguments, such as Integer or String, are passed into methods by value. This fact means that any changes
to the arguments exist only within the scope of the method. When the method returns, the changes to the arguments are lost.

Non-primitive data type arguments, such as sObjects, are passed into methods by reference. Therefore, when the method returns, the
passed-in argument still references the same object as before the method call. Within the method, the reference can't be changed to
point to another object, but the values of the object's fields can be changed.

Using Statements

A _statement_ is any coded instruction that performs an action.

In Apex, statements must end with a semicolon and can be one of these types:

**•** Assignment, such as assigning a value to a variable

**•** Conditional (if-else)

**•** Loops:

**–** Do-while

**–** While

**–** For

**•** Locking

**•** Data Manipulation Language (DML)

**•** Transaction Control

**•** Method Invoking

**•** Exception Handling


Apex Developer Guide Introducing Apex

A _block_ is a series of statements that are grouped with curly braces and can be used in any place where a single statement is allowed.
For example:

```
   if (true) {

      System.debug(1);

      System.debug(2);

   } else {

      System.debug(3);

      System.debug(4);

   }

```

In cases where a block consists of only one statement, the curly braces can be left off. For example:

```
   if (true)

      System.debug(1);

   else

      System.debug(2);

```

Using Collections

Apex has the following types of collections:

**•** Lists (arrays)

**•** Maps

**•** Sets

A _list_ is a collection of elements, such as Integers, Strings, objects, or other collections. Use a list when the sequence of elements is
important. You can have duplicate elements in a list.

The first index position in a list is always 0.

To create a list:

**•** Use the `new` keyword

**•** Use the `List` keyword followed by the element type contained within `<>` characters.

Use the following syntax for creating a list:

```
   List < datatype > list_name

     [= new List< datatype >();] |

     [=new List< datatype >{ value [, value2 . . .]};] |

     ;

```

The following example creates a list of Integer, and assigns it to the variable `My_List` . Remember, because Apex is strongly typed,
you must declare the data type of `My_List` as a list of Integer.

```
   List<Integer> My_List = new List<Integer>();

```

For more information, see Lists on page 29.

A _set_ is a collection of unique, unordered elements. It can contain primitive data types, such as String, Integer, Date, and so on. It can
also contain more complex data types, such as sObjects.

To create a set:

**•** Use the `new` keyword

**•** Use the `Set` keyword followed by the primitive data type contained within `<>` characters


Apex Developer Guide Introducing Apex

Use the following syntax for creating a set:

```
   Set< datatype > set_name

     [= new Set< datatype >();] |

     [= new Set< datatype >{ value [, value2 . . .] };] |

     ;

```

The following example creates a set of String. The values for the set are passed in using the curly braces `{}` .

```
   Set<String> My_String = new Set<String>{'a', 'b', 'c'};

```

For more information, see Sets on page 31.

A _map_ is a collection of key-value pairs. Keys can be any primitive data type. Values can include primitive data types, as well as objects
and other collections. Use a map when finding something by key matters. You can have duplicate values in a map, but each key must
be unique.

To create a map:

**•** Use the `new` keyword

**•** Use the `Map` keyword followed by a key-value pair, delimited by a comma and enclosed in `<>` characters.

Use the following syntax for creating a map:

```
   Map< key_datatype, value_datatype > map_name

     [=new Map< key_datatype, value_datatype >();] |

     [=new Map< key_datatype, value_datatype >

     { key1_value => value1_value

     [, key2_value => value2_value . . .]};] |

     ;

```

The following example creates a map that has a data type of Integer for the key and String for the value. In this example, the values for
the map are being passed in between the curly braces `{}` as the map is being created.

```
   Map<Integer, String> My_Map = new Map<Integer, String>{1 => 'a', 2 => 'b', 3 => 'c'};

```

For more information, see Maps on page 32.

Using Branching

An `if` statement is a true-false test that enables your application to do different things based on a condition. The basic syntax is as
follows:

```
   if ( Condition ){

   // Do this if the condition is true

   } else {

   // Do this if the condition is not true

   }

```

For more information, see Conditional (If-Else) Statements on page 54.

Using Loops

While the `if` statement enables your application to do things based on a condition, loops tell your application to do the same thing
again and again based on a condition. Apex supports the following types of loops:

**•** Do-while


Apex Developer Guide Introducing Apex

**•** While

**•** For

A _Do-while_ loop checks the condition after the code has executed.

A _While_ loop checks the condition at the start, before the code executes.

A _For_ loop enables you to more finely control the condition used with the loop. In addition, Apex supports traditional For loops where
you set the conditions, as well as For loops that use lists and SOQL queries as part of the condition.

For more information, see Loops on page 58.

#### When Should I Use Apex?

Salesforce provides the ability to customize prebuilt apps to fit your organization. For complex business processes, you can implement
custom functionality and user interfaces with a variety of tools, including Apex and Lightning Components.

Apex

Use Apex if you want to:

**•** Create Web services.

**•** Create email services.

**•** Perform complex validation over multiple objects.

**•** Create complex business processes that aren’t supported by Flow Builder.

**•** Create custom transactional logic (logic that occurs over the entire transaction, not just with a single record or object).

**•** Attach custom logic to another operation, such as saving a record, so that it occurs whenever the operation is executed, regardless
of whether it originates in the user interface, a Visualforce page, or from SOAP API.

Lightning Components

Develop Lightning components to customize Lightning Experience, the Salesforce mobile app, or to build your own standalone apps.
You can also use out-of-the-box components to speed up development.

As of Spring ’19 (API version 45.0), you can build Lightning components using two programming models: the Lightning Web Components
model, and the original Aura Components model. Lightning web components are custom HTML elements built using HTML and modern
JavaScript. Lightning web components and Aura components can coexist and interoperate on a page. Configure Lightning web
components and Aura components to work in Lightning App Builder and Experience Builder. Admins and end users don’t know which
programming model was used to develop the components. To them, they’re simply Lightning components.

We recommend using the Lightning Web Components (LWC) model to create custom user interfaces. LWC follows W3C web standards,
and you can build and package components using standard JavaScript syntax. With LWC, you can work easily with Salesforce data using
Apex and Lightning Data Service.

[For more information, see the LWC Dev Guide.](https://developer.salesforce.com/docs/platform/lwc)

Visualforce

Visualforce consists of a tag-based markup language that gives developers a more powerful way of building applications and customizing
the Salesforce user interface. With Visualforce you can:

**•** Build wizards and other multistep processes.

**•** Create your own custom flow control through an application.


Apex Developer Guide Introducing Apex

**•** Define navigation patterns and data-specific rules for optimal, efficient application interaction.

[For more information, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

SOAP API

Use standard SOAP API calls when you want to add functionality to a composite application that processes only one type of record at a
time and does not require any transactional control (such as setting a Savepoint or rolling back changes).

[For more information, see the SOAP API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/)

#### How Does Apex Work?

All Apex runs entirely on-demand on the Lightning Platform. Developers write and save Apex code to the platform, and end users trigger
the execution of the Apex code via the user interface.

**Apex is compiled, stored, and run entirely on the Lightning Platform**

When a developer writes and saves Apex code to the platform, the platform application server first compiles the code into an abstract
set of instructions that can be understood by the Apex runtime interpreter, and then saves those instructions as metadata.

When an end user triggers the execution of Apex, perhaps by clicking a button or accessing a Visualforce page, the platform application
server retrieves the compiled instructions from the metadata and sends them through the runtime interpreter before returning the
result. The end user observes no differences in execution time from standard platform requests.

#### Developing Code in the Cloud

The Apex programming language is saved and runs in the cloud—the multitenant platform. Apex is tailored for data access and data
manipulation on the platform, and it enables you to add custom business logic to system events. While it provides many benefits for
automating business processes on the platform, it is not a general purpose programming language.

Apex cannot be used to:

**•** Render elements in the user interface other than error messages

**•** Change standard functionality—Apex can only prevent the functionality from happening, or add additional functionality

**•** Create temporary files

**•** Spawn threads

Tip: All Apex code runs on the Lightning Platform, which is a shared resource used by all other organizations. To guarantee
consistent performance and scalability, the execution of Apex is bound by governor limits that ensure no single Apex execution
impacts the overall service of Salesforce. This means all Apex code is limited by the number of operations (such as DML or SOQL)
that it can perform within one process.


### Apex Developer Guide Apex Development Process

All Apex requests return a collection that contains from 1 to 50,000 records. You cannot assume that your code only works on a
single record at a time. Therefore, you must implement programming patterns that take bulk processing into account. If you don’t,
you may run into the governor limits.

SEE ALSO:

Trigger and Bulk Request Best Practices

### Apex Development Process

In this chapter, you’ll learn about the Apex development lifecycle, and which organization and tools to use to develop Apex. You’ll also
learn about testing and deploying Apex code.

#### What is the Apex Development Process?

To develop Apex, get a Developer Edition account, write and test your code, then deploy your code.

Choose a Salesforce Org for Apex Development
You can develop Apex in a sandbox, scratch org, or Developer Edition org, but not directly in a production org. With so many choices,
here’s some help to determine which org type is right for you and how to create it.

Choose a Development Environment for Writing Apex
There are several development environments for developing Apex code. Choose the environment that meets your needs.

Learning Apex
After you have your developer account, there are many resources available to you for learning about Apex

Writing Tests
Testing is the key to successful long-term development and is a critical component of the development process. We strongly
recommend that you use a _test-driven development_ process, that is, test development that occurs at the same time as code
development.

Deploying Apex to a Sandbox Organization
Sandboxes create copies of your Salesforce org in separate environments. Use them for development, testing, and training without
compromising the data and applications in your production org. Sandboxes are isolated from your production org, so operations
that you perform in your sandboxes don’t affect your production org.

Deploy Apex to a Salesforce Production Organization
After you’ve finished all of your unit tests and verified that your Apex code is executing properly, the final step is deploying Apex to
your Salesforce production organization.

Adding Apex Code to a AppExchange App
You can include an Apex class or trigger in an app that you’re creating for AppExchange.

#### What is the Apex Development Process?

To develop Apex, get a Developer Edition account, write and test your code, then deploy your code.

We recommend the following process for developing Apex:

**1.** Choose a Salesforce Org for Apex development.

**2.** Learn more about Apex.

**3.** Write your Apex.


Apex Developer Guide Apex Development Process

**4.** While writing Apex, you should also be writing tests.

**5.** Optionally deploy your Apex to a sandbox organization and do final unit tests.

**6.** Deploy your Apex to your Salesforce production organization.

In addition to deploying your Apex, once it is written and tested, you can also add your classes and triggers to a AppExchange App
package.

#### Choose a Salesforce Org for Apex Development

You can develop Apex in a sandbox, scratch org, or Developer Edition org, but not directly in a production org. With so many choices,
here’s some help to determine which org type is right for you and how to create it.

Sandboxes (Recommended)

A sandbox is a copy of your production org’s metadata in a separate environment, with varying amounts of data depending on the
sandbox type. A sandbox provides a safe space for developers and admins to experiment with new features and validate changes before
deploying code to production. Developer and Developer Pro sandboxes with source tracking enabled can take advantage of many of
[the features of our Salesforce DX source-driven development tools, including Salesforce CLI, Code Builder, and DevOps Center. See Create](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_create.htm&type=5&language=en_US)
[a Sandbox in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_create.htm&type=5&language=en_US)

Scratch Orgs (Recommended)

A scratch org is a source-driven and temporary deployment of Salesforce code and metadata. A scratch org is fully configurable, allowing
you to emulate different Salesforce editions with different features and settings. Scratch orgs have a maximum 30-day lifespan, with the
[default set at 7 days. For information on using and creating scratch orgs, see Scratch Orgs in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs.htm) _Salesforce DX Developer Guide_ .

Developer Edition (DE) Orgs

A DE org is a free org that provides access to many of the features available in an Enterprise Edition org. Developer Edition orgs can
[become out-of-date over time and have limited storage. Developer Edition orgs don’t have source tracking enabled and can’t be used](https://help.salesforce.com/s/articleView?id=000382500&type=1&language=en_US)
as development environments in DevOps Center. Developer Edition orgs expire if they aren't logged into regularly. You can sign up for
[as many Developer Edition orgs as you like on the Developer Edition Signup page.](https://developer.salesforce.com/signup)

Trial Edition Orgs

Trial editions usually expire after 30 days, so they’re great for evaluating Salesforce functionality but aren’t intended for use as a permanent
development environment. Although Apex triggers are available in trial editions, they’re disabled when you convert to any other edition.
Deploy your code to another org before conversion to retain your Apex triggers. Salesforce offers several product- and industry-specific
[free trial orgs.](https://developer.salesforce.com/free-trials)

Production Orgs (Not Supported)

A production org is the final destination for your code and applications, and has live users accessing your data. You can't develop Apex
in your Salesforce production org, and we recommend that you avoid directly modifying any code or metadata directly in production.
Live users accessing the system while you're developing can destabilize your data or corrupt your application.

#### Choose a Development Environment for Writing Apex

There are several development environments for developing Apex code. Choose the environment that meets your needs.


Apex Developer Guide Apex Development Process

Agentforce for Developers

Agentforce for Developers is an AI-powered developer tool that generates Apex code from natural language prompts and automatically
suggests code completions as you type. Use Agentforce for Developers to easily create unit test cases for your Apex code and get to the
required Apex test coverage.

[Agentforce for Developers extension (salesforcedx-einstein-gpt) is a part of the Salesforce Expanded Pack. Agentforce for Developers is](https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode-expanded)
[enabled by default in VS Code. For more information, see Set Up Agentforce for Developers.](https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-setup.html)

**•** [To access Agentforce for Developers from inside an Apex file in the VS Code editor, see Generate Apex Code.](https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-apex.html)

**•** [To use AI-based autocomplete to accept suggestions for Apex code as you write it, see Inline Auto Completion.](https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-inline.html)

**•** [To use Agentforce for Developers to quickly generate unit tests, see Test Case Generation.](https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-testcasegen.html)

Salesforce Extensions for Visual Studio Code and Code Builder

[The Salesforce Extensions for Visual Studio Code and Code Builder are tools for developing on the Salesforce platform in the lightweight,](https://developer.salesforce.com/tools/vscode)
extensible VS Code editor. These tools provide features for working with development orgs (scratch orgs, sandboxes, and developer
edition orgs), Apex, Lightning components, and Visualforce.

Code Builder is a browser-based version of the desktop experience, with everything installed and configured. It provides all the goodness
of the desktop experience, but provides you with the flexibility to work anywhere, from any computer.

Developer Console

The Developer Console is an integrated development environment (IDE) built into Salesforce. Use it to create, debug, and test Apex
classes and triggers.

To open the Developer Console from Lightning Experience: Click the quick access menu ( ), then click **Developer Console** .

To open the Developer Console from Salesforce Classic: Click `Your Name`    - **Developer Console** .

The Developer Console supports these tasks:

**•** Writing code—You can add code using the source code editor. Also, you can browse packages in your organization.

**•** Compiling code—When you save a trigger or class, the code is automatically compiled. Any compilation errors are reported.

**•** Debugging—You can view debug logs and set checkpoints that aid in debugging.

**•** Testing—You can execute tests of specific test classes or all tests in your organization, and you can view test results. Also, you can
inspect code coverage.

**•** Checking performance—You can inspect debug logs to locate performance bottlenecks.

**•** SOQL queries—You can query data in your organization and view the results using the Query Editor.

**•** Color coding and autocomplete—The source code editor uses a color scheme for easier readability of code elements and provides
autocompletion for class and method names.

Salesforce Setup Code Editors

In Salesforce Setup, you can view and edit Apex classes and triggers.

All classes and triggers are compiled when they’re saved, and any syntax errors are flagged. You can’t save your code until it compiles
without errors. The Salesforce user interface also numbers the lines in the code, and uses color coding to distinguish different elements,
such as comments, keywords, literal strings, and so on.

**•** From Setup in the Quick Find box, enter `Apex`, and select an Apex class or trigger. To edit it, click **Edit** beside the class or trigger
name.


Apex Developer Guide Apex Development Process

**•** To create a trigger on an object, from Setup in the Quick Find box, enter `Object` and click **Object Manager** . Click the object name
and click **Triggers** . Click **New** and enter your code.

Note: You can’t use the Salesforce Setup code editors to modify Apex in a Salesforce production org.

Additional Editors

Alternatively, you can use any text editor, such as Notepad, to write Apex code. Then either copy and paste the code into your application,
or use one of the API calls to deploy it.

To develop an Apex IDE of your own, use SOAP API methods for compiling triggers and classes, and executing test methods. Use Metadata
API methods for deploying code to production environments. For more information, see Deploying Apex on page 764.

SEE ALSO:

_Salesforce Help_ [: Find Object Management Settings](https://help.salesforce.com/HTViewHelpDoc?id=extend_click_find_objectmgmt_parent.htm&language=en_US)

#### Learning Apex

After you have your developer account, there are many resources available to you for learning about Apex

Apex Trailhead Content

Beginning and intermediate programmers

Several Trailhead modules provide tutorials on learning Apex. Use these modules to learn the fundamentals of Apex and how you can
use it on the Salesforce Platform. Use Apex to add custom business logic through triggers, unit tests, asynchronous Apex, REST Web
services, and Lightning components.

**•** [Quick Start: Apex](https://trailhead.salesforce.com/projects/quickstart-apex)

**•** [Apex Basics & Database](https://trailhead.salesforce.com/modules/apex_database)

**•** [Apex Triggers](https://trailhead.salesforce.com/modules/apex_triggers)

**•** [Apex Integration Services](https://trailhead.salesforce.com/modules/apex_integration_services)

**•** [Apex Testing](https://trailhead.salesforce.com/modules/apex_testing)

**•** [Asynchronous Apex](https://trailhead.salesforce.com/modules/asynchronous_apex)

Salesforce Developers Apex Developer Center

Beginning and advanced programmers

[The Apex Developer Center has links to several resources including articles about the Apex programming language. These resources](https://developer.salesforce.com/developer-centers/apex)
provide a quick introduction to Apex and include best practices for Apex development.

Code Samples and SDKs

Beginning and advanced programmers

[Open-source code samples and SDKs, reference code, and best practices can be found at Code samples and SDKs. A library of concise,](https://developer.salesforce.com/code-samples-and-sdks)
[meaningful examples of Apex code for common use cases, following best practices, can be found at Apex-recipes.](https://github.com/trailheadapps/apex-recipes)


Apex Developer Guide Apex Development Process

Training Courses

[Training classes are also available from Salesforce Trailhead Academy. Grow and validate your skills with Salesforce Credentials.](https://trailheadacademy.salesforce.com/overview)

In This Guide (Apex Developer Guide)

Beginning programmers can look at the following:

**•** Introducing Apex, and in particular:

**–** Documentation Conventions

**–** Core Concepts

**–** Quick Start Tutorial

**•** Classes, Objects, and Interfaces

**•** Testing Apex

**•** Execution Governors and Limits

In addition, advanced programmers can look at:

**•** Trigger and Bulk Request Best Practices

**•** Advanced Apex Programming Example

**•** Understanding Apex Describe Information

**•** Asynchronous Execution ( `@future` Annotation)

**•** Batch Apex and Apex Scheduler

#### Writing Tests

Testing is the key to successful long-term development and is a critical component of the development process. We strongly recommend
that you use a _test-driven development_ process, that is, test development that occurs at the same time as code development.

To facilitate the development of robust, error-free code, Apex supports the creation and execution of _unit tests_ . Unit tests are class
methods that verify whether a particular piece of code is working properly. Unit test methods take no arguments, commit no data to
the database, and send no emails. Such methods are flagged with the `@IsTest` annotation in the method definition. Unit test methods
must be defined in test classes, that is, classes annotated with `@IsTest` .

Note: The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce
recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future
release.

In addition, before you deploy Apex or package it for the AppExchange, the following must be true.

**•** Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully.

Note the following.

**–** When deploying Apex to a production organization, each unit test in your organization namespace is executed by default.

**–** Calls to `System.debug` aren’t counted as part of Apex code coverage.

**–** Test methods and test classes aren’t counted as part of Apex code coverage.

**–** While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead,
make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single
records. This approach ensures that 75% or more of your code is covered by unit tests.

**•** Every trigger must have some test coverage.


### Apex Developer Guide Apex Quick Start

**•** All classes and triggers must compile successfully.

For more information on writing tests, see Testing Apex on page 720.

#### Deploying Apex to a Sandbox Organization

Sandboxes create copies of your Salesforce org in separate environments. Use them for development, testing, and training without
compromising the data and applications in your production org. Sandboxes are isolated from your production org, so operations that
you perform in your sandboxes don’t affect your production org.

[To deploy Apex from a local project in the Salesforce extension for Visual Studio Code to a Salesforce organization, see Salesforce](https://developer.salesforce.com/tools/vscode/)
[Extensions for Visual Studio Code.](https://developer.salesforce.com/tools/vscode/)

You can also use the `deploy()` Metadata API call to deploy your Apex from a developer organization to a sandbox organization.

A useful API call is `runTests()` . In a development or sandbox organization, you can run the unit tests for a specific class, a list of
classes, or a namespace.

[You can also use Salesforce CLI. See Develop Against Any Org for details.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_develop_any_org.htm)

For more information, see Deploying Apex.

#### Deploy Apex to a Salesforce Production Organization

After you’ve finished all of your unit tests and verified that your Apex code is executing properly, the final step is deploying Apex to your
Salesforce production organization.

**1.** [To deploy Apex from a local project in Visual Studio Code editor to a Salesforce organization, see Salesforce Extensions for Visual](https://developer.salesforce.com/tools/vscode/)
[Studio Code and Code Builder.](https://developer.salesforce.com/tools/vscode/)

Also, you can deploy Apex through change sets in the Salesforce user interface. For more information and for additional deployment
[options, see Deploying Apex on page 764, and Build and Release Your App.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_build_and_release_your_app.htm)

#### Adding Apex Code to a AppExchange App

You can include an Apex class or trigger in an app that you’re creating for AppExchange.

Any Apex that is included as part of a package must have at least 75% cumulative test coverage. Each trigger must also have some test
coverage. When you upload your package to AppExchange, all tests are run to ensure that they run without errors. In addition, tests
with the `@isTest(OnInstall=true)` annotation run when the package is installed in the installer's organization. You can specify
which tests should run during package install by annotating them with `@isTest(OnInstall=true)` . This subset of tests must
pass for the package install to succeed.

[For more information, see the Second-Generation Managed Packaging Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)

### Apex Quick Start

This step-by-step tutorial shows how to create a simple Apex class and trigger, and how to deploy these components to a production
organization.

When you have a Developer Edition or sandbox organization, you can learn some of the core concepts of Apex. After reviewing the
basics, you’re ready to write your first Apex program—a simple class, trigger, and unit test.

Because Apex is similar to Java, you can recognize much of the functionality.

This tutorial is based on a custom object called Book that is created in the first step. This custom object is updated through a trigger.


Apex Developer Guide Apex Quick Start

This Hello World sample requires custom objects. You can either create these objects on your own, or download the objects and Apex
[code as an unmanaged package from AppExchange. To obtain the sample assets in your org, install the Apex Tutorials Package. This](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000001saDCEAY)
package also contains sample code and objects for the Shipping Invoice example.

Note: There’s a more complex Shipping Invoice example that you can also walk through. That example illustrates many more
features of the language.

#### 1. Create a Custom Object

In this step, you create a custom object called Book with one custom field called Price.

2. Add an Apex Class
In this step, you add an Apex class that contains a method for updating the book price. This method is called by the trigger that
you’ll be adding in the next step.

3. Add an Apex Trigger
In this step, you create a trigger for the `Book__c` custom object that calls the `applyDiscount` method of the `MyHelloWorld`
class that you created in the previous step.

4. Add a Test Class
In this step, you add a test class with one test method. You also run the test and verify code coverage. The test method exercises
and validates the code in the trigger and class. Also, it enables you to reach 100% code coverage for the trigger and class.

5. Deploy Components to Production
In this step, you deploy the Apex code and the custom object you created previously to your production organization using change
sets.

#### Create a Custom Object

In this step, you create a custom object called Book with one custom field called Price.

Prerequisites:

A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org.

For more information about creating a sandbox org, see “Sandbox Types and Templates” in Salesforce Help. To sign up for a free Developer
[org, see the Developer Edition Environment Sign Up Page.](http://developer.force.com/join)

**1.** Log in to your sandbox or Developer org.

**2.** From your management settings for custom objects, if you’re using Salesforce Classic, click **New Custom Object**, or if you’re using
#### Lightning Experience, select Create > Custom Object .

**3.** Enter _`Book`_ for the label.

**4.** Enter _`Books`_ for the plural label.

**5.** Click **Save** .
Ta dah! You’ve now created your first custom object. Now let’s create a custom field.

**6.** In the **Custom Fields & Relationships** section of the Book detail page, click **New** .

**7.** Select Number for the data type and click **Next** .

**8.** Enter _`Price`_ for the field label.

**9.** Enter 16 in the length text box.

**10.** Enter 2 in the decimal places text box, and click **Next** .

**11.** Click **Next** to accept the default values for field-level security.


Apex Developer Guide Apex Quick Start

**12.** Click **Save** .

You've created a custom object called Book, and added a custom field to that custom object. Custom objects already have some standard
fields, like Name and CreatedBy, and allow you to add other fields that are more specific to your implementation. For this tutorial, the
Price field is part of our Book object, and the Apex class you’ll write in the next step accesses it.

SEE ALSO:

_Salesforce Help_ [: Find Object Management Settings](https://help.salesforce.com/HTViewHelpDoc?id=extend_click_find_objectmgmt_parent.htm&language=en_US)

#### Add an Apex Class

In this step, you add an Apex class that contains a method for updating the book price. This method is called by the trigger that you’ll
be adding in the next step.

Prerequisites:

**•** A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org.

**•** The Book custom object.

**1.** From Setup, enter “Apex Classes” in the `Quick Find` box, then select **Apex Classes** and click **New** .

**2.** In the class editor, enter this class definition:

```
     public class MyHelloWorld {

     }

```

The previous code is the class definition to which you’ll be adding one method in the next step. Apex code is contained in _classes._
This class is defined as `public`, which means the class is available to other Apex classes and triggers. For more information, see
Classes, Objects, and Interfaces on page 61.

**3.** Add this method definition between the class opening and closing brackets.

```
     public static void applyDiscount(Book__c[] books) {

       for (Book__c b :books){

         b.Price__c *= 0.9;

       }

     }

```

This method is called `applyDiscount`, and it’s both public and static. Because it’s a static method, you don't need to create an
instance of the class to access the method—you can use the name of the class followed by a dot (.) and the name of the method.
For more information, see Static and Instance Methods, Variables, and Initialization Code on page 70.

This method takes one parameter, a list of Book records, which is assigned to the variable `books` . Notice the `__c` in the object
name `Book__c` . This indicates that it’s a _custom object_ that you created. Standard objects that are provided in the Salesforce
application, such as Account, don't end with this postfix.

The next section of code contains the rest of the method definition:

```
     for (Book__c b :books){

       b.Price__c *= 0.9;

     }

```

Notice the `__c` after the field name `Price__c` . This indicates that it’s a _custom field_ that you created. Standard fields that are
provided by default in Salesforce are accessed using the same type of dot notation but without the `__c`, for example, `Name` doesn't
end with `__c` in `Book__c.Name` . The statement `b.Price__c *= 0.9;` takes the old value of `b.Price__c`, multiplies
it by 0.9, which means its value is discounted by 10%, and then stores the new value into the `b.Price__c` field. The `*=` operator


Apex Developer Guide Apex Quick Start

is a shortcut. Another way to write this statement is `b.Price__c = b.Price__c * 0.9;` . See Expression Operators on
page 40.

**4.** Click **Save** to save the new class. You now have this full class definition.

```
     public class MyHelloWorld {

       public static void applyDiscount(Book__c[] books) {

         for (Book__c b :books){

          b.Price__c *= 0.9;

         }

       }

     }

```

You now have a class that contains some code that iterates over a list of books and updates the Price field for each book. This code is
part of the `applyDiscount` static method called by the trigger that you’ll create in the next step.

#### Add an Apex Trigger

In this step, you create a trigger for the `Book__c` custom object that calls the `applyDiscount` method of the `MyHelloWorld`
class that you created in the previous step.

Prerequisites:

**•** A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org.

**•** The MyHelloWorld Apex class.

#### A trigger is a piece of code that executes before or after records of a particular type are inserted, updated, or deleted from the Lightning

Platform database. Every trigger runs with a set of context variables that provide access to the records that caused the trigger to fire. All
triggers run in bulk; that is, they process several records at once.

**1.** From the object management settings for books, go to Triggers, and then click **New** .

**2.** In the trigger editor, delete the default template code and enter this trigger definition:

```
     trigger HelloWorldTrigger on Book__c (before insert) {

       Book__c[] books = Trigger.new;

       MyHelloWorld.applyDiscount(books);

     }

```

The first line of code defines the trigger:

```
     trigger HelloWorldTrigger on Book__c (before insert) {

```

It gives the trigger a name, specifies the object on which it operates, and defines the events that cause it to fire. For example, this
trigger is called HelloWorldTrigger, it operates on the `Book__c` object, and runs before new books are inserted into the database.

The next line in the trigger creates a list of book records named `books` and assigns it the contents of a trigger context variable
called `Trigger.new` . Trigger context variables such as `Trigger.new` are implicitly defined in all triggers and provide access
to the records that caused the trigger to fire. In this case, `Trigger.new` contains all the new books that are about to be inserted.

```
     Book__c[] books = Trigger.new;

```

The next line in the code calls the method `applyDiscount` in the `MyHelloWorld` class. It passes in the array of new books.

```
     MyHelloWorld.applyDiscount(books);

```


Apex Developer Guide Apex Quick Start

You now have all the code that is needed to update the price of all books that get inserted. However, there’s still one piece of the puzzle
missing. Unit tests are an important part of writing code and are required. In the next step, you'll see why this is so and will be able to
add a test class.

SEE ALSO:

_Salesforce Help_ [: Find Object Management Settings](https://help.salesforce.com/HTViewHelpDoc?id=extend_click_find_objectmgmt_parent.htm&language=en_US)

#### Add a Test Class

In this step, you add a test class with one test method. You also run the test and verify code coverage. The test method exercises and
validates the code in the trigger and class. Also, it enables you to reach 100% code coverage for the trigger and class.

Prerequisites:

**•** A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org.

**•** The HelloWorldTrigger Apex trigger.

Note: Testing is an important part of the development process. Before you can deploy Apex or package it for AppExchange, the
following must be true.

**•** Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully.

Note the following.

**–** When deploying Apex to a production organization, each unit test in your organization namespace is executed by default.

**–** Calls to `System.debug` aren’t counted as part of Apex code coverage.

**–** Test methods and test classes aren’t counted as part of Apex code coverage.

**–** While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead,
make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and
single records. This approach ensures that 75% or more of your code is covered by unit tests.

**•** Every trigger must have some test coverage.

**•** All classes and triggers must compile successfully.

**1.** From Setup, enter _`Apex Classes`_ in the `Quick Find` box, then select **Apex Classes** and click **New** .

**2.** In the class editor, add this test class definition, and then click **Save** .

```
     @IsTest

     private class HelloWorldTestClass {

       @IsTest

       static void validateHelloWorld() {

         Book__c b = new Book__c(Name='Behind the Cloud', Price__c=100);

         System.debug('Price before inserting new book: ' + b.Price__c);

         // Insert book

         insert b;

         // Retrieve the new book

         b = [SELECT Price__c FROM Book__c WHERE Id =:b.Id];

         System.debug('Price after trigger fired: ' + b.Price__c);

         // Test that the trigger correctly updated the price

         System.assertEquals(90, b.Price__c);

```


Apex Developer Guide Apex Quick Start

```
       }

     }

```

This class is defined using the `@IsTest` annotation. Classes defined this way should only contain test methods and any methods
required to support those test methods. One advantage to creating a separate class for testing is that classes defined with `@IsTest`
don’t count against your org’s limit of 6 MB of Apex code. You can also add the `@IsTest` annotation to individual methods. For
more information, see `@IsTest` Annotation on page 106 and Execution Governors and Limits.

The method `validateHelloWorld` is defined using the `@IsTest` annotation. This annotation means that if changes are
made to the database, they’re rolled back when execution completes. You don’t have to delete any test data created in the test
method.

Note: The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce
recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a
future release.

First, the test method creates a book and inserts it into the database temporarily. The `System.debug` statement writes the value
of the price in the debug log.

```
     Book__c b = new Book__c(Name='Behind the Cloud', Price__c=100);

     System.debug('Price before inserting new book: ' + b.Price__c);

     // Insert book

     insert b;

```

After the book is inserted, the code retrieves the newly inserted book, using the ID that was initially assigned to the book when it
was inserted. The `System.debug` statement then logs the new price that the trigger modified.

```
     // Retrieve the new book

     b = [SELECT Price__c FROM Book__c WHERE Id =:b.Id];

     System.debug('Price after trigger fired: ' + b.Price__c);

```

When the `MyHelloWorld` class runs, it updates the `Price__c` field and reduces its value by 10%. The following test verifies
that the method `applyDiscount` ran and produced the expected result.

```
     // Test that the trigger correctly updated the price

     System.assertEquals(90, b.Price__c);

```

**3.** To run this test and view code coverage information, switch to the Developer Console.

**4.** In the Developer Console, click **Test**    - **New Run** .

**5.** To select your test class, click **HelloWorldTestClass** .

**6.** To add all methods in the `HelloWorldTestClass` class to the test run, click **Add Selected** .

**7.** Click **Run** .
The test result displays in the Tests tab. Optionally, you can expand the test class in the Tests tab to view which methods were run.
In this case, the class contains only one test method.

**8.** The Overall Code Coverage pane shows the code coverage of this test class. To view the percentage of lines of code in the trigger
covered by this test, which is 100%, double-click the code coverage line for **HelloWorldTrigger** . Because the trigger calls a method
from the `MyHelloWorld` class, this class also has coverage (100%). To view the class coverage, double-click **MyHelloWorld** .

**9.** To open the log file, in the Logs tab, double-click the most recent log line in the list of logs. The execution log displays, including
logging information about the trigger event, the call to the `applyDiscount` method, and the price before and after the trigger.


Apex Developer Guide Apex Quick Start

By now, you’ve completed all the steps necessary for writing some Apex code with a test that runs in your development environment.
In the real world, after you tested your code and are satisfied with it, you want to deploy the code and any prerequisite components to
a production org. The next step shows you how to do this deployment for the code and custom object you created.

SEE ALSO:

_Salesforce Help_ [: Open the Developer Console](https://help.salesforce.com/HTViewHelpDoc?id=code_dev_console_opening.htm&language=en_US)

#### Deploy Components to Production

In this step, you deploy the Apex code and the custom object you created previously to your production organization using change
sets.

Prerequisites:

**•** A Salesforce account in a sandbox Performance, Unlimited, or Enterprise Edition organization.

**•** The HelloWorldTestClass Apex test class.

**•** A deployment connection between the sandbox and production organizations that allows inbound change sets to be received by
the production organization. See “Change Sets” in Salesforce Help.

**•** “Create and Upload Change Sets” user permission to create, edit, or upload outbound change sets.

This procedure doesn't apply to Developer organizations since change sets are available only in Performance, Unlimited, Enterprise, or
Database.com Edition organizations. If you have a Developer Edition account, you can use other deployment methods. For more
information, see Deploying Apex.

**1.** From Setup, enter _`Outbound Changesets`_ in the `Quick Find` box, then select **Outbound Changesets** .

**2.** If a splash page appears, click **Continue** .

**3.** In the Change Sets list, click **New** .

**4.** Enter a name for your change set, for example, _`HelloWorldChangeSet`_, and optionally a description. Click **Save** .

**5.** In the Change Set Components section, click **Add** .

**6.** Select Apex Class from the component type dropdown list, then select the MyHelloWorld and the HelloWorldTestClass classes from
the list and click **Add to Change Set** .

**7.** To add the dependent components, click **View/Add Dependencies** .

**8.** To select all components, select the top checkbox. Click **Add To Change Set** .

**9.** In the Change Set Detail section of the change set page, click **Upload** .

**10.** Select the target organization, in this case production, and click **Upload** .

**11.** After the change set upload completes, deploy it in your production organization.

**a.** Log in to your production organization.

**b.** From Setup, enter _`Inbound Change Sets`_ in the `Quick Find` box, then select **Inbound Change Sets** .

**c.** If a splash page appears, click **Continue** .

**d.** In the change sets awaiting deployment list, click your change set's name.

#### e. Click Deploy .

In this tutorial, you learned how to create a custom object, how to add an Apex trigger, class, and test class. Finally, you also learned
how to test your code, and how to upload the code and the custom object using Change Sets.


## Apex Developer Guide Writing Apex Writing Apex

Apex is like Java for Salesforce. It enables you to add and interact with data in the Lightning Platform persistence layer. It uses classes,
data types, variables, and if-else statements. You can make it execute based on a condition, or have a block of code execute repeatedly.

### Data Types and Variables

Apex uses data types, variables, and related language constructs such as enums, constants, expressions, operators, and assignment
statements.

Control Flow Statements
Apex provides if-else statements, switch statements, and loops to control the flow of code execution. Statements are generally
executed line by line, in the order they appear. With control flow statements, you can make Apex code execute based on a certain
condition, or have a block of code execute repeatedly.

Working with Data in Apex
You can add and interact with data in the Lightning Platform persistence layer. The sObject data type is the main data type that
holds data objects. You’ll use Data Manipulation Language (DML) to work with data, and use query languages to retrieve data, such
as the (), among other things.

Document Your Apex Code
ApexDoc is a standardized comment format that makes it easier for humans, documentation generators, and AI agents to understand
your codebase. We recommend using ApexDoc comments to facilitate code collaboration and increase long-term code maintainability.
Based on the JavaDoc standard, ApexDoc provides specifications, such as specialized tags and guidelines, that are tailored to Apex
and the Salesforce ecosystem.

### Data Types and Variables

Apex uses data types, variables, and related language constructs such as enums, constants, expressions, operators, and assignment
statements.

### 1. Data Types

In Apex, all variables and expressions have a data type, such as sObject, primitive, or enum.

2. Primitive Data Types
Apex uses the same primitive data types as SOAP API, except for higher-precision Decimal type in certain cases.

3. Collections
Collections in Apex can be lists, sets, or maps.

4. Enums
An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Enums are
typically used to define a set of possible values that don’t otherwise have a numerical order. Typical examples include the suit of a
card, or a particular season of the year.

5. Variables
Local variables are declared with Java-style syntax.

6. Constants
Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the `final`
keyword.


#### Apex Developer Guide Data Types and Variables

7. Expressions and Operators
An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value.

8. Assignment Statements
An assignment statement is any statement that places a value into a variable.

9. Rules of Conversion
In general, Apex requires you to explicitly convert one data type to another. For example, a variable of the Integer data type cannot
be implicitly converted to a String. You must use the `string.format` method. However, a few data types can be implicitly
converted, without using a method.

#### Data Types

In Apex, all variables and expressions have a data type, such as sObject, primitive, or enum.

**•** A primitive, such as an Integer, Double, Long, Date, Datetime, String, ID, or Boolean (see Primitive Data Types on page 24)

**•** An sObject, either as a generic sObject or as a specific sObject, such as an Account, Contact, or MyCustomObject__c (see Working
with sObjects on page 133 in Chapter 4.)

**•** A collection, including:

**–** A list (or array) of primitives, sObjects, user defined objects, objects created from Apex classes, or collections (see Lists on page
29)

**–** A set of primitives (see Sets on page 31)

**–** A map from a primitive to a primitive, sObject, or collection (see Maps on page 32)

**•** A typed list of values, also known as an _enum_ (see Enums on page 34)

**•** Objects created from user-defined Apex classes (see Classes, Objects, and Interfaces on page 61)

**•** Objects created from system supplied Apex classes

**•** Null (for the `null` constant, which can be assigned to any variable)

Methods can return values of any of the listed types, or return no value and be of type Void.

Type checking is strictly enforced at compile time. For example, the parser generates an error if an object field of type Integer is assigned
a value of type String. However, all compile-time exceptions are returned as specific fault codes, with the line number and column of
the error. For more information, see Debugging Apex on page 678.

#### Primitive Data Types

Apex uses the same primitive data types as SOAP API, except for higher-precision Decimal type in certain cases.

All Apex variables, whether they’re class member variables or method variables, are initialized to `null` . Make sure that you initialize
your variables to appropriate values before using them. For example, initialize a Boolean variable to `false` .

Apex primitive data types include:

#### **Data Type Description**

Blob A collection of binary data stored as a single object. You can convert this data type to String or from
String using the `toString` and `valueOf` methods, respectively. Blobs can be accepted as Web

service arguments, stored in a document (the body of a document is a Blob), or sent as attachments.
[For more information, see Crypto Class. Salesforce supports Blob manipulation only with Apex class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_restful_crypto.htm)
methods that are supplied by Salesforce.


Apex Developer Guide Data Types and Variables

**Data Type** **Description**

Boolean

Date

Datetime

Decimal

Double

ID

A value that can only be assigned `true`, `false`, or `null` . For example:

```
Boolean isWinner = true;

```

A value that indicates a particular day. Unlike Datetime values, Date values contain no information
about time. Always create date values with a system static method.

You can add or subtract an Integer value from a Date value, returning a Date value. Addition and
subtraction of Integer values are the only arithmetic functions that work with Date values. You can’t
[perform arithmetic functions that include two or more Date values. Instead, use the Date methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_date.htm)

Use the `String.valueOf()` method to obtain the date without an appended timestamp.
Using an implicit string conversion with a Date value results in the date with the timestamp appended.

A value that indicates a particular day and time, such as a timestamp. Always create datetime values
with a system static method.

You can add or subtract an Integer or Double value from a Datetime value, returning a Date value.
Addition and subtraction of Integer and Double values are the only arithmetic functions that work

with Datetime values. You can’t perform arithmetic functions that include two or more Datetime
[values. Instead, use the Datetime methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_datetime.htm)

A number that includes a decimal point. Decimal is an arbitrary precision number. Currency fields
are automatically assigned the type Decimal.

If you don’t explicitly set the number of decimal places for a Decimal, the item from which the Decimal
is created determines the Decimal’s scale. _Scale_ is a count of decimal places. Use the `setScale`
method to set a Decimal’s scale.

**•** If the Decimal is created as part of a query, the scale is based on the scale of the field returned
from the query.

**•** If the Decimal is created from a String, the scale is the number of characters after the decimal
point of the String.

**•** If the Decimal is created from a non-decimal number, the number is first converted to a String.
The scale is then set using the number of characters after the decimal point.

Note: Two Decimal objects that are numerically equivalent but differ in scale (such as 1.1
and 1.10) generally don’t have the same hashcode. Use caution when such Decimal objects
are used in Sets or as Map keys.

A 64-bit number that includes a decimal point. Doubles have a minimum value of -2 [63] and a maximum
value of 2 [63] -1. For example:

```
Double pi = 3.14159;

Double e = 2.7182818284D;

```

Scientific notation (e) for Doubles isn’t supported.

Any valid 18-character Lightning Platform record identifier. For example:

```
ID id='00300000003T2PGAA0';

```


Apex Developer Guide Data Types and Variables

**Data Type** **Description**

If you set `ID` to a 15-character value, Apex converts the value to its 18-character representation. All
invalid `ID` values are rejected with a runtime exception.

Integer

Long

Object

String

A 32-bit number that doesn’t include a decimal point. Integers have a minimum value of
-2,147,483,648 and a maximum value of 2,147,483,647. For example:

```
Integer i = 1;

```

A 64-bit number that doesn’t include a decimal point. Longs have a minimum value of -2 [63] and a
maximum value of 2 [63] -1. Use this data type when you need a range of values wider than the range
provided by Integer. For example:

```
Long l = 2147483648L;

```

Any data type that is supported in Apex. Apex supports primitive data types (such as Integer),
user-defined custom classes, the sObject generic type, or an sObject specific type (such as Account).
All Apex data types inherit from Object.

You can cast an object that represents a more specific data type to its underlying data type. For
example:

```
Object obj = 10;

// Cast the object to an integer.

Integer i = (Integer)obj;

System.assertEquals(10, i);

```

The next example shows how to cast an object to a user-defined type—a custom Apex class named
`MyApexClass` that is predefined in your organization.

```
Object obj = new MyApexClass();

// Cast the object to the MyApexClass custom type.

MyApexClass mc = (MyApexClass)obj;

// Access a method on the user-defined class.

mc.someClassMethod();

```

Any set of characters surrounded by single quotes. For example,

```
String s = 'The quick brown fox jumped over the lazy dog.';

```

**String size** : The limit on the number of characters is governed by the heap size limit.

**Empty Strings and Trailing Whitespace** : sObject String field values follow the same rules as in
SOAP API: they can never be empty (only `null` ), and they can never include leading and trailing
whitespace. These conventions are necessary for database storage.

Conversely, Strings in Apex can be `null` or empty and can include leading and trailing whitespace,
which can be used to construct a message.

**EscapeSequences** : All Strings in Apex use the same escape sequences as SOQL strings: `\b`
(backspace), `\t` (tab), `\n` (line feed), `\f` (form feed), `\r` (carriage return), `\s` (space), `\"` (double
quote), `\'` (single quote), and `\\` (backslash).

**Comparison Operators** : Unlike Java, Apex Strings support using the comparison operators `==`,
`!=`, `<`, `<=`, `>`, and `>=` . Because Apex uses SOQL comparison semantics, results for Strings are collated


Apex Developer Guide Data Types and Variables

**Data Type** **Description**

[according to the context user’s locale and aren’t case-sensitive. For more information, see Expression](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_expressions_operators_understanding.htm)
[Operators.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_expressions_operators_understanding.htm)

**String Methods** : As in Java, Strings can be manipulated with several standard methods. For more
[information, see String Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm)

**Multiline Strings** : To represent a block of text that spans multiple lines, use a multiline string. A
multiline string starts with three single quotes ( `'''` ) immediately followed by a new line. To terminate
a multiline string, use three single quotes ( `'''` ). For example:

```
                 String multilineStr = '''

                 {

                    "Name" : "John Doe",

                    "Type" : "New Customer"

                 }''';

```

For more information, see the Multiline String Usage section.

Time A value that indicates a particular time. Always create time values with a system static method. See
[Time Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_time.htm)

In addition, two non-standard primitive data types can’t be used as variable or method types, but do appear in system static methods:

**•** AnyType. The `valueOf` static method converts an sObject field of type AnyType to a standard primitive. AnyType is used within
the Lightning Platform database exclusively for sObject fields in field history tracking tables.

**•** Currency. The `Currency.newInstance` static method creates a literal of type Currency. This method is for use solely within
SOQL and SOSL `WHERE` clauses to filter against sObject currency fields. You can’t instantiate Currency in any other type of Apex.

[For more information on the AnyType data type, see Field Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/field_types.htm) _Object Reference for Salesforce_ .

Multiline String Usage

**Line Breaks** : Line breaks are automatically translated into newline sequences in the resulting string.

**Whitespace** : Any whitespace before the leftmost non-whitespace character of the string is stripped. Trailing whitespace on each line
is also stripped. During compilation, whitespace stripping occurs before escape sequences are processed.

In this example, the initial eight whitespace characters, represented as periods, on each line are stripped. This removal occurs because
the `<` character is the leftmost non-whitespace character in the string. The trailing whitespace characters found on the first, third, and
fifth lines of the string are also stripped.

```
   String str = '''

   . . . . . . . . <html> . . .

   . . . . . . . . . . . . <body>

   . . . . . . . . . . . . . . . . <p>Hello, world</p> . . .

   . . . . . . . . . . . . </body>

   . . . . . . . . </html> . . .

   . . . . . . . .''';

```

**Escape Sequences** : Multiline strings support the same escape sequences as regular Apex strings.


Apex Developer Guide Data Types and Variables

Use the `\s` escape sequence at the end of a line to create intentional trailing whitespace. In this example, three trailing whitespace
characters are preserved on the first and fifth lines of the string. The trailing whitespace on the third line of the string is stripped.

```
   String str = '''

   . . . . . . . . <html> . . . . \s

   . . . . . . . . . . . . <body>

   . . . . . . . . . . . . . . . . <p>Hello, world</p> . . . .

   . . . . . . . . . . . . </body>

   . . . . . . . . </html> . . . . \s

   . . . . . . . .''';

```

Multiline strings additionally support the `\` (concatenate) sequence at the end of lines. The `\` escape sequence concatenates multiple
lines and prevents the insertion of a newline sequence between them. For example, this multiline string compiles as one line.

```
   String str = '''

      This is a string that doesn't fit on one line \

      but I don't want it to contain newlines \

   ....so I am using this escape sequence to \

   ....prevent them from being inserted''';

```

Unlike regular Apex strings, multiline strings also support unescaped single quotes ( `'` ). However, to use a single quote directly before
the closing single quotes ( `'''` ), first escape the single quote. ( `\''''` ). For example, the second single quote in this multiline string
requires an escape character, whereas the first one doesn’t.

```
   String str = '''

      I want a single quote here '

      And also right before the string ends\'''';

```

**SOQL Queries** : In SOQL and SOSL queries, you can use multiline strings stored in variables. However, unlike regular string literals, you
can’t use multiline literals in SOQL or SOSL queries, except in bind expressions. For example, this pattern is unsupported.

```
   // Unsupported

   List<Account> accs = [SELECT Id FROM Account

                 WHERE Name = '''

                        ExampleOne

                        '''

                 WITH USER_MODE

                ];

```

Otherwise, you can use multiline literals anywhere you can use regular string literals, such as annotation parameters, variable assignments,
and method argument values.

Versioned Behavior Changes

In API version 16.0 and later, Apex uses the higher-precision Decimal data type in certain types such as currency.

In API version 15.0 and later, Apex classes and triggers produce a runtime error if you assign a String value that is too long for the field.

SEE ALSO:

Expression Operators

Class Methods

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/primitive_data_types.htm)_ : Primitive Data Types


Apex Developer Guide Data Types and Variables

#### Collections Collections in Apex can be lists, sets, or maps.

Note: There is no limit on the number of items a collection can hold. However, there is a general limit on heap size.

##### Lists

A list is an ordered collection of elements that are distinguished by their indices. List elements can be of any data type—primitive
types, collections, sObjects, user-defined types, and built-in Apex types.

Sets
A set is an unordered collection of elements that do not contain any duplicates. Set elements can be of any data type—primitive
types, collections, sObjects, user-defined types, and built-in Apex types.

Maps
A map is a collection of key-value pairs where each unique key maps to a single value. Keys and values can be any data type—primitive
types, collections, sObjects, user-defined types, and built-in Apex types.

Parameterized Typing
Apex, in general, is a statically-typed programming language, which means users must specify the data type for a variable before
that variable can be used.

SEE ALSO:

Execution Governors and Limits

##### Lists

A list is an ordered collection of elements that are distinguished by their indices. List elements can be of any data type—primitive types,
collections, sObjects, user-defined types, and built-in Apex types.

This table is a visual representation of a list of Strings:

**Index 0** **Index 1** **Index 2** **Index 3** **Index 4** **Index 5**

'Red' 'Orange' 'Yellow' 'Green' 'Blue' 'Purple'

The index position of the first element in a list is always 0.

##### Lists can contain any collection and can be nested within one another and become multidimensional. For example, you can have a list

of lists of sets of Integers. A list can contain up to seven levels of nested collections inside it, that is, up to eight levels overall.

##### To declare a list, use the List keyword followed by the primitive data, sObject, nested list, map, or set type within <> characters. For

example:

```
   // Create an empty list of String

   List<String> my_list = new List<String>();

   // Create a nested list

   List<List<Set<Integer>>> my_list_2 = new List<List<Set<Integer>>>();

##### To access elements in a list, use the List methods provided by Apex. For example:

   List<Integer> myList = new List<Integer>(); // Define a new list

   myList.add(47); // Adds a second element of value 47 to the end

```


Apex Developer Guide Data Types and Variables

```
                           // of the list

   Integer i = myList.get(0); // Retrieves the element at index 0

   myList.set(0, 1); // Adds the integer 1 to the list at index 0

   myList.clear(); // Removes all elements from the list

```

[For more information, including a complete list of all supported methods, see List Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_list.htm)

Using Array Notation for One-Dimensional Lists

When using one-dimensional lists of primitives or objects, you can also use more traditional array notation to declare and reference list
elements. For example, you can declare a one-dimensional list of primitives or objects by following the data type name with the []
characters:

```
   String[] colors = new List<String>();

```

These two statements are equivalent to the previous:

```
   List<String> colors = new String[1];

   String[] colors = new String[1];

```

To reference an element of a one-dimensional list, you can also follow the name of the list with the element's index position in square
brackets. For example:

```
   colors[0] = 'Green';

```

Even though the size of the previous `String` array is defined as one element (the number between the brackets in `new String[1]` ),
lists are elastic and can grow as needed provided that you use the `List add` method to add new elements. For example, you can
add two or more elements to the `colors` list. But if you’re using square brackets to add an element to a list, the list behaves like an
array and isn’t elastic, that is, you won’t be allowed to add more elements than the declared array size.

All lists are initialized to `null` . Lists can be assigned values and allocated memory using literal notation. For example:

**Example** **Description**

Defines an Integer list of size zero with no elements
```
    List<Integer> ints = new Integer[0];

```

Defines an Integer list with memory allocated for six Integers
```
    List<Integer> ints = new Integer[6];

###### List Sorting
```

You can sort list elements and the sort order depends on the data type of the elements.

###### List Sorting

You can sort list elements and the sort order depends on the data type of the elements.

Using the `List.sort` method, you can sort elements in a list. Sorting is in ascending order for elements of primitive data types, such
as strings. The sort order of other more complex data types is described in the chapters covering those data types.

You can sort custom types (your Apex classes) if they implement the `Comparable` interface. Alternatively, a class implementing the
`Comparator` interface can be passed as a parameter to the `List.sort` method. For more information on the sort order used for
[sObjects, see Sorting Lists of sObjects.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_list_sorting_sobject.htm)


Apex Developer Guide Data Types and Variables

This example shows how to sort a list of strings and verifies that the colors are in ascending order in the list.

```
   List<String> colors = new List<String>{

      'Yellow',

      'Red',

      'Green'};

   colors.sort();

   System.assertEquals('Green', colors.get(0));

   System.assertEquals('Red', colors.get(1));

   System.assertEquals('Yellow', colors.get(2));

```

For the Visualforce SelectOption control, sorting is in ascending order based on the value and label fields. See this next section for the
sequence of comparison steps used for SelectOption.

Default Sort Order for SelectOption

The `List.sort` method sorts SelectOption elements in ascending order using the value and label fields, and is based on this
comparison sequence.

**1.** The value field is used for sorting first.

**2.** If two value fields have the same value or are both empty, the label field is used.

The disabled field isn’t used for sorting.

For text fields, the sort algorithm uses the Unicode sort order. Also, empty fields precede non-empty fields in the sort order.

In this example, a list contains three SelectOption elements. Two elements, United States and Mexico, have the same value field (‘A’).
The `List.sort` method sorts these two elements based on the label field, and places Mexico before United States, as shown in the
output. The last element in the sorted list is Canada and is sorted on its value field ‘C’, which comes after ‘A’.

```
   List<SelectOption> options = new List<SelectOption>();

   options.add(new SelectOption('A','United States'));

   options.add(new SelectOption('C','Canada'));

   options.add(new SelectOption('A','Mexico'));

   System.debug('Before sorting: ' + options);

   options.sort();

   System.debug('After sorting: ' + options);

```

The output of the debug statements shows the contents of the list, both before and after the sort.

```
   DEBUG|Before sorting: (System.SelectOption[value="A", label="United States",

   disabled="false"],

     System.SelectOption[value="C", label="Canada", disabled="false"],

     System.SelectOption[value="A", label="Mexico", disabled="false"])

   DEBUG|After sorting: (System.SelectOption[value="A", label="Mexico", disabled="false"],

     System.SelectOption[value="A", label="United States", disabled="false"],

     System.SelectOption[value="C", label="Canada", disabled="false"])

##### Sets

```

A set is an unordered collection of elements that do not contain any duplicates. Set elements can be of any data type—primitive types,
collections, sObjects, user-defined types, and built-in Apex types.

This table represents a set of strings that uses city names:

'San Francisco' 'New York' 'Paris' 'Tokyo'


Apex Developer Guide Data Types and Variables

Sets can contain collections that can be nested within one another. For example, you can have a set of lists of sets of Integers. A set can
contain up to seven levels of nested collections inside it, that is, up to eight levels overall.

To declare a set, use the `Set` keyword followed by the primitive data type name within <> characters. For example:

```
   Set<String> myStringSet = new Set<String>();

```

The following example shows how to create a set with two hardcoded string values.

```
   // Defines a new set with two elements

   Set<String> set1 = new Set<String>{'New York', 'Paris'};

```

To access elements in a set, use the system methods provided by Apex. For example:

```
   // Define a new set

   Set<Integer> mySet = new Set<Integer>();

   // Add two elements to the set

   mySet.add(1);

   mySet.add(3);

   // Assert that the set contains the integer value we added

   System.assert(mySet.contains(1));

   // Remove the integer value from the set

   mySet.remove(1);

```

The following example shows how to create a set from elements of another set.

```
   // Define a new set that contains the

   // elements of the set created in the previous example

   Set<Integer> mySet2 = new Set<Integer>(mySet);

   // Assert that the set size equals 1

   // Note: The set from the previous example contains only one value

   System.assert(mySet2.size() == 1);

```

[For more information, including a complete list of all supported set system methods, see Set Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_set.htm)

Note the following limitations on sets:

**•** Unlike Java, Apex developers do not need to reference the algorithm that is used to implement a set in their declarations (for example,
`HashSet` or `TreeSet` ). Apex uses a hash structure for all sets.

**•** A set is an unordered collection—you can’t access a set element at a specific index. You can only iterate over set elements.

**•** The iteration order of set elements is deterministic, so you can rely on the order being the same in each subsequent execution of
the same code.

##### Maps

A map is a collection of key-value pairs where each unique key maps to a single value. Keys and values can be any data type—primitive
types, collections, sObjects, user-defined types, and built-in Apex types.

This table represents a map of countries and currencies:

**Country (Key)** 'United States' 'Japan' 'France' 'England' 'India'

**Currency (Value)** 'Dollar' 'Yen' 'Euro' 'Pound' 'Rupee'

Map keys and values can contain any collection, and can contain nested collections. For example, you can have a map of Integers to
maps, which, in turn, map Strings to lists. Map keys can contain up to seven levels of nested collections, that is, up to eight levels overall.


Apex Developer Guide Data Types and Variables

To declare a map, use the `Map` keyword followed by the data types of the key and the value within `<>` characters. For example:

```
   Map<String, String> country_currencies = new Map<String, String>();

   Map<ID, Set<String>> m = new Map<ID, Set<String>>();

```

You can use the generic or specific sObject data types with maps. You can also create a generic instance of a map.

As with lists, you can populate map key-value pairs when the map is declared by using curly brace ( `{}` ) syntax. Within the curly braces,
specify the key first, then specify the value for that key using `=>` . For example:

```
   Map<String, String> MyStrings = new Map<String, String>{'a' => 'b', 'c' =>

   'd'.toUpperCase()};

```

In the first example, the value for the key `a` is `b`, and the value for the key `c` is `D` .

To access elements in a map, use the Map methods provided by Apex. This example creates a map of integer keys and string values. It
adds two entries, checks for the existence of the first key, retrieves the value for the second entry, and finally gets the set of all keys.

```
   Map<Integer, String> m = new Map<Integer, String>(); // Define a new map

   m.put(1, 'First entry'); // Insert a new key-value pair in the map

   m.put(2, 'Second entry'); // Insert a new key-value pair in the map

   System.assert(m.containsKey(1)); // Assert that the map contains a key

   String value = m.get(2); // Retrieve a value, given a particular key

   System.assertEquals('Second entry', value);

   Set<Integer> s = m.keySet(); // Return a set that contains all of the keys in the

   map

```

[For more information, including a complete list of all supported Map methods, see Map Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_map.htm)

Map Considerations

**•** Unlike Java, Apex developers don’t need to reference the algorithm that is used to implement a map in their declarations (for example,
`HashMap` or `TreeMap` ). Apex uses a hash structure for all maps.

**•** The iteration order of map elements is deterministic. You can rely on the order being the same in each subsequent execution of the
same code. However, we recommend to always access map elements by key.

**•** A map key can hold the `null` value.

**•** Adding a map entry with a key that matches an existing key in the map overwrites the existing entry with that key with the new
entry.

**•** Map keys of type String are case-sensitive. Two keys that differ only by the case are considered unique and have corresponding
distinct Map entries. Subsequently, the Map methods, including `put`, `get`, `containsKey`, and `remove` treat these keys as
distinct.

**•** Uniqueness of map keys of user-defined types is determined by the `equals` and `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)` methods, which you provide in
your classes. Uniqueness of keys of all other non-primitive types, such as sObject keys, is determined by comparing the objects’ field
values. Use caution when you use an sObject as a map key because when the sObject is changed, it no longer maps to the same
value. For information and examples, see
[https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_map_sobject_considerations.htm](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_map_sobject_considerations.htm)

**•** A Map object is serializable into JSON only if it uses one of the following data types as a key.

**–** [Boolean](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_boolean.htm)

**–** [Date](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_date.htm)

**–** [DateTime](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_datetime.htm)

**–** [Decimal](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_decimal.htm)

**–** [Double](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_double.htm)


Apex Developer Guide Data Types and Variables

#### – Enum

**–** [Id](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_id.htm)

**–** [Integer](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_integer.htm)

**–** [Long](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_long.htm)

**–** [String](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_string.htm)

**–** [Time](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_time.htm)

##### Parameterized Typing

Apex, in general, is a statically-typed programming language, which means users must specify the data type for a variable before that
variable can be used.

This is legal in Apex:

```
   Integer x = 1;

```

This is not legal, if `x` has not been defined earlier:

```
   x = 1;

```

Lists, maps and sets are _parameterized_ in Apex: they take any data type Apex supports for them as an argument. That data type must be
replaced with an actual data type upon construction of the list, map or set. For example:

```
   List<String> myList = new List<String>();

```

Subtyping with Parameterized Lists

In Apex, if type `T` is a subtype of `U`, then `List<T>` would be a subtype of `List<U>` . For example, the following is legal:

```
   List<String> slst = new List<String> {'alpha', 'beta'};

   List<Object> olst = slst;

#### Enums

```

An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Enums are typically
used to define a set of possible values that don’t otherwise have a numerical order. Typical examples include the suit of a card, or a
particular season of the year.

Although each value corresponds to a distinct integer value, the enum hides this implementation. Hiding the implementation prevents
any possible misuse of the values to perform arithmetic and so on. After you create an enum, variables, method arguments, and return
types can be declared of that type.

Note: Unlike Java, the enum type itself has no constructor syntax.

To define an enum, use the `enum` keyword in your declaration and use curly braces to demarcate the list of possible values. For example,
the following code creates an enum called `Season` :

```
   public enum Season {WINTER, SPRING, SUMMER, FALL}

```


Apex Developer Guide Data Types and Variables

By creating the enum `Season`, you have also created a new data type called `Season` . You can use this new data type as you would
any other data type. For example:

```
   Season southernHemisphereSeason = Season.WINTER;

   public Season getSouthernHemisphereSeason(Season northernHemisphereSeason) {

      if (northernHemisphereSeason == Season.SUMMER) return southernHemisphereSeason;

      //...

   }

```

You can also define a class as an enum. When you create an enum class, do not use the `class` keyword in the definition.

```
   public enum MyEnumClass { X, Y }

```

You can use an enum in any place you can use another data type name. If you define a variable whose type is an enum, any object you
assign to it must be an instance of that enum class.

Any `webservice` method can use enum types as part of their signature. In this case, the associated WSDL file includes definitions
for the enum and its values, which the API client can use.

Apex provides the following system-defined enums:

**•** `System.StatusCode`

This enum corresponds to the API error code that is exposed in the WSDL document for all API operations. For example:

```
     StatusCode.CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY

     StatusCode.INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY

```

The full list of status codes is available in the WSDL file for your organization. For more information about accessing the WSDL file
for your organization, see _Downloading Salesforce WSDLs and Client Authentication Certificates_ in Salesforce Help.

**•** `System.XmlTag` :

This enum returns a list of XML tags used for parsing the result XML from a `webservice` method. For more information, see
[XmlStreamReader Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_xml_XmlStream_reader.htm)

**•** `System.ApplicationReadWriteMode` : This enum indicates if an organization is in 5 Minute Upgrade read-only mode
[during Salesforce upgrades and downtimes. For more information, see System.getApplicationReadWriteMode().](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_System_getApplicationReadWriteMode)

**•** `System.LoggingLevel` :

This enum is used with the `system.debug` method, to specify the log level for all `debug` [calls. For more information, see System](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)
[Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_system.htm)

**•** `System.RoundingMode` :

This enum is used by methods that perform mathematical operations to specify the rounding behavior for the operation. Typical
examples are the Decimal `divide` method and the Double `round` [method. For more information, see Rounding Mode.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_decimal.htm)

**•** `System.SoapType` :

This enum is returned by the field describe result `getSoapType` [method. For more information, see SOAPType Enum.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Schema_SOAPType.htm)

**•** `System.DisplayType` :

This enum is returned by the field describe result `getType` [method. For more information, see DisplayType Enum.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_Schema_DisplayType.htm)

**•** `System.JSONToken` :

[This enum is used for parsing JSON content. For more information, see JsonToken Enum.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_enum_System_JsonToken.htm)


Apex Developer Guide Data Types and Variables

**•** `ApexPages.Severity` :

[This enum specifies the severity of a Visualforce message. For more information, see ApexPages.Severity Enum.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_pages_message.htm)

**•** `Dom.XmlNodeType` :

This enum specifies the node type in a DOM document.

Note: System-defined enums cannot be used in Web service methods.

[All enum values, including system enums, have common methods associated with them. For more information, see Enum Methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_enum.htm)

You cannot add user-defined methods to enum values.

#### Variables

Local variables are declared with Java-style syntax.

For example:

```
   Integer i = 0;

   String str;

   List<String> strList;

   Set<String> s;

   Map<ID, String> m;

```

As with Java, multiple variables can be declared and initialized in a single statement, using comma separation. For example:

```
   Integer i, j, k;

```

Variable Naming Rules

When naming variables, follow these rules.

**•** Variable names are case-insensitive.

**•** Variable names can contain only letters (A-Z or a-z), numbers (0-9), and underscores (_). Spaces and other special characters, including
dollar signs ($) and hyphens (-), aren’t allowed.

**•** Variable names must begin with a letter (A-Z or a-z). Names can’t begin with a number (0-9) or an underscore (_).

**•** Variable names can’t end with an underscore (_).

**•** Varable names can’t contain consecutive underscores (_ _).

**•** [Reserved keywords can’t be used as variable names.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_reserved_words.htm)

**•** Variable names can have a maximum length of 255 characters.

**•** Salesforce doesn't recommend sharing the same name between a variable and either its class or a method in its class, although it
is permitted to do so.

Null Variables and Initial Values

If you declare a variable and don't initialize it with a value, it will be `null` . In essence, `null` means the absence of a value. You can
also assign `null` to any variable declared with a primitive type. For example, both of these statements result in a variable set to `null` :

```
   Boolean x = null;

   Decimal d;

```


Apex Developer Guide Data Types and Variables

Many instance methods on the data type will fail if the variable is `null` . In this example, the second statement generates an exception
( `NullPointerException` )

```
   Date d;

   d.addDays(2);

```

All variables are initialized to `null` if they aren’t assigned a value. For instance, in the following example, `i`, and `k` are assigned values,
while the integer variable `j` and the boolean variable `b` are set to `null` because they aren’t explicitly initialized.

```
   Integer i = 0, j, k = 1;

   Boolean b;

```

Note: A common pitfall is to assume that an uninitialized boolean variable is initialized to `false` by the system. This isn’t the
case. Like all other variables, boolean variables are null if not assigned a value explicitly.

Variable Scope

Variables can be defined at any point in a block, and take on scope from that point forward. Sub-blocks can’t redefine a variable name
that has already been used in a parent block, but parallel blocks can reuse a variable name. For example:

```
   Integer i;

   {

     // Integer i; This declaration is not allowed

   }

   for (Integer j = 0; j < 10; j++);

   for (Integer j = 0; j < 10; j++);

```

Case Sensitivity

To avoid confusion with case-insensitive SOQL and SOSL queries, Apex is also case-insensitive. This means:

**•** Variable and method names are case-insensitive. For example:

```
     Integer I;

     //Integer i;

```

**•** References to object and field names are case-insensitive. For example:

```
     Account a1;

     ACCOUNT a2;

```

**•** SOQL and SOSL statements are case- insensitive. For example:

```
     Account[] accts = [sELect ID From ACCouNT where nAme = 'fred'];

```

Note: You’ll learn more about sObjects, SOQL, and SOSL later in this guide.

Also note that Apex uses the same filtering semantics as SOQL, which is the basis for comparisons in the SOAP API and the Salesforce
user interface. The use of these semantics can lead to some interesting behavior. For example, if an end-user generates a report based
on a filter for values that come before 'm' in the alphabet (that is, values < 'm'), null fields are returned in the result. The rationale for this


Apex Developer Guide Data Types and Variables

behavior is that users typically think of a field without a value as just a space character, rather than its actual `null` value. Consequently,
in Apex, the following expressions all evaluate to `true` :

```
   String s;

   System.assert('a' == 'A');

   System.assert(s < 'b');

   System.assert(!(s > 'b'));

```

Note: Although `s < 'b'` evaluates to `true` in the example above, `'b.'compareTo(s)` generates an error because
you’re trying to compare a letter to a `null` value.

SEE ALSO:

Naming Conventions

#### Constants

Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the `final` keyword.

The `final` keyword means that the variable can be assigned at most once, either in the declaration itself, or with a static initializer
method if the constant is defined in a class. This example declares two constants. The first is initialized in the declaration statement. The
second is assigned a value in a static block by calling a static method.

```
   public class myCls {

     static final Integer PRIVATE_INT_CONST = 200;

     static final Integer PRIVATE_INT_CONST2;

     public static Integer calculate() {

        return 2 + 7;

     }

     static {

        PRIVATE_INT_CONST2 = calculate();

     }

   }

```

For more information, see Using the `final` Keyword on page 86.

#### Expressions and Operators

An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value.

#### Expressions

An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value.

Expression Operators
Expressions can be joined to one another with operators to create compound expressions.

Safe Navigation Operator
Use the safe navigation operator ( `?.` ) to replace explicit, sequential checks for null references. This operator short-circuits expressions
that attempt to operate on a null value and returns null instead of throwing a NullPointerException.


Apex Developer Guide Data Types and Variables

Null Coalescing Operator
The `??` operator returns its right-hand side operand when its left-hand side operand is null. Similar to the safe navigation operator
( `?.` ), the null coalescing operator ( `??` ) replaces verbose and explicit checks for null references in code.

Operator Precedence
Operators are interpreted in order, according to rules.

Comments
Both single and multiline comments are supported in Apex code.

SEE ALSO:

Expanding sObject and List Expressions

##### Expressions

An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value.

In Apex, an expression is always one of the following types:

**•** A literal expression. For example:

```
     1 + 1

```

**•** A new sObject, Apex object, list, set, or map. For example:

```
     new Account(<field_initializers>)

     new Integer[<n>]

     new Account[]{<elements>}

     new List<Account>()

     new Set<String>{}

     new Map<String, Integer>()

     new myRenamingClass(string oldName, string newName)

```

**•** Any value that can act as the left-hand of an assignment operator (L-values), including variables, one-dimensional list positions, and
most sObject or Apex object field references. For example:

```
     Integer i

     myList[3]

     myContact.name

     myRenamingClass.oldName

```

**•** Any sObject field reference that is not an L-value, including:

**–** The ID of an sObject in a list (see Lists)

**–** A set of child records associated with an sObject (for example, the set of contacts associated with a particular account). This type
of expression yields a query result, much like SOQL and SOSL queries.

**•** A SOQL or SOSL query surrounded by square brackets, allowing for on-the-fly evaluation in Apex. For example:

```
     Account[] aa = [SELECT Id, Name FROM Account WHERE Name ='Acme'];

     Integer i = [SELECT COUNT() FROM Contact WHERE LastName ='Weissman'];

     List<List<SObject>> searchList = [FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name),

      Contact, Opportunity, Lead];

```

For information, see SOQL and SOSL Queries on page 170.


Apex Developer Guide Data Types and Variables

**•** A static or instance method invocation. For example:

```
     System.assert(true)

     myRenamingClass.replaceNames()

     changePoint(new Point(x, y));

##### Expression Operators

```

Expressions can be joined to one another with operators to create compound expressions.

Apex supports the following operators:

**Operator** **Syntax** **Description**

`=` `x = y` **Assignment operator** (Right associative). Assigns the value of `y` to the L-value
`x` . The data type of `x` must match the data type of `y` and can’t be `null` .

```
+= x += y

```

**Addition assignment operator** (Right associative). Adds the value of `y` to the
original value of `x` and then reassigns the new value to `x` . See `+` for additional
information. `x` and `y` can’t be `null` .

`*=` `x *= y` **Multiplication assignment operator** (Right associative). Multiplies the value of
`y` with the original value of `x` and then reassigns the new value to `x` .

Note: `x` and `y` must be Integers or Doubles or a combination.

`x` and `y` can’t be `null` .

`-=` `x -= y` **Subtraction assignment operator** (Right associative). Subtracts the value of `y`
from the original value of `x` and then reassigns the new value to `x` .

Note: `x` and `y` must be Integers or Doubles or a combination.

`x` and `y` can’t be `null` .

`/=` `x /= y` **Division assignment operator** (Right associative). Divides the original value of `x`
with the value of `y` and then reassigns the new value to `x` .

Note: `x` and `y` must be Integers or Doubles or a combination.

`x` and `y` can’t be `null` .

```
|= x |= y

&= x &= y

<<= x <<= y

```

**OR assignment operator** (Right associative). If `x`, a Boolean, and `y`, a Boolean,
are both false, then `x` remains false. Otherwise `x` is assigned the value of true. `x`
and `y` can’t be `null` .

**AND assignment operator** (Right associative). If `x`, a Boolean, and `y`, a Boolean,
are both true, then `x` remains true. Otherwise `x` is assigned the value of false. `x`
and `y` can’t be `null` .

**Bitwise shift left assignment operator** . Shifts each bit in `x` to the left by `y` bits
so that the high-order bits are lost and the new right bits are set to 0. This value is
then reassigned to `x` .

`>>=` `x >>= y` **Bitwise shift right signed assignment operator** . Shifts each bit in `x` to the right
by `y` bits so that the low-order bits are lost and the new left bits are set to 0 for


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

positive values of `y` and 1 for negative values of `y` . This value is then reassigned to
`x` .

```
>>>= x >>>= y

? : x ? y : z

&& x && y

|| x || y

```

**Bitwise shift right unsigned assignment operator** . Shifts each bit in `x` to the
right by `y` bits so that the low-order bits are lost and the new left bits are set to 0
for all values of `y` . This value is then reassigned to `x` .

**Ternary operator** (Right associative). This operator acts as a short-hand for
if-then-else statements. If `x`, a Boolean, is true, `y` is the result. Otherwise `z` is the
result.

Note: `x` can’t be `null` .

**AND logical operator** (Left associative). If `x`, a Boolean, and `y`, a Boolean, are both
true, then the expression evaluates to true. Otherwise the expression evaluates to
false.

Note:

**•** `&&` has precedence over `||`

**•** This operator exhibits short-circuiting behavior, which means `y` is evaluated
only if `x` is true.

**•** `x` and `y` can’t be `null` .

**OR logical operator** (Left associative). If `x`, a Boolean, and `y`, a Boolean, are both
false, then the expression evaluates to false. Otherwise the expression evaluates to
true.

Note:

**•** `&&` has precedence over `||`

**•** This operator exhibits short-circuiting behavior, which means `y` is evaluated
only if `x` is false.

**•** `x` and `y` can’t be `null` .

`==` `x == y` **Equality operator** . If the value of `x` equals the value of `y`, the expression evaluates
to true. Otherwise the expression evaluates to false.

Note:

**•** Unlike Java, `==` in Apex compares object value equality not reference
equality, except for user-defined types. Therefore:

**–** String comparison using `==` is case-insensitive and is performed
according to the locale of the context user

**–** ID comparison using `==` is case-sensitive and doesn’t distinguish
between 15-character and 18-character formats

**–** User-defined types are compared by reference, which means that
two objects are equal only if they reference the same location in
memory. You can override this default comparison behavior by


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

providing `equals` and `hashCode` methods in your class to
compare object values instead.

**•** For sObjects and sObject arrays, `==` performs a deep check of all sObject
field values before returning its result. Likewise for collections and built-in
Apex objects.

**•** For records, every field must have the same value for `==` to evaluate to
true.

**•** `x` or `y` can be the literal `null` .

**•** The comparison of any two values can never result in `null` .

**•** SOQL and SOSL use `=` for their equality operator and not `==` . Although
Apex and SOQL and SOSL are strongly linked, this unfortunate syntax
discrepancy exists because most modern languages use `=` for assignment
and `==` for equality. The designers of Apex deemed it more valuable to
maintain this paradigm than to force developers to learn a new
assignment operator. As a result, Apex developers must use `==` for
equality tests in the main body of the Apex code, and `=` for equality in
SOQL and SOSL queries.

`===` `x === y` **Exact equality operator** . If `x` and `y` reference the exact same location in memory
the expression evaluates to true. Otherwise the expression evaluates to false.

`<` `x < y` **Less than operator** . If `x` is less than `y`, the expression evaluates to true. Otherwise
the expression evaluates to false.

Note:

**•** Unlike other database stored procedures, Apex doesn’t support tri-state
Boolean logic and the comparison of any two values can never result in

`null` .

**•** If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes,
the expression is false.

**•** A non- `null` String or ID value is always greater than a `null` value.

**•** If `x` and `y` are IDs, they must reference the same type of object.
Otherwise a runtime error results.

**•** If `x` or `y` is an ID and the other value is a String, the String value is
validated and treated as an ID.

**•** `x` and `y` can’t be Booleans.

**•** The comparison of two strings is performed according to the locale of
the context user and is case-insensitive.

`>` `x > y` **Greater than operator** . If `x` is greater than `y`, the expression evaluates to true.
Otherwise the expression evaluates to false.

Note:

**•** The comparison of any two values can never result in `null` .


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

**•** If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes,
the expression is false.

**•** A non- `null` String or ID value is always greater than a `null` value.

**•** If `x` and `y` are IDs, they must reference the same type of object.
Otherwise a runtime error results.

**•** If `x` or `y` is an ID and the other value is a String, the String value is
validated and treated as an ID.

**•** `x` and `y` can’t be Booleans.

**•** The comparison of two strings is performed according to the locale of
the context user and is case-insensitive.

`<=` `x <= y` **Less than or equal to operator** . If `x` is less than or equal to `y`, the expression
evaluates to true. Otherwise the expression evaluates to false.

Note:

**•** The comparison of any two values can never result in `null` .

**•** If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes,
the expression is false.

**•** A non- `null` String or ID value is always greater than a `null` value.

**•** If `x` and `y` are IDs, they must reference the same type of object.
Otherwise a runtime error results.

**•** If `x` or `y` is an ID and the other value is a String, the String value is
validated and treated as an ID.

**•** `x` and `y` can’t be Booleans.

**•** The comparison of two strings is performed according to the locale of
the context user and is case-insensitive.

`>=` `x >= y` **Greater than or equal to operator** . If `x` is greater than or equal to `y`, the
expression evaluates to true. Otherwise the expression evaluates to false.

Note:

**•** The comparison of any two values can never result in `null` .

**•** If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes,
the expression is false.

**•** A non- `null` String or ID value is always greater than a `null` value.

**•** If `x` and `y` are IDs, they must reference the same type of object.
Otherwise a runtime error results.

**•** If `x` or `y` is an ID and the other value is a String, the String value is
validated and treated as an ID.

**•** `x` and `y` can’t be Booleans.

**•** The comparison of two strings is performed according to the locale of
the context user and is case-insensitive.


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

`!=` `x != y` **Inequality operator** . If the value of `x` doesn’t equal the value of `y`, the expression
evaluates to true. Otherwise the expression evaluates to false.

Note:

**•** String comparison using `!=` is case-insensitive

**•** Unlike Java, `!=` in Apex compares object value equality not reference
equality, except for user-defined types.

**•** For sObjects and sObject arrays, `!=` performs a deep check of all sObject
field values before returning its result.

**•** For records, `!=` evaluates to true if the records have different values for
any field.

**•** User-defined types are compared by reference, which means that two
objects are different only if they reference different locations in memory.
You can override this default comparison behavior by providing `equals`
and `hashCode` methods in your class to compare object values instead.

**•** `x` or `y` _can_ be the literal `null` .

**•** The comparison of any two values can never result in `null` .

```
!== x !== y

```

**Exact inequality operator** . If `x` and `y` don’t reference the exact same location in
memory, the expression evaluates to true. Otherwise the expression evaluates to
false.

`+` `x + y` **Addition operator** . Adds the value of `x` to the value of `y` according to the
following rules:

**•** If `x` and `y` are Integers or Doubles, the operator adds the value of `x` to the
value of `y` . If a Double is used, the result is a Double.

**•** If `x` is a Date and `y` is an Integer, returns a new Date that is incremented by
the specified number of days.

**•** If `x` is a Datetime and `y` is an Integer or Double, returns a new Date that is
incremented by the specified number of days, with the fractional portion
corresponding to a portion of a day.

**•** If `x` is a String and `y` is a String or any other type of non- `null` argument,
concatenates `y` to the end of `x` .

`-` `x - y` **Subtraction operator** . Subtracts the value of `y` from the value of `x` according to
the following rules:

**•** If `x` and `y` are Integers or Doubles, the operator subtracts the value of `y` from
the value of `x` . If a Double is used, the result is a Double.

**•** If `x` is a Date and `y` is an Integer, returns a new Date that is decremented by
the specified number of days.

**•** If `x` is a Datetime and `y` is an Integer or Double, returns a new Date that is
decremented by the specified number of days, with the fractional portion
corresponding to a portion of a day.


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

`*` `x * y` **Multiplication operator** . Multiplies `x`, an Integer or Double, with `y`, another
Integer or Double. If a double is used, the result is a Double.

`/` `x / y` **Division operator** . Divides `x`, an Integer or Double, by `y`, another Integer or Double.
If a double is used, the result is a Double.

`!` `!x` **Logical complement operator** . Inverts the value of a Boolean so that true becomes
false and false becomes true.

```
- -x

```

```
++

-
```

```
x++

++x

x-
--x

```

**Unary negation operator** . Multiplies the value of `x`, an Integer or Double, by -1.
The positive equivalent `+` is also syntactically valid but doesn’t have a mathematical
effect.

**Increment operator** . Adds 1 to the value of `x`, a variable of a numeric type. If
prefixed ( `++x` ), the expression evaluates to the value of x after the increment. If
postfixed ( `x++` ), the expression evaluates to the value of x before the increment.

**Decrement operator** . Subtracts 1 from the value of `x`, a variable of a numeric type.
If prefixed ( `--x` ), the expression evaluates to the value of x after the decrement. If
postfixed ( `x--` ), the expression evaluates to the value of x before the decrement.

`&` `x & y` **Bitwise AND operator** . ANDs each bit in `x` with the corresponding bit in `y` so
that the result bit is set to 1 if both of the bits are set to 1.

`|` `x | y` **Bitwise OR operator** . ORs each bit in `x` with the corresponding bit in `y` so that
the result bit is set to 1 if at least one of the bits is set to 1.

```
^ x ^ y

^= x ^= y

```

**Bitwise exclusive OR operator** . Exclusive ORs each bit in `x` with the corresponding
bit in `y` so that the result bit is set to 1 if exactly one of the bits is set to 1 and the
other bit is set to 0.

**Bitwise exclusive OR operator** . Exclusive ORs each bit in `x` with the corresponding
bit in `y` so that the result bit is set to 1 if exactly one of the bits is set to 1 and the
other bit is set to 0. Assigns the result of the exclusive OR operation to `x` .

`<<` `x << y` **Bitwise shift left operator** . Shifts each bit in `x` to the left by `y` bits so that the
high-order bits are lost and the new right bits are set to 0.

```
>> x >> y

>>> x >>> y

~ ~x

```

**Bitwise shift right signed operator** . Shifts each bit in `x` to the right by `y` bits so
that the low-order bits are lost and the new left bits are set to 0 for positive values
of `y` and 1 for negative values of `y` .

**Bitwise shift right unsigned operator** . Shifts each bit in `x` to the right by `y` bits
so that the low-order bits are lost and the new left bits are set to 0 for all values of
`y` .

**Bitwise Not or Complement operator** . Toggles each binary digit of `x`, converting
0 to 1 and 1 to 0. Boolean values are converted from `True` to `False` and vice
versa.

`()` `(x)` **Parentheses** . Elevates the precedence of an expression `x` so that it’s evaluated
first in a compound expression.


Apex Developer Guide Data Types and Variables

**Operator** **Syntax** **Description**

`?.` x?.y **Safe navigation operator** . Short-circuits expressions that attempt to operate on
a null value, and returns null instead of throwing a NullPointerException. If the

left-hand side of the chain expression evaluates to null, the right-hand side of the
chain expression isn’t evaluated.

##### Safe Navigation Operator

Use the safe navigation operator ( `?.` ) to replace explicit, sequential checks for null references. This operator short-circuits expressions
that attempt to operate on a null value and returns null instead of throwing a NullPointerException.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

If the left-hand-side of the chain expression evaluates to null, the right-hand-side isn’t evaluated. Use the safe navigation operator ( `?.` )
in method, variable, and property chaining. The part of the expression that isn’t evaluated can include variable references, method
references, or array expressions.

Note: All Apex types are implicitly nullable and can hold a null value returned from the operator.

Examples

**•** This example first evaluates `a`, and returns null if `a` is null. Otherwise the return value is `a.b` .

```
     a?.b // Evaluates to: a == null ? null : a.b

```

**•** This example returns null if `a[x]` evaluates to null. If `a[x]` doesn’t evaluate to null and `aMethod()` returns null, then this
expression throws a NullPointerException.

```
     a[x]?.aMethod().aField // Evaluates to null if a[x] == null

```

**•** This example returns null if `a[x].aMethod()` evaluates to null.

```
     a[x].aMethod()?.aField

```

**•** This example indicates that the type of the expression is the same whether the safe navigation operator is used in the expression or
not.

```
     Integer x = anObject?.anIntegerField; // The expression is of type Integer because the

      field is of type Integer

```

**•** This example shows a single statement replacing a block of code that checks for nulls.

```
     // Previous code checking for nulls

     String profileUrl = null;

     if (user.getProfileUrl() != null) {

       profileUrl = user.getProfileUrl().toExternalForm();

     }

     // New code using the safe navigation operator

     String profileUrl = user.getProfileUrl()?.toExternalForm();

```


Apex Developer Guide Data Types and Variables

**•** This example shows a single-row SOQL query using the safe navigation operator.

```
     // Previous code checking for nulls

     results = [SELECT Name FROM Account WHERE Id = :accId];

     if (results.size() == 0) { // Account was deleted

       return null;

     }

     return results[0].Name;

     // New code using the safe navigation operator

     return [SELECT Name FROM Account WHERE Id = :accId]?.Name;

```

**Table 1: Safe Navigation Operator Use-Cases**


Apex Developer Guide Data Types and Variables

You can’t use the Safe Navigation Operator in certain cases. Attempting to use the operator in these ways causes an error during
compilation:

**•** Types and static expressions with dots. For example:

**–** Namespaces

**–** {Namespace}.{Class}

**–** Trigger.new

**–** Flow.interview.{flowName}

**–** {Type}.class

**•** Static variable access, method calls, and expressions. For example:

**–** `AClass.AStaticMethodCall()`

**–** `AClass.AStaticVariable`

**–** `String.format('{0}', 'hello` `world')`

**–** `Page.{pageName}`

**•** Assignable expressions. For example:

**–** `foo?.bar = 42;`

**–** `++foo?.bar;`

**•** SOQL bind expressions. For example:

```
     class X { public String query = 'xyz';}

     X x = new X();

     List<Account> accounts = [SELECT Name FROM Account WHERE Name = :X?.query]

     List<List<SObject>> moreAccounts = [FIND :X?.query IN ALL FIELDS

       RETURNING Account(Name)];

```

**•** With `addError()` on SObject scalar fields. For example:

```
     Contact c;

     c.LastName?.addError('The field must have a value');

```

Note: You can use the operator with `addError()` on SObjects, including lookup and master-detail fields.


Apex Developer Guide Data Types and Variables

##### Null Coalescing Operator

The `??` operator returns its right-hand side operand when its left-hand side operand is null. Similar to the safe navigation operator ( `?.` ),
the null coalescing operator ( `??` ) replaces verbose and explicit checks for null references in code.

The null coalescing operator is a binary operator in the form `a ?? b` that returns `a` if _`a`_ isn’t null, and otherwise returns _`b`_ . The operator
is left-associative. The left-hand operand is evaluated only one time. The right-hand operand is only evaluated if the left-hand operand
is null.

You must ensure type compatibility between the operands. For example, in the expression: `objectZ result = objectA ??`
`objectB`, both _`objectA`_ and _`objectB`_ must be instances of objectZ to avoid a compile-time error.

Here’s a comparison that illustrates the operator usage. Before the Null Coalescing Operator, you used:

```
   Integer notNullReturnValue = (anInteger != null) ? anInteger : 100;

```

With the Null Coalescing Operator, use:

```
   Integer notNullReturnValue = anInteger ?? 100;

```

While using the null coalescing operator, always keep operator precedence in mind. In some cases, using parentheses is necessary to
obtain the desired results. For example, the expression `top ?? 100 - bottom ?? 0` evaluates to `top ?? (100 - bottom`
`?? 0)` and not to `(top ?? 100) - (bottom ?? 0)` .

Apex supports assignment of a single resultant record from a SOQL query, but throws an exception if there are no rows returned by the
query. The null coalescing operator can be used to gracefully deal with the case where the query doesn’t return any rows. If a SOQL
query is used as the left-hand operand of the operator and rows are returned, then the null coalescing operator returns the query results.
If no rows are returned, the null coalescing operator returns the right-hand operand.

Warning: Salesforce recommends against using multiple SOQL queries in a single statement that also uses the null coalescing
operator.

These examples work with Account objects.

```
   Account defaultAccount = new Account(name = 'Acme');

   // Left operand SOQL is empty, return defaultAccount from right operand:

   Account a = [SELECT Id FROM Account

     WHERE Id = '001000000FAKEID'] ?? defaultAccount;

   Assert.areEqual(defaultAccount, a);

   // If there isn't a matching Account or the Billing City is null, replace the value

   string city = [Select BillingCity

      From Account

      Where Id = '001xx000000001oAAA']?.BillingCity;

   System.debug('Matches count: ' + city?.countMatches('San Francisco') ?? 0 );

```

Usage

There are some restrictions on using the null coalescing operator.

**•** You can’t use the null coalescing operator as the left side of an assignment operator in an assignment.

**–** `foo??bar = 42;// This is not a valid assignment`

**–** `foo??bar++; // This is not a valid assignment`


Apex Developer Guide Data Types and Variables

**•** SOQL bind expressions don’t support the null coalescing operator.

```
     class X { public String query = 'xyz';}

     X x = new X();

     List<Account> accounts = [SELECT Name FROM Account WHERE Name = :X??query]

     List<List<SObject>> moreAccounts = [FIND :X??query IN ALL FIELDS

       RETURNING Account(Name)];

```

SEE ALSO:

##### Operator Precedence

Using SOQL Queries That Return One Record

##### Operator Precedence

Operators are interpreted in order, according to rules.

Apex uses the following operator precedence rules:

**Precedence** **Operators** **Description**

1 `{} () ++ --` Grouping and prefix increments and decrements

2 `~ ! -x +x (type) new` Unary operators, additive operators, type cast and object
creation

3 `* /` Multiplication and division

4 `+ -` Addition and subtraction

5 `<< >> >>>` Shift Operators

6 `< <= > >= instanceof` Greater-than and less-than comparisons, reference tests

7 `== !=` Comparisons: equal and not-equal

8 `&` Bitwise AND

9 `^` Bitwise XOR

10 `|` Bitwise OR

11 `&&` Logical AND

12 `||` Logical OR

13 `??` Null Coalescing

14 `?:` Ternary

15 `= += -= *= /= &= <<= >>= >>>=` Assignment operators

##### Comments

Both single and multiline comments are supported in Apex code.


Apex Developer Guide Data Types and Variables

Tip: We recommend using the standardized ApexDoc comment format to increase code readability, collaboration, and long-term
maintainability. For the full specifications, see Document Your Apex Code on page 245.

**•** To create a single line comment, use `//` . All characters on the same line to the right of the `//` are ignored by the parser. For example:

```
     Integer i = 1; // This comment is ignored by the parser

```

**•** To create a multiline comment, use `/*` and `*/` to demarcate the beginning and end of the comment block. For example:

```
     Integer i = 1; /* This comment can wrap over multiple

                lines without getting interpreted by the

                parser. */

#### Assignment Statements

```

An assignment statement is any statement that places a value into a variable.

An assignment statement generally takes one of two forms:

```
   [LValue] = [new_value_expression];

   [LValue] = [[inline_soql_query]];

```

In the forms above, `[LValue]` stands for any expression that can be placed on the left side of an assignment operator. These include:

**•** A simple variable. For example:

```
     Integer i = 1;

     Account a = new Account();

     Account[] accts = [SELECT Id FROM Account];

```

**•** A de-referenced list element. For example:

```
     ints[0] = 1;

     accts[0].Name = 'Acme';

```

**•** An sObject field reference that the context user has permission to edit. For example:

```
     Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');

     // IDs cannot be set prior to an insert call

     // a.Id = '00300000003T2PGAA0';

     // Instead, insert the record. The system automatically assigns it an ID.

     insert a;

     // Fields also must be writable for the context user

     // a.CreatedDate = System.today(); This code is invalid because

     // createdDate is read-only!

     // Since the account a has been inserted, it is now possible to

     // create a new contact that is related to it

     Contact c = new Contact(LastName = 'Roth', Account = a);

     // Notice that you can write to the account name directly through the contact

     c.Account.Name = 'salesforce.com';

```


Apex Developer Guide Data Types and Variables

Assignment is always done by reference. For example:

```
   Account a = new Account();

   Account b;

   Account[] c = new Account[]{};

   a.Name = 'Acme';

   b = a;

   c.add(a);

   // These asserts should now be true. You can reference the data

   // originally allocated to account a through account b and account list c.

   System.assertEquals(b.Name, 'Acme');

   System.assertEquals(c[0].Name, 'Acme');

```

Similarly, two lists can point at the same value in memory. For example:

```
   Account[] a = new Account[]{new Account()};

   Account[] b = a;

   a[0].Name = 'Acme';

   System.assert(b[0].Name == 'Acme');

```

In addition to `=`, other valid assignment operators include `+=`, `*=`, `/=`, `|=`, `&=`, `++`, and `--` . See Expression Operators on page 40.

#### Rules of Conversion

In general, Apex requires you to explicitly convert one data type to another. For example, a variable of the Integer data type cannot be
implicitly converted to a String. You must use the `string.format` method. However, a few data types can be implicitly converted,
without using a method.

Numbers form a hierarchy of types. Variables of lower numeric types can always be assigned to higher types without explicit conversion.
The following is the hierarchy for numbers, from lowest to highest:

**1.** Integer

**2.** Long

**3.** Double

**4.** Decimal

Note: Once a value has been passed from a number of a lower type to a number of a higher type, the value is converted to the
higher type of number.

Note that the hierarchy and implicit conversion is unlike the Java hierarchy of numbers, where the base interface number is used and
implicit object conversion is never allowed.

In addition to numbers, other data types can be implicitly converted. The following rules apply:

**•** IDs can always be assigned to Strings.

**•** Strings can be assigned to IDs. However, at runtime, the value is checked to ensure that it is a legitimate ID. If it is not, a runtime
exception is thrown.

**•** The `instanceOf` keyword can always be used to test whether a string is an ID.


### Apex Developer Guide Control Flow Statements

Additional Considerations for Data Types

**Data Types of Numeric Values**
Numeric values represent Integer values unless they are appended with L for a Long or with .0 for a Double or Decimal. For example,
the expression `Long d = 123;` declares a Long variable named d and assigns it to an Integer numeric value (123), which is
implicitly converted to a Long. The Integer value on the right hand side is within the range for Integers and the assignment succeeds.
However, if the numeric value on the right hand side exceeds the maximum value for an Integer, you get a compilation error. In this
case, the solution is to append L to the numeric value so that it represents a Long value which has a wider range, as shown in this
example: `Long d = 2147483648L;` .

**Overflow and Underflow of Data Type Values**
Arithmetic computations that produce values larger than the maximum value of the current type are said to overflow and values
lower than the minimum value of the current type are said to be underflow. Apex doesn’t throw an exception for overflow and
underflow of data type values. For example, `Integer i = 2147483647 + 1;` yields a value of –2147483648 because
2147483647 is the maximum value for an Integer, so adding one to it wraps the value around to the minimum negative value for
Integers: –2147483648. Similarly, subtracting one from the minimum integer -2,147,483,648 wraps the value around to the maximum
value for Integers: 2,147,483,647.

If arithmetic computations generate results larger than the maximum value for the current type, the end result will be incorrect
because the computed values that are larger than the maximum will overflow. For example, the expression `Long MillsPerYear`
`= 365 * 24 * 60 * 60 * 1000;` results in an incorrect result because the products of Integers on the right hand side
are larger than the maximum Integer value and they overflow. As a result, the final product isn't the expected one. You can avoid
this by ensuring that the type of numeric values or variables you are using in arithmetic operations are large enough to hold the
results. In this example, append L to numeric values to make them Long so the intermediate products will be Long as well and no
overflow occurs. The following example shows how to correctly compute the amount of milliseconds in a year by multiplying Long
numeric values.

```
     Long MillsPerYear = 365L * 24L * 60L * 60L * 1000L;

     Long ExpectedValue = 31536000000L;

     System.assertEquals(MillsPerYear, ExpectedValue);

```

**Loss of Fractions in Divisions**
When dividing numeric Integer or Long values, the fractional portion of the result, if any, is removed before performing any implicit
conversions to a Double or Decimal. For example, `Double d = 5/3;` returns 1.0 because the actual result (1.666...) is an Integer
and is rounded to 1 before being implicitly converted to a Double. To preserve the fractional value, ensure that you are using Double
or Decimal numeric values in the division. For example, `Double d = 5.0/3.0;` returns 1.6666666666666667 because 5.0
and 3.0 represent Double values, which results in the quotient being a Double as well and no fractional value is lost.

**Conversion of Date to Datetime**
Apex supports both implicit and explicit casting of Date values to Datetime, with the time component being zeroed out in the
resulting Datetime value.

### Control Flow Statements

Apex provides if-else statements, switch statements, and loops to control the flow of code execution. Statements are generally executed
line by line, in the order they appear. With control flow statements, you can make Apex code execute based on a certain condition, or
have a block of code execute repeatedly.

Conditional (If-Else) Statements
The conditional statement in Apex works similarly to Java.


Apex Developer Guide Control Flow Statements

#### Switch Statements

Apex provides a `switch` statement that tests whether an expression matches one of several values and branches accordingly.

Loops
Apex supports five types of procedural loops.

#### Conditional (If-Else) Statements

The conditional statement in Apex works similarly to Java.

```
   if ([Boolean_condition])

      // Statement 1

   else

      // Statement 2

```

The `else` portion is always optional, and always groups with the closest `if` . For example:

```
   Integer x, sign;

   // Your code

   if (x <= 0) if (x == 0) sign = 0; else sign = -1;

```

is equivalent to:

```
   Integer x, sign;

   // Your code

   if (x <= 0) {

      if (x == 0) {

          sign = 0;

      } else {

          sign = -1;

      }

   }

```

Repeated `else if` statements are also allowed. For example:

```
   if (place == 1) {

      medal_color = 'gold';

   } else if (place == 2) {

      medal_color = 'silver';

   } else if (place == 3) {

      medal_color = 'bronze';

   } else {

      medal_color = null;

   }

#### Switch Statements

```

Apex provides a `switch` statement that tests whether an expression matches one of several values and branches accordingly.

The syntax is:

```
   switch on expression {

      when value1 { // when block 1

        // code block 1

      }

      when value2 { // when block 2

```


Apex Developer Guide Control Flow Statements

```
        // code block 2

      }

      when value3 { // when block 3

        // code block 3

      }

      when else { // default block, optional

        // code block 4

      }

   }

```

The `when` value can be a single value, multiple values, or sObject types. For example:

```
   when value1 {

   }

   when value2, value3 {

   }

   when TypeName VariableName {

   }

```

The `switch` statement evaluates the expression and executes the code block for the matching `when` value. If no value matches, the
`when else` code block is executed. If there isn’t a `when else` block, no action is taken.

Note: There is no fall-through. After the code block is executed, the `switch` statement exits.

Apex `switch` statement expressions can be one of the following types.

**•** Integer

**•** Long

**•** sObject

**•** String

**•** Enum

When Blocks

Each `when` block has a value that the expression is matched against. These values can take one of the following forms.

**•** when `literal` {} (a when block can have multiple, comma-separated literal clauses)

**•** when SObjectType `identifier` {}

**•** when `enum_value` {}

The value `null` is a legal value for all types.

Each `when` value must be unique. For example, you can use the literal _`x`_ only in one `when` block clause. A `when` block is matched
one time at most.

When Else Block

If no `when` values match the expression, the `when else` block is executed.

Note: Salesforce recommends including a `when else` block, especially with enum types, although it isn’t required. When you
build a `switch` statement using enum values provided by a managed package, your code might not behave as expected if a


Apex Developer Guide Control Flow Statements

new version of the package contains additional enum values. You can prevent this problem by including a `when else` block
to handle unanticipated values.

If you include a `when else` block, it must be the last block in the `switch` statement.

Examples with Literals

You can use literal `when` values for switching on Integer, Long, and String types. String clauses are case-sensitive. For example, “orange”
is a different value than “ORANGE.”

**Single Value Example**

The following example uses integer literals for `when` values.

```
   switch on i {

     when 2 {

        System.debug('when block 2');

     }

     when -3 {

        System.debug('when block -3');

     }

     when else {

        System.debug('default');

     }

   }

```

**Null Value Example**

Because all types in Apex are nullable, a `when` value can be `null` .

```
   switch on i {

     when 2 {

        System.debug('when block 2');

     }

     when null {

        System.debug('bad integer');

     }

     when else {

        System.debug('default ' + i);

     }

   }

```

**Multiple Values Examples**

The Apex `switch` statement doesn’t fall-through, but a `when` clause can include multiple literal values to match against. You can
also nest Apex `switch` statements to provide multiple execution paths within a `when` clause.

```
   switch on i {

     when 2, 3, 4 {

        System.debug('when block 2 and 3 and 4');

     }

     when 5, 6 {

        System.debug('when block 5 and 6');

     }

     when 7 {

        System.debug('when block 7');

     }

```


Apex Developer Guide Control Flow Statements

```
     when else {

        System.debug('default');

     }

   }

```

**Method Example**

Instead of switching on a variable expression, the following example switches on the result of a method call.

```
   switch on someInteger(i) {

     when 2 {

        System.debug('when block 2');

     }

     when 3 {

        System.debug('when block 3');

     }

     when else {

        System.debug('default');

     }

   }

```

Example with sObjects

Switching on an sObject value allows you to implicitly perform `instanceof` checks and casting. For example, consider the following
code that uses if-else statements.

```
   if (sobject instanceof Account) {

      Account a = (Account) sobject;

      System.debug('account ' + a);

   } else if (sobject instanceof Contact) {

      Contact c = (Contact) sobject;

      System.debug('contact ' + c);

   } else {

      System.debug('default');

   }

```

You can replace and simplify this code with the following `switch` statement.

```
   switch on sobject {

     when Account a {

        System.debug('account ' + a);

     }

     when Contact c {

        System.debug('contact ' + c);

     }

     when null {

        System.debug('null');

     }

     when else {

        System.debug('default');

     }

   }

```

Note: You can use only one sObject type per `when` block.


Apex Developer Guide Control Flow Statements

Example with Enums

A `switch` statement that uses enum `when` values doesn’t require a `when else` block, but it is recommended. You can use multiple
enum values per `when` block clause.

```
   switch on season {

     when WINTER {

        System.debug('boots');

     }

     when SPRING, SUMMER {

        System.debug('sandals');

     }

     when else {

        System.debug('none of the above');

     }

   }

#### Loops

```

Apex supports five types of procedural loops.

These types of procedural loops are supported:

**•** `do {` _**`statement`**_ `} while (` _**`Boolean_condition`**_ `);`

**•** `while (` _**`Boolean_condition`**_ `)` _**`statement`**_ `;`

**•** `for (` _**`initialization`**_ `;` _**`Boolean_exit_condition`**_ `;` _**`increment`**_ `)` _**`statement`**_ `;`

**•** `for (` _**`variable`**_ `:` _**`array_or_set`**_ `)` _**`statement`**_ `;`

**•** `for (` _**`variable`**_ `: [` _**`inline_soql_query`**_ `])` _**`statement`**_ `;`

All loops allow for loop control structures:

**•** `break;` exits the entire loop

**•** `continue;` skips to the next iteration of the loop

##### 1. Do-While Loops

2. While Loops

3. For Loops

##### Do-While Loops

The Apex `do-while` loop repeatedly executes a block of code as long as a particular Boolean condition remains true. Its syntax is:

```
   do {

     code_block

   } while (condition);

```

Note: Curly braces ( `{}` ) are always required around a _**`code_block`**_ .

As in Java, the Apex `do-while` loop does not check the Boolean condition statement until after the first loop is executed. Consequently,
the code block always runs at least once.


Apex Developer Guide Control Flow Statements

As an example, the following code outputs the numbers 1 - 10 into the debug log:

```
   Integer count = 1;

   do {

      System.debug(count);

      count++;

   } while (count < 11);

##### While Loops

```

The Apex `while` loop repeatedly executes a block of code as long as a particular Boolean condition remains true. Its syntax is:

```
   while (condition) {

     code_block

   }

```

Note: Curly braces ( `{}` ) are required around a _**`code_block`**_ only if the block contains more than one statement.

Unlike `do-while`, the `while` loop checks the Boolean condition statement before the first loop is executed. Consequently, it is
possible for the code block to never execute.

As an example, the following code outputs the numbers 1 - 10 into the debug log:

```
   Integer count = 1;

   while (count < 11) {

      System.debug(count);

      count++;

   }

##### For Loops

```

Apex supports three variations of the `for` loop:

**•** The traditional `for` loop:

```
     for ( init_stmt ; exit_condition ; increment_stmt ) {

       code_block

     }

```

**•** The list or set iteration `for` loop:

```
     for ( variable : list_or_set ) {

       code_block

     }

```

where _**`variable`**_ must be of the same primitive or sObject type as _**`list_or_set`**_ .

**•** The SOQL `for` loop:

```
     for ( variable : [ soql_query ]) {

       code_block

     }

```


Apex Developer Guide Control Flow Statements

or

```
     for ( variable_list : [ soql_query ]) {

       code_block

     }

```

Both _**`variable`**_ and _**`variable_list`**_ must be of the same sObject type as is returned by the _**`soql_query`**_ .

Note: Curly braces ( `{}` ) are required around a _**`code_block`**_ only if the block contains more than one statement.

Each is discussed further in the sections that follow.

###### Traditional For Loops List or Set Iteration for Loops

Iterating Collections

###### Traditional For Loops

The traditional `for` loop in Apex corresponds to the traditional syntax used in Java and other languages. Its syntax is:

```
   for ( init_stmt ; exit_condition ; increment_stmt ) {

     code_block

   }

```

When executing this type of `for` loop, the Apex runtime engine performs the following steps, in order:

**1.** Execute the _**`init_stmt`**_ component of the loop. Note that multiple variables can be declared and/or initialized in this statement,
separated by commas.

**2.** Perform the _**`exit_condition`**_ check. If true, the loop continues. If false, the loop exits.

**3.** Execute the _**`code_block`**_ .

**4.** Execute the _**`increment_stmt`**_ statement.

**5.** Return to Step 2.

As an example, the following code outputs the numbers 1 - 10 into the debug log. Note that an additional initialization variable, `j`, is
included to demonstrate the syntax:

```
   for (Integer i = 0, j = 0; i < 10; i++) {

      System.debug(i+1);

   }

###### List or Set Iteration for Loops

```

The list or set iteration `for` loop iterates over all the elements in a list or set. Its syntax is:

```
   for ( variable : list_or_set ) {

     code_block

   }

```

where _**`variable`**_ must be of the same primitive or sObject type as _**`list_or_set`**_ .

When executing this type of `for` loop, the Apex runtime engine assigns _**`variable`**_ to each element in _**`list_or_set`**_, and
runs the _**`code_block`**_ for each value.


### Apex Developer Guide Classes, Objects, and Interfaces

For example, the following code outputs the numbers 1 - 10 to the debug log:

```
   Integer[] myInts = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

   for (Integer i : myInts) {

      System.debug(i);

   }

###### Iterating Collections

```

Collections can consist of lists, sets, or maps. Modifying a collection's elements while iterating through that collection is not supported
and causes an error. Do not directly add or remove elements while iterating through the collection that includes them.

Adding Elements During Iteration

To add elements while iterating a list, set or map, keep the new elements in a temporary list, set, or map and add them to the original
after you finish iterating the collection.

Removing Elements During Iteration

To remove elements while iterating a list, create a new list, then copy the elements you wish to keep. Alternatively, add the elements
you wish to remove to a temporary list and remove them after you finish iterating the collection.

Note: The `List.remove` method performs linearly. Using it to remove elements has time and resource implications.

To remove elements while iterating a map or set, keep the keys you wish to remove in a temporary list, then remove them after you
finish iterating the collection.

### Classes, Objects, and Interfaces

Apex classes are modeled on their counterparts in Java. You’ll define, instantiate, and extend classes, and you’ll work with interfaces,
Apex class versions, properties, and other related class concepts.

### 1. Classes

As in Java, you can create classes in Apex. A _class_ is a template or blueprint from which objects are created. An _object_ is an instance
of a class.

2. Interfaces
An _interface_ is like a class in which none of the methods have been implemented—the method signatures are there, but the body
of each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained
in the interface.

3. Keywords
Apex provides the keywords `final`, `instanceof`, `super`, `this`, `transient`, `with sharing` and `without`
`sharing` .

4. Annotations
An Apex annotation modifies the way that a method or class is used, similar to annotations in Java. Annotations are defined with
an initial `@` symbol, followed by the appropriate keyword.


#### Apex Developer Guide Classes, Objects, and Interfaces 5. Classes and Casting

In general, all type information is available at run time. This means that Apex enables _casting_, that is, a data type of one class can be
assigned to a data type of another class, but only if one class is a subclass of the other class. Use casting when you want to convert
an object from one data type to another.

6. Differences Between Apex Classes and Java Classes
Apex classes and Java classes work in similar ways, but there are some significant differences.

7. Class Definition Creation
Use the class editor to create a class in Salesforce.

8. Namespace Prefix
The Salesforce application supports the use of _namespace prefixes_ . Namespace prefixes are used in managed AppExchange packages
to differentiate custom object and field names from names used by other organizations.

9. Apex Code Versions
To aid backwards-compatibility, classes and triggers are stored with the version settings for a specific Salesforce API version.

10. Lists of Custom Types and Sorting

Lists can hold objects of your user-defined types (your Apex classes). Lists of user-defined types can be sorted.

11. Using Custom Types in Map Keys and Sets

You can add instances of your own Apex classes to maps and sets.

#### Classes

As in Java, you can create classes in Apex. A _class_ is a template or blueprint from which objects are created. An _object_ is an instance of a
class.

For example, the `PurchaseOrder` class describes an entire purchase order, and everything that you can do with a purchase order.
An instance of the `PurchaseOrder` class is a specific purchase order that you send or receive.

All objects have _state_ and _behavior_, that is, things that an object knows about itself, and things that an object can do. The state of a
PurchaseOrder object—what it knows—includes the user who sent it, the date and time it was created, and whether it was flagged as
important. The behavior of a PurchaseOrder object—what it can do—includes checking inventory, shipping a product, or notifying a
customer.

A class can contain variables and methods. Variables are used to specify the state of an object, such as the object's `Name` or `Type` .
Since these variables are associated with a class and are members of it, they are commonly referred to as _member variables_ . Methods
are used to control behavior, such as `getOtherQuotes` or `copyLineItems` .

A class can contain other classes, exception types, and initialization code.

An _interface_ is like a class in which none of the methods have been implemented—the method signatures are there, but the body of
each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained in the
interface.

[For more general information on classes, objects, and interfaces, see http://java.sun.com/docs/books/tutorial/java/concepts/index.html](http://java.sun.com/docs/books/tutorial/java/concepts/index.html)

In addition to classes, Apex provides triggers, similar to database triggers. A trigger is Apex code that executes before or after database
operations. See Triggers.

1. Apex Class Definition

2. Class Variables


Apex Developer Guide Classes, Objects, and Interfaces

3. Class Methods
Learn how to define Apex methods. Understand the differences between passing method arguments by value and passing method
arguments by reference.

4. Using Constructors

5. Access Modifiers

6. Static and Instance Methods, Variables, and Initialization Code
In Apex, you can have _static_ methods, variables, and initialization code. However, Apex classes can't be static. You can also have
_instance_ methods, member variables, and initialization code, which have no modifiers, and _local_ variables.

7. Apex Properties

8. Extending a Class
You can extend a class to provide more specialized behavior.

9. Extended Class Example

##### Apex Class Definition

In Apex, you can define top-level classes (also called outer classes) as well as inner classes, that is, a class defined within another class.
You can only have inner classes one level deep. For example:

```
   public class myOuterClass {

     // Additional myOuterClass code here

     class myInnerClass {

      // myInnerClass code here

     }

   }

```

To define a class, specify the following:

**1.** Access modifiers:

**•** You must use one of the access modifiers (such as `public` or `global` ) in the declaration of a top-level class.

**•** You don’t have to use an access modifier in the declaration of an inner class.

**2.** Optional definition modifiers (such as `virtual`, `abstract`, and so on)

**3.** Required: The keyword `class` followed by the name of the class

**4.** Optional extensions or implementations or both

Note: Avoid using standard object names for class names. Doing so causes unexpected results. For a list of standard objects, see
[Object Reference for Salesforce.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/)

Use the following syntax for defining classes:

```
   private | public | global

   [virtual | abstract | with sharing | without sharing]

   class ClassName [implements InterfaceNameList ] [extends ClassName ]

   {

   // The body of the class

   }

```

**•** The `private` access modifier declares that this class is only known locally, that is, only by this section of code. This is the default
access for inner classes—that is, if you don't specify an access modifier for an inner class, it’s considered `private` . This keyword
can only be used with inner classes (or with top-level test classes marked with the `@IsTest` annotation).


Apex Developer Guide Classes, Objects, and Interfaces

**•** The `public` access modifier declares that this class is visible in your application or namespace.

**•** The `global` access modifier declares that this class is known by all Apex code everywhere. All classes containing methods defined
with the `webservice` keyword must be declared as `global` . If a method or inner class is declared as `global`, the outer,
top-level class must also be defined as `global` .

**•** The `with sharing` and `without sharing` keywords specify the sharing mode for this class. For more information, see
Use the with sharing, without sharing, and inherited sharing Keywords on page 90.

**•** The `virtual` definition modifier declares that this class allows extension and overrides. You can’t override a method with the

`override` keyword unless the class has been defined as `virtual` .

**•** The `abstract` definition modifier declares that this class contains abstract methods, that is, methods that only have their signature
declared and no body defined.

Note:

**•** You can’t add an abstract method to a global class after the class has been uploaded in a Managed - Released package version.

**•** If the class in the Managed - Released package is virtual, the method that you can add to it must also be virtual and must have
an implementation.

**•** You can’t override a public or protected virtual method of a global class of an installed managed package.

For more information about managed packages, see Managed Package Types on page 766.

A class can implement multiple interfaces, but only extend one existing class. This restriction means that Apex doesn’t support multiple
inheritance. The interface names in the list are separated by commas. For more information about interfaces, see Interfaces on page 82.

For more information about method and variable access modifiers, see Access Modifiers on page 69.

Versioned Behavior Changes

In API version 65.0 and later, an abstract or override method requires a `protected`, `public`, or `global` access modifier. If one of
these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is
invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare
an abstract or override method without an allowed access modifier, you get the compilation error `Abstract methods require`
`at least one of the following: global, public, protected` .

In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass.
This change is versioned, so to prevent the override, update your abstract or virtual classes that contain private methods to API version
61.0 or later. In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in
one of its superclasses, the subclass method overrides the private method.

SEE ALSO:

Documentation Typographical Conventions

_Salesforce Help_ [: Manage Apex Classes](https://help.salesforce.com/articleView?id=code_manage_packages.htm&language=en_US)

_Salesforce Help_ [: Developer Console Functionality](https://help.salesforce.com/articleView?id=code_system_log.htm&language=en_US)

##### Class Variables

To declare a variable, specify the following:

**•** Optional: Modifiers, such as `public` or `final`, as well as `static` .

**•** Required: The data type of the variable, such as String or Boolean.

**•** Required: The name of the variable.


Apex Developer Guide Classes, Objects, and Interfaces

**•** Optional: The value of the variable.

Use the following syntax when defining a variable:

```
   [public | private | protected | global] [final] [static] data_type variable_name

   [= value ]

```

For example:

```
       private static final Integer MY_INT;

       private final Integer i = 1;

```

Versioned Behavior Changes

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation. For more
[information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

##### Class Methods

Learn how to define Apex methods. Understand the differences between passing method arguments by value and passing method
arguments by reference.

Apex methods are comprised of these elements.

**•** Optional: Modifiers, such as `public` or `protected` .

**•** Required: The data type of the value returned by the method, such as String or Integer. Use `void` if the method doesn’t return a
value.

**•** Required: A list of input parameters for the method, separated by commas, each preceded by its data type, and enclosed in parentheses
`()` . If there are no parameters, use a set of empty parentheses. A method can only have 32 input parameters.

**•** Required: The body of the method, enclosed in braces `{}` . All the code for the method, including any local variable declarations, is
contained here.

Note: All Apex types implement the Object class methods.

To define a method, use this syntax.

```
   [public | private | protected | global] [override] [static] data_type method_name ( input

    parameters ) {

      // The body of the method

   }

```

Note: You can use `override` to override methods only in classes that have been defined as `virtual` or `abstract` .

This method has the correct syntax.:

```
     public static Integer getInt() {

      return MY_INT;

   }

```

As in Java, methods that return values can also be run as a statement if their results aren’t assigned to another variable.

User-defined methods:

**•** Can be used anywhere that system methods are used.

**•** Can be recursive.


Apex Developer Guide Classes, Objects, and Interfaces

**•** Can have side effects, such as DML `insert` [statements that initialize sObject record IDs. See Apex DML Statements.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm#apex_dml)

**•** Can refer to themselves or to methods defined later in the same class or anonymous block. Apex parses methods in two phases, so
forward declarations aren’t needed.

**•** Can be overloaded. For example, a method named `example` can be implemented in two ways, one with a single Integer parameter
and one with two Integer parameters. Depending on whether the method is called with one or two Integers, the Apex parser selects
the appropriate implementation to execute. If the parser can’t find an exact match, it then seeks an approximate match using type
coercion rules. For more information on data conversion, see Rules of Conversion on page 52.

Note: If the parser finds multiple approximate matches, a parse-time exception is generated.

**•** Methods with a void return type are typically invoked as a standalone statement in Apex code. For example:

```
     System.debug('Here is a note for the log.');

```

**•** Can have statements where the return values are run as a statement if their results aren’t assigned to another variable. This rule is
the same in Java.

Note: All user-defined types support the `clone` method. The `clone()` [method in Apex is based on the clone method in](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)
[Java.](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

Passing Method Arguments by Value

In Apex, primitive data type arguments, such as Integer or String, are passed into methods by value. This fact means that any changes
to the arguments exist only within the scope of the method. When the method returns, the changes to the arguments are lost.

Non-primitive data type arguments, such as sObjects, are passed into methods by reference. Therefore, when the method returns, the
passed-in argument still references the same object as before the method call. Within the method, the reference can't be changed to
point to another object but the values of the object's fields can be changed.

These examples demonstrate the differences between passing primitive and non-primitive data type arguments into methods.

**Example: Passing Primitive Data Type Arguments**

This example shows how a primitive argument of type String is passed by value into another method. The `debugStatusMessage`
method in this example creates a String variable, _`msg`_, and assigns it a value. It then passes this variable as an argument to another
method, which modifies the value of this String. However, because String is a primitive type, it’s passed by value, and when the method
returns, the value of the original variable, _`msg`_, is unchanged. An assert statement verifies that the value of _`msg`_ is still the old value.

```
   public class PassPrimitiveTypeExample {

      public static void debugStatusMessage() {

        String msg = 'Original value';

        processString(msg);

        // The value of the msg variable didn't

        // change; it is still the old value.

        System.assertEquals(msg, 'Original value');

      }

      public static void processString(String s) {

        s = 'Modified value';

      }

   }

```

**Example: Passing Non-Primitive Data Type Arguments**

This example shows how a List argument is passed by reference into the `reference()` method and is modified. It then shows, in
the `referenceNew()` method, that the List argument can't be changed to point to another List object.


Apex Developer Guide Classes, Objects, and Interfaces

First, the `createTemperatureHistory` method creates a variable, _`fillMe`_, that is a List of Integers and passes it to a method.
The called method fills this list with Integer values representing rounded temperature values. When the method returns, an assert
statement verifies that the contents of the original List variable has changed and now contains five values. Next, the example creates a
second List variable, _`createMe`_, and passes it to another method. The called method assigns the passed-in argument to a newly
created List that contains new Integer values. When the method returns, the original _`createMe`_ variable doesn't point to the new
List but still points to the original List, which is empty. An assert statement verifies that _`createMe`_ contains no values.

```
   public class PassNonPrimitiveTypeExample {

      public static void createTemperatureHistory() {

        List<Integer> fillMe = new List<Integer>();

        reference(fillMe);

        // The list is modified and contains five items

        // as expected.

        System.assertEquals(fillMe.size(),5);

        List<Integer> createMe = new List<Integer>();

        referenceNew(createMe);

        // The list is not modified because it still points

        // to the original list, not the new list

        // that the method created.

        System.assertEquals(createMe.size(),0);

      }

      public static void reference(List<Integer> m) {

        // Add rounded temperatures for the last five days.

        m.add(70);

        m.add(68);

        m.add(75);

        m.add(80);

        m.add(82);

      }

      public static void referenceNew(List<Integer> m) {

        // Assign argument to a new List of

        // five temperature values.

        m = new List<Integer>{55, 59, 62, 60, 63};

      }

   }

```

Versioned Behavior Changes

In API version 65.0 and later, an abstract or override method requires a `protected`, `public`, or `global` access modifier. If one of
these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is
invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare
an abstract or override method without an allowed access modifier, you get the compilation error `Abstract methods require`
`at least one of the following: global, public, protected` .


Apex Developer Guide Classes, Objects, and Interfaces

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation. For more
[information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

SEE ALSO:

Primitive Data Types

##### Using Constructors

A _constructor_ is code that is invoked when an object is created from the class blueprint. You do not need to write a constructor for every
class. If a class doesn't have a user-defined constructor, a default, no-argument constructor with the same visibility as the containing
class is generated.

The syntax for a constructor is similar to a method, but it differs from a method definition in that it never has an explicit return type and
it is not inherited by the object created from it.

After you write the constructor for a class, you must use the `new` keyword in order to instantiate an object from that class, using that
constructor. For example, using the following class:

```
   public class TestObject {

     // The no argument constructor

     public TestObject() {

       // more code here

     }

   }

```

A new object of this type can be instantiated with this code.

```
   TestObject myTest = new TestObject();

```

If you write a constructor that takes arguments, you can then use that constructor to create an object using those arguments.

If you create a constructor that takes arguments, and you still want to use a no-argument constructor, you must create your own
no-argument constructor in your code. After you create a constructor for a class, you no longer have access to the default, no-argument
public constructor.

In Apex, a constructor can be _overloaded_, that is, there can be more than one constructor for a class, each having different parameters.
This example illustrates a class with two constructors: one with no arguments and one that takes a simple Integer argument. It also
illustrates how one constructor calls another constructor using the `this(...)` syntax, also know as _constructor chaining_ .

```
   public class TestObject2 {

   private static final Integer DEFAULT_SIZE = 10;

   Integer size;

     //Constructor with no arguments

     public TestObject2() {

        this(DEFAULT_SIZE); // Using this(...) calls the one argument constructor

     }

     // Constructor with one argument

     public TestObject2(Integer ObjectSize) {

      size = ObjectSize;

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     }

   }

```

New objects of this type can be instantiated with this code.

```
     TestObject2 myObject1 = new TestObject2(42);

     TestObject2 myObject2 = new TestObject2();

```

Every constructor that you create for a class must have a different argument list. In this example, all of the constructors are possible.

```
   public class Leads {

     // First a no-argument constructor

     public Leads () {}

     // A constructor with one argument

     public Leads (Boolean call) {}

     // A constructor with two arguments

     public Leads (String email, Boolean call) {}

     // Though this constructor has the same arguments as the

     // one above, they are in a different order, so this is legal

     public Leads (Boolean call, String email) {}

   }

```

When you define a new class, you are defining a new data type. You can use class name in any place you can use other data type names,
such as String, Boolean, or Account. If you define a variable whose type is a class, any object you assign to it must be an instance of that
class or subclass.

##### Access Modifiers

Apex allows you to use the `private`, `protected`, `public`, and `global` access modifiers when defining methods and variables.

While triggers and anonymous blocks can also use these access modifiers, they aren’t as useful in smaller portions of Apex. For example,
declaring a method as `global` in an anonymous block doesn’t enable you to call it from outside of that code.

For more information on class access modifiers, see Apex Class Definition on page 63.

Note: Methods defined in an interface have the same access modifier as the interface ( `public` or `global` ). For more information,
see Interfaces.

By default, a method or variable is visible only to the Apex code _within the defining class_ . Explicitly specify a method or variable as public
in order for it to be available to other classes in the same application namespace (see Namespace Prefix). You can change the level of
visibility by using the following access modifiers:

```
   private
```

This access modifier is the default, and means that the method or variable is accessible only within the Apex class in which it’s defined.
If you don’t specify an access modifier, the method or variable is `private` .

```
   protected
```

This means that the method or variable is visible to any inner classes in the defining Apex class, and to the classes that extend the
defining Apex class. You can only use this access modifier for instance methods and member variables. This setting is strictly more
permissive than the default (private) setting, just like Java.


Apex Developer Guide Classes, Objects, and Interfaces

```
   public
```

This means that the method or variable is accessible by all Apex within a specific package. For accessibility by all second-generation
(2GP) managed packages that share a namespace, use `public` with the `@NamespaceAccessible` annotation. Using the
public access modifier in no-namespace packages implicitly renders the Apex code as @NamespaceAccessible.

Note: In Apex, the `public` access modifier isn’t the same as it is in Java. This was done to discourage joining applications,
to keep the code for each application separate. In Apex, if you want to make something public like it is in Java, you must use
the `global` access modifier.

[For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

```
   global
```

This means the method or variable can be used by any Apex code that has access to the class, not just the Apex code in the same
application. This access modifier must be used for any method that must be referenced outside of the application, either in SOAP
API or by other Apex code. If you declare a method or variable as `global`, you must also declare the class that contains it as

`global` .

Note: We recommend using the `global` access modifier rarely, if at all. Cross-application dependencies are difficult to
maintain.

To use the `private`, `protected`, `public`, or `global` access modifiers, use the following syntax:

```
   [(none)|private|protected|public|global] declaration

```

For example:

```
   // private variable s1

   private string s1 = '1';

   // public method getsz()

   public string getsz() {

     ...

   }

```

Versioned Behavior Changes

In API version 65.0 and later, an abstract or override method requires a `protected`, `public`, or `global` access modifier. If one of
these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is
invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare
an abstract or override method without an allowed access modifier, you get the compilation error `Abstract methods require`
`at least one of the following: global, public, protected` .

##### Static and Instance Methods, Variables, and Initialization Code

In Apex, you can have _static_ methods, variables, and initialization code. However, Apex classes can't be static. You can also have _instance_
methods, member variables, and initialization code, which have no modifiers, and _local_ variables.

Characteristics

Static methods, variables, and initialization code have these characteristics.

**•** They’re associated with a class.

**•** They’re allowed only in outer classes.

**•** They’re initialized only when a class is loaded.


Apex Developer Guide Classes, Objects, and Interfaces

**•** They aren’t transmitted as part of the view state for a Visualforce page.

Instance methods, member variables, and initialization code have these characteristics.

**•** They’re associated with a particular object.

**•** They have no definition modifier.

**•** They’re created with every object instantiated from the class in which they’re declared.

Local variables have these characteristics.

**•** They’re associated with the block of code in which they’re declared.

**•** They must be initialized before they’re used.

The following example shows a local variable whose scope is the duration of the `if` code block.

```
   Boolean myCondition = true;

   if (myCondition) {

      integer localVariable = 10;

   }

```

Using Static Methods and Variables

You can use static methods and variables only with outer classes. Inner classes have no static methods or variables. A static method or
variable doesn’t require an instance of the class in order to run.

Before an object of a class is created, all static member variables in a class are initialized, and all static initialization code blocks are
executed. These items are handled in the order in which they appear in the class.

A static method is used as a utility method, and it never depends on the value of an instance member variable. Because a static method
is only associated with a class, it can’t access the instance member variable values of its class.

A static variable is static only within the scope of the Apex transaction. It’s not static across the server or the entire organization. The
value of a static variable persists within the context of a single transaction and is reset across transaction boundaries. For example, if an
Apex DML request causes a trigger to fire multiple times, the static variables persist across these trigger invocations.

To store information that is shared across instances of a class, use a static variable. All instances of the same class share a single copy of
the static variable. For example, all triggers that a single transaction spawns can communicate with each other by viewing and updating
static variables in a related class. A recursive trigger can use the value of a class variable to determine when to exit the recursion.

Suppose that you had the following class.

```
   public class P {

     public static boolean firstRun = true;

   }

```

A trigger that uses this class could then selectively fail the first run of the trigger.

```
   trigger T1 on Account (before delete, after delete, after undelete) {

        if(Trigger.isBefore){

         if(Trigger.isDelete){

           if(p.firstRun){

              Trigger.old[0].addError('Before Account Delete Error');

              p.firstRun=false;

            }

          }

        }

   }

```


Apex Developer Guide Classes, Objects, and Interfaces

A static variable defined in a trigger doesn't retain its value between different trigger contexts within the same transaction, such as
between before insert and after insert invocations. Instead, define the static variables in a class so that the trigger can access these class
member variables and check their static values.

A class static variable can’t be accessed through an instance of that class. If class `MyClass` has a static variable `myStaticVariable`,
and `myClassInstance` is an instance of `MyClass`, `myClassInstance.myStaticVariable` isn’t a legal expression.

The same is true for instance methods. If `myStaticMethod()` is a static method, `myClassInstance.myStaticMethod()`
isn’t legal. Instead, refer to those static identifiers using the class: `MyClass.myStaticVariable` and
`MyClass.myStaticMethod()` .

Local variable names are evaluated before class names. If a local variable has the same name as a class, the local variable hides methods
and variables on the class of the same name. For example, this method works if you comment out the `String` line. But if the `String`
line is included the method doesn’t compile, because Salesforce reports that the method doesn’t exist or has an incorrect signature.

```
   public static void method() {

   String Database = '';

   Database.insert(new Account());

   }

```

An inner class behaves like a static Java inner class, but doesn’t require the `static` keyword. An inner class can have instance member
variables like an outer class, but there’s no implicit pointer to an instance of the outer class (using the `this` keyword).

Note: In API version 20.0 and earlier, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to
process is split into chunks of 100 records. In Salesforce API version 21.0 and later, no further splits of API chunks occur. If a Bulk
API request causes a trigger to fire multiple times for chunks of 200 records, governor limits are reset between these trigger
invocations for the same HTTP request. Static variables aren’t reset within the multiple trigger invocations for the same Bulk API
request.

Using Instance Methods and Variables

Instance methods and member variables are used by an instance of a class, that is, by an object. An instance member variable is declared
inside a class, but not within a method. Instance methods usually use instance member variables to affect the behavior of the method.

Suppose that you want to have a class that collects two-dimensional points and plots them on a graph. The following skeleton class
uses member variables to hold the list of points and an inner class to manage the two-dimensional list of points.

```
   public class Plotter {

      // This inner class manages the points

      class Point {

        Double x;

        Double y;

        Point(Double x, Double y) {

           this.x = x;

           this.y = y;

        }

        Double getXCoordinate() {

           return x;

        }

        Double getYCoordinate() {

           return y;

        }

      }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      List<Point> points = new List<Point>();

      public void plot(Double x, Double y) {

        points.add(new Point(x, y));

      }

      // The following method takes the list of points and does something with them

      public void render() {

      }

   }

```

Using Initialization Code

Instance initialization code is a block of code in the following form that is defined in a class.

```
   {

     //code body

   }

```

The instance initialization code in a class is executed each time an object is instantiated from that class. These code blocks run before
the constructor.

If you don’t want to write your own constructor for a class, you can use an instance initialization code block to initialize instance variables.
In simple situations, use an ordinary initializer. Reserve initialization code for complex situations, such as initializing a static map. A static
initialization block runs only one time, regardless of how many times you access the class that contains it.

Static initialization code is a block of code preceded with the keyword `static` .

```
   static {

     //code body

   }

```

Similar to other static code, a static initialization code block is only initialized one time on the first use of the class.

A class can have any number of either static or instance initialization code blocks. They can appear anywhere in the code body. The code
blocks are executed in the order in which they appear in the file, just as they are in Java.

You can use static initialization code to initialize static final variables and to declare information that’s static, such as a map of values. For
example:

```
   public class MyClass {

      class RGB {

        Integer red;

        Integer green;

        Integer blue;

        RGB(Integer red, Integer green, Integer blue) {

           this.red = red;

           this.green = green;

           this.blue = blue;

```


Apex Developer Guide Classes, Objects, and Interfaces

```
        }

      }

     static Map<String, RGB> colorMap = new Map<String, RGB>();

      static {

        colorMap.put('red', new RGB(255, 0, 0));

        colorMap.put('cyan', new RGB(0, 255, 255));

        colorMap.put('magenta', new RGB(255, 0, 255));

      }

   }

```

Versioned Behavior Changes

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation. For more
[information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

##### Apex Properties

An Apex _property_ is similar to a variable; however, you can do additional things in your code to a property value before it’s accessed or
returned. Properties can be used to validate data before a change is made, to prompt an action when data is changed (such as altering
the value of other member variables), or to expose data that is retrieved from some other source (such as another class).

Property definitions include one or two code blocks, representing a _get accessor_ and a _set accessor_ :

**•** The code in a get accessor executes when the property is read.

**•** The code in a set accessor executes when the property is assigned a new value.

If a property has only a get accessor, it’s considered read-only. If a property has only a set accessor, it’s considered write-only. A property
with both accessors is considered read-write.

To declare a property, use the following syntax in the body of a class:

```
   Public class BasicClass {

     // Property declaration

     access_modifier return_type property_name {

       get {

         //Get accessor code block

       }

       set {

         //Set accessor code block

       }

     }

   }

```

Where:

**•** _`access_modifier`_ is the access modifier for the property. The access modifiers that can be applied to properties include:

`public`, `private`, `global`, and `protected` . In addition, these definition modifiers can be applied: `static` and
`transient` . For more information on access modifiers, see Access Modifiers on page 69.

**•** _`return_type`_ is the type of the property, such as Integer, Double, sObject, and so on. For more information, see Data Types on
page 24.

**•** _`property_name`_ is the name of the property


Apex Developer Guide Classes, Objects, and Interfaces

For example, the following class defines a property named `prop` . The property is public. The property returns an integer data type.

```
   public class BasicProperty {

     public integer prop {

       get { return prop; }

       set { prop = value; }

     }

   }

```

The following code segment calls the BasicProperty class, exercising the get and set accessors:

```
   BasicProperty bp = new BasicProperty();

   bp.prop = 5; // Calls set accessor

   System.assertEquals(5, bp.prop); // Calls get accessor

```

Note the following:

**•** The body of the get accessor is similar to that of a method. It must return a value of the property type. Executing the get accessor is
the same as reading the value of the variable.

**•** The get accessor must end in a return statement.

**•** We recommend that your get accessor not change the state of the object that it’s defined on.

**•** The set accessor is similar to a method whose return type is void.

**•** When you assign a value to the property, the set accessor is invoked with an argument that provides the new value.

**•** In API version 42.0 and later, unless a variable value is set in a set accessor, you can’t update its value in a get accessor.

**•** When the set accessor is invoked, the system passes an implicit argument to the setter called `value` of the same data type as the
property.

**•** Properties can’t be defined on `interface` .

**•** Apex properties are based on their counterparts in C#, with the following differences:

**–** Properties provide storage for values directly. You don’t need to create supporting members for storing values.

**–** It’s possible to create automatic properties in Apex. For more information, see Using Automatic Properties on page 75.

Using Automatic Properties

Properties don’t require additional code in their get or set accessor code blocks. Instead, you can leave get and set accessor code blocks
empty to define an _automatic property_ . Automatic properties allow you to write more compact code that is easier to debug and maintain.
They can be declared as read-only, read-write, or write-only. The following example creates three automatic properties:

```
   public class AutomaticProperty {

     public integer MyReadOnlyProp { get; }

     public double MyReadWriteProp { get; set; }

     public string MyWriteOnlyProp { set; }

   }

```

The following code segment exercises these properties:

```
   AutomaticProperty ap = new AutomaticProperty();

   ap.MyReadOnlyProp = 5; // This produces a compile error: not writable

   ap.MyReadWriteProp = 5; // No error

   System.assertEquals(5, ap.MyWriteOnlyProp); // This produces a compile error: not readable

```


Apex Developer Guide Classes, Objects, and Interfaces

Using Static Properties

When a property is declared as `static`, the property's accessor methods execute in a static context. Therefore, accessors don’t have
access to non-static member variables defined in the class. The following example creates a class with both static and instance properties:

```
   public class StaticProperty {

     private static integer StaticMember;

     private integer NonStaticMember;

     // The following produces a system error

     // public static integer MyBadStaticProp { return NonStaticMember; }

     public static integer MyGoodStaticProp {

      get {return StaticMember;}

      set { StaticMember = value; }

     }

     public integer MyGoodNonStaticProp {

      get {return NonStaticMember;}

      set { NonStaticMember = value; }

     }

   }

```

The following code segment calls the static and instance properties:

```
   StaticProperty sp = new StaticProperty();

   // The following produces a system error: a static variable cannot be

   // accessed through an object instance

   // sp.MyGoodStaticProp = 5;

   // The following does not produce an error

   StaticProperty.MyGoodStaticProp = 5;

```

Using Access Modifiers on Property Accessors

Property accessors can be defined with their own access modifiers. If an accessor includes its own access modifier, this modifier overrides
the access modifier of the property. The access modifier of an individual accessor must be more restrictive than the access modifier on
the property itself. For example, if the property has been defined as `public`, the individual accessor can’t be defined as `global` . The
following class definition shows additional examples:

```
   global virtual class PropertyVisibility {

     // X is private for read and public for write

     public integer X { private get; set; }

     // Y can be globally read but only written within a class

     global integer Y { get; public set; }

     // Z can be read within the class but only subclasses can set it

     public integer Z { get; protected set; }

   }

##### Extending a Class

```

You can extend a class to provide more specialized behavior.

A class that extends another class inherits all the methods and properties of the extended class. In addition, the extending class can
override the existing virtual methods by using the override keyword in the method definition. Overriding a virtual method allows you


Apex Developer Guide Classes, Objects, and Interfaces

to provide a different implementation for an existing method. This means that the behavior of a particular method is different based on
the object you’re calling it on. This is referred to as polymorphism.

A class extends another class using the `extends` keyword in the class definition. A class can only extend one other class, but it can
implement more than one interface.

This example shows how the `YellowMarker` class extends the `Marker` class. To run the inheritance examples in this section, first
create the `Marker` class.

```
   public virtual class Marker {

      public virtual void write() {

        System.debug('Writing some text.');

      }

      public virtual Double discount() {

        return .05;

      }

   }

```

Then create the `YellowMarker` class, which extends the `Marker` class.

```
   // Extension for the Marker class

   public class YellowMarker extends Marker {

      public override void write() {

        System.debug('Writing some text using the yellow marker.');

      }

   }

```

This code segment shows polymorphism. The example declares two objects of the same type ( `Marker` ). Even though both objects
are markers, the second object is assigned to an instance of the `YellowMarker` class. Hence, calling the `write` method on it yields
a different result than calling this method on the first object, because this method has been overridden. However, you can call the
`discount` method on the second object even though this method isn't part of the `YellowMarker` class definition. But it’s part
of the extended class, and hence, is available to the extending class, `YellowMarker` . Run this snippet in the Execute Anonymous
window of the Developer Console.

```
   Marker obj1, obj2;

   obj1 = new Marker();

   // This outputs 'Writing some text.'

   obj1.write();

   obj2 = new YellowMarker();

   // This outputs 'Writing some text using the yellow marker.'

   obj2.write();

   // We get the discount method for free

   // and can call it from the YellowMarker instance.

   Double d = obj2.discount();

```

The extending class can have more method definitions that aren't common with the original extended class. In this example, the
`RedMarker` class extends the `Marker` class and has one extra method, `computePrice`, that isn't available for the `Marker`
class. To call the extra methods, the object type must be the extending class.

Before running the next snippet, create the `RedMarker` class, which requires the `Marker` class in your org.

```
   // Extension for the Marker class

   public class RedMarker extends Marker {

      public override void write() {

        System.debug('Writing some text in red.');

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      }

      // Method only in this class

      public Double computePrice() {

        return 1.5;

      }

   }

```

This snippet shows how to call the additional method on the `RedMarker` class. Run this snippet in the Execute Anonymous window
of the Developer Console.

```
   RedMarker obj = new RedMarker();

   // Call method specific to RedMarker only

   Double price = obj.computePrice();

```

Extensions also apply to interfaces—an interface can extend another interface. As with classes, when an interface extends another
interface, all the methods and properties of the extended interface are available to the extending interface.

Versioned Behavior Changes

In API version 65.0 and later, an abstract or override method requires a `protected`, `public`, or `global` access modifier. If one of
these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is
invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare
an abstract or override method without an allowed access modifier, you get the compilation error `Abstract methods require`
`at least one of the following: global, public, protected` .

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation. For more
[information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

##### Extended Class Example

The following is an extended example of a class, showing all the features of Apex classes. The keywords and concepts introduced in the
example are explained in more detail throughout this chapter.

```
   // Top-level (outer) class must be public or global (usually public unless they contain

   // a Web Service, then they must be global)

   public class OuterClass {

     // Static final variable (constant) – outer class level only

     private static final Integer MY_INT;

     // Non-final static variable - use this to communicate state across triggers

     // within a single request)

     public static String sharedState;

     // Static method - outer class level only

     public static Integer getInt() { return MY_INT; }

     // Static initialization (can be included where the variable is defined)

     static {

      MY_INT = 2;

     }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     // Member variable for outer class

     private final String m;

     // Instance initialization block - can be done where the variable is declared,

     // or in a constructor

     {

      m = 'a';

     }

     // Because no constructor is explicitly defined in this outer class, an implicit,

     // no-argument, public constructor exists

     // Inner interface

     public virtual interface MyInterface {

      // No access modifier is necessary for interface methods - these are always

      // public or global depending on the interface visibility

      void myMethod();

     }

     // Interface extension

     interface MySecondInterface extends MyInterface {

      Integer method2(Integer i);

     }

     // Inner class - because it is virtual it can be extended.

     // This class implements an interface that, in turn, extends another interface.

     // Consequently the class must implement all methods.

     public virtual class InnerClass implements MySecondInterface {

      // Inner member variables

      private final String s;

      private final String s2;

      // Inner instance initialization block (this code could be located above)

      {

        this.s = 'x';

      }

      // Inline initialization (happens after the block above executes)

      private final Integer i = s.length();

      // Explicit no argument constructor

      InnerClass() {

        // This invokes another constructor that is defined later

        this('none');

      }

      // Constructor that assigns a final variable value

      public InnerClass(String s2) {

       this.s2 = s2;

      }

      // Instance method that implements a method from MyInterface.

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      // Because it is declared virtual it can be overridden by a subclass.

      public virtual void myMethod() { /* does nothing */ }

      // Implementation of the second interface method above.

      // This method references member variables (with and without the "this" prefix)

      public Integer method2(Integer i) { return this.i + s.length(); }

     }

     // Abstract class (that subclasses the class above). No constructor is needed since

     // parent class has a no-argument constructor

     public abstract class AbstractChildClass extends InnerClass {

      // Override the parent class method with this signature.

      // Must use the override keyword

      public override void myMethod() { /* do something else */ }

      // Same name as parent class method, but different signature.

      // This is a different method (displaying polymorphism) so it does not need

      // to use the override keyword

      protected void method2() {}

      // Abstract method - subclasses of this class must implement this method

      public abstract Integer abstractMethod();

     }

     // Complete the abstract class by implementing its abstract method

     public class ConcreteChildClass extends AbstractChildClass {

      // Here we expand the visibility of the parent method - note that visibility

      // cannot be restricted by a sub-class

      public override Integer abstractMethod() { return 5; }

     }

     // A second sub-class of the original InnerClass

     public class AnotherChildClass extends InnerClass {

      AnotherChildClass(String s) {

       // Explicitly invoke a different super constructor than one with no arguments

       super(s);

      }

     }

     // Exception inner class

     public virtual class MyException extends Exception {

      // Exception class member variable

      public Double d;

      // Exception class constructor

      MyException(Double d) {

       this.d = d;

      }

      // Exception class method, marked as protected

      protected void doIt() {}

     }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     // Exception classes can be abstract and implement interfaces

     public abstract class MySecondException extends Exception implements MyInterface {

     }

   }

```

This code example illustrates:

**•** A top-level class definition (also called an _outer class_ )

**•** Static variables and static methods in the top-level class, as well as static initialization code blocks

**•** Member variables and methods for the top-level class

**•** Classes with no user-defined constructor — these have an implicit, no-argument constructor

**•** An interface definition in the top-level class

**•** An interface that extends another interface

**•** Inner class definitions (one level deep) within a top-level class

**•** A class that implements an interface (and, therefore, its associated sub-interface) by implementing public versions of the method
signatures

**•** An inner class constructor definition and invocation

**•** An inner class member variable and a reference to it using the `this` keyword (with no arguments)

**•** An inner class constructor that uses the `this` keyword (with arguments) to invoke a different constructor

**•** Initialization code outside of constructors — both where variables are defined, as well as with anonymous blocks in curly braces
( `{}` ). Note that these execute with every construction in the order they appear in the file, as with Java.

**•** Class extension and an abstract class

**•** Methods that override base class methods (which must be declared `virtual` )

**•** The `override` keyword for methods that override subclass methods

**•** Abstract methods and their implementation by concrete sub-classes

**•** The `protected` access modifier

**•** Exceptions as first class objects with members, methods, and constructors

This example shows how the class above can be called by other Apex code:

```
   // Construct an instance of an inner concrete class, with a user-defined constructor

   OuterClass.InnerClass ic = new OuterClass.InnerClass('x');

   // Call user-defined methods in the class

   System.assertEquals(2, ic.method2(1));

   // Define a variable with an interface data type, and assign it a value that is of

   // a type that implements that interface

   OuterClass.MyInterface mi = ic;

   // Use instanceof and casting as usual

   OuterClass.InnerClass ic2 = mi instanceof OuterClass.InnerClass ?

                    (OuterClass.InnerClass)mi : null;

   System.assert(ic2 != null);

   // Construct the outer type

   OuterClass o = new OuterClass();

   System.assertEquals(2, OuterClass.getInt());

```


Apex Developer Guide Classes, Objects, and Interfaces

```
   // Construct instances of abstract class children

   System.assertEquals(5, new OuterClass.ConcreteChildClass().abstractMethod());

   // Illegal - cannot construct an abstract class

   // new OuterClass.AbstractChildClass();

   // Illegal – cannot access a static method through an instance

   // o.getInt();

   // Illegal - cannot call protected method externally

   // new OuterClass.ConcreteChildClass().method2();

```

This code example illustrates:

**•** Construction of the outer class

**•** Construction of an inner class and the declaration of an inner interface type

**•** A variable declared as an interface type can be assigned an instance of a class that implements that interface

**•** Casting an interface variable to be a class type that implements that interface (after verifying this using the `instanceof` operator)

#### Interfaces

An _interface_ is like a class in which none of the methods have been implemented—the method signatures are there, but the body of
each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained in the
interface.

#### Interfaces can provide a layer of abstraction to your code. They separate the specific implementation of a method from the declaration

for that method. This way you can have different implementations of a method based on your specific application.

Defining an interface is similar to defining a new class. For example, a company can have two types of purchase orders, ones that come
from customers, and others that come from their employees. Both are a type of purchase order. Suppose you needed a method to
provide a discount. The amount of the discount can depend on the type of purchase order.

You can model the general concept of a purchase order as an interface and have specific implementations for customers and employees.
In the following example the focus is only on the discount aspect of a purchase order.

Here’s the definition of the `PurchaseOrder` interface.

```
   // An interface that defines what a purchase order looks like in general

   public interface PurchaseOrder {

      // All other functionality excluded

      Double discount();

   }

```

This class implements the `PurchaseOrder` interface for customer purchase orders.

```
   // One implementation of the interface for customers

   public class CustomerPurchaseOrder implements PurchaseOrder {

      public Double discount() {

        return .05; // Flat 5% discount

      }

   }

```


Apex Developer Guide Classes, Objects, and Interfaces

This class implements the `PurchaseOrder` interface for employee purchase orders.

```
   // Another implementation of the interface for employees

   public class EmployeePurchaseOrder implements PurchaseOrder {

       public Double discount() {

        return .10; // It’s worth it being an employee! 10% discount

       }

   }

```

Note the following about the example:

**•** The interface `PurchaseOrder` is defined as a general prototype. Methods defined within an interface have no access modifiers
and contain just their signature.

**•** The `CustomerPurchaseOrder` class implements this interface; therefore, it must provide a definition for the `discount`
method. Any class that implements an interface must define all the methods contained in the interface.

When you define a new interface, you’re defining a new data type. You can use an interface name in any place you can use another data
type name. Any object assigned to a variable of type interface must be an instance of a class that implements the interface, or a
sub-interface data type.

See also Classes and Casting on page 118.

Note: You can’t add a method to a global interface after the class has been uploaded in a Managed - Released package version.

Versioned Behavior Changes

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation. For more
[information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass.
This change is versioned, so to prevent the override, update your abstract or virtual classes that contain private methods to API version
61.0 or later. In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in
one of its superclasses, the subclass method overrides the private method.

##### 1. Custom Iterators Custom Iterators

An iterator traverses through every item in a collection. For example, in a procedural loop, you define a condition for exiting the loop,
and you must provide some means of traversing the collection, that is, an iterator. In this example, `count` is incremented by 1 every
time the loop is executed.

```
   while (count < 11) {

     System.debug(count);

       count++;

     }

```

Using the `Iterator` interface you can create a custom set of instructions for traversing a List through a loop. The iterator is useful for
data that exists in sources outside of Salesforce that you would normally define the scope of using a `SELECT` statement. Iterators can
also be used if you have multiple `SELECT` statements.


Apex Developer Guide Classes, Objects, and Interfaces

Using Custom Iterators

To use custom iterators, you must create an Apex class that implements the `Iterator` interface.

The `Iterator` interface has the following instance methods:

**Name** **Arguments** **Returns** **Description**

`hasNext` Boolean Returns `true` if there’s another item in the collection being
traversed, `false` otherwise.

`next` Any type Returns the next item in the collection.

All methods in the `Iterator` interface must be declared as `global` or `public` .

This example code uses a custom iterator to iterate through a list of strings.

```
   IterableString x = new IterableString('This is a really cool test.');

   while(x.hasNext()){

     system.debug(x.next());

   }

```

Using Custom Iterators with **`Iterable`**

If you don’t want to use a custom iterator with a list, but instead want to create your own data structure, you can use the `Iterable`
interface to generate the data structure.

The `Iterable` interface has the following method:

**Name** **Arguments** **Returns** **Description**

`iterator` Iterator class Returns a reference to the iterator for this interface.

The `iterator` method must be declared as `global` or `public` . It creates a reference to the iterator that you can then use to
traverse the data structure.

In the following example a custom iterator iterates through a collection:

```
   public class CustomIterator

     implements Iterator<Account>{

     private List<Account> accounts;

     private Integer currentIndex;

     public CustomIterator(List<Account> accounts){

        this.accounts = accounts;

        this.currentIndex = 0;

     }

     public Boolean hasNext(){

        return currentIndex < accounts.size();

     }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     public Account next(){

        if(hasNext()) {

          return accounts[currentIndex++];

        } else {

          throw new NoSuchElementException('Iterator has no more elements.');

        }

     }

   }

   public class CustomIterable implements Iterable<Account> {

     public Iterator<Account> iterator(){

       List<Account> accounts =

       [SELECT Id, Name,

        NumberOfEmployees

        FROM Account

        LIMIT 10];

       return new CustomIterator(accounts);

     }

   }

```

The following is a batch job that uses an iterator:

```
   public class BatchClass implements Database.Batchable<Account>{

     public Iterable<Account> start(Database.BatchableContext info){

        return new CustomIterable();

     }

     public void execute(Database.BatchableContext info, List<Account> scope){

        List<Account> accsToUpdate = new List<Account>();

        for(Account acc : scope){

          acc.Name = 'changed';

          acc.NumberOfEmployees = 69;

          accsToUpdate.add(acc);

        }

        update accsToUpdate;

     }

     public void finish(Database.BatchableContext info){

     }

   }

#### Keywords

```

Apex provides the keywords `final`, `instanceof`, `super`, `this`, `transient`, `with sharing` and `without sharing` .

1. Using the final Keyword

2. Using the instanceof Keyword

3. Using the super Keyword

4. Using the this Keyword

5. Using the transient Keyword


Apex Developer Guide Classes, Objects, and Interfaces

6. Use the with sharing, without sharing, and inherited sharing Keywords
Use the `with sharing` or `without sharing` keywords on a class to specify whether sharing rules are enforced. Use the
`inherited sharing` keyword on a class to run the class in the sharing mode of the calling class. The default sharing mode
is `with sharing` .

SEE ALSO:

Reserved Keywords

##### Using the final Keyword

Keep in mind these consideration while using the `final` keyword to modify variables.

**•** Final variables can be assigned a value only once. Static final variables can be initialized in static initialization code blocks or where
defined. Member final variables can be initialized in initialization code blocks, constructors, or where defined.

**•** To define a constant, mark a variable as both `static` and `final` .

**•** Non-final static variables are used to communicate state at the class level (such as state between triggers). However, they aren’t
shared across requests.

**•** Methods and classes are final by default. You can’t use the `final` keyword in the declaration of a class or method. This means
they can’t be overridden. Use the `virtual` keyword if you need to override a method or class.

**•** You can’t use the `final` keyword with properties.

SEE ALSO:

Extended Class Example

##### Using the instanceof Keyword

If you need to verify at run time whether an object is actually an instance of a particular class, use the `instanceof` keyword. The

`instanceof` keyword can only be used to verify if the target type in the expression on the right of the keyword is a viable alternative
for the declared type of the expression on the left.

You could add the following check to the `Report` class in the classes and casting example before you cast the item back into a
`CustomReport` object.

```
   if (Reports.get(0) instanceof CustomReport) {

      // Can safely cast it back to a custom report object

     CustomReport c = (CustomReport) Reports.get(0);

     } else {

     // Do something with the non-custom-report.

   }

```

Implementation Considerations

Keep these considerations in mind while using the `instanceof` keyword.

**•** If the declared type on the left of the expression using the `instanceof` keyword is always an instance of the target type,
compilation fails. An example expression that’s always true and therefore causes a compilation error.

```
     Account acc = new Account();

     if(acc instanceOf Account) {

        //condition is always true since an instance of Account is always an instance of

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     Account

     }

```

**•** When you perform `instanceof` checks, implicit type casting from String to ID can result in unexpected behavior if the String
meets the requirements to be cast to an ID.

Versioned Behavior Changes

In API version 60.0 and later, if a `List` data type implements the `Iterable` data type, compilation fails. An example `instanceof`
expression that causes a compilation error.

```
   public class BaseClass {}

   public class SubClass extends BaseClass {}

   List<SubClass> subClasses = new List<SubClass>();

   if(subClasses instanceof Iterable<BaseClass>) {

      //condition is always true since an instance of SubClass is always an instance of

   BaseClass

   }

```

In API version 32.0 and later, `instanceof` returns `false` if the left operand is a null object. In API version 31.0 and earlier,

`instanceof` returns true in this case. For example, the code sample returns `false` in API version 32.0 and later.

```
   Object o = null;

   Boolean result = o instanceof Account;

   System.assertEquals(false, result);

##### Using the super Keyword

```

The `super` keyword can be used by classes that are extended from virtual or abstract classes. By using `super`, you can override
constructors and methods from the parent class.

For example, if you have the following virtual class:

```
   public virtual class SuperClass {

      public String mySalutation;

      public String myFirstName;

      public String myLastName;

      public SuperClass() {

        mySalutation = 'Mr.';

        myFirstName = 'Carl';

        myLastName = 'Vonderburg';

      }

      public SuperClass(String salutation, String firstName, String lastName) {

        mySalutation = salutation;

        myFirstName = firstName;

        myLastName = lastName;

      }

      public virtual void printName() {

```


Apex Developer Guide Classes, Objects, and Interfaces

```
        System.debug('My name is ' + mySalutation + myLastName);

      }

     public virtual String getFirstName() {

        return myFirstName;

     }

   }

```

You can create the following class that extends `Superclass` and overrides its `printName` method:

```
   public class Subclass extends Superclass {

     public override void printName() {

        super.printName();

        System.debug('But you can call me ' + super.getFirstName());

      }

   }

```

The expected output when calling `Subclass.printName` is `My name is Mr. Vonderburg. But you can call`

```
   me Carl.

```

You can also use `super` to call constructors. Add the following constructor to `SubClass` :

```
   public Subclass() {

      super('Madam', 'Brenda', 'Clapentrap');

   }

```

Now, the expected output of `Subclass.printName` is `My name is Madam Clapentrap. But you can call`

```
   me Brenda.

```

Best Practices for Using the **`super`** Keyword

**•** Only classes that are extending from `virtual` or `abstract` classes can use `super` .

**•** You can only use `super` in methods that are designated with the `override` keyword.

##### Using the this Keyword

There are two different ways of using the `this` keyword.

You can use the `this` keyword in dot notation, without parenthesis, to represent the current instance of the class in which it appears.
Use this form of the `this` keyword to access instance variables and methods. For example:

```
   public class myTestThis {

   string s;

     {

       this.s = 'TestString';

     }

   }

```

In the above example, the class `myTestThis` declares an instance variable `s` . The initialization code populates the variable using the

`this` keyword.


Apex Developer Guide Classes, Objects, and Interfaces

Or you can use the `this` keyword to do constructor chaining, that is, in one constructor, call another constructor. In this format, use
the `this` keyword with parentheses. For example:

```
   public class testThis {

   // First constructor for the class. It requires a string parameter.

     public testThis(string s2) {

     }

   // Second constructor for the class. It does not require a parameter.

   // This constructor calls the first constructor using the this keyword.

     public testThis() {

        this('None');

     }

   }

```

When you use the `this` keyword in a constructor to do constructor chaining, it must be the first statement in the constructor.

##### Using the transient Keyword

Use the `transient` keyword to declare instance variables that can't be saved, and shouldn't be transmitted as part of the view state
for a Visualforce page. For example:

```
   Transient Integer currentTotal;

```

You can also use the `transient` keyword in Apex classes that are serializable, namely in controllers, controller extensions, or classes
that implement the `Batchable` or `Schedulable` interface. In addition, you can use `transient` in classes that define the types
of fields declared in the serializable classes.

Declaring variables as `transient` reduces view state size. A common use case for the `transient` keyword is a field on a Visualforce
page that is needed only for the duration of a page request, but should not be part of the page's view state and would use too many
system resources to be recomputed many times during a request.

Some Apex objects are automatically considered transient, that is, their value does not get saved as part of the page's view state. These
objects include the following:

**•** PageReferences

**•** XmlStream classes

**•** Collections automatically marked as transient only if the type of object that they hold is automatically marked as transient, such as
a collection of Savepoints

**•** Most of the objects generated by system methods, such as `Schema.getGlobalDescribe` .

**•** `JSONParser` class instances.

[Static variables also don't get transmitted through the view state.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_static.htm)

The following example contains both a Visualforce page and a custom controller. Clicking the **refresh** button on the page causes the
transient date to be updated because it is being recreated each time the page is refreshed. The non-transient date continues to have
its original value, which has been deserialized from the view state, so it remains the same.

```
   <apex:page controller="ExampleController">

     T1: {!t1} <br/>

     T2: {!t2} <br/>

     <apex:form>

      <apex:commandLink value="refresh"/>

```


Apex Developer Guide Classes, Objects, and Interfaces

```
     </apex:form>

   </apex:page>

   public class ExampleController {

      DateTime t1;

      transient DateTime t2;

      public String getT1() {

        if (t1 == null) t1 = System.now();

        return '' + t1;

      }

      public String getT2() {

        if (t2 == null) t2 = System.now();

        return '' + t2;

      }

   }

```

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_JsonParser.htm)_ : JSONParser Class

##### Use the with sharing, without sharing, and inherited sharing Keywords Use the with sharing or without sharing keywords on a class to specify whether sharing rules are enforced. Use the

`inherited sharing` keyword on a class to run the class in the sharing mode of the calling class. The default sharing mode is
`with sharing` .

[Tip: For information about how to create sharing rules, see Sharing Rules in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.security_about_sharing_rules.htm&type=5&language=en_US)

With Sharing

##### Use the with sharing keyword when declaring a class to enforce sharing rules of the current user. Salesforce recommends that

you explicitly set this keyword to ensure that Apex code runs in the current user context. If a class doesn’t have an explicit sharing
declaration, then it defaults to `with sharing` .

```
   public with sharing class sharingClass {

        // Code here

        }

```

Without Sharing

##### Use the without sharing keyword when declaring a class to ensure that the sharing rules for the current user aren’t enforced.

For example, you can explicitly allow a class to ignore sharing rules even when it’s called from another class that does enforce sharing
rules.

```
   public without sharing class noSharing {

        // Code here

```


Apex Developer Guide Classes, Objects, and Interfaces

```
        }

```

Important: If you declare a class as `without sharing`, the class can access records that the current user otherwise doesn’t
have permission to access. Salesforce recommends that you use `without sharing` only for classes that require system-level
access.

Inherited Sharing

Use the `inherited sharing` keyword when declaring a class to enforce the sharing rules of the calling class. Using `inherited`
`sharing` is an advanced technique to determine the sharing mode at run time and design Apex classes that can run in either `with`
`sharing` or `without sharing` mode.

Important: Because the sharing mode is determined at run time, you must take extreme care to ensure that your Apex code is
secure to run in both `with sharing` and `without sharing` modes.

Using `inherited sharing`, along with other appropriate security checks, helps your code pass AppExchange security review and
ensures that your privileged Apex code isn’t used in unexpected or insecure ways. An Apex class with `inherited sharing` runs
in `with sharing` mode if used as:

**•** An Aura component controller

**•** An `@AuraEnabled` method called from a Lightning web component

**•** A Visualforce controller

**•** An Apex REST service

**•** An asynchronous Apex class

**•** Any other entry point to an Apex transaction

A class declared as `inherited sharing` runs as `without sharing` only when explicitly called from an already established
`without sharing` context.

Omitted Sharing

Apex without an explicit sharing declaration runs as `with sharing` by default. However, if an Apex class without an explicit sharing
declaration extends from a parent class, it adopts the same sharing mode as the parent class.

Important: We recommend that you always include an explicit sharing declaration on Apex classes that include database
operations or SOQL queries. This practice promotes intentionality and increases code maintainability.

Identifying the sharing mode for Apex classes compiled with API version 66.0 or earlier is challenging without an explicit declaration.
Determining the sharing mode in these cases requires a thorough investigation of the class inheritance tree, the caller sequence,
and the class’s behavior. See the Versioned Behavior Changes section.

Implementation in Apex Triggers

Apex triggers can’t have an explicit sharing declaration. Triggers always run in system mode and as `without sharing`, which
means that they bypass the sharing rules, field-level security, and object permissions of the current user. Instead, to enforce data access
settings, delegate business logic to separate trigger handlers, where you can define sharing and access modes.

Other Implementation Details

**•** Sharing declarations don’t enforce object-level access or field-level security. See Enforcing Object and Field Permissions.


Apex Developer Guide Classes, Objects, and Interfaces

**•** Except for methods in an `inherited sharing` class, the sharing mode of a method is determined by where the method is
defined, not where it’s called from. For example, a method defined in a `with sharing` class still enforces sharing rules even if
it’s called from a `without sharing` class. Exceptions also apply to methods for classes compiled with API version 66.0 or earlier.
See the Versioned Behavior Changes section.

**•** You can declare a sharing mode on both inner classes and outer classes. Inner classes don’t adopt the sharing mode of the container
class. Otherwise, the sharing setting applies to all code contained in the class, including initialization code, constructors, and methods.

**•** If an Apex class without an explicit sharing declaration extends from a parent class, then it adopts the same sharing mode as the
parent class.

**•** Asynchronous Apex classes defined with `inherited sharing` always run in `with sharing` mode for asynchronous
operations. Each asynchronous operation is a new entry point and the sharing mode isn’t serialized.

**•** Anonymous Apex and Connect in Apex always run in `with sharing` mode.

Best Practices

We recommend that you always include an explicit sharing declaration on Apex classes that include database operations or SOQL queries.
This practice promotes intentionality and increases code maintainability.

Versioned Behavior Changes

In API version 67.0 and later, classes without an explicit sharing declaration run in `with sharing` mode.

In API version 66.0 and earlier, the sharing mode of classes without an explicit sharing declaration is determined according these factors.

**•** If the class is part of an inheritance chain, and any class in that chain is saved as API version 67.0 and later, the class runs in `with`
`sharing` mode.

**•** If the class is an Aura controller or an `@AuraEnabled` method called from a Lightning web component, the class runs in `with`
`sharing` mode.

**•** Otherwise, the class runs in `without sharing` mode.

**•** If the class isn’t an Apex entry point, its sharing mode is defined by the sharing mode of the calling class.

#### Annotations

An Apex annotation modifies the way that a method or class is used, similar to annotations in Java. Annotations are defined with an
initial `@` symbol, followed by the appropriate keyword.


Apex Developer Guide Classes, Objects, and Interfaces

To add an annotation to a method, specify it immediately before the method or class definition. For example:

```
   global class MyClass {

      @Future

      Public static void myMethod(String a)

      {

         //long-running Apex code

      }

   }

```

Apex supports these annotations.

**•** `@AuraEnabled`

**•** `@Deprecated`

**•** `@Future`

**•** `@InvocableMethod`

**•** `@InvocableVariable`

**•** `@IsTest`

**•** `@JsonAccess`

**•** `@NamespaceAccessible`

**•** `@ReadOnly`

**•** `@RemoteAction`

**•** `@SuppressWarnings`

**•** `@TestSetup`

**•** `@TestVisible`

**•** Apex REST annotations:

**–** `@ReadOnly`

**–** `@RestResource(urlMapping='/` _**`yourUrl`**_ `')`

**–** `@HttpDelete`

**–** `@HttpGet`

**–** `@HttpPatch`

**–** `@HttpPost`

**–** `@HttpPut`

You can use multiple annotations for the same class or method. Specify each annotation on a separate line immediately before the class
or method definition. Some annotations can’t be used together. If applicable, these limitations are documented on the page for the
annotation.

1. AuraEnabled Annotation

2. Deprecated Annotation

3. Future Annotation
Use the `Future` annotation to identify methods that run asynchronously. A future method runs when Salesforce has available
resources.


Apex Developer Guide Classes, Objects, and Interfaces

4. IntegrationTest Annotation (Developer Preview)
Use the `IntegrationTest` annotation to mark both classes and methods that are used in integration testing.

5. InvocableMethod Annotation
Use the `InvocableMethod` annotation to identify methods that can be run as invocable actions.

6. InvocableVariable Annotation
To identify variables used by invocable methods in custom classes, use the `InvocableVariable` annotation.

7. IsTest Annotation

8. JsonAccess Annotation
The `@JsonAccess` annotation defined at Apex class level controls whether instances of the class can be serialized or deserialized.
If the annotation restricts the JSON or XML serialization and deserialization, a runtime `JSONException` exception is thrown.

9. NamespaceAccessible Annotation

10. ReadOnly Annotation

11. RemoteAction Annotation

12. SuppressWarnings Annotation

This annotation does nothing in Apex but can be used to provide information to third-party tools.

13. TestSetup Annotation

Methods defined with the `@TestSetup` annotation are used for creating common test records that are available for all test
methods in the class.

14. TearDown Annotation (Developer Preview)

Use the `TearDown` annotation to mark a cleanup method that runs after the test completes, regardless of pass or fail.

15. TestVisible Annotation

##### AuraEnabled Annotation

The `@AuraEnabled` annotation enables client-side and server-side access to an Apex controller method. Providing this annotation
makes your methods available to your Lightning components (both Lightning web components and Aura components). Only methods
with this annotation are exposed.

In API version 44.0 and later, you can improve runtime performance by caching method results on the client by using the annotation
`@AuraEnabled(cacheable=true)` . You can cache method results only for methods that retrieve data but don’t modify it.
Using this annotation eliminates the need to call `setStorable()` in JavaScript code on every action that calls the Apex method.

In API version 55.0 and later, you can use the annotation `@AuraEnabled(cacheable=true scope='global')` to enable
Apex methods to be cached in a global cache.

[For more information, see Lightning Aura Components Developer Guide and Lightning Web Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/)

Versioned Behavior Changes

In API version 55.0 and later, overloads aren’t allowed on methods annotated with `@AuraEnabled` .

##### Deprecated Annotation Use the Deprecated annotation to identify methods, classes, exceptions, enums, interfaces, or variables that can no longer be

referenced in subsequent releases of the managed package in which they reside. This annotation is useful when you’re refactoring code
in managed packages as the requirements evolve. New subscribers can’t see the deprecated elements, while the elements continue to
function for existing subscribers and API integrations.


Apex Developer Guide Classes, Objects, and Interfaces

The following code snippet shows a deprecated method. The same syntax can be used to deprecate classes, exceptions, enums, interfaces,
or variables.

```
     @Deprecated

     // This method is deprecated. Use myOptimizedMethod(String a, String b) instead.

     global void myMethod(String a) {

   }

```

Note the following rules when deprecating Apex identifiers:

**•** Unmanaged packages can’t contain code that uses the `deprecated` keyword.

**•** When an Apex item is deprecated, all `global` access modifiers that reference the deprecated identifier must also be deprecated.
Any global method that uses the deprecated type in its signature, either in an input argument or the method return type, must also
be deprecated. A deprecated item, such as a method or a class, can still be referenced internally by the package developer.

**•** `webservice` methods and variables can’t be deprecated.

**•** You can deprecate an `enum` but you can’t deprecate individual `enum` values.

**•** You can deprecate an interface but you can’t deprecate individual methods in an interface.

**•** You can deprecate an abstract class but you can’t deprecate individual abstract methods in an abstract class.

**•** You can’t remove the `Deprecated` annotation to undeprecate something in Apex after you’ve released a package version where
that item in Apex is deprecated.

For more information about package versions, see Managed Package Types on page 766.

##### Future Annotation Use the Future annotation to identify methods that run asynchronously. A future method runs when Salesforce has available resources.

Important: Salesforce now recommends that you use Queueable Apex instead of Apex future methods. Queueables have the
same use cases as future methods but offer extra benefits, including job IDs, support for non-primitive types, and job chaining.

See Queueable Apex.

##### For example, you can use the Future annotation when making an asynchronous web service callout to an external service. Without

the annotation, the web service callout is made from the same thread that is running the Apex code. Then no additional processing can
occur until the callout is complete (synchronous processing).

##### Methods with the Future annotation must be static methods, and can only return a void type. The specified parameters must be primitive data types, arrays of primitive data types, or collections of primitive data types. Methods with the Future annotation can’t

take sObjects or objects as arguments.

##### To make a method in a class execute asynchronously, define the method with the Future annotation. For example:

```
   public with sharing class MyFutureClass {

      @Future

      static void myMethod(String a, Integer i) {

        System.debug('Method called with: ' + a + ' and ' + i);

        // Perform long-running code

      }

   }

##### To allow callouts in a Future method, specify (callout=true) . The default is (callout=false), which prevents a method
```

from making callouts.


Apex Developer Guide Classes, Objects, and Interfaces

The following snippet shows how to specify that a method executes a callout:

```
   @Future (callout=true)

   public static void doCalloutFromFuture() {

      //Add code to perform callout

   }

```

Future Method Considerations

**•** Remember that any method that uses the `Future` annotation requires special consideration because the method doesn’t necessarily
execute in the same order that it’s called in.

**•** Methods with the `Future` annotation can’t be used in Visualforce controllers in either `get` _**`MethodName`**_ or `set` _**`MethodName`**_
methods, nor in the constructor.

**•** You can’t call a method annotated with `Future` from a method that also has the `Future` annotation. Nor can you call a trigger
from an annotated method that calls another annotated method.

##### IntegrationTest Annotation (Developer Preview) Use the IntegrationTest annotation to mark both classes and methods that are used in integration testing.

Note: The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The
feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases
or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or
without notice. Don't implement functionality developed with these commands or tools in your production package.

A class annotated with @IntegrationTest can only contain integration test methods and @TearDown methods. You can't mix
@IntegrationTest and @IsTest annotations on the same class.

Integration test methods cannot be called from non-test contexts or from @IsTest test methods. However, integration tests can call
methods in @IsTest utility classes, for example, shared test data factories.

##### InvocableMethod Annotation Use the InvocableMethod annotation to identify methods that can be run as invocable actions.

Note: If a flow invokes Apex, the running user must have the corresponding Apex class security set in their user profile or permission
set.

Invocable methods are called natively from REST, Apex, flows, Agentforce agents or AI bots that interact with the external API source.
Invocable methods have dynamic input and output values and support `describe` calls.

This code sample shows an invocable method with primitive data types.

```
   public with sharing class AccountQueryAction {

     @InvocableMethod(

      label='Get Account Names'

      description='Returns the list of account names corresponding to the specified account

    IDs.'

      category='Account'

     )

     public static List<String> getAccountNames(List<ID> ids) {

      List<Account> accounts = [

       SELECT Name

       FROM Account

```


Apex Developer Guide Classes, Objects, and Interfaces

```
       WHERE Id IN :ids

       WITH USER_MODE

      ];

      Map<ID, String> idToName = new Map<ID, String>();

      for (Account account : accounts) {

       idToName.put(account.Id, account.Name);

      }

      // put each name in the output at the same position as the id in the input

      List<String> accountNames = new List<String>();

      for (String id : ids) {

       accountNames.add(idToName.get(id));

      }

      return accountNames;

     }

   }

```

This code sample shows an invocable method with a specific sObject data type.

```
   public with sharing class AccountInsertAction {

     @InvocableMethod(

      label='Insert Accounts'

      description='Inserts the accounts specified and returns the IDs of the new accounts

   or null if account is failed to create.'

      category='Account'

     )

     public static List<ID> insertAccounts(List<Account> accounts) {

      Database.SaveResult[] results = Database.insert(

       accounts,

       false,

       AccessLevel.USER_MODE

      );

      List<ID> accountIds = new List<ID>();

      for (Database.SaveResult result : results) {

       if (result.isSuccess()) {

        accountIds.add(result.getId());

       } else {

        accountIds.add(null);

       }

      }

      return accountIds;

     }

   }

```

This code sample shows an invocable method with the generic sObject data type.

```
   public with sharing class GetFirstFromCollection {

     @InvocableMethod

     public static List<Results> execute(List<Requests> requestList) {

      List<Results> results = new List<Results>();

      for (Requests request : requestList) {

       List<SObject> inputCollection = request.inputCollection;

       SObject outputMember = inputCollection[0];

```


Apex Developer Guide Classes, Objects, and Interfaces

```
       //Create a Results object to hold the return values

       Results result = new Results();

       //Add the return values to the Results object

       result.outputMember = outputMember;

       //Add Result to the results List at the same position as the request is in the

   requests List

       results.add(result);

      }

      return results;

     }

     public with sharing class Requests {

      @InvocableVariable(

       label='Records for Input'

       description='yourDescription'

       required=true

      )

      public List<SObject> inputCollection;

     }

     public with sharing class Results {

      @InvocableVariable(

       label='Records for Output'

       description='yourDescription'

       required=true

      )

      public SObject outputMember;

     }

   }

```

This code sample shows an invocable method with a custom icon from an SVG file.

```
   global with sharing class CustomSvgIcon {

     @InvocableMethod(label='myIcon' iconName='resource:myPackageNamespace__google:top')

     global static List<Integer> myMethod(List<Integer> request) {

      List<Integer> results = new List<Integer>();

      for(Integer reqInt : request) {

        results.add(reqInt);

      }

      return results;

     }

   }

```

This code sample shows an invocable method with a custom icon from the Salesforce Lightning Design System (SLDS).

```
   public with sharing class CustomSldsIcon {

     @InvocableMethod(iconName='slds:standard:choice')

     public static void run() {}

     }

```

To handle exceptions within an invocable method, wrap the results in an Apex object that reports failures. The execution of the invocable
method must run and return the same number of results as inputs received even if errors occur.


Apex Developer Guide Classes, Objects, and Interfaces

For example, this code sample adjusts positive values by taking their square root and multiplying by pi, setting a success flag to `true` .
For negative values, it sets the success flag to `false` .

```
   global with sharing class AdjustPositiveValuesAction {

     @InvocableMethod(

      label='Adjust Positive Values'

      description='Returns the list of adjusted values. If a number is negative, a failure

   is reported for that value.'

     )

     public static List<AdjustmentResult> doAdjustment(List<Double> values) {

      List<AdjustmentResult> results = new List<AdjustmentResult>();

      for (Double value : values) {

       AdjustmentResult result = new AdjustmentResult();

       try {

        // Adjust the value, scale by pi.

        // Note: If the value is negative, this operation throws an exception.

        result.adjustedValue = Math.sqrt(value) * Math.PI;

        result.adjustmentSucceeded = true;

       } catch (Exception e) {

        // If a negative value caused an exception, mark the adjustment as failed, and

   keep processing other values.

        result.adjustmentSucceeded = false;

       }

       results.add(result);

      }

      return results;

     }

     global with sharing class AdjustmentResult {

      @InvocableVariable(label='True if adjustment succeeded')

      global boolean adjustmentSucceeded;

      @InvocableVariable(

       label='Adjusted value, only valid if adjustment succeeded'

      )

      global Double adjustedValue;

     }

   }

```

This test method checks whether the value adjustments were successful and verifies the calculated values for positive inputs.

```
   // Test class for AdjustPositiveValuesAction

   @IsTest

   private with sharing class AdjustPositiveValuesActionTest {

     @IsTest

   private static void doTest() {

      // Create a list of test values: 4, -1, 1

      List<Double> values = new List<Double>();

      values.add(4);

      values.add(-1);

      values.add(1);

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      Test.startTest();

      // Call the doAdjustment method with the test values.

      List<AdjustPositiveValuesAction.AdjustmentResult> results =

   AdjustPositiveValuesAction.doAdjustment(values);

      Test.stopTest();

      // Assertions to check if adjustments were successful or not for each input value.

      Assert.isTrue(results[0].adjustmentSucceeded);

      Assert.isFalse(results[1].adjustmentSucceeded);

      Assert.isTrue(results[2].adjustmentSucceeded);

      // Assertions to check the calculated adjusted values for positive inputs.

      Assert.areEqual(2 * Math.PI, results[0].adjustedValue);

      Assert.areEqual(Math.PI, results[2].adjustedValue);

     }

   }

```

Supported Modifiers

All modifiers are optional.

**label**
The label for the method, which appears as the action name in Flow Builder. The default is the method name, though we recommend
that you provide a label.

**description**
The description for the method, which appears as the action description in Flow Builder. The default is `Null` .

**callout**
The callout modifier identifies whether the method calls to an external system. If the method calls to an external system, add

`callout=true` . The default value is `false` .

**capabilityType**
The capability that integrates with the method. The valid format is _`Name://Name`_, for example:

```
    PromptTemplateType://SalesEmail

```

**category**
The category for the method, which appears as the action category in Flow Builder. If no category is provided (by default), actions
appear under Uncategorized.

**configurationEditor**
The custom property editor that is registered with the method and appears in Flow Builder when an admin configures the action.
If you don’t specify this modifier, Flow Builder uses the standard property editor.

**iconName**
The name of the icon to use as a custom icon for the action in the Flow Builder canvas. You can specify an SVG file that you uploaded
as a static resource or a Salesforce Lightning Design System standard icon.

InvocableMethod Considerations

**Implementation Notes**

**•** The invocable method must be `static` and `public` or `global`, and its class must be an outer class.


Apex Developer Guide Classes, Objects, and Interfaces

**•** Only one method in a class can have the `InvocableMethod` annotation.

**•** The only annotation that can be used with the `InvocableMethod` annotation is `Deprecated` .

**Inputs and Outputs**
There can be at most one input parameter and its data type must be one of the following:

**•** A list of a primitive data type or a list of lists of a primitive data type – the generic `Object` type isn’t supported.

**•** A list of an sObject type or a list of lists of an sObject type.

**•** A list of the generic sObject type ( `List<sObject>` ) or a list of lists of the generic sObject type ( `List<List<sObject>>` ).

**•** A list of a user-defined type, containing variables of the supported types or user-defined Apex types, with the
`InvocableVariable` annotation. To implement your data type, create a custom global or public Apex class. The class
must contain at least one member variable with the invocable variable annotation.

Note: `@InvocableVariable` fields of type `List<List<sObject>>` are not supported in user-defined Apex
classes and cause a runtime error. Use `List<List<sObject>>` only as a direct `@InvocableMethod` return
type.

If the return type isn’t `Null`, the data type returned by the method must be one of the following:

**•** A list of a primitive data type or a list of lists of a primitive data type – the generic `Object` type isn’t supported.

**•** A list of an sObject type or a list of lists of an sObject type.

**•** A list of the generic sObject type ( `List<sObject>` ) or a list of lists of the generic sObject type ( `List<List<sObject>>` ).

**•** A list of a user-defined type, containing variables of the supported types or user-defined Apex types, with the
`InvocableVariable` annotation. To implement your data type, create a custom global or public Apex class. The class
must contain at least one member variable with the invocable variable annotation.

Note: `@InvocableVariable` fields of type `List<List<sObject>>` are not supported in user-defined Apex
classes and cause a runtime error. Use `List<List<sObject>>` only as a direct `@InvocableMethod` return
type.

For a correct bulkification implementation, the Inputs and Outputs must match on both the size and the order. For example, the
i-th Output entry must correspond to the i-th Input entry. Matching entries are required for data correctness when your action is in
bulkified execution, such as when an apex action is used in a record trigger flow.

**Managed Packages**

**•** You can use invocable methods in packages, but after you add an invocable method you can’t remove it from later versions of
the package.

**•** Public invocable methods can be referred to by flows and processes within the managed package.

**•** Global invocable methods can be referred to anywhere in the subscriber org. Only global invocable methods appear in Flow
Builder and Process Builder in the subscriber org. See Best Practices for Using Global Apex in Managed Packages on page 773.


Apex Developer Guide Classes, Objects, and Interfaces

[For more information about invocable actions, see Apex Actions in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_action.meta/api_action/actions_intro.htm) _Actions Developer Guide_ .

SEE ALSO:

##### InvocableVariable Annotation

_[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_action.meta/api_action/actions_obj_apex.htm)_ : Apex Actions

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_actions_invocable.htm)_ : Invocable Actions

_Salesforce Help_ [: Add a Custom Icon to an Apex-Defined Action](https://help.salesforce.com/s/articleView?id=platform.flow_build_extend_apex_type_add_a_custom_icon.htm&type=5&language=en_US)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Invocable_Action.htm)_ : Action Class

_Lightning Web Components Developer Guide_ [: Develop Custom Property Editors for Flow Builder](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.use_flow_custom_property_editor)

_Prompt Builder_ [: Ground with Apex](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_ground_apex.htm&type=5&language=en_US)

Making Callouts to External Systems from Invocable Actions

Extend Invocable Action Configuration in Flow Builder

##### InvocableVariable Annotation To identify variables used by invocable methods in custom classes, use the InvocableVariable annotation. The InvocableVariable annotation identifies a class variable used as an input or output parameter for an InvocableMethod

method’s invocable action. If you create your own custom class to use as the input or output to an invocable method, you can annotate
individual class member variables to make them available to the method.

This code sample shows an invocable method with invocable variables.

```
   global class ConvertLeadAction {

     @InvocableMethod(label='Convert Leads')

     global static List<ConvertLeadActionResult> convertLeads(List<ConvertLeadActionRequest>

    requests) {

      List<ConvertLeadActionResult> results = new List<ConvertLeadActionResult>();

      for (ConvertLeadActionRequest request : requests) {

       results.add(convertLead(request));

      }

      return results;

     }

     public static ConvertLeadActionResult convertLead(ConvertLeadActionRequest request) {

      Database.LeadConvert lc = new Database.LeadConvert();

      lc.setLeadId(request.leadId);

      lc.setConvertedStatus(request.convertedStatus);

      if (request.accountId != null) {

        lc.setAccountId(request.accountId);

      }

      if (request.contactId != null) {

       lc.setContactId(request.contactId);

      }

      if (request.overWriteLeadSource != null && request.overWriteLeadSource) {

       lc.setOverwriteLeadSource(request.overWriteLeadSource);

      }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      if (request.createOpportunity != null && !request.createOpportunity) {

       lc.setDoNotCreateOpportunity(!request.createOpportunity);

      }

      if (request.opportunityName != null) {

       lc.setOpportunityName(request.opportunityName);

      }

      if (request.ownerId != null) {

       lc.setOwnerId(request.ownerId);

      }

      if (request.sendEmailToOwner != null && request.sendEmailToOwner) {

       lc.setSendNotificationEmail(request.sendEmailToOwner);

      }

      Database.LeadConvertResult lcr = Database.convertLead(lc, true);

      if (lcr.isSuccess()) {

       ConvertLeadActionResult result = new ConvertLeadActionResult();

       result.accountId = lcr.getAccountId();

       result.contactId = lcr.getContactId();

       result.opportunityId = lcr.getOpportunityId();

       return result;

      } else {

       throw new ConvertLeadActionException(lcr.getErrors()[0].getMessage());

      }

     }

     global class ConvertLeadActionRequest {

      @InvocableVariable(required=true)

      global ID leadId;

      @InvocableVariable(required=true)

      global String convertedStatus;

      @InvocableVariable

      global ID accountId;

      @InvocableVariable

      global ID contactId;

      @InvocableVariable

      global Boolean overWriteLeadSource;

      @InvocableVariable

      global Boolean createOpportunity;

      @InvocableVariable

      global String opportunityName;

      @InvocableVariable

      global ID ownerId;

      @InvocableVariable

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      global Boolean sendEmailToOwner;

     }

     global class ConvertLeadActionResult {

      @InvocableVariable

      global ID accountId;

      @InvocableVariable

      global ID contactId;

      @InvocableVariable

      global ID opportunityId;

     }

     class ConvertLeadActionException extends Exception {}

   }

```

This code sample shows an invocable method with invocable variables that have the generic sObject data type.

```
   public with sharing class GetFirstFromCollection {

     @InvocableMethod

     public static List <Results> execute (List<Requests> requestList) {

      List<SObject> inputCollection = requestList[0].inputCollection;

      SObject outputMember = inputCollection[0];

      //Create a Results object to hold the return values

      Results response = new Results();

      //Add the return values to the Results object

      response.outputMember = outputMember;

      //Wrap the Results object in a List container

      //(an extra step added to allow this interface to also support bulkification)

      List<Results> responseWrapper= new List<Results>();

      responseWrapper.add(response);

      return responseWrapper;

     }

   public class Requests {

    @InvocableVariable(label=' Records for Input ' description=' yourDescription ' required=true)

     public List<SObject> inputCollection;

     }

   public class Results {

     @InvocableVariable(label=' Records for Output ' description=' yourDescription '

   required=true)

     public SObject outputMember;

     }

   }

```

Supported Modifiers

All modifiers are optional.


Apex Developer Guide Classes, Objects, and Interfaces

Tip: Default values, labels, and placeholder text appear in Flow Builder for the Action element that corresponds to an invocable
method. These modifiers help admins understand how to use variables in the flow.

**defaultValue**
Provide a value to the action at runtime, if no value is provided then these default values are provided to the action at runtime.
Valid invocable variable data types are:

**•** Boolean - fields must have a value of `'true'` or `'false'` and case-insensitive.

```
       @InvocableVariable(defaultValue='true')

       public Boolean myBoolean;

```

**•** Decimal - fields must have a value of `'validDecimalValue'` where the floating point value can’t have a suffix.

```
       @InvocableVariable(defaultValue='123.4')

       public Decimal myDecimal;

```

**•** Double - fields must have a value of `'validDoubleValue'` where the d suffix is required and case-insensitive.

```
       @InvocableVariable(defaultValue='867.3D')

       public Double myDouble;

```

**•** Integer - fields must have a value of `'validIntegerValue'` where the integer value can’t have a suffix.

```
       @InvocableVariable(defaultValue='-214')

       public Integer myInteger;

```

**•** Long - fields must have a value of `'validLongValue'` where the l suffix is required and case-insensitive.

```
       @InvocableVariable(defaultValue='922337L')

       public Long myLong;

```

**•** String - fields can use any valid string value including the empty string.

```
       @InvocableVariable(defaultValue='hello world!')

       public String myString;

```

**description**
The description for the variable. The default is `Null` .

**label**
The label for the variable. The default is the variable name.

**placeholderText**
Provides examples or additional guidance about the invocable variable, such as examples of values that can set the invocable variable.
Valid invocable variable data types are:

**•** Double - fields must have a value of `'validDoubleValue'` where the d suffix is required and case-insensitive.

**•** Integer - fields must have a value of `'validIntegerValue'` where the integer value can’t have a suffix.

**•** String - fields can use any valid string value including the empty string.

**required**
Specifies whether the variable is required. If not specified, the default is `false` . The value is ignored for output variables.

Note: The `defaultValue` modifier throws an error when used with `required` .


Apex Developer Guide Classes, Objects, and Interfaces

Example: The invocable variable annotation supports the modifiers shown in this example.

```
      @InvocableVariable(label=' yourLabel '

      description=' yourDescription ' placeholderText=' yourPlaceholderText '

      required=(true | false))

```

The invocable variable annotation supports `defaultValue` in this example.

```
      @InvocableVariable(defaultValue=' yourDefaultValue ')

           global String createOpportunity;

```

InvocableVariable Considerations

**•** Other annotations can’t be used with the `InvocableVariable` annotation.

**•** Only global and public variables can be invocable variables.

**•** The invocable variable can’t be any of these:

**–** A non-member variable such as a `static` or `local` variable.

**–** A property.

**–** A `final` variable.

**–** `Protected` or `private` .

**•** The data type of the invocable variable must be one of these:

**–** A primitive other than Object

**–** An sObject, either the generic sObject or a specific sObject

**–** A list of primitives, sObjects, or objects created from Apex classes

**–** A list of lists of primitives or objects created from Apex classes

**•** The invocable variable name in Apex must match the name in the flow. The name is case-sensitive.

**•** For managed packages:

**–** Public invocable variables can be set in flows and processes within the same managed package.

**–** Global invocable variables can be set anywhere in the subscriber org. Only global invocable variables appear in Flow Builder and
Process Builder in the subscriber org.

**•** Starting in API version 66.0, Apex classes used for invocable action parameters must have a visible no-argument constructor. Use
the default constructor or add your own constructor. The constructor must be public for non-packaged classes or global for packaged
classes invoked from outside the package. See Using Constructors on page 68.

SEE ALSO:

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Invocable_Action.htm)_ : Action Class

Extend Invocable Action Configuration in Flow Builder

##### IsTest Annotation

Use the `@IsTest` annotation to define classes and methods that only contain code used for testing your app. The annotation can
take multiple modifiers within parentheses and separated by blanks.


Apex Developer Guide Classes, Objects, and Interfaces

Note: The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce
recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future
release.

Classes and methods that are defined as `@IsTest` can be either `private` or `public` . Classes defined as `@IsTest` must be
top-level classes.

Note: Classes defined with the `@IsTest` annotation don't count against your organization limit of 6 MB for all Apex code.

Here’s an example of a private test class that contains two test methods.

```
   @IsTest

   private class MyTestClass {

     // Methods for testing

     @IsTest

     static void test1() {

       // Implement test code

     }

     @IsTest

     static void test2() {

       // Implement test code

     }

   }

```

Here’s an example of a public test class that contains utility methods for test data creation:

```
   @IsTest

   public class TestUtil {

     public static void createTestAccounts() {

       // Create some test accounts

     }

     public static void createTestContacts() {

       // Create some test contacts

     }

   }

```

Classes defined as `@IsTest` can't be interfaces or enums.

Methods of a public test class can only be called from a running test, that is, a test method or code invoked by a test method. Non-test
requests can’t call public methods.. To learn about the various ways you can run test methods, see Run Unit Test Methods.

**`@IsTest(SeeAllData=true)`** Annotation

For Apex code saved using Salesforce API version 24.0 and later, use the `@IsTest(SeeAllData=true)` annotation to grant test
classes and individual test methods access to all data in the organization. The access includes pre-existing data that the test didn’t create.
Starting with Apex code saved using Salesforce API version 24.0, test methods don’t have access to pre-existing data in the organization.
However, test code saved against Salesforce API version 23.0 and earlier continues to have access to all data in the organization. See
Isolation of Test Data from Organization Data in Unit Tests on page 727.


Apex Developer Guide Classes, Objects, and Interfaces

**Considerations for the** **`@IsTest(SeeAllData=true)`** **Annotation**

**•** If a test class is defined with the `@IsTest(SeeAllData=true)` annotation, the `SeeAllData=true` applies to all
test methods that don’t explicitly set the `SeeAllData` keyword.

**•** The `@IsTest(SeeAllData=true)` annotation is used to open up data access when applied at the class or method level.
However, if the containing class has been annotated with `@IsTest(SeeAllData=true)`, annotating a method with

`@IsTest(SeeAllData=false)` is ignored for that method. In this case, that method still has access to all the data in
the organization. Annotating a method with `@IsTest(SeeAllData=true)` overrides, for that method, an

`@IsTest(SeeAllData=false)` annotation on the class.

**•** `@IsTest(SeeAllData=true)` and `@IsTest(IsParallel=true)` annotations can’t be used together on the
same Apex method.

This example shows how to define a test class with the `@IsTest(SeeAllData=true)` annotation. All the test methods in this
class have access to all data in the organization.

```
   // All test methods in this class can access all data.

   @IsTest(SeeAllData=true)

   public class TestDataAccessClass {

      // This test accesses an existing account.

      // It also creates and accesses a new test account.

      @IsTest

      static void myTestMethod1() {

        // Query an existing account in the organization.

        Account a = [SELECT Id, Name FROM Account WHERE Name='Acme' LIMIT 1];

        System.assert(a != null);

        // Create a test account based on the queried account.

        Account testAccount = a.clone();

        testAccount.Name = 'Acme Test';

        insert testAccount;

        // Query the test account that was inserted.

        Account testAccount2 = [SELECT Id, Name FROM Account

                       WHERE Name='Acme Test' LIMIT 1];

        System.assert(testAccount2 != null);

      }

      // Like the previous method, this test method can also access all data

      // because the containing class is annotated with @IsTest(SeeAllData=true).

      @IsTest

      static void myTestMethod2() {

        // Can access all data in the organization.

     }

   }

```

This second example shows how to apply the `@IsTest(SeeAllData=true)` annotation on a test method. Because the test
method’s class isn’t annotated, you have to annotate the method to enable access to all data for the method. The second test method


Apex Developer Guide Classes, Objects, and Interfaces

doesn’t have this annotation, so it can access only the data it creates. In addition, it can access objects that are used to manage your
organization, such as users.

```
   // This class contains test methods with different data access levels.

   @IsTest

   private class ClassWithDifferentDataAccess {

      // Test method that has access to all data.

      @IsTest(SeeAllData=true)

      static void testWithAllDataAccess() {

        // Can query all data in the organization.

      }

      // Test method that has access to only the data it creates

      // and organization setup and metadata objects.

      @IsTest

      static void testWithOwnDataAccess() {

        // This method can still access the User object.

        // This query returns the first user object.

        User u = [SELECT UserName,Email FROM User LIMIT 1];

        System.debug('UserName: ' + u.UserName);

        System.debug('Email: ' + u.Email);

        // Can access the test account that is created here.

        Account a = new Account(Name='Test Account');

        insert a;

        // Access the account that was just created.

        Account insertedAcct = [SELECT Id,Name FROM Account

                       WHERE Name='Test Account'];

        System.assert(insertedAcct != null);

      }

   }

```

**`@IsTest(OnInstall=true)`** Annotation

Use the `@IsTest(OnInstall=true)` annotation to specify which Apex tests are executed during package installation. This
annotation is used for tests in managed or unmanaged packages. Only test methods with this annotation, or methods that are part of
a test class that has this annotation, are executed during package installation. Tests annotated to run during package installation must
pass in order for the package installation to succeed. It’s no longer possible to bypass a failing test during package installation. A test
method or a class that doesn't have this annotation, or that is annotated with `@IsTest(OnInstall=false)` or `@IsTest`, isn’t
executed during installation.

Tests annotated with `IsTest(OnInstall=true)` that run during package install and upgrade aren’t counted towards code
coverage. However, code coverage is tracked and counted during a package creation operation. Because Apex code installed from a
managed package is excluded from org level requirements for code coverage, it’s unlikely that you’re affected. But, if you track managed
package test coverage, you must rerun these tests outside of the package install or upgrade operation for code coverage statistics to be
updated. Package install isn’t blocked by code coverage requirements.

This example shows how to annotate a test method that is executed during package installation. In this example, `test1` is executed
but `test2` and `test3` isn’t.

```
   public class OnInstallClass {

     // Implement logic for the class.

     public void method1(){

```


Apex Developer Guide Classes, Objects, and Interfaces

```
       // Some code

     }

   }

   @IsTest

   private class OnInstallClassTest {

     // This test method will be executed

     // during the installation of the package.

     @IsTest(OnInstall=true)

     static void test1() {

       // Some test code

     }

     // Tests excluded from running during the

     // the installation of a package.

     @IsTest

     static void test2() {

       // Some test code

     }

     @IsTest

     static void test3() {

       // Some test code

     }

   }

```

**`@IsTest(IsParallel=true)`** Annotation

Use the `@IsTest(IsParallel=true)` annotation to indicate test classes that can run in parallel.

**Considerations for the** **`@IsTest(IsParallel=true)`** **annotation**

**•** This annotation forces the test to run in parallel even if the org-wide `Disable Parallel Apex Testing` option is
set.

**•** `@IsTest(SeeAllData=true)` and `@IsTest(IsParallel=true)` annotations can’t be used together on the
same Apex method.

**Restrictions on Apex tests using the** **`@IsTest(IsParallel=true)`** **annotation**

**•** Tests can’t call the `Test.getStandardPricebookId()` method.

**•** Tests can’t call the `System.schedule()` and `System.enqueueJob()` methods.

**•** Tests can’t insert a ContentNote SObject.

**•** Tests can’t create User or GroupMember SObjects.

**•** Tests can’t use the SObjects that are listed in sObjects That Can't Be Used Together in DML Operations.

**`@IsTest(critical=true)`** Annotation (Beta)

Important: The `RunRelevantTests` test level and the associated `@IsTest()` annotations are pilot or beta services that
are subject to the Beta Services Terms at Agreements — Salesforce.com or a written Unified Pilot Agreement if executed by
Customer, and applicable terms in the Product Terms Directory. Use of these pilot or beta services are at the Customer’s sole
discretion.


Apex Developer Guide Classes, Objects, and Interfaces

If you set the deployment test level to `[RunRelevantTests](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_deploy_run_relevant_tests.htm)`, use the `@IsTest(critical=true)` annotation to guarantee
that the test class always runs during deployments, regardless of the deployment payload. This annotation is available at the test class
level in Salesforce API version 66.0 and later. Using this annotation on a test method results in a compilation error.

This example code shows a test class marked with the `@IsTest(critical=true)` annotation. When you set the deployment
test level to `RunRelevantTests`, the tests in this class always run.

```
   @IsTest(critical=true)

   public with sharing class AccountServiceTest {

     // ...

   }

```

**`@IsTest(testFor='...')`** Annotation (Beta)

Important: The `RunRelevantTests` test level and the associated `@IsTest()` annotations are pilot or beta services that
are subject to the Beta Services Terms at Agreements — Salesforce.com or a written Unified Pilot Agreement if executed by
Customer, and applicable terms in the Product Terms Directory. Use of these pilot or beta services are at the Customer’s sole
discretion.

If you set the deployment test level to `[RunRelevantTests](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_deploy_run_relevant_tests.htm)`, use the `@IsTest(testFor='...')` annotation to guarantee
that the tests in the class run whenever the deployment includes new or modified versions of the referenced Apex components. This
annotation is available at the test class level in Salesforce API version 66.0 and later. Using this annotation on a test method results in a
compilation error.

To use `@IsTest(testFor='...')`, set the `testFor` parameter to a comma-separated string of Apex classes and Apex triggers.
For Apex classes, use the format `ApexClass:` _**`ClassName`**_ . For Apex triggers, use the format `ApexTrigger:` _**`TriggerName`**_ .
If specifying a class or trigger from a different namespace, use the fully qualified name, for example,
`ApexClass:` _**`MyNamespace`**_ `.` _**`ClassName`**_ .

This example code shows a test class marked with the `@IsTest(testFor='...')` annotation. If you set the deployment test
level to `RunRelevantTests`, this test class runs whenever `AccountHandler` or `AccountTrigger` are new or modified
in the deployment payload.

```
   @IsTest(testFor='ApexClass:AccountHandler,ApexTrigger:AccountTrigger')

   public with sharing class AccountHandlerTest {

     // ...

   }

##### JsonAccess Annotation

```

The `@JsonAccess` annotation defined at Apex class level controls whether instances of the class can be serialized or deserialized. If
the annotation restricts the JSON or XML serialization and deserialization, a runtime `JSONException` exception is thrown.

The `serializable` and `deserializable` parameters of the `@JsonAccess` annotation enforce the contexts in which Apex
allows serialization and deserialization. You can specify one or both parameters, but you can’t specify the annotation with no parameters.
The valid values for the parameters to indicate whether serialization and deserialization are allowed:

**•** `never` : never allowed

**•** `sameNamespace` : allowed only for Apex code in the same namespace

**•** `samePackage` : allowed only for Apex code in the same package (impacts only second-generation packages)

**•** `always` : always allowed for any Apex code


Apex Developer Guide Classes, Objects, and Interfaces

This example code shows an Apex class marked with the `@JsonAccess` annotation.

```
   // SomeSerializableClass is serializable in the same package and deserializable in the

   wider namespace

   @JsonAccess(serializable='samePackage' deserializable='sameNamespace')

   public class SomeSerializableClass { }

   // AlwaysDeserializable class is always deserializable and serializable only in the same

   namespace (default value from version 49.0 and later)

   @JsonAccess(deserializable='always')

   public class AlwaysDeserializable { }

```

**`JsonAccess`** Considerations

**•** If an Apex class annotated with `JsonAccess` is extended, the extended class doesn’t inherit this property.

**•** If the `toString` method is applied on objects that mustn't be serialized, private data can be exposed. You must override the
`toString` method on objects whose data must be protected. For example, serializing an object stored as a key in a Map invokes
the `toString` method. The generated map includes key (string) and value entries, thus exposing all the fields of the object.

Versioned Behavior Changes

In versions 48.0 and earlier, the default access for deserialization is `always` and the default access for serialization is `sameNamespace`
to preserve the existing behavior. From version 49.0 onwards, the default access for both serialization and deserialization is
`sameNamespace` .

##### NamespaceAccessible Annotation

The `@NamespaceAccessible` makes public Apex in a package available to other packages that use the same namespace. Without
this annotation, Apex classes, methods, interfaces, properties, and abstract classes defined in a 2GP package aren’t accessible to the
other packages with which they share a namespace. Apex that is declared global is always available across all namespaces, and needs
no annotation.

[For more information on 2GP managed packages, see Second-Generation Managed Packages in](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ .

Considerations for Apex Accessibility Across Packages

**•** You can’t use the `@NamespaceAccessible` annotation for an `@AuraEnabled` Apex method or an `@InvocableMethod`
Apex method.

**•** You can add or remove the `@NamespaceAccessible` annotation at any time, even on managed and released Apex code.
Make sure that you don’t have dependent packages relying on the functionality of the annotation before adding or removing it.

**•** When adding or removing `@NamespaceAccessible` Apex from a package, consider the impact to customers with installed
versions of other packages that reference this package’s annotation. Before pushing a package upgrade, ensure that no customer
is running a package version that would fail to fully compile when the upgrade is pushed.

**•** If a public interface is declared as `@NamespaceAccessible`, then all interface members inherit the annotation. Individual
interface members can’t be annotated with `@NamespaceAccessible` .

**•** If a public or protected variable or method is declared as `@NamespaceAccessible`, its defining class must be either global or
public with the `@NamespaceAccessible` annotation.


Apex Developer Guide Classes, Objects, and Interfaces

**•** If a public or protected inner class is declared as `@NamespaceAccessible`, its enclosing class must be either global or public
with the `@NamespaceAccessible` annotation.

This example shows an Apex class marked with the `@NamespaceAccessible` annotation. The class is accessible to other packages
within the same namespace. The first constructor is also visible within the namespace, but the second constructor isn’t.

```
   // A namespace-visible Apex class

   @NamespaceAccessible

   public class MyClass {

      private Boolean bypassFLS;

      // A namespace-visible constructor that only allows secure use

      @NamespaceAccessible

      public MyClass() {

        bypassFLS = false;

      }

      // A package private constructor that allows use in trusted contexts,

      // but only internal to the package

      public MyClass (Boolean bypassFLS) {

        this.bypassFLS = bypassFLS;

      }

      @NamespaceAccessible

      protected Boolean getBypassFLS() {

        return bypassFLS;

      }

   }

```

Versioned Behavior Changes

In API version 47.0 and later, `@NamespaceAccessible` isn’t allowed on an entity marked with `@AuraEnabled` . Therefore, an
Aura or Lightning web component installed from a package can’t call an Apex method from another package, even if both packages
are in the same namespace. However, an `@AuraEnabled` public method from one package can call a `@NamespaceAccessible`
public method from another package in the same namespace.

Therefore, this behavior isn’t allowed.

```
   // In Package1 in the Acme namespace

   public with sharing class MyController {

      // Stacking these annotations isn't allowed

      @AuraEnabled

      @NamespaceAccessible

      public static void myMethod( ){

        // ...

      }

   }

```

But this behavior is allowed.

```
   // In Package1 in the Acme namespace

   public with sharing class Service {

      @NamespaceAccessible

      public static void doSomething() {

        // ...

      }

```


Apex Developer Guide Classes, Objects, and Interfaces

```
   }

   // In Package2 in the Acme namespace

   public with sharing class MyController {

      // Can call the @NamespaceAccessible method

      @AuraEnabled

      public static void myMethod( ){

        Service.doSomething();

      }

   }

```

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are
annotated with `@NamespaceAccessible` . For accessibility considerations, see Considerations for Apex Acessibility Across Packages.
[For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_namespace_visibility.htm)

##### ReadOnly Annotation

The `@ReadOnly` annotation allows you to perform less restrictive queries against the Lightning Platform database by increasing the
limit of the number of returned rows for a request to 1,000,000. All other limits still apply. The annotation blocks the following operations
within the request: DML operations, calls to `System.schedule`, and enqueued asynchronous Apex jobs.

The `@ReadOnly` annotation is available for REST and SOAP Web services and the `Schedulable` interface. To use the `@ReadOnly`
annotation, the top-level request must be in the schedule execution or the Web service invocation. For example, if a Visualforce page
calls a Web service that contains the `@ReadOnly` annotation, the request fails because Visualforce is the top-level request, not the
Web service.

Visualforce pages can call controller methods with the `@ReadOnly` annotation, and those methods run with the same relaxed
restrictions. To increase other Visualforce-specific limits, such as the size of a collection that can be used by an iteration component like

`<apex:pageBlockTable>`, you can set the `readonly` attribute on the `<apex:page>` tag to `true` . For more information,
[see Working with Large Sets of Data in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_controller_readonly_context.htm) _[Visualforce Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)_ .

Versioned Behavior Changes

Prior to API version 49.0, using `@ReadOnly` on Apex REST methods (@HttpDelete, @HttpGet, @HttpPatch, @HttpPost, or @HttpPut)
also required annotating the method with `@RemoteAction` . In API version 49.0 and later, you can annotate Apex REST methods
with just `@ReadOnly` .

##### RemoteAction Annotation The RemoteAction annotation provides support for Apex methods used in Visualforce to be called via JavaScript. This process is

often referred to as JavaScript remoting.

##### Note: Methods with the RemoteAction annotation must be static and either global or public .

Add the Apex class as a custom controller or a controller extension to your page.

```
   <apex:page controller="MyController" extension="MyExtension">

```

Warning: Adding a controller or controller extension grants access to all `@RemoteAction` methods in that Apex class, even
if those methods aren’t used in the page. Anyone who can view the page can execute all `@RemoteAction` methods and
provide fake or malicious data to the controller.


Apex Developer Guide Classes, Objects, and Interfaces

Then, add the request as a JavaScript function call. A simple JavaScript remoting invocation takes the following form.

```
   [ namespace .] MyController . method (

      [parameters...,]

     callbackFunction,

      [configuration]

   );

```

**Table 2: Remote Request Elements**

In your controller, your Apex method declaration is preceded with the `@RemoteAction` annotation like this:

```
@RemoteAction

global static String getItemId(String objectName) { ... }

```

Apex `@RemoteAction` methods must be `static` and either `global` or `public` .

Your method can take Apex primitives, collections, typed and generic sObjects, and user-defined Apex classes and interfaces as arguments.
Generic sObjects must have an ID or sobjectType value to identify actual type. Interface parameters must have an apexType to identify
actual type. Your method can return Apex primitives, sObjects, collections, user-defined Apex classes and enums, `SaveResult`,
`UpsertResult`, `DeleteResult`, `SelectOption`, or `PageReference` .

For more information, see “JavaScript Remoting for Apex Controllers” in the _Visualforce Developer's Guide_ .

##### SuppressWarnings Annotation

This annotation does nothing in Apex but can be used to provide information to third-party tools.

The `@SuppressWarnings` annotation does nothing in Apex but can be used to provide information to third-party tools.

##### TestSetup Annotation

Methods defined with the `@TestSetup` annotation are used for creating common test records that are available for all test methods
in the class.


Apex Developer Guide Classes, Objects, and Interfaces

Syntax

Test setup methods are defined in a test class, take no arguments, and return no value. The following is the syntax of a test setup method.

```
   @TestSetup static void methodName () {

   }

```

If a test class contains a test setup method, the testing framework executes the test setup method first, before any test method in the
class. Records that are created in a test setup method are available to all test methods in the test class and are rolled back at the end of
test class execution. If a test method changes those records, such as record field updates or record deletions, those changes are rolled
back after each test method finishes execution. The next executing test method gets access to the original unmodified state of those
records.

Note: You can have only one test setup method per test class.

Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access
to organization data by using the `@IsTest(SeeAllData=true)` annotation, test setup methods aren’t supported in this class.
Because data isolation for tests is available for API versions 24.0 and later, test setup methods are also available for those versions only.

For more information, see Using Test Setup Methods.

##### TearDown Annotation (Developer Preview) Use the TearDown annotation to mark a cleanup method that runs after the test completes, regardless of pass or fail.

Note: The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The
feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases
or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or
without notice. Don't implement functionality developed with these commands or tools in your production package.

The annotation is applied to a static method that runs after the integration test completes, regardless of whether the test passed, failed,
or threw an exception. Use this annotation to clean up committed test data. The teardown transaction auto-commits at the end of the
execution.

##### TestVisible Annotation Use the TestVisible annotation to allow test methods to access private or protected members of another class outside the test

class. These members include methods, member variables, and inner classes. This annotation enables a more permissive access level
for running tests only. This annotation doesn’t change the visibility of members if accessed by non-test classes.

With this annotation, you don’t have to change the access modifiers of your methods and member variables to public if you want to
access them in a test method. For example, if a private member variable isn’t supposed to be exposed to external classes but it must be
##### accessible by a test method, you can add the TestVisible annotation to the variable definition. This example shows how to annotate a private class member variable and private method with TestVisible .

```
   public class TestVisibleExample {

      // Private member variable

      @TestVisible private static Integer recordNumber = 1;

      // Private method

      @TestVisible private static void updateRecord(String name) {

        // Do something

      }

   }

```


Apex Developer Guide Classes, Objects, and Interfaces

This test class uses the previous class and contains the test method that accesses the annotated member variable and method.

```
   @IsTest

   private class TestVisibleExampleTest {

      @IsTest static void test1() {

        // Access private variable annotated with TestVisible

        Integer i = TestVisibleExample.recordNumber;

        System.assertEquals(1, i);

        // Access private method annotated with TestVisible

        TestVisibleExample.updateRecord('RecordName');

        // Perform some verification

      }

   }

##### Apex REST Annotations

```

Use these annotations to expose an Apex class as a RESTful Web service.

**•** `@ReadOnly`

**•** `@RestResource(urlMapping='/` _**`yourUrl`**_ `')`

**•** `@HttpDelete`

**•** `@HttpGet`

**•** `@HttpPatch`

**•** `@HttpPost`

**•** `@HttpPut`

SEE ALSO:

Exposing Apex Classes as REST Web Services

###### RestResource Annotation

The `@RestResource` annotation is used at the class level and enables you to expose an Apex class as a REST resource.

Some considerations when using this annotation:

**•** The URL mapping is relative to `https://` _`instance`_ `.salesforce.com/services/apexrest/` .

**•** The URL mapping can contain a wildcard (*).

**•** The URL mapping is case-sensitive. For example, a URL mapping for `my_url` matches a REST resource containing `my_url` and
not `My_Url` .

**•** To use this annotation, your Apex class must be defined as global.

URL Guidelines

URL path mappings are as follows:

**•** The path must begin with a forward slash (/).

**•** The path can be up to 255 characters long.

**•** A wildcard (*) that appears in a path must be preceded by a forward slash (/). Additionally, unless the wildcard is the last character
in the path, it must be followed by a forward slash (/).


Apex Developer Guide Classes, Objects, and Interfaces

The rules for mapping URLs are:

**•** An exact match always wins.

**•** If no exact match is found, find all the patterns with wildcards that match, and then select the longest (by string length) of those.

**•** If no wildcard match is found, an HTTP response status code 404 is returned.

The URL for a namespaced class contains the namespace. For example, if your class is in namespace `abc` and the class is mapped to
`your_url`, then the API URL is modified as follows:
`https://` _`instance`_ `.salesforce.com/services/apexrest/abc/your_url/` . In the case of a URL collision, the
namespaced class is always used.

###### HttpDelete Annotation

The `@HttpDelete` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This
method is called when an HTTP `DELETE` request is sent, and deletes the specified resource.

To use this annotation, your Apex method must be defined as global static.

###### HttpGet Annotation

The `@HttpGet` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method
is called when an HTTP `GET` request is sent, and returns the specified resource.

These are some considerations when using this annotation:

**•** To use this annotation, your Apex method must be defined as global static.

**•** Methods annotated with `@HttpGet` are also called if the HTTP request uses the `HEAD` request method.

###### HttpPatch Annotation

The `@HttpPatch` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method
is called when an HTTP `PATCH` request is sent, and updates the specified resource.

To use this annotation, your Apex method must be defined as global static.

###### HttpPost Annotation

The `@HttpPost` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method
is called when an HTTP `POST` request is sent, and creates a new resource.

To use this annotation, your Apex method must be defined as global static.

###### HttpPut Annotation

The `@HttpPut` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method
is called when an HTTP `PUT` request is sent, and creates or updates the specified resource.

To use this annotation, your Apex method must be defined as global static.

#### Classes and Casting

In general, all type information is available at run time. This means that Apex enables _casting_, that is, a data type of one class can be
assigned to a data type of another class, but only if one class is a subclass of the other class. Use casting when you want to convert an
object from one data type to another.


Apex Developer Guide Classes, Objects, and Interfaces

In the following example, `CustomReport` extends the class `Report` . Therefore, it is a subclass of that class. This means that you
can use casting to assign objects with the parent data type ( `Report` ) to the objects of the subclass data type ( `CustomReport` ).

```
   public virtual class Report {

   }

   public class CustomReport extends Report {

   }

```

In the following code segment, a custom report object is first added to a list of report objects. Then the custom report object is returned
as a report object, which is then cast back into a custom report object.

```
   ...

     // Create a list of report objects

     Report[] Reports = new Report[5];

     // Create a custom report object

     CustomReport a = new CustomReport();

     // Because the custom report is a sub class of the Report class,

     // you can add the custom report object a to the list of report objects

     Reports.add(a);

     // The following is not legal:

     // CustomReport c = Reports.get(0);

     // because the compiler does not know that what you are

     // returning is a custom report.

     // You must use cast to tell it that you know what

     // type you are returning. Instead, get the first item in the list

     // by casting it back to a custom report object

     CustomReport c = (CustomReport) Reports.get(0);

   ...

```


Apex Developer Guide Classes, Objects, and Interfaces

**Casting Example**

In addition, an interface type can be cast to a sub-interface or a class type that implements that interface.

Tip: To verify if a class is a specific type of class, use the `instanceOf` keyword. For more information, see Using the

`instanceof` Keyword on page 86.

##### 1. Classes and Collections

2. Collection Casting

##### Classes and Collections

Lists and maps can be used with classes and interfaces, in the same ways that lists and maps can be used with sObjects. This means, for
example, that you can use a user-defined data type for the value or the key of a map. Likewise, you can create a set of user-defined
objects.

If you create a map or list of interfaces, any child type of the interface can be put into that collection. For instance, if the List contains an
interface _`i1`_, and _`MyC`_ implements _`i1`_, then _`MyC`_ can be placed in the list.

SEE ALSO:

Using Custom Types in Map Keys and Sets


Apex Developer Guide Classes, Objects, and Interfaces

##### Collection Casting

Because collections in Apex have a declared type at runtime, Apex allows collection casting.

Collections can be cast in a similar manner that arrays can be cast in Java. For example, a list of CustomerPurchaseOrder objects can be
assigned to a list of PurchaseOrder objects if class `CustomerPurchaseOrder` is a child of class `PurchaseOrder` .

```
   public virtual class PurchaseOrder {

      Public class CustomerPurchaseOrder extends PurchaseOrder {

      }

      {

        List<PurchaseOrder> POs = new PurchaseOrder[] {};

        List<CustomerPurchaseOrder> CPOs = new CustomerPurchaseOrder[]{};

        POs = CPOs;

      }

   }

```

Once the `CustomerPurchaseOrder` list is assigned to the `PurchaseOrder` list variable, it can be cast back to a list of
CustomerPurchaseOrder objects, but only because that instance was originally instantiated as a list of CustomerPurchaseOrder objects.
A list of PurchaseOrder objects that is instantiated as such cannot be cast to a list of CustomerPurchaseOrder objects, even if the list of
PurchaseOrder objects contains only CustomerPurchaseOrder objects.

If the user of a PurchaseOrder list that only includes CustomerPurchaseOrders objects tries to insert a non-CustomerPurchaseOrder
subclass of `PurchaseOrder` (such as `InternalPurchaseOrder` ), a runtime exception results. This is because Apex collections
have a declared type at runtime.

Note: Maps behave in the same way as lists with regards to the value side of the Map. If the value side of map A can be cast to
the value side of map B, and they have the same key type, then map A can be cast to map B. A runtime error results if the casting
is not valid with the particular map at runtime.

#### Differences Between Apex Classes and Java Classes

Apex classes and Java classes work in similar ways, but there are some significant differences.

These are the major differences between Apex classes and Java classes:

**•** Inner classes and interfaces can only be declared one level deep inside an outer class.

**•** Static methods and variables can only be declared in a top-level class definition, not in an inner class.

**•** An inner class behaves like a static Java inner class, but doesn’t require the `static` keyword. An inner class can have instance
member variables like an outer class, but there is no implicit pointer to an instance of the outer class (using the `this` keyword).

**•** The `private` access modifier is the default, and means that the method or variable is accessible only within the Apex class in
which it is defined. If you do not specify an access modifier, the method or variable is `private` .

**•** Specifying no access modifier for a method or variable and the `private` access modifier are synonymous.

**•** The `public` access modifier means the method or variable can be used by any Apex in this application or namespace.

**•** The `global` access modifier means the method or variable can be used by any Apex code that has access to the class, not just
the Apex code in the same application. This access modifier should be used for any method that needs to be referenced outside of
the application, either in the SOAP API or by other Apex code. If you declare a method or variable as `global`, you must also declare
the class that contains it as `global` .

**•** Methods and classes are final by default.

**–** The `virtual` definition modifier allows extension and overrides.


Apex Developer Guide Classes, Objects, and Interfaces

**–** The `override` keyword must be used explicitly on methods that override base class methods.

**•** Methods defined in an interface have the same access modifier ( `public` or `global` ) as the interface.

**•** Exception classes must extend either exception or another user-defined exception.

**–** Their names must end with the word `exception` .

**–** Exception classes have four implicit constructors that are built-in, although you can add others.

**•** Classes and interfaces can be defined in triggers and anonymous blocks, but only as local.

SEE ALSO:

Exceptions in Apex

#### Class Definition Creation

Use the class editor to create a class in Salesforce.

**1.** From Setup, enter _`Apex Classes`_ in the `Quick Find` box, then select **Apex Classes** .

**2.** Click **New** .

**3.** Click **Version Settings** to specify the version of Apex and the API used with this class. If your organization has installed managed
packages from the AppExchange, you can also specify which version of each managed package to use with this class. Use the default
values for all versions. This associates the class with the most recent version of Apex and the API, as well as each managed package.
You can specify an older version of a managed package if you want to access components or functionality that differs from the most
recent package version. You can specify an older version of Apex and the API to maintain specific behavior.

**4.** In the class editor, enter the Apex code for the class. A single class can be up to 1 million characters in length, not including comments,
test methods, or classes defined using `@IsTest` .

**5.** Click **Save** to save your changes and return to the class detail screen, or click **Quick Save** to save your changes and continue editing
your class. Your Apex class must compile correctly before you can save your class.

Classes can also be automatically generated from a WSDL by clicking **Generate from WSDL** . See SOAP Services: Defining a Class from
a WSDL Document on page 616.

Once saved, classes can be invoked through class methods or variables by other Apex code, such as a trigger.

Note: To aid backwards-compatibility, classes are stored with the version settings for a specified version of Apex and the API. If
the Apex class references components, such as a custom object, in installed managed packages, the version settings for each
managed package referenced by the class is saved too. Additionally, classes are stored with an `isValid` flag that is set to `true`
as long as dependent metadata hasn’t changed since the class was last compiled. If any changes are made to object names or
fields that are used in the class, including superficial changes such as edits to an object or field description, or if changes are made
to a class that calls this class, the `isValid` flag is set to `false` . When a trigger or Web service call invokes the class, the code
is recompiled and the user is notified if there are any errors. If there are no errors, the `isValid` flag is reset to `true` .

The Apex Class Editor

The Apex and Visualforce editor has the following functionality:

**Syntax highlighting**
The editor automatically applies syntax highlighting for keywords and all functions and operators.

**Search (** **)**
Search enables you to search for text within the current page, class, or trigger. To use search, enter a string in the `Search` textbox
and click **Find Next** .


Apex Developer Guide Classes, Objects, and Interfaces

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
This button allows you to highlight a specified line number. If the line isn’t currently visible, the editor scrolls to that line.

**Undo (** **) and Redo (** **)**
Use undo to reverse an editing action and redo to recreate an editing action that was undone.

**Font size**
Select a font size from the dropdown list to control the size of the characters displayed in the editor.

**Line and column position**
The line and column position of the cursor is displayed in the status bar at the bottom of the editor. This can be used with go to line

( ) to quickly navigate through the editor.

**Line and character count**
The total number of lines and characters is displayed in the status bar at the bottom of the editor.

##### 1. Naming Conventions 2. Name Shadowing Naming Conventions

We recommend following Java standards for naming, that is, classes start with a capital letter, methods start with a lowercase verb, and
variable names should be meaningful.

It is not legal to define a class and interface with the same name in the same class. It is also not legal for an inner class to have the same
name as its outer class. However, methods and variables have their own namespaces within the class so these three types of names do
not clash with each other. In particular it is legal for a variable, method, and a class within a class to have the same name.

SEE ALSO:

Variables

##### Name Shadowing

Member variables can be shadowed by local variables—in particular function arguments. This allows methods and constructors of the
standard Java form:

```
   Public Class Shadow {

     String s;

     Shadow(String s) { this.s = s; } // Same name ok

     setS(String s) { this.s = s; } // Same name ok

   }

```


Apex Developer Guide Classes, Objects, and Interfaces

Member variables in one class can shadow member variables with the same name in a parent classes. This can be useful if the two classes
are in different top-level classes and written by different teams. For example, if one has a reference to a class C and wants to gain access
to a member variable M in parent class P (with the same name as a member variable in C) the reference should be assigned to a reference
to P first.

Static variables can be shadowed across the class hierarchy—so if P defines a static S, a subclass C can also declare a static S. References
to S inside C refer to that static—in order to reference the one in P, the syntax P.S must be used.

Static class variables cannot be referenced through a class instance. They must be referenced using the raw variable name by itself (inside
that top-level class file) or prefixed with the class name. For example:

```
   public class p1 {

     public static final Integer CLASS_INT = 1;

     public class c { };

   }

   p1.c c = new p1.c();

   // This is illegal

   // Integer i = c.CLASS_INT;

   // This is correct

   Integer i = p1.CLASS_INT;

#### Namespace Prefix

```

The Salesforce application supports the use of _namespace prefixes_ . Namespace prefixes are used in managed AppExchange packages
to differentiate custom object and field names from names used by other organizations.

Important: When creating a namespace, use something that’s useful and informative to users. However, don’t name a namespace
after a person (for example, by using a person's name, nickname, or private information). Once namespaces are assigned, they
cannot be changed.

After a developer registers a globally unique namespace prefix and registers it with AppExchange registry, external references to custom
object and field names in the developer's managed packages take on the following long format:

```
    namespace_prefix __ obj_or_field_name __c

```

These fully qualified names can be onerous to update in working SOQL or SOSL statements, and Apex once a class is marked as “managed”.
Therefore, Apex supports a default namespace for schema names. When looking at identifiers, the parser assumes that the namespace
of the current object is the namespace of all other objects and fields unless otherwise specified. Therefore, a stored class must refer to
custom object and field names directly (using _**`obj_or_field_name`**_ `__c` ) for those objects that are defined within its same
application namespace.

Tip: Only use namespace prefixes when referring to custom objects and fields in managed packages that have been installed to
your organization from the AppExchange.

Using Namespaces When Invoking Package Methods

To invoke a method that is defined in a managed package, Apex allows fully qualified identifiers of the form:

```
    namespace_prefix . class . method ( args )

```


Apex Developer Guide Classes, Objects, and Interfaces

Versioned Behavior Changes

In API version 34.0 and later, Schema.DescribeSObjectResult on a custom SObjectType includes map keys prefixed with the namespace,
even if the namespace is that of currently executing code. If you work with multiple namespaces and generate runtime describe data,
make sure that your code accesses keys correctly using the namespace prefix.

##### 1. Using the System Namespace

2. Using the Schema Namespace
The `Schema` namespace provides classes and methods for working with schema metadata information. We implicitly import
`Schema.*`, but you must fully qualify your uses of `Schema` namespace elements when they have naming conflicts with items
in your unmanaged code. If your org contains an Apex class that has the same name as an sObject, add the `Schema` namespace
prefix to the sObject name in your code.

3. Namespace, Class, and Variable Name Precedence

4. Type Resolution and System Namespace for Types

##### Using the System Namespace

The `System` namespace is the default namespace in Apex. This means that you can omit the namespace when creating a new instance
of a system class or when calling a system method. For example, because the built-in URL class is in the `System` namespace, both of
these statements to create an instance of the `URL` class are equivalent:

```
   System.URL url1 = new System.URL('https:// MyDomainName .my.salesforce.com/');

```

And:

```
   URL url1 = new URL('https:// MyDomainName .my.salesforce.com/');

```

Similarly, to call a static method on the `URL` class, you can write either of the following:

```
   System.URL.getCurrentRequestUrl();

```

Or:

```
   URL.getCurrentRequestUrl();

```

Note: In addition to the `System` namespace, there is a built-in `System` class in the `System` namespace, which provides
methods like `assertEquals` and `debug` . Don’t get confused by the fact that both the namespace and the class have the
same name in this case. The `System.debug('debug message');` and `System.System.debug('debug`

`message');` statements are equivalent.

##### Using the System Namespace for Disambiguation

It is easier to not include the `System` namespace when calling static methods of system classes, but there are situations where you
must include the `System` namespace to differentiate the built-in Apex classes from custom Apex classes with the same name. If your
organization contains Apex classes that you’ve defined with the same name as a built-in class, the Apex runtime defaults to your custom
class and calls the methods in your class. Let’s take a look at the following example.

Create this custom Apex class:

```
   public class Database {

      public static String query() {

        return 'wherefore art thou namespace?';

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      }

   }

```

Execute this statement in the Developer Console:

```
   sObject[] acct = Database.query('SELECT Name FROM Account LIMIT 1');

   System.debug(acct[0].get('Name'));

```

When the `Database.query` statement executes, Apex looks up the query method on the custom `Database` class first. However,
the query method in this class doesn’t take any parameters and no match is found, hence you get an error. The custom `Database`
class overrides the built-in `Database` class in the `System` namespace. To solve this problem, add the `System` namespace prefix
to the class name to explicitly instruct the Apex runtime to call the query method on the built-in Database class in the `System`
namespace:

```
   sObject[] acct = System. Database.query('SELECT Name FROM Account LIMIT 1');

   System.debug(acct[0].get('Name'));

```

SEE ALSO:

##### Using the Schema Namespace Using the Schema Namespace

The `Schema` namespace provides classes and methods for working with schema metadata information. We implicitly import `Schema.*`,
but you must fully qualify your uses of `Schema` namespace elements when they have naming conflicts with items in your unmanaged
code. If your org contains an Apex class that has the same name as an sObject, add the `Schema` namespace prefix to the sObject name
in your code.

You can omit the namespace when creating an instance of a schema class or when calling a schema method. For example, because the
`DescribeSObjectResult` and `FieldSet` classes are in the `Schema` namespace, these code segments are equivalent.

```
   Schema.DescribeSObjectResult d = Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FSMap = d.fieldSets.getMap();

```

And:

```
   DescribeSObjectResult d = Account.sObjectType.getDescribe();

   Map<String, FieldSet> FSMap = d.fieldSets.getMap();

##### Using the Schema Namespace for Disambiguation

```

Use `Schema.` _**`object_name`**_ to refer to an sObject that has the same name as a custom class. This disambiguation instructs the
Apex runtime to use the sObject.

```
   public class Account {

     public Integer myInteger;

   }

   // ...

   // Create a standard Account object myAccountSObject

   Schema.Account myAccountSObject = new Schema.Account();

   // Create accountClassInstance, a custom class in your org

   Account accountClassInstance = new Account();

```


Apex Developer Guide Classes, Objects, and Interfaces

```
   myAccountSObject.Name = 'Snazzy Account';

   accountClassInstance.myInteger = 1;

```

SEE ALSO:

Using the System Namespace

##### Namespace, Class, and Variable Name Precedence

Because local variables, class names, and namespaces can all hypothetically use the same identifiers, the Apex parser evaluates expressions
in the form of `name1.name2.[...].nameN` as follows:

**1.** The parser first assumes that `name1` is a local variable with `name2`    - `nameN` as field references.

**2.** If the first assumption does not hold true, the parser then assumes that `name1` is a class name and `name2` is a static variable name
with `name3`      - `nameN` as field references.

**3.** If the second assumption does not hold true, the parser then assumes that `name1` is a namespace name, `name2` is a class name,
`name3` is a static variable name, and `name4`    - `nameN` are field references.

**4.** If the third assumption does not hold true, the parser reports an error.

If the expression ends with a set of parentheses (for example, `name1.name2.[...].nameM.nameN()` ), the Apex parser evaluates
the expression as follows:

**1.** The parser first assumes that `name1` is a local variable with `name2`    - `nameM` as field references, and `nameN` as a method
invocation.

**2.** If the first assumption does not hold true:

**•** If the expression contains only two identifiers ( `name1.name2()` ), the parser then assumes that `name1` is a class name and
`name2` is a method invocation.

**•** If the expression contains more than two identifiers, the parser then assumes that `name1` is a class name, `name2` is a static
variable name with `name3`        - `nameM` as field references, and `nameN` is a method invocation.

**3.** If the second assumption does not hold true, the parser then assumes that `name1` is a namespace name, `name2` is a class name,
`name3` is a static variable name, `name4`    - `nameM` are field references, and `nameN` is a method invocation.

**4.** If the third assumption does not hold true, the parser reports an error.

However, with class variables Apex also uses dot notation to reference member variables. Those member variables might refer to other
class instances, or they might refer to an sObject which has its own dot notation rules to refer to field names (possibly navigating foreign
keys).

Once you enter an sObject field in the expression, the remainder of the expression stays within the sObject domain, that is, sObject fields
cannot refer back to Apex expressions.

For instance, if you have the following class:

```
   public class c {

     c1 c1 = new c1();

     class c1 { c2 c2; }

     class c2 { Account a; }

   }

```

Then the following expressions are all legal:

```
   c.c1.c2.a.name

   c.c1.c2.a.owner.lastName.toLowerCase()

```


Apex Developer Guide Classes, Objects, and Interfaces

```
   c.c1.c2.a.tasks

   c.c1.c2.a.contacts.size()

##### Type Resolution and System Namespace for Types

```

Because the type system must resolve user-defined types defined locally or in other classes, the Apex parser evaluates types as follows:

**1.** For a type reference `TypeN`, the parser first looks up that type as a scalar type.

**2.** If `TypeN` is not found, the parser looks up locally defined types.

**3.** If `TypeN` still is not found, the parser looks up a class of that name.

**4.** If `TypeN` still is not found, the parser looks up system types such as sObjects.

For the type `T1.T2` this could mean an inner type `T2` in a top-level class `T1`, or it could mean a top-level class `T2` in the namespace
`T1` (in that order of precedence).

#### Apex Code Versions

To aid backwards-compatibility, classes and triggers are stored with the version settings for a specific Salesforce API version.

If an Apex class or trigger references components, such as a custom object, in installed managed packages, the version settings for each
managed package referenced by the class are saved too. This ensures that as Apex, the API, and the components in managed packages
evolve in subsequent released versions, a class or trigger is still bound to versions with specific, known behavior.

Setting a version for an installed package determines the exposed interface of any Apex code in the installed package. This allows you
to continue to reference Apex that may be deprecated in the latest version of an installed package, if you installed a version of the
package before the code was deprecated.

Typically, you reference the latest Salesforce API version and each installed package version. If you save an Apex class or trigger without
specifying the Salesforce API version, the class or trigger is associated with the latest installed version by default. If you save or redeploy
an Apex class or trigger that references a managed package without specifying a version of the managed package, the class or trigger
is associated with the latest installed version of the managed package by default.

Versioning of Apex Classes and Methods

When classes and methods are added to the Apex language, those classes and methods are available to all API versions your Apex code
is saved with, regardless of the API version (Salesforce release) they were introduced in. For example, if a method was added in API
version 33.0, you can use this method in a custom class saved with API version 33.0 or another class saved with API version 25.0.

There is one exception to this rule. The classes and methods of the `[ConnectApi](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_connect_api.htm)` namespace are supported only in the API versions
specified in the documentation. For example, if a class or method is introduced in API version 33.0, it is not available in earlier versions.
For more information, see ConnectApi Versioning and Equality Checking on page 464.

Keep these guidelines in mind regarding API version usage:

**•** Salesforce strongly recommends that you use the latest available API version.

**•** If you can't upgrade to the latest version yet, use API versions released in the past three years, for improved performance, security,
and compatibility.

**•** To reduce complexity, consolidate your Apex codebase to use the minimal number of API versions, ideally, just one API version.

For a non-exhaustive list of major Apex behavior changes across API versions, organized by version number, see Apex Versioned Behavior
Changes on page 794.

Setting the Salesforce API Version for Classes and Triggers


Apex Developer Guide Classes, Objects, and Interfaces

Setting Package Versions for Apex Classes and Triggers
As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use.

SEE ALSO:

Use Apex Referenced by Managed Packages

##### Setting the Salesforce API Version for Classes and Triggers

To set the Salesforce API and Apex version for a class or trigger:

**1.** Edit either a class or trigger, and click **Version Settings** .

**2.** Select the `Version` of the Salesforce API. This version is also the version of Apex associated with the class or trigger.

**3.** Click **Save** .

If you pass an object as a parameter in a method call from one Apex class, C1, to another class, C2, and C2 has different fields exposed
due to the Salesforce API version setting, the fields in the objects are controlled by the version settings of C2.

In this example, the `Categories` field is set to `null` after calling the `insertIdea` method in class C2 from a method in the test
class C1, because the `Categories` field isn’t available in version 13.0 of the API.

The first class is saved using Salesforce API version 13.0:

```
   // This class is saved using Salesforce API version 13.0

   // Version 13.0 does not include the Idea.categories field

   global class C2

   {

      global Idea insertIdea(Idea a) {

        insert a; // category field set to null on insert

        // retrieve the new idea

        Idea insertedIdea = [SELECT title FROM Idea WHERE Id =:a.Id];

        return insertedIdea;

      }

   }

```

The following class is saved using Salesforce API version 16.0:

```
   @IsTest

   // This class is bound to API version 16.0 by Version Settings

   private class C1

   {

      static testMethod void testC2Method() {

        Idea i = new Idea();

        i.CommunityId = '09aD000000004YCIAY';

        i.Title = 'Testing Version Settings';

        i.Body = 'Categories field is included in API version 16.0';

        i.Categories = 'test';

        C2 c2 = new C2();

        Idea returnedIdea = c2.insertIdea(i);

        // retrieve the new idea

        Idea ideaMoreFields = [SELECT title, categories FROM Idea

           WHERE Id = :returnedIdea.Id];

```


Apex Developer Guide Classes, Objects, and Interfaces

```
        // assert that the categories field from the object created

        // in this class is not null

        System.assert(i.Categories != null);

        // assert that the categories field created in C2 is null

        System.assert(ideaMoreFields.Categories == null);

      }

   }

##### Setting Package Versions for Apex Classes and Triggers

```

As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use.

Note: In Summer ’25 and later, package subscribers can use version settings to specify the version of a migrated second-generation
managed package (2GP) that an Apex class or trigger depends on. This functionality is already available to first-generation managed
[packages (1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)
[in Migrated Second-Generation Managed Packages (2GP).](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)

To configure the package version settings for a class or trigger:

**1.** From Setup, enter _`Apex Classes`_ or _`Apex Triggers`_ in the Quick Find box, and then select **Apex Classes** or **Apex Triggers** .

**2.** From the list, click **Edit** for the Apex class or trigger that you want to configure.

**3.** Click the **Version Settings** tab.

**4.** From the Version dropdown for the managed package, select the desired version referenced by the class or trigger.

The class or trigger continues to use this version even if you install later versions of the managed package, unless you manually
update the version setting.

**5.** Click **Save** .

When working with package version settings, keep these considerations in mind.

**•** By default, an Apex class or trigger that references a managed package is associated with the version of the package installed when
that class or trigger was last saved or deployed.

**•** If a class or trigger references a managed package, you can’t remove the package’s version settings for that class or trigger. To find
where the class or trigger references a managed package, on the class or trigger’s Detail page, click **Show Dependencies** .

Tip: You can also set the package version for an Apex class or trigger through metadata deployments or with API requests. See
Set Package Versions for Apex Classes and Triggers on page 783.

SEE ALSO:

Use Apex Referenced by Managed Packages

#### Lists of Custom Types and Sorting

Lists can hold objects of your user-defined types (your Apex classes). Lists of user-defined types can be sorted.

To sort such a list, your Apex class can implement the `Comparator` interface and pass it as a parameter to the `List.sort` method.
Alternatively, your Apex class can implement the `Comparable` interface.

The sort criteria and sort order depend on the implementation that you provide for the `Comparable.compareTo` or the
`Comparator.compare` method.


Apex Developer Guide Classes, Objects, and Interfaces

To perform locale-sensitive comparisons and sorting, use the `Collator` class. Because locale-sensitive sorting can produce different
results depending on the user running the code, avoid using it in triggers or in code that expects a particular sort order.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Collator.htm)_ : Collator Class

_Apex Reference Guide_ [: Comparable Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_comparable.htm)

_Apex Reference Guide_ [: Comparator Interface](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_System_Comparator.htm)

#### Using Custom Types in Map Keys and Sets

You can add instances of your own Apex classes to maps and sets.

For maps, instances of your Apex classes can be added either as keys or values. If you add them as keys, there are some special rules that
your class must implement for the map to function correctly; that is, for the key to fetch the right value. Similarly, if set elements are
instances of your custom class, your class must follow those same rules.

Warning: If the object in your map keys or set elements changes after being added to the collection, it won’t be found anymore
because of changed field values.

When using a custom type (your Apex class) for the map key or set elements, provide `equals` and `hashCode` methods in your
class. Apex uses these two methods to determine equality and uniqueness of keys for your objects.

Adding **`equals`** and **`hashCode`** Methods to Your Class

To ensure that map keys of your custom type are compared correctly and their uniqueness can be determined consistently, provide an
implementation of the following two methods in your class:

**•** The `[equals](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Object.htm#apex_System_Object_equals)` method with this signature:

```
     public Boolean equals(Object obj) {

       // Your implementation

     }

```

**•** The `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Object.htm#apex_System_Object_hashCode)` method with this signature:

```
     public Integer hashCode() {

       // Your implementation

     }

```

Sample

This sample shows how to implement the `equals` and `hashCode` methods. The class that provides those methods is listed first. It
also contains a constructor that takes two Integers. The second example is a code snippet that creates three objects of the class, two of
which have the same values. Next, map entries are added using the pair objects as keys. The sample verifies that the map has only two
entries since the entry that was added last has the same key as the first entry, and hence, overwrote it. The sample then uses the `==`
operator, which works as expected because the class implements `equals` . Also, some additional map operations are performed, like
checking whether the map contains certain keys, and writing all keys and values to the debug log. Finally, the sample creates a set and
adds the same objects to it. It verifies that the set size is two, since only two objects out of the three are unique.

```
   public class PairNumbers {

      Integer x,y;

```


Apex Developer Guide Classes, Objects, and Interfaces

```
      public PairNumbers(Integer a, Integer b) {

        x=a;

        y=b;

      }

      public Boolean equals(Object obj) {

        if (obj instanceof PairNumbers) {

           PairNumbers p = (PairNumbers)obj;

           return ((x==p.x) && (y==p.y));

        }

        return false;

      }

      public Integer hashCode() {

        return (31 * x) ^ y;

      }

   }

```

This code snippet makes use of the `PairNumbers` class.

```
   Map<PairNumbers, String> m = new Map<PairNumbers, String>();

   PairNumbers p1 = new PairNumbers(1,2);

   PairNumbers p2 = new PairNumbers(3,4);

   // Duplicate key

   PairNumbers p3 = new PairNumbers(1,2);

   m.put(p1, 'first');

   m.put(p2, 'second');

   m.put(p3, 'third');

   // Map size is 2 because the entry with

   // the duplicate key overwrote the first entry.

   System.assertEquals(2, m.size());

   // Use the == operator

   if (p1 == p3) {

      System.debug('p1 and p3 are equal.');

   }

   // Perform some other operations

   System.assertEquals(true, m.containsKey(p1));

   System.assertEquals(true, m.containsKey(p2));

   System.assertEquals(false, m.containsKey(new PairNumbers(5,6)));

   for(PairNumbers pn : m.keySet()) {

      System.debug('Key: ' + pn);

   }

   List<String> mValues = m.values();

   System.debug('m.values: ' + mValues);

   // Create a set

   Set<PairNumbers> s1 = new Set<PairNumbers>();

   s1.add(p1);

   s1.add(p2);

   s1.add(p3);

```


### Apex Developer Guide Working with Data in Apex

```
   // Verify that we have only two elements

   // since the p3 is equal to p1.

   System.assertEquals(2, s1.size());

### Working with Data in Apex

```

You can add and interact with data in the Lightning Platform persistence layer. The sObject data type is the main data type that holds
data objects. You’ll use Data Manipulation Language (DML) to work with data, and use query languages to retrieve data, such as the (),
among other things.

#### Working with sObjects

In this developer guide, the term _`sObject`_ refers to any object that can be stored in the Lightning platform database.

Data Manipulation Language
Apex enables you to insert, update, delete or restore data in the database. DML operations allow you to modify records one at a time
or in batches.

SOQL and SOSL Queries
You can evaluate Salesforce Object Query Language (SOQL) or Salesforce Object Search Language (SOSL) statements on-the-fly in
Apex by surrounding the statement in square brackets.

SOQL For Loops
SOQL `for` loops iterate over all of the sObject records returned by a SOQL query.

sObject Collections
You can manage sObjects in lists, sets, and maps.

Dynamic Apex

Apex Security and Sharing Model
The Apex security model includes record-level, field-level, and object-level security mechanisms. You can control record-level security
modes by using the `with sharing`, `without sharing`, and `inherited sharing` keywords on classes. Apex runs
in user mode by default, which means that user permissions on objects and field-level security are respected. A user cannot run
code that tries to access fields or objects that are hidden from the user. Other security mechanisms include the
`Security.stripInaccessible()` method, and Field and SObject describe methods.

Custom Settings
Custom settings are similar to custom objects. Application developers can create custom sets of data and associate custom data for
an organization, profile, or specific user. All custom settings data is exposed in the application cache, which enables efficient access
without the cost of repeated queries to the database. Formula fields, validation rules, flows, Apex, and SOAP API can then use this
data.

#### Working with sObjects

In this developer guide, the term _`sObject`_ refers to any object that can be stored in the Lightning platform database.

sObject Types
An sObject variable represents a row of data and can only be declared in Apex using SOAP API name of the object.

Accessing SObject Fields

Validating sObjects and Fields


Apex Developer Guide Working with Data in Apex

##### sObject Types

An sObject variable represents a row of data and can only be declared in Apex using SOAP API name of the object.

For example:

```
   Account a = new Account();

   MyCustomObject__c co = new MyCustomObject__c();

```

Similar to SOAP API, Apex allows the use of the generic sObject abstract type to represent any object. The sObject data type can be used
in code that processes different types of sObjects.

The `new` operator still requires a concrete sObject type, so all instances are specific sObjects. For example:

```
   sObject s = new Account();

```

You can also use casting between the generic sObject type and the specific sObject type. For example:

```
   // Cast the generic variable s from the example above

   // into a specific account and account variable a

   Account a = (Account)s;

   // The following generates a runtime error

   Contact c = (Contact)s;

```

Because sObjects work like objects, you can also have the following:

```
   Object obj = s;

   // and

   a = (Account)obj;

```

DML operations work on variables declared as the generic sObject data type as well as with regular sObjects.

sObject variables are initialized to `null`, but can be assigned a valid object reference with the `new` operator. For example:

```
   Account a = new Account();

```

Developers can also specify initial field values with comma-separated `name = value` pairs when instantiating a new sObject. For
example:

```
   Account a = new Account(name = 'Acme', billingcity = 'San Francisco');

```

For information on accessing existing sObjects from the Lightning Platform database, see “SOQL and SOSL Queries” in the _SOQL and_
_SOSL Reference_ .

Note: The Lightning Platform assigns ID values automatically when an object record is initially inserted to the database for the
first time. For more information see Lists on page 29.

Custom Labels

Custom labels aren’t standard sObjects. You can’t create a new instance of a custom label. You can only access the value of a custom
label using `system.label.` _**`label_name`**_ . For example:

```
   String errorMsg = System.Label.generic_error;

```

For more information on custom labels, see “Custom Labels” in Salesforce Help.


Apex Developer Guide Working with Data in Apex

##### Accessing SObject Fields

As in Java, SObject fields can be accessed or changed with simple dot notation. For example:

```
   Account a = new Account();

   a.Name = 'Acme'; // Access the account name field and assign it 'Acme'

```

System-generated fields, such as `Created By` or `Last Modified Date`, cannot be modified. If you try, the Apex runtime
engine generates an error. Additionally, formula field values and values for other fields that are read-only for the context user cannot be
changed.

If you use the generic SObject type instead of a specific object, such as Account, you can retrieve only the `Id` field using dot notation.
You can set the `Id` field for Apex code saved using Salesforce API version 27.0 and later). Alternatively, you can use the generic SObject
`put` and `get` [methods. See SObject Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject.htm)

This example shows how you can access the `Id` field and operations that aren’t allowed on generic SObjects.

```
   Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');

   insert a;

   sObject s = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];

   // This is allowed

   ID id = s.Id;

   // The following line results in an error when you try to save

   String x = s.Name;

   // This line results in an error when you try to save using API version 26.0 or earlier

   s.Id = [SELECT Id FROM Account WHERE Name = 'Acme' LIMIT 1].Id;

```

Note: If your organization has enabled person accounts, you have two different kinds of accounts: business accounts and person
accounts. If your code creates a new account using `name`, a business account is created. If your code uses `LastName`, a person
account is created.

If you want to perform operations on an SObject, it is recommended that you first convert it into a specific object. For example:

```
   Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');

   insert a;

   sObject s = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];

   ID id = s.ID;

   Account convertedAccount = (Account)s;

   convertedAccount.name = 'Acme2';

   update convertedAccount;

   Contact sal = new Contact(FirstName = 'Sal', Account = convertedAccount);

```

The following example shows how you can use SOSL over a set of records to determine their object types. Once you have converted
the generic SObject record into a Contact, Lead, or Account, you can modify its fields accordingly:

```
   public class convertToCLA {

      List<Contact> contacts = new List<Contact>();

      List<Lead> leads = new List<Lead>();

      List<Account> accounts = new List<Account>();

      public void convertType(String phoneNumber) {

        List<List<SObject>> results = [FIND :phoneNumber

           IN Phone FIELDS

           RETURNING Contact(Id, Phone, FirstName, LastName),

           Lead(Id, Phone, FirstName, LastName),

           Account(Id, Phone, Name)];

        List<SObject> records = new List<SObject>();

```


Apex Developer Guide Working with Data in Apex

```
        records.addAll(results[0]); //add Contact results to our results super-set

        records.addAll(results[1]); //add Lead results

        records.addAll(results[2]); //add Account results

        if (!records.isEmpty()) {

           for (Integer i = 0; i < records.size(); i++) {

             SObject record = records[i];

             if (record.getSObjectType() == Contact.sObjectType) {

               contacts.add((Contact) record);

             } else if (record.getSObjectType() == Lead.sObjectType){

               leads.add((Lead) record);

             } else if (record.getSObjectType() == Account.sObjectType) {

               accounts.add((Account) record);

             }

           }

        }

      }

   }

```

Using SObject Fields

SObject fields can be initially set or not set (unset); unset fields are not the same as null or blank fields. When you perform a DML operation
on an SObject, you can change a field that is set; you can’t change unset fields.

Note: To erase the current value of a field, set the field to null.

[If an Apex method takes an SObject parameter, you can use the System.isSet() method to identify the set fields. If you want to unset any](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_sobject.htm#apex_System_SObject_isSet)
fields to retain their values, first create an SObject instance. Then apply only the fields you want to be part of the DML operation.

This example code shows how SObject fields are identified as set or unset.

```
   Contact nullFirst = new Contact(LastName='Codey', FirstName=null);

   System.assertEquals(true, nullFirst.isSet('FirstName'), 'FirstName is set to a literal

   value, so it counts as set');

   Contact unsetFirst = new Contact(LastName='Astro');

   System.assertEquals(false, unsetFirst.isSet('FirstName'), ‘FirstName is not set’);

```

An expression with SObject fields of type Boolean evaluates to true only if the SObject field is true. If the field is false or null, the expression
evaluates to false. This example code shows an expression that checks if the `IsActive` field of a Campaign object is null. Because
this expression always evaluates to false, the code in the `if` statement is never executed.

```
   Campaign cObj= new Campaign();

   ...

     if (cObj.IsActive == null) {

     ... // IsActive is evaluated to false and this code block is not executed.

     }

##### Validating sObjects and Fields

```

When Apex code is parsed and validated, all sObject and field references are validated against actual object and field names, and a
parse-time exception is thrown when an invalid name is used.

In addition, the Apex parser tracks the custom objects and fields that are used, both in the code's syntax as well as in embedded SOQL
and SOSL statements. The platform prevents users from making the following types of modifications when those changes cause Apex
code to become invalid:


Apex Developer Guide Working with Data in Apex

**•** Changing a field or object name

**•** Converting from one data type to another

**•** Deleting a field or object

**•** Making certain organization-wide changes, such as record sharing, field history tracking, or record types

#### Data Manipulation Language

Apex enables you to insert, update, delete or restore data in the database. DML operations allow you to modify records one at a time or
in batches.

##### How DML Works

Adding and Retrieving Data With DML
Apex is tightly integrated with the Lightning Platform persistence layer. Records in the database can be inserted and manipulated
through Apex directly using simple statements. The language in Apex that allows you to add and manage records in the database
is the Data Manipulation Language (DML). In contrast to the SOQL language, which is used for read operations (querying records),
DML is used for write operations.

DML Statements vs. Database Class Methods
Apex offers two ways to perform DML operations: using DML statements or Database class methods. This provides flexibility in how
you perform data operations. DML statements are more straightforward to use and result in exceptions that you can handle in your
code.

DML Operations As Atomic Transactions

DML Operations
Using DML, you can insert new records and commit them to the database. You can also update the field values of existing records.

Exception Handling

More About DML
Here are some things you may want to know about using Data Manipulation Language.

Locking Records
When an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user
interface. The client locking the records can perform logic on the records and make updates with the guarantee that the locked
records won’t be changed by another client during the lock period.

##### How DML Works

Single vs. Bulk DML Operations

You can perform DML operations either on a single sObject, or in bulk on a list of sObjects. Performing bulk DML operations is the
recommended way because it helps avoid hitting governor limits, such as the DML limit of 150 statements per Apex transaction. This
limit is in place to ensure fair access to shared resources in the Lightning Platform. Performing a DML operation on a list of sObjects
counts as one DML statement, not as one statement for each sObject.

This example performs DML calls on single sObjects, which isn’t efficient.


Apex Developer Guide Working with Data in Apex

The `for` loop iterates over contacts. For each contact, if the department field matches a certain value, it sets a new value for the
Description field. If the list contains more than items, the 151st update returns an exception that can't be caught.

```
   List<Contact> conList = [Select Department, Description from Contact];

   for(Contact badCon : conList) {

      if (badCon.Department == 'Finance') {

        badCon.Description = 'New description';

      }

      // Not a good practice since governor limits might be hit.

      update badCon;

   }

```

This example is a modified version of the previous example that doesn't hit the governor limit. The DML operation is performed in bulk
by calling `update` on a list of contacts. This code counts as one DML statement, which is far below the limit of 150.

```
   // List to hold the new contacts to update.

   List<Contact> updatedList = new List<Contact>();

   List<Contact> conList = [Select Department, Description from Contact];

   for(Contact con : conList) {

      if (con.Department == 'Finance') {

        con.Description = 'New description';

        // Add updated contact sObject to the list.

        updatedList.add(con);

      }

   }

   // Call update on the list of contacts.

   // This results in one DML call for the entire list.

   update updatedList;

```

Another DML governor limit is the total number of rows that can be processed by DML operations in a single transaction, which is 10,000.
All rows processed by all DML calls in the same transaction count incrementally toward this limit. For example, if you insert 100 contacts
and update 50 contacts in the same transaction, your total DML processed rows are 150. You still have 9,850 rows left (10,000 - 150).

System Context and Sharing Rules

Most DML operations execute in user context, which means that the current user's permissions, field-level security, organization-wide
defaults, position in the role hierarchy, and sharing rules are enforced. See Apex Security and Sharing Model.

Best Practices

With DML on SObjects, it’s best to construct new instances and only update the fields you wish to modify without querying other fields.
If you query fields other than the fields you wish to update, you may revert queried field values that could have changed between the
query and the DML.

##### Adding and Retrieving Data With DML

Apex is tightly integrated with the Lightning Platform persistence layer. Records in the database can be inserted and manipulated
through Apex directly using simple statements. The language in Apex that allows you to add and manage records in the database is the
Data Manipulation Language (DML). In contrast to the SOQL language, which is used for read operations (querying records), DML is used
for write operations.

Before inserting or manipulating records, record data is created in memory as sObjects. The sObject data type is a generic data type and
corresponds to the data type of the variable that will hold the record data. There are specific data types, subtyped from the sObject data


Apex Developer Guide Working with Data in Apex

type, which correspond to data types of standard object records, such as Account or Contact, and custom objects, such as
Invoice_Statement__c. Typically, you will work with these specific sObject data types. But sometimes, when you don’t know the type
of the sObject in advance, you can work with the generic sObject data type. This is an example of how you can create a new specific
Account sObject and assign it to a variable.

```
   Account a = new Account(Name='Account Example');

```

In the previous example, the account referenced by the variable `a` exists in memory with the required `Name` field. However, it is not
persisted yet to the Lightning Platform persistence layer. You need to call DML statements to persist sObjects to the database. Here is
an example of creating and persisting this account using the `insert` statement.

```
   Account a = new Account(Name='Account Example');

   insert a;

```

Also, you can use DML to modify records that have already been inserted. Among the operations you can perform are record updates,
deletions, restoring records from the Recycle Bin, merging records, or converting leads. After querying for records, you get sObject
instances that you can modify and then persist the changes of. This is an example of querying for an existing record that has been
previously persisted, updating a couple of fields on the sObject representation of this record in memory, and then persisting this change
to the database.

```
   // Query existing account.

   Account a = [SELECT Name,Industry

            FROM Account

            WHERE Name='Account Example' LIMIT 1];

   // Write the old values the debug log before updating them.

   System.debug('Account Name before update: ' + a.Name); // Name is Account Example

   System.debug('Account Industry before update: ' + a.Industry);// Industry is not set

   // Modify the two fields on the sObject.

   a.Name = 'Account of the Day';

   a.Industry = 'Technology';

   // Persist the changes.

   update a;

   // Get a new copy of the account from the database with the two fields.

   Account a = [SELECT Name,Industry

           FROM Account

           WHERE Name='Account of the Day' LIMIT 1];

   // Verify that updated field values were persisted.

   System.assertEquals('Account of the Day', a.Name);

   System.assertEquals('Technology', a.Industry);

##### DML Statements vs. Database Class Methods

```

Apex offers two ways to perform DML operations: using DML statements or Database class methods. This provides flexibility in how you
perform data operations. DML statements are more straightforward to use and result in exceptions that you can handle in your code.

This is an example of a DML statement to insert a new record.

```
   // Create the list of sObjects to insert

   List<Account> acctList = new List<Account>();

   acctList.add(new Account(Name='Acme1'));

```


Apex Developer Guide Working with Data in Apex

```
   acctList.add(new Account(Name='Acme2'));

   // DML statement

   insert acctList;

```

This is an equivalent example to the previous one but it uses a method of the Database class instead of the DML verb.

```
   // Create the list of sObjects to insert

   List<Account> acctList = new List<Account>();

   acctList.add(new Account(Name='Acme1'));

   acctList.add(new Account(Name='Acme2'));

   // DML statement

   Database.SaveResult[] srList = Database.insert(acctList, false);

   // Iterate through each returned result

   for (Database.SaveResult sr : srList) {

      if (sr.isSuccess()) {

        // Operation was successful, so get the ID of the record that was processed

        System.debug('Successfully inserted account. Account ID: ' + sr.getId());

      }

      else {

        // Operation failed, so get all errors

        for(Database.Error err : sr.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Account fields that affected this error: ' + err.getFields());

        }

      }

   }

```

One difference between the two options is that by using the Database class method, you can specify whether or not to allow for partial
record processing if errors are encountered. You can do so by passing an additional second Boolean parameter. If you specify `false`
for this parameter and if a record fails, the remainder of DML operations can still succeed. Also, instead of exceptions, a result object
array (or one result object if only one sObject was passed in) is returned containing the status of each operation and any errors encountered.
By default, this optional parameter is `true`, which means that if at least one sObject can’t be processed, all remaining sObjects won’t
and an exception will be thrown for the record that causes a failure.

The following helps you decide when you want to use DML statements or Database class methods.

**•** Use DML statements if you want any error that occurs during bulk DML processing to be thrown as an Apex exception that immediately
interrupts control flow (by using `try. . .catch` blocks). This behavior is similar to the way exceptions are handled in most
database procedural languages.

**•** Use Database class methods if you want to allow partial success of a bulk DML operation—if a record fails, the remainder of the DML
operation can still succeed. Your application can then inspect the rejected records and possibly retry the operation. When using this
form, you can write code that never throws DML exception errors. Instead, your code can use the appropriate results array to judge
success or failure. Note that Database methods also include a syntax that supports thrown exceptions, similar to DML statements.

Note: Most operations overlap between the two, except for a few.

**•** The `convertLead` operation is only available as a Database class method, not as a DML statement.


Apex Developer Guide Working with Data in Apex

**•** The Database class also provides methods not available as DML statements, such as methods transaction control and rollback,
emptying the Recycle Bin, and methods related to SOQL queries.

SEE ALSO:

_Apex Reference Guide_ [: Database Class Methods](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm)

##### DML Operations As Atomic Transactions

DML operations execute within a transaction. All DML operations in a transaction either complete successfully, or if an error occurs in
one operation, the entire transaction is rolled back and no data is committed to the database. The boundary of a transaction can be a
trigger, a class method, an anonymous block of code, an Apex page, or a custom Web service method.

All operations that occur inside the transaction boundary represent a single unit of operations. This also applies to calls that are made
from the transaction boundary to external code, such as classes or triggers that get fired as a result of the code running in the transaction
boundary. For example, consider the following chain of operations: a custom Apex Web service method calls a method in a class that
performs some DML operations. In this case, all changes are committed to the database only after all operations in the transaction finish
executing and don’t cause any errors. If an error occurs in any of the intermediate steps, all database changes are rolled back and the
transaction isn’t committed.

##### DML Operations

Using DML, you can insert new records and commit them to the database. You can also update the field values of existing records.

###### Inserting and Updating Records

Using DML, you can insert new records and commit them to the database. Similarly, you can update the field values of existing
records.

Upserting Records

Merging Records
When you have duplicate lead, contact, case, or account records in the database, cleaning up your data and consolidating the records
is a good idea. You can merge up to three records of the same sObject type. The `merge` operation merges the duplicate records
into the main record, deletes the duplicate records, and reparents any related records.

Deleting Records

Restoring Deleted Records

Converting Leads

###### Inserting and Updating Records

Using DML, you can insert new records and commit them to the database. Similarly, you can update the field values of existing records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This example inserts three account records and updates an existing account record. First, three Account sObjects are created and added
to a list. An insert statement bulk inserts the list of accounts as an argument. Then, the second account record is updated, the billing city
is updated, and the update statement is called to persist the change in the database.

```
   Account[] accts = new List<Account>();

   for(Integer i=0;i<3;i++) {

```


Apex Developer Guide Working with Data in Apex

```
      Account a = new Account(Name='Acme' + i,

                    BillingCity='San Francisco');

      accts.add(a);

   }

   Account accountToUpdate;

   try {

      insert accts;

      // Update account Acme2.

      accountToUpdate =

        [SELECT BillingCity FROM Account

         WHERE Name='Acme2' AND BillingCity='San Francisco'

         LIMIT 1];

      // Update the billing city.

      accountToUpdate.BillingCity = 'New York';

      // Make the update call.

      update accountToUpdate;

   } catch(DmlException e) {

      System.debug('An unexpected error has occurred: ' + e.getMessage());

   }

   // Verify that the billing city was updated to New York.

   Account afterUpdate =

      [SELECT BillingCity FROM Account WHERE Id=:accountToUpdate.Id];

   System.assertEquals('New York', afterUpdate.BillingCity);

```

Inserting Related Records

You can insert records related to existing records if a relationship has already been defined between the two objects, such as a lookup
or master-detail relationship. A record is associated with a related record through a foreign key ID. For example, when inserting a new
contact, you can specify the contact’s related account record by setting the value of the `AccountId` field.

This example adds a contact to an account (the related record) by setting the `AccountId` field on the contact. Contact and Account
are linked through a lookup relationship.

```
   try {

      Account acct = new Account(Name='SFDC Account');

      insert acct;

      // Once the account is inserted, the sObject will be

      // populated with an ID.

      // Get this ID.

      ID acctID = acct.ID;

      // Add a contact to this account.

      Contact con = new Contact(

        FirstName='Joe',

        LastName='Smith',

        Phone='415.555.1212',

        AccountId=acctID);

      insert con;

   } catch(DmlException e) {

      System.debug('An unexpected error has occurred: ' + e.getMessage());

   }

```


Apex Developer Guide Working with Data in Apex

Updating Related Records

Fields on related records can't be updated with the same call to the DML operation and require a separate DML call. For example, if
inserting a new contact, you can specify the contact's related account record by setting the value of the `AccountId` field. However,
you can't change the account's name without updating the account itself with a separate DML call. Similarly, when updating a contact,
if you also want to update the contact’s related account, you must make two DML calls. The following example updates a contact and
its related account using two `update` statements.

```
   try {

      // Query for the contact, which has been associated with an account.

      Contact queriedContact = [SELECT Account.Name

                     FROM Contact

                     WHERE FirstName = 'Joe' AND LastName='Smith'

                     LIMIT 1];

      // Update the contact's phone number

      queriedContact.Phone = '415.555.1213';

      // Update the related account industry

      queriedContact.Account.Industry = 'Technology';

      // Make two separate calls

      // 1. This call is to update the contact's phone.

      update queriedContact;

      // 2. This call is to update the related account's Industry field.

      update queriedContact.Account;

   } catch(Exception e) {

      System.debug('An unexpected error has occurred: ' + e.getMessage());

   }

####### Relating Records by Using an External ID
```

Add related records by using a custom external ID field on the parent record. Associating records through the external ID field is an
alternative to using the record ID. You can add a related record to another record only if a relationship (such as master-detail or
lookup) has been defined for the objects involved.

Creating Parent and Child Records in a Single Statement Using Foreign Keys

####### Relating Records by Using an External ID

Add related records by using a custom external ID field on the parent record. Associating records through the external ID field is an
alternative to using the record ID. You can add a related record to another record only if a relationship (such as master-detail or lookup)
has been defined for the objects involved.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This example relates a new opportunity to an existing account. The Account sObject has a custom field marked as External ID. An
opportunity record is associated to the account record through the custom External ID field. The example assumes that:

**•** The Account sObject has an external ID field of type text and named `MyExtID`

**•** An account record exists where `MyExtID__c = ‘SAP111111’`


Apex Developer Guide Working with Data in Apex

Before the new opportunity is inserted, the account record is added to this opportunity as an sObject through the
`Opportunity.Account` relationship field.

```
   Opportunity newOpportunity = new Opportunity(

      Name='OpportunityWithAccountInsert',

      StageName='Prospecting',

      CloseDate=Date.today().addDays(7));

   // Create the parent record reference.

   // An account with external ID = 'SAP111111' already exists.

   // This sObject is used only for foreign key reference

   // and doesn't contain any other fields.

   Account accountReference = new Account(

      MyExtID__c='SAP111111');

   // Add the account sObject to the opportunity.

   newOpportunity.Account = accountReference;

   // Create the opportunity.

   Database.SaveResult results = Database.insert(newOpportunity);

```

The previous example performs an insert operation, but you can also relate sObjects through external ID fields when performing updates
or upserts. If the parent record doesn’t exist, you can create it with a separate DML statement or by using the same DML statement as
shown in Creating Parent and Child Records in a Single Statement Using Foreign Keys.

####### Creating Parent and Child Records in a Single Statement Using Foreign Keys

You can use external ID fields as foreign keys to create parent and child records of different sObject types in a single step instead of
creating the parent record first, querying its ID, and then creating the child record. To do this:

**•** Create the child sObject and populate its required fields, and optionally other fields.

**•** Create the parent reference sObject used only for setting the parent foreign key reference on the child sObject. This sObject has only
the external ID field defined and no other fields set.

**•** Set the foreign key field of the child sObject to the parent reference sObject you just created.

**•** Create another parent sObject to be passed to the `insert` statement. This sObject must have the required fields (and optionally
other fields) set in addition to the external ID field.

**•** Call `insert` by passing it an array of sObjects to create. The parent sObject must precede the child sObject in the array, that is,
the array index of the parent must be lower than the child’s index.

You can create related records that are up to 10 levels deep. Also, the related records created in a single call must have different sObject
[types. For more information, see Creating Records for Different Object Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_create.htm#MixedSaveSection) _SOAP API Developer Guide_ .

The following example shows how to create an opportunity with a parent account using the same `insert` statement. The example
creates an Opportunity sObject and populates some of its fields, then creates two Account objects. The first account is only for the foreign
key relationship, and the second is for the account creation and has the account fields set. Both accounts have the external ID field,
`MyExtID__c`, set. Next, the sample calls `Database.insert` by passing it an array of sObjects. The first element in the array is
the parent sObject and the second is the opportunity sObject. The `Database.insert` statement creates the opportunity with its
parent account in a single step. Finally, the sample checks the results and writes the IDs of the created records to the debug log, or the
first error if record creation fails. This sample requires an external ID text field on Account called MyExtID.

```
   public class ParentChildSample {

      public static void InsertParentChild() {

        Date dt = Date.today();

```


Apex Developer Guide Working with Data in Apex

```
        dt = dt.addDays(7);

        Opportunity newOpportunity = new Opportunity(

           Name='OpportunityWithAccountInsert',

           StageName='Prospecting',

           CloseDate=dt);

        // Create the parent reference.

        // Used only for foreign key reference

        // and doesn't contain any other fields.

        Account accountReference = new Account(

           MyExtID__c='SAP111111');

        newOpportunity.Account = accountReference;

        // Create the Account object to insert.

        // Same as above but has Name field.

        // Used for the insert.

        Account parentAccount = new Account(

           Name='Hallie',

           MyExtID__c='SAP111111');

        // Create the account and the opportunity.

        Database.SaveResult[] results = Database.insert(new SObject[] {

           parentAccount, newOpportunity });

        // Check results.

        for (Integer i = 0; i < results.size(); i++) {

           if (results[i].isSuccess()) {

           System.debug('Successfully created ID: '

              + results[i].getId());

           } else {

           System.debug('Error: could not create sobject '

              + 'for array element ' + i + '.');

           System.debug(' The error reported was: '

              + results[i].getErrors()[0].getMessage() + '\n');

           }

        }

      }

   }

###### Upserting Records

```

Using the `upsert` operation, you can either insert or update an existing record in one call. To determine whether a record already
exists, the `upsert` statement or Database method uses the record’s ID as the key to match records, a custom external ID field, or a
standard field with the `idLookup` attribute set to true.

**•** If the key isn’t matched, then a new object record is created.

**•** If the key is matched once, then the existing object record is updated.

**•** If the key is matched multiple times, then an error is generated and the object record is not inserted or updated.

Note: Custom field matching is case-insensitive only if the custom field has the **Unique** and **Treat "ABC" and "abc" as duplicate**
**values (case insensitive)** attributes selected as part of the field definition. If this is the case, “ABC123” is matched with “abc123.”


Apex Developer Guide Working with Data in Apex

Examples

The following example updates the city name for all existing accounts in the city formerly known as Bombay, and also inserts a new
account in San Francisco:

```
   Account[] acctsList = [SELECT Id, Name, BillingCity

                  FROM Account WHERE BillingCity = 'Bombay'];

   for (Account a : acctsList) {

      a.BillingCity = 'Mumbai';

   }

   Account newAcct = new Account(Name = 'Acme', BillingCity = 'San Francisco');

   acctsList.add(newAcct);

   try {

      upsert acctsList;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

This next example uses the `Database.upsert` method to upsert a collection of leads that are passed in. This example allows for
partial processing of records, that is, in case some records fail processing, the remaining records are still inserted or updated. It iterates
through the results and adds a task to each record that was processed successfully. The task sObjects are saved in a list, which is then
bulk inserted. This example is followed by a test class that contains a test method for testing the example.

```
   /* This class demonstrates and tests the use of the

    * partial processing DML operations */

   public class DmlSamples {

     /* This method accepts a collection of lead records and

       creates a task for the owner(s) of any leads that were

       created as new, that is, not updated as a result of the upsert

       operation */

     public static List<Database.upsertResult> upsertLeads(List<Lead> leads) {

       /* Perform the upsert. In this case the unique identifier for the

         insert or update decision is the Salesforce record ID. If the

         record ID is null the row will be inserted, otherwise an update

         will be attempted. */

       List<Database.upsertResult> uResults = Database.upsert(leads,false);

       /* This is the list for new tasks that will be inserted when new

         leads are created. */

       List<Task> tasks = new List<Task>();

       for(Database.upsertResult result:uResults) {

         if (result.isSuccess() && result.isCreated())

            tasks.add(new Task(Subject = 'Follow-up', WhoId = result.getId()));

       }

       /* If there are tasks to be inserted, insert them */

       Database.insert(tasks);

       return uResults;

```


Apex Developer Guide Working with Data in Apex

```
     }

   }

   @isTest

   private class DmlSamplesTest {

     public static testMethod void testUpsertLeads() {

        /* We only need to test the insert side of upsert */

       List<Lead> leads = new List<Lead>();

       /* Create a set of leads for testing */

       for(Integer i = 0;i < 100; i++) {

         leads.add(new Lead(LastName = 'testLead', Company = 'testCompany'));

       }

       /* Switch to the runtime limit context */

       Test.startTest();

       /* Exercise the method */

       List<Database.upsertResult> results = DmlSamples.upsertLeads(leads);

       /* Switch back to the test context for limits */

       Test.stopTest();

       /* ID set for asserting the tasks were created as expected */

       Set<Id> ids = new Set<Id>();

       /* Iterate over the results, asserting success and adding the new ID

         to the set for use in the comprehensive assertion phase below. */

       for(Database.upsertResult result:results) {

         System.assert(result.isSuccess());

         ids.add(result.getId());

       }

       /* Assert that exactly one task exists for each lead that was inserted. */

       for(Lead l:[SELECT Id, (SELECT Subject FROM Tasks) FROM Lead WHERE Id IN :ids]) {

         System.assertEquals(1,l.tasks.size());

       }

     }

   }

```

Use of `upsert` with an external ID can reduce the number of DML statements in your code, and help you to avoid hitting governor
limits (see Execution Governors and Limits).

This example uses `upsert` and an external ID field `Line_Item_Id__c` on the Asset object to maintain a one-to-one relationship
between an asset and an opportunity line item. Before running the sample, create a custom text field on the Asset object named
`Line_Item_Id__c` and mark it as an external ID. For information on custom fields, see Salesforce Help.

Note: External ID fields used in upsert calls must be unique or the user must have the View All Data permission.

```
   public void upsertExample() {

      Opportunity opp = [SELECT Id, Name, AccountId,

                     (SELECT Id, PricebookEntry.Product2Id, PricebookEntry.Name

                      FROM OpportunityLineItems)

                 FROM Opportunity

```


Apex Developer Guide Working with Data in Apex

```
                 WHERE HasOpportunityLineItem = true

                 LIMIT 1];

      Asset[] assets = new Asset[]{};

      // Create an asset for each line item on the opportunity

      for (OpportunityLineItem lineItem:opp.OpportunityLineItems) {

        //This code populates the line item Id, AccountId, and Product2Id for each asset

        Asset asset = new Asset(Name = lineItem.PricebookEntry.Name,

                       Line_Item_ID__c = lineItem.Id,

                       AccountId = opp.AccountId,

                       Product2Id = lineItem.PricebookEntry.Product2Id);

        assets.add(asset);

      }

      try {

        upsert assets Line_Item_ID__c; // This line upserts the assets list with

                           // the Line_Item_Id__c field specified as the

                           // Asset field that should be used for matching

                           // the record that should be upserted.

      } catch (DmlException e) {

        System.debug(e.getMessage());

      }

   }

###### Merging Records

```

When you have duplicate lead, contact, case, or account records in the database, cleaning up your data and consolidating the records
is a good idea. You can merge up to three records of the same sObject type. The `merge` operation merges the duplicate records into
the main record, deletes the duplicate records, and reparents any related records.

Use the **`merge`** Statement

This example shows how to merge a duplicate account record into a main account record. The duplicate account has a related contact,
which is moved to the main account record after the `merge` operation. After merging, the duplicate record is deleted and only the
main record remains in the database.

```
   // Insert new accounts

   List<Account> ls = new List<Account>{

      new Account(name='Acme Inc.'),

        new Account(name='Acme')

        };

   insert ls;

   // Queries to get the inserted accounts

   Account mainAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme Inc.' LIMIT 1];

   Account dupAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];

   // Add a contact to the account to be merged

   Contact c = new Contact(FirstName='Joe',LastName='Merged');

   c.AccountId = dupAcct.Id;

```


Apex Developer Guide Working with Data in Apex

```
   insert c;

   try {

      merge mainAcct dupAcct;

   } catch (DmlException e) {

      // Process exception

      System.debug('An unexpected error has occurred: ' + e.getMessage());

   }

   // After the account is merged with the main account,

   // the related contact is moved to the main record.

   mainAcct = [SELECT Id, Name, (SELECT FirstName,LastName From Contacts)

            FROM Account WHERE Name = 'Acme Inc.' LIMIT 1];

   System.assert(mainAcct.getSObjects('Contacts').size() > 0);

   System.assertEquals('Joe', mainAcct.getSObjects('Contacts')[0].get('FirstName'));

   System.assertEquals('Merged', mainAcct.getSObjects('Contacts')[0].get('LastName'));

   // Verify that the duplicate record is deleted

   Account[] result = [SELECT Id, Name FROM Account WHERE Id=:dupAcct.Id];

   System.assertEquals(0, result.size());

```

Use the **`Database.merge`** Method

This second example is similar to the previous example, except that it uses the `Database.merge` method instead of the `merge`
statement. The last argument of `Database.merge` is set to `false`, so any errors encountered in this operation are returned in the
merge result without throwing exceptions. In the example, a main account and two duplicate account records are created. One of the
duplicate account records has a child contact record. Through the merge operation, the contact is moved to the main account record,
and the other records are deleted.

Note: To use the AccountContactRelation sObject in this example, enable the “Allow users to relate a contact to multiple accounts”
[setting in your org. See Set Up Contacts to Multiple Accounts.](https://help.salesforce.com/s/articleView?id=sales.shared_contacts_set_up.htm&type=5&language=en_US)

```
   // Create main account

   Account main = new Account(Name='Account1');

   insert main;

   // Create duplicate accounts

   Account[] duplicates = new Account[]{

      // Duplicate account

      new Account(Name='Account1, Inc.'),

      // Second duplicate account

      new Account(Name='Account 1')

   };

   insert duplicates;

   // Create child contact and associate it with first account

   Contact c = new Contact(firstname='Joe',lastname='Smith', accountId=duplicates[0].Id);

   insert c;

   // Get the account contact relation ID, which is created when a contact is created on

   "Account1, Inc."

   AccountContactRelation resultAcrel = [SELECT Id FROM AccountContactRelation WHERE

```


Apex Developer Guide Working with Data in Apex

```
   ContactId=:c.Id LIMIT 1];

   // Merge duplicate accounts into main account

   Database.MergeResult[] results = Database.merge(main, duplicates, false);

   for(Database.MergeResult res : results) {

      if (res.isSuccess()) {

        // Get the main record ID from the result and validate it

        System.debug('Main record ID: ' + res.getId());

        System.assertEquals(main.Id, res.getId());

        // Get the IDs of the merged records and display them

        List<Id> mergedIds = res.getMergedRecordIds();

        System.debug('IDs of merged records: ' + mergedIds);

        // Get the ID of the reparented record and

        // validate that this the contact ID.

        System.debug('Reparented record ID: ' + res.getUpdatedRelatedIds());

     // Make sure there are two IDs (contact ID and account contact relation ID); the order

   isn't defined

        System.assertEquals(2, res.getUpdatedRelatedIds().size() );

        boolean flag1 = false;

    boolean flag2 = false;

      // Because the order of the IDs isn't defined, the ID can be at index 0 or 1 of the

   array

        if (resultAcrel.id == res.getUpdatedRelatedIds()[0] || resultAcrel.id ==

   res.getUpdatedRelatedIds()[1] )

           flag1 = true;

        if (c.id == res.getUpdatedRelatedIds()[0] || c.id == res.getUpdatedRelatedIds()[1]

    )

           flag2 = true;

        System.assertEquals(flag1, true);

        System.assertEquals(flag2, true);

      }

      else {

        for(Database.Error err : res.getErrors()) {

           // Write each error to the debug output

           System.debug(err.getMessage());

        }

      }

   }

```

Merge Considerations

When merging sObject records, consider these rules and guidelines:

**•** Only leads, contacts, cases, and accounts can be merged. See sObjects That Don’t Support DML Operations on page 165.


Apex Developer Guide Working with Data in Apex

**•** You can pass a main record and up to two additional sObject records to a single `merge` method.

**•** Field values on the main record, including null and empty field values, always supersede the corresponding field values on the
records to be merged. Therefore, if a field value on the main record is empty, the resulting field value remains empty after the `merge`
operation regardless of the field value on the duplicate record. To preserve a field value from a duplicate record, manually set this
field value on the main record before performing the merge.

**•** External ID fields can’t be used with `merge` .

###### Deleting Records

After you persist records in the database, you can delete those records using the `delete` operation. Deleted records aren’t deleted
permanently from Salesforce, but they are placed in the Recycle Bin for 15 days from where they can be restored. Restoring deleted
records is covered in a later section.

Example

The following example deletes all accounts that are named 'DotCom':

```
   Account[] doomedAccts = [SELECT Id, Name FROM Account

                  WHERE Name = 'DotCom'];

   try {

      delete doomedAccts;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

Referential Integrity When Deleting and Restoring Records

The `delete` operation supports cascading deletions. If you delete a parent object, you delete its children automatically, as long as
each child record can be deleted.

For example, if you delete a case record, Apex automatically deletes any CaseComment, CaseHistory, and CaseSolution records associated
with that case. However, if a particular child record is not deletable or is currently being used, then the `delete` operation on the parent
case record fails.

The `undelete` operation restores the record associations for the following types of relationships:

**•** Parent accounts (as specified in the `Parent Account` field on an account)

**•** Indirect account-contact relationships (as specified on the Related Accounts related list on a contact or the Related Contacts related
list on an account)

**•** Parent cases (as specified in the `Parent Case` field on a case)

**•** Master solutions for translated solutions (as specified in the `Master Solution` field on a solution)

**•** Managers of contacts (as specified in the `Reports To` field on a contact)

**•** Products related to assets (as specified in the `Product` field on an asset)

**•** Opportunities related to quotes (as specified in the `Opportunity` field on a quote)

**•** All custom lookup relationships

**•** Relationship group members on accounts and relationship groups, with some exceptions

**•** Tags

**•** An article's categories, publication state, and assignments


Apex Developer Guide Working with Data in Apex

Note: Salesforce only restores lookup relationships that have not been replaced. For example, if an asset is related to a different
product prior to the original product record being undeleted, that asset-product relationship is not restored.

###### Restoring Deleted Records

After you have deleted records, the records are placed in the Recycle Bin for 15 days, after which they are permanently deleted. While
the records are still in the Recycle Bin, you can restore them using the `undelete` operation. If you accidentally deleted some records
that you want to keep, restore them from the Recycle Bin.

Example

The following example undeletes an account named 'Universal Containers'. The `ALL ROWS` keyword queries all rows for both top
level and aggregate relationships, including deleted records and archived activities.

```
   Account a = new Account(Name='Universal Containers');

   insert(a);

   insert(new Contact(LastName='Carter',AccountId=a.Id));

   delete a;

   Account[] savedAccts = [SELECT Id, Name FROM Account WHERE Name = 'Universal Containers'

   ALL ROWS];

   try {

      undelete savedAccts;

   } catch (DmlException e) {

      // Process exception here

   }

```

Note: For more information on processing `DmlException` [s, see Bulk DML Exception Handling.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_bulk_exceptions.htm)

Undelete Considerations

Note the following when using the `undelete` statement.

**•** You can undelete records that were deleted as the result of a merge. However, the merge reparents the child objects, and that
reparenting can’t be undone.

**•** To identify deleted records, including records deleted as a result of a merge, use the `ALL ROWS` parameters with a SOQL query.

**•** See Referential Integrity When Deleting and Restoring Records.

SEE ALSO:

Querying All Records with a SOQL Statement

###### Converting Leads

The `convertLead` DML operation converts a lead into an account and contact, as well as (optionally) an opportunity. `convertLead`
is available only as a method on the `Database` class; it is not available as a DML statement.

Converting leads involves the following basic steps:

**1.** Your application determines the IDs of any lead(s) to be converted.


Apex Developer Guide Working with Data in Apex

**2.** Optionally, your application determines the IDs of any account(s) into which to merge the lead. Your application can use SOQL to
search for accounts that match the lead name, as in the following example:

```
     SELECT Id, Name FROM Account WHERE Name='CompanyNameOfLeadBeingMerged'

```

**3.** Optionally, your application determines the IDs of the contact or contacts into which to merge the lead. The application can use
SOQL to search for contacts that match the lead contact name, as in the following example:

```
     SELECT Id, Name FROM Contact WHERE FirstName='FirstName' AND LastName='LastName' AND

     AccountId = '001...'

```

**4.** Optionally, the application determines whether opportunities should be created from the leads.

**5.** The application uses the query ( `SELECT ... FROM LeadStatus WHERE IsConverted=true` ) to obtain the leads
with converted status.

**6.** The application calls `convertLead` .

**7.** The application iterates through the returned result or results and examines each LeadConvertResult object to determine whether
conversion succeeded for each lead.

**8.** Optionally, when converting leads owned by a queue, the owner must be specified. This is because accounts and contacts can’t be
owned by a queue. Even if you are specifying an existing account or contact, you must still specify an owner.

Example

This example shows how to use the `Database.convertLead` method to convert a lead. It inserts a new lead, creates a
`LeadConvert` object, sets its status to converted, and then passes it to the `Database.convertLead` method. Finally, it verifies
that the conversion was successful.

```
   Lead myLead = new Lead(LastName = 'Fry', Company='Fry And Sons');

   insert myLead;

   Database.LeadConvert lc = new database.LeadConvert();

   lc.setLeadId(myLead.id);

   LeadStatus convertStatus = [SELECT Id, ApiName FROM LeadStatus WHERE IsConverted=true LIMIT

    1];

   lc.setConvertedStatus(convertStatus.ApiName);

   Database.LeadConvertResult lcr = Database.convertLead(lc);

   System.assert(lcr.isSuccess());

```

Convert Leads Considerations

**•** Field mappings: The system automatically maps standard lead fields to standard account, contact, and opportunity fields. For custom
lead fields, your Salesforce administrator can specify how they map to custom account, contact, and opportunity fields. For more
information about field mappings, see Salesforce Help.

**•** Merged fields: If data is merged into existing account and contact objects, only empty fields in the target object are
overwritten—existing data (including IDs) are not overwritten. The only exception is if you specify `setOverwriteLeadSource`
on the LeadConvert object to true, in which case the `LeadSource` field in the target contact object is overwritten with the
contents of the `LeadSource` field in the source LeadConvert object.

**•** Record types: If the organization uses record types, the default record type of the new owner is assigned to records created during
lead conversion. The default record type of the user converting the lead determines the lead source values available during conversion.


Apex Developer Guide Working with Data in Apex

If the desired lead source values are not available, add the values to the default record type of the user converting the lead. For more
information about record types, see Salesforce Help.

**•** Picklist values: The system assigns the default picklist values for the account, contact, and opportunity when mapping any standard
lead picklist fields that are blank. If your organization uses record types, blank values are replaced with the default picklist values of
the new record owner.

**•** Automatic feed subscriptions: When you convert a lead into a new account, contact, and opportunity, the lead owner is unsubscribed
from the lead record’s Chatter feed. The lead owner, the owner of the generated records, and users that were subscribed to the lead
aren’t automatically subscribed to the generated records, unless they have automatic subscriptions enabled in their Chatter feed
settings. They must have automatic subscriptions enabled to see changes to the account, contact, and opportunity records in their
news feed. To subscribe to records they create, users must enable the `Automatically follow records that I`
`create` option in their personal settings. A user can subscribe to a record so that changes to the record display in the news feed
on the user's home page. This is a useful way to stay up-to-date with changes to records in Salesforce.

SEE ALSO:

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm)_ : Database Class

##### Exception Handling

DML statements return run-time exceptions if something went wrong in the database during the execution of the DML operations. You
can handle the exceptions in your code by wrapping your DML statements within try-catch blocks. The following example includes the

`insert` DML statement inside a try-catch block.

```
   Account a = new Account(Name='Acme');

   try {

      insert a;

   } catch(DmlException e) {

      // Process exception here

   }

###### Database Class Method Result Objects

```

Returned Database Errors

###### Database Class Method Result Objects

Database class methods return the results of the data operation. These result objects contain useful information about the data operation
for each record, such as whether the operation was successful or not, and any error information. Each type of operation returns a specific
result object type, as outlined below.

**Operation** **Result Class**

insert, update [SaveResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_saveresult.htm)

upsert [UpsertResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_upsertresult.htm)

merge [MergeResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_database_mergeresult.htm)

delete [DeleteResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_deleteresult.htm)

undelete [UndeleteResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_undeleteresult.htm)

convertLead [LeadConvertResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_database_leadconvertresult.htm)


Apex Developer Guide Working with Data in Apex

**Operation** **Result Class**

emptyRecycleBin [EmptyRecycleBinResult Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_EmptyRecycleBinResult.htm)

###### Returned Database Errors

While DML statements always return exceptions when an operation fails for one of the records being processed and the operation is
rolled back for all records, Database class methods can either do so or allow partial success for record processing. In the latter case of
partial processing, Database class methods don’t throw exceptions. Instead, they return a list of errors for any errors that occurred on
failed records.

The errors provide details about the failures and are contained in the result of the Database class method. For example, a `SaveResult`
object is returned for insert and update operations. Like all returned results, `SaveResult` contains a method called `getErrors`
that returns a list of `Database.Error` objects, representing the errors encountered, if any.

Example

This example shows how to get the errors returned by a `Database.insert` operation. It inserts two accounts, one of which doesn’t
have the required Name field, and sets the second parameter to `false` : `Database.insert(accts, false);` . This sets the
partial processing option. Next, the example checks if the call had any failures through `if (!sr.isSuccess())` and then iterates
through the errors, writing error information to the debug log.

```
   // Create two accounts, one of which is missing a required field

   Account[] accts = new List<Account>{

      new Account(Name='Account1'),

      new Account()};

   Database.SaveResult[] srList = Database.insert(accts, false);

   // Iterate through each returned result

   for (Database.SaveResult sr : srList) {

      if (!sr.isSuccess()) {

        // Operation failed, so get all errors

        for(Database.Error err : sr.getErrors()) {

           System.debug('The following error has occurred.');

           System.debug(err.getStatusCode() + ': ' + err.getMessage());

           System.debug('Fields that affected this error: ' + err.getFields());

        }

      }

   }

##### More About DML

```

Here are some things you may want to know about using Data Manipulation Language.

Setting DML Options
You can specify DML options for insert and update operations by setting the desired options in the `Database.DMLOptions`
object. You can set `Database.DMLOptions` for the operation by calling the `setOptions` method on the sObject, or by
passing it as a parameter to the `Database.insert` and `Database.update` methods.

Transaction Control
Read about transaction requests, generating and releasing savepoints, rolling back transactions, and more.


Apex Developer Guide Working with Data in Apex

sObjects That Can’t Be Used Together in DML Operations
DML operations on certain sObjects, sometimes referred to as setup objects, can’t be mixed with DML on non-setup sObjects in the
same transaction. This restriction exists because some sObjects affect the user’s access to records in the org. You must insert or
update these types of sObjects in a different transaction to prevent operations from happening with incorrect access-level permissions.
For example, you can’t update an account and a user role in a single transaction.

sObjects That Don’t Support DML Operations

Bulk DML Exception Handling

Things You Should Know about Data in Apex

###### Setting DML Options

You can specify DML options for insert and update operations by setting the desired options in the `Database.DMLOptions` object.
You can set `Database.DMLOptions` for the operation by calling the `setOptions` method on the sObject, or by passing it as
a parameter to the `Database.insert` and `Database.update` methods.

Using DML options, you can specify:

**•** The truncation behavior of fields.

**•** Assignment rule information.

**•** Duplicate rule information.

**•** Whether automatic emails are sent.

**•** The user locale for labels.

**•** Whether the operation allows for partial success.

The `Database.DMLOptions` class has the following properties:

**•** `allowFieldTruncation` Property

**•** `assignmentRuleHeader` Property

**•** `duplicateRuleHeader`

**•** `emailHeader` Property

**•** `localeOptions` Property

**•** `optAllOrNone` Property

DMLOptions is only available for Apex saved against API versions 15.0 and higher. DMLOptions settings take effect only for record
operations performed using Apex DML and not through the Salesforce user interface.

**`allowFieldTruncation`** Property

The `allowFieldTruncation` property specifies the truncation behavior of strings. In Apex saved against API versions previous
to 15.0, if you specify a value for a string and that value is too large, the value is truncated. For API version 15.0 and later, if a value is
specified that is too large, the operation fails and an error message is returned. The `allowFieldTruncation` property allows you
to specify that the previous behavior, truncation, be used instead of the new behavior in Apex saved against API versions 15.0 and later.

The `allowFieldTruncation` property takes a Boolean value. If `true`, the property truncates String values that are too long,
which is the behavior in API versions 14.0 and earlier. For example:

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.allowFieldTruncation = true;

```


Apex Developer Guide Working with Data in Apex

**`assignmentRuleHeader`** Property

The `assignmentRuleHeader` property specifies the assignment rule to be used when creating a case or lead.

Note: The Database.DMLOptions object supports assignment rules for cases and leads, but not for accounts.

Using the `assignmentRuleHeader` property, you can set these options:

**•** `assignmentRuleID` : The ID of an assignment rule for the case or lead. The assignment rule can be active or inactive. The ID
can be retrieved by querying the AssignmentRule sObject. If specified, do not specify `useDefaultRule` . If the value is not in
the correct ID format (15-character or 18-character Salesforce ID), the call fails and an exception is returned.

**•** `useDefaultRule` : Indicates whether the default (active) assignment rule will be used for a case or lead. If specified, do not
specify an `assignmentRuleId` .

The following example uses the `useDefaultRule` option:

```
   Database.DMLOptions dmo = new Database.DMLOptions();

   dmo.assignmentRuleHeader.useDefaultRule= true;

   Lead l = new Lead(company='ABC', lastname='Smith');

   l.setOptions(dmo);

   insert l;

```

The following example uses the `assignmentRuleID` option:

```
   Database.DMLOptions dmo = new Database.DMLOptions();

   dmo.assignmentRuleHeader.assignmentRuleId= '01QD0000000EqAn';

   Lead l = new Lead(company='ABC', lastname='Smith');

   l.setOptions(dmo);

   insert l;

```

Note: If there are no assignment rules in the organization, in API version 29.0 and earlier, creating a case or lead with
`useDefaultRule` set to `true` results in the case or lead being assigned to the predefined default owner. In API version 30.0
and later, the case or lead is unassigned and doesn't get assigned to the default owner.

**`duplicateRuleHeader`** Property

The `duplicateRuleHeader` property determines whether a record that’s identified as a duplicate can be saved. Duplicate rules
are part of the Duplicate Management feature.

Using the `duplicateRuleHeader` property, you can set these options.

**•** `allowSave` : Indicates whether a record that’s identified as a duplicate can be saved.

The following example shows how to save an account record that’s been identified as a duplicate. To learn how to iterate through
[duplicate errors, see DuplicateError Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_Database_DuplicateError.htm)

```
   Database.DMLOptions dml = new Database.DMLOptions();

   dml.DuplicateRuleHeader.AllowSave = true;

   Account duplicateAccount = new Account(Name='dupe');

   Database.SaveResult sr = Database.insert(duplicateAccount, dml);

   if (sr.isSuccess()) {

    System.debug('Duplicate account has been inserted in Salesforce!');

   }

```


Apex Developer Guide Working with Data in Apex

**`emailHeader`** Property

Important: System-generated emails from an unverified email-sending domain aren’t delivered, even if the From email address
[is verified. See Requirements to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

The Salesforce user interface allows you to specify whether or not to send an email when the following events occur:

**•** Creation of a new case or task

**•** Conversion of a case email to a contact

**•** New user email notification

**•** Lead queue email notification

**•** Password reset

In API version 15.0 and later, the Database.DMLOptions `emailHeader` property enables you to specify additional information regarding
the email that gets sent when one of the events occurs because of Apex DML code execution.

Using the `emailHeader` property, you can set these options.

**•** `triggerAutoResponseEmail` : Indicates whether to trigger auto-response rules ( `true` ) or not ( `false` ), for leads and cases.
This email can be automatically triggered by a number of events, for example when creating a case or resetting a user password. If
this value is set to `true`, when a case is created, if there is an email address for the contact specified in `ContactID`, the email is
sent to that address. If not, the email is sent to the address specified in `SuppliedEmail` .

**•** `triggerOtherEmail` : Indicates whether to trigger email outside the organization ( `true` ) or not ( `false` ). This email can be
automatically triggered by creating, editing, or deleting a contact for a case.

**•** `triggerUserEmail` : Indicates whether to trigger email that is sent to users in the organization ( `true` ) or not ( `false` ). This
email can be automatically triggered by a number of events; resetting a password, creating a new user, or creating or modifying a
task.

Note: Adding comments to a case in Apex doesn’t trigger email to users in the organization even if `triggerUserEmail`
is set to `true` .

Even though auto-sent emails can be triggered by actions in the Salesforce user interface, the DMLOptions settings for `emailHeader`
take effect only for DML operations carried out in Apex code.

In the following example, the `triggerAutoResponseEmail` option is specified:

```
   Account a = new Account(name='Acme Plumbing');

   insert a;

   Contact c = new Contact(email='jplumber@salesforce.com', firstname='Joe',lastname='Plumber',

    accountid=a.id);

   insert c;

   Database.DMLOptions dlo = new Database.DMLOptions();

   dlo.EmailHeader.triggerAutoResponseEmail = true;

   Case ca = new Case(subject='Plumbing Problems', contactid=c.id);

   database.insert(ca, dlo);

```


Apex Developer Guide Working with Data in Apex

Email sent through Apex because of a group event includes additional behaviors. A _group event_ is an event for which `IsGroupEvent`
is true. The EventAttendee object tracks the users, leads, or contacts that are invited to a group event. Note the following behaviors for
group event email sent through Apex:

**•** Sending a group event invitation to a user respects the `triggerUserEmail` option

**•** Sending a group event invitation to a lead or contact respects the `triggerOtherEmail` option

**•** Email sent when updating or deleting a group event also respects the `triggerUserEmail` and `triggerOtherEmail`
options, as appropriate

**`localeOptions`** Property

The `localeOptions` property specifies the language of any labels that are returned by Apex. The value must be a valid user locale
(language and country), such as de_DE or en_GB. The value is a String, 2-5 characters long. The first two characters are always an ISO
language code, for example 'fr' or 'en.' If the value is further qualified by a country, then the string also has an underscore (_) and another
ISO country code, for example 'US' or 'UK.' For example, the string for the United States is 'en_US', and the string for French Canadian is
'fr_CA'.

**`optAllOrNone`** Property

The `optAllOrNone` property specifies whether the operation allows for partial success. If `optAllOrNone` is set to `true`, all
changes are rolled back if any record causes errors. The default for this property is `false` and successfully processed records are
committed while records with errors aren't. This property is available in Apex saved against Salesforce API version 20.0 and later.

###### Transaction Control

Read about transaction requests, generating and releasing savepoints, rolling back transactions, and more.

All requests are delimited by the trigger, class method, Web Service, Visualforce page, or anonymous block that executes the Apex code.
If the entire request completes successfully, all changes are committed to the database. For example, suppose a Visualforce page called
an Apex controller, which in turn called an additional Apex class. Only when all the Apex code has finished running and the Visualforce
page has finished running, are the changes committed to the database. If the request doesn’t complete successfully, all database changes
are rolled back.

Generating Savepoints and Rolling Back Transactions

Sometimes during the processing of records, your business rules require that partial work (already executed DML statements) is rolled
back so that the processing can continue in another direction. Apex gives you the ability to generate a _savepoint_, that is, a point in the
request that specifies the state of the database at that time. Any DML statement that occurs after the savepoint can be discarded, restoring
the database to the condition it was in when you generated the savepoint. All table and row locks acquired since the savepoint are
released.

The following limitations apply to generating savepoint variables and rolling back the database:

**•** If you set more than one savepoint, then roll back to a savepoint that isn’t the last savepoint you generated, the later savepoint
variable is also rolled back and becomes invalid. For example, if you generated savepoint `SP1` first, savepoint `SP2` after that, and
then you rolled back to `SP1`, the variable `SP2` is no longer valid. If you try to use savepoint `SP2`, you receive a runtime error.

**•** References to savepoints can’t cross-trigger invocations because each trigger invocation is a new trigger context. If you declare a
savepoint as a static variable then try to use it across trigger contexts, you receive a run-time error.

**•** Each savepoint you set counts against the governor limit for DML statements.

**•** Static variables aren’t reverted during a rollback. If you try to run the trigger again, the static variables retain the values from the first
run.


Apex Developer Guide Working with Data in Apex

**•** `Database.rollback(Savepoint)` and `Database.setSavepoint()` don’t count against the DML row limit, but
count toward the DML statement limit. This behavior applies to all API versions.

**•** The ID on an sObject inserted after setting a savepoint isn’t cleared after a rollback. Attempting to insert the sObject using the variable
created before the rollback fails because the sObject variable has an ID. Updating or upserting the sObject using the same variable
also fails because the sObject isn’t in the database and, thus, can’t be updated. To perform further DML operations, create an sObject
variable without setting its ID.

The following is an example using the `setSavepoint` and `rollback` Database methods.

```
   Account a = new Account(Name = 'xyz');

   insert a;

   Assert.isNull([SELECT AccountNumber FROM Account WHERE Id = :a.Id]. AccountNumber);

   // Create a savepoint while AccountNumber is null

   Savepoint sp = Database.setSavepoint();

   // Change the account number

   a.AccountNumber = '123';

   update a;

   Assert.areEqual('123', [SELECT AccountNumber FROM Account WHERE Id = :a.Id].

   AccountNumber);

   // Rollback to the previous null value

   Database.rollback(sp);

   Assert.isNull([SELECT AccountNumber FROM Account WHERE Id = :a.Id]. AccountNumber);

```

Releasing Savepoints and Using Callouts

To allow callouts, roll back all uncommitted DML by using a savepoint. Then use the `Database.releaseSavepoint` method
to explicitly release savepoints before making the desired callout. When `Database.releaseSavepoint()` is called,
`SAVEPOINT_RELEASE` is logged.

See `[releaseSavepoint()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_releaseSavepoint)` for more information.

In this example, the `makeACallout()` callout succeeds because the uncommitted DML is rolled back and the savepoint is released.

```
   Savepoint sp = Database.setSavepoint();

   try {

     // Try a database operation

     insert new Account(name='Foo');

     integer bang = 1 / 0;

   } catch (Exception ex) {

     Database.rollback(sp);

     Database.releaseSavepoint(sp);

     makeACallout();

   }

```

In this example, the savepoint isn’t released before making the callout. The `CalloutException` informs you that you must release
all active savepoints before making the callout.

```
   Savepoint sp = Database.setSavepoint();

   try {

     makeACallout();

   } catch (System.CalloutException ex) {

     Assert.isTrue(ex.getMessage().contains('All active Savepoints must be released before

   making callouts.'));

   }

```


Apex Developer Guide Working with Data in Apex

In this example, DML is pending when the callout is made. The `CalloutException` informs you that you must roll back the
transaction before the callout is made or the transaction must be committed.

```
   Savepoint sp = Database.setSavepoint();

   insert new Account(name='Foo');

   Database.releaseSavepoint(sp);

   try {

     makeACallout();

   } catch (System.CalloutException ex) {

     Assert.isTrue(ex.getMessage().contains('You have uncommitted work pending. Please commit

    or rollback before calling out.'));

   }

```

Use these guidelines for using callouts and savepoints.

**•** If there’s uncommitted work pending when `Database.releaseSavepoint()` is called, the uncommitted work isn’t rolled
back. It’s committed if the transaction succeeds.

**•** Attempts to roll back to a released savepoint result in a `TypeException` .

**•** Attempts to roll back after calling `Database.releaseSavepoint()` result in a
`System.InvalidOperationException` .

**•** Calling the `Database.releaseSavepoint()` method on a savepoint also releases nested savepoints, that is, any subsequent
savepoints created after a savepoint.

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(databaseSavepoint)` and `Database.setSavepoint()` calls incremented the DML row
usage limit.

###### sObjects That Can’t Be Used Together in DML Operations

DML operations on certain sObjects, sometimes referred to as setup objects, can’t be mixed with DML on non-setup sObjects in the
same transaction. This restriction exists because some sObjects affect the user’s access to records in the org. You must insert or update
these types of sObjects in a different transaction to prevent operations from happening with incorrect access-level permissions. For
example, you can’t update an account and a user role in a single transaction.

Don’t include more than one of these sObjects in the same transaction when performing DML operations or when using the Metadata
API.

These sObjects also can't be used with the @IsTest (IsParallel=true) annotation. Split such operations into separate transactions.

Note: This list includes sObjects that cannot be used together in the same DML transaction, but is not an exhaustive list.

**•** AuthSession

**•** ContentWorkspace

**•** FieldPermissions

**•** ForecastingShare

**•** Group

You can only insert and update a group in a transaction with other sObjects. Other DML operations aren’t allowed.


Apex Developer Guide Working with Data in Apex

**•** GroupMember

Note: With legacy Apex code saved using Salesforce API version 14.0 and earlier, you can insert and update a group member
with other sObjects in the same transaction.

**•** ObjectPermissions

**•** ObjectTerritory2AssignmentRule

**•** ObjectTerritory2AssignmentRuleItem

**•** PermissionSet

**•** PermissionSetAssignment

**•** QueueSObject

**•** RuleTerritory2Association

**•** SetupEntityAccess

**•** Territory

**•** Territory2

**•** Territory2Model

**•** User

You can insert a user in a transaction with other sObjects in Apex code saved using Salesforce API version 14.0 and earlier.

You can insert a user in a transaction with other sObjects in Apex code saved using Salesforce API version 15.0 and later when
`UserRoleId` is specified as null.

You can update a user in a transaction with other sObjects in Apex code saved using Salesforce API version 14.0 and earlier

You can update a user in a transaction with other sObjects in Apex code saved using Salesforce API version 15.0 and later when the
[user isn’t included in a Lightning Sync or Einstein Activity Capture configuration (either active or inactive) and the following fields](https://help.salesforce.com/articleView?id=lightning_sync_admin_overview.htm&language=en_US)
aren’t updated:

**–** `UserRoleId`

**–** `IsActive`

**–** `ForecastEnabled`

**–** `IsPortalEnabled`

**–** `Username`

**–** `ProfileId`

**•** UserPackageLicense

**•** UserRole

**•** UserTerritory

**•** UserTerritory2Association

If you're using a Visualforce page with a custom controller, you can't mix sObject types with any of these special sObjects within a single
request or action. However, you can perform DML operations on these different types of sObjects in subsequent requests. For example,
you can create an account with a save button, and then create a user with a non-null role with a submit button.

You can perform DML operations on more than one type of sObject in a single class using the following process:

**1.** Create a method that performs a DML operation on one type of sObject.

**2.** Create a second method that uses the `future` annotation to manipulate a second sObject type.

This process is demonstrated in the example in the next section.


Apex Developer Guide Working with Data in Apex

Example: Using a Future Method to Perform Mixed DML Operations

This example shows how to perform mixed DML operations by using a future method to perform a DML operation on the User object.

```
   public class MixedDMLFuture {

      public static void useFutureMethod() {

        // First DML operation

        Account a = new Account(Name='Acme');

        insert a;

        // This next operation (insert a user with a role)

        // can't be mixed with the previous insert unless

        // it is within a future method.

        // Call future method to insert a user with a role.

        Util.insertUserWithRole(

           'mruiz@awcomputing.com', 'mruiz',

           'mruiz@awcomputing.com', 'Ruiz');

      }

   }

   public class Util {

      @future

      public static void insertUserWithRole(

        String uname, String al, String em, String lname) {

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

        UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];

        // Create new user with a non-null user role ID

        User u = new User(alias = al, email=em,

           emailencodingkey='UTF-8', lastname=lname,

           languagelocalekey='en_US',

           localesidkey='en_US', profileid = p.Id, userroleid = r.Id,

           timezonesidkey='America/Los_Angeles',

           username=uname);

        insert u;

      }

   }

####### Mixed DML Operations in Test Methods
```

Test methods allow for performing mixed Data Manipulation Language (DML) operations that include both setup sObjects and
other sObjects if the code that performs the DML operations is enclosed within `System.runAs` method blocks. You can also
perform DML in an asynchronous job that your test method calls. These techniques enable you, for example, to create a user with
a role and other sObjects in the same test.

####### Mixed DML Operations in Test Methods

Test methods allow for performing mixed Data Manipulation Language (DML) operations that include both setup sObjects and other
sObjects if the code that performs the DML operations is enclosed within `System.runAs` method blocks. You can also perform DML
in an asynchronous job that your test method calls. These techniques enable you, for example, to create a user with a role and other
sObjects in the same test.

The setup sObjects are listed in sObjects That Cannot Be Used Together in DML Operations.


Apex Developer Guide Working with Data in Apex

Note: Because validation for mixed DML operations is skipped during deployment, there can be a difference in the number of
test failures when tests are deployed versus when run in the user interface.

**Example: Mixed DML Operations in** **`System.runAs`** **Blocks**

This example shows how to enclose mixed DML operations within `System.runAs` blocks to avoid the mixed DML error. The
`System.runAs` block runs in the current user’s context. It creates a test user with a role and a test account, which is a mixed DML
operation.

```
   @isTest

   private class MixedDML {

      static testMethod void mixedDMLExample() {

        User u;

        Account a;

        User thisUser = [SELECT Id FROM User WHERE Id = :UserInfo.getUserId()];

        // Insert account as current user

        System.runAs (thisUser) {

           Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

           UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];

           u = new User(alias = 'jsmith', email='jsmith@acme.com',

             emailencodingkey='UTF-8', lastname='Smith',

             languagelocalekey='en_US',

             localesidkey='en_US', profileid = p.Id, userroleid = r.Id,

             timezonesidkey='America/Los_Angeles',

             username='jsmith@acme.com');

           insert u;

           a = new Account(name='Acme');

           insert a;

        }

      }

   }

```

**Use** **`@future`** **to Bypass the Mixed DML Error in a Test Method**

Mixed DML operations within a single transaction aren’t allowed. You can’t perform DML on a setup sObject and another sObject in the
same transaction. However, you can perform one type of DML as part of an asynchronous job and the others in other asynchronous jobs
or in the original transaction. This class contains an `@future` method to be called by the class in the subsequent example.

```
   public class InsertFutureUser {

      @future

      public static void insertUser() {

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

        UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];

        User futureUser = new User(firstname = 'Future', lastname = 'User',

           alias = 'future', defaultgroupnotificationfrequency = 'N',

           digestfrequency = 'N', email = 'test@test.org',

           emailencodingkey = 'UTF-8', languagelocalekey='en_US',

           localesidkey='en_US', profileid = p.Id,

           timezonesidkey = 'America/Los_Angeles',

           username = 'futureuser@test.org',

           userpermissionsmarketinguser = false,

           userpermissionsofflineuser = false, userroleid = r.Id);

        insert(futureUser);

```


Apex Developer Guide Working with Data in Apex

```
      }

   }

```

This class calls the method in the previous class.

```
   @isTest

   public class UserAndContactTest {

      public testmethod static void testUserAndContact() {

        InsertFutureUser.insertUser();

        Contact currentContact = new Contact(

           firstName = String.valueOf(System.currentTimeMillis()),

           lastName = 'Contact');

        insert(currentContact);

      }

   }

###### sObjects That Don’t Support DML Operations

```

Your organization contains standard objects provided by Salesforce and custom objects that you created. These objects can be accessed
in Apex as instances of the sObject data type. You can query these objects and perform DML operations on them. However, some
standard objects don’t support DML operations although you can still obtain them in queries. The following is a non-exhaustive list of
such objects:

**•** AccountTerritoryAssignmentRule

**•** AccountTerritoryAssignmentRuleItem

**•** ApexComponent

**•** ApexPage

**•** BusinessHours

**•** BusinessProcess

**•** CategoryNode

**•** CurrencyType

**•** DatedConversionRate

**•** NetworkMember (allows `update` only)

**•** ProcessInstance

**•** Profile

**•** RecordType

**•** SelfServiceUser

**•** StaticResource

**•** Territory2

**•** UserAccountTeamMember

**•** UserPreference

**•** UserTerritory

**•** WebLink

The following are special cases of DML operations on objects.

**•** If an Account record has a record type of Person Account, the Name field can’t be modified with DML operations.


Apex Developer Guide Working with Data in Apex

**•** All standard and custom objects can also be accessed through the SOAP API. ProcessInstance is an exception. You can’t create,
update, or delete ProcessInstance in the SOAP API.

**•** DML operations aren't supported on Data Cloud data model objects (DMOs). For details on using Apex with Data Cloud objects, see
[Data Cloud in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataCloudInApex.htm)

**•** To determine if DML is supported on your specific object, use the `Schema.describeSObjects()` method as shown in this
sample code.

```
     // This example describes the ApexPage object. Replace it with your

     // objects(s) in the results list to check if DML is permitted.

     List<Schema.DescribeSobjectResult> results = Schema.describeSObjects(new List<string>

       {'ApexPage'}, SObjectDescribeOptions.DEFERRED);

     DescribeSObjectResult d = results[0];

     System.debug('isCreateable():' + d.isCreateable());

     System.debug('isUpdateable():' + d.isUpdateable());

     System.debug('isQueryable(): ' + d.isQueryable());

###### Bulk DML Exception Handling

```

Exceptions that arise from a bulk DML call (including any recursive DML operations in triggers that are fired as a direct result of the call)
are handled differently depending on where the original call came from:

**•** When errors occur because of a bulk DML call that originates directly from the Apex DML statements, or if the _`allOrNone`_
parameter of a Database DML method is set to `true`, the runtime engine follows the “all or nothing” rule: during a single operation,
all records must be updated successfully or the entire operation rolls back to the point immediately preceding the DML statement.
If the _`allOrNone`_ parameter of a Database DML method is set to `false` and a record fails, the remainder of the DML operation
can still succeed. You must iterate through the returned results to identify which records succeeded or failed. If the _`allOrNone`_
parameter of a Database DML method is set to `false` and a before-trigger assigns an invalid value to a field, the partial set of valid
records isn’t inserted.

**•** When errors occur because of a bulk DML call that originates from SOAP API with default settings, or if the _`allOrNone`_ parameter
of a Database DML method was specified as `false`, the runtime engine attempts at least a partial save:

**1.** During the first attempt, the runtime engine processes all records. Any record that generates an error due to issues such as
validation rules or unique index violations is set aside.

**2.** If there were errors during the first attempt, the runtime engine makes a second attempt that includes only those records that
didn’t generate errors. All records that didn't generate an error during the first attempt are processed, and if any record generates
an error (perhaps because of race conditions) it’s also set aside.

**3.** If there were additional errors during the second attempt, the runtime engine makes a third and final attempt that includes only
those records that didn’t generate errors during the first and second attempts. If any record generates an error, the entire operation
fails with the error message, “Too many batch retries in the presence of Apex triggers and partial failures.”

Note:

**–** During the second and third attempts, governor limits are reset to their original state before the first attempt. See Execution
Governors and Limits on page 349.

**–** Apex triggers are fired for the first save attempt, and if errors are encountered for some records and subsequent attempts
are made to save the subset of successful records, triggers are refired on this subset of records.


Apex Developer Guide Working with Data in Apex

###### Things You Should Know about Data in Apex

**Non-Null Required Fields Values and Null Fields**
When inserting new records or updating required fields on existing records, you must supply non- `null` values for all required fields.

Unlike the SOAP API, Apex allows you to change field values to `null` without updating the `fieldsToNull` array on the sObject
record. The API requires an update to this array due to the inconsistent handling of `null` values by many SOAP providers. Because
Apex runs solely on the Lightning Platform, this workaround is unnecessary.

**DML Not Supported with Some sObjects**
DML operations are not supported with certain sObjects. See sObjects That Don’t Support DML Operations.

**String Field Truncation and API Version**
Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value
that is too long for the field.

**sObject Properties to Enable DML Operations**
To be able to insert, update, delete, or undelete an sObject record, the sObject must have the corresponding property ( `createable`,
`updateable`, `deletable`, or `undeletable` respectively) set to `true` .

**ID Values**
The `insert` statement automatically sets the ID value of all new sObject records. Inserting a record that already has an ID—and
therefore already exists in your organization's data—produces an error. See Lists for more information.

The `insert` and `update` statements check each batch of records for duplicate ID values. If there are duplicates, the first five are
processed. For the sixth and all additional duplicate IDs, the SaveResult for those entries is marked with an error similar to the following:

```
    Maximum number of duplicate updates in one batch (5 allowed). Attempt to update Id

    more than once in this API call: number_of_attempts .

```

The ID of an updated sObject record cannot be modified in an `update` statement, but related record IDs can.

**Fields With Unique Constraints**
For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example,
inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must have
unique names.

**System Fields Automatically Set**
When inserting new records, system fields such as `CreatedDate`, `CreatedById`, and `SystemModstamp` are automatically
updated. You cannot explicitly specify these values in your Apex. Similarly, when updating records, system fields such as
`LastModifiedDate`, `LastModifiedById`, and `SystemModstamp` are automatically updated.

**Maximum Number of Records Processed by DML Statement**
You can pass a maximum of 10,000 sObject records to a single `insert`, `update`, `delete`, and `undelete` method.

Each `upsert` statement consists of two operations, one for inserting records and one for updating records. Each of these operations
is subject to the runtime limits for `insert` and `update`, respectively. For example, if you upsert more than 10,000 records and
all of them are being updated, you receive an error. (See Execution Governors and Limits on page 349)

**Upsert and Foreign Keys**
[You can use foreign keys to upsert sObject records if they have been set as reference fields. For more information, see Field Types](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/field_types.htm)
in the _Object Reference for Salesforce._

**Creating Records for Multiple Object Types**

As with the SOAP API, you can create records in Apex for multiple object types, including custom objects, in one DML call with API
version 20.0 and later. For example, you can create a contact and an account in one call. You can create records for up to 10 object
types in one call.

Records are saved in the same order that they’re entered in the sObject input array. If you’re entering new records that have a
parent-child relationship, the parent record must precede the child record in the array. For example, if you’re creating a contact that


Apex Developer Guide Working with Data in Apex

references an account that’s also being created in the same call, the account must have a smaller index in the array than the contact
does. The contact references the account by using an `External ID` field.

You can’t add a record that references another record of the same object type in the same call. For example, the Contact object has
a `Reports To` field that’s a reference to another contact. You can’t create two contacts in one call if one contact uses the
`Reports To` field to reference a second contact in the input array. You can create a contact that references another contact that
has been previously created.

Records for multiple object types are broken into multiple chunks by Salesforce. A chunk is a subset of the input array, and each
chunk contains records of one object type. Data is committed on a chunk-by-chunk basis. Any Apex triggers that are related to the
records in a chunk are invoked once per chunk. Consider an sObject input array that contains the following set of records:

```
     account1, account2, contact1, contact2, contact3, case1, account3, account4, contact4

```

Salesforce splits the records into five chunks:

**1.** `account1, account2`

**2.** `contact1, contact2, contact3`

**3.** `case1`

**4.** `account3, account4`

**5.** `contact4`

Each call can process up to 10 chunks. If the sObject array contains more than 10 chunks, you must process the records in more than
[one call. For additional information about this feature, see Creating Records for Different Object Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_create.htm#MixedSaveTitle) _[SOAP API Developer](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_quickstart_intro.htm)_
_[Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_quickstart_intro.htm)_ .

Note: For Apex, the chunking of the input array for an insert or update DML operation has two possible causes: the existence
of multiple object types or the default chunk size of 200. If chunking in the input array occurs because of both of these reasons,
each chunk is counted toward the limit of 10 chunks. If the input array contains only one type of sObject, you won’t hit this
limit. However, if the input array contains at least two sObject types and contains a high number of objects that are chunked
into groups of 200, you might hit this limit. For example, if you have an array that contains 1,001 consecutive leads followed
by 1,001 consecutive contacts, the array will be chunked into 12 groups: Two groups are due to the different sObject types of
Lead and Contact, and the remaining are due to the default chunking size of 200 objects. In this case, the insert or update
operation returns an error because you reached the limit of 10 chunks in hybrid arrays. The workaround is to call the DML
operation for each object type separately.

**DML and Knowledge Objects**
To execute DML code on knowledge articles (KnowledgeArticleVersion types such as the custom FAQ__kav article type), the running
user must have the Knowledge User feature license. Otherwise, calling a class method that contains DML operations on knowledge
articles results in errors. If the running user isn’t a system administrator and doesn’t have the Knowledge User feature license, calling
any method in the class returns an error even if the called method doesn’t contain DML code for knowledge articles but another
method in the class does. For example, the following class contains two methods, only one of which performs DML on a knowledge
article. A non-administrator non-knowledge user who calls the `doNothing` method will get the following error: `DML operation`

```
    UPDATE not allowed on FAQ__kav

     public class KnowledgeAccess {

      public void doNothing() {

      }

      public void DMLOperation() {

       FAQ__kav[] articles = [SELECT Id FROM FAQ__kav WHERE PublishStatus = 'Draft' and

```


Apex Developer Guide Working with Data in Apex

```
     Language = 'en_US'];

       update articles;

      }

     }

```

As a workaround, cast the input array to the DML statement from an array of FAQ__kav articles to an array of the generic sObject
type as follows:

```
     public void DMLOperation() {

       FAQ__kav[] articles = [SELECT id FROM FAQ__kav WHERE PublishStatus = 'Draft' and

     Language = 'en_US'];

       update (sObject[]) articles;

     }

##### Locking Records

```

When an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user interface.
The client locking the records can perform logic on the records and make updates with the guarantee that the locked records won’t be
changed by another client during the lock period.

###### Locking Statements

In Apex, you can use `FOR UPDATE` to lock sObject records while they’re being updated in order to prevent race conditions and
other thread safety problems.

Locking in a SOQL For Loop

Avoiding Deadlocks

###### Locking Statements

In Apex, you can use `FOR UPDATE` to lock sObject records while they’re being updated in order to prevent race conditions and other
thread safety problems.

While an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user interface.
The client locking the records can perform logic on the records and make updates with the guarantee that the locked records won’t be
changed by another client during the lock period. The lock gets released when the transaction completes.

To lock a set of sObject records in Apex, embed the keywords `FOR UPDATE` after any inline SOQL statement. For example, the following
statement, in addition to querying for two accounts, also locks the accounts that are returned:

```
   Account [] accts = [SELECT Id FROM Account LIMIT 2 FOR UPDATE];

```

Note: You can’t use the `ORDER BY` keywords in any SOQL query that uses locking.

Locking Considerations

**•** While the records are locked by a client, the locking client can modify their field values in the database in the same transaction. Other
clients have to wait until the transaction completes and the records are no longer locked before being able to update the same
records. Other clients can still query the same records while they’re locked.

**•** If you attempt to lock a record currently locked by another client, your process waits a maximum of 10 seconds for the lock to be
released before acquiring a new lock. If the wait time exceeds 10 seconds, a `QueryException` is thrown. Similarly, if you attempt


Apex Developer Guide Working with Data in Apex

to update a record currently locked by another client and the lock isn’t released within a maximum of 10 seconds, a `DmlException`
is thrown.

**•** If a client attempts to modify a locked record, the update operation can succeed if the lock gets released within a short amount of
time after the update call was made. In this case, it’s possible that the updates overwrite changes made by the locking client if the
second client obtained an old copy of the record. To prevent the overwrite from happening, the second client must lock the record
first. The locking process returns a fresh copy of the record from the database through the `SELECT` statement. The second client
can use this copy to make new updates.

**•** The record locks that are obtained in Apex via `FOR UPDATE` clause are automatically released when making callouts. The information
is logged in the debug log and the logged message includes the most recently locked entity type. For example:

```
    FOR_UPDATE_LOCKS_RELEASE FOR UPDATE locks released due to a callout. The most recent
```

`lock was Account.` Use caution while making callouts in contexts where `FOR UPDATE` queries could have been previously
executed.

**•** When you perform a DML operation on one record, related records are locked in addition to the record in question.

Warning: Use care when setting locks in your Apex code. See Avoiding Deadlocks.

###### Locking in a SOQL For Loop

The `FOR UPDATE` keywords can also be used within SOQL `for` loops. For example:

```
   for (Account[] accts : [SELECT Id FROM Account

                  FOR UPDATE]) {

      // Your code

   }

```

As discussed in SOQL For Loops, the example above corresponds internally to calls to the `query()` and `queryMore()` methods
in the SOAP API.

Note that there is no `commit` statement. If your Apex trigger completes successfully, any database changes are automatically committed.
If your Apex trigger does not complete successfully, any changes made to the database are rolled back.

###### Avoiding Deadlocks

Apex has the possibility of deadlocks, as does any other procedural logic language involving updates to multiple database tables or
rows. To avoid such deadlocks, the Apex runtime engine:

**1.** First locks sObject parent records, then children.

**2.** Locks sObject records in order of ID when multiple records of the same type are being edited.

As a developer, use care when locking rows to ensure that you are not introducing deadlocks. Verify that you are using standard deadlock
avoidance techniques by accessing tables and rows in the same order from all locations in an application.

#### SOQL and SOSL Queries

You can evaluate Salesforce Object Query Language (SOQL) or Salesforce Object Search Language (SOSL) statements on-the-fly in Apex
by surrounding the statement in square brackets.

SOQL Statements

SOQL statements evaluate to a list of sObjects, a single sObject, or an Integer for `count` method queries.


Apex Developer Guide Working with Data in Apex

For example, you could retrieve a list of accounts that are named Acme:

```
   List<Account> aa = [SELECT Id, Name FROM Account WHERE Name = 'Acme'];

```

From this list, you can access individual elements:

```
   if (!aa.isEmpty()) {

     // Execute commands

   }

```

You can also create new objects from SOQL queries on existing ones. This example creates a new contact for the first account with the
number of employees greater than 10.

```
   Contact c = new Contact(Account = [SELECT Name FROM Account

      WHERE NumberOfEmployees > 10 LIMIT 1]);

   c.FirstName = 'James';

   c.LastName = 'Yoyce';

```

The newly created object contains null values for its fields, which must be set.

The `count` method can be used to return the number of rows returned by a query. The following example returns the total number
of contacts with the last name of Weissman:

```
   Integer i = [SELECT COUNT() FROM Contact WHERE LastName = 'Weissman'];

```

You can also operate on the results using standard arithmetic:

```
   Integer j = 5 * [SELECT COUNT() FROM Account];

```

SOQL limits apply when executing SOQL queries. See Execution Governors and Limits.

For a full description of SOQL query syntax, see the _[Salesforce SOQL and SOSL Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/)_ .

SOSL Statements

SOSL statements evaluate to a list of lists of sObjects, where each list contains the search results for a particular sObject type. The result
lists are always returned in the same order as they were specified in the SOSL query. If a SOSL query doesn’t return any records for a
specified sObject type, the search results include an empty list for that sObject.

For example, you can return a list of accounts, contacts, opportunities, and leads that begin with the phrase map:

```
   List<List<SObject>> searchList = [FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name),

    Contact, Opportunity, Lead];

```

Note: The syntax of the `FIND` clause in Apex differs from the syntax of the `FIND` clause in SOAP API and REST API:

**•** In Apex, the value of the `FIND` clause is demarcated with single quotes. For example:

```
       FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name), Contact, Opportunity, Lead

```

Note: Apex that is running in system mode ignores field-level security while scanning for a match using `IN ALL`
`FIELDS` .

**•** In the API, the value of the `FIND` clause is demarcated with braces. For example:

```
       FIND {map*} IN ALL FIELDS RETURNING Account (Id, Name), Contact, Opportunity, Lead

```


Apex Developer Guide Working with Data in Apex

From `searchList`, you can create arrays for each object returned:

```
   Account [] accounts = ((List<Account>)searchList[0]);

   Contact [] contacts = ((List<Contact>)searchList[1]);

   Opportunity [] opportunities = ((List<Opportunity>)searchList[2]);

   Lead [] leads = ((List<Lead>)searchList[3]);

```

SOSL limits apply when executing SOSL queries. See Execution Governors and Limits.

Note: The 4,000 characters limit for WHERE clause strings doesn’t apply to SOQL queries in Apex if the WHERE clause includes
the IN operator.

For a full description of SOSL query syntax, see the _[Salesforce SOQL and SOSL Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/)_ .

##### 1. Working with SOQL and SOSL Query Results

2. Accessing sObject Fields Through Relationships

3. Understanding Foreign Key and Parent-Child Relationship SOQL Queries

4. Working with SOQL Aggregate Functions
Aggregate functions in SOQL, such as `SUM()` and `MAX()`, allow you to roll up and summarize your data in a query.

5. Working with Very Large SOQL Queries

6. Using SOQL Queries That Return One Record
SOQL queries can be used to assign a single sObject value when the result list contains only one element.

7. Improve Performance by Avoiding Null Values

8. Working with Polymorphic Relationships in SOQL Queries
A polymorphic relationship is a relationship between objects where a referenced object can be one of several different types. For
example, the `Who` relationship field of a Task can be a Contact or a Lead.

9. Using Apex Variables in SOQL and SOSL Queries

10. Querying All Records with a SOQL Statement

##### Working with SOQL and SOSL Query Results

SOQL and SOSL queries only return data for sObject fields that are selected in the original query. If you try to access a field that was not
selected in the SOQL or SOSL query (other than ID), you receive a runtime error, even if the field contains a value in the database. The
following code example causes a runtime error:

```
   insert new Account(Name = 'Singha');

   Account acc = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1];

   // Note that name is not selected

   String name = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1].Name;

```

The following is the same code example rewritten so it does not produce a runtime error. Note that `Name` has been added as part of
the select statement, after `Id` .

```
   insert new Account(Name = 'Singha');

   Account acc = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1];

   // Note that name is now selected

   String name = [SELECT Id, Name FROM Account WHERE Name = 'Singha' LIMIT 1].Name;

```


Apex Developer Guide Working with Data in Apex

Even if only one sObject field is selected, a SOQL or SOSL query always returns data as complete records. Consequently, you must
dereference the field in order to access it. For example, this code retrieves an sObject list from the database with a SOQL query, accesses
the first account record in the list, and then dereferences the record's `AnnualRevenue` field:

```
   Double rev = [SELECT AnnualRevenue FROM Account

            WHERE Name = 'Acme'][0].AnnualRevenue;

   // When only one result is returned in a SOQL query, it is not necessary

   // to include the list's index.

   Double rev2 = [SELECT AnnualRevenue FROM Account

            WHERE Name = 'Acme' LIMIT 1].AnnualRevenue;

```

The only situation in which it is not necessary to dereference an sObject field in the result of an SOQL query, is when the query returns
an Integer as the result of a `COUNT` operation:

```
   Integer i = [SELECT COUNT() FROM Account];

```

Fields in records returned by SOSL queries must always be dereferenced.

Also note that sObject fields that contain formulas return the value of the field at the time the SOQL or SOSL query was issued. Any
changes to other fields that are used within the formula are not reflected in the formula field value until the record has been saved and
re-queried in Apex. Like other read-only sObject fields, the values of the formula fields themselves cannot be changed in Apex.

##### Accessing sObject Fields Through Relationships

sObject records represent relationships to other records with two fields: an ID and an address that points to a representation of the
associated sObject. For example, the Contact sObject has both an `AccountId` field of type ID, and an `Account` field of type Account
that points to the associated sObject record itself.

The ID field can be used to change the account with which the contact is associated, while the sObject reference field can be used to
access data from the account. The reference field is only populated as the result of a SOQL or SOSL query (see note).

For example, the following Apex code shows how an account and a contact can be associated with one another, and then how the
contact can be used to modify a field on the account:

Note: To provide the most complete example, this code uses some elements that are described later in this guide:

**•** For information on `insert` and `update` [, see Insert Statement and Update Statement.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm)

```
   Account a = new Account(Name = 'Acme');

   insert a; // Inserting the record automatically assigns a

          // value to its ID field

   Contact c = new Contact(LastName = 'Weissman');

   c.AccountId = a.Id;

   // The new contact now points at the new account

   insert c;

   // A SOQL query accesses data for the inserted contact,

   // including a populated c.account field

   c = [SELECT Account.Name FROM Contact WHERE Id = :c.Id];

   // Now fields in both records can be changed through the contact

   c.Account.Name = 'salesforce.com';

   c.LastName = 'Roth';

   // To update the database, the two types of records must be

```


Apex Developer Guide Working with Data in Apex

```
   // updated separately

   update c; // This only changes the contact's last name

   update c.Account; // This updates the account name

```

Note: The expression `c.Account.Name`, and any other expression that traverses a relationship, displays slightly different
characteristics when it is read as a value than when it is modified:

**•** When being read as a value, if `c.Account` is null, then `c.Account.Name` evaluates to `null`, but does _not_ yield a
`NullPointerException` . This design allows developers to navigate multiple relationships without the tedium of having
to check for null values.

**•** When being modified, if `c.Account` is null, then `c.Account.Name` _does_ yield a `NullPointerException` .

In SOSL, you would access data for the inserted contact in a similar way to the SELECT statement used in the previous SOQL example.

```
   List<List<SObject>> searchList = [FIND 'Acme' IN ALL FIELDS RETURNING

   Contact(id,Account.Name)]

```

In addition, the sObject field key can be used with `insert`, `update`, or `upsert` to resolve foreign keys by external ID. For example:

```
   Account refAcct = new Account(externalId__c = '12345');

   Contact c = new Contact(Account = refAcct, LastName = 'Kay');

   insert c;

```

This inserts a new contact with the `AccountId` equal to the account with the `external_id` equal to ‘12345’. If there is no such
account, the insert fails.

Tip: The following code is equivalent to the code above. However, because it uses a SOQL query, it is not as efficient. If this code
was called multiple times, it could reach the execution limit for the maximum number of SOQL queries. For more information on
execution limits, see Execution Governors and Limits on page 349.

```
      Account refAcct = [SELECT Id FROM Account WHERE externalId__c='12345'];

      Contact c = new Contact(Account = refAcct.Id);

      insert c;

##### Understanding Foreign Key and Parent-Child Relationship SOQL Queries

```

The `SELECT` statement of a SOQL query can be any valid SOQL statement, including foreign key and parent-child record joins. If foreign
key joins are included, the resulting sObjects can be referenced using normal field notation. For example:

```
   System.debug([SELECT Account.Name FROM Contact

            WHERE FirstName = 'Caroline'].Account.Name);

```

Additionally, parent-child relationships in sObjects act as SOQL queries as well. For example:

```
   for (Account a : [SELECT Id, Name, (SELECT LastName FROM Contacts)

              FROM Account

              WHERE Name = 'Acme']) {

      Contact[] cons = a.Contacts;

   }

   //The following example also works because we limit to only 1 contact

```


Apex Developer Guide Working with Data in Apex

```
   for (Account a : [SELECT Id, Name, (SELECT LastName FROM Contacts LIMIT 1)

              FROM Account

              WHERE Name = 'testAgg']) {

      Contact c = a.Contacts;

   }

##### Working with SOQL Aggregate Functions

```

Aggregate functions in SOQL, such as `SUM()` and `MAX()`, allow you to roll up and summarize your data in a query.

For more information on aggregate functions, see _Aggregate Functions_ [in the Salesforce SOQL and SOSL Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_agg_functions.htm)

You can use aggregate functions without using a `GROUP BY` clause. For example, you could use the `AVG()` aggregate function to
find the average `Amount` for all your opportunities.

```
   AggregateResult[] groupedResults

     = [SELECT AVG(Amount)aver FROM Opportunity];

   Object avgAmount = groupedResults[0].get('aver');

```

Note that any query that includes an aggregate function returns its results in an array of AggregateResult objects. AggregateResult is a
read-only sObject and is only used for query results.

Aggregate functions become a more powerful tool to generate reports when you use them with a `GROUP BY` clause. For example,
you could find the average `Amount` for all your opportunities by campaign.

```
   AggregateResult[] groupedResults

     = [SELECT CampaignId, AVG(Amount)

       FROM Opportunity

       GROUP BY CampaignId];

   for (AggregateResult ar : groupedResults) {

      System.debug('Campaign ID' + ar.get('CampaignId'));

      System.debug('Average amount' + ar.get('expr0'));

   }

```

Any aggregated field in a `SELECT` list that does not have an alias automatically gets an implied alias with a format `expr` _**`i`**_, where _`i`_
denotes the order of the aggregated fields with no explicit aliases. The value of _`i`_ starts at 0 and increments for every aggregated field
with no explicit alias. For more information, see _Using Aliases with_ _`GROUP BY`_ [in the Salesforce SOQL and SOSL Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/)

Note: Queries that include aggregate functions are still subject to the limit on total number of query rows. All aggregate functions
other than `COUNT()` or `COUNT(fieldname)` include each row used by the aggregation as a query row for the purposes
of limit tracking.

For `COUNT()` or `COUNT(fieldname)` queries, limits are counted as one query row, unless the query contains a GROUP BY
clause, in which case one query row per grouping is consumed.

For information about the limits that apply to queries with `for` loop, see SOQL For Loops on page 182.

##### Working with Very Large SOQL Queries

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Your SOQL query sometimes returns so many sObjects that the limit on heap size is exceeded and an error occurs. To resolve, use a SOQL
query `for` loop instead, since it can process multiple batches of records by using internal calls to `query` and `queryMore` .


Apex Developer Guide Working with Data in Apex

For example, if the results are too large, this syntax causes a runtime exception:

```
   Account[] accts = [SELECT Id FROM Account];

```

Instead, use a SOQL query `for` loop as in one of the following examples:

```
   // Use this format if you are not executing DML statements

   // within the for loop

   for (Account a : [SELECT Id, Name FROM Account

              WHERE Name LIKE 'Acme%']) {

      // Your code without DML statements here

   }

   // Use this format for efficiency if you are executing DML statements

   // within the for loop

   for (List<Account> accts : [SELECT Id, Name FROM Account

                    WHERE Name LIKE 'Acme%']) {

      for (Account a : accts) {

      // Your code here

      }

      update accts;

   }

```

Note: Using the SOQL query within the `for` loop reduces the possibility of reaching the limit on heap size. However, this approach
[can result in more CPU cycles being used with increased DML calls. For more information, see SOQL For Loops Versus Standard](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_loops_for_SOQL.htm#soql_for_loop_desc)
[SOQL Queries.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_loops_for_SOQL.htm#soql_for_loop_desc)

The following example demonstrates a SOQL query `for` loop that’s used to mass update records. Suppose that you want to change
the last name of a contact in records for contacts whose first and last names match specified criteria:

```
   public void massUpdate() {

      for (List<Contact> contacts:

       [SELECT FirstName, LastName FROM Contact]) {

        for(Contact c : contacts) {

           if (c.FirstName == 'Barbara' &&

            c.LastName == 'Gordon') {

             c.LastName = 'Wayne';

           }

        }

        update contacts;

      }

   }

```

Instead of using a SOQL query in a `for` loop, the preferred method of mass updating records is to use batch Apex, which minimizes
the risk of hitting governor limits.

For more information, see SOQL For Loops on page 182.

More Efficient SOQL Queries

For best performance, SOQL queries must be selective, particularly for queries inside triggers.

**Selective SOQL Query Criteria**

**•** A query is selective when one of the query filters is on an indexed field and the query filter reduces the resulting number of rows
below a system-defined threshold. The performance of the SOQL query improves when two or more filters used in the WHERE
clause meet the mentioned conditions.


Apex Developer Guide Working with Data in Apex

**•** As a best practice, a query is considered selective when a query filter on an indexed field matches less than 10% of the total
rows.

**Custom Index Considerations for Selective SOQL Queries**

**•** The following fields are indexed by default.

**–** Primary keys (Id, Name, and OwnerId fields)

