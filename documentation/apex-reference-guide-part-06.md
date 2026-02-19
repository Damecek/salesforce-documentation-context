   public static DataSource.Column textarea(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.STRING_LONG_TYPE

length 32000

decimalPlaces 0

##### **`time(name)`**

Returns a new column of data type `Time` with the specified name.

Signature

```
   public static DataSource.Column time(String name)

```


Apex Reference Guide Column Class

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

##### url(name, length)

Returns a new column of data type `URL_TYPE` with the specified name and length.

Signature

```
   public static DataSource.Column url(String name, Integer length)

```

Parameters

```
   name
```

Type: String

Name of the column.

```
   length
```

Type: Integer

Number of characters allowed in the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.URL_TYPE

length _`length`_

decimalPlaces 0


### Apex Reference Guide ColumnSelection Class

##### url(name)

Returns a new column of data type `URL_TYPE` with the specified name and the length of 1,000 characters.

Signature

```
   public static DataSource.Column url(String name)

```

Parameters

```
   name
```

Type: String

Name of the column.

Return Value

Type: DataSource.Column

The returned column has these property values.

**Property** **Value**

name _`name`_

label _`name`_

description _`name`_

isSortable true

isFilterable true

type DataSource.DataType.URL_TYPE

length 1000

decimalPlaces 0

### ColumnSelection Class

Identifies the list of columns to return during a query or search.

Namespace

DataSource Namespace

Usage

This class is associated with the `SELECT` clause for a SOQL query, or the `RETURNING` clause for a SOSL query.

IN THIS SECTION:

ColumnSelection Properties


Apex Reference Guide ColumnSelection Class

#### ColumnSelection Properties The following are properties for ColumnSelection .

IN THIS SECTION:

##### aggregation

How to aggregate the column’s data.

##### columnName

Name of the selected column.

##### tableName

Name of the column’s table.

##### aggregation

How to aggregate the column’s data.

Signature

```
   public DataSource.QueryAggregation aggregation {get; set;}

```

Property Value

Type: DataSource.QueryAggregation

##### columnName

Name of the selected column.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### tableName

Name of the column’s table.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String


### Apex Reference Guide Connection Class Connection Class

Extend this class to enable your Salesforce org to sync the external system’s schema and to handle queries, searches, and write operations
(upsert and delete) of the external data. This class extends the `DataSourceUtil` class and inherits its methods.

Namespace

DataSource

Usage

Your `DataSource.Connection` and `DataSource.Provider` classes compose a custom adapter for Salesforce Connect.

Changing the `sync` method on the `DataSource.Connection` class doesn’t automatically resync any external objects.

Example

```
   global class SampleDataSourceConnection extends DataSource.Connection {

      global SampleDataSourceConnection(DataSource.ConnectionParams connectionParams) {

      }

      override global List<DataSource.Table> sync() {

        List<DataSource.Table> tables = new List<DataSource.Table>();

        List<DataSource.Column> columns;

        columns = new List<DataSource.Column>();

        columns.add(DataSource.Column.text('Name', 255));

        columns.add(DataSource.Column.text('ExternalId', 255));

        columns.add(DataSource.Column.url('DisplayUrl'));

        tables.add(DataSource.Table.get('Sample', 'Title', columns));

        return tables;

      }

      override global DataSource.TableResult query(DataSource.QueryContext c) {

        return DataSource.TableResult.get(c, DataSource.QueryUtils.process(c, getRows()));

      }

      override global List<DataSource.TableResult> search(DataSource.SearchContext c) {

        List<DataSource.TableResult> results = new List<DataSource.TableResult>();

        for (DataSource.TableSelection tableSelection : c.tableSelections) {

           results.add(DataSource.TableResult.get(tableSelection, getRows()));

        }

        return results;

      }

      // Helper method to get record values from the external system for the Sample table.

      private List<Map<String, Object>> getRows () {

       // Get row field values for the Sample table from the external system via a callout.

        HttpResponse response = makeGetCallout();

        // Parse the JSON response and populate the rows.

        Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

```


Apex Reference Guide Connection Class

```
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

            // First, deserialize it.

            Map<String, Object> m = (Map<String, Object>)JSON.deserializeUntyped(

                 response.getBody());

            if (response.getStatusCode() == 200){

              results.add(DataSource.UpsertResult.success(

                   String.valueOf(m.get('id'))));

            }

            else {

              results.add(DataSource.UpsertResult.failure(

```


Apex Reference Guide Connection Class

```
                       String.valueOf(m.get('id')),

                'The callout resulted in an error: ' +

                response.getStatusCode()));

            }

          }

          return results;

        }

        return null;

      }

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

      // Helper methods

      // Make a GET callout

      private static HttpResponse makeGetCallout() {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

      // Populate a row based on values from the external system.

      private Map<String,Object> foundRow(Map<String,Object> foundRow) {

        Map<String,Object> row = new Map<String,Object>();

        row.put('ExternalId', string.valueOf(foundRow.get('Id')));

        row.put('DisplayUrl', string.valueOf(foundRow.get('DisplayUrl')));

        row.put('Name', string.valueOf(foundRow.get('Name')));

        return row;

      }

      // Make a POST callout

      private static HttpResponse makePostCallout(String jsonBody) {

         HttpResponse response;

         // Make callout

         // ...

```


Apex Reference Guide Connection Class

```
         return response;

      }

      // Make a PUT callout

      private static HttpResponse makePutCallout(String jsonBody, String externalID) {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

      // Make a DELETE callout

      private static HttpResponse makeDeleteCallout(String externalID) {

         HttpResponse response;

         // Make callout

         // ...

         return response;

      }

   }

```

IN THIS SECTION:

#### Connection Methods Connection Methods The following are methods for Connection .

IN THIS SECTION:

##### deleteRows(deleteContext)

Invoked when external object records are deleted via the Salesforce user interface, APIs, or Apex.

query(queryContext)
Invoked by a SOQL query of an external object. A SOQL query is generated and executed when a user visits an external object’s list
view or record detail page in Salesforce. Returns the results of the query.

search(searchContext)
Invoked by a SOSL query of an external object or when a user performs a Salesforce global search that also searches external objects.
Returns the results of the query.

sync()
Invoked when an administrator clicks **Validate and Sync** on the external data source detail page. Returns a list of tables that describe
the external system’s schema.

upsertRows(upsertContext)
Invoked when external object records are created or updated via the Salesforce user interface, APIs, or Apex.

##### deleteRows(deleteContext)

Invoked when external object records are deleted via the Salesforce user interface, APIs, or Apex.


Apex Reference Guide Connection Class

Signature

```
   public List<DataSource.DeleteResult> deleteRows(DataSource.DeleteContext deleteContext)

```

Parameters

```
   deleteContext
```

Type: DataSource.DeleteContext

Contains context information about the delete request.

Return Value

Type: List<DataSource.DeleteResult>

The results of the delete operation.

##### query(queryContext)

Invoked by a SOQL query of an external object. A SOQL query is generated and executed when a user visits an external object’s list view
or record detail page in Salesforce. Returns the results of the query.

Signature

```
   public DataSource.TableResult query(DataSource.QueryContext queryContext)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

Return Value

Type: DataSource.TableResult

##### search(searchContext)

Invoked by a SOSL query of an external object or when a user performs a Salesforce global search that also searches external objects.
Returns the results of the query.

Signature

```
   public List<DataSource.TableResult> search(DataSource.SearchContext searchContext)

```

Parameters

```
   searchContext
```

Type: DataSource.SearchContext

Represents the query to run against an external data table.


### Apex Reference Guide ConnectionParams Class

Return Value

Type: List<DataSource.TableResult>

##### sync()

Invoked when an administrator clicks **Validate and Sync** on the external data source detail page. Returns a list of tables that describe
the external system’s schema.

Signature

```
   public List<DataSource.Table> sync()

```

Return Value

Type: List<DataSource.Table>

Each returned table can be used to create an external object in Salesforce. On the Validate External Data Source page, the administrator
views the list of returned tables and selects which tables to sync. When the administrator clicks **Sync**, an external object is created for
each selected table. Each column within the selected tables also becomes a field in the external object.

##### upsertRows(upsertContext)

Invoked when external object records are created or updated via the Salesforce user interface, APIs, or Apex.

Signature

```
   public List<DataSource.UpsertResult> upsertRows(DataSource.UpsertContext upsertContext)

```

Parameters

```
   upsertContext
```

Type: DataSource.UpsertContext

Contains context information about the upsert request.

Return Value

Type: List<DataSource.UpsertResult>

The results of the upsert operation.

### ConnectionParams Class

Contains the credentials for authenticating to the external system.

Namespace

DataSource


Apex Reference Guide ConnectionParams Class

Usage

If your extension of the `[DataSource.Provider](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_Provider.htm)` class returns `[DataSource.AuthenticationCapability](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_enum_DataSource_AuthenticationCapability.htm)` values that
indicate support for authentication, the `[DataSource.Connection](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_Connection.htm)` class is instantiated with a
`[DataSource.ConnectionParams](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_class_DataSource_ConnectionParams.htm)` instance in the constructor.

The authentication credentials in the `DataSource.ConnectionParams` instance depend on the `Identity Type` field of
the external data source definition in Salesforce.

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

The values in this class can appear in debug logs and can be accessed by users who have the “Author Apex” permission. If you require
better security, we recommend that you specify named credentials instead of URLs as your Apex callout endpoints. Salesforce manages
all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to.

IN THIS SECTION:

#### ConnectionParams Properties ConnectionParams Properties The following are properties for ConnectionParams .

IN THIS SECTION:

certificateName
The name of the certificate for establishing each connection to the external system.

endpoint
The URL of the external system.

oauthToken
The OAuth token that’s issued by the external system.

password
The password for authenticating to the external system.

principalType
An instance of DataSource.IdentityType, which determines which set of credentials to use to access the external system.

protocol
The type of protocol that’s used to authenticate to the external system.

repository
Reserved for future use.

username
The username for authenticating to the external system.


Apex Reference Guide ConnectionParams Class

##### certificateName

The name of the certificate for establishing each connection to the external system.

Signature

```
   public String certificateName {get; set;}

```

Property Value

Type: String

The value comes from the external data source definition in Salesforce.

##### endpoint

The URL of the external system.

Signature

```
   public String endpoint {get; set;}

```

Property Value

Type: String

The value comes from the external data source definition in Salesforce.

##### oauthToken

The OAuth token that’s issued by the external system.

Signature

```
   public String oauthToken {get; set;}

```

Property Value

Type: String

##### password

The password for authenticating to the external system.

Signature

```
   public String password {get; set;}

```

Property Value

Type: String

The value depends on the `Identity Type` field of the external data source definition in Salesforce.


Apex Reference Guide ConnectionParams Class

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

##### principalType

An instance of DataSource.IdentityType, which determines which set of credentials to use to access the external system.

Signature

```
   public DataSource.IdentityType principalType {get; set;}

```

Property Value

Type: DataSource.IdentityType

##### protocol

The type of protocol that’s used to authenticate to the external system.

Signature

```
   public DataSource.AuthenticationProtocol protocol {get; set;}

```

Property Value

Type: DataSource.AuthenticationProtocol

##### repository

Reserved for future use.

Signature

```
   public String repository {get; set;}

```

Property Value

Type: String

Reserved for future use.

##### username

The username for authenticating to the external system.


### Apex Reference Guide DataSourceUtil Class

Signature

```
   public String username {get; set;}

```

Property Value

Type: String

The value depends on the `Identity Type` field of the external data source definition in Salesforce.

**•** If `Identity Type` is set to `Named Principal`, the credentials come from the external data source definition.

**•** If `Identity Type` is set to `Per User` :

**–** For queries and searches, the credentials are specific to the current user who invokes the query or search. The credentials come
from the user’s authentication settings for the external system.

**–** For administrative connections, such as syncing the external system’s schema, the credentials come from the external data
source definition.

### DataSourceUtil Class

Parent class for the `DataSource.Provider`, `DataSource.Connection`, `DataSource.Table`, and
`DataSource.Column` classes.

Namespace

### DataSource

IN THIS SECTION:

#### DataSourceUtil Methods DataSourceUtil Methods

### The following are methods for DataSourceUtil .

IN THIS SECTION:

##### logWarning(message)

Logs the error message in the debug log.

throwException(message)
Throws a `DataSourceException` and displays the provided message to the user.

##### logWarning(message)

Logs the error message in the debug log.

Signature

```
   public void logWarning(String message)

```


### Apex Reference Guide DataType Enum

Parameters

```
   message
```

Type: String

The error message.

Return Value

Type: void

##### throwException(message)

Throws a `DataSourceException` and displays the provided message to the user.

Signature

```
   public void throwException(String message)

```

Parameters

```
   message
```

Type: String

Error message to display to the user.

Return Value

Type: void

### DataType Enum

Specifies the data types that are supported by the Apex Connector Framework.

Usage

The `DataSource.DataType` enum is referenced by the `type` property on the `DataSource.Column` class.

Enum Values

The following are the values of the `DataSource.DataType` enum.

**Value** **Description**

`BOOLEAN_TYPE` Boolean

`CURRENCY_TYPE` Currency

`DATE_TYPE` Date

`DATETIME_TYPE` Date/Time

`EMAIL_TYPE` Email


### Apex Reference Guide DeleteContext Class

**Value** **Description**

`EXTERNAL_LOOKUP_TYPE` External lookup relationship

`INDIRECT_LOOKUP_TYPE` Indirect lookup relationship

`LOOKUP_TYPE` Lookup relationship

`NUMBER_TYPE` Number

`PERCENT_TYPE` Percent

`PHONE_TYPE` Phone

`PICKLIST_MULTISELECT_TYPE` Multi-select picklist

`PICKLIST_TYPE` Picklist

`STRING_LONG_TYPE` Long text area

`STRING_SHORT_TYPE` Text area

`TIME_TYPE` Time

`URL_TYPE` URL

### DeleteContext Class An instance of DeleteContext is passed to the deleteRows() method on your Database.Connection class. The class

provides context information about the delete request to the implementor of `deleteRows()` .

Namespace

DataSource

Usage

The Apex Connector Framework creates context for operations. Context is comprised of parameters about the operations, which other
### methods can use. An instance of the DeleteContext class packages these parameters into an object that can be used when a

`deleteRows()` operation is initiated.

IN THIS SECTION:

#### DeleteContext Properties DeleteContext Properties

### The following are properties for DeleteContext .

IN THIS SECTION:

externalIds
The external IDs of the rows representing external object records to delete.


### Apex Reference Guide DeleteResult Class

##### tableSelected

The name of the table to delete rows from.

##### externalIds

The external IDs of the rows representing external object records to delete.

Signature

```
   public List<String> externalIds {get; set;}

```

Property Value

Type: List<String>

##### tableSelected

The name of the table to delete rows from.

Signature

```
   public String tableSelected {get; set;}

```

Property Value

Type: String

### DeleteResult Class

Represents the result of a delete operation on an sObject record. The result is returned by the `DataSource.deleteRows` method
of the `DataSource.Connection` class.

Namespace

DataSource

Usage

A delete operation on external object records generates an array of objects of type `DataSource.DeleteResult` . Its methods
create result records that indicate whether the delete operation succeeded or failed.

IN THIS SECTION:

#### DeleteResult Properties

DeleteResult Methods

#### DeleteResult Properties

### The following are properties for DeleteResult .


Apex Reference Guide DeleteResult Class

IN THIS SECTION:

##### errorMessage

The error message that’s generated by a failed delete operation. Recorded with a result of type `DataSource.DeleteResult` .

##### externalId

The unique identifier of a row that represents an external object record to delete.

##### success

Indicates whether a delete operation succeeded or failed.

##### errorMessage

The error message that’s generated by a failed delete operation. Recorded with a result of type `DataSource.DeleteResult` .

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### externalId

The unique identifier of a row that represents an external object record to delete.

Signature

```
   public String externalId {get; set;}

```

Property Value

Type: String

##### success

Indicates whether a delete operation succeeded or failed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeleteResult Methods The following are methods for DeleteResult .


Apex Reference Guide DeleteResult Class

IN THIS SECTION:

##### equals(obj)

Maintains the integrity of lists of type `DeleteResult` by determining the equality of external objects in a list. This method is
##### dynamic and is based on the equals method in Java. failure(externalId, errorMessage)

Creates a delete result indicating the failure of a delete request for a given external ID.

hashCode()
Maintains the integrity of lists of type `DeleteResult` by determining the uniqueness of the external object records in a list.

success(externalId)
Creates a delete result indicating the successful completion of a delete request for a given external ID.

##### equals(obj)

Maintains the integrity of lists of type `DeleteResult` by determining the equality of external objects in a list. This method is dynamic
##### and is based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

##### For information about the equals method, see Using Custom Types in Map Keys and Sets.

Return Value

Type: Boolean

##### failure(externalId, errorMessage)

Creates a delete result indicating the failure of a delete request for a given external ID.

Signature

```
   public static DataSource.DeleteResult failure(String externalId, String errorMessage)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the sObject record to delete.

```
   errorMessage
```

Type: String

The reason the delete operation failed.


### Apex Reference Guide Filter Class

Return Value

Type: DataSource.DeleteResult

Status result of the delete operation.

##### hashCode()

Maintains the integrity of lists of type `DeleteResult` by determining the uniqueness of the external object records in a list.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### success(externalId)

Creates a delete result indicating the successful completion of a delete request for a given external ID.

Signature

```
   public static DataSource.DeleteResult success(String externalId)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the sObject record to delete.

Return Value

Type: DataSource.DeleteResult

Status result of the delete operation for the sObject with the given external ID.

### Filter Class

Represents a `WHERE` clause in a SOSL or SOQL query.

Namespace

DataSource

Usage

Compound types require child filters. Specifically, the `subfilters` property can’t be null if the `type` property is `NOT_`, `AND_`, or
`OR_` .


Apex Reference Guide Filter Class

IN THIS SECTION:

#### Filter Properties Filter Properties The following are properties for Filter .

IN THIS SECTION:

##### columnName

Name of the column that’s being evaluated in a simple comparative type of filter.

##### columnValue

Value that the filter compares records against in a simple comparative type of filter.

##### subfilters

List of subfilters for compound filter types, such as `NOT_`, `AND_`, and `OR_` .

tableName
Name of the table whose column is being evaluated in a simple comparative type of filter.

type
Type of filter operation that limits the returned data.

##### columnName

Name of the column that’s being evaluated in a simple comparative type of filter.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### columnValue

Value that the filter compares records against in a simple comparative type of filter.

Signature

```
   public Object columnValue {get; set;}

```

Property Value

Type: Object

##### subfilters

List of subfilters for compound filter types, such as `NOT_`, `AND_`, and `OR_` .


### Apex Reference Guide FilterType Enum

Signature

```
   public List<DataSource.Filter> subfilters {get; set;}

```

Property Value

Type: List<DataSource.Filter>

##### tableName

Name of the table whose column is being evaluated in a simple comparative type of filter.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

##### type

Type of filter operation that limits the returned data.

Signature

```
   public DataSource.FilterType type {get; set;}

```

Property Value

Type: DataSource.FilterType

### FilterType Enum

##### Referenced by the type property on a DataSource.Filter .

Usage

Determines how to limit the returned data.

Enum Values

The following are the values of the `DataSource.FilterType` enum.

**Value** **Description**

`AND_` This compound filter type returns all rows that match all the subfilters.

`CONTAINS` Simple comparative filter type.

`ENDS_WITH` Simple comparative filter type.


### Apex Reference Guide IdentityType Enum

**Value** **Description**

`EQUALS` Simple comparative filter type.

`GREATER_THAN` Simple comparative filter type.

`GREATER_THAN_OR_EQUAL_TO` Simple comparative filter type.

`LESS_THAN` Simple comparative filter type.

`LESS_THAN_OR_EQUAL_TO` Simple comparative filter type.

`LIKE_` Simple comparative filter type.

`NOT_` This compound filter type returns the rows that don’t match the subfilter.

`NOT_EQUALS` Simple comparative filter type.

`OR_` This compound filter type returns all rows that match any of the subfilters.

`STARTS_WITH` Simple comparative filter type.

### IdentityType Enum

Determines which set of credentials is used to authenticate to the external system.

Usage

The relevant credentials are passed to your `DataSource.Connection` class.

Enum Values

The following are the values of the `DataSource.IdentityType` enum.

**Value** **Description**

`ANONYMOUS` No credentials are used to authenticate to the external system.

```
NAMED_USER

PER_USER

### Order Class

```

The credentials in the external data source definition are used to authenticate to
the external system, regardless of which user is accessing the external data from
your organization.

For queries and searches, the credentials are specific to the current user who invokes
the query or search. The credentials come from the user’s authentication settings
for the external system.

For administrative connections, such as syncing the external system’s schema, the
credentials come from the external data source definition.

Contains details about how to sort the rows in the result set. Equivalent to an `ORDER BY` statement in a SOQL query.


Apex Reference Guide Order Class

Namespace

DataSource

Usage

Used in the `order` property on the `DataSource.TableSelection` class.

IN THIS SECTION:

#### Order Properties

Order Methods

#### Order Properties The following are properties for Order .

IN THIS SECTION:

##### columnName

Name of the column whose values are used to sort the rows in the result set.

##### direction

Direction for sorting rows based on column values.

tableName
Name of the table whose column values are used to sort the rows in the result set.

##### columnName

Name of the column whose values are used to sort the rows in the result set.

Signature

```
   public String columnName {get; set;}

```

Property Value

Type: String

##### direction

Direction for sorting rows based on column values.

Signature

```
   public DataSource.OrderDirection direction {get; set;}

```

Property Value

Type: DataSource.OrderDirection


Apex Reference Guide Order Class

##### tableName

Name of the table whose column values are used to sort the rows in the result set.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

#### Order Methods The following are methods for Order .

IN THIS SECTION:

##### get(tableName, columnName, direction)

Creates an instance of the DataSource.Order class.

##### get(tableName, columnName, direction)

Creates an instance of the DataSource.Order class.

Signature

```
   public static DataSource.Order get(String tableName, String columnName,

   DataSource.OrderDirection direction)

```

Parameters

##### _`tableName`_

Type: String

Name of the table whose column values are used to sort the rows in the result set.

```
   columnName
```

Type: String

Name of the column whose values are used to sort the rows in the result set.

```
   direction
```

Type: DataSource.OrderDirection

Direction for sorting rows based on column values.

Return Value

Type: DataSource.Order


### Apex Reference Guide OrderDirection Enum OrderDirection Enum

Specifies the direction for sorting rows based on column values.

Usage

Used by the direction property on the DataSource.Order class.

Enum Values

The following are the values of the `DataSource.OrderDirection` enum.

**Value** **Description**

`ASCENDING` Sort rows in ascending order (A–Z).

`DESCENDING` Sort rows in descending order (Z–A).

### Provider Class

Extend this base class to create a custom adapter for Salesforce Connect. The class informs Salesforce of the functional and authentication
capabilities that are supported by or required to connect to the external system. This class extends the `DataSourceUtil` class and
inherits its methods.

Namespace

DataSource

Usage

Create an Apex class that extends `DataSource.Provider` to specify the following.

**•** The types of authentication that can be used to access the external system

**•** The features that are supported for the connection to the external system

**•** The Apex class that extends `DataSource.Connection` to sync the external system’s schema and to handle the queries and
searches of the external data

The values that are returned by the `DataSource.Provider` class determine which settings are available in the external data
source definition in Salesforce. To access the external data source definition from Setup, enter _`External Data Sources`_ in the
`Quick Find` box, then select **External Data Sources** .

IN THIS SECTION:

#### Provider Methods Provider Methods

### The following are methods for Provider .


Apex Reference Guide Provider Class

IN THIS SECTION:

##### getAuthenticationCapabilities()

Returns the types of authentication that can be used to access the external system.

##### getCapabilities()

Returns the functional operations and endpoint settings that the external system supports.

##### getConnection(connectionParams)

Returns a connection that points to an instance of the external data source.

##### getAuthenticationCapabilities()

Returns the types of authentication that can be used to access the external system.

When you call this method, be sure the list of the external system’s authentication capabilities always contains the same values. The
returned authentication types should never change based on runtime conditions, user context, dynamic queries, or any other conditions.
Returning different authentication types for an external system can lead to errors that are difficult to troubleshoot.

For example, if your external system supports OAuth and Anonymous authentication, always return these types every time this method
is called. Don’t query the database, make callouts, or use conditional logic that varies the results of this method.

Signature

```
   public List<DataSource.AuthenticationCapability> getAuthenticationCapabilities()

```

Return Value

Type: List<DataSource.AuthenticationCapability>

##### getCapabilities()

Returns the functional operations and endpoint settings that the external system supports.

When you call this method, be sure the list of the external system’s capabilities always contains the same values. The returned capabilities
should never change based on runtime conditions, user context, dynamic queries, or any other conditions. Returning different capabilities
for an external system can lead to errors that are difficult to troubleshoot.

For example, if your external system supports the `ROW_QUERY` and `SEARCH` operations, always return these capabilities every time
this method is called. Don’t query the database, make callouts, or use conditional logic that varies the results of this method.

Signature

```
   public List<DataSource.Capability> getCapabilities()

```

Return Value

Type: List<DataSource.Capability>

##### getConnection(connectionParams)

Returns a connection that points to an instance of the external data source.


### Apex Reference Guide QueryAggregation Enum

Signature

```
   public DataSource.Connection getConnection(DataSource.ConnectionParams connectionParams)

```

Parameters

```
   connectionParams
```

Type: DataSource.ConnectionParams

Credentials for authenticating to the external system.

Return Value

Type: DataSource.Connection

### QueryAggregation Enum

Specifies how to aggregate a column in a query.

Usage

Used by the aggregation property on the DataSource.ColumnSelection class.

Enum Values

The following are the values of the `DataSource.QueryAggregation` enum.

**Value** **Description**

`AVG` Reserved for future use.

`COUNT` Returns the number of rows that meet the query criteria.

`MAX` Reserved for future use.

`MIN` Reserved for future use.

`NONE` No aggregation.

`SUM` Reserved for future use.

### QueryContext Class An instance of QueryContext is provided to the query method on your DataSource.Connection class. The instance

corresponds to a SOQL request.

Namespace

DataSource


Apex Reference Guide QueryContext Class

IN THIS SECTION:

#### QueryContext Properties QueryContext Methods QueryContext Properties The following are properties for QueryContext .

IN THIS SECTION:

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results.

##### tableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results.

Signature

```
   public String queryMoreToken {get; set;}

```

Property Value

Type: String

##### tableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

Signature

```
   public DataSource.TableSelection tableSelection {get; set;}

```

Property Value

Type: DataSource.TableSelection

#### QueryContext Methods The following are methods for QueryContext .

IN THIS SECTION:

get(metadata, offset, maxResults, tableSelection)
#### Creates an instance of the QueryContext class.


### Apex Reference Guide QueryUtils Class

##### get(metadata, offset, maxResults, tableSelection)

Creates an instance of the `QueryContext` class.

Signature

```
   public static DataSource.QueryContext get(List<DataSource.Table> metadata, Integer

   offset, Integer maxResults, DataSource.TableSelection tableSelection)

```

Parameters

```
   metadata
```

Type: List<DataSource.Table>

List of table metadata that describes the external system’s tables to query.

```
   offset
```

Type: Integer

Used for client-driven paging. Specifies the starting row offset into the query’s result set.

```
   maxResults
```

Type: Integer

Used for client-driven paging. Specifies the maximum number of rows to return in each batch.

```
   tableSelection
```

Type: DataSource.TableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

Return Value

Type: `DataSource.QueryContext`

### QueryUtils Class

Contains helper methods to locally filter, sort, and apply limit and offset clauses to data rows. This helper class is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

Namespace

DataSource

Usage

The `DataSource.QueryUtils` class and its helper methods can process query results locally within your Salesforce org. This class
is provided for your convenience to simplify the development of your Salesforce Connect custom adapter for initial tests. However, the
`DataSource.QueryUtils` class and its methods aren’t supported for use in production environments that use callouts to retrieve
data from external systems. Complete the filtering and sorting on the external system before sending the query results to Salesforce.
When possible, use server-driven paging or another technique to have the external system determine the appropriate data subsets
according to the limit and offset clauses in the query.


Apex Reference Guide QueryUtils Class

IN THIS SECTION:

#### QueryUtils Methods QueryUtils Methods The following are methods for QueryUtils .

IN THIS SECTION:

##### applyLimitAndOffset(queryContext, rows)

Returns a subset of data rows after locally applying limit and offset clauses from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

filter(queryContext, rows)
Returns a subset of data rows after locally ordering and applying filters from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

process(queryContext, rows)
Returns data rows after locally filtering, sorting, ordering, and applying limit and offset clauses from the query. This helper method
is provided for your convenience during early development and tests, but it isn’t supported for use in production environments.

sort(queryContext, rows)
Returns data rows after locally sorting and applying the order from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

##### applyLimitAndOffset(queryContext, rows)

Returns a subset of data rows after locally applying limit and offset clauses from the query. This helper method is provided for your
convenience during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,Object>> applyLimitAndOffset(DataSource.QueryContext

   queryContext, List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>


Apex Reference Guide QueryUtils Class

##### filter(queryContext, rows)

Returns a subset of data rows after locally ordering and applying filters from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,object>> filter(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

queryContext

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>

##### process(queryContext, rows)

Returns data rows after locally filtering, sorting, ordering, and applying limit and offset clauses from the query. This helper method is
provided for your convenience during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,object>> process(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>


### Apex Reference Guide ReadContext Class

##### sort(queryContext, rows)

Returns data rows after locally sorting and applying the order from the query. This helper method is provided for your convenience
during early development and tests, but it isn’t supported for use in production environments.

Signature

```
   public static List<Map<String,ject>> sort(DataSource.QueryContext queryContext,

   List<Map<String,object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: List<Map<String, Object>>

### ReadContext Class

Abstract base class for the `QueryContext` and `SearchContext` classes.

Namespace

DataSource

IN THIS SECTION:

#### ReadContext Properties ReadContext Properties

### The following are properties for ReadContext .

IN THIS SECTION:

maxResults
Maximum number of rows that the query can return.

metadata
Describes the external system’s tables to query.

offset
The starting row offset into the query’s result set. Used for client-driven paging.


### Apex Reference Guide SearchContext Class

##### maxResults

Maximum number of rows that the query can return.

Signature

```
   public Integer maxResults {get; set;}

```

Property Value

Type: Integer

##### metadata

Describes the external system’s tables to query.

Signature

```
   public List<DataSource.Table> metadata {get; set;}

```

Property Value

Type: List<DataSource.Table>

##### offset

The starting row offset into the query’s result set. Used for client-driven paging.

Signature

```
   public Integer offset {get; set;}

```

Property Value

Type: Integer

### SearchContext Class An instance of SearchContext is provided to the search method on your DataSource.Connection class. The instance

corresponds to a search or SOSL request.

Namespace

DataSource

IN THIS SECTION:

SearchContext Constructors

SearchContext Properties


Apex Reference Guide SearchContext Class

#### SearchContext Constructors The following are constructors for SearchContext .

IN THIS SECTION:

##### SearchContext(metadata, offset, maxResults, tableSelections, searchPhrase)
#### Creates an instance of the SearchContext class with the specified parameter values.

##### SearchContext()
#### Creates an instance of the SearchContext class.

##### SearchContext(metadata, offset, maxResults, tableSelections, searchPhrase)

#### Creates an instance of the SearchContext class with the specified parameter values.

Signature

```
   public SearchContext(List<DataSource.Table> metadata, Integer offset, Integer maxResults,

   List<DataSource.TableSelection> tableSelections, String searchPhrase)

```

Parameters

```
   metadata
```

Type: List<DataSource.Table>

List of table metadata that describes the external system’s tables to query.

```
   offset
```

Type: Integer

Specifies the starting row offset into the query’s result set.

```
   maxResults
```

Type: Integer

Specifies the maximum number of rows to return in each batch.

```
   tableSelections
```

Type: List<DataSource.TableSelection>

List of queries and their details. The details represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in each SOQL or SOSL
query.

```
   searchPhrase
```

Type: String

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

##### SearchContext()

#### Creates an instance of the SearchContext class.

Signature

```
   public SearchContext()

```


### Apex Reference Guide SearchUtils Class

#### SearchContext Properties The following are properties for SearchContext .

IN THIS SECTION:

##### searchPhrase

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

##### tableSelections

List of queries and their details. The details represent the FROM, ORDER BY, SELECT, and WHERE clauses in each SOQL or SOSL query.

##### searchPhrase

The user-entered search string as a case-sensitive single phrase, with all non-alphanumeric characters removed.

Signature

```
   public String searchPhrase {get; set;}

```

Property Value

Type: String

##### tableSelections

List of queries and their details. The details represent the FROM, ORDER BY, SELECT, and WHERE clauses in each SOQL or SOSL query.

Signature

```
   public List<DataSource.TableSelection> tableSelections {get; set;}

```

Property Value

Type: List<DataSource.TableSelection>

### SearchUtils Class

Helper class for implementing search on a custom adapter for Salesforce Connect.

Namespace

DataSource

Usage

We recommend that you develop your own search implementation that can search columns in addition to the designated name field.

IN THIS SECTION:

SearchUtils Methods


### Apex Reference Guide Table Class

#### SearchUtils Methods The following are methods for SearchUtils .

IN THIS SECTION:

##### searchByName(searchDetails, connection)

Queries all the tables and returns each row whose designated name field contains the search phrase.

##### searchByName(searchDetails, connection)

Queries all the tables and returns each row whose designated name field contains the search phrase.

Signature

```
   public static List<DataSource.TableResult> searchByName(DataSource.SearchContext

   searchDetails, DataSource.Connection connection)

```

Parameters

```
   searchDetails
```

Type: DataSource.SearchContext

The `SearchContext` class that specifies which data to search and what to search for.

```
   connection
```

Type: DataSource.Connection

The `DataSource.Connection` class that connects to the external system.

Return Value

Type: List<DataSource.TableResult>

### Table Class

Describes a table on an external system that the Salesforce Connect custom adapter connects to. This class extends the
`DataSourceUtil` class and inherits its methods.

Namespace

DataSource

Usage

A list of table metadata is provided by the `DataSource.Connection` class when the `sync()` method is invoked. Each table
can become an external object in Salesforce.

The metadata is stored in Salesforce. Updating the Apex code to return new or updated values for the table metadata doesn’t automatically
update the stored metadata in Salesforce.


Apex Reference Guide Table Class

IN THIS SECTION:

#### Table Properties

Table Methods

#### Table Properties The following are properties for Table .

IN THIS SECTION:

##### columns

List of table columns.

##### description

Description of what the table represents.

labelPlural
Plural form of the user-friendly name for the table. The `labelPlural` becomes the object’s plural label in the Salesforce user
interface.

labelSingular
Singular form of the user-friendly name for the table. The `labelSingular` becomes the object label in the Salesforce user
interface. We recommend that you make object labels unique across all standard, custom, and external objects in the org.

name
Name of the table on the external system.

nameColumn
Name of the table column that becomes the name field of the external object when the administrator syncs the table.

##### columns

List of table columns.

Signature

```
   public List<DataSource.Column> columns {get; set;}

```

Property Value

Type: List<DataSource.Column>

##### description

Description of what the table represents.

Signature

```
   public String description {get; set;}

```


Apex Reference Guide Table Class

Property Value

Type: String

##### labelPlural Plural form of the user-friendly name for the table. The labelPlural becomes the object’s plural label in the Salesforce user interface.

Signature

```
   public String labelPlural {get; set;}

   DataSource.Table, labelPlural

```

Property Value

Type: String

##### labelSingular Singular form of the user-friendly name for the table. The labelSingular becomes the object label in the Salesforce user interface.

We recommend that you make object labels unique across all standard, custom, and external objects in the org.

Signature

```
   public String labelSingular {get; set;}

```

Property Value

Type: String

##### name

Name of the table on the external system.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### nameColumn

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

Signature

```
   public String nameColumn {get; set;}

```


Apex Reference Guide Table Class

Property Value

Type: String

#### Table Methods The following are methods for Table .

IN THIS SECTION:

##### get(name, labelSingular, labelPlural, description, nameColumn, columns)

Returns the table metadata with the specified parameter values.

get(name, nameColumn, columns)
Returns the table metadata with the specified parameter values, using the name for the labels and description.

##### get(name, labelSingular, labelPlural, description, nameColumn, columns)

Returns the table metadata with the specified parameter values.

Signature

```
   public static DataSource.Table get(String name, String labelSingular, String labelPlural,

   String description, String nameColumn, List<DataSource.Column> columns)

```

Parameters

```
   name
```

Type: String

Name of the external table.

```
   labelSingular
```

Type: String

Singular form of the user-friendly name for the table. The `labelSingular` becomes the object label in the Salesforce user
interface.

```
   labelPlural
```

Type: String

Plural form of the user-friendly name for the table. The `labelPlural` becomes the object’s plural label in the Salesforce user
interface.

```
   description
```

Type: String

Description of the external table.

```
   nameColumn
```

Type: String

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

```
   columns
```

Type: List<DataSource.Column>

List of table columns.


### Apex Reference Guide TableResult Class

Return Value

Type: DataSource.Table

##### get(name, nameColumn, columns)

Returns the table metadata with the specified parameter values, using the name for the labels and description.

Signature

```
   public static DataSource.Table get(String name, String nameColumn,

   List<DataSource.Column> columns)

   DataSource.Table, get, [String, String, List<DataSource.Column>], DataSource.Table

```

Parameters

```
   name
```

Type: String

Name of the external table.

```
   nameColumn
```

Type: String

Name of the table column that becomes the name field of the external object when the administrator syncs the table.

```
   columns
```

Type: List<DataSource.Column>

List of table columns.

Return Value

Type: DataSource.Table

The returned table metadata has these property values.

**Property** **Value**

name _`name`_

labelSingular _`name`_

labelPlural _`name`_

description _`name`_

nameColumn _`nameColumn`_

columns _`columns`_

### TableResult Class

Contains the results of a search or query.


Apex Reference Guide TableResult Class

Namespace

DataSource

IN THIS SECTION:

#### TableResult Properties

TableResult Methods

#### TableResult Properties The following are properties for TableResult .

IN THIS SECTION:

##### errorMessage errorMessage queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results. This token is passed back
##### to the Apex data source on subsequent queries in the queryMoreToken property on the QueryContext .

rows
Rows of data.

success
Whether the search or query was successful.

tableName
Name of the table that was queried.

totalSize
The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

##### errorMessage errorMessage

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### queryMoreToken

Query token that’s used for server-driven paging to determine and fetch the subsequent batch of results. This token is passed back to
##### the Apex data source on subsequent queries in the queryMoreToken property on the QueryContext .


Apex Reference Guide TableResult Class

Signature

```
   public String queryMoreToken {get; set;}

```

Property Value

Type: String

##### rows

Rows of data.

Signature

```
   public List<Map<String,Object>> rows {get; set;}

```

Property Value

Type: List<Map<String, Object>>

##### success

Whether the search or query was successful.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

##### tableName

Name of the table that was queried.

Signature

```
   public String tableName {get; set;}

```

Property Value

Type: String

##### totalSize

The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

Signature

```
   public Integer totalSize {get; set;}

```


Apex Reference Guide TableResult Class

Property Value

Type: Integer

#### TableResult Methods The following are methods for TableResult .

IN THIS SECTION:

##### error(errorMessage)

Returns failed search or query results with the provided error message.

get(success, errorMessage, tableName, rows, totalSize)
#### Returns a subset of data rows in a TableResult with the provided property values and the number of rows in the table.

get(success, errorMessage, tableName, rows)
#### Returns a subset of data rows in a TableResult with the provided property values.

get(queryContext, rows)
#### Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a TableResult .

get(tableSelection, rows)
#### Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a TableResult .

##### error(errorMessage)

Returns failed search or query results with the provided error message.

Signature

```
   public static DataSource.TableResult error(String errorMessage)

```

Parameters

```
   errorMessage
```

Type: String

errorMessage

Return Value

Type: DataSource.TableResult

#### The returned TableResult has these property values.

**Property** **Value**

success false

errorMessage _`errorMessage`_

tableName null

rows null


Apex Reference Guide TableResult Class

**Property** **Value**

rows.size() 0

##### get(success, errorMessage, tableName, rows, totalSize)

Returns a subset of data rows in a `TableResult` with the provided property values and the number of rows in the table.

Signature

```
   public static DataSource.TableResult get(Boolean success, String errorMessage, String

   tableName, List<Map<String,Object>> rows, Integer totalSize)

```

Parameters

```
   success
```

Type: Boolean

Whether the search or query was successful.

```
   errorMessage
```

Type: String

errorMessage

```
   tableName
```

Type: String

Name of the table that was queried.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

```
   totalSize
```

Type: Integer

The total number of rows that meet the query criteria, even when the external system is requested to return a smaller batch size.

Return Value

Type: DataSource.TableResult

##### get(success, errorMessage, tableName, rows)

Returns a subset of data rows in a `TableResult` with the provided property values.

Signature

```
   public static DataSource.TableResult get(Boolean success, String errorMessage, String

   tableName, List<Map<String,Object>> rows)

```


Apex Reference Guide TableResult Class

Parameters

```
   success
```

Type: Boolean

Whether the search or query was successful.

```
   errorMessage
```

Type: String

errorMessage

```
   tableName
```

Type: String

Name of the table that was queried.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

##### get(queryContext, rows)

Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a `TableResult` .

Signature

```
   public static DataSource.TableResult get(DataSource.QueryContext queryContext,

   List<Map<String,Object>> rows)

```

Parameters

```
   queryContext
```

Type: DataSource.QueryContext

Represents the query to run against a data table.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

##### get(tableSelection, rows)

Returns the subset of data rows that meet the query criteria, and the number of rows in the table, in a `TableResult` .


### Apex Reference Guide TableSelection Class

Signature

```
   public static DataSource.TableResult get(DataSource.TableSelection tableSelection,

   List<Map<String,Object>> rows)

```

Parameters

```
   tableSelection
```

Type: DataSource.TableSelection

Query details that represent the `FROM`, `ORDER BY`, `SELECT`, and `WHERE` clauses in a SOQL or SOSL query.

```
   rows
```

Type: List<Map<String, Object>>

Rows of data.

Return Value

Type: DataSource.TableResult

### TableSelection Class

Contains a breakdown of the SOQL or SOSL query. Its properties represent the FROM, ORDER BY, SELECT, and WHERE clauses in the
query.

Namespace

DataSource

IN THIS SECTION:

#### TableSelection Properties TableSelection Properties

### The following are properties for TableSelection .

IN THIS SECTION:

columnsSelected
List of columns to query. Corresponds to the `SELECT` clause in a SOQL or SOSL query.

filter
Identifies the query filter, which can be a compound filter that has a list of subfilters. The filter corresponds to the `WHERE` clause in
a SOQL or SOSL query.

order
Identifies the order for sorting the query results. Corresponds to the `ORDER BY` clause in a SOQL or SOSL query.

tableSelected
Name of the table to query. Corresponds to the `FROM` clause in a SOQL or SOSL query.


Apex Reference Guide TableSelection Class

##### columnsSelected

List of columns to query. Corresponds to the `SELECT` clause in a SOQL or SOSL query.

Signature

```
   public List<DataSource.ColumnSelection> columnsSelected {get; set;}

```

Property Value

Type: List<DataSource.ColumnSelection>

##### filter

Identifies the query filter, which can be a compound filter that has a list of subfilters. The filter corresponds to the `WHERE` clause in a
SOQL or SOSL query.

Signature

```
   public DataSource.Filter filter {get; set;}

```

Property Value

Type: DataSource.Filter

##### order

Identifies the order for sorting the query results. Corresponds to the `ORDER BY` clause in a SOQL or SOSL query.

Signature

```
   public List<DataSource.Order> order {get; set;}

```

Property Value

Type: List<DataSource.Order>

##### tableSelected

Name of the table to query. Corresponds to the `FROM` clause in a SOQL or SOSL query.

Signature

```
   public String tableSelected {get; set;}

```

Property Value

Type: String


### Apex Reference Guide UpsertContext Class UpsertContext Class An instance of UpsertContext is passed to the upsertRows() method on your Datasource.Connection class. This

class provides context information about the upsert request to the implementor of `upsertRows()` .

Namespace

DataSource

Usage

The Apex Connector Framework creates the contet for operations. Context is comprised of parameters about the operations, which
### other methods can use. An instance of the UpsertContext class packages these parameters into an object that can be used when

an `upsertRows()` operation is initiated.

IN THIS SECTION:

#### UpsertContext Properties UpsertContext Properties

### The following are properties for UpsertContext .

IN THIS SECTION:

##### rows

List of rows corresponding to the external object records to upsert.

##### tableSelected

The name of the table to upsert rows in.

##### rows

List of rows corresponding to the external object records to upsert.

Signature

```
   public List<Map<String,ANY>> rows {get; set;}

```

Property Value

Type: List<Map<String,Object>>

##### tableSelected

The name of the table to upsert rows in.

Signature

```
   public String tableSelected {get; set;}

```


### Apex Reference Guide UpsertResult Class

Property Value

Type: String

### UpsertResult Class

Represents the result of an upsert operation on an external object record. The result is returned by the `upsertRows` method of the
`DataSource.Connection` class.

Namespace

DataSource

Usage

An upsert operation on external object records generates an array of objects of type `DataSource.UpsertResult` . Its methods
create result records that indicate whether the upsert operation succeeded or failed.

IN THIS SECTION:

#### UpsertResult Properties

UpsertResult Methods

#### UpsertResult Properties

### The following are properties for UpsertResult .

IN THIS SECTION:

##### errorMessage

The error message that’s generated by a failed upsert operation.

externalId
The unique identifier of a row that represents an external object record to upsert.

success
Indicates whether a delete operation succeeded or failed.

##### errorMessage

The error message that’s generated by a failed upsert operation.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String


Apex Reference Guide UpsertResult Class

##### externalId

The unique identifier of a row that represents an external object record to upsert.

Signature

```
   public String externalId {get; set;}

```

Property Value

Type: String

##### success

Indicates whether a delete operation succeeded or failed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### UpsertResult Methods The following are methods for UpsertResult .

IN THIS SECTION:

##### equals(obj)
#### Maintains the integrity of lists of type UpsertResult by determining the equality of external object records in a list. This method
##### is dynamic and is based on the equals method in Java.

failure(externalId, errorMessage)
Creates an upsert result that indicates the failure of a delete request for a given external ID.

hashCode()
#### Maintains the integrity of lists of type UpsertResult by determining the uniqueness of the external object records in a list.

##### success(externalId)

Creates a delete result that indicates the successful completion of an upsert request for a given external ID.

##### equals(obj)

#### Maintains the integrity of lists of type UpsertResult by determining the equality of external object records in a list. This method is
##### dynamic and is based on the equals method in Java.

Signature

```
   public Boolean equals(Object obj)

```


Apex Reference Guide UpsertResult Class

Parameters

```
   obj
```

Type: Object

External object whose key is to be validated.

Return Value

Type: Boolean

##### failure(externalId, errorMessage)

Creates an upsert result that indicates the failure of a delete request for a given external ID.

Signature

```
   public static DataSource.UpsertResult failure(String externalId, String errorMessage)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the external object record to upsert.

```
   errorMessage
```

Type: String

The reason the upsert operation failed.

Return Value

Type: DataSource.UpsertResult

Status result for the upsert operation.

##### hashCode()

Maintains the integrity of lists of type `UpsertResult` by determining the uniqueness of the external object records in a list.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### success(externalId)

Creates a delete result that indicates the successful completion of an upsert request for a given external ID.


### Apex Reference Guide DataSource Exceptions

Signature

```
   public static DataSource.UpsertResult success(String externalId)

```

Parameters

```
   externalId
```

Type: String

The unique identifier of the external object record to upsert.

Return Value

Type: DataSource.UpsertResult

Status result of the upsert operation for the external object record with the given external ID.

### DataSource Exceptions The DataSource namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The DataSource namespace contains these exceptions.

**Exception** **Description** **Methods**

To get the error message and write it
to debug log, use the `String`

`getMessage()` .

To get the error message and write it
to debug log, use the `String`

`getMessage()` .

```
DataSource.DataSourceException

DataSource.OAuthTokenExpiredException

## DataWeave Namespace

```

Throw this exception to indicate that an
error occurred while communicating with
an external data source.

Throw this exception to indicate that an
OAuth token has expired. The system then
attempts to refresh the token
automatically and restart the query, search,
or sync operation.

The DataWeave namespace provides classes and methods to support the invocation of DataWeave scripts from Apex.

DataWeave is the MuleSoft expression language for accessing, parsing, and transforming data that travels through a Mule application.
[For detailed information, see DataWeave Language.](https://docs.mulesoft.com/mule-runtime/4.3/dataweave)

## These are the classes in the DataWeave namespace.

IN THIS SECTION:

Result Class
Contains methods to retrieve data that was transformed using Script class methods.


### Apex Reference Guide Result Class

Script Class
Contains the `createScript()` method to load DataWeave scripts and the `execute()` method to obtain script output in
a `DataWeave.Result` object.

SEE ALSO:

[DataWeave in Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/DataWeaveInApex.htm)

### Result Class

Contains methods to retrieve data that was transformed using Script class methods.

Namespace

DataWeave

Example

See Script Class for an example to run a DataWeave script from Apex and retrieve the resulting script output.

IN THIS SECTION:

#### Result Methods Result Methods

### The following are methods for Result .

IN THIS SECTION:

##### getValue()

Returns the result of a DataWeave script execution as an object.

getValueAsString()
Returns the result of a DataWeave script execution as a string value.

##### **`getValue()`**

Returns the result of a DataWeave script execution as an object.

Signature

```
   public Object getValue()

```

Return Value

Type: Object


### Apex Reference Guide Script Class

##### **`getValueAsString()`**

Returns the result of a DataWeave script execution as a string value.

Signature

```
   public String getValueAsString()

```

Return Value

Type: String

### Script Class

Contains the `createScript()` method to load DataWeave scripts and the `execute()` method to obtain script output in a
`DataWeave.Result` object.

Namespace

DataWeave

This example runs a DataWeave script from Apex and retrieves the resulting script output. First deploy the script to the org as
`ContactsToJson.dwl` .

```
   %dw 2.0

   input records application/java

   output application/json

   --
   {

     users: records map(record) -> {

      firstName: record.FirstName,

      lastName: record.LastName

     }

```

Then, execute the script from Apex.

```
   List<Contact> data = [SELECT FirstName, LastName FROM Contact WHERE LastName LIMIT 5];

   Map<String, Object> args = new Map<String, Object>{ 'records' => data };

   DataWeave.Script script = DataWeave.Script.createScript('ContactsToJson');

   DataWeave.Result result = script.execute(args);

   string jsonOutput = result.getValueAsString();

```

IN THIS SECTION:

#### Script Methods Script Methods

### The following are methods for Script .


Apex Reference Guide Script Class

IN THIS SECTION:

##### createScript(scriptName)

Loads a DataWeave 2.0 script from the `.dwl` metadata file that is deployed in an org. The script can then be run using the
`Script.execute` method.

##### createScript(namespace, scriptName)

Loads a DataWeave 2.0 script from a specified namespace. The script can then be run using the `Script.execute` method.

execute(parameters)
Executes the DataWeave script that is loaded using the `createScript()` method and returns the script output.

toString()
Returns the name of the script.

##### **`createScript(scriptName)`**

Loads a DataWeave 2.0 script from the `.dwl` metadata file that is deployed in an org. The script can then be run using the
`Script.execute` method.

Signature

```
   public static createScript(String scriptName)

```

Parameters

```
   scriptName
```

Type: String

The name of the deployed metadata `.dwl` script (not including the file extension).

Return Value

Type: DataWeave.Script

DataWeave script that is used as a parameter in the `Script.execute()` method.

##### **`createScript(namespace, scriptName)`**

Loads a DataWeave 2.0 script from a specified namespace. The script can then be run using the `Script.execute` method.

Signature

```
   public static dataweave.Script createScript(String namespace, String scriptName)

```

Parameters

```
   namespace
```

Type: String

The namespace name for the deployed script. If the namespace name is null, the caller namespace is used. If the namespace name
is empty, the org namespace is used.

```
   scriptName
```

Type: String


## Apex Reference Guide Dom Namespace

The name of the deployed metadata `.dwl` script (not including the file extension).

Return Value

Type: DataWeave.Script

DataWeave script that is used as a parameter in the `Script.execute()` method.

##### **`execute(parameters)`**

Executes the DataWeave script that is loaded using the `createScript()` method and returns the script output.

Signature

```
   public execute(Map<String,Object> parameters)

```

Parameters

```
   parameters
```

Type: Map<String,Object>

Input to the DataWeave script. The keys correspond to the input directive names defined in the DataWeave header.

[See Input Directive and DataWeave Header.](https://docs.mulesoft.com/dataweave/1.2/dataweave-language-introduction#input-directive)

Return Value

Type: DataWeave.Result

The `DataWeave.Result` object contains the script output.

##### **`toString()`**

Returns the name of the script.

Signature

```
   public String toString()

```

Return Value

Type: String

## Dom Namespace The Dom namespace provides classes and methods for parsing and creating XML content. The following are the classes in the Dom namespace.

IN THIS SECTION:

Document Class
Use the `Document` class to process XML content. You can parse nested XML content that’s up to 50 nodes deep.


### Apex Reference Guide Document Class

XmlNode Class
Use the `XmlNode` class to work with a node in an XML document.

XmlNodeType Enum
Specifies the node type in an XML document.

### Document Class Use the Document class to process XML content. You can parse nested XML content that’s up to 50 nodes deep.

Namespace

Dom

Usage

One common application is to use it to create the body of a request for HttpRequest or to parse a response accessed by HttpResponse.

IN THIS SECTION:

#### Document Constructors Document Methods

SEE ALSO:

[Reading and Writing XML Using the DOM](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_dom.htm)

#### Document Constructors

### The following are constructors for Document .

IN THIS SECTION:

##### Document()

Creates a new instance of the `Dom.Document` class.

##### Document()

Creates a new instance of the `Dom.Document` class.

Signature

```
   public Document()

#### Document Methods

### The following are methods for Document . All are instance methods.

```


Apex Reference Guide Document Class

IN THIS SECTION:

##### createRootElement(name, namespace, prefix)

Creates the top-level root element for a document.

##### getRootElement()

Returns the top-level root element node in the document. If this method returns `null`, the root element has not been created yet.

load(xml)
Parse the XML representation of the document specified in the _`xml`_ argument and load it into a document.

toXmlString()
Returns the XML representation of the document as a String.

##### createRootElement(name, namespace, prefix)

Creates the top-level root element for a document.

Signature

```
   public Dom.XmlNode createRootElement(String name, String namespace, String prefix)

```

Parameters

```
   name
```

Type: String

```
   namespace
```

Type: String

```
   prefix
```

Type: String

Return Value

Type: Dom.XmlNode

Usage

[For more information about namespaces, see Reading and Writing XML Using the DOM.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_dom.htm)

Calling this method more than once on a document generates an error as a document can have only one root element.

##### getRootElement()

Returns the top-level root element node in the document. If this method returns `null`, the root element has not been created yet.

Signature

```
   public Dom.XmlNode getRootElement()

```

Return Value

Type: Dom.XmlNode


### Apex Reference Guide XmlNode Class

##### load(xml)

Parse the XML representation of the document specified in the _`xml`_ argument and load it into a document.

Signature

```
   public Void load(String xml)

```

Parameters

```
   xml
```

Type: String

Return Value

Type: Void

Example

```
   Dom.Document doc = new Dom.Document();

   doc.load(xml);

##### toXmlString()

```

Returns the XML representation of the document as a String.

Signature

```
   public String toXmlString()

```

Return Value

Type: String

### XmlNode Class Use the XmlNode class to work with a node in an XML document.

Namespace

Dom

#### XmlNode Methods

### The following are methods for XmlNode . All are instance methods.

IN THIS SECTION:

addChildElement(name, namespace, prefix)
Creates a child element node for this node.


Apex Reference Guide XmlNode Class

addCommentNode(text)
Creates a child comment node for this node.

addTextNode(text)
Creates a child text node for this node.

getAttribute(key, keyNamespace)
Returns _`namespacePrefix:attributeValue`_ for the given key and key namespace.

getAttributeCount()
Returns the number of attributes for this node.

getAttributeKeyAt(index)
Returns the attribute key for the given index. Index values start at 0.

getAttributeKeyNsAt(index)
Returns the attribute key namespace for the given index.

getAttributeValue(key, keyNamespace)
Returns the attribute value for the given key and key namespace.

getAttributeValueNs(key, keyNamespace)
Returns the attribute value namespace for the given key and key namespace.

getChildElement(name, namespace)
Returns the child element node for the node with the given name and namespace.

getChildElements()
Returns the child element nodes for this node. This doesn't include child text or comment nodes.

getChildren()
Returns the child nodes for this node. This includes all node types.

getName()
Returns the element name.

getNamespace()
Returns the namespace of the element.

getNamespaceFor(prefix)
Returns the namespace of the element for the given prefix.

getNodeType()
Returns the node type.

getParent()
Returns the parent of this element.

getPrefixFor(namespace)
Returns the prefix of the given namespace.

getText()
Returns the text for this node.

insertBefore(newChild, refChild)
Inserts a new child node before the specified node.

removeAttribute(key, keyNamespace)
Removes the attribute with the given key and key namespace. Returns `true` if successful, `false` otherwise.


Apex Reference Guide XmlNode Class

removeChild(childNode)
Removes the given child node.

setAttribute(key, value)
Sets the key attribute value.

setAttributeNs(key, value, keyNamespace, valueNamespace)
Sets the key attribute value.

setNamespace(prefix, namespace)
Sets the namespace for the given prefix.

##### addChildElement(name, namespace, prefix)

Creates a child element node for this node.

Signature

```
   public Dom.XmlNode addChildElement(String name, String namespace, String prefix)

```

Parameters

```
   name
```

Type: String

The _`name`_ argument can't have a `null` value.

```
   namespace
```

Type: String

```
   prefix
```

Type: String

Return Value

Type: Dom.XmlNode

Usage

**•** If the _`namespace`_ argument has a non- `null` value and the _`prefix`_ argument is `null`, the namespace is set as the default
namespace.

**•** If the _`prefix`_ argument is `null`, Salesforce automatically assigns a prefix for the element. The format of the automatic prefix is
`ns` _**`i`**_, where _`i`_ is a number.If the _`prefix`_ argument is `''`, the namespace is set as the default namespace.

##### addCommentNode(text)

Creates a child comment node for this node.

Signature

```
   public Dom.XmlNode addCommentNode(String text)

```


Apex Reference Guide XmlNode Class

Parameters

```
   text
```

Type: String

The _`text`_ argument can't have a `null` value.

Return Value

Type: Dom.XmlNode

##### addTextNode(text)

Creates a child text node for this node.

Signature

```
   public Dom.XmlNode addTextNode(String text)

```

Parameters

```
   text
```

Type: String

The _`text`_ argument can't have a `null` value.

Return Value

Type: Dom.XmlNode

##### getAttribute(key, keyNamespace)

Returns _`namespacePrefix:attributeValue`_ for the given key and key namespace.

Signature

```
   public String getAttribute(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

Example

For example, for the `<xyz a:b="c:d" />` element:


Apex Reference Guide XmlNode Class

##### • getAttribute returns c:d

**•** `getAttributeValue` returns `d`

##### getAttributeCount()

Returns the number of attributes for this node.

Signature

```
   public Integer getAttributeCount()

```

Return Value

Type: Integer

##### getAttributeKeyAt(index)

Returns the attribute key for the given index. Index values start at 0.

Signature

```
   public String getAttributeKeyAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

##### getAttributeKeyNsAt(index)

Returns the attribute key namespace for the given index.

Signature

```
   public String getAttributeKeyNsAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String


Apex Reference Guide XmlNode Class

##### getAttributeValue(key, keyNamespace)

Returns the attribute value for the given key and key namespace.

Signature

```
   public String getAttributeValue(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

Example

For example, for the `<xyz a:b="c:d" />` element:

##### • getAttribute returns c:d • getAttributeValue returns d getAttributeValueNs(key, keyNamespace)

Returns the attribute value namespace for the given key and key namespace.

Signature

```
   public String getAttributeValueNs(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: String

##### getChildElement(name, namespace)

Returns the child element node for the node with the given name and namespace.


Apex Reference Guide XmlNode Class

Signature

```
   public Dom.XmlNode getChildElement(String name, String namespace)

```

Parameters

```
   name
```

Type: String

```
   namespace
```

Type: String

Return Value

Type: Dom.XmlNode

##### getChildElements()

Returns the child element nodes for this node. This doesn't include child text or comment nodes.

Signature

```
   public Dom.XmlNode[] getChildElements()

```

Return Value

Type: Dom.XmlNode[]

##### getChildren()

Returns the child nodes for this node. This includes all node types.

Signature

```
   public Dom.XmlNode[] getChildren()

```

Return Value

Type: Dom.XmlNode[]

##### getName()

Returns the element name.

Signature

```
   public String getName()

```

Return Value

Type: String


Apex Reference Guide XmlNode Class

##### getNamespace()

Returns the namespace of the element.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

##### getNamespaceFor(prefix)

Returns the namespace of the element for the given prefix.

Signature

```
   public String getNamespaceFor(String prefix)

```

Parameters

```
   prefix
```

Type: String

Return Value

Type: String

##### getNodeType()

Returns the node type.

Signature

```
   public Dom.XmlNodeType getNodeType()

```

Return Value

Type: Dom.XmlNodeType

Uses `XmlNodeType` enum to return _`COMMENT`_, _`ELEMENT`_, or _`TEXT`_ as the node type.

##### getParent()

Returns the parent of this element.

Signature

```
   public Dom.XmlNode getParent()

```


Apex Reference Guide XmlNode Class

Return Value

Type: Dom.XmlNode

##### getPrefixFor(namespace)

Returns the prefix of the given namespace.

Signature

```
   public String getPrefixFor(String namespace)

```

Parameters

```
   namespace
```

Type: String

The _`namespace`_ argument can't have a `null` value.

Return Value

Type: String

##### getText()

Returns the text for this node.

Signature

```
   public String getText()

```

Return Value

Type: String

##### insertBefore(newChild, refChild)

Inserts a new child node before the specified node.

Signature

```
   public Dom.XmlNode insertBefore(Dom.XmlNode newChild, Dom.XmlNode refChild)

```

Parameters

```
   newChild
```

Type: Dom.XmlNode

The node to insert.

```
   refChild
```

Type: Dom.XmlNode

The node before the new node.


Apex Reference Guide XmlNode Class

Return Value

Type: Dom.XmlNode

Usage

**•** If _`refChild`_ is `null`, _`newChild`_ is inserted at the end of the list.

**•** If _`refChild`_ doesn't exist, an exception is thrown.

##### removeAttribute(key, keyNamespace)

Removes the attribute with the given key and key namespace. Returns `true` if successful, `false` otherwise.

Signature

```
   public Boolean removeAttribute(String key, String keyNamespace)

```

Parameters

```
   key
```

Type: String

```
   keyNamespace
```

Type: String

Return Value

Type: Boolean

##### removeChild(childNode)

Removes the given child node.

Signature

```
   public Boolean removeChild(Dom.XmlNode childNode)

```

Parameters

```
   childNode
```

Type: Dom.XmlNode

Return Value

Type: Boolean

##### setAttribute(key, value)

Sets the key attribute value.


Apex Reference Guide XmlNode Class

Signature

```
   public Void setAttribute(String key, String value)

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

##### setAttributeNs(key, value, keyNamespace, valueNamespace)

Sets the key attribute value.

Signature

```
   public Void setAttributeNs(String key, String value, String keyNamespace, String

   valueNamespace)

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

```
   keyNamespace
```

Type: String

```
   valueNamespace
```

Type: String

Return Value

Type: Void

##### setNamespace(prefix, namespace)

Sets the namespace for the given prefix.

Signature

```
   public Void setNamespace(String prefix, String namespace)

```


### Apex Reference Guide XmlNodeType Enum

Parameters

```
   prefix
```

Type: String

```
   namespace
```

Type: String

Return Value

Type: Void

### XmlNodeType Enum

Specifies the node type in an XML document.

Usage

### Use XMLNodeType enum with the getNodeType() method in the XmlNode class.

Enum Values

The following are the values of the `Dom.XMLNodeType` enum.

**Value** **Description**

`COMMENT` Dom node of type comment.

`ELEMENT` Dom node of type element.

`TEXT` Dom node of type text.

## embeddedai Namespace The embeddedai namespace provides classes and methods to manage and represent records and data in Apex to support embedded

AI features.

## These are the classes in the embeddedai namespace.

IN THIS SECTION:

### ApexMap Class

Create, clone, and convert string based key-value pairs to a JSON string format.

RecordApexRepresentation Class
Contains properties and a method to create a serializable representation of a record and its associated data for AI service integration
and data processing.

### ApexMap Class

Create, clone, and convert string based key-value pairs to a JSON string format.


Apex Reference Guide ApexMap Class

Namespace

embeddedai

IN THIS SECTION:

#### ApexMap Constructors

Learn more about the constructors available with the ApexMap class.

ApexMap Properties

ApexMap Methods
Create a copy of the ApexMap object and convert key-value pairs to string format.

#### ApexMap Constructors

Learn more about the constructors available with the ApexMap class.

#### The ApexMap class includes these constructors.

IN THIS SECTION:

##### ApexMap(key, value)

Initializes a new instance of the ApexMap class by assigning the specified key and value. This constructor creates a single key–value
entry that can be included in an embedded AI Apex map for passing contextual data to embedded AI logic.

ApexMap()
Initializes the ApexMap class.

##### **`ApexMap(key, value)`**

Initializes a new instance of the ApexMap class by assigning the specified key and value. This constructor creates a single key–value
entry that can be included in an embedded AI Apex map for passing contextual data to embedded AI logic.

Signature

```
   public ApexMap(String key, String value)

```

Parameters

```
   key
```

Type: String

The unique identifier for an entry in the embedded AI Apex map. This key references and retrieves the associated value during
embedded AI processing.

```
   value
```

Type: String

The data associated with the specified key in the embedded AI Apex map. This value stores the contextual information consumed
by embedded AI logic.


Apex Reference Guide ApexMap Class

##### **`ApexMap()`**

Initializes the ApexMap class.

Signature

```
   public ApexMap()

#### ApexMap Properties

##### These are the properties for ApexMap .

```

IN THIS SECTION:

##### key

Represents key of the key-value pair. This property is used to store the unique ID or name of the data.

##### value

Represents value of the key-value pair. This property is used to store the data associated with the key.

##### **`key`**

Represents key of the key-value pair. This property is used to store the unique ID or name of the data.

Signature

```
   public String key {get; set;}

   embeddedai.ApexMap, key

```

Property Value

Type: String

##### **`value`**

Represents value of the key-value pair. This property is used to store the data associated with the key.

Signature

```
   public String value {get; set;}

   embeddedai.ApexMap, value

```

Property Value

Type: String

#### ApexMap Methods

Create a copy of the ApexMap object and convert key-value pairs to string format.


### Apex Reference Guide RecordApexRepresentation Class

These are the methods for `ApexMap` .

IN THIS SECTION:

##### toString()

Returns a string representation of the `ApexMap` object.

##### **`toString()`**

Returns a string representation of the `ApexMap` object.

Signature

```
   public String toString()

   embeddedai.ApexMap, toString, [], String

```

Return Value

Type: String

### RecordApexRepresentation Class

Contains properties and a method to create a serializable representation of a record and its associated data for AI service integration and
data processing.

Namespace

embeddedai

IN THIS SECTION:

#### RecordApexRepresentation Constructors

Learn more about the constructors available with the RecordApexRepresentation class.

RecordApexRepresentation Properties

RecordApexRepresentation Methods
Create detailed, hierarchical record objects and convert them to a custom JSON string for structured AI input.

#### RecordApexRepresentation Constructors

Learn more about the constructors available with the RecordApexRepresentation class.

### The RecordApexRepresentation class includes these constructors.

IN THIS SECTION:

RecordApexRepresentation(objectType, recordData, relatedRecordData)
Initializes a new instance of the RecordApexRepresentation class with the specified object type, primary record data, and related
record data. This constructor represents a structured record and its relationships for consumption by embedded AI logic.


Apex Reference Guide RecordApexRepresentation Class

##### RecordApexRepresentation()

Initializes the RecordApexRepresentation class.

##### **`RecordApexRepresentation(objectType, recordData, relatedRecordData)`**

Initializes a new instance of the RecordApexRepresentation class with the specified object type, primary record data, and related record
data. This constructor represents a structured record and its relationships for consumption by embedded AI logic.

Signature

```
   public RecordApexRepresentation(String objectType, List<embeddedai.ApexMap> recordData,

   List<embeddedai.RecordApexRepresentation> relatedRecordData)

```

Parameters

```
   objectType
```

Type: String

The object type represented by this record (for example, Account, Case, or a custom object). This value defines the context in which
the record data is interpreted by embedded AI processing.

```
   recordData
```

Type: List<embeddedai.ApexMap on page 2797>

The field-level data for the primary record as a collection of key–value pairs. Each ApexMap entry corresponds to a field name and
its associated value used to construct the record context.

```
   relatedRecordData
```

Type: List<embeddedai.RecordApexRepresentation on page 2800>

Related records associated with the primary record. Each entry represents a related object and its data, enabling hierarchical or
relational record context to be passed to embedded AI logic.

##### **`RecordApexRepresentation()`**

Initializes the RecordApexRepresentation class.

Signature

```
   public RecordApexRepresentation()

#### RecordApexRepresentation Properties

##### The following are properties for RecordApexRepresentation .

```

IN THIS SECTION:

objectType
Stores the type of the object.

recordData
Stores a list of objects, where each object holds a key-value pair.


Apex Reference Guide RecordApexRepresentation Class

##### relatedRecordData

Stores a list that contains a child or related records associated with the record data.

##### **`objectType`**

Stores the type of the object.

Signature

```
   public String objectType {get; set;}

   embeddedai.RecordApexRepresentation, objectType

```

Property Value

Type: String

##### **`recordData`**

Stores a list of objects, where each object holds a key-value pair.

Signature

```
   public List<embeddedai.ApexMap> recordData {get; set;}

   embeddedai.RecordApexRepresentation, recordData

```

Property Value

Type: List<embeddedai.ApexMap>

##### **`relatedRecordData`**

Stores a list that contains a child or related records associated with the record data.

Signature

```
   public List<embeddedai.RecordApexRepresentation> relatedRecordData {get; set;}

   embeddedai.RecordApexRepresentation, relatedRecordData

```

Property Value

Type: List<embeddedai.RecordApexRepresentation>

#### RecordApexRepresentation Methods

Create detailed, hierarchical record objects and convert them to a custom JSON string for structured AI input.

#### The following are methods for RecordApexRepresentation .


## Apex Reference Guide EventBus Namespace

IN THIS SECTION:

##### toRecordApexRep(jsonString)

Converts a JSON-formatted string into a RecordApexRepresentation instance. This method parses the provided JSON and constructs
a structured record representation that can be used by embedded AI logic.

##### toString()

Returns a structured JSON string representation of the `RecordApexRepresentation` object and its nested related records.

##### **`toRecordApexRep(jsonString)`**

Converts a JSON-formatted string into a RecordApexRepresentation instance. This method parses the provided JSON and constructs a
structured record representation that can be used by embedded AI logic.

Signature

```
   public static embeddedai.RecordApexRepresentation toRecordApexRep(String jsonString)

```

Parameters

```
   jsonString
```

Type: String

The JSON-formatted string containing record data and related record information to be converted into a RecordApexRepresentation
object.

Return Value

Type: embeddedai.RecordApexRepresentation

Returns a RecordApexRepresentation instance populated with the data parsed from the provided JSON string.

##### **`toString()`**

Returns a structured JSON string representation of the `RecordApexRepresentation` object and its nested related records.

Signature

```
   public String toString()

   embeddedai.RecordApexRepresentation, toString, [], String

```

Return Value

Type: String

## EventBus Namespace The EventBus namespace provides classes and methods for platform events and Change Data Capture events. The following are the classes in the EventBus namespace.


### Apex Reference Guide ChangeEventHeader Class

IN THIS SECTION:

### ChangeEventHeader Class

Contains header fields of Change Data Capture events.

EventPublishFailureCallback Interface
Implement this interface to track platform event messages that failed to publish. The `onFailure()` method in this interface is
called when the final result of the asynchronous publish operation becomes available.

EventPublishSuccessCallback Interface
Implement this interface to track platform event messages that were published successfully. The `onSuccess()` method in this
interface is called when the final result of the asynchronous publish operation becomes available.

FailureResult Interface
Contains the result of an Apex publish callback when the event publishing failed. This interface is used as a parameter in the
`onFailure` method of the `EventPublishFailureCallback` interface.

SuccessResult Interface
Contains the result of an Apex publish callback when the event publishing succeeded. This interface is used as a parameter in the
`onSuccess` method of the `EventPublishSuccessCallback` interface.

TestBroker Class
Contains methods that simulate the successful delivery or failed publishing of platform event or change event messages in an Apex
test.

TriggerContext Class
Provides information about the platform event or change event trigger that’s currently executing, such as how many times the
trigger was retried due to the `EventBus.RetryableException` . Also, provides a method to resume trigger executions.

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

### ChangeEventHeader Class

Contains header fields of Change Data Capture events.

Namespace

EventBus

IN THIS SECTION:

#### ChangeEventHeader Properties

SEE ALSO:

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_intro.htm)_

#### ChangeEventHeader Properties

### The following are properties for ChangeEventHeader .


Apex Reference Guide ChangeEventHeader Class

IN THIS SECTION:

##### changedfields

A list of the fields that were changed in an update operation, including the `LastModifiedDate` system field. This field is empty
for other operations, including record creation. This property is available in Apex saved using API version 47.0 or later.

changeorigin
Only populated for changes done by API apps or from Lightning Experience; empty otherwise. The Salesforce API and the API client
ID that initiated the change, if set by the client. Use this field to detect whether your app initiated the change to not process the
change again and potentially avoid a deep cycle of changes.

changetype
The operation that caused the change.

commitnumber
The system change number (SCN) of a committed transaction, which increases sequentially. This field is provided for diagnostic
purposes. The field value is not guaranteed to be unique in Salesforce—it is unique only in a single database instance. If your
Salesforce org migrates to another database instance, the commit number might not be unique or sequential.

committimestamp
The date and time when the change occurred, represented as the number of milliseconds since January 1, 1970 00:00:00 GMT.

commituser
The ID of the user that ran the change operation.

difffields
Contains the names of fields whose values are sent as a unified diff because they contain large text values.

entityname
The API name of the standard or custom object that the change pertains to. For example, Account or MyObject__c.

nulledfields
Contains the names of fields whose values were changed to null in an update operation. Use this field in Apex change event messages
to determine if a field was changed to null in an update and isn’t an unchanged field.

recordids
One or more record IDs for the changed records. Typically, this field contains one record ID. If in one transaction the same change
occurred in multiple records of the same object type during one second, Salesforce merges the change notifications. In this case,
Salesforce sends one change event for all affected records and the `recordIds` field contains the IDs for all records that have the
same change.

sequencenumber
The sequence of the change within a transaction. The sequence number starts from 1.

transactionkey
A string that uniquely identifies each Salesforce transaction. You can use this key to identify and group all changes that were made
in the same transaction.

##### changedfields

A list of the fields that were changed in an update operation, including the `LastModifiedDate` system field. This field is empty
for other operations, including record creation. This property is available in Apex saved using API version 47.0 or later.

Signature

```
   public List<String> changedfields {get; set;}

```


Apex Reference Guide ChangeEventHeader Class

Property Value

Type: List<String>

##### changeorigin

Only populated for changes done by API apps or from Lightning Experience; empty otherwise. The Salesforce API and the API client ID
that initiated the change, if set by the client. Use this field to detect whether your app initiated the change to not process the change
again and potentially avoid a deep cycle of changes.

Signature

```
   public String changeorigin {get; set;}

```

Property Value

Type: String

The format of the `changeOrigin` field value is:

```
   com/salesforce/api/<API_Name>/<API_Version>;client=<Client_ID>

```

**•** `<API_Name>` is the name of the Salesforce API used to make the data change. It can take one of these values: soap, rest, bulkapi,
xmlrpc, oldsoap, toolingsoap, toolingrest, apex, apexdebuggerrest.

**•** `<API_Version>` is the version of the API call that made the change and is in the format _`XX.X`_ .

**•** `<Client_ID>` is a string that contains the client ID of the app that initiated the change. If the client ID is not set in the API call,
`client=<Client_ID>` is not appended to the `changeOrigin` field.

**Example:**

```
   com/salesforce/api/soap/49.0;client=Astro

```

The client ID is set in the Call Options header of an API call. For an example on how to set the Call Options header, see:

**•** [REST API: Sforce-Call-Options Header. (Bulk API also uses the Sforce-Call-Options header. )](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/headers_calloptions.htm)

**•** [SOAP API: CallOptions Header. (Apex API also uses the CallOptions element.)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_header_calloptions.htm)

##### changetype

The operation that caused the change.

Signature

```
   public String changetype {get; set;}

```

Property Value

Type: String

Can be one of the following values:

**•** CREATE

**•** UPDATE

**•** DELETE


Apex Reference Guide ChangeEventHeader Class

**•** UNDELETE

**•** SNAPSHOT (reserved for future use)

For gap events, the change type starts with the GAP_ prefix.

**•** GAP_CREATE

**•** GAP_UPDATE

**•** GAP_DELETE

**•** GAP_UNDELETE

For overflow events, the change type is GAP_OVERFLOW.

##### commitnumber

The system change number (SCN) of a committed transaction, which increases sequentially. This field is provided for diagnostic purposes.
The field value is not guaranteed to be unique in Salesforce—it is unique only in a single database instance. If your Salesforce org migrates
to another database instance, the commit number might not be unique or sequential.

Signature

```
   public Long commitnumber {get; set;}

```

Property Value

Type: Long

##### committimestamp

The date and time when the change occurred, represented as the number of milliseconds since January 1, 1970 00:00:00 GMT.

Signature

```
   public Long committimestamp {get; set;}

```

Property Value

Type: Long

##### commituser

The ID of the user that ran the change operation.

Signature

```
   public String commituser {get; set;}

```

Property Value

Type: String


Apex Reference Guide ChangeEventHeader Class

##### difffields

Contains the names of fields whose values are sent as a unified diff because they contain large text values.

Signature

```
   public List<String> difffields {get; set;}

```

Property Value

Type: List<String>

SEE ALSO:

_Change Data Capture Developer Guide_ [: Sending Data Differences for Fields of Updated Records](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_data_diff.htm)

##### entityname

The API name of the standard or custom object that the change pertains to. For example, Account or MyObject__c.

Signature

```
   public String entityname {get; set;}

```

Property Value

Type: String

##### nulledfields

Contains the names of fields whose values were changed to null in an update operation. Use this field in Apex change event messages
to determine if a field was changed to null in an update and isn’t an unchanged field.

Signature

```
   public List<String> nulledfields {get; set;}

```

Property Value

Type: List<String>

##### recordids

One or more record IDs for the changed records. Typically, this field contains one record ID. If in one transaction the same change occurred
in multiple records of the same object type during one second, Salesforce merges the change notifications. In this case, Salesforce sends
one change event for all affected records and the `recordIds` field contains the IDs for all records that have the same change.

Signature

```
   public List<String> recordids {get; set;}

```


### Apex Reference Guide EventPublishFailureCallback Interface

Property Value

Type: List<String>

Examples of operations with same changes are:

**•** Update of fieldA to valueA in Account records.

**•** Deletion of Account records.

**•** Renaming or replacing a picklist value that results in updating the field value in all affected records.

The `recordIds` field can contain a wildcard value when a change event message is generated for custom field type conversions that
cause data loss. In this case, the `recordIds` value is the three-character prefix of the object, followed by the wildcard character `*` .
For example, for accounts, the value is `001*` .

##### sequencenumber

The sequence of the change within a transaction. The sequence number starts from 1.

Signature

```
   public Integer sequencenumber {get; set;}

```

Property Value

Type: Integer

A lead conversion is an example of a transaction that can have multiple changes. A lead conversion results in the following sequence
of changes, all within the same transaction.

**1.** Create an account

**2.** Create a contact

**3.** Create an opportunity

**4.** Update a lead

##### transactionkey

A string that uniquely identifies each Salesforce transaction. You can use this key to identify and group all changes that were made in
the same transaction.

Signature

```
   public String transactionkey {get; set;}

```

Property Value

Type: String

### EventPublishFailureCallback Interface

Implement this interface to track platform event messages that failed to publish. The `onFailure()` method in this interface is called
when the final result of the asynchronous publish operation becomes available.


Apex Reference Guide EventPublishFailureCallback Interface

Namespace

EventBus

Usage

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
_Developer Guide_ .

IN THIS SECTION:

#### EventPublishFailureCallback Methods EventPublishFailureCallback Example Implementation EventPublishFailureCallback Methods The following are methods for EventPublishFailureCallback .

IN THIS SECTION:

##### onFailure(result)

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform
event message failed.

##### **`onFailure(result)`**

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform event
message failed.

Signature

```
   public void onFailure(eventbus.FailureResult result)

```

Parameters

```
   result
```

Type: EventBus.FailureResult

The final result of `EventBus.publish` .

Return Value

Type: void

#### EventPublishFailureCallback Example Implementation

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .


### Apex Reference Guide EventPublishSuccessCallback Interface EventPublishSuccessCallback Interface

Implement this interface to track platform event messages that were published successfully. The `onSuccess()` method in this
interface is called when the final result of the asynchronous publish operation becomes available.

Namespace

EventBus

Usage

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
_Developer Guide_ .

IN THIS SECTION:

#### EventPublishSuccessCallback Methods

EventPublishSuccessCallback Example Implementation

#### EventPublishSuccessCallback Methods

### The following are methods for EventPublishSuccessCallback .

IN THIS SECTION:

##### onSuccess(result)

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform
event message succeeded.

##### **`onSuccess(result)`**

The system invokes this method when the final result of `EventBus.publish` is available and the publishing of the platform event
message succeeded.

Signature

```
   public void onSuccess(eventbus.SuccessResult result)

```

Parameters

```
   result
```

Type: EventBus.SuccessResult

The final result of `EventBus.publish` .

Return Value

Type: void


### Apex Reference Guide FailureResult Interface

#### EventPublishSuccessCallback Example Implementation

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

### FailureResult Interface

Contains the result of an Apex publish callback when the event publishing failed. This interface is used as a parameter in the `onFailure`
method of the `EventPublishFailureCallback` interface.

Namespace

EventBus

IN THIS SECTION:

#### FailureResult Methods FailureResult Methods

### The following are methods for FailureResult .

IN THIS SECTION:

##### getEventUuids()

Returns a list of `EventUuid` field values of each platform event that is included in
`EventBus.EventPublishFailureCallback` .

##### **`getEventUuids()`**

Returns a list of `EventUuid` field values of each platform event that is included in
`EventBus.EventPublishFailureCallback` .

Signature

```
   public List<String> getEventUuids()

```

Return Value

Type: List<String>

### SuccessResult Interface

Contains the result of an Apex publish callback when the event publishing succeeded. This interface is used as a parameter in the
#### onSuccess method of the EventPublishSuccessCallback interface.

Namespace

EventBus


### Apex Reference Guide TestBroker Class

IN THIS SECTION:

#### SuccessResult Methods SuccessResult Methods The following are methods for SuccessResult .

IN THIS SECTION:

##### getEventUuids()

Returns a list of `EventUuid` field values of each platform event that is included in the
`EventBus.EventPublishSuccessCallback` .

##### **`getEventUuids()`**

Returns a list of `EventUuid` field values of each platform event that is included in the
`EventBus.EventPublishSuccessCallback` .

Signature

```
   public List<String> getEventUuids()

```

Return Value

Type: List<String>

### TestBroker Class

Contains methods that simulate the successful delivery or failed publishing of platform event or change event messages in an Apex test.

Namespace

EventBus

IN THIS SECTION:

#### TestBroker Methods TestBroker Methods

### The following are methods for TestBroker .

IN THIS SECTION:

deliver()
Delivers platform event messages to the test event bus. Use this method to deliver test event messages multiple times and verify
that event subscribers have processed the test events each step of the way.


Apex Reference Guide TestBroker Class

##### fail()

Causes the publishing of platform event messages to fail in the test event bus. Use this method to test Apex publish callbacks.

##### deliver()

Delivers platform event messages to the test event bus. Use this method to deliver test event messages multiple times and verify that
event subscribers have processed the test events each step of the way.

Signature

```
   public void deliver()

```

Return Value

Type: void

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

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

##### **`fail()`**

Causes the publishing of platform event messages to fail in the test event bus. Use this method to test Apex publish callbacks.

Signature

```
   public void fail()

```

Return Value

Type: void

Usage

```
   // Create test events

   // ...

   // Publish test events with EventBus.publish()

```


### Apex Reference Guide TriggerContext Class

```
   // ...

   // Fail publishing of test events

   Test.getEventBus().fail();

   // Perform validation

   // ...

```

For more information, see <link>Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks<link/> in the
_Platform Events Developer Guide_ .

### TriggerContext Class

Provides information about the platform event or change event trigger that’s currently executing, such as how many times the trigger
was retried due to the `EventBus.RetryableException` . Also, provides a method to resume trigger executions.

Namespace

EventBus

IN THIS SECTION:

#### TriggerContext Properties

TriggerContext Methods

#### TriggerContext Properties

### The following are properties for TriggerContext .

IN THIS SECTION:

##### lastError

Read-only. The error message that the last thrown `EventBus.RetryableException` contains.

retries
Read-only. The number of times the trigger was retried due to throwing the `EventBus.RetryableException` .

##### lastError

Read-only. The error message that the last thrown `EventBus.RetryableException` contains.

Signature

```
   public String lastError {get;}

```

Property Value

Type: String


Apex Reference Guide TriggerContext Class

Usage

The error message that this property returns is the message that was passed in when creating the
`EventBus.RetryableException` exception, as follows.

```
   throw new EventBus.RetryableException(

           'Condition is not met, so retrying the trigger again.');

##### retries

```

Read-only. The number of times the trigger was retried due to throwing the `EventBus.RetryableException` .

Signature

```
   public Integer retries {get;}

```

Property Value

Type: Integer

#### TriggerContext Methods The following are methods for TriggerContext .

IN THIS SECTION:

##### currentContext()

Returns an instance of the `EventBus.TriggerContext` class containing information about the currently executing trigger.

getResumeCheckpoint()
Returns the replay ID that was set by `setResumeCheckpoint()` . The returned value is the replay ID of the event message
after which trigger processing resumes in a new trigger invocation.

setResumeCheckpoint(resumeReplayId)
Sets a checkpoint in the event stream where the platform event trigger resumes execution in a new invocation. Use this method to
recover from limit and uncaught exceptions, or to control the number of events processed in one trigger execution. When calling
this method, pass in the replay ID of the last successfully processed event message. When the trigger stops execution before all
events in `Trigger.New` are processed, either because of an uncaught exception or intentionally, the trigger is invoked again.
The new execution starts with the event message in the stream after the one with the checkpointed Replay ID.

##### currentContext()

Returns an instance of the `EventBus.TriggerContext` class containing information about the currently executing trigger.

Signature

```
   public static eventbus.TriggerContext currentContext()

```

Return Value

Type: EventBus.TriggerContext

Information about the currently executing trigger.


Apex Reference Guide TriggerContext Class

##### getResumeCheckpoint()

Returns the replay ID that was set by `setResumeCheckpoint()` . The returned value is the replay ID of the event message after
which trigger processing resumes in a new trigger invocation.

Signature

```
   public String getResumeCheckpoint()

```

Return Value

Type: String

##### setResumeCheckpoint(resumeReplayId)

Sets a checkpoint in the event stream where the platform event trigger resumes execution in a new invocation. Use this method to
recover from limit and uncaught exceptions, or to control the number of events processed in one trigger execution. When calling this
method, pass in the replay ID of the last successfully processed event message. When the trigger stops execution before all events in
`Trigger.New` are processed, either because of an uncaught exception or intentionally, the trigger is invoked again. The new execution
starts with the event message in the stream after the one with the checkpointed Replay ID.

Signature

```
   public void setResumeCheckpoint(String resumeReplayId)

```

Parameters

```
   resumeReplayId
```

Type: String

The replay ID of the last successfully processed platform event message, after which to resume processing in a new trigger execution
context.

Return Value

Type: void

Usage

The method throws an `EventBus.InvalidReplayIdException` if the supplied Replay ID is not valid—the replay ID is not
in the current trigger batch of events, in the `Trigger.new` list.

Example

This snippet shows how to call the method and pass in the replayId property of an event instance.

```
   EventBus.TriggerContext.currentContext().setResumeCheckpoint(event.replayId);

```


## Apex Reference Guide ExternalService Namespace ExternalService Namespace The ExternalService namespace provides dynamically generated Apex service interfaces and Apex classes for complex object

data types.

## The ExternalService namespace doesn't define a fixed set of classes. The namespace reflects OpenAPI-compatible external

service registrations with active operations for type-safe outbound calls. The object schema, in the API specification that is associated
with the registered external service, maps to Apex types.

SEE ALSO:

_Salesforce Help:_ [Invoke External Service Callouts Using Apex](https://help.salesforce.com/s/articleView?id=platform.external_services_apex_invoking.htm&type=5&language=en_US)

## Flow Namespace The Flow namespace provides a class for advanced access to flows from Apex such as from Visualforce controllers and asynchronous

Apex.

## The following is the class in the Flow namespace.

IN THIS SECTION:

### Interview Class

The `Flow.Interview` class provides advanced controller access to flows and the ability to start a flow.

### Interview Class

The `Flow.Interview` class provides advanced controller access to flows and the ability to start a flow.

Namespace

## Flow

Usage

[SOQL and DML limits apply during flow execution. See Per-Transaction Flow Limits in Salesforce Help.](https://help.salesforce.com/articleView?id=flow_considerations_limit_transaction.htm&language=en_US)

To create an Interview object, you have two options.

Note: We recommend only using `createInterview()` if you must reuse your method or class. Using
`createInterview()` has these drawbacks.

**•** If you package a class that uses `createInterview()`, you have to add the associated flow manually.

**•** If you delete a flow, Salesforce doesn't check if it's referenced with `createInterview()` .

**•** Create the object directly in your class by using:

**–** No namespace: `Flow.Interview.` _**`flowName`**_

**–** Namespace: `Flow.Interview.` _**`namespace`**_ `.` _**`flowName`**_

**•** Create the object dynamically by using `createInterview()`


Apex Reference Guide Interview Class

To enforce sharing rules, run the flow or Apex on API version 62.0 or later. The Apex class must be declared using the `with sharing`
keyword. The flow runs more securely in the default context when an Apex class that’s declared using the `with sharing` keyword
launches an autolaunched flow. The flow enforces the sharing rules of the user that executes the Apex class. Data access is restricted to
the sharing rules of the user that executed the Apex class. For example, a query can return fewer rows than it did in system context
without sharing. An operation can fail because the user doesn’t have the correct permissions.

Examples: Starting Flow Interviews

[These examples are all sample controllers that start an interview for the flow from the Build a Discount Calculator project on Trailhead.](https://trailhead.salesforce.com/projects/flow_calculate)
Each shows a different permutation, based on:

**•** Whether the interview is created statically, with `Flow.Interview.` _**`myFlow`**_, or dynamically, with `createInterview()` .

**•** Whether the flow is managed or local.

Interview Created Statically for a Local Flow

```
   {

     Map<String, Object> inputs = new Map<String, Object>();

     inputs.put('AccountID', myAccount);

     inputs.put('OpportunityID', myOppty);

     Flow.Interview.Calculate_discounts myFlow =

      new Flow.Interview.Calculate_discounts(inputs);

     myFlow.start();

   }

```

Interview Created Dynamically for a Local Flow

```
   public void callFlow(String flowName, Map <String, Object> inputs) {

     Flow.Interview myFlow = Flow.Interview.createInterview(flowName, inputs);

     myFlow.start();

   }

```

Interview Created Statically for a Managed Flow

```
   {

     Map<String, Object> inputs = new Map<String, Object>();

     inputs.put('AccountID', myAccount);

     inputs.put('OpportunityID', myOppty);

     Flow.Interview.myNamespace.Calculate_discounts myFlow =

      new Flow.Interview.myNamespace.Calculate_discounts(inputs);

     myFlow.start();

   }

```

Interview Created Dynamically for a Managed Flow

```
   public void callFlow(String namespace, String flowName, Map <String, Object> inputs) {

     Flow.Interview myFlow = Flow.Interview.createInterview(namespace, flowName, inputs);

     myFlow.start();

   }

```


Apex Reference Guide Interview Class

Example: Getting Variable Values

This sample uses the `getVariableValue` method to obtain breadcrumb (navigation) information from a flow. If that flow contains
subflow elements, and each of the referenced flows also contains a _`vaBreadCrumb`_ variable, you can provide users with breadcrumbs
regardless of which flow the interview is running.

```
   public class SampleController {

     //Instance of the flow

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

_Tooling API Objects_ [: FlowTestCoverage](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_flowtestcoverage.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_qs_test.htm)_ : Add a Test Class

_Salesforce Help_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

_Apex Developer Guide_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

#### Interview Methods The following are instance methods for Interview .

##### **`createInterview(namespace, flowName, inputVariables)`**

Creates an interview for a namespaced flow.

Signature

```
   public static Flow.Interview createInterview(String namespace, String flowName,

   Map<String,ANY> inputVariables)

```

Parameters

```
   namespace
```

Type: String

The flow’s namespace.

```
   flowName
```

Type: String

The flow’s API name.


Apex Reference Guide Interview Class

```
   inputVariables
```

Type: Map<String,Object>

Initial values for the flow’s input variables.

Return Value

Type: Flow.Interview

Usage

Use this method to dynamically create a Flow.Interview object for the `start()` method.

How you get output variable values from an interview depends on the type of the Apex variable where you're storing the interview.

**•** If the variable is cast to a specific flow, you can use _myFlow.myVar_ to access a variable, where _myVar_ is the name of the variable.

```
     system.debug('My Output Variable: ' + myFlow.varName);

```

**•** If the variable is of type Flow.Interview but not cast to a specific flow, you must use getVariableValue() to access the flow's variables.

```
     system.debug('My Output Variable: ' + myFlow.getVariableValue('varName'));

```

If the flow doesn't exist in the current org, a TypeException is thrown.

##### **`createInterview(flowName, inputVariables)`**

Creates an interview for a flow.

Signature

```
   public static Flow.Interview createInterview(String flowName, Map<String,Object>

   inputVariables)

```

Parameters

```
   flowName
```

Type: String

The flow’s API name.

```
   inputVariables
```

Type: Map<String,Object>

Initial values for the flow’s input variables.

Return Value

Type: Flow.Interview

Usage

Use this method to dynamically create a Flow.Interview object for the `start()` method.

How you get output variable values from an interview depends on the type of the Apex variable where you're storing the interview.


Apex Reference Guide Interview Class

**•** If the variable is cast to a specific flow, you can use _myFlow.myVar_ to access a variable, where _myVar_ is the name of the variable.

```
     system.debug('My Output Variable: ' + myFlow.varName);

```

**•** If the variable is of type Flow.Interview but not cast to a specific flow, you must use getVariableValue() to access the flow's variables.

```
     system.debug('My Output Variable: ' + myFlow.getVariableValue('varName'));

```

If the flow doesn't exist in the current org, a TypeException is thrown.

##### **`getVariableValue(variableName)`**

Returns the value of the specified flow variable. The flow variable can be in the flow embedded in the Visualforce page, or in a separate
flow that is called by a subflow element.

Signature

```
   public Object getVariableValue(String variableName)

```

Parameters

```
   variableName
```

Type: String

Specifies the unique name of the flow variable.

Return Value

Type: Object

Usage

The returned variable value comes from whichever flow the interview is running. If the specified variable can't be found in that flow, the
method returns `null` .

This method checks for the existence of the variable at run time only, not at compile time.

##### **`start()`**

Starts an instance (interview) for an autolaunched or user provisioning flow.

Signature

```
   public Void start()

```

Return Value

Type: Void

Usage

This method can be used only with flows that have one of these types.

**•** Autolaunched Flow


## Apex Reference Guide Flowtesting Namespace

**•** User Provisioning Flow

[For details, see “Flow Types” in Salesforce Help.](https://help.salesforce.com/articleView?id=flow_concepts_type.htm&language=en_US)

When a flow user invokes an autolaunched flow, the active flow version runs. If there’s no active version, the latest version runs. When
a flow admin invokes a flow, the latest version always runs.

## Flowtesting Namespace

The `flowtesting` namespace provides dynamically generated Apex classes for flow tests that are created in Flow Builder.

The `flowtesting` namespace doesn't define a fixed set of classes. The namespace reflects flows and flow tests that are created in
Flow Builder. You can run flow tests with the Salesforce CLI command _`sf flow run test`_ . For more details about the command,
use the Salesforce CLI _`–help flag`_ .

SEE ALSO:

_[Salesforce CLI Setup Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)_ Before You Begin

## flowuiruntime Namespace

The classes and methods in this namespace are reserved for internal use only or future use.

## The following are the classes in the flowuiruntime namespace.

IN THIS SECTION:

### ComplexObjectFieldDetails Class

The methods and properties in this class are for internal use only.

### PropertyTypeDetails Class

The methods and properties in this class are for internal use only.

ToastLink Class
The methods and properties in this class are reserved for future use.

### ComplexObjectFieldDetails Class

The methods and properties in this class are for internal use only.

Namespace

## flowuiruntime

### PropertyTypeDetails Class

The methods and properties in this class are for internal use only.

Namespace

## flowuiruntime


### Apex Reference Guide ToastLink Class ToastLink Class

The methods and properties in this class are reserved for future use.

Namespace

flowuiruntime

## FormulaEval Namespace

The FormulaEval namespace provides classes and methods to evaluate dynamic formulas for SObjects and Apex objects. Use the methods
to avoid unnecessary DML statements to recalculate formula field values or evaluate dynamic formula expressions.

When using a formula against an SObject or Apex object as the context object, the class methods or properties referenced by the formula
must be global.

```
   Account myAcc = new Account(Name='123');

        FormulaEval.FormulaInstance ff = Formula.builder()

          .withType(Schema.Account.class)

          .withReturnType(FormulaEval.FormulaReturnType.STRING)

          .withFormula('name & " (" & website & ")"')

          .build();

   //Use the list of field names returned by the getReferenced method to generate dynamic

   soql

        String fieldNameList = String.join(ff.getReferencedFields(),',');

        String queryStr = 'select ' + fieldNameList + ' from Account LIMIT 1'; //select

   name, website from Account

        Account s = Database.query(queryStr);

        system.debug(ff.evaluate(s));

```

[For usage notes, see Formula Evaluation in Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_formulaeval.htm)

## The following are the classes and enums in the FormulaEval namespace.

IN THIS SECTION:

### FormulaBuilder Class

Contains methods to build and validate user-defined formulas.

FormulaGlobal Enum
Specifies a global variable that references data in your organization in the `withGlobalVariables(formulaGlobals)`
method.

FormulaInstance Class
Contains a method to evaluate the formula instance.

FormulaReturnType Enum
Specifies the return type for the `withReturnType(returnType)` method.

### FormulaBuilder Class

Contains methods to build and validate user-defined formulas.


Apex Reference Guide FormulaBuilder Class

Namespace

FormulaEval

Usage

The context type that corresponds to the Apex class used in the builder `withType()` method must be a global, user-defined Apex
class. Any fields or properties that the formula references must also be global.

IN THIS SECTION:

#### FormulaBuilder Methods FormulaBuilder Methods The following are methods for FormulaBuilder .

IN THIS SECTION:

##### build()
#### Validates and returns the formula instance created using the FormulaBuilder methods.

parseAsTemplate(templateMode)
##### Optional. Indicates whether a formula expression created with the build() method is evaluated in template mode. In template

mode, values are interpolated into a string by using merge field syntax rather than by concatenating strings with the `&` operator.
Merge fields use the syntax `{!Object_Name.Field_Name}`, where names are preceded by an exclamation mark and enclosed
in curly braces.

treatNumericNullAsZero(isNumericNullZero)
##### Optional. Indicates whether a null for a numeric data type is treated as zero while evaluating the formula with the build() method.

withFormula(formulaText)
##### Required. Sets the formula expression that the build() method uses to create the formula instance.

withGlobalVariables(formulaGlobals)
##### Optional. Sets the list of global variables that can be referenced in the formula expression created with the build() method.

withReturnType(returnType)
##### Required. Sets the formula output data type for the formula instance created with the build() method.

withType(contextType)
##### Sets the Apex type that corresponds to the Apex class used with the build() method.

withType(contextType)
##### Sets the Apex type that corresponds to the Apex class used with the build() method to SObject type. **`build()`**

#### Validates and returns the formula instance created using the FormulaBuilder methods.

Signature

```
   public FormulaEval.FormulaInstance build()

```


Apex Reference Guide FormulaBuilder Class

Return Value

Type: FormulaEval.FormulaInstance

Returns an instance of the `FormulaInstance` object. If the formula validation such as field references, functions, or syntax, fails,
the method throws a `FormulaValidationException` exception.

##### **`parseAsTemplate(templateMode)`**

Optional. Indicates whether a formula expression created with the `build()` method is evaluated in template mode. In template
mode, values are interpolated into a string by using merge field syntax rather than by concatenating strings with the `&` operator. Merge
fields use the syntax `{!Object_Name.Field_Name}`, where names are preceded by an exclamation mark and enclosed in curly
braces.

Signature

```
   public formulaeval.FormulaBuilder parseAsTemplate(Boolean templateMode)

```

Parameters

```
   templateMode
```

Type: Boolean

If `true`, the formula expression is evaluated in template mode. The default value is `false` .

Return Value

Type: FormulaEval.FormulaBuilder

Usage

In template mode, the `FormulaEval.FormulaReturnType` value that’s set with `withReturnType()` must be `STRING` .

Template mode supports the same global variables, formula expressions, and context types as non-template mode, as long as they are
correctly set using the FormulaBuilder methods.

Example

In this example, `true` is passed to `parseAsTemplate()` . The formula expression is evaluated in template mode, so the values of
the `name` and `website` fields on the Account record are interpolated into the string using merge field syntax. The output is equal
to the expression `'name & " (" & website & ")"'` .

```
   FormulaEval.FormulaInstance ff = Formula.builder()

      .withType(Schema.Account.class)

      .withReturnType(FormulaEval.FormulaReturnType.STRING)

      .withFormula('{!name} ({!website})')

      .parseAsTemplate(true)

      .build();

##### **`treatNumericNullAsZero(isNumericNullZero)`**

```

Optional. Indicates whether a null for a numeric data type is treated as zero while evaluating the formula with the `build()` method.


Apex Reference Guide FormulaBuilder Class

Signature

```
   public FormulaEval.FormulaBuilder treatNumericNullAsZero(Boolean isNumericNullZero)

```

Parameters

```
   isNumericNullZero
```

Type: Boolean

If `true`, null for numeric is treated as zero. The default value is `false` .

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withFormula(formulaText)`**

Required. Sets the formula expression that the `build()` method uses to create the formula instance.

Signature

```
   public FormulaEval.FormulaBuilder withFormula(String formulaText)

```

Parameters

```
   formulaText
```

Type: String

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withGlobalVariables(formulaGlobals)`**

Optional. Sets the list of global variables that can be referenced in the formula expression created with the `build()` method.

Signature

```
   public FormulaEval.FormulaBuilder withGlobalVariables(List<formulaeval.FormulaGlobal>

   formulaGlobals)

```

Parameters

```
   formulaGlobals
```

Type: List<FormulaEval.FormulaGlobal>

Uses values from the `FormulaGlobal` enum.

Return Value

Type: FormulaEval.FormulaBuilder


Apex Reference Guide FormulaBuilder Class

##### **`withReturnType(returnType)`**

Required. Sets the formula output data type for the formula instance created with the `build()` method.

Signature

```
   public FormulaEval.FormulaBuilder withReturnType(formulaeval.FormulaReturnType

   returnType)

```

Parameters

```
   returnType
```

Type: FormulaEval.FormulaReturnType

Uses values from the `FormulaReturnType` enum.

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withType(contextType)`**

Sets the Apex type that corresponds to the Apex class used with the `build()` method.

Signature

```
   public formulaeval.FormulaBuilder withType(System.Type contextType)

```

Parameters

```
   contextType
```

Type: System.Type

An instance of the Apex class type.

Return Value

Type: FormulaEval.FormulaBuilder

##### **`withType(contextType)`**

Sets the Apex type that corresponds to the Apex class used with the `build()` method to SObject type.

Signature

```
   public formulaeval.FormulaBuilder withType(Schema.SObjectType contextSObjectType)

```

Parameters

```
   contextSObjectType
```

Type: Schema.SObjectType

An instance of the SObject type.


### Apex Reference Guide FormulaGlobal Enum

Return Value

Type: FormulaEval.FormulaBuilder

Example

This example uses an SObject type as an input in the `withType()` method to build and evaluate a formula.

```
   FormulaEval.FormulaInstance ff = Formula.builder()

      .withReturnType(FormulaEval.FormulaReturnType.Boolean)

      .withType(Account.SObjectType)

      .withFormula('ISBLANK(Site)')

      .build();

   Boolean siteIsBlank = (Boolean)ff.evaluate(new Account(Site='Test'));

   Assert.isFalse(siteIsBlank);

### FormulaGlobal Enum

```

Specifies a global variable that references data in your organization in the `withGlobalVariables(formulaGlobals)`
method.

Enum Values

The following are the values of the `FormulaEval.FormulaGlobal` enum.

**Value** **Description**

`CUSTOMMETADATA` A custom metadata record.

`LABEL` A global variable to use when referencing a custom label.

`ORGANIZATION` A global variable to use when referencing information about your company profile,
such as organization’s city, fax, ID, or other details.

`PERMISSION` A global variable to use when referencing information about the current user’s
custom permission access.

`PROFILE` A global variable to use when referencing information about the current user’s
profile, such as license type or name.

`SETUP` A global variable to use when referencing a custom setting of type `hierarchy` .

```
SYSTEM

```

A global variable that exposes _`OriginDateTime`_ and represents the literal value
of 1900-01-01 00:00:00. Use this global variable when performing date/time offset
calculations, or to assign a literal value to a date/time field.

`USER` A global variable to use when referencing information about the current user, such
as alias, title, and ID.

`USERROLE` A global variable to use when referencing information about the current user’s role,
such as role name, description, and ID.


### Apex Reference Guide FormulaInstance Class FormulaInstance Class

Contains a method to evaluate the formula instance.

Namespace

FormulaEval

Example

```
   global class MotorYacht {

     global Integer lengthInYards;

     global Integer numOfGuestCabins;

     global String name;

     global Account owner;

   }

   MotorYacht aBoat = new MotorYacht();

   aBoat.lengthInYards = 52;

   aBoat.numOfGuestCabins = 4;

   aBoat.name = 'RV Foo';

   FormulaEval.FormulaInstance isItSuper = Formula.builder()

                    .withReturnType(FormulaEval.FormulaReturnType.STRING)

                    .withType(MotorYacht.class)

                    .withFormula('IF(lengthInYards < 100, "Not Super", "Super")')

                    .build();

   isItSuper.evaluate(aBoat); //=> "Not Super"

   aBoat.owner = new Account(Name='Acme Watercraft', Site='New York');

   FormulaEval.FormulaInstance ownerDetails = Formula.builder()

                    .withReturnType(FormulaEval.FormulaReturnType.STRING)

                    .withType(MotorYacht.class)

                    .withFormula('owner.Name & " (" & owner.Site & ")"')

                    .build();

   ownerDetails.evaluate(aBoat); //=> "Acme Watercraft (New York)"

```

Usage

The context type in the `withType` method must be a global, user-defined Apex class. Any fields or properties that the formula
references must also be global.

IN THIS SECTION:

#### FormulaInstance Methods FormulaInstance Methods

### The following are methods for FormulaInstance .


Apex Reference Guide FormulaInstance Class

IN THIS SECTION:

##### evaluate(contextObject)

Calculates the formula expression and returns the formula output.

##### getReferencedFields()

Returns a set of strings that denote the field names referenced in a formula.

##### **`evaluate(contextObject)`**

Calculates the formula expression and returns the formula output.

Signature

```
   public Object evaluate(Object contextObject)

```

Parameters

```
   contextObject
```

Type: Object

An instance of the Apex class as generated with the `FormulaBuilder.builder()` method.

Return Value

Type: Object

Apex type that corresponds to the Apex class as configured by the `withType()` method in the `FormulaBuilder` class.

##### **`getReferencedFields()`**

Returns a set of strings that denote the field names referenced in a formula.

Signature

```
   public Set<String> getReferencedFields()

```

Return Value

Type: Set<String>

Usage

A formula is built and evaluated in the context of the current namespace of the subscriber org. If you package a formula that references
fields, the fields must be fully qualified with the namespace name.

Example

```
   FormulaEval.FormulaInstance ff = Formula.builder()

                       .withType(Schema.Account.class)

                       .withReturnType(FormulaEval.FormulaReturnType.STRING)

                       .withFormula('name & website')

                       .build();

```


### Apex Reference Guide FormulaReturnType Enum

```
   // Returns the field names 'name', and 'website' required to process the formula

   Set<String> fieldNames = ff.getReferencedFields();

   // Use the list of field names to generate dynamic soql

   String queryStr = 'select ' + string.join(fieldNames, ', ') + ' from Account limit 1';

   List<sObject> accounts = Database.query(queryStr);

   string formulaOutput = (string)ff.evaluate(accounts[0]);

   System.debug(formulaOutput);

### FormulaReturnType Enum

```

Specifies the return type for the `withReturnType(returnType)` method.

Enum Values

The following are the values of the `FormulaEval.FormulaReturnType` enum.

**Value** **Description**

`BOOLEAN` A value that can only be assigned `true`, `false`, or `null` .

`DATE` A value that indicates a particular day.

`DATETIME` A value that indicates a particular day and time, such as a timestamp.

`DECIMAL` A number that includes a decimal point. Decimal is an arbitrary precision number.

`DOUBLE` A 64-bit number that includes a decimal point.

`ID` Any valid 18-character Lightning Platform record identifier.

`INTEGER` A 32-bit number that doesn’t include a decimal point.

`LONG` A 64-bit number that doesn’t include a decimal point.

`STRING` Any set of characters surrounded by single quotes.

`TIME` A value that indicates a particular time.

## fsccashflow Namespace The fsccashflow namespace provides classes used in the FSCCashFlow Flexcards and its child Flexcards. The fsccashflow namespace has these classes.

IN THIS SECTION:

FSCCashFlowUtil Class
Use the callable FSCCashFlowUtil class to manage and validate data for party income and expense entities by passing in the action
and the corresponding arguments. This class provides utility methods used in FSCCashFlow Flexcard and its child Flexcards.


### Apex Reference Guide FSCCashFlowUtil Class FSCCashFlowUtil Class

Use the callable FSCCashFlowUtil class to manage and validate data for party income and expense entities by passing in the action and
the corresponding arguments. This class provides utility methods used in FSCCashFlow Flexcard and its child Flexcards.

Namespace

fsccashflow Namespace

Usage

The Financial Goals FlexCards use Integration Procedures that call the FSCHouseholdService class. These FlexCards display information
about Financial Goals.

IN THIS SECTION:

#### FSCCashFlowUtil Methods FSCCashFlowUtil Methods

### The FSCCashFlowUtil has these methods.

IN THIS SECTION:

GetPartyIncomeFrequencyLabel
Returns the picklist values for the party income frequency field on the party income entity.

GetPartyIncomeTypeLabel
Returns the picklist values for the party income type field on the party income entity.

GetPartyIncomeStatusLabel
Returns the picklist values for the party income status field on the party income entity.

CalculateIncomeExpenseSummary
Calculates the monthly income, total income, average monthly income, monthly expense, total expense, average monthly expense
from a list of income and expenses provided.

GetPartyExpenseFrequencyLabel
Returns the picklist values for the party expense frequency field on the party expense entity.

GetPartyExpenseTypeLabel
Returns the picklist values for the party expense type field on the party expense entity.

GetPartyExpenseStatusLabel
Returns the picklist values for the party expense status field on the party expense entity.

PerformIncomeValidation
Performs validations on Party Income records. Ensure that the start date is not earlier than the end date.

PerformExpenseValidation
Performs validations on Party Income records.


Apex Reference Guide FSCCashFlowUtil Class

GetDurationDateRange
Returns the start and end date given a duration.For example, if you input the number 3 on the date 10/29/2024, it will return a start
date of 7/1/2024 and an end date of 10/1/2024.

HandleUpsertError
Helper method that constructs the error response for upsert of a partyIncome or partyExpense record.

CheckReadAccess
Checks for read access on the partyIncome and partyExpense entities.

CheckCrudOnIncome
Checks create, update and delete access on partyIncome entity.

CheckCrudOnExpense
Checks create, update and delete access on partyExpense entity.

##### **`GetPartyIncomeFrequencyLabel`**

Returns the picklist values for the party income frequency field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income frequency.

##### **`GetPartyIncomeTypeLabel`**

Returns the picklist values for the party income type field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income type.

##### **`GetPartyIncomeStatusLabel`**

Returns the picklist values for the party income status field on the party income entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income status.


Apex Reference Guide FSCCashFlowUtil Class

##### **`CalculateIncomeExpenseSummary`**

Calculates the monthly income, total income, average monthly income, monthly expense, total expense, average monthly expense from
a list of income and expenses provided.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns income and expense details.

Examples

Input and output JSON example of the actions are as follows.

Input format:

```
     [

       {

          "Duration": "12",

          "PartyExpenseList": [

            {

               "Name": "PE-0000000004",

               "UsageType": "CashFlow",

               "RecurrenceInterval": "Monthly",

               "Type": "Child Care",

               "Id": "2n3SG000007dkzpYAA",

               "TotalAmount": 999.99,

               "PartyId": "001SG000004TCczYAG",

               "Status": "Active",

               "StartDate": "2024-01-29T08:00:00.000Z"

            }

          ],

          "PartyIncomeList": [

            {

               "Name": "PI-0000000003",

               "UsageType": "CashFlow",

               "IncomeFrequency": "Monthly",

               "IncomeType": "Salary",

               "Id": "2m3SG000007dkzpYAA",

               "IncomeAmount": 999.99,

               "PartyId": "001SG000004TCczYAG",

               "IncomeStatus": "Active",

               "StartDate": "2024-01-29T08:00:00.000Z"

            }

          ]

       }

     ]

```

Output format:

```
     [

       {

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "MonthlyIncome": {

            "Nov 2023": 0,

            "Aug 2024": 999.99,

            "Oct 2023": 0,

            "Jan 2024": 96.7732258064516,

            "Mar 2024": 999.99,

            "Jul 2024": 999.99,

            "Apr 2024": 999.99,

            "Dec 2023": 0,

            "Jun 2024": 999.99,

            "Sep 2024": 999.99,

            "Feb 2024": 999.99,

            "May 2024": 999.99

          },

          "MonthlyExpense": {

            "Nov 2023": 0,

            "Aug 2024": 999.99,

            "Oct 2023": 0,

            "Jan 2024": 96.7732258064516,

            "Mar 2024": 999.99,

            "Jul 2024": 999.99,

            "Apr 2024": 999.99,

            "Dec 2023": 0,

            "Jun 2024": 999.99,

            "Sep 2024": 999.99,

            "Feb 2024": 999.99,

            "May 2024": 999.99

          },

          "AvgMonthlyExpense": 674.72,

          "TotalIncome": 8096.69,

          "TotalSurplus": 0,

          "AvgMonthlyIncome": 674.72,

          "AvgMonthlySurplus": 0,

          "TotalExpense": 8096.69

       }

     ]

##### **`GetPartyExpenseFrequencyLabel`**

```

Returns the picklist values for the party expense frequency field on the party expense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense frequency.

##### **`GetPartyExpenseTypeLabel`**

Returns the picklist values for the party expense type field on the party expense entity.


Apex Reference Guide FSCCashFlowUtil Class

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense type.

##### **`GetPartyExpenseStatusLabel`**

Returns the picklist values for the party expense status field on the party expense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Expense status.

##### **`PerformIncomeValidation`**

Performs validations on Party Income records. Ensure that the start date is not earlier than the end date.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income type.

Examples

Input and output JSON example of the actions are as follows.

Input format:

```
     [

       {

          "IncomeFrequency": "Weekly",

          "IncomeFrequencyLabelObject": {

            "value": "Weekly",

            "label": "Weekly"

          },

          "MemberOptionsList": [

            {

               "value": "001OG00000xx6gAYAQ",

               "label": "Okee PA"

            },

            {

               "value": "id2",

               "label": "Name2"

```


Apex Reference Guide FSCCashFlowUtil Class

```
            }

          ],

          "IsHousehold": true,

          "IncomeAmount": 100,

          "IncomeStatusOptions": [

            {

               "value": "Active",

               "label": "Active"

            },

            {

               "value": "Inactive",

               "label": "Inactive"

            }

          ],

          "PartyId": "001OG00000xx6gAYAQ",

          "IncomeStatus": "Active",

          "Party": {

            "Name": "Okee PA",

            "Id": "001OG00000xx6gAYAQ"

          },

          "IncomeTypeOptions": [

            {

               "value": "Salary",

               "label": "Salary"

            },

            {

               "value": "Commission",

               "label": "Commission"

            },

            {

               "value": "Fees",

               "label": "Fees"

            },

            {

               "value": "Rent",

               "label": "Rent"

            }

          ],

          "StartDate": "2024-02-02T00:00:00.000Z",

          "Name": "PI-0000000009",

          "FrequencyOptions": [

            {

               "value": "Weekly",

               "label": "Weekly"

            },

            {

               "value": "Monthly",

               "label": "Monthly"

            },

            {

               "value": "Yearly",

               "label": "Yearly"

            }

          ],

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "UsageType": "CashFlow",

          "IncomeId": "2m3OG000000009xxAQ",

          "IsPersonAccount": false,

          "IncomeTypeLabelObject": {

            "value": "Salary",

            "label": "Salary"

          }

       }

     ]

```

Output format:

```
     [

       {

          "dateErrorMessage": null,

          "IncomeFrequency": "Weekly",

          "IncomeFrequencyLabelObject": {

            "value": "Weekly",

            "label": "Weekly"

          },

          "MemberOptionsList": [

            {

               "value": "001OG000003f6gAYAQ",

               "label": "Okee PA"

            },

            {

               "value": "id2",

               "label": "Name2"

            }

          ],

          "requiredFieldErrorMessage": "Required fields:Type",

          "IsHousehold": true,

          "IncomeAmount": 100,

          "PartyId": "001OG000003f6gAYAQ",

          "IncomeStatusOptions": [

            {

               "value": "Active",

               "label": "Active"

            },

            {

               "value": "Inactive",

               "label": "Inactive"

            }

          ],

          "Party": {

            "Name": "Okee PA",

            "Id": "001OG000003f6gAYAQ"

          },

          "IncomeStatus": "Active",

          "hasUpsertError": false,

          "IncomeTypeOptions": [

            {

               "value": "Salary",

               "label": "Salary"

            },

```


Apex Reference Guide FSCCashFlowUtil Class

```
            {

               "value": "Commission",

               "label": "Commission"

            },

            {

               "value": "Fees",

               "label": "Fees"

            },

            {

               "value": "Rent",

               "label": "Rent"

            }

          ],

          "StartDate": "2024-02-02T00:00:00.000Z",

          "Name": "PI-0000000009",

          "FrequencyOptions": [

            {

               "value": "Weekly",

               "label": "Weekly"

            },

            {

               "value": "Monthly",

               "label": "Monthly"

            },

            {

               "value": "Yearly",

               "label": "Yearly"

            }

          ],

          "UsageType": "CashFlow",

          "IncomeId": "2m3OG000000009IYAQ",

          "IsPersonAccount": false,

          "IncomeTypeLabelObject": {

            "value": "Salary",

            "label": "Salary"

          }

       }

     ]

##### **`PerformExpenseValidation`**

```

Performs validations on Party Income records.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of picklist labels for Party Income frequency.


Apex Reference Guide FSCCashFlowUtil Class

Examples

Output JSON example of the actions are as follows.

Output format:

```
     {

       "Required fields": "Expense Type, Member, Amount, Start Date, Frequency"

     }

##### **`GetDurationDateRange`**

```

Returns the start and end date given a duration.For example, if you input the number 3 on the date 10/29/2024, it will return a start date
of 7/1/2024 and an end date of 10/1/2024.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns the start and end date for a specified duration.

Examples

Output JSON example of the actions are as follows.

Output format:

```
     {

           "DurationStartDate": "2024-02-02T00:00:00.000Z",

           "DurationEndDate": "2024-05-02T00:00:00.000Z"

          }

##### **`HandleUpsertError`**

```

Helper method that constructs the error response for upsert of a partyIncome or partyExpense record.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns a list of errors encountered while upserting the record in the database.

Examples

Input and output JSON example of the action are as follows.

Input format:

```
     [

       {

```


Apex Reference Guide FSCCashFlowUtil Class

```
          "Name": "PI-0000000003",

          "UsageType": "CashFlow",

          "IncomeFrequency": "Monthly",

          "IncomeType": "Salary",

          "Id": "2m3SG000007dkxxYAA",

          "IncomeAmount": 999.99,

          "PartyId": "001SG000004TCxxYAG",

          "IncomeStatus": "Active",

          "StartDate": "2024-01-29T08:00:00.000Z"

       }

     ]

```

Output format:

```
     [ { "UpsertError“: "Invalid Id“ } ]

##### **`CheckReadAccess`**

```

Checks for read access on the partyIncome and partyExpense entities.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether read access is granted or not.

Examples

Output JSON example of the action are as follows.

Output format:

```
     { "isAccessible" : "true" }

##### **`CheckCrudOnIncome`**

```

Checks create, update and delete access on partyIncome entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether create, update and delete access on the partyIncome entity is given.

Examples

Output JSON example of the action are as follows.


## Apex Reference Guide Functions Namespace

Output format:

```
     { "isCreatable" : "true", "isUpdateable" : "true", "isDeletable": "true" }

##### **`CheckCrudOnExpense`**

```

Checks create, update and delete access on partyExpense entity.

Signature

```
   call(String action, Map<String, Object> args

```

Return Value

Returns True or False based on whether create, update and delete access on the partyExpense entity is given.

Examples

Output JSON example of the action are as follows.

Output format:

```
     { "isCreatable" : "true", "isUpdateable" : "true", "isDeletable": "true" }

## Functions Namespace

```

The Functions namespace provides classes and methods used to invoke and manage Salesforce Functions.

Salesforce Functions is your code, run on demand, in the Salesforce Functions trusted elastic compute cloud. Upload your complex
business logic code, written using your preferred languages and frameworks, and Salesforce Functions takes care of everything else
necessary to invoke your code in a secure, multi-tenant aware, and self-scaling environment. For more details on Salesforce Functions,
[see Salesforce Functions.](https://developer.salesforce.com/docs/platform/functions/guide)

The following are the classes in the `functions` namespace.

IN THIS SECTION:

Function Class
Use the Function class to access deployed Salesforce Functions, and invoke them synchronously or asynchronously.

FunctionCallback Interface
Represents the callback Salesforce calls when an asynchronous, queued Function invocation has completed.

FunctionErrorType Enum
Represents the error type of FunctionInvocationError.

FunctionInvocation Interface
Use FunctionInvocation to get the status and results of a synchronous or asynchronous Function invocation.

FunctionInvocationError Interface
Use FunctionInvocationError to get detailed error information about a failed Function invocation.

FunctionInvocationStatus Enum
Represents the status of a Function invocation.


### Apex Reference Guide Function Class

FunctionInvokeMock Interface
Use the `FunctionInvokeMock` interface to mock Salesforce Functions responses during testing.

MockFunctionInvocationFactory Class
Use the `MockFunctionInvocationFactory` methods to generate appropriate mock responses for testing Salesforce
Functions.

### Function Class

Use the Function class to access deployed Salesforce Functions, and invoke them synchronously or asynchronously.

Namespace

functions

Usage

The Function class represents an instance of a deployed Function you can invoke from your org. You can invoke Functions synchronously,
or asynchronously using asynchronous Apex.

If your Function takes longer than 2 minutes to return, the request times out. To avoid timing out, consider using asynchronous invocation.
Invoking a Function asynchronously doesn’t count against asynchronous Apex limits, such as Apex Queueable limits.

Before synchronously invoking a Function, commit any pending data operations in Apex, otherwise you get a CalloutException. For
asynchronous invocations, the queued invocation doesn’t happen if the Apex transaction isn’t committed. Any data operations that
happen in the Function itself aren’t considered part of the Apex transaction.

Functions can’t be invoked in an Apex test. A “Function invocations from Apex tests are not supported” CalloutException is thrown if
Apex determines that a Function is being invoked during a test. If you must run tests against code that invokes Functions, mock your
Function invocations during the tests. See FunctionInvocation Example Implementation for an example of a mocked FunctionInvocation
that you can use in testing.

Example

The following example synchronously invokes a deployed “accountfunction” Function:

```
   functions.Function accountFunction = functions.Function.get('MyProject.accountfunction');

   functions.FunctionInvocation invocation = accountFunction.invoke('{ "accountName" : "Acct",

    "contactName" : "MyContact", "opportunityName" : "Oppty" }');

   String jsonResponse = invocation.getResponse();

```

The following example asynchronously invokes a deployed “AccountFunction” Function, using the provided callback:

```
   functions.Function accountFunction = functions.Function.get('MyProject.accountfunction');

   accountFunction.invoke('{ "accountName" : "Acct", "contactName" : "MyContact",

   "opportunityName" : "Oppty" }', new MyCallback());

   public class MyCallback

     implements functions.FunctionCallback {

      public void handleResponse(functions.FunctionInvocation result) {

       // Handle result of function invocation

       // ...

```


Apex Reference Guide Function Class

```
      }

   }

```

IN THIS SECTION:

#### Function Methods Function Methods The following are methods for Function .

IN THIS SECTION:

##### get(functionName)

Returns the Function instance for the named Function and Project. The Function must be properly deployed and have appropriate
permissions to work with the org running your Apex code.

get(namespace, functionName)
Returns the Function instance for the named Function, Project, and Namespace. The Function must be properly deployed and have
appropriate permissions to work with the org running your Apex code.

invoke(payload, callback)
Invokes the Function asynchronously.

invoke(payload)
Invokes the Function synchronously.

##### get(functionName)

Returns the Function instance for the named Function and Project. The Function must be properly deployed and have appropriate
permissions to work with the org running your Apex code.

Signature

```
   public static functions.Function get(String functionName)

```

Parameters

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
#### “ project name . function name ”. For example, to retrieve the generatepdf Function in the Onboarding Function

Project, use `Onboarding.generatepdf` . The Function and Project must be deployed to a compute environment connected
to the org.

Return Value

Type: functions.Function

Returns a Function instance that you can invoke.


Apex Reference Guide Function Class

Usage

The `Function.get()` method can throw the following exceptions:

**•** `InvalidParameterValueException`   - The _`functionName`_ parameter doesn’t have the correct _`project`_
_`name`_ . _`function name`_ format.

**•** `NoDataFoundException`   - The project or Function name provided in the _`functionName`_ parameter couldn’t be found.
Make sure the project and Function name are spelled correctly and that the project and Function have been properly deployed.

##### get(namespace, functionName)

Returns the Function instance for the named Function, Project, and Namespace. The Function must be properly deployed and have
appropriate permissions to work with the org running your Apex code.

Signature

```
   public static functions.Function get(String namespace, String functionName)

```

Parameters

```
   namespace
```

Type: String

The name of the Namespace that both the Salesforce Function and the Functions Project are part of. The org the Function is in must
be `global` to access across namespaces. Default value is the same org where the method is being called.

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
“ _`project name`_ . _`function name`_ ”. For example, to retrieve the `generatepdf` Function in the `Onboarding` Function
Project, use `Onboarding.generatepdf` . The Function and Project must be deployed to a compute environment connected
to the org.

Return Value

Type: functions.Function

Returns a Function instance that you can invoke.

Usage

The `Function.get()` method can throw the following exceptions:

**•** `InvalidParameterValueException`   - The _`functionName`_ parameter doesn’t have the correct _`project`_
_`name`_ . _`function name`_ format.

**•** `NoDataFoundException`   - The project or Function name provided in the _`functionName`_ parameter couldn’t be found.
Make sure the project and Function name are spelled correctly and that the project and Function have been properly deployed.

**•** `RuntimeException`   - The function is `public` yet references a function across namespaces. Make sure to retrieve references
across namespaces only in a `global` org.

##### invoke(payload, callback)

Invokes the Function asynchronously.


Apex Reference Guide Function Class

Signature

```
   public functions.FunctionInvocation invoke(String payload, functions.FunctionCallback

   callback)

```

Parameters

```
   payload
```

Type: String

The payload data that gets passed to the Function. Specify your payload data in a JSON-format string.

```
   callback
```

Type: functions.FunctionCallback

A FunctionCallback implementation that gets called when your Function is invoked asynchronously.

Return Value

Type: functions.FunctionInvocation

Returns a FunctionInvocation that contains information about the results of the invocation, such as the Function response, or error
results.

Usage

The `Function.invoke(payload, callback)` method can throw the following exceptions:

**•** `CalloutException`   - One of the following conditions causes this exception to be thrown:

**–** [Salesforce Functions isn’t enabled on the current org. For more details on enabling Functions, see Configure Orgs for Functions](https://developer.salesforce.com/docs/platform/functions/guide/config-org#enable-functions-on-dev-hub-orgs)
in the Functions Developer Guide.

**–** The Function is being invoked in an Apex test. Functions can’t be invoked in tests.

**–** The “Functions” permission set is missing or has incorrect permissions for `FunctionInvocationRequest` . For more
details on the correct permissions for `FunctionInvocationRequest` [see Function Permissions in the Functions Developer](https://developer.salesforce.com/docs/platform/functions/guide/permissions)
Guide.

**–** The provided payload isn’t valid JSON.

**–** The Function hasn’t completed deployment to a compute environment or invocation request returns a 404 HTTP error.

**•** `InvalidParameterValueException`   - The _`callback`_ parameter is null or references a class that doesn’t implement
`functions.FunctionCallback` .

**•** `NoDataFoundException`   - A reference for the Function couldn’t be found in the current org. Make sure the project and
Function have been properly deployed.

##### invoke(payload)

Invokes the Function synchronously.

Signature

```
   public functions.FunctionInvocation invoke(String payload)

```


### Apex Reference Guide FunctionCallback Interface

Parameters

```
   payload
```

Type: String

The payload data that gets passed to the Function. Specify your payload data in a JSON-format string.

Return Value

Type: functions.FunctionInvocation

Returns a FunctionInvocation that contains information about the results of the invocation, such as the Function response, or error
results.

Usage

The `Function.invoke(payload)` method can throw the following exceptions:

**•** `CalloutException`   - One of the following conditions causes this exception to be thrown:

**–** [Salesforce Functions isn’t enabled on the current org. For more details on enabling Functions, see Configure Orgs for Functions](https://developer.salesforce.com/docs/platform/functions/guide/config-org#enable-functions-on-dev-hub-orgs)
in the Functions Developer Guide.

**–** The Function is being invoked in an Apex test. Functions can’t be invoked in tests.

**–** The provided payload isn’t valid JSON.

**–** There are pending DML operations.

**–** The Function is being synchronously invoked from an Apex trigger.

**–** The Function hasn’t completed deployment to a compute environment or invocation request returns a 404 HTTP error.

**–** The Function request returns a 5xx HTTP error.

**–** The Function invocation has exceeded the time limit for synchronous invocations. For details on the time limit and work-arounds,
[see Limits in the Functions Developer Guide.](https://developer.salesforce.com/docs/platform/functions/guide/limits#apex-limits-and-functions)

**•** `NoDataFoundException`   - A reference for the Function couldn’t be found in the current org. Make sure the project and
Function have been properly deployed.

### FunctionCallback Interface

Represents the callback Salesforce calls when an asynchronous, queued Function invocation has completed.

Namespace

functions

Usage

When invoking Functions asynchronously via `Function.invoke(payload, callback)`, you provide your own class that
implements FunctionCallback.

IN THIS SECTION:

FunctionCallback Methods

FunctionCallback Example Implementation


### Apex Reference Guide FunctionErrorType Enum

#### FunctionCallback Methods The following are methods for FunctionCallback .

IN THIS SECTION:

##### handleResponse(var1)

Called when an asynchronous Function invocation has completed.

##### handleResponse(var1)

Called when an asynchronous Function invocation has completed.

Signature

```
   public void handleResponse(functions.FunctionInvocation var1)

```

Parameters

```
   var1
```

Type: functions.FunctionInvocation

The result parameter contains JSON response information and error information.

Return Value

Type: void

#### FunctionCallback Example Implementation

This is an example implementation of the `functions.FunctionCallback` interface.

```
   public class MyCallback

     implements functions.FunctionCallback {

      public void handleResponse(functions.FunctionInvocation result) {

       // Handle result of function invocation

       String jsonResponse = result.getResponse();

       System.debug('Got response ' + jsonResponse);

       JSONParser parser = JSON.createParser(jsonResponse);

       // Process JSON using your own data class...

      }

   }

```

The following example uses this implementation when invoking a Function asynchronously:

```
   myFunction.invoke('{ "accountName" : "Acct", "contactName" : "MyContact", "opportunityName"

    : "Oppty" }', new MyCallback());

### FunctionErrorType Enum

```

Represents the error type of FunctionInvocationError.


### Apex Reference Guide FunctionInvocation Interface

Enum Values

These are the values of the `functions.FunctionErrorType` enum.

**Value** **Description**

```
FUNCTION_EXCEPTION

```

A known exception resulting from the Function logic itself. Examples include an
exception thrown from the Function code, or an exception thrown from a library
or framework the Function uses.

`RUNTIME_EXCEPTION` A known exception resulting from the Salesforce Functions runtime. For example,
a malformed payload passed to the Function when invoked results in this error type.

`UNEXPECTED_FUNCTION_EXCEPTION` An unknown exception. For example, a network or system-level issue within the
Salesforce Functions infrastructure results in this error type.

### FunctionInvocation Interface

Use FunctionInvocation to get the status and results of a synchronous or asynchronous Function invocation.

Namespace

functions

Usage

The results of a Function invocation are passed back via FunctionInvocation. Use this instance to determine if the invocation was successful,
and any results from the Function invocation.

You can also implement your own FunctionInvocation interface if you run Apex tests with your Function invocation code. Your test code
can create and use your own FunctionInvocation instance in place of using the results from a call to `Function.invoke()` .

IN THIS SECTION:

#### FunctionInvocation Methods

FunctionInvocation Example Implementation

#### FunctionInvocation Methods

### The following are methods for FunctionInvocation .

IN THIS SECTION:

getError()
Returns error information for a Function invocation.

getInvocationId()
Returns the invocation ID of the Function invocation.

getResponse()
Returns the response string of the Function invocation.


Apex Reference Guide FunctionInvocation Interface

##### getStatus()

Returns the status of the Function invocation.

##### getError()

Returns error information for a Function invocation.

Signature

```
   public functions.FunctionInvocationError getError()

```

Return Value

Type: functions.FunctionInvocationError

Contains a `FunctionInvocationError` instance that you can use to get information about any invocation errors. If the Function
was invoked successfully, the returned instance is null.

##### getInvocationId()

Returns the invocation ID of the Function invocation.

Signature

```
   public String getInvocationId()

```

Return Value

Type: String

This ID is available after a call to either the synchronous or asynchronous `Function.invoke()` methods. For asynchronous
invocations, this ID can be used to check the status of the queued invocation.

##### getResponse()

Returns the response string of the Function invocation.

Signature

```
   public String getResponse()

```

Return Value

Type: String

The response string is the raw request JSON response, which can be parsed using the JSONParser Class.

##### getStatus()

Returns the status of the Function invocation.


### Apex Reference Guide FunctionInvocationError Interface

Signature

```
   public functions.FunctionInvocationStatus getStatus()

```

Return Value

Type: functions.FunctionInvocationStatus

The result of the invocation, such as `FunctionInvocationStatus.SUCCESS` or `FunctionInvocationStatus.ERROR` .

#### FunctionInvocation Example Implementation

This is an example implementation of the `functions.FunctionInvocation` interface.

```
   public class MyFunctionInvocationError

     implements functions.FunctionInvocationError {

      public String getMessage() {

       return 'Mock error message for testing';

      }

      public functions.FunctionErrorType getType() {

       return functions.FunctionErrorType.FUNCTION_EXCEPTION;

      }

   }

   public class MyFunctionInvocation

     implements functions.FunctionInvocation {

      public functions.FunctionInvocationStatus getStatus() {

       return functions.FunctionInvocationStatus.ERROR;

      }

      public String getResponse() {

       return 'Mock response for testing';

      }

      public String getInvocationId() {

       return 'MOCKTESTID';

      }

      public functions.FunctionInvocationError getError() {

       functions.FunctionInvocationError testError = new MyFunctionInvocationError();

       return testError;

      }

   }

```

The following example tests the implementation:

```
   functions.FunctionInvocation testInvocation = new MyFunctionInvocation();

   if (testInvocation.getStatus() == functions.FunctionInvocationStatus.ERROR) {

      System.debug('Error: ' + (testInvocation.getError() != null ?

   testInvocation.getError().getMessage() : 'UNKNOWN'));

      return;

   }

### FunctionInvocationError Interface

```

Use FunctionInvocationError to get detailed error information about a failed Function invocation.


Apex Reference Guide FunctionInvocationError Interface

Namespace

functions

Usage

FunctionInvocationError contains various error information such as the error message at the time of the error.

IN THIS SECTION:

#### FunctionInvocationError Methods

FunctionInvocationError Example Implementation

#### FunctionInvocationError Methods The following are methods for FunctionInvocationError .

IN THIS SECTION:

##### getMessage()

Returns the error message from a Function invocation error.

##### getType()

Returns the error type for FunctionInvocationError.

##### getMessage()

Returns the error message from a Function invocation error.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### **`getType()`**

Returns the error type for FunctionInvocationError.

Signature

```
   public functions.FunctionErrorType getType()

```

Return Value

Type: functions.FunctionErrorType


### Apex Reference Guide FunctionInvocationStatus Enum

#### FunctionInvocationError Example Implementation

This is an example implementation of the `functions.FunctionInvocationError` interface.

```
   public class MyFunctionInvocationError

     implements functions.FunctionInvocationError {

       public String getMessage() {

         return 'Mock error message for testing';

       }

       public functions.FunctionErrorType getType() {

         return functions.FunctionErrorType.FUNCTION_EXCEPTION;

       }

   }

```

This example tests the implementation.

```
   functions.FunctionInvocationError testError = new MyFunctionInvocationError();

   System.debug('Error: ' + testError.getMessage() + ' Type: ' + testError.getType());

### FunctionInvocationStatus Enum

```

Represents the status of a Function invocation.

Enum Values

The following are the values of the `functions.FunctionInvocationStatus` enum.

**Value** **Description**

`ERROR` The invocation failed. Check the FunctionInvocation and FunctionInvocationError
returned by the invoke call to debug the issue.

`PENDING` The invocation is pending. If the Function is being invoked asynchronously, the
invocation is still in the asynch queue.

```
SUCCESS

```

The invocation succeeded. Use `FunctionInvocation.getResponse()`
with the FunctionInvocation instance returned by the invoke call to get any response
returned by the Function.

### FunctionInvokeMock Interface Use the FunctionInvokeMock interface to mock Salesforce Functions responses during testing.

Namespace

functions

Usage

To mock Salesforce Functions testing, implement an appropriate mock response in the `respond(functionName,payload)`
### method of the FunctionInvokeMock interface. During mock testing of a Salesforce Functions, Apex runtime sends the response


Apex Reference Guide FunctionInvokeMock Interface

specified in the `respond()` method, rather than invoking the function itself. Appropriate success and error messages can be configured
with the `createSuccessResponse(invocationId,message)` and
`createErrorResponse(invocationId,functionsErrorType,errorMsg)` methods in
`Functions.MockFunctionInvocationFactory` .

IN THIS SECTION:

#### FunctionInvokeMock Methods

FunctionInvokeMock Example Implementation

#### FunctionInvokeMock Methods The following are methods for FunctionInvokeMock .

IN THIS SECTION:

##### respond(functionName, payload)

The mock response implemented in the `Functions.FunctionInvokeMock` interface. The response is sent by Apex runtime
when the `Test.setMock()` method is called.

##### **`respond(functionName, payload)`**

The mock response implemented in the `Functions.FunctionInvokeMock` interface. The response is sent by Apex runtime
when the `Test.setMock()` method is called.

Signature

```
   public functions.FunctionInvocation respond(String functionName, String payload)

```

Parameters

```
   functionName
```

Type: String

The name of the Salesforce Function and the Functions Project that the Function is part of. The format of the parameter string is
“ _`project name`_ . _`function name`_ ”.

```
   payload
```

Type: String

The JSON-format payload data that is passed to the Function.

Return Value

Type: FunctionInvocation Interface

The result of the mock call to Salesforce Functions. Appropriate responses can be generated by using the
`createSuccessResponse()` and `createErrorResponse()` methods in the
`Functions.MockFunctionInvocationFactory` class.


Apex Reference Guide FunctionInvokeMock Interface

#### FunctionInvokeMock Example Implementation

This is sample implementation of the `functions.FunctionInvokeMock` interface.

```
   @isTest

   public class FunctionsInvokeMockImpl implements functions.FunctionInvokeMock {

      public functions.FunctionInvocation respond(String functionName, String payload) {

        // return mock success response

        String invocationId = '000000000000000';

        String response = 'mockResponse';

       return functions.MockFunctionInvocationFactory.createSuccessResponse(invocationId,

    response);

      }

   }

```

This example shows the minimal setup required for testing synchronous and asynchronous functions and is simplified to include both
function invocations and the `FunctionCallback` class.

```
   @isTest

   public class FunctionTest {

      @isTest

      static void testSyncFunctionCall() {

           // Set mock class to respond to function invocations

        Test.setMock( functions.FunctionInvokeMock.class, new FunctionsInvokeMockInner());

          functions.Function mockedFunction = functions.Function.get('example.function');

           Test.startTest();

           // Synchronous function call

           functions.FunctionInvocation invokeResult = mockedFunction.invoke('{}');

           Test.stopTest();

           // Verify that the received response contains expected mock values

           System.assertEquals(functions.FunctionInvocationStatus.SUCCESS,

   invokeResult.getStatus());

           System.assertEquals('mockResponse', invokeResult.getResponse());

           System.assertEquals('000000000000000', invokeResult.getInvocationId());

        }

        @isTest

        static void testAsyncFunctionCall() {

           // Set mock class to respond to function invocations

           Test.setMock( functions.FunctionInvokeMock.class, new

   FunctionsInvokeMockInner());

          functions.Function mockedFunction = functions.Function.get('example.function2');

           Test.startTest();

           //Asynchronous function invocation with callback

           mockedFunction.invoke('{}', new DemoCallback());

```


### Apex Reference Guide MockFunctionInvocationFactory Class

```
           Test.stopTest();

           // Include assertions here about the expected callback processing

        }

         public class DemoCallback implements functions.FunctionCallback {

           public void handleResponse(functions.FunctionInvocation invokeResult) {

             // Handle result of function invocation

             // The callback is included in the example here for convenience

             // It would normally be defined in the classes being tested

             // Verify that the received response contains expected mock values

             System.assertEquals(invokeResult.getStatus(),

   functions.FunctionInvocationStatus.ERROR);

             functions.FunctionInvocationError resultError = invokeResult.getError();

           System.assertEquals('bang', invokeResult.getError().getMessage());

           System.assertEquals('000000000000000', invokeResult.getInvocationId());

           }

        }

        public class FunctionsInvokeMockInner implements functions.FunctionInvokeMock {

          public functions.FunctionInvocation respond(String functionName, String payload)

    {

             // return mock success response

             String invocationId = '000000000000000';

             if(functionName == 'example.function2') {

               return functions.MockFunctionInvocationFactory.createErrorResponse(

                  invocationId,

                  functions.FunctionErrorType.FUNCTION_EXCEPTION,

                  'bang');

             }

             String response = 'mockResponse';

             return

   functions.MockFunctionInvocationFactory.createSuccessResponse(invocationId, response);

           }

        }

      }

### MockFunctionInvocationFactory Class Use the MockFunctionInvocationFactory methods to generate appropriate mock responses for testing Salesforce Functions.

```

Namespace

functions


Apex Reference Guide MockFunctionInvocationFactory Class

Usage

To mock Salesforce Functions testing, implement an appropriate mock response in the `respond(functionName,payload)`
method of the `FunctionInvokeMock` interface. During mock testing of a Salesforce Functions, the Apex runtime sends the response
specified in the `respond()` method, rather than invoking the function itself. Appropriate success and error messages can be configured
with the `createSuccessResponse(invocationId,message)` and
`createErrorResponse(invocationId,functionsErrorType,errorMsg)` methods.

See FunctionInvokeMock Example Implementation.

IN THIS SECTION:

#### MockFunctionInvocationFactory Methods MockFunctionInvocationFactory Methods The following are methods for MockFunctionInvocationFactory .

IN THIS SECTION:

##### createErrorResponse(invocationId, functionsErrorType, errMsg)

Generate a response for an error condition during mock testing of Salesforce Functions.

createSuccessResponse(invocationId, response)
Generate a response for a successful mock test of Salesforce Functions.

##### **`createErrorResponse(invocationId, functionsErrorType, errMsg)`**

Generate a response for an error condition during mock testing of Salesforce Functions.

Signature

```
   public static functions.FunctionInvocation createErrorResponse(String invocationId,

   functions.FunctionErrorType functionsErrorType, String errMsg)

```

Parameters

```
   invocationId
```

Type: String

The ID associated with a call to either the synchronous or asynchronous `Function.invoke()` method.

```
   functionsErrorType
```

Type: FunctionErrorType Enum

The error type of `FunctionInvocationError` .

```
   errMsg
```

Type: String

The error message.

Return Value

Type: FunctionInvocation Interface


## Apex Reference Guide ise_bots_apex Namespace

##### **`createSuccessResponse(invocationId, response)`**

Generate a response for a successful mock test of Salesforce Functions.

Signature

```
   public static functions.FunctionInvocation createSuccessResponse(String invocationId,

   String response)

```

Parameters

```
   invocationId
```

Type: String

The ID associated with a call to either the synchronous or asynchronous `Function.invoke()` method.

```
   response
```

Type: String

The message indicating success.

Return Value

Type: FunctionInvocation Interface

## ise_bots_apex Namespace

The ise_bots_apex namespace provides classes and properties to facilitate dynamic content generation and data handling for menu-driven
bot interactions. Create and manage dynamic menu items that adapt to user inputs, context, and underlying object data.

## The ise_bots_apex namespace includes these classes.

IN THIS SECTION:

### DynamicMenuItem Class

Contains properties to define and hold the details for a single dynamic menu item Each item contains information related to an
object, such as identifiers, labels, summaries, and sorting logic. It enables bots to present context-aware and user-relevant choices
dynamically during conversations. .

### DynamicMenuItem Class

Contains properties to define and hold the details for a single dynamic menu item Each item contains information related to an object,
such as identifiers, labels, summaries, and sorting logic. It enables bots to present context-aware and user-relevant choices dynamically
during conversations. .

Namespace

ise_bots_apex on page 2859


Apex Reference Guide DynamicMenuItem Class

IN THIS SECTION:

#### DynamicMenuItem Properties

Learn more about the properties available with the DynamicMenuItem class.

#### DynamicMenuItem Properties

Learn more about the properties available with the DynamicMenuItem class.

#### The DynamicMenuItem class includes these properties.

IN THIS SECTION:

##### EntityId

API name representing the ID field of the related Salesforce object.

##### EntityIdValue

The ID value retrieved at run time for the associated object.

EntityName
API name or label of the object being referenced, for example Case, Contact, or a custom object such as Service__c.

EntityNameValue
The name of the specific object instance.

Label
The label used to define how the item must be displayed in the bot menu.

LabelValue
The value of the label displayed to the user for the menu item at run time.

SummaryTextWithFormula
A formula or a string of text that defines the structure of the summary text displayed for the item. This formula is used to construct
a dynamic summary for the user after they make a selection.

SummaryTextWithFormulaValue
The summary string based on the formula and object data.

sortByDate
The API name of a date or date/time field on the object that's used to sort the dynamic menu items.

sortByDateValue
The DateTime value used at run time to sort the menu items chronologically.

##### **`EntityId`**

API name representing the ID field of the related Salesforce object.

Signature

```
   public String EntityId {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityId

```


Apex Reference Guide DynamicMenuItem Class

Property Value

Type: String

##### **`EntityIdValue`**

The ID value retrieved at run time for the associated object.

Signature

```
   public String EntityIdValue {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityIdValue

```

Property Value

Type: String

##### **`EntityName`**

API name or label of the object being referenced, for example Case, Contact, or a custom object such as Service__c.

Signature

```
   public String EntityName {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityName

```

Property Value

Type: String

##### **`EntityNameValue`**

The name of the specific object instance.

Signature

```
   public String EntityNameValue {get; set;}

   ise_bots_apex.DynamicMenuItem, EntityNameValue

```

Property Value

Type: String

##### **`Label`**

The label used to define how the item must be displayed in the bot menu.


Apex Reference Guide DynamicMenuItem Class

Signature

```
   public String Label {get; set;}

   ise_bots_apex.DynamicMenuItem, Label

```

Property Value

Type: String

##### **`LabelValue`**

The value of the label displayed to the user for the menu item at run time.

Signature

```
   public String LabelValue {get; set;}

   ise_bots_apex.DynamicMenuItem, LabelValue

```

Property Value

Type: String

##### **`SummaryTextWithFormula`**

A formula or a string of text that defines the structure of the summary text displayed for the item. This formula is used to construct a
dynamic summary for the user after they make a selection.

Signature

```
   public String SummaryTextWithFormula {get; set;}

   ise_bots_apex.DynamicMenuItem, SummaryTextWithFormula

```

Property Value

Type: String

##### **`SummaryTextWithFormulaValue`**

The summary string based on the formula and object data.

Signature

```
   public String SummaryTextWithFormulaValue {get; set;}

   ise_bots_apex.DynamicMenuItem, SummaryTextWithFormulaValue

```

Property Value

Type: String


## Apex Reference Guide industriesNlpSvc

##### **`sortByDate`**

The API name of a date or date/time field on the object that's used to sort the dynamic menu items.

Signature

```
   public Date sortByDate {get; set;}

   ise_bots_apex.DynamicMenuItem, sortByDate

```

Property Value

Type: Date

##### **`sortByDateValue`**

The DateTime value used at run time to sort the menu items chronologically.

Signature

```
   public Date sortByDateValue {get; set;}

   ise_bots_apex.DynamicMenuItem, sortByDateValue

```

Property Value

Type: Date

## industriesNlpSvc

Stores the objects used in Industries Einstein Natural Language Processing (NLP) services.

The industriesNlpSvc namespace contains these classes that are the outputs for the transformNlpActionResult Invocable action.

### • NlpResponse — Stores the NLP Summarization result performed for an NLP Operation involving summarization use cases such

as SurveyLongSummarization and SurveyShortSummarization.

**•** _`NlpSummarizationResult`_   - Provides the summary obtained as result of NLP Operation.

IN THIS SECTION:

### NlpResponse Class

Stores the result for an NLP Operation. NLP operation can be SurveyLongSummarization and SurveyShortSummarization.

NlpSummarizationResult Class
Provides the summary obtained as result of NLP Operation.

### NlpResponse Class

Stores the result for an NLP Operation. NLP operation can be SurveyLongSummarization and SurveyShortSummarization.


### Apex Reference Guide NlpSummarizationResult Class

Namespace

industriesNlpSvc

IN THIS SECTION:

#### NlpResponse Properties NlpResponse Properties The following are properties for NlpResponse .

IN THIS SECTION:

##### summarizationResult

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

##### errors

Represents the property to store errors that occurred as a result of the NLP Operation.

##### **`summarizationResult`**

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

Signature

```
   public industriesNlpSvc.NlpSummarizationResult summarizationResult {get; set;}

```

Property Value

Type: List<industriesNlpSvc.NlpSummarizationResult on page 2864>

##### **`errors`**

Represents the property to store errors that occurred as a result of the NLP Operation.

Signature

```
   public List<String> errors {get; set;}

```

Property Value

Type: List<String>

### NlpSummarizationResult Class

Provides the summary obtained as result of NLP Operation.


## Apex Reference Guide IndustriesDigitalLending Namespace

Namespace

industriesNlpSvc

IN THIS SECTION:

#### NlpSummarizationResult Properties NlpSummarizationResult Properties The following are properties for NlpSummarizationResult :

IN THIS SECTION:

##### summary

Represents the field that captures the summary obtained as result of NLP Operation.

##### **`summary`**

Represents the field that captures the summary obtained as result of NLP Operation.

Signature

```
   public String summary {get; set;}

```

Property Value

Type: List<String>

## IndustriesDigitalLending Namespace

The `industriesDigitalLending` namespace provides classes used in the Digital Lending OmniScripts and Integration Procedures.

The industriesDigitalLending namespace contains these classes:

**•** _`DigitalLendingIntakeRecordsWrapper`_   - Use the callable DigitalLendingIntakeRecordsWrapper class to call utility
methods from OmniScripts used in Digital Lending application intake process.

**•** _`DigitalLendingPostIntakeRecordsWrapper`_   - Use the callable DigitalLendingPostIntakeRecordsWrapper class to
call utility methods from integration procedures used in Digital Lending post intake in FlexCards.

**•** _`DigitalLendingProductsApi`_   - Use the callable DigitalLendingProductsApi class to call utility methods from integration
procedures used in Digital Lending FlexCards.

**•** _`DigitalLendingUtils`_   - Use the callable DigitalLendingUtils class to call utility methods from integration procedures used
in Digital Lending PostIntake FlexCards.

**•** _`PricingExecutionWrapper`_   - Use the callable PricingExecutionWrapper class to call utility methods from integration
procedures used in Digital Lending FlexCards.

[See industriesDigitalLending namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/apex_namespace_industriesDigitalLending.htm)


## Apex Reference Guide Invocable Namespace Invocable Namespace The Invocable namespace provides classes for calling invocable actions from Apex. These classes are in the Invocable namespace.

IN THIS SECTION:

### Action Class

Contains methods to create, update, and retrieve information about invocable actions.

Action.Error Class
Contains methods to retrieve errors returned by invocable actions.

Action.Result Class
Contains methods to retrieve results from invocable actions called from Apex code.

### Action Class

Contains methods to create, update, and retrieve information about invocable actions.

Namespace

## Invocable

IN THIS SECTION:

#### Action Methods

SEE ALSO:

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_Salesforce Help_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

#### Action Methods

### These methods are for Action .

IN THIS SECTION:

addInvocation()
Creates an empty invocation in preparation for calling an invocable action. After you create the invocation, you can add parameters
to the invocation.

clearInvocations()
Clears the existing invocations from the action.

clone()
Creates a copy of the `Invocable.Action` .

createCustomAction(type, namespace, name)
Creates a wrapper for a custom invocable action in a specified package namespace.


Apex Reference Guide Action Class

createCustomAction(type, name)
Creates a wrapper for a custom invocable action.

createStandardAction(type)
Creates a wrapper for a standard invocable action.

getName()
Gets the name of an invocable action.

getNamespace()
Gets the namespace of a custom invocable action.

getType()
Gets the type of an invocable action.

invoke()
Invokes an invocable action from Apex code.

isStandard()
Determines whether an invocable action is a standard invocable action.

setInvocationParameter(parameterName, parameterValue)
Sets a value for an invocable action parameter.

setInvocations(invocations)
Initializes the invocations for an action from a pre-existing list of invocations.

##### **`addInvocation()`**

Creates an empty invocation in preparation for calling an invocable action. After you create the invocation, you can add parameters to
the invocation.

Signature

```
   public Invocable.Action addInvocation()

```

Return Value

Type: Invocable.Action on page 2866

##### **`clearInvocations()`**

Clears the existing invocations from the action.

Signature

```
   public Invocable.Action clearInvocations()

```

Return Value

Type: Invocable.Action on page 2866


Apex Reference Guide Action Class

##### **`clone()`**

Creates a copy of the `Invocable.Action` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### **`createCustomAction(type, namespace, name)`**

Creates a wrapper for a custom invocable action in a specified package namespace.

Signature

```
   public static Invocable.Action createCustomAction(String type, String namespace, String

   name)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

```
   namespace
```

Type: String

Namespace where the invocable action is located.

```
   name
```

Type: String

Name for the custom invocable action.

Return Value

Type: Invocable.Action

##### **`createCustomAction(type, name)`**

Creates a wrapper for a custom invocable action.

Signature

```
   public static Invocable.Action createCustomAction(String type, String name)

```

Parameters

```
   type
```

Type: String


Apex Reference Guide Action Class

Type of invocable action.

```
   name
```

Type: String

Name for the custom invocable action.

Return Value

Type: Invocable.Action

##### **`createStandardAction(type)`**

Creates a wrapper for a standard invocable action.

Signature

```
   public static Invocable.Action createStandardAction(String type)

```

Parameters

```
   type
```

Type: String

Type of invocable action.

Return Value

Type: Invocable.Action

##### **`getName()`**

Gets the name of an invocable action.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the invocable action.

##### **`getNamespace()`**

Gets the namespace of a custom invocable action.

Signature

```
   public String getNamespace()

```


Apex Reference Guide Action Class

Return Value

Type: String

Namespace of the custom invocable action.

##### **`getType()`**

Gets the type of an invocable action.

Signature

```
   public String getType()

```

Return Value

Type: String

Type of invocable action.

##### **`invoke()`**

Invokes an invocable action from Apex code.

Signature

```
   public List<Invocable.Action.Result> invoke()

```

Return Value

Type: List<Invocable.Action.Result>

##### **`isStandard()`**

Determines whether an invocable action is a standard invocable action.

Signature

```
   public Boolean isStandard()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action is a standard invocable action.

##### **`setInvocationParameter(parameterName, parameterValue)`**

Sets a value for an invocable action parameter.


### Apex Reference Guide Action.Error Class

Signature

```
   public Invocable.Action setInvocationParameter(String parameterName, Object

   parameterValue)

```

Parameters

```
   parameterName
```

Type: String

Name of the invocable action parameter to set.

```
   parameterValue
```

Type: Object

Value to set the invocable action parameter to.

Return Value

Type: Invocable.Action on page 2866

##### **`setInvocations(invocations)`**

Initializes the invocations for an action from a pre-existing list of invocations.

Signature

```
   public Invocable.Action setInvocations(List<Map<String,ANY>> invocations)

```

Parameters

```
   invocations
```

Type: List on page 3874<Map on page 3894<String on page 4107,ANY>>

List of invocations for the invocable action.

Return Value

Type: Invocable.Action on page 2866

### Action.Error Class

Contains methods to retrieve errors returned by invocable actions.

Namespace

Invocable

IN THIS SECTION:

Action.Error Methods


Apex Reference Guide Action.Error Class

#### Action.Error Methods These methods are for Action.Error .

IN THIS SECTION:

##### clone()

Creates a copy of the `Invocable.Action.Error` .

##### getCode()

Gets the error code returned by an invocable action.

##### getMessage()

Gets the error message returned by an invocable action.

##### **`clone()`**

Creates a copy of the `Invocable.Action.Error` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### **`getCode()`**

Gets the error code returned by an invocable action.

Signature

```
   public String getCode()

```

Return Value

Type: String

##### **`getMessage()`**

Gets the error message returned by an invocable action.

Signature

```
   public String getMessage()

```

Return Value

Type: String


### Apex Reference Guide Action.Result Class Action.Result Class

Contains methods to retrieve results from invocable actions called from Apex code.

Namespace

Invocable

IN THIS SECTION:

#### Action.Result Methods Action.Result Methods

### The methods are for Action.Result .

IN THIS SECTION:

##### clone()

Creates a copy of the `Invocable.Action.Result` .

getAction()
Gets the invocable action that was invoked and caused a result to be returned.

getErrors()
Gets a list of errors that were returned by an invocable action.

getInvocationParameters()
Gets a list of the parameter values set for an invocable action. This method returns a list that contains the input parameter values
for each invocation of an action. Each map in the list contains a key for the name of each input parameter.

getOutputParameters()
Gets a list of the parameter values returned by an invocable action. This method returns a list that contains the result for each
invocation of an action. Each map in the list contains a key for the name of each output parameter.

isSuccess()
Determines if an invocable action ran without errors.

##### **`clone()`**

Creates a copy of the `Invocable.Action.Result` .

Signature

```
   public Object clone()

```

Return Value

Type: Object


Apex Reference Guide Action.Result Class

##### **`getAction()`**

Gets the invocable action that was invoked and caused a result to be returned.

Signature

```
   public Invocable.Action getAction()

```

Return Value

Type: Invocable.Action on page 2866

##### **`getErrors()`**

Gets a list of errors that were returned by an invocable action.

Signature

```
   public List on page 4107<Invocable.Action.Error on page 2871> getErrors()

```

Return Value

Type: List on page 4107<Invocable.Action.Error on page 2871>

##### **`getInvocationParameters()`**

Gets a list of the parameter values set for an invocable action. This method returns a list that contains the input parameter values for
each invocation of an action. Each map in the list contains a key for the name of each input parameter.

Signature

```
   public Map<String,Object> getInvocationParameters()

```

Return Value

Type: Map on page 3894<String on page 4107,Object>

##### **`getOutputParameters()`**

Gets a list of the parameter values returned by an invocable action. This method returns a list that contains the result for each invocation
of an action. Each map in the list contains a key for the name of each output parameter.

Signature

```
   public Map<String,Object> getOutputParameters()

```

Return Value

Type: Map on page 3894<String on page 4107,Object>


## Apex Reference Guide InvoiceWriteOff Namespace

##### **`isSuccess()`**

Determines if an invocable action ran without errors.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action ran successfully.

## InvoiceWriteOff Namespace The InvoiceWriteOff namespace provides classes to create credit memos with the total charge amount on the invoice as the

write-off amount.

## The InvoiceWriteOff namespace includes these classes.

**•** [WriteOffInvoiceInputList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm)

**•** [WriteOffInvoiceInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm)

**•** [WriteOffInvoiceResponseList Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm)

**•** [WriteOffInvoiceResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm)

**•** [WriteOffInvoiceResponseError Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm)

## IsvPartners Namespace The IsvPartners namespace provides a class associated with Salesforce ISV partner use cases, such as optimizing code, providing

great customer trial experiences, and driving feature adoption.

## These are the classes in the IsvPartners namespace.

IN THIS SECTION:

### AppAnalytics Class

Contains methods to help with AppExchange App Analytics use cases, such as minimizing subscriber attrition and obtaining product
insights.

### AppAnalytics Class

Contains methods to help with AppExchange App Analytics use cases, such as minimizing subscriber attrition and obtaining product
insights.

Namespace

## IsvPartners


Apex Reference Guide AppAnalytics Class

Usage

#### Use AppAnalytics and its methods to log App Analytics custom interactions.

Example

```
   public void submitClicked() {

        Id jobId = System.enqueueJob(new MyQueueable(colorValue));

        IsvPartners.AppAnalytics.logCustomInteraction(

           MyPageInteractions.SUBMIT_CLICKED, jobId);

```

IN THIS SECTION:

#### AppAnalytics Methods AppAnalytics Methods These are methods for AppAnalytics .

IN THIS SECTION:

##### logCustomInteraction(interactionLabel, interactionId)

Logs the custom interaction using a label that you provide as an enum value and an interaction ID.

logCustomInteraction(interactionLabel, interactionUuid)
Logs the custom interaction using a label that you provide as an enum value and an interaction ID that you provide as an Apex UUID.

logCustomInteraction(interactionLabel)
Logs the custom interaction using a label that you provide as an enum value.

##### **`logCustomInteraction(interactionLabel, interactionId)`**

Logs the custom interaction using a label that you provide as an enum value and an interaction ID.

Signature

```
   public static void logCustomInteraction(Object interactionLabel, Id interactionId)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

```
   interactionId
```

Type: Id

An Apex ID that is associated with the custom interaction. The `interactionId` that you provide is hashed and tokenized before
it’s included in AppExchange App Analytics package usage logs.


Apex Reference Guide AppAnalytics Class

Return Value

Type: Void

##### **`logCustomInteraction(interactionLabel, interactionUuid)`**

Logs the custom interaction using a label that you provide as an enum value and an interaction ID that you provide as an Apex UUID.

Signature

```
   public static void logCustomInteraction(Object interactionLabel, System.UUID

   interactionUuid)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

```
   interactionUuid
```

Type: System.UUID

An Apex UUID that is associated with the custom interaction. The `interactionId` that you provide is hashed and tokenized
before being included in AppExchange App Analytics package usage logs.

Return Value

Type: Void

##### **`logCustomInteraction(interactionLabel)`**

Logs the custom interaction using a label that you provide as an enum value.

Signature

```
   public static void logCustomInteraction(Object interactionLabel)

```

Parameters

```
   interactionLabel
```

Type: Object

A value used to label the custom interaction. The value of _`interactionLabel`_ must be an enum with the same namespace
##### as the code that calls the logCustomInteraction method.

Return Value

Type: Void


## Apex Reference Guide KbManagement Namespace KbManagement Namespace The KbManagement namespace provides a class for managing knowledge articles. The following is the class in the KbManagement namespace.

IN THIS SECTION:

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.

Namespace

## KbManagement

Usage

Use the methods in the `KbManagement.PublishingService` class to manage the following parts of the lifecycle of an article
and its translations:

### • Publishing

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

#### PublishingService Methods

### The following are methods for PublishingService . All methods are static.

IN THIS SECTION:

archiveOnlineArticle(articleId, scheduledDate)
Archives an online version of an article. If the specified scheduledDate is null, the article is archived immediately. Otherwise, it archives
the article on the scheduled date.


Apex Reference Guide PublishingService Class

assignDraftArticleTask(articleId, assigneeId, instructions, dueDate, sendEmailNotification)
Assigns a review task related to a draft article.

assignDraftTranslationTask(articleVersionId, assigneeId, instructions, dueDate, sendEmailNotification)
Assigns a review task related to a draft translation.

cancelScheduledArchivingOfArticle(articleId)
Cancels the scheduled archiving of an online article.

cancelScheduledPublicationOfArticle(articleId)
Cancels the scheduled publication of a draft article.

completeTranslation(articleVersionId)
Puts a translation in a completed state that is ready to publish.

deleteArchivedArticle(articleId)
Deletes an archived article.

deleteArchivedArticleVersion(articleId, versionNumber)
Deletes a specific archived version of a published article.

deleteDraftArticle(articleId)
Deletes a draft article.

deleteDraftTranslation(articleVersionId)
Deletes a draft translation.

editArchivedArticle(articleId)
Creates a draft article from the archived primary version and returns the new draft primary version ID of the article.

editOnlineArticle(articleId, unpublish)
Creates a draft article from the online version and returns the new draft primary version ID of the article. Also, unpublishes the online
article, if _`unpublish`_ is set to `true` .

editPublishedTranslation(articleId, language, unpublish)
Creates a draft version of the online translation for a specific language and returns the new draft primary version ID of the article.
Also, unpublishes the article, if set to `true` .

publishArticle(articleId, flagAsNew)
Publishes an article. If _`flagAsNew`_ is set to `true`, the article is published as a major version.

restoreOldVersion(articleId, versionNumber)
Creates a draft article from an existing online article based on the specified archived version of the article and returns the article
version ID.

scheduleForPublication(articleId, scheduledDate)
Schedules the article for publication as a major version. If the specified date is null, the article is published immediately.

setTranslationToIncomplete(articleVersionId)
Sets a draft translation that is ready for publication back to “in progress” status.

submitForTranslation(articleId, language, assigneeId, dueDate)
Submits an article for translation to the specified language. Also assigns the specified user and due date to the submittal and returns
new ID of the draft translation.


Apex Reference Guide PublishingService Class

##### archiveOnlineArticle(articleId, scheduledDate)

Archives an online version of an article. If the specified scheduledDate is null, the article is archived immediately. Otherwise, it archives
the article on the scheduled date.

Signature

```
   public static Void archiveOnlineArticle(String articleId, Datetime scheduledDate)

```

Parameters

```
   articleId
```

Type: String

```
   scheduledDate
```

Type: Datetime

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Datetime scheduledDate = Datetime.newInstanceGmt(2012, 12,1,13,30,0);

   KbManagement.PublishingService.archiveOnlineArticle(articleId, scheduledDate);

##### assignDraftArticleTask(articleId, assigneeId, instructions, dueDate, sendEmailNotification)

```

Assigns a review task related to a draft article.

Signature

```
   public static Void assignDraftArticleTask(String articleId, String assigneeId, String

   instructions, Datetime dueDate, Boolean sendEmailNotification)

```

Parameters

```
   articleId
```

Type: String

```
   assigneeId
```

Type: String

```
   instructions
```

Type: String

```
   dueDate
```

Type: Datetime

```
   sendEmailNotification
```

Type: Boolean


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   String assigneeId = '';

   String instructions = 'Please review this draft.';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12, 1);

   KbManagement.PublishingService.assignDraftArticleTask(articleId, assigneeId, instructions,

    dueDate, true);

##### assignDraftTranslationTask(articleVersionId, assigneeId, instructions, dueDate, sendEmailNotification)

```

Assigns a review task related to a draft translation.

Signature

```
   public static Void assignDraftTranslationTask(String articleVersionId, String assigneeId,

   String instructions, Datetime dueDate, Boolean sendEmailNotification)

```

Parameters

```
   articleVersionId
```

Type: String

```
   assigneeId
```

Type: String

```
   instructions
```

Type: String

```
   dueDate
```

Type: Datetime

```
   sendEmailNotification
```

Type: Boolean

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   String assigneeId = ' Insert assignee ID ';

   String instructions = 'Please review this draft.';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12, 1);

   KbManagement.PublishingService.assignDraftTranslationTask(articleId, assigneeId,

   instructions, dueDate, true);

```


Apex Reference Guide PublishingService Class

##### cancelScheduledArchivingOfArticle(articleId)

Cancels the scheduled archiving of an online article.

Signature

```
   public static Void cancelScheduledArchivingOfArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.cancelScheduledArchivingOfArticle (articleId);

##### cancelScheduledPublicationOfArticle(articleId)

```

Cancels the scheduled publication of a draft article.

Signature

```
   public static Void cancelScheduledPublicationOfArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.cancelScheduledPublicationOfArticle (articleId);

##### completeTranslation(articleVersionId)

```

Puts a translation in a completed state that is ready to publish.

Signature

```
   public static Void completeTranslation(String articleVersionId)

```


Apex Reference Guide PublishingService Class

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.completeTranslation(articleVersionId);

##### deleteArchivedArticle(articleId)

```

Deletes an archived article.

Signature

```
   public static Void deleteArchivedArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.deleteArchivedArticle(articleId);

##### deleteArchivedArticleVersion(articleId, versionNumber)

```

Deletes a specific archived version of a published article.

Signature

```
   public static Void deleteArchivedArticleVersion(String articleId, Integer versionNumber)

```

Parameters

```
   articleId
```

Type: String

```
   versionNumber
```

Type: Integer


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Integer versionNumber = 1;

   KbManagement.PublishingService.deleteArchivedArticleVersion(articleId, versionNumber);

##### deleteDraftArticle(articleId)

```

Deletes a draft article.

Signature

```
   public static Void deleteDraftArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.deleteDraftArticle(articleId);

##### deleteDraftTranslation(articleVersionId)

```

Deletes a draft translation.

Signature

```
   public static Void deleteDraftTranslation(String articleVersionId)

```

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void


Apex Reference Guide PublishingService Class

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.deleteDraftTranslation (articleVersionId);

##### editArchivedArticle(articleId)

```

Creates a draft article from the archived primary version and returns the new draft primary version ID of the article.

Signature

```
   public static String editArchivedArticle(String articleId)

```

Parameters

```
   articleId
```

Type: String

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.editArchivedArticle(articleId);

##### editOnlineArticle(articleId, unpublish)

```

Creates a draft article from the online version and returns the new draft primary version ID of the article. Also, unpublishes the online
article, if _`unpublish`_ is set to `true` .

Signature

```
   public static String editOnlineArticle(String articleId, Boolean unpublish)

```

Parameters

```
   articleId
```

Type: String

```
   unpublish
```

Type: Boolean

Return Value

Type: String


Apex Reference Guide PublishingService Class

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.editOnlineArticle (articleId, true);

##### editPublishedTranslation(articleId, language, unpublish)

```

Creates a draft version of the online translation for a specific language and returns the new draft primary version ID of the article. Also,
unpublishes the article, if set to `true` .

Signature

```
   public static String editPublishedTranslation(String articleId, String language, Boolean

   unpublish)

```

Parameters

```
   articleId
```

Type: String

```
   language
```

Type: String

```
   unpublish
```

Type: Boolean

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String language = 'fr';

   String id = KbManagement.PublishingService.editPublishedTranslation(articleId, language,

   true);

##### publishArticle(articleId, flagAsNew)

```

Publishes an article. If _`flagAsNew`_ is set to `true`, the article is published as a major version.

Signature

```
   public static Void publishArticle(String articleId, Boolean flagAsNew)

```

Parameters

```
   articleId
```

Type: String

```
   flagAsNew
```

Type: Boolean


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   KbManagement.PublishingService.publishArticle(articleId, true);

##### restoreOldVersion(articleId, versionNumber)

```

Creates a draft article from an existing online article based on the specified archived version of the article and returns the article version
ID.

Signature

```
   public static String restoreOldVersion(String articleId, Integer versionNumber)

```

Parameters

```
   articleId
```

Type: String

```
   versionNumber
```

Type: Integer

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String id = KbManagement.PublishingService.restoreOldVersion (articleId, 1);

##### scheduleForPublication(articleId, scheduledDate)

```

Schedules the article for publication as a major version. If the specified date is null, the article is published immediately.

Signature

```
   public static Void scheduleForPublication(String articleId, Datetime scheduledDate)

```

Parameters

```
   articleId
```

Type: String

```
   scheduledDate
```

Type: Datetime


Apex Reference Guide PublishingService Class

Return Value

Type: Void

Example

```
   String articleId = ' Insert article ID ';

   Datetime scheduledDate = Datetime.newInstanceGmt(2012, 12,1,13,30,0);

   KbManagement.PublishingService.scheduleForPublication(articleId, scheduledDate);

##### setTranslationToIncomplete(articleVersionId)

```

Sets a draft translation that is ready for publication back to “in progress” status.

Signature

```
   public static Void setTranslationToIncomplete(String articleVersionId)

```

Parameters

```
   articleVersionId
```

Type: String

Return Value

Type: Void

Example

```
   String articleVersionId = ' Insert article ID ';

   KbManagement.PublishingService.setTranslationToIncomplete(articleVersionId);

##### submitForTranslation(articleId, language, assigneeId, dueDate)

```

Submits an article for translation to the specified language. Also assigns the specified user and due date to the submittal and returns
new ID of the draft translation.

Signature

```
   public static String submitForTranslation(String articleId, String language, String

   assigneeId, Datetime dueDate)

```

Parameters

```
   articleId
```

Type: String

```
   language
```

Type: String

```
   assigneeId
```

Type: String


## Apex Reference Guide LxScheduler Namespace

```
   dueDate
```

Type: Datetime

Return Value

Type: String

Example

```
   String articleId = ' Insert article ID ';

   String language = 'fr';

   String assigneeId = ' Insert assignee ID ';

   Datetime dueDate = Datetime.newInstanceGmt(2012, 12,1);

   String id = KbManagement.PublishingService.submitForTranslation(articleId, language,

   assigneeId, dueDate);

## LxScheduler Namespace The LxScheduler namespace provides an interface and classes for integrating Salesforce Scheduler with external calendars. The following are the classes and the interface in the LxScheduler namespace.

```

IN THIS SECTION:

GetAppointmentCandidatesInput Class
Contains information about the available service resources (appointment candidates) based on work type group and service territories.

GetAppointmentCandidatesInputBuilder Class
Contains methods to build an instance of the `lxscheduler.GetAppointmentCandidatesInput` class.

GetAppointmentSlotsInput Class
Contains information about the available appointment time slots for a resource based on given work type group and territories.

GetAppointmentSlotsInputBuilder Class
Contains methods to build an instance of the `lxscheduler.GetAppointmentSlotsInput` class.

SchedulerResources Class
Contains methods that holds the business logic to get resources availability.

SkillRequirement Class
Contains information about the set of skills that are required to complete a particular task for a work type.

SkillRequirementBuilder Class
Contains methods to build an instance of the `lxscheduler.SkillRequirement` class.

WorkType Class
Contains information about the type of work to be performed.

WorkTypeBuilder Class
Contains methods to build an instance of the `lxscheduler.WorkType` class.

ServiceResourceScheduleHandler Interface
Allows an implementing class to check external calendar events to find already booked time slots for the requested service resources.
This interface is part of Salesforce Scheduler.


### Apex Reference Guide GetAppointmentCandidatesInput Class

ServiceAppointmentRequestInfo Class
Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface. This class is implemented internally
by Apex.

ServiceResourceInfo Class
Contains information about a service resource.

ServiceResourceSchedule Class
Use this class to pass results from your implemented Apex class to the ServiceResourceScheduleHandler interface methods.

UnavailableTimeslot Class
Use this class to pass the unavailable time slots to the lxscheduler.ServiceResourceSchedule class. Timezones that differ across
operating hours are handled and results are always returned in UTC.

SEE ALSO:

[Apex Interface Implementation Limitations and Error Codes](https://help.salesforce.com/s/articleView?id=platform.ls_ext_cal_integration_troubleshooting.htm&type=5&language=en_US)

### GetAppointmentCandidatesInput Class

Contains information about the available service resources (appointment candidates) based on work type group and service territories.

Set up Salesforce Scheduler before making requests. This setup includes creating or configuring Service Resources, Service Territory
[Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Set Up Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&type=5&language=en_US)
for more information.

The appointment time slots are determined based on multiple factors, such as field values, scheduled appointments, absences, Scheduler
[Settings, and Scheduling Policies to determine available time slots. See How Salesforce Scheduler Determines Available Time Slots for](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
more information.

The following factors are considered for returning start time and end time of resources.

**Resource Availability**
Determined using service territory member, service territory, work type, and account operating hours fields.

**Resource Unavailability**
Determined by resource absences, existing appointments that the resource is assigned to. The resource must be marked as a required
resource for the appointment with a status that isn’t in closed, canceled, or completed.

**Appointment Start Time Interval in the Scheduling Policy**
Appointment start time interval field in the Scheduling Policy is used to determine when the appointment can start. This interval
can be 5, 10, 15, 20, 30, or 60. By default, it’s set to 15.

**Work Type Duration**
The end time is calculated as start time + duration of the work type.

Note: If asset scheduling is enabled, the response also includes asset-based candidates.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentCandidatesInput Class

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the
GetAppointmentCandidatesInputBuilder.build() method.

This example shows how to get a list of available appointment candidates based on `workTypeGroupId` :

```
   //Build input for GetAppointmentCandidates API

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkTypeGroupId('0VSRM0000000ABc4AM')

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

   .setEndTime(System.now().addDays(5).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

      .setAccountId('001RM0000053iQgYAI')

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows how to get a list of available appointment candidates based on `workType` :

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

      .setId('08qRM0000000G9RYAU')

      .build();

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkType(workType)

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

   .setEndTime(System.now().addDays(5).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/New_York'))

      .setAccountId('001RM0000053iQgYAI')

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows how to get a list of available candidate appointments based on `durationInMinutes` and without the
`workTypeGroupId` or `workType` fields:

Important: If you're using shifts, you must specify the `workTypeGroupId` or `workType` field.

```
   //Build SkillRequirement

     lxscheduler.SkillRequirement skillReq = new lxscheduler.SkillRequirementBuilder()

      .setSkillId('0C5RM0000004EZS0A2')

      .setSkillLevel(90)

      .build();

```


### Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

      .setDurationInMinutes(15)

      .setBlockTimeBeforeAppointmentInMinutes(5)

      .setBlockTimeAfterAppointmentInMinutes(5)

      .setTimeFrameStartInMinutes(10080)

      .setTimeFrameEndInMinutes(40320)

      .setOperatingHoursId('0OHRM0000000FmG4AU')

      .setSkillRequirements(new List<lxscheduler.SkillRequirement>{skillReq})

      .build();

     lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

      .setWorkType(workType)

      .setTerritoryIds(new List<String>{'0HhRM0000000FXd0AM'})

      .setSchedulingPolicyId('0VrRM00000000Bx')

      .setApiVersion(Double.valueOf('50.0'))

      .build();

     String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

This example shows a sample response of a list of available candidates:

```
   [

     {

       "startTime": "2021-02-16T16:15:00.000+0000",

       "endTime": "2021-02-16T16:16:00.000+0000",

       "resources": [

         "0Hnxx0000004C9BCAU"

       ],

       "territoryId": "0Hhxx0000004C92CAE"

     },

     {

       "startTime": "2021-02-16T16:30:00.000+0000",

       "endTime": "2021-02-16T16:31:00.000+0000",

       "resources": [

        "0Hnxx0000004C9BCAU"

       ],

       "territoryId": "0Hhxx0000004C92CAE"

     },

   ]

### GetAppointmentCandidatesInputBuilder Class

```

Contains methods to build an instance of the `lxscheduler.GetAppointmentCandidatesInput` class.

### A Builder object is obtained by invoking one of the GetAppointmentCandidatesInputBuilder methods defined by the GetAppointmentCandidatesInput class.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

IN THIS SECTION:

#### GetAppointmentCandidatesInputBuilder Methods GetAppointmentCandidatesInputBuilder Methods The following are methods for GetAppointmentCandidatesInputBuilder .

IN THIS SECTION:

##### build()

Returns an instance of the `lxscheduler.GetAppointmentCandidatesInput` object.

setAccountId(accountId)
Sets the ID of the associated account for which you want to create the appointments.

setAllowConcurrent(allowConcurrent)
Allows the scheduling of concurrent appointments.

setApiVersion(apiVersion)
Sets the API version of the business logic for the `getAppointmentCandidates` method.

setCorrelationId(correlationId)
Sets the correlation ID.

setEndTime(endTime)
Sets the scheduling end time.

setEngagementChannelTypeIds(engagementChannelTypeIds)
Sets an engagement channel type.

setFilterByResources(filterByResources)
Enables filtering resources using a comma-separated list of service resource IDs.

setResourceLimitApptDistribution(resourceLimitApptDistribution)
Sets the number of service resources to show during appointment scheduling.

setSchedulingPolicyId(schedulingPolicyId)
Sets the ID of the AppointmentSchedulingPolicy object.

setStartTime(startTime)
Sets the scheduling start time to the specified time.

setTerritoryIds(territoryIds)
Sets the service territory IDs.

setWorkType(workType)
Sets the type of work to be performed.

setWorkTypeGroupId(workTypeGroupId)
Sets the ID of the work type group.

##### **`build()`**

Returns an instance of the `lxscheduler.GetAppointmentCandidatesInput` object.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentCandidatesInput build()

```

Return Value

Type: lxscheduler.GetAppointmentCandidatesInput

##### **`setAccountId(accountId)`**

Sets the ID of the associated account for which you want to create the appointments.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setAccountId(String accountId)

```

Parameters

```
   accountId
```

Type: String

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setAllowConcurrent(allowConcurrent)`**

Allows the scheduling of concurrent appointments.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setAllowConcurrent(Boolean

   allowConcurrent)

```

Parameters

```
   allowConcurrent
```

Type: Boolean

If true, allows scheduling of concurrent appointments in a time slot. The default is false.

Available in API version 47.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setApiVersion(apiVersion)`**

Sets the API version of the business logic for the `getAppointmentCandidates` method.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setApiVersion(Double apiVersion)

```

Parameters

```
   apiVersion
```

Type: Double

Usage

The specified parameter must use the correct API version. For example, if API version is set to 45.0 and _`filterByResources`_ is set
(which is available in API version 51.0 and later), then this field is ignored. If no API version or incorrect API version is passed in the request
body, by default the latest version is used.

Note: The API is available since version 45.0.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setCorrelationId(correlationId)`**

Sets the correlation ID.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setCorrelationId(String

   correlationId)

```

Parameters

```
   correlationId
```

Type: String

ID to pass custom information to the `ServiceResourceScheduleHandler` Apex interface. For example, you can use the
correlation ID to identify the app, website, or any other external system that calls this Apex interface implementation. If you don’t
pass a custom value, a randomly generated identifier is passed. Available in API version 53.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setEndTime(endTime)`**

Sets the scheduling end time.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setEndTime(String endTime)

```


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Parameters

```
   endTime
```

Type: String

The latest time that a time slot can end (inclusive).

Note: If end time is not specified, it defaults to 31 days.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setEngagementChannelTypeIds(engagementChannelTypeIds)`**

Sets an engagement channel type.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder

   setEngagementChannelTypeIds(List<String> engagementChannelTypeIds)

```

Parameters

```
   engagementChannelTypeIds
```

Type: List<String>

The ID of the engagement channel type record. The availability of service resources is filtered based on the engagement channel
type selected. This field is available in API version 56.0 and later.

Note: This field supports only one engagement channel type ID.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

Usage

You can use engagement channel types only in these cases:

**•** The **Schedule Appointments Using Engagement Channels** setting is enabled in Salesforce Scheduler Settings in your Salesforce
org.

**•** [Shifts are defined in the scheduling policy. For more information on setting up shifts in scheduling policy, see Define Shift Rules in](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)
[Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating-hours rules in the scheduling policy.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

##### **`setFilterByResources(filterByResources)`**

Enables filtering resources using a comma-separated list of service resource IDs.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setFilterByResources(List<String>

   filterByResources)

```

Parameters

```
   filterByResources
```

Type: List<String>

Gets only eligible resources that are both in the list and in the selected service territory sorted by the order in which the resource
IDs are passed. This field is available in API version 51.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setResourceLimitApptDistribution(resourceLimitApptDistribution)`**

Sets the number of service resources to show during appointment scheduling.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder

   setResourceLimitApptDistribution(Integer resourceLimitApptDistribution)

```

Parameters

```
   resourceLimitApptDistribution
```

Type: Integer

Specify the maximum number of service resources that you want to show during appointment scheduling when appointment
distribution is enabled. Available in API version 53.0 and later.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setSchedulingPolicyId(schedulingPolicyId)`**

Sets the ID of the AppointmentSchedulingPolicy object.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setSchedulingPolicyId(String

   schedulingPolicyId)

```


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Parameters

```
   schedulingPolicyId
```

Type: String

The ID of the `AppointmentSchedulingPolicy` object. If no scheduling policy is passed in the request body, the default
configurations are used.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setStartTime(startTime)`**

Sets the scheduling start time to the specified time.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setStartTime(String startTime)

```

Parameters

```
   startTime
```

Type: String

The earliest time that a time slot can begin (inclusive). You can also use a time from the past.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setTerritoryIds(territoryIds)`**

Sets the service territory IDs.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setTerritoryIds(List<String>

   territoryIds)

```

Parameters

```
   territoryIds
```

Type: List<String>

List of service territory IDs, where the work that is being requested is performed. This is a required field.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setWorkType(workType)`**

Sets the type of work to be performed.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setWorkType(lxscheduler.WorkType

   workType)

```

Parameters

```
   workType
```

Type: lxscheduler.WorkType

This method takes input as an instance of the `lxscheduler.WorkType` class. Build the instance of the input class using the
`lxscheduler.WorkTypeBuilder` class.

Required if _`workTypeGroupId`_ is not given. If id of the _`workType`_ is given, the rest of _`workType`_ fields are optional.

Usage

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder

##### **`setWorkTypeGroupId(workTypeGroupId)`**

Sets the ID of the work type group.

Signature

```
   public lxscheduler.GetAppointmentCandidatesInputBuilder setWorkTypeGroupId(String

   workTypeGroupId)

```

Parameters

```
   workTypeGroupId
```

Type: String

The ID of the work type group containing the work types that are being performed. Required if _`workType`_ is not given. If _`workType`_
is given, then you must provide either _`id`_ or _`durationInMinutes`_, but not both.

Return Value

Type: LxScheduler.GetAppointmentCandidatesInputBuilder


### Apex Reference Guide GetAppointmentSlotsInput Class GetAppointmentSlotsInput Class

Contains information about the available appointment time slots for a resource based on given work type group and territories.

The appointment time slots are determined based on your Salesforce Scheduler data model configurations. Here are some prerequisites
that you can consider while setting up data.

**•** Set up Salesforce Scheduler before making your requests. The setup includes creating or configuring Service Resources, Service
[Territory Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Manage](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)
[Business Information in Salesforce Scheduler for more information.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)

**•** Configure a work type mapped for each territory in the request body via Service Territory Work Type. Map the same work type to
the work type group, via work type group member.

The following factors affect how time slots are calculated and returned.

**•** Timezones that differ across operating hours are handled and results are always returned in UTC.

**•** The resource must be marked as a required resource on the assigned resource object.

**•** The resource is considered unavailable If the status categories of the resource assigned to service appointments are other than
`Canceled`, `Cannot Complete`, and `Completed` .

**•** Resource Absences of all types are considered unavailable from start to end.

**•** The following fields of Work Type records, if configured, are used to fine-tune time slot requirements. For more information, see
[Create Work Types in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_create_work_types.htm&language=en_US)

**Parameter** **Description**

`Timeframe Start` Time slots sooner than `current time +` _**`Timeframe Start`**_ aren’t
returned.

`Timeframe End` Time slots later than `current time +` _**`Timeframe End`**_ aren’t returned.

`Block Time Before Appointment` The time period before the appointment is considered as unavailable.

`Block Time After Appointment` The time period after the appointment is considered as unavailable.

```
Operating Hours

```

The overlap of all operating hours from the account, work type, service territory, and
service territory member are considered while determining time slots. For more
[information, see Set Up Operating Hours in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up_oh.htm&type=5&language=en_US)

**•** Only the time slots within the period of 31 days from the start date are returned.

**•** Salesforce Scheduler uses multiple factors, such as field values, scheduled appointments, absences, Scheduler Settings, and Scheduling
[Policies to determine available time slots, including the earliest and latest appointment slots. See How Does Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
[Determine Available Time Slots.](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)

Note: If asset scheduling is enabled, you can provide an asset-based service resource in `requiredResourceIds` to
retrieve available timeslots for the asset resource.

Namespace

LxScheduler


Apex Reference Guide GetAppointmentSlotsInput Class

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the GetAppointmentSlotsInputBuilder.build()
method.

This example shows how to get a list of available time slots based on `workTypeGroupId` :

```
   //Build input for GetAppointmentSlots API

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkTypeGroupId('0VSxx0000004C92GAE')

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setEndTime(System.now().addDays(1).format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setAccountId('001xx000003GYK0AAO')

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

       .setSchedulingPolicyId('0Vrxx0000004CAe')

       .setApiVersion(Double.valueOf('48.0'))

       .build();

   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows how to get a list of available time slots based on `workType` :

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

       .setId('08qxx0000004C92AAE')

       .build();

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkType(workType)

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setEndTime(System.now().addDays(1).format('yyyy-MM-dd\'T\'HH:mm:ssZ'))

       .setAccountId('001xx000003GYK0AAO')

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

       .setSchedulingPolicyId('0Vrxx0000004CAe')

       .setApiVersion(Double.valueOf('48.0'))

       .build();

   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows how to get a list of available time slots based on `durationInMinutes` and without `workTypeGroupId`
or `workType` fields:

```
   //Build WorkType

     lxscheduler.WorkType workType = new lxscheduler.WorkTypeBuilder()

       .setDurationInMinutes(60)

       .build();

     lxscheduler.GetAppointmentSlotsInput input = new

   lxscheduler.GetAppointmentSlotsInputBuilder()

       .setWorkType(workType)

       .setTerritoryIds(new List<String>{'0Hhxx0000004C92CAE'})

       .setRequiredResourceIds(new List<String>{'0Hnxx0000004C92CAE'})

```


### Apex Reference Guide GetAppointmentSlotsInputBuilder Class

```
       .setApiVersion(Double.valueOf('48.0'))

       .build();

     String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

This example shows a sample response of a list of available time slots:

```
   [

     {

      "territoryId": "0Hhxx0000004C92CAE",

      "startTime": "2021-02-10T16:00:00.000+0000",

      "endTime": "2021-02-10T16:15:00.000+0000",

      "remainingAppointments": 1

     },

     {

      "territoryId": "0Hhxx0000004C92CAE",

      "startTime": "2021-02-10T16:15:00.000+0000",

      "endTime": "2021-02-10T16:30:00.000+0000",

      "remainingAppointments": 1

     },

   ]

### GetAppointmentSlotsInputBuilder Class

```

Contains methods to build an instance of the `lxscheduler.GetAppointmentSlotsInput` class.

### A Builder object is obtained by invoking one of the GetAppointmentSlotsInputBuilder methods defined by the GetAppointmentSlotsInput class.

Namespace

LxScheduler

IN THIS SECTION:

#### GetAppointmentSlotsInputBuilder Methods GetAppointmentSlotsInputBuilder Methods

### The following are methods for GetAppointmentSlotsInputBuilder .

IN THIS SECTION:

build()
Returns an instance of the `lxscheduler.GetAppointmentSlotsInput` object.

setAccountId(accountId)
Sets the ID of the associated account for which you want to create appointments.

setAllowConcurrentScheduling(allowConcurrentScheduling)
Allows the scheduling of concurrent appointments.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

setApiVersion(apiVersion)
Sets the API version of the business logic for the `getAppointmentSlots` method.

setCorrelationId(correlationId)
Sets the correlation ID.

setEndTime(endTime)
Sets the scheduling end time.

setEngagementChannelTypeIds(engagementChannelTypeIds)
Sets an engagement channel type.

setPrimaryResourceId(primaryResourceId)
Sets the ID of the primary resource.

setRequiredResourceIds(requiredResourceIds)
Sets the resource IDs.

setSchedulingPolicyId(schedulingPolicyId)
Sets the ID of the `AppointmentSchedulingPolicy` object.

setStartTime(startTime)
Sets the scheduling start time.

setTerritoryIds(territoryIds)
Sets the IDs of service territories.

setWorkType(workType)
Sets the type of work to be performed.

setWorkTypeGroupId(workTypeGroupId)
Sets the ID of the work type group.

##### **`build()`**

Returns an instance of the `lxscheduler.GetAppointmentSlotsInput` object.

Signature

```
   public lxscheduler.GetAppointmentSlotsInput build()

```

Return Value

Type: lxscheduler.GetAppointmentSlotsInput

##### **`setAccountId(accountId)`**

Sets the ID of the associated account for which you want to create appointments.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setAccountId(String accountId)

```


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Parameters

```
   accountId
```

Type: String

The ID of the associated account.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setAllowConcurrentScheduling(allowConcurrentScheduling)`**

Allows the scheduling of concurrent appointments.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setAllowConcurrentScheduling(Boolean

   allowConcurrentScheduling)

```

Parameters

```
   allowConcurrentScheduling
```

Type: Boolean

If true, allows scheduling of concurrent appointments in a time slot. If false, concurrent appointments are not allowed. The default
is false. Available in API version 47.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setApiVersion(apiVersion)`**

Sets the API version of the business logic for the `getAppointmentSlots` method.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setApiVersion(Double apiVersion)

```

Parameters

```
   apiVersion
```

Type: Double

Usage

The specified parameter must use the correct API version. For example, if API version is set to 45.0 and _`primaryResourceId`_ is set
(which is available in API version 48.0 and later), then this field is ignored. If no API version or incorrect API version is passed in the request
body, by default the latest version is used.

Note: The API is available since version 45.0.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setCorrelationId(correlationId)`**

Sets the correlation ID.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setCorrelationId(String correlationId)

```

Parameters

```
   correlationId
```

Type: String

ID to pass custom information to the `ServiceResourceScheduleHandler` Apex interface. For example, you can use the
correlation ID to identify the app, website, or any other external system that calls this Apex interface implementation. If you don’t
pass a custom value, a randomly generated identifier is passed. Available in API version 53.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setEndTime(endTime)`**

Sets the scheduling end time.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setEndTime(String endTime)

```

Parameters

```
   endTime
```

Type: String

The latest time that a time slot can end (inclusive). If end time is not specified, it defaults to 31 days.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setEngagementChannelTypeIds(engagementChannelTypeIds)`**

Sets an engagement channel type.


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder

   setEngagementChannelTypeIds(List<String> engagementChannelTypeIds)

```

Parameters

```
   engagementChannelTypeIds
```

Type: List<String>

The ID of the engagement channel type record. The availability of time slots is filtered based on the engagement channel type
selected. This field is available in API version 56.0 and later.

Note: This field supports only one engagement channel type ID.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

Usage

You can use engagement channel types only in these cases:

**•** The **Schedule Appointments Using Engagement Channels** setting is enabled in Salesforce Scheduler Settings in your Salesforce
org.

**•** [Shifts are defined in the scheduling policy. For more information on setting up shifts in scheduling policy, see Define Shift Rules in](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)
[Scheduling Policy.](https://help.salesforce.com/s/articleView?id=platform.ls_use_shifts_to_determine_time_slots.htm&type=5&language=en_US)

Note: Engagement channel types are not supported with operating-hours rules in the scheduling policy.

##### **`setPrimaryResourceId(primaryResourceId)`**

Sets the ID of the primary resource.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setPrimaryResourceId(String

   primaryResourceId)

```

Parameters

```
   primaryResourceId
```

Type: String

The ID of the primary resource in multi-resource scheduling. Required only when multi-resource scheduling is enabled. Available in
API version 48.0 and later.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

##### **`setRequiredResourceIds(requiredResourceIds)`**

Sets the resource IDs.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setRequiredResourceIds(List<String>

   requiredResourceIds)

```

Parameters

```
   requiredResourceIds
```

Type: List<String>

List of resource IDs that must be available during the time slot. This is a required field.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setSchedulingPolicyId(schedulingPolicyId)`**

Sets the ID of the `AppointmentSchedulingPolicy` object.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setSchedulingPolicyId(String

   schedulingPolicyId)

```

Parameters

```
   schedulingPolicyId
```

Type: String

If no scheduling policy is passed in the request body, the default configurations are used.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setStartTime(startTime)`**

Sets the scheduling start time.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setStartTime(String startTime)

```

Parameters

```
   startTime
```

Type: String


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

The earliest time that a time slot can begin (inclusive). Defaults to the current time of the request, if empty.

Usage

The specified string should use the standard date format “['yyyy-MM-dd\’T\’HH:mm:ssZ']” in the local time zone. Defaults to the user’s
time zone.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setTerritoryIds(territoryIds)`**

Sets the IDs of service territories.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setTerritoryIds(List<String>

   territoryIds)

```

Parameters

```
   territoryIds
```

Type: List<String>

List of IDs of service territories, where the work that is being requested is performed. This is a required field.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

##### **`setWorkType(workType)`**

Sets the type of work to be performed.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setWorkType(lxscheduler.WorkType

   workType)

```

Parameters

```
   workType
```

Type: lxscheduler.WorkType

This method takes input as an instance of the `lxscheduler.WorkType` class. Build the instance of the input class using the
`lxscheduler.WorkTypeBuilder` class.

Required if _`workTypeGroupId`_ is not given.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder


### Apex Reference Guide SchedulerResources Class

##### **`setWorkTypeGroupId(workTypeGroupId)`**

Sets the ID of the work type group.

Signature

```
   public lxscheduler.GetAppointmentSlotsInputBuilder setWorkTypeGroupId(String

   workTypeGroupId)

```

Parameters

```
   workTypeGroupId
```

Type: String

The ID of the work type group containing the work types that are being performed.

Return Value

Type: lxscheduler.GetAppointmentSlotsInputBuilder

### SchedulerResources Class

Contains methods that holds the business logic to get resources availability.

Namespace

LxScheduler

Implementation Considerations

### Apex implementation of the methods in the SchedulerResources class should adhere to Apex Governor Limits. It includes

synchronous heap size limit, synchronous CPU time limit, and synchronous concurrent transactions for long running transactions. To
avoid governor limits, you must tune the input by reducing the time frame, limiting number of service resources, or limiting number or
territories at a time. This will reduce the overall transaction time and response size of the implementation. For more information on
[standard Apex Governer Limits, see Salesforce Developer Limits and Allocations Quick Reference.](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm)

Example

To get list of available service resources (appointment candidates):

```
   String response = lxscheduler.SchedulerResources.getAppointmentCandidates(input);

```

To get a list of available appointment time slots for a resource:

```
   String response = lxscheduler.SchedulerResources.getAppointmentSlots(input);

```

IN THIS SECTION:

SchedulerResources Methods


Apex Reference Guide SchedulerResources Class

#### SchedulerResources Methods The following are methods for SchedulerResources .

IN THIS SECTION:

##### getAppointmentCandidates(getAppointmentCandidatesInput)

Returns a list of service resources based on work type group or work type and service territories.

getAppointmentSlots(getAppointmentSlotsInput)
Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

setAppointmentCandidatesMock(expectedResponse)
##### Sets a mock object when running tests for the getAppointmentCandidates method.

setAppointmentSlotsMock(expectedResponse)
Sets a mock object when running tests for the `getAppointmentSlots` method.

##### **`getAppointmentCandidates(getAppointmentCandidatesInput)`**

Returns a list of service resources based on work type group or work type and service territories.

Set up Salesforce Scheduler before making requests. This setup includes creating or configuring Service Resources, Service Territory
[Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Set Up Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&type=5&language=en_US)
for more information.

The appointment time slots are determined based on multiple factors, such as field values, scheduled appointments, absences, Scheduler
[Settings, and Scheduling Policies to determine available time slots. See How Salesforce Scheduler Determines Available Time Slots for](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
more information.

The following factors are considered for returning start time and end time of resources.

**Resource Availability**
Determined using service territory member, service territory, work type, and account operating hours fields.

**Resource Unavailability**
Determined by resource absences, existing appointments that the resource is assigned to. The resource must be marked as a required
resource for the appointment with a status that isn’t in closed, canceled, or completed.

**Appointment Start Time Interval in the Scheduling Policy**
Appointment start time interval field in the Scheduling Policy is used to determine when the appointment can start. This interval
can be 5, 10, 15, 20, 30, or 60. By default, it’s set to 15.

**Work Type Duration**
The end time is calculated as start time + duration of the work type.

Note: If asset scheduling is enabled, the response also includes asset-based candidates.

Signature

```
   public static String getAppointmentCandidates(lxscheduler.GetAppointmentCandidatesInput

   getAppointmentCandidatesInput)

```


Apex Reference Guide SchedulerResources Class

Parameters

```
   getAppointmentCandidatesInput
```

Type: lxscheduler.GetAppointmentCandidatesInput

This method takes input as an instance of the `lxscheduler.GetAppointmentCandidatesInput` class. Build the
instance of the input class using the `lxscheduler.GetAppointmentCandidatesInputBuilder` class.

Return Value

Type: String

##### **`getAppointmentSlots(getAppointmentSlotsInput)`**

Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

The appointment time slots are determined based on your Salesforce Scheduler data model configurations. Here are some prerequisites
that you can consider while setting up data.

**•** Set up Salesforce Scheduler before making your requests. The setup includes creating or configuring Service Resources, Service
[Territory Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Manage](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)
[Business Information in Salesforce Scheduler for more information.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up.htm&language=en_US)

**•** Configure a work type mapped for each territory in the request body via Service Territory Work Type. Map the same work type to
the work type group, via work type group member.

The following factors affect how time slots are calculated and returned.

**•** Timezones that differ across operating hours are handled and results are always returned in UTC.

**•** The resource must be marked as a required resource on the assigned resource object.

**•** The resource is considered unavailable If the status categories of the resource assigned to service appointments are other than
`Canceled`, `Cannot Complete`, and `Completed` .

**•** Resource Absences of all types are considered unavailable from start to end.

**•** The following fields of Work Type records, if configured, are used to fine-tune time slot requirements. For more information, see
[Create Work Types in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_create_work_types.htm&language=en_US)

**Parameter** **Description**

`Timeframe Start` Time slots sooner than `current time +` _**`Timeframe Start`**_ aren’t
returned.

`Timeframe End` Time slots later than `current time +` _**`Timeframe End`**_ aren’t returned.

`Block Time Before Appointment` The time period before the appointment is considered as unavailable.

`Block Time After Appointment` The time period after the appointment is considered as unavailable.

```
Operating Hours

```

The overlap of all operating hours from the account, work type, service territory, and
service territory member are considered while determining time slots. For more
[information, see Set Up Operating Hours in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=platform.ls_set_up_oh.htm&type=5&language=en_US)

**•** Only the time slots within the period of 31 days from the start date are returned.


Apex Reference Guide SchedulerResources Class

**•** Salesforce Scheduler uses multiple factors, such as field values, scheduled appointments, absences, Scheduler Settings, and Scheduling
[Policies to determine available time slots, including the earliest and latest appointment slots. See How Does Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)
[Determine Available Time Slots.](https://help.salesforce.com/s/articleView?id=platform.ls_how_are_time_slots_determined.htm&type=5&language=en_US)

Note: If asset scheduling is enabled, you can provide an asset-based service resource in `requiredResourceIds` to
retrieve available timeslots for the asset resource.

Signature

```
   public static String getAppointmentSlots(lxscheduler.GetAppointmentSlotsInput

   getAppointmentSlotsInput)

```

Parameters

```
   getAppointmentSlotsInput
```

Type: lxscheduler.GetAppointmentSlotsInput

This method takes input as an instance of the `lxscheduler.GetAppointmentSlotsInput` class. Build the instance of
the input class using the `lxscheduler.GetAppointmentSlotsInputBuilder` class.

Return Value

Type: String

##### **`setAppointmentCandidatesMock(expectedResponse)`**

Sets a mock object when running tests for the `getAppointmentCandidates` method.

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   public static void setAppointmentCandidatesMock(String expectedResponse)

```

Parameters

```
   expectedResponse
```

Type: String

Return Value

Type: void

This example shows a sample implementation of the `GetAppointmentCandidates` class:

```
   public class AppointmentCandidateService {

     //Instance members for parsing

     public String startTime;

     public String endTime;

     public List<String> resources;

     public String territoryId;

     public static List<AppointmentCandidateService> getAppointmentCandidates(){

```


Apex Reference Guide SchedulerResources Class

```
       //Build input for GetAppointmentCandidates API

       lxscheduler.GetAppointmentCandidatesInput input = new

   lxscheduler.GetAppointmentCandidatesInputBuilder()

         .setWorkTypeGroupId('0VSRM0000000AGT4A2')

         .setTerritoryIds(new List<String>{'0HhRM0000000G8W0AU'})

        .setStartTime(System.now().format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/Los_Angeles'))

   .setEndTime(System.now().addDays(2).format('yyyy-MM-dd\'T\'HH:mm:ssZ','America/Los_Angeles'))

         .setSchedulingPolicyId('0VrRM00000000D0')

         .setApiVersion(Double.valueOf('50.0'))

         .build();

       List<AppointmentCandidateService> vList =

   parse(lxscheduler.SchedulerResources.getAppointmentCandidates(input));

       return vList;

     }

     private static List<AppointmentCandidateService> parse(String json) {

       return (List<AppointmentCandidateService>) System.JSON.deserialize(json,

   List<AppointmentCandidateService>.class);

     }

   }

```

This example shows how to set a sample mock using the `setAppointmentCandidatesMock` method:

```
   @isTest

   private class GetAppointmentCandidatesTest {

     static testMethod void getAppCandidatesTest() {

       String expectedResponse = '[' +

                         ' {' +

                        ' \"startTime\": \"2021-03-18T16:00:00.000+0000\",'

    +

                         ' \"endTime\": \"2021-03-18T17:00:00.000+0000\",'

   +

                         ' \"resources\": [' +

                         ' \"0HnRM0000000Fxv0AE\"' +

                         ' ],' +

                         ' \"territoryId\": \"0HhRM0000000G8W0AU\"' +

                         ' },' +

                         ' {' +

                        ' \"startTime\": \"2021-03-18T19:00:00.000+0000\",'

    +

                         ' \"endTime\": \"2021-03-18T20:00:00.000+0000\",'

   +

                         ' \"resources\": [' +

                         ' \"0HnRM0000000Fxv0AE\"' +

                         ' ],' +

                         ' \"territoryId\": \"0HhRM0000000G8W0AU\"' +

                         ' }' +

                         ']';

       lxscheduler.SchedulerResources.setAppointmentCandidatesMock(expectedResponse);

       Test.startTest();

         List<AppointmentCandidateService> candidateList =

```


### Apex Reference Guide SkillRequirement Class

```
   AppointmentCandidateService.getAppointmentCandidates();

         System.assertEquals(2, candidateList.size(), 'Should return only 2 records!');

       Test.stopTest();

     }

   }

##### **`setAppointmentSlotsMock(expectedResponse)`**

```

Sets a mock object when running tests for the `getAppointmentSlots` method.

This constructor is intended for test usage and throws an exception if used outside of the Apex test context.

Signature

```
   public static void setAppointmentSlotsMock(String expectedResponse)

```

Parameters

```
   expectedResponse
```

Type: String

Return Value

Type: void

### SkillRequirement Class

Contains information about the set of skills that are required to complete a particular task for a work type.

Namespace

LxScheduler

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the SkillRequirementBuilder.build() method.

### SkillRequirementBuilder Class

Contains methods to build an instance of the `lxscheduler.SkillRequirement` class.

### A Builder object is obtained by invoking one of the SkillRequirementBuilder methods defined by the SkillRequirement

class.

Namespace

LxScheduler


Apex Reference Guide SkillRequirementBuilder Class

IN THIS SECTION:

#### SkillRequirementBuilder Methods SkillRequirementBuilder Methods The following are methods for SkillRequirementBuilder .

IN THIS SECTION:

##### build()

Returns an instance of the `lxscheduler.SkillRequirement` object.

##### setSkillId(skillId)

Sets the skill that is required to complete a particular task for a work type. This is a required field.

##### setSkillLevel(skillLevel)

Sets the level of the skill that is required to complete a particular task for a work type

##### **`build()`**

Returns an instance of the `lxscheduler.SkillRequirement` object.

Signature

```
   public lxscheduler.SkillRequirement build()

```

Return Value

Type: lxscheduler.SkillRequirement

##### **`setSkillId(skillId)`**

Sets the skill that is required to complete a particular task for a work type. This is a required field.

Signature

```
   public lxscheduler.SkillRequirementBuilder setSkillId(String skillId)

```

Parameters

```
   skillId
```

Type: String

Return Value

Type: lxscheduler.SkillRequirementBuilder

##### **`setSkillLevel(skillLevel)`**

Sets the level of the skill that is required to complete a particular task for a work type


### Apex Reference Guide WorkType Class

Signature

```
   public lxscheduler.SkillRequirementBuilder setSkillLevel(Double skillLevel)

```

Parameters

```
   skillLevel
```

Type: Double

The skill levels can range from zero to 99.99. Depending on your business needs, you might want the skill level to reflect years of
experience, certification levels, or license classes.

Return Value

Type: lxscheduler.SkillRequirementBuilder

### WorkType Class

Contains information about the type of work to be performed.

Namespace

LxScheduler

Usage

The constructor for this class can’t be called directly. Create an instance of this class using the WorkTypeBuilder.build() method.

### WorkTypeBuilder Class

Contains methods to build an instance of the `lxscheduler.WorkType` class.

### A Builder object is obtained by invoking one of the WorkTypeBuilder methods defined by the WorkType class.

Namespace

LxScheduler

IN THIS SECTION:

#### WorkTypeBuilder Methods WorkTypeBuilder Methods

### The following are methods for WorkTypeBuilder .

IN THIS SECTION:

build()
Returns an instance of the `lxscheduler.WorkType` object.


Apex Reference Guide WorkTypeBuilder Class

##### setBlockTimeAfterAppointmentInMinutes(blockTimeAfterAppointmentInMinutes)

Sets the time period, in minutes.

setBlockTimeBeforeAppointmentInMinutes(blockTimeBeforeAppointmentInMinutes)
Sets the time period, in minutes.

setDurationInMinutes(durationInMinutes)
Sets the event length.

setId(id)
Sets the ID of the work type to the specified ID.

setOperatingHoursId(operatingHoursId)
Sets the overlap of operating hours.

setSkillRequirements(skillRequirements)
Sets the skills that are required to complete a particular task for a work type.

setTimeFrameEndInMinutes(timeFrameEndInMinutes)
Sets the end of the timeframe.

setTimeFrameStartInMinutes(timeFrameStartInMinutes)
Sets the beginning of the timeframe.

##### **`build()`**

Returns an instance of the `lxscheduler.WorkType` object.

Signature

```
   public lxscheduler.WorkType build()

```

Return Value

Type: lxscheduler.WorkType

##### **`setBlockTimeAfterAppointmentInMinutes(blockTimeAfterAppointmentInMinutes)`**

Sets the time period, in minutes.

Signature

```
   public lxscheduler.WorkTypeBuilder setBlockTimeAfterAppointmentInMinutes(Integer

   blockTimeAfterAppointmentInMinutes)

```

Parameters

```
   blockTimeAfterAppointmentInMinutes
```

Type: Integer

The time period after the appointment is considered unavailable.


Apex Reference Guide WorkTypeBuilder Class

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setBlockTimeBeforeAppointmentInMinutes(blockTimeBeforeAppointmentInMinutes)`**

Sets the time period, in minutes.

Signature

```
   public lxscheduler.WorkTypeBuilder setBlockTimeBeforeAppointmentInMinutes(Integer

   blockTimeBeforeAppointmentInMinutes)

```

Parameters

```
   blockTimeBeforeAppointmentInMinutes
```

Type: Integer

The time period before the appointment is considered as unavailable.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setDurationInMinutes(durationInMinutes)`**

Sets the event length.

Signature

```
   public lxscheduler.WorkTypeBuilder setDurationInMinutes(Integer durationInMinutes)

```

Parameters

```
   durationInMinutes
```

Type: Integer

Contains the event length, in minutes. Required if _`id`_ is not given.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setId(id)`**

Sets the ID of the work type to the specified ID.

Signature

```
   public lxscheduler.WorkTypeBuilder setId(String id)

```


Apex Reference Guide WorkTypeBuilder Class

Parameters

```
   id
```

Type: String

The ID of the work type. Required if you're using shifts or if _`durationInMinutes`_ is not given.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setOperatingHoursId(operatingHoursId)`**

Sets the overlap of operating hours.

Signature

```
   public lxscheduler.WorkTypeBuilder setOperatingHoursId(String operatingHoursId)

```

Parameters

```
   operatingHoursId
```

Type: String

The overlap of all operating hours from the account, work type, service territory, and service territory member are considered while
determining time slots.

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setSkillRequirements(skillRequirements)`**

Sets the skills that are required to complete a particular task for a work type.

Signature

```
   public lxscheduler.WorkTypeBuilder

   setSkillRequirements(List<lxscheduler.SkillRequirement> skillRequirements)

```

Parameters

```
   skillRequirements
```

Type: List<lxscheduler.SkillRequirement>

This method takes input as an instance of the `lxscheduler.SkillRequirement` class. Build the instance of the input class
using the `lxscheduler.SkillRequirementBuilder` class.

Return Value

Type: lxscheduler.WorkTypeBuilder


### Apex Reference Guide ServiceResourceScheduleHandler Interface

##### **`setTimeFrameEndInMinutes(timeFrameEndInMinutes)`**

Sets the end of the timeframe.

Signature

```
   public lxscheduler.WorkTypeBuilder setTimeFrameEndInMinutes(Integer

   timeFrameEndInMinutes)

```

Parameters

```
   timeFrameEndInMinutes
```

Type: Integer

Return Value

Type: lxscheduler.WorkTypeBuilder

##### **`setTimeFrameStartInMinutes(timeFrameStartInMinutes)`**

Sets the beginning of the timeframe.

Signature

```
   public lxscheduler.WorkTypeBuilder setTimeFrameStartInMinutes(Integer

   timeFrameStartInMinutes)

```

Parameters

```
   timeFrameStartInMinutes
```

Type: Integer

Return Value

Type: lxscheduler.WorkTypeBuilder

### ServiceResourceScheduleHandler Interface

Allows an implementing class to check external calendar events to find already booked time slots for the requested service resources.
This interface is part of Salesforce Scheduler.

Namespace

LxScheduler

Usage

The `lxscheduler.ServiceResourceScheduleHandler` interface is called by Salesforce Scheduler APIs.


Apex Reference Guide ServiceResourceScheduleHandler Interface

To implement this interface, you must first declare a class with the `implements` keyword as follows:

```
   public class ServiceResourceScheduleHandlerImpl implements

   LxScheduler.ServiceResourceScheduleHandler{}

```

Next, your class must provide an implementation for the following method:

```
   public static List<LxScheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(LxScheduler.ServiceAppointmentRequestInfo requestInfo){

       //Your code here

   }

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

#### ServiceResourceScheduleHandler Methods

ServiceResourceScheduleHandler Example Implementation

#### ServiceResourceScheduleHandler Methods The following are methods for ServiceResourceScheduleHandler .

IN THIS SECTION:

##### getUnavailableTimeslots(var1)

Passes the required information to get unavailable time slots from an external system. The implementation of this method returns
the `lxscheduler.ServiceResourceSchedule` class.

##### getUnavailableTimeslots(var1)

Passes the required information to get unavailable time slots from an external system. The implementation of this method returns the
`lxscheduler.ServiceResourceSchedule` class.

Signature

```
   public List<lxscheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(lxscheduler.ServiceAppointmentRequestInfo var1)

```

Parameters

```
   var1
```

Type: lxscheduler.ServiceAppointmentRequestInfo

Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface.

Return Value

Type: List<lxscheduler.ServiceResourceSchedule>


Apex Reference Guide ServiceResourceScheduleHandler Interface

#### ServiceResourceScheduleHandler Example Implementation

This is an example implementation of the `lxscheduler.ServiceResourceScheduleHandler` interface.

```
   /**

    * Implement interface lxscheduler.ServiceResourceScheduleHandler

    * This class is called when fetching service resources and time slots through Salesforce

    Scheduler API.*/

     Public class ServiceResourceScheduleHandlerImpl implements

   lxscheduler.ServiceResourceScheduleHandler{

      // The main interface method.

      public static List<lxscheduler.ServiceResourceSchedule>

   getUnavailableTimeslots(lxscheduler.ServiceAppointmentRequestInfo requestInfo){

        //Request info values.

        List<lxscheduler.ServiceResourceInfo>

   serviceResources=requestInfo.getServiceResources();

        DateTime startDate=requestInfo.getStartDate();

        DateTime endDate=requestInfo.getEndDate();

        List<lxscheduler.ServiceResourceSchedule> resourceUnavailability = new

   List<lxscheduler.ServiceResourceSchedule>();

        Set<lxscheduler.UnavailableTimeslot> unavailabilityIntervals = new

   Set<lxscheduler.UnavailableTimeslot>();

        //This is a dummy response. Implement your own business logic to connect to your

   internal or external systems.

        for (Integer i = 0; i < 5; i++) {

           //Set the unavailability intervals of a service resource.

           unavailabilityIntervals.add(new

   lxscheduler.UnavailableTimeslot(startDate.addMinutes(15*i),startDate.addMinutes(15*(i+1))));

        }

        for (lxscheduler.ServiceResourceInfo ServiceResource:serviceResources) {

           //Set the unavailability of Service resource.

        resourceUnavailability.add(new

   lxscheduler.ServiceResourceSchedule(serviceResource.getServiceResourceId(),unavailabilityIntervals));

        }

        return resourceUnavailability;

      }

   }

```

This example shows how to set a sample test mock using the `lxscheduler.ServiceResourceScheduleHandler` interface.

```
   @isTest

   private class ServiceResourceScheduleHandlerImplTest {

     static testMethod void getUnavailableTimeslotsTest() {

       //Initializing the test execution with mock values. Change it according to the

```


### Apex Reference Guide ServiceAppointmentRequestInfo Class

```
   implementation.

       //In case of non-test execution, the lxscheduler.ServiceAppointmentRequestInfo

   instance will automatically initialize.

       //Mock values for lxscheduler.ServiceResourceInfo

       String userId = '005D2000000I1N6IAK';

       String userName = 'someuser@example.com';

       String email = 'someuser@example.com';

       String serviceResourceId = '0HnD20000004C9bKAE';

       List<String> territoryIds = new List<String>();

       String resourceType = 'T';

       lxscheduler.ServiceResourceInfo serviceResInfo = new

   lxscheduler.ServiceResourceInfo(userId, userName, email,

                                    serviceResourceId, territoryIds,

   resourceType);

       //Mock values for lxscheduler.ServiceAppointmentRequestInfo

       DateTime startDate = System.now();

       DateTime endDate = System.now();

       List<lxscheduler.ServiceResourceInfo> serviceResources = new

   List<lxscheduler.ServiceResourceInfo>();

       serviceResources.add(serviceResInfo);

       String schedulingPolicyId = '0VrD20000004C9S';

       String workTypeGroupId = '0VSD20000004C93OAE';

       String accountId = '001D2000002pkXwIAI';

       String primaryResourceId = '0HnD20000004C9bKAE';

       String workTypeId = '08qD20000004C9XIAU';

       String correlationId = 'SOME_ID';

       lxscheduler.ServiceAppointmentRequestInfo mockRequestInfo = new

   lxscheduler.ServiceAppointmentRequestInfo(startDate, endDate, serviceResources,

                                           schedulingPolicyId,

   workTypeGroupId, accountId,

                                           primaryResourceId,

   workTypeId, correlationId);

       ServiceResourceScheduleHandlerImpl.getUnavailableTimeslots(mockRequestInfo);

     }

   }

### ServiceAppointmentRequestInfo Class

```

Represents the list of parameters that are passed to the ServiceResourceScheduleHandler interface. This class is implemented internally
by Apex.

Namespace

LxScheduler

IN THIS SECTION:

ServiceAppointmentRequestInfo Constructors


Apex Reference Guide ServiceAppointmentRequestInfo Class

ServiceAppointmentRequestInfo Methods

#### ServiceAppointmentRequestInfo Constructors The following are constructors for ServiceAppointmentRequestInfo .

IN THIS SECTION:

##### ServiceAppointmentRequestInfo(startDate, endDate, ServiceResources, SchedulingPolicyId, workTypeGroupId, accountId,

primaryResourceId, workTypeId, correlationId)
Creates a new instance of the `lxscheduler.ServiceAppointmentRequestInfo` class using the specified start date,
end date, service resources, scheduling policy, work type group, accound ID, primary resource, work type, and correlation.

##### **`ServiceAppointmentRequestInfo(startDate, endDate, ServiceResources,`**

```
  SchedulingPolicyId, workTypeGroupId, accountId, primaryResourceId, workTypeId,

  correlationId)

```

Creates a new instance of the `lxscheduler.ServiceAppointmentRequestInfo` class using the specified start date, end
date, service resources, scheduling policy, work type group, accound ID, primary resource, work type, and correlation.

Signature

```
   public ServiceAppointmentRequestInfo(Datetime startDate, Datetime endDate,

   List<lxscheduler.ServiceResourceInfo> ServiceResources, String SchedulingPolicyId,

   String workTypeGroupId, String accountId, String primaryResourceId, String workTypeId,

   String correlationId)

```

Parameters

```
   startDate
```

Type: Datetime

The start date and time for which unavailable time slots are requested.

```
   endDate
```

Type: Datetime

The end date and time for which unavailable time slots are requested.

```
   ServiceResources
```

Type: List<lxscheduler.ServiceResourceInfo>

The list of requested service resources for the unavailable time slots.

```
   SchedulingPolicyId
```

Type: String

The ID of the scheduling policy .

```
   workTypeGroupId
```

Type: String

The work type group ID.

```
   accountId
```

Type: String


Apex Reference Guide ServiceAppointmentRequestInfo Class

The account ID of an existing user.

```
   primaryResourceId
```

Type: String

The ID of the primary service resource.

```
   workTypeId
```

Type: String

The work type ID.

```
   correlationId
```

Type: String

A unique identifier for a service appointment request.

#### ServiceAppointmentRequestInfo Methods The following are methods for ServiceAppointmentRequestInfo .

IN THIS SECTION:

##### getAccountId()

Returns the account ID of the customer if the API request contains one.

getCorrelationId()
Returns a unique identifier for a request.

getEndDate()
Returns the end date and time for which unavailable time slots are requested.

getPrimaryResourceId()
Returns the ID of the primary service resource.

getSchedulingPolicyId()
Returns the ID of the scheduling policy that the API request contains.

getServiceResources()
Returns the list of requested service resources for the unavailable time slots.

getStartDate()
Returns the start date and time for which unavailable time slots are requested.

getWorkTypeGroupId()
Returns the work type group ID if the API request contains one.

getWorkTypeId()
Returns the work type ID if the API request contains one.

##### getAccountId()

Returns the account ID of the customer if the API request contains one.

Signature

```
   public String getAccountId()

```


Apex Reference Guide ServiceAppointmentRequestInfo Class

Return Value

Type: String

##### getCorrelationId()

Returns a unique identifier for a request.

Signature

```
   public String getCorrelationId()

```

Return Value

Type: String

##### getEndDate()

Returns the end date and time for which unavailable time slots are requested.

Signature

```
   public Datetime getEndDate()

```

Return Value

Type: Datetime

##### getPrimaryResourceId()

Returns the ID of the primary service resource.

Signature

```
   public String getPrimaryResourceId()

```

Return Value

Type: String

##### getSchedulingPolicyId()

Returns the ID of the scheduling policy that the API request contains.

Signature

```
   public String getSchedulingPolicyId()

```

Return Value

Type: String


### Apex Reference Guide ServiceResourceInfo Class

##### getServiceResources()

Returns the list of requested service resources for the unavailable time slots.

Signature

```
   public List<lxscheduler.ServiceResourceInfo> getServiceResources()

```

Return Value

Type: List<lxscheduler.ServiceResourceInfo>

##### getStartDate()

Returns the start date and time for which unavailable time slots are requested.

Signature

```
   public Datetime getStartDate()

```

Return Value

Type: Datetime

##### getWorkTypeGroupId()

Returns the work type group ID if the API request contains one.

Signature

```
   public String getWorkTypeGroupId()

```

Return Value

Type: String

##### getWorkTypeId()

Returns the work type ID if the API request contains one.

Signature

```
   public String getWorkTypeId()

```

Return Value

Type: String

### ServiceResourceInfo Class

Contains information about a service resource.


Apex Reference Guide ServiceResourceInfo Class

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceInfo Constructors

ServiceResourceInfo Methods

#### ServiceResourceInfo Constructors The following are constructors for ServiceResourceInfo .

IN THIS SECTION:

##### ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds, resourceType)

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.

##### **`ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds,`**

```
  resourceType)

```

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.

Signature

```
   public ServiceResourceInfo(String userId, String userName, String email, String

   serviceResourceId, List<String> territoryIds, String resourceType)

```

Parameters

```
   userId
```

Type: String

The user ID of the service resource.

```
   userName
```

Type: String

The user name of the service resource.

```
   email
```

Type: String

The email ID of the service resource.

```
   serviceResourceId
```

Type: String

The ID of the service resource.

```
   territoryIds
```

Type: List<String>

A list of requested service territories for the service resource.


Apex Reference Guide ServiceResourceInfo Class

```
   resourceType
```

Type: String

The type of the service resource such as Technician or Asset.

#### ServiceResourceInfo Methods The following are methods for ServiceResourceInfo .

IN THIS SECTION:

##### getEmail()

Returns the email ID of the service resource.

##### getResourceType()

Returns the type of the service resource such as Technician or Asset.

getServiceResourceId()
Returns the ID of the service resource.

getTerritoryIds()
Returns a list of requested service territories for the service resource.

getUserId()
Returns the user ID of the service resource.

getUserName()
Returns the user name of the service resource.

##### getEmail()

Returns the email ID of the service resource.

Signature

```
   public String getEmail()

```

Return Value

Type: String

##### getResourceType()

Returns the type of the service resource such as Technician or Asset.

Signature

```
   public String getResourceType()

```

Return Value

Type: String


### Apex Reference Guide ServiceResourceSchedule Class

##### getServiceResourceId()

Returns the ID of the service resource.

Signature

```
   public String getServiceResourceId()

```

Return Value

Type: String

##### getTerritoryIds()

Returns a list of requested service territories for the service resource.

Signature

```
   public List<String> getTerritoryIds()

```

Return Value

Type: List<String>

##### getUserId()

Returns the user ID of the service resource.

Signature

```
   public String getUserId()

```

Return Value

Type: String

##### getUserName()

Returns the user name of the service resource.

Signature

```
   public String getUserName()

```

Return Value

Type: String

### ServiceResourceSchedule Class

Use this class to pass results from your implemented Apex class to the ServiceResourceScheduleHandler interface methods.


Apex Reference Guide ServiceResourceSchedule Class

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceSchedule Constructors ServiceResourceSchedule Properties ServiceResourceSchedule Constructors The following are constructors for ServiceResourceSchedule .

IN THIS SECTION:

##### ServiceResourceSchedule(serviceResourceId, unavailableTimeslots)

Creates a new instance of lxscheduler.ServiceResourceSchedule class.

##### ServiceResourceSchedule(serviceResourceId, unavailableTimeslots)

Creates a new instance of lxscheduler.ServiceResourceSchedule class.

Signature

```
   public ServiceResourceSchedule(String serviceResourceId,

   Set<lxscheduler.UnavailableTimeslot> unavailableTimeslots)

```

Parameters

```
   serviceResourceId
```

Type: String

Record ID of the service resource.

```
   unavailableTimeslots
```

Type: Set<lxscheduler.UnavailableTimeslot>

An instance of lxscheduler.UnavailableTimeslot class.

#### ServiceResourceSchedule Properties The following are properties for ServiceResourceSchedule .

IN THIS SECTION:

serviceResourceId
Record ID of the service resource.

unavailableTimeslots
An instance of lxscheduler.UnavailableTimeslot class.


### Apex Reference Guide UnavailableTimeslot Class

##### serviceResourceId

Record ID of the service resource.

Signature

```
   public String serviceResourceId {get; set;}

```

Property Value

Type: String

##### unavailableTimeslots

An instance of lxscheduler.UnavailableTimeslot class.

Signature

```
   public Set<lxscheduler.UnavailableTimeslot> unavailableTimeslots {get; set;}

```

Property Value

Type: Set<lxscheduler.UnavailableTimeslot>

### UnavailableTimeslot Class

Use this class to pass the unavailable time slots to the lxscheduler.ServiceResourceSchedule class. Timezones that differ across operating
hours are handled and results are always returned in UTC.

Namespace

LxScheduler

IN THIS SECTION:

#### UnavailableTimeslot Constructors

UnavailableTimeslot Properties

#### UnavailableTimeslot Constructors

### The following are constructors for UnavailableTimeslot .

IN THIS SECTION:

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.


Apex Reference Guide UnavailableTimeslot Class

Signature

```
   public UnavailableTimeslot(Datetime timeMin, Datetime timeMax)

```

Parameters

##### _`timeMin`_

Type: Datetime

Start time of an unavailable time slot.

##### _`timeMax`_

Type: Datetime

End time of an unavailable time slot.

#### UnavailableTimeslot Properties The following are properties for UnavailableTimeslot .

IN THIS SECTION:

##### timeMax

End time of an unavailable time slot.

##### timeMin

Start time of an unavailable time slot.

##### timeMax

End time of an unavailable time slot.

Signature

```
   public Datetime timeMax {get; set;}

```

Property Value

Type: Datetime

##### timeMin

Start time of an unavailable time slot.

Signature

```
   public Datetime timeMin {get; set;}

```

Property Value

Type: Datetime


## Apex Reference Guide Messaging Namespace Messaging Namespace The Messaging namespace provides classes and methods for Salesforce outbound and inbound email functionality. The following are the classes in the Messaging namespace.

IN THIS SECTION:

AttachmentRetrievalOption Enum
Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

Email Class (Base Email Methods)
Contains base email methods common to both single and mass email.

EmailFileAttachment Class
EmailFileAttachment is used in SingleEmailMessage to specify attachments passed in as part of the request, as opposed to existing
documents in Salesforce.

InboundEmail Class
Represents an inbound email object.

InboundEmail.AuthenticationResult Class
Contains the authentication type and response for inbound emails.

InboundEmail.AuthenticationResultField Class
Contains field data from the authentication result response for inbound emails.

InboundEmail.BinaryAttachment Class
An InboundEmail object stores binary attachments in an InboundEmail.BinaryAttachment object.

InboundEmail.TextAttachment Class
An InboundEmail object stores text attachments in an InboundEmail.TextAttachment object.

InboundEmailResult Class
The InboundEmailResult object is used to return the result of the email service. If this object is null, the result is assumed to be
successful.

InboundEnvelope Class
The InboundEnvelope object stores the envelope information associated with the inbound email, and has the following fields.

MassEmailMessage Class
Contains methods for sending mass email.

InboundEmail.Header Class
An InboundEmail object stores RFC 2822 email header information in an InboundEmail.Header object with the following properties.

PushNotification Class

`PushNotification` is used to configure push notifications and send them from an Apex trigger.

PushNotificationPayload Class
Contains methods to create the notification message payload for an Apple device.

CustomNotification Class

`CustomNotification` is used to create, configure, and send custom notifications from Apex code.

RenderEmailTemplateBodyResult Class
Contains the results for rendering email templates.


### Apex Reference Guide AttachmentRetrievalOption Enum

RenderEmailTemplateError Class
Represents an error that the `RenderEmailTemplateBodyResult` object can contain.

SendEmailError Class
Represents an error that the SendEmailResult object may contain.

SendEmailResult Class
Contains the result of sending an email message.

SingleEmailMessage Class
Contains methods for sending single email messages.

### AttachmentRetrievalOption Enum

Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

Namespace

Messaging

Usage

Use these enum values with the renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption) method.

Enum Values

The following are the values of the `Messaging.AttachmentRetrievalOption` enum.

**Value** **Description**

`METADATA_ONLY` Includes only the file name, content type, and the object ID in the
`fileAttachments` property of `Messaging.SingleEmailMessage` .

Note: When the template is rendered from a Visualforce template (and not
from a static file attached to the template), the object ID is not available.

```
METADATA_WITH_BODY

```

Includes the attachment content, in addition to the file name, content type, and
the object ID in the `fileAttachments` property of
`Messaging.SingleEmailMessage` .

`NONE` Doesn’t include any attachments in `Messaging.SingleEmailMessage` .

### Email Class (Base Email Methods)

Contains base email methods common to both single and mass email.

Namespace

Messaging


Apex Reference Guide Email Class (Base Email Methods)

Usage

Note: If templates are not being used, all email content must be in plain text, HTML, or both.Visualforce email templates cannot
be used for mass email.

#### Email Methods The following are methods for Email . All are instance methods.

IN THIS SECTION:

##### setBccSender(bcc)

Indicates whether the email sender receives a copy of the email that is sent. For a mass mail, the sender is only copied on the first
email sent.

setReplyTo(replyAddress)
Optional. The email address that receives the message when a recipient replies.

setTemplateID(templateId)
The ID of the template to be merged to create this email. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

setSaveAsActivity(saveAsActivity)
Optional. The default value is `true`, meaning the email is saved as an activity. This argument only applies if the recipient list is based
on `targetObjectId` or `targetObjectIds` . If HTML email tracking is enabled for the organization, you will be able to track
open rates.

setSenderDisplayName(displayName)
Optional. The name that appears on the From line of the email. This cannot be set if the object associated with a
`setOrgWideEmailAddressId` for a SingleEmailMessage has defined its `DisplayName` field.

setUseSignature(useSignature)
Indicates whether the email includes an email signature if the user has one configured. The default is `true`, meaning if the user
has a signature it is included in the email unless you specify `false` .

##### setBccSender(bcc)

Indicates whether the email sender receives a copy of the email that is sent. For a mass mail, the sender is only copied on the first email
sent.

Signature

```
   public Void setBccSender(Boolean bcc)

```

Parameters

```
   bcc
```

Type: Boolean

Return Value

Type: Void


Apex Reference Guide Email Class (Base Email Methods)

Usage

Note: If the BCC compliance option is set at the organization level, the user cannot add BCC addresses on standard messages.
The following error code is returned: `BCC_NOT_ALLOWED_IF_BCC_ COMPLIANCE_ENABLED` . Contact your Salesforce
representative for information on BCC compliance.

##### setReplyTo(replyAddress)

Optional. The email address that receives the message when a recipient replies.

Signature

```
   public Void setReplyTo(String replyAddress)

```

Parameters

```
   replyAddress
```

Type: String

Return Value

Type: Void

##### setTemplateID(templateId)

The ID of the template to be merged to create this email. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

Signature

```
   public Void setTemplateID(ID templateId)

```

Parameters

```
   templateId
```

Type: ID

Return Value

Type: Void

Usage

Note: `setHtmlBody` and `setPlainTextBody` apply only to single email methods, not to mass email methods.

##### setSaveAsActivity(saveAsActivity)

Optional. The default value is `true`, meaning the email is saved as an activity. This argument only applies if the recipient list is based
on `targetObjectId` or `targetObjectIds` . If HTML email tracking is enabled for the organization, you will be able to track
open rates.


Apex Reference Guide Email Class (Base Email Methods)

Signature

```
   public Void setSaveAsActivity(Boolean saveAsActivity)

```

Parameters

```
   saveAsActivity
```

Type: Boolean

Return Value

Type: Void

##### setSenderDisplayName(displayName)

Optional. The name that appears on the From line of the email. This cannot be set if the object associated with a
`setOrgWideEmailAddressId` for a SingleEmailMessage has defined its `DisplayName` field.

Signature

```
   public Void setSenderDisplayName(String displayName)

```

Parameters

```
   displayName
```

Type: String

Return Value

Type: Void

##### setUseSignature(useSignature)

Indicates whether the email includes an email signature if the user has one configured. The default is `true`, meaning if the user has a
signature it is included in the email unless you specify `false` .

Signature

```
   public Void setUseSignature(Boolean useSignature)

```

Parameters

```
   useSignature
```

Type: Boolean

Return Value

Type: Void


### Apex Reference Guide EmailFileAttachment Class EmailFileAttachment Class

EmailFileAttachment is used in SingleEmailMessage to specify attachments passed in as part of the request, as opposed to existing
documents in Salesforce.

Namespace

Messaging

IN THIS SECTION:

#### EmailFileAttachment Constructors EmailFileAttachment Properties EmailFileAttachment Constructors

### The following are constructors for EmailFileAttachment .

IN THIS SECTION:

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

Signature

```
   public EmailFileAttachment()

#### EmailFileAttachment Properties

### The following are properties for EmailFileAttachment .

```

IN THIS SECTION:

body
Gets or sets the attachment itself.

contenttype
Gets or sets the attachment's Content-Type.

filename
Gets or sets the name of the file to attach.

id
Read-Only. Gets the attachment ID.

inline
Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).


Apex Reference Guide EmailFileAttachment Class

##### body

Gets or sets the attachment itself.

Signature

```
   public Blob body {get; set;}

```

Property Value

Type: Blob

##### contenttype

Gets or sets the attachment's Content-Type.

Signature

```
   public String contenttype {get; set;}

```

Property Value

Type: String

##### filename

Gets or sets the name of the file to attach.

Signature

```
   public String filename {get; set;}

```

Property Value

Type: String

##### id

Read-Only. Gets the attachment ID.

Signature

```
   public Id id {get;}

```

Property Value

Type: Id

##### inline

Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).


### Apex Reference Guide InboundEmail Class

Signature

```
   public Boolean inline {get; set;}

```

Property Value

Type: Boolean

### InboundEmail Class

Represents an inbound email object.

Namespace

Messaging

IN THIS SECTION:

#### InboundEmail Constructors InboundEmail Properties InboundEmail Constructors

### The following are constructors for InboundEmail .

IN THIS SECTION:

##### InboundEmail()

Creates a new instance of the `Messaging.InboundEmail` class.

##### InboundEmail()

Creates a new instance of the `Messaging.InboundEmail` class.

Signature

```
   public InboundEmail()

#### InboundEmail Properties

### The following are properties for InboundEmail .

```

IN THIS SECTION:

authenticationResults
A list of authentication results received with the email, if any.

binaryAttachments
A list of binary attachments received with the email, if any.


Apex Reference Guide InboundEmail Class

ccAddresses
A list of carbon copy (CC) addresses, if any.

fromAddress
The email address that appears in the From field.

fromName
The name that appears in the From field, if any.

headers
A list of the RFC 2822 headers in the email.

htmlBody
The HTML version of the email, if specified by the sender.

htmlBodyIsTruncated
Indicates whether the HTML body text is truncated ( `true` ) or not ( `false` .)

inReplyTo
The In-Reply-To field of the incoming email. Identifies the email or emails to which this one is a reply (parent emails). Contains the
parent email or emails' message-IDs.

messageId
The Message-ID—the incoming email's unique identifier.

plainTextBody
The plain text version of the email, if specified by the sender.

plainTextBodyIsTruncated
Indicates whether the plain body text is truncated ( `true` ) or not ( `false` .)

references
The References field of the incoming email. Identifies an email thread. Contains a list of the parent emails' References and message
IDs, and possibly the In-Reply-To fields.

replyTo
The email address that appears in the reply-to header.

subject
The subject line of the email, if any.

textAttachments
A list of text attachments received with the email, if any.

toAddresses
The email address that appears in the `To` field.

##### **`authenticationResults`**

A list of authentication results received with the email, if any.

Signature

```
   public InboundEmail.AuthenticationResult[] authenticationResults {get; set;}

```


Apex Reference Guide InboundEmail Class

Property Value

Type: InboundEmail.AuthenticationResult[]

Usage

Examples of authentication results include `dkim`, `dmarc`, and `spf` .

##### binaryAttachments

A list of binary attachments received with the email, if any.

Signature

```
   public InboundEmail.BinaryAttachment[] binaryAttachments {get; set;}

```

Property Value

Type: InboundEmail.BinaryAttachment[]

Usage

Examples of binary attachments include image, audio, application, and video files.

##### ccAddresses

A list of carbon copy (CC) addresses, if any.

Signature

```
   public String[] ccAddresses {get; set;}

```

Property Value

Type: String[]

##### fromAddress

The email address that appears in the From field.

Signature

```
   public String fromAddress {get; set;}

```

Property Value

Type: String

##### fromName

The name that appears in the From field, if any.


Apex Reference Guide InboundEmail Class

Signature

```
   public String fromName {get; set;}

```

Property Value

Type: String

##### headers

A list of the RFC 2822 headers in the email.

Signature

```
   public InboundEmail.Header[] headers {get; set;}

```

Property Value

Type: InboundEmail.Header[]

Usage

The list of the RFC 2822 headers includes:

**•** Recieved from

**•** Custom headers

**•** Message-ID

**•** Date

##### htmlBody

The HTML version of the email, if specified by the sender.

Signature

```
   public String htmlBody {get; set;}

```

Property Value

Type: String

##### htmlBodyIsTruncated

Indicates whether the HTML body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean htmlBodyIsTruncated {get; set;}

```


Apex Reference Guide InboundEmail Class

Property Value

Type: Boolean

##### inReplyTo

The In-Reply-To field of the incoming email. Identifies the email or emails to which this one is a reply (parent emails). Contains the parent
email or emails' message-IDs.

Signature

```
   public String inReplyTo {get; set;}

```

Property Value

Type: String

##### messageId

The Message-ID—the incoming email's unique identifier.

Signature

```
   public String messageId {get; set;}

```

Property Value

Type: String

##### plainTextBody

The plain text version of the email, if specified by the sender.

Signature

```
   public String plainTextBody {get; set;}

```

Property Value

Type: String

##### plainTextBodyIsTruncated

Indicates whether the plain body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean plainTextBodyIsTruncated {get; set;}

```


Apex Reference Guide InboundEmail Class

Property Value

Type: Boolean

##### references

The References field of the incoming email. Identifies an email thread. Contains a list of the parent emails' References and message IDs,
and possibly the In-Reply-To fields.

Signature

```
   public String[] references {get; set;}

```

Property Value

Type: String[]

##### replyTo

The email address that appears in the reply-to header.

Signature

```
   public String replyTo {get; set;}

```

Property Value

Type: String

Usage

If there is no reply-to header, this field is identical to the `fromAddress` field.

##### subject

The subject line of the email, if any.

Signature

```
   public String subject {get; set;}

```

Property Value

Type: String

##### textAttachments

A list of text attachments received with the email, if any.


### Apex Reference Guide InboundEmail.AuthenticationResult Class

Signature

```
   public InboundEmail.TextAttachment[] textAttachments {get; set;}

```

Property Value

Type: InboundEmail.TextAttachment[]

Usage

The text attachments can be any of the following:

**•** Attachments with a Multipurpose Internet Mail Extension (MIME) type of `text`

**•** Attachments with a MIME type of `application/octet-stream` and a file name that ends with either a `.vcf` or `.vcs`
extension. These are saved as `text/x-vcard` and `text/calendar` MIME types, respectively.

##### toAddresses

The email address that appears in the `To` field.

Signature

```
   public String[] toAddresses {get; set;}

```

Property Value

Type: String[]

### InboundEmail.AuthenticationResult Class

Contains the authentication type and response for inbound emails.

Namespace

Messaging

IN THIS SECTION:

#### InboundEmail.AuthenticationResult Constructors

InboundEmail.AuthenticationResult Properties

#### InboundEmail.AuthenticationResult Constructors

### The following are constructors for InboundEmail.AuthenticationResult .

IN THIS SECTION:

InboundEmail.AuthenticationResult()
Creates a new instance of the `Messaging.InboundEmail.AuthenticationResult` class.


Apex Reference Guide InboundEmail.AuthenticationResult Class

##### InboundEmail.AuthenticationResult()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResult` class.

Signature

```
   public InboundEmail.AuthenticationResult()

#### InboundEmail.AuthenticationResult Properties

##### The following are properties for InboundEmail.AuthenticationResult .

```

IN THIS SECTION:

##### authenticationResultFields

Additional information in authentication result headers. Examples include: `name: smtp.mailfrom` and `value:`
`example.com` .

##### method

The authentication method used for the security check. Possible values include `dkim`, `dmarc`, or `spf` .

result
The result of the authentication check. When the email service is configured to verify the legitimacy of the sending server before
processing a message, possible values include `pass` or `fail` . Otherwise, the value returned is `none` .

##### **`authenticationResultFields`**

Additional information in authentication result headers. Examples include: `name: smtp.mailfrom` and `value: example.com` .

Signature

```
   public InboundEmail.AuthenticationResultField[] authenticationResultFields {get; set;}

```

Property Value

Type: InboundEmail.AuthenticationResultField[]

##### **`method`**

The authentication method used for the security check. Possible values include `dkim`, `dmarc`, or `spf` .

Signature

```
   public String method {get; set;}

```

Property Value

Type: String


### Apex Reference Guide InboundEmail.AuthenticationResultField Class

##### **`result`**

The result of the authentication check. When the email service is configured to verify the legitimacy of the sending server before processing
a message, possible values include `pass` or `fail` . Otherwise, the value returned is `none` .

Signature

```
   public String result {get; set;}

```

Property Value

Type: String

### InboundEmail.AuthenticationResultField Class

Contains field data from the authentication result response for inbound emails.

Namespace

Messaging

IN THIS SECTION:

#### InboundEmail.AuthenticationResultField Constructors InboundEmail.AuthenticationResultField Properties InboundEmail.AuthenticationResultField Constructors

### The following are constructors for InboundEmail.AuthenticationResultField .

IN THIS SECTION:

##### InboundEmail.AuthenticationResultField()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResultField` class.

##### InboundEmail.AuthenticationResultField()

Creates a new instance of the `Messaging.InboundEmail.AuthenticationResultField` class.

Signature

```
   public InboundEmail.AuthenticationResultField()

#### InboundEmail.AuthenticationResultField Properties

### The following are properties for InboundEmail.AuthenticationResultField .

```


### Apex Reference Guide InboundEmail.BinaryAttachment Class

IN THIS SECTION:

##### name

The authentication result field name. For example: `smtp.mailfrom` .

##### value

The authentication result field value. For example: `example.com` .

##### **`name`**

The authentication result field name. For example: `smtp.mailfrom` .

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`value`**

The authentication result field value. For example: `example.com` .

Signature

```
   public String value {get; set;}

```

Property Value

Type: String

### InboundEmail.BinaryAttachment Class

An InboundEmail object stores binary attachments in an InboundEmail.BinaryAttachment object.

Namespace

Messaging

Usage

Examples of binary attachments include image, audio, application, and video files.

IN THIS SECTION:

InboundEmail.BinaryAttachment Constructors

InboundEmail.BinaryAttachment Properties


Apex Reference Guide InboundEmail.BinaryAttachment Class

#### InboundEmail.BinaryAttachment Constructors The following are constructors for InboundEmail.BinaryAttachment .

IN THIS SECTION:

##### InboundEmail.BinaryAttachment()

Creates a new instance of the `Messaging.InboundEmail.BinaryAttachment` class.

##### InboundEmail.BinaryAttachment()

Creates a new instance of the `Messaging.InboundEmail.BinaryAttachment` class.

Signature

```
   public InboundEmail.BinaryAttachment()

#### InboundEmail.BinaryAttachment Properties The following are properties for InboundEmail.BinaryAttachment .

```

IN THIS SECTION:

##### body

The body of the attachment.

##### fileName

The name of the attached file.

headers
Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

mimeTypeSubType
The primary and sub MIME-type.

##### body

The body of the attachment.

Signature

```
   public Blob body {get; set;}

```

Property Value

Type: Blob

##### fileName

The name of the attached file.


### Apex Reference Guide InboundEmail.TextAttachment Class

Signature

```
   public String fileName {get; set;}

```

Property Value

Type: String

##### headers

Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

Signature

```
   public List<Messaging.InboundEmail.Header> headers {get; set;}

```

Property Value

Type: List<Messaging.InboundEmail.Header>

##### mimeTypeSubType

The primary and sub MIME-type.

Signature

```
   public String mimeTypeSubType {get; set;}

```

Property Value

Type: String

### InboundEmail.TextAttachment Class

An InboundEmail object stores text attachments in an InboundEmail.TextAttachment object.

Namespace

Messaging

Usage

The text attachments can be any of the following:

**•** Attachments with a Multipurpose Internet Mail Extension (MIME) type of `text`

**•** Attachments with a MIME type of `application/octet-stream` and a file name that ends with either a `.vcf` or `.vcs`
extension. These are saved as `text/x-vcard` and `text/calendar` MIME types, respectively.


Apex Reference Guide InboundEmail.TextAttachment Class

IN THIS SECTION:

#### InboundEmail.TextAttachment Constructors InboundEmail.TextAttachment Properties InboundEmail.TextAttachment Constructors The following are constructors for InboundEmail.TextAttachment .

IN THIS SECTION:

##### InboundEmail.TextAttachment()

Creates a new instance of the `Messaging.InboundEmail.TextAttachment` class.

##### InboundEmail.TextAttachment()

Creates a new instance of the `Messaging.InboundEmail.TextAttachment` class.

Signature

```
   public InboundEmail.TextAttachment()

#### InboundEmail.TextAttachment Properties The following are properties for InboundEmail.TextAttachment .

```

IN THIS SECTION:

##### body

The body of the attachment.

##### bodyIsTruncated

Indicates whether the attachment body text is truncated ( `true` ) or not ( `false` .)

charset
The original character set of the body field. The body is re-encoded as UTF-8 as input to the Apex method.

fileName
The name of the attached file.

headers
Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .

mimeTypeSubType
The primary and sub MIME-type.

##### body

The body of the attachment.


Apex Reference Guide InboundEmail.TextAttachment Class

Signature

```
   public String body {get; set;}

```

Property Value

Type: String

##### bodyIsTruncated

Indicates whether the attachment body text is truncated ( `true` ) or not ( `false` .)

Signature

```
   public Boolean bodyIsTruncated {get; set;}

```

Property Value

Type: Boolean

##### charset

The original character set of the body field. The body is re-encoded as UTF-8 as input to the Apex method.

Signature

```
   public String charset {get; set;}

```

Property Value

Type: String

##### fileName

The name of the attached file.

Signature

```
   public String fileName {get; set;}

```

Property Value

Type: String

##### headers

Any header values associated with the attachment. Examples of header names include `Content-Type`,
`Content-Transfer-Encoding`, and `Content-ID` .


### Apex Reference Guide InboundEmailResult Class

Signature

```
   public List<Messaging.InboundEmail.Header> headers {get; set;}

```

Property Value

Type: List<Messaging.InboundEmail.Header>

##### mimeTypeSubType

The primary and sub MIME-type.

Signature

```
   public String mimeTypeSubType {get; set;}

```

Property Value

Type: String

### InboundEmailResult Class

The InboundEmailResult object is used to return the result of the email service. If this object is null, the result is assumed to be successful.

Namespace

Messaging

#### InboundEmailResult Properties

### The following are properties for InboundEmailResult .

IN THIS SECTION:

##### message

A message that Salesforce returns in the body of a reply email. This field can be populated with text irrespective of the value returned
by the `Success` field.

success
A value that indicates whether the email was successfully processed.

##### message

A message that Salesforce returns in the body of a reply email. This field can be populated with text irrespective of the value returned
by the `Success` field.

Signature

```
   public String message {get; set;}

```


### Apex Reference Guide InboundEnvelope Class

Property Value

Type: String

##### success

A value that indicates whether the email was successfully processed.

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

Usage

If `false`, Salesforce rejects the inbound email and sends a reply email to the original sender containing the message specified in the
`Message` field.

### InboundEnvelope Class

The InboundEnvelope object stores the envelope information associated with the inbound email, and has the following fields.

Namespace

Messaging

#### InboundEnvelope Properties

### The following are properties for InboundEnvelope .

IN THIS SECTION:

##### fromAddress

The name that appears in the `From` field of the envelope, if any.

toAddress
The name that appears in the `To` field of the envelope, if any.

##### fromAddress

The name that appears in the `From` field of the envelope, if any.

Signature

```
   public String fromAddress {get; set;}

```


### Apex Reference Guide MassEmailMessage Class

Property Value

Type: String

##### toAddress

The name that appears in the `To` field of the envelope, if any.

Signature

```
   public String toAddress {get; set;}

```

Property Value

Type: String

### MassEmailMessage Class

Contains methods for sending mass email.

Namespace

Messaging

Usage

MassEmailMessage extends Email and inherits all of its methods. All base email ( `Email` class) methods are also available to the
### MassEmailMessage objects.

IN THIS SECTION:

#### MassEmailMessage Constructors

MassEmailMessage Methods

SEE ALSO:

Email Class (Base Email Methods)

#### MassEmailMessage Constructors

### The following are constructors for MassEmailMessage .

IN THIS SECTION:

##### MassEmailMessage()

Creates a new instance of the `Messaging.MassEmailMessage` class.

##### MassEmailMessage()

Creates a new instance of the `Messaging.MassEmailMessage` class.


Apex Reference Guide MassEmailMessage Class

Signature

```
   public MassEmailMessage()

#### MassEmailMessage Methods The following are methods for MassEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the MassEmailMessage objects. These methods are described in Email Class (Base Email Methods).

```

IN THIS SECTION:

##### setDescription(description)

The description of the email.

##### setTargetObjectIds(targetObjectIds)

A list of IDs of the contacts, leads, or users to which the email will be sent. The IDs you specify set the context and ensure that merge
fields in the template contain the correct data. The objects must be of the same type (all contacts, all leads, or all users).

setWhatIds(whatIds)
Optional. If you specify a list of contacts for the `targetObjectIds` field, you can specify a list of `whatIds` as well. This helps
to further ensure that merge fields in the template contain the correct data.

##### setDescription(description)

The description of the email.

Signature

```
   public Void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: Void

##### setTargetObjectIds(targetObjectIds)

A list of IDs of the contacts, leads, or users to which the email will be sent. The IDs you specify set the context and ensure that merge
fields in the template contain the correct data. The objects must be of the same type (all contacts, all leads, or all users).

Signature

```
   public Void setTargetObjectIds(ID[] targetObjectIds)

```

Parameters

```
   targetObjectIds
```

Type: ID[]


### Apex Reference Guide InboundEmail.Header Class

Return Value

Type: Void

Usage

You can list multiple IDs per email. If you specify a value for the `targetObjectIds` field, optionally specify a `whatId` as well to
set the email context to a user, contact, or lead. This ensures that merge fields in the template contain the correct data. Each ID counts
against the sending organization's daily mass email limit.

Do not specify the IDs of records that have the `Email Opt Out` option selected.

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setWhatIds(whatIds)

Optional. If you specify a list of contacts for the `targetObjectIds` field, you can specify a list of `whatIds` as well. This helps to
further ensure that merge fields in the template contain the correct data.

Signature

```
   public Void setWhatIds(ID[] whatIds)

```

Parameters

```
   whatIds
```

Type: ID[]

Return Value

Type: Void

Usage

The values must be one of the following types:

**•** Contract

**•** Case

**•** Opportunity

**•** Product

Note: If you specify `whatIds`, specify one for each `targetObjectId` ; otherwise, you will receive an `INVALID_ID_FIELD`
error.

### InboundEmail.Header Class

An InboundEmail object stores RFC 2822 email header information in an InboundEmail.Header object with the following properties.


### Apex Reference Guide PushNotification Class

Namespace

Messaging

#### InboundEmail.Header Properties The following are properties for InboundEmail.Header .

IN THIS SECTION:

##### name

The name of the header parameter, such as `Date` or `Message-ID` .

##### value

The value of the header.

##### name

The name of the header parameter, such as `Date` or `Message-ID` .

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### value

The value of the header.

Signature

```
   public String value {get; set;}

```

Property Value

Type: String

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound_what_is.htm)_ : Apex Email Service

_Apex Developer Guide_ [: Using the InboundEmail Object](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound_using.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_email_inbound.htm)_ : Inbound Email

_[Internet Engineering Task Force (IETF) Data Tracker](https://datatracker.ietf.org/doc/html/rfc2822#section-3.6)_ : RFC 2822 Section 3.6

### PushNotification Class PushNotification is used to configure push notifications and send them from an Apex trigger.


Apex Reference Guide PushNotification Class

Namespace

Messaging

Example

This sample Apex trigger sends push notifications to the external client app named _`Test_App`_, which corresponds to a mobile app
on iOS mobile clients. The trigger fires after cases have been updated and sends the push notification to two users: the case owner and
the user who last modified the case.

```
   trigger caseAlert on Case (after update) {

      for(Case cs : Trigger.New)

      {

        // Instantiating a notification

        Messaging.PushNotification msg =

           new Messaging.PushNotification();

        // Assembling the necessary payload parameters for Apple.

        // Apple params are:

        // (<alert text>,<alert sound>,<badge count>,

        // <free-form data>)

        // This example doesn't use badge count or free-form data.

        // The number of notifications that haven't been acted

        // upon by the intended recipient is best calculated

        // at the time of the push. This timing helps

        // ensure accuracy across multiple target devices.

        Map<String, Object> payload =

           Messaging.PushNotificationPayload.apple(

             'Case ' + cs.CaseNumber + ' status changed to: '

             + cs.Status, '', null, null);

        // Adding the assembled payload to the notification

        msg.setPayload(payload);

        // Getting recipient users

        String userId1 = cs.OwnerId;

        String userId2 = cs.LastModifiedById;

        // Adding recipient users to list

        Set<String> users = new Set<String>();

        users.add(userId1);

        users.add(userId2);

        // Sending the notification to the specified app and users.

        // Here we specify the API name of the external client app.

        msg.send('Test_App', users);

      }

   }

```

IN THIS SECTION:

PushNotification Constructors


Apex Reference Guide PushNotification Class

#### PushNotification Methods PushNotification Constructors The following are the constructors for PushNotification .

IN THIS SECTION:

##### PushNotification()

Creates a new instance of the `Messaging.PushNotification` class.

##### PushNotification(payload)

Creates a new instance of the `Messaging.PushNotification` class using the specified payload parameters as key-value
pairs. When you use this constructor, you don’t need to call `setPayload` to set the payload.

##### PushNotification()

Creates a new instance of the `Messaging.PushNotification` class.

Signature

```
   public PushNotification()

##### PushNotification(payload)

```

Creates a new instance of the `Messaging.PushNotification` class using the specified payload parameters as key-value pairs.
When you use this constructor, you don’t need to call `setPayload` to set the payload.

Signature

```
   public PushNotification(Map<String,Object> payload )

```

Parameters

```
   payload
```

Type:Map<String, Object>

The payload, expressed as a map of key-value pairs.

#### PushNotification Methods The following are the methods for PushNotification . All are global methods.

IN THIS SECTION:

send(application, users)
Sends a push notification message to the specified users.

setPayload(payload)
Sets the payload of the push notification message.


Apex Reference Guide PushNotification Class

##### setTtl(ttl)

Reserved for future use.

##### send(application, users)

Sends a push notification message to the specified users.

Signature

```
   public void send(String application, Set<String> users)

```

Parameters

```
   application
```

Type: String

The connected app API name. This corresponds to the mobile client app the notification should be sent to.

```
   users
```

Type: Set

A set of user IDs that correspond to the users the notification should be sent to.

Example

See the Push Notification Example.

##### setPayload(payload)

Sets the payload of the push notification message.

Signature

```
   public void setPayload(Map<String,Object> payload)

```

Parameters

```
   payload
```

Type: Map<String, Object>

The payload, expressed as a map of key-value pairs.

Payload parameters can be different for each mobile OS vendor. For more information on Apple’s payload parameters, search for
[“Apple Push Notification Service” at https://developer.apple.com/library/mac/documentation/.](https://developer.apple.com/library/mac/documentation)

To create the payload for an Apple device, see the PushNotificationPayload Class.

Example

See the Push Notification Example.

##### setTtl(ttl)

Reserved for future use.


### Apex Reference Guide PushNotificationPayload Class

Signature

```
   public void setTtl(Integer ttl)

```

Parameters

```
   ttl
```

Type: Integer

Reserved for future use.

### PushNotificationPayload Class

Contains methods to create the notification message payload for an Apple device.

Namespace

Messaging

Usage

Apple has specific requirements for the notification payload. and this class has helper methods to create the payload. For more information
[on Apple’s payload parameters, search for “Apple Push Notification Service” at https://developer.apple.com/library/mac/documentation/.](https://developer.apple.com/library/mac/documentation/)

Example

See the Push Notification Example.

IN THIS SECTION:

#### PushNotificationPayload Methods PushNotificationPayload Methods

### The following are the methods for PushNotificationPayload . All are global static methods.

IN THIS SECTION:

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

apple(alertBody, actionLocKey, locKey, locArgs, launchImage, sound, badgeCount, userData)
Helper method that creates a valid Apple payload from the specified arguments.

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.


Apex Reference Guide PushNotificationPayload Class

Signature

```
   public static Map<String,Object> apple(String alert, String sound, Integer badgeCount,

   Map<String,Object> userData)

```

Parameters

```
   alert
```

Type: String

Notification message to be sent to the mobile client.

```
   sound
```

Type: String

Name of a sound file to be played as an alert. This sound file should be in the mobile application bundle.

```
   badgeCount
```

Type: Integer

Number to display as the badge of the application icon.

```
   userData
```

Type: Map<String, Object>

Map of key-value pairs that contains any additional data used to provide context for the notification. For example, it can contain IDs
of the records that caused the notification to be sent. The mobile client app can use these IDs to display these records.

Return Value

Type:Map<String, Object>

Returns a formatted payload that includes all of the specified arguments.

Usage

To generate a valid payload, you must provide a value for at least one of the following parameters: `alert`, `sound`, `badgeCount` .

Example

See the Push Notification Example.

##### apple(alertBody, actionLocKey, locKey, locArgs, launchImage, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

Signature

```
   public static Map<String,Object> apple(String alertBody, String actionLocKey, String

   locKey, String[] locArgs, String launchImage, String sound, Integer badgeCount,

   Map<String,Object> userData)

```

Parameters

```
   alertBody
```

Type: String


### Apex Reference Guide CustomNotification Class

Text of the alert message.

```
   actionLocKey
```

Type: String

If a value is specified for the _`actionLocKey`_ argument, an alert with two buttons is displayed. The value is a key to get a localized
string in a `Localizable.strings` file to use for the right button’s title.

```
   locKey
```

Type: String

Key to an alert-message string in a `Localizable.strings` file for the current localization.

```
   locArgs
```

Type: List<String>

Variable string values to appear in place of the format specifiers in _`locKey`_ .

```
   launchImage
```

Type: String

File name of an image file in the application bundle.

```
   sound
```

Type: String

Name of a sound file to be played as an alert. This sound file should be in the mobile application bundle.

```
   badgeCount
```

Type: Integer

Number to display as the badge of the application icon.

```
   userData
```

Type: Map<String, Object>

Map of key-value pairs that contains any additional data used to provide context for the notification. For example, it can contain IDs
of the records that caused the notification to be sent. The mobile client app can use these IDs to display these records.

Return Value

Type: Map<String, Object>

Returns a formatted payload that includes all of the specified arguments.

Usage

To generate a valid payload, you must provide a value for at least one of the following parameters: `alert`, `sound`, `badgeCount` .

### CustomNotification Class CustomNotification is used to create, configure, and send custom notifications from Apex code.

Namespace

Messaging


Apex Reference Guide CustomNotification Class

Usage

`CustomNotification` allows two approaches to creating and configuring a custom notification.

**•** Create an instance with the default constructor, and then set notification attributes using the various setter methods.

**•** Create an instance and configure notification parameters at the same time using the parameterized constructor.

Once the custom notification is configured, call `send()` to send the notification.

**Notification Target**

The _notification target_ is used by the receiving client application to navigate to an appropriate record or page when a user responds to
a notification. For example, when a user is notified that a record was updated, responding to the notification can open the relevant
record.

You must specify a target for a notification. The target can be specified using either the `targetID` or the `targetPageRef` attribute.
Neither attribute is required, but if both are omitted, `send()` throws an exception. If there’s no natural target for a notification, set the
`targetID` to a dummy value, such as _`000000000000000AAA`_ . A dummy value prevents the exception, and also prevents
automatic navigation when responding to the notification in the client app.

You can set both `targetID` and `targetPageRef` in the same notification. The client app that receives the notification determines
which target, if any, to use when responding to the notification.

Important: Before Winter ’21 you could set only a target record ( `targetID` ) for a notification. Most client applications expect
to find a `targetID` in the notification payload. If you can’t update a client app to handle notifications that include only a
`targetPageRef`, set the `targetID` to a dummy value.

**Execution Context and Notification Permissions**

By default Apex code executes in system mode, and doesn’t require user permissions to send notifications with `CustomNotification` .
However, if your Apex code runs in a user context—for example, by executing anonymous Apex in the Developer Console—the Send
Custom Notifications user permission is checked, and `send()` fails if you don’t have the required permission.

Example

This example Apex class provides a static method for sending a custom notification to a recipient list. Call this method from a trigger,
flow, or wherever you want to send a custom notification from Apex.

```
   public without sharing class CustomNotificationFromApex {

      public static void notifyUsers(Set<String> recipientsIds, String targetId) {

        // Get the Id for our custom notification type

        CustomNotificationType notificationType =

           [SELECT Id, DeveloperName

           FROM CustomNotificationType

           WHERE DeveloperName='Custom_Notification'];

        // Create a new custom notification

        Messaging.CustomNotification notification = new Messaging.CustomNotification();

        // Set the contents for the notification

        notification.setTitle('Apex Custom Notification');

        notification.setBody('The notifications are coming from INSIDE the Apex!');

        // Set the notification type and target

        notification.setNotificationTypeId(notificationType.Id);

```


Apex Reference Guide CustomNotification Class

```
        notification.setTargetId(targetId);

        // Actually send the notification

        try {

           notification.send(recipientsIds);

        }

        catch (Exception e) {

           System.debug('Problem sending notification: ' + e.getMessage());

        }

      }

   }

```

Note: This example uses a custom notification type with the `DeveloperName` (API name) _`Custom_Notification`_ .
[You can create a custom notification type using Notification Builder in Setup or Tooling API. Then, use your notification type’s](https://help.salesforce.com/s/articleView?id=platform.notif_builder.htm&language=en_US)
`DeveloperName` (API name) in the query to find the ID of the notification type.

`CustomNotification.send()` can throw an exception, which is handled minimally in this example. Add more substantial
error handling to code you plan to use in production.

IN THIS SECTION:

#### CustomNotification Constructors

CustomNotification Methods

SEE ALSO:

_Salesforce Help_ [: Send Custom Notifications](https://help.salesforce.com/articleView?id=notif_builder_custom.htm&language=en_US)

_Actions Developer Guide_ [: Custom Notification Actions](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_action.meta/api_action/actions_obj_custom_notification.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_customnotificationtype.htm)_ : CustomNotificationType

#### CustomNotification Constructors The following are constructors for CustomNotification .

IN THIS SECTION:

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

CustomNotification(typeId, sender, title, body, targetId, targetPageRef)
Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this
constructor, you don’t need to call the various setter methods to define the custom notification attributes.

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

Signature

```
   public CustomNotification()

```


Apex Reference Guide CustomNotification Class

##### CustomNotification(typeId, sender, title, body, targetId, targetPageRef)

Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this constructor,
you don’t need to call the various setter methods to define the custom notification attributes.

Signature

```
   public CustomNotification(String typeId, String sender, String title, String body,

   String targetId, String targetPageRef)

```

Parameters

```
   typeId
```

Type: String

The ID of the Custom Notification Type being used for the notification.

```
   sender
```

Type: String

The User ID of the sender of the notification.

```
   title
```

Type: String

The title of the notification. Maximum characters: 250.

```
   body
```

Type: String

The body of the notification. Maximum characters: 750.

```
   targetId
```

Type: String

The Record ID for the target record of the notification.

You must specify either a `targetID` or a `targetPageRef` . See Custom Notification Usage.

```
   targetPageRef
```

Type: String

The `PageReference` [for the navigation target of the notification. To see how to specify the target using JSON, see pageReference](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_navigation_page_definitions.htm)
[Types.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_navigation_page_definitions.htm)

You must specify either a `targetID` or a `targetPageRe` . See Custom Notification Usage.

Usage

A client may see a truncated notification title or body depending on the delivery channel or app, and how the Connect API notification
parameters are configured. For more information on the `trimMessages` [query parameter, see Notification .](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_notifications_list.htm)

#### CustomNotification Methods

##### The following are methods for CustomNotification .


Apex Reference Guide CustomNotification Class

IN THIS SECTION:

##### send(users)

Sends a custom notification to the specified users.

setNotificationTypeId(id)
Sets the type of the custom notification.

setTitle(title)
Sets the title of the custom notification.

setBody(body)
Sets the body of the custom notification.

setSenderId(id)
Sets the sender of the custom notification.

setTargetId(targetId)
Sets the target record of the custom notification.

setTargetPageRef(pageRef)
Sets the target page of the custom notification.

##### send(users)

Sends a custom notification to the specified users.

Signature

```
   public void send(Set<String> users)

```

Parameters

```
   users
```

Type: Set<String>

Required. A set of recipient IDs. Each recipient ID corresponds to a recipient or recipient type that the notification should be sent to.
Valid recipient or recipient type values are:

**•** `UserId`     - The notification is sent to this user, if this user is active.

**•** `AccountId`     - The notification is sent to all active users who are members of this account’s Account Team.

Note: This recipient type is valid if account teams are enabled for your org.

**•** `OpportunityId`     - The notification is sent to all active users who are members of this opportunity’s Opportunity Team.

Note: This recipient type is valid if team selling is enabled for your org.

**•** `GroupId`     - The notification is sent to all active users who are members of this group.

**•** `QueueId`     - The notification is sent to all active users who are members of this queue.

Values can be combined in a set, up to the maximum of 500 values.

Return Value

Type: void


Apex Reference Guide CustomNotification Class

Example

See the Custom Notification Example.

##### setNotificationTypeId(id)

Sets the type of the custom notification.

Signature

```
   public void setNotificationTypeId(String id)

```

Parameters

```
   id
```

Type: String

The ID of the Custom Notification Type being used for the notification.

A notification type is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTitle(title)

Sets the title of the custom notification.

Signature

```
   public void setTitle(String title)

```

Parameters

```
   title
```

Type: String

The title of the notification, as it will be seen by recipients. Maximum characters: 250.

A title is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.


Apex Reference Guide CustomNotification Class

##### setBody(body)

Sets the body of the custom notification.

Signature

```
   public void setBody(String body)

```

Parameters

```
   body
```

Type: String

The body of the notification, as it will be seen by recipients. Maximum characters: 750.

A body is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setSenderId(id)

Sets the sender of the custom notification.

Signature

```
   public void setSenderId(String id)

```

Parameters

```
   id
```

Type: String

The User ID of the sender of the notification.

Setting a sender is optional. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTargetId(targetId)

Sets the target record of the custom notification.


### Apex Reference Guide RenderEmailTemplateBodyResult Class

Signature

```
   public void setTargetId(String targetId)

```

Parameters

```
   targetId
```

Type: String

The Record ID for the target record of the notification.

Either a `targetID` or a `targetPageRef` is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

##### setTargetPageRef(pageRef)

Sets the target page of the custom notification.

Signature

```
   public void setTargetPageRef(String pageRef)

```

Parameters

```
   pageRef
```

Type: String

The `PageReference` for the navigation target of the notification.

Either a `targetID` or a `targetPageRef` is required to send a custom notification. See Custom Notification Usage.

Return Value

Type: void

Example

See the Custom Notification Example.

### RenderEmailTemplateBodyResult Class

Contains the results for rendering email templates.

Namespace

Messaging


Apex Reference Guide RenderEmailTemplateBodyResult Class

IN THIS SECTION:

#### RenderEmailTemplateBodyResult Methods RenderEmailTemplateBodyResult Methods The following are methods for RenderEmailTemplateBodyResult .

IN THIS SECTION:

##### getErrors()

If an error occurred during the `renderEmailTemplate` method, a `RenderEmailTemplateError` object is returned.

##### getMergedBody()

Returns the rendered body text with merge field references replaced with the corresponding record data.

##### getSuccess()

Indicates whether the operation was successful.

##### getErrors()

If an error occurred during the `renderEmailTemplate` method, a `RenderEmailTemplateError` object is returned.

Signature

```
   public List<Messaging.RenderEmailTemplateError> getErrors()

```

Return Value

Type: List<Messaging.RenderEmailTemplateError>

##### getMergedBody()

Returns the rendered body text with merge field references replaced with the corresponding record data.

Signature

```
   public String getMergedBody()

```

Return Value

Type: String

##### getSuccess()

Indicates whether the operation was successful.

Signature

```
   public Boolean getSuccess()

```


### Apex Reference Guide RenderEmailTemplateError Class

Return Value

Type: Boolean

### RenderEmailTemplateError Class

Represents an error that the `RenderEmailTemplateBodyResult` object can contain.

Namespace

Messaging

IN THIS SECTION:

#### RenderEmailTemplateError Methods RenderEmailTemplateError Methods

### The following are methods for RenderEmailTemplateError .

IN THIS SECTION:

##### getFieldName()

Returns the name of the merge field in the error.

##### getMessage()

Returns a message describing the error.

getOffset()
Returns the offset within the supplied body text where the error was discovered. If the offset cannot be determined, -1 is returned.

getStatusCode()
Returns a Salesforce API status code.

##### getFieldName()

Returns the name of the merge field in the error.

Signature

```
   public String getFieldName()

```

Return Value

Type: String

##### getMessage()

Returns a message describing the error.


### Apex Reference Guide SendEmailError Class

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### getOffset()

Returns the offset within the supplied body text where the error was discovered. If the offset cannot be determined, -1 is returned.

Signature

```
   public Integer getOffset()

```

Return Value

Type: Integer

##### getStatusCode()

Returns a Salesforce API status code.

Signature

```
   public System.StatusCode getStatusCode()

```

Return Value

Type: System.StatusCode

### SendEmailError Class

Represents an error that the SendEmailResult object may contain.

Namespace

Messaging

#### SendEmailError Methods

### The following are methods for SendEmailError . All are instance methods.

IN THIS SECTION:

getFields()
A list of one or more field names. Identifies which fields in the object, if any, affected the error condition.

getMessage()
The text of the error message.


Apex Reference Guide SendEmailError Class

##### getStatusCode()

Returns a code that characterizes the error.

##### getTargetObjectId()

The ID of the target record for which the error occurred.

##### getFields()

A list of one or more field names. Identifies which fields in the object, if any, affected the error condition.

Signature

```
   public String[] getFields()

```

Return Value

Type: String[]

##### getMessage()

The text of the error message.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### getStatusCode()

Returns a code that characterizes the error.

Signature

```
   public System.StatusCode getStatusCode()

```

Return Value

Type: System.StatusCode

Usage

The full list of status codes is available in the WSDL file for your organization. For more information about accessing the WSDL file for
your organization, see _Downloading Salesforce WSDLs and Client Authentication Certificates_ in the Salesforce online help.

##### getTargetObjectId()

The ID of the target record for which the error occurred.


### Apex Reference Guide SendEmailResult Class

Signature

```
   public String getTargetObjectId()

```

Return Value

Type: String

### SendEmailResult Class

Contains the result of sending an email message.

Namespace

Messaging

#### SendEmailResult Methods

### The following are methods for SendEmailResult . All are instance methods.

IN THIS SECTION:

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

##### isSuccess() Indicates whether the email was successfully submitted for delivery ( true ) or not ( false ). Even if isSuccess is true, it does

not mean the intended recipients received the email, as there could have been a problem with the email address or it could have
bounced or been blocked by a spam blocker.

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

Signature

```
   public SendEmailError[] getErrors()

```

Return Value

Type: Messaging.SendEmailError[]

##### isSuccess() Indicates whether the email was successfully submitted for delivery ( true ) or not ( false ). Even if isSuccess is true, it does not

mean the intended recipients received the email, as there could have been a problem with the email address or it could have bounced
or been blocked by a spam blocker.

Signature

```
   public Boolean isSuccess()

```


### Apex Reference Guide SingleEmailMessage Class

Return Value

Type: Boolean

### SingleEmailMessage Class

Contains methods for sending single email messages.

Namespace

Messaging

Usage

SingleEmailMessage extends Email and inherits all of its methods. All base email ( `Email` class) methods are also available to the
### SingleEmailMessage objects. Emails sent via SingleEmailMessage count against the sending organization's daily single email

limit.

Email properties are readable and writable. Each property has corresponding setter and getter methods. For example, the
`toAddresses()` property is equivalent to the `setToAddresses()` and `getToAddresses()` methods. Only the setter
methods are documented. However, the `getTemplateName()` method doesn’t have an equivalent setter method; use
`setTemplateId()` to specify a template name.

IN THIS SECTION:

#### SingleEmailMessage Constructors

SingleEmailMessage Methods

SEE ALSO:

Email Class (Base Email Methods)

#### SingleEmailMessage Constructors

### The following are constructors for SingleEmailMessage .

IN THIS SECTION:

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

Signature

```
   public SingleEmailMessage()

```


Apex Reference Guide SingleEmailMessage Class

#### SingleEmailMessage Methods The following are methods for SingleEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the SingleEmailMessage objects. These methods are described in Email Class (Base Email Methods).

IN THIS SECTION:

getOneClickPost()
Optional. Returns a boolean value based on the value set by the `setOneClickPost` method. Default is `false` .

getTemplateName()
The name of the template used to create the email.

setBccAddresses(bccAddresses)
Optional. A list of blind carbon copy (BCC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The
maximum size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per
email is 150. All recipients in these three fields count against the limit for email sent using Apex or the API.

setCcAddresses(ccAddresses)
Optional. A list of carbon copy (CC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum
size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150.
All recipients in these three fields count against the limit for email sent using Apex or the API.

setCharset(characterSet)
Optional. The character set for the email. If this value is null, the user's default value is used.

setDocumentAttachments(documentIds)
**(Deprecated. Use** `setEntityAttachments()` **instead.)** Optional. A list containing the ID of each document object you
want to attach to the email.

setEntityAttachments(ids)
[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

setFileAttachments(fileNames)
Optional. A list containing the file names of the binary and text files you want to attach to the email.

setHtmlBody(htmlBody)
Optional. The HTML version of the email, specified by the sender. The value is encoded according to the specification associated
with the organization. Specify a value for `setTemplateId`, `setHtmlBody`, or `setPlainTextBody` . Or, you can define
both `setHtmlBody` and `setPlainTextBody` .

setInReplyTo(parentMessageIds)
Sets the optional In-Reply-To field of the outgoing email. This field identifies the email or emails to which this email is a reply (parent
emails).

setOneClickPost(oneClickPost)
Optional. If set to true, a List-Unsubscribe-Post header is added to an email with List-Unsubscribe=One-Click. Use this method to
support unsubscribe functionality in email sent via Salesforce. You can provide additional instructions on how to send unsubscribe
requests by using the header. This includes specifying the HTTP method and content type to use and provides a secure way to add
more info to unsubscribe requests. Default is `false` .

setOptOutPolicy(emailOptOutPolicy)
Optional. If you added recipients by ID instead of email address and the `Email Opt Out` option is set, this method determines
the behavior of the `sendEmail()` call. If you add recipients by their email addresses, the opt-out settings for those recipients
aren’t checked and those recipients always receive the email.


Apex Reference Guide SingleEmailMessage Class

setPlainTextBody(plainTextBody)
Optional. The text version of the email, specified by the sender. Specify a value for `setTemplateId`, `setHtmlBody`, or
`setPlainTextBody` . Or, you can define both `setHtmlBody` and `setPlainTextBody` .

setOrgWideEmailAddressId(emailAddressId)
Optional. The ID of the organization-wide email address associated with the outgoing email. If you’re using Apex to send emails
from the guest user, set the sender to the verified org-wide email address or the emails are blocked. The object's `DisplayName`
field cannot be set if the `setSenderDisplayName` field is already set.

setReferences(references)
Optional. The References field of the outgoing email. Identifies an email thread. Contains the parent emails' References and message
IDs, and possibly the In-Reply-To fields.

setSubject(subject)
Optional. The email subject line. If you are using an email template, the subject line of the template overrides this value.

setTargetObjectId(targetObjectId)
Required if using a template, optional otherwise. The ID of the contact, lead, or user to which the email will be sent. The ID you
specify sets the context and ensures that merge fields in the template contain the correct data.

setTemplateId(templateId)
Required if using a template, optional otherwise. The ID of the template used to create the email.

setToAddresses(toAddresses)
Optional. A list of email addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum size for
this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All
recipients in these three fields count against the limit for email sent using Apex or the API.

setTreatBodiesAsTemplate(treatAsTemplate)
Optional. If set to `true`, the subject, plain text, and HTML text bodies of the email are treated as template data. The merge fields
are resolved using the `renderEmailTemplate` method. Default is `false` .

setTreatTargetObjectAsRecipient(treatAsRecipient)
Optional. If set to `true`, the `targetObjectId` (a contact, lead, or user) is the recipient of the email. If set to `false`, the
`targetObjectId` is supplied as the `WhoId` field for template rendering but isn’t a recipient of the email. The default is `true` .

setUnsubscribeComment(unsubscribeComment)
Optional. Sets a comment in the List-Unsubscribe email header. This comment is ignored by email clients and systems that parse
the header. The comments contain human-readable notes or context for developers, administrators, or other stakeholders managing
the email system.

setUnsubscribeUrls(UnsubscribeUrls)
Optional. Sets a `mailto` URI and HTTP URL of a mechanism for unsubscribing a recipient from an email list. A list of all unsubscribe
URLs passed through `setUnsubscribeUrls` is added to the `List-Unsubscribe` header. A minimum of one URL is
required to use this method.

setWhatId(whatId)
If you specify a contact for the `targetObjectId` field, you can specify an optional `whatId` as well. This helps to further ensure
that merge fields in the template contain the correct data.

##### **`getOneClickPost()`**

Optional. Returns a boolean value based on the value set by the `setOneClickPost` method. Default is `false` .


Apex Reference Guide SingleEmailMessage Class

Signature

```
   public Boolean getOneClickPost()

```

Parameters

Type: Boolean

Return Value

Type: Boolean

Usage

Invoke the `setOneClickPost` method before using `getOneClickPost` . The value of `getOneClickPost` will be false if
the `setOneClickPost` method is set to true only after invoking the `setUnsubscribeUrls` method.

##### getTemplateName()

The name of the template used to create the email.

Signature

```
   public STRING getTemplateName()

```

Return Value

Type: String

Usage

##### There is no equivalent setter method for getTemplateName() . If the email didn’t use a template, getTemplateName() returns nothing. If you use setTemplateId(), and then call getTemplateName(), the template name associated to the

template ID is returned.

##### setBccAddresses(bccAddresses)

Optional. A list of blind carbon copy (BCC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The
maximum size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email
is 150. All recipients in these three fields count against the limit for email sent using Apex or the API.

Signature

```
   public Void setBccAddresses(String[] bccAddresses)

```

Parameters

```
   bccAddresses
```

Type: String[]


Apex Reference Guide SingleEmailMessage Class

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

If the BCC compliance option is set at the organization level, the user cannot add BCC addresses on standard messages. The following
error code is returned: `BCC_NOT_ALLOWED_IF_BCC_ COMPLIANCE_ENABLED` . Contact your Salesforce representative for
information on BCC compliance.

##### setCcAddresses(ccAddresses)

Optional. A list of carbon copy (CC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum
size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All
recipients in these three fields count against the limit for email sent using Apex or the API.

Signature

```
   public Void setCcAddresses(String[] ccAddresses)

```

Parameters

```
   ccAddresses
```

Type: String[]

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setCharset(characterSet)

Optional. The character set for the email. If this value is null, the user's default value is used.


Apex Reference Guide SingleEmailMessage Class

Signature

```
   public Void setCharset(String characterSet)

```

Parameters

```
   characterSet
```

Type: String

Return Value

Type: Void

##### setDocumentAttachments(documentIds)

**(Deprecated. Use** `setEntityAttachments()` **instead.)** Optional. A list containing the ID of each document object you want
to attach to the email.

Signature

```
   public Void setDocumentAttachments(ID[] documentIds)

```

Parameters

```
   documentIds
```

Type: ID[]

Return Value

Type: Void

Usage

You can attach multiple documents as long as the total size of all attachments does not exceed 10 MB.

##### setEntityAttachments(ids)

[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

Signature

```
   public void setEntityAttachments(List<String> ids)

```

Parameters

```
   ids
```

Type: List<String>

Return Value

Type: void


Apex Reference Guide SingleEmailMessage Class

##### setFileAttachments(fileNames)

Optional. A list containing the file names of the binary and text files you want to attach to the email.

Signature

```
   public Void setFileAttachments(EmailFileAttachment[] fileNames)

```

Parameters

```
   fileNames
```

Type: Messaging.EmailFileAttachment[]

Return Value

Type: Void

Usage

You can attach multiple files as long as the total size of all attachments does not exceed 10 MB.

##### setHtmlBody(htmlBody)

Optional. The HTML version of the email, specified by the sender. The value is encoded according to the specification associated with
##### the organization. Specify a value for setTemplateId, setHtmlBody, or setPlainTextBody . Or, you can define both setHtmlBody and setPlainTextBody .

Signature

```
   public Void setHtmlBody(String htmlBody)

```

Parameters

```
   htmlBody
```

Type: String

Return Value

Type: Void

##### setInReplyTo(parentMessageIds)

Sets the optional In-Reply-To field of the outgoing email. This field identifies the email or emails to which this email is a reply (parent
emails).

Signature

```
   public Void setInReplyTo(String parentMessageIds)

```


Apex Reference Guide SingleEmailMessage Class

Parameters

```
   parentMessageIds
```

Type: String

Contains one or more parent email message IDs.

Return Value

Type: Void

##### **`setOneClickPost(oneClickPost)`**

Optional. If set to true, a List-Unsubscribe-Post header is added to an email with List-Unsubscribe=One-Click. Use this method to support
unsubscribe functionality in email sent via Salesforce. You can provide additional instructions on how to send unsubscribe requests by
using the header. This includes specifying the HTTP method and content type to use and provides a secure way to add more info to
unsubscribe requests. Default is `false` .

Signature

```
   public void setOneClickPost(Boolean oneClickPost)

```

Parameters

```
   oneClickPost
```

Type: Boolean

Return Value

Type: void

Usage

You can set the `oneClickPost` method to true only after invoking the `setUnsubscribeUrls` method. If set to true, pass at
least one HTTPS unsubscribe URL to unsubscribe.

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class with enhanced
unsubscribe functionality. It creates an email message with a recipient, subject, and body, and includes an unsubscribe URL. It also
enables the `oneClickPost` feature, allowing for a simplified unsubscribe process. The email message is added to a list and sent
using the `Messaging.sendEmail` method.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS' };

   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

```


Apex Reference Guide SingleEmailMessage Class

```
   unsubscribeUrls.add('https://example.com/unsubscribe.html?opaque=123456789');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   // Enable the one-click unsubscribe feature

   message.oneClickPost = true;

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setOptOutPolicy(emailOptOutPolicy)

```

Optional. If you added recipients by ID instead of email address and the `Email Opt Out` option is set, this method determines the
behavior of the `sendEmail()` call. If you add recipients by their email addresses, the opt-out settings for those recipients aren’t
checked and those recipients always receive the email.

Signature

```
   public void setOptOutPolicy(String emailOptOutPolicy)

```

Parameters

```
   emailOptOutPolicy
```

Type: String

Possible values of the _`emailOptOutPolicy`_ parameter are:

**•** `SEND` (default)—The email is sent to all recipients. The recipients’ `Email Opt Out` setting is ignored. The setting Enforce
email privacy settings is ignored.

**•** `FILTER` —No email is sent to recipients that have the `Email Opt Out` option set. Emails are sent to the other recipients.
The setting Enforce email privacy settings is ignored.

**•** `REJECT` —If any of the recipients have the `Email Opt Out` option set, `sendEmail()` throws an error and no email is
sent. The setting Enforce email privacy settings is respected, as are the selections in the data privacy record based on the Individual
object. If any of the recipients have Don’t Market, Don’t Process, or Forget This Individual selected, `sendEmail()` throws an
error and no email is sent.

Return Value

Type: void


Apex Reference Guide SingleEmailMessage Class

Example

This example shows how to send an email with the opt-out setting enforced. Recipients are specified by their IDs. The `FILTER` option
causes the email to be sent only to recipients that haven’t opted out from email. This example uses dot notation of the email properties,
which is equivalent to using the set methods.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set recipients to two contact IDs.

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS', '003D000000QDfW5' };

   message.optOutPolicy = 'FILTER';

   message.subject = 'Opt Out Test Message';

   message.plainTextBody = 'This is the message body.';

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

         Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setPlainTextBody(plainTextBody)

```

Optional. The text version of the email, specified by the sender. Specify a value for `setTemplateId`, `setHtmlBody`, or
##### setPlainTextBody . Or, you can define both setHtmlBody and setPlainTextBody .

Signature

```
   public Void setPlainTextBody(String plainTextBody)

```

Parameters

```
   plainTextBody
```

Type: String

Return Value

Type: Void

##### setOrgWideEmailAddressId(emailAddressId)

Optional. The ID of the organization-wide email address associated with the outgoing email. If you’re using Apex to send emails from
the guest user, set the sender to the verified org-wide email address or the emails are blocked. The object's `DisplayName` field cannot
be set if the `setSenderDisplayName` field is already set.

Signature

```
   public Void setOrgWideEmailAddressId(ID emailAddressId)

```


Apex Reference Guide SingleEmailMessage Class

Parameters

```
   emailAddressId
```

Type: ID

Usage

After you create an org-wide email address, you’re sent a confirmation email to verify it. Copy the Id from the URL and use
the _`setOrgWideEmailAddressId(Id)`_ method on your instance of _`Messaging.SingleEmailMessage`_ .

To avoid hard-coding an ID, after creating your org-wide email address, you can query them.

```
   OrgWideEmailAddress[] owea = [select Id from OrgWideEmailAddress where Address =

   'doNotReply@<somedomain>.com'];

   Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

   if ( owea.size() > 0 ) {

      mail.setOrgWideEmailAddressId(owea.get(0).Id);

   }

```

Return Value

Type: Void

##### setReferences(references)

Optional. The References field of the outgoing email. Identifies an email thread. Contains the parent emails' References and message
IDs, and possibly the In-Reply-To fields.

Signature

```
   public Void setReferences(String references)

```

Parameters

```
   references
```

Type: String

Return Value

Type: Void

##### setSubject(subject)

Optional. The email subject line. If you are using an email template, the subject line of the template overrides this value.

Signature

```
   public Void setSubject(String subject)

```

Parameters

```
   subject
```

Type: String


Apex Reference Guide SingleEmailMessage Class

Return Value

Type: Void

##### setTargetObjectId(targetObjectId)

Required if using a template, optional otherwise. The ID of the contact, lead, or user to which the email will be sent. The ID you specify
sets the context and ensures that merge fields in the template contain the correct data.

Signature

```
   public Void setTargetObjectId(ID targetObjectId)

```

Parameters

```
   targetObjectId
```

Type: ID

Return Value

Type: Void

Usage

Do not specify the IDs of records that have the `Email Opt Out` option selected.

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setTemplateId(templateId)

Required if using a template, optional otherwise. The ID of the template used to create the email.

Signature

```
   public Void setTemplateId(ID templateId)

```

Parameters

```
   templateId
```

Type: ID

Return Value

Type: Void


Apex Reference Guide SingleEmailMessage Class

##### setToAddresses(toAddresses)

Optional. A list of email addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum size for this
field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All recipients
in these three fields count against the limit for email sent using Apex or the API.

Signature

```
   public Void setToAddresses(String[] toAddresses)

```

Parameters

```
   toAddresses
```

Type: String[]

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setTreatBodiesAsTemplate(treatAsTemplate)

Optional. If set to `true`, the subject, plain text, and HTML text bodies of the email are treated as template data. The merge fields are
resolved using the `renderEmailTemplate` method. Default is `false` .

Signature

```
   public void setTreatBodiesAsTemplate(Boolean treatAsTemplate)

```

Parameters

```
   treatAsTemplate
```

Type: Boolean

Return Value

Type: void

##### setTreatTargetObjectAsRecipient(treatAsRecipient)

Optional. If set to `true`, the `targetObjectId` (a contact, lead, or user) is the recipient of the email. If set to `false`, the
`targetObjectId` is supplied as the `WhoId` field for template rendering but isn’t a recipient of the email. The default is `true` .


Apex Reference Guide SingleEmailMessage Class

Signature

```
   public void setTreatTargetObjectAsRecipient(Boolean treatAsRecipient)

```

Parameters

```
   treatAsRecipient
```

Type: Boolean

Return Value

Type: void

Usage

Note: You can set TO, CC, and BCC addresses using the email messaging methods regardless of whether a template is used for
the email or the target object is a recipient.

##### **`setUnsubscribeComment(unsubscribeComment)`**

Optional. Sets a comment in the List-Unsubscribe email header. This comment is ignored by email clients and systems that parse the
header. The comments contain human-readable notes or context for developers, administrators, or other stakeholders managing the
email system.

Signature

```
   public void setUnsubscribeComment(String unsubscribeComment)

```

Parameters

```
   unsubscribeComment
```

Type: String

Return Value

Type: void

Usage

##### Invoke the setUnsubscribeUrls method before using setUnsubscribeComment .

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class with an option
to include an unsubscribe link. It creates an email message with a recipient, subject, and body, and includes an unsubscribe URL that
directs the recipient to send an unsubscribe request via email. Additionally, it sets an `unsubscribeComment` to provide context
for the unsubscribe action.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org

   message.toAddresses = new String[] { '003D000000QDexS' };

```


Apex Reference Guide SingleEmailMessage Class

```
   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

   unsubscribeUrls.add('mailto:listrequest@example.com?subject=unsubscribe');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   // Set an unsubscribe comment to provide context for the unsubscribe action

   message.unsubscribeComment = 'email unsubscribe support';

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### **`setUnsubscribeUrls(UnsubscribeUrls)`**

```

Optional. Sets a `mailto` URI and HTTP URL of a mechanism for unsubscribing a recipient from an email list. A list of all unsubscribe
##### URLs passed through setUnsubscribeUrls is added to the List-Unsubscribe header. A minimum of one URL is required

to use this method.

Signature

```
   public void setUnsubscribeUrls(List<String> unsubscribeUrls)

```

Parameters

```
    UnsubscribeUrls

```

Type: List<String>

Return Value

Type: void

Usage

Provide a list of URLs that support unsubscribe functionality by offering recipients multiple ways to opt-out of future communications.
Each provided URL can use different protocols to allow for technical capacities of the recipient.

##### All setUnsubscribeUrls must have a value of one of these types:


Apex Reference Guide SingleEmailMessage Class

**•** `Mailto` : Allows recipients to send an unsubscribe request via email.

**–** Example: `mailto:listrequest@example.com?subject=unsubscribe`

**•** `HTTP` : Directs recipients to a web page where they can unsubscribe.

**–** Example: `http://example.com/unsubscribe.html?opaque=123456789`

**•** `HTTPS` : Directs recipients to a secure web page to unsubscribe.

**–** Example: `https://example.com/unsubscribe.html?opaque=123456789`

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class that includes an
option to include an unsubscribe link for a user to click. It creates an email message, sets the recipient's email address, subject, and body,
and includes an unsubscribe URL. The email message is added to a list and sent using the `Messaging.sendEmail` method.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS' };

   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

   unsubscribeUrls.add('https://example.com/unsubscribe.html?opaque=123456789');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setWhatId(whatId)

```

If you specify a contact for the `targetObjectId` field, you can specify an optional `whatId` as well. This helps to further ensure
that merge fields in the template contain the correct data.

Signature

```
   public Void setWhatId(ID whatId)

```


## Apex Reference Guide Metadata Namespace

Parameters

```
   whatId
```

Type: ID

Return Value

Type: Void

Usage

The value must be one of the following types:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contract

**•** Opportunity

**•** Order

**•** Product

**•** Solution

**•** Custom

## Metadata Namespace The Metadata namespace provides classes and methods for working with custom metadata in Salesforce

Salesforce uses metadata types and components to represent org configuration and customization. Metadata is used for org settings
## that admins control or configuration information applied by installed apps and packages. Use the classes in the Metadata namespace

to access metadata from within Apex code.

Metadata access in Apex is available for Apex classes using API version 40.0 and later.

[For more information, see Metadata.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_metadata.htm)

## The following are the classes in the Metadata namespace.

IN THIS SECTION:

AnalyticsCloudComponentLayoutItem Class
Represents the settings for a Wave Analytics dashboard on a standard or custom page.

ConsoleComponent Class
Represents a custom console component on a section of a page layout.

Container Class
Represents a location and style in which to display more than one custom console component in the sidebars of the console.

CustomConsoleComponents Class
Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.


Apex Reference Guide Metadata Namespace

CustomMetadata Class
Represents records of custom metadata types.

CustomMetadataValue Class
Represents custom metadata values for a custom metadata component.

DeployCallback Interface
An interface for metadata deployment callback classes.

DeployCallbackContext Class
Represents context information for a deployment job.

DeployContainer Class
Represents a container for custom metadata components to be deployed.

DeployDetails Class
Contains detailed information on deployed components.

DeployMessage Class
Represents result information for the deployment of a metadata component.

DeployProblemType Enum
Describes the problem type for an unsuccessful component deploy.

DeployResult Class
Represents the results of a metadata deployment.

DeployStatus Enum
The result status of a deployment.

FeedItemTypeEnum Enum
The type of feed item in a feed-based page layout.

FeedLayout Class
Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case,
Contact, Lead, Opportunity, custom, and external objects. They include a feed view and a detail view.

FeedLayoutComponent Class
Represents a component in the feed view of a feed-based page layout.

FeedLayoutComponentType Enum
Indicates the type of feed layout component.

FeedLayoutFilter Class
Represents a feed filter option in the feed view of a feed-based page layout. A filter can have only `standardFilter` or
`feedItemType` set.

FeedLayoutFilterPosition Enum
Describes where the feed filters list is included in the layout.

FeedLayoutFilterType Enum
The type of feed layout filter.

Layout Class
Represents the metadata associated with a page layout.

LayoutColumn Class
Represents the items in a column within a layout section.


Apex Reference Guide Metadata Namespace

LayoutHeader Enum
Represents tagging types used for `Metadata.Layout.headers`

LayoutItem Class
Represents the valid values that define a layout item.

LayoutSection Class
Represents a section of a page layout, such as the Custom Links section.

LayoutSectionStyle Enum
Describes the possible styles for a layout section.

Metadata Class
An abstract base class that represents a custom metadata component.

MetadataType Enum
Represents the custom metadata components available in Apex.

MetadataValue Class
An abstract base class that represents a custom metadata component field.

MiniLayout Class
Represents a mini view of a record in the Console tab, hover details, and event overlays.

Operations Class
Represents a class to execute metadata operations, such as retrieving or deploying custom metadata.

PlatformActionList Class
Represents the list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

PlatformActionListContextEnum Enum
Describes the different contexts of action lists.

PlatformActionListItem Class
Represents an action in the platform action list for a layout.

PlatformActionTypeEnum Enum
The type of action for a `PlatformActionListItem` .

PrimaryTabComponents Class
Represents custom console components on primary tabs in the Salesforce console.

QuickActionList Class
Represents the list of actions associated with the page layout.

QuickActionListItem Class
Represents an action in the `QuickActionList` .

RelatedContent Class
Represents the Mobile Cards section of the page layout.

RelatedContentItem Class
Represents an individual item in the `RelatedContent` list.

RelatedList Class
Represents related list custom components on the sidebars of the Salesforce console.

RelatedListItem Class
Represents an item in the related list in a page layout.


### Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

ReportChartComponentLayoutItem Class
Represents the settings for a report chart on a standard or custom page.

ReportChartComponentSize Enum
Describes the size of the displayed report chart component.

SidebarComponent Class
Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars
of the Salesforce console.

SortOrder Enum
Describes the sort order of a related list.

StatusCode Enum
Describes the status code for an unsuccessful component deploy.

SubtabComponents Class
Represents custom console components on subtabs in the Salesforce console.

SummaryLayoutStyleEnum Enum
Describes the highlights panel style for a `SummaryLayout` .

SummaryLayout Class
Controls the appearance of the highlights panel, which summarizes key fields in a grid at the top of a page layout, when Case Feed
is enabled.

SummaryLayoutItem Class
Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel.

UiBehavior Enum
Describes the behavior for a layout item on a layout page.

### AnalyticsCloudComponentLayoutItem Class

Represents the settings for a Wave Analytics dashboard on a standard or custom page.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“AnalyticsCloudComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

AnalyticsCloudComponentLayoutItem Properties

AnalyticsCloudComponentLayoutItem Methods


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

#### AnalyticsCloudComponentLayoutItem Properties The following are properties for AnalyticsCloudComponentLayoutItem .

IN THIS SECTION:

##### assetType

Specifies the type of Wave Analytics asset.

##### devName

Unique development name of the dashboard to add.

error
An error string that is populated only when an error occurred in the underlying dashboard.

filter
Dashboard filters for mapping data fields in the dashboard to the object’s fields.

height
Specifies the height of the dashboard, in pixels.

hideOnError
Controls whether users see a dashboard that has an error.

showHeader
If `true`, includes the dashboard’s header bar. If `false`, the dashboard appears without a header bar.

showSharing
If set to true, and the dashboard is shareable the dashboard shows the Share icon. If set to false, the dashboard doesn’t show the
Share icon.

showTitle
If true, includes the dashboard’s title above the dashboard. If false, the dashboard appears without a title.

width
Specifies the width of the dashboard, in pixels or percentage.

##### assetType

Specifies the type of Wave Analytics asset.

Signature

```
   public String assetType {get; set;}

```

Property Value

Type: String

##### devName

Unique development name of the dashboard to add.


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

Signature

```
   public String devName {get; set;}

```

Property Value

Type: String

##### error

An error string that is populated only when an error occurred in the underlying dashboard.

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### filter

Dashboard filters for mapping data fields in the dashboard to the object’s fields.

Signature

```
   public String filter {get; set;}

```

Property Value

Type: String

##### height

Specifies the height of the dashboard, in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### hideOnError

Controls whether users see a dashboard that has an error.

Signature

```
   public Boolean hideOnError {get; set;}

```


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

Property Value

Type: Boolean

##### showHeader

If `true`, includes the dashboard’s header bar. If `false`, the dashboard appears without a header bar.

Signature

```
   public Boolean showHeader {get; set;}

```

Property Value

Type: Boolean

##### showSharing

If set to true, and the dashboard is shareable the dashboard shows the Share icon. If set to false, the dashboard doesn’t show the Share
icon.

Signature

```
   public Boolean showSharing {get; set;}

```

Property Value

Type: Boolean

##### showTitle

If true, includes the dashboard’s title above the dashboard. If false, the dashboard appears without a title.

Signature

```
   public Boolean showTitle {get; set;}

```

Property Value

Type: Boolean

##### width

Specifies the width of the dashboard, in pixels or percentage.

Signature

```
   public String width {get; set;}

```


### Apex Reference Guide ConsoleComponent Class

Property Value

Type: String

#### AnalyticsCloudComponentLayoutItem Methods The following are methods for AnalyticsCloudComponentLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.AnalyticsCloudComponentLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.AnalyticsCloudComponentLayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ConsoleComponent Class

Represents a custom console component on a section of a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “ConsoleComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### ConsoleComponent Properties

ConsoleComponent Methods

#### ConsoleComponent Properties

### The following are properties for ConsoleComponent .


Apex Reference Guide ConsoleComponent Class

IN THIS SECTION:

##### height

The height of the custom console component in pixels.

##### location

The location of the custom console component on the page layout. Valid values are right, left, top, and bottom.

##### visualforcePage

The unique name of the custom console component.

##### width

The width of the custom console component in pixels.

##### height

The height of the custom console component in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### location

The location of the custom console component on the page layout. Valid values are right, left, top, and bottom.

Signature

```
   public String location {get; set;}

```

Property Value

Type: String

##### visualforcePage

The unique name of the custom console component.

Signature

```
   public String visualforcePage {get; set;}

```

Property Value

Type: String

##### width

The width of the custom console component in pixels.


### Apex Reference Guide Container Class

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### ConsoleComponent Methods The following are methods for ConsoleComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.ConsoleComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.ConsoleComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### Container Class

Represents a location and style in which to display more than one custom console component in the sidebars of the console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “Container” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

Container Properties

Container Methods


Apex Reference Guide Container Class

#### Container Properties The following are properties for Container .

IN THIS SECTION:

##### height

The height of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

##### isContainerAutoSizeEnabled

If set to true, stacked console components in the sidebars autosize vertically.

##### region

The location of the component’s container (right, left, bottom, top).

sidebarComponents
Represents a specific custom console component to display in the components’ container.

style
The style of the container in which to display multiple components (stack, tab, accordion).

unit
The unit of measurement, in pixels or percent, for the height or width of the components’ container.

width
The width of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

##### height

The height of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### isContainerAutoSizeEnabled

If set to true, stacked console components in the sidebars autosize vertically.

Signature

```
   public Boolean isContainerAutoSizeEnabled {get; set;}

```

Property Value

Type: Boolean

##### region

The location of the component’s container (right, left, bottom, top).


Apex Reference Guide Container Class

Signature

```
   public String region {get; set;}

```

Property Value

Type: String

##### sidebarComponents

Represents a specific custom console component to display in the components’ container.

Signature

```
   public List<Metadata.SidebarComponent> sidebarComponents {get; set;}

```

Property Value

Type: List<Metadata.SidebarComponent>

##### style

The style of the container in which to display multiple components (stack, tab, accordion).

Signature

```
   public String style {get; set;}

```

Property Value

Type: String

##### unit

The unit of measurement, in pixels or percent, for the height or width of the components’ container.

Signature

```
   public String unit {get; set;}

```

Property Value

Type: String

##### width The width of the component’s container. The unit property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer width {get; set;}

```


### Apex Reference Guide CustomConsoleComponents Class

Property Value

Type: Integer

#### Container Methods The following are methods for Container .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Container` .

##### clone()

Makes a duplicate copy of the `Metadata.Container` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### CustomConsoleComponents Class

Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “CustomConsoleComponents”
in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### CustomConsoleComponents Properties

CustomConsoleComponents Methods

#### CustomConsoleComponents Properties

### The following are properties for CustomConsoleComponents .


Apex Reference Guide CustomConsoleComponents Class

IN THIS SECTION:

##### primaryTabComponents

Represents custom console components on primary tabs in the Salesforce console.

##### subtabComponents

Represents custom console components on subtabs in the Salesforce console.

##### primaryTabComponents

Represents custom console components on primary tabs in the Salesforce console.

Signature

```
   public Metadata.PrimaryTabComponents primaryTabComponents {get; set;}

```

Property Value

Type: Metadata.PrimaryTabComponents

##### subtabComponents

Represents custom console components on subtabs in the Salesforce console.

Signature

```
   public Metadata.SubtabComponents subtabComponents {get; set;}

```

Property Value

Type: Metadata.SubtabComponents

#### CustomConsoleComponents Methods The following are methods for CustomConsoleComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomConsoleComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomConsoleComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide CustomMetadata Class

Return Value

Type: Object

### CustomMetadata Class

Represents records of custom metadata types.

Warning: Protected custom metadata types behave like public custom metadata types when they are outside of a managed
package. Public custom metadata types are readable for all profiles, including the guest user. Do not store secrets, personally
identifying information, or any private data in these records. Use protected custom metadata types only in managed packages.
Outside of a managed package, use named credentials or encrypted custom fields to store secrets like OAuth tokens, passwords,
and other confidential material.

Namespace

Metadata

Usage

Use `Metadata.CustomMetadata` [to represent records of custom metadata types in Apex. For more information, see Custom](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm)
[Metadata Types in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm) _Metadata API Developer Guide_ .

Example

```
   // Set up custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

      Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

      customField.field = 'customField__c';

      customField.value = 'New value';

      customMetadata.values.add(customField);

```

Note: When you assign namespaces to records, provide full, qualified record names to the app. If both the type and the record
are in _`Namespace`_, use something like: `customMetadata.fullName =`

```
     ' Namespace __MetadataTypeName. Namespace __MetadataRecordName'

```

IN THIS SECTION:

#### CustomMetadata Properties

CustomMetadata Methods

#### CustomMetadata Properties

### The following are properties for CustomMetadata .


Apex Reference Guide CustomMetadata Class

IN THIS SECTION:

##### description

The description of the custom metadata.

##### label

The label of the custom metadata record.

##### protected_x

Property that describes whether the custom metadata record is a protected component.

##### values

A list of custom metadata values, such as custom fields, for the custom metadata record.

##### description

The description of the custom metadata.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

##### label

The label of the custom metadata record.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### protected_x

Property that describes whether the custom metadata record is a protected component.

Signature

```
   public Boolean protected_x {get; set;}

```

Property Value

Type: Boolean

##### values

A list of custom metadata values, such as custom fields, for the custom metadata record.


### Apex Reference Guide CustomMetadataValue Class

Signature

```
   public List<Metadata.CustomMetadataValue> values {get; set;}

```

Property Value

Type: List<Metadata.CustomMetadataValue>

#### CustomMetadata Methods The following are methods for CustomMetadata .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadata` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadata` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### CustomMetadataValue Class

Represents custom metadata values for a custom metadata component.

Namespace

Metadata

Usage

Use `Metadata.CustomMetadataValue` to access values for custom fields of custom metadata records.

Supported Apex primitive types are:

**•** Boolean

**•** Date

**•** DateTime

**•** Decimal

**•** Double

**•** Integer

**•** Long


Apex Reference Guide CustomMetadataValue Class

**•** String

Example

```
   // Set a custom field value for a custom metadata record

   Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

   customField.field = 'CustomField1__c';

   customField.value = 'New Value';

   customMetadata.values.add(customField);

```

IN THIS SECTION:

#### CustomMetadataValue Properties

CustomMetadataValue Methods

#### CustomMetadataValue Properties The following are properties for CustomMetadataValue .

IN THIS SECTION:

##### field

The field name for the custom metadata value.

##### value

The field value for the custom metadata value.

##### field

The field name for the custom metadata value.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### value

The field value for the custom metadata value.

Signature

```
   public Object value {get; set;}

```

Property Value

Type: Object


### Apex Reference Guide DeployCallback Interface

Supported Apex primitive types are:

**•** Boolean

**•** Date

**•** DateTime

**•** Decimal

**•** Double

**•** Integer

**•** Long

**•** String

When setting the value for relationship fields, use the qualified API name of the related metadata, not the ID.

[For more information, see Primitive Data Types.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### CustomMetadataValue Methods The following are methods for CustomMetadataValue .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployCallback Interface

An interface for metadata deployment callback classes.

Namespace

Metadata

Usage

You must provide a callback class for the asynchronous deployment of custom metadata through Apex. This class must implement the
`Metadata.DeployCallback` interface.


Apex Reference Guide DeployCallback Interface

Salesforce calls your `DeployCallback.handleResult()` method asynchronously once the queued deployment completes.
Because the callback is called as asynchronous Apex after deployment, there may be a brief period where the deploy has completed,
but your callback has not been called yet.

IN THIS SECTION:

#### DeployCallback Methods DeployCallback Example Implementation DeployCallback Methods The following are methods for DeployCallback .

IN THIS SECTION:

##### handleResult(var1, var2)

Method that is called when the asynchronous deployment of custom metadata completes.

##### handleResult(var1, var2)

Method that is called when the asynchronous deployment of custom metadata completes.

Signature

```
   public void handleResult(Metadata.DeployResult var1, Metadata.DeployCallbackContext

   var2)

```

Parameters

```
   var1
```

Type: Metadata.DeployResult

The results of the asynchronous deployment.

```
   var2
```

Type: Metadata.DeployCallbackContext

The context for the queued asynchronous deployment job.

Return Value

Type: void

#### DeployCallback Example Implementation

This is an example implementation of the `Metadata.DeployCallback` interface.

```
   public class MyCallback implements Metadata.DeployCallback {

      public void handleResult(Metadata.DeployResult result,

                     Metadata.DeployCallbackContext context) {

        if (result.status == Metadata.DeployStatus.Succeeded) {

           // Deployment was successful

```


### Apex Reference Guide DeployCallbackContext Class

```
        } else {

           // Deployment was not successful

        }

      }

   }

```

The following example uses this implementation for a deployment.

```
   // Setup callback and deploy

   MyCallback callback = new MyCallback();

   Metadata.Operations.enqueueDeployment(mdContainer, callback);

### DeployCallbackContext Class

```

Represents context information for a deployment job.

Namespace

Metadata

Usage

After an asynchronous metadata deployment finishes, Salesforce provides an instance of `Metadata.DeployCallbackContext`
in an asynchronous call to your implementation of `handleResult()` in your `Metadata.DeployCallback` class.

Example

```
   public void handleResult(Metadata.DeployResult result,

                  Metadata.DeployCallbackContext context) {

     // Check the callback job ID for the deployment

     Id jobId = context.getCallbackJobId();

     // ...process the results...

   }

```

IN THIS SECTION:

#### DeployCallbackContext Methods DeployCallbackContext Methods

### The following are methods for DeployCallbackContext .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.DeployCallbackContext` .

getCallbackJobId()
Gets the asynchronous Apex job ID for the callback job.


### Apex Reference Guide DeployContainer Class

##### clone()

Makes a duplicate copy of the `Metadata.DeployCallbackContext` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### getCallbackJobId()

Gets the asynchronous Apex job ID for the callback job.

Signature

```
   public Id getCallbackJobId()

```

Return Value

Type: Id

### DeployContainer Class

Represents a container for custom metadata components to be deployed.

Namespace

Metadata

Usage

Use `Metadata.DeployContainer` to manage custom metadata components for deployment. A container must have one or
more components before being deployed.

Example

```
   // Use DeployContainer for deployment

   Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

   mdContainer.addMetadata(customMetadata);

   ...

   // Enqueue deploy

   Metadata.Operations.enqueueDeployment(mdContainer, callback);

```


Apex Reference Guide DeployContainer Class

IN THIS SECTION:

#### DeployContainer Methods DeployContainer Methods The following are methods for DeployContainer .

IN THIS SECTION:

##### addMetadata(md)

Add a custom metadata component to the container.

##### clone()

Makes a duplicate copy of the `Metadata.DeployContainer` .

getMetadata()
Retrieves a list of custom metadata components from the container.

removeMetadata(md)
Removes a metadata component from the container.

removeMetadataByFullName(fullName)
Removes a metadata component from the container using the component’s full name.

##### addMetadata(md)

Add a custom metadata component to the container.

Signature

```
   public void addMetadata(Metadata.Metadata md)

```

Parameters

```
   md
```

Type: Metadata.Metadata

A custom metadata component class that derives from `Metadata.Metadata` . Avoid adding components to a
`Metadata.DeployContainer` that have the same `Metadata.Metadata.fullName` because it causes deployment
errors.

Return Value

Type: void

##### clone()

Makes a duplicate copy of the `Metadata.DeployContainer` .

Signature

```
   public Object clone()

```


Apex Reference Guide DeployContainer Class

Return Value

Type: Object

##### getMetadata()

Retrieves a list of custom metadata components from the container.

Signature

```
   public List<Metadata.Metadata> getMetadata()

```

Return Value

Type: List<Metadata.Metadata>

##### removeMetadata(md)

Removes a metadata component from the container.

Signature

```
   public Boolean removeMetadata(Metadata.Metadata md)

```

Parameters

```
   md
```

Type: Metadata.Metadata

Metadata component to remove.

Return Value

Type: Boolean

Returns `true` if the container changed as a result of the call.

##### removeMetadataByFullName(fullName)

Removes a metadata component from the container using the component’s full name.

Signature

```
   public Boolean removeMetadataByFullName(String fullName)

```

Parameters

```
   fullName
```

Type: String

Full name of the component to remove.


### Apex Reference Guide DeployDetails Class

Return Value

Type: Boolean

Returns `true` if the container changed as a result of the call.

### DeployDetails Class

Contains detailed information on deployed components.

Namespace

Metadata

Usage

Use this class to obtain a list of the successfully and unsuccessfully deployed components after a completed deployment by Salesforce
in your `Metadata.DeployCallback` results.

IN THIS SECTION:

#### DeployDetails Properties

DeployDetails Methods

#### DeployDetails Properties

### The following are properties for DeployDetails .

IN THIS SECTION:

##### componentFailures

Contains a list of information about components that failed to deploy.

##### componentSuccesses

Contains a list of information about components that deployed successfully.

##### componentFailures

Contains a list of information about components that failed to deploy.

Signature

```
   public List<Metadata.DeployMessage> componentFailures {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

##### componentSuccesses

Contains a list of information about components that deployed successfully.


### Apex Reference Guide DeployMessage Class

Signature

```
   public List<Metadata.DeployMessage> componentSuccesses {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

#### DeployDetails Methods The following are methods for DeployDetails .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployDetails` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployDetails` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployMessage Class

Represents result information for the deployment of a metadata component.

Namespace

Metadata

Usage

### Use DeployMessage to access detailed information about component deployments. Salesforce provides a list of DeployMessages
#### for a completed deployment via the DeployDetails and DeployResults instances sent in the

`DeployCallback.handleResult()` callback.

IN THIS SECTION:

DeployMessage Properties

DeployMessage Methods


Apex Reference Guide DeployMessage Class

#### DeployMessage Properties The following are properties for DeployMessage .

IN THIS SECTION:

##### changed

Determines whether the component was changed after deployment. If true, the component was changed as a result of the deployment.
If false, the deployed component was the same as the corresponding component already in the org.

columnNumber
Each component is represented by a text file. If an error occurs during deployment, this property represents the column of the text
file where the error occurred.

componentType
The metadata type of the component in the deployment.

created
If true, the component was created as a result of the deployment. If false, the component was modified as a result of the deployment.

createdDate
The date and time when the component was created as a result of the deployment.

deleted
If true, the component was deleted as a result of the deployment. If false, the component was either new or modified as result of
the deployment.

fileName
The name of the file in the metadata archive used to deploy the component.

fullName
Full name for the custom metadata component.

id
ID of the component that was deployed.

lineNumber
Each component is represented by a text file. If an error occurs during deployment, this field represents the line number of the text
file where the error occurred.

problem
If an error or warning occurred, this field contains a description of the problem that caused the deployment to fail.

problemType
Indicates the problem type, for example, an error or warning.

success
Indicates whether the component was successfully deployed (true) or not (false).

##### changed

Determines whether the component was changed after deployment. If true, the component was changed as a result of the deployment.
If false, the deployed component was the same as the corresponding component already in the org.


Apex Reference Guide DeployMessage Class

Signature

```
   public Boolean changed {get; set;}

```

Property Value

Type: Boolean

##### columnNumber

Each component is represented by a text file. If an error occurs during deployment, this property represents the column of the text file
where the error occurred.

Signature

```
   public Integer columnNumber {get; set;}

```

Property Value

Type: Integer

##### componentType

The metadata type of the component in the deployment.

Signature

```
   public String componentType {get; set;}

```

Property Value

Type: String

##### created

If true, the component was created as a result of the deployment. If false, the component was modified as a result of the deployment.

Signature

```
   public Boolean created {get; set;}

```

Property Value

Type: Boolean

##### createdDate

The date and time when the component was created as a result of the deployment.


Apex Reference Guide DeployMessage Class

Signature

```
   public Datetime createdDate {get; set;}

```

Property Value

Type: Datetime

##### deleted

If true, the component was deleted as a result of the deployment. If false, the component was either new or modified as result of the
deployment.

Signature

```
   public Boolean deleted {get; set;}

```

Property Value

Type: Boolean

##### fileName

The name of the file in the metadata archive used to deploy the component.

Signature

```
   public String fileName {get; set;}

```

Property Value

Type: String

##### fullName

Full name for the custom metadata component.

Signature

```
   public String fullName {get; set;}

```

Property Value

Type: String

##### id

ID of the component that was deployed.


Apex Reference Guide DeployMessage Class

Signature

```
   public Id id {get; set;}

```

Property Value

Type: Id

##### lineNumber

Each component is represented by a text file. If an error occurs during deployment, this field represents the line number of the text file
where the error occurred.

Signature

```
   public Integer lineNumber {get; set;}

```

Property Value

Type: Integer

##### problem

If an error or warning occurred, this field contains a description of the problem that caused the deployment to fail.

Signature

```
   public String problem {get; set;}

```

Property Value

Type: String

##### problemType

Indicates the problem type, for example, an error or warning.

Signature

```
   public Metadata.DeployProblemType problemType {get; set;}

```

Property Value

Type: Metadata.DeployProblemType

##### success

Indicates whether the component was successfully deployed (true) or not (false).


### Apex Reference Guide DeployProblemType Enum

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeployMessage Methods The following are methods for DeployMessage .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployMessage` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployMessage` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployProblemType Enum

Describes the problem type for an unsuccessful component deploy.

Enum Values

The following are the values of the `Metadata.DeployProblemType` enum.

**Value** **Description**

`Error` The deploy problem is an error.

`Info` The deploy problem is of type “Info”.

`Warning` The deploy problem is a warning.

SEE ALSO:

StatusCode Enum


### Apex Reference Guide DeployResult Class DeployResult Class

Represents the results of a metadata deployment.

Namespace

Metadata

Usage

After an asynchronous metadata deployment finishes, Salesforce provides an instance of `Metadata.DeployResult` in a call to
your implementation of `handleResult()` in your `Metadata.DeployCallback` class.

Example

```
   public void handleResult(Metadata.DeployResult result,

                  Metadata.DeployCallbackContext context) {

      if (result.status == Metadata.DeployStatus.Succeeded) {

        // Deployment was successful

      } else {

        // Deployment was not successful

      }

   }

```

IN THIS SECTION:

#### DeployResult Properties

DeployResult Methods

#### DeployResult Properties

### The following are properties for DeployResult .

IN THIS SECTION:

canceledBy
ID of the user who canceled the queued deployment.

canceledByName
Full name of the user who canceled the queued deployment.

checkOnly
Indicates whether the deployment checked only the validity of the deployed files without making changes in the org. A check-only
deployment does not deploy components or change the org in any way.

completedDate
Date and time for when the deployment process ended.

createdBy
ID of the user who created the deployment job.


Apex Reference Guide DeployResult Class

createdByName
Full name of the user who created the deployment job.

createdDate
Date and time the deployment job was first queued.

details
Provides the details for components in a completed deployment.

done
Indicates whether Salesforce finished processing the deployment.

errorMessage
Message corresponding to the values in the `errorStatusCode` property, if any.

errorStatusCode
If an error occurs during deployment, a status code is returned. The message corresponding to the status code is returned in the
`errorMessagefield` property.

id
ID of the deployment job.

ignoreWarnings
Specifies whether a deployment continues, even if the deployment generates warnings.

lastModifiedDate
Date and time of the last update for the deployment process.

messages
A list of all the detail messages for a deployment.

numberComponentErrors
The number of components that generated errors during the deployment.

numberComponentsDeployed
The number of components deployed in the deployment process. Use this value with the `numberComponentsTotal` property
to get an estimate of the deployment’s progress.

numberComponentsTotal
The total number of components in the deployment. Use this value with the `numberComponentsDeployed` property to get
an estimate of the deployment’s progress.

rollbackOnError
Indicates whether any failure causes a complete rollback (true) or not (false) of the deployment.

startDate
Date and time the deployment process began.

stateDetail
Indicates which component is being deployed.

status
Indicates the current state of the deployment.

success
Indicates whether the deployment was successful (true) or not (false).


Apex Reference Guide DeployResult Class

##### canceledBy

ID of the user who canceled the queued deployment.

Signature

```
   public String canceledBy {get; set;}

```

Property Value

Type: String

##### canceledByName

Full name of the user who canceled the queued deployment.

Signature

```
   public String canceledByName {get; set;}

```

Property Value

Type: String

##### checkOnly

Indicates whether the deployment checked only the validity of the deployed files without making changes in the org. A check-only
deployment does not deploy components or change the org in any way.

Signature

```
   public Boolean checkOnly {get; set;}

```

Property Value

Type: Boolean

##### completedDate

Date and time for when the deployment process ended.

Signature

```
   public Datetime completedDate {get; set;}

```

Property Value

Type: Datetime


Apex Reference Guide DeployResult Class

##### createdBy

ID of the user who created the deployment job.

Signature

```
   public String createdBy {get; set;}

```

Property Value

Type: String

##### createdByName

Full name of the user who created the deployment job.

Signature

```
   public String createdByName {get; set;}

```

Property Value

Type: String

##### createdDate

Date and time the deployment job was first queued.

Signature

```
   public Datetime createdDate {get; set;}

```

Property Value

Type: Datetime

##### details

Provides the details for components in a completed deployment.

Signature

```
   public Metadata.DeployDetails details {get; set;}

```

Property Value

Type: Metadata.DeployDetails

##### done

Indicates whether Salesforce finished processing the deployment.


Apex Reference Guide DeployResult Class

Signature

```
   public Boolean done {get; set;}

```

Property Value

Type: Boolean

##### errorMessage Message corresponding to the values in the errorStatusCode property, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### errorStatusCode

If an error occurs during deployment, a status code is returned. The message corresponding to the status code is returned in the
##### errorMessagefield property.

Signature

```
   public String errorStatusCode {get; set;}

```

Property Value

Type: String

[For a description of each status code value, see Core Data Types Used in API Calls in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_concepts_core_data_objects.htm) _SOAP API Developer Guide_ .

##### id

ID of the deployment job.

Signature

```
   public Id id {get; set;}

```

Property Value

Type: Id

##### ignoreWarnings

Specifies whether a deployment continues, even if the deployment generates warnings.


Apex Reference Guide DeployResult Class

Signature

```
   public Boolean ignoreWarnings {get; set;}

```

Property Value

Type: Boolean

##### lastModifiedDate

Date and time of the last update for the deployment process.

Signature

```
   public Datetime lastModifiedDate {get; set;}

```

Property Value

Type: Datetime

##### messages

A list of all the detail messages for a deployment.

Note: Removed in API version 29.0 and later.

Signature

```
   public List<Metadata.DeployMessage> messages {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

##### numberComponentErrors

The number of components that generated errors during the deployment.

Signature

```
   public Integer numberComponentErrors {get; set;}

```

Property Value

Type: Integer

##### numberComponentsDeployed

The number of components deployed in the deployment process. Use this value with the `numberComponentsTotal` property
to get an estimate of the deployment’s progress.


Apex Reference Guide DeployResult Class

Signature

```
   public Integer numberComponentsDeployed {get; set;}

```

Property Value

Type: Integer

##### numberComponentsTotal

The total number of components in the deployment. Use this value with the `numberComponentsDeployed` property to get an
estimate of the deployment’s progress.

Signature

```
   public Integer numberComponentsTotal {get; set;}

```

Property Value

Type: Integer

##### rollbackOnError

Indicates whether any failure causes a complete rollback (true) or not (false) of the deployment.

Signature

```
   public Boolean rollbackOnError {get; set;}

```

Property Value

Type: Boolean

##### startDate

Date and time the deployment process began.

Signature

```
   public Datetime startDate {get; set;}

```

Property Value

Type: Datetime

##### stateDetail

Indicates which component is being deployed.


Apex Reference Guide DeployResult Class

Signature

```
   public String stateDetail {get; set;}

```

Property Value

Type: String

##### status

Indicates the current state of the deployment.

Signature

```
   public Metadata.DeployStatus status {get; set;}

```

Property Value

Type: Metadata.DeployStatus

##### success

Indicates whether the deployment was successful (true) or not (false).

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeployResult Methods The following are methods for DeployResult .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployResult` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployResult` .

Signature

```
   public Object clone()

```


### Apex Reference Guide DeployStatus Enum

Return Value

Type: Object

### DeployStatus Enum

The result status of a deployment.

Usage

`Metadata.DeployResult.status` uses this enum to describe the results of the deployment.

Enum Values

The following are the values of the `Metadata.DeployStatus` enum.

**Value** **Description**

`Canceled` The queued deployment was canceled.

`Canceling` The queued deployment is being canceled.

`Failed` The deployment failed.

`FinalizingDeploy` The deployment has started, and is in the finalizing state. Deployments in the state
can't be canceled.

`FinalizingDeployFailed` The deployment failed during the finalizing state.

`InProgress` The deployment has been started and is in progress.

`Pending` The deployment has been queued but not started.

`Succeeded` The deployment succeeded.

`SucceededPartial` The deployment succeeded, but some components might not have been successfully
deployed. Check `Metadata.DeployResult` for more details.

### FeedItemTypeEnum Enum

The type of feed item in a feed-based page layout.

Enum Values

The following are the values of the `Metadata.FeedItemTypeEnum` enum.

**Value** **Description**

`ActivityEvent` Activity on tasks and events associated with a case. Available only on Case layouts.

`AdvancedTextPost` Group announcements posted on a feed.

`AnnouncementPost` Not used.


Apex Reference Guide FeedItemTypeEnum Enum

**Value** **Description**

`ApprovalPost` Approvals submitted on a feed.

`AttachArticleEvent` Activity related to attaching articles to cases.

`BasicTemplateFeedItem` Activity from the Log a Call action. Available only on layouts for objects that support
Activities (tasks and events).

`CallLogPost` Activity from the Log a Call action. Available only on layouts for objects that support
Activities (tasks and events).

`CanvasPost` Posts a canvas app makes on a feed.

`CaseCommentPost` Activity from the Case Note action. Available only on Case layouts.

`ChangeStatusPost` Activity from the Change Status action. Available only on Case layouts.

`ChatTranscriptPost` Activity related to attaching Chat transcripts to cases. Available only on Case layouts.

`CollaborationGroupCreated` Creating a public group.

`CollaborationGroupUnarchived` Not used.

`ContentPost` Attaching a file to a post.

`CreateRecordEvent` Creating a record from the publisher.

`DashboardComponentAlert` Not used.

`DashboardComponentSnapshot` Posting a dashboard snapshot on a feed.

`EmailMessageEvent` Activity from the Email action. Available only on Case layouts.

`FacebookPost` Not used.

`LinkPost` Attaching a URL to a post.

`MilestoneEvent` Changing the milestone status on a case. Available only on Case layouts.

`PollPost` Posting a poll on a feed.

`ProfileSkillPost` Adding skills to a user’s Chatter profile.

`QuestionPost` Posting a question on a feed.

`ReplyPost` Activity from the Portal action. Available only on Case layouts.

`RypplePost` Creating a Thanks badge in WDC.

`SocialPost` Activity on Twitter from the Social Post action.

`TestItem` Creating a text post from the publisher.

`TextPost` Making a change or group of changes to a tracked field.

`TrackedChange` Not used.

`Undefined` Undefined feed item.

`UserStatus` Not used.


### Apex Reference Guide FeedLayout Class FeedLayout Class

Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case, Contact,
Lead, Opportunity, custom, and external objects. They include a feed view and a detail view.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayout Properties

FeedLayout Methods

#### FeedLayout Properties

### The following are properties for FeedLayout .

IN THIS SECTION:

autocollapsePublisher
Specifies whether the publisher is collapsed when the page loads (true) or not (false).

compactFeed
Specifies whether the feed-based page layout uses a compact feed (true) or not (false). If set to true, feed items on the page are
collapsed by default, and the feed view has an updated design.

feedFilterPosition
Indicates where the feed filters list is included in the layout.

feedFilters
The individual filters displayed in the feed filters list.

fullWidthFeed
Specifies whether the feed expands horizontally to take up all available space on the page ( `true` ) or not ( `false` ).

hideSidebar
Specifies whether the sidebar is hidden ( `true` ) or not ( `false` ).

highlightExternalFeedItems
Controls whether to highlight external feed items (true) or not (false).

leftComponents
The individual components displayed in the left column of the feed view.

rightComponents
Lists the individual components displayed in the right column of the feed view.


Apex Reference Guide FeedLayout Class

useInlineFiltersInConsole
Indicates whether to use inline filters in the Salesforce console.

##### autocollapsePublisher

Specifies whether the publisher is collapsed when the page loads (true) or not (false).

Signature

```
   public Boolean autocollapsePublisher {get; set;}

```

Property Value

Type: Boolean

##### compactFeed

Specifies whether the feed-based page layout uses a compact feed (true) or not (false). If set to true, feed items on the page are collapsed
by default, and the feed view has an updated design.

Signature

```
   public Boolean compactFeed {get; set;}

```

Property Value

Type: Boolean

##### feedFilterPosition

Indicates where the feed filters list is included in the layout.

Signature

```
   public Metadata.FeedLayoutFilterPosition feedFilterPosition {get; set;}

```

Property Value

Type: FeedLayoutFilterPosition Enum

##### feedFilters

The individual filters displayed in the feed filters list.

Signature

```
   public List<Metadata.FeedLayoutFilter> feedFilters {get; set;}

```

Property Value

Type: List<FeedLayoutFilter Class>.


Apex Reference Guide FeedLayout Class

##### fullWidthFeed

Specifies whether the feed expands horizontally to take up all available space on the page ( `true` ) or not ( `false` ).

Signature

```
   public Boolean fullWidthFeed {get; set;}

```

Property Value

Type: Boolean

##### hideSidebar

Specifies whether the sidebar is hidden ( `true` ) or not ( `false` ).

Signature

```
   public Boolean hideSidebar {get; set;}

```

Property Value

Type: Boolean

##### highlightExternalFeedItems

Controls whether to highlight external feed items (true) or not (false).

Signature

```
   public Boolean highlightExternalFeedItems {get; set;}

```

Property Value

Type: Boolean

##### leftComponents

The individual components displayed in the left column of the feed view.

Signature

```
   public List<Metadata.FeedLayoutComponent> leftComponents {get; set;}

```

Property Value

Type: List<FeedLayoutComponent Class>

##### rightComponents

Lists the individual components displayed in the right column of the feed view.


### Apex Reference Guide FeedLayoutComponent Class

Signature

```
   public List<Metadata.FeedLayoutComponent> rightComponents {get; set;}

```

Property Value

Type: List<FeedLayoutComponent Class>

##### useInlineFiltersInConsole

Indicates whether to use inline filters in the Salesforce console.

Signature

```
   public Boolean useInlineFiltersInConsole {get; set;}

```

Property Value

Type: Boolean

#### FeedLayout Methods The following are methods for FeedLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutComponent Class

Represents a component in the feed view of a feed-based page layout.

Namespace

Metadata


Apex Reference Guide FeedLayoutComponent Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutComponent” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutComponent Properties

FeedLayoutComponent Methods

#### FeedLayoutComponent Properties The following are properties for FeedLayoutComponent . See FeedLayoutComponent in the Metadata API Developer Guide

IN THIS SECTION:

##### componentType

Represents a component in the feed view of a feed-based page layout. The type of component is required.

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

page_x
The name of the Visualforce page used as a custom component.

##### componentType

Represents a component in the feed view of a feed-based page layout. The type of component is required.

Signature

```
   public Metadata.FeedLayoutComponentType componentType {get; set;}

```

Property Value

Type: Metadata.FeedLayoutComponentType on page 3041

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer


### Apex Reference Guide FeedLayoutComponentType Enum

##### page_x

The name of the Visualforce page used as a custom component.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

#### FeedLayoutComponent Methods The following are methods for FeedLayoutComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutComponentType Enum

Indicates the type of feed layout component.

Enum Values

The following are the values of the `Metadata.FeedLayoutComponentType` enum.

**Value** **Description**

`CaseExperts` List of case experts.

`CaseUnifiedFiles` List of all files attached to the case.

`CustomButtons` Custom button.

`CustomLinks` Custom link.

`Followers` List of followers.


### Apex Reference Guide FeedLayoutFilter Class

**Value** **Description**

```
Following

```

Icon that toggles between a Follow button (if the user viewing a record doesn’t
already follow it) and a Following indicator (if the user viewing a record does follow
it).

`HelpAndToolLinks` Icons that link to the help topic for the page, the page layout, and, the printable
view of the page. Available only on Case layouts.

`Milestones` Milestone tracker, which lets users see the status of a milestone on a case. Available
only on Case layouts.

`SimilarCases` List of similar cases.

`Topics` List of topics related to the record.

`Visualforce` Custom Visualforce component.

### FeedLayoutFilter Class

Represents a feed filter option in the feed view of a feed-based page layout. A filter can have only `standardFilter` or
`feedItemType` set.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutFilter” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutFilter Properties

FeedLayoutFilter Methods

#### FeedLayoutFilter Properties

### The following are properties for FeedLayoutFilter .

IN THIS SECTION:

feedFilterName
The name of a `CustomFeedFilter` component. Names are prefixed with the name of the parent object. For example,
`Case.MyCustomFeedFilter` .

feedFilterType
The type of filter.


Apex Reference Guide FeedLayoutFilter Class

##### feedItemType

The type of feed item to display.

##### feedFilterName

The name of a `CustomFeedFilter` component. Names are prefixed with the name of the parent object. For example,
`Case.MyCustomFeedFilter` .

Signature

```
   public String feedFilterName {get; set;}

```

Property Value

Type: String

##### feedFilterType

The type of filter.

Signature

```
   public Metadata.FeedLayoutFilterType feedFilterType {get; set;}

```

Property Value

Type: FeedLayoutFilterType Enum

##### feedItemType

The type of feed item to display.

Signature

```
   public Metadata.FeedItemTypeEnum feedItemType {get; set;}

```

Property Value

Type: FeedItemTypeEnum Enum

#### FeedLayoutFilter Methods The following are methods for FeedLayoutFilter .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.FeedLayoutFilter` .


### Apex Reference Guide FeedLayoutFilterPosition Enum

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutFilter` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutFilterPosition Enum

Describes where the feed filters list is included in the layout.

Enum Values

The following are the values of the `Metadata.FeedLayoutFilterPosition` enum.

**Value** **Description**

`CenterDropDown` As a drop-down list in the center column.

`LeftFixed` As a fixed list in the left column.

`LeftFloat` As a floating list in the left column.

### FeedLayoutFilterType Enum

The type of feed layout filter.

Enum Values

The following are the values of the `Metadata.FeedLayoutFilterType` enum.

**Value** **Description**

`AllUpdates` Shows all feed items on a record.

`Custom` Shows custom feed items.

`FeedItemType` Shows feed items only for a particular type of activity on the record.

### Layout Class

Represents the metadata associated with a page layout.


Apex Reference Guide Layout Class

Namespace

Metadata

Usage

[Use this class to access layout metadata components. For more information, see Layout in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_layouts.htm) _Metadata API Developer Guide_ .

IN THIS SECTION:

#### Layout Properties

Layout Methods

#### Layout Properties The following are properties for Layout .

IN THIS SECTION:

customButtons
The custom buttons for this layout.

customConsoleComponents
Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

emailDefault
Default value for the email checkbox. Only relevant if the `showEmailCheckbox` property is set.

excludeButtons
List of standard buttons to exclude from this layout.

feedLayout
Represents the values that define the feed view of a feed-based page layout.

headers
Represents the layout headers used for tagging.

layoutSections
The main sections of the layout containing fields, s-controls, and custom links. The order here determines the layout order.

miniLayout
Represents a minilayout, which is used in the mini view of a record in the Console tab, hover details, and event overlays.

multilineLayoutFields
Fields for special multiline layout fields which appear in OpportunityProduct layouts.

platformActionList
The list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

quickActionList
The list of quick actions that display in the full Salesforce site for the page layout.

relatedContent
The Related Content section of the page layout.


Apex Reference Guide Layout Class

relatedLists
The related lists for the layout, listed in the order they appear in the user interface.

relatedObjects
The list of related objects that appears in the mini view of the console.

runAssignmentRulesDefault
Default value for the “run assignment rules” checkbox. Only relevant if the `showRunAssignmentRulesCheckbox` property
is set.

showEmailCheckbox
Controls whether to show the email checkbox. Only allowed on Case, CaseClose, and Task layouts. The default state of checkbox is
controlled by the `emailDefault` property.

showHighlightsPanel
If set, the highlights panel displays on pages in the Salesforce console.

showInteractionLogPanel
If set, the interaction log displays on pages in the Salesforce console.

showKnowledgeComponent
Only allowed on Case layouts. If set, the Knowledge sidebar displays on cases in the Salesforce console.

showRunAssignmentRulesCheckbox
Controls whether to show the Run Assignment Rules checkbox. Only allowed on Lead and Case layouts. The default state of checkbox
is controlled by the `runAssignmentRulesDefault` property.

showSolutionSection
Only allowed on CaseClose layout. If set, the built-in solution information section shows up on the page.

showSubmitAndAttachButton
For Cast layouts only. If set, the Submit & Add Attachment button displays on case edit pages to portal users in the Customer Portal.

summaryLayout
The summary layout for this layout.

##### customButtons

The custom buttons for this layout.

Signature

```
   public List<String> customButtons {get; set;}

```

Property Value

Type: List<String>

##### customConsoleComponents

Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

Signature

```
   public Metadata.CustomConsoleComponents customConsoleComponents {get; set;}

```


Apex Reference Guide Layout Class

Property Value

Type: CustomConsoleComponents Class

##### emailDefault

Default value for the email checkbox. Only relevant if the `showEmailCheckbox` property is set.

Signature

```
   public Boolean emailDefault {get; set;}

```

Property Value

Type: Boolean

##### excludeButtons

List of standard buttons to exclude from this layout.

Signature

```
   public List<String> excludeButtons {get; set;}

```

Property Value

Type: List<String>

##### feedLayout

Represents the values that define the feed view of a feed-based page layout.

Signature

```
   public Metadata.FeedLayout feedLayout {get; set;}

```

Property Value

Type: Metadata.FeedLayout

##### headers

Represents the layout headers used for tagging.

Signature

```
   public List<Metadata.LayoutHeader> headers {get; set;}

```

Property Value

Type: List<Metadata.LayoutHeader>


Apex Reference Guide Layout Class

##### layoutSections

The main sections of the layout containing fields, s-controls, and custom links. The order here determines the layout order.

Signature

```
   public List<Metadata.LayoutSection> layoutSections {get; set;}

```

Property Value

Type: List<Metadata.LayoutSection>

##### miniLayout

Represents a minilayout, which is used in the mini view of a record in the Console tab, hover details, and event overlays.

Signature

```
   public Metadata.MiniLayout miniLayout {get; set;}

```

Property Value

Type: Metadata.MiniLayout

##### multilineLayoutFields

Fields for special multiline layout fields which appear in OpportunityProduct layouts.

Signature

```
   public List<String> multilineLayoutFields {get; set;}

```

Property Value

Type: List<String>

##### platformActionList

The list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

Signature

```
   public Metadata.PlatformActionList platformActionList {get; set;}

```

Property Value

Type: Metadata.PlatformActionList

##### quickActionList

The list of quick actions that display in the full Salesforce site for the page layout.


Apex Reference Guide Layout Class

Signature

```
   public Metadata.QuickActionList quickActionList {get; set;}

```

Property Value

Type: Meatadata.QuickActionL.

##### relatedContent

The Related Content section of the page layout.

Signature

```
   public Metadata.RelatedContent relatedContent {get; set;}

```

Property Value

Type: Metadata.RelatedContent

##### relatedLists

The related lists for the layout, listed in the order they appear in the user interface.

Signature

```
   public List<Metadata.RelatedListItem> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedListItem>

##### relatedObjects

The list of related objects that appears in the mini view of the console.

Signature

```
   public List<String> relatedObjects {get; set;}

```

Property Value

Type: List<String>

##### runAssignmentRulesDefault

Default value for the “run assignment rules” checkbox. Only relevant if the `showRunAssignmentRulesCheckbox` property is
set.


Apex Reference Guide Layout Class

Signature

```
   public Boolean runAssignmentRulesDefault {get; set;}

```

Property Value

Type: Boolean

##### showEmailCheckbox

Controls whether to show the email checkbox. Only allowed on Case, CaseClose, and Task layouts. The default state of checkbox is
controlled by the `emailDefault` property.

Signature

```
   public Boolean showEmailCheckbox {get; set;}

```

Property Value

Type: Boolean

##### showHighlightsPanel

If set, the highlights panel displays on pages in the Salesforce console.

Signature

```
   public Boolean showHighlightsPanel {get; set;}

```

Property Value

Type: Boolean

##### showInteractionLogPanel

If set, the interaction log displays on pages in the Salesforce console.

Signature

```
   public Boolean showInteractionLogPanel {get; set;}

```

Property Value

Type: Boolean

##### showKnowledgeComponent

Only allowed on Case layouts. If set, the Knowledge sidebar displays on cases in the Salesforce console.


Apex Reference Guide Layout Class

Signature

```
   public Boolean showKnowledgeComponent {get; set;}

```

Property Value

Type: Boolean

##### showRunAssignmentRulesCheckbox

Controls whether to show the Run Assignment Rules checkbox. Only allowed on Lead and Case layouts. The default state of checkbox
is controlled by the `runAssignmentRulesDefault` property.

Signature

```
   public Boolean showRunAssignmentRulesCheckbox {get; set;}

```

Property Value

Type: Boolean

##### showSolutionSection

Only allowed on CaseClose layout. If set, the built-in solution information section shows up on the page.

Signature

```
   public Boolean showSolutionSection {get; set;}

```

Property Value

Type: Boolean

##### showSubmitAndAttachButton

For Cast layouts only. If set, the Submit & Add Attachment button displays on case edit pages to portal users in the Customer Portal.

Signature

```
   public Boolean showSubmitAndAttachButton {get; set;}

```

Property Value

Type: Boolean

##### summaryLayout

The summary layout for this layout.


### Apex Reference Guide LayoutColumn Class

Signature

```
   public Metadata.SummaryLayout summaryLayout {get; set;}

```

Property Value

Type: Metadata.SummaryLayout

#### Layout Methods The following are methods for Layout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Layout` .

##### clone()

Makes a duplicate copy of the `Metadata.Layout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutColumn Class

Represents the items in a column within a layout section.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutColumn” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

LayoutColumn Properties

LayoutColumn Methods


Apex Reference Guide LayoutColumn Class

#### LayoutColumn Properties The following are properties for LayoutColumn .

IN THIS SECTION:

##### layoutItems

The individual items within a column (ordered from top to bottom).

##### reserved

This field is reserved for Salesforce.

##### layoutItems

The individual items within a column (ordered from top to bottom).

Signature

```
   public List<Metadata.LayoutItem> layoutItems {get; set;}

```

Property Value

Type: List<Metadata.LayoutItem>

##### reserved

This field is reserved for Salesforce.

Signature

```
   public String reserved {get; set;}

```

Property Value

Type: String

#### LayoutColumn Methods The following are methods for LayoutColumn .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutColumn` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutColumn` .


### Apex Reference Guide LayoutHeader Enum

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutHeader Enum

Represents tagging types used for `Metadata.Layout.headers`

Enum Values

The following are the values of the `Metadata.LayoutHeader` enum.

**Value** **Description**

`PersonalTagging` Tag is set to private user.

`PublicTagging` Tag is viewable to any user who can access the record.

### LayoutItem Class

Represents the valid values that define a layout item.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutItem Properties

LayoutItem Methods

#### LayoutItem Properties

### The following are properties for LayoutItem .

IN THIS SECTION:

analyticsCloudComponent
A Wave Analytics dashboard component on a page.


Apex Reference Guide LayoutItem Class

##### behavior

Determines the field behavior.

canvas
References a canvas app.

component
References a component.

customLink
The custom link reference.

emptySpace
Controls if this layout item is a blank space.

field
The field name reference, relative to the layout, for example “Description” or “MyField__c”.

height
For s-controls and pages only, the height in pixels.

page_x
Reference to a Visualforce page.

reportChartComponent
Refers to a report chart that you can add to a standard or custom object page.

scontrol
Reference to an s-control.

showLabel
For s-control and pages only, whether to show the label.

showScrollbars
For s-control and pages only, whether to show scrollbars.

width
For s-control and pages only, the width in pixels or percent. Pixel values are simply the number of pixels, for example, 500. Percentage
values must include the percent sign, for example, 20%.

##### analyticsCloudComponent

A Wave Analytics dashboard component on a page.

Signature

```
   public Metadata.AnalyticsCloudComponentLayoutItem analyticsCloudComponent {get; set;}

```

Property Value

Type: Metadata.AnalyticsCloudComponentLayoutItem

##### behavior

Determines the field behavior.


Apex Reference Guide LayoutItem Class

Signature

```
   public Metadata.UiBehavior behavior {get; set;}

```

Property Value

Type: Metadata.UiBehavior

##### canvas

References a canvas app.

Signature

```
   public String canvas {get; set;}

```

Property Value

Type: String

##### component

References a component.

Signature

```
   public String component {get; set;}

```

Property Value

Type: String

##### customLink

The custom link reference.

Signature

```
   public String customLink {get; set;}

```

Property Value

Type: String

##### emptySpace

Controls if this layout item is a blank space.

Signature

```
   public Boolean emptySpace {get; set;}

```


Apex Reference Guide LayoutItem Class

Property Value

Type: Boolean

##### field

The field name reference, relative to the layout, for example “Description” or “MyField__c”.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### height

For s-controls and pages only, the height in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### page_x

Reference to a Visualforce page.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

##### reportChartComponent

Refers to a report chart that you can add to a standard or custom object page.

Signature

```
   public Metadata.ReportChartComponentLayoutItem reportChartComponent {get; set;}

```

Property Value

Type: Metadata.ReportChartComponentLayoutItem


Apex Reference Guide LayoutItem Class

##### scontrol

Reference to an s-control.

Signature

```
   public String scontrol {get; set;}

```

Property Value

Type: String

##### showLabel

For s-control and pages only, whether to show the label.

Signature

```
   public Boolean showLabel {get; set;}

```

Property Value

Type: Boolean

##### showScrollbars

For s-control and pages only, whether to show scrollbars.

Signature

```
   public Boolean showScrollbars {get; set;}

```

Property Value

Type: Boolean

##### width

For s-control and pages only, the width in pixels or percent. Pixel values are simply the number of pixels, for example, 500. Percentage
values must include the percent sign, for example, 20%.

Signature

```
   public String width {get; set;}

```

Property Value

Type: String


### Apex Reference Guide LayoutSection Class

#### LayoutItem Methods The following are methods for LayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutSection Class

Represents a section of a page layout, such as the Custom Links section.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutSection” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutSection Properties

LayoutSection Methods

#### LayoutSection Properties

### The following are properties for LayoutSection .

IN THIS SECTION:

customLabel
Indicates if this section's label is custom or standard (built-in).

detailHeading
Controls whether this heading appears on the detail page.


Apex Reference Guide LayoutSection Class

##### editHeading

Controls whether this heading appears on the edit page.

##### label

The label; either standard or custom, based on the customLabel property.

layoutColumns
Lists the layout columns. You can have one, two, or three columns, ordered left to right, are possible.

style
The style of the layout for this section.

##### customLabel

Indicates if this section's label is custom or standard (built-in).

Signature

```
   public Boolean customLabel {get; set;}

```

Property Value

Type: Boolean

##### **`detailHeading`**

Controls whether this heading appears on the detail page.

Signature

```
   public Boolean detailHeading {get; set;}

```

Property Value

Type: Boolean

##### **`editHeading`**

Controls whether this heading appears on the edit page.

Signature

```
   public Boolean editHeading {get; set;}

```

Property Value

Type: Boolean

##### label

The label; either standard or custom, based on the customLabel property.


Apex Reference Guide LayoutSection Class

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### layoutColumns

Lists the layout columns. You can have one, two, or three columns, ordered left to right, are possible.

Signature

```
   public List<Metadata.LayoutColumn> layoutColumns {get; set;}

```

Property Value

Type: List<Metadata.LayoutColumn>

##### style

The style of the layout for this section.

Signature

```
   public Metadata.LayoutSectionStyle style {get; set;}

```

Property Value

Type: Metadata.LayoutSectionStyle

#### LayoutSection Methods The following are methods for LayoutSection .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

Signature

```
   public Object clone()

```


### Apex Reference Guide LayoutSectionStyle Enum

Return Value

Type: Object

### LayoutSectionStyle Enum

Describes the possible styles for a layout section.

Enum Values

The following are the values of the `Metadata.LayoutSectionStyle` enum.

**Value** **Description**

`CustomLinks` Contains custom links only

`OneColumn` One column

`TwoColumnsLeftToRight` Two columns, tab goes left to right

`TwoColumnsTopToBottom` Two columns, tab goes top to bottom

### Metadata Class

An abstract base class that represents a custom metadata component.

Namespace

### Metadata

Usage

You can’t create instances of this abstract class. Instead, create an instance of a specific custom metadata component class that derives
from `Metadata.Metadata`, such as `Metadata.CustomMetadata` [. For more information, see Metadata in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) _Metadata API_
_Developer Guide_ .

IN THIS SECTION:

#### Metadata Properties

Metadata Methods

#### Metadata Properties

### The following are properties for Metadata .

IN THIS SECTION:

fullName
The full name of the custom metadata, which can include the namespace, type, and component name.


### Apex Reference Guide MetadataType Enum

##### fullName

The full name of the custom metadata, which can include the namespace, type, and component name.

Signature

```
   public String fullName {get; set;}

```

Property Value

Type: String

The format of the full name can include the namespace, metadata type, and metadata component name. If you’re updating components
in a namespace, you also need to qualify the namespace for the component in the full name. For example, the full name for a custom
metadata "MDType1__mdt" component named "Component1" that is contained in the "myPackage" namespace is
"myPackage__MDType1__mdt.myPackage__Component1". For more information on full name formats for different metadata types,
see reference documentation on the metadata types in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

#### Metadata Methods The following are methods for Metadata .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Metadata` .

##### clone()

Makes a duplicate copy of the `Metadata.Metadata` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### MetadataType Enum

Represents the custom metadata components available in Apex.

Enum Values

The following are the values of the `Metadata.MetadataType` enum.

**Value** **Description**

`CustomMetadata` Records of custom metadata types


### Apex Reference Guide MetadataValue Class

**Value** **Description**

`Layout` Layouts

### MetadataValue Class

An abstract base class that represents a custom metadata component field.

Namespace

### Metadata

Usage

You can’t create instances of this abstract class. Instead, create an instance of a specific custom metadata component value class that
derives from `Metadata.MetadataValue`, such as `Metadata.CustomMetadataValue` .

IN THIS SECTION:

#### MetadataValue Methods MetadataValue Methods

### The following are methods for MetadataValue .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.MetadataValue` .

##### clone()

Makes a duplicate copy of the `Metadata.MetadataValue` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### MiniLayout Class

Represents a mini view of a record in the Console tab, hover details, and event overlays.


Apex Reference Guide MiniLayout Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “MiniLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### MiniLayout Properties

MiniLayout Methods

#### MiniLayout Properties The following are properties for MiniLayout .

IN THIS SECTION:

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

##### relatedLists

The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the
mini related lists must appear in the main layout.

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

Signature

```
   public List<String> fields {get; set;}

```

Property Value

Type: List<String>

##### relatedLists

The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the mini
related lists must appear in the main layout.

Signature

```
   public List<Metadata.RelatedListItem> relatedLists {get; set;}

```


### Apex Reference Guide Operations Class

Property Value

Type: List<Metadata.RelatedListItem>

#### MiniLayout Methods The following are methods for MiniLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### Operations Class

Represents a class to execute metadata operations, such as retrieving or deploying custom metadata.

Namespace

Metadata

Usage

Use the `Metadata.Operations` class to execute metadata operations. For more information on use cases and restrictions of
metadata operations in Apex, see Metadata.

Example: Retrieve Metadata

The following example retrieves the “MyTestCustomMDType” custom metadata record from the subscriber org, and inspects the custom
fields.

```
   public class ReadMetadata {

     public void retrieveMetadata () {

      // List fullnames of components we want to retrieve

      List<String> componentNameList =

   new List<String>{'ISVNamespace__TestCustomMDType.MyTestCustomMDType'};

      // Retrieve components that are records of custom metadata types

```


Apex Reference Guide Operations Class

```
      // based on name

      List<Metadata.Metadata> components = Metadata.Operations.retrieve(

   Metadata.MetadataType.CustomMetadata, componentNameList);

      Metadata.CustomMetadata customMetadataRecord = (Metadata.CustomMetadata)

   components.get(0);

      // Check fields of retrieved component

      List<Metadata.CustomMetadataValue> values = customMetadataRecord.values;

      for (integer i = 0; i < values.size(); i++) {

       if (values.get(i).field == 'testField__c' &&

         values.get(i).value == 'desired value') {

        // ...process accordingly...

       }

      }

     }

   }

```

Example: Deploy Metadata

The following example uses the Metadata API in Apex to update the customField custom field value of the MetadataRecordName custom
metadata record and deploy this change into the subscriber org. Because the deployment is asynchronous, you must provide a callback
class that implements the `Metadata.DeployCallback` interface, which is then used when the queued deployment completes.

```
   public class CreateMetadata{

     public void updateAndDeployMetadata() {

      // Setup custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

      Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

      customField.field = 'customField__c';

      customField.value = 'New value';

      customMetadata.values.add(customField);

      Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

      mdContainer.addMetadata(customMetadata);

      // Setup deploy callback, MyDeployCallback implements

      // the Metadata.DeployCallback interface (code for

      // this class not shown in this example)

      MyDeployCallback callback = new MyDeployCallback();

      // Enqueue custom metadata deployment

      Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, callback);

     }

   }

```

Example: Create Two Metadata Records Synchronously

Create a metadata record along with another one that references it in the same transaction. If the parent record was installed with a
namespace, prefix the developer name with _`recordNs__`_ .


Apex Reference Guide Operations Class

Note: No custom metadata relationship can relate records of the same type to each other.

```
   public class CreateMetadata {

      public Id doCreate(

        String parentRecDevName,

        String parentRecLabel,

        String childRecDevName,

        String childRecLabel) {

        Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

        Metadata.CustomMetadata parentRecord = new Metadata.CustomMetadata();

        parentRecord.fullName = 'ParentType.' + parentRecDevName;

        parentRecord.label = parentRecLabel;

        mdContainer.addMetadata(parentRecord);

        Metadata.CustomMetadata childRecord = new Metadata.CustomMetadata();

        childRecord.fullName = 'ChildType.' + childRecDevName;

        childRecord.label = childRecLabel;

        Metadata.CustomMetadataValue relValue = new Metadata.CustomMetadataValue();

        relValue.field = 'Parent__c';

        relValue.value = parentRecDevName;

        childRecord.values.add(relValue);

        mdContainer.addMetadata(childRecord);

        Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, null);

        return jobId;

      }

   }

```

IN THIS SECTION:

#### Operations Methods Operations Methods The following are methods for Operations .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.Operations` .

enqueueDeployment(container, callback)
Deploys custom metadata components asynchronously.

retrieve(type, fullNames)
Retrieves a list of custom metadata components.


Apex Reference Guide Operations Class

##### clone()

Makes a duplicate copy of the `Metadata.Operations` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### enqueueDeployment(container, callback)

Deploys custom metadata components asynchronously.

Signature

To preserve service function, we limit the number of Metadata API deployments originating from Apex that can be enqueued at a time.
See Limit on Enqueued Deployments from Apex.

```
   public static Id enqueueDeployment(Metadata.DeployContainer container,

   Metadata.DeployCallback callback)

```

Parameters

```
   container
```

Type: Metadata.DeployContainer

Container that contains the set of metadata components to deploy.

```
   callback
```

Type: Metadata.DeployCallback

A class that implements the `Metadata.DeployCallback` interface. Used by Salesforce to return information about the
deployment results.

Return Value

Type: Id

ID of deployment request.

##### retrieve(type, fullNames)

Retrieves a list of custom metadata components.

Signature

```
   public static List<Metadata.Metadata> retrieve(Metadata.MetadataType type, List<String>

   fullNames)

```


### Apex Reference Guide PlatformActionList Class

Parameters

```
   type
```

Type: Metadata.MetadataType

The metadata component type.

```
   fullNames
```

Type: List<String>

A list of component names to retrieve. For information on component name formats, see Metadata.fullName().

Return Value

Type: List<Metadata.Metadata>

### PlatformActionList Class

Represents the list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionList” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionList Properties

PlatformActionList Methods

#### PlatformActionList Properties

### The following are properties for PlatformActionList .

IN THIS SECTION:

actionListContext
The context of the action list.

platformActionListItems
The actions in the platform action list.

relatedSourceEntity
When the `actionListContext` property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the
related list to which the action belongs.


Apex Reference Guide PlatformActionList Class

##### actionListContext

The context of the action list.

Signature

```
   public Metadata.PlatformActionListContextEnum actionListContext {get; set;}

```

Property Value

Type: Metadata.PlatformActionListContextEnum

##### platformActionListItems

The actions in the platform action list.

Signature

```
   public List<Metadata.PlatformActionListItem> platformActionListItems {get; set;}

```

Property Value

Type: List<Metadata.PlatformActionListItem>

##### relatedSourceEntity When the actionListContext property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the related

list to which the action belongs.

Signature

```
   public String relatedSourceEntity {get; set;}

```

Property Value

Type: String

#### PlatformActionList Methods The following are methods for PlatformActionList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .


### Apex Reference Guide PlatformActionListContextEnum Enum

Signature

```
   public Object clone()

```

Return Value

Type: Object

### PlatformActionListContextEnum Enum

Describes the different contexts of action lists.

Enum Values

The following are the values of the `Metadata.PlatformActionListContextEnum` enum.

**Value** **Description**

`ActionDefinition` Action definition context.

`Assistant` Assistant context.

`BannerPhoto` Banner photo context.

`Chatter` Chatter context.

`Dockable` Dockable context.

`FeedElement` Feed element context.

`Flexipage` Flexipage context.

`Global_x` Global context.

`ListView` Listview context.

`ListViewDefinition` Listview definition context.

`ListViewRecord` Listview record context.

`Lookup` Lookup context.

`MruList` MRU list context.

`MruRow` MRU row context.

`ObjectHomeChart` Object home chart context.

`Photo` Photo context

`Record` Record context.

`RecordEdit` Record edit context

`RelatedList` Related list context.

`RelatedListRecord` Related list record context.


### Apex Reference Guide PlatformActionListItem Class PlatformActionListItem Class

Represents an action in the platform action list for a layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionListItem Properties

PlatformActionListItem Methods

#### PlatformActionListItem Properties

### The following are properties for PlatformActionListItem .

IN THIS SECTION:

##### actionName

The API name for the action in the list.

##### actionType

The type of action.

sortOrder
The placement of the action in the list.

subtype
The subtype of the action.

##### actionName

The API name for the action in the list.

Signature

```
   public String actionName {get; set;}

```

Property Value

Type: String

##### actionType

The type of action.


Apex Reference Guide PlatformActionListItem Class

Signature

```
   public Metadata.PlatformActionTypeEnum actionType {get; set;}

```

Property Value

Type: Metadata.PlatformActionTypeEnum

##### sortOrder

The placement of the action in the list.

Signature

```
   public Integer sortOrder {get; set;}

```

Property Value

Type: Integer

##### subtype

The subtype of the action.

Signature

```
   public String subtype {get; set;}

```

Property Value

Type: String

#### PlatformActionListItem Methods The following are methods for PlatformActionListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide PlatformActionTypeEnum Enum

Return Value

Type: Object

### PlatformActionTypeEnum Enum

The type of action for a `PlatformActionListItem` .

Enum Values

The following are the values of the `Metadata.PlatformActionTypeEnum` enum.

**Value** **Description**

`ActionLink` An indicator on a feed element that targets an API, a web page, or a file, represented
by a button in the Salesforce Chatter feed UI.

`CustomButton` When clicked, opens a URL or a Visualforce page in a window or executes JavaScript.

`InvocableAction` An invocable action such as posting to Chatter.

`ProductivityAction` Productivity actions are predefined by Salesforce and are attached to a limited set
of objects. You can’t edit or delete productivity actions.

`QuickAction` A global or object-specific action.

`StandardButton` A predefined Salesforce button such as New, Edit, and Delete.

### PrimaryTabComponents Class

Represents custom console components on primary tabs in the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PrimaryTabComponents” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PrimaryTabComponents Properties

PrimaryTabComponents Methods

#### PrimaryTabComponents Properties

### The following are properties for PrimaryTabComponents .


Apex Reference Guide PrimaryTabComponents Class

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### PrimaryTabComponents Methods The following are methods for PrimaryTabComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide QuickActionList Class

Return Value

Type: Object

### QuickActionList Class

Represents the list of actions associated with the page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### QuickActionList Properties QuickActionList Methods QuickActionList Properties

### The following are properties for QuickActionList .

IN THIS SECTION:

##### quickActionListItems
### List of QuickActionList objects.

##### quickActionListItems

### List of QuickActionList objects.

Signature

```
   public List<Metadata.QuickActionListItem> quickActionListItems {get; set;}

```

Property Value

Type: List<Metadata.QuickActionListItem>

#### QuickActionList Methods

### The following are methods for QuickActionList .


### Apex Reference Guide QuickActionListItem Class

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### QuickActionListItem Class Represents an action in the QuickActionList .

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### QuickActionListItem Properties

QuickActionListItem Methods

#### QuickActionListItem Properties

### The following are properties for QuickActionListItem .

IN THIS SECTION:

##### quickActionName

The API name of the action.

##### quickActionName

The API name of the action.


### Apex Reference Guide RelatedContent Class

Signature

```
   public String quickActionName {get; set;}

```

Property Value

Type: String

#### QuickActionListItem Methods The following are methods for QuickActionListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedContent Class

Represents the Mobile Cards section of the page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContent” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

RelatedContent Properties

RelatedContent Methods


### Apex Reference Guide RelatedContentItem Class

#### RelatedContent Properties The following are properties for RelatedContent .

IN THIS SECTION:

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

Signature

```
   public List<Metadata.RelatedContentItem> relatedContentItems {get; set;}

```

Property Value

Type: List<Metadata.RelatedContentItem>

#### RelatedContent Methods The following are methods for RelatedContent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedContentItem Class

#### Represents an individual item in the RelatedContent list.

Namespace

Metadata


Apex Reference Guide RelatedContentItem Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContentItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedContentItem Properties RelatedContentItem Methods RelatedContentItem Properties The following are properties for RelatedContentItem .

IN THIS SECTION:

##### layoutItem

An individual layout item in the Mobile Cards section.

##### layoutItem

An individual layout item in the Mobile Cards section.

Signature

```
   public Metadata.LayoutItem layoutItem {get; set;}

```

Property Value

Type: Metadata.LayoutItem

#### RelatedContentItem Methods The following are methods for RelatedContentItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide RelatedList Class

Return Value

Type: Object

### RelatedList Class

Represents related list custom components on the sidebars of the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedList Properties

RelatedList Methods

#### RelatedList Properties

### The following are properties for RelatedList .

IN THIS SECTION:

##### hideOnDetail

When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

name
The name of the component as it appears to console users.

##### hideOnDetail

When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

Signature

```
   public Boolean hideOnDetail {get; set;}

```

Property Value

Type: Boolean


### Apex Reference Guide RelatedListItem Class

##### name

The name of the component as it appears to console users.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

#### RelatedList Methods The following are methods for RelatedList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedListItem Class

Represents an item in the related list in a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedListItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

RelatedListItem Properties

RelatedListItem Methods


Apex Reference Guide RelatedListItem Class

#### RelatedListItem Properties The following are properties for RelatedListItem .

IN THIS SECTION:

##### customButtons

A list of custom buttons used in the related list.

##### excludeButtons

A list of excluded related-list buttons.

fields
A list of fields displayed in the related list. Uses aliases instead of field or API names.

quickActions
A list of quick actions used on the related list.

relatedList
The name of the related list.

sortField
The name of the field used for sorting.

sortOrder
When `sortField` is set, the `sortOrder` property determines the sort order.

##### customButtons

A list of custom buttons used in the related list.

Signature

```
   public List<String> customButtons {get; set;}

```

Property Value

Type: List<String>

For more information, see “Define Custom Buttons and Links” in the Salesforce online help.

##### excludeButtons

A list of excluded related-list buttons.

Signature

```
   public List<String> excludeButtons {get; set;}

```

Property Value

Type: List<String>


Apex Reference Guide RelatedListItem Class

##### fields

A list of fields displayed in the related list. Uses aliases instead of field or API names.

Signature

```
   public List<String> fields {get; set;}

```

Property Value

Type: List<String>

##### **`quickActions`**

A list of quick actions used on the related list.

Signature

```
   public List<String> quickActions {get; set;}

```

Property Value

Type: List<String>

##### relatedList

The name of the related list.

Signature

```
   public String relatedList {get; set;}

```

Property Value

Type: String

##### sortField

The name of the field used for sorting.

Signature

```
   public String sortField {get; set;}

```

Property Value

Type: String

##### sortOrder When sortField is set, the sortOrder property determines the sort order.


### Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public Metadata.SortOrder sortOrder {get; set;}

```

Property Value

Type: Metadata.SortOrder

#### RelatedListItem Methods The following are methods for RelatedListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ReportChartComponentLayoutItem Class

Represents the settings for a report chart on a standard or custom page.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“ReportChartComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

ReportChartComponentLayoutItem Properties

ReportChartComponentLayoutItem Methods


Apex Reference Guide ReportChartComponentLayoutItem Class

#### ReportChartComponentLayoutItem Properties The following are properties for ReportChartComponentLayoutItem .

IN THIS SECTION:

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.

##### contextFilterableField

Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for
the parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match
for a chart to return relevant data.

error
Error string that is populated only when an error occurs in the underlying report.

hideOnError
Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any
data except the error. Set the attribute to true to hide the chart from a page on error.

includeContext
If true, filters the report chart to return data that’s relevant to the page.

reportName
Unique development name of a report that includes a chart.

showTitle
If true, applies the title from the report to the chart.

size
Size of the displayed chart. The default is medium.

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.

Signature

```
   public Boolean cacheData {get; set;}

```

Property Value

Type: Boolean

##### contextFilterableField

Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for the
parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match for a chart
to return relevant data.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public String contextFilterableField {get; set;}

```

Property Value

Type: String

##### error

Error string that is populated only when an error occurs in the underlying report.

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### hideOnError

Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any data
except the error. Set the attribute to true to hide the chart from a page on error.

Signature

```
   public Boolean hideOnError {get; set;}

```

Property Value

Type: Boolean

##### includeContext

If true, filters the report chart to return data that’s relevant to the page.

Signature

```
   public Boolean includeContext {get; set;}

```

Property Value

Type: Boolean

##### reportName

Unique development name of a report that includes a chart.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public String reportName {get; set;}

```

Property Value

Type: String

##### showTitle

If true, applies the title from the report to the chart.

Signature

```
   public Boolean showTitle {get; set;}

```

Property Value

Type: Boolean

##### size

Size of the displayed chart. The default is medium.

Signature

```
   public Metadata.ReportChartComponentSize size {get; set;}

```

Property Value

Type: Metadata.ReportChartComponentSize

#### ReportChartComponentLayoutItem Methods The following are methods for ReportChartComponentLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide ReportChartComponentSize Enum

Return Value

Type: Object

### ReportChartComponentSize Enum

Describes the size of the displayed report chart component.

Enum Values

The following are the values of the `Metadata.ReportChartComponentSize` enum.

**Value** **Description**

`LARGE` Large chart size.

`MEDIUM` Medium chart size.

`SMALL` Small chart size.

### SidebarComponent Class

Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars of the
Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SidebarComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SidebarComponent Properties

SidebarComponent Methods

#### SidebarComponent Properties

### The following are properties for SidebarComponent .

IN THIS SECTION:

componentType
Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and
“CaseExperts”.


Apex Reference Guide SidebarComponent Class

##### createAction

If the component is a lookup field, the name of the quick action used to create a record.

enableLinking
If the component is a lookup field, lets users associate a record with this field.

height
The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

knowledgeOneEnable
Indicates if the component is enabled for Knowledge One.

label
The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

lookup
If the component is a lookup field, the name of the field.

page_x
If the component is a Visualforce page, the name of the Visualforce page.

relatedLists
If the component is a related list component, the list of related list names.

unit
The unit of measurement (pixels or percent) for the height and width of the component in the container.

updateAction
If the component is a lookup field, the name of the quick action used to update a record.

width
The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

##### componentType

Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and “CaseExperts”.

Signature

```
   public String componentType {get; set;}

```

Property Value

Type: String

##### createAction

If the component is a lookup field, the name of the quick action used to create a record.

Signature

```
   public String createAction {get; set;}

```


Apex Reference Guide SidebarComponent Class

Property Value

Type: String

##### enableLinking

If the component is a lookup field, lets users associate a record with this field.

Signature

```
   public Boolean enableLinking {get; set;}

```

Property Value

Type: Boolean

##### height

The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### knowledgeOneEnable

Indicates if the component is enabled for Knowledge One.

Signature

```
   public Boolean knowledgeOneEnable {get; set;}

```

Property Value

Type: Boolean

##### label

The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String


Apex Reference Guide SidebarComponent Class

##### lookup

If the component is a lookup field, the name of the field.

Signature

```
   public String lookup {get; set;}

```

Property Value

Type: String

##### page_x

If the component is a Visualforce page, the name of the Visualforce page.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

##### relatedLists

If the component is a related list component, the list of related list names.

Signature

```
   public List<Metadata.RelatedList> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedList>

##### unit

The unit of measurement (pixels or percent) for the height and width of the component in the container.

Signature

```
   public String unit {get; set;}

```

Property Value

Type: String

##### updateAction

If the component is a lookup field, the name of the quick action used to update a record.


### Apex Reference Guide SortOrder Enum

Signature

```
   public String updateAction {get; set;}

```

Property Value

Type: String

##### width

The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### SidebarComponent Methods The following are methods for SidebarComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SortOrder Enum

Describes the sort order of a related list.

Enum Values

The following are the values of the `Metadata.SortOrder` enum.


### Apex Reference Guide StatusCode Enum

**Value** **Description**

`Asc_x` Sort in ascending order.

`Desc_x` Sort in descending order.

### StatusCode Enum

Describes the status code for an unsuccessful component deploy.

Enum Values

The following are the values of the `Metadata.StatusCode` enum.

**Value** **Description**

`INVALID_SCS_INBOUND_USER` Log in as the RunAs user configured in your SCS setup.

`REQUIRE_CONNECTED_APP_SCS` SCS Connected App is not installed.

`REQUIRE_CONNECTED_APP_SESSION_SCS` To use the SCS connected app, the user must be authenticated.

`REQUIRE_RUNAS_USER` A RunAs user must be configured in your org.

SEE ALSO:

DeployProblemType Enum

### SubtabComponents Class

Represents custom console components on subtabs in the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SubtabComponents” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SubtabComponents Properties

SubtabComponents Methods

#### SubtabComponents Properties

### The following are properties for SubtabComponents .


Apex Reference Guide SubtabComponents Class

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### SubtabComponents Methods The following are methods for SubtabComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide SummaryLayoutStyleEnum Enum

Return Value

Type: Object

### SummaryLayoutStyleEnum Enum Describes the highlights panel style for a SummaryLayout .

Enum Values

The following are the values of the `Metadata.SummaryLayoutStyleEnum` enum.

**Value** **Description**

`CaseInteraction` Case interaction style.

`ChildServiceReportTemplateStyle` Child service report template style.

`DefaultQuoteTemplate` Default quote template style.

`DefaultServiceReportTemplate` Default service report style

`Default_x` Default style.

`PathAssistant` Path assisstant style.

`QuickActionLayoutLeftRight` Quick action left-right layout style.

`QuickActionLayoutTopDown` Quick action top-down layout style.

`QuoteTemplate` Quote template style.

`ServiceReportTemplate` Service report style.

### SummaryLayout Class

Controls the appearance of the highlights panel, which summarizes key fields in a grid at the top of a page layout, when Case Feed is
enabled.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayout” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

SummaryLayout Properties

SummaryLayout Methods


Apex Reference Guide SummaryLayout Class

#### SummaryLayout Properties The following are properties for SummaryLayout .

IN THIS SECTION:

##### masterLabel

The name of the layout label.

##### sizeX

Number of columns in the highlights pane, between 1 and 4 (inclusive).

sizeY
Number of rows in each column, either 1 or 2.

sizeZ
If provided, the setting is not visible to users.

summaryLayoutItems
Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

summaryLayoutStyle
Specifies the panel style.

##### masterLabel

The name of the layout label.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public String masterLabel {get; set;}

```

Property Value

Type: String

##### sizeX

Number of columns in the highlights pane, between 1 and 4 (inclusive).

Signature

```
   public Integer sizeX {get; set;}

```

Property Value

Type: Integer


Apex Reference Guide SummaryLayout Class

##### sizeY

Number of rows in each column, either 1 or 2.

Signature

```
   public Integer sizeY {get; set;}

```

Property Value

Type: Integer

##### sizeZ

If provided, the setting is not visible to users.

Signature

```
   public Integer sizeZ {get; set;}

```

Property Value

Type: Integer

##### summaryLayoutItems

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

Signature

```
   public List<Metadata.SummaryLayoutItem> summaryLayoutItems {get; set;}

```

Property Value

Type: List<Metadata.SummaryLayoutItem>

##### summaryLayoutStyle

Specifies the panel style.

Signature

```
   public Metadata.SummaryLayoutStyleEnum summaryLayoutStyle {get; set;}

```

Property Value

Type: Metadata.SummaryLayoutStyleEnum


### Apex Reference Guide SummaryLayoutItem Class

#### SummaryLayout Methods The following are methods for SummaryLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SummaryLayoutItem Class

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayoutItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SummaryLayoutItem Properties

SummaryLayoutItem Methods

#### SummaryLayoutItem Properties

### The following are properties for SummaryLayoutItem .

IN THIS SECTION:

customLink
The custom link reference.


Apex Reference Guide SummaryLayoutItem Class

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .

##### posY

The item's row position in the highlights panel grid. Must be within the range of `sizeY` .

posZ
Reserved for future use. If provided, the setting is not visible to users.

##### customLink

The custom link reference.

Signature

```
   public String customLink {get; set;}

```

Property Value

Type: String

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .

Signature

```
   public Integer posX {get; set;}

```

Property Value

Type: Integer

##### posY

The item's row position in the highlights panel grid. Must be within the range of `sizeY` .


### Apex Reference Guide UiBehavior Enum

Signature

```
   public Integer posY {get; set;}

```

Property Value

Type: Integer

##### posZ

Reserved for future use. If provided, the setting is not visible to users.

Signature

```
   public Integer posZ {get; set;}

```

Property Value

Type: Integer

#### SummaryLayoutItem Methods The following are methods for SummaryLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### UiBehavior Enum

Describes the behavior for a layout item on a layout page.

Enum Values

The following are the values of the `Metadata.UiBehavior` enum.


## Apex Reference Guide PlaceQuote Namespace

**Value** **Description**

`Edit` The layout field can be edited but is not required.

`Readonly` The layout field is read-only.

`Required` The layout field can be edited and is required.

## PlaceQuote Namespace The PlaceQuote namespace provides classes and methods to create or update quotes with pricing preferences and configuration

options.

[See PlaceQuote namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_placequote.htm)

## Pref_center Namespace

The Pref_center namespace provides an interface, classes, and methods to create and retrieve data in forms in Preference Manager.
Preference Manager, previously called Preference Center, is a feature within the Privacy Center app.

## The following are the classes in the Pref_center namespace.

IN THIS SECTION:

### LoadFormData Class

Retrieve records related to the tokenized record id, and populate the values of a preference form.

LoadParameters Class
Contains methods to retrieve record Id information for parameters passed into the load-form handler.

PreferenceCenterApexHandler Interface
Pass data between your organization and a form in Preference Manager.

SubmitFormData Class
Contains methods to retrieve information on buttons and options selected in a preference form.

SubmitParameters Class
Retrieve record ID information to use with your submit-form handler.

TokenType Enum
Defines the types of values supported by the TokenUtility methods.

TokenUtility Class
Generate authentication tokens to access preference forms.

ValidationResult Class
This class is reserved for future use with Preference Manager.

### LoadFormData Class

Retrieve records related to the tokenized record id, and populate the values of a preference form.


Apex Reference Guide LoadFormData Class

Namespace

Pref_center

Example

#### Use methods in the LoadFormData class to set available and selected values in different form components:

```
   List<System.SelectOption> picklistOptions = new List<System.SelectOption>();

   picklistOptions.add(new System.SelectOption('optIn', 'Opt In'));

   picklistOptions.add(new System.SelectOption('optOut', 'Opt Out'));

   // Set the available options for the picklist

   loadFormData.setOptions('myPicklist', picklistOptions);

   // Add an option to the existing options for the picklist

   loadFormData.addOption('myPicklist', 'optOutAll', 'Opt Out All');

   // Select the 'optIn' option in the picklist

   loadFormData.setSelectedOption('myPicklist', 'optIn');

   List<System.SelectOption> checkboxOptions = new List<System.SelectOption>();

   checkboxOptions.add(new System.SelectOption('yes', 'Yes'));

   checkboxOptions.add(new System.SelectOption('no', 'No'));

   // Set available options for the checkbox group

   loadFormData.setOptions('myCheckbox', checkboxOptions);

   // Select the 'yes' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'yes');

   // Also select the 'no' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'no');

   // Another way to select both the 'yes' and 'no' options in the checkbox group

   loadFormData.setSelectedOptions('myCheckbox', new List<String>{'yes', 'no'});

   // Fill the value in the text input

   loadFormData.setTextValue('myTextInput', 'admin@salesforce.com');

   // Set the hint text for the text input

   loadFormData.setTextHint('myTextInput', 'Email Address');

   // Set the label for the button

   loadFormData.setButtonLabel('myButton', 'Save Preferences');

```

IN THIS SECTION:

#### LoadFormData Constructors

LoadFormData Methods

#### LoadFormData Constructors The following are constructors for LoadFormData .


Apex Reference Guide LoadFormData Class

IN THIS SECTION:

##### LoadFormData(data) Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager. **`LoadFormData(data)`** Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager.

Signature

```
   public LoadFormData(Map<String,pref_center.FieldProperties> data)

```

Parameters

```
   data
```

Type: Map<String,pref_center.FieldProperties>Map

Maps preference form data from the field ID to the field properties.

Usage

This constructor is available in API version 56.0 and later.

#### LoadFormData Methods

##### The following are methods for LoadFormData .

IN THIS SECTION:

addOption(fieldId, value, label)
Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

addOption(fieldId, option)
Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.

addSelectedOption(fieldId, option)
Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a
set value.

setButtonLabel(fieldId, label)
Set the label of a button added to the preference form.

setOptions(fieldId, options)
Add a list of selectable options for a field on a preference form.

setSelectedOption(fieldId, optionValue)
For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

setSelectedOptions(fieldId, options)
For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.


Apex Reference Guide LoadFormData Class

setTextHint(fieldId, hintText)
Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

setTextValue(fieldId, value)
Set the value of a text field in a preference form.

##### **`addOption(fieldId, value, label)`**

Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

Signature

```
   public void addOption(String fieldId, String value, String label)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the selection or text entered in a preference form field.

```
   label
```

Type: String

The label for the value of a field in a preference form.

Return Value

Type: void

##### **`addOption(fieldId, option)`**

Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.

Signature

```
   public void addOption(String fieldId, System.SelectOption option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: System.SelectOption

The option selected on a field in the preference form.


Apex Reference Guide LoadFormData Class

Return Value

Type: void

##### **`addSelectedOption(fieldId, option)`**

Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a set
value.

Signature

```
   public void addSelectedOption(String fieldId, String option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: String

The selectable option being added.

Return Value

Type: void

##### **`setButtonLabel(fieldId, label)`**

Set the label of a button added to the preference form.

Signature

```
   public void setButtonLabel(String fieldId, String label)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   label
```

Type: String

The label for a button added to the preference form.

Return Value

Type: void


Apex Reference Guide LoadFormData Class

##### **`setOptions(fieldId, options)`**

Add a list of selectable options for a field on a preference form.

Signature

```
   public void setOptions(String fieldId, List<System.SelectOption> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   options
```

Type: List<System.SelectOption>

The selectable options for a field in the preference form.

Return Value

Type: void

##### **`setSelectedOption(fieldId, optionValue)`**

For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

Signature

```
   public void setSelectedOption(String fieldId, String optionValue)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   optionValue
```

Type: String

The value for the selected option.

Return Value

Type: void

##### **`setSelectedOptions(fieldId, options)`**

For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.


Apex Reference Guide LoadFormData Class

Signature

```
   public void setSelectedOptions(String fieldId, List<String> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies the checkbox field in the preference form.

```
   options
```

Type: List<String>

The selected options for a field in the preference form.

Return Value

Type: void

##### **`setTextHint(fieldId, hintText)`**

Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

Signature

```
   public void setTextHint(String fieldId, String hintText)

```

Parameters

```
   fieldId
```

Type: String

The ID of the text input field in the preference form.

```
   hintText
```

Type: String

The hint text in the text input field.

Return Value

Type: void

##### **`setTextValue(fieldId, value)`**

Set the value of a text field in a preference form.

Signature

```
   public void setTextValue(String fieldId, String value)

```


### Apex Reference Guide LoadParameters Class

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the value entered for the text field in a preference form.

Return Value

Type: void

### LoadParameters Class

Contains methods to retrieve record Id information for parameters passed into the load-form handler.

Namespace

Pref_center

Example

```
   String userId = loadParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```

IN THIS SECTION:

#### LoadParameters Methods LoadParameters Methods

### The following are methods for LoadParameters .

IN THIS SECTION:

##### getRecordId()

Returns the untokenized version of the record Id.

##### **`getRecordId()`**

Returns the untokenized version of the record Id.

Signature

```
   public String getRecordId()

```


### Apex Reference Guide PreferenceCenterApexHandler Interface

Return Value

Type: String

### PreferenceCenterApexHandler Interface

Pass data between your organization and a form in Preference Manager.

Namespace

Pref_center

IN THIS SECTION:

#### PreferenceCenterApexHandler Methods PreferenceCenterApexHandler Methods

### The following are methods for PreferenceCenterApexHandler .

IN THIS SECTION:

##### load(loadParams, formData, validationResult)

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

submit(loadParams, formData, validationResult)
Updates the changed values of fields when the preference form is submitted.

##### **`load(loadParams, formData, validationResult)`**

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

Signature

```
   public pref_center.LoadFormData load(pref_center.LoadParameters loadParams,

   pref_center.LoadFormData formData, pref_center.ValidationResult validationResult)

```

Parameters

```
   loadParams
```

Type: pref_center.LoadParameters

Retrieve the tokenized record ID.

```
   formData
```

Type: pref_center.LoadFormData

Set the initial values of fields in a form before they are edited.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.


### Apex Reference Guide SubmitFormData Class

Return Value

Type: pref_center.LoadFormData

##### **`submit(loadParams, formData, validationResult)`**

Updates the changed values of fields when the preference form is submitted.

Signature

```
   public void submit(pref_center.SubmitParameters submitParams, pref_center.SubmitFormData

   formData, pref_center.ValidationResult validationResult)

```

Parameters

```
   submitParams
```

Type: pref_center.SubmitParameters

Retrieve the tokenized record Id.

```
   formData
```

Type: pref_center.SubmitFormData

Retrieve the values of fields in a submitted form.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.

Return Value

Type: void

### SubmitFormData Class

Contains methods to retrieve information on buttons and options selected in a preference form.

Namespace

Pref_center

Example

### Use methods in the SubmitFormData class to retrieve the selected values in different form components:

```
   String buttonClickedId = formData.getButtonClicked();

   if (buttonClickedId == 'submitButton') {

   // Handle form submit

   } else if (buttonClickedId == 'cancelButton') {

   // Handle form cancel

   }

   String picklistValueOld = formData.getOldSelectedValue('myPicklist');

```


Apex Reference Guide SubmitFormData Class

```
   String picklistValueNew = formData.getSelectedValue('myPicklist');

   if (picklistValueOld != picklistValueNew) {

   // Do something

   }

   List<String> checkboxValuesOld = formData.getOldSelectedValues('myCheckbox');

   List<String> checkboxValuesNew = formData.getSelectedValues('myCheckbox');

   if (checkboxValuesOld != null && checkboxValuesNew != null && (checkboxValuesOld.size()

   != checkboxValuesNew.size())) {

   // Do something

   }

   String textinputValueOld = formData.getOldStringValue('myTextinput');

   String textinputValueNew = formData.getStringValue('myTextinput');

   if (textinputValueOld != textinputValueNew) {

   // Do something

   }

```

IN THIS SECTION:

#### SubmitFormData Methods SubmitFormData Methods The following are methods for SubmitFormData .

IN THIS SECTION:

getButtonClicked()
Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked
#### button was Submit or Cancel .

getOldSelectedValue(fieldId)
Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is
used for field types such as picklist or radio buttons.

getOldSelectedValues(fieldId)
Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.

getOldStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text, and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

getSelectedValue(fieldId)
Returns the string value that is currently selected for a picklist or radio button field in the preference form.

getSelectedValues(fieldId)
Returns a list of string values that are currently selected on a checkbox field in the preference form.

getStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text.


Apex Reference Guide SubmitFormData Class

##### **`getButtonClicked()`**

Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked button
was **Submit** or **Cancel** .

Signature

```
   public String getButtonClicked()

```

Return Value

Type: String

##### **`getOldSelectedValue(fieldId)`**

Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is used
for field types such as picklist or radio buttons.

Signature

```
   public String getOldSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getOldSelectedValues(fieldId)`**

Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.

Signature

```
   public List<String> getOldSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: List<String>


Apex Reference Guide SubmitFormData Class

##### **`getOldStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text,
and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

Signature

```
   public String getOldStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getSelectedValue(fieldId)`**

Returns the string value that is currently selected for a picklist or radio button field in the preference form.

Signature

```
   public String getSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getSelectedValues(fieldId)`**

Returns a list of string values that are currently selected on a checkbox field in the preference form.

Signature

```
   public List<String> getSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.


### Apex Reference Guide SubmitParameters Class

Return Value

Type: List<String>

##### **`getStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text.

Signature

```
   public String getStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

### SubmitParameters Class

Retrieve record ID information to use with your submit-form handler.

Namespace

Pref_center

Example

```
   String userId = submitParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```

IN THIS SECTION:

#### SubmitParameters Methods SubmitParameters Methods

### The following are methods for SubmitParameters .

IN THIS SECTION:

getRecordId()
Returns the untokenized version of the record ID.


### Apex Reference Guide TokenType Enum

##### **`getRecordId()`**

Returns the untokenized version of the record ID.

Signature

```
   public String getRecordId()

```

Return Value

Type: String

### TokenType Enum

Defines the types of values supported by the TokenUtility methods.

Enum Values

The following are the values of the `pref_center.TokenType` enum.

**Value** **Description**

`EMAIL` Identifies the token as an email address.

`STANDARD` Identifies the token as a Salesforce record ID. This is the default token type.

### TokenUtility Class

Generate authentication tokens to access preference forms.

Namespace

Pref_center

Example

Call the `generateToken()` method to generate a single token for a specified Salesforce record ID:

```
   Individual individual = [SELECT Id FROM Individual LIMIT 1];

   String token = pref_center.TokenUtility.generateToken(individual.Id);

   // Do something with the token

   System.debug(token)

```

Call the `generateTokens()` method to generate tokens in bulk when given a list of Salesforce record IDs:

```
   List<Id> individualIds = new List<Id>();

   // Get Ids of Individuals who have not opted out of tracking

   for (Individual individual : [SELECT Id FROM Individual WHERE HasOptedOutTracking = false])

    {

      individualIds.add(individual.Id);

   }

```


Apex Reference Guide TokenUtility Class

```
   // Generate tokens for the list of Individual record Ids

   Map<String, String> tokens = pref_center.TokenUtility.generateTokens(individualIds);

   String firstIndividualId = individualIds[0];

   // The returned Map has the input record Id as key and the corresponding token as value

   String tokenForFirstIndividual = tokens.get(firstIndividualId);

   // Do something with the token

   System.debug(tokenForFirstIndividual);

```

IN THIS SECTION:

#### TokenUtility Methods TokenUtility Methods The following are methods for TokenUtility .

IN THIS SECTION:

##### generateToken(tokenValue, tokenType)

Returns the authentication token for the specified token value using the given token type.

generateToken(tokenValue)
Returns the authentication token for the specified token value using the default `standard` token type.

generateTokens(tokenValues, tokenType)
Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is
the corresponding token. The given token type is used to generate the tokens.

generateTokens(tokenValues)
Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.

##### **`generateToken(tokenValue, tokenType)`**

Returns the authentication token for the specified token value using the given token type.

Signature

```
   public static String generateToken(String tokenValue, pref_center.TokenType tokenType)

```

Parameters

```
   tokenValue
```

Type: String

The value passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies the
entity that the preference form is acting on.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.


Apex Reference Guide TokenUtility Class

Return Value

Type: String

##### **`generateToken(tokenValue)`**

Returns the authentication token for the specified token value using the default `standard` token type.

Signature

```
   public static String generateToken(String tokenValue)

```

Parameters

```
   tokenValue
```

Type: String

Identifies the entity that the preference form is acting on. The value passed to `LoadParameters.getRecordId()` and
`SubmitParameters.getRecordId()` .

Return Value

Type: String

##### **`generateTokens(tokenValues, tokenType)`**

Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is the
corresponding token. The given token type is used to generate the tokens.

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues,

   pref_center.TokenType tokenType)

```

Parameters

```
   tokenValues
```

Type: List<String>

The values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies
the entity that the preference form is acting on. Contains multiple values to be encrypted with authentication tokens.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>

##### **`generateTokens(tokenValues)`**

Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.


### Apex Reference Guide ValidationResult Class

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues)

```

Parameters

```
   tokenValues
```

Type: List<String>

The list of string values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId().`
Contains multiple values to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>, where the map key is the input value to be tokenized and the map value is the corresponding token.

### ValidationResult Class

This class is reserved for future use with Preference Manager.

Namespace

Pref_center

## Process Namespace The Process namespace provides an interface and classes for passing data between your organization and a flow. The following are the interfaces and classes in the Process namespace.

IN THIS SECTION:

Plugin Interface
Allows you to pass data between your organization and a specified flow.

PluginDescribeResult Class
Describes the input and output parameters for `Process.PluginResult` .

PluginDescribeResult.InputParameter Class
Describes the input parameter for `Process.PluginResult` .

PluginDescribeResult.OutputParameter Class
Describes the output parameter for `Process.PluginResult` .

PluginDescribeResult.ParameterType Enum
Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

PluginRequest Class
Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.


### Apex Reference Guide Plugin Interface

PluginResult Class
Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

SEE ALSO:

_Apex Developer Guide_ [: Passing Data to a Flow Using the Process.Plugin Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_process_plugin_using.htm)

### Plugin Interface

Allows you to pass data between your organization and a specified flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### Plugin Methods

Plugin Example Implementation

#### Plugin Methods

### The following are instance methods for Plugin .

IN THIS SECTION:

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

invoke(request)
Primary method that the system invokes when the class that implements the interface is instantiated.

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

Signature

```
   public Process.PluginDescribeResult describe()

```


Apex Reference Guide Plugin Interface

Return Value

Type: Process.PluginDescribeResult

##### invoke(request)

Primary method that the system invokes when the class that implements the interface is instantiated.

Signature

```
   public Process.PluginResult invoke(Process.PluginRequest request)

```

Parameters

```
   request
```

Type: Process.PluginRequest

Return Value

Type: Process.PluginResult

#### Plugin Example Implementation

```
   global class flowChat implements Process.Plugin {

   // The main method to be implemented. The Flow calls this at run time.

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

```


### Apex Reference Guide PluginDescribeResult Class

```
        return result;

      }

   }

```

Test Class

The following is a test class for the above class.

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

### PluginDescribeResult Class

```

Describes the input and output parameters for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

PluginDescribeResult Constructors

PluginDescribeResult Properties


Apex Reference Guide PluginDescribeResult Class

#### PluginDescribeResult Constructors The following are constructors for PluginDescribeResult .

IN THIS SECTION:

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

Signature

```
   public PluginDescribeResult()

#### PluginDescribeResult Properties The following are properties for PluginDescribeResult .

```

IN THIS SECTION:

##### description

This optional field describes the purpose of the plug-in.

inputParameters
The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.

name
Unique name of the plug-in.

outputParameters
The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

##### description

This optional field describes the purpose of the plug-in.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.


### Apex Reference Guide PluginDescribeResult.InputParameter Class

##### inputParameters

The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.

Signature

```
   public List<Process.PluginDescribeResult.InputParameter> inputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.InputParameter>

##### name

Unique name of the plug-in.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### outputParameters

The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

Signature

```
   public List<Process.PluginDescribeResult.OutputParameter> outputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.OutputParameter>

### PluginDescribeResult.InputParameter Class

Describes the input parameter for `Process.PluginResult` .

Namespace

Process


Apex Reference Guide PluginDescribeResult.InputParameter Class

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### PluginDescribeResult.InputParameter Constructors

PluginDescribeResult.InputParameter Properties

#### PluginDescribeResult.InputParameter Constructors The following are constructors for PluginDescribeResult.InputParameter .

IN THIS SECTION:

##### PluginDescribeResult.InputParameter(name, description, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.

PluginDescribeResult.InputParameter(name, parameterType, required)
Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

##### PluginDescribeResult.InputParameter(name, description, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType


Apex Reference Guide PluginDescribeResult.InputParameter Class

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

##### PluginDescribeResult.InputParameter(name, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

#### PluginDescribeResult.InputParameter Properties

##### The following are properties for PluginDescribeResult.InputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

Name
Unique name of the plug-in.

ParameterType
The data type of the input parameter.

Required
Set to `true` for required and `false` otherwise.

##### Description

This optional field describes the purpose of the plug-in.


Apex Reference Guide PluginDescribeResult.InputParameter Class

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the input parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

##### Required

Set to `true` for required and `false` otherwise.

Signature

```
   public Boolean Required {get; set;}

```

Property Value

Type: Boolean


### Apex Reference Guide PluginDescribeResult.OutputParameter Class PluginDescribeResult.OutputParameter Class

Describes the output parameter for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### PluginDescribeResult.OutputParameter Constructors

PluginDescribeResult.OutputParameter Properties

#### PluginDescribeResult.OutputParameter Constructors

### The following are constructors for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

PluginDescribeResult.OutputParameter(name, parameterType)
Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

Signature

```
   public PluginDescribeResult.OutputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String


Apex Reference Guide PluginDescribeResult.OutputParameter Class

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

##### PluginDescribeResult.OutputParameter(name, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

Signature

```
   public PluginDescribeResult.OutputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

#### PluginDescribeResult.OutputParameter Properties

##### The following are properties for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

Name
Unique name of the plug-in.

ParameterType
The data type of the output parameter.

##### Description

This optional field describes the purpose of the plug-in.


### Apex Reference Guide PluginDescribeResult.ParameterType Enum

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the output parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

### PluginDescribeResult.ParameterType Enum

Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

Enum Values

The following are the values of the `Process.PluginDescribeResult.ParameterType` enum.

**Value** **Description**

`BOOLEAN` A value that can only be assigned `true`, `false`, or `null` .


### Apex Reference Guide PluginRequest Class

**Value** **Description**

`DATE` A value that indicates a particular day.

`DATETIME` A value that indicates a particular day and time, such as a timestamp.

`DECIMAL` A number that includes a decimal point. Decimal is an arbitrary precision number.

`DOUBLE` A 64-bit number that includes a decimal point.

`FLOAT` A floating point number.

`ID` Any valid 18-character Lightning Platform record identifier.

`INTEGER` A 32-bit number that doesn’t include a decimal point.

`LONG` A 64-bit number that doesn’t include a decimal point.

`STRING` Any set of characters surrounded by single quotes.

`TIME` A value that indicates a particular time.

### PluginRequest Class

Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

#### PluginRequest Properties

### The following are properties for PluginRequest .

IN THIS SECTION:

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.


### Apex Reference Guide PluginResult Class

Signature

```
   public MAP<String,ANY> inputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

### PluginResult Class

Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

Namespace

Process

#### PluginResult Properties

### The following are properties for PluginResult .

IN THIS SECTION:

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

Signature

```
   public MAP<String, ANY> outputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

## QuickAction Namespace The QuickAction namespace provides classes and methods for quick actions.


### Apex Reference Guide DescribeAvailableQuickActionResult Class

The following are the classes in the `QuickAction` namespace.

IN THIS SECTION:

### DescribeAvailableQuickActionResult Class

Contains describe metadata information for a quick action that is available for a specified parent.

DescribeLayoutComponent Class
Represents the smallest unit in a layout—a field or a separator.

DescribeLayoutItem Class
Represents an individual item in a `QuickAction.DescribeLayoutRow` .

DescribeLayoutRow Class
Represents a row in a `QuickAction.DescribeLayoutSection` .

DescribeLayoutSection Class
Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

DescribeQuickActionDefaultValue Class
Returns a default value for a quick action.

DescribeQuickActionParameter Class
Represents the parameters corresponding to a quick action.

DescribeQuickActionResult Class
Contains describe metadata information for a quick action.

QuickActionDefaults Class
Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container
of the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

QuickActionDefaultsHandler Interface
The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email
and Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject,
and email body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context
where the action is displayed, such as the case origin (for example, country) and subject.

QuickActionRequest Class
Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
`QuickAction` class methods. Action information includes the action name, context record ID, and record.

QuickActionResult Class
After you initiate a quick action with the `QuickAction` class, use the `QuickActionResult` class for processing action
results.

SendEmailQuickActionDefaults Class
Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action
was invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields
before the standard Email Action is rendered.

### DescribeAvailableQuickActionResult Class

Contains describe metadata information for a quick action that is available for a specified parent.


Apex Reference Guide DescribeAvailableQuickActionResult Class

Namespace

QuickAction

Usage

The QuickAction `describeAvailableQuickActions` method returns an array of available quick action describe result objects
( `QuickAction.DescribeAvailableQuickActionResult` ).

#### DescribeAvailableQuickActionResult Methods The following are methods for DescribeAvailableQuickActionResult . All are instance methods.

IN THIS SECTION:

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

##### getLabel()

The quick action label.

getName()
The quick action name.

getType()
The quick action type.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getLabel()

The quick action label.

Signature

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide DescribeLayoutComponent Class

##### getName()

The quick action name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getType()

The quick action type.

Signature

```
   public String getType()

```

Return Value

Type: String

### DescribeLayoutComponent Class

Represents the smallest unit in a layout—a field or a separator.

Namespace

QuickAction

#### DescribeLayoutComponent Methods

### The following are methods for DescribeLayoutComponent . All are instance methods.

IN THIS SECTION:

getDisplayLines()
Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

getTabOrder()
Returns the tab order for the item in the row.

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

getValue()
Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .


### Apex Reference Guide DescribeLayoutItem Class

##### getDisplayLines()

Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

Signature

```
   public Integer getDisplayLines()

```

Return Value

Type: Integer

##### getTabOrder()

Returns the tab order for the item in the row.

Signature

```
   public Integer getTabOrder()

```

Return Value

Type: Integer

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getValue()

Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .

Signature

```
   public String getValue()

```

Return Value

Type: String

### DescribeLayoutItem Class

Represents an individual item in a `QuickAction.DescribeLayoutRow` .


Apex Reference Guide DescribeLayoutItem Class

Namespace

QuickAction

Usage

For most fields on a layout, there is only one component per layout item. However, in a display-only view, the
`QuickAction.DescribeLayoutItem` might be a composite of the individual fields (for example, an address can consist of
street, city, state, country, and postal code data). On the corresponding edit view, each component of the address field would be split
up into separate `QuickAction.DescribeLayoutItem` s.

#### DescribeLayoutItem Methods The following are methods for DescribeLayoutItem . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the label text for this item.

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.

isEditableForNew()
Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

isEditableForUpdate()
Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

isPlaceholder()
Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

isRequired()
Indicates whether this item is required ( `true` ) or not ( `false` ).

##### getLabel()

Returns the label text for this item.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.


Apex Reference Guide DescribeLayoutItem Class

Signature

```
   public List<QuickAction.DescribeLayoutComponent> getLayoutComponents()

```

Return Value

Type: List<QuickAction.DescribeLayoutComponent>

##### isEditableForNew()

Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForNew()

```

Return Value

Type: Boolean

##### isEditableForUpdate()

Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForUpdate()

```

Return Value

Type: Boolean

##### isPlaceholder()

Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

Signature

```
   public Boolean isPlaceholder()

```

Return Value

Type: Boolean

##### isRequired()

Indicates whether this item is required ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isRequired()

```


### Apex Reference Guide DescribeLayoutRow Class

Return Value

Type: Boolean

Usage

This is useful if, for example, you want to render required fields in a contrasting color.

### DescribeLayoutRow Class

Represents a row in a `QuickAction.DescribeLayoutSection` .

Namespace

QuickAction

Usage

A `QuickAction.DescribeLayoutRow` consists of one or more `QuickAction.DescribeLayoutItem` objects. For
each `QuickAction.DescribeLayoutRow`, a `QuickAction.DescribeLayoutItem` refers either to a specific field or
to an “empty” `QuickAction.DescribeLayoutItem` (one that contains no `QuickAction.DescribeLayoutComponent`
objects). An empty `QuickAction.DescribeLayoutItem` can be returned when a given
`QuickAction.DescribeLayoutRow` is sparse (for example, containing more fields on the right column than on the left column).

#### DescribeLayoutRow Methods

### The following are methods for DescribeLayoutRow . All are instance methods.

IN THIS SECTION:

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

getNumItems()
Returns the number of `QuickAction.DescribeLayoutItem` .

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

Signature

```
   public List<QuickAction.DescribeLayoutItem> getLayoutItems()

```

Return Value

Type: List<QuickAction.DescribeLayoutItem>


### Apex Reference Guide DescribeLayoutSection Class

##### getNumItems()

Returns the number of `QuickAction.DescribeLayoutItem` .

Signature

```
   public Integer getNumItems()

```

Return Value

Type: Integer

### DescribeLayoutSection Class

Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

Namespace

QuickAction

#### DescribeLayoutSection Properties

### The following are properties for DescribeLayoutSection .

##### collapsed

The current view of the record details section: collapsed ( `true` ) or expanded ( `false` ).

Signature

```
   public Boolean collapsed {get; set;}

```

Property Value

Type: Boolean

##### layoutsectionid

The unique ID of the record details section in the layout.

Signature

```
   public Id layoutsectionid {get; set;}

```

Property Value

Type: Id


Apex Reference Guide DescribeLayoutSection Class

#### DescribeLayoutSection Methods The following are methods for DescribeLayoutSection .

IN THIS SECTION:

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

getLayoutRows()
Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

getLayoutSectionId()
Returns the ID of the record details section in the layout.

getParentLayoutId()
#### Returns the ID of the layout upon which this DescribeLayoutSection resides.

getRows()
Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

isCollapsed()
Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

isUseCollapsibleSection()
Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

isUseHeading()
Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getColumns()

```

Return Value

Type: Integer

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

Signature

```
   public String getHeading()

```


Apex Reference Guide DescribeLayoutSection Class

Return Value

Type: String

##### getLayoutRows()

Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

Signature

```
   public List<QuickAction.DescribeLayoutRow> getLayoutRows()

```

Return Value

Type: List<QuickAction.DescribeLayoutRow>

##### getLayoutSectionId()

Returns the ID of the record details section in the layout.

Signature

```
   public Id getLayoutSectionId()

```

Return Value

Type: Id

##### getParentLayoutId()

Returns the ID of the layout upon which this `DescribeLayoutSection` resides.

Signature

```
   public Id getParentLayoutId()

```

Return Value

Type: Id

##### getRows()

Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getRows()

```

Return Value

Type: Integer


### Apex Reference Guide DescribeQuickActionDefaultValue Class

##### isCollapsed()

Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

Signature

```
   public Boolean isCollapsed()

```

Return Value

Type: Boolean

##### isUseCollapsibleSection()

Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseCollapsibleSection()

```

Return Value

Type: Boolean

##### isUseHeading()

Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseHeading()

```

Return Value

Type: Boolean

### DescribeQuickActionDefaultValue Class

Returns a default value for a quick action.

Namespace

QuickAction

Usage

Represents the default values of fields to use in default layouts.


### Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionDefaultValue Methods The following are methods for DescribeQuickActionDefaultValue . All are instance methods.

IN THIS SECTION:

##### getDefaultValue()

Returns the default value of the quick action.

##### getField()

Returns the field name of the action.

##### getDefaultValue()

Returns the default value of the quick action.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getField()

Returns the field name of the action.

Signature

```
   public String getField()

```

Return Value

Type: String

### DescribeQuickActionParameter Class

Represents the parameters corresponding to a quick action.

Namespace

QuickAction

IN THIS SECTION:

DescribeQuickActionParameter Properties
Learn more about the available properties with the `CalculateTaxRequest` class.

DescribeQuickActionParameter Methods


Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionParameter Properties

Learn more about the available properties with the `CalculateTaxRequest` class.

#### The following are properties for DescribeQuickActionParameter .The following are properties for DescribeQuickActionParameter .

IN THIS SECTION:

##### parametername

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a
parameter that is associated with agent quick actions.

##### parametertype

Describes the type of quick action. The type can either be Input or Output.

##### parametervalue

Describes the value of the parameter associated with the quick action.

##### **`parametername`**

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a parameter
that is associated with agent quick actions.

Signature

```
   public String parametername {get; set;}

```

Property Value

Type: String

##### **`parametertype`**

Describes the type of quick action. The type can either be Input or Output.

Signature

```
   public String parametertype {get; set;}

```

Property Value

Type: String

##### **`parametervalue`**

Describes the value of the parameter associated with the quick action.

Signature

```
   public String parametervalue {get; set;}

```


Apex Reference Guide DescribeQuickActionParameter Class

Property Value

Type: String

#### DescribeQuickActionParameter Methods The following are methods for DescribeQuickActionParameter .

IN THIS SECTION:

##### getParameterName()

Returns the name of the parameter associated with the quick action.

##### getParameterType()

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

##### getParameterValue()

Returns the value of the parameter associated with the quick action.

##### **`getParameterName()`**

Returns the name of the parameter associated with the quick action.

Signature

```
   public String getParameterName()

```

Return Value

Type: String

##### **`getParameterType()`**

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

Signature

```
   public String getParameterType()

```

Return Value

Type: String

##### **`getParameterValue()`**

Returns the value of the parameter associated with the quick action.

Signature

```
   public String getParameterValue()

```


### Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

### DescribeQuickActionResult Class

Contains describe metadata information for a quick action.

Namespace

QuickAction

Usage

The QuickAction `describeQuickActions` method returns an array of quick action describe result objects
( `QuickAction.DescribeQuickActionResult` ).

IN THIS SECTION:

#### DescribeQuickActionResult Properties

DescribeQuickActionResult Methods

#### DescribeQuickActionResult Properties

### The following are properties for DescribeQuickActionResult .

IN THIS SECTION:

canvasapplicationname
The name of the Canvas application invoked by the custom action.

colors
Array of color information. Each color is associated with a theme.

contextsobjecttype
The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

defaultvalues
The action’s default values.

flowdevname
If the custom action invokes a flow, the fully qualified name of the flow.

flowrecordidvar
If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

height
The height in pixels of the action pane.

iconname
The name of the icon used for the action. If a custom icon is not used, this value isn’t set.


Apex Reference Guide DescribeQuickActionResult Class

icons
Array of icons. Each icon is associated with a theme.

iconurl
The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

layout
The section of the layout where the action resides.

lightningcomponentbundleid
If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

lightningcomponentbundlename
If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

lightningcomponentqualifiedname
The fully qualified name of the Aura component invoked by the custom action.

lightningwebcomponentbundleid
If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentbundlename
If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentqualifiedname
The fully qualified name of the Lightning web component invoked by the custom action.

miniiconurl
The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

showquickactionlcheader
Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing
the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

showquickactionvfheader
Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

targetparentfield
The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target
object is Contact and the parent object is Account.

targetrecordtypeid
The record type of the target record.

targetsobjecttype
The action’s target object type.

visualforcepagename
The name of the Visualforce page associated with the custom action.

visualforcepageurl
The URL of the Visualforce page associated with the action.


Apex Reference Guide DescribeQuickActionResult Class

width
The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

##### canvasapplicationname

The name of the Canvas application invoked by the custom action.

Signature

```
   public String canvasapplicationname {get; set;}

```

Property Value

Type: String

##### colors

Array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> colors {get; set;}

```

Property Value

Type: List<Schema.DescribeColorResult> on page 3357

##### contextsobjecttype

The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

Signature

```
   public String contextsobjecttype {get; set;}

```

Property Value

Type: String

##### defaultvalues

The action’s default values.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> defaultvalues {get; set;}

```

Property Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>


Apex Reference Guide DescribeQuickActionResult Class

##### flowdevname

If the custom action invokes a flow, the fully qualified name of the flow.

Signature

```
   public String flowdevname {get; set;}

```

Property Value

Type: String

##### flowrecordidvar

If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

Signature

```
   public String flowrecordidvar {get; set;}

```

Property Value

Type: String

Valid values are _`null`_ or _`recordId`_ .

##### height

The height in pixels of the action pane.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### iconname

The name of the icon used for the action. If a custom icon is not used, this value isn’t set.

Signature

```
   public String iconname {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### icons

Array of icons. Each icon is associated with a theme.

Signature

```
   public List<Schema.DescribeIconResult> icons {get; set;}

```

Property Value

Type: List<Schema.DescribeIconResult on page 3381>

If no custom icon was associated with the quick action and the quick action creates a specific object, the icons will correspond to the
##### icons used for the created object. For example, if the quick action creates an Account, the icon array will contain the icons used for

Account.

If a custom icon was associated with the quick action, the array will contain that custom icon.

##### iconurl

The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

Signature

```
   public String iconurl {get; set;}

```

Property Value

Type: String

##### layout

The section of the layout where the action resides.

Signature

```
   public QuickAction.DescribeLayoutSection layout {get; set;}

```

Property Value

Type: QuickAction.DescribeLayoutSection on page 3141

##### lightningcomponentbundleid

If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundleid {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### lightningcomponentbundlename

If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundlename {get; set;}

```

Property Value

Type: String

##### lightningcomponentqualifiedname

The fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String lightningcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundleid`**

If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundleid {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundlename`**

If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundlename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### **`lightningwebcomponentqualifiedname`**

The fully qualified name of the Lightning web component invoked by the custom action.

Signature

```
   public String lightningwebcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### miniiconurl

The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

Signature

```
   public String miniiconurl {get; set;}

```

Property Value

Type: String

##### showquickactionlcheader

Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionlcheader {get; set;}

```

Property Value

Type: Boolean

##### showquickactionvfheader

Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionvfheader {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: Boolean

##### targetparentfield

The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target object
is Contact and the parent object is Account.

Signature

```
   public String targetparentfield {get; set;}

```

Property Value

Type: String

##### targetrecordtypeid

The record type of the target record.

Signature

```
   public String targetrecordtypeid {get; set;}

```

Property Value

Type: String

##### targetsobjecttype

The action’s target object type.

Signature

```
   public String targetsobjecttype {get; set;}

```

Property Value

Type: String

##### visualforcepagename

The name of the Visualforce page associated with the custom action.

Signature

```
   public String visualforcepagename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### visualforcepageurl

The URL of the Visualforce page associated with the action.

Signature

```
   public String visualforcepageurl {get; set;}

```

Property Value

Type: String

##### width

The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### DescribeQuickActionResult Methods The following are methods for DescribeQuickActionResult . All are instance methods.

IN THIS SECTION:

getActionEnumOrId()
Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

getCanvasApplicationName()
Returns the name of the Canvas application, if used.

getColors()
Returns an array of color information. Each color is associated with a theme.

getContextSobjectType()
Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

getDefaultValues()
Returns the default values for a action.

getFlowDevName()
If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

getFlowRecordIdVar()
If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.


Apex Reference Guide DescribeQuickActionResult Class

getHeight()
Returns the height in pixels of the action pane.

getIconName()
Returns the actions’ icon name.

getIconUrl()
Returns the URL of the 32x32 icon used for the action.

getIcons()
Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

getLabel()
Returns the action label.

getLayout()
Returns the layout sections that comprise an action.

getLightningComponentBundleId()
If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

getLightningComponentBundleName()
If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

getLightningComponentQualifiedName()
If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom
action.

getLightningWebComponentBundleId()
If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentBundleName()
If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentQualifiedName()
If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

getMiniIconUrl()
Returns the 16x16 icon URL.

getName()
Returns the action name.

getShowQuickActionLcHeader()
Returns an indication of whether the Lightning component quick action header and footer are shown.

getShowQuickActionVfHeader()
Returns an indication of whether the Visualforce quick action header and footer should be shown.

getSourceSobjectType()
Returns the object type used for the action.

getTargetParentField()
Returns the parent object’s type for the action.


Apex Reference Guide DescribeQuickActionResult Class

getTargetRecordTypeId()
Returns the record type of the targeted record.

getTargetSobjectType()
Returns the action’s target object type.

getType()
Returns a create or custom Visualforce action.

getVisualforcePageName()
If Visualforce is used, returns the name of the associated page for the action.

getVisualforcePageUrl()
Returns the URL of the Visualforce page associated with the action.

getWidth()
If a custom action is created, returns the width in pixels of the action pane.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getCanvasApplicationName()

Returns the name of the Canvas application, if used.

Syntax

```
   public String getCanvasApplicationName()

```

Return Value

Type: String

##### getColors()

Returns an array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```

Return Value

Type: List <Schema.DescribeColorResult>


Apex Reference Guide DescribeQuickActionResult Class

##### getContextSobjectType()

Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

Signature

```
   public String getContextSobjectType()

```

Return Value

Type: String

##### getDefaultValues()

Returns the default values for a action.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> getDefaultValues()

```

Return Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>

##### getFlowDevName()

If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

Signature

```
   public String getFlowDevName()

```

Return Value

Type: String

##### getFlowRecordIdVar()

If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.

Signature

```
   public String getFlowRecordIdVar()

```

Return Value

Type: String

##### getHeight()

Returns the height in pixels of the action pane.


Apex Reference Guide DescribeQuickActionResult Class

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer

##### getIconName()

Returns the actions’ icon name.

Signature

```
   public String getIconName()

```

Return Value

Type: String

##### getIconUrl()

Returns the URL of the 32x32 icon used for the action.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>

##### getLabel()

Returns the action label.

Signature

```
   public String getLabel()

```


Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

##### getLayout()

Returns the layout sections that comprise an action.

Signature

```
   public QuickAction.DescribeLayoutSection getLayout()

```

Return Value

Type: QuickAction.DescribeLayoutSection

##### getLightningComponentBundleId()

If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleId()

```

Return Value

Type: String

##### getLightningComponentBundleName()

If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleName()

```

Return Value

Type: String

##### getLightningComponentQualifiedName()

If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String getLightningComponentQualifiedName()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### **`getLightningWebComponentBundleId()`**

If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String getLightningWebComponentBundleId()

```

Return Value

Type: String

##### **`getLightningWebComponentBundleName()`**

If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

Signature

```
   public String getLightningWebComponentBundleName()

```

Return Value

Type: String

##### **`getLightningWebComponentQualifiedName()`**

If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

Signature

```
   public String getLightningWebComponentQualifiedName()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the 16x16 icon URL.

Signature

```
   public String getMiniIconUrl()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getName()

Returns the action name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getShowQuickActionLcHeader()

Returns an indication of whether the Lightning component quick action header and footer are shown.

Signature

```
   public Boolean getShowQuickActionLcHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getShowQuickActionVfHeader()

Returns an indication of whether the Visualforce quick action header and footer should be shown.

Signature

```
   public Boolean getShowQuickActionVfHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getSourceSobjectType()

Returns the object type used for the action.

Signature

```
   public String getSourceSobjectType()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getTargetParentField()

Returns the parent object’s type for the action.

Signature

```
   public String getTargetParentField()

```

Return Value

Type: String

##### getTargetRecordTypeId()

Returns the record type of the targeted record.

Signature

```
   public String getTargetRecordTypeId()

```

Return Value

Type: String

##### getTargetSobjectType()

Returns the action’s target object type.

Signature

```
   public String getTargetSobjectType()

```

Return Value

Type: String

##### getType()

Returns a create or custom Visualforce action.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getVisualforcePageName()

If Visualforce is used, returns the name of the associated page for the action.


### Apex Reference Guide QuickActionDefaults Class

Signature

```
   public String getVisualforcePageName()

```

Return Value

Type: String

##### getVisualforcePageUrl()

Returns the URL of the Visualforce page associated with the action.

Signature

```
   public String getVisualforcePageUrl()

```

Return Value

Type: String

##### getWidth()

If a custom action is created, returns the width in pixels of the action pane.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

### QuickActionDefaults Class

Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container of
the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

Namespace

### QuickAction

Usage

Note: You cannot extend this abstract class. You can use the getter methods when using it in the context of
QuickAction.QuickActionDefaultsHandler. Salesforce provides a class that extends this class (See
QuickAction.SendEmailQuickActionDefaults.)

IN THIS SECTION:

QuickActionDefaults Methods


Apex Reference Guide QuickActionDefaults Class

#### QuickActionDefaults Methods The following are methods for QuickActionDefaults .

IN THIS SECTION:

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

getTargetSObject()
The target object of the standard Email Action on Case Feed (EmailMessage).

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

Signature

```
   public String getActionName()

```

Return Value

Type: String

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

Signature

```
   public String getActionType()

```

Return Value

Type: String

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

Signature

```
   public Id getContextId()

```


### Apex Reference Guide QuickActionDefaultsHandler Interface

Return Value

Type: Id

##### getTargetSObject()

The target object of the standard Email Action on Case Feed (EmailMessage).

Signature

```
   public SObject getTargetSObject()

```

Return Value

Type: SObject

### QuickActionDefaultsHandler Interface

The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email and
Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject, and email
body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context where the action
is displayed, such as the case origin (for example, country) and subject.

Namespace

### QuickAction

Usage

To specify default values for the standard Email action in the case feed, create a class that implements
`QuickAction.QuickActionDefaultsHandler` .

The `QuickAction.QuickActionDefaultsHandler` interface works in Salesforce Classic and Lightning Experience.

When working in Lightning Experience, keep the following things in mind:

**•** The interface overrides email values set up with predefined IDs.

**•** The interface works with the out-of-the-box Email action provided on cases. You can also use the interface with custom Email actions
for the case object.

**•** The interface in Lightning Experience doesn’t support:

**–** Email attachments

**–** Custom email fields

**–** Visualforce email templates, which are a type of email template available in Salesforce Classic

**•** The From field determines the from address picklist. While you can’t customize this picklist in Send Email action types via the
QuickActionDefaultsHandler interface, you can customize the From Address field. To customize this field, remove the From field
from the SendEmail quick action layout and add the From Address field instead. Then provide a valid and verified from address in
the QuickActionDefaultsHandler code. This address must be the current user’s address, an organization-wide email address that the
current user has access to, or an Email-to-Case routing address.

**•** If your Apex interface adds content to the email body, merge fields display as unresolved. During preview and send, the merge fields
resolve.


Apex Reference Guide QuickActionDefaultsHandler Interface

When you implement this interface, provide an empty parameterless constructor.

IN THIS SECTION:

#### QuickActionDefaultsHandler Methods QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

#### QuickActionDefaultsHandler Methods The following are methods for QuickActionDefaultsHandler .

IN THIS SECTION:

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

Signature

```
   public void onInitDefaults(QuickAction.QuickActionDefaults[] actionDefaults)

```

Parameters

```
   actionDefaults
```

Type: QuickAction.QuickActionDefaults[]

This array contains only one item of type `QuickAction.SendEmailQuickActionDefaults` .

Return Value

Type: void

#### QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

##### In this example, the onInitDefaults method checks whether the element passed in the array is for the standard Email action in

the case feed. Then, it performs a query to retrieve the case that corresponds to the context ID. Next, it sets the value of the BCC address
of the corresponding email message to a default value. The default value is based on the case reason. Finally, it sets the default values
##### of the email template properties. The onInitDefaults method determines the default values based on two criteria: first, whether

a reply action on an email message initiated the call to the method, and second, whether any previous emails attached to the case are
associated with the call.

```
   global class EmailPublisherLoader implements QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherLoader() {

      }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults = null;

        // Check if the quick action is the standard case feed Email action

        for (Integer j = 0; j < defaults.size(); j++) {

           if (defaults.get(j) instanceof QuickAction.SendEmailQuickActionDefaults &&

            defaults.get(j).getTargetSObject().getSObjectType() ==

               EmailMessage.sObjectType &&

            defaults.get(j).getActionName().equals('Case.Email') &&

            defaults.get(j).getActionType().equals('Email')) {

               sendEmailDefaults =

                 (QuickAction.SendEmailQuickActionDefaults)defaults.get(j);

               break;

           }

        }

        if (sendEmailDefaults != null) {

           Case c = [SELECT Status, Reason FROM Case

                 WHERE Id=:sendEmailDefaults.getContextId()];

          EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

           // Set BCC address to make sure each email goes for audit

           emailMessage.BccAddress = getBccAddress(c.Reason);

           /*

           Set Template related fields

           when the In Reply To Id field is null we know the interface

           is called on page load. Here we check if

           there are any previous emails attached to the case and load

           the 'New_Case_Created' or 'Automatic_Response' template.

           When the In Reply To Id field is not null we know that

           the interface is called on click of reply/reply all

           of an email and we load the 'Default_reply_template' template

           */

           if (sendEmailDefaults.getInReplyToId() == null) {

             Integer emailCount = [SELECT count() FROM EmailMessage

                          WHERE ParentId=:sendEmailDefaults.getContextId()];

             if (emailCount!= null && emailCount > 0) {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('Automatic_Response'));

             } else {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('New_Case_Created'));

             }

             sendEmailDefaults.setInsertTemplateBody(false);

             sendEmailDefaults.setIgnoreTemplateSubject(false);

           } else {

             sendEmailDefaults.setTemplateId(

               getTemplateIdHelper('Default_reply_template'));

             sendEmailDefaults.setInsertTemplateBody(false);

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
             sendEmailDefaults.setIgnoreTemplateSubject(true);

           }

        }

      }

      private Id getTemplateIdHelper(String templateApiName) {

        Id templateId = null;

        try {

           templateId = [select id, name from EmailTemplate

                   where developername = : templateApiName].id;

        } catch (Exception e) {

           system.debug('Unble to locate EmailTemplate using name: ' +

             templateApiName + ' refer to Setup | Communications Templates '

               + templateApiName);

        }

        return templateId;

      }

   private String getBccAddress(String reason) {

        if (reason != null && reason.equals('Technical'))

           { return 'support_technical@mycompany.com'; }

        else if (reason != null && reason.equals('Billing'))

           { return 'support_billing@mycompany.com'; }

        else { return 'support@mycompany.com'; }

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Priority is set to _`High`_ . If the Priority is set to _`High`_, the email address
_`managers@acme.com`_ is appended to the BCC field.

```
   global class EmailPublisherForHighPriorityCases implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForHighPriorityCases() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

        EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

        Case c = [SELECT CaseNumber, Priority FROM Case WHERE

   Id=:sendEmailDefaults.getContextId()];

        // If case severity is “High,” append “managers@acme.com” to the existing (and

   possibly blank) BCC field

        if (c.Priority != null && c.Priority.equals('High')) { // Priority is 'High'

           emailMessage.BccAddress = 'managers@acme.com';

        }

      }

   }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Type is set to _`Problem`_ . If the type is set to _`Problem`_, the _`First`_
_`Response`_ email template is inserted into the body of the email.

```
   global class EmailPublisherForCaseType implements QuickAction.QuickActionDefaultsHandler

   {

      // Empty constructor

      global EmailPublisherForCaseType() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

     Case c = [SELECT CaseNumber, Type FROM Case WHERE Id=:sendEmailDefaults.getContextId()];

      // If case type is “Problem,” insert the “First Response” email template

      if (c.CaseNumber != null && c.Type.equals('Problem')) {

        sendEmailDefaults.setTemplateId('Insert Email Template ID Here'); // Set the

   template Id corresponding to First Response

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the email is a Reply or Reply All email. If the email is a Reply or Reply All email,
the corresponding email templates for these emails are inserted into the body of the email.

```
   global class EmailPublisherForReplyAndReplyAll implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForReplyAndReplyAll() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

      // If the email is a “Reply” email, insert the “Reply Email Template” to the email

   body

      if (sendEmailDefaults.getActionName().equals('EmailMessage._Reply')) {

        sendEmailDefaults.setTemplateId('Insert Reply Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

```


### Apex Reference Guide QuickActionRequest Class

```
      // If the email is a “Reply All” email, insert the “Reply All Email Template” to the

   email body

      } else if (sendEmailDefaults.getActionName().equals('EmailMessage._ReplyAll')) {

        sendEmailDefaults.setTemplateId('Insert Reply All Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

   }

### QuickActionRequest Class

```

Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
### QuickAction class methods. Action information includes the action name, context record ID, and record.

Namespace

### QuickAction

Usage

For Apex saved using Salesforce API version 28.0, a parent ID is associated with the QuickActionRequest instead of the context ID.

The constructor of this class takes no arguments:

```
   QuickAction.QuickActionRequest qar = new QuickAction.QuickActionRequest();

```

Example

In this sample, a new quick action is created to create a contact and assign a record to it.

```
   QuickAction.QuickActionRequest req = new QuickAction.QuickActionRequest();

   // Some quick action name

   req.quickActionName = Schema.Account.QuickAction.AccountCreateContact;

   // Define a record for the quick action to create

   Contact c = new Contact();

   c.lastname = 'last name';

   req.record = c;

   // Provide the context ID (or parent ID). In this case, it is an Account record.

   req.contextid = '001xx000003DGcO';

   QuickAction.QuickActionResult res = QuickAction.performQuickAction(req);

```

IN THIS SECTION:

QuickActionRequest Constructors


Apex Reference Guide QuickActionRequest Class

#### QuickActionRequest Methods

SEE ALSO:

QuickAction Class

#### QuickActionRequest Constructors The following are constructors for QuickActionRequest .

IN THIS SECTION:

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

Signature

```
   public QuickActionRequest()

#### QuickActionRequest Methods The following are methods for QuickActionRequest . All are instance methods.

```

IN THIS SECTION:

##### getContextId()

Returns this QuickAction’s context record ID.

getQuickActionName()
Returns this QuickAction’s name.

getRecord()
Returns the QuickAction’s associated record.

setContextId(contextId)
##### Sets this QuickAction’s context ID. Returned by getContextId .

setQuickActionName(name)
Sets this QuickAction’s name. Returned by `getQuickActionName` .

setRecord(record)
Sets a record for this QuickAction. Returned by `getRecord` .

##### getContextId()

Returns this QuickAction’s context record ID.


Apex Reference Guide QuickActionRequest Class

Signature

```
   public Id getContextId()

```

Return Value

Type: ID

##### getQuickActionName()

Returns this QuickAction’s name.

Signature

```
   public String getQuickActionName()

```

Return Value

Type: String

##### getRecord()

Returns the QuickAction’s associated record.

Signature

```
   public SObject getRecord()

```

Return Value

Type: sObject

##### setContextId(contextId)

Sets this QuickAction’s context ID. Returned by `getContextId` .

Signature

```
   public Void setContextId(Id contextId)

```

Parameters

```
   contextId
```

Type: ID

Return Value

Type: Void

Usage

For Apex saved using Salesforce API version 28.0, sets this QuickAction’s parent ID and is returned by `getParentId` .


### Apex Reference Guide QuickActionResult Class

##### setQuickActionName(name)

Sets this QuickAction’s name. Returned by `getQuickActionName` .

Signature

```
   public Void setQuickActionName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: Void

##### setRecord(record)

Sets a record for this QuickAction. Returned by `getRecord` .

Signature

```
   public Void setRecord(SObject record)

```

Parameters

```
   record
```

Type: sObject

Return Value

Type: Void

### QuickActionResult Class After you initiate a quick action with the QuickAction class, use the QuickActionResult class for processing action results.

Namespace

### QuickAction

SEE ALSO:

QuickAction Class

#### QuickActionResult Methods

### The following are methods for QuickActionResult . All are instance methods.


Apex Reference Guide QuickActionResult Class

IN THIS SECTION:

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

##### getIds()

The IDs of the QuickActions being processed.

##### getSuccessMessage()

Returns the success message associated with the quick action.

isCreated()
Returns `true` if the action is created; otherwise, `false` .

isSuccess()
Returns `true` if the action completes successfully; otherwise, `false` .

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getIds()

The IDs of the QuickActions being processed.

Signature

```
   public List<Id> getIds()

```

Return Value

Type: List<Id>

##### getSuccessMessage()

Returns the success message associated with the quick action.

Signature

```
   public String getSuccessMessage()

```

Return Value

Type: String


### Apex Reference Guide SendEmailQuickActionDefaults Class

##### isCreated()

Returns `true` if the action is created; otherwise, `false` .

Signature

```
   public Boolean isCreated()

```

Return Value

Type: Boolean

##### isSuccess()

Returns `true` if the action completes successfully; otherwise, `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### SendEmailQuickActionDefaults Class

Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action was
invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields before
the standard Email Action is rendered.

Namespace

QuickAction

Usage

Note: You cannot instantiate this class. One can use the getters/setters when using it in the context of
`QuickAction.QuickActionDefaultsHandler` .

IN THIS SECTION:

#### SendEmailQuickActionDefaults Methods SendEmailQuickActionDefaults Methods

### The following are methods for SendEmailQuickActionDefaults .


Apex Reference Guide SendEmailQuickActionDefaults Class

IN THIS SECTION:

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject
should replace the original subject (false).

setInsertTemplateBody(keepOriginalBodyContent)
Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the
entire content with the template body (false).

setTemplateId(templateId)
Sets the email template ID to load into the email body.

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

Signature

```
   public List<String> getFromAddressList()

```

Return Value

Type: List<String>

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

Signature

```
   public Id getInReplyToId()

```

Return Value

Type: Id

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject should
replace the original subject (false).

Signature

```
   public void setIgnoreTemplateSubject(Boolean useOriginalSubject)

```


## Apex Reference Guide Reports Namespace

Parameters

```
   useOriginalSubject
```

Type: Boolean

Return Value

Type: void

##### setInsertTemplateBody(keepOriginalBodyContent)

Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the entire
content with the template body (false).

Signature

```
   public void setInsertTemplateBody(Boolean keepOriginalBodyContent)

```

Parameters

```
   keepOriginalBodyContent
```

Type: Boolean

Return Value

Type: void

##### setTemplateId(templateId)

Sets the email template ID to load into the email body.

Signature

```
   public void setTemplateId(Id templateId)

```

Parameters

```
   templateId
```

Type: Id

The template ID.

Return Value

Type: void

## Reports Namespace The Reports namespace provides classes for accessing the same data as is available in the Salesforce Reports and Dashboards REST

API.

## The following are the classes in the Reports namespace.


Apex Reference Guide Reports Namespace

IN THIS SECTION:

AggregateColumn Class
Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas.
Includes name, label, data type, and grouping context.

BucketField Class
Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed
values.

BucketFieldValue Class
Contains information about the report values included in a bucket field.

BucketType Enum
The types of values included in a bucket.

ColumnDataType Enum
The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

ColumnSortOrder Enum
The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

CrossFilter Class
Contains methods and constructors used to work with information about a cross filter.

CsfGroupType Enum
The group level at which the custom summary format aggregate is displayed in a report.

DateGranularity Enum
The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

DetailColumn Class
Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.

Dimension Class
Contains information for each row or column grouping.

EvaluatedCondition Class
Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

EvaluatedConditionOperator Enum
The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to
a value. It is returned by the `getOperator` method.

FilterOperator Class
Contains information about a filter operator, such as display name and API name.

FilterValue Class
Contains information about a filter value, such as the display name and API name.

FormulaType Enum
The format of the numbers in a custom summary formula.

GroupingColumn Class
Contains methods for describing fields that are used for column grouping.

GroupingInfo Class
Contains methods for describing fields that are used for grouping.


Apex Reference Guide Reports Namespace

GroupingValue Class
Contains grouping values for a row or column, including the key, label, and value.

NotificationAction Interface
Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

NotificationActionContext Class
Contains information about the report instance and condition threshold for a report notification.

ReportCsf Class
Contains methods and constructors for working with information about a custom summary formula (CSF).

ReportCurrency Class
Contains information about a currency value, including the amount and currency code.

ReportDataCell Class
Contains the data for a cell in the report, including the display label and value.

ReportDescribeResult Class
Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

ReportDetailRow Class
Contains data cells for a detail row of a report.

ReportDivisionInfo Class
Contains information about the divisions that can be used to filter a report.

ReportExtendedMetadata Class
Contains report extended metadata for a tabular, summary, or matrix report.

ReportFact Class
Contains the fact map for the report, which represents the report’s data values.

ReportFactWithDetails Class
Contains the detailed fact map for the report, which represents the report’s data values.

ReportFactWithSummaries Class
Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

ReportFilter Class
Contains information about a report filter, including column, operator, and value.

ReportFormat Enum
Contains the possible report format types.

ReportFilterType Enum
The types of values included in a report filter type.

ReportInstance Class
Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

ReportManager Class
Runs a report synchronously or asynchronously and with or without details.

ReportMetadata Class
Contains report metadata for a tabular, summary, or matrix report.

ReportResults Class
Contains the results of running a report.


Apex Reference Guide Reports Namespace

ReportScopeInfo Class
Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you
can set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My`
`opportunities` .

ReportScopeValue Class
Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .

ReportType Class
Contains the unique API name and display name for the report type.

ReportTypeColumn Class
Contains detailed report type metadata about a field, including data type, display name, and filter values.

ReportTypeColumnCategory Class
Information about categories of fields in a report type.

ReportTypeMetadata Class
Contains report type metadata, which gives you information about the fields that are available in each section of the report type,
plus filter information for those fields.

SortColumn Class
Contains information about the sort column used in the report.

StandardDateFilter Class
Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.

StandardDateFilterDuration Class
Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display
label of the standard date filter duration as well as the start and end dates.

StandardDateFilterDurationGroup Class
Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that
fall under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar`
`Week`, `Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

StandardFilter Class
Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

StandardFilterInfo Class
Is an abstract base class for an object that provides standard filter information.

StandardFilterInfoPicklist Class
Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value,
and a list of all possible picklist values.

StandardFilterType Enum
The `StandardFilterType` enum describes the type of standard filters in a report. The `getType()` method returns a
`Reports.StandardFilterType` enum value.

SummaryValue Class
Contains summary data for a cell of the report.

ThresholdInformation Class
Contains a list of evaluated conditions for a report notification.


### Apex Reference Guide AggregateColumn Class

TopRows Class
Contains methods and constructors for working with information about a row limit filter.

Reports Exceptions
The `Reports` namespace contains exception classes.

### AggregateColumn Class

Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas. Includes
name, label, data type, and grouping context.

Namespace

Reports

#### AggregateColumn Methods

### The following are methods for AggregateColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the summary field.

##### getLabel()

Returns the localized display name for the summarized or custom summary formula field.

getDataType()
Returns the data type of the summarized or custom summary formula field.

getAcrossGroupingContext()
Returns the column grouping in the report where the summary field is displayed.

getDownGroupingContext()
Returns the row grouping in the report where the summary field is displayed.

##### getName()

Returns the unique API name of the summary field.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name for the summarized or custom summary formula field.


### Apex Reference Guide BucketField Class

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the summarized or custom summary formula field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getAcrossGroupingContext()

Returns the column grouping in the report where the summary field is displayed.

Syntax

```
   public String getAcrossGroupingContext()

```

Return Value

Type: String

##### getDownGroupingContext()

Returns the row grouping in the report where the summary field is displayed.

Syntax

```
   public String getDownGroupingContext()

```

Return Value

Type: String

### BucketField Class

Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed values.

Namespace

Reports


Apex Reference Guide BucketField Class

IN THIS SECTION:

#### BucketField Constructors

BucketField Methods

#### BucketField Constructors The following are constructors for BucketField .

IN THIS SECTION:

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel, sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

BucketField()
Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel,

sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

Signature

```
   public BucketField(Reports.BucketType bucketType, String devloperName, String label,

   Boolean nullTreatedAsZero, String otherBucketLabel, String sourceColumnName,

   List<Reports.BucketFieldValue> values)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

The type of bucket.

```
   devloperName
```

Type: String

API name of the bucket.

```
   label
```

Type: String

User-facing name of the bucket.

```
   nullTreatedAsZero
```

Type: Boolean

Specifies whether null values are converted to zero ( `true` ) or not ( `false` ).

```
   otherBucketLabel
```

Type: String

Name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

```
   sourceColumnName
```

Type: String


Apex Reference Guide BucketField Class

Name of the bucketed field.

```
   values
```

Type: List<Reports.BucketType>

Types of the values included in the bucket.

##### BucketField()

Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketField()

#### BucketField Methods

##### The following are methods for BucketField .

```

IN THIS SECTION:

getBucketType()
Returns the bucket type.

getDevloperName()
Returns the bucket’s API name.

getLabel()
Returns the user-facing name of the bucket.

getNullTreatedAsZero()
Returns `true` if null values are converted to the number zero, otherwise returns `false` .

getOtherBucketLabel()
Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

getSourceColumnName()
Returns the API name of the bucketed field.

getValues()
Returns the report values grouped by the bucket field.

setBucketType(value)
Sets the `BucketType` of the bucket.

setBucketType(bucketType)
Sets the `BucketType` of the bucket.

setDevloperName(devloperName)
Sets the API name of the bucket.

setLabel(label)
Sets the user-facing name of the bucket.

setNullTreatedAsZero(nullTreatedAsZero)
Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).


Apex Reference Guide BucketField Class

setOtherBucketLabel(otherBucketLabel)
Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

setSourceColumnName(sourceColumnName)
Specifies the name of the bucketed field.

setValues(values)
Specifies which type of values are included in the bucket.

toString()
Returns a string.

##### getBucketType()

Returns the bucket type.

Signature

```
   public Reports.BucketType getBucketType()

```

Return Value

Type: Reports.BucketType

##### getDevloperName()

Returns the bucket’s API name.

Signature

```
   public String getDevloperName()

```

Return Value

Type: String

##### getLabel()

Returns the user-facing name of the bucket.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getNullTreatedAsZero()

Returns `true` if null values are converted to the number zero, otherwise returns `false` .


Apex Reference Guide BucketField Class

Signature

```
   public Boolean getNullTreatedAsZero()

```

Return Value

Type: Boolean

##### getOtherBucketLabel()

Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

Signature

```
   public String getOtherBucketLabel()

```

Return Value

Type: String

##### getSourceColumnName()

Returns the API name of the bucketed field.

Signature

```
   public String getSourceColumnName()

```

Return Value

Type: String

##### getValues()

Returns the report values grouped by the bucket field.

Signature

```
   public List<Reports.BucketFieldValue> getValues()

```

Return Value

Type: List on page 3874<Reports.BucketFieldValue>

##### setBucketType(value)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(String value)

```


Apex Reference Guide BucketField Class

Parameters

```
   value
```

Type: String

See the Reports.BucketType enum for valid values.

Return Value

Type: void

##### setBucketType(bucketType)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(Reports.BucketType bucketType)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

Return Value

Type: void

##### setDevloperName(devloperName)

Sets the API name of the bucket.

Signature

```
   public void setDevloperName(String devloperName)

```

Parameters

```
   devloperName
```

Type: String

The API name to assign to the bucket.

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the bucket.


Apex Reference Guide BucketField Class

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setNullTreatedAsZero(nullTreatedAsZero)

Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).

Signature

```
   public void setNullTreatedAsZero(Boolean nullTreatedAsZero)

```

Parameters

```
   nullTreatedAsZero
```

Type: Boolean

Return Value

Type: void

##### setOtherBucketLabel(otherBucketLabel)

Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

Signature

```
   public void setOtherBucketLabel(String otherBucketLabel)

```

Parameters

```
   otherBucketLabel
```

Type: String

Return Value

Type: void

##### setSourceColumnName(sourceColumnName)

Specifies the name of the bucketed field.


### Apex Reference Guide BucketFieldValue Class

Signature

```
   public void setSourceColumnName(String sourceColumnName)

```

Parameters

```
   sourceColumnName
```

Type: String

Return Value

Type: void

##### setValues(values)

Specifies which type of values are included in the bucket.

Signature

```
   public void setValues(List<Reports.BucketFieldValue> values)

```

Parameters

```
   values
```

Type: List on page 3874<Reports.BucketFieldValue>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BucketFieldValue Class

Contains information about the report values included in a bucket field.

Namespace

Reports


Apex Reference Guide BucketFieldValue Class

IN THIS SECTION:

#### BucketFieldValue Constructors BucketFieldValue Methods BucketFieldValue Constructors The following are constructors for BucketFieldValue .

IN THIS SECTION:

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

##### BucketFieldValue()

Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

Signature

```
   public BucketFieldValue(String label, List<String> sourceDimensionValues, Double

   rangeUpperBound)

```

Parameters

```
   label
```

Type: String

The user-facing name of the bucket.

```
   sourceDimensionValues
```

Type: List on page 3874<String>

A list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

```
   rangeUpperBound
```

Type: Double

The greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

##### BucketFieldValue()

Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketFieldValue()

#### BucketFieldValue Methods The following are methods for BucketFieldValue .

```


Apex Reference Guide BucketFieldValue Class

IN THIS SECTION:

##### getLabel()

Returns the user-facing name of the bucket category.

##### getRangeUpperBound()

Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

##### getSourceDimensionValues()

Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of
type `TEXT` ).

setLabel(label)
Set the user-facing name of the bucket category.

setRangeUpperBound(rangeUpperBound)
Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

setSourceDimensionValues(sourceDimensionValues)
Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).

toString()
Returns a string.

##### getLabel()

Returns the user-facing name of the bucket category.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getRangeUpperBound()

Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public Double getRangeUpperBound()

```

Return Value

Type: Double

##### getSourceDimensionValues()

Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).


Apex Reference Guide BucketFieldValue Class

Signature

```
   public List<String> getSourceDimensionValues()

```

Return Value

Type: List<String>

##### setLabel(label)

Set the user-facing name of the bucket category.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setRangeUpperBound(rangeUpperBound)

Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public void setRangeUpperBound(Double rangeUpperBound)

```

Parameters

```
   rangeUpperBound
```

Type: Double

Return Value

Type: void

##### setSourceDimensionValues(sourceDimensionValues)

Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

Signature

```
   public void setSourceDimensionValues(List<String> sourceDimensionValues)

```


### Apex Reference Guide BucketType Enum

Parameters

```
   sourceDimensionValues
```

Type: List<String>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BucketType Enum

The types of values included in a bucket.

Enum Values

The following are the values of the `Reports.BucketType` enum.

**Value** **Description**

`NUMBER` Numeric values

`PICKLIST` Picklist values

`TEXT` String values

### ColumnDataType Enum

The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ColumnDataType` enum.


### Apex Reference Guide ColumnSortOrder Enum

**Value** **Description**

`BOOLEAN_DATA` Boolean ( `true` or `false` ) values

`COMBOBOX_DATA` Comboboxes, which provide a set of enumerated values and enable the user to
specify a value that is not in the list

`CURRENCY_DATA` Currency values

`DATETIME_DATA` DateTime values

`DATE_DATA` Date values

`DOUBLE_DATA` Double values

`EMAIL_DATA` Email addresses

`ID_DATA` An object’s Salesforce ID

`INT_DATA` Integer values

`MULTIPICKLIST_DATA` Multi-select picklists, which provide a set of enumerated values from which multiple
values can be selected

`PERCENT_DATA` Percent values

`PHONE_DATA` Phone numbers. Values can include alphabetic characters. Client applications are
responsible for phone number formatting.

`PICKLIST_DATA` Single-select picklists, which provide a set of enumerated values from which only
one value can be selected

`REFERENCE_DATA` Cross-references to another object, analogous to a foreign key field

`STRING_DATA` String values

`TEXTAREA_DATA` String values that are displayed as multiline text fields

`TIME_DATA` Time values

`URL_DATA` URL values that are displayed as hyperlinks

### ColumnSortOrder Enum

The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

Namespace

Reports

Usage

The `GroupingInfo.getColumnSortOrder()` method returns a `Reports.ColumnSortOrder` enum value. The
`GroupingInfo.setColumnSortOrder()` method takes the enum value as an argument.


### Apex Reference Guide CrossFilter Class

Enum Values

The following are the values of the `Reports.ColumnSortOrder` enum.

**Value** **Description**

`ASCENDING` Sort data in ascending order (A–Z)

`DESCENDING` Sort data in descending order (Z–A)

### CrossFilter Class

Contains methods and constructors used to work with information about a cross filter.

Namespace

Reports

IN THIS SECTION:

#### CrossFilter Constructors

CrossFilter Methods

#### CrossFilter Constructors

### The following are constructors for CrossFilter .

IN THIS SECTION:

##### CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)

Creates an instance of the `Reports.CrossFilter` class using the specified parameters.

CrossFilter()
Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

##### CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)

Creates an instance of the `Reports.CrossFilter` class using the specified parameters.

Signature

```
   public CrossFilter(List<Reports.ReportFilter> criteria, Boolean includesObject, String

   primaryEntityField, String relatedEntity, String relatedEntityJoinField)

```

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Information about how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .


Apex Reference Guide CrossFilter Class

```
   includesObject
```

Type: Boolean

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true) or not (false).`

```
   primaryEntityField
```

Type: String

The name of the object on which the cross filter is evaluated.

```
   relatedEntity
```

Type: String

The name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

```
   relatedEntityJoinField
```

Type: String

The name of the field used to join the `primaryEntityField` and `relatedEntity` .

##### CrossFilter()

Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

Signature

```
   public CrossFilter()

#### CrossFilter Methods

##### The following are methods for CrossFilter .

```

IN THIS SECTION:

getCriteria()
Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

getIncludesObject()
Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

getPrimaryEntityField()
Returns the name of the object on which the cross filter is evaluated.

getRelatedEntity()
Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

getRelatedEntityJoinField()
Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

setCriteria(criteria)
Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

setIncludesObject(includesObject)
Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).


Apex Reference Guide CrossFilter Class

setPrimaryEntityField(primaryEntityField)
Specifies the name of the object on which the cross filter is evaluated.

setRelatedEntity(relatedEntity)
Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

setRelatedEntityJoinField(relatedEntityJoinField)
Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

toString()
Returns a string.

##### getCriteria()

Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

Signature

```
   public List<Reports.ReportFilter> getCriteria()

```

Return Value

Type: List<Reports.ReportFilter>

##### getIncludesObject()

Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

Signature

```
   public Boolean getIncludesObject()

```

Return Value

Type: Boolean

##### getPrimaryEntityField()

Returns the name of the object on which the cross filter is evaluated.

Signature

```
   public String getPrimaryEntityField()

```

Return Value

Type: String

##### getRelatedEntity()

Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.


Apex Reference Guide CrossFilter Class

Signature

```
   public String getRelatedEntity()

```

Return Value

Type: String

##### getRelatedEntityJoinField()

Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public String getRelatedEntityJoinField()

```

Return Value

Type: String

##### setCriteria(criteria)

Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

Signature

```
   public void setCriteria(List<Reports.ReportFilter> criteria)

```

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Return Value

Type: void

##### setIncludesObject(includesObject)

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).

Signature

```
   public void setIncludesObject(Boolean includesObject)

```

Parameters

```
   includesObject
```

Type: Boolean


Apex Reference Guide CrossFilter Class

Return Value

Type: void

##### setPrimaryEntityField(primaryEntityField)

Specifies the name of the object on which the cross filter is evaluated.

Signature

```
   public void setPrimaryEntityField(String primaryEntityField)

```

Parameters

```
   primaryEntityField
```

Type: String

Return Value

Type: void

##### setRelatedEntity(relatedEntity)

Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

Signature

```
   public void setRelatedEntity(String relatedEntity)

```

Parameters

```
   relatedEntity
```

Type: String

Return Value

Type: void

##### setRelatedEntityJoinField(relatedEntityJoinField)

Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public void setRelatedEntityJoinField(String relatedEntityJoinField)

```

Parameters

```
   relatedEntityJoinField
```

Type: String


### Apex Reference Guide CsfGroupType Enum

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### CsfGroupType Enum

The group level at which the custom summary format aggregate is displayed in a report.

Enum Values

The following are the values of the `Reports.CsfGroupType` enum.

**Value** **Description**

`ALL` The aggregate is displayed at the end of every summary row.

`CUSTOM` The aggregate is displayed at specified grouping levels.

`GRAND_TOTAL` The aggregate is displayed only at the grand total level.

### DateGranularity Enum

The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

Namespace

Reports

Usage

The `GroupingInfo.getDateGranularity` method returns a `Reports.DateGranularity` enum value. The
`GroupingInfo.setDateGranularity` method takes the enum value as an argument.

Enum Values

The following are the values of the `Reports.DateGranularity` enum.


### Apex Reference Guide DetailColumn Class

**Value** **Description**

`DAY` The day of the week (Monday–Sunday)

`DAY_IN_MONTH` The day of the month (1–31)

`FISCAL_PERIOD` The fiscal period

`FISCAL_QUARTER` The fiscal quarter

`FISCAL_WEEK` The fiscal week

`FISCAL_YEAR` The fiscal year

`MONTH` The month (January–December)

`MONTH_IN_YEAR` The month number (1–12)

`NONE` No date grouping

`QUARTER` The quarter number (1–4)

`WEEK` The week number (1–52)

`YEAR` The year number (####)

### DetailColumn Class

Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.

Namespace

Reports

#### DetailColumn Instance Methods

### The following are instance methods for DetailColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the detail column field.

getLabel()
Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed
data.

getDataType()
Returns the data type of a detail column field.

##### getName()

Returns the unique API name of the detail column field.


### Apex Reference Guide Dimension Class

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed data.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of a detail column field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

### Dimension Class

Contains information for each row or column grouping.

Namespace

Reports

#### Dimension Methods

### The following are methods for Dimension . All are instance methods.

IN THIS SECTION:

getGroupings()
Returns information for each row or column grouping as a list.


### Apex Reference Guide EvaluatedCondition Class

##### getGroupings()

Returns information for each row or column grouping as a list.

Syntax

```
   public List<Reports.GroupingValue> getGroupings()

```

Return Value

Type: List<Reports.GroupingValue>

### EvaluatedCondition Class

Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

Namespace

Reports

IN THIS SECTION:

#### EvaluatedCondition Constructors

EvaluatedCondition Methods

#### EvaluatedCondition Constructors

### The following are constructors for EvaluatedCondition .

IN THIS SECTION:

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue, displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue,

displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

Signature

```
   public EvaluatedCondition(String aggregateName, String aggregateLabel, Double

   compareToValue, Double aggregateValue, String displayCompareTo, String displayValue,

   Reports.EvaluatedConditionOperator operator)

```

Parameters

```
   aggregateName
```

Type: String


Apex Reference Guide EvaluatedCondition Class

The unique API name of the aggregate.

```
   aggregateLabel
```

Type: String

The localized display name of the aggregate.

```
   compareToValue
```

Type: Double

The value that the aggregate is compared to in the condition.

```
   aggregateValue
```

Type: Double

The actual value of the aggregate when the report is run.

```
   displayCompareTo
```

Type: String

The value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency is
$20.00 or USD20.00 instead of 20.00.

```
   displayValue
```

Type: String

The value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

```
   operator
```

Type: Reports.EvaluatedConditionOperator

The operator used in the condition.

#### EvaluatedCondition Methods The following are methods for EvaluatedCondition .

IN THIS SECTION:

getAggregateLabel()
Returns the localized display name of the aggregate.

getAggregateName()
Returns the unique API name of the aggregate.

getCompareTo()
Returns the value that the aggregate is compared to in the condition.

getDisplayCompareTo()
Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

getDisplayValue()
Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00
or USD20.00 instead of 20.00.

getOperator()
Returns the operator used in the condition.


Apex Reference Guide EvaluatedCondition Class

getValue()
Returns the actual value of the aggregate when the report is run.

##### getAggregateLabel()

Returns the localized display name of the aggregate.

Signature

```
   public String getAggregateLabel()

```

Return Value

Type: String

##### getAggregateName()

Returns the unique API name of the aggregate.

Signature

```
   public String getAggregateName()

```

Return Value

Type: String

##### getCompareTo()

Returns the value that the aggregate is compared to in the condition.

Signature

```
   public Double getCompareTo()

```

Return Value

Type: Double

##### getDisplayCompareTo()

Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

Signature

```
   public String getDisplayCompareTo()

```

Return Value

Type: String


### Apex Reference Guide EvaluatedConditionOperator Enum

##### getDisplayValue()

Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

Signature

```
   public String getDisplayValue()

```

Return Value

Type: String

##### getOperator()

Returns the operator used in the condition.

Signature

```
   public Reports.EvaluatedConditionOperator getOperator()

```

Return Value

Type: Reports.EvaluatedConditionOperator

##### getValue()

Returns the actual value of the aggregate when the report is run.

Signature

```
   public Double getValue()

```

Return Value

Type: Double

### EvaluatedConditionOperator Enum

The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to a
##### value. It is returned by the getOperator method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.EvaluatedConditionOperator` enum.


### Apex Reference Guide FilterOperator Class

**Value** **Description**

`EQUAL` Equality operator.

`GREATER_THAN` Greater than operator.

`GREATER_THAN_EQUAL` Greater than or equal to operator.

`LESS_THAN` Less than operator.

`LESS_THAN_EQUAL` Less than or equal to operator.

`NOT_EQUAL` Inequality operator.

### FilterOperator Class

Contains information about a filter operator, such as display name and API name.

Namespace

Reports

#### FilterOperator Methods

### The following are methods for FilterOperator . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the
column being filtered.

getName()
Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide FilterValue Class

##### getName()

Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FilterValue Class

Contains information about a filter value, such as the display name and API name.

Namespace

Reports

#### FilterValue Methods

### The following are methods for FilterValue . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide FormulaType Enum

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column being
filtered.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FormulaType Enum

The format of the numbers in a custom summary formula.

Enum Values

The following are the values of the `Reports.FormulaType` enum.

**Value** **Description**

`CURRENCY` Formatted as currency. For example, $100.00.

`NUMBER` Formatted as numbers. For example, 100.

`PERCENT` Formatted as percentages. For example, 100%.

### GroupingColumn Class

Contains methods for describing fields that are used for column grouping.

Namespace

Reports

### The GroupingColumn class provides basic information about column grouping fields. The GroupingInfo class includes

additional methods for describing and updating grouping fields.

#### GroupingColumn Methods

### The following are methods for GroupingColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

getLabel()
Returns the localized display name of the field that is used for column grouping.


Apex Reference Guide GroupingColumn Class

##### getDataType()

Returns the data type of the field that is used for column grouping.

##### getGroupingLevel()

Returns the level of grouping for the column.

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of the field that is used for column grouping.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the field that is used for column grouping.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getGroupingLevel()

Returns the level of grouping for the column.

Syntax

```
   public Integer getGroupingLevel()

```


### Apex Reference Guide GroupingInfo Class

Return Value

Type: Integer

Usage

**•** In a summary report, 0, 1, or 2 indicates grouping at the first, second, or third row level.

**•** In a matrix report, 0 or 1 indicates grouping at the first or second row or column level.

### GroupingInfo Class

Contains methods for describing fields that are used for grouping.

Namespace

Reports

#### GroupingInfo Methods

### The following are methods for GroupingInfo . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).

getDateGranularity()
Returns the date interval that is used for row or column grouping.

getSortAggregate()
Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a
grouping is not sorted by a summary field.

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).


### Apex Reference Guide GroupingValue Class

Syntax

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder

##### getDateGranularity()

Returns the date interval that is used for row or column grouping.

Syntax

```
   public Reports.DateGranularity getDateGranularity()

```

Return Value

Type: Reports.DateGranularity

##### getSortAggregate()

Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a grouping
is not sorted by a summary field.

Syntax

```
   public String getSortAggregate()

```

Return Value

Type: String

### GroupingValue Class

Contains grouping values for a row or column, including the key, label, and value.

Namespace

Reports

#### GroupingValue Methods

### The following are methods for GroupingValue . All are instance methods.

IN THIS SECTION:

getGroupings()
Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.


Apex Reference Guide GroupingValue Class

##### getKey()

Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

##### getLabel()

Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

##### getValue()

Returns the value of the field that is used as a row or column grouping.

##### getGroupings()

Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.

Syntax

```
   public LIST<Reports.GroupingValue> getGroupings()

```

Return Value

Type: List<Reports.GroupingValue>

##### getKey()

Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of the field that is used as a row or column grouping.


### Apex Reference Guide NotificationAction Interface

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

Usage

The value depends on the field’s data type.

**•** Currency fields:

**–** `amount` : Of type currency. A data cell’s value.

**–** `currency` : Of type picklist. The ISO 4217 currency code, if available; for example, USD for US dollars or CNY for Chinese yuan.
(If the grouping is on the converted currency, this value is the currency code for the report and not for the record.)

**•** Picklist fields: API name. For example, a custom picklist field— `Type of Business` with values 1, 2, and 3 for Consulting,
Services, and Add-On Business respectively—has `1`, `2`, or `3` as the grouping value.

**•** ID fields: API name.

**•** Record type fields: API name.

**•** Date and time fields: Date or time in ISO-8601 format.

**•** Lookup fields: Unique API name. For example, for the `Opportunity Owner` lookup field, the ID of each opportunity owner’s
Chatter profile page can be a grouping value.

### NotificationAction Interface

Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

Namespace

Reports

Usage

Report notifications for reports that users have subscribed to can trigger a custom Apex class, which must implement the
`Reports.NotificationAction` interface. The `execute` method in this interface receives a
`NotificationActionContext` object as a parameter, which contains information about the report instance and the conditions
that must be met for a notification to be triggered.

IN THIS SECTION:

#### NotificationAction Methods

NotificationAction Example Implementation

#### NotificationAction Methods

### The following are methods for NotificationAction .


### Apex Reference Guide NotificationActionContext Class

IN THIS SECTION:

##### execute(context)
### Executes the custom Apex action specified in the context parameter of the context object, NotificationActionContext .

The object contains information about the report instance and the conditions that must be met for a notification to be triggered.
The method executes whenever the specified conditions are met.

##### execute(context)

### Executes the custom Apex action specified in the context parameter of the context object, NotificationActionContext .

The object contains information about the report instance and the conditions that must be met for a notification to be triggered. The
method executes whenever the specified conditions are met.

Signature

```
   public void execute(Reports.NotificationActionContext context)

```

Parameters

```
   context
```

Type: Reports.NotificationActionContext

Return Value

Type: Void

#### NotificationAction Example Implementation

This is an example implementation of the `Reports.NotificationAction` interface.

```
   public class AlertOwners implements Reports.NotificationAction {

      public void execute(Reports.NotificationActionContext context) {

        Reports.ReportResults results = context.getReportInstance().getReportResults();

        for(Reports.GroupingValue g: results.getGroupingsDown().getGroupings()) {

           FeedItem t = new FeedItem();

           t.ParentId = (Id)g.getValue();

           t.Body = 'This record needs attention. Please view the report.';

           t.Title = 'Needs Attention: '+ results.getReportMetadata().getName();

           t.LinkUrl = '/' + results.getReportMetadata().getId();

           insert t;

        }

      }

   }

### NotificationActionContext Class

```

Contains information about the report instance and condition threshold for a report notification.


Apex Reference Guide NotificationActionContext Class

Namespace

Reports

IN THIS SECTION:

#### NotificationActionContext Constructors NotificationActionContext Methods NotificationActionContext Constructors The following are constructors for NotificationActionContext .

IN THIS SECTION:

##### NotificationActionContext(reportInstance, thresholdInformation)

Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.

##### NotificationActionContext(reportInstance, thresholdInformation)

Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.

Signature

```
   public NotificationActionContext(Reports.ReportInstance reportInstance,

   Reports.ThresholdInformation thresholdInformation)

```

Parameters

```
   reportInstance
```

Type: Reports.ReportInstance

An instance of a report.

```
   thresholdInformation
```

Type: Reports.ThresholdInformation

The evaluated conditions for the notification.

#### NotificationActionContext Methods The following are methods for NotificationActionContext .

IN THIS SECTION:

getReportInstance()
Returns the report instance associated with the notification.

getThresholdInformation()
Returns the threshold information associated with the notification.


### Apex Reference Guide ReportCsf Class

##### getReportInstance()

Returns the report instance associated with the notification.

Signature

```
   public Reports.ReportInstance getReportInstance()

```

Return Value

Type: Reports.ReportInstance

##### getThresholdInformation()

Returns the threshold information associated with the notification.

Signature

```
   public Reports.ThresholdInformation getThresholdInformation()

```

Return Value

Type: Reports.ThresholdInformation

### ReportCsf Class

Contains methods and constructors for working with information about a custom summary formula (CSF).

Namespace

Reports

IN THIS SECTION:

#### ReportCsf Constructors

ReportCsf Methods

#### ReportCsf Constructors

### The following are constructors for ReportCsf .

IN THIS SECTION:

ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType, acrossGroup, acrossGroupType, formula)
Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

ReportCsf()
Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.


Apex Reference Guide ReportCsf Class

##### ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType,

acrossGroup, acrossGroupType, formula)

Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

Signature

```
   public ReportCsf(String label, String description, Reports.FormulaType formulaType,

   Integer decimalPlaces, String downGroup, Reports.CsfGroupType downGroupType, String

   acrossGroup, Reports.CsfGroupType acrossGroupType, String formula)

```

Parameters

```
   label
```

Type: String

The user-facing name of the custom summary formula.

```
   description
```

Type: String

The user-facing description of the custom summary formula.

```
   formulaType
```

Type: Reports.FormulaType

The format of the numbers in the custom summary formula.

```
   decimalPlaces
```

Type: Integer

The number of decimal places to include in numbers.

```
   downGroup
```

Type: String

The name of a row grouping when the `downGroupType` is `CUSTOM` ; `null` otherwise.

```
   downGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   acrossGroup
```

Type: String

The name of a column grouping when the `accrossGroupType` is `CUSTOM` ; `null` otherwise.

```
   acrossGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   formula
```

Type: String

The operations performed on values in the custom summary formula.

##### ReportCsf()

Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.


Apex Reference Guide ReportCsf Class

Signature

```
   public ReportCsf()

#### ReportCsf Methods The following are methods for ReportCsf .

```

IN THIS SECTION:

getAcrossGroup()
Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

getAcrossGroupType()
Returns where to display the aggregate.

getDecimalPlaces()
Returns the number of decimal places that numbers in the custom summary formula have.

getDescription()
Returns the user-facing description of a custom summary formula.

getDownGroup()
Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .

getDownGroupType()
Returns where to display the aggregate of the custom summary formula.

getFormula()
Returns the operations performed on values in the custom summary formula.

getFormulaType()
Returns the formula type.

getLabel()
Returns the user-facing name of the custom summary formula.

setAcrossGroup(acrossGroup)
Specifies the column for the across grouping.

setAcrossGroupType(value)
Sets where to display the aggregate.

setAcrossGroupType(acrossGroupType)
Sets where to display the aggregate.

setDecimalPlaces(decimalPlaces)
Sets the number of decimal places in numbers.

setDescription(description)
Sets the user-facing description of the custom summary formula.

setDownGroup(downGroup)
Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

setDownGroupType(value)
Sets where to display the aggregate.


Apex Reference Guide ReportCsf Class

setDownGroupType(downGroupType)
Sets where to display the aggregate.

setFormula(formula)
Sets the operations to perform on values in the custom summary formula.

setFormulaType(value)
Sets the format of the numbers in the custom summary formula.

setFormulaType(formulaType)
Sets the format of numbers used in the custom summary formula.

setLabel(label)
Sets the user-facing name of the custom summary formula.

toString()
Returns a string.

##### getAcrossGroup()

Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

Signature

```
   public String getAcrossGroup()

```

Return Value

Type: String

##### getAcrossGroupType()

Returns where to display the aggregate.

Signature

```
   public Reports.CsfGroupType getAcrossGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getDecimalPlaces()

Returns the number of decimal places that numbers in the custom summary formula have.

Signature

```
   public Integer getDecimalPlaces()

```

Return Value

Type: Integer


Apex Reference Guide ReportCsf Class

##### getDescription()

Returns the user-facing description of a custom summary formula.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDownGroup()

Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .

Signature

```
   public String getDownGroup()

```

Return Value

Type: String

##### getDownGroupType()

Returns where to display the aggregate of the custom summary formula.

Signature

```
   public Reports.CsfGroupType getDownGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getFormula()

Returns the operations performed on values in the custom summary formula.

Signature

```
   public String getFormula()

```

Return Value

Type: String

##### getFormulaType()

Returns the formula type.


Apex Reference Guide ReportCsf Class

Signature

```
   public Reports.FormulaType getFormulaType()

```

Return Value

Type: Reports.FormulaType

##### getLabel()

Returns the user-facing name of the custom summary formula.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### setAcrossGroup(acrossGroup)

Specifies the column for the across grouping.

Signature

```
   public void setAcrossGroup(String acrossGroup)

```

Parameters

```
   acrossGroup
```

Type: String

Return Value

Type: void

##### setAcrossGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.CsfGroupType.


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setAcrossGroupType(acrossGroupType)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(Reports.CsfGroupType acrossGroupType)

```

Parameters

```
   acrossGroupType
```

Type: Reports.CsfGroupType

Return Value

Type: void

##### setDecimalPlaces(decimalPlaces)

Sets the number of decimal places in numbers.

Signature

```
   public void setDecimalPlaces(Integer decimalPlaces)

```

Parameters

```
   decimalPlaces
```

Type: Integer

Return Value

Type: void

##### setDescription(description)

Sets the user-facing description of the custom summary formula.

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setDownGroup(downGroup)

Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

Signature

```
   public void setDownGroup(String downGroup)

```

Parameters

```
   downGroup
```

Type: String

Return Value

Type: void

##### setDownGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.CsfGroupType.

Return Value

Type: void

##### setDownGroupType(downGroupType)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(Reports.CsfGroupType downGroupType)

```

Parameters

```
   downGroupType
```

Type: Reports.CsfGroupType


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setFormula(formula)

Sets the operations to perform on values in the custom summary formula.

Signature

```
   public void setFormula(String formula)

```

Parameters

```
   formula
```

Type: String

Return Value

Type: void

##### setFormulaType(value)

Sets the format of the numbers in the custom summary formula.

Signature

```
   public void setFormulaType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.FormulaType.

Return Value

Type: void

##### setFormulaType(formulaType)

Sets the format of numbers used in the custom summary formula.

Signature

```
   public void setFormulaType(Reports.FormulaType formulaType)

```

Parameters

```
   formulaType
```

Type: Reports.FormulaType


### Apex Reference Guide ReportCurrency Class

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the custom summary formula.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### ReportCurrency Class

Contains information about a currency value, including the amount and currency code.

Namespace

Reports

#### ReportCurrency Methods

### The following are methods for ReportCurrency . All are instance methods.

IN THIS SECTION:

getAmount()
Returns the amount of the currency value.


### Apex Reference Guide ReportDataCell Class

##### getCurrencyCode()

Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null`
if the organization does not have multicurrency enabled.

##### getAmount()

Returns the amount of the currency value.

Syntax

```
   public Decimal getAmount()

```

Return Value

Type: Decimal

##### getCurrencyCode()

Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if
the organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

### ReportDataCell Class

Contains the data for a cell in the report, including the display label and value.

Namespace

Reports

#### ReportDataCell Methods

### The following are methods for ReportDataCell . All are instance methods.

IN THIS SECTION:

getLabel()
Returns the localized display name of the value of a specified cell in the report.

getValue()
Returns the value of a specified cell of a detail row of a report.


### Apex Reference Guide ReportDescribeResult Class

##### getLabel()

Returns the localized display name of the value of a specified cell in the report.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of a specified cell of a detail row of a report.

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ReportDescribeResult Class

Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

#### ReportDescribeResult Methods

### The following are methods for ReportDescribeResult . All are instance methods.

IN THIS SECTION:

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.

getReportMetadata()
Returns unique identifiers for groupings and summaries.

getReportTypeMetadata()
Returns the fields in each section of a report type, plus filtering information for those fields.

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.


### Apex Reference Guide ReportDetailRow Class

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns unique identifiers for groupings and summaries.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```

Return Value

Type: Reports.ReportMetadata

##### getReportTypeMetadata()

Returns the fields in each section of a report type, plus filtering information for those fields.

Syntax

```
   public Reports.ReportTypeMetadata getReportTypeMetadata()

```

Return Value

Type: Reports.ReportTypeMetadata

### ReportDetailRow Class

Contains data cells for a detail row of a report.

Namespace

Reports

#### ReportDetailRow Methods

### The following are methods for ReportDetailRow . All are instance methods.

IN THIS SECTION:

getDataCells()
Returns a list of data cells for a detail row.


### Apex Reference Guide ReportDivisionInfo Class

##### getDataCells()

Returns a list of data cells for a detail row.

Syntax

```
   public LIST<Reports.ReportDataCell> getDataCells()

```

Return Value

Type: List<Reports.ReportDataCell>

### ReportDivisionInfo Class

Contains information about the divisions that can be used to filter a report.

Available only if your organization uses divisions to segment data and you have the “Affected by Divisions” permission. If you do not
have the “Affected by Divisions” permission, your reports include records in all divisions.

Namespace

Reports

Usage

Use to filter records in the report based on a division, like West Coast and East Coast.

#### ReportDivisionInfo Methods

### The following are methods for ReportDivisionInfo .

##### getDefaultValue()

Returns the default division for the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of all possible divisions for the report.

Signature

```
   public List<Reports.FilterValue> getValues()

```


### Apex Reference Guide ReportExtendedMetadata Class

Return Value

Type: List<Reports.FilterValue>

### ReportExtendedMetadata Class

Contains report extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

Report extended metadata provides additional, detailed metadata about summary and grouping fields, including data type and label
information.

#### ReportExtendedMetadata Methods

### The following are methods for ReportExtendedMetadata . All are instance methods.

IN THIS SECTION:

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains
values for each summary that is listed in the report metadata.

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are
also listed in the report metadata.

getGroupingColumnInfo()
Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the
groupingsDown and groupingsAcross lists.

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains values
for each summary that is listed in the report metadata.

Syntax

```
   public MAP<String,Reports.AggregateColumn> getAggregateColumnInfo()

```

Return Value

Type: Map<String,Reports.AggregateColumn>

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are also
listed in the report metadata.


### Apex Reference Guide ReportFact Class

Syntax

```
   public MAP<String,Reports.DetailColumn> getDetailColumnInfo()

```

Return Value

Type: Map<String,Reports.DetailColumn>

##### getGroupingColumnInfo()

Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the groupingsDown
and groupingsAcross lists.

Syntax

```
   public MAP<String,Reports.GroupingColumn> getGroupingColumnInfo()

```

Return Value

Type: Map<String,Reports.GroupingColumn>

### ReportFact Class

Contains the fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### ReportFact is the parent class of ReportFactWithDetails and ReportFactWithSummaries . If includeDetails

is `true` when the report is run, the fact map is a `ReportFactWithDetails` object. If `includeDetails` is `false` when
the report is run, the fact map is a `ReportFactWithSummaries` object.

#### ReportFact Methods

### The following are methods for ReportFact . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns summary-level data for a report, including the record count.

getKey()
Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.


### Apex Reference Guide ReportFactWithDetails Class

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

### ReportFactWithDetails Class

Contains the detailed fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### The ReportFactWithDetails class extends the ReportFact class. A ReportFactWithDetails object is returned if

`includeDetails` is set to `true` when the report is run. To access the detail values, you’ll need to cast the return value of the
### ReportResults.getFactMap method to a ReportFactWithDetails object.

#### ReportFactWithDetails Methods

### The following are methods for ReportFactWithDetails . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.


### Apex Reference Guide ReportFactWithSummaries Class

##### getRows()

Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getRows()

Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

Syntax

```
   public LIST<Reports.ReportDetailRow> getRows()

```

Return Value

Type: List<Reports.ReportDetailRow>

### ReportFactWithSummaries Class

Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

Namespace

Reports


Apex Reference Guide ReportFactWithSummaries Class

Usage

#### The ReportFactWithSummaries class extends the ReportFact class. A ReportFactWithSummaries object is

returned if `includeDetails` is set to `false` when the report is run.

#### ReportFactWithSummaries Methods The following are methods for ReportFactWithSummaries . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.

##### toString()

Returns a string.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### toString()

Returns a string.

Signature

```
   public String toString()

```


### Apex Reference Guide ReportFilter Class

Return Value

Type: String

### ReportFilter Class

Contains information about a report filter, including column, operator, and value.

Namespace

Reports

IN THIS SECTION:

#### ReportFilter Constructors

ReportFilter Methods

#### ReportFilter Constructors

### The following are constructors for ReportFilter .

IN THIS SECTION:

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

##### ReportFilter(column, operator, value)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

ReportFilter(column, operator, value, filterType)
Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

ReportFilter(column, operator, value, filterType, entityName)
Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

Signature

```
   public ReportFilter()

##### ReportFilter(column, operator, value)

```

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Signature

```
   public ReportFilter(String column, String operator, String value)

```


Apex Reference Guide ReportFilter Class

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

##### ReportFilter(column, operator, value, filterType)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3244

##### **`ReportFilter(column, operator, value, filterType, entityName)`**

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType, String entityName)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3244


Apex Reference Guide ReportFilter Class

```
   entityName
```

Type: String

#### ReportFilter Methods The following are methods for ReportFilter . All are instance methods.

IN THIS SECTION:

##### getColumn()

Returns the unique API name for the field that’s being filtered.

getEntityName()
Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

getFilterType()
Returns the type of report filter.

getOperator()
Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

getValue()
Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

setColumn(column)
Sets the unique API name for the field that’s being filtered.

setEntityName(entityName)
Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

setFilterType()
Sets the type of report filter.

setOperator(operator)
Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

setValue(value)
Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

toString(column)
Returns a string representation of the filter.

##### getColumn()

Returns the unique API name for the field that’s being filtered.

Syntax

```
   public String getColumn()

```


Apex Reference Guide ReportFilter Class

Return Value

Type: String

##### **`getEntityName()`**

Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public String getEntityName()

```

Return Value

Type: String

##### getFilterType()

Returns the type of report filter.

Syntax

```
   public String getFilterType()

```

Return Value

Type: ReportFilterType Enum on page 3244

##### getOperator()

Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

Syntax

```
   public String getOperator()

```

Return Value

Type: String

##### getValue()

Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

Syntax

```
   public String getValue()

```


Apex Reference Guide ReportFilter Class

Return Value

Type: String

##### setColumn(column)

Sets the unique API name for the field that’s being filtered.

Syntax

```
   public Void setColumn(String column)

```

Parameters

```
   column
```

Type: String

Return Value

Type: Void

##### **`setEntityName(entityName)`**

Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public Void setEntityName(String entityName)

```

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setFilterType()

Sets the type of report filter.

Syntax

```
   public Void setFilterType(String column)

```

Parameters

```
   column
```

Type: String


Apex Reference Guide ReportFilter Class

Return Value

Type: Void

##### setOperator(operator)

Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions depend
on the data type of the field.

Syntax

```
   public Void setOperator(String operator)

```

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setValue(value)

Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

Syntax

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

##### toString(column)

Returns a string representation of the filter.

Signature

```
   public String toString()

```

Return Value

Type: String


### Apex Reference Guide ReportFormat Enum ReportFormat Enum

Contains the possible report format types.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ReportFormat` enum.

**Value** **Description**

`MATRIX` Matrix report format

`SUMMARY` Summary report format

`TABULAR` Tabular report format

### ReportFilterType Enum

The types of values included in a report filter type.

Enum Values

The following are the values of the `Reports.ReportFilterType` enum.

**Value** **Description**

`fieldToField` Field-to-field filter

`fieldValue` Field-to-value filter

### ReportInstance Class

Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

Namespace

Reports

#### ReportInstance Methods

### The following are methods for ReportInstance . All are instance methods.


Apex Reference Guide ReportInstance Class

IN THIS SECTION:

##### getCompletionDate()

Returns the date and time when the instance of the report finished running. The completion date is available only if the report
instance ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

##### getId()

Returns the unique ID for an instance of a report that was run asynchronously.

##### getOwnerId()

Returns the ID of the user who created the report instance.

getReportId()
Returns the unique ID of the report this instance is based on.

getReportResults()
Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize
data or include details.

getRequestDate()
Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

getStatus()
Returns the status of a report.

##### getCompletionDate()

Returns the date and time when the instance of the report finished running. The completion date is available only if the report instance
ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getCompletionDate()

```

Return Value

Type: Datetime

##### getId()

Returns the unique ID for an instance of a report that was run asynchronously.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getOwnerId()

Returns the ID of the user who created the report instance.


Apex Reference Guide ReportInstance Class

Syntax

```
   public Id getOwnerId()

```

Return Value

Type: Id

##### getReportId()

Returns the unique ID of the report this instance is based on.

Syntax

```
   public Id getReportId()

```

Return Value

Type: Id

##### getReportResults()

Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize data
or include details.

Syntax

```
   public Reports.ReportResults getReportResults()

```

Return Value

Type: Reports.ReportResults

##### getRequestDate()

Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getRequestDate()

```

Return Value

Type: Datetime

##### getStatus()

Returns the status of a report.


### Apex Reference Guide ReportManager Class

Syntax

```
   public String getStatus()

```

Return Value

Type: String

Usage

**•** `New` if the report run was recently triggered through a request.

**•** `Success` if the report ran.

**•** `Running` if the report is being run.

**•** `Error` if the report run failed. The instance of a report run can return an error if, for example, your permission to access the report
was removed after you requested the run.

### ReportManager Class

Runs a report synchronously or asynchronously and with or without details.

Namespace

Reports

Usage

Gets instances of reports and describes the metadata of Reports.

#### ReportManager Methods

### The following are methods for ReportManager . All methods are static.

IN THIS SECTION:

describeReport(reportId)
Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

getDatatypeFilterOperatorMap()
Lists the field data types that you can use to filter the report.

getReportInstance(instanceId)
Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

getReportInstances(reportId)
Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report,
with metadata for the time at which the report was run.

runAsyncReport(reportId, reportMetadata, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based
on the report metadata in _`reportMetadata`_ .


Apex Reference Guide ReportManager Class

runAsyncReport(reportId, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .

runAsyncReport(reportId, reportMetadata)
Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

runAsyncReport(reportId)
Runs a report asynchronously with the report ID.

runReport(reportId, reportMetadata, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on
the report metadata in _`reportMetadata`_ .

runReport(reportId, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .

runReport(reportId, reportMetadata)
Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

runReport(reportId)
Runs a report immediately with the report ID.

##### describeReport(reportId)

Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

Syntax

```
   public static Reports.ReportDescribeResult describeReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportDescribeResult

##### getDatatypeFilterOperatorMap()

Lists the field data types that you can use to filter the report.

Syntax

```
   public static MAP<String,LIST<Reports.FilterOperator>> getDatatypeFilterOperatorMap()

```

Return Value

Type: Map<String, List<Reports.FilterOperator>>


Apex Reference Guide ReportManager Class

##### getReportInstance(instanceId)

Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

Syntax

```
   public static Reports.ReportInstance getReportInstance(Id instanceId)

```

Parameters

```
   instanceId
```

Type: Id

Return Value

Type: Reports.ReportInstance

##### getReportInstances(reportId)

Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report, with
metadata for the time at which the report was run.

Syntax

```
   public static LIST<Reports.ReportInstance> getReportInstances(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: List<Reports.ReportInstance>

##### runAsyncReport(reportId, reportMetadata, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based on
the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id


Apex Reference Guide ReportManager Class

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, reportMetadata)

Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

Return Value

Type: Reports.ReportInstance


Apex Reference Guide ReportManager Class

##### runAsyncReport(reportId)

Runs a report asynchronously with the report ID.

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportInstance

##### runReport(reportId, reportMetadata, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on the
report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Boolean includeDetails)

```


Apex Reference Guide ReportManager Class

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, reportMetadata)

Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata Reports.ReportMetadata

Return Value

Type: Reports.ReportResults

##### runReport(reportId)

Runs a report immediately with the report ID.

Syntax

```
   public static Reports.ReportResults runReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportResults


### Apex Reference Guide ReportMetadata Class ReportMetadata Class

Contains report metadata for a tabular, summary, or matrix report.

Namespace

Reports

Usage

Report metadata gives information about the report as a whole, such as the report type, format, summary fields, row or column groupings,
### and filters that are saved to the report. You can use the ReportMetadata class to retrieve report metadata and to set metadata

that can be used to filter a report.

#### ReportMetadata Methods

### The following are methods for ReportMetadata . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns unique identifiers for summary or custom summary formula fields in the report.

getBuckets()
Returns a list of bucket fields in the report.

getCrossFilters()
Returns information about cross filters applied to a report.

getCurrencyCode()
Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

getCustomSummaryFormula()
Returns information about custom summary formulas in a report.

getDescription()
Returns the description of the report.

getDetailColumns()
Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the
following values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

getDeveloperName()
Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

getDivision()
Returns the division specified in the report.

getGroupingsAcross()
Returns column groupings in a report.

getGroupingsDown()
Returns row groupings for a report.


Apex Reference Guide ReportMetadata Class

getHasDetailRows()
Indicates whether the report has detail rows.

getHasRecordCount()
Indicates whether the report shows the total number of records.

getHistoricalSnapshotDates()
Returns a list of historical snapshot dates.

getId()
Returns the unique report ID.

getName()
Returns the report name.

getReportBooleanFilter()
Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

getReportFilters()
Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

getReportFormat()
Returns the format of the report.

getReportType()
Returns the unique API name and display name for the report type.

getScope()
Returns the API name for the scope defined for the report. Scope values depend on the report type.

getShowGrandTotal()
Indicates whether the report shows the grand total.

getShowSubtotals()
Indicates whether the report shows subtotals, such as column or row totals.

getSortBy()
Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

getStandardDateFilter()
Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API
name.

getStandardFilters()
Returns a list of standard filters for the report.

getTopRows()
Returns information about a row limit filter, including the number of rows returned and the sort order.

setAggregates(aggregates)
Sets unique identifiers for standard or custom summary formula fields in the report.

setBuckets(buckets)
Creates bucket fields in a report.

setCrossFilters(crossFilters)
Applies cross filters to a report.

setCurrencyCode(currencyCode)
Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.


Apex Reference Guide ReportMetadata Class

setCustomSummaryFormula(customSummaryFormula)
Adds a custom summary formula to a report.

setDescription(description)
Sets the description of the report.

setDetailColumns(detailColumns)
Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

setDeveloperName(developerName)
Sets the report API name—for example, `Closed_Sales_This_Quarter` .

setDivision(division)
Sets the division of the report.

setGroupingsAcross(groupingInfo)
Sets column groupings in a report.

setGroupingsDown(groupingInfo)
Sets row groupings for a report.

setHasDetailRows(hasDetailRows)
Specifies whether the report has detail rows.

setHasRecordCount(hasRecordCount)
Specifies whether the report is configured to show the total number of records.

setHistoricalSnapshotDates(historicalSnapshot)
Sets a list of historical snapshot dates.

setId(id)
Sets the unique report ID.

setName(name)
Sets the report name.

setReportBooleanFilter(reportBooleanFilter)
Sets logic to parse custom field filters.

setReportFilters(reportFilters)
Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

setReportFormat(format)
Sets the format of the report.

setReportType(reportType)
Sets the unique API name and display name for the report type.

setScope(scopeName)
Sets the API name for the scope defined for the report. Scope values depend on the report type.

setShowGrandTotal(showGrandTotal)
Specifies whether the report shows the grand total.

setShowSubtotals(showSubtotals)
Specifies whether the report shows subtotals, such as column or row totals.

setSortBy(column)
Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.


Apex Reference Guide ReportMetadata Class

setStandardDateFilter(dateFilter)
Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.

setStandardFilters(filters)
Sets one or more standard filters on the report.

setTopRows(topRows)
Applies a row limit filter to a report.

##### getAggregates()

Returns unique identifiers for summary or custom summary formula fields in the report.

Syntax

```
   public LIST<String> getAggregates()

```

Return Value

Type: List<String>

Usage

For example:

**•** `a!Amount` represents the average for the `Amount` column.

**•** `s!Amount` represents the sum of the `Amount` column.

**•** `m!Amount` represents the minimum value of the `Amount` column.

**•** `x!Amount` represents the maximum value of the `Amount` column.

**•** `s!` _`<customfieldID>`_ represents the sum of a custom field column. For custom fields and custom report types, the identifier
is a combination of the summary type and the field ID.

##### getBuckets()

Returns a list of bucket fields in the report.

Signature

```
   public List<Reports.BucketField> getBuckets()

```

Return Value

Type: List<Reports.BucketField>

##### getCrossFilters()

Returns information about cross filters applied to a report.

Signature

```
   public Reports.CrossFilter getCrossFilters()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<Reports.CrossFilter>

##### getCurrencyCode()

Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

##### getCustomSummaryFormula()

Returns information about custom summary formulas in a report.

Signature

```
   public Map<String,Reports.ReportCsf> getCustomSummaryFormula()

```

Return Value

Type: Map<String,Reports.ReportCsf>

##### getDescription()

Returns the description of the report.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDetailColumns()

Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the following
values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

Syntax

```
   public LIST<String> getDetailColumns()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<String>

##### getDeveloperName()

Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

Syntax

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getDivision()

Returns the division specified in the report.

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.

Signature

```
   public String getDivision()

```

Return Value

Type: String

##### getGroupingsAcross()

Returns column groupings in a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsAcross()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** An empty array for reports in summary format, because summary reports don't include column groupings

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for a column grouping


Apex Reference Guide ReportMetadata Class

##### getGroupingsDown()

Returns row groupings for a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsDown()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for grouping

##### getHasDetailRows()

Indicates whether the report has detail rows.

Signature

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean

##### getHasRecordCount()

Indicates whether the report shows the total number of records.

Signature

```
   public Boolean getHasRecordCount()

```

Return Value

Type: Boolean

##### getHistoricalSnapshotDates()

Returns a list of historical snapshot dates.

Syntax

```
   public LIST<String> getHistoricalSnapshotDates()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<String>

##### getId()

Returns the unique report ID.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getName()

Returns the report name.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getReportBooleanFilter()

Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

Syntax

```
   public String getReportBooleanFilter()

```

Return Value

Type: String

##### getReportFilters()

Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public LIST<Reports.ReportFilter> getReportFilters()

```

Return Value

Type: List<Reports.ReportFilter>


Apex Reference Guide ReportMetadata Class

##### getReportFormat()

Returns the format of the report.

Syntax

```
   public Reports.ReportFormat getReportFormat()

```

Return Value

Type: Reports.ReportFormat

Usage

This value can be:

**•** `TABULAR`

**•** `SUMMARY`

**•** `MATRIX`

##### getReportType()

Returns the unique API name and display name for the report type.

Syntax

```
   public Reports.ReportType getReportType()

```

Return Value

Type: Reports.ReportType

##### getScope()

Returns the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public String getScope()

```

Return Value

Type: String

##### getShowGrandTotal()

Indicates whether the report shows the grand total.

Signature

```
   public Boolean getShowGrandTotal()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: Boolean

##### getShowSubtotals()

Indicates whether the report shows subtotals, such as column or row totals.

Signature

```
   public Boolean getShowSubtotals()

```

Return Value

Type: Boolean

##### getSortBy()

Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

Signature

```
   public List<Reports.SortColumn> getSortBy()

```

Return Value

Type: List<Reports.SortColumn>

##### getStandardDateFilter()

Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API name.

Signature

```
   public Reports.StandardDateFilter getStandardDateFilter()

```

Return Value

Type: Reports.StandardDateFilter

##### getStandardFilters()

Returns a list of standard filters for the report.

Signature

```
   public List<Reports.StandardFilter> getStandardFilters()

```

Return Value

Type: List<Reports.StandardFilter>


Apex Reference Guide ReportMetadata Class

##### getTopRows()

Returns information about a row limit filter, including the number of rows returned and the sort order.

Signature

```
   public Reports.TopRows getTopRows()

```

Return Value

Type: Reports.TopRows

##### setAggregates(aggregates)

Sets unique identifiers for standard or custom summary formula fields in the report.

Signature

```
   public void setAggregates(List<String> aggregates)

```

Parameters

```
   aggregates
```

Type: List<String>

Return Value

Type: void

##### setBuckets(buckets)

Creates bucket fields in a report.

Signature

```
   public void setBuckets(List<Reports.BucketField> buckets)

```

Parameters

```
   buckets
```

Type: List<Reports.BucketField>

Return Value

Type: void

##### setCrossFilters(crossFilters)

Applies cross filters to a report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setCrossFilters(List<Reports.CrossFilter> crossFilters)

```

Parameters

```
   crossFilter
```

Type: List<Reports.CrossFilter>

Return Value

Type: void

##### setCurrencyCode(currencyCode)

Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.

Signature

```
   public void setCurrencyCode(String currencyCode)

```

Parameters

```
   currencyCode
```

Type: String

Return Value

Type: void

##### setCustomSummaryFormula(customSummaryFormula)

Adds a custom summary formula to a report.

Signature

```
   public void setCustomSummaryFormula(MAP<String,Reports.ReportCsf> customSummaryFormula)

```

Parameters

```
   customSummaryFormula
```

Type: Map<String, Reports.ReportCsf>

Return Value

Type: void

##### setDescription(description)

Sets the description of the report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: void

##### setDetailColumns(detailColumns)

Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

Signature

```
   public void setDetailColumns(List<String> detailColumns)

```

Parameters

```
   detailColumns
```

Type: List<String>

Return Value

Type: void

##### setDeveloperName(developerName)

Sets the report API name—for example, `Closed_Sales_This_Quarter` .

Signature

```
   public void setDeveloperName(String developerName)

```

Parameters

```
   developerName
```

Type: String

Return Value

Type: void

##### setDivision(division)

Sets the division of the report.


Apex Reference Guide ReportMetadata Class

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.

Signature

```
   public void setDivision(String division)

```

Parameters

```
   division
```

Type: String

Return Value

Type: void

##### setGroupingsAcross(groupingInfo)

Sets column groupings in a report.

Signature

```
   public void setGroupingsAcross(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void

##### setGroupingsDown(groupingInfo)

Sets row groupings for a report.

Signature

```
   public void setGroupingsDown(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setHasDetailRows(hasDetailRows)

Specifies whether the report has detail rows.

Signature

```
   public void setHasDetailRows(Boolean hasDetailRows)

```

Parameters

```
   hasDetailRows
```

Type: Boolean

Return Value

Type: void

##### setHasRecordCount(hasRecordCount)

Specifies whether the report is configured to show the total number of records.

Signature

```
   public void setHasRecordCount(Boolean hasRecordCount)

```

Parameters

```
   hasRecordCount
```

Type: Boolean

Return Value

Type: void

##### setHistoricalSnapshotDates(historicalSnapshot)

Sets a list of historical snapshot dates.

Syntax

```
   public Void setHistoricalSnapshotDates(LIST<String> historicalSnapshot)

```

Parameters

```
   historicalSnapshot
```

Type: List<String>

Return Value

Type: Void


Apex Reference Guide ReportMetadata Class

##### setId(id)

Sets the unique report ID.

Signature

```
   public void setId(Id id)

```

Parameters

```
   id
```

Type: Id

Return Value

Type: void

##### setName(name)

Sets the report name.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void

##### setReportBooleanFilter(reportBooleanFilter)

Sets logic to parse custom field filters.

Syntax

```
   public Void setReportBooleanFilter(String reportBooleanFilter)

```

Parameters

```
   reportBooleanFilter
```

Type: String

Return Value

Type: Void


Apex Reference Guide ReportMetadata Class

##### setReportFilters(reportFilters)

Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public Void setReportFilters(LIST<Reports.ReportFilter> reportFilters)

```

Parameters

```
   reportFilters
```

Type: List<Reports.ReportFilter>

Return Value

Type: Void

##### setReportFormat(format)

Sets the format of the report.

Signature

```
   public void setReportFormat(Reports.ReportFormat format)

```

Parameters

```
   format
```

Type: Reports.ReportFormat

Return Value

Type: void

##### setReportType(reportType)

Sets the unique API name and display name for the report type.

Signature

```
   public void setReportType(Reports.ReportType reportType)

```

Parameters

```
   reportType
```

Type: Reports.ReportType

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setScope(scopeName)

Sets the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public void setScope(String scopeName)

```

Parameters

```
   scopeName
```

Type: String

Return Value

Type: void

##### setShowGrandTotal(showGrandTotal)

Specifies whether the report shows the grand total.

Signature

```
   public void setShowGrandTotal(Boolean showGrandTotal)

```

Parameters

```
   showGrandTotal
```

Type: Boolean

Return Value

Type: void

##### setShowSubtotals(showSubtotals)

Specifies whether the report shows subtotals, such as column or row totals.

Signature

```
   public void setShowSubtotals(Boolean showSubtotals)

```

Parameters

```
   showSubtotals
```

Type: Boolean

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setSortBy(column)

Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.

Signature

```
   public void setSortBy(List<Reports.SortColumn> column)

```

Parameters

```
   column
```

Type: List<Reports.SortColumn>

Return Value

Type: void

##### setStandardDateFilter(dateFilter)

Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.

Signature

```
   public void setStandardDateFilter(Reports.StandardDateFilter dateFilter)

```

Parameters

```
   dateFilter
```

Type: Reports.StandardDateFilter

Return Value

Type: void

##### setStandardFilters(filters)

Sets one or more standard filters on the report.

Signature

```
   public void setStandardFilters(List<Reports.StandardFilter> filters)

```

Parameters

```
   filters
```

Type: List<Reports.StandardFilter>

Return Value

Type: void


### Apex Reference Guide ReportResults Class

##### setTopRows(topRows)

Applies a row limit filter to a report.

Signature

```
   public Reports.TopRows setTopRows(Reports.TopRows topRows)

```

Parameters

```
   topRows
```

Type: Reports.TopRows

Return Value

Type: void

### ReportResults Class

Contains the results of running a report.

Namespace

Reports

#### ReportResults Methods

### The following are methods for ReportResults . All are instance methods.

IN THIS SECTION:

getAllData()
Returns all report data.

getFactMap()
Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

getGroupingsAcross()
Returns a collection of column groupings, keys, and values.

getGroupingsDown()
Returns a collection of row groupings, keys, and values.

getHasDetailRows()
Returns information about whether the fact map has detail rows.

getReportExtendedMetadata()
Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

getReportMetadata()
Returns metadata about the report, including grouping and summary information.


Apex Reference Guide ReportResults Class

##### getAllData()

Returns all report data.

Syntax

```
   public Boolean getAllData()

```

Return Value

Type: Boolean

Usage

When `true`, indicates that all report results are returned.

When `false`, indicates that results are returned for the same number of rows as in a report run in Salesforce.

Note: For reports that contain too many records, use filters to refine results.

##### getFactMap()

Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

Syntax

```
   public MAP<String,Reports.ReportFact> getFactMap()

```

Return Value

Type: Map<String,Reports.ReportFact>

##### getGroupingsAcross()

Returns a collection of column groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsAcross()

```

Return Value

Type: Reports.Dimension

##### getGroupingsDown()

Returns a collection of row groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsDown()

```


### Apex Reference Guide ReportScopeInfo Class

Return Value

Type: Reports.Dimension

##### getHasDetailRows()

Returns information about whether the fact map has detail rows.

Syntax

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean

Usage

**•** When `true`, indicates that the fact map returns values for summary-level and record-level data.

**•** When `false`, indicates that the fact map returns summary values.

##### getReportExtendedMetadata()

Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns metadata about the report, including grouping and summary information.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```

Return Value

Type: Reports.ReportMetadata

### ReportScopeInfo Class

Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you can
set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .


### Apex Reference Guide ReportScopeValue Class

Namespace

Reports

IN THIS SECTION:

#### ReportScopeInfo Methods ReportScopeInfo Methods The following are methods for ReportScopeInfo .

IN THIS SECTION:

##### getDefaultValue()

Returns the default scope of the data to display in the report.

##### getValues()

Returns a list of scope values specified for the report.

##### getDefaultValue()

Returns the default scope of the data to display in the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of scope values specified for the report.

Signature

```
   public List<Reports.ReportScopeValue> getValues()

```

Return Value

Type: List<Reports.ReportScopeValue>

### ReportScopeValue Class

Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .


Apex Reference Guide ReportScopeValue Class

Namespace

Reports

IN THIS SECTION:

#### ReportScopeValue Methods ReportScopeValue Methods The following are methods for ReportScopeValue .

IN THIS SECTION:

##### getAllowsDivision()

Returns a boolean value that indicates whether you can segment the report by this scope.

##### getLabel()

Returns the display name of the scope of the report.

##### getValue()

Returns the scope value for the report.

##### getAllowsDivision()

Returns a boolean value that indicates whether you can segment the report by this scope.

Signature

```
   public Boolean getAllowsDivision()

```

Return Value

Type: Boolean

##### getLabel()

Returns the display name of the scope of the report.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the scope value for the report.


### Apex Reference Guide ReportType Class

Signature

```
   public String getValue()

```

Return Value

Type: String

### ReportType Class

Contains the unique API name and display name for the report type.

Namespace

Reports

#### ReportType Methods

### The following are methods for ReportType . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the report type.

##### getType()

Returns the unique identifier of the report type.

##### getLabel()

Returns the localized display name of the report type.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the unique identifier of the report type.

Syntax

```
   public String getType()

```

Return Value

Type: String


### Apex Reference Guide ReportTypeColumn Class ReportTypeColumn Class

Contains detailed report type metadata about a field, including data type, display name, and filter values.

Namespace

Reports

#### ReportTypeColumn Methods

### The following are methods for ReportTypeColumn . All are instance methods.

IN THIS SECTION:

##### getDataType()

Returns the data type of the field.

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox
fields always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values
can’t be determined.

getFilterable()
If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

getLabel()
Returns the localized display name of the field.

getName()
Returns the unique API name of the field.

##### getDataType()

Returns the data type of the field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox fields
always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values can’t be
determined.

Syntax

```
   public LIST<Reports.FilterValue> getFilterValues()

```


### Apex Reference Guide ReportTypeColumnCategory Class

Return Value

Type: List<Reports.FilterValue>

##### getFilterable()

If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

Syntax

```
   public Boolean getFilterable()

```

Return Value

Type: Boolean

##### getLabel()

Returns the localized display name of the field.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique API name of the field.

Syntax

```
   public String getName()

```

Return Value

Type: String

### ReportTypeColumnCategory Class

Information about categories of fields in a report type.

Namespace

Reports


Apex Reference Guide ReportTypeColumnCategory Class

Usage

A report type column category is a set of fields that the report type grants access to. For example, an opportunity report has categories
like _Opportunity Information_ and _Primary Contact_ . The Opportunity Information category has fields like _Amount_, _Probability_, and _Close_
_Date_ .

Get category information about a report by first getting the report metadata:

```
   // Get the report ID

   List <Report> reportList = [SELECT Id,DeveloperName FROM Report where DeveloperName =

   'Q1_Opportunities2'];

   String reportId = (String)reportList.get(0).get('Id');

   // Describe the report

   Reports.ReportDescribeResult describeResults =

   Reports.ReportManager.describeReport(reportId);

   // Get report type metadata

   Reports.ReportTypeMetadata reportTypeMetadata = describeResults.getReportTypeMetadata();

   // Get report type column categories

   List<Reports.ReportTypeColumnCategory> reportTypeColumnCategories =

   reportTypeMetadata.getCategories();

   System.debug('reportTypeColumnCategories: ' + reportTypeColumnCategories);

#### ReportTypeColumnCategory Methods The following are methods for ReportTypeColumnCategory . All are instance methods.

```

IN THIS SECTION:

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

getLabel()
Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts
with Contacts custom report type, `Account General` is the display name of the section that contains fields on general account
information.

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

Syntax

```
   public MAP<String,Reports.ReportTypeColumn> getColumns()

```

Return Value

Type: Map<String,Reports.ReportTypeColumn>


### Apex Reference Guide ReportTypeMetadata Class

##### getLabel()

Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts with
Contacts custom report type, `Account General` is the display name of the section that contains fields on general account information.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

### ReportTypeMetadata Class

Contains report type metadata, which gives you information about the fields that are available in each section of the report type, plus
filter information for those fields.

Namespace

Reports

IN THIS SECTION:

#### ReportTypeMetadata Methods ReportTypeMetadata Methods

### The following are methods for ReportTypeMetadata . All are instance methods.

IN THIS SECTION:

##### getCategories()

Returns all fields in the report type. The fields are organized by section.

getDivisionInfo()
Returns the default division and a list of all possible divisions that can be applied to this type of report.

getScopeInfo()
Returns information about the scopes that can be applied to this type of report.

getStandardDateFilterDurationGroups()
Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based
on a user-defined date range.

getStandardFilterInfos()
Returns information about standard date filters that can be applied to this type of report.

##### getCategories()

Returns all fields in the report type. The fields are organized by section.


Apex Reference Guide ReportTypeMetadata Class

Syntax

```
   public LIST<Reports.ReportTypeColumnCategory> getCategories()

```

Return Value

Type: List<Reports.ReportTypeColumnCategory>

##### getDivisionInfo()

Returns the default division and a list of all possible divisions that can be applied to this type of report.

Signature

```
   public Reports.ReportDivisionInfo getDivisionInfo()

```

Return Value

Type: Reports.ReportDivisionInfo

##### getScopeInfo()

Returns information about the scopes that can be applied to this type of report.

Signature

```
   public Reports.ReportScopeInfo getScopeInfo()

```

Return Value

Type: Reports.ReportScopeInfo

##### getStandardDateFilterDurationGroups()

Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based on
a user-defined date range.

Signature

```
   public List<Reports.StandardDateFilterDurationGroup>

##### `getStandardDateFilterDurationGroups()`

```

Return Value

Type: List<Reports.StandardDateFilterDurationGroup>

##### getStandardFilterInfos()

Returns information about standard date filters that can be applied to this type of report.


### Apex Reference Guide SortColumn Class

Signature

```
   public Map<String,Reports.StandardFilterInfo> getStandardFilterInfos()

```

Return Value

Type: Map<String,Reports.StandardFilterInfo>

### SortColumn Class

Contains information about the sort column used in the report.

Namespace

Reports

IN THIS SECTION:

#### SortColumn Methods SortColumn Methods

### The following are methods for SortColumn .

IN THIS SECTION:

##### getSortColumn()

Returns the column used to sort the records in the report.

getSortOrder()
Returns the the sort order— ascending or descending—for the sort column.

setSortColumn(sortColumn)
Sets the column used to sort the records in the report.

setSortOrder(SortOrder)
Sets the sort order— ascending or descending—for the sort column.

##### getSortColumn()

Returns the column used to sort the records in the report.

Signature

```
   public String getSortColumn()

```

Return Value

Type: String


### Apex Reference Guide StandardDateFilter Class

##### getSortOrder()

Returns the the sort order— ascending or descending—for the sort column.

Signature

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder

##### setSortColumn(sortColumn)

Sets the column used to sort the records in the report.

Signature

```
   public void setSortColumn(String sortColumn)

```

Parameters

```
   sortColumn
```

Type: String

Return Value

Type: void

##### setSortOrder(SortOrder)

Sets the sort order— ascending or descending—for the sort column.

Signature

```
   public void setSortOrder(Reports.ColumnSortOrder sortOrder)

```

Parameters

```
   sortOrder
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

### StandardDateFilter Class

Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.


Apex Reference Guide StandardDateFilter Class

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilter Methods StandardDateFilter Methods The following are methods for StandardDateFilter .

IN THIS SECTION:

##### getColumn()

Returns the API name of the standard date filter column.

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date
filter.

getEndDate()
Returns the end date of the standard date filter.

getStartDate()
Returns the start date for the standard date filter.

setColumn(standardDateFilterColumnName)
Sets the API name of the standard date filter column.

setDurationValue(durationName)
Sets the API name of the standard date filter.

setEndDate(endDate)
Sets the end date for the standard date filter.

setStartDate(startDate)
Sets the start date for the standard date filter.

##### getColumn()

Returns the API name of the standard date filter column.

Signature

```
   public String getColumn()

```

Return Value

Type: String

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date filter.


Apex Reference Guide StandardDateFilter Class

Signature

```
   public String getDurationValue()

```

Return Value

Type: String

##### getEndDate()

Returns the end date of the standard date filter.

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getStartDate()

Returns the start date for the standard date filter.

Signature

```
   public String getStartDate()

```

Return Value

Type: String

##### setColumn(standardDateFilterColumnName)

Sets the API name of the standard date filter column.

Signature

```
   public void setColumn(String standardDateFilterColumnName)

```

Parameters

```
   standardDateFilterColumnName
```

Type: String

Return Value

Type: void


Apex Reference Guide StandardDateFilter Class

##### setDurationValue(durationName)

Sets the API name of the standard date filter.

Signature

```
   public void setDurationValue(String durationName)

```

Parameters

```
   durationName
```

Type: String

Return Value

Type: void

##### setEndDate(endDate)

Sets the end date for the standard date filter.

Signature

```
   public void setEndDate(String endDate)

```

Parameters

```
   endDate
```

Type: String

Return Value

Type: void

##### setStartDate(startDate)

Sets the start date for the standard date filter.

Signature

```
   public void setStartDate(String startDate)

```

Parameters

```
   startDate
```

Type: String

Return Value

Type: void


### Apex Reference Guide StandardDateFilterDuration Class StandardDateFilterDuration Class

Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display label
of the standard date filter duration as well as the start and end dates.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilterDuration Methods StandardDateFilterDuration Methods

### The following are methods for StandardDateFilterDuration .

IN THIS SECTION:

##### getEndDate()

Returns the end date of the date filter.

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.

getStartDate()
Returns the start date of the date filter.

getValue()
Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

##### getEndDate()

Returns the end date of the date filter.

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.


### Apex Reference Guide StandardDateFilterDurationGroup Class

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getStartDate()

Returns the start date of the date filter.

Signature

```
   public String getStartDate()

```

Return Value

Type: String

##### getValue()

Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

Signature

```
   public String getValue()

```

Return Value

Type: String

### StandardDateFilterDurationGroup Class

Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that fall
under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar Week`,
`Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilterDurationGroup Methods StandardDateFilterDurationGroup Methods

### The following are methods for StandardDateFilterDurationGroup .


### Apex Reference Guide StandardFilter Class

IN THIS SECTION:

##### getLabel()

Returns the display label for the standard date filter grouping.

##### getStandardDateFilterDurations()

Returns the standard date filter groupings.

##### getLabel()

Returns the display label for the standard date filter grouping.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getStandardDateFilterDurations()

Returns the standard date filter groupings.

Signature

```
   public List<Reports.StandardDateFilterDuration> getStandardDateFilterDurations()

```

Return Value

Type: List<Reports.StandardDateFilterDuration>

For example, a standard filter date grouping might look like this:

```
   Reports.StandardDateFilterDuration[endDate=2015-12-31, label=Current FY,

   startDate=2015-01-01, value=THIS_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous FY,

   startDate=2014-01-01, value=LAST_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous 2 FY,

   startDate=2013-01-01, value=LAST_N_FISCAL_YEARS:2]

### StandardFilter Class

```

Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

Namespace

Reports


Apex Reference Guide StandardFilter Class

Usage

Use to get or set standard filters on a report. Standard filters vary by report type. For example, standard filters for reports on the Opportunity
object are Show, Opportunity Status, and Probability.

IN THIS SECTION:

#### StandardFilter Methods StandardFilter Methods The following are methods for StandardFilter .

IN THIS SECTION:

##### getName()

Return the API name of the standard filter.

##### getValue()

Returns the standard filter value.

setName(name)
Sets the API name of the standard filter.

setValue(value)
Sets the standard filter value.

##### getName()

Return the API name of the standard filter.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getValue()

Returns the standard filter value.

Signature

```
   public String getValue()

```

Return Value

Type: String


### Apex Reference Guide StandardFilterInfo Class

##### setName(name)

Sets the API name of the standard filter.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void

##### setValue(value)

Sets the standard filter value.

Signature

```
   public void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: void

### StandardFilterInfo Class

Is an abstract base class for an object that provides standard filter information.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfo Methods StandardFilterInfo Methods

### The following are methods for StandardFilterInfo .


### Apex Reference Guide StandardFilterInfoPicklist Class

IN THIS SECTION:

##### getLabel()

Returns the display label of the standard filter.

##### getType()

Returns the type of standard filter.

##### getLabel()

Returns the display label of the standard filter.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the type of standard filter.

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterInfoPicklist Class

Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value, and
a list of all possible picklist values.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfoPicklist Methods StandardFilterInfoPicklist Methods

### The following are methods for StandardFilterInfoPicklist .


Apex Reference Guide StandardFilterInfoPicklist Class

IN THIS SECTION:

##### getDefaultValue()

Returns the default value for the standard filter picklist.

##### getFilterValues()

Returns a list of standard filter picklist values.

##### getLabel()

Returns the display name of the standard filter picklist.

##### getType()

Returns the type of the standard filter picklist.

##### getDefaultValue()

Returns the default value for the standard filter picklist.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getFilterValues()

Returns a list of standard filter picklist values.

Signature

```
   public List<Reports.FilterValue> getFilterValues()

```

Return Value

Type: List<Reports.FilterValue>

##### getLabel()

Returns the display name of the standard filter picklist.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the type of the standard filter picklist.


### Apex Reference Guide StandardFilterType Enum

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterType Enum The StandardFilterType enum describes the type of standard filters in a report. The getType() method returns a

`Reports.StandardFilterType` enum value.

Namespace

Reports

Enum Values

The following are the values of the `Reports.StandardFilterType` enum.

**Value** **Description**

`PICKLIST` Values for the standard filter type.

`STRING` String values.

### SummaryValue Class

Contains summary data for a cell of the report.

Namespace

Reports

#### SummaryValue Methods

### The following are methods for SummaryValue . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the formatted summary data for a specified cell.

getValue()
Returns the numeric value of the summary data for a specified cell.

##### getLabel()

Returns the formatted summary data for a specified cell.


### Apex Reference Guide ThresholdInformation Class

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the numeric value of the summary data for a specified cell.

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ThresholdInformation Class

Contains a list of evaluated conditions for a report notification.

Namespace

Reports

IN THIS SECTION:

#### ThresholdInformation Constructors

ThresholdInformation Methods

#### ThresholdInformation Constructors

### The following are constructors for ThresholdInformation .

IN THIS SECTION:

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

Signature

```
   public ThresholdInformation(List<Reports.EvaluatedCondition> evaluatedConditions)

```


### Apex Reference Guide TopRows Class

Parameters

```
   evaluatedConditions
```

Type: List<Reports.EvaluatedCondition>

A list of `Reports.EvaluatedCondition` objects.

#### ThresholdInformation Methods The following are methods for ThresholdInformation .

IN THIS SECTION:

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

Signature

```
   public List<Reports.EvaluatedCondition> getEvaluatedConditions()

```

Return Value

Type: List<Reports.EvaluatedCondition>

### TopRows Class

Contains methods and constructors for working with information about a row limit filter.

Namespace

Reports

IN THIS SECTION:

#### TopRows Constructors

TopRows Methods

#### TopRows Constructors

### The following are constructors for TopRows .

IN THIS SECTION:

TopRows(rowLimit, direction)
Creates an instance of the `Reports.TopRows` class using the specified parameters.


Apex Reference Guide TopRows Class

##### TopRows()

Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

##### TopRows(rowLimit, direction)

Creates an instance of the `Reports.TopRows` class using the specified parameters.

Signature

```
   public TopRows(Integer rowLimit, Reports.ColumnSortOrder direction)

```

Parameters

```
   rowLimit
```

Type: Integer

The number of rows returned in the report.

```
   direction
```

Type: Reports.ColumnSortOrder

The sort order of the report rows.

##### TopRows()

Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

Signature

```
   public TopRows()

#### TopRows Methods

##### The following are methods for TopRows .

```

IN THIS SECTION:

getDirection()
Returns the sort order of the report rows.

getRowLimit()
Returns the maximum number of rows shown in the report.

setDirection(value)
Sets the sort order of the report’s rows.

setDirection(direction)
Sets the sort order of the report’s rows.

setRowLimit(rowLimit)
Sets the maximum number of rows included in the report.

toString()
Returns a string.


Apex Reference Guide TopRows Class

##### getDirection()

Returns the sort order of the report rows.

Signature

```
   public Reports.ColumnSortOrder getDirection()

```

Return Value

Type: Reports.ColumnSortOrder

##### getRowLimit()

Returns the maximum number of rows shown in the report.

Signature

```
   public Integer getRowLimit()

```

Return Value

Type: Integer

##### setDirection(value)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.ColumnSortOrder.

Return Value

Type: void

##### setDirection(direction)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(Reports.ColumnSortOrder direction)

```


### Apex Reference Guide Reports Exceptions

Parameters

```
   direction
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

##### setRowLimit(rowLimit)

Sets the maximum number of rows included in the report.

Signature

```
   public void setRowLimit(Integer rowLimit)

```

Parameters

```
   rowLimit
```

Type: Integer

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### Reports Exceptions The Reports namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3767.

### The Reports namespace contains these exceptions:

**Exception** **Description** **Methods**

`Reports.FeatureNotSupportedException` Invalid report format

`Reports.InstanceAccessException` Unable to access report
instance


## Apex Reference Guide RevSignaling Namespace

**Exception** **Description** **Methods**

`Reports.InvalidFilterException` Filter validation error `List<String> getFilterErrors()` returns a list of
filter errors

`Reports.InvalidReportMetadataException` Missing metadata for `List<String> getReportMetadataErrors()`
filters returns a list of metadata errors

`Reports.InvalidSnapshotDateException` Invalid historical report `List<String> getSnapshotDateErrors()` returns
format a list of snapshot date errors

`Reports.MetadataException` No selected report
columns

`Reports.ReportRunException` Error running report

`Reports.UnsupportedOperationException` Missing permissions for
running reports

## RevSignaling Namespace The RevSignaling namespace provides classes to extend the standard procedure plan implementation through custom logic. A

procedure plan helps you set up your procedures, configure the procedure execution settings, and relate them to a context definition
in one centralized location based on your requirements.

## The RevSignaling namespace includes these classes and an interface.

**•** [ProcedurePlan Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_ProcedurePlan.htm)

**•** [SignalingApexProcessor Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_interface_RevSignaling_SignalingApexProcessor.htm)

**•** [TransactionRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionRequest.htm)

**•** [TransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionResponse.htm)

## RevSalesTrxn Namespace The RevSalesTrxn namespace provides classes and methods to create a sales transaction, such as a quote or an order, with

integrated pricing and configuration.

## The RevSalesTrxn namespace includes these classes.

**•** [ConfigurationOptionsInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm)

**•** [GraphRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_GraphRequest.htm)

**•** [PlaceSalesTransactionException Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm)

**•** [PlaceSalesTransactionExecutor Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm)

**•** [PlaceSalesTransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm)

**•** [RecordResource Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordResource.htm)

**•** [RecordWithReferenceRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm)

SEE ALSO:

_Salesforce Help_ [: Build Your Procedure Plan Framework](https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_plan_framework.htm&language=en_US)


## Apex Reference Guide RichMessaging Namespace RichMessaging Namespace

Provides objects and methods for handling content in enhanced Messaging channels.

## The following are the classes in the RichMessaging namespace.

IN THIS SECTION:

AbstractTiming Class
Parent class for other RichMessaging timing classes.

AddressableContact Class
Represents an addressable contact.

AuthRequestHandler Interface
Use this interface to handle authorization request responses.

AuthRequestResponse Class
This class contains authorization request response data.

AuthRequestResult Class
This class contains the result from handling the authorization request response.

AuthRequestResultStatus Enum
This enum describes the authentication result status.

DeferredTiming Class
Represents timing for a transaction that occurs in the future.

MessageDefinitionInputParameter Class
Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to
structured content payloads in rich content messages.

PaymentItemStatus Enum
Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

PaymentLineItem Class
Represents a payment line item in payment requests sent in enhanced Messaging channels.

PaymentMethod Class
Represents a payment method.

PostalAddress Class
Represents the postal address.

ProcessFormHandler Interface
Apex interface that processes the responses to forms submitted in a messaging session.

ProcessPaymentHandler Interface
Interface used to process payment requests.

ProcessPaymentRequest Class
Represents a request to process a payment.

ProcessPaymentResult Class
Represents the result of a payment processing operation.


### Apex Reference Guide AbstractTiming Class

ProcessPaymentResultStatus Enum
Represents the status of a payment processing result.

RecurringTiming Class
Represents a payment that occurs on a regular basis.

ShippingMethod Class
Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

TimeSlotOption Class
Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.

TimingIntervalUnit Enum
Represents an enumerated type that describes the timing interval.

TimingType Enum
Represents an enumerated type that describes the type of timing.

### AbstractTiming Class

Parent class for other RichMessaging timing classes.

Namespace

RichMessaging

SEE ALSO:

DeferredTiming Class

RecurringTiming Class

### AddressableContact Class

Represents an addressable contact.

Namespace

RichMessaging

IN THIS SECTION:

#### AddressableContact Constructors

AddressableContact Properties

#### AddressableContact Constructors

### The following are constructors for AddressableContact .


Apex Reference Guide AddressableContact Class

IN THIS SECTION:

##### AddressableContact(givenName, phoneticGivenName, familyName, phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

Creates a new instance of the `RichMessaging.AddressableContact` class.

##### **`AddressableContact(givenName, phoneticGivenName, familyName,`**

```
  phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

```

Creates a new instance of the `RichMessaging.AddressableContact` class.

Signature

```
   public AddressableContact(String givenName, String phoneticGivenName, String familyName,

   String phoneticFamilyName, String emailAddress, String phoneNumber,

   RichMessaging.PostalAddress postalAddress)

```

Parameters

```
   givenName
```

Type: String

The contact’s first name.

```
   phoneticGivenName
```

Type: String

The phonetic spelling of the contact’s first name.

```
   familyName
```

Type: String

The contact’s surname.

```
   phoneticFamilyName
```

Type: String

The phonetic spelling of the contact’s surname.

```
   emailAddress
```

Type: String

The contact’s email address.

```
   phoneNumber
```

Type: String

The contact’s phone number.

```
   postalAddress
```

Type: RichMessaging.PostalAddress

The contact’s postal address.

#### AddressableContact Properties

##### The following are properties for AddressableContact .


Apex Reference Guide AddressableContact Class

IN THIS SECTION:

##### emailAddress

The contact’s email address.

##### familyName

The contact’s surname.

##### givenName

The contact’s first name.

phoneNumber
The contact’s phone number.

phoneticFamilyName
The phonetic spelling of the contact’s surname.

phoneticGivenName
The phonetic spelling of the contact’s first name.

postalAddress
The contact’s postal address.

##### **`emailAddress`**

The contact’s email address.

Signature

```
   public String emailAddress {get; set;}

```

Property Value

Type: String

##### **`familyName`**

The contact’s surname.

Signature

```
   public String familyName {get; set;}

```

Property Value

Type: String

##### **`givenName`**

The contact’s first name.

Signature

```
   public String givenName {get; set;}

```


Apex Reference Guide AddressableContact Class

Property Value

Type: String

##### **`phoneNumber`**

The contact’s phone number.

Signature

```
   public String phoneNumber {get; set;}

```

Property Value

Type: String

##### **`phoneticFamilyName`**

The phonetic spelling of the contact’s surname.

Signature

```
   public String phoneticFamilyName {get; set;}

```

Property Value

Type: String

##### **`phoneticGivenName`**

The phonetic spelling of the contact’s first name.

Signature

```
   public String phoneticGivenName {get; set;}

```

Property Value

Type: String

##### **`postalAddress`**

The contact’s postal address.

Signature

```
   public RichMessaging.PostalAddress postalAddress {get; set;}

```

Property Value

Type: RichMessaging.PostalAddress


### Apex Reference Guide AuthRequestHandler Interface AuthRequestHandler Interface

Use this interface to handle authorization request responses.

Namespace

RichMessaging on page 3302

Usage

[When using this interface, the following limits are overridden. See Execution Governors and Limits in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**Table 1: Overridden Limits**

IN THIS SECTION:

#### AuthRequestHandler Methods

AuthRequestHandler Example Implementation

#### AuthRequestHandler Methods

### The following are methods for AuthRequestHandler .

IN THIS SECTION:

##### handleAuthRequest(var1)

Handles authorization request response.

##### **`handleAuthRequest(var1)`**

Handles authorization request response.

Signature

```
   public RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse var1)

```


Apex Reference Guide AuthRequestHandler Interface

Parameters

```
   var1
```

Type: RichMessaging.AuthRequestResponse on page 3309

The authorization response.

Return Value

Type: RichMessaging.AuthRequestResult on page 3311

#### AuthRequestHandler Example Implementation

This is an example implementation of the `RichMessaging.AuthRequestHandler` interface.

```
   global class SampleAuthRequestHandler implements RichMessaging.AuthRequestHandler {

      global RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse authReqResponse) {

        // Get contact email from messaging session

        String sessionId = authReqResponse.getContextRecordId();

        String contactEmail = [select MessagingSession.EndUserContact.Email from

   MessagingSession where id = :sessionId].EndUserContact.Email;

        RichMessaging.AuthRequestResultStatus authRequestStatus =

   RichMessaging.AuthRequestResultStatus.DECLINED;

        DateTime dt = DateTime.now();

        // Get user info if there's a valid contact email

        if (!String.isBlank(contactEmail)) {

           String userInfoUrl = 'https://api.MY_AUTH_DOMAIN.com/v1/';

           HttpRequest req = new HttpRequest();

           req.setEndpoint(userInfoUrl);

           req.setHeader('Content-Type','application/json');

           req.setMethod('GET');

           req.setHeader('Authorization', 'Bearer '+authReqResponse.getAccessToken());

           Http http = new Http();

           HTTPResponse res = http.send(req);

           String responseBody = res.getBody();

           UserWrapper userInfo = (UserWrapper)System.JSON.deserialize(responseBody,

   UserWrapper.class);

           if (userInfo.email == contactEmail) {

             authRequestStatus = RichMessaging.AuthRequestResultStatus.AUTHENTICATED;

             dt = dt.addHours(6);

           }

         }

        return new RichMessaging.AuthRequestResult(

           null,

```


### Apex Reference Guide AuthRequestResponse Class

```
           authRequestStatus,

           dt);

      }

      public class UserWrapper{

        public String href;

        public String display_name;

        public String type;

        public String country;

        public String product;

        public String email;

      }

   }

### AuthRequestResponse Class

```

This class contains authorization request response data.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResponse Constructors

AuthRequestResponse Methods

#### AuthRequestResponse Constructors

### The following are constructors for AuthRequestResponse .

IN THIS SECTION:

##### AuthRequestResponse(accessToken, contextRecordId, authProviderName)

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

##### **`AuthRequestResponse(accessToken, contextRecordId, authProviderName)`**

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

Signature

```
   public AuthRequestResponse(String accessToken, String contextRecordId, String

   authProviderName)

```

Parameters

```
   accessToken
```

Type: String


Apex Reference Guide AuthRequestResponse Class

The authorization access token.

```
   contextRecordId
```

Type: String

The context record ID.

```
   authProviderName
```

Type: String

The provider name.

#### AuthRequestResponse Methods The following are methods for AuthRequestResponse .

IN THIS SECTION:

##### getAccessToken()

Gets the authorization access token.

##### getAuthProviderName()

Get the authorization provider name.

getContextRecordId()
Gets the context record ID.

##### **`getAccessToken()`**

Gets the authorization access token.

Signature

```
   public String getAccessToken()

```

Return Value

Type: String

The access token.

##### **`getAuthProviderName()`**

Get the authorization provider name.

Signature

```
   public String getAuthProviderName()

```

Return Value

Type: String

The authorization provider name.


### Apex Reference Guide AuthRequestResult Class

##### **`getContextRecordId()`**

Gets the context record ID.

Signature

```
   public String getContextRecordId()

```

Return Value

Type: String

The context record ID.

### AuthRequestResult Class

This class contains the result from handling the authorization request response.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResult Constructors

AuthRequestResult Properties

#### AuthRequestResult Constructors

### The following are constructors for AuthRequestResult .

IN THIS SECTION:

##### AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

##### **`AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)`**

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

Signature

```
   public AuthRequestResult(System.PageReference redirectPageReference,

   RichMessaging.AuthRequestResultStatus resultStatus, Datetime expirationDateTime)

```

Parameters

```
   redirectPageReference
```

Type: System.PageReference on page 3967

The reference to the redirect page.


Apex Reference Guide AuthRequestResult Class

##### _`resultStatus`_

Type: RichMessaging.AuthRequestResultStatus on page 3313

The result status value.

##### _`expirationDateTime`_

Type: Datetime

The expiration time.

#### AuthRequestResult Properties The following are properties for AuthRequestResult .

IN THIS SECTION:

##### expirationDateTime

The expiration date and time.

##### redirectPageReference

The reference to the redirect page.

##### resultStatus

The result status value.

##### **`expirationDateTime`**

The expiration date and time.

Signature

```
   public Datetime expirationDateTime {get; set;}

```

Property Value

Type: Datetime

##### **`redirectPageReference`**

The reference to the redirect page.

Signature

```
   public System.PageReference redirectPageReference {get; set;}

```

Property Value

Type: System.PageReference on page 3967

##### **`resultStatus`**

The result status value.


### Apex Reference Guide AuthRequestResultStatus Enum

Signature

```
   public RichMessaging.AuthRequestResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.AuthRequestResultStatus on page 3313

### AuthRequestResultStatus Enum

This enum describes the authentication result status.

Enum Values

The following are the values of the `RichMessaging.AuthRequestResultStatus` enum.

**Value** **Description**

`AUTHENTICATED` Authenticated result.

`DECLINED` Declined result.

### DeferredTiming Class

Represents timing for a transaction that occurs in the future.

Namespace

RichMessaging

IN THIS SECTION:

#### DeferredTiming Constructors

DeferredTiming Properties

#### DeferredTiming Constructors

### The following are constructors for DeferredTiming .

IN THIS SECTION:

##### DeferredTiming(deferredDate)

Creates a new instance of the `RichMessaging.DeferredTiming` class.

DeferredTiming()
Creates a new instance of the `RichMessaging.DeferredTiming` class.

##### **`DeferredTiming(deferredDate)`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.


Apex Reference Guide DeferredTiming Class

Signature

```
   public DeferredTiming(Datetime deferredDate)

```

Parameters

##### _`deferredDate`_

Type: Datetime

The deferred date.

##### **`DeferredTiming()`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.

Signature

```
   public DeferredTiming()

#### DeferredTiming Properties

##### The following are properties for DeferredTiming .

```

IN THIS SECTION:

##### deferredDate

The deferred date. Invocable variable.

##### deferredDateValue

The deferred date. Enabled for Lightning components.

timingType
Always returns “DeferredTiming”.

##### **`deferredDate`**

The deferred date. Invocable variable.

Signature

```
   public Datetime deferredDate {get; set;}

```

Property Value

Type: Datetime

##### **`deferredDateValue`**

The deferred date. Enabled for Lightning components.


### Apex Reference Guide MessageDefinitionInputParameter Class

Signature

```
   public Datetime deferredDateValue {get; set;}

```

Property Value

Type: Datetime

##### **`timingType`**

Always returns “DeferredTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### MessageDefinitionInputParameter Class

Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### MessageDefinitionInputParameter Properties MessageDefinitionInputParameter Properties

### The following are properties for MessageDefinitionInputParameter .

IN THIS SECTION:

booleanValue
A boolean input parameter.

booleanValues
A list of boolean parameters.

dateTimeValue
A datetime input parameter.

dateTimeValues
A list of datetime input parameters.


Apex Reference Guide MessageDefinitionInputParameter Class

dateValue
A date input parameter.

dateValues
A list of date input parameters.

name
A name input parameter.

numberValue
A number input parameter.

numberValues
A list of number input parameters.

recordIdValue
A record ID input parameter.

recordIdValues
A list of record ID input parameters.

textValue
A text input parameter.

textValues
A list of text input parameters.

##### **`booleanValue`**

A boolean input parameter.

Signature

```
   public Boolean booleanValue {get; set;}

```

Property Value

Type: Boolean

##### **`booleanValues`**

A list of boolean parameters.

Signature

```
   public List<Boolean> booleanValues {get; set;}

```

Property Value

Type: List on page 3874<Boolean>

##### **`dateTimeValue`**

A datetime input parameter.


Apex Reference Guide MessageDefinitionInputParameter Class

Signature

```
   public Datetime dateTimeValue {get; set;}

```

Property Value

Type: Datetime

##### **`dateTimeValues`**

A list of datetime input parameters.

Signature

```
   public List<Datetime> dateTimeValues {get; set;}

```

Property Value

Type: List on page 3874<Datetime>

##### **`dateValue`**

A date input parameter.

Signature

```
   public Date dateValue {get; set;}

```

Property Value

Type: Date

##### **`dateValues`**

A list of date input parameters.

Signature

```
   public List<Date> dateValues {get; set;}

```

Property Value

Type: List on page 3874<Date>

##### **`name`**

A name input parameter.

Signature

```
   public String name {get; set;}

```


Apex Reference Guide MessageDefinitionInputParameter Class

Property Value

Type: String

##### **`numberValue`**

A number input parameter.

Signature

```
   public Double numberValue {get; set;}

```

Property Value

Type: Double

##### **`numberValues`**

A list of number input parameters.

Signature

```
   public List<Double> numberValues {get; set;}

```

Property Value

Type: List on page 3874<Double>

##### **`recordIdValue`**

A record ID input parameter.

Signature

```
   public String recordIdValue {get; set;}

```

Property Value

Type: String

##### **`recordIdValues`**

A list of record ID input parameters.

Signature

```
   public List<String> recordIdValues {get; set;}

```

Property Value

Type: List on page 3874<String>


### Apex Reference Guide PaymentItemStatus Enum

##### **`textValue`**

A text input parameter.

Signature

```
   public String textValue {get; set;}

```

Property Value

Type: String

##### **`textValues`**

A list of text input parameters.

Signature

```
   public List<String> textValues {get; set;}

```

Property Value

Type: List on page 3874<String>

### PaymentItemStatus Enum

Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

Enum Values

The following are the values of the `RichMessaging.PaymentItemStatus` enum.

**Value** **Description**

`FinalCost` Indicates that the payment item's cost is final and has been determined.

`PendingCost` Indicates that the payment item's cost is pending and has not been determined
yet.

### PaymentLineItem Class

Represents a payment line item in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging


Apex Reference Guide PaymentLineItem Class

Example

```
   public with sharing class MessagingPaymentLineItems {

      @InvocableMethod

      public static List<List<RichMessaging.PaymentLineItem>> getLineItems() {

        Double amount = 0.25;

        List<List<RichMessaging.PaymentLineItem>> result = new

   List<List<RichMessaging.PaymentLineItem>>();

        RichMessaging.PaymentLineItem pizza = new RichMessaging.PaymentLineItem('pizza',

   amount);

        RichMessaging.PaymentLineItem pasta = new RichMessaging.PaymentLineItem('pasta',

   amount);

        pizza.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        pasta.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        List<RichMessaging.PaymentLineItem> options = new

   List<RichMessaging.PaymentLineItem>{

           pizza, pasta

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### PaymentLineItem Constructors

PaymentLineItem Properties

PaymentLineItem Methods

#### PaymentLineItem Constructors The following are constructors for PaymentLineItem .

IN THIS SECTION:

##### PaymentLineItem(label, amount, timing)

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem(label, amount)
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem()
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

##### **`PaymentLineItem(label, amount, timing)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.


Apex Reference Guide PaymentLineItem Class

Signature

```
   public PaymentLineItem(String label, Double amount, RichMessaging.AbstractTiming timing)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.

```
   amount
```

Type: Double

The amount of the payment line item.

```
   timing
```

Type: RichMessaging.AbstractTiming

The timing of the payment line item.

##### **`PaymentLineItem(label, amount)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem(String label, Double amount)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.

```
   amount
```

Type: Double

The amount of the payment line item.

##### **`PaymentLineItem()`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem()

#### PaymentLineItem Properties

##### The following are properties for PaymentLineItem .

```


Apex Reference Guide PaymentLineItem Class

IN THIS SECTION:

##### amount

The amount of the payment line item.

##### amountValue

The amount value of the payment line item.

automaticReloadPaymentThresholdAmount
The automatic reload payment threshold amount of the payment line item.

automaticReloadPaymentThresholdAmountValue
The automatic reload payment threshold amount value of the payment line item.

label
The label of the payment line item.

labelValue
The label value of the payment line item.

lineItemType
The line item type of the payment line item. Read-only variable.

status
The status of the payment line item.

statusValue
The status value of the payment line item.

timing
The timing of the payment line item.

timingValue
The timing value of the payment line item.

##### **`amount`**

The amount of the payment line item.

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the payment line item.

Signature

```
   public Double amountValue {get; set;}

```


Apex Reference Guide PaymentLineItem Class

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmount`**

The automatic reload payment threshold amount of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmount {get; set;}

```

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmountValue`**

The automatic reload payment threshold amount value of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmountValue {get; set;}

```

Property Value

Type: Double

##### **`label`**

The label of the payment line item.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the payment line item.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String


Apex Reference Guide PaymentLineItem Class

##### **`lineItemType`**

The line item type of the payment line item. Read-only variable.

Signature

```
   public String lineItemType {get; set;}

```

Property Value

Type: String

##### **`status`**

The status of the payment line item.

Signature

```
   public String status {get; set;}

```

Property Value

Type: String

##### **`statusValue`**

The status value of the payment line item.

Signature

```
   public RichMessaging.PaymentItemStatus statusValue {get; set;}

```

Property Value

Type: RichMessaging.PaymentItemStatus

##### **`timing`**

The timing of the payment line item.

Signature

```
   public RichMessaging.AbstractTiming timing {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

##### **`timingValue`**

The timing value of the payment line item.


### Apex Reference Guide PaymentMethod Class

Signature

```
   public RichMessaging.AbstractTiming timingValue {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

#### PaymentLineItem Methods The following are methods for PaymentLineItem .

### PaymentMethod Class

Represents a payment method.

Namespace

RichMessaging

IN THIS SECTION:

#### PaymentMethod Constructors

PaymentMethod Properties

#### PaymentMethod Constructors

### The following are constructors for PaymentMethod .

IN THIS SECTION:

##### PaymentMethod(network, paymentType, displayName)

Creates a new instance of the `RichMessaging.PaymentMethod` class.

##### **`PaymentMethod(network, paymentType, displayName)`**

Creates a new instance of the `RichMessaging.PaymentMethod` class.

Signature

```
   public PaymentMethod(String network, String paymentType, String displayName)

```

Parameters

```
   network
```

Type: String

The network associated with the payment method.

```
   paymentType
```

Type: String


Apex Reference Guide PaymentMethod Class

The payment type of the payment method.

##### _`displayName`_

Type: String

The display name of the payment method.

#### PaymentMethod Properties The following are properties for PaymentMethod .

IN THIS SECTION:

##### displayName

The display name of the payment method.

##### network

The network associated with the payment method.

##### paymentType

The payment type of the payment method.

##### **`displayName`**

The display name of the payment method.

Signature

```
   public String displayName {get; set;}

```

Property Value

Type: String

##### **`network`**

The network associated with the payment method.

Signature

```
   public String network {get; set;}

```

Property Value

Type: String

##### **`paymentType`**

The payment type of the payment method.

Signature

```
   public String paymentType {get; set;}

```


### Apex Reference Guide PostalAddress Class

Property Value

Type: String

### PostalAddress Class

Represents the postal address.

Namespace

RichMessaging

IN THIS SECTION:

#### PostalAddress Constructors

PostalAddress Properties

#### PostalAddress Constructors

### The following are constructors for PostalAddress .

IN THIS SECTION:

##### PostalAddress(addressLines, subLocality, locality, postalCode, subAdministrativeArea, administrativeArea, country, countryCode)

Creates a new instance of the `RichMessaging.PostalAddress` class.

##### **`PostalAddress(addressLines, subLocality, locality, postalCode,`**

```
  subAdministrativeArea, administrativeArea, country, countryCode)

```

Creates a new instance of the `RichMessaging.PostalAddress` class.

Signature

```
   public PostalAddress(List<String> addressLines, String subLocality, String locality,

   String postalCode, String subAdministrativeArea, String administrativeArea, String

   country, String countryCode)

```

Parameters

```
   addressLines
```

Type: List<String>

The street address.

```
   subLocality
```

Type: String

The sub-locality of the address.

```
   locality
```

Type: String

The locality of the address.


Apex Reference Guide PostalAddress Class

```
   postalCode
```

Type: String

The postal code.

```
   subAdministrativeArea
```

Type: String

The sub-administrative area.

```
   administrativeArea
```

Type: String

The administrative area.

```
   country
```

Type: String

The country.

```
   countryCode
```

Type: String

The country code.

#### PostalAddress Properties The following are properties for PostalAddress .

IN THIS SECTION:

##### addressLines

The street address.

administrativeArea
The administrative area.

country
The country.

countryCode
The country code.

locality
The locality of the address.

postalCode
The postal code.

subAdministrativeArea
The sub-administrative area.

subLocality
The sub-locality of the address.

##### **`addressLines`**

The street address.


Apex Reference Guide PostalAddress Class

Signature

```
   public List<String> addressLines {get; set;}

```

Property Value

Type: List<String>

##### **`administrativeArea`**

The administrative area.

Signature

```
   public String administrativeArea {get; set;}

```

Property Value

Type: String

##### **`country`**

The country.

Signature

```
   public String country {get; set;}

```

Property Value

Type: String

##### **`countryCode`**

The country code.

Signature

```
   public String countryCode {get; set;}

```

Property Value

Type: String

##### **`locality`**

The locality of the address.

Signature

```
   public String locality {get; set;}

```


### Apex Reference Guide ProcessFormHandler Interface

Property Value

Type: String

##### **`postalCode`**

The postal code.

Signature

```
   public String postalCode {get; set;}

```

Property Value

Type: String

##### **`subAdministrativeArea`**

The sub-administrative area.

Signature

```
   public String subAdministrativeArea {get; set;}

```

Property Value

Type: String

##### **`subLocality`**

The sub-locality of the address.

Signature

```
   public String subLocality {get; set;}

```

Property Value

Type: String

### ProcessFormHandler Interface

Apex interface that processes the responses to forms submitted in a messaging session.

Namespace

RichMessaging

IN THIS SECTION:

ProcessFormHandler Methods


Apex Reference Guide ProcessFormHandler Interface

#### ProcessFormHandler Methods The following are methods for ProcessFormHandler .

IN THIS SECTION:

##### processFormRequest

Processes the form request and returns the ID of the record created during form processing.

##### **`processFormRequest`**

Processes the form request and returns the ID of the record created during form processing.

Signature

```
   ID processFormRequest(RichMessaging.ProcessFormResponse formResponse)

```

Parameters

```
   formResponse
```

Type: RichMessaging.ProcessFormResponse

The form response.

Return Value

```
   ID
```

Type: RichMessaging.ProcessFormResponse

ProcessFormHandler Example Implementation

The sample `ContactApexFormHandler` Apex class automatically captures the customer's submitted details, creates a Contact
record in Salesforce, and returns the Contact record ID.

This is an example implementation of the `RichMessaging.ProcessFormHandler` interface.

```
   global class ContactApexFormHandler implements Richmessaging.ProcessFormHandler{

      global ID

##### `processFormRequest(RichMessaging.ProcessFormResponse formResponse) {`

        // Create a new Contact object

           Contact newContact = new Contact(

           Phone = formResponse.formValues.get('Phone'),

           Salutation = formResponse.formValues.get('Salutation'),

           Email = formResponse.formValues.get('Email')

           );

      // Insert the new contact into the database

      insert newContact;

      // Return the ID of the newly created contact

      return newContact.Id;

```

[For more information, see "Create a Form Based on an Apex Class" in this help topic.](https://help.salesforce.com/s/articleView?id=service.messaging_components_forms.htm&language=en_US)


### Apex Reference Guide ProcessPaymentHandler Interface ProcessPaymentHandler Interface

Interface used to process payment requests.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentHandler Methods ProcessPaymentHandler Example Implementation ProcessPaymentHandler Methods

### The following are methods for ProcessPaymentHandler .

IN THIS SECTION:

##### processPaymentRequest(var1)

Processes a payment request.

##### **`processPaymentRequest(var1)`**

Processes a payment request.

Signature

```
   public RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest var1)

```

Parameters

```
   var1
```

Type: RichMessaging.ProcessPaymentRequest

The payment request.

Return Value

Type: RichMessaging.ProcessPaymentResult

#### ProcessPaymentHandler Example Implementation

This is an example implementation of the `RichMessaging.ProcessPaymentHandler` interface.

```
   global class MyProcessPaymentHandler implements Richmessaging.ProcessPaymentHandler {

     global RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest paymentRequest) {

```


### Apex Reference Guide ProcessPaymentRequest Class

```
        // TODO: Reach out to your payment processor here and return success or failure

   based on the result of that request

        return new

   RichMessaging.ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus.SUCCESS);

     }

   }

### ProcessPaymentRequest Class

```

Represents a request to process a payment.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentRequest Constructors

ProcessPaymentRequest Properties

#### ProcessPaymentRequest Constructors

### The following are constructors for ProcessPaymentRequest .

IN THIS SECTION:

##### ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact, shippingContact, paymentMethod, shippingMethod,

contextRecordId)
Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

##### **`ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact,`**

```
  shippingContact, paymentMethod, shippingMethod, contextRecordId)

```

Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

Signature

```
   public ProcessPaymentRequest(String transactionIdentifier, String paymentData,

   RichMessaging.AddressableContact billingContact, RichMessaging.AddressableContact

   shippingContact, RichMessaging.PaymentMethod paymentMethod, RichMessaging.ShippingMethod

   shippingMethod, String contextRecordId)

```

Parameters

```
   transactionIdentifier
```

Type: String

The transaction identifier associated with the payment request.


Apex Reference Guide ProcessPaymentRequest Class

```
   paymentData
```

Type: String

The encrypted payment data for the payment request.

```
   billingContact
```

Type: RichMessaging.AddressableContact

The billing contact information for the payment request.

```
   shippingContact
```

Type: RichMessaging.AddressableContact

The shipping contact information for the payment request.

```
   paymentMethod
```

Type: RichMessaging.PaymentMethod

The payment method for the payment request.

```
   shippingMethod
```

Type: RichMessaging.ShippingMethod

The shipping method for the payment request.

```
   contextRecordId
```

Type: String

The context record ID associated with the payment request.

#### ProcessPaymentRequest Properties The following are properties for ProcessPaymentRequest .

IN THIS SECTION:

billingContact
The billing contact information for the payment request.

contextRecordId
The context record ID associated with the payment request.

paymentData
The encrypted payment data for the payment request.

paymentMethod
The payment method for the payment request.

shippingContact
The shipping contact information for the payment request.

shippingMethod
The shipping method for the payment request.

transactionIdentifier
The transaction identifier associated with the payment request.


Apex Reference Guide ProcessPaymentRequest Class

##### **`billingContact`**

The billing contact information for the payment request.

Signature

```
   public RichMessaging.AddressableContact billingContact {get; set;}

```

Property Value

Type: RichMessaging.AddressableContact

##### **`contextRecordId`**

The context record ID associated with the payment request.

Signature

```
   public String contextRecordId {get; set;}

```

Property Value

Type: String

##### **`paymentData`**

The encrypted payment data for the payment request.

Signature

```
   public String paymentData {get; set;}

```

Property Value

Type: String

##### **`paymentMethod`**

The payment method for the payment request.

Signature

```
   public RichMessaging.PaymentMethod paymentMethod {get; set;}

```

Property Value

Type: RichMessaging.PaymentMethod

##### **`shippingContact`**

The shipping contact information for the payment request.


### Apex Reference Guide ProcessPaymentResult Class

Signature

```
   public RichMessaging.AddressableContact shippingContact {get; set;}

```

Property Value

Type: RichMessaging.AddressableContact

##### **`shippingMethod`**

The shipping method for the payment request.

Signature

```
   public RichMessaging.ShippingMethod shippingMethod {get; set;}

```

Property Value

Type: RichMessaging.ShippingMethod

##### **`transactionIdentifier`**

The transaction identifier associated with the payment request.

Signature

```
   public String transactionIdentifier {get; set;}

```

Property Value

Type: String

### ProcessPaymentResult Class

Represents the result of a payment processing operation.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentResult Constructors

ProcessPaymentResult Properties

#### ProcessPaymentResult Constructors

### The following are constructors for ProcessPaymentResult .


Apex Reference Guide ProcessPaymentResult Class

IN THIS SECTION:

##### ProcessPaymentResult(resultStatus, errorMessage)

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

##### ProcessPaymentResult(resultStatus)

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

##### **`ProcessPaymentResult(resultStatus, errorMessage)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus,

   String errorMessage)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

```
   errorMessage
```

Type: String

The error message associated with the payment processing result, if any.

##### **`ProcessPaymentResult(resultStatus)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

#### ProcessPaymentResult Properties

##### The following are properties for ProcessPaymentResult .

IN THIS SECTION:

errorMessage
The error message associated with the payment processing result, if any.


### Apex Reference Guide ProcessPaymentResultStatus Enum

##### resultStatus

The status of the payment processing result.

##### **`errorMessage`**

The error message associated with the payment processing result, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### **`resultStatus`**

The status of the payment processing result.

Signature

```
   public RichMessaging.ProcessPaymentResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.ProcessPaymentResultStatus

### ProcessPaymentResultStatus Enum

Represents the status of a payment processing result.

Enum Values

The following are the values of the `RichMessaging.ProcessPaymentResultStatus` enum.

**Value** **Description**

`PROCESSOR_ERROR` Indicates an error occurred during payment processing at the processor level.

`SUCCESS` Indicates a successful payment processing result.

### RecurringTiming Class

Represents a payment that occurs on a regular basis.

Namespace

RichMessaging


Apex Reference Guide RecurringTiming Class

IN THIS SECTION:

#### RecurringTiming Constructors

RecurringTiming Properties

#### RecurringTiming Constructors The following are constructors for RecurringTiming .

IN THIS SECTION:

##### RecurringTiming(startDate, endDate, intervalCount, intervalUnit)

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### RecurringTiming()

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### **`RecurringTiming(startDate, endDate, intervalCount, intervalUnit)`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.

Signature

```
   public RecurringTiming(Date startDate, Date endDate, Integer intervalCount,

   RichMessaging.TimingIntervalUnit intervalUnit)

```

Parameters

```
   startDate
```

Type: Date

The start date. Invocable variable.

```
   endDate
```

Type: Date

The end date. Invocable variable.

```
   intervalCount
```

Type: Integer

The number of interval units that make up the total payment interval. Invocable variable.

```
   intervalUnit
```

Type: RichMessaging.TimingIntervalUnit

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

##### **`RecurringTiming()`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.


Apex Reference Guide RecurringTiming Class

Signature

```
   public RecurringTiming()

#### RecurringTiming Properties The following are properties for RecurringTiming .

```

IN THIS SECTION:

##### endDate

The end date. Invocable variable.

##### endDateValue

The end date. Enabled for Lightning components.

intervalCount
The number of interval units that make up the total payment interval. Invocable variable.

intervalCountValue
The number of interval units that make up the total payment interval. Enabled for Lightning components.

intervalUnit
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

intervalUnitValue
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.

startDate
The start date. Invocable variable.

startDateValue
The start date. Enabled for Lightning components.

timingType
Always returns “RecurringTiming”.

##### **`endDate`**

The end date. Invocable variable.

Signature

```
   public Date endDate {get; set;}

```

Property Value

Type: Date

##### **`endDateValue`**

The end date. Enabled for Lightning components.


Apex Reference Guide RecurringTiming Class

Signature

```
   public Date endDateValue {get; set;}

```

Property Value

Type: Date

##### **`intervalCount`**

The number of interval units that make up the total payment interval. Invocable variable.

Signature

```
   public Integer intervalCount {get; set;}

```

Property Value

Type: Integer

##### **`intervalCountValue`**

The number of interval units that make up the total payment interval. Enabled for Lightning components.

Signature

```
   public Integer intervalCountValue {get; set;}

```

Property Value

Type: Integer

##### **`intervalUnit`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Invocable
variable.

Signature

```
   public String intervalUnit {get; set;}

```

Property Value

Type: String

##### **`intervalUnitValue`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.


### Apex Reference Guide ShippingMethod Class

Signature

```
   public RichMessaging.TimingIntervalUnit intervalUnitValue {get; set;}

```

Property Value

Type: RichMessaging.TimingIntervalUnit

##### **`startDate`**

The start date. Invocable variable.

Signature

```
   public Date startDate {get; set;}

```

Property Value

Type: Date

##### **`startDateValue`**

The start date. Enabled for Lightning components.

Signature

```
   public Date startDateValue {get; set;}

```

Property Value

Type: Date

##### **`timingType`**

Always returns “RecurringTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### ShippingMethod Class

Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging


Apex Reference Guide ShippingMethod Class

Example

```
   public with sharing class MessagingShippingMethods {

      @InvocableMethod

      public static List<List<RichMessaging.ShippingMethod>> getShippingMethods(){

        Double amount = 0.25;

        List<List<RichMessaging.ShippingMethod>> result = new

   List<List<RichMessaging.ShippingMethod>>();

       List<RichMessaging.ShippingMethod> options = new List<RichMessaging.ShippingMethod>{

          new RichMessaging.ShippingMethod('doordash', amount, '1 hour delivery to your

    door', 'ddash'),

           new RichMessaging.ShippingMethod('UPS', amount, '2 days delivery', 'UPS')

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### ShippingMethod Constructors

ShippingMethod Properties

#### ShippingMethod Constructors The following are constructors for ShippingMethod .

IN THIS SECTION:

##### ShippingMethod(label, amount, detail, identifier)

Creates a new instance of the `RichMessaging.ShippingMethod` class.

ShippingMethod()
Creates a new instance of the `RichMessaging.ShippingMethod` class.

##### **`ShippingMethod(label, amount, detail, identifier)`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod(String label, Double amount, String detail, String identifier)

```

Parameters

```
   label
```

Type: String


Apex Reference Guide ShippingMethod Class

The label of the shipping method.

```
   amount
```

Type: Double

The amount of the shipping method.

```
   detail
```

Type: String

Details about the shipping method.

```
   identifier
```

Type: String

The identifier of the shipping method.

##### **`ShippingMethod()`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod()

#### ShippingMethod Properties

##### The following are properties for ShippingMethod .

```

IN THIS SECTION:

amount
The amount of the shipping method.

amountValue
The amount value of the shipping method.

detail
Details about the shipping method.

detailValue
The detail value of the shipping method.

identifier
The identifier of the shipping method.

identifierValue
The identifier value of the shipping method.

label
The label of the shipping method.

labelValue
The label value of the shipping method.

shippingMethodType
The shipping method type. Read only.


Apex Reference Guide ShippingMethod Class

##### **`amount`**

The amount of the shipping method.

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the shipping method.

Signature

```
   public Double amountValue {get; set;}

```

Property Value

Type: Double

##### **`detail`**

Details about the shipping method.

Signature

```
   public String detail {get; set;}

```

Property Value

Type: String

##### **`detailValue`**

The detail value of the shipping method.

Signature

```
   public String detailValue {get; set;}

```

Property Value

Type: String

##### **`identifier`**

The identifier of the shipping method.


Apex Reference Guide ShippingMethod Class

Signature

```
   public String identifier {get; set;}

```

Property Value

Type: String

##### **`identifierValue`**

The identifier value of the shipping method.

Signature

```
   public String identifierValue {get; set;}

```

Property Value

Type: String

##### **`label`**

The label of the shipping method.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the shipping method.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String

##### **`shippingMethodType`**

The shipping method type. Read only.

Signature

```
   public String shippingMethodType {get; set;}

```


### Apex Reference Guide TimeSlotOption Class

Property Value

Type: String

### TimeSlotOption Class

Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### TimeSlotOption Constructors

TimeSlotOption Properties

#### TimeSlotOption Constructors

### The following are constructors for TimeSlotOption .

IN THIS SECTION:

##### TimeSlotOption(startTime, endTime)
### Creates a TimeSlotOption object with a start and end time.

TimeSlotOption(startTime, duration)
### Creates a TimeSlotOption object with a start time and a duration.

TimeSlotOption()
### Creates a TimeSlotOption object.

##### **`TimeSlotOption(startTime, endTime)`**

### Creates a TimeSlotOption object with a start and end time.

Signature

```
   public TimeSlotOption(Datetime startTime, Datetime endTime)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

```
   endTime
```

Type: Datetime

End time.


Apex Reference Guide TimeSlotOption Class

##### **`TimeSlotOption(startTime, duration)`** Creates a TimeSlotOption object with a start time and a duration.

Signature

```
   public TimeSlotOption(Datetime startTime, Integer duration)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

##### _`duration`_

Type: Integer

Duration in seconds.

##### **`TimeSlotOption()`** Creates a TimeSlotOption object.

Signature

```
   public TimeSlotOption()

#### TimeSlotOption Properties

##### The following are properties for TimeSlotOption .

```

IN THIS SECTION:

##### duration

The duration in seconds.

##### durationValue

The duration in seconds. Enabled for Lightning components.

endTimeValue
The end time. Enabled for Lightning components.

startTime
The start time.

startTimeValue
The start time. Enabled for Lightning components.

##### **`duration`**

The duration in seconds.


Apex Reference Guide TimeSlotOption Class

Signature

```
   public Integer duration {get; set;}

```

Property Value

Type: Integer

##### **`durationValue`**

The duration in seconds. Enabled for Lightning components.

Signature

```
   public Integer durationValue {get; set;}

```

Property Value

Type: Integer

##### **`endTimeValue`**

The end time. Enabled for Lightning components.

Signature

```
   public Datetime endTimeValue {get; set;}

```

Property Value

Type: Datetime

##### **`startTime`**

The start time.

Signature

```
   public Datetime startTime {get; set;}

```

Property Value

Type: Datetime

##### **`startTimeValue`**

The start time. Enabled for Lightning components.

Signature

```
   public Datetime startTimeValue {get; set;}

```


### Apex Reference Guide TimingIntervalUnit Enum

Property Value

Type: Datetime

### TimingIntervalUnit Enum

Represents an enumerated type that describes the timing interval.

Enum Values

The following are the values of the `RichMessaging.TimingIntervalUnit` enum.

**Value** **Description**

`Day` Day interval.

`Hour` Hour interval.

`Minute` Minute interval.

`Month` Month interval.

`Year` Year interval.

### TimingType Enum

Represents an enumerated type that describes the type of timing.

Enum Values

The following are the values of the `RichMessaging.TimingType` enum.

**Value** **Description**

`DeferredTiming` Indicates that the timing is deferred. See DeferredTiming Class.

`RecurringTiming` Indicates that the timing recurs. See RecurringTiming Class.

## RulesAppln Namespace

The RulesAppln namespace contains output classes that store details about a rules-based application of payments and credits.

[The rules are applied by using the applyPaymentsAndCreditsByRules invocable action. See Apply Payments and Credits by Rules Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_apply_rules.htm)
in the _Revenue Cloud Developer Guide_ .

## The RulesAppln namespace includes these classes.

**•** [RulesApplicationResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationResponse.htm)

**•** [RulesApplicationSummaryResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationSummaryResponse.htm)

**•** [RulesApplicationErrorResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationErrorResponse.htm)


## Apex Reference Guide Schema Namespace Schema Namespace The Schema namespace provides classes and methods for schema metadata information. The following are the classes in the Schema namespace.

IN THIS SECTION:

ChildRelationship Class
Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

DataCategory Class
Represents the categories within a category group.

DataCategoryGroupSobjectTypePair Class
Specifies a category group and an associated object.

DescribeColorResult Class
Contains color metadata information for a tab.

DescribeDataCategoryGroupResult Class
Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

DescribeDataCategoryGroupStructureResult Class
Contains the category groups and categories associated with KnowledgeArticleVersion and Question.

DescribeFieldResult Class
Contains methods for describing sObject fields.

DescribeIconResult Class
Contains icon metadata information for a tab.

DescribeSObjectResult Class
Contains methods for describing SObjects. None of the methods take an argument.

DescribeTabResult Class
Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.

DescribeTabSetResult Class
Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.

DisplayType Enum
A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

FieldDescribeOptions Enum
A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

FieldSet Class
Contains methods for discovering and retrieving the details of field sets created on sObjects.

FieldSetMember Class
Contains methods for accessing the metadata for field set member fields.

PicklistEntry Class
Represents a picklist entry.

RecordTypeInfo Class
Contains methods for accessing record type information for an sObject with associated record types.


### Apex Reference Guide ChildRelationship Class

SOAPType Enum
A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

SObjectDescribeOptions Enum
A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

SObjectField Class
A `Schema.sObjectField` object is returned from the field describe result using the `getController` and
`getSObjectField` methods.

SObjectType Class
A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from
the sObject describe result using the `getSObjectType` method.

### ChildRelationship Class

Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

Namespace

Schema

Example

A ChildRelationship object is returned from the sObject describe result using the `getChildRelationship` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.ChildRelationship> C = R.getChildRelationships();

#### ChildRelationship Methods

### The following are methods for ChildRelationship . All are instance methods.

```

IN THIS SECTION:

getChildSObject()
Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

getField()
Returns the token of the field that has a foreign key back to the parent sObject.

getRelationshipName()
Returns the name of the relationship.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.


Apex Reference Guide ChildRelationship Class

##### getChildSObject()

Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectType getChildSObject()

```

Return Value

Type: Schema.SObjectType

##### getField()

Returns the token of the field that has a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectField getField()

```

Return Value

Type: Schema.SObjectField

##### getRelationshipName()

Returns the name of the relationship.

Signature

```
   public String getRelationshipName()

```

Return Value

Type: String

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.


### Apex Reference Guide DataCategory Class

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

### DataCategory Class

Represents the categories within a category group.

Namespace

Schema

Usage

The `Schema.DataCategory` object is returned by the `getTopCategories` method.

#### DataCategory Methods

### The following are methods for DataCategory . All are instance methods.

IN THIS SECTION:

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.

getLabel()
Returns the label for the data category used in the Salesforce user interface.

getName()
Returns the unique name used by the API to access to the data category.

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.


### Apex Reference Guide DataCategoryGroupSobjectTypePair Class

Signature

```
   public Schema.DataCategory getChildCategories()

```

Return Value

Type: List<Schema.DataCategory>

##### getLabel()

Returns the label for the data category used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category.

Signature

```
   public String getName()

```

Return Value

Type: String

### DataCategoryGroupSobjectTypePair Class

Specifies a category group and an associated object.

Namespace

Schema

Usage

Schema.DataCategoryGroupSobjectTypePair is used by the `describeDataCategory GroupStructures` method to return
the categories available to this object.

IN THIS SECTION:

DataCategoryGroupSobjectTypePair Constructors

DataCategoryGroupSobjectTypePair Methods


Apex Reference Guide DataCategoryGroupSobjectTypePair Class

#### DataCategoryGroupSobjectTypePair Constructors The following are constructors for DataCategoryGroupSobjectTypePair .

IN THIS SECTION:

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

Signature

```
   public DataCategoryGroupSobjectTypePair()

#### DataCategoryGroupSobjectTypePair Methods The following are methods for DataCategoryGroupSobjectTypePair . All are instance methods.

```

IN THIS SECTION:

##### getDataCategoryGroupName()

Returns the unique name used by the API to access the data category group.

##### getSobject()

Returns the object name associated with the data category group.

setDataCategoryGroupName(name)
Specifies the unique name used by the API to access the data category group.

setSobject(sObjectName)
Sets the sObject associated with the data category group.

##### getDataCategoryGroupName()

Returns the unique name used by the API to access the data category group.

Signature

```
   public String getDataCategoryGroupName()

```

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.


### Apex Reference Guide DescribeColorResult Class

Signature

```
   public String getSobject()

```

Return Value

Type: String

##### setDataCategoryGroupName(name)

Specifies the unique name used by the API to access the data category group.

Signature

```
   public String setDataCategoryGroupName(String name)

```

Parameters

**name**
Type: String

Return Value

Type: Void

##### setSobject(sObjectName)

Sets the sObject associated with the data category group.

Signature

```
   public Void setSobject(String sObjectName)

```

Parameters

```
   sObjectName
```

Type: String

The _`sObjectName`_ is the object name associated with the data category group. Valid values are:

**•** `KnowledgeArticleVersion` —for article types.

**•** `Question` —for questions from Answers.

Return Value

Type: Void

### DescribeColorResult Class

Contains color metadata information for a tab.


Apex Reference Guide DescribeColorResult Class

Namespace

Schema

Usage

The `getColors` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeColorResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeColorResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`colorResultObj.color` is equivalent to `colorResultObj.getColor()` .

Example

This sample shows how to get the color information in the Sales app for the first tab’s first color.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.DescribeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Display tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get color information for the first tab

        List<Schema.DescribeColorResult> colorDesc = tsr.getTabs()[0].getColors();

        // Display the icon color, theme, and context of the first color returned

        System.debug('Color: ' + colorDesc[0].getColor());

        System.debug('Theme: ' + colorDesc[0].getTheme());

        System.debug('Context: ' + colorDesc[0].getContext());

      }

   }

   // Example debug statement output

   // DEBUG|Color: 1797C0

   // DEBUG|Theme: theme4

   // DEBUG|Context: primary

#### DescribeColorResult Methods The following are methods for DescribeColorResult . All are instance methods.

```

IN THIS SECTION:

getColor()
Returns the Web RGB color code, such as `00FF00` .

getContext()
Returns the color context. The context determines whether the color is the main color for the tab or not.

getTheme()
Returns the color theme.


Apex Reference Guide DescribeDataCategoryGroupResult Class

##### getColor()

Returns the Web RGB color code, such as `00FF00` .

Signature

```
   public String getColor()

```

Return Value

Type: String

##### getContext()

Returns the color context. The context determines whether the color is the main color for the tab or not.

Signature

```
   public String getContext()

```

Return Value

Type: String

##### getTheme()

Returns the color theme.

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

DescribeDataCategoryGroupResult Class

Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

Namespace

Schema


Apex Reference Guide DescribeDataCategoryGroupResult Class

Usage

The `describeDataCategoryGroups` method returns a `Schema.DescribeDataCategoryGroupResult` object
containing the list of the category groups associated with the specified object.

For additional information and code examples using `describeDataCategoryGroups` [, see Accessing All Data Categories](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)
[Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group describe result object:

```
   List <String> objType = new List<String>();

   objType.add('KnowledgeArticleVersion');

   objType.add('Question');

   List<Schema.DescribeDataCategoryGroupResult> describeCategoryResult =

     Schema.describeDataCategoryGroups(objType);

#### DescribeDataCategoryGroupResult Methods The following are methods for DescribeDataCategoryGroupResult . All are instance methods.

```

IN THIS SECTION:

##### getCategoryCount()

Returns the number of visible data categories in the data category group.

getDescription()
Returns the description of the data category group.

getLabel()
Returns the label for the data category group used in the Salesforce user interface.

getName()
Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the object name associated with the data category group.

##### getCategoryCount()

Returns the number of visible data categories in the data category group.

Signature

```
   public Integer getCategoryCount()

```

Return Value

Type: Integer


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

DescribeDataCategoryGroupStructureResult Class

Contains the category groups and categories associated with KnowledgeArticleVersion and Question.


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

Namespace

Schema

Usage

The `describeDataCategoryGroupStructures` method returns a list of `Schema.Describe`
`DataCategoryGroupStructureResult` objects containing the category groups and categories associated with the specified
object.

[For additional information and code examples, see Accessing All Data Categories Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group structure describe result object:

```
   List <DataCategoryGroupSobjectTypePair> pairs =

       new List<DataCategoryGroupSobjectTypePair>();

   DataCategoryGroupSobjectTypePair pair1 =

       new DataCategoryGroupSobjectTypePair();

   pair1.setSobject('KnowledgeArticleVersion');

   pair1.setDataCategoryGroupName('Regions');

   DataCategoryGroupSobjectTypePair pair2 =

       new DataCategoryGroupSobjectTypePair();

   pair2.setSobject('Questions');

   pair2.setDataCategoryGroupName('Regions');

   pairs.add(pair1);

   pairs.add(pair2);

   List<Schema.DescribeDataCategoryGroupStructureResult>results =

       Schema.describeDataCategoryGroupStructures(pairs, true);

#### DescribeDataCategoryGroupStructureResult Methods The following are methods for DescribeDataCategoryGroupStructureResult . All are instance methods.

```

IN THIS SECTION:

getDescription()
Returns the description of the data category group.

getLabel()
Returns the label for the data category group used in the Salesforce user interface.

getName()
Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the name of object associated with the data category group.


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

getTopCategories()
Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getSobject()

Returns the name of object associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String


### Apex Reference Guide DescribeFieldResult Class

##### getTopCategories()

Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

Signature

```
   public List<Schema.DataCategory> getTopCategories()

```

Return Value

Type: List<Schema.DataCategory>

Usage

For more information on data category group visibility, see “Data Category Visibility” in the Salesforce online help.

### DescribeFieldResult Class

Contains methods for describing sObject fields.

Namespace

Schema

Usage

### Instances of field describe results on the same DescribeFieldResult aren’t guaranteed to be equal because the state and

behavior of a describe object is determined by various factors including the API version used. To compare describe results, call the
`getSObjectField()` method on the field describe results and use the equality operator ( `==` ) to compare the `SObjectField`
values.

Example

The following is an example of how to instantiate a field describe result object:

```
   Schema.DescribeFieldResult dfr = Account.Description.getDescribe();

#### DescribeFieldResult Methods

### The following are methods for DescribeFieldResult . All are instance methods.

```

IN THIS SECTION:

getByteLength()
For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

getCalculatedFormula()
Returns the formula specified for this field.


Apex Reference Guide DescribeFieldResult Class

getController()
Returns the token of the controlling field.

getDefaultValue()
Returns the default value for this field.

getDefaultValueFormula()
Returns the default formula value that is specified for this formula field.

getDigits()
Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

getInlineHelpText()
Returns the content of the field-level help.

getLabel()
Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

getLength()
Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

getLocalName()
Returns the name of the field, similar to the `getName` method. However, if the field is part of the current namespace, the namespace
portion of the name is omitted.

getName()
Returns the field name used in Apex.

getPicklistValues()
Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

getPrecision()
For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the
right of the decimal point (but excluding the decimal point character).

getReferenceTargetField()
Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the
child external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

getReferenceTo()
Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

getRelationshipName()
Returns the name of the child-to-parent relationship.

getRelationshipOrder()
Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

getScale()
For fields of type Double, returns the number of digits to the right of the decimal point.

getSOAPType()
Returns one of the SoapType enum values, depending on the type of field.

getSObjectField()
Returns the token for this field.


Apex Reference Guide DescribeFieldResult Class

getSObjectType()
Returns the Salesforce object type from which this field originates.

getType()
Returns one of the DisplayType enum values, depending on the type of field.

isAccessible()
Returns `true` if the current user can see this field, `false` otherwise.

isAiPredictionField() (Beta)
Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

isAutoNumber()
Returns `true` if the field is an Auto Number field, `false` otherwise.

isCalculated()
Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isCaseSensitive()
Returns `true` if the field is case sensitive, `false` otherwise.

isCreateable()
Returns `true` if the field can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

isDefaultedOnCreate()
Returns `true` if the field receives a default value when created, `false` otherwise.

isDependentPicklist()
Returns `true` if the picklist is a dependent picklist, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isEncrypted()
Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

isExternalID()
Returns `true` if the field is used as an external ID, `false` otherwise.

isFilterable()
Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

isFormulaTreatNullNumberAsZero()
Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

isGroupable()
Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only
available for Apex classes and triggers saved using API version 18.0 and higher.

isHtmlFormatted()
Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has
an `IMAGE` text function.


Apex Reference Guide DescribeFieldResult Class

isIdLookup()
Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

isNameField()
Returns `true` if the field is a name field, `false` otherwise.

isNamePointing()
Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead`
`ID` ( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of
those objects can be the parent of a particular task record. This method returns `false` otherwise.

isNillable()
Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a
value for the object to be created or saved.

isPermissionable()
Returns `true` if field permissions can be specified for the field, `false` otherwise.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

isRestrictedPicklist()
Returns `true` if the field is a restricted picklist, `false` otherwise

isSearchPrefilterable()
Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

isSortable()
Returns `true` if a query can sort on the field, `false` otherwise

isUnique()
Returns `true` if the value for the field must be unique, `false` otherwise

isUpdateable()
Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object
can be reparented to different parent records; `false` otherwise.

isWriteRequiresMasterRead()
Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

##### getByteLength()

For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

Signature

```
   public Integer getByteLength()

```

Return Value

Type: Integer

##### getCalculatedFormula()

Returns the formula specified for this field.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public String getCalculatedFormula()

```

Return Value

Type: String

##### getController()

Returns the token of the controlling field.

Signature

```
   public Schema.sObjectField getController()

```

Return Value

Type: Schema.SObjectField

##### getDefaultValue()

Returns the default value for this field.

Signature

```
   public Object getDefaultValue()

```

Return Value

Type: Object

##### getDefaultValueFormula()

Returns the default formula value that is specified for this formula field.

Signature

```
   public String getDefaultValueFormula()

```

Return Value

Type: String

##### getDigits()

Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

Signature

```
   public Integer getDigits()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Integer

##### getInlineHelpText()

Returns the content of the field-level help.

Signature

```
   public String getInlineHelpText()

```

Return Value

Type: String

Usage

For more information, see “Define Field-Level Help” in the Salesforce online help.

##### getLabel()

Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

##### Note: For the Type field on standard objects, getLabel returns a label different from the default label. It returns a label of the form Object Type, where Object is the standard object label. For example, for the Type field on Account, getLabel returns Account Type instead of the default label Type . If the Type label is renamed, getLabel returns the new label. You can

check or change the labels of all standard object fields from Setup by entering _`Rename Tabs and Labels`_ in the `Quick`
`Find box`, then selecting **Rename Tabs and Labels** .

##### getLength()

Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

Signature

```
   public Integer getLength()

```

Return Value

Type: Integer


Apex Reference Guide DescribeFieldResult Class

##### getLocalName() Returns the name of the field, similar to the getName method. However, if the field is part of the current namespace, the namespace

portion of the name is omitted.

Signature

```
   public String getLocalName()

```

Return Value

Type: String

##### getName()

Returns the field name used in Apex.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getPicklistValues()

Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

Signature

```
   public List<Schema.PicklistEntry> getPicklistValues()

```

Return Value

Type: List<Schema.PicklistEntry>

##### getPrecision()

For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the right
of the decimal point (but excluding the decimal point character).

Signature

```
   public Integer getPrecision()

```

Return Value

Type: Integer


Apex Reference Guide DescribeFieldResult Class

##### getReferenceTargetField()

Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the child
external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

Signature

```
   public String getReferenceTargetField()

```

Return Value

Type: String

Usage

For information about indirect lookup relationships, see “Indirect Lookup Relationship Fields on External Objects” in the Salesforce Help.

##### getReferenceTo()

Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

Signature

```
   public List <Schema.sObjectType> getReferenceTo()

```

Return Value

Type: List<Schema.sObjectType>

Versioned Behavior Changes

##### In API version 51.0 and later, the getReferenceTo() method returns referenced objects that aren’t accessible to the context user.

If the context user has access to an object’s field that references another object, irrespective of the context user’s access to the
cross-referenced object, the method returns references. In API version 50.0 and earlier, if the context user doesn’t have access to the
cross-referenced object, the method returns an empty list.

##### getRelationshipName()

Returns the name of the child-to-parent relationship.

Signature

```
   public String getRelationshipName()

```

Return Value

Type: String


Apex Reference Guide DescribeFieldResult Class

Usage

[For more information about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getRelationshipOrder()

Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

Signature

```
   public Integer getRelationshipOrder()

```

Return Value

Type: Integer

Usage

[For more information about primary and secondary relationships, see Considerations for Object Relationships. For more information](https://help.salesforce.com/s/articleView?id=sf.relationships_considerations.htm&language=en_US)
[about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getScale()

For fields of type Double, returns the number of digits to the right of the decimal point.

Signature

```
   public Integer getScale()

```

Return Value

Type: Integer

##### getSOAPType()

Returns one of the SoapType enum values, depending on the type of field.

Signature

```
   public Schema.SOAPType getSOAPType()

```

Return Value

Type: Schema.SOAPType

##### getSObjectField()

Returns the token for this field.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Schema.sObjectField getSObjectField()

```

Return Value

Type: Schema.SObjectField

##### **`getSObjectType()`**

Returns the Salesforce object type from which this field originates.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Example

```
   Schema.DescribeFieldResult f = Account.Industry.getDescribe();

   Schema.sObjectType sourceType = f.getSObjectType();

   Assert.areEqual(Account.sObjectType, sourceType);

##### getType()

```

Returns one of the DisplayType enum values, depending on the type of field.

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: Schema.DisplayType

##### isAccessible()

Returns `true` if the current user can see this field, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeFieldResult Class

##### isAiPredictionField() (Beta)

Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

Signature

```
   public Boolean isAiPredictionField()

```

Return Value

Type: Boolean

Usage

Custom number fields can be set to display Einstein prediction values. If you are participating in the Einstein Prediction Builder Beta
program, use Einstein Prediction Builder to set up the value to display. Use this method to find out if a field is enabled to display an
Einstein prediction value.

##### isAutoNumber()

Returns `true` if the field is an Auto Number field, `false` otherwise.

Signature

```
   public Boolean isAutoNumber()

```

Return Value

Type: Boolean

Usage

Analogous to a SQL IDENTITY type, Auto Number fields are read-only, non-createable text fields with a maximum length of 30 characters.
Auto Number fields are used to provide a unique ID that is independent of the internal object ID (such as a purchase order number or
invoice number). Auto Number fields are configured entirely in the Salesforce user interface.

##### isCalculated()

Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

Signature

```
   public Boolean isCalculated()

```

Return Value

Type: Boolean

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isCaseSensitive()

Returns `true` if the field is case sensitive, `false` otherwise.

Signature

```
   public Boolean isCaseSensitive()

```

Return Value

Type: Boolean

##### isCreateable()

Returns `true` if the field can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isDefaultedOnCreate()

Returns `true` if the field receives a default value when created, `false` otherwise.

Signature

```
   public Boolean isDefaultedOnCreate()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

Usage

If this method returns `true`, Salesforce implicitly assigns a value for this field when the object is created, even if a value for this field is
not passed in on the create call. For example, in the Opportunity object, the Probability field has this attribute because its value is derived
from the Stage field. Similarly, the Owner has this attribute on most objects because its value is derived from the current user (if the
Owner field is not specified).

##### isDependentPicklist()

Returns `true` if the picklist is a dependent picklist, `false` otherwise.

Signature

```
   public Boolean isDependentPicklist()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isEncrypted()

Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

Signature

```
   public Boolean isEncrypted()

```

Return Value

Type: Boolean

##### isExternalID()

Returns `true` if the field is used as an external ID, `false` otherwise.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Boolean isExternalID()

```

Return Value

Type: Boolean

##### isFilterable()

Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

Signature

```
   public Boolean isFilterable()

```

Return Value

Type: Boolean

##### isFormulaTreatNullNumberAsZero()

Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

Signature

```
   public Boolean isFormulaTreatNullNumberAsZero()

```

Return Value

Type: Boolean

##### isGroupable()

Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only available
for Apex classes and triggers saved using API version 18.0 and higher.

Signature

```
   public Boolean isGroupable()

```

Return Value

Type: Boolean

##### isHtmlFormatted()

Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has an
`IMAGE` text function.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Boolean isHtmlFormatted()

```

Return Value

Type: Boolean

##### isIdLookup()

Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

Signature

```
   public Boolean isIdLookup()

```

Return Value

Type: Boolean

##### isNameField()

Returns `true` if the field is a name field, `false` otherwise.

Signature

```
   public Boolean isNameField()

```

Return Value

Type: Boolean

Usage

This method is used to identify the name field for standard objects (such as `AccountName` for an Account object) and custom objects.
Objects can only have one name field, except where the `FirstName` and `LastName` fields are used instead (such as on the Contact
object).

##### If a compound name is present, for example, the Name field on a person account, isNameField is set to true for that record. isNamePointing()

Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead ID`
( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of those objects
can be the parent of a particular task record. This method returns `false` otherwise.

Signature

```
   public Boolean isNamePointing()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isNillable()

Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a value
for the object to be created or saved.

Signature

```
   public Boolean isNillable()

```

Return Value

Type: Boolean

##### isPermissionable()

Returns `true` if field permissions can be specified for the field, `false` otherwise.

Signature

```
   public Boolean isPermissionable()

```

Return Value

Type: Boolean

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

##### isRestrictedPicklist()

Returns `true` if the field is a restricted picklist, `false` otherwise

Signature

```
   public Boolean isRestrictedPicklist()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isSearchPrefilterable()

Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

Signature

```
   public Boolean isSearchPrefilterable()

```

Return Value

Type: Boolean

Usage

_Prefiltering_ means to filter by a specific field value before executing the full search query. Prefiltering is supported only in `WHERE` clauses
with the equals ( `=` ) operator.

##### isSortable()

Returns `true` if a query can sort on the field, `false` otherwise

Signature

```
   public Boolean isSortable()

```

Return Value

Type: Boolean

##### isUnique()

Returns `true` if the value for the field must be unique, `false` otherwise

Signature

```
   public Boolean isUnique()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object can
be reparented to different parent records; `false` otherwise.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


### Apex Reference Guide DescribeIconResult Class

Signature

```
   public Boolean isUpdateable()

```

Return Value

Type: Boolean

##### isWriteRequiresMasterRead()

Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

Signature

```
   public Boolean isWriteRequiresMasterRead()

```

Return Value

Type: Boolean

### DescribeIconResult Class

Contains icon metadata information for a tab.

Namespace

Schema

Usage

The `getIcons` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeIconResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeIconResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`iconResultObj.url` is equivalent to `iconResultObj.getUrl()` .

Example

This sample shows how to get the icon information in the Sales app for the first tab’s first icon.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get icon information for the first tab

        List<Schema.DescribeIconResult> iconDesc = tsr.getTabs()[0].getIcons();

        // Display the icon height and width of the first icon

        System.debug('Height: ' + iconDesc[0].getHeight());

```


Apex Reference Guide DescribeIconResult Class

```
        System.debug('Width: ' + iconDesc[0].getWidth());

      }

   }

   // Example debug statement output

   // DEBUG|Height: 32

   // DEBUG|Width: 32

#### DescribeIconResult Methods The following are methods for DescribeIconResult . All are instance methods.

```

IN THIS SECTION:

##### getContentType()

Returns the tab icon’s content type, such as `image/png` .

##### getHeight()

Returns the tab icon’s height in pixels.

getTheme()
Returns the tab’s icon theme.

getUrl()
Returns the tab’s icon fully qualified URL.

getWidth()
Returns the tab’s icon width in pixels.

##### getContentType()

Returns the tab icon’s content type, such as `image/png` .

Signature

```
   public String getContentType()

```

Return Value

Type: String

##### getHeight()

Returns the tab icon’s height in pixels.

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer


Apex Reference Guide DescribeIconResult Class

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its height is zero.

##### getTheme()

Returns the tab’s icon theme.

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

##### getUrl()

Returns the tab’s icon fully qualified URL.

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### getWidth()

Returns the tab’s icon width in pixels.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its width is zero.


### Apex Reference Guide DescribeSObjectResult Class DescribeSObjectResult Class

Contains methods for describing SObjects. None of the methods take an argument.

Namespace

Schema

Usage

### Instances of describe results on the same DescribeSObjectResult aren’t guaranteed to be equal because the state and behavior

of a describe object is determined by various factors including the API version used. To compare describe results, call the
`getSObjectType()` method on the SObject describe results and use the equality operator ( `==` ) to compare the `SObjectType`
values.

#### DescribeSObjectResult Properties

### The following are properties for DescribeSObjectResult .

##### **`accessible`**

Indicates whether the current user has access to the SObject.

Signature

```
   public Boolean accessible {get; set;}

```

Property Value

Type: Boolean

##### **`associateentitytype`**

The type of associated object. For example, `History` or `Share` .

Signature

```
   public String associateentitytype {get; set;}

```

Property Value

Type: String

##### **`associateparententity`**

The parent object of an associated object.

Signature

```
   public String associateparententity {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: String

##### **`childrelationships`**

A list of child relationships, which is the name of the sObject that has a foreign key to the sObject being described.

Signature

```
   public List<Schema.ChildRelationship> childrelationships {get; set;}

```

Property Value

Type: List<Schema.ChildRelationship on page 3352>

##### **`createable`**

Indicates whether the SObject can be created by the current user.

Signature

```
   public Boolean createable {get; set;}

```

Property Value

Type: Boolean

##### **`custom`**

Indicates whether the SObject is a custom object.

Signature

```
   public Boolean custom {get; set;}

```

Property Value

Type: Boolean

##### **`customsetting`**

Indicates whether the SObject is a custom setting.

Signature

```
   public Boolean customsetting {get; set;}

```

Property Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### **`datatranslationenabled`**

Indicates whether data translation is enabled for the SObject. This property is available in API version 49.0 and later.

Signature

```
   public Boolean datatranslationenabled {get; set;}

```

Property Value

Type: Boolean

##### **`defaultimplementation`**

Reserved for future use.

Signature

```
   public String defaultimplementation {get; set;}

```

Property Value

Type: String

##### **`deletable`**

Indicates whether the SObject can be deleted by the current user.

Signature

```
   public Boolean deletable {get; set;}

```

Property Value

Type: Boolean

##### **`deprecatedandhidden`**

Reserved for future use.

Signature

```
   public Boolean deprecatedandhidden {get; set;}

```

Property Value

Type: Boolean

##### **`feedenabled`**

Indicates whether Chatter feeds are enabled for the SObject.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean feedenabled {get; set;}

```

Property Value

Type: Boolean

##### fields

A list of fields associated with the SObject.

Signature

```
   public Schema.SObjectTypeFields fields {get; set;}

```

Property Value

Type: Schema.SObjectTypeFields

##### Follow fields with the getMap method.

Example

##### This sample code shows how to use fields . To get a custom field, specify the custom field name.

```
   Schema.DescribeFieldResult dfr = Schema.SObjectType.Account.fields.Name;

##### fieldSets

```

Represents field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets fieldsets {get; set;}

```

Property Value

Type: Schema.SObjectTypeFieldSets

##### Follow fieldSets with a field set name or with the getMap method.

Example

##### This sample code shows how to use fieldSet .

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

```


Apex Reference Guide DescribeSObjectResult Class

##### **`hassubtypes`**

Reserved for future use.

Signature

```
   public Boolean hassubtypes {get; set;}

```

Property Value

Type: Boolean

##### **`implementedby`**

Reserved for future use.

Signature

```
   public String implementedby {get; set;}

```

Property Value

Type: String

##### **`implementsinterfaces`**

Reserved for future use.

Signature

```
   public String implementsinterfaces {get; set;}

```

Property Value

Type: String

##### **`isinterface`**

Reserved for future use.

Signature

```
   public Boolean isinterface {get; set;}

```

Property Value

Type: Boolean

##### **`keyprefix`**

The three-character prefix code in the SObject ID.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public String keyprefix {get; set;}

```

Property Value

Type: String

##### **`label`**

The SObject's label, which may or may not match the object name. For example, an organization representing a medical vertical might
rename Account to Patient. Tabs and fields can be renamed in the Salesforce user interface.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelplural`**

The SObject's plural label, which may or may not match the object name. For example, Accounts.

Signature

```
   public String labelplural {get; set;}

```

Property Value

Type: String

##### **`localname`**

The name of the SObject. If the object is part of the current namespace, the namespace portion of the name is omitted.

Signature

```
   public String localname {get; set;}

```

Property Value

Type: String

##### **`mergeable`**

Indicates whether the SObject can be merged with other objects of its type by the current user. This is set to `true` for leads, contacts,
and accounts.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean mergeable {get; set;}

```

Property Value

Type: Boolean

##### **`mruenabled`**

Indicates whether Most Recently Used (MRU) list functionality is enabled for the SObject.

Signature

```
   public Boolean mruenabled {get; set;}

```

Property Value

Type: Boolean

##### **`name`**

The name field of the SObject.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`queryable`**

Indicates whether the SObject can be queried by the current user.

Signature

```
   public Boolean queryable {get; set;}

```

Property Value

Type: Boolean

##### **`recordtypeinfos`**

A list of the record types supported by the SObject.

Signature

```
   public List<Schema.RecordTypeInfo> recordtypeinfos {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: List<Schema.RecordTypeInfo>

##### **`recordtypeinfosbydevelopername`**

A map that matches developer names to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbydevelopername {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyid`**

A map that matches record IDs to their associated record types.

Signature

```
   public Map<Id,Schema.RecordTypeInfo> recordtypeinfosbyid {get; set;}

```

Property Value

Type: Map<ID, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyname`**

A map that matches record labels to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbyname {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`searchable`**

Indicates whether the SObject can be searched by the current user.

Signature

```
   public Boolean searchable {get; set;}

```

Property Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### **`sobjectdescribeoption`**

The effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions sobjectdescribeoption {get; set;}

```

Property Value

Type: SObjectDescribeOptions Enum

##### **`sobjecttype`**

The Schema.SObjectType object for the SObject.

Signature

```
   public Schema.SObjectType sobjecttype {get; set;}

```

Property Value

Type: Schema.SObjectType

##### **`undeletable`**

Indicates whether the SObject can be undeleted by the current user.

Signature

```
   public Boolean undeletable {get; set;}

```

Property Value

Type: Boolean

##### **`updateable`**

Indicates whether the SObject can be updated by the current user.

Signature

```
   public Boolean updateable {get; set;}

```

Property Value

Type: Boolean

#### DescribeSObjectResult Methods The following are methods for DescribeSObjectResult . All are instance methods.


Apex Reference Guide DescribeSObjectResult Class

IN THIS SECTION:

equals(obj)
Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.

getAssociateEntityType()
Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
combination with the `getAssociateParentEntity()` method to get the parent object. For example, invoking the method
on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getAssociateParentEntity()
Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with
the `getAssociateEntityType()` method to get the type of associated object. For example, invoking the method on
AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getChildRelationships()
Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

getDataTranslationEnabled()
Returns true if data translation is enabled for the SObject. Otherwise, returns false.

getDefaultImplementation()
Reserved for future use.

getFields()
Returns the fields that make up the SObject being described.

getFieldSets()
Returns field sets, which is a grouping of the SObject fields.

getHasSubtypes()
Reserved for future use.

getImplementedBy()
Reserved for future use.

getImplementsInterfaces()
Reserved for future use.

getIsInterface()
Reserved for future use.

getKeyPrefix()
Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of
the object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

getLabel()
Returns the object's label, which may or may not match the object name.

getLabelPlural()
Returns the object's plural label, which may or may not match the object name.

getLocalName()
Returns the name of the object, similar to the `getName` method. However, if the object is part of the current namespace, the
namespace portion of the name is omitted.

getName()
Returns the name of the object.


Apex Reference Guide DescribeSObjectResult Class

getRecordTypeInfos()
Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it
in this list.

getRecordTypeInfosByDeveloperName()
Returns a map that matches developer names to their associated record type. The current user is not required to have access to a
record type to see it in this map.

getRecordTypeInfosById()
Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record
type to see it in this map.

getRecordTypeInfosByName()
Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record
type to see it in this map.

getSObjectDescribeOption()
Returns the effective describe option used by the system for the SObject.

getSobjectType()
Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

getHasSubtypes()
Reserved for future use.

hashCode()
Returns the hash code for the SObject.

isAccessible()
Returns `true` if the current user can see this object, `false` otherwise.

isCreateable()
Returns `true` if the object can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the object is a custom object, `false` if it is a standard object.

isCustomSetting()
Returns `true` if the object is a custom setting, `false` otherwise.

isDeletable()
Returns `true` if the object can be deleted by the current user, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isFeedEnabled()
Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and
triggers saved using SalesforceAPI version 19.0 and later.

isMergeable()
Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned
for leads, contacts, and accounts.

isMruEnabled()
Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.


Apex Reference Guide DescribeSObjectResult Class

isQueryable()
Returns `true` if the object can be queried by the current user, `false` otherwise

isSearchable()
Returns `true` if the object can be searched by the current user, `false` otherwise.

isUndeletable()
Returns `true` if the object can be undeleted by the current user, `false` otherwise.

isUpdateable()
Returns `true` if the object can be updated by the current user, `false` otherwise.

toString()
Returns a string that represents the SObject.

##### **`equals(obj)`**

Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.

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

##### **`getAssociateEntityType()`**

Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
combination with the `getAssociateParentEntity()` method to get the parent object. For example, invoking the method
on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String associateentitytype {get; set;}

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties


Apex Reference Guide DescribeSObjectResult Class

##### **`getAssociateParentEntity()`**

Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with the
`getAssociateEntityType()` method to get the type of associated object. For example, invoking the method on AccountHistory
returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String getAssociateParentEntity()

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties

##### getChildRelationships()

Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

Signature

```
   public Schema.ChildRelationship getChildRelationships()

```

Return Value

Type: List<Schema.ChildRelationship>

Example

For example, the Account object includes `Contacts` and `Opportunities` as child relationships.

##### **`getDataTranslationEnabled()`**

Returns true if data translation is enabled for the SObject. Otherwise, returns false.

Signature

```
   public Boolean getDataTranslationEnabled()

```

Return Value

Type: Boolean

##### getDefaultImplementation()

Reserved for future use.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public String getDefaultImplementation()

```

Return Value

Type: String

##### **`getFields()`**

Returns the fields that make up the SObject being described.

Signature

```
   public Schema.SObjectTypeFields getFields()

```

Return Value

Type: Schema.SObjectTypeFields

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFields.

Usage

When you describe SObjects and their fields from within an Apex class, custom fields of new field types are returned regardless of the
API version that the class is saved in. If a field type, such as the geolocation field type, is available only in a recent API version, components
of a geolocation field are returned even if the class is saved in an earlier API version.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### **`getFieldSets()`**

Returns field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets getFieldSets()

```

Return Value

Type: Schema.SObjectTypeFieldSets


Apex Reference Guide DescribeSObjectResult Class

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFieldSets.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### getHasSubtypes()

Reserved for future use.

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean

##### getImplementedBy()

Reserved for future use.

Signature

```
   public String getImplementedBy()

```

Return Value

Type: String

##### getImplementsInterfaces()

Reserved for future use.

Signature

```
   public String getImplementsInterfaces()

```

Return Value

Type: String

##### getIsInterface()

Reserved for future use.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean getIsInterface()

```

Return Value

Type: Boolean

##### getKeyPrefix()

Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of the
object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

Signature

```
   public String getKeyPrefix()

```

Return Value

Type: String

Usage

The DescribeSobjectResult object returns a value for objects that have a stable prefix. For object types that do not have a stable or
predictable prefix, this field is blank. Client applications that rely on these codes can use this way of determining object type to ensure
forward compatibility.

##### getLabel()

Returns the object's label, which may or may not match the object name.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The object's label might not always match the object name. For example, an organization in the medical industry might change the
label for Account to Patient. This label is then used in the Salesforce user interface. See the Salesforce online help for more information.

##### getLabelPlural()

Returns the object's plural label, which may or may not match the object name.

Signature

```
   public String getLabelPlural()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: String

Usage

The object's plural label might not always match the object name. For example, an organization in the medical industry might change
the plural label for Account to Patients. This label is then used in the Salesforce user interface. See the Salesforce online help for more
information.

##### getLocalName() Returns the name of the object, similar to the getName method. However, if the object is part of the current namespace, the namespace

portion of the name is omitted.

Signature

```
   public String getLocalName()

```

Return Value

Type: String

##### getName()

Returns the name of the object.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeInfos()

Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it in
this list.

Signature

```
   public List<Schema.RecordTypeInfo> getRecordTypeInfos()

```

Return Value

Type: List<Schema.RecordTypeInfo>


Apex Reference Guide DescribeSObjectResult Class

##### getRecordTypeInfosByDeveloperName()

Returns a map that matches developer names to their associated record type. The current user is not required to have access to a record
type to see it in this map.

Signature

```
   public Map<String, Schema.RecordTypeInfo> getRecordTypeInfosByDeveloperName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getRecordTypeInfosById()

Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosById()

```

Return Value

Type: Map<ID, Schema.RecordTypeInfo>

##### getRecordTypeInfosByName()

Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosByName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getSObjectDescribeOption()

Returns the effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions getSObjectDescribeOption()

```

Return Value

Type: Schema.SObjectDescribeOptions

Valid values are:


Apex Reference Guide DescribeSObjectResult Class

**•** `SObjectDescribeOptions.FULL` : Indicates eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation.

**•** `SObjectDescribeOptions.DEFERRED` : Indicates lazy-load child relationships. This means that all child relationships will
not be loaded at the time of first invocation of the method.

##### getSobjectType()

Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

Signature

```
   public Schema.SObjectType getSobjectType()

```

Return Value

Type: Schema.SObjectType

##### getHasSubtypes()

Reserved for future use.

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean

##### **`hashCode()`**

Returns the hash code for the SObject.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### isAccessible()

Returns `true` if the current user can see this object, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: Boolean

Versioned Behavior Changes

In API version 54.0 and later, for custom settings and custom metadata type objects,
`DescribeSObjectResult.isAccessible()` returns `false` if the user doesn’t have permissions to access the queried
objects. In API version 53.0 and earlier, the method returns `true` even if the user doesn't have the required permissions.

##### isCreateable()

Returns `true` if the object can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the object is a custom object, `false` if it is a standard object.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isCustomSetting()

Returns `true` if the object is a custom setting, `false` otherwise.

Signature

```
   public Boolean isCustomSetting()

```

Return Value

Type: Boolean

##### isDeletable()

Returns `true` if the object can be deleted by the current user, `false` otherwise.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean isDeletable()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isFeedEnabled()

Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and triggers
saved using SalesforceAPI version 19.0 and later.

Signature

```
   public Boolean isFeedEnabled()

```

Return Value

Type: Boolean

##### isMergeable()

Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned for
leads, contacts, and accounts.

Signature

```
   public Boolean isMergeable()

```

Return Value

Type: Boolean

##### isMruEnabled()

Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean isMruEnabled()

```

Return Value

Type: Boolean

##### isQueryable()

Returns `true` if the object can be queried by the current user, `false` otherwise

Signature

```
   public Boolean isQueryable()

```

Return Value

Type: Boolean

##### isSearchable()

Returns `true` if the object can be searched by the current user, `false` otherwise.

Signature

```
   public Boolean isSearchable()

```

Return Value

Type: Boolean

##### isUndeletable()

Returns `true` if the object can be undeleted by the current user, `false` otherwise.

Signature

```
   public Boolean isUndeletable()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the object can be updated by the current user, `false` otherwise.

Signature

```
   public Boolean isUpdateable()

```


### Apex Reference Guide DescribeTabResult Class

Return Value

Type: Boolean

##### **`toString()`**

Returns a string that represents the SObject.

Signature

```
   public String toString()

```

Return Value

Type: String

### DescribeTabResult Class

Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.

Namespace

Schema

Usage

The `getTabs` method of the `Schema.DescribeTabSetResult` returns a list of `Schema.DescribeTabResult` objects
that describe the tabs of one app.

The methods in the `Schema.DescribeTabResult` class can be called using their property counterparts. For each method starting
with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`tabResultObj.label` is equivalent to `tabResultObj.getLabel()` . Similarly, for each method starting with `is`, omit
the `is` prefix and the ending parentheses `()` . For example, `tabResultObj.isCustom` is equivalent to
`tabResultObj.custom` .

#### DescribeTabResult Methods

### The following are methods for DescribeTabResult . All are instance methods.

IN THIS SECTION:

getColors()
Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

getIconUrl()
Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to
the heading at the top of most pages.

getIcons()
Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.


Apex Reference Guide DescribeTabResult Class

getLabel()
Returns the display label of this tab.

getMiniIconUrl()
Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears
in related lists and other locations.

getSobjectName()
Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

getUrl()
Returns a fully qualified URL for viewing this tab.

isCustom()
Returns `true` if this is a custom tab, or `false` if this is a standard tab.

##### getColors()

Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```

Return Value

Type: List<Schema.DescribeColorResult>

##### getIconUrl()

Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to the
heading at the top of most pages.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>


Apex Reference Guide DescribeTabResult Class

##### getLabel()

Returns the display label of this tab.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears in
related lists and other locations.

Signature

```
   public String getMiniIconUrl()

```

Return Value

Type: String

##### getSobjectName()

Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

Signature

```
   public String getSobjectName()

```

Return Value

Type: String

##### getUrl()

Returns a fully qualified URL for viewing this tab.

Signature

```
   public String getUrl()

```

Return Value

Type: String


### Apex Reference Guide DescribeTabSetResult Class

##### isCustom()

Returns `true` if this is a custom tab, or `false` if this is a standard tab.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

### DescribeTabSetResult Class

Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.

Namespace

Schema

Usage

The `Schema.describeTabs` method returns a list of `Schema.DescribeTabSetResult` objects that describe Salesforce
Classic standard and custom apps.

The methods in the `Schema.DescribeTabSetResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`tabSetResultObj.label` is equivalent to `tabSetResultObj.getLabel()` . Similarly, for each method starting with
##### is, omit the is prefix and the ending parentheses () . For example, tabSetResultObj.isSelected is equivalent to

`tabSetResultObj.selected` .

Example

This example shows how to call the `Schema.describeTabs` method to get describe information for all available Salesforce Classic
apps. This example iterates through each describe result and gets more metadata information for the Sales app.

```
   // App we're interested to get more info about

   String appName = 'Sales';

   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get more information for the Sales app

      if (tsr.getLabel() == appName) {

        // Find out if the app is selected

        if (tsr.isSelected()) {

           System.debug('The ' + appName + ' app is selected. ');

        }

        // Get the app's Logo URL and namespace

        String logo = tsr.getLogoUrl();

```


Apex Reference Guide DescribeTabSetResult Class

```
        System.debug('Logo URL: ' + logo);

        String ns = tsr.getNamespace();

        if (ns == '') {

           System.debug('The ' + appName + ' app has no namespace defined.');

        }

        else {

           System.debug('Namespace: ' + ns);

        }

        // Get the number of tabs

        System.debug('The ' + appName + ' app has ' + tsr.getTabs().size() + ' tabs.');

      }

   }

   // Example debug statement output

   // DEBUG|The Sales app is selected.

   // DEBUG|Logo URL:

   https:// MyDomainName .my.salesforce.com/img/seasonLogos/2014_winter_aloha.png

   // DEBUG|The Sales app has no namespace defined.

   // DEBUG|The Sales app has 14 tabs.

#### DescribeTabSetResult Methods The following are methods for DescribeTabSetResult . All are instance methods.

```

IN THIS SECTION:

##### getDescription()

Returns the display description for the standard or custom app.

getLabel()
Returns the display label for the standard or custom app.

getLogoUrl()
Returns a fully qualified URL to the logo image associated with the standard or custom app.

getNamespace()
Returns the developer namespace prefix of a Salesforce AppExchange managed package.

getTabs()
Returns metadata information about the standard or custom app’s displayed tabs.

isSelected()
Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

##### getDescription()

Returns the display description for the standard or custom app.

Signature

```
   public String getDescription()

```


Apex Reference Guide DescribeTabSetResult Class

Return Value

Type: String

##### getLabel()

Returns the display label for the standard or custom app.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The display label changes when tabs are renamed in the Salesforce user interface. See the Salesforce online help for more information.

##### getLogoUrl()

Returns a fully qualified URL to the logo image associated with the standard or custom app.

Signature

```
   public String getLogoUrl()

```

Return Value

Type: String

##### getNamespace()

