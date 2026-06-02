Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

Signature

```
   public static Database.SaveResult update(SObject recordToUpdate, Database.DMLOptions

   dmlOptions, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   recordToUpdate
```

Type: SObject

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.SaveResult

##### **`update(recordsToUpdate, dmlOptions, accessLevel)`**

Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

Signature

```
   public static List<Database.SaveResult> update(List<SObject> recordsToUpdate,

   Database.DMLOptions dmlOptions, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToUpdate
```

Type: List<sObject>

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>


Apex Reference Guide Database Class

##### upsert(recordToUpsert, externalIdField, allOrNone)

Creates a new sObject record or updates an existing sObject record within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

Signature

```
   public static Database.UpsertResult upsert(sObject recordToUpsert, Schema.SObjectField

   externalIDField, Boolean allOrNone)

```

Parameters

```
   recordToUpsert
```

Type: sObject

```
   externalIdField
```

Type: Schema.SObjectField

(Optional) The _`externalIdField`_ is of type `Schema.SObjectField`, that is, a field token. Find the token for the field by
using the `fields` special method. For example, `Schema.SObjectField f = Account.Fields.MyExternalId` .
The _`externalIdField`_ parameter is the field that `upsert()` uses to match sObjects with existing records. This field can be
a custom field marked as external ID, or a standard field with the `idLookup` attribute.

Note: If _`externalIdField`_ isn’t specified, then the ID field is used to determine a match with existing records.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.UpsertResult

Usage

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed upsert method counts against the governor limit for DML statements.

For more information on how the upsert operation works, see the upsert() statement.

##### upsert(recordsToUpsert, externalIdField, allOrNone)

Creates new sObject records or updates existing sObject records within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

Signature

```
   public static Database.UpsertResult[] upsert(sObject[] recordsToUpsert,

   Schema.SObjectField externalIdField, Boolean allOrNone)

```


Apex Reference Guide Database Class

Parameters

```
   recordsToUpsert
```

Type: sObject []

```
   externalIdField
```

Type: Schema.SObjectField

(Optional) The _`externalIdField`_ is of type `Schema.SObjectField`, that is, a field token. Find the token for the field by
using the `fields` special method. For example, `Schema.SObjectField f = Account.Fields.MyExternalId` .
The _`externalIdField`_ parameter is the field that `upsert()` uses to match sObjects with existing records. This field can be
a custom field marked as external ID, or a standard field with the `idLookup` attribute.

Note: If _`externalIdField`_ isn’t specified, then the ID field is used to determine a match with existing records.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

If _`allOrNone`_ is set to `false` and a before-trigger assigns an invalid value to a field, the partial set of valid records isn’t inserted.

Return Value

Type: Database.UpsertResult[]

Usage

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed upsert method counts against the governor limit for DML statements.

For more information on how the upsert operation works, see the upsert() statement.

##### **`upsert(recordToUpsert, externalIdField, allOrNone, accessLevel)`**

Creates a new sObject record or updates an existing sObject record within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

Signature

```
   public static Database.UpsertResult upsert(SObject recordToUpsert, Schema.SObjectField

   externalIdField, Boolean allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordToUpsert
```

Type: SObject

```
   externalIdField
```

Type: Schema.SObjectField


Apex Reference Guide Database Class

(Optional) The _`externalIdField`_ is of type `Schema.SObjectField`, that is, a field token. Find the token for the field by
using the `fields` special method. For example, `Schema.SObjectField f = Account.Fields.MyExternalId` .
The _`externalIdField`_ parameter is the field that `upsert()` uses to match sObjects with existing records. This field can be
a custom field marked as external ID, or a standard field with the `idLookup` attribute.

Note: If _`externalIdField`_ isn’t specified, then the ID field is used to determine a match with existing records.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.UpsertResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed upsert method counts against the governor limit for DML statements.

For more information on how the upsert operation works, see the upsert() statement.

##### **`upsert(recordsToUpsert, externalIdField, allOrNone, accessLevel)`**

Creates new sObject records or updates existing sObject records within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.


Apex Reference Guide Database Class

Signature

```
   public static List<Database.UpsertResult> upsert(List<SObject> recordsToUpsert,

   Schema.SObjectField externalIdField, Boolean allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToUpsert
```

Type: List<sObject >

```
   externalIdField
```

Type: Schema.SObjectField

(Optional) The _`externalIdField`_ is of type `Schema.SObjectField`, that is, a field token. Find the token for the field by
using the `fields` special method. For example, `Schema.SObjectField f = Account.Fields.MyExternalId` .
The _`externalIdField`_ parameter is the field that `upsert()` uses to match sObjects with existing records. This field can be
a custom field marked as external ID, or a standard field with the `idLookup` attribute.

Note: If _`externalIdField`_ isn’t specified, then the ID field is used to determine a match with existing records.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

If _`allOrNone`_ is set to `false` and a before-trigger assigns an invalid value to a field, the partial set of valid records isn’t inserted.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.UpsertResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)


Apex Reference Guide Database Class

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

Each executed `upsert` method counts against the governor limit for DML statements.

For more information on how the upsert operation works, see the upsert() statement.

##### updateAsync(sobjects, callback)

Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

Signature

```
   public static List<Database.SaveResult> updateAsync(List<SObject> sobjects,

   DataSource.AsyncSaveCallback callback)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncSaveCallback` .

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobject, callback)

Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

Signature

```
   public static Database.SaveResult updateAsync(SObject sobject,

   DataSource.AsyncSaveCallback callback)

```


Apex Reference Guide Database Class

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncSaveCallback` .

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobjects)

Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

Signature

```
   public static List<Database.SaveResult> updateAsync(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobject)

Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

Signature

```
   public static Database.SaveResult updateAsync(SObject sobject)

```


Apex Reference Guide Database Class

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobjects, callback, accessLevel)

Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

Signature

```
   public static List<Database.SaveResult> updateAsync(List<SObject> sobjects,

   DataSource.AsyncSaveCallback callback, System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. The execution is in system mode regardless of the `accessLevel` parameter. Use the
action callback to update org data according to the operation’s results. The callback object must extend
`DataSource.AsyncSaveCallback` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .


Apex Reference Guide Database Class

##### updateAsync(sobject, callback, accessLevel)

Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

Signature

```
   public static Database.SaveResult updateAsync(SObject sobject,

   DataSource.AsyncSaveCallback callback, System.AccessLevel accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. The execution is in system mode regardless of the `accessLevel` parameter. Use the
action callback to update org data according to the operation’s results. The callback object must extend
`DataSource.AsyncSaveCallback` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobjects, accessLevel)

Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

Signature

```
   public static List<Database.SaveResult> updateAsync(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobject, accessLevel)

Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

Signature

```
   public static Database.SaveResult updateAsync(SObject sobject, System.AccessLevel

   accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .


Apex Reference Guide Database Class

##### updateImmediate(sobjects)

Initiates requests to update external object data on the relevant external systems. The requests are executed synchronously and are sent
to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains pending
changes, the synchronous operations can't be completed and throw exceptions.

Signature

```
   public static List<Database.SaveResult> updateImmediate(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation.

Usage

The operation allows partial success. If one or more record updates fail, the method doesn’t throw an exception and the remainder of
the DML operation can still succeed. The returned `SaveResult` objects indicate whether the operation was successful. If it wasn’t
successful, the objects also return the error code and description.

##### updateImmediate(sobject)

Initiates a request to update external object data on the relevant external system. The request is executed synchronously and is sent to
the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.SaveResult updateImmediate(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

Return Value

Type: Database.SaveResult

Status result for the update operation.


Apex Reference Guide Database Class

Usage

If a record update fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it wasn’t successful, the object returns the error code and description.

##### **`updateImmediate(sobjects, accessLevel)`**

Initiates requests to update external object data on the relevant external systems. The requests are executed synchronously and are sent
to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains pending
changes, the synchronous operations can't be completed and throw exceptions.

Signature

```
   public static List<Database.SaveResult> updateImmediate(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to modify.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation.

Usage

The operation allows partial success. If one or more record updates fail, the method doesn’t throw an exception and the remainder of
the DML operation can still succeed. The returned `SaveResult` objects indicate whether the operation was successful. If it wasn’t
successful, the objects also return the error code and description.

##### **`updateImmediate(sobject, accessLevel)`**

Initiates a request to update external object data on the relevant external system. The request is executed synchronously and is sent to
the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.SaveResult updateImmediate(SObject sobject, System.AccessLevel

   accessLevel)

```


### Apex Reference Guide Date Class

Parameters

```
   sobject
```

Type: SObject

External object record to modify.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.SaveResult

Status result for the update operation.

Usage

If a record update fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it failed, the object returns the error code and description.

### Date Class

Contains methods for the Date primitive data type.

Namespace

System

Usage

[For more information on Dates, see Date Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Date Methods

### The following are methods for Date .

IN THIS SECTION:

addDays(additionalDays)
Adds the specified number of additional days to a Date.

addMonths(additionalMonths)
Adds the specified number of additional months to a Date

addYears(additionalYears)
Adds the specified number of additional years to a Date


Apex Reference Guide Date Class

day()
Returns the day-of-month component of a Date.

dayOfYear()
Returns the day-of-year component of a Date.

daysBetween(secondDate)
Returns the number of days between the Date that called the method and the specified date.

daysInMonth(year, month)
Returns the number of days in the month for the specified _`year`_ and _`month`_ (1=Jan).

format()
Returns the Date as a string using the locale of the context user

isLeapYear(year)
Returns `true` if the specified year is a leap year.

isSameDay(dateToCompare)
Returns `true` if the Date that called the method is the same as the specified date.

month()
Returns the month component of a Date (1=Jan).

monthsBetween(secondDate)
Returns the number of months between the Date that called the method and the specified date, ignoring the difference in days.

newInstance(year, month, day)
Constructs a Date from Integer representations of the _`year`_, _`month`_ (1=Jan), and _`day`_ .

parse(stringDate)
Constructs a Date from a String. The format of the String depends on the local date format.

today()
Returns the current date in the current user's time zone.

toStartOfMonth()
Returns the first of the month for the Date that called the method.

toStartOfWeek()
Returns the start of the week for the Date that called the method, depending on the context user's locale.

valueOf(stringDate)
Returns a Date that contains the value of the specified String.

valueOf(fieldValue)
Converts the specified object to a `Date` . Use this method to convert a history tracking field value or an object that represents a
`Date` value.

year()
Returns the year component of a Date

##### addDays(additionalDays)

Adds the specified number of additional days to a Date.


Apex Reference Guide Date Class

Signature

```
   public Date addDays(Integer additionalDays)

```

Parameters

```
   additionalDays
```

Type: Integer

Return Value

Type: Date

Example

```
   Date myDate = Date.newInstance(1960, 2, 17);

   Date newDate = mydate.addDays(2);

##### addMonths(additionalMonths)

```

Adds the specified number of additional months to a Date

Signature

```
   public Date addMonths(Integer additionalMonths)

```

Parameters

```
   additionalMonths
```

Type: Integer

Return Value

Type: Date

Example

```
   date myDate = date.newInstance(1990, 11, 21);

   date newDate = myDate.addMonths(3);

   date expectedDate = date.newInstance(1991, 2, 21);

   system.assertEquals(expectedDate, newDate);

##### addYears(additionalYears)

```

Adds the specified number of additional years to a Date

Signature

```
   public Date addYears(Integer additionalYears)

```


Apex Reference Guide Date Class

Parameters

```
   additionalYears
```

Type: Integer

Return Value

Type: Date

Example

```
   date myDate = date.newInstance(1983, 7, 15);

   date newDate = myDate.addYears(2);

   date expectedDate = date.newInstance(1985, 7, 15);

   system.assertEquals(expectedDate, newDate);

##### day()

```

Returns the day-of-month component of a Date.

Signature

```
   public Integer day()

```

Return Value

Type: Integer

Example

```
   date myDate = date.newInstance(1989, 4, 21);

   Integer day = myDate.day();

   system.assertEquals(21, day);

##### dayOfYear()

```

Returns the day-of-year component of a Date.

Signature

```
   public Integer dayOfYear()

```

Return Value

Type: Integer

Example

```
   date myDate = date.newInstance(1998, 10, 21);

   Integer day = myDate.dayOfYear();

   system.assertEquals(294, day);

```


Apex Reference Guide Date Class

##### daysBetween(secondDate)

Returns the number of days between the Date that called the method and the specified date.

Signature

```
   public Integer daysBetween(Date secondDate)

```

Parameters

```
   secondDate
```

Type: Date

Return Value

Type: Integer

Usage

If the Date that calls the method occurs after the _`secondDate`_, the return value is negative.

Example

```
   Date startDate = Date.newInstance(2008, 1, 1);

   Date dueDate = Date.newInstance(2008, 1, 30);

   Integer numberDaysDue = startDate.daysBetween(dueDate);

##### daysInMonth(year, month)

```

Returns the number of days in the month for the specified _`year`_ and _`month`_ (1=Jan).

Signature

```
   public static Integer daysInMonth(Integer year, Integer month)

```

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

Return Value

Type: Integer

Example

The following example finds the number of days in the month of February in the year 1960.

```
   Integer numberDays = date.daysInMonth(1960, 2);

```


Apex Reference Guide Date Class

##### format()

Returns the Date as a string using the locale of the context user

Signature

```
   public String format()

```

Return Value

Type: String

Example

```
   // In American-English locale

   date myDate = date.newInstance(2001, 3, 21);

   String dayString = myDate.format();

   system.assertEquals('3/21/2001', dayString);

##### isLeapYear(year)

```

Returns `true` if the specified year is a leap year.

Signature

```
   public static Boolean isLeapYear(Integer year)

```

Parameters

```
   year
```

Type: Integer

Return Value

Type: Boolean

Example

```
   system.assert(Date.isLeapYear(2004));

##### isSameDay(dateToCompare)

```

Returns `true` if the Date that called the method is the same as the specified date.

Signature

```
   public Boolean isSameDay(Date dateToCompare)

```


Apex Reference Guide Date Class

Parameters

```
   dateToCompare
```

Type: Date

Return Value

Type: Boolean

Example

```
   date myDate = date.today();

   date dueDate = date.newInstance(2008, 1, 30);

   boolean dueNow = myDate.isSameDay(dueDate);

##### month()

```

Returns the month component of a Date (1=Jan).

Signature

```
   public Integer month()

```

Return Value

Type: Integer

Example

```
   date myDate = date.newInstance(2004, 11, 21);

   Integer month = myDate.month();

   system.assertEquals(11, month);

##### monthsBetween(secondDate)

```

Returns the number of months between the Date that called the method and the specified date, ignoring the difference in days.

Signature

```
   public Integer monthsBetween(Date secondDate)

```

Parameters

```
   secondDate
```

Type: Date

Return Value

Type: Integer


Apex Reference Guide Date Class

Example

```
   Date firstDate = Date.newInstance(2006, 12, 2);

   Date secondDate = Date.newInstance(2012, 12, 8);

   Integer monthsBetween = firstDate.monthsBetween(secondDate);

   System.assertEquals(72, monthsBetween);

##### newInstance(year, month, day)

```

Constructs a Date from Integer representations of the _`year`_, _`month`_ (1=Jan), and _`day`_ .

Signature

```
   public static Date newInstance(Integer year, Integer month, Integer day)

```

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

```
   day
```

Type: Integer

Return Value

Type: Date

Example

The following example creates the date February 17th, 1960:

```
   Date myDate = date.newinstance(1960, 2, 17);

##### parse(stringDate)

```

Constructs a Date from a String. The format of the String depends on the local date format.

Signature

```
   public static Date parse(String stringDate)

```

Parameters

```
   stringDate
```

Type: String

Return Value

Type: Date


Apex Reference Guide Date Class

Example

The following example works in some locales.

```
   date mydate = date.parse('12/27/2009');

##### today()

```

Returns the current date in the current user's time zone.

Signature

```
   public static Date today()

```

Return Value

Type: Date

##### toStartOfMonth()

Returns the first of the month for the Date that called the method.

Signature

```
   public Date toStartOfMonth()

```

Return Value

Type: Date

Example

```
   date myDate = date.newInstance(1987, 12, 17);

   date firstDate = myDate.toStartOfMonth();

   date expectedDate = date.newInstance(1987, 12, 1);

   system.assertEquals(expectedDate, firstDate);

##### toStartOfWeek()

```

Returns the start of the week for the Date that called the method, depending on the context user's locale.

Signature

```
   public Date toStartOfWeek()

```

Return Value

Type: Date


Apex Reference Guide Date Class

Example

For example, the start of a week is Sunday in the United States locale, and Monday in European locales. For example:

```
   Date myDate = Date.today();

   Date weekStart = myDate.toStartofWeek();

##### valueOf(stringDate)

```

Returns a Date that contains the value of the specified String.

Signature

```
   public static Date valueOf(String stringDate)

```

Parameters

```
   stringDate
```

Type: String

Return Value

Type: Date

Usage

The specified string should use the standard date format “yyyy-MM-dd HH:mm:ss” in the local time zone.

Example

```
   string year = '2008';

   string month = '10';

   string day = '5';

   string hour = '12';

   string minute = '20';

   string second = '20';

   string stringDate = year + '-' + month

    + '-' + day + ' ' + hour + ':' +

   minute + ':' + second;

   Date myDate = date.valueOf(stringDate);

##### valueOf(fieldValue)

```

Converts the specified object to a `Date` . Use this method to convert a history tracking field value or an object that represents a `Date`
value.

Signature

```
   public static Date valueOf(Object fieldValue)

```


Apex Reference Guide Date Class

Parameters

```
   fieldValue
```

Type: Object

Return Value

Type: Date

Usage

Use this method with the `OldValue` or `NewValue` fields of history sObjects, such as `AccountHistory`, when the field is a Date
field.

Example

This example converts history tracking fields to `Date` values.

```
   List<AccountHistory> ahlist = [SELECT Field,OldValue,NewValue FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'MyDate__c') {

      Date oldValue = Date.valueOf(ah.OldValue);

      Date newValue = Date.valueOf(ah.NewValue);

     }

   }

```

Versioned Behavior Changes

`Date.valueOf` has been versioned in these releases.

**API version 33.0 or earlier**
If you call `Date.valueOf` with a `Datetime` object, the method returns a `Date` value that contains the hours, minutes,
seconds, and milliseconds set.

**API version 34.0 to API version 53.0**
If you call `Date.valueOf` with a `Datetime` object, the method converts `Datetime` to a valid `Date` without the time
information, but the result depends on the manner in which the `Datetime` object was initialized. For example, if the `Datetime`
object was initialized using `Datetime.valueOf(stringDate)`, the returned `Date` value contains time (hours) information.
If the `Datetime` object is initialized using `Datetime.newInstance(year, month, day, hour, minute,`
`second)` the returned `Date` value doesn’t contain time information.

**API version 54.0 and later**
If you call `Date.valueOf` with a `Datetime` object, the method converts the object to a valid `Date` without the time
information.

##### year()

Returns the year component of a Date

Signature

```
   public Integer year()

```


### Apex Reference Guide Datetime Class

Return Value

Type: Integer

Example

```
   date myDate = date.newInstance(1988, 12, 17);

   system.assertEquals(1988, myDate.year());

### Datetime Class

```

Contains methods for the Datetime primitive data type.

Namespace

System

Usage

Apex supports both implicit and explicit casting of Date values to Datetime, with the time component being zeroed out in the resulting
[Datetime value. For more information about the Datetime, see Datetime Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Datetime Methods

### The following are methods for Datetime .

IN THIS SECTION:

addDays(additionalDays)
Adds the specified number of days to a Datetime.

addHours(additionalHours)
Adds the specified number of hours to a Datetime.

addMinutes(additionalMinutes)
Adds the specified number of minutes to a Datetime.

addMonths(additionalMonths)
Adds the specified number of months to a Datetime.

addSeconds(additionalSeconds)
Adds the specified number of seconds to a Datetime.

addYears(additionalYears)
Adds the specified number of years to a Datetime.

date()
Returns the Date component of a Datetime in the local time zone of the context user.

dateGMT()
Return the Date component of a Datetime in the GMT time zone.

day()
Returns the day-of-month component of a Datetime in the local time zone of the context user.


Apex Reference Guide Datetime Class

dayGmt()
Returns the day-of-month component of a Datetime in the GMT time zone.

dayOfYear()
Returns the day-of-year component of a Datetime in the local time zone of the context user.

dayOfYearGmt()
Returns the day-of-year component of a Datetime in the GMT time zone.

format()
Converts the date to the local time zone and returns the converted date as a formatted string using the locale of the context user.
If the time zone cannot be determined, GMT is used.

format(dateFormatString)
Converts the date to the local time zone and returns the converted date as a string using the supplied Java simple date format. If
the time zone cannot be determined, GMT is used.

format(dateFormatString, timezone)
Converts the date to the specified time zone and returns the converted date as a string using the supplied Java simple date format.
If the supplied time zone is not in the correct format, GMT is used.

formatGmt(dateFormatString)
Returns a Datetime as a string using the supplied Java simple date format and the GMT time zone.

formatLong()
Converts the date to the local time zone and returns the converted date in long date format.

getTime()
Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT represented by this DateTime object.

hour()
Returns the hour component of a Datetime in the local time zone of the context user.

hourGmt()
Returns the hour component of a Datetime in the GMT time zone.

isSameDay(dateToCompare)
Returns true if the Datetime that called the method is the same as the specified Datetime in the local time zone of the context user.

millisecond()
Return the millisecond component of a Datetime in the local time zone of the context user.

millisecondGmt()
Return the millisecond component of a Datetime in the GMT time zone.

minute()
Returns the minute component of a Datetime in the local time zone of the context user.

minuteGmt()
Returns the minute component of a Datetime in the GMT time zone.

month()
Returns the month component of a Datetime in the local time zone of the context user (1=Jan).

monthGmt()
Returns the month component of a Datetime in the GMT time zone (1=Jan).

newInstance(milliseconds)
Constructs a Datetime and initializes it to represent the specified number of milliseconds since January 1, 1970, 00:00:00 GMT.


Apex Reference Guide Datetime Class

newInstance(date, time)
Constructs a DateTime from the specified date and time in the local time zone.

newInstance(year, month, day)
Constructs a Datetime from Integer representations of the specified year, month (1=Jan), and day at midnight in the local time zone.

newInstance(year, month, day, hour, minute, second)
Constructs a Datetime from Integer representations of the specified year, month (1=Jan), day, hour, minute, and second in the local
time zone.

newInstanceGmt(date, time)
Constructs a DateTime from the specified date and time in the GMT time zone.

newInstanceGmt(year, month, date)
Constructs a Datetime from Integer representations of the specified year, month (1=Jan), and day at midnight in the GMT time zone

newInstanceGmt(year, month, date, hour, minute, second)
Constructs a Datetime from Integer representations of the specified year, month (1=Jan), day, hour, minute, and second in the GMT
time zone

now()
Returns the current Datetime based on a GMT calendar.

parse(datetimeString)
Constructs a Datetime from the given String in the local time zone and in the format of the user locale.

second()
Returns the second component of a Datetime in the local time zone of the context user.

secondGmt()
Returns the second component of a Datetime in the GMT time zone.

time()
Returns the time component of a Datetime in the local time zone of the context user.

timeGmt()
Returns the time component of a Datetime in the GMT time zone.

valueOf(dateTimeString)
Returns a Datetime that contains the value of the specified string.

valueOf(fieldValue)
Converts the specified object to a Datetime. Use this method to convert a history tracking field value or an object that represents a
Datetime value.

valueOfGmt(dateTimeString)
Returns a Datetime that contains the value of the specified String.

year()
Returns the year component of a Datetime in the local time zone of the context user.

yearGmt()
Returns the year component of a Datetime in the GMT time zone.

##### addDays(additionalDays)

Adds the specified number of days to a Datetime.


Apex Reference Guide Datetime Class

Signature

```
   public Datetime addDays(Integer additionalDays)

```

Parameters

```
   additionalDays
```

Type: Integer

Return Value

Type: Datetime

Example

```
   Datetime myDateTime = Datetime.newInstance(1960, 2, 17);

   Datetime newDateTime = myDateTime.addDays(2);

   Datetime expected = Datetime.newInstance(1960, 2, 19);

   System.assertEquals(expected, newDateTime);

##### addHours(additionalHours)

```

Adds the specified number of hours to a Datetime.

Signature

```
   public Datetime addHours(Integer additionalHours)

```

Parameters

```
   additionalHours
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime myDateTime = DateTime.newInstance(1997, 1, 31, 7, 8, 16);

   DateTime newDateTime = myDateTime.addHours(3);

   DateTime expected = DateTime.newInstance(1997, 1, 31, 10, 8, 16);

   System.assertEquals(expected, newDateTime);

##### addMinutes(additionalMinutes)

```

Adds the specified number of minutes to a Datetime.

Signature

```
   public Datetime addMinutes(Integer additionalMinutes)

```


Apex Reference Guide Datetime Class

Parameters

```
   additionalMinutes
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime myDateTime = DateTime.newInstance(1999, 2, 11, 8, 6, 16);

   DateTime newDateTime = myDateTime.addMinutes(7);

   DateTime expected = DateTime.newInstance(1999, 2, 11, 8, 13, 16);

   System.assertEquals(expected, newDateTime);

##### addMonths(additionalMonths)

```

Adds the specified number of months to a Datetime.

Signature

```
   public Datetime addMonths(Integer additionalMonths)

```

Parameters

```
   additionalMonths
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime myDateTime = DateTime.newInstance(2000, 7, 7, 7, 8, 12);

   DateTime newDateTime = myDateTime.addMonths(1);

   DateTime expected = DateTime.newInstance(2000, 8, 7, 7, 8, 12);

   System.assertEquals(expected, newDateTime);

##### addSeconds(additionalSeconds)

```

Adds the specified number of seconds to a Datetime.

Signature

```
   public Datetime addSeconds(Integer additionalSeconds)

```


Apex Reference Guide Datetime Class

Parameters

```
   additionalSeconds
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime myDateTime = DateTime.newInstance(2001, 7, 19, 10, 7, 12);

   DateTime newDateTime = myDateTime.addSeconds(4);

   DateTime expected = DateTime.newInstance(2001, 7, 19, 10, 7, 16);

   System.assertEquals(expected, newDateTime);

##### addYears(additionalYears)

```

Adds the specified number of years to a Datetime.

Signature

```
   public Datetime addYears(Integer additionalYears)

```

Parameters

```
   additionalYears
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime myDateTime = DateTime.newInstance(2009, 12, 17, 13, 6, 6);

   DateTime newDateTime = myDateTime.addYears(1);

   DateTime expected = DateTime.newInstance(2010, 12, 17, 13, 6, 6);

   System.assertEquals(expected, newDateTime);

##### date()

```

Returns the Date component of a Datetime in the local time zone of the context user.

Signature

```
   public Date date()

```

Return Value

Type: Date


Apex Reference Guide Datetime Class

Example

```
   DateTime myDateTime = DateTime.newInstance(2006, 3, 16, 12, 6, 13);

   Date myDate = myDateTime.date();

   Date expected = Date.newInstance(2006, 3, 16);

   System.assertEquals(expected, myDate);

##### dateGMT()

```

Return the Date component of a Datetime in the GMT time zone.

Signature

```
   public Date dateGMT()

```

Return Value

Type: Date

Example

```
   // California local time, PST

   DateTime myDateTime = DateTime.newInstance(2006, 3, 16, 23, 0, 0);

   Date myDate = myDateTime.dateGMT();

   Date expected = Date.newInstance(2006, 3, 17);

   System.assertEquals(expected, myDate);

##### day()

```

Returns the day-of-month component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer day()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(1986, 2, 21, 23, 0, 0);

   System.assertEquals(21, myDateTime.day());

##### dayGmt()

```

Returns the day-of-month component of a Datetime in the GMT time zone.

Signature

```
   public Integer dayGmt()

```


Apex Reference Guide Datetime Class

Return Value

Type: Integer

Example

```
   // California local time, PST

   DateTime myDateTime = DateTime.newInstance(1987, 1, 14, 23, 0, 3);

   System.assertEquals(15, myDateTime.dayGMT());

##### dayOfYear()

```

Returns the day-of-year component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer dayOfYear()

```

Return Value

Type: Integer

Example

For example, February 5, 2008 08:30:12 would be day 36.

```
   Datetime myDate = Datetime.newInstance(2008, 2, 5, 8, 30, 12);

   system.assertEquals(myDate.dayOfYear(), 36);

##### dayOfYearGmt()

```

Returns the day-of-year component of a Datetime in the GMT time zone.

Signature

```
   public Integer dayOfYearGmt()

```

Return Value

Type: Integer

Example

```
   // This sample assumes we are in the PST timezone

   DateTime myDateTime = DateTime.newInstance(1999, 2, 5, 23, 0, 3);

   // January has 31 days + 5 days in February = 36 days

   // dayOfYearGmt() adjusts the time zone from the current time zone to GMT

   // by adding 8 hours to the PST time zone, so it's 37 days and not 36 days

   System.assertEquals(37, myDateTime.dayOfYearGmt());

```


Apex Reference Guide Datetime Class

##### format()

Converts the date to the local time zone and returns the converted date as a formatted string using the locale of the context user. If the
time zone cannot be determined, GMT is used.

Signature

```
   public String format()

```

Return Value

Type: String

Example

Note: The sample is executed in an org where the “Enable ICU Locale Formats” crucial update is enabled. See
[https://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_forcecom_globalization_enable_icu_cruc.htm.](https://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_forcecom_globalization_enable_icu_cruc.htm)

```
   DateTime.myDateTime = DateTime.newInstance(1993, 6, 6, 3, 3, 3);

   system.assertEquals('6/6/1993, 3:03 AM', mydatetime.format());

##### format(dateFormatString)

```

Converts the date to the local time zone and returns the converted date as a string using the supplied Java simple date format. If the
time zone cannot be determined, GMT is used.

Signature

```
   public String format(String dateFormatString)

```

Parameters

```
   dateFormatString
```

Type: String

Return Value

Type: String

Usage

[For more information on the Java simple date format, see Java SimpleDateFormat.](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)

Example

```
   Datetime myDT = DateTime.newInstance(2022, 5, 4, 19, 37, 55);

   String myDate = myDT.format('yyyy-MM-dd h:mm a');

   String expected = '2022-05-04 7:37 PM';

   System.assertEquals(expected, myDate);

```


Apex Reference Guide Datetime Class

##### format(dateFormatString, timezone)

Converts the date to the specified time zone and returns the converted date as a string using the supplied Java simple date format. If
the supplied time zone is not in the correct format, GMT is used.

Signature

```
   public String format(String dateFormatString, String timezone)

```

Parameters

```
   dateFormatString
```

Type: String

```
   timezone
```

Type: String

Valid time zone values for the _`timezone`_ argument are the time zones of the Java TimeZone class that correspond to the time
[zones returned by the TimeZone.getAvailableIDs method in Java. We recommend you use full time zone names, not the three-letter](http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html#getAvailableIDs())
abbreviations.

Return Value

Type: String

Usage

[For more information on the Java simple date format, see Java SimpleDateFormat.](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)

Example

##### This example uses format to convert a GMT date to the America/New_York time zone and formats the date using the specified date

format.

```
   Datetime GMTDate =

     Datetime.newInstanceGmt(2011,6,1,12,1,5);

   String strConvertedDate =

     GMTDate.format('MM/dd/yyyy HH:mm:ss',

              'America/New_York');

   // Date is converted to

   // the new time zone and is adjusted

   // for daylight saving time.

   System.assertEquals(

     '06/01/2011 08:01:05', strConvertedDate);

##### formatGmt(dateFormatString)

```

Returns a Datetime as a string using the supplied Java simple date format and the GMT time zone.

Signature

```
   public String formatGmt(String dateFormatString)

```


Apex Reference Guide Datetime Class

Parameters

```
   dateFormatString
```

Type: String

Return Value

Type: String

Usage

[For more information on the Java simple date format, see Java SimpleDateFormat.](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)

Example

```
   DateTime myDateTime = DateTime.newInstance(1993, 6, 6, 3, 3, 3);

   String formatted = myDateTime.formatGMT('EEE, MMM d yyyy HH:mm:ss');

   String expected = 'Sun, Jun 6 1993 10:03:03';

   System.assertEquals(expected, formatted);

##### formatLong()

```

Converts the date to the local time zone and returns the converted date in long date format.

Signature

```
   public String formatLong()

```

Return Value

Type: String

Example

```
   // Passing local date based on the PST time zone

   Datetime dt = DateTime.newInstance(2012,12,28,10,0,0);

   // Writes 12/28/2012 10:00:00 AM PST

   System.debug('dt.formatLong()=' + dt.formatLong());

##### getTime()

```

Returns the number of milliseconds since January 1, 1970, 00:00:00 GMT represented by this DateTime object.

Signature

```
   public Long getTime()

```

Return Value

Type: Long


Apex Reference Guide Datetime Class

Example

```
   DateTime dt = DateTime.newInstanceGMT(2007, 6, 23, 3, 3, 3);

   Long gettime = dt.getTime();

   Long expected = 1182567783000L;

   System.assertEquals(expected, gettime);

##### hour()

```

Returns the hour component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer hour()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(1998, 11, 21, 3, 3, 3);

   System.assertEquals(3, myDateTime.hour());

##### hourGmt()

```

Returns the hour component of a Datetime in the GMT time zone.

Signature

```
   public Integer hourGmt()

```

Return Value

Type: Integer

Example

```
   // California local time

   DateTime myDateTime = DateTime.newInstance(2000, 4, 27, 3, 3, 3);

   System.assertEquals(10, myDateTime.hourGMT());

##### isSameDay(dateToCompare)

```

Returns true if the Datetime that called the method is the same as the specified Datetime in the local time zone of the context user.

Signature

```
   public Boolean isSameDay(Datetime dateToCompare)

```


Apex Reference Guide Datetime Class

Parameters

```
   dateToCompare
```

Type: Datetime

Return Value

Type: Boolean

Example

```
   datetime myDate = datetime.now();

   datetime dueDate =

      datetime.newInstance(2008, 1, 30);

   boolean dueNow = myDate.isSameDay(dueDate);

##### millisecond()

```

Return the millisecond component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer millisecond()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.now();

   system.debug(myDateTime.millisecond());

##### millisecondGmt()

```

Return the millisecond component of a Datetime in the GMT time zone.

Signature

```
   public Integer millisecondGmt()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.now();

   system.debug(myDateTime.millisecondGMT());

```


Apex Reference Guide Datetime Class

##### minute()

Returns the minute component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer minute()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(2001, 2, 27, 3, 3, 3);

   system.assertEquals(3, myDateTime.minute());

##### minuteGmt()

```

Returns the minute component of a Datetime in the GMT time zone.

Signature

```
   public Integer minuteGmt()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(2002, 12, 3, 3, 3, 3);

   system.assertEquals(3, myDateTime.minuteGMT());

##### month()

```

Returns the month component of a Datetime in the local time zone of the context user (1=Jan).

Signature

```
   public Integer month()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(2004, 11, 4, 3, 3, 3);

   system.assertEquals(11, myDateTime.month());

```


Apex Reference Guide Datetime Class

##### monthGmt()

Returns the month component of a Datetime in the GMT time zone (1=Jan).

Signature

```
   public Integer monthGmt()

```

Return Value

Type: Integer

Example

```
   DateTime myDateTime = DateTime.newInstance(2006, 11, 19, 3, 3, 3);

   system.assertEquals(11, myDateTime.monthGMT());

##### newInstance(milliseconds)

```

Constructs a Datetime and initializes it to represent the specified number of milliseconds since January 1, 1970, 00:00:00 GMT.

Signature

```
   public static Datetime newInstance(Long milliseconds)

```

Parameters

```
   milliseconds
```

Type: Long

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Example

```
   Long longtime = 1341828183000L;

   DateTime dt = DateTime.newInstance(longtime);

   DateTime expected = DateTime.newInstance(2012, 7, 09, 3, 3, 3);

   System.assertEquals(expected, dt);

##### newInstance(date, time)

```

Constructs a DateTime from the specified date and time in the local time zone.

Signature

```
   public static Datetime newInstance(Date date, Time time)

```


Apex Reference Guide Datetime Class

Parameters

```
   date
```

Type: Date

```
   time
```

Type: Time

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Example

```
   Date myDate = Date.newInstance(2011, 11, 18);

   Time myTime = Time.newInstance(3, 3, 3, 0);

   DateTime dt = DateTime.newInstance(myDate, myTime);

   DateTime expected = DateTime.newInstance(2011, 11, 18, 3, 3, 3);

   System.assertEquals(expected, dt);

##### newInstance(year, month, day)

```

Constructs a Datetime from Integer representations of the specified year, month (1=Jan), and day at midnight in the local time zone.

Signature

```
   public static Datetime newInstance(Integer year, Integer month, Integer day)

```

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

```
   day
```

Type: Integer

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Example

```
   datetime myDate = datetime.newInstance(2008, 12, 1);

```


Apex Reference Guide Datetime Class

##### newInstance(year, month, day, hour, minute, second)

Constructs a Datetime from Integer representations of the specified year, month (1=Jan), day, hour, minute, and second in the local time
zone.

Signature

```
   public static Datetime newInstance(Integer year, Integer month, Integer day, Integer

   hour, Integer minute, Integer second)

```

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

```
   day
```

Type: Integer

```
   hour
```

Type: Integer

```
   minute
```

Type: Integer

```
   second
```

Type: Integer

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Example

```
   Datetime myDate = Datetime.newInstance(2008, 12, 1, 12, 30, 2);

##### newInstanceGmt(date, time)

```

Constructs a DateTime from the specified date and time in the GMT time zone.

Signature

```
   public static Datetime newInstanceGmt(Date date, Time time)

```

Parameters

```
   date
```

Type: Date

```
   time
```

Type: Time


Apex Reference Guide Datetime Class

Return Value

Type: Datetime

Example

```
   Date myDate = Date.newInstance(2013, 11, 12);

   Time myTime = Time.newInstance(3, 3, 3, 0);

   DateTime dt = DateTime.newInstanceGMT(myDate, myTime);

   DateTime expected = DateTime.newInstanceGMT(2013, 11, 12, 3, 3, 3);

   System.assertEquals(expected, dt);

##### newInstanceGmt(year, month, date)

```

Constructs a Datetime from Integer representations of the specified year, month (1=Jan), and day at midnight in the GMT time zone

Signature

```
   public static Datetime newInstanceGmt(Integer year, Integer month, Integer date)

```

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

```
   date
```

Type: Integer

Return Value

Type: Datetime

Example

```
   DateTime dt = DateTime.newInstanceGMT(1996, 3, 22);

##### newInstanceGmt(year, month, date, hour, minute, second)

```

Constructs a Datetime from Integer representations of the specified year, month (1=Jan), day, hour, minute, and second in the GMT
time zone

Signature

```
   public static Datetime newInstanceGmt(Integer year, Integer month, Integer date, Integer

   hour, Integer minute, Integer second)

```


Apex Reference Guide Datetime Class

Parameters

```
   year
```

Type: Integer

```
   month
```

Type: Integer

```
   date
```

Type: Integer

```
   hour
```

Type: Integer

```
   minute
```

Type: Integer

```
   second
```

Type: Integer

Return Value

Type: Datetime

Example

```
   //California local time

   DateTime dt = DateTime.newInstanceGMT(1998, 1, 29, 2, 2, 3);

   DateTime expected = DateTime.newInstance(1998, 1, 28, 18, 2, 3);

   System.assertEquals(expected, dt);

##### now()

```

Returns the current Datetime based on a GMT calendar.

Signature

```
   public static Datetime now()

```

Return Value

Type: Datetime

The format of the returned datetime is: `'MM/DD/YYYY HH:MM PERIOD'`

Example

```
   datetime myDateTime = datetime.now();

##### parse(datetimeString)

```

Constructs a Datetime from the given String in the local time zone and in the format of the user locale.


Apex Reference Guide Datetime Class

Signature

```
   public static Datetime parse(String datetimeString)

```

Parameters

```
   datetimeString
```

Type: String

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Example

This example uses `parse` to create a Datetime from a date passed in as a string and that is formatted for the English (United States)
locale. You may need to change the format of the date string if you have a different locale.

Note: This sample is executed in an org where the “Enable ICU Locale Formats” crucial update is enabled. See
[https://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_forcecom_globalization_enable_icu_cruc.htm.](https://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_forcecom_globalization_enable_icu_cruc.htm)

```
   Datetime dt = DateTime.parse('10/14/2011, 11:46 AM');

   String myDtString = dt.format();

   system.assertEquals(myDtString, '10/14/2011, 11:46 AM');

##### second()

```

Returns the second component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer second()

```

Return Value

Type: Integer

Example

```
   DateTime dt = DateTime.newInstanceGMT(1999, 9, 22, 3, 1, 2);

   System.assertEquals(2, dt.second());

##### secondGmt()

```

Returns the second component of a Datetime in the GMT time zone.

Signature

```
   public Integer secondGmt()

```


Apex Reference Guide Datetime Class

Return Value

Type: Integer

Example

```
   DateTime dt = DateTime.newInstance(2000, 2, 3, 3, 1, 5);

   System.assertEquals(5, dt.secondGMT());

##### time()

```

Returns the time component of a Datetime in the local time zone of the context user.

Signature

```
   public Time time()

```

Return Value

Type: Time

Example

```
   DateTime dt = DateTime.newInstance(2002, 11, 21, 0, 2, 2);

   Time expected = Time.newInstance(0, 2, 2, 0);

   System.assertEquals(expected, dt.time());

##### timeGmt()

```

Returns the time component of a Datetime in the GMT time zone.

Signature

```
   public Time timeGmt()

```

Return Value

Type: Time

Example

```
   // This sample is based on the PST time zone

   DateTime dt = DateTime.newInstance(2004, 1, 27, 4, 1, 2);

   Time expected = Time.newInstance(12, 1, 2, 0);

   // 8 hours are added to the time to convert it from

   // PST to GMT

   System.assertEquals(expected, dt.timeGMT());

##### valueOf(dateTimeString)

```

Returns a Datetime that contains the value of the specified string.


Apex Reference Guide Datetime Class

Signature

```
   public static Datetime valueOf(String dateTimeString)

```

Parameters

```
   dateTimeString
```

Type: String

Return Value

Type: Datetime

The returned date is in the GMT time zone.

Usage

The specified string should use the standard date format “yyyy-MM-dd HH:mm:ss” in the local time zone.

Example

```
   string year = '2008';

   string month = '10';

   string day = '5';

   string hour = '12';

   string minute = '20';

   string second = '20';

   string stringDate = year + '-' + month + '-' + day + ' ' + hour + ':'

      + minute + ':' + second;

   Datetime myDate = Datetime.valueOf(stringDate);

##### valueOf(fieldValue)

```

Converts the specified object to a Datetime. Use this method to convert a history tracking field value or an object that represents a
Datetime value.

Signature

```
   public static Datetime valueOf(Object fieldValue)

```

Parameters

```
   fieldValue
```

Type: Object

Return Value

Type: Datetime


Apex Reference Guide Datetime Class

Usage

Use this method with the `OldValue` or `NewValue` fields of history sObjects, such as `AccountHistory`, when the field is a
Date/Time field.

Example

```
   List<AccountHistory> ahlist = [SELECT Field,OldValue,NewValue FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'MyDatetime__c') {

      Datetime oldValue = Datetime.valueOf(ah.OldValue);

      Datetime newValue = Datetime.valueOf(ah.NewValue);

     }

   }

##### valueOfGmt(dateTimeString)

```

Returns a Datetime that contains the value of the specified String.

Signature

```
   public static Datetime valueOfGmt(String dateTimeString)

```

Parameters

```
   dateTimeString
```

Type: String

Return Value

Type: Datetime

Usage

The specified string should use the standard date format “yyyy-MM-dd HH:mm:ss” in the GMT time zone.

Example

```
   // California locale time

   string year = '2009';

   string month = '3';

   string day = '5';

   string hour = '5';

   string minute = '2';

   string second = '2';

   string stringDate = year + '-' + month + '-' + day + ' ' + hour + ':'

      + minute + ':' + second;

   Datetime myDate = Datetime.valueOfGMT(stringDate);

```


### Apex Reference Guide Decimal Class

```
   DateTime expected = DateTime.newInstance(2009, 3, 4, 21, 2, 2);

   System.assertEquals(expected, myDate);

##### year()

```

Returns the year component of a Datetime in the local time zone of the context user.

Signature

```
   public Integer year()

```

Return Value

Type: Integer

Example

```
   DateTime dt = DateTime.newInstance(2012, 1, 26, 5, 2, 4);

   System.assertEquals(2012, dt.year());

##### yearGmt()

```

Returns the year component of a Datetime in the GMT time zone.

Signature

```
   public Integer yearGmt()

```

Return Value

Type: Integer

Example

```
   DateTime dt = DateTime.newInstance(2012, 10, 4, 6, 4, 6);

   System.assertEquals(2012, dt.yearGMT());

### Decimal Class

```

Contains methods for the Decimal primitive data type.

Namespace

System

Usage

Note: Two Decimal objects that are numerically equivalent but differ in scale (such as 1.1 and 1.10) generally do not have the
same hashcode. Use caution when such Decimal objects are used in Sets or as Map keys.


Apex Reference Guide Decimal Class

[For more information on Decimal, see Decimal Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

IN THIS SECTION:

#### Rounding Mode

Rounding mode specifies the rounding behavior for numerical operations capable of discarding precision.

Decimal Methods

#### Rounding Mode

Rounding mode specifies the rounding behavior for numerical operations capable of discarding precision.

Each rounding mode indicates how the least significant returned digit of a rounded result is to be calculated. The following are the valid
values for _`roundingMode`_ .

**Name** **Description**

```
CEILING

DOWN

```

Rounds towards positive infinity. That is, if the result is positive, this mode behaves the same as
the `UP` rounding mode; if the result is negative, it behaves the same as the `DOWN` rounding
mode. Note that this rounding mode never decreases the calculated value. For example:

**•** Input number 5.5: `CEILING` round mode result: 6

**•** Input number 1.1: `CEILING` round mode result: 2

**•** Input number -1.1: `CEILING` round mode result: -1

**•** Input number -2.7: `CEILING` round mode result: -2

```
Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

Long[] expected = new Long[]{6, 2, -1, -2};

for(integer x = 0; x < example.size(); x++){

   System.assertEquals(expected[x],

     example[x].round(System.RoundingMode.CEILING));

}

```

Rounds towards zero. This rounding mode always discards any fractions (decimal points) prior
to executing. Note that this rounding mode never increases the magnitude of the calculated
value. For example:

**•** Input number 5.5: `DOWN` round mode result: 5

**•** Input number 1.1: `DOWN` round mode result: 1

**•** Input number -1.1: `DOWN` round mode result: -1

**•** Input number -2.7: `DOWN` round mode result: -2

```
Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

Long[] expected = new Long[]{5, 1, -1, -2};

for(integer x = 0; x < example.size(); x++){

   System.assertEquals(expected[x],

     example[x].round(System.RoundingMode.DOWN));

}

```


Apex Reference Guide Decimal Class

**Name** **Description**

```
FLOOR

```

Rounds towards negative infinity. That is, if the result is positive, this mode behaves the same as
the `DOWN` rounding mode; if negative, this mode behaves the same as the `UP` rounding mode.
Note that this rounding mode never increases the calculated value. For example:

**•** Input number 5.5: `FLOOR` round mode result: 5

**•** Input number 1.1: `FLOOR` round mode result: 1

**•** Input number -1.1: `FLOOR` round mode result: -2

**•** Input number -2.7: `FLOOR` round mode result: -3

```
Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

Long[] expected = new Long[]{5, 1, -2, -3};

for(integer x = 0; x < example.size(); x++){

   System.assertEquals(expected[x],

     example[x].round(System.RoundingMode.FLOOR));

}

```

`HALF_DOWN` Rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case
this mode rounds down. This rounding mode behaves the same as the `UP` rounding mode if

the discarded fraction (decimal point) is > 0.5; otherwise, it behaves the same as `DOWN` rounding
mode. For example:

**•** Input number 5.5: `HALF_DOWN` round mode result: 5

**•** Input number 1.1: `HALF_DOWN` round mode result: 1

**•** Input number -1.1: `HALF_DOWN` round mode result: -1

**•** Input number -2.7: `HALF_DOWN` round mode result: -3

```
               Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

               Long[] expected = new Long[]{5, 1, -1, -3};

               for(integer x = 0; x < example.size(); x++){

                  System.assertEquals(expected[x],

                    example[x].round(System.RoundingMode.HALF_DOWN));

               }

```

`HALF_EVEN` Rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case,
this mode rounds towards the even neighbor. This rounding mode behaves the same as the

`HALF_UP` rounding mode if the digit to the left of the discarded fraction (decimal point) is
odd. It behaves the same as the `HALF_DOWN` rounding method if it is even. For example:

**•** Input number 5.5: `HALF_EVEN` round mode result: 6

**•** Input number 1.1: `HALF_EVEN` round mode result: 1

**•** Input number -1.1: `HALF_EVEN` round mode result: -1

**•** Input number -2.7: `HALF_EVEN` round mode result: -3


Apex Reference Guide Decimal Class

**Name** **Description**

Note that this rounding mode statistically minimizes cumulative error when applied repeatedly
over a sequence of calculations.

`HALF_UP` Rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case,
this mode rounds up. This rounding method behaves the same as the `UP` rounding method if

the discarded fraction (decimal point) is >= 0.5; otherwise, this rounding method behaves the
same as the `DOWN` rounding method. For example:

**•** Input number 5.5: `HALF_UP` round mode result: 6

**•** Input number 1.1: `HALF_UP` round mode result: 1

**•** Input number -1.1: `HALF_UP` round mode result: -1

**•** Input number -2.7: `HALF_UP` round mode result: -3

```
                   Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

                   Long[] expected = new Long[]{6, 1, -1, -3};

                   for(integer x = 0; x < example.size(); x++){

                     System.assertEquals(expected[x],

                        example[x].round(System.RoundingMode.HALF_UP));

                   }

```

```
UNNECESSARY

UP

```

Asserts that the requested operation has an exact result, which means that no rounding is
necessary. If this rounding mode is specified on an operation that yields an inexact result, a
MathException is thrown. For example:

**•** Input number 5.5: `UNNECESSARY` round mode result: MathException

**•** Input number 1.1: `UNNECESSARY` round mode result: MathException

**•** Input number 1.0: `UNNECESSARY` round mode result: 1

**•** Input number -1.0: `UNNECESSARY` round mode result: -1

**•** Input number -2.2: `UNNECESSARY` round mode result: MathException

```
Decimal example1 = 5.5;

Decimal example2 = 1.0;

system.assertEquals(1,

   example2.round(System.RoundingMode.UNNECESSARY));

try{

   example1.round(System.RoundingMode.UNNECESSARY);

} catch(Exception E) {

  system.assertEquals('System.MathException', E.getTypeName());

}

```

Rounds away from zero. This rounding mode always truncates any fractions (decimal points)
prior to executing. Note that this rounding mode never decreases the magnitude of the calculated
value. For example:

**•** Input number 5.5: `UP` round mode result: 6

**•** Input number 1.1: `UP` round mode result: 2

**•** Input number -1.1: `UP` round mode result: -2


Apex Reference Guide Decimal Class

**Name** **Description**

**•** Input number -2.7: `UP` round mode result: -3

```
                   Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

                   Long[] expected = new Long[]{6, 2, -2, -3};

                   for(integer x = 0; x < example.size(); x++){

                     System.assertEquals(expected[x],

                        example[x].round(System.RoundingMode.UP));

                   }

#### Decimal Methods The following are methods for Decimal .

```

IN THIS SECTION:

abs()
Returns the absolute value of the Decimal.

divide(divisor, scale)
Divides this Decimal by the specified divisor, and sets the scale, that is, the number of decimal places, of the result using the specified
scale.

divide(divisor, scale, roundingMode)
Divides this Decimal by the specified divisor, sets the scale, that is, the number of decimal places, of the result using the specified
scale, and if necessary, rounds the value using the rounding mode.

doubleValue()
Returns the Double value of this Decimal.

format()
Returns the String value of this Decimal using the locale of the context user.

intValue()
Returns the Integer value of this Decimal.

longValue()
Returns the Long value of this Decimal.

pow(exponent)
Returns the value of this decimal raised to the power of the specified exponent.

precision()
Returns the total number of digits for the Decimal.

round()
Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards
the even neighbor.

round(roundingMode)
Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using the rounding mode
specified by the rounding mode.


Apex Reference Guide Decimal Class

scale()
Returns the scale of the Decimal, that is, the number of decimal places.

setScale(scale)
Returns the Decimal scaled to the specified number of decimal places, using half-even rounding, if necessary. Half-even rounding
mode rounds toward the “nearest neighbor.” If both neighbors are equidistant, the number is rounded toward the even neighbor.

setScale(scale, roundingMode)
Returns the Decimal scaled to the specified number of decimal places, using the specified rounding mode, if necessary.

stripTrailingZeros()
Returns the Decimal with any trailing zeros removed.

toPlainString()
Returns the String value of this Decimal, without using scientific notation.

valueOf(doubleToDecimal)
Returns a Decimal that contains the value of the specified Double.

valueOf(longToDecimal)
Returns a Decimal that contains the value of the specified Long.

valueOf(stringToDecimal)
Returns a Decimal that contains the value of the specified String. As in Java, the string is interpreted as representing a signed Decimal.

##### abs()

Returns the absolute value of the Decimal.

Signature

```
   public Decimal abs()

```

Return Value

Type: Decimal

Example

```
   Decimal myDecimal = -6.02214129;

   System.assertEquals(6.02214129, myDecimal.abs());

##### divide(divisor, scale)

```

Divides this Decimal by the specified divisor, and sets the scale, that is, the number of decimal places, of the result using the specified
scale.

Signature

```
   public Decimal divide(Decimal divisor, Integer scale)

```


Apex Reference Guide Decimal Class

Parameters

```
   divisor
```

Type: Decimal

```
   scale
```

Type: Integer

Return Value

Type: Decimal

Example

```
   Decimal decimalNumber = 19;

   Decimal result = decimalNumber.divide(100, 3);

   System.assertEquals(0.190, result);

##### divide(divisor, scale, roundingMode)

```

Divides this Decimal by the specified divisor, sets the scale, that is, the number of decimal places, of the result using the specified scale,
and if necessary, rounds the value using the rounding mode.

Signature

```
   public Decimal divide(Decimal divisor, Integer scale, System.RoundingMode roundingMode)

```

Parameters

```
   divisor
```

Type: Decimal

```
   scale
```

Type: Integer

```
   roundingMode
```

Type: System.RoundingMode

Return Value

Type: Decimal

Example

```
   Decimal myDecimal = 12.4567;

   Decimal divDec = myDecimal.divide(7, 2, System.RoundingMode.UP);

   System.assertEquals(divDec, 1.78);

##### doubleValue()

```

Returns the Double value of this Decimal.


Apex Reference Guide Decimal Class

Signature

```
   public Double doubleValue()

```

Return Value

Type: Double

Example

```
   Decimal myDecimal = 6.62606957;

   Double value = myDecimal.doubleValue();

   System.assertEquals(6.62606957, value);

##### format()

```

Returns the String value of this Decimal using the locale of the context user.

Signature

```
   public String format()

```

Return Value

Type: String

Usage

Scientific notation will be used if an exponent is needed.

Example

```
   // U.S. locale

   Decimal myDecimal = 12345.6789;

   system.assertEquals('12,345.679', myDecimal.format());

##### intValue()

```

Returns the Integer value of this Decimal.

Signature

```
   public Integer intValue()

```

Return Value

Type: Integer


Apex Reference Guide Decimal Class

Example

```
   Decimal myDecimal = 1.602176565;

   system.assertEquals(1, myDecimal.intValue());

##### longValue()

```

Returns the Long value of this Decimal.

Signature

```
   public Long longValue()

```

Return Value

Type: Long

Example

```
   Decimal myDecimal = 376.730313461;

   system.assertEquals(376, myDecimal.longValue());

##### pow(exponent)

```

Returns the value of this decimal raised to the power of the specified exponent.

Signature

```
   public Decimal pow(Integer exponent)

```

Parameters

```
   exponent
```

Type: Integer

The value of _`exponent`_ must be between 0 and 32,767.

Return Value

Type: Decimal

Usage

If you use `MyDecimal.pow(0)`, 1 is returned.

The `Math.pow` method does accept negative values.

Example

```
   Decimal myDecimal = 4.12;

   Decimal powDec = myDecimal.pow(2);

   System.assertEquals(powDec, 16.9744);

```


Apex Reference Guide Decimal Class

##### precision()

Returns the total number of digits for the Decimal.

Signature

```
   public Integer precision()

```

Return Value

Type: Integer

Example

##### For example, if the Decimal value was 123.45, precision returns 5. If the Decimal value is 123.123, precision returns 6.

```
   Decimal D1 = 123.45;

   Integer precision1 = D1.precision();

   system.assertEquals(precision1, 5);

   Decimal D2 = 123.123;

   Integer precision2 = D2.precision();

   system.assertEquals(precision2, 6);

##### round()

```

Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards the
even neighbor.

Signature

```
   public Long round()

```

Return Value

Type: Long

Usage

Note that this rounding mode statistically minimizes cumulative error when applied repeatedly over a sequence of calculations.

Example

```
   Decimal D = 4.5;

   Long L = D.round();

   System.assertEquals(4, L);

   Decimal D1 = 5.5;

   Long L1 = D1.round();

   System.assertEquals(6, L1);

   Decimal D2 = 5.2;

```


Apex Reference Guide Decimal Class

```
   Long L2 = D2.round();

   System.assertEquals(5, L2);

   Decimal D3 = -5.7;

   Long L3 = D3.round();

   System.assertEquals(-6, L3);

##### round(roundingMode)

```

Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using the rounding mode specified
by the rounding mode.

Signature

```
   public Long round(System.RoundingMode roundingMode)

```

Parameters

```
   roundingMode
```

Type: System.RoundingMode

Return Value

Type: Long

##### scale()

Returns the scale of the Decimal, that is, the number of decimal places.

Signature

```
   public Integer scale()

```

Return Value

Type: Integer

Example

```
   Decimal myDecimal = 9.27400968;

   system.assertEquals(8, myDecimal.scale());

##### setScale(scale)

```

Returns the Decimal scaled to the specified number of decimal places, using half-even rounding, if necessary. Half-even rounding mode
rounds toward the “nearest neighbor.” If both neighbors are equidistant, the number is rounded toward the even neighbor.

Signature

```
   public Decimal setScale(Integer scale)

```


Apex Reference Guide Decimal Class

Parameters

```
   scale
```

Type: Integer

The value of _`scale`_ must be between –33 and 33. If the value of _`scale`_ is negative, your unscaled value is multiplied by 10 to
the power of the negation of _`scale`_ . For example, after this operation, the value of _`d`_ is `4*10^3` .

```
     Decimal d = 4000;

     d = d.setScale(-3);

```

Return Value

Type: Decimal

Usage

If you do not explicitly set the scale for a Decimal, the item from which the Decimal is created determines the scale.

**•** If the Decimal is created as part of a query, the scale is based on the scale of the field returned from the query.

**•** If the Decimal is created from a String, the scale is the number of characters after the decimal point of the String.

**•** If the Decimal is created from a non-decimal number, the number is first converted to a String. The scale is then set using the number
of characters after the decimal point.

Example

```
   Decimal myDecimal = 8.987551787;

   Decimal setScaled = myDecimal.setscale(3);

   System.assertEquals(8.988, setScaled);

##### setScale(scale, roundingMode)

```

Returns the Decimal scaled to the specified number of decimal places, using the specified rounding mode, if necessary.

Signature

```
   public Decimal setScale(Integer scale, System.RoundingMode roundingMode)

```

Parameters

```
   scale
```

Type: Integer

The value of _`scale`_ must be between –33 and 33. If the value of _`scale`_ is negative, your unscaled value is multiplied by 10 to
the power of the negation of _`scale`_ . For example, after this operation, the value of _`d`_ is `4*10^3` .

```
     Decimal d = 4000;

     d = d.setScale(-3);

   roundingMode
```

Type: System.RoundingMode


Apex Reference Guide Decimal Class

Return Value

Type: Decimal

Usage

If you do not explicitly set the scale for a Decimal, the item from which the Decimal is created determines the scale.

**•** If the Decimal is created as part of a query, the scale is based on the scale of the field returned from the query.

**•** If the Decimal is created from a String, the scale is the number of characters after the decimal point of the String.

**•** If the Decimal is created from a non-decimal number, the number is first converted to a String. The scale is then set using the number
of characters after the decimal point.

##### stripTrailingZeros()

Returns the Decimal with any trailing zeros removed.

Signature

```
   public Decimal stripTrailingZeros()

```

Return Value

Type: Decimal

Example

```
   Decimal myDecimal = 1.10000;

   Decimal stripped = myDecimal.stripTrailingZeros();

   System.assertEquals(stripped, 1.1);

##### toPlainString()

```

Returns the String value of this Decimal, without using scientific notation.

Signature

```
   public String toPlainString()

```

Return Value

Type: String

Example

```
   Decimal myDecimal = 12345.6789;

   System.assertEquals('12345.6789', myDecimal.toPlainString());

##### valueOf(doubleToDecimal)

```

Returns a Decimal that contains the value of the specified Double.


Apex Reference Guide Decimal Class

Signature

```
   public static Decimal valueOf(Double doubleToDecimal)

```

Parameters

```
   doubleToDecimal
```

Type: Double

Return Value

Type: Decimal

Example

```
   Double myDouble = 2.718281828459045;

   Decimal myDecimal = Decimal.valueOf(myDouble);

   System.assertEquals(2.718281828459045, myDecimal);

##### valueOf(longToDecimal)

```

Returns a Decimal that contains the value of the specified Long.

Signature

```
   public static Decimal valueOf(Long longToDecimal)

```

Parameters

```
   longToDecimal
```

Type: Long

Return Value

Type: Decimal

Example

```
   Long myLong = 299792458;

   Decimal myDecimal = Decimal.valueOf(myLong);

   System.assertEquals(299792458, myDecimal);

##### valueOf(stringToDecimal)

```

Returns a Decimal that contains the value of the specified String. As in Java, the string is interpreted as representing a signed Decimal.

Signature

```
   public static Decimal valueOf(String stringToDecimal)

```


### Apex Reference Guide Domain Class

Parameters

```
   stringToDecimal
```

Type: String

Return Value

Type: Decimal

Example

```
   String temp = '12.4567';

   Decimal myDecimal = Decimal.valueOf(temp);

### Domain Class

```

Represents an existing domain hosted by Salesforce that serves the org or its content. Contains methods to obtain information about
these domains, such as the domain type, My Domain name, and sandbox name.

Namespace

System

Usage

Use the Domain class to obtain information about the domains that Salesforce hosts for your org. This class only applies to domains
hosted by Salesforce, and can’t be used to generate a new domain.

Example

This code uses the System.DomainParser class to parse a hostname. It then gets the associated domain type.

```
   System.Domain d = DomainParser.parse('mycompany.lightning.force.com');

   String myDomainName = d.getMyDomainName();

   System.DomainType domainType = d.getDomainType();

```

IN THIS SECTION:

#### Domain Methods Domain Methods

### The following are methods for Domain .

IN THIS SECTION:

getDomainType()
Returns the domain’s type, such as `CONTENT_DOMAIN`, `EXPERIENCE_CLOUD_SITES_DOMAIN`, or `LIGHTNING_DOMAIN` .


Apex Reference Guide Domain Class

##### getMyDomainName()

Returns the domain’s My Domain name.

##### getPackageName()

For a domain that includes the package name, such as a Lightning Component domain or Visualforce page domain, returns the
package name. For a domain that doesn’t contain a package name, this method returns `null` .

getSandboxName()
For a sandbox org domain, returns the sandbox name. For a production org domain, returns `null` .

getSitesSubdomainName()
[For a system-managed Experience Cloud site domain or Salesforce Site domain, returns the sites subdomain name. If enhanced](https://help.salesforce.com/s/articleView?id=domain_name_enhanced.htm&language=en_US)
[domains are enabled, this method always returns](https://help.salesforce.com/s/articleView?id=domain_name_enhanced.htm&language=en_US) `null` . When enhanced domains are enabled, the org’s My Domain name is the
subdomain for the system-managed domains for Experience Cloud sites and Salesforce Sites domains.

##### **`getDomainType()`**

Returns the domain’s type, such as `CONTENT_DOMAIN`, `EXPERIENCE_CLOUD_SITES_DOMAIN`, or `LIGHTNING_DOMAIN` .

Signature

```
   public System.DomainType getDomainType()

```

Return Value

Type: System.DomainType

##### **`getMyDomainName()`**

Returns the domain’s My Domain name.

Signature

```
   public String getMyDomainName()

```

Return Value

Type: String

##### **`getPackageName()`**

For a domain that includes the package name, such as a Lightning Component domain or Visualforce page domain, returns the package
name. For a domain that doesn’t contain a package name, this method returns `null` .

Signature

```
   public String getPackageName()

```

Return Value

Type: String


### Apex Reference Guide DomainCreator Class

##### **`getSandboxName()`**

For a sandbox org domain, returns the sandbox name. For a production org domain, returns `null` .

Signature

```
   public String getSandboxName()

```

Return Value

Type: String

##### **`getSitesSubdomainName()`**

[For a system-managed Experience Cloud site domain or Salesforce Site domain, returns the sites subdomain name. If enhanced domains](https://help.salesforce.com/s/articleView?id=domain_name_enhanced.htm&language=en_US)
are enabled, this method always returns `null` . When enhanced domains are enabled, the org’s My Domain name is the subdomain
for the system-managed domains for Experience Cloud sites and Salesforce Sites domains.

Signature

```
   public String getSitesSubdomainName()

```

Return Value

Type: String

### DomainCreator Class

Use the DomainCreator class to return a hostname specific to the org. For example, get the org’s Visualforce hostname. Values are
returned as a hostname, such as _**`MyDomainName`**_ `.lightning.force.com` .

Namespace

System

Examples

This example code fetches the org’s My Domain login hostname and the Visualforce hostname for the `uat` package.

```
   //Get the My Domain login hostname

   String myDomainHostname = DomainCreator.getOrgMyDomainHostname();

   //Get the Visualforce hostname

   String vfHostname = DomainCreator.getVisualforceHostname('uat');

```

In this case, in a production org with a My Domain name of `mycompany`, `myDomainHostname` returns
`mycompany.my.salesforce.com` . And in the same production org, `vfHostname` returns
`mycompany--uat.vf.force.com` .


Apex Reference Guide DomainCreator Class

This example code creates a link to a Salesforce Account record. It gets the Lightning hostname associated with this org. It then gets the
Account record ID and uses concatenation to build the link URL.

```
   //Get the org’s Lightning hostname

   String myLightningHostname = DomainCreator.getLightningHostname();

   //Get the ID of a record Account with the name ‘Acme’

   Account acct = [SELECT Id FROM Account WHERE Name = 'Acme' LIMIT 1];

   //Build the URL to view the account record

   String fullRecordURL = 'https://' + myLightningHostname + '/lightning/r/Account/' + acct.Id

    + '/view';

```

IN THIS SECTION:

#### DomainCreator Methods DomainCreator Methods The following are methods for DomainCreator .

IN THIS SECTION:

getContentHostname()
Returns the hostname for content stored in the org, such as files.

getExperienceCloudSitesBuilderHostname()
Returns the hostname to access Experience Builder for the org’s Experience Cloud sites.

getExperienceCloudSitesHostname()
Returns the system-managed hostname for the org’s Experience Cloud sites, such as
_**`ExperienceCloudSitesSubdomainName`**_ `.force.com` . If Digital Experiences aren’t enabled, this method throws an
`InvalidParameterValueException` .

getExperienceCloudSitesLivePreviewHostname()
Returns the hostname to access Experience Builder Live Preview for the org’s Experience Cloud sites.

getExperienceCloudSitesPreviewHostname()
Returns the hostname to access Experience Builder Preview for the org’s Experience Cloud sites.

getLightningContainerComponentHostname(packageName)
Returns the hostname for the org’s Lightning Container Components.

getLightningHostname()
Returns the hostname for the org’s Lightning pages.

getOrgMyDomainHostname()
Returns the hostname for the org’s My Domain login domain.

getSalesforceSitesHostname()
Returns the hostname for the org’s Salesforce Sites. If Salesforce Sites aren’t enabled, this method throws an
`InvalidParameterValueException` .

getSetupHostname()
Returns the hostname for the org’s setup domain, which hosts Setup pages in Salesforce.


Apex Reference Guide DomainCreator Class

getVisualforceHostname(packageName)
Returns the hostname for the org’s Visualforce pages.

##### **`getContentHostname()`**

Returns the hostname for content stored in the org, such as files.

Signature

```
   public static String getContentHostname()

```

Return Value

Type: String

##### **`getExperienceCloudSitesBuilderHostname()`**

Returns the hostname to access Experience Builder for the org’s Experience Cloud sites.

Signature

```
   public static String getExperienceCloudSitesBuilderHostname()

```

Return Value

Type: String

##### **`getExperienceCloudSitesHostname()`**

Returns the system-managed hostname for the org’s Experience Cloud sites, such as
_**`ExperienceCloudSitesSubdomainName`**_ `.force.com` . If Digital Experiences aren’t enabled, this method throws an
`InvalidParameterValueException` .

Signature

```
   public static String getExperienceCloudSitesHostname()

```

Return Value

Type: String

##### **`getExperienceCloudSitesLivePreviewHostname()`**

Returns the hostname to access Experience Builder Live Preview for the org’s Experience Cloud sites.

Signature

```
   public static String getExperienceCloudSitesLivePreviewHostname()

```


Apex Reference Guide DomainCreator Class

Return Value

Type: String

##### **`getExperienceCloudSitesPreviewHostname()`**

Returns the hostname to access Experience Builder Preview for the org’s Experience Cloud sites.

Signature

```
   public static String getExperienceCloudSitesPreviewHostname()

```

Return Value

Type: String

##### **`getLightningContainerComponentHostname(packageName)`**

Returns the hostname for the org’s Lightning Container Components.

Signature

```
   public static String getLightningContainerComponentHostname(String packageName)

```

Parameters

```
   packageName
```

Type: String

The package name for this component.

If packageName is `null`, this method uses the org’s namespace prefix as the package name. Otherwise, it uses the default namespace.

Return Value

Type: String

##### **`getLightningHostname()`**

Returns the hostname for the org’s Lightning pages.

Signature

```
   public static String getLightningHostname()

```

Return Value

Type: String

##### **`getOrgMyDomainHostname()`**

Returns the hostname for the org’s My Domain login domain.


Apex Reference Guide DomainCreator Class

Signature

```
   public static String getOrgMyDomainHostname()

```

Return Value

Type: String

##### **`getSalesforceSitesHostname()`**

Returns the hostname for the org’s Salesforce Sites. If Salesforce Sites aren’t enabled, this method throws an
`InvalidParameterValueException` .

Signature

```
   public static String getSalesforceSitesHostname()

```

Return Value

Type: String

##### **`getSetupHostname()`**

Returns the hostname for the org’s setup domain, which hosts Setup pages in Salesforce.

Signature

```
   public static String getSetupHostname()

```

Return Value

Type: String

##### **`getVisualforceHostname(packageName)`**

Returns the hostname for the org’s Visualforce pages.

Signature

```
   public static String getVisualforceHostname(String packageName)

```

Parameters

```
   packageName
```

Type: String

The package name for this component.

If packageName is `null`, this method uses the org’s namespace prefix as the package name. Otherwise, it uses the default namespace.

Return Value

Type: String


### Apex Reference Guide DomainParser Class DomainParser Class

Use the DomainParser class to parse a domain that Salesforce hosts for the org and extract information about the domain.

Namespace

System

Examples

This example code parses the org’s Lightning domain and gets the My Domain name and domain type from the `System.Domain`
object.

```
   System.Domain d = DomainParser.parse('mycompany.lightning.force.com');

   String myDomainName = d.getMyDomainName();

   System.DomainType domainType = d.getDomainType();

```

This example code parses a known Visualforce URL to get the domain type, the org’s My Domain name, and the package name.

```
   //Parse a known URL

   System.Domain domain = DomainParser.parse('https://mycompany--abcpackage.vf.force.com');

   //Get the domain type

   System.DomainType domainType = domain.getDomainType(); // Returns VISUALFORCE_DOMAIN

   //Get the org’s My Domain name

   String myDomainName = domain.getMyDomainName(); // Returns mycompany

   //Get the package name

   String packageName = domain.getPackageName(); // Returns abcpackage

```

IN THIS SECTION:

#### DomainParser Methods DomainParser Methods

### The following are methods for DomainParser .

IN THIS SECTION:

##### parse(hostname)

Parses a passed hostname of a domain that Salesforce hosts for the org, and returns the System.Domain.

parse(url)
Parses a passed uniform resource locator (URL) of a domain that Salesforce hosts for the org, and returns the System.Domain.

##### **`parse(hostname)`**

Parses a passed hostname of a domain that Salesforce hosts for the org, and returns the System.Domain.


### Apex Reference Guide DomainType Enum

Signature

```
   public static System.Domain parse(String hostname)

```

Parameters

```
   hostname
```

Type: String

The label that identifies a Salesforce host, including all subdomains but without the protocol, path, or any parameters. For example,
`mycompany.my.site.com` or `mycompany--sandbox1.sandbox.my.salesforceforce.com` .

If the hostname format is invalid, it isn’t a Salesforce hosted domain, or it isn’t owned by this org, this method throws an
`InvalidParameterValueException` .

Return Value

Type: System.Domain

##### **`parse(url)`**

Parses a passed uniform resource locator (URL) of a domain that Salesforce hosts for the org, and returns the System.Domain.

Signature

```
   public static System.Domain parse(System.Url url)

```

Parameters

```
   url
```

Type: System.Url

A uniform resource locator (URL) for a Salesforce org, including all subdomains and the protocol. For example,
`https://mycompany--sandbox1.sandbox.my.salesforceforce.com` .

The URL can also include paths and parameters. For example, `https://mycompany.my.site.com/en/us/help` or
`https://mycompany.file.force.com/servlet/servlet.FileDownload?file=015300000000xvU` .

If the URL format is invalid, it isn’t a Salesforce hosted domain, or it isn’t owned by this org, this method throws an
`InvalidParameterValueException` .

Return Value

Type: System.Domain

### DomainType Enum

Specifies the domain type for a System.Domain.

Usage

### Use the DomainType enum to obtain the type of a domain parsed through the System.DomainParser class.


### Apex Reference Guide Double Class

Enum Values

The following are the values of the `System.DomainType` enum. These values only apply to Salesforce-hosted domains.

**Value** **Description**

`CMS_DOMAIN` Content Management System (CMS) public channel domains.

`CONTENT_DOMAIN` Domains that serve content (files) stored in Salesforce.

`CUSTOMER_360_ADMIN_DOMAIN` Customer 360 Data Manager domains.

`CUSTOMER_360_DOMAIN` Customer 360 Data Manager Admin domains.

`EXPERIENCE_CLOUD_SITES_BUILDER_DOMAIN` Experience Builder for Experience Cloud sites domains.

`EXPERIENCE_CLOUD_SITES_DOMAIN` Salesforce-hosted domains that serve Experience Cloud sites.

`EXPERIENCE_CLOUD_SITES_LIVE_PREVIEW_DOMAIN` Experience Builder Live Preview domains.

`EXPERIENCE_CLOUD_SITES_PREVIEW_DOMAIN` Experience Builder Preview domains.

`LIGHTNING_CONTAINER_COMPONENT_DOMAIN` Lightning Container Component domains.

`LIGHTNING_DOMAIN` Domains that serve Lighting pages.

`ORG_MY_DOMAIN` My Domain login domains.

`SALESFORCE_SITES_DOMAIN` Salesforce-hosted domains that serve Salesforce Sites.

`SETUP_DOMAIN` The Salesforce-hosted domain that serves Setup pages.

`VISUALFORCE_DOMAIN` Domains that serve Visualforce pages.

### Double Class

Contains methods for the Double primitive data type.

Namespace

System

Usage

[For more information on Double, see Double Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Double Methods

### The following are methods for Double .

IN THIS SECTION:

format()
Returns the String value for this Double using the locale of the context user


Apex Reference Guide Double Class

##### intValue()

Returns the Integer value of this Double by casting it to an Integer.

longValue()
Returns the Long value of this Double.

round()
Returns the closest Long to this Double value.

valueOf(stringToDouble)
Returns a Double that contains the value of the specified String. As in Java, the String is interpreted as representing a signed decimal.

valueOf(fieldValue)
Converts the specified object to a Double value. Use this method to convert a history tracking field value or an object that represents
a Double value.

##### format()

Returns the String value for this Double using the locale of the context user

Signature

```
   public String format()

```

Return Value

Type: String

Example

```
   Double myDouble = 1261992;

   system.assertEquals('1,261,992', myDouble.format());

##### intValue()

```

Returns the Integer value of this Double by casting it to an Integer.

Signature

```
   public Integer intValue()

```

Return Value

Type: Integer

Example

```
   Double DD1 = double.valueOf('3.14159');

   Integer value = DD1.intValue();

   system.assertEquals(value, 3);

```


Apex Reference Guide Double Class

##### longValue()

Returns the Long value of this Double.

Signature

```
   public Long longValue()

```

Return Value

Type: Long

Example

```
   Double myDouble = 421994;

   Long value = myDouble.longValue();

   System.assertEquals(421994, value);

##### round()

```

Returns the closest Long to this Double value.

Signature

```
   public Long round()

```

Return Value

Type: Long

Example

```
   Double D1 = 4.5;

   Long L1 = D1.round();

   System.assertEquals(5, L1);

   Double D2= 4.2;

   Long L2= D2.round();

   System.assertEquals(4, L2);

   Double D3= -4.7;

   Long L3= D3.round();

   System.assertEquals(-5, L3);

##### valueOf(stringToDouble)

```

Returns a Double that contains the value of the specified String. As in Java, the String is interpreted as representing a signed decimal.

Signature

```
   public static Double valueOf(String stringToDouble)

```


Apex Reference Guide Double Class

Parameters

```
   stringToDouble
```

Type: String

Return Value

Type: Double

Example

```
   Double DD1 = double.valueOf('3.14159');

##### valueOf(fieldValue)

```

Converts the specified object to a Double value. Use this method to convert a history tracking field value or an object that represents a
Double value.

Signature

```
   public static Double valueOf(Object fieldValue)

```

Parameters

```
   fieldValue
```

Type: Object

Return Value

Type: Double

Usage

Use this method with the `OldValue` or `NewValue` fields of history sObjects, such as `AccountHistory`, when the field type
corresponds to a Double type, like a number field.

Example

```
   List<AccountHistory> ahlist =

     [SELECT Field,OldValue,NewValue

     FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'NumberOfEmployees') {

      Double oldValue =

       Double.valueOf(ah.OldValue);

      Double newValue =

       Double.valueOf(ah.NewValue);

   }

```


### Apex Reference Guide EmailMessages Class EmailMessages Class Use the methods in the EmailMessages class to interact with emails and email threading.

Namespace

System

#### EmailMessages Methods

### The following are static methods for EmailMessages .

IN THIS SECTION:

##### getFormattedThreadingToken(recordId)

Returns an email threading token that’s formatted with the correct prefix and suffix. This token can be embedded in an outbound
email body, email subject, or both the body and subject. When users reply to the email, threading tokens can be used to attach
responses to a record, such as a Case record in Email-to-Case.

getRecordIdFromEmail(subject, textBody, htmlBody)
Returns the record ID corresponding to the specified email threading token, or returns null if none is found.

##### **`getFormattedThreadingToken(recordId)`**

Returns an email threading token that’s formatted with the correct prefix and suffix. This token can be embedded in an outbound email
body, email subject, or both the body and subject. When users reply to the email, threading tokens can be used to attach responses to
a record, such as a Case record in Email-to-Case.

Signature

```
   public static Id getFormattedThreadingToken(Id recordId)

```

Parameters

```
   recordId
```

Type:Id

The record ID associated with the threading token.

Return Value

Type: String

The returned value is a formatted string that includes a prefix and suffix, for example:

```
   thread::pp5XPGfmNf2hRZdRCWnrohc::

```

Usage

When sending emails in Apex, use the returned string to match emails to a record, such as a Case record, that’s associated with the email
thread. Embed the formatted token in the body or subject of outgoing emails. To find the corresponding record ID in incoming emails,
use EmailMessages.getRecordIdFromEmail(subject, textBody, htmlBody) on page 3866.


Apex Reference Guide EmailMessages Class

If there is no existing token, `getFormattedThreadingToken` may perform a Data Manipulation Language (DML) operation to
generate one.

If something goes wrong while generating the token, such as a user lacking permission to access the parent record, then null is returned.

Example

In this sample, we send an email with a threading token so that the email and any responses are associated with the related case.

```
   // Get your Record ID. Here, we're using a dummy Case ID.

   ID caseId = Id.valueOf('500xx000000bpkTAAQ');

   // Get the formatted threading token.

   String formattedToken = EmailMessages.getFormattedThreadingToken(caseId);

   // Create a SingleEmailMessage object.

   Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();

   // Set recipients and other fields.

   email.setToAddresses(new String[] {'test@example.com'});

   // Append the threading token to the email body (text or html), subject,

   // or both body and subject.

   email.setPlainTextBody('Test Email Notification text body' + '\n\n' + formattedToken);

   email.setHtmlBody('Test Email Notification html body' + '<br><br>' + formattedToken);

   email.setSubject('Test Notification ' + '[ ' + formattedToken + ' ]');

   // ........... more fields ...........

   // Send out the email.

   Messaging.sendEmail(new Messaging.SingleEmailMessage[]{email});

##### **`getRecordIdFromEmail(subject, textBody, htmlBody)`**

```

Returns the record ID corresponding to the specified email threading token, or returns null if none is found.

Signature

```
   public static Id getRecordIdFromEmail(String subject, String textBody, String htmlBody)

```

Parameters

```
   subject
```

Type: String

The subject of the email.

```
   textBody
```

Type: String

The body of the email in text format.

```
   htmlBody
```

Type: String

The body of the email in HTML format.


Apex Reference Guide EmailMessages Class

Return Value

Type: Id

The record ID that corresponds to the embedded threading token.

Usage

When you send emails with threading tokens embedded in the email subject, the email body, or in both the subject and body, most
email clients quote the email body and maintain the email subject in a response. This method finds a corresponding record that matches
the embedded threading token in a response.

[Typically this method is used in Email Services so that you can provide your own handling of inbound emails using Apex code.](https://help.salesforce.com/s/articleView?id=platform.code_email_services.htm&type=5&language=en_US)

Example

If you implement header-based threading in your Email Services currently, we recommend that you use Lightning threading, which
combines token-based threading and header-based threading. For header-based threading to continue to work, store emails as
EmailMessage records with the MessagedIdentifier field set properly. With Lightning threading, you can use threading tokens as the
primary threading method and rely on header-based threading as a fallback, or vice versa.

In this example, we rely on threading tokens and use header-based threading as a fallback.

```
   global class AttachEmailMessageToCaseExample implements Messaging.InboundEmailHandler {

      global Messaging.InboundEmailResult handleInboundEmail(Messaging.inboundEmail email,

             Messaging.InboundEnvelope env) {

        // Create an InboundEmailResult object for returning the result of the

        // Apex Email Service.

        Messaging.InboundEmailResult result = new Messaging.InboundEmailResult();

        // Try to find the Case ID using threading tokens in email attributes.

        Id caseId = EmailMessages.getRecordIdFromEmail(email.subject, email.plainTextBody,

    email.htmlBody);

        // If we haven't found the Case ID, try finding it using headers.

        if (caseId == null) {

           caseId = Cases.getCaseIdFromEmailHeaders(email.headers);

        }

        // If a Case isn’t found, create a new Case record.

        if (caseId == null) {

           Case c = new Case(Subject = email.subject);

           insert c;

           System.debug('New Case Object: ' + c);

           caseId = c.Id;

        }

        // Process recipients

        String toAddresses;

        if (email.toAddresses != null) {

           toAddresses = String.join(email.toAddresses, '; ');

        }

        // To store an EmailMessage for threading, you need at minimum

```


### Apex Reference Guide EncodingUtil Class

```
        // the Status, the MessageIdentifier, and the ParentId fields.

        EmailMessage em = new EmailMessage(

           Status = '0',

           MessageIdentifier = email.messageId,

           ParentId = caseId,

           // Other important fields.

           FromAddress = email.fromAddress,

           FromName = email.fromName,

           ToAddress = toAddresses,

           TextBody = email.plainTextBody,

           HtmlBody = email.htmlBody,

           Subject = email.subject,

           // Parse thread-index header to remain consistent with Email-to-Case.

           ClientThreadIdentifier = getClientThreadIdentifier(email.headers)

           // Other fields you wish to add.

        );

        // Insert the new EmailMessage.

        insert em;

        System.debug('New EmailMessage Object: ' + em );

      // Set the result to true. No need to send an email back to the user

      // with an error message.

      result.success = true;

      // Return the result for the Apex Email Service.

      return result;

     }

     private String getClientThreadIdentifier(List<Messaging.InboundEmail.Header> headers) {

      if (headers == null || headers.size() == 0) return null;

      try {

        for (Messaging.InboundEmail.Header header : headers) {

           if (header.name.equalsIgnoreCase('thread-index')) {

             Blob threadIndex = EncodingUtil.base64Decode(header.value.trim());

            return EncodingUtil.convertToHex(threadIndex).substring(0, 44).toUpperCase();

           }

        }

      } catch (Exception e){

        return null;

      }

      return null;

     }

   }

### EncodingUtil Class Use the methods in the EncodingUtil class to encode and decode URL strings, and convert strings to hexadecimal format.

```


Apex Reference Guide EncodingUtil Class

Namespace

System

Usage

Note: You cannot use the EncodingUtil methods to move documents with non-ASCII characters to Salesforce. You can, however,
download a document from Salesforce. To do so, query the ID of the document using the API `query` call, then request it by ID.

#### EncodingUtil Methods The following are methods for EncodingUtil . All methods are static.

IN THIS SECTION:

##### base64Decode(inputString)

Converts a Base64-encoded String to a Blob representing its normal form.

base64Encode(inputBlob)
Converts a Blob to an unencoded String representing its normal form.

convertFromHex(inputString)
Converts the specified hexadecimal (base 16) string to a Blob value and returns this Blob value.

convertToHex(inputBlob)
Returns a hexadecimal (base 16) representation of the _`inputBlob`_ . This method can be used to compute the client response (for
example, HA1 or HA2) for HTTP Digest Authentication (RFC2617).

urlDecode(inputString, encodingScheme)
Decodes a string in `application/x-www-form-urlencoded` format using a specific encoding scheme, for example
“UTF-8.”

urlEncode(inputString, encodingScheme)
Encodes a string into the `application/x-www-form-urlencoded` format using a specific encoding scheme, for example
“UTF-8.”

##### base64Decode(inputString)

Converts a Base64-encoded String to a Blob representing its normal form.

Signature

```
   public static Blob base64Decode(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: Blob


Apex Reference Guide EncodingUtil Class

##### base64Encode(inputBlob)

Converts a Blob to an unencoded String representing its normal form.

Signature

```
   public static String base64Encode(Blob inputBlob)

```

Parameters

```
   inputBlob
```

Type: Blob

Return Value

Type: String

##### convertFromHex(inputString)

Converts the specified hexadecimal (base 16) string to a Blob value and returns this Blob value.

Signature

```
   public static Blob convertFromHex(String inputString)

```

Parameters

```
   inputString
```

Type: String

The hexadecimal string to convert. The string can contain only valid hexadecimal characters (0-9, a-f, A-F) and must have an even
number of characters.

Return Value

Type: Blob

Usage

Each byte in the Blob is constructed from two hexadecimal characters in the input string.

##### The convertFromHex method throws the following exceptions.

**•** `NullPointerException`   - the _`inputString`_ is `null` .

**•** `InvalidParameterValueException`   - the _`inputString`_ contains invalid hexadecimal characters or doesn’t contain
an even number of characters.

Example

```
   Blob blobValue = EncodingUtil.convertFromHex('4A4B4C');

   System.assertEquals('JKL', blobValue.toString());

```


Apex Reference Guide EncodingUtil Class

##### convertToHex(inputBlob)

Returns a hexadecimal (base 16) representation of the _`inputBlob`_ . This method can be used to compute the client response (for
example, HA1 or HA2) for HTTP Digest Authentication (RFC2617).

Signature

```
   public static String convertToHex(Blob inputBlob)

```

Parameters

```
   inputBlob
```

Type: Blob

Return Value

Type: String

##### urlDecode(inputString, encodingScheme)

Decodes a string in `application/x-www-form-urlencoded` format using a specific encoding scheme, for example “UTF-8.”

Signature

```
   public static String urlDecode(String inputString, String encodingScheme)

```

Parameters

```
   inputString
```

Type: String

```
   encodingScheme
```

Type: String

Return Value

Type: String

Usage

This method uses the supplied encoding scheme to determine which characters are represented by any consecutive sequence of the
form `\"%xy\"` [. For more information about the format, see The form-urlencoded Media Type in](http://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2.1) _Hypertext Markup Language - 2.0_ .

##### urlEncode(inputString, encodingScheme)

Encodes a string into the `application/x-www-form-urlencoded` format using a specific encoding scheme, for example
“UTF-8.”

Signature

```
   public static String urlEncode(String inputString, String encodingScheme)

```


### Apex Reference Guide Enum Methods

Parameters

```
   inputString
```

Type: String

```
   encodingScheme
```

Type: String

Return Value

Type: String

Usage

The rules that apply when the method encodes a string:

**•** These characters remain the same:

**–** Alphanumeric characters A - Z, a - z, and 0 -9.

**–** Special characters dot (.), hyphen (-), asterisk (*), and under score (_).

**•** The space character is converted to a plus sign (+).

**•** All other characters are unsafe. This method uses the supplied encoding scheme to obtain the bytes for unsafe characters. For more
[information about the format, see The form-urlencoded Media Type in](https://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2.1) _Hypertext Markup Language - 2.0_ .

Example

```
   String encoded = EncodingUtil.urlEncode( url, 'UTF-8');

### Enum Methods

```

An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Apex provides
built-in enums, such as `LoggingLevel`, and you can define your own enum.

All Apex enums, whether user-defined enums or built-in enums, have these common methods:

```
   values
```

This method returns the values of the Enum as a list of the same Enum type.

```
   valueOf(string enumStr)
```

This method converts a specified string to an enum constant value. An exception is thrown if the input string doesn’t match an
enum value.

Each Enum value has the following methods that take no arguments.

```
   name
```

Returns the name of the Enum item as a String.

```
   ordinal
```

Returns the position of the item, as an Integer, in the list of Enum values starting with zero.

Enum values cannot have user-defined methods added to them.

[For more information about Enum, see Enums.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_enums.htm)


### Apex Reference Guide EventBus Class

Example

```
   Integer i = StatusCode.DELETE_FAILED.ordinal();

   String s = StatusCode.DELETE_FAILED.name();

   List<StatusCode> values = StatusCode.values();

   StatusCode statusCodeValue = StatusCode.valueOf('delete_failed');

### EventBus Class

```

Contains methods for publishing platform events.

Namespace

System

IN THIS SECTION:

#### EventBus Methods

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish.htm)_ : Publishing Platform Events

#### EventBus Methods

### The following are methods for EventBus . All methods are static.

IN THIS SECTION:

getOperationId(result)
Returns the event UUID, which identifies a published event message.

publish(event)
Publishes the given platform event.

publish(events)
Publishes the given list of platform events.

publish(event, callback)
Publishes the given platform event using the specified callback. To track asynchronous publish failures, you can implement an Apex
publish callback.

publish(events, callback)
Publishes the given list of platform events using the specified callback. To track asynchronous publish failures, you can implement
an Apex publish callback.

publishWithAccessLevel(event, accesslevel)
Publishes the given platform event.


Apex Reference Guide EventBus Class

publishWithAccessLevel(events, accesslevel)
Publishes the given list of platform events.

publishWithAcessLevel(event, callback, accesslevel)
Publishes the given platform event using the specified callback. To track asynchronous publish failures, you can implement an Apex
publish callback.

publishWithAccessLevel(events, callback, accesslevel)
Publishes the given list of platform events using the specified callback. To track asynchronous publish failures, you can implement
an Apex publish callback.

##### getOperationId(result)

Returns the event UUID, which identifies a published event message.

Signature

```
   public static String getOperationId(Object result)

```

Parameters

```
   result
```

Type: Object

The SaveResult that is returned by the `EventBus.publish` call.

Return Value

Type: String

Usage

**•** If the event publish request fails to be enqueued in Salesforce, and `EventBus.publish` returns a synchronous error,
##### getOperationId returns null. Also in this case, getOperationId returns null even when the event was created using the

newSObject(recordTypeId, loadDefaults) method and contains a prepopulated UUID.

##### publish(event)

Publishes the given platform event.

Signature

```
   public static Database.SaveResult publish(SObject event)

```

Parameters

```
   event
```

Type: SObject

An instance of a platform event. For example, an instance of _`MyEvent__e`_ . You must first define your platform event object in
your org.


Apex Reference Guide EventBus Class

Return Value

Type: Database.SaveResult

The result of publishing the given event. `Database.SaveResult` contains information about whether the operation was successful
and the errors encountered. If the `isSuccess()` method returns `true`, the publish request is queued in Salesforce and the event
[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

`Database.SaveResult` also contains the `Id` system field. The `Id` field value isn’t included in the event message delivered to
subscribers. It isn’t used to identify an event message, and isn’t always unique.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

Usage

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

**•** Prior to API version 67.0, this method ran with `AccessLevel.SYSTEM_MODE` access. Starting with API version 67.0, it runs
with `AccessLevel.USER_MODE` access. The user will be the automated process user unless you set a user using the
PlatformEventSubscriberConfig.

##### publish(events)

Publishes the given list of platform events.

Signature

```
   public static List<Database.SaveResult> publish(List<SObject> events)

```

Parameters

```
   events
```

Type: List<sObject>

A list of platform event instances. For example, a list of _`MyEvent__e`_ objects. You must first define your platform event object in
your Salesforce org.

Return Value

Type: List<Database.SaveResult>

A list of results, each corresponding to the result of publishing one event. For each event, `Database.SaveResult` contains
information about whether the operation was successful and the errors encountered. If the `isSuccess()` method returns `true`,
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in


Apex Reference Guide EventBus Class

the `Database.Error` object. `EventBus.publish()` can publish some passed-in events, even when other events can’t be
published due to errors. The `EventBus.publish()` method doesn’t throw exceptions caused by an unsuccessful publish operation.
It’s similar in behavior to the Apex `Database.insert` method when called with the partial success option.

`Database.SaveResult` also contains the `Id` system field. The `Id` field value isn’t included in the event message delivered to
subscribers. It isn’t used to identify an event message, and isn’t always unique.

If an empty list is passed in for the _`events`_ parameter, no event is published, and an empty `List<Database.SaveResult>`
is returned.

This method returns a `System.UnexpectedException` if you attempt to publish a list of type `List<SObject>` that contains
objects that aren’t platform events.

Usage

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

**•** Prior to API version 67.0, this method ran with `AccessLevel.SYSTEM_MODE` access. Starting with API version 67.0, it runs
with `AccessLevel.USER_MODE` access. The user will be the automated process user unless you set a user using the
PlatformEventSubscriberConfig.

##### **`publish(event, callback)`**

Publishes the given platform event using the specified callback. To track asynchronous publish failures, you can implement an Apex
publish callback.

Signature

```
   public static Database.SaveResult publish(SObject event, Object callback)

```

Parameters

```
   event
```

Type: SObject

An instance of a platform event. For example, an instance of _`MyEvent__e`_ . You must first define your platform event object in
your Salesforce org.

```
   callback
```

Type: Object

An Apex class that implements the EventPublishFailureCallback Interface or EventPublishSuccessCallback Interface.

Return Value

Type: Database.SaveResult

The result of publishing the given event. `Database.SaveResult` contains information about whether the operation was successful
and the errors encountered. If the `isSuccess()` method returns `true`, the publish request is queued in Salesforce and the event


Apex Reference Guide EventBus Class

[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

**•** Prior to API version 67.0, this method ran with `AccessLevel.SYSTEM_MODE` access. Starting with API version 67.0, it runs
with `AccessLevel.USER_MODE` access. The user will be the automated process user unless you set a user using the
PlatformEventSubscriberConfig.

##### **`publish(events, callback)`**

Publishes the given list of platform events using the specified callback. To track asynchronous publish failures, you can implement an
Apex publish callback.

Signature

```
   public static List<Database.SaveResult> publish(List<SObject> sobjects, Object callback)

```

Parameters

```
   sobjects
```

Type: List<SObject>

A list of platform event instances. For example, a list of _`MyEvent__e`_ objects. You must first define your platform event object in
your Salesforce org.

```
   callback
```

Type: Object

An Apex class that implements the EventPublishFailureCallback Interface or EventPublishSuccessCallback Interface.

Return Value

Type: List<Database.SaveResult>

A list of results, each corresponding to the result of publishing one event. For each event, `Database.SaveResult` contains
information about whether the operation was successful and the errors encountered. If the `isSuccess()` method returns `true`,
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in


Apex Reference Guide EventBus Class

the `Database.Error` object. `EventBus.publish()` can publish some passed-in events, even when other events can’t be
published due to errors. The `EventBus.publish()` method doesn’t throw exceptions caused by an unsuccessful publish operation.
It’s similar in behavior to the Apex `Database.insert` method when called with the partial success option.

If an empty list is passed in for the _`events`_ parameter, no event is published, and an empty `List<Database.SaveResult>`
is returned.

This method returns a `System.UnexpectedException` if you attempt to publish a list of type `List<SObject>` that contains
objects that aren’t platform events.

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

**•** Prior to API version 67.0, this method ran with `AccessLevel.SYSTEM_MODE` access. Starting with API version 67.0, it runs
with `AccessLevel.USER_MODE` access. The user will be the automated process user unless you set a user using the
PlatformEventSubscriberConfig.

##### **`publishWithAccessLevel(event, accesslevel)`**

Publishes the given platform event.

Signature

```
   public static Database.SaveResult publishWithAccessLevel(SObject event, AccessLevel

   accesslevel)

```

Parameters

```
   event
```

Type: SObject

An instance of a platform event. For example, an instance of _`MyEvent__e`_ . You must first define your platform event object in
your org.

```
   accesslevel
```

Type: AccessLevel

Either `AccessLevel.SYSTEM_MODE` or `AccessLevel.USER_MODE` . Can't be null. The user is the automated process
user unless a user is set using the PlatformEventSubscriberConfig.

Return Value

Type: Database.SaveResult


Apex Reference Guide EventBus Class

The result of publishing the given event. `Database.SaveResult` contains information about whether the operation was successful
and the errors encountered. If the `isSuccess()` method returns `true`, the publish request is queued in Salesforce and the event
[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

`Database.SaveResult` also contains the `Id` system field. The `Id` field value isn’t included in the event message delivered to
subscribers. It isn’t used to identify an event message, and isn’t always unique.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

Usage

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm)

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

##### **`publishWithAccessLevel(events, accesslevel)`**

Publishes the given list of platform events.

Signature

```
   public static List<Database.SaveResult> publishWithAccessLevel(List<SObject> events,

   AccessLevel accesslevel)

```

Parameters

```
   events
```

Type: List<sObject>

A list of platform event instances. For example, a list of _`MyEvent__e`_ objects. You must first define your platform event object in
your Salesforce org.

```
   accesslevel
```

Type: AccessLevel

Either `AccessLevel.SYSTEM_MODE` or `AccessLevel.USER_MODE` . Can't be null. The user is the automated process
user unless a user is set using the PlatformEventSubscriberConfig.

Return Value

Type: List<Database.SaveResult>

A list of results, each corresponding to the result of publishing one event. For each event, `Database.SaveResult` contains
information about whether the operation was successful and the errors encountered. If the `isSuccess()` method returns `true`,
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in
the `Database.Error` object. `EventBus.publish()` can publish some passed-in events, even when other events can’t be


Apex Reference Guide EventBus Class

published due to errors. The `EventBus.publish()` method doesn’t throw exceptions caused by an unsuccessful publish operation.
It’s similar in behavior to the Apex `Database.insert` method when called with the partial success option.

`Database.SaveResult` also contains the `Id` system field. The `Id` field value isn’t included in the event message delivered to
subscribers. It isn’t used to identify an event message, and isn’t always unique.

If an empty list is passed in for the _`events`_ parameter, no event is published, and an empty `List<Database.SaveResult>`
is returned.

This method returns a `System.UnexpectedException` if you attempt to publish a list of type `List<SObject>` that contains
objects that aren’t platform events.

Usage

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm)

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

##### **`publishWithAcessLevel(event, callback, accesslevel)`**

Publishes the given platform event using the specified callback. To track asynchronous publish failures, you can implement an Apex
publish callback.

Signature

```
   public static Database.SaveResult publishWithAccessLevel(SObject event, Object callback,

   AccessLevel accesslevel)

```

Parameters

```
   event
```

Type: SObject

An instance of a platform event. For example, an instance of _`MyEvent__e`_ . You must first define your platform event object in
your Salesforce org.

```
   callback
```

Type: Object

An Apex class that implements the EventPublishFailureCallback Interface or EventPublishSuccessCallback Interface.

```
   accesslevel
```

Type: SObject

Either `AccessLevel.SYSTEM_MODE` or `AccessLevel.USER_MODE` . Can't be null. The user is the automated process
user unless a user is set using the PlatformEventSubscriberConfig.

Return Value

Type: Database.SaveResult


Apex Reference Guide EventBus Class

The result of publishing the given event. `Database.SaveResult` contains information about whether the operation was successful
and the errors encountered. If the `isSuccess()` method returns `true`, the publish request is queued in Salesforce and the event
[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

\

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm)

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

##### **`publishWithAccessLevel(events, callback, accesslevel)`**

Publishes the given list of platform events using the specified callback. To track asynchronous publish failures, you can implement an
Apex publish callback.

Signature

```
   public static List<Database.SaveResult> publishWithAccessLevel(List<SObject> sobjects,

   Object callback, AccessLevel accesslevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

A list of platform event instances. For example, a list of _`MyEvent__e`_ objects. You must first define your platform event object in
your Salesforce org.

```
   callback
```

Type: Object

An Apex class that implements the EventPublishFailureCallback Interface or EventPublishSuccessCallback Interface.

```
   accesslevel
```

Type: AccessLevel

Either `AccessLevel.SYSTEM_MODE` or `AccessLevel.USER_MODE` . Can't be null. The user is the automated process
user unless a user is set using the PlatformEventSubscriberConfig.


### Apex Reference Guide Exception Class and Built-In Exceptions

Return Value

Type: List<Database.SaveResult>

A list of results, each corresponding to the result of publishing one event. For each event, `Database.SaveResult` contains
information about whether the operation was successful and the errors encountered. If the `isSuccess()` method returns `true`,
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in
the `Database.Error` object. `EventBus.publish()` can publish some passed-in events, even when other events can’t be
published due to errors. The `EventBus.publish()` method doesn’t throw exceptions caused by an unsuccessful publish operation.
It’s similar in behavior to the Apex `Database.insert` method when called with the partial success option.

If an empty list is passed in for the _`events`_ parameter, no event is published, and an empty `List<Database.SaveResult>`
is returned.

This method returns a `System.UnexpectedException` if you attempt to publish a list of type `List<SObject>` that contains
objects that aren’t platform events.

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_define_ui.htm)

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3984 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3987 method.

### Exception Class and Built-In Exceptions

An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create custom
exceptions. All exceptions have common methods.

All exceptions support built-in methods for returning the error message and exception type. In addition to the standard `exception`
class, there are several different types of exceptions:

The following are exceptions in the `System` namespace.

### **Exception Description**

`AssertException` A System.assert failure that halts code execution. Optionally contains the custom
message specified in the last ( `msg` ) argument to the `assert()` method.

`AuraException` Legacy Aura-related exception. Use System.AuraHandledException instead.

`AuraHandledException` [Returns a custom error message to a JavaScript controller. See Returning Errors from](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/controllers_server_apex_custom_errors.htm)
[an Apex Server-Side Controller.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/controllers_server_apex_custom_errors.htm)

`AsyncException` Any problem with an asynchronous operation, such as failing to enqueue an
asynchronous call.


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

`BigObjectException` Any problem with big object records, such as connection timeouts during attempts to
access or insert big object records.

`CalloutException` Any problem with a web service operation, such as failing to make a callout to an
external system.

`DataWeaveScriptException` Any run-time script errors that occur within DataWeave in Apex.

`DmlException` Any problem with a DML statement, such as an `insert` statement missing a required
field on a record.

`DuplicateMessageException` Attempt to enqueue job with duplicate queueable signature

`EmailException` [Any problem with email, such as failure to deliver. For more information, see Outbound](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_forcecom_email_outbound.htm)
[Email.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_forcecom_email_outbound.htm)

`ExternalObjectException` Any problem with external object records, such as connection timeouts during attempts
to access the data that’s stored on external systems.

`FatalCursorException` Any problem with Apex cursors in a transaction.

`FinalException` Any attempt to mutate a read-only collection or record such as an sObject in an
after-update trigger, or a final variable. This exception causes execution to halt.

`FlowException` Any problem with starting flow interviews from Apex. For example, if an active version
of the flow can’t be found or it can’t be started from Apex.

`HandledException` A generic handled exception.

`IllegalArgumentException` An illegal argument was provided to a method call. For example, a method that requires
a non-null argument throws this exception if a null value is passed into the method.

```
InvalidHeaderException

```

An illegal header argument was provided to an Apex REST call. For example, a call to
the `RestResponse.addHeader(name, value)` method throws this
exception if the header name is `cookie` .

`InvalidParameterValueException` This exception is used with both Visualforce pages and Salesforce Functions.

**•** **Visualforce** : The exception is thrown when an invalid parameter is supplied for a
method, or any problem is encountered with a URL used with Visualforce pages.
[For more information on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

**•** **Salesforce Functions** : The exception is thrown when the
`functionName` parameter to `Function.get()` doesn’t have the
correct `project name.function name` format. For more information on
Salesforce functions, see `[Function.get()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_functions_Function.htm)` .

`LimitException` A governor limit has been exceeded. This exception can’t be caught.

```
JSONException

```

Any problem with JSON serialization and deserialization operations. For more
information, see the methods of `System.JSON`, `System.JSONParser`, and
`System.JSONGenerator` .

`ListException` Any problem with a list, such as attempting to access an index that is out of bounds.

`MathException` Any problem with a mathematical operation, such as dividing by zero.


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

```
NoAccessException

```

Any problem with unauthorized access, such as trying to access an sObject that the
current user doesn’t have access to. This exception is used with Visualforce pages. For
[more information on Visualforce, see the Visualforce Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

`NoDataFoundException` This exception is used with both Visualforce pages and Salesforce Functions.

**•** **Visualforce** : The exception is thrown with data that doesn't exist, such as trying
to access an sObject that has been deleted. For more information on Visualforce,
[see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

**•** **Salesforce Functions** : The exception is thrown when the project or function name
provided in the `functionName` parameter to the `Function.get()` method
can't be found. For more information on Salesforce functions, see
`[Function.get()](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_functions_Function.htm)` .

`NoSuchElementException` This exception is thrown if you try to access items that are outside the bounds of a list.
[This exception is used by the Iterator](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_iterable.htm) `next` method. For example, if

`iterator.hasNext() == false` and you call `iterator.next()`, this
exception is thrown. This exception is also used by the Apex Flex Queue methods and
is thrown if you attempt to access a job at an invalid position in the flex queue.

```
NullPointerException

```

Any problem with dereferencing null, such as in the following code:

```
String s;

s.toLowerCase(); // Since s is null, this call causes

           // a NullPointerException

```

`QueryException` Any problem with SOQL queries, such as assigning a query that returns no records or
more than one record to a singleton sObject variable.

`RequiredFeatureMissing` A Chatter feature is required for code that has been deployed to an organization that
doesn’t have Chatter enabled.

```
SearchException

```

Any problem with SOSL queries executed with SOAP API `search()` call, for example,
when the `searchString` parameter contains fewer than two characters. For more
[information, see the SOAP API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/)

`SecurityException` Any problem with static methods in the Crypto utility class. For more information, see
Crypto Class.

`SerializationException` Any problem with the serialization of data. This exception is used with Visualforce pages.
[For more information on Visualforce, see the Visualforce Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

`SObjectException` Any problem with sObject records, such as attempting to change a field in an `update`
statement that can only be changed during `insert` .

`StringException` Any problem with Strings, such as a String that is exceeding your heap size.

`TransientCursorException` A transient problem with an Apex cursor transaction. The failed transaction can be
retried.

`TypeException` Any problem with type conversions, such as attempting to convert the String 'a' to an
Integer using the `valueOf` method.


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

`UnexpectedException` A non-recoverable internal error within Salesforce has occurred. This exception causes
execution to halt. If necessary, contact Salesforce Customer Support for more information.

`VisualforceException` Any problem with a Visualforce page. For more information on Visualforce, see the
[Visualforce Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

`XmlException` Any problem with the XmlStream classes, such as failing to read or write XML.

The following is an example using the DmlException exception:

```
   Account[] accts = new Account[]{new Account(billingcity = 'San Jose')};

   try {

      insert as user accts;

   } catch (System.DmlException e) {

      for (Integer i = 0; i < e.getNumDml(); i++) {

        // Process exception here

        System.debug(e.getDmlMessage(i));

      }

   }

```

For exceptions in other namespaces, see:

**•** Cache Exceptions

**•** Canvas Exceptions

**•** Compression Exceptions

**•** `ConnectApi` Exceptions

**•** DataSource Exceptions

**•** Reports Exceptions

**•** Site Exceptions

Common Exception Method

Exception methods are all called by and operate on an instance of an exception. This table describes all instance exception methods.
All types of exceptions have these methods in common.

**Name** **Arguments** **Return Type** **Description**

`getCause` Exception Returns the cause of the exception as an exception object.

`getLineNumber` Integer Returns the line number from where the exception was
thrown.

`getMessage` String Returns the error message that displays for the user.

`getStackTraceString` String Returns the stack trace of a thrown exception as a string.

`getTypeName` String Returns the type of exception, such as DmlException,
ListException, MathException, and so on.


Apex Reference Guide Exception Class and Built-In Exceptions

**Name** **Arguments** **Return Type** **Description**

`initCause` Exception _`cause`_ Void Sets the cause for this exception, if one hasn’t already been
set.

`setMessage` String _`s`_ Void Sets the error message that displays for the user.

DMLException and EmailException Methods

In addition to the common exception methods, DMLException and EmailException have these methods:

**Name** **Arguments** **Return Type** **Description**

`getDmlFieldNames` Integer _`i`_ String [] Returns the names of the field or fields that caused the error
described by the _`i`_ _`[th]`_ failed row.

`getDmlFields` Integer _`i`_ Schema.sObjectField []

Returns the field token or tokens for the field or fields that
caused the error described by the _`i`_ _`[th]`_ failed row. For more
[information on field tokens, see Dynamic Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic.htm)

`getDmlId` Integer _`i`_ String Returns the ID of the failed record that caused the error
described by the _`i`_ _`[th]`_ failed row.

`getDmlIndex` Integer _`i`_ Integer Returns the original row position of the _`i`_ _`[th]`_ failed row.

`getDmlMessage` Integer _`i`_ String Returns the user message for the _`i`_ _`[th]`_ failed row.

`getDmlStatusCode` Integer _`i`_ String Deprecated. Use getDmlType instead. Returns the Apex
failure code for the _`i`_ _`[th]`_ failed row.

`getDmlType` Integer _`i`_ [System.StatusCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

Returns the value of the System.StatusCode enum. For
example:

```
try {

  insert as user new Account();

} catch (System.DmlException ex) {

    Assert.areEqual(

StatusCode.REQUIRED_FIELD_MISSING,

      ex.getDmlType(0));

}

```

[For more information about System.StatusCode, see Enums.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

`getNumDml` Integer Returns the number of failed rows for DML exceptions.

QueryException Method

In addition to the common exception methods, QueryException has this method.


### Apex Reference Guide ExternalServiceTest Class

**Name** **Arguments** **Return Type** **Description**

```
getInaccessibleFields

### ExternalServiceTest Class

```

Map on page Returns a map in which each key is an `sObjectType`
4013<String,Set< on and its corresponding value is the set of inaccessible field
page 4157String>> names in fully qualified format

(Namespace__FieldName__c).

Use this method to determine the cause of the
`QueryException` . The returned map contains data only
if the method that threw the `QueryException` is
running in user mode.

In this code sample, it's assumed that the user doesn’t have
field level security access to the `Contact.Email` and
`Account.Website` fields.

```
          try {

             List<Account> accounts = [SELECT

          Website, (SELECT Email FROM Contacts)

          FROM Account WITH USER_MODE];

          } catch (QueryException qe) {

             // Handle inaccessible fields

             Map<String, Set<String>>

          inaccessible =

          qe.getInaccessibleFields();

             Set<String> accountFields =

          inaccessible.get('Account');

             Set<String> contactFields =

          inaccessible.get('Contact');

          }

```

Provides methods to test an external service's asynchronous callouts, enables sending a mock request, asserts the expected request
payload, then triggers the mocked external service’s asynchronous callback response.

Namespace

System

Usage

[See Create Unit Testing for Asynchronous Callouts in the "Extend Salesforce with Clicks, Not Code" Help Guide.](https://help.salesforce.com/s/articleView?id=platform.external_services_aysnc_ops_testing.htm&type=5&language=en_US)

IN THIS SECTION:

ExternalServiceTest Methods
An instance of the ExternalServiceTest method is used when the test class triggers a mocked external service’s callback response.
You can access ExternalServiceTest through `Test.getExternalService()`


### Apex Reference Guide FeatureManagement Class

#### ExternalServiceTest Methods

An instance of the ExternalServiceTest method is used when the test class triggers a mocked external service’s callback response. You
can access ExternalServiceTest through `Test.getExternalService()`

#### The following are methods for ExternalServiceTest .

IN THIS SECTION:

##### sendCallback(request)

Sends the HTTP request back as an external service asynchronous response.

##### sendCallback(request)

Sends the HTTP request back as an external service asynchronous response.

Signature

```
   public System.HttpResponse sendCallback(System.HttpRequest request)

   System.ExternalServiceTest, sendCallback, [System.HttpRequest], System.HttpResponse

```

Parameters

```
   request
```

Type: System.HttpRequest on page 3907

Return Value

Type: System.HttpResponse on page 3916

### FeatureManagement Class

Use the methods in the `System.FeatureManagement` class to check and modify the values of feature parameters, and to show
or hide custom objects and custom permissions in your subscribers’ orgs.

Namespace

System

Usage

[For information about feature parameters, see Manage Features in Second Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_fma_manage_features.htm) _Second-Generation_
_Managed Packaging Developer Guide_ [, or Manage Features in First-Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_manage_features.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

The set methods (setPackageBooleanValue, setPackageDateValue, setPackageIntegerValue) use DML operations on setup sObjects. To
[learn more about mixing operations in a test, see Mixed DML Operations in Test Methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects_test_methods.htm)


Apex Reference Guide FeatureManagement Class

IN THIS SECTION:

#### FeatureManagement Methods FeatureManagement Methods The following are methods for FeatureManagement .

IN THIS SECTION:

##### changeProtection(apiName, typeApiName, protection)

Hides or reveals custom permissions, or reveals custom objects, in your subscriber’s org.

checkPackageBooleanValue(apiName)
Checks the `value__c` value of the `FeatureParameterBoolean__c` record for a feature parameter in your subscriber’s
org. You set the record’s value using `setPackageBooleanValue(apiName, value)` .

checkPackageDateValue(apiName)
Checks the `value__c` value of the `FeatureParameterDate__c` record for a feature parameter in your subscriber’s org.
You can set the record’s value using `setPackageDateValue(apiName, value)` .

checkPackageIntegerValue(apiName)
Checks the `value__c` value of the `FeatureParameterInteger__c` record for a feature parameter in your subscriber’s
org. You can set the record’s value using `setPackageIntegerValue(apiName, value)` .

checkPermission(apiName)
Checks whether a custom permission is enabled.

setPackageBooleanValue(apiName, value)
Sets the `value__c` value of the `FeatureParameterBoolean__c` record for a subscriber-to-LMO feature parameter in
your subscriber’s org. You can check the record’s value using `checkPackageBooleanValue(apiName)` .

setPackageDateValue(apiName, value)
Sets the `value__c` value of the `FeatureParameterDate__c` record for a subscriber-to-LMO feature parameter in your
subscriber’s org. You can check the record’s value using `checkPackageDateValue(apiName)` .

setPackageIntegerValue(apiName, value)
Sets the `value__c` value of the `FeatureParameterInteger__c` record for a subscriber-to-LMO feature parameter in
your subscriber’s org. You can check the record’s value using `checkPackageIntegerValue(apiName)` .

##### changeProtection(apiName, typeApiName, protection)

Hides or reveals custom permissions, or reveals custom objects, in your subscriber’s org.

Signature

```
   public static void changeProtection(String apiName, String typeApiName, String

   protection)

```

Parameters

```
   apiName
```

Type: String


Apex Reference Guide FeatureManagement Class

The API name of the custom object or custom permission to show or hide—for example, `'MyCustomObject__c'` or

`'MyCustomPermission'` .

```
   typeApiName
```

Type: String

The API name of the type that you want to show or hide: `'CustomObject'` or `'CustomPermission'` .

```
   protection
```

Type: String

To show a custom object or custom permission, `'Unprotected'` .

To hide a custom permission, `'Protected'` .

Return Value

Type: void

Usage

Warning: For custom permissions, you can toggle the protected value indefinitely. However, after you’ve released unprotected
objects to subscribers, you can’t set visibility to `Protected` . Be sure to protect any custom objects that you want to hide before
you release the first package version that contains them.

To hide custom permissions in released packages:

```
   FeatureManagement.changeProtection(' YourCustomPermissionName ', 'CustomPermission',

      'Protected');

```

To unhide custom permissions and custom objects in released packages:

```
   FeatureManagement.changeProtection(' YourCustomPermissionName ', 'CustomPermission',

      'Unprotected');

   FeatureManagement.changeProtection(' YourCustomObjectName__c ', 'CustomObject',

      'Unprotected');

##### checkPackageBooleanValue(apiName)

```

Checks the `value__c` value of the `FeatureParameterBoolean__c` record for a feature parameter in your subscriber’s org.
You set the record’s value using `setPackageBooleanValue(apiName, value)` .

Signature

```
   public static Boolean checkPackageBooleanValue(String apiName)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to check—for example,

`'SpecialAccessAvailable'` .


Apex Reference Guide FeatureManagement Class

Return Value

Type: Boolean

The value that’s currently assigned to the `value__c` field on the `FeatureParameterBoolean__c` record that associates the
feature parameter with its related license.

##### checkPackageDateValue(apiName)

Checks the `value__c` value of the `FeatureParameterDate__c` record for a feature parameter in your subscriber’s org. You
can set the record’s value using `setPackageDateValue(apiName, value)` .

Signature

```
   public static Date checkPackageDateValue(String apiName)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to check—for example, `'TrialExpirationDate'` .

Return Value

Type: Date

The value that’s currently assigned to the `value__c` field on the `FeatureParameterDate__c` record that associates the
feature parameter with its related license.

##### checkPackageIntegerValue(apiName)

Checks the `value__c` value of the `FeatureParameterInteger__c` record for a feature parameter in your subscriber’s org.
You can set the record’s value using `setPackageIntegerValue(apiName, value)` .

Signature

```
   public static Integer checkPackageIntegerValue(String apiName)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to check—for example, `'NumberOfLicenses'` .

Return Value

Type: Integer

The value that’s currently assigned to the `value__c` field on the `FeatureParameterInteger__c` record that associates the
feature parameter with its related license.


Apex Reference Guide FeatureManagement Class

##### checkPermission(apiName)

Checks whether a custom permission is enabled.

Signature

```
   public static Boolean checkPermission(String apiName)

```

Parameters

```
   apiName
```

Type: String

The API name of the custom permission to check the value of—for example, `'MyCustomPermission'` .

Return Value

Type: Boolean

Shows whether the permission is enabled ( `true` ) or disabled ( `false` ).

##### setPackageBooleanValue(apiName, value)

Sets the `value__c` value of the `FeatureParameterBoolean__c` record for a subscriber-to-LMO feature parameter in your
subscriber’s org. You can check the record’s value using `checkPackageBooleanValue(apiName)` .

Signature

```
   public static void setPackageBooleanValue(String apiName, Boolean value)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to set—for example,

`'SpecialAccessAvailable'` .

```
   value
```

Type: Boolean

The value to assign to the `value__c` field on the `FeatureParameterBoolean__c` record that associates the feature
parameter with its related license.

Return Value

Type: void

##### setPackageDateValue(apiName, value)

Sets the `value__c` value of the `FeatureParameterDate__c` record for a subscriber-to-LMO feature parameter in your
subscriber’s org. You can check the record’s value using `checkPackageDateValue(apiName)` .


### Apex Reference Guide Finalizer Interface

Signature

```
   public static void setPackageDateValue(String apiName, Date value)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to set—for example, `'TrialExpirationDate'` .

```
   value
```

Type: Date

The value to assign to the `value__c` field on the `FeatureParameterDate__c` record that associates the feature parameter
with its related license.

Return Value

Type: void

##### setPackageIntegerValue(apiName, value)

Sets the `value__c` value of the `FeatureParameterInteger__c` record for a subscriber-to-LMO feature parameter in your
subscriber’s org. You can check the record’s value using `checkPackageIntegerValue(apiName)` .

Signature

```
   public static void setPackageIntegerValue(String apiName, Integer value)

```

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to set—for example, `'NumberOfLicenses'` .

```
   value
```

Type: Integer

The value to assign to the `value__c` field on the `FeatureParameterInteger__c` record that associates the feature
parameter with its related license.

Return Value

Type: void

### Finalizer Interface

Use this interface to attach actions that are executed at the end of asynchronous Queueable job executions. A specific use case is to
design recovery actions when a Queueable job fails.


Apex Reference Guide Finalizer Interface

Namespace

System

Usage

#### The execute method is called on the provided Finalizer instance for every enqueued job that has an attached finalizer. Within
##### the execute method, you can define the actions to be taken at the end of the Queueable job. An instance of System.FinalizerContext is injected by the Apex runtime engine as an argument to the execute method.

IN THIS SECTION:

#### Finalizer Methods Finalizer Example Implementation Finalizer Methods The following are methods for Finalizer .

IN THIS SECTION:

##### execute(finalizerContext)
#### The execute method is called on the provided Finalizer instance for every enqueued job that has an attached finalizer.
##### Within the execute method, you can define the actions to be taken at the end of the Queueable job. **`execute(finalizerContext)`**

#### The execute method is called on the provided Finalizer instance for every enqueued job that has an attached finalizer. Within
##### the execute method, you can define the actions to be taken at the end of the Queueable job.

Signature

```
   public void execute(System.FinalizerContext finalizerContext)

```

Parameters

```
   finalizerContext
```

Type: FinalizerContext Interface on page 3895

Return Value

Type: void

#### Finalizer Example Implementation

For a sample implementation of the `System.Finalizer` [interface, see the Logging Finalizer Example in Transaction Finalizers.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_transaction_finalizers.htm)


### Apex Reference Guide FinalizerContext Interface FinalizerContext Interface

Represents the parameter type of the `execute` method in a class that implements the Finalizer interface. This interface is implemented
##### internally by Apex. The System.FinalizerContext interface contains four methods: getAsyncApexJobId, getRequestId, getResult, and getException . An instance of System.FinalizerContext is injected by the Apex runtime engine as

an argument to the `Finalizer.execute` method.

Namespace

System

IN THIS SECTION:

#### FinalizerContext Methods FinalizerContext Methods

### The following are methods for FinalizerContext .

IN THIS SECTION:

##### getAsyncApexJobId()

Returns the ID of the Queueable job for which this finalizer is defined.

##### getException()

Returns the exception with which the Queueable job failed when `getResult` is `UNHANDLED_EXCEPTION`, null otherwise.

getRequestId()
Returns the request ID that can be correlated with Event Monitoring logs. To correlate the request with the AsyncApexJob table, use
##### the getAsyncApexJobId method instead. The Queueable job and the Finalizer execution share the same request ID.

getResult()
Returns the `System.ParentJobResult` enum, which represents the result of the parent asynchronous Apex Queueable job
to which the finalizer is attached. The enum takes these values: `SUCCESS`, `UNHANDLED_EXCEPTION` .

##### **`getAsyncApexJobId()`**

Returns the ID of the Queueable job for which this finalizer is defined.

Signature

```
   public Id getAsyncApexJobId()

```

Return Value

Type: Id

##### **`getException()`**

Returns the exception with which the Queueable job failed when `getResult` is `UNHANDLED_EXCEPTION`, null otherwise.


### Apex Reference Guide FlexQueue Class

Signature

```
   public Exception getException()

```

Return Value

Type: Exception

##### **`getRequestId()`**

Returns the request ID that can be correlated with Event Monitoring logs. To correlate the request with the AsyncApexJob table, use the
`getAsyncApexJobId` method instead. The Queueable job and the Finalizer execution share the same request ID.

Signature

```
   public String getRequestId()

```

Return Value

Type: String

##### **`getResult()`**

Returns the `System.ParentJobResult` enum, which represents the result of the parent asynchronous Apex Queueable job to
which the finalizer is attached. The enum takes these values: `SUCCESS`, `UNHANDLED_EXCEPTION` .

Signature

```
   public System.ParentJobResult getResult()

```

Return Value

Type: System.ParentJobResult on page 4103

### FlexQueue Class

Contains methods that reorder batch jobs in the Apex flex queue.

Namespace

System

Usage

You can place up to 100 batch jobs in a holding status for future execution. When system resources become available, the jobs are taken
from the top of the Apex flex queue and moved to the batch job queue. Up to five queued or active jobs can be processed simultaneously
for each org. When a job is moved out of the flex queue for processing, its status changes from Holding to Queued. Queued jobs are
executed when the system is ready to process new jobs.

### Use this class’s methods to reorder your Holding jobs in the flex queue. As best practice and for safe usage, a FlexQueue reorder

method must be the final statement in a transaction.


Apex Reference Guide FlexQueue Class

Example

This example moves a job to the front of the flex queue so that it’s executed immediately. The job is moved by calling the
`System.FlexQueue.moveJobToFront()` method with the high priority job ID as the parameter.

```
   ID highPriorityJobId = Database.executeBatch(new HighPriorityBatchClass(), 200);

   boolean jobMovedToFrontOfQueue = FlexQueue.moveJobToFront(highPriorityJobId);

```

IN THIS SECTION:

#### FlexQueue Methods

SEE ALSO:

[Monitoring the Apex Flex Queue](https://help.salesforce.com/HTViewHelpDoc?id=code_apex_flex_queue.htm&language=en_US)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)_ : Using Batch Apex

#### FlexQueue Methods The following are methods for FlexQueue .

IN THIS SECTION:

##### moveAfterJob(jobToMoveId, jobInQueueId)

Moves the job with the ID _`jobToMoveId`_ immediately after the job with the ID _`jobInQueueId`_ in the flex queue. You can
##### move jobToMoveId forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception.

Returns `true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately after _`jobInQueueId`_, so no change
is made.

moveBeforeJob(jobToMoveId, jobInQueueId)
Moves the job with the ID _`jobToMoveId`_ immediately before the job with the ID _`jobInQueueId`_ in the flex queue. You can
##### move jobToMoveId forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception.

Returns `true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately before _`jobInQueueId`_, so no change
is made.

moveJobToEnd(jobId)
Moves the specified job the end of the flex queue, to index position `(size - 1)` . All jobs after the job’s starting position move
one spot forward. If the job isn’t in the queue, it throws an element-not-found exception. Returns `true` if the job is moved, or

`false` if the job is already at the end of the queue, so no change is made.

moveJobToFront(jobId)
Moves the specified job to the front of the flex queue, to index position `0` . All other jobs move back one spot. If the job isn’t in the
queue, it throws an element-not-found exception. Returns `true` if the job is moved, or `false` if the job is already at the front of
the queue, so no change is made.

##### moveAfterJob(jobToMoveId, jobInQueueId)

Moves the job with the ID _`jobToMoveId`_ immediately after the job with the ID _`jobInQueueId`_ in the flex queue. You can move
_`jobToMoveId`_ forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception. Returns
`true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately after _`jobInQueueId`_, so no change is made.


Apex Reference Guide FlexQueue Class

Signature

```
   public static Boolean moveAfterJob(Id jobToMoveId, Id jobInQueueId)

```

Parameters

```
   jobToMoveId
```

Type: Id

The ID of the job to move.

```
   jobInQueueId
```

Type: Id

The ID of the job to move after.

Return Value

Type: Boolean

##### moveBeforeJob(jobToMoveId, jobInQueueId)

Moves the job with the ID _`jobToMoveId`_ immediately before the job with the ID _`jobInQueueId`_ in the flex queue. You can move
_`jobToMoveId`_ forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception. Returns
`true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately before _`jobInQueueId`_, so no change is made.

Signature

```
   public static Boolean moveBeforeJob(Id jobToMoveId, Id jobInQueueId)

```

Parameters

```
   jobToMoveId
```

Type: Id

The ID of the job to move.

```
   jobInQueueId
```

Type: Id

The ID of the job to use as a reference point.

Return Value

Type: Boolean

##### moveJobToEnd(jobId)

Moves the specified job the end of the flex queue, to index position `(size - 1)` . All jobs after the job’s starting position move one
spot forward. If the job isn’t in the queue, it throws an element-not-found exception. Returns `true` if the job is moved, or `false` if
the job is already at the end of the queue, so no change is made.

Signature

```
   public static Boolean moveJobToEnd(Id jobId)

```


### Apex Reference Guide Formula Class

Parameters

```
   jobId
```

Type: Id

The ID of the job to move.

Return Value

Type: Boolean

##### moveJobToFront(jobId)

Moves the specified job to the front of the flex queue, to index position `0` . All other jobs move back one spot. If the job isn’t in the queue,
it throws an element-not-found exception. Returns `true` if the job is moved, or `false` if the job is already at the front of the queue,
so no change is made.

Signature

```
   public static Boolean moveJobToFront(Id jobId)

```

Parameters

```
   jobId
```

Type: Id

The ID of the job to move.

Return Value

Type: Boolean

### Formula Class

Contains methods to get a builder for creating a formula instance and to update all formula fields on the input SObjects.

Namespace

System

Usage

Use the Formula class in conjunction with the FormulaBuilder and FormulaInstance on page 2893 classes in the FormulaEval on page 2887
namespace.

[See Formula Evaluation in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_formulaeval.htm)


Apex Reference Guide Formula Class

Example

This example creates a formula instance using `Formula.builder()` and the FormulaBuilder methods.

```
   FormulaEval.FormulaInstance ff = Formula.builder()

      .withType(Account.SObjectType)

      .withReturnType(FormulaEval.FormulaReturnType.STRING)

      .withFormula('{!name} ({!website})')

      .parseAsTemplate(true)

      .build();

```

IN THIS SECTION:

#### Formula Methods Formula Methods The following are methods for Formula .

IN THIS SECTION:

##### builder()

Creates an instance of `FormulaBuilder` for configuring the formula with formula expression, context type, and output data
type as inputs.

##### recalculateFormulas(sobjects)

Updates (recalculates) all formula fields on the input SObjects.

##### **`builder()`**

Creates an instance of `FormulaBuilder` for configuring the formula with formula expression, context type, and output data type
as inputs.

Signature

```
   public static formulaeval.FormulaBuilder builder()

```

Return Value

Type: FormulaEval.FormulaBuilder

##### recalculateFormulas(sobjects)

Updates (recalculates) all formula fields on the input SObjects.

Signature

```
   public static List<System.FormulaRecalcResult> recalculateFormulas(List<SObject>

   sobjects)

```


### Apex Reference Guide FormulaRecalcFieldError Class

Parameters

```
   sobjects
```

Type: List<SObject>

List of sObjects whose formula fields are to be recalculated.

Return Value

Type: List<FormulaRecalcResult Class>

Usage

Recalculate formula fields on new or queried SObjects. If all data is present on the SObjects, SOQL limits are not affected. If the data
required to evaluate a formula field is missing, that data is retrieved and limits are changed accordingly.

The new formula values are stored in the SObjects themselves and overwrite previous values of formula fields.

Example

```
   Account a = new Account();

   a.Name = 'Salesforce';

   a.BillingCity = 'San Francisco';

   List<Account> accounts = new List<Account>{a};

   List<FormulaRecalcResult> results = Formula.recalculateFormulas(accounts);

   System.assert(results[0].isSuccess());

   // Option 1

   System.debug('New value: ' + accounts[0].get('My_Formula_Field__c'));

   // Option 2

   System.debug('New value: ' + results[0].getSObject().get(‘My_Formula_Field__c’));

### FormulaRecalcFieldError Class

```

The return type of the `FormulaRecalcResult.getErrors` method.

Namespace

System

IN THIS SECTION:

#### FormulaRecalcFieldError Methods FormulaRecalcFieldError Methods

### The following are methods for FormulaRecalcFieldError .

IN THIS SECTION:

getFieldError()
Returns a message describing the errors encountered during formula recalculation.


### Apex Reference Guide FormulaRecalcResult Class

##### getFieldName()

Returns the name of the formula recalculation error field.

##### getFieldError()

Returns a message describing the errors encountered during formula recalculation.

Signature

```
   public String getFieldError()

```

Return Value

Type: String

##### getFieldName()

Returns the name of the formula recalculation error field.

Signature

```
   public String getFieldName()

```

Return Value

Type: String

### FormulaRecalcResult Class

The return type of the `Formula.recalculateFormulas` method.

Namespace

System

Usage

Indicates the result and status of recalculating formulas on a single sObject. Holds a reference to the sObject and a list of all the fields
that were recalculated.

Example

This example assumes that you have a formula field called `divide__c with formula “1 / LEN(Name)` .

```
   List<Account> accounts = [SELECT Name FROM Account WHERE Name='Acme'];

   accounts[0].Name = '';

   List<FormulaRecalcResult> results = Formula.recalculateFormulas(accounts);

   FormulaRecalcResult result0 = results[0];

   FormulaRecalcFieldError fieldError = result0.getErrors()[0];

```


Apex Reference Guide FormulaRecalcResult Class

```
   System.debug(fieldError.getFieldName()); // 'divide'

   System.debug(fieldError.getFieldError()); // 'Division by zero'

```

IN THIS SECTION:

#### FormulaRecalcResult Methods FormulaRecalcResult Methods The following are methods for FormulaRecalcResult .

IN THIS SECTION:

##### getErrors()

If an error occurs during formula recalculation, an array of one or more database error objects, along with error codes and descriptions,
is returned.

##### getSObject()

Returns the sObject with formulas recalculated.

##### isSuccess()

Returns a Boolean value that is set to `true` if the formula recalculation process completed successfully; otherwise, it is set to `false` .

##### getErrors()

If an error occurs during formula recalculation, an array of one or more database error objects, along with error codes and descriptions,
is returned.

Signature

```
   public List<System.FormulaRecalcFieldError> getErrors()

```

Return Value

Type: List<FormulaRecalcFieldError Class>

##### getSObject()

Returns the sObject with formulas recalculated.

Signature

```
   public SObject getSObject()

```

Return Value

Type: SObject

##### isSuccess()

Returns a Boolean value that is set to `true` if the formula recalculation process completed successfully; otherwise, it is set to `false` .


### Apex Reference Guide Http Class

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### Http Class Use the Http class to initiate an HTTP request and response.

Namespace

System

#### Http Methods

### The following are methods for Http . All are instance methods.

IN THIS SECTION:

##### send(request)

Sends an HttpRequest and returns the response.

##### toString()

Returns a string that displays and identifies the object's properties.

##### send(request)

Sends an HttpRequest and returns the response.

Signature

```
   public HttpResponse send(HttpRequest request)

```

Parameters

```
   request
```

Type: System.HttpRequest

Return Value

Type: System.HttpResponse

##### toString()

Returns a string that displays and identifies the object's properties.


### Apex Reference Guide HttpCalloutMock Interface

Signature

```
   public String toString()

```

Return Value

Type: String

### HttpCalloutMock Interface

Enables sending fake responses when testing HTTP callouts.

Namespace

System

Usage

### For an implementation example, see Testing HTTP Callouts by Implementing the HttpCalloutMock Interface.

#### HttpCalloutMock Methods

### The following are methods for HttpCalloutMock .

IN THIS SECTION:

##### respond(request)

Returns an HTTP response for the given request. The implementation of this method is called by the Apex runtime to send a fake
response when an HTTP callout is made after `Test.setMock` has been called.

##### respond(request)

Returns an HTTP response for the given request. The implementation of this method is called by the Apex runtime to send a fake response
when an HTTP callout is made after `Test.setMock` has been called.

Signature

```
   public HttpResponse respond(HttpRequest request)

```

Parameters

```
   request
```

Type: System.HttpRequest

Return Value

Type: System.HttpResponse


### Apex Reference Guide HttpRequest Class HttpRequest Class Use the HttpRequest class to programmatically create HTTP requests like GET, POST, PATCH, PUT, and DELETE.

Namespace

System

Usage

### Use the XML classes or JSON classes to parse XML or JSON content in the body of a request created by HttpRequest .

Example

The following example illustrates how you can use an authorization header with a request and handle the response.

```
   public with sharing class AuthCallout {

     public void basicAuthCallout(){

      HttpRequest req = new HttpRequest();

      req.setEndpoint('http://www.yahoo.com');

      req.setMethod('GET');

      // Specify the required user name and password to access the endpoint

      // As well as the header and header information

      String username = 'myname';

      String password = 'mypwd';

      Blob headerValue = Blob.valueOf(username + ':' + password);

      String authorizationHeader = 'Basic ' +

      EncodingUtil.base64Encode(headerValue);

      req.setHeader('Authorization', authorizationHeader);

      // Create a new http object to send the request object

      // A response object is generated as a result of the request

      Http http = new Http();

      HTTPResponse res = http.send(req);

      System.debug(res.getBody());

     }

   }

```

Note: You can set the endpoint as a named credential URL. A named credential URL contains the scheme `callout:`, the name
of the named credential, and an optional path. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ . A named
credential specifies the URL of a callout endpoint and its required authentication parameters in one definition. Salesforce manages
all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to. See
[Named Credentials as Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)


Apex Reference Guide HttpRequest Class

Compression

To compress the data you send, use `setCompressed` .

```
   HttpRequest req = new HttpRequest();

   req.setEndPoint(' my_endpoint ');

   req.setCompressed(true);

   req.setBody(' some post body ');

```

If a response comes back in compressed format, `getBody` recognizes the format, uncompresses it, and returns the uncompressed
value.

IN THIS SECTION:

#### HttpRequest Constructors HttpRequest Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_methods_system_json_overview.htm)_ : JSON Support

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_xml_support.htm)_ : XML Support

#### HttpRequest Constructors The following are constructors for HttpRequest .

IN THIS SECTION:

##### HttpRequest()
#### Creates a new instance of the HttpRequest class.

##### HttpRequest()

#### Creates a new instance of the HttpRequest class.

Signature

```
   public HttpRequest()

#### HttpRequest Methods The following are methods for HttpRequest . All are instance methods.

```

IN THIS SECTION:

getBody()
Retrieves the body of this request.

getBodyAsBlob()
Retrieves the body of this request as a Blob.


Apex Reference Guide HttpRequest Class

getBodyDocument()
Retrieves the body of this request as a DOM document.

getCompressed()
If `true`, the request body is compressed, `false` otherwise.

getEndpoint()
Retrieves the URL for the endpoint of the external server for this request.

getHeader(key)
Retrieves the contents of the request header.

getMethod()
Returns the type of method used by `HttpRequest` .

setBody(body)
Sets the contents of the body for this request.

setBodyAsBlob(body)
Sets the contents of the body for this request using a Blob.

setBodyDocument(document)
Sets the contents of the body for this request. The contents represent a DOM document.

setClientCertificate(clientCert, password)
This method is deprecated. Use `setClientCertificateName` instead.

setClientCertificateName(certDevName)
If the external service requires a client certificate for authentication, set the certificate name.

setCompressed(flag)
If `true`, the data in the body is delivered to the endpoint in the gzip compressed format. If `false`, no compression format is used.

setEndpoint(endpoint)
Specifies the endpoint for this request.

setHeader(key, value)
Sets the contents of the request header.

setMethod(method)
Sets the type of method to be used for the HTTP request.

setTimeout(timeout)
Sets a timeout for the request between 1 and 120,000 milliseconds. The timeout is the maximum time to wait for establishing the
HTTP connection. The same timeout is used for waiting for the request to start. When the request is executing, such as retrieving or
posting data, the connection is kept alive until the request finishes.

toString()
Returns a string containing the URL for the endpoint of the external server for this request and the method used, for example,

```
    Endpoint=http://YourServer, Method=POST

##### getBody()

```

Retrieves the body of this request.


Apex Reference Guide HttpRequest Class

Signature

```
   public String getBody()

```

Return Value

Type: String

##### getBodyAsBlob()

Retrieves the body of this request as a Blob.

Signature

```
   public Blob getBodyAsBlob()

```

Return Value

Type: Blob

##### getBodyDocument()

Retrieves the body of this request as a DOM document.

Signature

```
   public Dom.Document getBodyDocument()

```

Return Value

Type: Dom.Document

Example

Use this method as a shortcut for:

```
   String xml = httpRequest.getBody();

   Dom.Document domDoc = new Dom.Document(xml);

##### getCompressed()

```

If `true`, the request body is compressed, `false` otherwise.

Signature

```
   public Boolean getCompressed()

```

Return Value

Type: Boolean


Apex Reference Guide HttpRequest Class

##### getEndpoint()

Retrieves the URL for the endpoint of the external server for this request.

Signature

```
   public String getEndpoint()

```

Return Value

Type: String

##### getHeader(key)

Retrieves the contents of the request header.

Signature

```
   public String getHeader(String key)

```

Parameters

```
   key
```

Type: String

Return Value

Type: String

##### getMethod()

Returns the type of method used by `HttpRequest` .

Signature

```
   public String getMethod()

```

Return Value

Type: String

Usage

Examples of return values:

**•** DELETE

**•** GET

**•** HEAD

**•** PATCH

**•** POST

**•** PUT


Apex Reference Guide HttpRequest Class

**•** TRACE

##### setBody(body)

Sets the contents of the body for this request.

Signature

```
   public Void setBody(String body)

```

Parameters

```
   body
```

Type: String

Return Value

Type: Void

Usage

Limit: 6 MB for synchronous Apex or 12 MB for asynchronous Apex.

The HTTP request and response sizes count towards the total heap size.

##### setBodyAsBlob(body)

Sets the contents of the body for this request using a Blob.

Signature

```
   public Void setBodyAsBlob(Blob body)

```

Parameters

```
   body
```

Type: Blob

Return Value

Type: Void

Usage

Limit: 6 MB for synchronous Apex or 12 MB for asynchronous Apex.

The HTTP request and response sizes count towards the total heap size.

##### setBodyDocument(document)

Sets the contents of the body for this request. The contents represent a DOM document.


Apex Reference Guide HttpRequest Class

Signature

```
   public Void setBodyDocument(Dom.Document document)

```

Parameters

```
   document
```

Type: Dom.Document

Return Value

Type: Void

Usage

Limit: 6 MB for synchronous Apex or 12 MB for asynchronous Apex.

##### setClientCertificate(clientCert, password) This method is deprecated. Use setClientCertificateName instead.

Signature

```
   public Void setClientCertificate(String clientCert, String password)

```

Parameters

```
   clientCert
```

Type: String

```
   password
```

Type: String

Return Value

Type: Void

Usage

If the server requires a client certificate for authentication, set the client certificate PKCS12 key store and password.

##### setClientCertificateName(certDevName)

If the external service requires a client certificate for authentication, set the certificate name.

Signature

```
   public Void setClientCertificateName(String certDevName)

```


Apex Reference Guide HttpRequest Class

Parameters

```
   certDevName
```

Type: String

Return Value

Type: Void

Usage

[See Using Certificates with HTTP Requests.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_client_certs_http.htm)

##### setCompressed(flag)

If `true`, the data in the body is delivered to the endpoint in the gzip compressed format. If `false`, no compression format is used.

Signature

```
   public Void setCompressed(Boolean flag)

```

Parameters

```
   flag
```

Type: Boolean

Return Value

Type: Void

##### setEndpoint(endpoint)

Specifies the endpoint for this request.

Signature

```
   public Void setEndpoint(String endpoint)

```

Parameters

```
   endpoint
```

Type: String

Possible values for the endpoint:

**•** Endpoint URL

```
       https://my_endpoint.example.com/some_path

```

**•** Named credential URL, which contains the scheme `callout`, the name of the named credential, and, optionally, an appended
path

```
       callout:My_Named_Credential/some_path

```


Apex Reference Guide HttpRequest Class

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

##### setHeader(key, value)

Sets the contents of the request header.

Signature

```
   public Void setHeader(String key, String value)

```

Parameters

```
   key
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void

Usage

Limit 100 KB.

##### setMethod(method)

Sets the type of method to be used for the HTTP request.

Signature

```
   public Void setMethod(String method)

```

Parameters

```
   method
```

Type: String

Possible values for the method type include:

**•** DELETE

**•** GET

**•** HEAD

**•** PATCH

**•** POST


### Apex Reference Guide HttpResponse Class

**•** PUT

**•** TRACE

Return Value

Type: Void

Usage

You can also use this method to set any required options.

##### setTimeout(timeout)

Sets a timeout for the request between 1 and 120,000 milliseconds. The timeout is the maximum time to wait for establishing the HTTP
connection. The same timeout is used for waiting for the request to start. When the request is executing, such as retrieving or posting
data, the connection is kept alive until the request finishes.

Signature

```
   public Void setTimeout(Integer timeout)

```

Parameters

```
   timeout
```

Type: Integer

Return Value

Type: Void

##### toString()

Returns a string containing the URL for the endpoint of the external server for this request and the method used, for example,

```
   Endpoint=http://YourServer, Method=POST

```

Signature

```
   public String toString()

```

Return Value

Type: String

### HttpResponse Class Use the HttpResponse class to handle the HTTP response returned by the Http class.

Namespace

System


Apex Reference Guide HttpResponse Class

Usage

#### Use the XML classes or JSON Classes to parse XML or JSON content in the body of a response accessed by HttpResponse .

Example

In the following `getXmlStreamReader` example, content is retrieved via an HTTP callout, then the XML is parsed using
the `XmlStreamReader` class.

```
   public with sharing class ReaderFromCalloutSample {

      public void getAndParse() {

        // Get the XML document from the endpoint

        Http http = new Http();

        HttpRequest req = new HttpRequest();

        req.setEndpoint(URL.getOrgDomainUrl().toExternalForm() + '/services/data');

        req.setMethod('GET');

        req.setHeader('Accept', 'application/xml');

        HttpResponse res = http.send(req);

        // Log the XML content

        System.debug(res.getBody());

        // Generate the HTTP response as an XML stream

        XmlStreamReader reader = res.getXmlStreamReader();

        // Read through the XML

        while(reader.hasNext()) {

           System.debug('Event Type:' + reader.getEventType());

           if (reader.getEventType() == XmlTag.START_ELEMENT) {

           System.debug(reader.getLocalName());

           }

        reader.next();

        }

     }

   }

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_methods_system_json_overview.htm)_ : JSON Support

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_xml_support.htm)_ : XML Support

#### HttpResponse Methods The following are methods for HttpResponse . All are instance methods.

IN THIS SECTION:

getBody()
Retrieves the body returned in the response.


Apex Reference Guide HttpResponse Class

getBodyAsBlob()
Retrieves the body returned in the response as a Blob.

getBodyDocument()
Retrieves the body returned in the response as a DOM document.

getHeader(key)
Retrieves the contents of the response header.

getHeaderKeys()
Retrieves an array of header keys returned in the response.

getStatus()
Retrieves the status message returned for the response.

getStatusCode()
Retrieves the value of the status code returned in the response.

getXmlStreamReader()
Returns an `XmlStreamReader` that parses the body of the callout response.

setBody(body)
Specifies the body returned in the response.

setBodyAsBlob(body)
Specifies the body returned in the response using a Blob.

setHeader(key, value)
Specifies the contents of the response header.

setStatus(status)
Specifies the status message returned in the response.

setStatusCode(statusCode)
Specifies the value of the status code returned in the response.

toString()
Returns the status message and status code returned in the response, for example:

##### getBody()

Retrieves the body returned in the response.

Signature

```
   public String getBody()

```

Return Value

Type: String

Usage

Limit 6 MB for synchronous Apex or 12 MB for asynchronous Apex. The HTTP request and response sizes count towards the total heap
size.


Apex Reference Guide HttpResponse Class

##### getBodyAsBlob()

Retrieves the body returned in the response as a Blob.

Signature

```
   public Blob getBodyAsBlob()

```

Return Value

Type: Blob

Usage

Limit 6 MB for synchronous Apex or 12 MB for asynchronous Apex. The HTTP request and response sizes count towards the total heap
size.

##### getBodyDocument()

Retrieves the body returned in the response as a DOM document.

Signature

```
   public Dom.Document getBodyDocument()

```

Return Value

Type: `Dom.Document`

Example

Use it as a shortcut for:

```
   String xml = httpResponse.getBody();

   Dom.Document domDoc = new Dom.Document(xml);

##### getHeader(key)

```

Retrieves the contents of the response header.

Signature

```
   public String getHeader(String key)

```

Parameters

```
   key
```

Type: String

Return Value

Type: String


Apex Reference Guide HttpResponse Class

##### getHeaderKeys()

Retrieves an array of header keys returned in the response.

Signature

```
   public String[] getHeaderKeys()

```

Return Value

Type: String[]

##### getStatus()

Retrieves the status message returned for the response.

Signature

```
   public String getStatus()

```

Return Value

Type: String

##### getStatusCode()

Retrieves the value of the status code returned in the response.

Signature

```
   public Integer getStatusCode()

```

Return Value

Type: Integer

##### getXmlStreamReader()

Returns an `XmlStreamReader` that parses the body of the callout response.

Signature

```
   public XmlStreamReader getXmlStreamReader()

```

Return Value

Type: System.XmlStreamReader


Apex Reference Guide HttpResponse Class

Usage

Use it as a shortcut for:

```
   String xml = httpResponse.getBody();

   XmlStreamReader xsr = new XmlStreamReader(xml);

##### setBody(body)

```

Specifies the body returned in the response.

Signature

```
   public Void setBody(String body)

```

Parameters

```
   body
```

Type: String

Return Value

Type: Void

##### setBodyAsBlob(body)

Specifies the body returned in the response using a Blob.

Signature

```
   public Void setBodyAsBlob(Blob body)

```

Parameters

```
   body
```

Type: Blob

Return Value

Type: Void

##### setHeader(key, value)

Specifies the contents of the response header.

Signature

```
   public Void setHeader(String key, String value)

```


Apex Reference Guide HttpResponse Class

Parameters

```
   key
```

Type: String

```
   value
```

Type: String

Return Value

Type: Void

##### setStatus(status)

Specifies the status message returned in the response.

Signature

```
   public Void setStatus(String status)

```

Parameters

```
   status
```

Type: String

Return Value

Type: Void

##### setStatusCode(statusCode)

Specifies the value of the status code returned in the response.

Signature

```
   public Void setStatusCode(Integer statusCode)

```

Parameters

```
   statusCode
```

Type: Integer

Return Value

Type: Void

##### toString()

Returns the status message and status code returned in the response, for example:


### Apex Reference Guide Id Class

Signature

```
   public String toString()

```

Return Value

Type: String

Example

```
   Status=OK, StatusCode=200

### Id Class

```

Contains methods for the ID primitive data type.

Namespace

System

Example: Getting an sObject Token From an ID

This sample shows how to use the `getSObjectType` method to obtain an sObject token from an ID. The `updateOwner` method
in this sample accepts a list of IDs of the sObjects to update the ownerId field of. This list contains IDs of sObjects of the same type. The
second parameter is the new owner ID. Note that since it is a future method, it doesn’t accept sObject types as parameters; this is why
it accepts IDs of sObjects. This method gets the sObject token from the first ID in the list, then does a describe to obtain the object name
and constructs a query dynamicallly. It then queries for all sObjects and updates their owner ID fields to the new owner ID.

```
   public class MyDynamicSolution {

      @future

      public static void updateOwner(List<ID> objIds, ID newOwnerId) {

        // Validate input

        System.assert(objIds != null);

        System.assert(objIds.size() > 0);

        System.assert(newOwnerId != null);

        // Get the sObject token from the first ID

        // (the List contains IDs of sObjects of the same type).

        Schema.SObjectType token = objIds[0].getSObjectType();

        // Using the token, do a describe

        // and construct a query dynamically.

        Schema.DescribeSObjectResult dr = token.getDescribe();

        String queryString = 'SELECT ownerId FROM ' + dr.getName() +

           ' WHERE ';

        for(ID objId : objIds) {

           queryString += 'Id=\'' + objId + '\' OR ';

        }

        // Remove the last ' OR'

        queryString = queryString.subString(0, queryString.length() - 4);

        sObject[] objDBList = Database.query(queryString);

```


Apex Reference Guide Id Class

```
        System.assert(objDBList.size() > 0);

        // Update the owner ID on the sObjects

        for(Integer i=0;i<objDBList.size();i++) {

           objDBList[i].put('ownerId', newOwnerId);

        }

        Database.SaveResult[] srList = Database.update(objDBList, false);

        for(Database.SaveResult sr : srList) {

           if (sr.isSuccess()) {

             System.debug('Updated owner ID successfully for ' +

               dr.getName() + ' ID ' + sr.getId());

           }

           else {

            System.debug('Updating ' + dr.getName() + ' returned the following errors.');

             for(Database.Error e : sr.getErrors()) {

               System.debug(e.getMessage());

             }

           }

        }

      }

   }

#### Id Methods The following are methods for Id .

```

IN THIS SECTION:

addError(errorMsg)
Marks a trigger record with a custom error message and prevents any DML operation from occurring.

addError(errorMsg, escape)
Marks a trigger record with a custom error message, specifies if the error message should be escaped, and prevents any DML operation
from occurring.

addError(exceptionError)
Marks a trigger record with a custom error message and prevents any DML operation from occurring.

addError(exceptionError, escape)
Marks a trigger record with a custom error message and prevents any DML operation from occurring.

getSObjectType()
Returns the token for the sObject corresponding to this ID. This method is primarily used with describe information.

to15()
Converts an 18-character Id value to a 15-character case-sensitive string.

valueOf(toID)
Converts the specified String into an ID and returns the ID.

valueOf(str, restoreCasing)
Converts the specified string into an ID and returns the ID. If `restoreCasing` is `true`, and the string represents an 18-character
ID that has incorrect casing, the method returns an 18-character ID that is correctly aligned with its encoded casing.


Apex Reference Guide Id Class

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

##### This method is similar to the addError(errorMsg) sObject method.

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

Example

```
   Trigger.new[0].Id.addError('bad');

##### addError(errorMsg, escape)

```

Marks a trigger record with a custom error message, specifies if the error message should be escaped, and prevents any DML operation
from occurring.

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


Apex Reference Guide Id Class

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
   Trigger.new[0].Id.addError('Fix & resubmit', false);

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

Usage

##### This method is similar to the addError(exceptionError) sObject method.

This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`,
`\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user interface.

Example

```
   public class MyException extends Exception{}

   Trigger.new[0].Id.addError(new myException('Invalid Id'));

```


Apex Reference Guide Id Class

##### addError(exceptionError, escape)

Marks a trigger record with a custom error message and prevents any DML operation from occurring.

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
content, such as input field values. Otherwise, specify `true` for the _`escape`_ argument or call `addError(Exception` _**`e`**_ `)`
instead.

Example

```
   public class MyException extends Exception{}

   account a = new account();

   a.addError(new MyException('Invalid Id & other issues'), false);

##### getSObjectType()

```

Returns the token for the sObject corresponding to this ID. This method is primarily used with describe information.

Signature

```
   public Schema.SObjectType getSObjectType()

```


Apex Reference Guide Id Class

Return Value

Type: Schema.SObjectType

Usage

[For more information about describes, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

Example

```
   account a = new account(name = 'account');

   insert a;

   Id myId = a.id;

   system.assertEquals(Schema.Account.SObjectType, myId.getSobjectType());

##### to15()

```

Converts an 18-character Id value to a 15-character case-sensitive string.

Signature

```
   public static string to15()

```

Return Value

Type: String

Example

```
   String Id_15_char = '0D5B000001DVM9t';

   String Id_18_char = '0D5B000001DVM9tkAh';

   ID testId = Id_18_char;

   System.assertEquals(testId.to15(),Id_15_char);

##### valueOf(toID)

```

Converts the specified String into an ID and returns the ID.

Signature

```
   public static ID valueOf(String toID)

```

Parameters

```
   toID
```

Type: String

Return Value

Type: ID


### Apex Reference Guide Ideas Class

Example

```
   Id myId = Id.valueOf('001xa000003DIlo');

```

Versioned Behavior Changes

In API version 54.0 and later, assignment of an invalid 15 or 18 character ID to a variable results in a `System.StringException`
exception.

##### **`valueOf(str, restoreCasing)`**

Converts the specified string into an ID and returns the ID. If `restoreCasing` is `true`, and the string represents an 18-character
ID that has incorrect casing, the method returns an 18-character ID that is correctly aligned with its encoded casing.

Signature

```
   public static Id valueOf(String str, Boolean restoreCasing)

```

Parameters

```
   str
```

Type: String

String to be converted to an ID

```
   restoreCasing
```

Type: Boolean

If set to `true`, and _`str`_ represents an 18-character ID, the method returns an 18-character ID that is correctly aligned with its
casing.

Return Value

Type: Id

The return value depends on both the _`str`_ and the _`restoreCasing`_ parameter values.

Note: If the _`str`_ is invalid, the method throws a `System.StringException` exception.

### Ideas Class

Represents zone ideas.


Apex Reference Guide Ideas Class

Namespace

System

Usage

Ideas is a zone of users who post, vote for, and comment on ideas. An Ideas zone provides an online, transparent way for you to attract,
manage, and showcase innovation.

A set of _recent replies_ (returned by methods, see below) includes ideas that a user posted or commented on that already have comments
posted by another user. The returned ideas are listed based on the time of the last comment made by another user, with the most recent
ideas appearing first.

The _`userID`_ argument is a required argument that filters the results so only the ideas that the specified user has posted or commented
on are returned.

The _`communityID`_ argument filters the results so only the ideas within the specified zone are returned. If this argument is the empty
string, then all recent replies for the specified user are returned regardless of the zone.

For more information on ideas, see “Using Ideas” in the Salesforce online help.

Example

The following example finds ideas in a specific zone that have similar titles as a new idea:

```
   public class FindSimilarIdeasController {

     public static void test() {

       // Instantiate a new idea

       Idea idea = new Idea ();

       // Specify a title for the new idea

       idea.Title = 'Increase Vacation Time for Employees';

       // Specify the communityID (INTERNAL_IDEAS) in which to find similar ideas.

       Community community = [ SELECT Id FROM Community WHERE Name = 'INTERNAL_IDEAS' ];

       idea.CommunityId = community.Id;

       ID[] results = Ideas.findSimilar(idea);

     }

   }

```

The following example uses a Visualforce page in conjunction with a _custom controller_, that is, a special Apex class. For more information
[on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

This example creates an Apex method in the controller that returns unread recent replies. You can leverage this same example for the
`getAllRecentReplies` and `getReadRecentReplies` methods. For this example to work, there must be ideas posted to
the zone. In addition, at least one zone member must have posted a comment to another zone member's idea or comment.

```
   // Create an Apex method to retrieve the recent replies marked as unread in all communities

   public class IdeasController {

     public Idea[] getUnreadRecentReplies() {

        Idea[] recentReplies;

        if (recentReplies == null) {

```


Apex Reference Guide Ideas Class

```
         Id[] recentRepliesIds = Ideas.getUnreadRecentReplies(UserInfo.getUserId(), '');

          recentReplies = [SELECT Id, Title FROM Idea WHERE Id IN :recentRepliesIds];

        }

        return recentReplies;

     }

   }

```

The following is the markup for a Visualforce page that uses the above custom controller to list unread recent replies.

```
   <apex:page controller="IdeasController" showHeader="false">

      <apex:dataList value="{!unreadRecentReplies}" var="recentReplyIdea">

          <a href="/apex/viewIdea?id={!recentReplyIdea.Id}">

              <apex:outputText value="{!recentReplyIdea.Title}" escape="true"/></a>

      </apex:dataList>

   </apex:page>

```

The following example uses a Visualforce page in conjunction with a custom controller to list ideas. Then, a second Visualforce page
and custom controller is used to display a specific idea and mark it as read. For this example to work, there must be ideas posted to the
zone.

```
   // Create a controller to use on a VisualForce page to list ideas

   public class IdeaListController {

      public final Idea[] ideas {get; private set;}

      public IdeaListController() {

        Integer i = 0;

        ideas = new Idea[10];

        for (Idea tmp : Database.query

   ('SELECT Id, Title FROM Idea WHERE Id != null AND parentIdeaId = null LIMIT 10')) {

           i++;

           ideas.add(tmp);

        }

      }

   }

```

The following is the markup for a Visualforce page that uses the above custom controller to list ideas:

```
   <apex:page controller="IdeaListController" tabStyle="Idea" showHeader="false">

        <apex:dataList value="{!ideas}" var="idea" id="ideaList">

           <a href="/apex/viewIdea?id={!idea.id}">

   <apex:outputText value="{!idea.title}" escape="true"/></a>

        </apex:dataList>

   </apex:page>

```

The following example also uses a Visualforce page and custom controller, this time, to display the idea that is selected on the above
idea list page. In this example, the `markRead` method marks the selected idea and associated comments as read by the user that is
currently logged in. Note that the `markRead` method is in the constructor so that the idea is marked read immediately when the user


Apex Reference Guide Ideas Class

goes to a page that uses this controller. For this example to work, there must be ideas posted to the zone. In addition, at least one zone
member must have posted a comment to another zone member's idea or comment.

```
   // Create an Apex method in the controller that marks all comments as read for the

   // selected idea

   public class ViewIdeaController {

     private final String id = System.currentPage().getParameters().get('id');

     public ViewIdeaController(ApexPages.StandardController controller) {

             Ideas.markRead(id);

     }

   }

```

The following is the markup for a Visualforce page that uses the above custom controller to display the idea as read.

```
   <apex:page standardController="Idea" extensions="ViewIdeaController" showHeader="false">

      <h2><apex:outputText value="{!idea.title}" /></h2>

      <apex:outputText value="{!idea.body}" />

   </apex:page>

#### Ideas Methods The following are methods for Ideas . All methods are static.

```

IN THIS SECTION:

##### findSimilar(idea)

Returns a list of similar ideas based on the title of the specified idea.

getAllRecentReplies(userID, communityID)
Returns ideas that have recent replies for the specified user or zone. This includes all read and unread replies.

getReadRecentReplies(userID, communityID)
Returns ideas that have recent replies marked as read.

getUnreadRecentReplies(userID, communityID)
Returns ideas that have recent replies marked as unread.

markRead(ideaID)
Marks all comments as read for the user that is currently logged in.

##### findSimilar(idea)

Returns a list of similar ideas based on the title of the specified idea.

Signature

```
   public static ID[] findSimilar(Idea idea)

```


Apex Reference Guide Ideas Class

Parameters

```
   idea
```

Type: Idea

Return Value

Type: ID[]

Usage

Each `findSimilar` [call counts against the SOSL query limits. See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

##### getAllRecentReplies(userID, communityID)

Returns ideas that have recent replies for the specified user or zone. This includes all read and unread replies.

Signature

```
   public static ID[] getAllRecentReplies(String userID, String communityID)

```

Parameters

```
   userID
```

Type: String

```
   communityID
```

Type: String

Return Value

Type: ID[]

Usage

##### Each getAllRecentReplies call counts against the SOQL query limits. See Execution Governors and Limits. getReadRecentReplies(userID, communityID)

Returns ideas that have recent replies marked as read.

Signature

```
   public static ID[] getReadRecentReplies(String userID, String communityID)

```

Parameters

```
   userID
```

Type: String

```
   communityID
```

Type: String


### Apex Reference Guide InstallHandler Interface

Return Value

Type: ID[]

Usage

Each `getReadRecentReplies` [call counts against the SOQL query limits. See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

##### getUnreadRecentReplies(userID, communityID)

Returns ideas that have recent replies marked as unread.

Signature

```
   public static ID[] getUnreadRecentReplies(String userID, String communityID)

```

Parameters

```
   userID
```

Type: String

```
   communityID
```

Type: String

Return Value

Type: ID[]

Usage

##### Each getUnreadRecentReplies call counts against the SOQL query limits. See Execution Governors and Limits. markRead(ideaID)

Marks all comments as read for the user that is currently logged in.

Signature

```
   public static Void markRead(String ideaID)

```

Parameters

```
   ideaID
```

Type: String

Return Value

Type: Void

### InstallHandler Interface

Enables custom code to run after a managed package installation or upgrade.


Apex Reference Guide InstallHandler Interface

Namespace

System

Usage

App developers can implement this interface to specify Apex code that runs automatically after a subscriber installs or upgrades a
managed package. The package install or upgrade can be customized based on details of the subscriber’s organization. For instance,
you can use the script to populate custom settings, create sample data, send an email to the installer, notify an external system, or kick
off a batch operation to populate a new field across a large set of data.

The post install script is invoked after tests have been run, and is subject to default governor limits. It runs as a special system user that
represents your package, so all operations performed by the script appear to be done by your package. You can access this user by using
UserInfo. You only see this user at runtime, not while running tests.

If the script fails, the install or upgrade is aborted. Any errors in the script are emailed to the user specified in the **Notify on Apex Error**
field of the package. If no user is specified, the install or upgrade details are unavailable.

The post install script has the following additional properties.

**•** It can initiate batch, scheduled, and future jobs.

**•** It can’t access Session IDs.

**•** It can only perform callouts using an async operation. The callout occurs after the script is run and the install is complete and
committed.

**•** It can’t call another Apex class in the package if that Apex class uses the `with sharing` keyword. This keyword can prevent the
[package from successfully installing. To learn more, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

The `InstallHandler` interface has a single method called `onInstall`, which specifies the actions to be performed on install
or upgrade.

```
   public interface InstallHandler {

     void onInstall(InstallContext context)

   };

```

The `onInstall` method takes a context object as its argument, which provides the following information.

**•** The org ID of the organization in which the installation takes place.

**•** The user ID of the user who initiated the installation.

**•** The version number of the previously installed package (specified using the `Version` class). The version is always a three-part
number, such as 1.2.0.

**•** Whether the installation is an upgrade.

**•** Whether the installation is a push.

The context argument is an object whose type is the `InstallContext` interface. This interface is automatically implemented by
the system. The following definition of the `InstallContext` interface shows the methods you can call on the context argument.

```
   public interface InstallContext {

     ID organizationId();

     ID installerId();

     Boolean isUpgrade();

     Boolean isPush();

     Version previousVersion();

   }

```


Apex Reference Guide InstallHandler Interface

IN THIS SECTION:

#### InstallHandler Methods InstallHandler Example Implementation InstallHandler Methods The following are methods for InstallHandler .

IN THIS SECTION:

##### onInstall(context)

Specifies the actions to be performed on install/upgrade.

##### onInstall(context)

Specifies the actions to be performed on install/upgrade.

Signature

```
   public Void onInstall(InstallContext context)

```

Parameters

```
   context
```

Type: System.InstallContext

Return Value

Type: Void

#### InstallHandler Example Implementation

The following sample post install script performs these actions on package install/upgrade.

**•** If the previous version is null, that is, the package is being installed for the first time, the script:

**–** Creates a new Account called Newco and verifies that it was created.

**–** Creates a new instance of the custom object Survey, called Client Satisfaction Survey.

**–** Sends an email message to the subscriber confirming installation of the package.

**•** If the previous version is 1.0, the script creates a new instance of Survey called ”Upgrading from Version 1.0”.

**•** If the package is an upgrade, the script creates a new instance of Survey called ”Sample Survey during Upgrade”.

**•** If the upgrade is being pushed, the script creates a new instance of Survey called ”Sample Survey during Push”.

```
   public class PostInstallClass implements InstallHandler {

     global void onInstall(InstallContext context) {

      if(context.previousVersion() == null) {

       Account a = new Account(name='Newco');

       insert(a);

```


### Apex Reference Guide Integer Class

```
       Survey__c obj = new Survey__c(name='Client Satisfaction Survey');

       insert obj;

       User u = [Select Id, Email from User where Id =:context.installerID()];

       String toAddress= u.Email;

       String[] toAddresses = new String[]{toAddress};

       Messaging.SingleEmailMessage mail =

        new Messaging.SingleEmailMessage();

       mail.setToAddresses(toAddresses);

       mail.setReplyTo('support@package.dev');

       mail.setSenderDisplayName('My Package Support');

       mail.setSubject('Package install successful');

       mail.setPlainTextBody('Thanks for installing the package.');

       Messaging.sendEmail(new Messaging.Email[] { mail });

       }

      else

       if(context.previousVersion().compareTo(new Version(1,0)) == 0) {

       Survey__c obj = new Survey__c(name='Upgrading from Version 1.0');

       insert(obj);

       }

      if(context.isUpgrade()) {

       Survey__c obj = new Survey__c(name='Sample Survey during Upgrade');

       insert obj;

       }

      if(context.isPush()) {

       Survey__c obj = new Survey__c(name='Sample Survey during Push');

       insert obj;

       }

      }

     }

```

You can test a post install script using the new `testInstall` method of the `Test` class. This method takes the following arguments.

**•** A class that implements the `InstallHandler` interface.

**•** A `Version` object that specifies the version number of the existing package.

**•** An optional Boolean value that is `true` if the installation is a push. The default is `false` .

This sample shows how to test a post install script implemented in the `PostInstallClass` Apex class.

```
   @isTest

   static void testInstallScript() {

     PostInstallClass postinstall = new PostInstallClass();

      Test.testInstall(postinstall, null);

      Test.testInstall(postinstall, new Version(1,0), true);

      List<Account> a = [Select id, name from Account where name ='Newco'];

      System.assertEquals(1, a.size(), 'Account not found');

     }

### Integer Class

```

Contains methods for the Integer primitive data type.


Apex Reference Guide Integer Class

Namespace

System

Usage

[For more information on integers, see Integer Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Integer Methods The following are methods for Integer .

IN THIS SECTION:

##### format()

Returns the integer as a string using the locale of the context user.

##### valueOf(stringToInteger)

Returns an Integer that contains the value of the specified String. As in Java, the String is interpreted as representing a signed decimal
integer.

valueOf(fieldValue)
Converts the specified object to an Integer. Use this method to convert a history tracking field value or an object that represents an
Integer value.

##### format()

Returns the integer as a string using the locale of the context user.

Signature

```
   public String format()

```

Return Value

Type: String

Example

```
   integer myInt = 22;

   system.assertEquals('22', myInt.format());

##### valueOf(stringToInteger)

```

Returns an Integer that contains the value of the specified String. As in Java, the String is interpreted as representing a signed decimal
integer.

Signature

```
   public static Integer valueOf(String stringToInteger)

```


Apex Reference Guide Integer Class

Parameters

```
   stringToInteger
```

Type: String

Return Value

Type: Integer

Examples

```
   Integer myInt = Integer.valueOf('123');

```

A `TypeException` is returned if you attempt to convert a string to an invalid integer.

```
   String n = 'NotAnInteger';

   try {

      Integer myInt = Integer.valueOf(n);

   } catch (TypeException ex) {

      System.debug(LoggingLevel.Error, ex.getMessage());

   }

##### valueOf(fieldValue)

```

Converts the specified object to an Integer. Use this method to convert a history tracking field value or an object that represents an
Integer value.

Signature

```
   public static Integer valueOf(Object fieldValue)

```

Parameters

```
   fieldValue
```

Type: Object

Return Value

Type: Integer

Usage

Use this method with the `OldValue` or `NewValue` fields of history sObjects, such as `AccountHistory`, when the field type
corresponds to an Integer type, like a number field.

Example:

Example

```
   List<AccountHistory> ahlist =

     [SELECT Field,OldValue,NewValue

     FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

```


### Apex Reference Guide IntegrationTest Class (Developer Preview)

```
     System.debug('Field: ' + ah.Field);

     if (ah.field == 'NumberOfEmployees') {

      Integer oldValue =

       Integer.valueOf(ah.OldValue);

      Integer newValue =

       Integer.valueOf(ah.NewValue);

   }

### IntegrationTest Class (Developer Preview)

##### Contains the commitTestOnly() method that can be called from an @IntegrationMethod to commit data mid-transaction
```

so that it’s visible to service threads such as Agentforce and Data 360.

Namespace

System

Note: The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The
feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases
or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or
without notice. Don't implement functionality developed with these commands or tools in your production package.

IN THIS SECTION:

#### IntegrationTest Methods IntegrationTest Methods

### The following are methods for IntegrationTest .

IN THIS SECTION:

##### commitTestOnly()(Developer Preview)

Commits data to the database mid-transaction so it’s visible to service threads such as Agentforce and Data 360. It resets the
uncommitted work checkpoint and mixed DML tracking for the new transaction boundary. The method can only be called from an
`@IntegrationTest` method.

##### **`commitTestOnly()(Developer Preview)`**

Commits data to the database mid-transaction so it’s visible to service threads such as Agentforce and Data 360. It resets the uncommitted
work checkpoint and mixed DML tracking for the new transaction boundary. The method can only be called from an
`@IntegrationTest` method.

Note: The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The
feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases
or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or
without notice. Don't implement functionality developed with these commands or tools in your production package.


### Apex Reference Guide JSON Class

Signature

```
   public static void commitTestOnly()

```

Return Value

Type: void

SEE ALSO:

_Apex Developer Guide_ [: Apex Integration Tests for Agentforce and Data 360 Services (Developer Preview)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_integration_testing.htm)

### JSON Class

Contains methods for serializing Apex objects into JSON format and deserializing JSON content that was serialized using the `serialize`
method in this class.

Namespace

System

Usage

Use the methods in the `System.JSON` class to perform round-trip JSON serialization and deserialization of Apex objects.

SEE ALSO:

_Apex Developer Guide_ [: Roundtrip Serialization and Deserialization](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_json_json.htm)

#### JSON Methods

### The following are methods for JSON . All methods are static.

IN THIS SECTION:

createGenerator(prettyPrint)
Returns a new JSON generator.

createParser(jsonString)
Returns a new JSON parser.

deserialize(jsonString, apexType)
Deserializes the specified JSON string into an Apex object of the specified type.

deserializeStrict(jsonString, apexType)
Deserializes the specified JSON string into an Apex object of the specified type.

deserializeUntyped(jsonString)
Deserializes the specified JSON string into collections of primitive data types.

serialize(objectToSerialize)
Serializes Apex objects into JSON content.


Apex Reference Guide JSON Class

serialize(objectToSerialize, suppressApexObjectNulls)
Suppresses `null` values when serializing Apex objects into JSON content.

serializePretty(objectToSerialize)
Serializes Apex objects into JSON content and generates indented content using the pretty-print format.

serializePretty(objectToSerialize, suppressApexObjectNulls)
Suppresses `null` values when serializing Apex objects into JSON content and generates indented content using the pretty-print
format.

##### createGenerator(prettyPrint)

Returns a new JSON generator.

Signature

```
   public static System.JSONGenerator createGenerator(Boolean prettyPrint)

```

Parameters

```
   prettyPrint
```

Type: Boolean

Determines whether the JSON generator creates JSON content in pretty-print format with the content indented. Set to `true` to
create indented content.

Return Value

Type: System.JSONGenerator

##### createParser(jsonString)

Returns a new JSON parser.

Signature

```
   public static System.JSONParser createParser(String jsonString)

```

Parameters

```
   jsonString
```

Type: String

The JSON content to parse.

Return Value

Type: System.JSONParser

##### deserialize(jsonString, apexType)

Deserializes the specified JSON string into an Apex object of the specified type.


Apex Reference Guide JSON Class

Signature

```
   public static Object deserialize(String jsonString, System.Type apexType)

```

Parameters

```
   jsonString
```

Type: String

The JSON content to deserialize.

```
   apexType
```

Type: System.Type

The Apex type of the object that this method creates after deserializing the JSON content.

Return Value

Type: Object

Usage

If the JSON content contains attributes not present in the `System.Type` argument, such as a missing field or object, deserialization
fails in some circumstances. When deserializing JSON content into a custom object or an sObject using Salesforce API version 34.0 or
earlier, this method throws a runtime exception when passed extraneous attributes. When deserializing JSON content into an Apex class
in any API version, or into an object in API version 35.0 or later, no exception is thrown. When no exception is thrown, this method ignores
extraneous attributes and parses the rest of the JSON content.

Example

The following example deserializes a `Decimal` value.

```
   Decimal n = (Decimal)JSON.deserialize(

            '100.1', Decimal.class);

   System.assertEquals(n, 100.1);

##### deserializeStrict(jsonString, apexType)

```

Deserializes the specified JSON string into an Apex object of the specified type.

Signature

```
   public static Object deserializeStrict(String jsonString, System.Type apexType)

```

Parameters

```
   jsonString
```

Type: String

The JSON content to deserialize.

```
   apexType
```

Type: System.Type

The Apex type of the object that this method creates after deserializing the JSON content.


Apex Reference Guide JSON Class

Return Value

Type: Object

Usage

All attributes in the JSON string must be present in the specified type. If the JSON content contains attributes not present in the
`System.Type` argument, such as a missing field or object, deserialization fails in some circumstances. When deserializing JSON
content with extraneous attributes into an Apex class, this method throws an exception in all API versions. However, no exception is
thrown when you use this method to deserialize JSON content into a custom object or an sObject.

Example

The following example deserializes a JSON string into an object of a user-defined type represented by the `Car` class, which this example
also defines.

```
   public class Car {

      public String make;

      public String year;

   }

   public void parse() {

      Car c = (Car)JSON.deserializeStrict(

        '{"make":"SFDC","year":"2020"}',

        Car.class);

      System.assertEquals(c.make, 'SFDC');

      System.assertEquals(c.year, '2020');

   }

##### deserializeUntyped(jsonString)

```

Deserializes the specified JSON string into collections of primitive data types.

Signature

```
   public static Object deserializeUntyped(String jsonString)

```

Parameters

```
   jsonString
```

Type: String

The JSON content to deserialize.

Return Value

Type: Object


Apex Reference Guide JSON Class

Example

The following example deserializes a JSON representation of an appliance object into a map that contains primitive data types and
further collections of primitive types. It then verifies the deserialized values.

```
   String jsonInput = '{\n' +

      ' "description" :"An appliance",\n' +

      ' "accessories" : [ "powerCord", ' +

       '{ "right":"door handle1", ' +

        '"left":"door handle2" } ],\n' +

      ' "dimensions" : ' +

       '{ "height" : 5.5, ' +

        '"width" : 3.0, ' +

        '"depth" : 2.2 },\n' +

      ' "type" : null,\n' +

      ' "inventory" : 2000,\n' +

      ' "price" : 1023.45,\n' +

      ' "isShipped" : true,\n' +

      ' "modelNumber" : "123"\n' +

      '}';

   Map<String, Object> m =

     (Map<String, Object>)

       JSON.deserializeUntyped(jsonInput);

   System.assertEquals(

     'An appliance', m.get('description'));

   List<Object> a =

     (List<Object>)m.get('accessories');

   System.assertEquals('powerCord', a[0]);

   Map<String, Object> a2 =

     (Map<String, Object>)a[1];

   System.assertEquals(

     'door handle1', a2.get('right'));

   System.assertEquals(

     'door handle2', a2.get('left'));

   Map<String, Object> dim =

     (Map<String, Object>)m.get('dimensions');

   System.assertEquals(

     5.5, dim.get('height'));

   System.assertEquals(

     3.0, dim.get('width'));

   System.assertEquals(

     2.2, dim.get('depth'));

   System.assertEquals(null, m.get('type'));

   System.assertEquals(

     2000, m.get('inventory'));

   System.assertEquals(

     1023.45, m.get('price'));

   System.assertEquals(

     true, m.get('isShipped'));

```


Apex Reference Guide JSON Class

```
   System.assertEquals(

     '123', m.get('modelNumber'));

##### serialize(objectToSerialize)

```

Serializes Apex objects into JSON content.

Signature

```
   public static String serialize(Object objectToSerialize)

```

Parameters

```
   objectToSerialize
```

Type: Object

The Apex object to serialize.

Return Value

Type: String

Example

The following example serializes a new `Datetime` value.

```
   Datetime dt = Datetime.newInstance(

            Date.newInstance(

              2011, 3, 22),

            Time.newInstance(

              1, 15, 18, 0));

      String str = JSON.serialize(dt);

      System.assertEquals(

        '"2011-03-22T08:15:18.000Z"',

        str);

##### serialize(objectToSerialize, suppressApexObjectNulls)

```

Suppresses `null` values when serializing Apex objects into JSON content.

Signature

```
   public static String serialize(Object objectToSerialize, Boolean suppressApexObjectNulls)

```

Parameters

```
   objectToSerialize
```

Type: Object

The Apex object to serialize.

```
   suppressApexObjectNulls
```

Type: Boolean


Apex Reference Guide JSON Class

If true, remove `null` values before serializing the JSON object.

Note: This parameter doesn’t apply to sObjects retrieved via SOQL.

Return Value

Type: String

Usage

This method allows you to specify whether to suppress `null` values when serializing Apex objects into JSON content.

##### serializePretty(objectToSerialize)

Serializes Apex objects into JSON content and generates indented content using the pretty-print format.

Signature

```
   public static String serializePretty(Object objectToSerialize)

```

Parameters

```
   objectToSerialize
```

Type: Object

The Apex object to serialize.

Return Value

Type: String

##### serializePretty(objectToSerialize, suppressApexObjectNulls)

Suppresses `null` values when serializing Apex objects into JSON content and generates indented content using the pretty-print format.

Signature

```
   public static String serializePretty(Object objectToSerialize, Boolean

   suppressApexObjectNulls)

```

Parameters

```
   objectToSerialize
```

Type: Object

The Apex object to serialize.

```
   suppressApexObjectNulls
```

Type: Boolean

If true, remove `null` values before serializing the JSON object.

Note: This parameter doesn’t apply to sObjects retrieved via SOQL.


### Apex Reference Guide JSONGenerator Class

Return Value

Type: String

### JSONGenerator Class

Contains methods used to serialize objects into JSON content using the standard JSON encoding.

Namespace

System

Usage

The `System.JSONGenerator` class is provided to enable the generation of standard JSON-encoded content and gives you more
control on the structure of the JSON output.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_json_jsongenerator.htm)_ : JSON Generator

#### JSONGenerator Methods

### The following are methods for JSONGenerator . All are instance methods.

IN THIS SECTION:

close()
Closes the JSON generator.

getAsString()
Returns the generated JSON content.

isClosed()
Returns `true` if the JSON generator is closed; otherwise, returns `false` .

writeBlob(blobValue)
Writes the specified `Blob` value as a base64-encoded string.

writeBlobField(fieldName, blobValue)
Writes a field name and value pair using the specified field name and BLOB value.

writeBoolean(blobValue)
Writes the specified Boolean value.

writeBooleanField(fieldName, booleanValue)
Writes a field name and value pair using the specified field name and Boolean value.

writeDate(dateValue)
Writes the specified date value in the ISO-8601 format.

writeDateField(fieldName, dateValue)
Writes a field name and value pair using the specified field name and date value. The date value is written in the ISO-8601 format.


Apex Reference Guide JSONGenerator Class

writeDateTime(datetimeValue)
Writes the specified date and time value in the ISO-8601 format.

writeDateTimeField(fieldName, datetimeValue)
Writes a field name and value pair using the specified field name and date and time value. The date and time value is written in the
ISO-8601 format.

writeEndArray()
Writes the ending marker of a JSON array (']').

writeEndObject()
Writes the ending marker of a JSON object ('}').

writeFieldName(fieldName)
Writes a field name.

writeId(identifier)
Writes the specified ID value.

writeIdField(fieldName, identifier)
Writes a field name and value pair using the specified field name and identifier value.

writeNull()
Writes the JSON null literal value.

writeNullField(fieldName)
Writes a field name and value pair using the specified field name and the JSON null literal value.

writeNumber(number)
Writes the specified decimal value.

writeNumber(number)
Writes the specified double value.

writeNumber(number)
Writes the specified integer value.

writeNumber(number)
Writes the specified long value.

writeNumberField(fieldName, number)
Writes a field name and value pair using the specified field name and decimal value.

writeNumberField(fieldName, number)
Writes a field name and value pair using the specified field name and double value.

writeNumberField(fieldName, number)
Writes a field name and value pair using the specified field name and integer value.

writeNumberField(fieldName, number)
Writes a field name and value pair using the specified field name and long value.

writeObject(anyObject)
Writes the specified Apex object in JSON format.

writeObjectField(fieldName, value)
Writes a field name and value pair using the specified field name and Apex object.

writeStartArray()
Writes the starting marker of a JSON array ('[').


Apex Reference Guide JSONGenerator Class

writeStartObject()
Writes the starting marker of a JSON object ('{').

writeString(stringValue)
Writes the specified string value.

writeStringField(fieldName, stringValue)
Writes a field name and value pair using the specified field name and string value.

writeTime(timeValue)
Writes the specified time value in the ISO-8601 format.

writeTimeField(fieldName, timeValue)
Writes a field name and value pair using the specified field name and time value in the ISO-8601 format.

##### close()

Closes the JSON generator.

Signature

```
   public Void close()

```

Return Value

Type: Void

Usage

No more content can be written after the JSON generator is closed.

##### getAsString()

Returns the generated JSON content.

Signature

```
   public String getAsString()

```

Return Value

Type: String

Usage

This method closes the JSON generator if it isn't closed already.

##### isClosed()

Returns `true` if the JSON generator is closed; otherwise, returns `false` .


Apex Reference Guide JSONGenerator Class

Signature

```
   public Boolean isClosed()

```

Return Value

Type: Boolean

##### writeBlob(blobValue)

Writes the specified `Blob` value as a base64-encoded string.

Signature

```
   public Void writeBlob(Blob blobValue)

```

Parameters

```
   blobValue
```

Type: Blob

Return Value

Type: Void

##### writeBlobField(fieldName, blobValue)

Writes a field name and value pair using the specified field name and BLOB value.

Signature

```
   public Void writeBlobField(String fieldName, Blob blobValue)

```

Parameters

```
   fieldName
```

Type: String

```
   blobValue
```

Type: Blob

Return Value

Type: Void

##### writeBoolean(blobValue)

Writes the specified Boolean value.

Signature

```
   public Void writeBoolean(Boolean blobValue)

```


Apex Reference Guide JSONGenerator Class

Parameters

```
   blobValue
```

Type: Boolean

Return Value

Type: Void

##### writeBooleanField(fieldName, booleanValue)

Writes a field name and value pair using the specified field name and Boolean value.

Signature

```
   public Void writeBooleanField(String fieldName, Boolean booleanValue)

```

Parameters

```
   fieldName
```

Type: String

```
   booleanValue
```

Type: Boolean

Return Value

Type: Void

##### writeDate(dateValue)

Writes the specified date value in the ISO-8601 format.

Signature

```
   public Void writeDate(Date dateValue)

```

Parameters

```
   dateValue
```

Type: Date

Return Value

Type: Void

##### writeDateField(fieldName, dateValue)

Writes a field name and value pair using the specified field name and date value. The date value is written in the ISO-8601 format.


Apex Reference Guide JSONGenerator Class

Signature

```
   public Void writeDateField(String fieldName, Date dateValue)

```

Parameters

```
   fieldName
```

Type: String

```
   dateValue
```

Type: Date

Return Value

Type: Void

##### writeDateTime(datetimeValue)

Writes the specified date and time value in the ISO-8601 format.

Signature

```
   public Void writeDateTime(Datetime datetimeValue)

```

Parameters

```
   datetimeValue
```

Type: Datetime

Return Value

Type: Void

##### writeDateTimeField(fieldName, datetimeValue)

Writes a field name and value pair using the specified field name and date and time value. The date and time value is written in the
ISO-8601 format.

Signature

```
   public Void writeDateTimeField(String fieldName, Datetime datetimeValue)

```

Parameters

```
   fieldName
```

Type: String

```
   datetimeValue
```

Type: Datetime

Return Value

Type: Void


Apex Reference Guide JSONGenerator Class

##### writeEndArray()

Writes the ending marker of a JSON array (']').

Signature

```
   public Void writeEndArray()

```

Return Value

Type: Void

##### writeEndObject()

Writes the ending marker of a JSON object ('}').

Signature

```
   public Void writeEndObject()

```

Return Value

Type: Void

##### writeFieldName(fieldName)

Writes a field name.

Signature

```
   public Void writeFieldName(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

Return Value

Type: Void

##### writeId(identifier)

Writes the specified ID value.

Signature

```
   public Void writeId(ID identifier)

```


Apex Reference Guide JSONGenerator Class

Parameters

```
   identifier
```

Type: ID

Return Value

Type: Void

##### writeIdField(fieldName, identifier)

Writes a field name and value pair using the specified field name and identifier value.

Signature

```
   public Void writeIdField(String fieldName, Id identifier)

```

Parameters

```
   fieldName
```

Type: String

```
   identifier
```

Type: ID

Return Value

Type: Void

##### writeNull()

Writes the JSON null literal value.

Signature

```
   public Void writeNull()

```

Return Value

Type: Void

##### writeNullField(fieldName)

Writes a field name and value pair using the specified field name and the JSON null literal value.

Signature

```
   public Void writeNullField(String fieldName)

```


Apex Reference Guide JSONGenerator Class

Parameters

```
   fieldName
```

Type: String

Return Value

Type: Void

##### writeNumber(number)

Writes the specified decimal value.

Signature

```
   public Void writeNumber(Decimal number)

```

Parameters

```
   number
```

Type: Decimal

Return Value

Type: Void

##### writeNumber(number)

Writes the specified double value.

Signature

```
   public Void writeNumber(Double number)

```

Parameters

```
   number
```

Type: Double

Return Value

Type: Void

##### writeNumber(number)

Writes the specified integer value.

Signature

```
   public Void writeNumber(Integer number)

```


Apex Reference Guide JSONGenerator Class

Parameters

```
   number
```

Type: Integer

Return Value

Type: Void

##### writeNumber(number)

Writes the specified long value.

Signature

```
   public Void writeNumber(Long number)

```

Parameters

```
   number
```

Type: Long

Return Value

Type: Void

##### writeNumberField(fieldName, number)

Writes a field name and value pair using the specified field name and decimal value.

Signature

```
   public Void writeNumberField(String fieldName, Decimal number)

```

Parameters

```
   fieldName
```

Type: String

```
   number
```

Type: Decimal

Return Value

Type: Void

##### writeNumberField(fieldName, number)

Writes a field name and value pair using the specified field name and double value.


Apex Reference Guide JSONGenerator Class

Signature

```
   public Void writeNumberField(String fieldName, Double number)

```

Parameters

```
   fieldName
```

Type: String

```
   number
```

Type: Double

Return Value

Type: Void

##### writeNumberField(fieldName, number)

Writes a field name and value pair using the specified field name and integer value.

Signature

```
   public Void writeNumberField(String fieldName, Integer number)

```

Parameters

```
   fieldName
```

Type: String

```
   number
```

Type: Integer

Return Value

Type: Void

##### writeNumberField(fieldName, number)

Writes a field name and value pair using the specified field name and long value.

Signature

```
   public Void writeNumberField(String fieldName, Long number)

```

Parameters

```
   fieldName
```

Type: String

```
   number
```

Type: Long


Apex Reference Guide JSONGenerator Class

Return Value

Type: Void

##### writeObject(anyObject)

Writes the specified Apex object in JSON format.

Signature

```
   public Void writeObject(Object anyObject)

```

Parameters

```
   anyObject
```

Type: Object

Return Value

Type: Void

##### writeObjectField(fieldName, value)

Writes a field name and value pair using the specified field name and Apex object.

Signature

```
   public Void writeObjectField(String fieldName, Object value)

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

Type: Void

##### writeStartArray()

Writes the starting marker of a JSON array ('[').

Signature

```
   public Void writeStartArray()

```

Return Value

Type: Void


Apex Reference Guide JSONGenerator Class

##### writeStartObject()

Writes the starting marker of a JSON object ('{').

Signature

```
   public Void writeStartObject()

```

Return Value

Type: Void

##### writeString(stringValue)

Writes the specified string value.

Signature

```
   public Void writeString(String stringValue)

```

Parameters

```
   stringValue
```

Type: String

Return Value

Type: Void

##### writeStringField(fieldName, stringValue)

Writes a field name and value pair using the specified field name and string value.

Signature

```
   public Void writeStringField(String fieldName, String stringValue)

```

Parameters

```
   fieldName
```

Type: String

```
   stringValue
```

Type: String

Return Value

Type: Void

##### writeTime(timeValue)

Writes the specified time value in the ISO-8601 format.


### Apex Reference Guide JSONParser Class

Signature

```
   public Void writeTime(Time timeValue)

```

Parameters

```
   timeValue
```

Type: Time

Return Value

Type: Void

##### writeTimeField(fieldName, timeValue)

Writes a field name and value pair using the specified field name and time value in the ISO-8601 format.

Signature

```
   public Void writeTimeField(String fieldName, Time timeValue)

```

Parameters

```
   fieldName
```

Type: String

```
   timeValue
```

Type: Time

Return Value

Type: Void

### JSONParser Class

Represents a parser for JSON-encoded content.

Namespace

System

Usage

Use the `System.JSONParser` methods to parse a response that's returned from a call to an external service that is in JSON format,
such as a JSON-encoded response of a Web service callout.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_json_jsonparser.htm)_ : JSON Parsing


Apex Reference Guide JSONParser Class

#### JSONParser Methods The following are methods for JSONParser . All are instance methods.

IN THIS SECTION:

clearCurrentToken()
Removes the current token.

getBlobValue()
Returns the current token as a BLOB value.

getBooleanValue()
Returns the current token as a Boolean value.

getCurrentName()
Returns the name associated with the current token.

getCurrentToken()
Returns the token that the parser currently points to or `null` if there's no current token.

getDatetimeValue()
Returns the current token as a date and time value.

getDateValue()
Returns the current token as a date value.

getDecimalValue()
Returns the current token as a decimal value.

getDoubleValue()
Returns the current token as a double value.

getIdValue()
Returns the current token as an ID value.

getIntegerValue()
Returns the current token as an integer value.

getLastClearedToken()
Returns the last token that was cleared by the `clearCurrentToken` method.

getLongValue()
Returns the current token as a long value.

getText()
Returns the textual representation of the current token or `null` if there's no current token.

getTimeValue()
Returns the current token as a time value.

hasCurrentToken()
Returns `true` if the parser currently points to a token; otherwise, returns `false` .

nextToken()
Returns the next token or `null` if the parser has reached the end of the input stream.

nextValue()
Returns the next token that is a value type or `null` if the parser has reached the end of the input stream.


Apex Reference Guide JSONParser Class

readValueAs(apexType)
Deserializes JSON content into an object of the specified Apex type and returns the deserialized object.

readValueAsStrict(apexType)
Deserializes JSON content into an object of the specified Apex type and returns the deserialized object. All attributes in the JSON
content must be present in the specified type.

skipChildren()
Skips all child tokens of type `JSONToken.START_ARRAY` and `JSONToken.START_OBJECT` that the parser currently
points to.

##### clearCurrentToken()

Removes the current token.

Signature

```
   public Void clearCurrentToken()

```

Return Value

Type: Void

Usage

After this method is called, a call to `hasCurrentToken` returns `false` and a call to `getCurrentToken` returns `null` . You
can retrieve the cleared token by calling `getLastClearedToken` .

##### getBlobValue()

Returns the current token as a BLOB value.

Signature

```
   public Blob getBlobValue()

```

Return Value

Type: Blob

Usage

The current token must be of type `JSONToken.VALUE_STRING` and must be Base64-encoded.

##### getBooleanValue()

Returns the current token as a Boolean value.

Signature

```
   public Boolean getBooleanValue()

```


Apex Reference Guide JSONParser Class

Return Value

Type: Boolean

Usage

The current token must be of type `JSONToken.VALUE_TRUE` or `JSONToken.VALUE_FALSE` .

The following example parses a sample JSON string and retrieves a Boolean value.

```
   String JSONContent =

      '{"isActive":true}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the Boolean value.

   Boolean isActive = parser.getBooleanValue();

##### getCurrentName()

```

Returns the name associated with the current token.

Signature

```
   public String getCurrentName()

```

Return Value

Type: String

Usage

If the current token is of type `JSONToken.FIELD_NAME`, this method returns the same value as `getText` . If the current token is
a value, this method returns the field name that precedes this token. For other values such as array values or root-level values, this method
returns `null` .

The following example parses a sample JSON string. It advances to the field value and retrieves its corresponding field name.

Example

```
   String JSONContent = '{"firstName":"John"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the field name for the current value.

   String fieldName = parser.getCurrentName();

   // Get the textual representation

```


Apex Reference Guide JSONParser Class

```
   // of the value.

   String fieldValue = parser.getText();

##### getCurrentToken()

```

Returns the token that the parser currently points to or `null` if there's no current token.

Signature

```
   public System.JSONToken getCurrentToken()

```

Return Value

Type: System.JSONToken

Usage

The following example iterates through all the tokens in a sample JSON string.

```
   String JSONContent = '{"firstName":"John"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the next token.

   while (parser.nextToken() != null) {

      System.debug('Current token: ' +

        parser.getCurrentToken());

   }

##### getDatetimeValue()

```

Returns the current token as a date and time value.

Signature

```
   public Datetime getDatetimeValue()

```

Return Value

Type: Datetime

Usage

The current token must be of type `JSONToken.VALUE_STRING` and must represent a `Datetime` value in the ISO-8601 format.

The following example parses a sample JSON string and retrieves a Datetime value.

```
   String JSONContent =

   '{"transactionDate":"2011-03-22T13:01:23"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

```


Apex Reference Guide JSONParser Class

```
   parser.nextValue();

   // Get the transaction date.

   Datetime transactionDate =

     parser.getDatetimeValue();

##### getDateValue()

```

Returns the current token as a date value.

Signature

```
   public Date getDateValue()

```

Return Value

Type: Date

Usage

The current token must be of type `JSONToken.VALUE_STRING` and must represent a `Date` value in the ISO-8601 format.

The following example parses a sample JSON string and retrieves a Date value.

```
   String JSONContent =

     '{"dateOfBirth":"2011-03-22"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the date of birth.

   Date dob = parser.getDateValue();

##### getDecimalValue()

```

Returns the current token as a decimal value.

Signature

```
   public Decimal getDecimalValue()

```

Return Value

Type: Decimal

Usage

The current token must be of type `JSONToken.VALUE_NUMBER_FLOAT` or `JSONToken.VALUE_NUMBER_INT` and is a
numerical value that can be converted to a value of type `Decimal` .


Apex Reference Guide JSONParser Class

The following example parses a sample JSON string and retrieves a Decimal value.

```
   String JSONContent =

     '{"GPA":3.8}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the GPA score.

   Decimal gpa = parser.getDecimalValue();

##### getDoubleValue()

```

Returns the current token as a double value.

Signature

```
   public Double getDoubleValue()

```

Return Value

Type: Double

Usage

The current token must be of type `JSONToken.VALUE_NUMBER_FLOAT` and is a numerical value that can be converted to a
value of type `Double` .

The following example parses a sample JSON string and retrieves a Double value.

```
   String JSONContent =

     '{"GPA":3.8}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the GPA score.

   Double gpa = parser.getDoubleValue();

##### getIdValue()

```

Returns the current token as an ID value.

Signature

```
   public ID getIdValue()

```


Apex Reference Guide JSONParser Class

Return Value

Type: ID

Usage

The current token must be of type `JSONToken.VALUE_STRING` and must be a valid `ID` .

The following example parses a sample JSON string and retrieves an ID value.

```
   String JSONContent =

     '{"recordId":"001R0000002nO6H"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the record ID.

   ID recordID = parser.getIdValue();

##### getIntegerValue()

```

Returns the current token as an integer value.

Signature

```
   public Integer getIntegerValue()

```

Return Value

Type: Integer

Usage

The current token must be of type `JSONToken.VALUE_NUMBER_INT` and must represent an `Integer` .

The following example parses a sample JSON string and retrieves an Integer value.

```
   String JSONContent =

     '{"recordCount":10}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the record count.

   Integer count = parser.getIntegerValue();

##### getLastClearedToken()

```

Returns the last token that was cleared by the `clearCurrentToken` method.


Apex Reference Guide JSONParser Class

Signature

```
   public System.JSONToken getLastClearedToken()

```

Return Value

Type: System.JSONToken

##### getLongValue()

Returns the current token as a long value.

Signature

```
   public Long getLongValue()

```

Return Value

Type: Long

Usage

The current token must be of type `JSONToken.VALUE_NUMBER_INT` and is a numerical value that can be converted to a value
of type `Long` .

The following example parses a sample JSON string and retrieves a Long value.

```
   String JSONContent =

     '{"recordCount":2097531021}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the record count.

   Long count = parser.getLongValue();

##### getText()

```

Returns the textual representation of the current token or `null` if there's no current token.

Signature

```
   public String getText()

```

Return Value

Type: String


Apex Reference Guide JSONParser Class

Usage

##### No current token exists, and therefore this method returns null, if nextToken has not been called yet for the first time or if the

parser has reached the end of the input stream.

##### getTimeValue()

Returns the current token as a time value.

Signature

```
   public Time getTimeValue()

```

Return Value

Type: Time

Usage

The current token must be of type `JSONToken.VALUE_STRING` and must represent a `Time` value in the ISO-8601 format.

The following example parses a sample JSON string and retrieves a Datetime value.

```
   String JSONContent =

     '{"arrivalTime":"18:05"}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Advance to the start object marker.

   parser.nextToken();

   // Advance to the next value.

   parser.nextValue();

   // Get the arrival time.

   Time arrivalTime = parser.getTimeValue();

##### hasCurrentToken()

```

Returns `true` if the parser currently points to a token; otherwise, returns `false` .

Signature

```
   public Boolean hasCurrentToken()

```

Return Value

Type: Boolean

##### nextToken()

Returns the next token or `null` if the parser has reached the end of the input stream.

Signature

```
   public System.JSONToken nextToken()

```


Apex Reference Guide JSONParser Class

Return Value

Type: System.JSONToken

Usage

Advances the stream enough to determine the type of the next token, if any.

##### nextValue()

Returns the next token that is a value type or `null` if the parser has reached the end of the input stream.

Signature

```
   public System.JSONToken nextValue()

```

Return Value

Type: System.JSONToken

Usage

Advances the stream enough to determine the type of the next token that is of a value type, if any, including a JSON array and object
start and end markers.

##### readValueAs(apexType)

Deserializes JSON content into an object of the specified Apex type and returns the deserialized object.

Signature

```
   public Object readValueAs(System.Type apexType)

```

Parameters

```
   apexType
```

Type: System.Type

The _`apexType`_ argument specifies the type of the object that this method returns after deserializing the current value.

Return Value

Type: Object

Usage

If the JSON content contains attributes not present in the `System.Type` argument, such as a missing field or object, deserialization
fails in some circumstances. When deserializing JSON content into a custom object or an sObject using Salesforce API version 34.0 or
earlier, this method throws a runtime exception when passed extraneous attributes. When deserializing JSON content into an Apex class
in any API version, or into an object in API version 35.0 or later, no exception is thrown. When no exception is thrown, this method ignores
extraneous attributes and parses the rest of the JSON content.


Apex Reference Guide JSONParser Class

Example

The following example parses a sample JSON string and retrieves a Datetime value. Before being able to run this sample, you must create
a new Apex class as follows:

```
   public class Person {

      public String name;

      public String phone;

   }

```

Next, insert the following sample in a class method:

```
   // JSON string that contains a Person object.

   String JSONContent =

      '{"person":{' +

        '"name":"John Smith",' +

        '"phone":"555-1212"}}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Make calls to nextToken()

   // to point to the second

   // start object marker.

   parser.nextToken();

   parser.nextToken();

   parser.nextToken();

   // Retrieve the Person object

   // from the JSON string.

   Person obj =

     (Person)parser.readValueAs(

       Person.class);

   System.assertEquals(

     obj.name, 'John Smith');

   System.assertEquals(

     obj.phone, '555-1212');

##### readValueAsStrict(apexType)

```

Deserializes JSON content into an object of the specified Apex type and returns the deserialized object. All attributes in the JSON content
must be present in the specified type.

Signature

```
   public Object readValueAsStrict(System.Type apexType)

```

Parameters

```
   apexType
```

Type: System.Type

The _`apexType`_ argument specifies the type of the object that this method returns after deserializing the current value.

Return Value

Type: Object


Apex Reference Guide JSONParser Class

Usage

If the JSON content contains attributes not present in the `System.Type` argument, such as a missing field or object, deserialization
fails in some circumstances. When deserializing JSON content with extraneous attributes into an Apex class, this method throws an
exception in all API versions. However, no exception is thrown when you use this method to deserialize JSON content into a custom
object or an sObject.

The following example parses a sample JSON string and retrieves a Datetime value. Before being able to run this sample, you must create
a new Apex class as follows:

```
   public class Person {

      public String name;

      public String phone;

   }

```

Next, insert the following sample in a class method:

```
   // JSON string that contains a Person object.

   String JSONContent =

      '{"person":{' +

        '"name":"John Smith",' +

        '"phone":"555-1212"}}';

   JSONParser parser =

     JSON.createParser(JSONContent);

   // Make calls to nextToken()

   // to point to the second

   // start object marker.

   parser.nextToken();

   parser.nextToken();

   parser.nextToken();

   // Retrieve the Person object

   // from the JSON string.

   Person obj =

     (Person)parser.readValueAsStrict(

       Person.class);

   System.assertEquals(

     obj.name, 'John Smith');

   System.assertEquals(

     obj.phone, '555-1212');

##### skipChildren()

```

Skips all child tokens of type `JSONToken.START_ARRAY` and `JSONToken.START_OBJECT` that the parser currently points
to.

Signature

```
   public Void skipChildren()

```

Return Value

Type: Void


### Apex Reference Guide JSONToken Enum JSONToken Enum

Contains all token values used for parsing JSON content.

Namespace

System

**Enum Value** **Description**

END_ARRAY The ending of an array value. This token is returned when ']' is
encountered.

END_OBJECT The ending of an object value. This token is returned when '}' is
encountered.

FIELD_NAME A string token that is a field name.

NOT_AVAILABLE The requested token isn't available.

START_ARRAY The start of an array value. This token is returned when '[' is
encountered.

START_OBJECT The start of an object value. This token is returned when '{' is
encountered.

VALUE_EMBEDDED_OBJECT

An embedded object that isn't accessible as a typical object
structure that includes the start and end object tokens
START_OBJECT and END_OBJECT but is represented as a raw object.

VALUE_FALSE The literal “false” value.

VALUE_NULL The literal “null” value.

VALUE_NUMBER_FLOAT A float value.

VALUE_NUMBER_INT An integer value.

VALUE_STRING A string value.

VALUE_TRUE A value that corresponds to the “true” string literal.

### Label Class

Provides methods to retrieve a custom label or to check if translation exists for a label in a specific language and namespace. Label names
are dynamically resolved at run time, overriding the user’s current language if a translation exists for the requested language. You can’t
access labels that are protected in a different namespace.

Namespace

System


Apex Reference Guide Label Class

Usage

Custom labels enable developers to create multilingual applications by automatically presenting information (for example, help text or
error messages) in a user’s native language. Custom labels have a limit of 1000 characters and can be accessed from Apex classes,
[Visualforce pages, Lightning pages, or Lightning components. For more information on custom labels, see Custom Labels in](https://help.salesforce.com/s/articleView?id=platform.cl_about.htm&type=5&language=en_US) _Salesforce_
_Help_ [.The label values can be translated into any language Salesforce supports. For supported languages, see Supported Languages in](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)
_Salesforce Help_ .

**•** To define custom labels, from Setup, in the Quick Find box, enter _`Custom Labels`_, and then select **Custom Labels** .

**•** To assign translated values, turn on Translation Workbench and add translation mappings.

**•** To retrieve the label for a default language setting or for a language and namespace, use `System.Label.get(namespace,`
`label, language)` .

**•** To check if translation exists for a label and language in a namespace, use `Label.translationExists(namespace,`
`label, language)` .

In Apex code, you can refer to or instantiate a Label like this:

```
   System.Label. myLabelName

```

[For information on passing in labels into Aura components, see Getting Labels in Apex in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/labels_apex.htm) _Lightning Aura Components Developer Guide_ .

Examples

This example returns `True` if an English label called _`MyLabel`_ exists in the _`MyNamespace`_ namespace.

```
   boolean exists = Label.translationExists('MyNamespace', 'MyLabel', 'en')

```

This example retrieves the custom label translation text for _`MyLabel`_ in French.

```
   String value = Label.get('MyNamespace', 'MyLabel', 'fr')

```

IN THIS SECTION:

#### Label Methods Label Methods The following are methods for Label .

IN THIS SECTION:

##### get(namespace, label)

Retrieve a custom label for the specified namespace and a default language setting.

get(namespace, label, language)
Retrieve a custom label for the specified namespace and language.

translationExists(namespace, label, language)
Check if translation exists for a label and language in a namespace.

##### **`get(namespace, label)`**

Retrieve a custom label for the specified namespace and a default language setting.


Apex Reference Guide Label Class

Signature

```
   public static String get(String namespace, String label)

```

Parameters

```
   namespace
```

Type: String

If the namespace name is null, it defaults to the package namespace. If the namespace name is an empty string, it implies the org
namespace.

```
   label
```

Type: String

The label name cannot be null or an empty string.

Return Value

Type: String

##### **`get(namespace, label, language)`**

Retrieve a custom label for the specified namespace and language.

Signature

```
   public static String get(String namespace, String label, String language)

```

Parameters

```
   namespace
```

Type: String

If the namespace name is null, it defaults to the package namespace. If the namespace name is an empty string, it implies the org
namespace.

```
   label
```

Type: String

The label name cannot be null or an empty string.

```
   language
```

Type: String

[This parameter must be a valid language ISO code. See the Platform-Only Languages section in Supported Languages in Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)
Help.

Return Value

Type: String

##### **`translationExists(namespace, label, language)`**

Check if translation exists for a label and language in a namespace.


### Apex Reference Guide Limits Class

Signature

```
   public static Boolean translationExists(string namespace, string label, string language)

```

Parameters

```
   namespace
```

Type: String

If the namespace name is null, it defaults to the package namespace. If the namespace name is an empty string, it implies the org
namespace.

```
   label
```

Type: String

The label name cannot be null or an empty string.

```
   language
```

Type: String

[This parameter must be a valid language ISO code. See the Platform-Only Languages section in Supported Languages in Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)
Help.

Return Value

Type: Boolean

### Limits Class

Contains methods that return limit information for specific resources.

Namespace

System

Usage

The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap
size remaining.

Because Apex runs in a multitenant environment, the Apex runtime engine strictly enforces a number of limits to ensure that runaway
Apex doesn’t monopolize shared resources.

None of the Limits methods require an argument. The format of the limits methods is as follows:

```
   myDMLLimit = Limits.getDMLStatements();

```

There are two versions of every method: the first returns the amount of the resource that has been used while the second version contains
the word limit and returns the total amount of the resource that is available.

[See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

#### Limits Methods

### The following are methods for Limits . All methods are static.


Apex Reference Guide Limits Class

IN THIS SECTION:

getAggregateQueries()
Returns the number of aggregate queries that have been processed with any SOQL query statement.

getLimitAggregateQueries()
Returns the total number of aggregate queries that can be processed with SOQL query statements.

getApexCursors()
Gets the number of Apex cursors that are created.

getLimitApexCursors()
Gets the maximum number of Apex cursors that can be created in a 24-hour period.

getApexCursorRows()
Gets the number of rows returned by an Apex cursor.

getLimitApexCursorRows()
Gets the maximum number of rows that can be returned by an Apex cursor.

getApexPaginationCursors()
Gets the number of Apex pagination cursors that are created.

getLimitApexPaginationCursors()
Gets the maximum number of Apex pagination cursors that can be created in a 24-hour period.

getApexPaginationCursorRows()
Gets the number of rows returned by an Apex pagination cursor.

getLimitApexPaginationCursorRows()
Gets the maximum number of rows that can be returned by an Apex pagination cursor.

getFetchCallsOnApexCursor()
Gets the number of fetch calls on an Apex cursor.

getLimitFetchCallsOnApexCursor()
Gets the maximum number of fetch calls that can be made on an Apex cursor.

getAsyncCalls()
Reserved for future use.

getLimitAsyncCalls()
Reserved for future use.

getCallouts()
Returns the number of Web service statements that have been processed.

getChildRelationshipsDescribes()
Deprecated. Returns the number of child relationship objects that have been returned.

getLimitCallouts()
Returns the total number of Web service statements that can be processed.

getCpuTime()
Returns the CPU time (in milliseconds) that has been used in the current transaction.

getLimitCpuTime()
Returns the maximum CPU time (in milliseconds) that can be used in a transaction.


Apex Reference Guide Limits Class

getDMLRows()
Returns the number of records that have been processed with any statement that counts against DML limits, such as DML statements,
the `Database.emptyRecycleBin` method, and other methods.

getLimitDMLRows()
Returns the total number of records that can be processed with any statement that counts against DML limits, such as DML statements,
the `database.EmptyRecycleBin` method, and other methods.

getDMLStatements()
Returns the number of DML statements (such as `insert`, `update` or the `database.EmptyRecycleBin` method) that
have been called.

getLimitDMLStatements()
Returns the total number of DML statements or the `database.EmptyRecycleBin` methods that can be called.

getEmailInvocations()
Returns the number of email invocations (such as `sendEmail` ) that have been called.

getLimitEmailInvocations()
Returns the total number of email invocation (such as `sendEmail` ) that can be called.

getFindSimilarCalls()
Deprecated. Returns the same value as `getSoslQueries` . The number of `findSimilar` methods is no longer a separate
limit, but is tracked as the number of SOSL queries issued.

getLimitFindSimilarCalls()
Deprecated. Returns the same value as `getLimitSoslQueries` . The number of `findSimilar` methods is no longer a
separate limit, but is tracked as the number of SOSL queries issued.

getFutureCalls()
Returns the number of methods with the `future` annotation that have been executed (not necessarily completed).

getLimitFutureCalls()
Returns the total number of methods with the `future` annotation that can be executed (not necessarily completed).

getHeapSize()
Returns the approximate amount of memory (in bytes) that has been used for the heap.

getLimitHeapSize()
Returns the total amount of memory (in bytes) that can be used for the heap.

getMobilePushApexCalls()
Returns the number of Apex calls that have been used by mobile push notifications during the current metering interval.

getLimitMobilePushApexCalls()
Returns the total number of Apex calls that are allowed per transaction for mobile push notifications.

getPublishImmediateDML()
Returns the number of `EventBus.publish` calls that have been made for platform events configured to publish immediately.

getLimitPublishImmediateDML()
Returns the total number of `EventBus.publish` statements that can be called for platform events configured to publish
immediately.

getQueries()
Returns the number of SOQL queries that have been issued.


Apex Reference Guide Limits Class

getLimitQueries()
Returns the total number of SOQL queries that can be issued.

getQueryLocatorRows()
Returns the number of records that have been returned by the `Database.getQueryLocator` method.

getLimitQueryLocatorRows()
Returns the total number of records that can be returned by the `Database.getQueryLocator` method.

getQueryRows()
Returns the number of records that have been returned by issuing SOQL queries.

getLimitQueryRows()
Returns the total number of records that can be returned by issuing SOQL queries.

getQueueableJobs()
Returns the number of queueable jobs that have been added to the queue per transaction. A queueable job corresponds to a class
that implements the `Queueable` interface.

getLimitQueueableJobs()
Returns the maximum number of queueable jobs that can be added to the queue per transaction. A queueable job corresponds to
a class that implements the `Queueable` interface.

getRunAs()
Deprecated. Returns the same value as `getDMLStatements` .

getLimitRunAs()
Deprecated. Returns the same value as `getLimitDMLStatements` .

getSavepointRollbacks()
Deprecated. Returns the same value as `getDMLStatements` .

getLimitSavepointRollbacks()
Deprecated. Returns the same value as `getLimitDMLStatements` .

getSavepoints()
Deprecated. Returns the same value as `getDMLStatements` .

getLimitSavepoints()
Deprecated. Returns the same value as `getLimitDMLStatements` .

getSoslQueries()
Returns the number of SOSL queries that have been issued.

getLimitSoslQueries()
Returns the total number of SOSL queries that can be issued.

##### getAggregateQueries()

Returns the number of aggregate queries that have been processed with any SOQL query statement.

Signature

```
   public static Integer getAggregateQueries()

```


Apex Reference Guide Limits Class

Return Value

Type: Integer

##### getLimitAggregateQueries()

Returns the total number of aggregate queries that can be processed with SOQL query statements.

Signature

```
   public static Integer getLimitAggregateQueries()

```

Return Value

Type: Integer

##### **`getApexCursors()`**

Gets the number of Apex cursors that are created.

Signature

```
   public static Integer getApexCursors()

```

Return Value

Type: Integer

##### **`getLimitApexCursors()`**

Gets the maximum number of Apex cursors that can be created in a 24-hour period.

Signature

```
   public static Integer getLimitApexCursors()

```

Return Value

Type: Integer

##### **`getApexCursorRows()`**

Gets the number of rows returned by an Apex cursor.

Signature

```
   public static Integer getApexCursorRows()

```

Return Value

Type: Integer


Apex Reference Guide Limits Class

##### **`getLimitApexCursorRows()`**

Gets the maximum number of rows that can be returned by an Apex cursor.

Signature

```
   public static Integer getLimitApexCursorRows()

```

Return Value

Type: Integer

##### **`getApexPaginationCursors()`**

Gets the number of Apex pagination cursors that are created.

Signature

```
   public static Integer getApexPaginationCursors()

```

Return Value

Type: Integer

##### **`getLimitApexPaginationCursors()`**

Gets the maximum number of Apex pagination cursors that can be created in a 24-hour period.

Signature

```
   public static Integer getLimitApexPaginationCursors()

```

Return Value

Type: Integer

##### **`getApexPaginationCursorRows()`**

Gets the number of rows returned by an Apex pagination cursor.

Signature

```
   public static Integer getApexPaginationCursorRows()

```

Return Value

Type: Integer

##### **`getLimitApexPaginationCursorRows()`**

Gets the maximum number of rows that can be returned by an Apex pagination cursor.


Apex Reference Guide Limits Class

Signature

```
   public static Integer getLimitApexPaginationCursorRows()

```

Return Value

Type: Integer

##### **`getFetchCallsOnApexCursor()`**

Gets the number of fetch calls on an Apex cursor.

Signature

```
   public static Integer getFetchCallsOnApexCursor()

```

Return Value

Type: Integer

##### **`getLimitFetchCallsOnApexCursor()`**

Gets the maximum number of fetch calls that can be made on an Apex cursor.

Signature

```
   public static Integer getLimitFetchCallsOnApexCursor()

```

Return Value

Type: Integer

##### getAsyncCalls()

Reserved for future use.

Signature

```
   public static Integer getAsyncCalls()

```

Return Value

Type: Integer

##### getLimitAsyncCalls()

Reserved for future use.

Signature

```
   public static Integer getLimitAsyncCalls()

```


Apex Reference Guide Limits Class

Return Value

Type: Integer

##### getCallouts()

Returns the number of Web service statements that have been processed.

Signature

```
   public static Integer getCallouts()

```

Return Value

Type: Integer

##### getChildRelationshipsDescribes()

Deprecated. Returns the number of child relationship objects that have been returned.

Signature

```
   public static Integer getChildRelationshipsDescribes()

```

Return Value

Type: Integer

Usage

Note: Because describe limits are no longer enforced in any API version, this method is no longer available. In API version 30.0
and earlier, this method is available but is deprecated.

##### getLimitCallouts()

Returns the total number of Web service statements that can be processed.

Signature

```
   public static Integer getLimitCallouts()

```

Return Value

Type: Integer

##### getCpuTime()

Returns the CPU time (in milliseconds) that has been used in the current transaction.


Apex Reference Guide Limits Class

Signature

```
   public static Integer getCpuTime()

```

Return Value

Type: Integer

##### getLimitCpuTime()

Returns the maximum CPU time (in milliseconds) that can be used in a transaction.

Signature

```
   public static Integer getLimitCpuTime()

```

Return Value

Type: Integer

##### getDMLRows()

Returns the number of records that have been processed with any statement that counts against DML limits, such as DML statements,
the `Database.emptyRecycleBin` method, and other methods.

Signature

```
   public static Integer getDMLRows()

```

Return Value

Type: Integer

##### getLimitDMLRows()

Returns the total number of records that can be processed with any statement that counts against DML limits, such as DML statements,
the `database.EmptyRecycleBin` method, and other methods.

Signature

```
   public static Integer getLimitDMLRows()

```

Return Value

Type: Integer

##### getDMLStatements()

Returns the number of DML statements (such as `insert`, `update` or the `database.EmptyRecycleBin` method) that have
been called.


Apex Reference Guide Limits Class

Signature

```
   public static Integer getDMLStatements()

```

Return Value

Type: Integer

##### getLimitDMLStatements()

Returns the total number of DML statements or the `database.EmptyRecycleBin` methods that can be called.

Signature

```
   public static Integer getLimitDMLStatements()

```

Return Value

Type: Integer

##### getEmailInvocations()

Returns the number of email invocations (such as `sendEmail` ) that have been called.

Signature

```
   public static Integer getEmailInvocations()

```

Return Value

Type: Integer

##### getLimitEmailInvocations()

Returns the total number of email invocation (such as `sendEmail` ) that can be called.

Signature

```
   public static Integer getLimitEmailInvocations()

```

Return Value

Type: Integer

##### getFindSimilarCalls()

Deprecated. Returns the same value as `getSoslQueries` . The number of `findSimilar` methods is no longer a separate limit,
but is tracked as the number of SOSL queries issued.


Apex Reference Guide Limits Class

Signature

```
   public static Integer getFindSimilarCalls()

```

Return Value

Type: Integer

##### getLimitFindSimilarCalls()

Deprecated. Returns the same value as `getLimitSoslQueries` . The number of `findSimilar` methods is no longer a separate
limit, but is tracked as the number of SOSL queries issued.

Signature

```
   public static Integer getLimitFindSimilarCalls()

```

Return Value

Type: Integer

##### getFutureCalls()

Returns the number of methods with the `future` annotation that have been executed (not necessarily completed).

Signature

```
   public static Integer getFutureCalls()

```

Return Value

Type: Integer

##### getLimitFutureCalls()

Returns the total number of methods with the `future` annotation that can be executed (not necessarily completed).

Signature

```
   public static Integer getLimitFutureCalls()

```

Return Value

Type: Integer

##### getHeapSize()

Returns the approximate amount of memory (in bytes) that has been used for the heap.


Apex Reference Guide Limits Class

Signature

```
   public static Integer getHeapSize()

```

Return Value

Type: Integer

##### getLimitHeapSize()

Returns the total amount of memory (in bytes) that can be used for the heap.

Signature

```
   public static Integer getLimitHeapSize()

```

Return Value

Type: Integer

##### getMobilePushApexCalls()

Returns the number of Apex calls that have been used by mobile push notifications during the current metering interval.

Signature

```
   public static Integer getMobilePushApexCalls()

```

Return Value

Type:Integer

##### getLimitMobilePushApexCalls()

Returns the total number of Apex calls that are allowed per transaction for mobile push notifications.

Signature

```
   public static Integer getLimitMobilePushApexCalls()

```

Return Value

Type:Integer

##### getPublishImmediateDML()

Returns the number of `EventBus.publish` calls that have been made for platform events configured to publish immediately.

Signature

```
   public static Integer getPublishImmediateDML()

```


Apex Reference Guide Limits Class

Return Value

Type: Integer

##### getLimitPublishImmediateDML()

Returns the total number of `EventBus.publish` statements that can be called for platform events configured to publish immediately.

Signature

```
   public static Integer getLimitPublishImmediateDML()

```

Return Value

Type: Integer

##### getQueries()

Returns the number of SOQL queries that have been issued.

Signature

```
   public static Integer getQueries()

```

Return Value

Type: Integer

##### getLimitQueries()

Returns the total number of SOQL queries that can be issued.

Signature

```
   public static Integer getLimitQueries()

```

Return Value

Type: Integer

##### getQueryLocatorRows()

Returns the number of records that have been returned by the `Database.getQueryLocator` method.

Signature

```
   public static Integer getQueryLocatorRows()

```

Return Value

Type: Integer


Apex Reference Guide Limits Class

##### getLimitQueryLocatorRows()

Returns the total number of records that can be returned by the `Database.getQueryLocator` method.

Signature

```
   public static Integer getLimitQueryLocatorRows()

```

Return Value

Type: Integer

##### getQueryRows()

Returns the number of records that have been returned by issuing SOQL queries.

Signature

```
   public static Integer getQueryRows()

```

Return Value

Type: Integer

##### getLimitQueryRows()

Returns the total number of records that can be returned by issuing SOQL queries.

Signature

```
   public static Integer getLimitQueryRows()

```

Return Value

Type: Integer

##### getQueueableJobs()

Returns the number of queueable jobs that have been added to the queue per transaction. A queueable job corresponds to a class that
implements the `Queueable` interface.

Signature

```
   public static Integer getQueueableJobs()

```

Return Value

Type: Integer


Apex Reference Guide Limits Class

##### getLimitQueueableJobs()

Returns the maximum number of queueable jobs that can be added to the queue per transaction. A queueable job corresponds to a
class that implements the `Queueable` interface.

Signature

```
   public static Integer getLimitQueueableJobs()

```

Return Value

Type: Integer

##### getRunAs()

Deprecated. Returns the same value as `getDMLStatements` .

Signature

```
   public static Integer getRunAs()

```

Return Value

Type: Integer

Usage

The number of `RunAs` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getLimitRunAs()

Deprecated. Returns the same value as `getLimitDMLStatements` .

Signature

```
   public static Integer getLimitRunAs()

```

Return Value

Type: Integer

Usage

The number of `RunAs` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getSavepointRollbacks()

Deprecated. Returns the same value as `getDMLStatements` .


Apex Reference Guide Limits Class

Signature

```
   public static Integer getSavepointRollbacks()

```

Return Value

Type: Integer

Usage

The number of `Rollback` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getLimitSavepointRollbacks()

Deprecated. Returns the same value as `getLimitDMLStatements` .

Signature

```
   public static Integer getLimitSavepointRollbacks()

```

Return Value

Type: Integer

Usage

The number of `Rollback` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getSavepoints()

Deprecated. Returns the same value as `getDMLStatements` .

Signature

```
   public static Integer getSavepoints()

```

Return Value

Type: Integer

Usage

The number of `setSavepoint` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getLimitSavepoints()

Deprecated. Returns the same value as `getLimitDMLStatements` .

Signature

```
   public static Integer getLimitSavepoints()

```


### Apex Reference Guide List Class

Return Value

Type: Integer

Usage

The number of `setSavepoint` methods is no longer a separate limit, but is tracked as the number of DML statements issued.

##### getSoslQueries()

Returns the number of SOSL queries that have been issued.

Signature

```
   public static Integer getSoslQueries()

```

Return Value

Type: Integer

##### getLimitSoslQueries()

Returns the total number of SOSL queries that can be issued.

Signature

```
   public static Integer getLimitSoslQueries()

```

Return Value

Type: Integer

### List Class

Contains methods for the List collection type.

Namespace

System

Usage

The list methods are all instance methods, that is, they operate on a particular instance of a list. For example, the following removes all
elements from `myList` :

```
   myList.clear();

```

Even though the `clear` method does not include any parameters, the list that calls it is its implicit parameter.


Apex Reference Guide List Class

Note:

**•** When using a custom type for the list elements, provide an `equals` method in your class. Apex uses this method to determine
equality and uniqueness for your objects. For more information on providing an `equals` [method, see Using Custom Types](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)
[in Map Keys and Sets.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)

**•** If the list contains String elements, the elements are case-sensitive. Two list elements that differ only by case are considered
distinct.

[For more information on lists, see Lists.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_lists.htm)

IN THIS SECTION:

#### List Constructors

List Methods

#### List Constructors The following are constructors for List .

IN THIS SECTION:

##### List<T>()
#### Creates a new instance of the List class. A list can hold elements of any data type T.

List<T>(listToCopy)
#### Creates a new instance of the List class by copying the elements from the specified list. T is the data type of the elements in both

lists and can be any data type.

List<T>(setToCopy)
#### Creates a new instance of the List class by copying the elements from the specified set. T is the data type of the elements in the

set and list and can be any data type.

##### List<T>()

#### Creates a new instance of the List class. A list can hold elements of any data type T.

Signature

```
   public List<T>()

```

Example

```
   // Create a list

   List<Integer> ls1 = new List<Integer>();

   // Add two integers to the list

   ls1.add(1);

   ls1.add(2);

```


Apex Reference Guide List Class

##### List<T>(listToCopy) Creates a new instance of the List class by copying the elements from the specified list. T is the data type of the elements in both

lists and can be any data type.

Signature

```
   public List<T>(List<T> listToCopy)

```

Parameters

```
   listToCopy
```

Type: List<T>

The list containing the elements to initialize this list from. T is the data type of the list elements.

Example

```
   List<Integer> ls1 = new List<Integer>();

   ls1.add(1);

   ls1.add(2);

   // Create a list based on an existing one

   List<Integer> ls2 = new List<Integer>(ls1);

   // ls2 elements are copied from ls1

   System.debug(ls2);// DEBUG|(1, 2)

##### List<T>(setToCopy) Creates a new instance of the List class by copying the elements from the specified set. T is the data type of the elements in the set
```

and list and can be any data type.

Signature

```
   public List<T>(Set<T> setToCopy)

```

Parameters

**setToCopy**
Type: Set<T>

The set containing the elements to initialize this list with. T is the data type of the set elements.

Example

```
   Set<Integer> s1 = new Set<Integer>();

   s1.add(1);

   s1.add(2);

   // Create a list based on a set

   List<Integer> ls = new List<Integer>(s1);

   // ls elements are copied from s1

   Assert.isTrue(ls.contains(2));

   Assert.isTrue(ls.contains(1));

```


Apex Reference Guide List Class

#### List Methods The following are methods for List . All are instance methods.

IN THIS SECTION:

add(listElement)
Adds an element to the end of the list.

add(index, listElement)
Inserts an element into the list at the specified index position and shifts all subsequent elements one index position to the right.

addAll(fromList)
Adds all of the elements in the specified list to the list that calls the method. Both lists must be of the same type.

addAll(fromSet)
Add all of the elements in specified set to the list that calls the method. The set and the list must be of the same type.

clear()
Removes all elements from a list, consequently setting the list's length to zero.

clone()
Makes a duplicate copy of a list.

contains(listElement)
Returns `true` if the list contains the specified element.

deepClone(preserveId, preserveReadonlyTimestamps, preserveAutonumber)
Makes a duplicate copy of a list of sObject records, including the sObject records themselves.

equals(list2)
Compares this list with the specified list and returns `true` if both lists are equal; otherwise, returns `false` .

get(index)
Returns the list element stored at the specified index.

getSObjectType()
Returns the token of the sObject type that makes up a list of sObjects.

hashCode()
Returns the hashcode corresponding to this list and its contents.

indexOf(listElement)
Returns the index of the first occurrence of the specified element in this list. If this list does not contain the element, returns -1.

isEmpty()
Returns true if the list has zero elements.

iterator()
Returns an instance of an iterator for this list.

remove(index)
Removes the list element stored at the specified index, returning the element that was removed.

set(index, listElement)
Sets the specified value for the element at the given index.

size()
Returns the number of elements in the list.


Apex Reference Guide List Class

sort()
Sorts the items in the list in ascending order.

toString()
Returns the string representation of the list.

##### add(listElement)

Adds an element to the end of the list.

Signature

```
   public Void add(Object listElement)

```

Parameters

```
   listElement
```

Type: Object

Return Value

Type: Void

Example

```
   List<Integer> myList = new List<Integer>();

   myList.add(47);

   Integer myNumber = myList.get(0);

   system.assertEquals(47, myNumber);

##### **`add(index, listElement)`**

```

Inserts an element into the list at the specified index position and shifts all subsequent elements one index position to the right.

Signature

```
   public Void add(Integer index, Object listElement)

```

Parameters

```
   index
```

Type: Integer

```
   listElement
```

Type: Object

Return Value

Type: Void


Apex Reference Guide List Class

Example

In this example, a list with six elements is created. Integers are added to the first and second index positions, and the subsequent elements
are shifted to the right. After the two methods are called, the list has eight total elements.

```
   List<Integer> myList = new Integer[6];

   myList.add(0, 47);

   myList.add(1, 52);

   system.debug(myList); // DEBUG|(47, 52, null, null, null, null, null, null)

   system.assertEquals(52, myList.get(1));

##### addAll(fromList)

```

Adds all of the elements in the specified list to the list that calls the method. Both lists must be of the same type.

Signature

```
   public Void addAll(List fromList)

```

Parameters

```
   fromList
```

Type: List

Return Value

Type: Void

##### addAll(fromSet)

Add all of the elements in specified set to the list that calls the method. The set and the list must be of the same type.

Signature

```
   public Void addAll(Set fromSet)

```

Parameters

```
   fromSet
```

Type: Set

Return Value

Type: Void

##### clear()

Removes all elements from a list, consequently setting the list's length to zero.

Signature

```
   public Void clear()

```


Apex Reference Guide List Class

Return Value

Type: Void

##### clone()

Makes a duplicate copy of a list.

Signature

```
   public List<Object> clone()

```

Return Value

Type: List<Object>

Usage

The cloned list is of the same type as the current list.

Note that if this is a list of sObject records, the duplicate list will only be a shallow copy of the list. That is, the duplicate will have references
to each object, but the sObject records themselves will not be duplicated. For example:

To also copy the sObject records, you must use the `deepClone` method.

Example

```
   Account a = new Account(Name='Acme', BillingCity='New York');

   Account b = new Account();

   Account[] q1 = new Account[]{a,b};

   Account[] q2 = q1.clone();

   q1[0].BillingCity = 'San Francisco';

   System.assertEquals(

       'San Francisco',

       q1[0].BillingCity);

   System.assertEquals(

       'San Francisco',

       q2[0].BillingCity);

##### contains(listElement)

```

Returns `true` if the list contains the specified element.

Signature

```
   public Boolean contains(Object listElement)

```


Apex Reference Guide List Class

Parameters

```
   listElement
```

Type: Object

Return Value

Type: Boolean

Example

```
   List<String> myStrings = new List<String>{'a', 'b'};

   Boolean result = myStrings.contains('z');

   System.assertEquals(false, result);

##### deepClone(preserveId, preserveReadonlyTimestamps, preserveAutonumber)

```

Makes a duplicate copy of a list of sObject records, including the sObject records themselves.

Signature

```
   public List<Object> deepClone(Boolean preserveId, Boolean preserveReadonlyTimestamps,

   Boolean preserveAutonumber)

```

Parameters

```
   preserveId
```

Type: Boolean

The optional _`preserveId`_ argument determines whether the IDs of the original objects are preserved or cleared in the duplicates.
If set to `true`, the IDs are copied to the cloned objects. The default is `false`, that is, the IDs are cleared.

```
   preserveReadonlyTimestamps
```

Type: Boolean

The optional _`preserveReadonlyTimestamps`_ argument determines whether the read-only timestamp and user ID fields
are preserved or cleared in the duplicates. If set to `true`, the read-only fields `CreatedById`, `CreatedDate`,
`LastModifiedById`, and `LastModifiedDate` are copied to the cloned objects. The default is `false`, that is, the values
are cleared.

```
   preserveAutonumber
```

Type: Boolean

The optional _`preserveAutonumber`_ argument determines whether the autonumber fields of the original objects are preserved
or cleared in the duplicates. If set to `true`, auto number fields are copied to the cloned objects. The default is `false`, that is, auto
number fields are cleared.

Return Value

Type: List<Object>

Usage

The returned list is of the same type as the current list.


Apex Reference Guide List Class

Note:

**•** `deepClone` only works with lists of sObjects, not with lists of primitives.

**•** For Apex saved using Salesforce API version 22.0 or earlier, the default value for the _`preserve_id`_ argument is `true`, that
is, the IDs are preserved.

To make a shallow copy of a list without duplicating the sObject records it contains, use the `clone` method.

Example

This example performs a deep clone for a list with two accounts.

```
   Account a = new Account(Name='Acme', BillingCity='New York');

   Account b = new Account(Name='Salesforce');

   Account[] q1 = new Account[]{a,b};

   Account[] q2 = q1.deepClone();

   q1[0].BillingCity = 'San Francisco';

   System.assertEquals(

      'San Francisco',

      q1[0].BillingCity);

   System.assertEquals(

      'New York',

      q2[0].BillingCity);

```

This example is based on the previous example and shows how to clone a list with preserved read-only timestamp and user ID fields.

```
   insert q1;

   List<Account> accts = [SELECT CreatedById, CreatedDate, LastModifiedById,

                 LastModifiedDate, BillingCity

                 FROM Account

                 WHERE Name='Acme' OR Name='Salesforce'];

   // Clone list while preserving timestamp and user ID fields.

   Account[] q3 = accts.deepClone(false,true,false);

   // Verify timestamp fields are preserved for the first list element.

   System.assertEquals(

      accts[0].CreatedById,

      q3[0].CreatedById);

   System.assertEquals(

      accts[0].CreatedDate,

      q3[0].CreatedDate);

   System.assertEquals(

      accts[0].LastModifiedById,

      q3[0].LastModifiedById);

   System.assertEquals(

      accts[0].LastModifiedDate,

      q3[0].LastModifiedDate);

```


Apex Reference Guide List Class

##### equals(list2)

Compares this list with the specified list and returns `true` if both lists are equal; otherwise, returns `false` .

Signature

```
   public Boolean equals(List list2)

```

Parameters

```
   list2
```

Type: List

The list to compare this list with.

Return Value

Type: Boolean

Usage

Two lists are equal if their elements are equal and are in the same order. The `==` operator is used to compare the elements of the lists.

##### The == operator is equivalent to calling the equals method, so you can call list1.equals(list2); instead of list1 ==

`list2;` .

##### get(index)

Returns the list element stored at the specified index.

Signature

```
   public Object get(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: Object

Usage

To reference an element of a one-dimensional list of primitives or sObjects, you can also follow the name of the list with the element's
index position in square brackets as shown in the example.

If the element referenced is out of bounds, this exception is thrown: `System.ListException: List index is out of`
`bounds` .


Apex Reference Guide List Class

Example

```
   List<Integer> myList = new List<Integer>();

   myList.add(47);

   Integer myNumber = myList.get(0);

   system.assertEquals(47, myNumber);

   List<String> colors = new String[3];

   colors[0] = 'Red';

   colors[1] = 'Blue';

   colors[2] = 'Green';

##### getSObjectType()

```

Returns the token of the sObject type that makes up a list of sObjects.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Usage

Use this method with describe information to determine if a list contains sObjects of a particular type.

Note that this method can only be used with lists that are composed of sObjects.

[For more information, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

Example

```
   // Create a generic sObject variable.

   SObject sObj = Database.query('SELECT Id FROM Account LIMIT 1');

   // Verify if that sObject variable is an Account token.

   System.assertEquals(

     Account.sObjectType,

     sObj.getSObjectType());

   // Create a list of generic sObjects.

   List<sObject> q = new Account[]{};

   // Verify if the list of sObjects

   // contains Account tokens.

   System.assertEquals(

     Account.sObjectType,

     q.getSObjectType());

```


Apex Reference Guide List Class

##### hashCode()

Returns the hashcode corresponding to this list and its contents.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### indexOf(listElement)

Returns the index of the first occurrence of the specified element in this list. If this list does not contain the element, returns -1.

Signature

```
   public Integer indexOf(Object listElement)

```

Parameters

```
   listElement
```

Type: Object

Return Value

Type: Integer

Example

```
   List<String> myStrings = new List<String>{'a', 'b', 'a'};

   Integer result = myStrings.indexOf('a');

   System.assertEquals(0, result);

##### isEmpty()

```

Returns true if the list has zero elements.

Signature

```
   public Boolean isEmpty()

```

Return Value

Type: Boolean

##### iterator()

Returns an instance of an iterator for this list.


Apex Reference Guide List Class

Signature

```
   public Iterator iterator()

```

Return Value

Type: Iterator

Usage

From the returned iterator, you can use the iterable methods `hasNext` and `next` to iterate through the list.

Note: You don’t have to implement the `iterable` interface to use the `iterable` methods with a list.

[See Custom Iterators.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_iterable.htm)

Example

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

     public Account next(){

        if(hasNext()) {

          return accounts[currentIndex++];

        } else {

          throw new NoSuchElementException('Iterator has no more elements.');

        }

     }

   }

##### remove(index)

```

Removes the list element stored at the specified index, returning the element that was removed.

Signature

```
   public Object remove(Integer index)

```


Apex Reference Guide List Class

Parameters

```
   index
```

Type: Integer

Return Value

Type: Object

Example

```
   List<String> colors = new String[3];

   colors[0] = 'Red';

   colors[1] = 'Blue';

   colors[2] = 'Green';

   String s1 = colors.remove(2);

   system.assertEquals('Green', s1);

##### set(index, listElement)

```

Sets the specified value for the element at the given index.

Signature

```
   public Void set(Integer index, Object listElement)

```

Parameters

```
   index
```

Type: Integer

The index of the list element to set.

```
   listElement
```

Type: Object

The value of the list element to set.

Return Value

Type: Void

Usage

To set an element of a one-dimensional list of primitives or sObjects, you can also follow the name of the list with the element's index
position in square brackets.

Example

```
   List<Integer> myList = new Integer[6];

   myList.set(0, 47);

```


Apex Reference Guide List Class

```
   myList.set(1, 52);

   system.assertEquals(52, myList.get(1));

   List<String> colors = new String[3];

   colors[0] = 'Red';

   colors[1] = 'Blue';

   colors[2] = 'Green';

##### size()

```

Returns the number of elements in the list.

Signature

```
   public Integer size()

```

Return Value

Type: Integer

Example

```
   List<Integer> myList = new List<Integer>();

   Integer size = myList.size();

   system.assertEquals(0, size);

   List<Integer> myList2 = new Integer[6];

   Integer size2 = myList2.size();

   system.assertEquals(6, size2);

##### sort()

```

Sorts the items in the list in ascending order.

Signature

```
   public Void sort()

```

Return Value

Type: Void

Usage

Using this method, you can sort primitive types, SelectOption elements, and sObjects (standard objects and custom objects). For more
[information on the sort order used for sObjects, see Sorting Lists of sObjects. You can sort custom types (your Apex classes) if they](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_list_sorting_sobject.htm)
implement the Comparable interface. Alternatively, a class implementing the Comparator interface can be passed as a parameter to the
`List.sort` method.

##### When you use sort() methods on List<Id>s that contain both 15-character and 18-character IDs, IDs for the same record sort

together in API version 35.0 and later.


### Apex Reference Guide Location Class

Example

In the following example, the list has three elements. When the list is sorted, the first element is null because it has no value assigned.
The second element and third element have values of 5 and 10.

```
   List<Integer> q1 = new Integer[3];

   // Assign values to the first two elements.

   q1[0] = 10;

   q1[1] = 5;

   q1.sort();

   // Verify sorted list. Elements are sorted in nulls-first order: null, 5, and 10

   system.assertEquals(null, q1.get(0));

   system.assertEquals(5, q1.get(1));

   system.assertEquals(10, q1.get(2));

##### toString()

```

Returns the string representation of the list.

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

### Location Class

Contains methods for accessing the component fields of geolocation compound fields.


Apex Reference Guide Location Class

Namespace

system

Usage

Each of these methods is also equivalent to a read-only property. For each getter method you can access the property using dot notation.
For example, `myLocation.getLatitude()` is equivalent to `myLocation.latitude` .

You can’t use dot notation to access compound fields’ subfields directly on the parent field. Instead, assign the parent field to a variable
#### of type Location, and then access its components.

```
   Location loc = myAccount.MyLocation__c;

   Double lat = loc.latitude;

```

Important: “Location” in Salesforce can also refer to the Location standard object. When referencing the Location object in your
#### Apex code, always use Schema.Location instead of Location to prevent confusion with the standard Location compound

field. If referencing both the location object and the Location field in the same snippet, you can differentiate between the two by
using `System.Location` for the field and `Schema.Location` for the object.

Example

```
   // Select and access the Location field. MyLocation__c is the name of a geolocation field

    on Account.

   Account[] records = [SELECT id, MyLocation__c FROM Account LIMIT 10];

   for(Account acct : records) {

     Location loc = acct.MyLocation__c;

     Double lat = loc.latitude;

     Double lon = loc.longitude;

   }

   // Instantiate new Location objects and compute the distance between them in different

   ways.

   Location loc1 = Location.newInstance(28.635308,77.22496);

   Location loc2 = Location.newInstance(37.7749295,-122.4194155);

   Double dist = Location.getDistance(loc1, loc2, 'mi');

   Double dist2 = loc1.getDistance(loc2, 'mi');

```

IN THIS SECTION:

#### Location Methods Location Methods The following are methods for Location .

IN THIS SECTION:

getDistance(toLocation, unit)
Calculates the distance between this location and the specified location, using an approximation of the haversine formula and the
specified unit.


Apex Reference Guide Location Class

##### getDistance(firstLocation, secondLocation, unit)

Calculates the distance between the two specified locations, using an approximation of the haversine formula and the specified
unit.

getLatitude()
Returns the latitude field of this location.

getLongitude()
Returns the longitude field of this location.

newInstance(latitude, longitude)
Creates an instance of the `Location` class, with the specified latitude and longitude.

##### getDistance(toLocation, unit)

Calculates the distance between this location and the specified location, using an approximation of the haversine formula and the
specified unit.

Signature

```
   public Double getDistance(Location toLocation, String unit)

```

Parameters

```
   toLocation
```

Type: Location

The `Location` to which you want to calculate the distance from the current `Location` .

```
   unit
```

Type: String

The distance unit you want to use: `mi` or `km` .

Return Value

Type: Double

##### getDistance(firstLocation, secondLocation, unit)

Calculates the distance between the two specified locations, using an approximation of the haversine formula and the specified unit.

Signature

```
   public static Double getDistance(Location firstLocation, Location secondLocation, String

   unit)

```

Parameters

```
   firstLocation
```

Type: Location

The first of two locations used to calculate distance.


Apex Reference Guide Location Class

```
   secondLocation
```

Type: Location

The second of two locations used to calculate distance.

```
   unit
```

Type: String

The distance unit you want to use: `mi` or `km` .

Return Value

Type: Double

##### getLatitude()

Returns the latitude field of this location.

Signature

```
   public Double getLatitude()

```

Return Value

Type: Double

##### getLongitude()

Returns the longitude field of this location.

Signature

```
   public Double getLongitude()

```

Return Value

Type: Double

##### newInstance(latitude, longitude)

Creates an instance of the `Location` class, with the specified latitude and longitude.

Signature

```
   public static Location newInstance(Decimal latitude, Decimal longitude)

```

Parameters

```
   latitude
```

Type: Decimal

```
   longitude
```

Type: Decimal


### Apex Reference Guide LoggingLevel Enum

Return Value

Type: Location

### LoggingLevel Enum

Specifies the logging level for the `System.debug` method.

Enum Values

The following are the values of the `System.LoggingLevel` enum, listed from the lowest to the highest levels. The level is cumulative,
that is, if you select FINE, the log also includes all events logged at the DEBUG, INFO, WARN, and ERROR levels.

**Value** **Description**

`NONE` No logging.

`ERROR` Error and exception logging.

`WARN` Warning logging.

`INFO` Informational logging.

`DEBUG` User-specified debug logging.

`FINE` High level of logging.

`FINER` Higher level of logging than FINE.

`FINEST` Highest level of logging.

Usage

Log levels are cumulative. For example, if the lowest level, `ERROR`, is specified for Apex code, only `System.debug` methods with
the log level of `ERROR` are logged. If the next log level, `WARN`, is specified, `System.debug` methods specified with either `ERROR`
or `WARN` levels are logged.

In this example, if the log level is set to `ERROR`, the string `MsgTxt` isn’t written to the debug log because the `debug` method has a
level of `INFO` .

```
   System.debug(logginglevel.INFO, 'MsgTxt');

```

[For more information on log levels, see Debug Log Levels in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.code_setting_debug_log_levels.htm&language=en_US)

### Long Class

Contains methods for the Long primitive data type.

Namespace

System


Apex Reference Guide Long Class

Usage

[For more information on Long, see Long Data Type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Long Methods The following are methods for Long .

IN THIS SECTION:

##### format()

Returns the String format for this Long using the locale of the context user.

##### intValue()

Returns the Integer value for this Long.

valueOf(stringToLong)
Returns a Long that contains the value of the specified String. As in Java, the string is interpreted as representing a signed decimal
Long.

##### format()

Returns the String format for this Long using the locale of the context user.

Signature

```
   public String format()

```

Return Value

Type: String

Example

```
   Long myLong = 4271990;

   system.assertEquals('4,271,990', myLong.format());

##### intValue()

```

Returns the Integer value for this Long.

Signature

```
   public Integer intValue()

```

Return Value

Type: Integer


### Apex Reference Guide Map Class

Example

```
   Long myLong = 7191991;

   Integer value = myLong.intValue();

   system.assertEquals(7191991, myLong.intValue());

##### valueOf(stringToLong)

```

Returns a Long that contains the value of the specified String. As in Java, the string is interpreted as representing a signed decimal Long.

Signature

```
   public static Long valueOf(String stringToLong)

```

Parameters

```
   stringToLong
```

Type: String

Return Value

Type: Long

Example

```
   Long L1 = long.valueOf('123456789');

### Map Class

```

Contains methods for the Map collection type.

Namespace

System

Usage

The Map methods are all instance methods, that is, they operate on a particular instance of a map. The following are the instance methods
for maps.

Note:

**•** Map keys and values can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex
types.

**•** Uniqueness of map keys of user-defined types is determined by the `equals` and `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)` methods, which you provide
in your classes. Uniqueness of keys of all other non-primitive types, such as sObject keys, is determined by comparing the
objects’ field values. Use caution when you use an sObject as a map key because when the sObject is changed, it no longer
maps to the same value. For information and examples, see
[https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_map_sobject_considerations.htm](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_map_sobject_considerations.htm)


Apex Reference Guide Map Class

**•** Map keys of type String are case-sensitive. Two keys that differ only by the case are considered unique and have corresponding
distinct Map entries. Subsequently, the Map methods, including `put`, `get`, `containsKey`, and `remove` treat these keys
as distinct.

**•** With the `keySet()` method, the returned keySet is backed by the map and reflects any changes made to the map, and
vice versa.

[For more information on maps, see Maps.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)

IN THIS SECTION:

#### Map Constructors

Map Methods

#### Map Constructors The following are constructors for Map .

IN THIS SECTION:

##### Map<T1,T2>()
#### Creates a new instance of the Map class. T1 is the data type of the keys and T2 is the data type of the values.

##### Map<T1,T2>(mapToCopy)
#### Creates a new instance of the Map class and initializes it by copying the entries from the specified map. T1 is the data type of the

keys and T2 is the data type of the values.

Map<ID,sObject>(recordList)
#### Creates a new instance of the Map class and populates it with the passed-in list of sObject records. The keys are populated with

the sObject IDs and the values are the sObjects.

##### Map<T1,T2>()

#### Creates a new instance of the Map class. T1 is the data type of the keys and T2 is the data type of the values.

Signature

```
   public Map<T1,T2>()

```

Example

```
   Map<Integer, String> m1 = new Map<Integer, String>();

   m1.put(1, 'First item');

   m1.put(2, 'Second item');

##### Map<T1,T2>(mapToCopy)

#### Creates a new instance of the Map class and initializes it by copying the entries from the specified map. T1 is the data type of the keys
```

and T2 is the data type of the values.


Apex Reference Guide Map Class

Signature

```
   public Map<T1,T2>(Map<T1,T2> mapToCopy)

```

Parameters

```
   mapToCopy
```

Type: Map<T1, T2>

The map to initialize this map with. T1 is the data type of the keys and T2 is the data type of the values. All map keys and values are
copied to this map.

Example

```
   Map<Integer, String> m1 = new Map<Integer, String>();

   m1.put(1, 'First item');

   m1.put(2, 'Second item');

   Map<Integer, String> m2 = new Map<Integer, String>(m1);

   // The map elements of m2 are copied from m1

   System.debug(m2);

##### Map<ID,sObject>(recordList) Creates a new instance of the Map class and populates it with the passed-in list of sObject records. The keys are populated with the
```

sObject IDs and the values are the sObjects.

Signature

```
   public Map<ID,sObject>(List<sObject> recordList)

```

Parameters

```
   recordList
```

Type: List<sObject>

The list of sObjects to populate the map with.

Example

```
   List<Account> ls = [select Id,Name from Account];

   Map<Id, Account> m = new Map<Id, Account>(ls);

#### Map Methods

##### The following are methods for Map . All are instance methods.

```

IN THIS SECTION:

clear()
Removes all of the key-value mappings from the map.


Apex Reference Guide Map Class

clone()
Makes a duplicate copy of the map.

containsKey(key)
Returns `true` if the map contains a mapping for the specified key.

deepClone()
Makes a duplicate copy of a map, including sObject records if this is a map with sObject record values.

equals(map2)
Compares this map with the specified map and returns `true` if both maps are equal; otherwise, returns `false` .

get(key)
Returns the value to which the specified key is mapped, or `null` if the map contains no value for this key.

getSObjectType()
Returns the token of the sObject type that makes up the map values.

hashCode()
Returns the hashcode corresponding to this map.

isEmpty()
Returns true if the map has zero key-value pairs.

keySet()
Returns a set that contains all of the keys in the map.

put(key, value)
Associates the specified value with the specified key in the map.

putAll(fromMap)
Copies all of the mappings from the specified map to the original map.

putAll(sobjectArray)
Adds the list of sObject records to a map declared as Map<ID, sObject> or Map<String, sObject>.

remove(key)
Removes the mapping for the specified key from the map, if present, and returns the corresponding value.

size()
Returns the number of key-value pairs in the map.

toString()
Returns the string representation of the map.

values()
Returns a list that contains all the values in the map.

##### clear()

Removes all of the key-value mappings from the map.

Signature

```
   public Void clear()

```


Apex Reference Guide Map Class

Return Value

Type: Void

##### clone()

Makes a duplicate copy of the map.

Signature

```
   public Map<Object, Object> clone()

```

Return Value

Type: Map (of same type)

Usage

If this is a map with sObject record values, the duplicate map will only be a shallow copy of the map. That is, the duplicate will have
references to each sObject record, but the records themselves are not duplicated. For example:

To also copy the sObject records, you must use the `deepClone` method.

Example

```
   Account a = new Account(

     Name='Acme',

     BillingCity='New York');

   Map<Integer, Account> map1 = new Map<Integer, Account> {};

   map1.put(1, a);

   Map<Integer, Account> map2 = map1.clone();

   map1.get(1).BillingCity =

   'San Francisco';

   System.assertEquals(

     'San Francisco',

     map1.get(1).BillingCity);

   System.assertEquals(

     'San Francisco',

     map2.get(1).BillingCity);

##### containsKey(key)

```

Returns `true` if the map contains a mapping for the specified key.

Signature

```
   public Boolean containsKey(Object key)

```


Apex Reference Guide Map Class

Parameters

```
   key
```

Type: Object

Return Value

Type: Boolean

Usage

If the key is a string, the key value is case-sensitive.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

   Boolean contains = colorCodes.containsKey('Blue');

   System.assertEquals(true, contains);

##### deepClone()

```

Makes a duplicate copy of a map, including sObject records if this is a map with sObject record values.

Signature

```
   public Map<Object, Object> deepClone()

```

Return Value

Type: Map (of the same type)

Usage

To make a shallow copy of a map without duplicating the sObject records it contains, use the `clone()` method.

Example

```
   Account a = new Account(

     Name='Acme',

     BillingCity='New York');

   Map<Integer, Account> map1 = new Map<Integer, Account> {};

   map1.put(1, a);

   Map<Integer, Account> map2 = map1.deepClone();

   // Update the first entry of map1

```


Apex Reference Guide Map Class

```
   map1.get(1).BillingCity = 'San Francisco';

   // Verify that the BillingCity is updated in map1 but not in map2

   System.assertEquals('San Francisco', map1.get(1).BillingCity);

   System.assertEquals('New York', map2.get(1).BillingCity);

##### equals(map2)

```

Compares this map with the specified map and returns `true` if both maps are equal; otherwise, returns `false` .

Signature

```
   public Boolean equals(Map map2)

```

Parameters

```
   map2
```

Type: Map

The _`map2`_ argument is the map to compare this map with.

Return Value

Type: Boolean

Usage

Two maps are equal if their key/value pairs are identical, regardless of the order of those pairs. The `==` operator is used to compare the
map keys and values.

##### The == operator is equivalent to calling the equals method, so you can call map1.equals(map2); instead of map1 ==

`map2;` .

##### get(key)

Returns the value to which the specified key is mapped, or `null` if the map contains no value for this key.

Signature

```
   public Object get(Object key)

```

Parameters

```
   key
```

Type: Object

Return Value

Type: Object

Usage

If the key is a string, the key value is case-sensitive.


Apex Reference Guide Map Class

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

   String code = colorCodes.get('Blue');

   System.assertEquals('0000A0', code);

   // The following is not a color in the map

   String code2 = colorCodes.get('Magenta');

   System.assertEquals(null, code2);

##### getSObjectType()

```

Returns the token of the sObject type that makes up the map values.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Usage

Use this method with describe information, to determine if a map contains sObjects of a particular type.

Note that this method can only be used with maps that have sObject values.

[For more information, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

Example

```
   // Create a generic sObject variable.

   SObject sObj = Database.query('SELECT Id FROM Account LIMIT 1');

   // Verify if that sObject variable is an Account token.

   System.assertEquals(

     Account.sObjectType,

     sObj.getSObjectType());

   // Create a map of generic sObjects

   Map<Integer, Account> m = new Map<Integer, Account>();

   // Verify if the map contains Account tokens.

   System.assertEquals(

     Account.sObjectType,

     m.getSObjectType());

```


Apex Reference Guide Map Class

##### hashCode()

Returns the hashcode corresponding to this map.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### isEmpty()

Returns true if the map has zero key-value pairs.

Signature

```
   public Boolean isEmpty()

```

Return Value

Type: Boolean

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   Boolean empty = colorCodes.isEmpty();

   System.assertEquals(true, empty);

##### keySet()

```

Returns a set that contains all of the keys in the map.

Signature

```
   public Set<Object> keySet()

```

Return Value

Type: Set (of key type)

The returned keySet is backed by the map, so the keySet reflects any changes made to the map, and vice-versa.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

```


Apex Reference Guide Map Class

```
   Set <String> colorSet = new Set<String>();

   colorSet = colorCodes.keySet();

##### put(key, value)

```

Associates the specified value with the specified key in the map.

Signature

```
   public Object put(Object key, Object value)

```

Parameters

```
   key
```

Type: Object

```
   value
```

Type: Object

Return Value

Type: Object

Usage

If the map previously contained a mapping for this key, the old value is returned by the method and then replaced.

If the key is a string, the key value is case-sensitive.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'ff0000');

   colorCodes.put('Red', '#FF0000');

   // Red is now #FF0000

##### putAll(fromMap)

```

Copies all of the mappings from the specified map to the original map.

Signature

```
   public Void putAll(Map fromMap)

```

Parameters

```
   fromMap
```

Type: Map


Apex Reference Guide Map Class

Return Value

Type: Void

Usage

The new mappings from _`fromMap`_ are merged with any mappings that existed in the original map. If any of the keys match, the
original map values are replaced by corresponding values in the new mapping.

Example

```
   Map<String, String> map1 = new Map<String, String>();

   map1.put('Red','FF0000');

   Map<String, String> map2 = new Map<String, String>();

   map2.put('Blue','0000FF');

   // Add map1 entries to map2

   map2.putAll(map1);

   System.assertEquals(2, map2.size());

##### putAll(sobjectArray)

```

Adds the list of sObject records to a map declared as Map<ID, sObject> or Map<String, sObject>.

Signature

```
   public Void putAll(sObject[] sobjectArray)

```

Parameters

```
   sobjectArray
```

Type: sObject[]

Return Value

Type: Void

Usage

This method is similar to calling the Map constructor with the same input.

Example

```
   List<Account> accts = new List<Account>();

   accts.add(new Account(Name='Account1'));

   accts.add(new Account(Name='Account2'));

   // Insert accounts so their IDs are populated.

   insert accts;

   Map<Id, Account> m = new Map<Id, Account>();

   // Add all the records to the map.

   m.putAll(accts);

   System.assertEquals(2, m.size());

```


Apex Reference Guide Map Class

##### remove(key)

Removes the mapping for the specified key from the map, if present, and returns the corresponding value.

Signature

```
   public Object remove(Key key)

```

Parameters

```
   key
```

Type: Key

Return Value

Type: Object

Usage

If the key is a string, the key value is case-sensitive.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

   String myColor = colorCodes.remove('Blue');

   String code2 = colorCodes.get('Blue');

   System.assertEquals(null, code2);

##### size()

```

Returns the number of key-value pairs in the map.

Signature

```
   public Integer size()

```

Return Value

Type: Integer

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

```


Apex Reference Guide Map Class

```
   Integer mSize = colorCodes.size();

   system.assertEquals(2, mSize);

##### toString()

```

Returns the string representation of the map.

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

##### values()

Returns a list that contains all the values in the map.

Signature

```
   public List<Object> values()

```

Return Value

Type: List<Object>

Usage

The order of map elements is deterministic. You can rely on the order being the same in each subsequent execution of the same code.
##### For example, suppose the values() method returns a list containing value1 and index 0 and value2 and index 1. Subsequent

runs of the same code result in those values being returned in the same order.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

   List<String> colors = new List<String>();

   colors = colorCodes.values();

```


### Apex Reference Guide Matcher Class Matcher Class

Matchers use Patterns to perform match operations on a character string.

Namespace

System

#### Matcher Methods

### The following are methods for Matcher .

IN THIS SECTION:

end()
Returns the position after the last matched character.

end(groupIndex)
Returns the position after the last character of the subsequence captured by the group index during the previous match operation.
If the match was successful but the group itself did not match anything, this method returns -1.

find()
Attempts to find the next subsequence of the input sequence that matches the pattern. This method returns true if a subsequence
of the input sequence matches this Matcher object's pattern.

find(group)
Resets the Matcher object and then tries to find the next subsequence of the input sequence that matches the pattern. This method
returns `true` if a subsequence of the input sequence matches this Matcher object's pattern.

group()
Returns the input subsequence returned by the previous match.

group(groupIndex)
Returns the input subsequence captured by the specified group index during the previous match operation. If the match was
successful but the specified group failed to match any part of the input sequence, `null` is returned.

groupCount()
Returns the number of capturing groups in this Matching object's pattern. Group zero denotes the entire pattern and is not included
in this count.

hasAnchoringBounds()
Returns true if the Matcher object has anchoring bounds, false otherwise. By default, a Matcher object uses anchoring bounds regions.

hasTransparentBounds()
Returns true if the Matcher object has transparent bounds, false if it uses opaque bounds. By default, a Matcher object uses opaque
region boundaries.

hitEnd()
Returns true if the end of input was found by the search engine in the last match operation performed by this Matcher object. When
this method returns true, it is possible that more input would have changed the result of the last search.

lookingAt()
Attempts to match the input sequence, starting at the beginning of the region, against the pattern.


Apex Reference Guide Matcher Class

matches()
Attempts to match the entire region against the pattern.

pattern()
Returns the Pattern object from which this Matcher object was created.

quoteReplacement(inputString)
Returns a literal replacement string for the specified string _`inputString`_ . The characters in the returned string match the sequence
of characters in _`inputString`_ .

region(start, end)
Sets the limits of this Matcher object's region. The region is the part of the input sequence that is searched to find a match.

regionEnd()
Returns the end index (exclusive) of this Matcher object's region.

regionStart()
Returns the start index (inclusive) of this Matcher object's region.

replaceAll(replacementString)
Replaces every subsequence of the input sequence that matches the pattern with the replacement string.

replaceFirst(replacementString)
Replaces the first subsequence of the input sequence that matches the pattern with the replacement string.

requireEnd()
Returns true if more input could change a positive match into a negative one.

reset()
Resets this Matcher object. Resetting a Matcher object discards all of its explicit state information.

reset(inputSequence)
Resets this Matcher object with the new input sequence. Resetting a Matcher object discards all of its explicit state information.

start()
Returns the start index of the first character of the previous match.

start(groupIndex)
Returns the start index of the subsequence captured by the group specified by the group index during the previous match operation.
Captured groups are indexed from left to right, starting at one. Group zero denotes the entire pattern, so the expression `m.start(0)`
is equivalent to `m.start()` .

useAnchoringBounds(anchoringBounds)
Sets the anchoring bounds of the region for the Matcher object. By default, a Matcher object uses anchoring bounds regions.

usePattern(pattern)
Changes the Pattern object that the Matcher object uses to find matches. This method causes the Matcher object to lose information
about the groups of the last match that occurred. The Matcher object's position in the input is maintained.

useTransparentBounds(transparentBounds)
Sets the transparency bounds for this Matcher object. By default, a Matcher object uses anchoring bounds regions.

##### end()

Returns the position after the last matched character.


Apex Reference Guide Matcher Class

Signature

```
   public Integer end()

```

Return Value

Type: Integer

##### end(groupIndex)

Returns the position after the last character of the subsequence captured by the group index during the previous match operation. If
the match was successful but the group itself did not match anything, this method returns -1.

Signature

```
   public Integer end(Integer groupIndex)

```

Parameters

```
   groupIndex
```

Type: Integer

Return Value

Type: Integer

Usage

Captured groups are indexed from left to right, starting at one. Group zero denotes the entire pattern, so the expression `m.end(0)` is
equivalent to `m.end()` .

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

##### find()

Attempts to find the next subsequence of the input sequence that matches the pattern. This method returns true if a subsequence of
the input sequence matches this Matcher object's pattern.

Signature

```
   public Boolean find()

```

Return Value

Type: Boolean

Usage

This method starts at the beginning of this Matcher object's region, or, if a previous invocation of the method was successful and the
Matcher object has not since been reset, at the first character not matched by the previous match.

##### If the match succeeds, more information can be obtained using the start, end, and group methods.


Apex Reference Guide Matcher Class

[For more information, see Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### find(group)

Resets the Matcher object and then tries to find the next subsequence of the input sequence that matches the pattern. This method
returns `true` if a subsequence of the input sequence matches this Matcher object's pattern.

Signature

```
   public Boolean find(Integer group)

```

Parameters

##### _`group`_

Type: Integer

Return Value

Type: Boolean

Usage

##### If the match succeeds, more information can be obtained using the start, end, and group methods. group()

Returns the input subsequence returned by the previous match.

Signature

```
   public String group()

```

Return Value

Type: String

Usage

Note that some groups, such as `(a*)`, match the empty string. This method returns the empty string when such a group successfully
matches the empty string in the input.

##### group(groupIndex)

Returns the input subsequence captured by the specified group index during the previous match operation. If the match was successful
but the specified group failed to match any part of the input sequence, `null` is returned.

Signature

```
   public String group(Integer groupIndex)

```


Apex Reference Guide Matcher Class

Parameters

```
   groupIndex
```

Type: Integer

Return Value

Type: String

Usage

Captured groups are indexed from left to right, starting at one. Group zero denotes the entire pattern, so the expression `m.group(0)`
is equivalent to `m.group()` .

Note that some groups, such as `(a*)`, match the empty string. This method returns the empty string when such a group successfully
matches the empty string in the input.

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

##### groupCount()

Returns the number of capturing groups in this Matching object's pattern. Group zero denotes the entire pattern and is not included in
this count.

Signature

```
   public Integer groupCount()

```

Return Value

Type: Integer

Usage

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

##### hasAnchoringBounds()

Returns true if the Matcher object has anchoring bounds, false otherwise. By default, a Matcher object uses anchoring bounds regions.

Signature

```
   public Boolean hasAnchoringBounds()

```

Return Value

Type: Boolean

Usage

If a Matcher object uses anchoring bounds, the boundaries of this Matcher object's region match start and end of line anchors such as
^ and $.


Apex Reference Guide Matcher Class

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

##### hasTransparentBounds()

Returns true if the Matcher object has transparent bounds, false if it uses opaque bounds. By default, a Matcher object uses opaque
region boundaries.

Signature

```
   public Boolean hasTransparentBounds()

```

Return Value

Type: Boolean

Usage

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

##### hitEnd()

Returns true if the end of input was found by the search engine in the last match operation performed by this Matcher object. When
this method returns true, it is possible that more input would have changed the result of the last search.

Signature

```
   public Boolean hitEnd()

```

Return Value

Type: Boolean

##### lookingAt()

Attempts to match the input sequence, starting at the beginning of the region, against the pattern.

Signature

```
   public Boolean lookingAt()

```

Return Value

Type: Boolean

Usage

Like the `matches` method, this method always starts at the beginning of the region; unlike that method, it does not require the entire
region be matched.

If the match succeeds, more information can be obtained using the `start`, `end`, and `group` methods.

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)


Apex Reference Guide Matcher Class

##### matches()

Attempts to match the entire region against the pattern.

Signature

```
   public Boolean matches()

```

Return Value

Type: Boolean

Usage

If the match succeeds, more information can be obtained using the `start`, `end`, and `group` methods.

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### pattern()

Returns the Pattern object from which this Matcher object was created.

Signature

```
   public Pattern object pattern()

```

Return Value

Type: System.Pattern

##### quoteReplacement(inputString)

Returns a literal replacement string for the specified string _`inputString`_ . The characters in the returned string match the sequence
of characters in _`inputString`_ .

Signature

```
   public static String quoteReplacement(String inputString)

```

Parameters

```
   inputString
```

Type: String

Return Value

Type: String

Usage

Metacharacters (such as `$` or `^` ) and escape sequences in the input string are treated as literal characters with no special meaning.


Apex Reference Guide Matcher Class

##### region(start, end)

Sets the limits of this Matcher object's region. The region is the part of the input sequence that is searched to find a match.

Signature

```
   public Matcher object region(Integer start, Integer end)

```

Parameters

```
   start
```

Type: Integer

```
   end
```

Type: Integer

Return Value

Type: Matcher

Usage

This method first resets the Matcher object, then sets the region to start at the index specified by `start` and end at the index specified
by `end` .

Depending on the transparency boundaries being used, certain constructs such as anchors may behave differently at or around the
boundaries of the region.

[See Using Regions and Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### regionEnd()

Returns the end index (exclusive) of this Matcher object's region.

Signature

```
   public Integer regionEnd()

```

Return Value

Type: Integer

Usage

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### regionStart()

Returns the start index (inclusive) of this Matcher object's region.

Signature

```
   public Integer regionStart()

```


Apex Reference Guide Matcher Class

Return Value

Type: Integer

Usage

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### replaceAll(replacementString)

Replaces every subsequence of the input sequence that matches the pattern with the replacement string.

Signature

```
   public String replaceAll(String replacementString)

```

Parameters

```
   replacementString
```

Type: String

Return Value

Type: String

Usage

This method first resets the Matcher object, then scans the input sequence looking for matches of the pattern. Characters that are not
part of any match are appended directly to the result string; each match is replaced in the result by the replacement string. The replacement
string may contain references to captured subsequences.

Note that backslashes (\) and dollar signs ($) in the replacement string may cause the results to be different than if the string was treated
as a literal replacement string. Dollar signs may be treated as references to captured subsequences, and backslashes are used to escape
literal characters in the replacement string.

Invoking this method changes this Matcher object's state. If the Matcher object is to be used in further matching operations it should
first be reset.

Given the regular expression `a*b`, the input `"aabxyzaabxyzabxyzb"`, and the replacement string `"-"`, an invocation of this
method on a Matcher object for that expression would yield the string `"-xyz-xyz-xyz-"` .

##### replaceFirst(replacementString)

Replaces the first subsequence of the input sequence that matches the pattern with the replacement string.

Signature

```
   public String replaceFirst(String replacementString)

```

Parameters

```
   replacementString
```

Type: String


Apex Reference Guide Matcher Class

Return Value

Type: String

Usage

Note that backslashes (\) and dollar signs ($) in the replacement string may cause the results to be different than if the string was treated
as a literal replacement string. Dollar signs may be treated as references to captured subsequences, and backslashes are used to escape
literal characters in the replacement string.

Invoking this method changes this Matcher object's state. If the Matcher object is to be used in further matching operations it should
first be reset.

Given the regular expression `dog`, the input `"zzzdogzzzdogzzz"`, and the replacement string `"cat"`, an invocation of this
method on a Matcher object for that expression would return the string `"zzzcatzzzdogzzz"` .

##### requireEnd()

Returns true if more input could change a positive match into a negative one.

Signature

```
   public Boolean requireEnd()

```

Return Value

Type: Boolean

Usage

If this method returns true, and a match was found, then more input could cause the match to be lost.

If this method returns false and a match was found, then more input might change the match but the match won't be lost.

##### If a match was not found, then requireEnd has no meaning. reset()

Resets this Matcher object. Resetting a Matcher object discards all of its explicit state information.

Signature

```
   public Matcher object reset()

```

Return Value

Type: Matcher

Usage

This method does not change whether the Matcher object uses anchoring bounds. You must explicitly use the `useAnchoringBounds`
method to change the anchoring bounds.

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)


Apex Reference Guide Matcher Class

##### reset(inputSequence)

Resets this Matcher object with the new input sequence. Resetting a Matcher object discards all of its explicit state information.

Signature

```
   public Matcher reset(String inputSequence)

```

Parameters

```
   inputSequence
```

Type: String

Return Value

Type: Matcher

##### start()

Returns the start index of the first character of the previous match.

Signature

```
   public Integer start()

```

Return Value

Type: Integer

##### start(groupIndex)

Returns the start index of the subsequence captured by the group specified by the group index during the previous match operation.
Captured groups are indexed from left to right, starting at one. Group zero denotes the entire pattern, so the expression `m.start(0)`
is equivalent to `m.start()` .

Signature

```
   public Integer start(Integer groupIndex)

```

Parameters

```
   groupIndex
```

Type: Integer

Return Value

Type: Integer

Usage

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)


Apex Reference Guide Matcher Class

##### useAnchoringBounds(anchoringBounds)

Sets the anchoring bounds of the region for the Matcher object. By default, a Matcher object uses anchoring bounds regions.

Signature

```
   public Matcher object useAnchoringBounds(Boolean anchoringBounds)

```

Parameters

```
   anchoringBounds
```

Type: Boolean

If you specify `true`, the Matcher object uses anchoring bounds. If you specify `false`, non-anchoring bounds are used.

Return Value

Type: Matcher

Usage

If a Matcher object uses anchoring bounds, the boundaries of this Matcher object's region match start and end of line anchors such as
^ and $.

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

##### usePattern(pattern)

Changes the Pattern object that the Matcher object uses to find matches. This method causes the Matcher object to lose information
about the groups of the last match that occurred. The Matcher object's position in the input is maintained.

Signature

```
   public Matcher object usePattern(Pattern pattern)

```

Parameters

```
   pattern
```

Type: System.Pattern

Return Value

Type: Matcher

##### useTransparentBounds(transparentBounds)

Sets the transparency bounds for this Matcher object. By default, a Matcher object uses anchoring bounds regions.

Signature

```
   public Matcher object useTransparentBounds(Boolean transparentBounds)

```


### Apex Reference Guide Math Class

Parameters

```
   transparentBounds
```

Type: Boolean

If you specify `true`, the Matcher object uses transparent bounds. If you specify `false`, opaque bounds are used.

Return Value

Type: Matcher

Usage

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

### Math Class

Contains methods for mathematical operations.

Namespace

System

#### Math Fields

### The following are fields for Math .

IN THIS SECTION:

##### E

Returns the mathematical constant _e_, which is the base of natural logarithms.

##### PI

Returns the mathematical constant _pi_, which is the ratio of the circumference of a circle to its diameter.

##### E

Returns the mathematical constant _e_, which is the base of natural logarithms.

Signature

```
   public static final Double E

```

Property Value

Type: Double

##### PI

Returns the mathematical constant _pi_, which is the ratio of the circumference of a circle to its diameter.


Apex Reference Guide Math Class

Signature

```
   public static final Double PI

```

Property Value

Type: Double

#### Math Methods The following are methods for Math . All methods are static.

IN THIS SECTION:

abs(decimalValue)
Returns the absolute value of the specified Decimal.

abs(doubleValue)
Returns the absolute value of the specified Double.

abs(integerValue)
Returns the absolute value of the specified Integer.

abs(longValue)
Returns the absolute value of the specified Long.

acos(decimalAngle)
Returns the arc cosine of an angle, in the range of 0.0 through _pi_ .

acos(doubleAngle)
Returns the arc cosine of an angle, in the range of 0.0 through _pi_ .

asin(decimalAngle)
Returns the arc sine of an angle, in the range of - _pi_ /2 through _pi_ /2.

asin(doubleAngle)
Returns the arc sine of an angle, in the range of - _pi_ /2 through _pi_ /2.

atan(decimalAngle)
Returns the arc tangent of an angle, in the range of - _pi_ /2 through _pi_ /2.

atan(doubleAngle)
Returns the arc tangent of an angle, in the range of - _pi_ /2 through _pi_ /2.

atan2(xCoordinate, yCoordinate)
Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the
phase _`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

atan2(xCoordinate, yCoordinate)
Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the
phase _`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

cbrt(decimalValue)
Returns the cube root of the specified Decimal. The cube root of a negative value is the negative of the cube root of that value's
magnitude.


Apex Reference Guide Math Class

cbrt(doubleValue)
Returns the cube root of the specified Double. The cube root of a negative value is the negative of the cube root of that value's
magnitude.

ceil(decimalValue)
Returns the smallest (closest to negative infinity) Decimal that is not less than the argument and is equal to a mathematical integer.

ceil(doubleValue)
Returns the smallest (closest to negative infinity) Double that is not less than the argument and is equal to a mathematical integer.

cos(decimalAngle)
Returns the trigonometric cosine of the angle specified by _`decimalAngle`_ .

cos(doubleAngle)
Returns the trigonometric cosine of the angle specified by _`doubleAngle`_ .

cosh(decimalAngle)
Returns the hyperbolic cosine of _`decimalAngle`_ . The hyperbolic cosine of _`d`_ is defined to be ( _e_ [x] + _e_ [-x] )/2 where _e_ is Euler's number.

cosh(doubleAngle)
Returns the hyperbolic cosine of _`doubleAngle`_ . The hyperbolic cosine of _`d`_ is defined to be ( _e_ [x] + _e_ [-x] )/2 where _e_ is Euler's number.

exp(exponentDecimal)
Returns Euler's number _e_ raised to the power of the specified Decimal.

exp(exponentDouble)
Returns Euler's number _e_ raised to the power of the specified Double.

floor(decimalValue)
Returns the largest (closest to positive infinity) Decimal that is not greater than the argument and is equal to a mathematical integer.

floor(doubleValue)
Returns the largest (closest to positive infinity) Double that is not greater than the argument and is equal to a mathematical integer.

log(decimalValue)
Returns the natural logarithm (base _e_ ) of the specified Decimal.

log(doubleValue)
Returns the natural logarithm (base _e_ ) of the specified Double.

log10(decimalValue)
Returns the logarithm (base _10_ ) of the specified Decimal.

log10(doubleValue)
Returns the logarithm (base _10_ ) of the specified Double.

max(decimalValue1, decimalValue2)
Returns the larger of the two specified Decimals.

max(doubleValue1, doubleValue2)
Returns the larger of the two specified Doubles.

max(integerValue1, integerValue2)
Returns the larger of the two specified Integers.

max(longValue1, longValue2)
Returns the larger of the two specified Longs.

min(decimalValue1, decimalValue2)
Returns the smaller of the two specified Decimals.


Apex Reference Guide Math Class

min(doubleValue1, doubleValue2)
Returns the smaller of the two specified Doubles.

min(integerValue1, integerValue2)
Returns the smaller of the two specified Integers.

min(longValue1, longValue2)
Returns the smaller of the two specified Longs.

mod(integerValue1, integerValue2)
Returns the remainder of _`integerValue1`_ divided by _`integerValue2`_ .

mod(longValue1, longValue2)
Returns the remainder of _`longValue1`_ divided by _`longValue2`_ .

pow(doubleValue, exponent)
Returns the value of the first Double raised to the power of _`exponent`_ .

random()
Returns a positive Double that is greater than or equal to 0.0 and less than 1.0.

rint(decimalValue)
Returns the value that is closest in value to _`decimalValue`_ and is equal to a mathematical integer.

rint(doubleValue)
Returns the value that is closest in value to _`doubleValue`_ and is equal to a mathematical integer.

round(doubleValue)
Do not use. This method is deprecated as of the Winter '08 release. Instead, use `Math.roundToLong` . Returns the closest Integer
to the specified Double. If the result is less than -2,147,483,648 or greater than 2,147,483,647, Apex generates an error.

round(decimalValue)
Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards
the even neighbor. If the result is less than -2,147,483,648 or greater than 2,147,483,647, Apex generates an error.

roundToLong(decimalValue)
Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards
the even neighbor.

roundToLong(doubleValue)
Returns the closest Long to the specified Double.

signum(decimalValue)
Returns the signum function of the specified Decimal, which is 0 if _`decimalValue`_ is 0, 1.0 if _`decimalValue`_ is greater than
0, -1.0 if _`decimalValue`_ is less than 0.

signum(doubleValue)
Returns the signum function of the specified Double, which is 0 if _`doubleValue`_ is 0, 1.0 if _`doubleValue`_ is greater than 0,
-1.0 if _`doubleValue`_ is less than 0.

sin(decimalAngle)
Returns the trigonometric sine of the angle specified by _`decimalAngle`_ .

sin(doubleAngle)
Returns the trigonometric sine of the angle specified by _`doubleAngle`_ .


Apex Reference Guide Math Class

sinh(decimalAngle)
Returns the hyperbolic sine of _`decimalAngle`_ . The hyperbolic sine of _`decimalAngle`_ is defined to be ( _e_ [x]       - _e_ [-x] )/2 where _e_ is
Euler's number.

sinh(doubleAngle)
Returns the hyperbolic sine of _`doubleAngle`_ . The hyperbolic sine of _`doubleAngle`_ is defined to be ( _e_ [x]       - _e_ [-x] )/2 where _e_ is
Euler's number.

sqrt(decimalValue)
Returns the correctly rounded positive square root of _`decimalValue`_ .

sqrt(doubleValue)
Returns the correctly rounded positive square root of _`doubleValue`_ .

tan(decimalAngle)
Returns the trigonometric tangent of the angle specified by _`decimalAngle`_ .

tan(doubleAngle)
Returns the trigonometric tangent of the angle specified by _`doubleAngle`_ .

tanh(decimalAngle)
Returns the hyperbolic tangent of _`decimalAngle`_ . The hyperbolic tangent of _`decimalAngle`_ is defined to be ( _e_ [x]      - _e_ [-x] )/( _e_ [x] +
_e_ [-x] ) where _e_ is Euler's number. In other words, it is equivalent to `sinh(x)/cosinh(x)` . The absolute value of the exact `tanh`
is always less than 1.

tanh(doubleAngle)
Returns the hyperbolic tangent of _`doubleAngle`_ . The hyperbolic tangent of _`doubleAngle`_ is defined to be ( _e_ [x]      - _e_ [-x] )/( _e_ [x] + _e_ [-x] )
where _e_ is Euler's number. In other words, it is equivalent to `sinh(x)/cosinh(x)` . The absolute value of the exact `tanh` is
always less than 1.

##### abs(decimalValue)

Returns the absolute value of the specified Decimal.

Signature

```
   public static Decimal abs(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### abs(doubleValue)

Returns the absolute value of the specified Double.

Signature

```
   public static Double abs(Double doubleValue)

```


Apex Reference Guide Math Class

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### abs(integerValue)

Returns the absolute value of the specified Integer.

Signature

```
   public static Integer abs(Integer integerValue)

```

Parameters

```
   integerValue
```

Type: Integer

Return Value

Type: Integer

Example

```
   Integer i = -42;

   Integer i2 = math.abs(i);

   system.assertEquals(i2, 42);

##### abs(longValue)

```

Returns the absolute value of the specified Long.

Signature

```
   public static Long abs(Long longValue)

```

Parameters

```
   longValue
```

Type: Long

Return Value

Type: Long


Apex Reference Guide Math Class

##### acos(decimalAngle)

Returns the arc cosine of an angle, in the range of 0.0 through _pi_ .

Signature

```
   public static Decimal acos(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### acos(doubleAngle)

Returns the arc cosine of an angle, in the range of 0.0 through _pi_ .

Signature

```
   public static Double acos(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### asin(decimalAngle)

Returns the arc sine of an angle, in the range of - _pi_ /2 through _pi_ /2.

Signature

```
   public static Decimal asin(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal


Apex Reference Guide Math Class

##### asin(doubleAngle)

Returns the arc sine of an angle, in the range of - _pi_ /2 through _pi_ /2.

Signature

```
   public static Double asin(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### atan(decimalAngle)

Returns the arc tangent of an angle, in the range of - _pi_ /2 through _pi_ /2.

Signature

```
   public static Decimal atan(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### atan(doubleAngle)

Returns the arc tangent of an angle, in the range of - _pi_ /2 through _pi_ /2.

Signature

```
   public static Double atan(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double


Apex Reference Guide Math Class

##### atan2(xCoordinate, yCoordinate)

Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the phase
_`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

Signature

```
   public static Decimal atan2(Decimal xCoordinate, Decimal yCoordinate)

```

Parameters

```
   xCoordinate
```

Type: Decimal

```
   yCoordinate
```

Type: Decimal

Return Value

Type: Decimal

##### atan2(xCoordinate, yCoordinate)

Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the phase
_`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

Signature

```
   public static Double atan2(Double xCoordinate, Double yCoordinate)

```

Parameters

```
   xCoordinate
```

Type: Double

```
   yCoordinate
```

Type: Double

Return Value

Type: Double

##### cbrt(decimalValue)

Returns the cube root of the specified Decimal. The cube root of a negative value is the negative of the cube root of that value's magnitude.

Signature

```
   public static Decimal cbrt(Decimal decimalValue)

```


Apex Reference Guide Math Class

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### cbrt(doubleValue)

Returns the cube root of the specified Double. The cube root of a negative value is the negative of the cube root of that value's magnitude.

Signature

```
   public static Double cbrt(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### ceil(decimalValue)

Returns the smallest (closest to negative infinity) Decimal that is not less than the argument and is equal to a mathematical integer.

Signature

```
   public static Decimal ceil(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### ceil(doubleValue)

Returns the smallest (closest to negative infinity) Double that is not less than the argument and is equal to a mathematical integer.

Signature

```
   public static Double ceil(Double doubleValue)

```


Apex Reference Guide Math Class

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### cos(decimalAngle)

Returns the trigonometric cosine of the angle specified by _`decimalAngle`_ .

Signature

```
   public static Decimal cos(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### cos(doubleAngle)

Returns the trigonometric cosine of the angle specified by _`doubleAngle`_ .

Signature

```
   public static Double cos(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### cosh(decimalAngle)

Returns the hyperbolic cosine of _`decimalAngle`_ . The hyperbolic cosine of _`d`_ is defined to be ( _e_ [x] + _e_ [-x] )/2 where _e_ is Euler's number.

Signature

```
   public static Decimal cosh(Decimal decimalAngle)

```


Apex Reference Guide Math Class

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### cosh(doubleAngle) Returns the hyperbolic cosine of doubleAngle . The hyperbolic cosine of d is defined to be ( e [x] + e [-x] )/2 where e is Euler's number.

Signature

```
   public static Double cosh(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### exp(exponentDecimal) Returns Euler's number e raised to the power of the specified Decimal.

Signature

```
   public static Decimal exp(Decimal exponentDecimal)

```

Parameters

```
   exponentDecimal
```

Type: Decimal

Return Value

Type: Decimal

##### exp(exponentDouble) Returns Euler's number e raised to the power of the specified Double.

Signature

```
   public static Double exp(Double exponentDouble)

```


Apex Reference Guide Math Class

Parameters

```
   exponentDouble
```

Type: Double

Return Value

Type: Double

##### floor(decimalValue)

Returns the largest (closest to positive infinity) Decimal that is not greater than the argument and is equal to a mathematical integer.

Signature

```
   public static Decimal floor(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### floor(doubleValue)

Returns the largest (closest to positive infinity) Double that is not greater than the argument and is equal to a mathematical integer.

Signature

```
   public static Double floor(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### log(decimalValue)

Returns the natural logarithm (base _e_ ) of the specified Decimal.

Signature

```
   public static Decimal log(Decimal decimalValue)

```


Apex Reference Guide Math Class

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### log(doubleValue)

Returns the natural logarithm (base _e_ ) of the specified Double.

Signature

```
   public static Double log(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### log10(decimalValue)

Returns the logarithm (base _10_ ) of the specified Decimal.

Signature

```
   public static Decimal log10(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### log10(doubleValue)

Returns the logarithm (base _10_ ) of the specified Double.

Signature

```
   public static Double log10(Double doubleValue)

```


Apex Reference Guide Math Class

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### max(decimalValue1, decimalValue2)

Returns the larger of the two specified Decimals.

Signature

```
   public static Decimal max(Decimal decimalValue1, Decimal decimalValue2)

```

Parameters

```
   decimalValue1
```

Type: Decimal

```
   decimalValue2
```

Type: Decimal

Return Value

Type: Decimal

Example

```
   Decimal larger = math.max(12.3, 156.6);

   system.assertEquals(larger, 156.6);

##### max(doubleValue1, doubleValue2)

```

Returns the larger of the two specified Doubles.

Signature

```
   public static Double max(Double doubleValue1, Double doubleValue2)

```

Parameters

```
   doubleValue1
```

Type: Double

```
   doubleValue2
```

Type: Double


Apex Reference Guide Math Class

Return Value

Type: Double

##### max(integerValue1, integerValue2)

Returns the larger of the two specified Integers.

Signature

```
   public static Integer max(Integer integerValue1, Integer integerValue2)

```

Parameters

```
   integerValue1
```

Type: Integer

```
   integerValue2
```

Type: Integer

Return Value

Type: Integer

##### max(longValue1, longValue2)

Returns the larger of the two specified Longs.

Signature

```
   public static Long max(Long longValue1, Long longValue2)

```

Parameters

```
   longValue1
```

Type: Long

```
   longValue2
```

Type: Long

Return Value

Type: Long

##### min(decimalValue1, decimalValue2)

Returns the smaller of the two specified Decimals.

Signature

```
   public static Decimal min(Decimal decimalValue1, Decimal decimalValue2)

```


Apex Reference Guide Math Class

Parameters

```
   decimalValue1
```

Type: Decimal

```
   decimalValue2
```

Type: Decimal

Return Value

Type: Decimal

Example

```
   Decimal smaller = math.min(12.3, 156.6);

   system.assertEquals(smaller, 12.3);

##### min(doubleValue1, doubleValue2)

```

Returns the smaller of the two specified Doubles.

Signature

```
   public static Double min(Double doubleValue1, Double doubleValue2)

```

Parameters

```
   doubleValue1
```

Type: Double

```
   doubleValue2
```

Type: Double

Return Value

Type: Double

##### min(integerValue1, integerValue2)

Returns the smaller of the two specified Integers.

Signature

```
   public static Integer min(Integer integerValue1, Integer integerValue2)

```

Parameters

```
   integerValue1
```

Type: Integer

```
   integerValue2
```

Type: Integer


Apex Reference Guide Math Class

Return Value

Type: Integer

##### min(longValue1, longValue2)

Returns the smaller of the two specified Longs.

Signature

```
   public static Long min(Long longValue1, Long longValue2)

```

Parameters

```
   longValue1
```

Type: Long

```
   longValue2
```

Type: Long

Return Value

Type: Long

##### mod(integerValue1, integerValue2)

Returns the remainder of _`integerValue1`_ divided by _`integerValue2`_ .

Signature

```
   public static Integer mod(Integer integerValue1, Integer integerValue2)

```

Parameters

```
   integerValue1
```

Type: Integer

```
   integerValue2
```

Type: Integer

Return Value

Type: Integer

Example

```
   Integer remainder = math.mod(12, 2);

   system.assertEquals(remainder, 0);

   Integer remainder2 = math.mod(8, 3);

   system.assertEquals(remainder2, 2);

```


Apex Reference Guide Math Class

##### mod(longValue1, longValue2)

Returns the remainder of _`longValue1`_ divided by _`longValue2`_ .

Signature

```
   public static Long mod(Long longValue1, Long longValue2)

```

Parameters

```
   longValue1
```

Type: Long

```
   longValue2
```

Type: Long

Return Value

Type: Long

##### pow(doubleValue, exponent)

Returns the value of the first Double raised to the power of _`exponent`_ .

Signature

```
   public static Double pow(Double doubleValue, Double exponent)

```

Parameters

```
   doubleValue
```

Type: Double

```
   exponent
```

Type: Double

Return Value

Type: Double

##### random()

Returns a positive Double that is greater than or equal to 0.0 and less than 1.0.

Signature

```
   public static Double random()

```

Return Value

Type: Double


Apex Reference Guide Math Class

##### rint(decimalValue)

Returns the value that is closest in value to _`decimalValue`_ and is equal to a mathematical integer.

Signature

```
   public static Decimal rint(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal

##### rint(doubleValue)

Returns the value that is closest in value to _`doubleValue`_ and is equal to a mathematical integer.

Signature

```
   public static Double rint(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### round(doubleValue)

Do not use. This method is deprecated as of the Winter '08 release. Instead, use `Math.roundToLong` . Returns the closest Integer
to the specified Double. If the result is less than -2,147,483,648 or greater than 2,147,483,647, Apex generates an error.

Signature

```
   public static Integer round(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Integer


Apex Reference Guide Math Class

##### round(decimalValue)

Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards the
even neighbor. If the result is less than -2,147,483,648 or greater than 2,147,483,647, Apex generates an error.

Signature

```
   public static Integer round(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Integer

Usage

Note that this rounding mode statistically minimizes cumulative error when applied repeatedly over a sequence of calculations.

Example

```
   Decimal d1 = 4.5;

   Integer i1 = Math.round(d1);

   System.assertEquals(4, i1);

   Decimal d2 = 5.5;

   Integer i2 = Math.round(d2);

   System.assertEquals(6, i2);

##### roundToLong(decimalValue)

```

Returns the rounded approximation of this Decimal. The number is rounded to zero decimal places using half-even rounding mode,
that is, it rounds towards the “nearest neighbor” unless both neighbors are equidistant, in which case, this mode rounds towards the
even neighbor.

Signature

```
   public static Long roundToLong(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Long


Apex Reference Guide Math Class

Usage

Note that this rounding mode statistically minimizes cumulative error when applied repeatedly over a sequence of calculations.

Example

```
   Decimal d1 = 4.5;

   Long i1 = Math.roundToLong(d1);

   System.assertEquals(4, i1);

   Decimal d2 = 5.5;

   Long i2 = Math.roundToLong(d2);

   System.assertEquals(6, i2);

##### roundToLong(doubleValue)

```

Returns the closest Long to the specified Double.

Signature

```
   public static Long roundToLong(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Long

##### signum(decimalValue)

Returns the signum function of the specified Decimal, which is 0 if _`decimalValue`_ is 0, 1.0 if _`decimalValue`_ is greater than 0,
-1.0 if _`decimalValue`_ is less than 0.

Signature

```
   public static Decimal signum(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal

Return Value

Type: Decimal


Apex Reference Guide Math Class

##### signum(doubleValue)

Returns the signum function of the specified Double, which is 0 if _`doubleValue`_ is 0, 1.0 if _`doubleValue`_ is greater than 0, -1.0
if _`doubleValue`_ is less than 0.

Signature

```
   public static Double signum(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### sin(decimalAngle)

Returns the trigonometric sine of the angle specified by _`decimalAngle`_ .

Signature

```
   public static Decimal sin(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### sin(doubleAngle)

Returns the trigonometric sine of the angle specified by _`doubleAngle`_ .

Signature

```
   public static Double sin(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double


Apex Reference Guide Math Class

##### sinh(decimalAngle)

Returns the hyperbolic sine of _`decimalAngle`_ . The hyperbolic sine of _`decimalAngle`_ is defined to be ( _e_ [x]     - _e_ [-x] )/2 where _e_ is Euler's
number.

Signature

```
   public static Decimal sinh(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### sinh(doubleAngle)

Returns the hyperbolic sine of _`doubleAngle`_ . The hyperbolic sine of _`doubleAngle`_ is defined to be ( _e_ [x]     - _e_ [-x] )/2 where _e_ is Euler's
number.

Signature

```
   public static Double sinh(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### sqrt(decimalValue)

Returns the correctly rounded positive square root of _`decimalValue`_ .

Signature

```
   public static Decimal sqrt(Decimal decimalValue)

```

Parameters

```
   decimalValue
```

Type: Decimal


Apex Reference Guide Math Class

Return Value

Type: Decimal

##### sqrt(doubleValue)

Returns the correctly rounded positive square root of _`doubleValue`_ .

Signature

```
   public static Double sqrt(Double doubleValue)

```

Parameters

```
   doubleValue
```

Type: Double

Return Value

Type: Double

##### tan(decimalAngle)

Returns the trigonometric tangent of the angle specified by _`decimalAngle`_ .

Signature

```
   public static Decimal tan(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### tan(doubleAngle)

Returns the trigonometric tangent of the angle specified by _`doubleAngle`_ .

Signature

```
   public static Double tan(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double


### Apex Reference Guide Messaging Class

Return Value

Type: Double

##### tanh(decimalAngle)

Returns the hyperbolic tangent of _`decimalAngle`_ . The hyperbolic tangent of _`decimalAngle`_ is defined to be ( _e_ [x]    - _e_ [-x] )/( _e_ [x] + _e_ [-x] )
##### where e is Euler's number. In other words, it is equivalent to sinh(x)/cosinh(x) . The absolute value of the exact tanh is always

less than 1.

Signature

```
   public static Decimal tanh(Decimal decimalAngle)

```

Parameters

```
   decimalAngle
```

Type: Decimal

Return Value

Type: Decimal

##### tanh(doubleAngle)

Returns the hyperbolic tangent of _`doubleAngle`_ . The hyperbolic tangent of _`doubleAngle`_ is defined to be ( _e_ [x]    - _e_ [-x] )/( _e_ [x] + _e_ [-x] )
##### where e is Euler's number. In other words, it is equivalent to sinh(x)/cosinh(x) . The absolute value of the exact tanh is always

less than 1.

Signature

```
   public static Double tanh(Double doubleAngle)

```

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

### Messaging Class

Contains messaging methods used when sending a single or mass email.

Namespace

System


Apex Reference Guide Messaging Class

Usage

Important: Sending email by using Apex requires domain-level and user-level email verification. System-generated emails also
[require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements to](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

#### Messaging Methods The following are methods for Messaging . All are instance methods.

IN THIS SECTION:

extractInboundEmail(source, includeForwardedAttachments)
Use this method in your email service code to control how to parse and process forwarded or attached emails. Returns an instance
of `Messaging.InboundEmail` from a stream of data that is in RFC822 format. The data stream can be a forwarded email in
an attachment to an existing InboundEmail, or a stream from another source.

reserveMassEmailCapacity(amountReserved)
Reserves email capacity to send mass email to the specified number of email addresses, after the current transaction commits.

reserveSingleEmailCapacity(amountReserved)
Reserves email capacity to send single email to the specified number of email addresses, after the current transaction commits.

sendEmail(emails, allOrNothing)
Sends the list of emails instantiated with either `SingleEmailMessage` or `MassEmailMessage` and returns a list of
SendEmailResult objects. When org preferences are set to save EmailMessage objects and a trigger is defined for EmailMessage
objects, the trigger is fired for each `SingleEmailMessage` individually. The `sendEmail` method can be called 10 times per
Apex transaction and each method invocation can include up to 100 "To", 25 "Cc", and 25 "Bcc" recipients.

sendEmailMessage(emailMessageIds, allOrNothing)
Sends draft email messages as defined by the specified email message IDs and returns a list of SendEmailResult objects.

renderEmailTemplate(whoId, whatId, bodies)
Replaces merge fields in text bodies of email templates with values from Salesforce records. Returns an array of
`RenderEmailTemplateBodyResult` objects, each of which corresponds to an element in the supplied array of text bodies.
Each `RenderEmailTemplateBodyResult` provides a success or failure indication, along with either an error code or the
rendered text.

renderStoredEmailTemplate(templateId, whoId, whatId)
Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Includes all attachment content in the returned email message.

renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption)
Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Provides options for including attachment metadata only, attachment metadata and
content, or excluding attachments.

renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption, updateEmailTemplateUsage)
Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Provides options for including attachment metadata only, attachment metadata and
content, or excluding attachments.


Apex Reference Guide Messaging Class

##### extractInboundEmail(source, includeForwardedAttachments)

Use this method in your email service code to control how to parse and process forwarded or attached emails. Returns an instance of
`Messaging.InboundEmail` from a stream of data that is in RFC822 format. The data stream can be a forwarded email in an
attachment to an existing InboundEmail, or a stream from another source.

Signature

```
   public static Messaging.InboundEmail extractInboundEmail(Object source, Boolean

   includeForwardedAttachments)

```

Parameters

```
   source
```

Type: Object

An instance of `Messaging.InboundEmail.BinaryAttachment` whose MimeTypeSubtype is `message/rfc822`
or a Blob. If _`source`_ is a Blob, then supply a byte array in RFC822 format.

```
   includeForwardedAttachments
```

Type: Boolean

This parameter controls how attachments to embedded or forwarded emails are handled. Set to `true` to provide all attachments,
even attachments in embedded emails in the `binaryAttachments` and `textAttachments` properties of the returned
value. Set to `false` to provide only the attachments that are at the top level of the source email.

Return Value

Type: Messaging.InboundEmail

##### reserveMassEmailCapacity(amountReserved)

Reserves email capacity to send mass email to the specified number of email addresses, after the current transaction commits.

Signature

```
   public Void reserveMassEmailCapacity(Integer amountReserved)

```

Parameters

```
   amountReserved
```

Type: Integer

Return Value

Type: Void

Usage

This method can be called when you know in advance how many addresses emails will be sent to as a result of the transaction. If the
transaction would cause the organization to exceed its daily email limit, using this method results in the following error:
`System.HandledException: The daily limit for the org would be exceeded by this request.` If


Apex Reference Guide Messaging Class

the organization doesn’t have permission to send API or mass email, using this method results in the following error:

```
   System.NoAccessException: The organization is not permitted to send email.

##### reserveSingleEmailCapacity(amountReserved)

```

Reserves email capacity to send single email to the specified number of email addresses, after the current transaction commits.

Signature

```
   public Void reserveSingleEmailCapacity(Integer amountReserved)

```

Parameters

```
   amountReserved
```

Type: Integer

Return Value

Type: Void

Usage

This method can be called when you know in advance how many addresses emails will be sent to as a result of the transaction. If the
transaction would cause the organization to exceed its daily email limit, using this method results in the following error:
`System.HandledException: The daily limit for the org would be exceeded by this request.` If
the organization doesn’t have permission to send API or mass email, using this method results in the following error:

```
   System.NoAccessException: The organization is not permitted to send email.

##### sendEmail(emails, allOrNothing)

```

Sends the list of emails instantiated with either `SingleEmailMessage` or `MassEmailMessage` and returns a list of
SendEmailResult objects. When org preferences are set to save EmailMessage objects and a trigger is defined for EmailMessage objects,
##### the trigger is fired for each SingleEmailMessage individually. The sendEmail method can be called 10 times per Apex

transaction and each method invocation can include up to 100 "To", 25 "Cc", and 25 "Bcc" recipients.

Signature

```
   public Messaging.SendEmailResult[] sendEmail(Messaging.Email[] emails, Boolean

   allOrNothing)

```

Parameters

```
   emails
```

Type: Messaging.Email[]

```
   allOrNothing
```

Type: Boolean

##### The optional opt_allOrNone parameter specifies whether sendEmail prevents delivery of all other messages when any of

the messages fail due to an error ( `true` ), or whether it allows delivery of the messages that don't have errors ( `false` ). The default
is `true` .


Apex Reference Guide Messaging Class

Return Value

Type: Messaging.SendEmailResult[]

##### **`sendEmailMessage(emailMessageIds, allOrNothing)`**

Sends draft email messages as defined by the specified email message IDs and returns a list of SendEmailResult objects.

Signature

```
   public Messaging.SendEmailResult[] sendEmailMessage(List<ID> emailMessageIds, Boolean

   allOrNothing)

```

Parameters

```
   emailMessageIds
```

Type: List<ID>

```
   allOrNothing
```

Type: Boolean

Return Value

Type: Messaging.SendEmailResult[]

If the _`emailMessageIds`_ parameter is null, the method throws a `System.IllegalArgumentException` exception.

Usage

##### The sendEmailMessage method assumes that the optional allOrNothing parameter is always false and ignores the

value you set. Delivery of all messages is attempted even if some messages fail due to an error.

##### The email address of the user calling the sendEmailMessage method is inserted in the From Address field of the email header and

the Email Message record.

Example

This example shows how to send a draft email message. It creates a case and a new email message associated with the case. Next, the
example sends a draft email message and checks the results. Before running this example, make sure to replace the email address with
a valid address.

```
   Case c = new Case();

   insert c;

   EmailMessage e = new EmailMessage();

   e.parentid = c.id;

   // Set to draft status.

   // This status is required

   // for sendEmailMessage().

   e.Status = '5';

   e.TextBody =

     'Sample email message.';

   e.Subject = 'Apex sample';

   e.ToAddress = 'customer@email.com';

```


Apex Reference Guide Messaging Class

```
   insert e;

   List<Messaging.SendEmailResult>

     results =

     Messaging.sendEmailMessage(new ID[]

      { e.id });

   System.assertEquals(1, results.size());

   System.assertEquals(true,

               results[0].success);

```

Versioned Behavior Changes

In API version 54.0 and later, a null _`emailMessageIds`_ parameter results in a `System.IllegalArgumentException`
exception. In API version 53.0 and earlier, a null _`emailMessageIds`_ parameter results in an error.

##### renderEmailTemplate(whoId, whatId, bodies)

Replaces merge fields in text bodies of email templates with values from Salesforce records. Returns an array of
`RenderEmailTemplateBodyResult` objects, each of which corresponds to an element in the supplied array of text bodies.
Each `RenderEmailTemplateBodyResult` provides a success or failure indication, along with either an error code or the
rendered text.

Signature

```
   public static List<Messaging.RenderEmailTemplateBodyResult> renderEmailTemplate(String

   whoId, String whatId, List<String> bodies)

```

Parameters

```
   whoId
```

Type: String

The identifier of an object in the database, typically a contact, lead, or user. The database record for that object is read and used in
merge field processing.

```
   whatId
```

Type: String

Identifies an object in the database like an account or opportunity. The record for that object is read and used in merge field processing.

```
   bodies
```

Type: List<String>

An array of strings that are examined for merge field references. The corresponding data from the object referenced by the `whoId`
or `whatId` replaces the merge field reference.

Return Value

Type: List<Messaging.RenderEmailTemplateBodyResult>


Apex Reference Guide Messaging Class

Usage

Use this method in situations in which you want to dynamically compose blocks of text that are enriched with data from the database.
You can then use the the rendered blocks of text to compose and send an email or update a text value in another database record.

Executing the `renderEmailTemplate` method counts toward the SOQL governor limit. The number of SOQL queries that this
method consumes is the number of elements in the list of strings passed in the _`bodies`_ parameter.

SEE ALSO:

[Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)

##### renderStoredEmailTemplate(templateId, whoId, whatId)

Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Includes all attachment content in the returned email message.

Signature

```
   public static Messaging.SingleEmailMessage renderStoredEmailTemplate(String templateId,

   String whoId, String whatId)

```

Parameters

```
   templateId
```

Type: String

An email template that exists in the database, such as text, HTML, custom, and Visualforce templates.

```
   whoId
```

Type: String

The identifier of an object in the database, typically a contact, lead, or user. The database record for that object is read and used in
merge field processing.

```
   whatId
```

Type: String

Identifies an object in the database, like an account or opportunity. The record for that object is read and used in merge field
processing.

Return Value

Type: Messaging.SingleEmailMessage

Usage

##### Executing the renderStoredEmailTemplate method counts toward the SOQL governor limit as one query.

SEE ALSO:

[Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)


Apex Reference Guide Messaging Class

##### renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption)

Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Provides options for including attachment metadata only, attachment metadata and
content, or excluding attachments.

Signature

```
   public static Messaging.SingleEmailMessage renderStoredEmailTemplate(String templateId,

   String whoId, String whatId, Messaging.AttachmentRetrievalOption

   attachmentRetrievalOption)

```

Parameters

```
   templateId
```

Type: String

An email template that exists in the database, such as text, HTML, custom, and Visualforce templates.

```
   whoId
```

Type: String

The identifier of an object in the database, typically a contact, lead, or user. The database record for that object is read and used in
merge field processing.

```
   whatId
```

Type: String

Identifies an object in the database, like an account or opportunity. The record for that object is read and used in merge field
processing.

```
   attachmentRetrievalOption
```

Type: Messaging.AttachmentRetrievalOption

Specifies options for including attachments in the `fileAttachments` property of the returned
`Messaging.SingleEmailMessage` . Set to one of the Messaging.AttachmentRetrievalOption values to include attachment
metadata only, attachment metadata and content, or to exclude attachments.

Note: When the _`attachmentRetrievalOption`_ parameter is _not_ set to `NONE`, the `entityAttachments`
property of `Messaging.SingleEmailMessage` contains the ID of the Salesforce content objects to attach
(ContentVersion or Document). The `fileAttachments` property contains the IDs of attachments, in addition to all the
IDs in the `entityAttachments` property. As a result, the ID values in `entityAttachments` are duplicates of the
IDs in the `fileAttachments` property. If you call `renderStoredEmailTemplate()` by passing the
`METADATA_WITH_BODY` option, and send the rendered email message, the email will contain duplicate attachments.
Before using the returned email message with sendEmail(emails, allOrNothing), you can remove attachments from
`fileAttachments` that are duplicated in `entityAttachments` .

Return Value

Type: Messaging.SingleEmailMessage

Usage

##### Executing the renderStoredEmailTemplate method counts toward the SOQL governor limit as one query.


Apex Reference Guide Messaging Class

##### renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption,

updateEmailTemplateUsage)

Renders a text, custom, HTML, or Visualforce email template that exists in the database into an instance of
`Messaging.SingleEmailMessage` . Provides options for including attachment metadata only, attachment metadata and
content, or excluding attachments.

Signature

```
   public static Messaging.SingleEmailMessage renderStoredEmailTemplate(String templateId,

   String whoId, String whatId, Messaging.AttachmentRetrievalOption

   attachmentRetrievalOption, Boolean updateEmailTemplateUsage)

```

Parameters

```
   templateId
```

Type: String

An email template that exists in the database, such as text, HTML, custom, and Visualforce templates.

```
   whoId
```

Type: String

The identifier of an object in the database, typically a contact, lead, or user. The database record for that object is read and used in
merge field processing.

```
   whatId
```

Type: String

Identifies an object in the database, like an account or opportunity. The record for that object is read and used in merge field
processing.

```
   attachmentRetrievalOption
```

Type: Messaging.AttachmentRetrievalOption

Specifies options for including attachments in the `fileAttachments` property of the returned
`Messaging.SingleEmailMessage` . Set to one of the Messaging.AttachmentRetrievalOption values to include attachment
metadata only, attachment metadata and content, or to exclude attachments.

Note: When the _`attachmentRetrievalOption`_ parameter is _not_ set to `NONE`, the `entityAttachments`
property of `Messaging.SingleEmailMessage` contains the ID of the Salesforce content objects to attach
(ContentVersion or Document). The `fileAttachments` property contains the IDs of attachments, in addition to all the
IDs in the `entityAttachments` property. As a result, the ID values in `entityAttachments` are duplicates of the
IDs in the `fileAttachments` property. If you call `renderStoredEmailTemplate()` by passing the
`METADATA_WITH_BODY` option, and send the rendered email message, the email will contain duplicate attachments.
Before using the returned email message with sendEmail(emails, allOrNothing), you can remove attachments from
`fileAttachments` that are duplicated in `entityAttachments` .

```
   updateEmailTemplateUsage
```

Type: Boolean

Specifies whether the usage field in the EmailTemplate record is updated upon successful rendering.

Return Value

Type: Messaging.SingleEmailMessage


### Apex Reference Guide MultiStaticResourceCalloutMock Class

Usage

Executing the `renderStoredEmailTemplate` method counts toward the SOQL governor limit as one query.

### MultiStaticResourceCalloutMock Class

Utility class used to specify a fake response using multiple resources for testing HTTP callouts.

Namespace

System

Usage

Use the methods in this class to set the response properties for testing HTTP callouts. You can specify a resource for each endpoint.

IN THIS SECTION:

#### MultiStaticResourceCalloutMock Constructors MultiStaticResourceCalloutMock Methods MultiStaticResourceCalloutMock Constructors

### The following are constructors for MultiStaticResourceCalloutMock .

IN THIS SECTION:

##### MultiStaticResourceCalloutMock()

Creates a new instance of the `System.MultiStaticResourceCalloutMock` class.

##### MultiStaticResourceCalloutMock()

Creates a new instance of the `System.MultiStaticResourceCalloutMock` class.

Signature

```
   public MultiStaticResourceCalloutMock()

#### MultiStaticResourceCalloutMock Methods

### The following are methods for MultiStaticResourceCalloutMock . All are instance methods.

```

IN THIS SECTION:

setHeader(headerName, headerValue)
Sets the specified header name and value for the fake response.

setStaticResource(endpoint, resourceName)
Sets the specified static resource corresponding to the endpoint. The static resource contains the response body.


Apex Reference Guide MultiStaticResourceCalloutMock Class

##### setStatus(httpStatus)

Sets the specified HTTP status for the response.

setStatusCode(httpStatusCode)
Sets the specified HTTP status code for the response.

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

##### setStaticResource(endpoint, resourceName)

Sets the specified static resource corresponding to the endpoint. The static resource contains the response body.

Signature

```
   public Void setStaticResource(String endpoint, String resourceName)

```

Parameters

```
   endpoint
```

Type: String

```
   resourceName
```

Type: String

Return Value

Type: Void

##### setStatus(httpStatus)

Sets the specified HTTP status for the response.


### Apex Reference Guide Network Class

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

Sets the specified HTTP status code for the response.

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

### Network Class

Manage Experience Cloud sites.

Namespace

System

IN THIS SECTION:

#### Network Constructors

Create an instance of the `System.Network` class.

Network Methods
Get the default landing page, login page, and self-registration page of a site. Asynchronously create site users and records. Get the
login and logout URLs for a site. Get a user’s current site. Map dashboards and Insights reports.

#### Network Constructors

Create an instance of the `System.Network` class.


Apex Reference Guide Network Class

##### The following are constructors for Network .

IN THIS SECTION:

##### Network()

Creates a new instance of the `System.Network` class.

##### Network()

Creates a new instance of the `System.Network` class.

Signature

```
   public Network()

#### Network Methods

```

Get the default landing page, login page, and self-registration page of a site. Asynchronously create site users and records. Get the login
and logout URLs for a site. Get a user’s current site. Map dashboards and Insights reports.

##### The following are methods for Network . All methods are static.

IN THIS SECTION:

communitiesLanding()
Returns a Page Reference to the default landing page for the Experience Cloud site. This is the first tab of the site.

createExternalUserAsync(user, contact, account)
Asynchronously creates an Experience Cloud site user for the given account or contact and associates it with the site. This method
processes requests in batches and then sends an email with login information to the user.

createRecordAsync(processType, mbObject)
Asynchronously creates case, lead, and custom object records. This method collects record creation requests and processes them
in batches.

forwardToAuthPage(startURL)
Returns a Page Reference to the default login page. StartURL is included as a query paremeter for where to redirect after a successful
login.

getLoginUrl(networkId)
Returns the absolute URL of the login page used by the Experience Cloud site.

getLogoutUrl(networkId)
Returns the absolute URL of the logout page used by the Experience Cloud site.

getNetworkId()
Returns the user’s current Experience Cloud site.

getSelfRegUrl(networkId)
Returns the absolute URL of the self-registration page used by the Experience Cloud site.

loadAllPackageDefaultNetworkDashboardSettings()
Maps the dashboards from the Salesforce Communities Management package onto each Experience Cloud site’s unconfigured
dashboard settings. Returns the number of settings it configures.


Apex Reference Guide Network Class

loadAllPackageDefaultNetworkPulseSettings()
Maps the Insights reports from the Salesforce Communities Management package onto each Experience Cloud site’s unconfigured
Insights settings. Returns the number of settings it configures.

##### communitiesLanding()

Returns a Page Reference to the default landing page for the Experience Cloud site. This is the first tab of the site.

Signature

```
   public static String communitiesLanding()

```

Return Value

Type: PageReference

Usage

If digital experiences isn’t enabled for the user’s org or the user is currently in the internal org, returns `null` .

##### **`createExternalUserAsync(user, contact, account)`**

Asynchronously creates an Experience Cloud site user for the given account or contact and associates it with the site. This method
processes requests in batches and then sends an email with login information to the user.

Signature

```
   public static String createExternalUserAsync(SObject user, SObject contact, SObject

   account)

```

Parameters

```
   user
```

Type: SObject (optional)

Information required to create a user.

```
   contact
```

Type: SObject (optional)

The contact you want to associate the user with.

```
   account
```

Type: SObject

The account you want to associate the user with.

Return Value

Type: String

Returns the UUID for the site user.


Apex Reference Guide Network Class

##### **`createRecordAsync(processType, mbObject)`**

Asynchronously creates case, lead, and custom object records. This method collects record creation requests and processes them in
batches.

Signature

```
   public static String createRecordAsync(String processType, SObject mbObject)

```

Parameters

```
   processType
```

Type: String

The process you use to create records.

```
   mbObject
```

Type: SObject

The records created for objects. Objects must be supported by the high-volume record creation.

Return Value

Type: String

Returns the UUID for the record created.

##### forwardToAuthPage(startURL)

Returns a Page Reference to the default login page. StartURL is included as a query paremeter for where to redirect after a successful
login.

Signature

```
   public static PageReference forwardToAuthPage(String startURL)

```

Parameters

```
   startURL
```

Type: String

Return Value

Type: PageReference

Usage

If digital experiences isn’t enabled for the user’s org or the user is currently in the internal org, returns `null` .

##### getLoginUrl(networkId)

Returns the absolute URL of the login page used by the Experience Cloud site.


Apex Reference Guide Network Class

Signature

```
   public static String getLoginUrl(String networkId)

```

Parameters

```
   networkId
```

Type: String

The ID of the Experience Cloud site you’re retrieving this information for.

Return Value

Type: String

Usage

Returns the full URL for the Lightning Platform or Experience Builder page used as the login page in the Experience Cloud site.

##### getLogoutUrl(networkId)

Returns the absolute URL of the logout page used by the Experience Cloud site.

Signature

```
   public static String getLogoutUrl(String networkId)

```

Parameters

```
   networkId
```

Type: String

The ID of the Experience Cloud site you’re retrieving this information for.

Return Value

Type: String

Usage

Returns the full URL for the Lightning Platform page, Experience Builder page, or Web page used as the logout page in the Experience
Cloud site.

##### getNetworkId()

Returns the user’s current Experience Cloud site.

Signature

```
   public static String getNetworkId()

```


Apex Reference Guide Network Class

Return Value

Type: String

Usage

If digital experiences isn’t enabled for the user’s org or the user is currently in the internal org, returns `null` .

##### getSelfRegUrl(networkId)

Returns the absolute URL of the self-registration page used by the Experience Cloud site.

Signature

```
   public static String getSelfRegUrl(String networkId)

```

Parameters

```
   networkId
```

Type: String

The ID of the Experience Cloud site you’re retrieving this information for.

Return Value

Type: String

Usage

Returns the full URL for the Lightning Platform or Experience Builder page used as the self-registration page in the Experience Cloud
site.

##### loadAllPackageDefaultNetworkDashboardSettings()

Maps the dashboards from the Salesforce Communities Management package onto each Experience Cloud site’s unconfigured dashboard
settings. Returns the number of settings it configures.

Signature

```
   public static Integer loadAllPackageDefaultNetworkDashboardSettings()

```

Return Value

Type: Integer

Usage

If digital experiences is enabled, and the Salesforce Communities Management package is installed, maps the dashboards provided in
the package onto each Experience Cloud site’s unconfigured dashboard settings. Returns the number of settings it configures. This
method is invoked automatically during site creation and package installation, but isn’t typically invoked manually.

If digital experiences isn’t enabled for the user’s org or the user is in the internal org, returns `0` .


### Apex Reference Guide Object Class

##### loadAllPackageDefaultNetworkPulseSettings()

Maps the Insights reports from the Salesforce Communities Management package onto each Experience Cloud site’s unconfigured
Insights settings. Returns the number of settings it configures.

Signature

```
   public static Integer loadAllPackageDefaultNetworkPulseSettings()

```

Return Value

Type: Integer

Usage

If digital experiences is enabled, and the Salesforce Communities Management package is installed, maps the Insights reports provided
in the package onto each Experience Cloud site’s unconfigured Insights settings. Returns the number of settings it configures. This
method is invoked automatically during site creation and package installation, but isn’t typically invoked manually.

If digital experiences isn’t enabled for the user’s org or the user is in the internal org, returns `0` .

### Object Class

Contains methods that are implemented by all Apex types.

Namespace

System

Usage

All Apex classes have the Object class as the base class, and therefore implement all the Object class methods.

IN THIS SECTION:

#### Object Methods Object Methods

### The following are methods for Object .

IN THIS SECTION:

equals(obj)
Compares an object to the specified object and returns true if both are equal. Otherwise, returns false.

hashCode()
Returns a hash code for the object.

toString()
Returns a string that represents the object. The string includes the class name of which the object is an instance, the at (@) character,
and the unsigned hexadecimal representation of the object’s hash code value.


Apex Reference Guide Object Class

##### **`equals(obj)`**

Compares an object to the specified object and returns true if both are equal. Otherwise, returns false.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

The object with which to compare.

Return Value

Type: Boolean

Usage

##### If x, y, and z are non-null instances of a class, the equals method must be:

**•** Reflexive: `x.equals(x)`

**•** Symmetric: `x.equals(y)` returns `true` if and only if `y.equals(x)` returns `true`

**•** Transitive: If `x.equals(y)` returns `true` and `y.equals(z)` returns `true`, then `x.equals(z)` returns `true`

**•** Consistent: Multiple invocations of `x.equals(y)` consistently return `true` or consistently return `false`, provided the objects
used in comparison are not modified.

**•** For any non-null reference value x, `x.equals(null)` returns `false`

##### Use the equals method in your class to simplify comparision of objects. You can use the == operator to compare objects, or the equals method. For example:

```
   // obj1 and obj2 are instances of MyClass

   if (obj1 == obj2) {

      // Do something

   }

   if (obj1.equals(obj2)) {

      // Do something

   }

##### **`hashCode()`**

```

Returns a hash code for the object.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer


### Apex Reference Guide OrgLimit Class

Usage

**•** If the `hashCode` method is invoked on the same object more than once during execution of an Apex request, it must return the
same value.

**–** The hash code value is same provided no information used in equals comparisons on the object is modified.

**–** The hash code value need not remain consistent from one Apex execution request to another execution of the same application.

**•** If two objects are equal, based on the `equals` method, `hashCode` must return the same value.

**•** If two objects are unequal, based on the result of the `equals` method, it is not required that `hashCode` return distinct values.

##### **`toString()`**

Returns a string that represents the object. The string includes the class name of which the object is an instance, the at (@) character,
and the unsigned hexadecimal representation of the object’s hash code value.

Signature

```
   public String toString()

```

Return Value

Type: String

Versioned Behavior Changes

##### In API version 57.0 and later, the toString() method only includes member variables of Apex objects that are visible in the current namespace. Non-global properties are suppressed from output when you invoke toString() on managed Apex types. To keep the non-global state of the object visible in debug output, you can explicitly override the toString() method.

### OrgLimit Class

Contains methods that provide the name, maximum value, and current value of an org limit.

Namespace

System

Usage

Use the `System.OrgLimits getAll` and `getMap` methods to obtain either a list or a map of all your org limits. To get details
on each limit, use instance methods from `System.OrgLimit` .

For comparison, the Limits Class returns Apex governor limits and not Salesforce API limits.

Note: Limit values are updated asynchronously, in near-real-time.

IN THIS SECTION:

OrgLimit Methods


Apex Reference Guide OrgLimit Class

#### OrgLimit Methods The following are methods for OrgLimit .

IN THIS SECTION:

##### getLimit()

Returns the maximum allowed limit value.

##### getName()

Returns the limit’s name.

getValue()
Returns the limit usage value.

toString()
Returns the string representation of the org limit.

##### getLimit()

Returns the maximum allowed limit value.

Signature

```
   public Integer getLimit()

```

Return Value

Type: Integer

Example

```
   List<System.OrgLimit> limits = OrgLimits.getAll();

   for (System.OrgLimit aLimit: limits) {

      System.debug('Limit: ' + aLimit.getName());

      System.debug('Max Limit is: ' + aLimit.getLimit());

   }

##### getName()

```

Returns the limit’s name.

Signature

```
   public String getName()

```

Return Value

Type: String


### Apex Reference Guide OrgLimits Class

Example

```
   List<System.OrgLimit> limits = OrgLimits.getAll();

   for (System.OrgLimit aLimit: limits) {

      System.debug('Limit: ' + aLimit.getName());

      System.debug('Max Limit is: ' + aLimit.getLimit());

   }

##### getValue()

```

Returns the limit usage value.

Signature

```
   public Integer getValue()

```

Return Value

Type: Integer

Example

```
   List<System.OrgLimit> limits = OrgLimits.getAll();

   for (System.OrgLimit aLimit: limits) {

      System.debug('Limit: ' + aLimit.getName());

      System.debug('Usage Value is: ' + aLimit.getValue());

   }

##### **`toString()`**

```

Returns the string representation of the org limit.

Signature

```
   public String toString()

```

Return Value

Type: String

String denoting the name, current consumption, and maximum value of the org limit. For example:

```
   OrgLimit[DailyBulkApiBatches: consumed 25 of 15000]

### OrgLimits Class

```

Contains methods that provide a list or map of all OrgLimit instances for Salesforce your org, such as SOAP API requests, Bulk API requests,
and Streaming API limits.


Apex Reference Guide OrgLimits Class

Namespace

System

Usage

##### Use the System.OrgLimits getAll and getMap methods to obtain either a list or a map of all your org limits. To get details

on each limit, use instance methods from `System.OrgLimit` .

For comparison, the Limits Class returns Apex governor limits and not Salesforce API limits.

Note: Limit values are updated asynchronously, in near-real-time.

IN THIS SECTION:

#### OrgLimits Methods

SEE ALSO:

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_limits.htm)_ : Limits

#### OrgLimits Methods The following are methods for OrgLimits .

IN THIS SECTION:

##### getAll()

Returns a list of OrgLimit instances.

##### getMap()

Returns a map of all OrgLimit instances with the limit name as key.

##### getAll()

Returns a list of OrgLimit instances.

Signature

```
   public static List<System.OrgLimit> getAll()

```

Return Value

Type: List<System.OrgLimit>

##### getMap()

Returns a map of all OrgLimit instances with the limit name as key.

Signature

```
   public static Map<String,System.OrgLimit> getMap()

```


### Apex Reference Guide PageReference Class

Return Value

Type: Map<String,System.OrgLimit>

Example

```
   Map<String,System.OrgLimit> limitsMap = OrgLimits.getMap();

   System.OrgLimit apiRequestsLimit = limitsMap.get('DailyApiRequests');

   System.debug('Limit Name: ' + apiRequestsLimit.getName());

   System.debug('Usage Value: ' + apiRequestsLimit.getValue());

   System.debug('Maximum Limit: ' + apiRequestsLimit.getLimit());

### PageReference Class

```

A PageReference is a reference to an instantiation of a page. Among other attributes, PageReferences consist of a URL and a set of query
parameter names and values.

Namespace

System

Use a PageReference object:

**•** To view or set query string parameters and values for a page

**•** To send the user to a different page as the result of an action method

Instantiation

In a custom controller or controller extension, you can refer to or instantiate a PageReference in one of these ways.


Apex Reference Guide PageReference Class

**•** `Page.` _**`existingPageName`**_

Refers to a PageReference for a Visualforce page that has already been saved in your organization. By referring to a page in this way,
the platform recognizes that this controller or controller extension is dependent on the existence of the specified page and will
prevent the page from being deleted while the controller or extension exists.

**•** `PageReference pageRef = new PageReference('` _**`partialURL`**_ `');`

Creates a PageReference to any page that is hosted on the Lightning platform. For example, setting _`'partialURL'`_ to

`'/apex/HelloWorld'` refers to the Visualforce page located at
`http://` _`mySalesforceInstance`_ `/apex/HelloWorld` . Likewise, setting `'` _**`partialURL`**_ `'` to `'/' + '` _**`recordID`**_ `'`
refers to the detail page for the specified record.

This syntax is less preferable for referencing other Visualforce pages than `Page.` _**`existingPageName`**_ because the PageReference
is constructed at runtime, rather than referenced at compile time. Runtime references are not available to the referential integrity
system. Consequently, the platform doesn't recognize that this controller or controller extension is dependent on the existence of
the specified page and won't issue an error message to prevent user deletion of the page.

**•** `PageReference pageRef = new PageReference('` _**`fullURL`**_ `');`

Creates a PageReference for an external URL. For example:

```
     PageReference pageRef = new PageReference('http://www.google.com');

```

You can also instantiate a PageReference object for the current page with the `currentPage` ApexPages method. For example:

```
   PageReference pageRef = ApexPages.currentPage();

```

Request Headers

Here’s a non-exhaustive list of headers that are set on requests.

**Header** **Description**

Host

The host name requested in the request URL. This header is always set on Lightning Platform Site
requests and My Domain requests. This header is optional on other requests when HTTP/1.0 is
used instead of HTTP/1.1.

Referer The URL that is either included or linked to the current request's URL. This header is optional.

User-Agent

CipherSuite

The name, version, and extension support of the program that initiated this request, such as a web
browser. This header is optional and can be overridden in most browsers to be a different value.
Therefore, this header can’t be relied upon.

If this header exists and has a non-blank value, this means that the request is using HTTPS. Otherwise,
the request is using HTTP. The contents of a non-blank value are not defined by this API, and can
be changed without notice.

X-Salesforce-SIP The source IP address of the request. This header is always set on HTTP and HTTPS requests that
are initiated outside of Salesforce's data centers.

Note: If a request passes through a content delivery network (CDN) or proxy server, the
source IP address might be altered, and no longer the original client IP address.


Apex Reference Guide PageReference Class

**Header** **Description**

X-Salesforce-Forwarded-To The fully qualified domain name of the Salesforce instance that is handling this request. This header
is always set on HTTP and HTTPS requests that are initiated outside of Salesforce's data centers.

Example: Retrieving Query String Parameters

This example shows how to use a PageReference object to retrieve a query string parameter in the current page URL. In this example,
the `getAccount` method references the `id` query string parameter.

```
   public with sharing class MyController {

     public Account getAccount() {

        return [SELECT Id, Name FROM Account WITH USER_MODE

             WHERE Id = :ApexPages.currentPage().getParameters().get('Id')];

      }

   }

```

This page markup calls the `getAccount` method from that controller.

```
   <apex:page controller="MyController">

      <apex:pageBlock title="Retrieving Query String Parameters">

        You are viewing the {!account.name} account.

      </apex:pageBlock>

   </apex:page>

```

Note: For this example to render properly, you must associate the Visualforce page with a valid account record in the URL. For
example, if `001D000000IRt53` is the account ID, the resulting URL should be:

```
      https:// Visualforce_Url /apex/MyFirstPage?id=001D000000IRt53

```

Replace _`Visualforce_URL`_ with the Visualforce URL for your org. For production, this URL is in the format
_**`MyDomainName`**_ `--` _**`PackageName`**_ `.vf.force.com`, and if your installed package is unmanaged, the package name is `c` .
[For more information on the format of the URLs that Salesforce serves for your org, see My Domain Login and Application URL](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)
[Formats and Partitioned Domains in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

The `getAccount` method uses an embedded SOQL query to return the account specified by the `id` parameter in the URL of the
page. To access `id`, the `getAccount` method uses the `ApexPages` namespace.

**•** First the `currentPage` method returns the `PageReference` instance for the current page. `PageReference` returns a
reference to a Visualforce page, including its query string parameters.

**•** Using the page reference, use the `getParameters` method to return a map of the specified query string parameter names and
values.

**•** Then a call to the `get` method specifying `id` returns the value of the `id` parameter itself.

Example: Navigating to a New Page as the Result of an Action Method

Any action method in a custom controller or controller extension can return a PageReference object as the result of the method. If the
`redirect` attribute on the PageReference is set to `true`, the user navigates to the URL specified by the PageReference.


Apex Reference Guide PageReference Class

This example shows how this can be implemented with a `save` method. In this example, the PageReference returned by the `save`
method redirects the user to the detail page for the account record that was just saved.

```
   public class mySecondController {

      Account account;

      public Account getAccount() {

        if(account == null) account = new Account();

        return account;

      }

      public PageReference save() {

        // Add the account to the database.

        insert account;

        // Send the user to the detail page for the new account.

        PageReference acctPage = new ApexPages.StandardController(account).view();

        acctPage.setRedirect(true);

        return acctPage;

      }

   }

```

This page markup calls the `save` method from that controller. When a user clicks **Save**, he or she is redirected to the detail page for
the account just created:

```
   <apex:page controller="mySecondController" tabStyle="Account">

      <apex:sectionHeader title="New Account Edit Page" />

      <apex:form>

        <apex:pageBlock title="Create a New Account">

           <apex:pageBlockButtons location="bottom">

             <apex:commandButton action="{!save}" value="Save"/>

           </apex:pageBlockButtons>

           <apex:pageBlockSection title="Account Information">

             <apex:inputField id="accountName" value="{!account.name}"/>

             <apex:inputField id="accountSite" value="{!account.site}"/>

           </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

Example: Redirect Users to a Replacement Experience Cloud Site

This example shows how to redirect a user attempting to access a retired feedback site to a self-service help site. If the `redirect`
attribute is set to `true` on the PageReference for the feedback site, the user navigates to the URL specified by the PageReference. The
`redirectCode` attribute defines the redirection type for search engine optimization in public Experience Cloud sites.

```
   public class RedirectController {

      // Redirect users to the self-service help site public PageReference redirect() {

        final PageReference target = new

        PageReference(Site.getBaseSecureUrl() + '/SiteLogin');

        target.setRedirect(true);

        // This is a permanent redirection

        target.setRedirectCode(301);

        return target;

```


Apex Reference Guide PageReference Class

```
      }

   }

```

This example shows how to call the RedirectController class from the retired site page.

```
   <apex:page controller="RedirectController" action="{!redirect}"/>

```

Note: To redirect a page that’s served by a third-party CDN, configure that CDN to pass the origin IP address via the
`true-client-ip` [HTTP header on the page. For more information, see Prerequisites for a Custom Domain That Uses a](https://help.salesforce.com/s/articleView?id=platform.domain_mgmt_enable_https.htm&language=en_US)
[Third-Party Service or CDN in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.domain_mgmt_enable_https.htm&language=en_US)

IN THIS SECTION:

#### PageReference Constructors

PageReference Methods

#### PageReference Constructors The following are constructors for PageReference .

IN THIS SECTION:

##### PageReference(partialURL)
#### Creates a new instance of the PageReference class using the specified URL.

##### PageReference(record)
#### Generate a new instance of the PageReference class for the specified sObject record.

##### PageReference(partialURL)

#### Creates a new instance of the PageReference class using the specified URL.

Signature

```
   public PageReference(String partialURL)

```

Parameters

```
   partialURL
```

Type: String

The partial URL of a page hosted on the Lightning Platform or a full external URL. The following are some examples of the
_`partialURL`_ parameter values:

**•** `/apex/HelloWorld` : refers to the Visualforce page located at
`http://` _`MyDomainName`_ `-` _`PackageName`_ `.vf.force.com/apex/HelloWorld` .

**•** `/` _`recordID`_ : refers to the detail page of a specified record.

**•** `http://www.google.com` : refers to an external URL.

##### PageReference(record)

#### Generate a new instance of the PageReference class for the specified sObject record.


Apex Reference Guide PageReference Class

Signature

```
   public PageReference(SObject record)

```

Parameters

```
   record
```

Type: SObject

The sObject record that references the `ApexPage` . The reference must be an `ApexPage` .

SEE ALSO:

_[Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_compref_page.htm)_ : apex:page

_[SOAP API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_objects_apexpage.htm)_ : ApexPage

#### PageReference Methods The following are methods for PageReference . All are instance methods.

IN THIS SECTION:

forResource(resourceName, path)
Create a PageReference for nested content inside a zip static resource, by name and path.

forResource(resourceName)
Create a PageReference for a static resource, by name.

getAnchor()
Returns the name of the anchor referenced in the page’s URL. That is, the part of the URL after the hashtag (#).

getContent()
Returns the output of the page, as displayed to a user in a web browser.

getContentAsPDF()
Returns the page in PDF, regardless of the `<apex:page>` component’s `renderAs` attribute.

getCookies()
Returns a map of cookie names and cookie objects, where the key is a String of the cookie name and the the value contains the
cookie object with that name.

getHeaders()
Returns a map of the request headers, where the key string contains the name of the header, and the value string contains the value
of the header.

getParameters()
Returns a map of the query string parameters for the PageReference; both POST and GET parameters are included. The key string
contains the name of the parameter, while the value string contains the value of the parameter.

getRedirect()
Returns the current value of the PageReference object's `redirect` attribute.

getRedirectCode()
Returns the HTTP redirect code used when getRedirect() is set to `true` for the PageReference object.


Apex Reference Guide PageReference Class

getUrl()
Returns the relative URL associated with the PageReference when it was originally defined, including any query string parameters
and anchors.

setAnchor(anchor)
Sets the URL’s anchor reference to the specified string.

setCookies(cookies)
Creates a list of cookie objects. Used in conjunction with the `Cookie` class.

setRedirect(redirect)
Sets the value of the PageReference object's `redirect` attribute. If set to `true`, a redirect is performed through a client side
redirect.

setRedirectCode(redirectCode)
Sets the HTTP redirect code to use for the PageReference object when setRedirect(redirect) is set to `true` .

##### forResource(resourceName, path)

Create a PageReference for nested content inside a zip static resource, by name and path.

Signature

```
   public static System.PageReference forResource(String resourceName, String path)

```

Parameters

```
   resourceName
```

Type: String

The resource name

```
   path
```

Type: String

The resource path

Return Value

Type: System.PageReference

##### forResource(resourceName)

Create a PageReference for a static resource, by name.

Signature

```
   public static System.PageReference forResource(String resourceName)

```

Parameters

```
   resourceName
```

Type: String

The resource name


Apex Reference Guide PageReference Class

Return Value

Type: System.PageReference

##### getAnchor()

Returns the name of the anchor referenced in the page’s URL. That is, the part of the URL after the hashtag (#).

Signature

```
   public String getAnchor()

```

Return Value

Type: String

Note: Instances of `PageReference` returned by `ApexPages.currentPage()` have a null anchor attribute, because
URL fragments are not sent to the Salesforce server during a request.

##### getContent()

Returns the output of the page, as displayed to a user in a web browser.

Signature

```
   public Blob getContent()

```

Return Value

Type: Blob

Usage

The content of the returned Blob depends on how the page is rendered. If the page is rendered as a PDF file, it returns the PDF document.
If the page isn’t rendered as PDF, it returns HTML. To access the content of the returned HTML as a string, use the `toString` Blob
method. If the Visualforce page has an error, an `ExecutionException` is thrown.

##### You can’t use the getContent method in:

**•** Triggers

##### • Test methods. If you use getContent in a test method, the test method fails. getContent is treated as a callout in API version

34.0 and later.

**•** Apex email services

You also can’t use the method to retrieve the output of a different Visualforce page with the same controller and controller extensions.
Instead, pass the base URL of the destination page.

```
   new PageReference(Site.getBaseUrl() + '/apex/ VisualforcePageName ').getContent();

##### getContentAsPDF()

```

Returns the page in PDF, regardless of the `<apex:page>` component’s `renderAs` attribute.


Apex Reference Guide PageReference Class

Signature

```
   public Blob getContentAsPDF()

```

Return Value

Type: Blob

Usage

This method can’t be used in:

**•** Triggers

**•** Test methods. If you use `getContentAsPDF` in a test method, the test method fails. `getContentAsPDF` is treated as a
callout in API version 34.0 and later.

**•** Apex email services

You also can’t use the method to retrieve the output of a different Visualforce page with the same controller and controller extensions.
Instead, pass the base URL of the destination page.

```
   new PageReference(Site.getBaseUrl() + '/apex/ VisualforcePageName ').getContentAsPDF();

##### getCookies()

```

Returns a map of cookie names and cookie objects, where the key is a String of the cookie name and the the value contains the cookie
object with that name.

Signature

```
   public Map<String, System.Cookie> getCookies()

```

Return Value

Type: Map<String, System.Cookie>

Usage

Used in conjunction with the `Cookie` class. Only returns cookies with the “ `apex__` ” prefix set by the `setCookies` method.

##### getHeaders()

Returns a map of the request headers, where the key string contains the name of the header, and the value string contains the value of
the header.

Signature

```
   public Map<String, String> getHeaders()

```

Return Value

Type: Map<String, String>


Apex Reference Guide PageReference Class

Usage

This map can be modified and remains in scope for the PageReference object. For instance, you could do:

```
   PageReference.getHeaders().put('Date', '9/9/99');

```

For a description of request headers, see Request Headers.

##### getParameters()

Returns a map of the query string parameters for the PageReference; both POST and GET parameters are included. The key string contains
the name of the parameter, while the value string contains the value of the parameter.

Signature

```
   public Map<String, String> getParameters()

```

Return Value

Type: Map<String, String>

Usage

This map can be modified and remains in scope for the PageReference object. For instance, you could do:

```
   PageReference.getParameters().put('id', myID);

```

Parameter keys are case-insensitive. For example:

```
   System.assert(

      ApexPages.currentPage().getParameters().get('myParamName') ==

      ApexPages.currentPage().getParameters().get('myparamname'));

##### getRedirect()

```

Returns the current value of the PageReference object's `redirect` attribute.

Signature

```
   public Boolean getRedirect()

```

Return Value

Type: Boolean

Usage

Note that if the URL of the PageReference object is set to a website outside of the `salesforce.com` domain, the redirect always
occurs, regardless of whether the `redirect` attribute is set to `true` or `false` .

##### getRedirectCode()

Returns the HTTP redirect code used when getRedirect() is set to `true` for the PageReference object.


Apex Reference Guide PageReference Class

Signature

```
   public Integer getRedirectCode()

```

Return Value

Type: Integer

Possible Values:

**•** 0 — Redirect using the default redirect action for this PageReference. Typically a JavaScript-based redirection or HTTP 302.

Note: [Site URLRewriter Interface implementations pointing to a PageReference with a](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_site_urlRewriter.htm) _`redirectCode`_ of 0 are not
redirected.

**•** 301 — Moved Permanently. Redirect users by sending an HTTP GET request to the target location. Includes instructions to update
any references to the requested URL with the target location.

**•** 302 — Moved Temporarily. Redirect users by sending an HTTP GET request to the target location. Because the redirection is temporary,
it doesn’t include update instructions.

**•** 303 — See Other. Redirect users by sending an HTTP GET request to the target location. Not commonly used. Useful when the client
sends a POST request and you want the client to call the new web page using a GET request instead of a POST request.

**•** 307 — Temporary Redirect. Send the same HTTP request, regardless of the HTTP method, to the target location. Because the
redirection is temporary, it doesn’t include update instructions.

**•** 308 — Permanent Redirect. Send the same HTTP request, regardless of the HTTP method, to the target location. Includes instructions
to update any references to the requested URL with the target location.

##### getUrl()

Returns the relative URL associated with the PageReference when it was originally defined, including any query string parameters and
anchors.

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### setAnchor(anchor)

Sets the URL’s anchor reference to the specified string.

Signature

```
   public System.PageReference setAnchor(String anchor)

```

Parameters

```
   anchor
```

Type: String


Apex Reference Guide PageReference Class

Return Value

Type: System.PageReference

##### setCookies(cookies)

Creates a list of cookie objects. Used in conjunction with the `Cookie` class.

Signature

```
   public Void setCookies(Cookie[] cookies)

```

Parameters

```
   cookies
```

Type: System.Cookie[]

Return Value

Type: Void

Usage

Important:

**•** Cookie names and values set in Apex are URL encoded, that is, characters such as @ are replaced with a percent sign and their
hexadecimal representation.

##### • The setCookies method adds the prefix “ apex__ ” to the cookie names.

**•** Setting a cookie's value to `null` sends a cookie with an empty string value instead of setting an expired attribute.

**•** After you create a cookie, the properties of the cookie can't be changed.

**•** Be careful when storing sensitive information in cookies. Pages are cached regardless of a cookie value. If you use a cookie
[value to generate dynamic content, you should disable page caching. For more information, see Configure Site Caching in](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)
Salesforce Help.

##### setRedirect(redirect)

Sets the value of the PageReference object's `redirect` attribute. If set to `true`, a redirect is performed through a client side redirect.

Signature

```
   public System.PageReference setRedirect(Boolean redirect)

```

Parameters

```
   redirect
```

Type: Boolean

Return Value

Type: System.PageReference


### Apex Reference Guide Packaging Class

Usage

This type of redirect performs an HTTP GET request, and flushes the view state, which uses POST. If set to `false`, the redirect is a
server-side forward that preserves the view state if and only if the target page uses the same controller and contains the proper subset
of extensions used by the source page.

Note that if the URL of the PageReference object is set to a website outside of the `salesforce.com` domain, or to a page with a
different controller or controller extension, the redirect always occurs, regardless of whether the `redirect` attribute is set to `true`
or `false` .

##### setRedirectCode(redirectCode)

Sets the HTTP redirect code to use for the PageReference object when setRedirect(redirect) is set to `true` .

Signature

```
   public System.PageReference setRedirectCode(Integer redirectCode)

```

Parameters

```
   redirectCode
```

Type: Integer

Valid values:

**•** 0 — Redirect using the default redirect action for this PageReference. Typically a JavaScript-based redirection or HTTP 302.

Note: [Site URLRewriter Interface implementations pointing to a PageReference with a](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_site_urlRewriter.htm) _`redirectCode`_ of 0 are not
redirected.

**•** 301 — Moved Permanently. Redirect users by sending an HTTP GET request to the target location. Includes instructions to update
any references to the requested URL with the target location.

**•** 302 — Moved Temporarily. Redirect users by sending an HTTP GET request to the target location. Because the redirection is
temporary, it doesn’t include update instructions.

**•** 303 — See Other. Redirect users by sending an HTTP GET request to the target location. Not commonly used. Useful when the
client sends a POST request and you want the client to call the new web page using a GET request instead of a POST request.

**•** 307 — Temporary Redirect. Send the same HTTP request, regardless of the HTTP method, to the target location. Because the
redirection is temporary, it doesn’t include update instructions.

**•** 308 — Permanent Redirect. Send the same HTTP request, regardless of the HTTP method, to the target location. Includes
instructions to update any references to the requested URL with the target location.

