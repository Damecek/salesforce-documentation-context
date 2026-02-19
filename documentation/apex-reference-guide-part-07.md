Returns the developer namespace prefix of a Salesforce AppExchange managed package.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Usage

This namespace prefix corresponds to the namespace prefix of the Developer Edition organization that was enabled to allow publishing
a managed package. This method applies to a custom app containing a set of tabs and installed as part of a managed package.


### Apex Reference Guide DisplayType Enum

##### getTabs()

Returns metadata information about the standard or custom app’s displayed tabs.

Signature

```
   public List<Schema.DescribeTabResult> getTabs()

```

Return Value

Type: List<Schema.DescribeTabResult>

##### **`isSelected()`**

Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

Signature

```
   public Boolean isSelected()

```

Return Value

Type: Boolean

### DisplayType Enum

A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`ADDRESS` Address values

`ANYTYPE` Any value of the following types: `String`, `Picklist`, `Boolean`, `Integer`, `Double`,
`Percent`, `ID`, `Date`, `DateTime`, `URL`, or `Email` .

`BASE64` Base64-encoded arbitrary binary data (of type base64Binary)

`BOOLEAN` Boolean ( `true` or `false` ) values

`COMBOBOX` Comboboxes, which provide a set of enumerated values and allow the user to specify a value
not in the list

`COMPLEXVALUE` Complex Value Type (CVT)

`CURRENCY` Currency values

`DATACATEGORYGROUPREFERENCE` Reference to a data category group or a category unique name

`DATE` Date values


### Apex Reference Guide FieldDescribeOptions Enum

**Type Field Value** **What the Field Object Contains**

`DATETIME` DateTime values

`DOUBLE` Double values

`EMAIL` Email addresses

`ENCRYPTEDSTRING` Encrypted string

`FLOATARRAY` Array of float values, reserved for future use.

`ID` Primary key field for an object

`INTEGER` Integer values

`JSON` JSON format

`LOCATION` Location values, including latitude and longitude.

`LONG` Long values

`MULTIPICKLIST` Multi-select picklists, which provide a set of enumerated values from which multiple values can
be selected

`PERCENT` Percent values

`PHONE` Phone numbers. Values can include alphabetic characters. Client applications are responsible for
phone number formatting.

`PICKLIST` Single-select picklists, which provide a set of enumerated values from which only one value can
be selected

`REFERENCE` Cross-references to a different object, analogous to a foreign key field

`SOBJECT` An sObject variable represents a row of data and can only be declared in Apex using the SOAP
API name of the object.

`STRING` String values

`TEXTAREA` String values that are displayed as multiline text fields

`TEXTARRAY` Array of text values, reserved for future use.

`TIME` Time values

`URL` URL values that are displayed as hyperlinks

Usage

[For more information, see Field Types in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/field_types.htm) _Object Reference for Salesforce_ . For more information about the methods shared by all enums,
see Enum Methods.

### FieldDescribeOptions Enum

A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.


### Apex Reference Guide FieldSet Class

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.FieldDescribeOptions` enum.

**Value** **Description**

`DEFAULT` Compute context-specific, describe field results.

`FULL_DESCRIBE` Compute all aspects of describe field results.

### FieldSet Class

Contains methods for discovering and retrieving the details of field sets created on sObjects.

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSet` class to discover the fields contained within a field set, and get details about the field
set itself, such as the name, namespace, label, and so on. The following example shows how to get a collection of field set describe result
objects for an sObject. The key of the returned Map is the field set name, and the value is the corresponding field set describe result.

```
   Map<String, Schema.FieldSet> FsMap =

      Schema.SObjectType.Account.fieldSets.getMap();

```

Field sets are also available from sObject describe results. The following lines of code are equivalent to the prior sample:

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

```

To work with an individual field set, you can access it via the map of field sets on an sObject or, when you know the name of the field
set in advance, using an explicit reference to the field set. The following two lines of code retrieve the same field set:

```
   Schema.FieldSet fs1 = Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name');

   Schema.FieldSet fs2 = Schema.SObjectType.Account.fieldSets.field_set_name;

```


Apex Reference Guide FieldSet Class

Example: Displaying a Field Set on a Visualforce Page

This sample uses `Schema.FieldSet` and `Schema.FieldSetMember` methods to dynamically get all the fields in the
Dimensions field set for the Merchandise custom object. The list of fields is then used to construct a SOQL query that ensures those fields
are available for display. The Visualforce page uses the `MerchandiseDetails` class as its controller.

```
   public class MerchandiseDetails {

      public Merchandise__c merch { get; set; }

      public MerchandiseDetails() {

        this.merch = getMerchandise();

      }

      public List<Schema.FieldSetMember> getFields() {

        return SObjectType.Merchandise__c.FieldSets.Dimensions.getFields();

      }

      private Merchandise__c getMerchandise() {

        String query = 'SELECT ';

        for(Schema.FieldSetMember f : this.getFields()) {

           query += f.getFieldPath() + ', ';

        }

        query += 'Id, Name FROM Merchandise__c LIMIT 1';

        return Database.query(query);

      }

   }

```

The Visualforce page using the above controller is simple:

```
   <apex:page controller="MerchandiseDetails">

      <apex:form >

       <apex:pageBlock title="Product Details">

         <apex:pageBlockSection title="Product">

            <apex:inputField value="{!merch.Name}"/>

         </apex:pageBlockSection>

         <apex:pageBlockSection title="Dimensions">

            <apex:repeat value="{!fields}" var="f">

              <apex:inputField value="{!merch[f.fieldPath]}"

                 required="{!OR(f.required, f.dbrequired)}"/>

            </apex:repeat>

         </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

One thing to note about the above markup is the expression used to determine if a field on the form should be indicated as being a
required field. A field in a field set can be required by either the field set definition, or the field’s own definition. The expression handles
both cases.


Apex Reference Guide FieldSet Class

#### FieldSet Methods The following are methods for FieldSet . All are instance methods.

IN THIS SECTION:

##### getDescription()

Returns the field set’s description.

##### getFields()

Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

getLabel()
Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

getName()
Returns the field set’s name.

getNamespace()
Returns the field set’s namespace.

getSObjectType()
Returns the `Schema.sObjectType` of the sObject containing the field set definition.

##### getDescription()

Returns the field set’s description.

Signature

```
   public String getDescription()

```

Return Value

Type: `String`

Usage

Description is a required field for a field set, intended to describe the context and content of the field set. It’s often intended for
administrators who might be configuring a field set defined in a managed package, rather than for end users.

##### getFields()

Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

Signature

```
   public List<FieldSetMember> getFields()

```

Return Value

Type: List<Schema.FieldSetMember>


Apex Reference Guide FieldSet Class

##### getLabel()

Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getName()

Returns the field set’s name.

Signature

```
   public String getName()

```

Return Value

Type: `String`

##### getNamespace()

Returns the field set’s namespace.

Signature

```
   public String getNamespace()

```

Return Value

Type: `String`

Usage

The returned namespace is an empty string if your organization hasn’t set a namespace, and the field set is defined in your organization.
Otherwise, it’s the namespace of your organization, or the namespace of the managed package containing the field set.

##### getSObjectType()

Returns the `Schema.sObjectType` of the sObject containing the field set definition.

Signature

```
   public Schema.SObjectType getSObjectType()

```


### Apex Reference Guide FieldSetMember Class

Return Value

Type: `Schema.SObjectType`

### FieldSetMember Class

Contains methods for accessing the metadata for field set member fields.

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSetMember` class to get details about fields contained within a field set, such as the field
label, type, a dynamic SOQL-ready field path, and so on. The following example shows how to get a collection of field set member
describe result objects for a specific field set on an sObject:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name').getFields();

```

If you know the name of the field set in advance, you can access its fields more directly using an explicit reference to the field set:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.field_set_name.getFields();

```

SEE ALSO:

FieldSet Class

#### FieldSetMember Methods

### The following are methods for FieldSetMember . All are instance methods.

IN THIS SECTION:

getDBRequired()
Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

getFieldPath()
Returns a field path string in a format ready to be used in a dynamic SOQL query.

getLabel()
Returns the text label that’s displayed next to the field in the Salesforce user interface.

getRequired()
Returns `true` if the field is required by the field set, otherwise, `false` .

getType()
Returns the field’s Apex data type.

getSObjectField()
Returns the token for this field.


Apex Reference Guide FieldSetMember Class

##### getDBRequired()

Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

Signature

```
   public Boolean getDBRequired()

```

Return Value

Type: `Boolean`

##### getFieldPath()

Returns a field path string in a format ready to be used in a dynamic SOQL query.

Signature

```
   public String getFieldPath()

```

Return Value

Type: `String`

Example

See Displaying a Field Set on a Visualforce Page for an example of how to use this method.

##### getLabel()

Returns the text label that’s displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getRequired()

Returns `true` if the field is required by the field set, otherwise, `false` .

Signature

```
   public Boolean getRequired()

```

Return Value

Type: `Boolean`


### Apex Reference Guide PicklistEntry Class

##### getType()

Returns the field’s Apex data type.

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: `Schema.DisplayType`

##### getSObjectField()

Returns the token for this field.

Signature

```
   public Schema.sObjectField getSObjectField()

```

Return Value

Type: Schema.SObjectField

### PicklistEntry Class

Represents a picklist entry.

Namespace

Schema

Usage

Picklist fields contain a list of one or more items from which a user chooses a single item. They display as drop-down lists in the Salesforce
user interface. One of the items can be configured as the default item.

A `Schema.PicklistEntry` object is returned from the field describe result using the `getPicklistValues` method. For
example:

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.PicklistEntry> P = F.getPicklistValues();

#### PicklistEntry Methods

### The following are methods for PicklistEntry . All are instance methods.

```

IN THIS SECTION:

getLabel()
Returns the display name of this item in the picklist.


Apex Reference Guide PicklistEntry Class

##### getValue()

Returns the value of this item in the picklist.

##### isActive()

Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

##### isDefaultValue()

Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as
the default.

##### getLabel()

Returns the display name of this item in the picklist.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of this item in the picklist.

Signature

```
   public String getValue()

```

Return Value

Type: String

##### isActive()

Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean

##### isDefaultValue()

Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as the
default.


### Apex Reference Guide RecordTypeInfo Class

Signature

```
   public Boolean isDefaultValue()

```

Return Value

Type: Boolean

### RecordTypeInfo Class

Contains methods for accessing record type information for an sObject with associated record types.

Namespace

Schema

Usage

A RecordTypeInfo object is returned from the sObject describe result using the `getRecordTypeInfos` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.RecordTypeInfo> RT = R.getRecordTypeInfos();

```

In addition to the `getRecordTypeInfos` method, you can use the `getRecordTypeInfosById` and the
`getRecordTypeInfosByName` methods. These methods return maps that associate RecordTypeInfo with record IDs and record
labels, respectively.

Example

The following example assumes at least one record type has been created for the Account object:

```
   RecordType rt = [SELECT Id,Name FROM RecordType WHERE SobjectType='Account' LIMIT 1];

   Schema.DescribeSObjectResult d = Schema.SObjectType.Account;

   Map<Id,Schema.RecordTypeInfo> rtMapById = d.getRecordTypeInfosById();

   Schema.RecordTypeInfo rtById = rtMapById.get(rt.id);

   Map<String,Schema.RecordTypeInfo> rtMapByName = d.getRecordTypeInfosByName();

   Schema.RecordTypeInfo rtByName = rtMapByName.get(rt.name);

   System.assertEquals(rtById,rtByName);

#### RecordTypeInfo Methods

### The following are methods for RecordTypeInfo . All are instance methods.

```

IN THIS SECTION:

getDeveloperName()
Returns the developer name for this record type.

getName()
Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.


Apex Reference Guide RecordTypeInfo Class

##### getRecordTypeId()

Returns the ID of this record type.

isActive()
Returns `true` if this record type is active, `false` otherwise.

isAvailable()
Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available
record types to the user when he or she is creating a new record.

isDefaultRecordTypeMapping()
Returns `true` if this is the default record type for the user, `false` otherwise.

isMaster()
Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.

##### getDeveloperName()

Returns the developer name for this record type.

Signature

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getName()

Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeId()

Returns the ID of this record type.

Signature

```
   public ID getRecordTypeId()

```

Return Value

Type: ID


Apex Reference Guide RecordTypeInfo Class

##### isActive()

Returns `true` if this record type is active, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean

##### isAvailable()

Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available record
types to the user when he or she is creating a new record.

Signature

```
   public Boolean isAvailable()

```

Return Value

Type: Boolean

##### isDefaultRecordTypeMapping()

Returns `true` if this is the default record type for the user, `false` otherwise.

Signature

```
   public Boolean isDefaultRecordTypeMapping()

```

Return Value

Type: Boolean

##### isMaster()

Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.

Signature

```
   public Boolean isMaster()

```

Return Value

Type: Boolean


### Apex Reference Guide SOAPType Enum SOAPType Enum

A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`anytype` Any value of the following types: `String`, `Boolean`, `Integer`, `Double`, `ID`, `Date` or
`DateTime` .

`base64binary` Base64-encoded arbitrary binary data (of type base64Binary)

`Boolean` Boolean ( `true` or `false` ) values

`Date` Date values

`DateTime` DateTime values

`Double` Double values

`ID` Primary key field for an object

`Integer` Integer values

`String` String values

`Time` Time values

Usage

To programmatically retrieve the list of valid SOAPType enum values, use this code sample.

```
   system.debug(SoapType.values().size()); //Gets the number of supported values

   for (SoapType st : SoapType.values()) system.debug(st);

```

[For more information, see SOAPTypes in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm#soaptype_topic) _SOAP API Developer Guide_ . For more information about the methods shared by all enums,
see Enum Methods.

### SObjectDescribeOptions Enum

A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.SObjectDescribeOptions` enum.


### Apex Reference Guide SObjectField Class

**Value** **Description**

`DEFAULT` Either eager-load or lazy-load depending on the API version.

`DEFERRED` Lazy-load child relationships; do not load all child relationships at the time of first
invocation of the method.

`FULL` Eager-load all elements of the describe, including child relationships, up-front at
the time of method invocation.

See `getDescribe(options)` .

### SObjectField Class

A `Schema.sObjectField` object is returned from the field describe result using the `getController` and `getSObjectField`
methods.

Namespace

Schema

Example

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   Schema.sObjectField T = F.getSObjectField();

#### sObjectField Methods The following are instance methods for sObjectField .

```

IN THIS SECTION:

##### getDescribe()

Returns the describe field result for this field.

getDescribe(options)
Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

##### getDescribe()

Returns the describe field result for this field.

Signature

```
   public Schema.DescribeFieldResult getDescribe()

```

Return Value

Type: Schema.DescribeFieldResult


### Apex Reference Guide SObjectType Class

##### getDescribe(options)

Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

Signature

```
   public Schema.DescribeFieldResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object

Use this parameter to pass `FieldDescribeOptions.FULL_DESCRIBE` when a subset of system objects could have
different results for picklist values based on the context they're invoked in. This parameter computes all aspects of describe field
results.

For example, `AIConversationContext.PersonType` field is a picklist that contains a list of accessible object types.

Return Value

Type: Schema.DescribeFieldResult

### SObjectType Class

A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from the
sObject describe result using the `getSObjectType` method.

Namespace

Schema

Usage

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.sObjectType> P = F.getReferenceTo();

#### SObjectType Methods

### The following are methods for SObjectType . All are instance methods.

```

IN THIS SECTION:

getDescribe()
Returns the describe sObject result for this field.

##### getDescribe(options)

Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front,
or not.

newSObject()
Constructs a new sObject of this type.


Apex Reference Guide SObjectType Class

newSObject(id)
Constructs a new sObject of this type, with the specified ID.

newSObject(recordTypeId, loadDefaults)
Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

##### getDescribe()

Returns the describe sObject result for this field.

Signature

```
   public Schema.DescribeSObjectResult getDescribe()

```

Return Value

Type: Schema.DescribeSObjectResult

##### getDescribe(options)

Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front, or
not.

Signature

```
   public Schema.DescribeSObjectResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object

The parameter values determine how the elements of the describe operation are loaded.

**•** Use `SObjectDescribeOptions.FULL` to eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation. This describe guarantees fully coherent results, even if the describe object is passed to another
namespace, API version, or other Apex context that may have different results when generating describe attributes.

**•** Use `SObjectDescribeOptions.DEFERRED` to enable lazy initialization of describe attributes on first use. This means
that all child relationships will not be loaded at the time of first invocation of the method.

**•** Use `SObjectDescribeOptions.DEFAULT` to default to either eager-load or lazy-load depending on the API version.

The type of describe operation, as determined by the parameter value is depicted in this table.

**Table 2: Type of Load for SObjectType.getDescribe()**


Apex Reference Guide SObjectType Class

Return Value

Type: Schema.DescribeSObjectResult

##### newSObject()

Constructs a new sObject of this type.

Signature

```
   public sObject newSObject()

```

Return Value

Type: sObject

Example

[For an example, see Dynamic DML.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_dml.htm)

##### newSObject(id)

Constructs a new sObject of this type, with the specified ID.

Signature

```
   public sObject newSObject(ID id)

```

Parameters

```
   id
```

Type: ID

Return Value

Type: sObject

Usage

For the argument, pass the ID of an existing record in the database.

After you create a new sObject, the sObject returned has all fields set to `null` . You can set any updateable field to desired values and
then update the record in the database. Only the fields you set new values for are updated and all other fields which are not system
fields are preserved.

##### newSObject(recordTypeId, loadDefaults)

Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Apex Reference Guide SObjectType Class

Signature

```
   public sObject newSObject(ID recordTypeId, Boolean loadDefaults)

```

Parameters

```
   recordTypeId
```

Type: ID

Specifies the record type ID of the sObject to create. If no record type exists for this sObject, use `null` . If the sObject has record
types and you specify `null`, the default record type is used.

```
   loadDefaults
```

Type: Boolean

Specifies whether to populate custom fields with their predefined default values ( `true` ) or not ( `false` ).

Return Value

Type: sObject

Usage

**•** For required fields that have no default values, make sure to provide a value before inserting the new sObject. Otherwise, the insertion
results in an error. An example is the Account Name field or a master-detail relationship field.

**•** Since picklists and multi-select picklists can have default values specified per record type, this method populates the default value
corresponding to the record type specified.

**•** If fields have no predefined default values and the _`loadDefaults`_ argument is `true`, this method creates the sObject with field
values of `null` .

**•** If the _`loadDefaults`_ argument is `false`, this method creates the sObject with field values of `null` .

**•** This method populates read-only custom fields of the new sObject with default values. You can then insert the new sObject with
the read-only fields, even though these fields cannot be edited after they’re inserted.

**•** If a custom field is marked as unique and also provides a default value, inserting more than one new sObject will cause a run-time
exception because of duplicate field values.

To learn more about default field values, see “Default Field Values” in the Salesforce online help.

Note: You can also use this method to create a platform event with a prepopulated `EventUuid` field value for Apex publish
[callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
_Platform Events Developer Guide_ .

Example: Creating New sObject with Default Values

This sample creates an account with any default values populated for its custom fields, if any, using the `newSObject` method. It also
creates a second account for a specific record type. For both accounts, the sample sets the Name field, which is a required field that
doesn’t have a default value, before inserting the new accounts.

```
   // Create an account with predefined default values

   Account acct = (Account)Account.sObjectType.newSObject(null, true);

   // Provide a value for Name

   acct.Name = 'Acme';

   // Insert new account

   insert acct;

```


## Apex Reference Guide Search Namespace

```
   // This is for record type RT1 of Account

   ID rtId = [SELECT Id FROM RecordType WHERE sObjectType='Account' AND Name='RT1'].Id;

   Account acct2 = (Account)Account.sObjectType.newSObject(rtId, true);

   // Provide a value for Name

   acct2.Name = 'Acme2';

   // Insert new account

   insert acct2;

## Search Namespace The Search namespace provides classes for getting search results and suggestion results. The following are the classes in the Search namespace.

```

IN THIS SECTION:

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType,`
`options)` when the SOSL search query contains a KnowledgeArticleVersion object.

QuestionSuggestionFilter Class
The `Search.QuestionSuggestionFilter` class filters results from a call to
`System.Search.suggest(searchQuery, sObjectType, options)` when the SOSL `searchQuery` contains
a `FeedItem` object.

SearchResult Class
A wrapper object that contains an sObject and search metadata.

SearchResults Class
Wraps the results returned by the `Search.find(String)` method.

SuggestionOption Class
Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String,`

`String, Search.SuggestionOption)` .

SuggestionResult Class
A wrapper object that contains an sObject.

SuggestionResults Class
Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

SEE ALSO:

find(searchQuery)

suggest(searchQuery, sObjectType, suggestions)

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType, options)`
when the SOSL search query contains a KnowledgeArticleVersion object.


Apex Reference Guide KnowledgeSuggestionFilter Class

Namespace

Search

#### KnowledgeSuggestionFilter Methods The following are methods for KnowledgeSuggestionFilter .

IN THIS SECTION:

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

addDataCategory(dataCategoryGroupName, dataCategoryName)
Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.

addTopic(topic)
Specifies the article topic to return. This filter is optional.

setChannel(channelName)
Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.

setDataCategories(dataCategoryFilters)
Adds filters that narrow suggestion results to display articles in the specified data categories. Use this method to set multiple data
category group and name pairs in one call. This filter is optional.

setLanguage(localeCode)
Sets a language to narrow the suggestion results to display articles in that language. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setPublishStatus(publishStatus)
Sets a publish status to narrow the suggestion results to display articles with that status. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setValidationStatus(validationStatus)
Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

Signature

```
   public void addArticleType(String articleType)

```

Parameters

```
   articleType
```

Type: String

A three-character ID prefix indicating the desired article type.


Apex Reference Guide KnowledgeSuggestionFilter Class

Return Value

Type: void

Usage

To add more than 1 article type, call the method multiple times.

##### addDataCategory(dataCategoryGroupName, dataCategoryName)

Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.

Signature

```
   public void addDataCategory(String dataCategoryGroupName, String dataCategoryName)

```

Parameters

```
   dataCategoryGroupName
```

Type: String

The name of the data category group

```
   dataCategoryName
```

Type: String

The name of the data category.

Return Value

Type: void

Usage

To set multiple data categories, call the method multiple times. The name of the data category group and name of the data category
for desired articles, expressed as a mapping, for example,
`Search.KnowledgeSuggestionFilter.addDataCategory('Regions', 'Asia')` .

##### addTopic(topic)

Specifies the article topic to return. This filter is optional.

Signature

```
   public void addTopic(String topic)

```

Parameters

##### _`addTopic`_

Type: String

The name of the article topic.


Apex Reference Guide KnowledgeSuggestionFilter Class

Return Value

Type: void

Usage

To add more than 1 article topic, call the method multiple times.

##### setChannel(channelName)

Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.

Signature

```
   public void setChannel(String channelName)

```

Parameters

```
   channelName
```

Type: String

The name of a channel. Valid values are:

**•** `AllChannels` –Visible in all channels the user has access to

**•** `App` –Visible in the internal Salesforce Knowledge application

**•** `Pkb` –Visible in the public knowledge base

**•** `Csp` –Visible in the Customer Portal

**•** `Prm` –Visible in the Partner Portal

If `channel` isn’t specified, the default value is determined by the type of user.

**•** `Pkb` for a guest user

**•** `Csp` for a Customer Portal user

**•** `Prm` for a Partner Portal user

**•** `App` for any other type of user

If `channel` is specified, the specified value may not be the actual value requested, because of certain requirements.

**•** For guest, Customer Portal, and Partner Portal users, the specified value must match the default value for each user type. If the
values don’t match or `AllChannels` is specified, then `App` replaces the specified value.

**•** For all users other than guest, Customer Portal, and Partner Portal users:

**–** If `Pkb`, `Csp`, `Prm`, or `App` are specified, then the specified value is used.

**–** If `AllChannels` is specified, then `App` replaces the specified value.

Return Value

Type: void

##### setDataCategories(dataCategoryFilters)

Adds filters that narrow suggestion results to display articles in the specified data categories. Use this method to set multiple data category
group and name pairs in one call. This filter is optional.


Apex Reference Guide KnowledgeSuggestionFilter Class

Signature

```
   public void setDataCategories(Map dataCategoryFilters)

```

Parameters

```
   dataCategoryFilters
```

Type: Map

A map of data category group and data category name pairs.

Return Value

Type: void

##### setLanguage(localeCode)

Sets a language to narrow the suggestion results to display articles in that language. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

Signature

```
   public void setLanguage(String localeCode)

```

Parameters

```
   localeCode
```

Type: String

A locale code. For example, `'en_US'` (English–United States), or `'es'` (Spanish).

Return Value

Type: void

SEE ALSO:

[Supported Locales](https://help.salesforce.com/HTViewHelpDoc?id=admin_supported_locales.htm&language=en_US)

##### setPublishStatus(publishStatus)

Sets a publish status to narrow the suggestion results to display articles with that status. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

Signature

```
   public void setPublishStatus(String publishStatus)

```

Parameters

```
   publishStatus
```

Type: String


### Apex Reference Guide QuestionSuggestionFilter Class

A publish status. Valid values are:

**•** `Draft` –Articles aren’t published in Salesforce Knowledge.

**•** `Online` –Articles are published in Salesforce Knowledge.

**•** `Archived` –Articles aren’t published and are available in Archived Articles view.

##### setValidationStatus(validationStatus)

Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.

Signature

```
   public void setValidationStatus(String validationStatus)

```

Parameters

```
   validationStatus
```

Type: String

An article validation status. These values are available in the `ValidationStatus` field on the KnowledgeArticleVersion object.

Return Value

Type: void

### QuestionSuggestionFilter Class

The `Search.QuestionSuggestionFilter` class filters results from a call to `System.Search.suggest(searchQuery,`
`sObjectType, options)` when the SOSL `searchQuery` contains a `FeedItem` object.

Namespace

Search

IN THIS SECTION:

#### QuestionSuggestionFilter Methods QuestionSuggestionFilter Methods

### The following are methods for QuestionSuggestionFilter .

IN THIS SECTION:

addGroupId(groupId)
Adds a filter to display questions associated with the single specified group whose ID is passed in as an argument. This filter is
optional.

addNetworkId(networkId)
Adds a filter to display questions associated with the single specified network whose ID is passed in as an argument. This filter is
optional.


Apex Reference Guide QuestionSuggestionFilter Class

addUserId(userId)
Adds a filter to display questions belonging to the single specified user whose ID is passed in as an argument. This filter is optional.

setGroupIds(groupIds)
Sets a new list of groups to replace the current list of groups where the group IDs are passed in as an argument. This filter is optional.

setNetworkIds(networkIds)
Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.

setTopicId(topicId)
Sets a filter to display questions associated with the single specified topic whose ID is passed in as an argument. This filter is optional.

setUserIds(userIds)
Sets a new list of users to replace the current list of users where the users IDs are passed in as an argument. This filter is optional.

##### addGroupId(groupId)

Adds a filter to display questions associated with the single specified group whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addGroupId(String groupId)

```

Parameters

```
   groupId
```

Type: String

The ID for a group.

Return Value

Type: void

Usage

To add more than one group, call the method multiple times.

##### addNetworkId(networkId)

Adds a filter to display questions associated with the single specified network whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addNetworkId(String networkId)

```

Parameters

```
   networkId
```

Type: String

The ID of the Experience Cloud site about which you’re retrieving this information.


Apex Reference Guide QuestionSuggestionFilter Class

Return Value

Type: void

Usage

To add more than one network, call the method multiple times.

##### addUserId(userId)

Adds a filter to display questions belonging to the single specified user whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addUserId(String userId)

```

Parameters

```
   userId
```

Type: String

The ID for the user.

Return Value

Type: void

Usage

To add more than one user, call the method multiple times.

##### setGroupIds(groupIds)

Sets a new list of groups to replace the current list of groups where the group IDs are passed in as an argument. This filter is optional.

Signature

```
   public void setGroupIds(List<String> groupIds)

```

Parameters

```
   groupIds
```

Type: List<String>

A list of group IDs.

Return Value

Type: void


Apex Reference Guide QuestionSuggestionFilter Class

##### setNetworkIds(networkIds)

Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.

Signature

```
   public void setNetworkIds(List<String> networkIds)

```

Parameters

```
   networkIds
```

Type: List<String>

A list of network IDs.

Return Value

Type: void

##### setTopicId(topicId)

Sets a filter to display questions associated with the single specified topic whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void setTopicId(String topicId)

```

Parameters

```
   topicId
```

Type: String

The ID for a topic.

Return Value

Type: void

##### setUserIds(userIds)

Sets a new list of users to replace the current list of users where the users IDs are passed in as an argument. This filter is optional.

Signature

```
   public void setUserIds(List<String> userIds)

```

Parameters

```
   userIds
```

Type: List<String>

A list of user IDs.


### Apex Reference Guide SearchResult Class

Return Value

Type: void

### SearchResult Class

A wrapper object that contains an sObject and search metadata.

Namespace

### Search

#### SearchResult Methods

### The following are methods for SearchResult .

IN THIS SECTION:

##### getSObject()

Returns an sObject from a SearchResult object.

##### getSnippet(fieldName)

Returns a snippet from a Case, Feed, or Knowledge Article SearchResult object based on the specified field name.

getSnippet()
Returns a snippet from a SearchResult object based on the default field.

##### getSObject()

Returns an sObject from a SearchResult object.

Signature

```
   public SObject getSObject()

```

Return Value

Type: SObject

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### getSnippet(fieldName)

Returns a snippet from a Case, Feed, or Knowledge Article SearchResult object based on the specified field name.

Signature

```
   public String getSnippet(String fieldName)

```


### Apex Reference Guide SearchResults Class

Parameters

```
   fieldName
```

Type: String

The field name to use for creating the snippet.

Valid values: `Case.Casenumber`, `FeedPost.Title`, `KnowledgeArticleVersion.Title`

Return Value

Type: String

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### getSnippet()

Returns a snippet from a SearchResult object based on the default field.

Signature

```
   public String getSnippet()

```

Return Value

Type: String

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SearchResults Class

Wraps the results returned by the `Search.find(String)` method.

Namespace

### Search

#### SearchResults Methods

### The following are methods for SearchResults .

IN THIS SECTION:

get(sObjectType)
Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.


### Apex Reference Guide SuggestionOption Class

##### get(sObjectType)

Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.

Signature

```
   public List<Search.SearchResult> get(String sObjectType)

```

Parameters

```
   sObjectType
```

Type: String

The name of an sObject in the dynamic SOSL query passed to the `Search.find(String)` method.

Return Value

Type: List<Search.SearchResult>

Usage

SOSL queries passed to the `Search.find(String)` method can return results for multiple objects. For example, the query
`Search.find('FIND \'map\' IN ALL FIELDS RETURNING Account, Contact, Opportunity')` includes
results for 3 objects. You can call `get(string)` to retrieve search results for 1 object at a time. For example, to get results for the
Account object, call `Search.SearchResults.get('Account')` .

SEE ALSO:

find(searchQuery)

SearchResult Methods

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SuggestionOption Class

Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

Namespace

Search

#### SuggestionOption Methods

### The following are methods for SuggestionOption .

IN THIS SECTION:

setFilter(knowledgeSuggestionFilter)
Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .


Apex Reference Guide SuggestionOption Class

##### setLimit(limit)

The maximum number of record or article suggestions to retrieve.

##### setFilter(knowledgeSuggestionFilter)

Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

Signature

```
   public void setFilter(Search.KnowledegeSuggestionFilter knowledgeSuggestionFilter)

```

Parameters

```
   knowledgeSuggestionFilter
```

Type: KnowledgeSuggestionFilter

An object containing filters that narrow the search results.

Return Value

Type: void

Usage

```
   Search.KnowledgeSuggestionFilter filters = new Search.KnowledgeSuggestionFilter();

   filters.setLanguage('en_US');

   filters.setPublishStatus('Online');

   filters.setChannel('app');

   Search.SuggestionOption options = new Search.SuggestionOption();

   options.setFilter(filters);

   Search.SuggestionResults suggestionResults = Search.suggest('all', 'KnowledgeArticleVersion',

    options);

   for (Search.SuggestionResult searchResult : suggestionResults.getSuggestionResults()) {

     KnowledgeArticleVersion article = (KnowledgeArticleVersion)searchResult.getSObject();

     System.debug(article.title);

   }

##### setLimit(limit)

```

The maximum number of record or article suggestions to retrieve.

Signature

```
   public void setLimit(Integer limit)

```


### Apex Reference Guide SuggestionResult Class

Parameters

```
   limit
```

Type: Integer

The maximum number of record or article suggestions to retrieve.

Return Value

Type: void

Usage

By default, the `System.Search.suggest(String, String, Search.SuggestionOption)` method returns the
5 most relevant results. However, if your query is broad, it could match more than 5 results. If
`Search.SuggestionResults.hasMoreResults()` returns `true`, there are more than 5 results. To retrieve them, call
`setLimit(Integer)` to increase the number of suggestions results.

```
   Search.SuggestionOption option = new Search.SuggestionOption();

   option.setLimit(10);

   Search.suggest('my query', 'mySObjectType', option);

### SuggestionResult Class

```

A wrapper object that contains an sObject.

Namespace

Search

#### SuggestionResult Methods

### The following are methods for SuggestionResult .

IN THIS SECTION:

##### getSObject()

Returns the sObject from a SuggestionResult object.

##### getSObject()

Returns the sObject from a SuggestionResult object.

Signature

```
   public SObject getSObject()

```

Return Value

Type: SObject


### Apex Reference Guide SuggestionResults Class SuggestionResults Class

Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

Namespace

Search

#### SuggestionResults Methods

### The following are methods for SuggestionResults .

IN THIS SECTION:

##### getSuggestionResults()

Returns a list of SuggestionResult objects from the response to a call to `Search.suggest(String, String,`
`Search.SuggestionOption)` .

##### hasMoreResults() Indicates whether a call to System.Search.suggest(String, String, Search.SuggestionOption) has

more results available than were returned.

##### getSuggestionResults()

Returns a list of SuggestionResult objects from the response to a call to `Search.suggest(String, String,`
`Search.SuggestionOption)` .

Signature

```
   public List<Search.SuggestionResult> getSuggestionResults()

```

Return Value

Type: List<SuggestionResult>

##### hasMoreResults()

Indicates whether a call to `System.Search.suggest(String, String, Search.SuggestionOption)` has more
results available than were returned.

Signature

```
   public Boolean hasMoreResults()

```

Return Value

Type: Boolean


## Apex Reference Guide setup_flow_performance Namespace

Usage

If a limit isn’t specified, 5 records are returned in calls to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` . If there are more suggested records than the limit specified, a call to `hasMoreResults()`
returns `true` .

## setup_flow_performance Namespace

The class and methods in this namespace are for internal use only.

## The following are the classes in the setup_flow_performance namespace.

IN THIS SECTION:

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

Namespace

## setup_flow_performance Sfc Namespace

The Sfc namespace contains classes used in Salesforce Files.

## The following are the classes in the Sfc namespace.

IN THIS SECTION:

### ContentDownloadContext Enum

This enum specifies the download context.

ContentDownloadHandler Class
Use ContentDownloadHandler to define a custom download handler that controls how content is downloaded.

ContentDownloadHandlerFactory Interface
Use this interface to provide a class factory that Salesforce can call to create instances of your custom ContentDownloadHandler.

### ContentDownloadContext Enum

This enum specifies the download context.


### Apex Reference Guide ContentDownloadHandler Class

Usage

If the operationContext is `CONTENT`, `CHATTER`, `DELIVERY`, `S1`, or `MOBILE`, it can be used in a shepherd servlet as a query
parameter. It’s possible for a user to change the query parameters. If a user enters a value other than `CONTENT`, `CHATTER`, `DELIVERY`,
`S1`, or `MOBILE`, the value is treated as the default value `CONTENT` .

Users can’t set query parameters to `REST_API`, `SOQL`, or `RETRIEVE`, so these values can be assumed to be accurate.

Enum Values

The Sfc.ContentDownloadContext enum value identifies the content download context. The enum value is provided as a query parameter
in the file download servlet. The following are the values of the `Sfc.ContentDownloadContext` enum.

**Value** **Description**

`CHATTER` Download from Chatter.

`CONTENT` Default value. Downloads from the Salesforce CRM Content product.

`DELIVERY` Download of a content delivery.

`REST_API` Download from the Connect API ( `/connect/files/${fileId}/content`
endpoint). Used in both Android and iOS apps.

`RETRIEVE` Retrieve VersionData from SObject API.

`S1` Download from Lightning Experience.

`SOQL` Select VersionData from SOQL.

### ContentDownloadHandler Class

Use ContentDownloadHandler to define a custom download handler that controls how content is downloaded.

Namespace

Sfc on page 3446

IN THIS SECTION:

#### ContentDownloadHandler Properties ContentDownloadHandler Properties

### The following are properties for ContentDownloadHandler .

IN THIS SECTION:

downloadErrorMessage
A customized error message explaining why the download isn’t allowed.

isDownloadAllowed
Indicates whether or not download is allowed.


### Apex Reference Guide ContentDownloadHandlerFactory Interface

##### redirectUrl

The URL the user is redirected to when the download action isn't available, for applying Information Rights Management (IRM)
control, virus scanning, or other behavior.

##### downloadErrorMessage

A customized error message explaining why the download isn’t allowed.

Signature

```
   public String downloadErrorMessage {get; set;}

```

Property Value

Type: String

##### This message is used if a redirectUrl is not provided. If the download is not allowed, Salesforce will throw a ContentCustomizedDownloadException exception that contains the downloadErrorMessage . isDownloadAllowed

Indicates whether or not download is allowed.

Signature

```
   public Boolean isDownloadAllowed {get; set;}

```

Property Value

Type: Boolean

##### redirectUrl

The URL the user is redirected to when the download action isn't available, for applying Information Rights Management (IRM) control,
virus scanning, or other behavior.

Signature

```
   public String redirectUrl {get; set;}

```

Property Value

Type: String

The URL must be a valid relative URL. For example, the redirect can be a custom Visualforce page such as “/apex/IRMControl”. URLs with
no path, such as “www.domain.com”, results in an `InvalidParameterValueException` .

### ContentDownloadHandlerFactory Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom ContentDownloadHandler.


Apex Reference Guide ContentDownloadHandlerFactory Interface

Namespace

Sfc on page 3446

Usage

ContentDownloadHandler getContentDownloadHandler(List<ID> ids, ContentDownloadContext context);

IN THIS SECTION:

#### ContentDownloadHandlerFactory Methods ContentDownloadHandlerFactory Example Implementation ContentDownloadHandlerFactory Methods The following are methods for ContentDownloadHandlerFactory .

IN THIS SECTION:

##### getContentDownloadHandler(var1, var2)

Returns a ContentDownloadHandler for a given list of content IDs and a download context.

##### getContentDownloadHandler(var1, var2)

Returns a ContentDownloadHandler for a given list of content IDs and a download context.

Signature

```
   public Sfc.ContentDownloadHandler getContentDownloadHandler(List<Id> var1,

   Sfc.ContentDownloadContext var2)

```

Parameters

```
   var1
```

Type: List<Id>

```
   var2
```

Type: Sfc.ContentDownloadContext on page 3446

Return Value

Type: Sfc.ContentDownloadHandler on page 3447

#### ContentDownloadHandlerFactory Example Implementation

This example creates a class that implements the `Sfc.ContentDownloadHandlerFactory` interface and returns a download
handler that blocks downloading content to mobile devices.

```
   // Allow customization of the content Download experience

   public class ContentDownloadHandlerFactoryImpl implements Sfc.ContentDownloadHandlerFactory

    {

```


## Apex Reference Guide Sfdc_Checkout Namespace

```
     public Sfc.ContentDownloadHandler getContentDownloadHandler(List<ID> ids,

   Sfc.ContentDownloadContext context) {

      Sfc.ContentDownloadHandler contentDownloadHandler = new Sfc.ContentDownloadHandler();

      if(context == Sfc.ContentDownloadContext.MOBILE) {

       contentDownloadHandler.isDownloadAllowed = false;

       contentDownloadHandler.downloadErrorMessage = 'Downloading a file from a mobile

   device is not allowed.';

       return contentDownloadHandler;

      }

      contentDownloadHandler.isDownloadAllowed = true;

      return contentDownloadHandler;

     }

   }

## Sfdc_Checkout Namespace

```

The Sfdc_Checkout namespace provides an interface and classes for B2B Commerce apps in Salesforce.

## The following are the classes in the Sfdc_Checkout namespace.

IN THIS SECTION:

### AsyncCartProcessor Interface

Use this interface to implement asynchronous integrations in B2B Commerce.

B2BCheckoutController Class
Communicate with simple checkout Apex methods to work with data related to B2B Commerce checkout.

IntegrationInfo Class
Provides the values that B2B Commerce Checkout uses to map requests to responses, necessary metadata, and context.

IntegrationStatus Class
Supports synchronous execution of Apex integrations for B2B Commerce. The implementation must return the status of the execution.

IntegrationStatus.Status Enum
The IntegrationStatus.Status enum describes the status of the current integration.

### AsyncCartProcessor Interface

Use this interface to implement asynchronous integrations in B2B Commerce.

Namespace

## Sfdc_Checkout

IN THIS SECTION:

AsyncCartProcessor Methods

AsyncCartProcessor Example Implementation


Apex Reference Guide AsyncCartProcessor Interface

#### AsyncCartProcessor Methods The following are methods for AsyncCartProcessor .

IN THIS SECTION:

##### startCartProcessAsync(integrationInfo, cartId)

The startCartProcessAsync method is called asynchronously by the integration framework. Calling this method begins cart processing
for Commerce checkout.

##### startCartProcessAsync(integrationInfo, cartId)

The startCartProcessAsync method is called asynchronously by the integration framework. Calling this method begins cart processing
for Commerce checkout.

Signature

```
   public sfdc_checkout.IntegrationStatus

   startCartProcessAsync(sfdc_checkout.IntegrationInfo integrationInfo, Id cartId)

```

Parameters

```
   integrationInfo
```

Type: IntegrationInfo

Provides values that B2B Commerce checkout APIs use to map requests to responses, necessary metadata, and context.

```
   cartId
```

Type: Id

ID of the WebCart object.

Return Value

Type: IntegrationStatus

Status of the current integration. Possible values are `SUCCESS` and `FAILED` .

#### AsyncCartProcessor Example Implementation

This is an example implementation of the `sfdc_checkout.AsyncCartProcessor` interface.

```
   global interface checkout_AsyncCartProcessor {

     //Integration for async processing

     IntegrationStatus startCartProcessAsync(

       IntegrationInfo integrationInfo,

       Id cartId);

   }

```

AsyncCartProcessor is a base interface. There are four interfaces that extend it, including CartInventoryValidation, CartPriceCalculations,
CartShippingCharges, and CartTaxCalculations. For more information about these interfaces, including code examples and test classes,
[see Checkout Integrations.](https://github.com/forcedotcom/b2b-commerce-on-lightning-quickstart/tree/master/examples/checkout/integrations)


### Apex Reference Guide B2BCheckoutController Class B2BCheckoutController Class

Communicate with simple checkout Apex methods to work with data related to B2B Commerce checkout.

Namespace

sfdc_checkout

Usage

You must specify the `sfdc_checkout` namespace when creating an instance of this class.

IN THIS SECTION:

#### B2BCheckoutController Methods B2BCheckoutController Methods

### The following are methods for B2BCheckoutController .

IN THIS SECTION:

##### licenseCompliance(cartId, orderId)

If you implement your own cart-to-order process without invoking the Cart to Order flow core action, you must invoke this method
to correctly track your orders for GMV (Gross Merchandise Value) recognition.

##### licenseCompliance(cartId, orderId)

If you implement your own cart-to-order process without invoking the Cart to Order flow core action, you must invoke this method to
correctly track your orders for GMV (Gross Merchandise Value) recognition.

Signature

```
   public static void licenseCompliance(String cartId, String orderId)

```

Parameters

```
   cartId
```

Type: String

The `cartId` of a web cart from which an order is created.

```
   orderId
```

Type: String

The `orderId` of the order you created from the cart.

Return Value

Type: Void


### Apex Reference Guide IntegrationInfo Class IntegrationInfo Class

Provides the values that B2B Commerce Checkout uses to map requests to responses, necessary metadata, and context.

Namespace

sfdc_checkout on page 3450

Usage

This class provides information about a B2B Commerce integration. An instance of this class is passed as a parameter into the integration
interface.

IN THIS SECTION:

#### IntegrationInfo Properties IntegrationInfo Properties

### The following are properties for IntegrationInfo .

IN THIS SECTION:

##### integrationId

The unique ID of a B2B Commerce integration.

##### jobId

The ID of the job, specific to the Salesforce Background Operation framework.

siteLanguage
Site language to be used by third party services.

##### integrationId

The unique ID of a B2B Commerce integration.

Signature

```
   public String integrationId {get; set;}

```

Property Value

Type: String

##### jobId

The ID of the job, specific to the Salesforce Background Operation framework.

Signature

```
   public String jobId {get; set;}

```


### Apex Reference Guide IntegrationStatus Class

Property Value

Type: String

##### siteLanguage

Site language to be used by third party services.

Signature

```
   public String siteLanguage {get; set;}

```

Property Value

Type: String

### IntegrationStatus Class

Supports synchronous execution of Apex integrations for B2B Commerce. The implementation must return the status of the execution.

Namespace

sfdc_checkout

Usage

You must specify the `sfdc_checkout` namespace when creating an instance of this class.

IN THIS SECTION:

#### IntegrationStatus Properties IntegrationStatus Properties

### The following are properties for IntegrationStatus .

IN THIS SECTION:

##### status

Indicates the status of the integration process and whether or not it completed successfully.

##### status

Indicates the status of the integration process and whether or not it completed successfully.

Signature

```
   public sfdc_checkout.IntegrationStatus.Status status {get; set;}

```


### Apex Reference Guide IntegrationStatus.Status Enum

Property Value

Type: sfdc_checkout.IntegrationStatus.Status on page 3455

### IntegrationStatus.Status Enum

The IntegrationStatus.Status enum describes the status of the current integration.

Enum Values

The following are the values of the `sfdc_checkout.IntegrationStatus.Status` enum.

**Value** **Description**

`FAILED` Indicates transient, unknown error, managed by the implementor. The buyer can
retry this action.

`SUCCESS` Indicates the integration executed successfully.

## Sfdc_Enablement Namespace

The `sfdc_enablement` namespace provides classes for creating custom learning items to implement custom exercise types in
Enablement programs. Lightning web components are used to render the custom exercises on Program Builder.

The following are the classes in the `sfdc_enablement` namespace.

IN THIS SECTION:

### LearningEvaluation Class

Contains methods to retrieve and update details that are required to evaluate a learning item.

LearningEvaluationResult Class
Represents a user’s progress and progress status of a custom exercise in an Enablement program.

LearningItemEvaluationHandler Class
Contains methods to customize the evaluation process of a learning item.

LearningItemProgressStatus Enum
Represents the status of a user’s progress for a learning item in an Enablement program.

LearningItemSerializeDeserializer Class
Serializes and deserializes the content associated with a custom exercise when migrating an Enablement program from one org to
another.

### LearningEvaluation Class

Contains methods to retrieve and update details that are required to evaluate a learning item.

Namespace

sfdc_enablement


Apex Reference Guide LearningEvaluation Class

Usage

Pass this class as input to the sfdc_enablement.LearningEvaluationResult class.

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3459.

IN THIS SECTION:

#### LearningEvaluation Methods LearningEvaluation Methods The following are methods for LearningEvaluation .

IN THIS SECTION:

##### getDetails()

Retrieves the details associated with the learning evaluation instance.

##### getLearningItemId()

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

setDetails(details)
Sets or updates the details of the learning item record for this learning evaluation instance.

setLearningItemId(learningItemId)
Sets or updates the learning item record ID for this learning evaluation instance.

##### **`getDetails()`**

Retrieves the details associated with the learning evaluation instance.

Signature

```
   public Map<String,Object> getDetails()

```

Return Value

Type: Map on page 3894<String,Object on page 3961>

##### **`getLearningItemId()`**

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

Signature

```
   public String getLearningItemId()

```


### Apex Reference Guide LearningEvaluationResult Class

Return Value

Type: String

##### **`setDetails(details)`**

Sets or updates the details of the learning item record for this learning evaluation instance.

Signature

```
   public void setDetails(Map<String,Object> details)

```

Parameters

```
   details
```

Type: Map<String,Object>

[The details of the learning item record that you get by calling evaluateLearningItem API.](https://developer.salesforce.com/docs/platform/lwc/guide/reference-evaluate-learning-item.html)

Return Value

Type: void

##### **`setLearningItemId(learningItemId)`**

Sets or updates the learning item record ID for this learning evaluation instance.

Signature

```
   public void setLearningItemId(String learningItemId)

```

Parameters

```
   learningItemId
```

Type: String

Return Value

Type: void

### LearningEvaluationResult Class

Represents a user’s progress and progress status of a custom exercise in an Enablement program.

Namespace

sfdc_enablement


Apex Reference Guide LearningEvaluationResult Class

Usage

To calculate the user’s progress through an exercise as a percentage and return the progress status, use the
`sfdc_enablement.LearningEvaluationResult` class inside the sfdc_enablement.LearningItemEvaluationHandler. In
your custom code, set the percentages to correspond to these sfdc_enablement.LearningItemProgressStatus on page 3462 enum values.

**•** `NotStarted` is equal to 0.00

**•** `InProgress` is from 0.01 through 99.99

**•** `Completed` is equal to 100.00

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3459.

IN THIS SECTION:

#### LearningEvaluationResult Methods LearningEvaluationResult Methods The following are methods for LearningEvaluationResult .

IN THIS SECTION:

##### getLearningItemProgress()

Returns the progress percentage of the learning item.

getLearningItemProgressStatus()
Retrieves the progress status of the learning item.

setLearningItemProgress(learningItemProgress)
Sets the progress percentage of the learning item.

setLearningItemProgressStatus(learningItemProgressStatus)
Sets the progress status of the learning item.

##### **`getLearningItemProgress()`**

Returns the progress percentage of the learning item.

Signature

```
   public Double getLearningItemProgress()

```

Return Value

Type: Double

The progress percentage is formatted to two decimal places.


### Apex Reference Guide LearningItemEvaluationHandler Class

##### **`getLearningItemProgressStatus()`**

Retrieves the progress status of the learning item.

Signature

```
   public sfdc_enablement.LearningItemProgressStatus getLearningItemProgressStatus()

```

Return Value

Type: sfdc_enablement.LearningItemProgressStatus on page 3462

##### **`setLearningItemProgress(learningItemProgress)`**

Sets the progress percentage of the learning item.

Signature

```
   public void setLearningItemProgress(Double learningItemProgress)

```

Parameters

```
   learningItemProgress
```

Type: Double

The progress in percentage formatted to two decimal places.

Return Value

Type: void

##### **`setLearningItemProgressStatus(learningItemProgressStatus)`**

Sets the progress status of the learning item.

Signature

```
   public void setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus

   learningItemProgressStatus)

```

Parameters

```
   learningItemProgressStatus
```

Type: Sfdc_enablement.LearningItemProgressStatus on page 3462

Return Value

Type: void

### LearningItemEvaluationHandler Class

Contains methods to customize the evaluation process of a learning item.


Apex Reference Guide LearningItemEvaluationHandler Class

Namespace

sfdc_enablement

Usage

[Extend this class and implement your custom progress evaluation method. Then link this class to a LearningItemType metadata record](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
by passing the Apex class name to the `ApexEvaluationHandler` field.

Example

This code updates a user’s progress when they take a custom screen flow exercise in an Enablement program. The code updates the
progress by checking the number of screens the user has navigated, calculating the progress percentage, and returning the progress
[status. See Track a User's Progress in a Custom Exercise from](https://developer.salesforce.com/docs/sales/enablement/guide/custom-exercise-track-progress.html) _Salesforce Developer Guide_ : Sales Programs and Partner Tracks with Enablement.

```
   global class ScreenFlowEvaluationHandler extends

   sfdc_enablement.LearningItemEvaluationHandler {

      global override sfdc_enablement.LearningEvaluationResult

   evaluate(sfdc_enablement.LearningEvaluation learningEvaluation) {

        sfdc_enablement.LearningEvaluationResult result = new

   sfdc_enablement.LearningEvaluationResult();

        Double percentage = 100.0d;

        Map<String, Object> details = learningEvaluation.getDetails();

        String currentScreen = (String) details.get('currentScreen');

        String allScreensString = (String) details.get('allScreens');

        List<String> allScreens = allScreensString.split(',');

        String status = (String) details.get('status');

        if (status == 'FINISHED') {

           percentage = 100;

        } else {

           Integer index = 0;

           for (Integer i = 0; i < allScreens.size(); i++) {

             if (allScreens.get(i).equals(currentScreen)) {

               index = i + 1;

               break;

             }

           }

           if (index == allScreens.size()) {

             percentage = 99.0d;

           } else {

             percentage = (Double.valueOf(index) / Double.valueOf(allScreens.size()))

   * 100.0d;

           }

        }

        result.setLearningItemProgress(percentage);

        if (percentage == 100.0d) {

```


Apex Reference Guide LearningItemEvaluationHandler Class

```
   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.Completed);

        } else if (percentage == 0.0d) {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.NotStarted);

        } else {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.InProgress);

        }

        return result;

      }

   }

```

IN THIS SECTION:

#### LearningItemEvaluationHandler Methods LearningItemEvaluationHandler Methods The following are methods for LearningItemEvaluationHandler .

IN THIS SECTION:

##### evaluate(learningEvaluation)

Contains the custom logic for evaluating a learning item.

##### **`evaluate(learningEvaluation)`**

Contains the custom logic for evaluating a learning item.

Signature

```
   public Sfdc_enablement.LearningEvaluationResult

   evaluate(Sfdc_enablement.LearningEvaluation learningEvaluation)

```

Parameters

```
   learningEvaluation
```

Type: Sfdc_enablement.LearningEvaluation on page 3455

The details of the learning item record to be evaluated.

Return Value

Type: Sfdc_enablement.LearningEvaluationResult on page 3457

The result of the evaluation, including progress and status details.


### Apex Reference Guide LearningItemProgressStatus Enum LearningItemProgressStatus Enum

Represents the status of a user’s progress for a learning item in an Enablement program.

Usage

To set the progress status in the sfdc_enablement.LearningEvaluationResult on page 3457 class, use this enum.

Enum Values

The following are the values for the `sfdc_enablement.LearningItemProgressStatus` enum.

**Value** **Description**

`NotStarted` The user hasn't started the custom exercise.

`InProgress` The user's custom exercise is in progress.

`Completed` The user completed the custom exercise.

### LearningItemSerializeDeserializer Class

Serializes and deserializes the content associated with a custom exercise when migrating an Enablement program from one org to
another.

Namespace

sfdc_enablement

Usage

The class contains methods to serialize and deserialize custom exercise content between orgs when an Enablement program that
includes a custom exercise is migrated from one org to another through change sets or packaging.

Extend the `sfdc_enablement.LearningItemSerializeDeserializer` Apex abstract class and add the class name
to the `ApexSerializerDeserializer` [field of the LearningItemType metadata record. If you don’t add the class name to the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
LearningItemType metadata record, the `customContent` property for the custom exercise is empty in the destination org and no
[corresponding LearningItem record is created for the exercise’s EnblProgramTaskDefinition record.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_enblprogramtaskdefinition.htm)

The serialize on page 3464 method serializes the custom content of the learning item from the source org. This method is called when
you retrieve custom content from the source org.

The deserialize on page 3464 method is called during the deployment of a program. This method takes the serialized custom content,
recreates the custom object record in the target org, and returns a new learning item record ID.


Apex Reference Guide LearningItemSerializeDeserializer Class

Example

The sample code serializes and deserializes the custom content for a given learning item of a custom screen flow exercise in an Enablement
program. For this example to work, make sure the screen flow exists in the target org.

```
   global class ScreenFlowSerializerDeserializer extends

   Sfdc_enablement.LearningItemSerializeDeserializer {

      // The serialize method returns the serialized output of the

      // learning item’s custom content.

      global override String serialize(String learningItemId) {

        // Get the screen flow record ID associated with the learning item.

        LearningItem learningItem = [SELECT ScreenFlow_Field__c from LearningItem where

   Id =: learningItemId LIMIT 1];

        String screenFlowRecordId = learningItem.ScreenFlow_Field__c;

        // Get the flow version ID associated with that screen flow.

        ScreenFlow_Object__c screenFlowRecord = [SELECT FlowVersionId__c from

   ScreenFlow_Object__c where Id =: screenFlowRecordId LIMIT 1];

        String flowVersionId = screenFlowRecord.FlowVersionId__c;

        // Query the flow definition associated with that flow version.

        // Get the information you need to recreate the custom object

        // record in the destination org.

        // In this example, we're only getting the API name of the

        // flow version.

        FlowDefinitionView flowDefinitionView = [SELECT ApiName from FlowDefinitionView

   where ActiveVersionId =: flowVersionId LIMIT 1];

        // Return the serialized string.

        // In this example, we're only returning the API name of the flow

        // definition in the string.

        return flowDefinitionView.ApiName;

      }

      // The deserialize method deserializes the string containing the custom

      // content. In the method, you recreate the custom object record

      // for the destination org and populate it with the custom content.

      // Then insert the record in the destination org and return the new

      // custom object record ID.

      global override String deserialize(String serializedOutput) {

        // Find the flow active version ID of the same screen flow in the

        // destination org.

        FlowDefinitionView flowDefinitionView = [SELECT ActiveVersionId from

   FlowDefinitionView where ApiName =: serializedOutput LIMIT 1];

        String flowActiveVersionId = flowDefinitionView.ActiveVersionId;

        // Create the screen flow custom object record using the

        // information you passed to the string in the serialize method.

        // In this example, we only passed the API name of the screen flow

        // to the string.

        ScreenFlow_Object__c screenFlowRecord = new ScreenFlow_Object__c();

        screenFlowRecord.Name = serializedOutput;

        screenFlowRecord.FlowVersionId__c = flowActiveVersionId;

        // Insert the custom object record into the destination org.

```


Apex Reference Guide LearningItemSerializeDeserializer Class

```
        insert screenFlowRecord;

        // Return the new screen flow record ID for the new learning item

        // in the destination org.

        return screenFlowRecord.Id;

      }

   }

```

IN THIS SECTION:

#### LearningItemSerializeDeserializer Methods LearningItemSerializeDeserializer Methods The following are methods for LearningItemSerializeDeserializer .

IN THIS SECTION:

##### deserialize(serializedOutput)

Deserializes the provided custom content string and returns the record ID of the learning item.

##### serialize(learningItemId)

Serializes the custom content associated with the specified learning item. The serialized string represents the metadata of the custom
content and is used to recreate the custom content in the target Salesforce org during deployment.

##### **`deserialize(serializedOutput)`**

Deserializes the provided custom content string and returns the record ID of the learning item.

Signature

```
   public String deserialize(String serializedOutput)

```

Parameters

```
   serializedOutput
```

Type: String

The serialized information of custom content associated with a learning item The serialize(learningItemId) on page 3464 method
returns this information as a string that is less than or equal to 250 characters.

Return Value

Type: String

The ID of the learning item created for the target org.

##### **`serialize(learningItemId)`**

Serializes the custom content associated with the specified learning item. The serialized string represents the metadata of the custom
content and is used to recreate the custom content in the target Salesforce org during deployment.


## Apex Reference Guide sfdc_surveys Namespace

Signature

```
   public String serialize(String learningItemId)

```

Parameters

```
   learningItemId
```

Type: String

The ID of the learning item associated with the custom content to be serialized.

Return Value

Type: String

The serialized information of the custom content of the specified learning item. The format is a string that’s less than or equal to 250
characters long.

## sfdc_surveys Namespace The sfdc_surveys namespace provides an interface for shortening survey invitations. The following are the classes in the sfdc_surveys namespace.

IN THIS SECTION:

### SurveyInvitationLinkShortener Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom
### SurveyInvitationLinkShortener .

Example Implementation to Associate SurveySubjects with SurveyInvitation and SurveyResponses
If no survey responses are populated, create a custom code to associate SurveySubjects with SurveyInvitation and SurveyResponses.

### SurveyInvitationLinkShortener Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom
### SurveyInvitationLinkShortener .

Namespace

## sfdc_surveys

Usage

### Implement an instance of the SurveyInvitationLinkShortener interface to shorten the survey invitation that can be

distributed as short URLs over customer engaged channels, such as SMS, WhatsApp, or Facebook Messenger.

Special access rules

To implement this interface, you must have the Salesforce Feedback Management license enabled in your Salesforce organization.


Apex Reference Guide SurveyInvitationLinkShortener Interface

IN THIS SECTION:

#### SurveyInvitationLinkShortener Methods SurveyInvitationLinkShortener Example Implementation SurveyInvitationLinkShortener Methods The following are methods for SurveyInvitationLinkShortener .

IN THIS SECTION:

##### getShortenedURL(var1)

Returns a shortened URL for a given survey invitation.

##### **`getShortenedURL(var1)`**

Returns a shortened URL for a given survey invitation.

Signature

```
   public String getShortenedURL(String var1)

```

Parameters

```
   var1
```

Type: String

Return Value

Type: String

#### SurveyInvitationLinkShortener Example Implementation

This is an example implementation of the `sfdc_surveys.SurveyInvitationLinkShortener` interface.

[This sample code uses Named Credentials for authentication. For more information on Named Credentials, see Named Credentials as](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)
[Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

```
   public class SurveyInvitationLinkShortenerImpl implements

   sfdc_surveys.SurveyInvitationLinkShortener {

     public String getShortenedURL(String invitationURL) {

       return shortenUrlUsingBitlyService(invitationURL);

     }

     public String shortenUrlUsingBitlyService(String invitationURL) {

       HttpRequest request = new HttpRequest();

       request.setEndpoint('callout:bitly/v4/shorten');

       request.setMethod('POST');

       request.setHeader('Authorization', 'Bearer {!$Credential.Password}');

       request.setHeader('Accept', 'application/json');

       request.setHeader('Content-Type', 'application/json');

       request.setBody(JSON.serialize(new Map<String, Object>{

```


### Apex Reference Guide Example Implementation to Associate SurveySubjects with

SurveyInvitation and SurveyResponses

```
       'group_guid' => '{!$Credential.UserName}',

       'long_url' => invitationURL

       }));

       Http http = new Http();

       HttpResponse res = http.send(request);

       Object result = JSON.deserializeUntyped(res.getBody());

       if (result instanceof Map<String, Object>) {

         Map<String, Object> resultMap = (Map<String, Object>) result;

         Object shortenedLinkVal = resultMap.get('link');

         if(shortenedLinkVal != null && shortenedLinkVal instanceof String) {

           return (String) shortenedLinkVal;

         }

       }

       return invitationURL;

     }

   }

### Example Implementation to Associate SurveySubjects with SurveyInvitation
```

and SurveyResponses

If no survey responses are populated, create a custom code to associate SurveySubjects with SurveyInvitation and SurveyResponses.

This example shows how to associate SurveySubjects with SurveyInvitation and SurveyResponses.

```
   public class CreateEntriesInSurveyInvitationRespRL {

      // Utility to create SurveyInvitation and SurveySubject record

      public static void addEntry(String associatedRecordId, String surveyId, String

   participantId) {

        String invitationId = createSurveyInvitation(surveyId, participantId);

        createSurveySubject(invitationId, associatedRecordId);

      }

      // Create an unauthenticated invitation by setting the surveyId and participantId

      private static String createSurveyInvitation(String surveyId, String participantId) {

        SurveyInvitation surveyInv = new SurveyInvitation();

        surveyInv.Name = 'SurveyInvitationForCase'; // add your survey invitation name

   here

        surveyInv.ParticipantId = participantId;

        surveyInv.CommunityId = '0DBRM0000004n4y'; //add your community id here

        surveyInv.OptionsAllowGuestUserResponse = true;

        surveyInv.SurveyId = surveyId;

        // Insert the SurveyInvitation Record

        insert surveyInv;

        return surveyInv.Id;

      }

      // Associate the above invitation to the required record (eg: Case, Opportunity...)

```


## Apex Reference Guide Site Namespace

```
     private static void createSurveySubject(String invitationId, String associatedRecordId)

    {

        SurveySubject subj = new SurveySubject();

        subj.Name = 'Sur_Subject_for_invitation';

       subj.ParentId = invitationId; // similary you can use survey response id to associate

    survey subject to a response record.

        subj.SubjectId = associatedRecordId;

        // Insert the SurveySubject Record

        insert subj;

      }

   }

   //Use this trigger to create a survey subject record associated to

   //the Survey Response record

   trigger SurveyResponseForCaseTrigger on SurveyResponse (after insert) {

      System.debug('Inside Survey response trigger ');

      for(SurveyResponse sr: Trigger.New)

      {

       SurveySubject subj = new SurveySubject();

        subj.Name = 'Sur_Subject_for_response';

        subj.ParentId = sr.id; //Associating survey response id

        //Get the associatedRecordId recordId (like Case, Opportunity etc) using the

   SurveyInvitation Id and

        //assigning it to SubjectId, assuming we inserted SurveySubject record for the

   associated invitation

        //using the previous code

        List<SurveySubject> SurSubj=[select subjectid from SurveySubject where parentid =

   :sr.invitationId];

        for(SurveySubject sub:SurSubj){

           String ids=String.valueOf(sub.subjectid).substring(0,3);

           if('500'.equals(ids)){

             subj.SubjectId =sub.subjectid;

        // Insert the SurveySubject Record

           insert subj;

             break;

           }

   }

## Site Namespace The Site namespace provides an interface for rewriting Sites URLs. The following is the interface in the Site namespace.

```


### Apex Reference Guide UrlRewriter Interface

IN THIS SECTION:

### UrlRewriter Interface

Enables rewriting Sites URLs.

Site Exceptions
The `Site` namespace contains an exception class.

### UrlRewriter Interface

Enables rewriting Sites URLs.

Namespace

Site

Usage

Sites provides built-in logic that helps you display user-friendly URLs and links to site visitors. Create rules to rewrite URL requests typed
into the address bar, launched from bookmarks, or linked from external websites. You can also create rules to rewrite the URLs for links
within site pages. URL rewriting not only makes URLs more descriptive and intuitive for users, it allows search engines to better index
your site pages.

For example, let's say that you have a blog site. Without URL rewriting, a blog entry's URL might look like this:

```
   https://myblog.my.salesforce-sites.com/posts?id=003D000000Q0PcN

```

To rewrite URLs for a site, create an Apex class that maps the original URLs to user-friendly URLs, and then add the Apex class to your
site.

#### UrlRewriter Methods

### The following are methods for UrlRewriter . All are instance methods.

IN THIS SECTION:

##### generateUrlFor(salesforceUrls)

Maps a list of Salesforce URLs to a list of user-friendly URLs.

mapRequestUrl(userFriendlyUrl)
Maps a user-friendly URL to a Salesforce URL.

##### generateUrlFor(salesforceUrls)

Maps a list of Salesforce URLs to a list of user-friendly URLs.

Signature

```
   public System.PageReference[] generateUrlFor(System.PageReference[] salesforceUrls)

```


### Apex Reference Guide Site Exceptions

Parameters

```
   salesforceUrls
```

Type: System.PageReference[]

Return Value

Type: System.PageReference[]

Usage

You can use `List<PageReference>` instead of `PageReference[]`, if you prefer.

Important: The size and order of the input list of Salesforce URLs must exactly correspond to the size and order of the generated
list of user-friendly URLs. The `generateUrlFor` method maps input URLs to output URLs based on the order in the lists.

##### mapRequestUrl(userFriendlyUrl)

Maps a user-friendly URL to a Salesforce URL.

Signature

```
   public System.PageReference mapRequestUrl(System.PageReference userFriendlyUrl)

```

Parameters

```
   userFriendlyUrl
```

Type: System.PageReference

Return Value

Type: System.PageReference

### Site Exceptions The Site namespace contains an exception class.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The Site namespace contains this exception:

**Exception** **Description** **Methods**

`Site.ExternalUserCreateException` Unable to create
external user

Use the `String getMessage()` to get the error message
and write it to debug log.

Use `List<String> getDisplayMessages()` to get
a list of errors displayed to the end user.

This exception can’t be subclassed or thrown in code.


## Apex Reference Guide Slack Namespace Slack Namespace The Slack Namespace provides tools designed to accelerate and ease the process of developing Slack apps on the Salesforce platform. The following are the classes in the Slack namespace.

[App Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_access.html)

[Action Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_dispatchers.html)

[AppClient](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client.html)

[AppRequest Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_apprequest.html)

[Apps Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_apps.html)

[Auth Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_auth.html)

[BotClient Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_bot.html)

[BotsInfo Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_bot.html)

[Call Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_calls.html)

[Channel Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_channels.html)

[Chat Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_chat.html)

[Conversation Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_conversations.html)

[Dnd Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_dnd.html)

[Emoji CLasses](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_emojis.html)

[Event Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_events.html)

[Field Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_fields.html)

[File Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_files.html)

[Latest Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_latest.html)

[Message Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_messages.html)

[MigrationExchange Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_migrationexc.html)

[Modals Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_modal.html)

[Options Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_options.html)

[Paging Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_paging.html)

[Pin Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_pins.html)

[Purpose Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_purpose.html)

[Reaction Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_reactions.html)

[Reminder Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_reminders.html)

[RequestContext Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_requestcontext.html)

[ResponseMetadata Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_response_metadata.html)

[RunnableHandler Interface](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_runnablehandler.html)

[Search Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_search.html)

[Shortcut Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_shortcut.html)

[SlackCommand Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_slashcommand.html)


## Apex Reference Guide Support Namespace

[Star Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_stars.html)

[Team Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_teams.html)

[TestHarness Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_testharness.html)

[Topic Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_topics.html)

[User Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_users.html)

[UserClient Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_user.html)

[Usergroup Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_usergroups.html)

[UserMapping Service Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_usermapping_service.html)

[Views Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_views.html)

[Workflow Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_workflows.html)

## Support Namespace The Support namespace provides an interface used for Case Feed. The following is the interface in the Support namespace.

IN THIS SECTION:

### EmailTemplateSelector Interface

The `Support.EmailTemplateSelector` interface enables providing default email templates in Case Feed. With default
email templates, specified email templates are preloaded for cases based on criteria such as case origin or subject.

MilestoneTriggerTimeCalculator Interface
The `Support.MilestoneTriggerTimeCalculator` interface calculates the time trigger for a milestone.

### EmailTemplateSelector Interface

The `Support.EmailTemplateSelector` interface enables providing default email templates in Case Feed. With default email
templates, specified email templates are preloaded for cases based on criteria such as case origin or subject.

`Support.EmailTemplateSelector` works only in Salesforce Classic, not in Lightning Experience. Lightning Experience users
can specify default values for emails using the `QuickActionDefaultsHandler` interface.

Namespace

## Support

To specify default templates, you must create a class that implements `Support.EmailTemplateSelector` .

When you implement this interface, provide an empty parameterless constructor.

IN THIS SECTION:

EmailTemplateSelector Methods

EmailTemplateSelector Example Implementation


Apex Reference Guide EmailTemplateSelector Interface

#### EmailTemplateSelector Methods The following are methods for EmailTemplateSelector .

IN THIS SECTION:

##### getDefaultTemplateId(caseId)

Returns the ID of the email template to preload for the case currently being viewed in the case feed using the specified case ID.

##### getDefaultTemplateId(caseId)

Returns the ID of the email template to preload for the case currently being viewed in the case feed using the specified case ID.

Signature

```
   public ID getDefaultTemplateId(ID caseId)

```

Parameters

```
   caseId
```

Type: ID

Return Value

Type: ID

#### EmailTemplateSelector Example Implementation

This is an example implementation of the `Support.EmailTemplateSelector` interface.

The `getDefaultEmailTemplateId` method implementation retrieves the subject and description of the case corresponding
to the specified case ID. Next, it selects an email template based on the case subject and returns the email template ID.

```
   global class MyCaseTemplateChooser implements Support.EmailTemplateSelector {

      // Empty constructor

      global MyCaseTemplateChooser() { }

      // The main interface method

      global ID getDefaultEmailTemplateId(ID caseId) {

        // Select the case we're interested in, choosing any fields that are relevant to

   our decision

        Case c = [SELECT Subject, Description FROM Case WHERE Id=:caseId];

        EmailTemplate et;

        if (c.subject.contains('LX-1150')) {

           et = [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1150_template'];

        } else if(c.subject.contains('LX-1220')) {

           et = [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1220_template'];

        }

        // Return the ID of the template selected

        return et.id;

```


### Apex Reference Guide MilestoneTriggerTimeCalculator Interface

```
      }

   }

```

The following example tests the above code:

```
   @isTest

   private class MyCaseTemplateChooserTest {

      static testMethod void testChooseTemplate() {

        MyCaseTemplateChooser chooser = new MyCaseTemplateChooser();

        // Create a simulated case to test with

        Case c = new Case();

        c.Subject = 'I\'m having trouble with my LX-1150';

        Database.insert(c);

        // Make sure the proper template is chosen for this subject

        Id actualTemplateId = chooser.getDefaultEmailTemplateId(c.Id);

        EmailTemplate expectedTemplate =

         [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1150_template'];

        Id expectedTemplateId = expectedTemplate.Id;

        System.assertEquals(actualTemplateId, expectedTemplateId);

        // Change the case properties to match a different template

        c.Subject = 'My LX1220 is overheating';

        Database.update(c);

        // Make sure the correct template is chosen in this case

        actualTemplateId = chooser.getDefaultEmailTemplateId(c.Id);

        expectedTemplate =

         [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1220_template'];

        expectedTemplateId = expectedTemplate.Id;

        System.assertEquals(actualTemplateId, expectedTemplateId);

      }

   }

### MilestoneTriggerTimeCalculator Interface

```

The `Support.MilestoneTriggerTimeCalculator` interface calculates the time trigger for a milestone.

Namespace

Support

Implement the `Support.MilestoneTriggerTimeCalculator` interface to calculate a dynamic time trigger for a milestone
based on the milestone type, the properties of the case, and case-related objects. To implement the
`Support.MilestoneTriggerTimeCalculator` interface, you must first declare a class with the `implements` keyword
as follows:

```
   global class Employee implements Support.MilestoneTriggerTimeCalculator {

```


Apex Reference Guide MilestoneTriggerTimeCalculator Interface

Next, your class must provide an implementation for the following method:

```
   global Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId)

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

#### MilestoneTriggerTimeCalculator Methods MilestoneTriggerTimeCalculator Example Implementation MilestoneTriggerTimeCalculator Methods The following are instance methods for MilestoneTriggerTimeCalculator .

IN THIS SECTION:

##### calculateMilestoneTriggerTime(caseId, milestoneTypeId)

Calculates the milestone trigger time based on the specified case and milestone type and returns the time in minutes.

##### calculateMilestoneTriggerTime(caseId, milestoneTypeId)

Calculates the milestone trigger time based on the specified case and milestone type and returns the time in minutes.

Syntax

```
   public Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId)

```

Parameters

```
   caseId
```

Type: String

ID of the case the milestone is applied to.

```
   milestoneTypeId
```

Type: String

ID of the milestone type.

Return Value

Type: Integer

The calculated trigger time in minutes.

#### MilestoneTriggerTimeCalculator Example Implementation

This sample class demonstrates the implementation of the `Support.MilestoneTriggerTimeCalculator` interface. In this
sample, the case’s priority and the milestone `m1` determine that the time trigger is 18 minutes.

```
   global class myMilestoneTimeCalculator implements Support.MilestoneTriggerTimeCalculator

   {

```


## Apex Reference Guide System Namespace

```
      global Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId){

        Case c = [SELECT Priority FROM Case WHERE Id=:caseId];

        MilestoneType mt = [SELECT Name FROM MilestoneType WHERE Id=:milestoneTypeId];

        if (c.Priority != null && c.Priority.equals('High')){

            if (mt.Name != null && mt.Name.equals('m1')) { return 7;}

            else { return 5; }

        }

        else {

           return 18;

        }

      }

   }

```

This test class can be used to test the implementation of `Support.MilestoneTriggerTimeCalculator` .

```
   @isTest

   private class MilestoneTimeCalculatorTest {

      static testMethod void testMilestoneTimeCalculator() {

        // Select an existing milestone type to test with

        MilestoneType[] mtLst = [SELECT Id, Name FROM MilestoneType LIMIT 1];

        if(mtLst.size() == 0) { return; }

        MilestoneType mt = mtLst[0];

        // Create case data.

        // Typically, the milestone type is related to the case,

        // but for simplicity, the case is created separately for this test.

        Case c = new Case(priority = 'High');

        insert c;

        myMilestoneTimeCalculator calculator = new myMilestoneTimeCalculator();

        Integer actualTriggerTime = calculator.calculateMilestoneTriggerTime(c.Id, mt.Id);

        if(mt.name != null && mt.Name.equals('m1')) {

           System.assertEquals(actualTriggerTime, 7);

        }

        else {

           System.assertEquals(actualTriggerTime, 5);

        }

        c.priority = 'Low';

        update c;

        actualTriggerTime = calculator.calculateMilestoneTriggerTime(c.Id, mt.Id);

        System.assertEquals(actualTriggerTime, 18);

      }

   }

## System Namespace The System namespace provides classes and methods for core Apex functionality. The following are the classes in the System namespace.

```


Apex Reference Guide System Namespace

IN THIS SECTION:

AccessLevel Class
Defines the different modes, such as system or user mode, that Apex database operations execute in.

AccessType Enum
Specifies the access check type for the fields of an sObject.

Address Class
Contains methods for accessing the component fields of address compound fields.

Answers Class
Represents zone answers.

ApexPages Class
Use `ApexPages` to add and check for messages associated with the current page, as well as to reference the current page.

Approval Class
Contains methods for processing approval requests and setting approval-process locks and unlocks on records.

Assert Class
Contains methods to assert various conditions with test methods, such as whether two values are the same, a condition is true, or
a variable is null.

AsyncInfo Class
Provides methods to get the current stack depth, maximum stack depth, and the minimum queueable delay for Queueable
transactions, and to determine if maximum stack depth is set.

AsyncOptions Class
Contains maximum stack depths for queueable transactions and the minimum queueable delay in minutes. Passed as parameter
to the `System.enqueueJob()` method to define a unique queueable job signature, the maximum stack depth for queueable
transactions and the minimum queueable delay in minutes.

Blob Class
Contains methods for the Blob primitive data type.

Boolean Class
Contains methods for the Boolean primitive data type.

BusinessHours Class
Use the `BusinessHours` methods to set the business hours at which your customer support team operates.

CallbackStatus Enum
Specifies the status of asynchronous requests to an external system.

Callable Interface
Enables developers to use a common interface to build loosely coupled integrations between Apex classes or triggers, even for code
in separate packages. Agreeing upon a common interface enables developers from different companies or different departments
to build upon one another’s solutions. Implement this interface to enable the broader community, which might have different
solutions than the ones you had in mind, to extend your code’s functionality.

Cases Class
Use the `Cases` class to interact with case records.

Collator Class
Contains methods to get locale-specific instances that can be used for comparisons and sorting. Use the `getInstance()`
method to obtain the Collator instance for a given locale and pass the Collator as the Comparator parameter to the `list.sort()`
method.


Apex Reference Guide System Namespace

Comparable Interface
Adds sorting support for Lists that contain non-primitive types, that is, Lists of user-defined types. Your implementation must explicitly
handle null inputs in the `compareTo()` method to avoid a null pointer exception.

Comparator Interface
Implement different sort orders with the Comparator interface’s `compare()` method, and pass the Comparator as a parameter
to `List.sort()` . Your implementation must explicitly handle null inputs in the `compare()` method to avoid a null pointer
exception.

Continuation Class
Use the `Continuation` class to make callouts asynchronously to a SOAP or REST Web service.

Cookie Class
The `Cookie` class lets you access cookies for your Salesforce site using Apex.

Crypto Class
Provides methods for creating digests, message authentication codes, and signatures, as well as encrypting and decrypting information.

Custom Metadata Type Methods
Custom metadata types are customizable, deployable, packageable, and upgradeable application metadata. All custom metadata
is exposed in the application cache, which allows access without repeated queries to the database. The metadata is then available
for formula fields, validation rules, flows, Apex, and SOAP API. All methods are static.

Custom Settings Methods
Custom settings are similar to custom objects and enable application developers to create custom sets of data, as well as create and
associate custom data for an organization, profile, or specific user. All custom settings data is exposed in the application cache, which
enables efficient access without the cost of repeated queries to the database. This data is then available for formula fields, validation
rules, flows, Apex, and the SOAP API.

Database Class
Contains methods for creating and manipulating data.

Date Class
Contains methods for the Date primitive data type.

Datetime Class
Contains methods for the Datetime primitive data type.

Decimal Class
Contains methods for the Decimal primitive data type.

Domain Class
Represents an existing domain hosted by Salesforce that serves the org or its content. Contains methods to obtain information about
these domains, such as the domain type, My Domain name, and sandbox name.

DomainCreator Class
Use the DomainCreator class to return a hostname specific to the org. For example, get the org’s Visualforce hostname. Values are
returned as a hostname, such as _**`MyDomainName`**_ `.lightning.force.com` .

DomainParser Class
Use the DomainParser class to parse a domain that Salesforce hosts for the org and extract information about the domain.

DomainType Enum
Specifies the domain type for a System.Domain.

Double Class
Contains methods for the Double primitive data type.


Apex Reference Guide System Namespace

EmailMessages Class
Use the methods in the `EmailMessages` class to interact with emails and email threading.

EncodingUtil Class
Use the methods in the `EncodingUtil` class to encode and decode URL strings, and convert strings to hexadecimal format.

Enum Methods
An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Apex provides
built-in enums, such as `LoggingLevel`, and you can define your own enum.

EventBus Class
Contains methods for publishing platform events.

Exception Class and Built-In Exceptions
An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create
custom exceptions. All exceptions have common methods.

ExternalServiceTest Class
Provides methods to test an external service's asynchronous callouts, enables sending a mock request, asserts the expected request
payload, then triggers the mocked external service’s asynchronous callback response.

FlexQueue Class
Contains methods that reorder batch jobs in the Apex flex queue.

FeatureManagement Class
Use the methods in the `System.FeatureManagement` class to check and modify the values of feature parameters, and to
show or hide custom objects and custom permissions in your subscribers’ orgs.

Formula Class
Contains methods to get a builder for creating a formula instance and to update all formula fields on the input SObjects.

FormulaRecalcFieldError Class
The return type of the `FormulaRecalcResult.getErrors` method.

FormulaRecalcResult Class
The return type of the `Formula.recalculateFormulas` method.

Http Class
Use the `Http` class to initiate an HTTP request and response.

HttpCalloutMock Interface
Enables sending fake responses when testing HTTP callouts.

HttpRequest Class
Use the `HttpRequest` class to programmatically create HTTP requests like GET, POST, PATCH, PUT, and DELETE.

HttpResponse Class
Use the `HttpResponse` class to handle the HTTP response returned by the `Http` class.

Id Class
Contains methods for the ID primitive data type.

Ideas Class
Represents zone ideas.

InstallHandler Interface
Enables custom code to run after a managed package installation or upgrade.


Apex Reference Guide System Namespace

Integer Class
Contains methods for the Integer primitive data type.

JSON Class
Contains methods for serializing Apex objects into JSON format and deserializing JSON content that was serialized using the
`serialize` method in this class.

JSONGenerator Class
Contains methods used to serialize objects into JSON content using the standard JSON encoding.

JSONParser Class
Represents a parser for JSON-encoded content.

JSONToken Enum
Contains all token values used for parsing JSON content.

Label Class
Provides methods to retrieve a custom label or to check if translation exists for a label in a specific language and namespace. Label
names are dynamically resolved at run time, overriding the user’s current language if a translation exists for the requested language.
You can’t access labels that are protected in a different namespace.

Limits Class
Contains methods that return limit information for specific resources.

List Class
Contains methods for the List collection type.

Location Class
Contains methods for accessing the component fields of geolocation compound fields.

LoggingLevel Enum
Specifies the logging level for the `System.debug` method.

Long Class
Contains methods for the Long primitive data type.

Map Class
Contains methods for the Map collection type.

Matcher Class
Matchers use Patterns to perform match operations on a character string.

Math Class
Contains methods for mathematical operations.

Messaging Class
Contains messaging methods used when sending a single or mass email.

MultiStaticResourceCalloutMock Class
Utility class used to specify a fake response using multiple resources for testing HTTP callouts.

Network Class
Manage Experience Cloud sites.

Object Class
Contains methods that are implemented by all Apex types.

OrgLimit Class
Contains methods that provide the name, maximum value, and current value of an org limit.


Apex Reference Guide System Namespace

OrgLimits Class
Contains methods that provide a list or map of all OrgLimit instances for Salesforce your org, such as SOAP API requests, Bulk API
requests, and Streaming API limits.

PageReference Class
A PageReference is a reference to an instantiation of a page. Among other attributes, PageReferences consist of a URL and a set of
query parameter names and values.

Packaging Class
Contains a method for obtaining information about managed and unlocked packages.

Pattern Class
Represents a compiled representation of a regular expression.

Queueable Interface
Enables the asynchronous execution of Apex jobs that can be monitored.

QueueableContext Interface
Represents the parameter type of the `execute()` method in a class that implements the `Queueable` interface and contains
the job ID. This interface is implemented internally by Apex.

QueueableDuplicateSignature Class
Used in the `AsyncOptions` class to store the queueable job signature in the `DuplicateSignature` property.

QueueableDuplicateSignature.Builder Class
Build a unique signature for your queueable job using this inner builder class. The `build()` class method builds a
`QueueableDuplicateSignature` object, with input from the `addId()`, `addInteger()`, and `addString()`
methods. Use the `DuplicateSignature` property in the `AsyncOptions` class to store the queueable job signature.
Enqueue your job by using the `System.enqueueJob()` with the `AsyncOptions` parameter.

QuickAction Class
Use Apex to request and process actions on objects that allow custom fields, on objects that appear in a Chatter feed, or on objects
that are available globally.

Quiddity Enum
Specifies a Quiddity value used by the methods in the System.Request class

RemoteObjectController
Use `RemoteObjectController` to access the standard Visualforce Remote Objects operations in your Remote Objects
override methods.

Request Class
Contains methods to obtain the request ID and Quiddity value of the current Salesforce request.

ResetPasswordResult Class
Represents the result of a password reset.

RestContext Class
Contains the `RestRequest` and `RestResponse` objects.

RestRequest Class
Use the `System.RestRequest` class to access and pass request data in a RESTful Apex method.

RestResponse Class
Represents an object used to pass data from an Apex RESTful Web service method to an HTTP response.


Apex Reference Guide System Namespace

SandboxPostCopy Interface
To make your sandbox environment business ready, automate data manipulation or business logic tasks. Extend this interface and
add methods to perform post-copy tasks, then specify the class during sandbox creation.

Schedulable Interface
The class that implements this interface can be scheduled to run at different intervals.

SchedulableContext Interface
Represents the parameter type of a method in a class that implements the `Schedulable` interface and contains the scheduled
job ID. This interface is implemented internally by Apex.

Schema Class
Contains methods for obtaining schema describe information.

Search Class
Use the methods of the Search class to perform dynamic SOSL queries.

Security Class
Contains methods to securely implement Apex applications.

SelectOption Class
A `SelectOption` object specifies one of the possible values for a Visualforce `selectCheckboxes`, `selectList`, or
`selectRadio` component.

Set Class
Represents a collection of unique elements with no duplicate values.

Site Class
Use the `Site` Class to manage your sites. Change, reset, validate, and check the expiration of passwords. Create site users, person
accounts, and portal users. Get the admin email and ID. Get various URLs, the path prefix, the ID, the template, and the type of the
site. Log in to the site.

SObject Class
Contains methods for the sObject data type.

SObjectAccessDecision Class
Contains the results of a call to the Security.stripInaccessible method and methods to retrieve those results.

SoqlStubProvider Class
Contains a method to create a mock test class for handling SOQL query responses for Data Cloud data model objects (DMOs).

StaticResourceCalloutMock Class
Utility class used to specify a fake response for testing HTTP callouts.

String Class
Contains methods for the String primitive data type.

StubProvider Interface

`StubProvider` is a callback interface that you can use as part of the Apex stub API to implement a mocking framework. Use this
interface with the `Test.createStub()` method to create stubbed Apex objects for testing.

System Class
Contains methods for system operations, such as writing debug messages and scheduling jobs.

Test Class
Contains methods related to Apex tests.


### Apex Reference Guide AccessLevel Class

Time Class
Contains methods for the Time primitive data type.

TimeZone Class
Represents a time zone. Contains methods for creating a new time zone and obtaining time zone properties, such as the time zone
ID, offset, and display name.

Trigger Class
Use the `Trigger` class to access run-time context information in a trigger, such as the type of trigger or the list of sObject records
that the trigger operates on.

TriggerOperation Enum
System.TriggerOperation enum values are associated with trigger events.

Type Class
Contains methods for getting the Apex type that corresponds to an Apex class and for instantiating new types.

UninstallHandler Interface
Enables custom code to run after a managed package is uninstalled.

URL Class
Represents a uniform resource locator (URL) and provides access to parts of the URL. Enables access to the base URL used to access
your Salesforce org.

UserInfo Class
Contains methods for obtaining information about the context user.

UserManagement Class
Contains methods to manage end users, for example, to register their verification methods, verify their identity, or remove their
personal information.

UUID Class
Contains methods to randomly generate a version 4 universally unique identifier (UUID), compare UUIDs, and convert UUID instance
to a string.

Version Class
Use the Version methods to get the version of a first-generation managed package (1GP) or a migrated second-generation managed
package (2GP), and to compare package versions.

WebServiceCallout Class
Enables making callouts to SOAP operations on an external Web service. This class is used in the Apex stub class that is auto-generated
from a WSDL.

WebServiceMock Interface
Enables sending fake responses when testing Web service callouts of a class auto-generated from a WSDL.

XmlStreamReader Class Class
The `XmlStreamReader` class provides methods for forward, read-only access to XML data. You can pull data from XML or skip
unwanted events. You can parse nested XML content that’s up to 50 nodes deep.

XmlStreamWriter Class
The `XmlStreamWriter` class provides methods for writing XML data.

### AccessLevel Class

Defines the different modes, such as system or user mode, that Apex database operations execute in.


Apex Reference Guide AccessLevel Class

Namespace

System

Usage

By default, Apex code runs in system mode, which means that it runs with substantially elevated permissions over the user running the
code. In system mode, the object and field-level permissions of the current user are ignored, and the record sharing rules are controlled
[by the class sharing keywords. In user mode, the current user's object permissions, field-level security, and sharing rules are enforced.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Many of the DML methods of the `System.Database` and `System.Search` classes include an `accessLevel` parameter to
specify the execution mode.

Avoid specifying an `accessLevel` parameter in the same query as a `WITH SECURITY_ENFORCED` clause. Salesforce recommends
that you specify either system mode or user mode, and remove any redundant `WITH SECURITY_ENFORCED` clauses.

Example

If the user running this Apex code doesn't have write access to the Account object, the `Database.insert()` method returns an
error.

```
   List<Account> toInsert = new List<Account>{new Account(Name = 'Exciting New Account')};

   List<Database.SaveResult> sr = Database.insert(toInsert, AccessLevel.USER_MODE);

```

In contrast, this example shows the method running in system mode. The success of the insert doesn't depend on whether the user
running the Apex code has create access to the Account object.

```
   List<Account> toInsert = new List<Account>{new Account(Name = 'Exciting New Account')};

   List<Database.SaveResult> sr = Database.insert(toInsert, AccessLevel.SYSTEM_MODE);

```

IN THIS SECTION:

#### AccessLevel Methods

AccessLevel Properties

#### AccessLevel Methods The following are methods for AccessLevel .

IN THIS SECTION:

##### withPermissionSetId(permissionSetId)(Developer Preview)

Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.

##### **`withPermissionSetId(permissionSetId)(Developer Preview)`**

Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.


Apex Reference Guide AccessLevel Class

Note: Feature is available as a developer preview. Feature isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don’t implement functionality developed with these commands or
tools in a production environment. You can provide feedback and suggestions for the “Permission Sets with User Mode” feature
[in the Trailblazer Community.](https://trailhead.salesforce.com/trailblazer-community/groups/0F94S000000GvrW)

This feature is available in scratch orgs where the `ApexUserModeWithPermset` feature is enabled. If the feature isn’t enabled,
Apex code with this feature can be compiled but not executed.

Signature

```
   public System.AccessLevel withPermissionSetId(String permissionSetId)

```

Parameters

```
   permissionSetId
```

Type: String

Permissions in the specified permission set are enforced while running user-mode DML operations, in addition to the running user’s
permissions.

Return Value

Type: Access Level Class

Example: This example runs the `AccessLevel.withPermissionSetId()` method with the specified permission set
and inserts a custom object.

```
      @isTest

      public with sharing class ElevateUserModeOperations_Test {

        @isTest

        static void objectCreatePermViaPermissionSet() {

          Profile p = [SELECT Id FROM Profile WHERE Name='Minimum Access - Salesforce'];

           User u = new User(Alias = 'standt', Email='standarduser@testorg.com',

             EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',

             LocaleSidKey='en_US', ProfileId = p.Id,

             TimeZoneSidKey='America/Los_Angeles',

             UserName='standarduser' + DateTime.now().getTime() + '@testorg.com');

           System.runAs(u) {

             try {

               Database.insert(new Account(name='foo'), AccessLevel.User_mode);

               Assert.fail();

             } catch (SecurityException ex) {

               Assert.isTrue(ex.getMessage().contains('Account'));

             }

             //Get ID of previously created permission set named 'AllowCreateToAccount'

```


Apex Reference Guide AccessLevel Class

```
             Id permissionSetId = [Select Id from PermissionSet

               where Name = 'AllowCreateToAccount' limit 1].Id;

             Database.insert(new Account(name='foo'),

      AccessLevel.User_mode.withPermissionSetId(permissionSetId));

             // The elevated access level in not persisted to subsequent operations

             try {

               Database.insert(new Account(name='foo2'), AccessLevel.User_mode);

               Assert.fail();

             } catch (SecurityException ex) {

               Assert.isTrue(ex.getMessage().contains('Account'));

             }

           }

        }

      }

#### AccessLevel Properties The following are properties for AccessLevel .

```

IN THIS SECTION:

##### SYSTEM_MODE

Execution mode in which the the object and field-level permissions of the current user are ignored, and the record sharing rules are
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

##### USER_MODE

Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.

##### **`SYSTEM_MODE`**

Execution mode in which the the object and field-level permissions of the current user are ignored, and the record sharing rules are
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Signature

```
   public System.AccessLevel SYSTEM_MODE {get;}

```

Property Value

Type: System.AccessLevel

##### **`USER_MODE`**

Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.


### Apex Reference Guide AccessType Enum

Signature

```
   public System.AccessLevel USER_MODE {get;}

```

Property Value

Type: System.AccessLevel

### AccessType Enum

Specifies the access check type for the fields of an sObject.

Usage

Use these enum values for the `accessCheckType` parameter of the stripInaccessible method.

Enum Values

The following are the values of the `System.AccessType` enum.

**Value** **Description**

`CREATABLE` Check the fields of an sObject for create access.

`READABLE` Check the fields of an sObject for read access.

`UPDATABLE` Check the fields of an sObject for update access.

`UPSERTABLE` Check the fields of an sObject for both insert and update access.

### Address Class

Contains methods for accessing the component fields of address compound fields.

Namespace

System

Usage

Each of these methods is also equivalent to a read-only property. For each getter method, you can access the property using dot notation.
For example, `myAddress.getCity()` is equivalent to `myAddress.city` .

You can’t use dot notation to access compound fields’ subfields directly on the parent field. Instead, assign the parent field to a variable
### of type Address, and then access its components. For example, to access the City field in myAccount.BillingAddress,

do the following:

```
   Address addr = myAccount.BillingAddress;

   String acctCity = addr.City;

```


Apex Reference Guide Address Class

Important: “Address” in Salesforce can also refer to the Address standard object. When referencing the Address object in your
#### Apex code, always use Schema.Address instead of Address to prevent confusion with the standard Address compound

field. If referencing both the Address object and the Address standard field in the same snippet, you can differentiate between the
two by using `System.Address` for the field and `Schema.Address` for the object.

Example

```
   // Select and access Address fields.

   // Call the getDistance() method in different ways.

   Account[] records = [SELECT id, BillingAddress FROM Account LIMIT 10];

   for(Account acct : records) {

     Address addr = acct.BillingAddress;

     Double lat = addr.latitude;

     Double lon = addr.longitude;

     Location loc1 = Location.newInstance(30.1944,-97.6682);

     Double apexDist1 = addr.getDistance(loc1, 'mi');

     Double apexDist2 = loc1.getDistance(addr, 'mi');

     System.assertEquals(apexDist1, apexDist2);

     Double apexDist3 = Location.getDistance(addr, loc1, 'mi');

     System.assertEquals(apexDist2, apexDist3);

   }

```

IN THIS SECTION:

#### Address Methods Address Methods The following are methods for Address .

IN THIS SECTION:

getCity()
Returns the city field of this address.

getCountry()
Returns the text-only country/territory name component of this address.

getCountryCode()
Returns the country/territory code of this address if state and country/territory picklists are enabled in your organization. Otherwise,
returns `null` .

getDistance(toLocation, unit)
Returns the distance from this location to the specified location using the specified unit.

getGeocodeAccuracy()
When using geolocation data for a given address, this method gives you relative location information based on latitude and longitude
values. For example, you can find out if the latitude and longitude values point to the middle of the street, instead of the exact
address.

getLatitude()
Returns the latitude field of this address.


Apex Reference Guide Address Class

getLongitude()
Returns the longitude field of this address.

getPostalCode()
Returns the postal code of this address.

getState()
Returns the text-only state name component of this address.

getStateCode()
Returns the state code of this address if state and country/territory picklists are enabled in your organization. Otherwise, returns

`null` .

getStreet()
Returns the street field of this address.

##### getCity()

Returns the city field of this address.

Signature

```
   public String getCity()

```

Return Value

Type: String

##### getCountry()

Returns the text-only country/territory name component of this address.

Signature

```
   public String getCountry()

```

Return Value

Type: String

##### getCountryCode()

Returns the country/territory code of this address if state and country/territory picklists are enabled in your organization. Otherwise,
returns `null` .

Signature

```
   public String getCountryCode()

```

Return Value

Type: String


Apex Reference Guide Address Class

##### getDistance(toLocation, unit)

Returns the distance from this location to the specified location using the specified unit.

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

##### getGeocodeAccuracy()

When using geolocation data for a given address, this method gives you relative location information based on latitude and longitude
values. For example, you can find out if the latitude and longitude values point to the middle of the street, instead of the exact address.

Signature

```
   public String getGeocodeAccuracy()

```

Return Value

Type: String

##### The getGeocodeAccuracy() return value tells you more about the location at a latitude and longitude for a given address. For

example, `Zip` means the latitude and longitude point to the center of the zip code area, in case a match for an exact street address
can’t be found.


Apex Reference Guide Address Class

Geocodes are added only for some standard addresses.

**•** `Billing Address` on accounts

**•** `Shipping Address` on accounts

**•** `Mailing Address` on contacts

**•** `Address` on leads

Person accounts are not supported.

Note: For `getGeocodeAccuracy()` to work, set up and activate the geocode data integration rules for the related address
fields.

##### getLatitude()

Returns the latitude field of this address.

Signature

```
   public Double getLatitude()

```

Return Value

Type: Double

##### getLongitude()

Returns the longitude field of this address.

Signature

```
   public Double getLongitude()

```

Return Value

Type: Double

##### getPostalCode()

Returns the postal code of this address.


### Apex Reference Guide Answers Class

Signature

```
   public String getPostalCode()

```

Return Value

Type: String

##### getState()

Returns the text-only state name component of this address.

Signature

```
   public String getState()

```

Return Value

Type: String

##### getStateCode()

Returns the state code of this address if state and country/territory picklists are enabled in your organization. Otherwise, returns `null` .

Signature

```
   public String getStateCode()

```

Return Value

Type: String

##### getStreet()

Returns the street field of this address.

Signature

```
   public String getStreet()

```

Return Value

Type: String

### Answers Class

Represents zone answers.

Namespace

System


Apex Reference Guide Answers Class

Usage

Answers is a feature that enables users to ask questions and have zone members post replies. Members can then vote on the helpfulness
of each reply, and the person who asked the question can mark one reply as the best answer.

For more information on answers, see “Answers Overview” in the Salesforce online help.

Example

The following example finds questions in an internal zone that have similar titles as a new question:

```
   public class FindSimilarQuestionController {

     public static void test() {

     // Instantiate a new question

     Question question = new Question ();

     // Specify a title for the new question

     question.title = 'How much vacation time do full-time employees get?';

     // Specify the communityID (INTERNAL_COMMUNITY) in which to find similar questions.

     Community community = [ SELECT Id FROM Community WHERE Name = 'INTERNAL_COMMUNITY' ];

     question.communityId = community.id;

     ID[] results = Answers.findSimilar(question);

     }

   }

```

The following example marks a reply as the best reply:

```
   ID questionId = [SELECT Id FROM Question WHERE Title = 'Testing setBestReplyId' LIMIT

   1].Id;

   ID replyID = [SELECT Id FROM Reply WHERE QuestionId = :questionId LIMIT 1].Id;

   Answers.setBestReply(questionId,replyId);

#### Answers Methods The following are methods for Answers . All methods are static.

```

IN THIS SECTION:

##### findSimilar(yourQuestion)

Returns a list of similar questions based on the title of the specified question.

setBestReply(questionId, replyId)
Sets the specified reply for the specified question as the best reply. Because a question can have multiple replies, setting the best
reply helps users quickly identify the reply that contains the most helpful information.

##### findSimilar(yourQuestion)

Returns a list of similar questions based on the title of the specified question.


### Apex Reference Guide ApexPages Class

Signature

```
   public static ID[] findSimilar(Question yourQuestion)

```

Parameters

```
   yourQuestion
```

Type: Question

Return Value

Type: ID[]

Usage

Each `findSimilar` call counts against the SOSL statements governor limit allowed for the process.

##### setBestReply(questionId, replyId)

Sets the specified reply for the specified question as the best reply. Because a question can have multiple replies, setting the best reply
helps users quickly identify the reply that contains the most helpful information.

Signature

```
   public static Void setBestReply(String questionId, String replyId)

```

Parameters

```
   questionId
```

Type: String

```
   replyId
```

Type: String

Return Value

Type: Void

### ApexPages Class Use ApexPages to add and check for messages associated with the current page, as well as to reference the current page.

Namespace

System

Usage

### In addition, ApexPages is used as a namespace for the PageReference Class and the Message Class.


Apex Reference Guide ApexPages Class

#### ApexPages Methods The following are methods for ApexPages . All are instance methods.

IN THIS SECTION:

##### addMessage(message)

Add a message to the current page context.

##### addMessages(exceptionThrown)

Adds a list of messages to the current page context based on a thrown exception.

currentPage()
Returns the current page's PageReference.

getMessages()
Returns a list of the messages associated with the current context.

hasMessages()
Returns `true` if there are messages associated with the current context, `false` otherwise.

hasMessages(severity)
Returns `true` if messages of the specified severity exist, `false` otherwise.

##### addMessage(message)

Add a message to the current page context.

Signature

```
   public Void addMessage(ApexPages.Message message)

```

Parameters

**message**
Type: ApexPages.Message

Return Value

Type: Void

##### addMessages(exceptionThrown)

Adds a list of messages to the current page context based on a thrown exception.

Signature

```
   public Void addMessages(Exception exceptionThrown)

```

Parameters

```
   exceptionThrown
```

Type: Exception


Apex Reference Guide ApexPages Class

Return Value

Type: Void

##### currentPage()

Returns the current page's PageReference.

Signature

```
   public System.PageReference currentPage()

```

Return Value

Type: System.PageReference

Example

This code segment returns the id parameter of the current page.

```
   public MyController() {

      account = [

        SELECT Id, Name, Site

        FROM Account

        WHERE Id =

           :ApexPages.currentPage().

           getParameters().

           get('id')

      ];

   }

##### getMessages()

```

Returns a list of the messages associated with the current context.

Signature

```
   public ApexPages.Message[] getMessages()

```

Return Value

Type: ApexPages.Message[]

##### hasMessages()

Returns `true` if there are messages associated with the current context, `false` otherwise.

Signature

```
   public Boolean hasMessages()

```


### Apex Reference Guide Approval Class

Return Value

Type: Boolean

##### hasMessages(severity)

Returns `true` if messages of the specified severity exist, `false` otherwise.

Signature

```
   public Boolean hasMessages(ApexPages.Severity severity)

```

Parameters

```
   sev
```

Type: ApexPages.Severity

Return Value

Type: Boolean

### Approval Class

Contains methods for processing approval requests and setting approval-process locks and unlocks on records.

Namespace

System

Usage

Salesforce admins can edit locked records. Depending on your approval process configuration settings, an assigned approver can also
edit locked records. Locks and unlocks that are set programmatically use the same record editability settings as other approval-process
locks and unlocks.

Record locks and unlocks are treated as DML. They’re blocked before a callout, they count toward your DML limits, and if a failure occurs,
they’re rolled back along with the rest of your transaction. To change this rollback behavior, use an `allOrNone` parameter.

Approval is also used as a namespace for the `ProcessRequest` and `ProcessResult` classes.

SEE ALSO:

[Approval Process Considerations](https://help.salesforce.com/HTViewHelpDoc?id=approvals_considerations.htm&language=en_US)

#### Approval Methods

### The following are methods for Approval . All methods are static.

IN THIS SECTION:

isLocked(id)
Returns `true` if the record with the ID `id` is locked, or `false` if it’s not.


Apex Reference Guide Approval Class

isLocked(ids)
Returns a map of record IDs and their lock statuses. If the record is locked the status is `true` . If the record is not locked the status
is `false` .

isLocked(sobject)
Returns `true` if the `sobject` record is locked, or `false` if it’s not.

isLocked(sobjects)
Returns a map of record IDs to lock statuses. If the record is locked the status is `true` . If the record is not locked the status is `false` .

lock(recordId)
Locks an object, and returns the lock results.

lock(recordIds)
Locks a set of objects, and returns the lock results, including failures.

lock(recordToLock)
Locks an object, and returns the lock results.

lock(recordsToLock)
Locks a set of objects, and returns the lock results, including failures.

lock(recordId, allOrNothing)
Locks an object, with the option for partial success, and returns the lock result.

lock(recordIds, allOrNothing)
Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

lock(recordToLock, allOrNothing)
Locks an object, with the option for partial success, and returns the lock result.

lock(recordsToLock, allOrNothing)
Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

process(approvalRequest)
Submits a new approval request and approves or rejects existing approval requests.

process(approvalRequest, allOrNone)
Submits a new approval request and approves or rejects existing approval requests.

process(approvalRequests)
Submits a list of new approval requests, and approves or rejects existing approval requests.

process(approvalRequests, allOrNone)
Submits a list of new approval requests, and approves or rejects existing approval requests.

unlock(recordId)
Unlocks an object, and returns the unlock results.

unlock(recordIds)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordToUnlock)
Unlocks an object, and returns the unlock results.

unlock(recordsToUnlock)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordId, allOrNothing)
Unlocks an object, with the option for partial success, and returns the unlock result.


Apex Reference Guide Approval Class

unlock(recordIds, allOrNothing)
Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

unlock(recordToUnlock, allOrNothing)
Unlocks an object, with the option for partial success, and returns the unlock result.

unlock(recordsToUnlock, allOrNothing)
Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

##### isLocked(id)

Returns `true` if the record with the ID `id` is locked, or `false` if it’s not.

Signature

```
   public static Boolean isLocked(Id id)

```

Parameters

```
   id
```

Type: Id

The ID of the record whose lock or unlock status is in question.

Return Value

Type: Boolean

##### isLocked(ids)

Returns a map of record IDs and their lock statuses. If the record is locked the status is `true` . If the record is not locked the status is

`false` .

Signature

```
   public static Map<Id,Boolean> isLocked(List<Id> ids)

```

Parameters

```
   ids
```

Type: List<Id>

The IDs of the records whose lock or unlock statuses are in question.

Return Value

Type: Map<Id,Boolean>

##### isLocked(sobject)

Returns `true` if the `sobject` record is locked, or `false` if it’s not.


Apex Reference Guide Approval Class

Signature

```
   public static Boolean isLocked(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

The record whose lock or unlock status is in question.

Return Value

Type: Boolean

##### isLocked(sobjects)

Returns a map of record IDs to lock statuses. If the record is locked the status is `true` . If the record is not locked the status is `false` .

Signature

```
   public static Map<Id,Boolean> isLocked(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

The records whose lock or unlock statuses are in question.

Return Value

Type: Map<Id,Boolean>

##### lock(recordId)

Locks an object, and returns the lock results.

Signature

```
   public static Approval.LockResult lock(Id recordId)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

Return Value

Type: Approval.LockResult


Apex Reference Guide Approval Class

##### lock(recordIds)

Locks a set of objects, and returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<Id> ids)

```

Parameters

```
   ids
```

Type: List<Id>

IDs of the objects to lock.

Return Value

Type: List<Approval.LockResult>

##### lock(recordToLock)

Locks an object, and returns the lock results.

Signature

```
   public static Approval.LockResult lock(SObject recordToLock)

```

Parameters

```
   recordToLock
```

Type: SObject

Return Value

Type: Approval.LockResult

##### lock(recordsToLock)

Locks a set of objects, and returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<SObject> recordsToLock)

```

Parameters

```
   recordsToLock
```

Type: List<SObject>

Return Value

Type: List<Approval.LockResult>


Apex Reference Guide Approval Class

##### lock(recordId, allOrNothing)

Locks an object, with the option for partial success, and returns the lock result.

Signature

```
   public static Approval.LockResult lock(Id recordId, Boolean allOrNothing)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.LockResult

##### lock(recordIds, allOrNothing)

Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<Id> recordIds, Boolean allOrNothing)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.LockResult>

##### lock(recordToLock, allOrNothing)

Locks an object, with the option for partial success, and returns the lock result.


Apex Reference Guide Approval Class

Signature

```
   public static Approval.LockResult lock(SObject recordToLock, Boolean allOrNothing)

```

Parameters

```
   recordToLock
```

Type: SObject

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.LockResult

##### lock(recordsToLock, allOrNothing)

Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<SObject> recordsToLock, Boolean

   allOrNothing)

```

Parameters

```
   recordsToLock
```

Type: List<SObject>

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.LockResult>

##### process(approvalRequest)

Submits a new approval request and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult process(Approval.ProcessRequest approvalRequest)

```


Apex Reference Guide Approval Class

Parameters

```
   approvalRequest
```

Type: Approval.ProcessRequest

Return Value

Type: Approval.ProcessResult

Example

```
   // Insert an account

   Account a = new Account(Name='Test',

                annualRevenue=100.0);

   insert a;

   // Create an approval request for the account

   Approval.ProcessSubmitRequest req1 =

       new Approval.ProcessSubmitRequest();

   req1.setObjectId(a.id);

   // Submit the approval request for the account

   Approval.ProcessResult result =

               Approval.process(req1);

##### process(approvalRequest, allOrNone)

```

Submits a new approval request and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult process(Approval.ProcessRequest approvalRequest,

   Boolean allOrNone)

```

Parameters

```
   approvalRequest
```

Approval.ProcessRequest

```
   allOrNone
```

Type: Boolean

The optional _`allOrNone`_ parameter specifies whether the operation allows for partial success. If you specify `false` for this
parameter and an approval fails, the remainder of the approval processes can still succeed.

Return Value

Approval.ProcessResult


Apex Reference Guide Approval Class

##### process(approvalRequests)

Submits a list of new approval requests, and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult [] process(Approval.ProcessRequest[]

   approvalRequests)

```

Parameters

```
   approvalRequests
```

Approval.ProcessRequest []

Return Value

Approval.ProcessResult []

##### process(approvalRequests, allOrNone)

Submits a list of new approval requests, and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult [] process(Approval.ProcessRequest[]

   approvalRequests, Boolean allOrNone)

```

Parameters

```
   approvalRequests
```

Approval.ProcessRequest []

```
   allOrNone
```

Type: Boolean

The optional _`allOrNone`_ parameter specifies whether the operation allows for partial success. If you specify `false` for this
parameter and an approval fails, the remainder of the approval processes can still succeed.

Return Value

Approval.ProcessResult []

##### unlock(recordId)

Unlocks an object, and returns the unlock results.

Signature

```
   public static Approval.UnlockResult unlock(Id recordId)

```


Apex Reference Guide Approval Class

Parameters

```
   recordId
```

Type: Id

ID of the object to unlock.

Return Value

Type: Approval.UnlockResult

##### unlock(recordIds)

Unlocks a set of objects, and returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<Id> recordIds)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to unlock.

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordToUnlock)

Unlocks an object, and returns the unlock results.

Signature

```
   public static Approval.UnlockResult unlock(SObject recordToUnlock)

```

Parameters

```
   recordToUnlock
```

Type: SObject

Return Value

Type: Approval.UnlockResult

##### unlock(recordsToUnlock)

Unlocks a set of objects, and returns the unlock results, including failures.


Apex Reference Guide Approval Class

Signature

```
   public static List<Approval.UnlockResult> unlock(List<SObject> recordsToUnlock)

```

Parameters

```
   recordsToUnlock
```

Type: List<SObject>

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordId, allOrNothing)

Unlocks an object, with the option for partial success, and returns the unlock result.

Signature

```
   public static Approval.UnlockResult unlock(Id recordId, Boolean allOrNothing)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.UnlockResult

##### unlock(recordIds, allOrNothing)

Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<Id> recordIds, Boolean

   allOrNothing)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to unlock.


Apex Reference Guide Approval Class

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordToUnlock, allOrNothing)

Unlocks an object, with the option for partial success, and returns the unlock result.

Signature

```
   public static Approval.UnlockResult unlock(SObject recordToUnlock, Boolean allOrNothing)

```

Parameters

```
   recordToUnlock
```

Type: SObject

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.UnlockResult

##### unlock(recordsToUnlock, allOrNothing)

Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<SObject> recordsToUnlock, Boolean

   allOrNothing)

```

Parameters

```
   recordsToUnlock
```

Type: List<SObject>

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.


### Apex Reference Guide Assert Class

Return Value

Type: List<Approval.UnlockResult>

### Assert Class

Contains methods to assert various conditions with test methods, such as whether two values are the same, a condition is true, or a
variable is null.

Namespace

System

#### Assert Methods

### The following are methods for Assert .

IN THIS SECTION:

areEqual(expected, actual, msg)
Asserts that the first two arguments are the same.

areEqual(expected, actual)
Asserts that the two arguments are the same.

areNotEqual(notExpected, actual, msg)
Asserts that the first two arguments aren’t the same.

areNotEqual(notExpected, actual)
Asserts that the two arguments aren’t the same.

fail(msg)
Immediately return a fatal error that causes code execution to halt.

fail()
Immediately return a fatal error that causes code execution to halt.

isFalse(condition, msg)
Asserts that the specified condition is `false` .

isFalse(condition)
Asserts that the specified condition is `false` .

isInstanceOfType(instance, expectedType, msg)
Asserts that the instance is of the specified type.

isInstanceOfType(instance, expectedType)
Asserts that the instance is of the specified type.

isNotInstanceOfType(instance, notExpectedType, msg)
Asserts that the instance isn’t of the specified type.

isNotInstanceOfType(instance, notExpectedType)
Asserts that the instance isn’t of the specified type.


Apex Reference Guide Assert Class

isNotNull(value, msg)
Asserts that the value isn’t null.

isNotNull(value)
Asserts that the value isn’t null.

isNull(value, msg)
Asserts that the value is null.

isNull(value)
Asserts that the value is null.

isTrue(condition, msg)
Asserts that the specified condition is `true` .

isTrue(condition)
Asserts that the specified condition is `true` .

##### areEqual(expected, actual, msg)

Asserts that the first two arguments are the same.

Signature

```
   public static void areEqual(Object expected, Object actual, String msg)

```

Parameters

```
   expected
```

Type: Object

Expected value.

```
   actual
```

Type: Object

Actual value.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the first two arguments aren't the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areEqual('cde', sub, 'Expected characters after first two'); // Succeeds

##### areEqual(expected, actual)

```

Asserts that the two arguments are the same.

Signature

```
   public static void areEqual(Object expected, Object actual)

```

Parameters

```
   expected
```

Type: Object

Expected value.

```
   actual
```

Type: Object

Actual value.

Return Value

Type: void

Usage

If the two arguments aren't the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areEqual('cde', sub); // Succeeds

##### areNotEqual(notExpected, actual, msg)

```

Asserts that the first two arguments aren’t the same.

Signature

```
   public static void areNotEqual(Object notExpected, Object actual, String msg)

```

Parameters

```
   notExpected
```

Type: Object

Value that’s not expected.


Apex Reference Guide Assert Class

```
   actual
```

Type: Object

Actual value.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the first two arguments are the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areNotEqual('xyz', sub, 'Characters not expected after first two'); // Succeeds

##### areNotEqual(notExpected, actual)

```

Asserts that the two arguments aren’t the same.

Signature

```
   public static void areNotEqual(Object notExpected, Object actual)

```

Parameters

```
   notExpected
```

Type: Object

Value that’s not expected.

```
   actual
```

Type: Object

Actual value.

Return Value

Type: void

Usage

If the two arguments are the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areNotEqual('xyz', sub); // Succeeds

##### fail(msg)

```

Immediately return a fatal error that causes code execution to halt.

Signature

```
   public static void fail(String msg)

```

Parameters

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

Commonly used in a try/catch block test case where an exception is expected to be thrown. You can’t, however, catch the assertion
failure in the try/catch block even though it’s logged as an exception.

Example

```
   // test case where exception is expected

   try {

      SomeClass.methodUnderTest();

      Assert.fail('DmlException Expected');

   } catch (DmlException ex) {

      // Add assertions here about the expected exception

   }

##### fail()

```

Immediately return a fatal error that causes code execution to halt.

Signature

```
   public static void fail()

```

Return Value

Type: void


Apex Reference Guide Assert Class

Usage

Commonly used in a try/catch block test case where an exception is expected to be thrown. You can’t, however, catch the assertion
failure in the try/catch block even though it’s logged as an exception.

Example

```
   // test case where exception is expected

   try {

      SomeClass.methodUnderTest();

      Assert.fail();

   } catch (DmlException ex) {

      // Add assertions here about the expected exception

   }

##### isFalse(condition, msg)

```

Asserts that the specified condition is `false` .

Signature

```
   public static void isFalse(Boolean condition, String msg)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `false` .

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the condition is `true`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsCode = 'Salesforce'.contains('code');

   Assert.isFalse(containsCode, 'No code'); // Assertion succeeds

##### isFalse(condition)

```

Asserts that the specified condition is `false` .


Apex Reference Guide Assert Class

Signature

```
   public static void isFalse(Boolean condition)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `false` .

Return Value

Type: void

Usage

If the condition is `true`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsCode = 'Salesforce'.contains('code');

   Assert.isFalse(containsCode); // Assertion succeeds

##### isInstanceOfType(instance, expectedType, msg)

```

Asserts that the instance is of the specified type.

Signature

```
   public static void isInstanceOfType(Object instance, System.Type expectedType, String

   msg)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   expectedType
```

Type: System.Type on page 4243

Expected type.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void


Apex Reference Guide Assert Class

Usage

If the instance isn't of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class); // Succeeds

##### isInstanceOfType(instance, expectedType)

```

Asserts that the instance is of the specified type.

Signature

```
   public static void isInstanceOfType(Object instance, System.Type expectedType)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   expectedType
```

Type: System.Type on page 4243

Expected type.

Return Value

Type: void

Usage

If the instance isn't of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class); // Succeeds

   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class, 'Expected type.'); // Succeeds

##### isNotInstanceOfType(instance, notExpectedType, msg)

```

Asserts that the instance isn’t of the specified type.


Apex Reference Guide Assert Class

Signature

```
   public static void isNotInstanceOfType(Object instance, System.Type notExpectedType,

   String msg)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   notExpectedType
```

Type: System.Type on page 4243

Type that's not expected.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the instance is of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Contact con = new Contact();

   Assert.isNotInstanceOfType(con, Account.class, 'Not expected type'); // Succeeds

##### isNotInstanceOfType(instance, notExpectedType)

```

Asserts that the instance isn’t of the specified type.

Signature

```
   public static void isNotInstanceOfType(Object instance, System.Type notExpectedType)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   notExpectedType
```

Type: System.Type on page 4243

Type that's not expected.


Apex Reference Guide Assert Class

Return Value

Type: void

Usage

If the instance is of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Contact con = new Contact();

   Assert.isNotInstanceOfType(con, Account.class); // Succeeds

##### isNotNull(value, msg)

```

Asserts that the value isn’t null.

Signature

```
   public static void isNotNull(Object value, String msg)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s not null.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the value is null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = 'value';

   Assert.isNotNull(myString, 'myString should not be null'); // Succeeds

##### isNotNull(value)

```

Asserts that the value isn’t null.


Apex Reference Guide Assert Class

Signature

```
   public static void isNotNull(Object value)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s not null.

Return Value

Type: void

Usage

If the value is null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = 'value';

   Assert.isNotNull(myString); // Succeeds

##### isNull(value, msg)

```

Asserts that the value is null.

Signature

```
   public static void isNull(Object value, String msg)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s null.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the value isn't null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String myString = null;

   Assert.isNull(myString, 'String should be null'); // Succeeds

##### isNull(value)

```

Asserts that the value is null.

Signature

```
   public static void isNull(Object value)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s null.

Return Value

Type: void

Usage

If the value isn't null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = null;

   Assert.isNull(myString); // Succeeds

##### isTrue(condition, msg)

```

Asserts that the specified condition is `true` .

Signature

```
   public static void isTrue(Boolean condition, String msg)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `true` .

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.


### Apex Reference Guide AsyncInfo Class

Return Value

Type: void

Usage

If the specified condition is `false`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsForce = 'Salesforce'.contains('force');

   Assert.isTrue(containsForce, 'Contains force'); // Assertion succeeds

##### isTrue(condition)

```

Asserts that the specified condition is `true` .

Signature

```
   public static void isTrue(Boolean condition)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `true` .

Return Value

Type: void

Usage

If the specified condition is `false`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsForce = 'Salesforce'.contains('force');

   Assert.isTrue(containsForce); // Assertion succeeds

### AsyncInfo Class

```

Provides methods to get the current stack depth, maximum stack depth, and the minimum queueable delay for Queueable transactions,
and to determine if maximum stack depth is set.


Apex Reference Guide AsyncInfo Class

Namespace

System

IN THIS SECTION:

#### AsyncInfo Methods AsyncInfo Methods The following are methods for AsyncInfo .

IN THIS SECTION:

##### getCurrentQueueableStackDepth()

Get the current queueable stack depth for queueable transactions.

##### getMaximumQueueableStackDepth()

Get the maximum queueable stack depth for queueable transactions.

getMinimumQueueableDelayInMinutes()
Get the minimum queueable delay for queueable transactions (in minutes).

hasMaxStackDepth()
Determine if maximum stack depth is set for your queueable requests.

##### **`getCurrentQueueableStackDepth()`**

Get the current queueable stack depth for queueable transactions.

Signature

```
   public static Integer getCurrentQueueableStackDepth()

```

Return Value

Type: Integer

##### **`getMaximumQueueableStackDepth()`**

Get the maximum queueable stack depth for queueable transactions.

Signature

```
   public static Integer getMaximumQueueableStackDepth()

```

Return Value

Type: Integer


### Apex Reference Guide AsyncOptions Class

##### **`getMinimumQueueableDelayInMinutes()`**

Get the minimum queueable delay for queueable transactions (in minutes).

Signature

```
   public static Integer getMinimumQueueableDelayInMinutes()

```

Return Value

Type: Integer

Returns null if no delay is defined.

##### **`hasMaxStackDepth()`**

Determine if maximum stack depth is set for your queueable requests.

Signature

```
   public static Boolean hasMaxStackDepth()

```

Return Value

Type: Boolean

### AsyncOptions Class

Contains maximum stack depths for queueable transactions and the minimum queueable delay in minutes. Passed as parameter to the
`System.enqueueJob()` method to define a unique queueable job signature, the maximum stack depth for queueable transactions
and the minimum queueable delay in minutes.

Namespace

System

IN THIS SECTION:

#### AsyncOptions Properties

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)

#### AsyncOptions Properties

### The following are properties for AsyncOptions .


### Apex Reference Guide Blob Class

IN THIS SECTION:

##### DuplicateSignature

A unique signature for a Queueable job.

##### MaximumQueueableStackDepth

Maximum stack depth for queueable transactions.

##### MinimumQueueableDelayInMinutes

Minimum queueable delay for queueable transactions.

##### **`DuplicateSignature`**

A unique signature for a Queueable job.

Signature

```
   public System.QueueableDuplicateSignature DuplicateSignature {get; set;}

```

Property Value

Type: QueueableDuplicateSignature Class

##### **`MaximumQueueableStackDepth`**

Maximum stack depth for queueable transactions.

Signature

```
   public Integer MaximumQueueableStackDepth {get; set;}

```

Property Value

Type: Integer

##### **`MinimumQueueableDelayInMinutes`**

Minimum queueable delay for queueable transactions.

Signature

```
   public Integer MinimumQueueableDelayInMinutes {get; set;}

```

Property Value

Type: Integer

### Blob Class

Contains methods for the Blob primitive data type.


Apex Reference Guide Blob Class

Namespace

System

Usage

Salesforce supports Blob manipulation only with Apex class methods that are supplied by Salesforce. For more information on Blobs,
[see Primitive Data Types.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Blob Methods The following are methods for Blob .

IN THIS SECTION:

##### size()

Returns the number of bytes in the Blob.

##### toPdf(stringToConvert)

Creates a binary object out of the given string, encoding it as a PDF file.

toString()
Casts the Blob into a String.

valueOf(stringToBlob)
Casts the specified String to a Blob.

##### size()

Returns the number of bytes in the Blob.

Signature

```
   public Integer size()

```

Return Value

Type: Integer

Example

```
   String myString = 'StringToBlob';

   Blob myBlob = Blob.valueof(myString);

   Integer size = myBlob.size();

##### toPdf(stringToConvert)

```

Creates a binary object out of the given string, encoding it as a PDF file.

Signature

```
   public static Blob toPdf(String stringToConvert)

```


Apex Reference Guide Blob Class

Parameters

```
   stringToConvert
```

Type: String

Return Value

Type: Blob

Usage

`Blob.toPDF(stringToConvert)` works with any string value. Since the Spring ’26 release, `Blob.toPDF()` uses the same
[PDF rendering service as Visualforce. See Render a Visualforce Page as a PDF File for details, including considerations and limitations for](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_output_pdf_renderas.htm)
rendering PDF files.

The Visualforce PDF rendering service expands the range of fonts available, and includes a multibyte-capable font. The default font is
`sans-serif` [. See Fonts Available When Using Visualforce PDF Rendering.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_output_pdf_supported_fonts.htm)

Example

```
   String pdfContent = 'This is a test string';

   Account a = new account(name = 'test');

   insert a;

   Attachment attachmentPDF = new Attachment();

   attachmentPdf.parentId = a.id;

   attachmentPdf.name = a.name + '.pdf';

   attachmentPdf.body = Blob.toPDF(pdfContent);

   insert attachmentPDF;

##### toString()

```

Casts the Blob into a String.

Signature

```
   public String toString()

```

Return Value

Type: String

Example

```
   String myString = 'StringToBlob';

   Blob myBlob = Blob.valueof(myString);

   System.assertEquals('StringToBlob', myBlob.toString());

##### valueOf(stringToBlob)

```

Casts the specified String to a Blob.


### Apex Reference Guide Boolean Class

Signature

```
   public static Blob valueOf(String stringToBlob)

```

Parameters

```
   stringToBlob
```

Type: String

Return Value

Type: Blob

Example

```
   String myString = 'StringToBlob';

   Blob myBlob = Blob.valueof(myString);

### Boolean Class

```

Contains methods for the Boolean primitive data type.

Namespace

System

#### Boolean Methods

### The following are methods for Boolean . All methods are static.

IN THIS SECTION:

##### valueOf(stringToBoolean)

Converts the specified string to a Boolean value and returns `true` if the specified string value is `true` . Otherwise, returns `false` .

valueOf(fieldValue)
Converts the specified object to a Boolean value. Use this method to convert a history tracking field value or an object that represents
a Boolean value.

##### valueOf(stringToBoolean)

Converts the specified string to a Boolean value and returns `true` if the specified string value is `true` . Otherwise, returns `false` .

Signature

```
   public static Boolean valueOf(String stringToBoolean)

```


Apex Reference Guide Boolean Class

Parameters

```
   stringToBoolean
```

Type: String

Return Value

Type: Boolean

Usage

If the specified argument is null, this method throws an exception.

Example

```
   Boolean b = Boolean.valueOf('true');

   System.assertEquals(true, b);

##### valueOf(fieldValue)

```

Converts the specified object to a Boolean value. Use this method to convert a history tracking field value or an object that represents
a Boolean value.

Signature

```
   public static Boolean valueOf(Object fieldValue)

```

Parameters

```
   fieldValue
```

Type: Object

Return Value

Type: Boolean

Usage

Use this method with the `OldValue` or `NewValue` fields of history sObjects, such as `AccountHistory`, when the field type
corresponds to a Boolean type, like a checkbox field.

Example

```
   List<AccountHistory> ahlist =

      [SELECT Field,OldValue,NewValue FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'IsPlatinum__c') {

       Boolean oldValue = Boolean.valueOf(ah.OldValue);

       Boolean newValue = Boolean.valueOf(ah.NewValue);

```


### Apex Reference Guide BusinessHours Class

```
     }

   }

### BusinessHours Class Use the BusinessHours methods to set the business hours at which your customer support team operates.

```

Namespace

System

#### BusinessHours Methods

### The following are methods for BusinessHours . All methods are static.

IN THIS SECTION:

##### add(businessHoursId, startDate, intervalMilliseconds)

Adds an interval of time from a start Datetime traversing business hours only. Returns the result Datetime in the local time zone.

addGmt(businessHoursId, startDate, intervalMilliseconds)
Adds an interval of milliseconds from a start Datetime traversing business hours only. Returns the result Datetime in GMT.

diff(businessHoursId, startDate, endDate)
Returns the difference in milliseconds between a start and end Datetime based on a specific set of business hours.

isWithin(businessHoursId, targetDate)
Returns `true` if the specified target date occurs within business hours. Holidays are included in the calculation.

nextStartDate(businessHoursId, targetDate)
Starting from the specified target date, returns the next date when business hours are open. If the specified target date falls within
business hours, this target date is returned.

##### add(businessHoursId, startDate, intervalMilliseconds)

Adds an interval of time from a start Datetime traversing business hours only. Returns the result Datetime in the local time zone.

Signature

```
   public static Datetime add(String businessHoursId, Datetime startDate, Long

   intervalMilliseconds)

```

Parameters

```
   businessHoursId
```

Type: String

```
   startDate
```

Type: Datetime

```
   intervalMilliseconds
```

Type: Long


Apex Reference Guide BusinessHours Class

Interval value should be provided in milliseconds, however time precision smaller than one minute is ignored.

Return Value

Type: Datetime

##### addGmt(businessHoursId, startDate, intervalMilliseconds)

Adds an interval of milliseconds from a start Datetime traversing business hours only. Returns the result Datetime in GMT.

Signature

```
   public static Datetime addGmt(String businessHoursId, Datetime startDate, Long

   intervalMilliseconds)

```

Parameters

```
   businessHoursId
```

Type: String

```
   startDate
```

Type: Datetime

```
   intervalMilliseconds
```

Type: Long

Return Value

Type: Datetime

##### diff(businessHoursId, startDate, endDate)

Returns the difference in milliseconds between a start and end Datetime based on a specific set of business hours.

Signature

```
   public static Long diff(String businessHoursId, Datetime startDate, Datetime endDate)

```

Parameters

```
   businessHoursId
```

Type: String

```
   startDate
```

Type: Datetime

```
   endDate
```

Type: Datetime

Return Value

Type: Long


Apex Reference Guide BusinessHours Class

##### isWithin(businessHoursId, targetDate)

Returns `true` if the specified target date occurs within business hours. Holidays are included in the calculation.

Signature

```
   public static Boolean isWithin(String businessHoursId, Datetime targetDate)

```

Parameters

```
   businessHoursId
```

Type: String

The business hours ID.

```
   targetDate
```

Type: Datetime

The date to verify.

Return Value

Type: Boolean

Example

The following example finds whether a given time is within the default business hours.

```
   // Get the default business hours

   BusinessHours bh = [SELECT Id FROM BusinessHours WHERE IsDefault=true];

   // Create Datetime on May 28, 2013 at 1:06:08 AM in the local timezone.

   Datetime targetTime = Datetime.newInstance(2013, 5, 28, 1, 6, 8);

   // Find whether the time is within the default business hours

   Boolean isWithin= BusinessHours.isWithin(bh.id, targetTime);

##### nextStartDate(businessHoursId, targetDate)

```

Starting from the specified target date, returns the next date when business hours are open. If the specified target date falls within
business hours, this target date is returned.

Signature

```
   public static Datetime nextStartDate(String businessHoursId, Datetime targetDate)

```

Parameters

```
   businessHoursId
```

Type: String

The business hours ID.

```
   targetDate
```

Type: Datetime


### Apex Reference Guide CallbackStatus Enum

The date used as a start date to obtain the next date.

Return Value

Type: Datetime

Example

The following example finds the next date starting from the target date when business hours reopens. If the target date is within the
given business hours, the target date is returned. The returned time is in the local time zone.

```
   // Get the default business hours

   BusinessHours bh = [SELECT Id FROM BusinessHours WHERE IsDefault=true];

   // Create Datetime on May 28, 2013 at 1:06:08 AM in the local timezone.

   Datetime targetTime = Datetime.newInstance(2013, 5, 28, 1, 6, 8);

   // Starting from the targetTime, find the next date when business hours reopens. Return

   the target time.

   // if it is within the business hours. The returned time will be in the local time zone

   Datetime nextStart = BusinessHours.nextStartDate(bh.id, targetTime);

### CallbackStatus Enum

```

Specifies the status of asynchronous requests to an external system.

Enum Values

The following are the values of the `System.CallbackStatus` enum.

**Value** **Description**

CANCELLED The asynchronous operation has been cancelled.

COMPLETED The asynchronous operation has been completed.

PENDING The asynchronous operation is in progress.

TIMED_OUT The asynchronous operation has timed out.

### Callable Interface

Enables developers to use a common interface to build loosely coupled integrations between Apex classes or triggers, even for code in
separate packages. Agreeing upon a common interface enables developers from different companies or different departments to build
upon one another’s solutions. Implement this interface to enable the broader community, which might have different solutions than
the ones you had in mind, to extend your code’s functionality.

Note: This interface is not an analog of the Java Callable interface, which is used for asynchronous invocation. Don’t confuse the
two.


Apex Reference Guide Callable Interface

Namespace

System

Usage

#### To implement the Callable interface, you need to write only one method: call(String action, Map<String,

`Object> args)` .

#### In code that utilizes or tests an implementation of Callable, cast an instance of your type to Callable . This interface is not intended to replace defining more specific interfaces. Rather, the Callable interface allows integrations in which

code from different classes or packages can use common base types.

IN THIS SECTION:

#### Callable Methods

Callable Example Implementation

#### Callable Methods The following are methods for Callable .

IN THIS SECTION:

##### call(action, args)

Provides functionality that other classes or packages can utilize and build upon.

##### call(action, args)

Provides functionality that other classes or packages can utilize and build upon.

Signature

```
   public Object call(String action, Map<String,Object> args)

```

Parameters

```
   action
```

Type: String

The behavior for the method to exhibit.

```
   args
```

Type: Map on page 3894<String,Object>

Arguments to be used by the specified action.

Return Value

Type: Object

The result of the method invocation.


Apex Reference Guide Callable Interface

#### Callable Example Implementation

This class is an example implementation of the `System.Callable` interface.

```
   public class Extension implements Callable {

     // Actual method

     String concatStrings(String stringValue) {

      return stringValue + stringValue;

     }

     // Actual method

     Decimal multiplyNumbers(Decimal decimalValue) {

      return decimalValue * decimalValue;

     }

     // Dispatch actual methods

     public Object call(String action, Map<String, Object> args) {

      switch on action {

        when 'concatStrings' {

         return this.concatStrings((String)args.get('stringValue'));

        }

        when 'multiplyNumbers' {

         return this.multiplyNumbers((Decimal)args.get('decimalValue'));

        }

        when else {

        throw new ExtensionMalformedCallException('Method not implemented');

        }

      }

     }

     public class ExtensionMalformedCallException extends Exception {}

   }

```

The following test code illustrates how calling code utilizes the interface to call a method.

```
   @IsTest

   private with sharing class ExtensionCaller {

     @IsTest

     private static void givenConfiguredExtensionWhenCalledThenValidResult() {

       // Given

       String extensionClass = 'Extension'; // Typically set via configuration

       Decimal decimalTestValue = 10;

       // When

       Callable extension =

         (Callable) Type.forName(extensionClass).newInstance();

       Decimal result = (Decimal)

         extension.call('multiplyNumbers', new Map<String, Object> {

           'decimalValue' => decimalTestValue

         });

       // Then

```


### Apex Reference Guide Cases Class

```
       System.assertEquals(100, result);

     }

   }

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_casting.htm)_ : Classes and Casting

### Cases Class Use the Cases class to interact with case records.

Namespace

System

#### Cases Methods

### The following are static methods for Cases .

IN THIS SECTION:

##### generateThreadingMessageId(caseId)

Returns an RFC 2822-compliant message identifier that contains information used to match the email and its replies to a case.

getCaseIdFromEmailHeaders(headers)
Returns the case ID corresponding to the specified email header information, or returns null if none is found.

getCaseIdFromEmailThreadId(emailThreadId)
Returns the case ID corresponding to the specified email thread ID. **(Deprecated. Use getCaseIdFromEmailHeaders and**
**EmailMessages.getRecordIdFromEmail instead.)**

##### generateThreadingMessageId(caseId)

Returns an RFC 2822-compliant message identifier that contains information used to match the email and its replies to a case.

Signature

```
   public static String generateThreadingMessageId(Id caseId)

```

Parameters

```
   caseId
```

Type: Id

The case SObject ID to which replies to this email should be attached.

Return Value

Type: String


Apex Reference Guide Cases Class

Usage

Use the returned message identifier when sending case-related emails in Apex. The returned message identifier can be used in Message-ID
or References headers. However, because Salesforce doesn’t let users specify the Message-ID, we set this identifier in the References
header. When users reply to the sent email, replies should be attached to the specified case.

Example

In this sample, we create an email with a message identifier so that the email and any responses can be associated with the related case.

```
   //Get your Case ID. Here we use a dummy ID

   ID caseId = Id.valueOf('500xx000000bpkTAAQ');

   //Create a SingleEmailMessage object

   Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();

   //Set recipients and other fields

   email.setToAddresses(new String[] {'test@salesforce.com'});

   email.setPlainTextBody('Test Email Notification');

   //........... more fields ...........

   //Get the threading message identifier

   String messageId = Cases.generateThreadingMessageId(caseId);

   //Insert the message identifier into the References header

   email.setReferences(messageId);

   //Send out the email

   Messaging.sendEmail(new Messaging.SingleEmailMessage[]{email});

##### **`getCaseIdFromEmailHeaders(headers)`**

```

Returns the case ID corresponding to the specified email header information, or returns null if none is found.

Signature

```
   public static Id getCaseIdFromEmailHeaders(List<Messaging.InboundEmail.Header> headers)

```

Parameters

```
   headers
```

Type: List<Messaging.InboundEmail.Header>

Return Value

Type: Id

Usage

To optimize finding a match between email threads and cases in your custom code, we recommend that you use this method and
`EmailMessages.getRecordIdFromEmail` to implement a combination of token- and header-based threading.

If you are transitioning from Ref ID threading, we recommend that you replace `Cases.getCaseIdFromEmailThreadId` with
a combination of `Cases.getCaseIdFromEmailHeaders` and `EmailMessages.getRecordIdFromEmail` . If you
choose to implement header-based threading only, replace `Cases.getCaseIdFromEmailThreadId` with
`Cases.getCaseIdFromEmailHeaders` .

The _`headers`_ argument is used to find the matching Case Id using values for the `In-Reply-To` and `References` headers
based on RFC 2822. If Email-to-Case can’t find any emails with a matching `In-Reply-To` or `References` header, it also checks


Apex Reference Guide Cases Class

the incoming email for an Outlook-specific header called `Thread-Index` . The first 22 bytes of this header uniquely identify the thread.
If Email-to-Case detects a `Thread-Index` header on the incoming mail, it looks for matching information in the ClientThreadIdentifier
field in EmailMessage records. If a match is found, the customer’s reply email is linked to the related case.

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

        // the Status, the MessageIdentifier, and the ParentId fields.

        EmailMessage em = new EmailMessage(

           Status = '0',

           MessageIdentifier = email.messageId,

           ParentId = caseId,

           // Other important fields.

           FromAddress = email.fromAddress,

```


### Apex Reference Guide Collator Class

```
           FromName = email.fromName,

           ToAddress = toAddresses,

           TextBody = email.plainTextBody,

           HtmlBody = email.htmlBody,

           Subject = email.subject

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

   }

##### **`getCaseIdFromEmailThreadId(emailThreadId)`**

```

Returns the case ID corresponding to the specified email thread ID. **(Deprecated. Use getCaseIdFromEmailHeaders and**
**EmailMessages.getRecordIdFromEmail instead.)**

Signature

```
   public static ID getCaseIdFromEmailThreadId(String emailThreadId)

```

Parameters

```
   emailThreadId
```

Type: String

Return Value

Type: ID

Usage

The argument for emailThreadId, also known as Ref ID, has the format `!00Dxx01gEW.!500xx0Yktl` . This format was introduced
in the Winter ‘24 release. The previous format, `_00Dxx1gEW._500xxYktl`, is supported for backward compatibility, but emails
sent from the Winter ‘24 release onward use the new format. Other formats that include `ref:` or `[ref:` aren’t supported by this
method.

### Collator Class

Contains methods to get locale-specific instances that can be used for comparisons and sorting. Use the `getInstance()` method
to obtain the Collator instance for a given locale and pass the Collator as the Comparator parameter to the `list.sort()` method.


Apex Reference Guide Collator Class

Namespace

System

Usage

Because locale-sensitive sorting can produce different results depending on the user running the code, avoid using it in triggers or in
code that expects a particular sort order.

Example

This example performs a default list sort and then uses Collator to sort based on the user locale.

```
   @IsTest

      static void userLocaleSort() {

        string userLocale = 'fr_FR';

        User u = new User(Alias = 'standt', Email='standarduser@testorg.com',

        EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',

        LocaleSidKey=userLocale, TimeZoneSidKey='America/Los_Angeles',

        ProfileId = [SELECT Id FROM Profile WHERE Name='Standard User'].Id,

        UserName='standarduser' + DateTime.now().getTime() + '@testorg.com');

        System.runAs(u) {

           List<String> shoppingList = new List<String> {

             'épaule désosé Agneau',

             'Juice',

             'à la mélasse Galette 5 kg',

             'Bread',

             'Grocery'

           };

           // Default sort

           shoppingList.sort();

           Assert.areEqual('Bread', shoppingList[0]);

           // Sort based on user Locale

           Collator myCollator = Collator.getInstance();

           shoppingList.sort(myCollator);

           Assert.areEqual('à la mélasse Galette 5 kg', shoppingList[0]);

           Assert.areEqual('Bread', shoppingList[1]);

           Assert.areEqual('épaule désosé Agneau', shoppingList[2]);

           Assert.areEqual('Grocery', shoppingList[3]);

           Assert.areEqual('Juice', shoppingList[4]);

        }

      }

```

IN THIS SECTION:

Collator Methods


### Apex Reference Guide Comparable Interface

#### Collator Methods The following are methods for Collator .

IN THIS SECTION:

##### compare(source, target)

Perform string comparisons for a given locale.

##### getInstance()

Gets the Collator instance for the current user’s locale.

##### **`compare(source, target)`**

Perform string comparisons for a given locale.

Signature

```
   public Integer compare(String source, String target)

```

Parameters

```
   source
```

Type: String

```
   target
```

Type: String

Return Value

Type: Integer

##### **`getInstance()`**

Gets the Collator instance for the current user’s locale.

Signature

```
   public static System.Collator getInstance()

```

Return Value

Type: Collator Class

### Comparable Interface

Adds sorting support for Lists that contain non-primitive types, that is, Lists of user-defined types. Your implementation must explicitly
handle null inputs in the `compareTo()` method to avoid a null pointer exception.


Apex Reference Guide Comparable Interface

Namespace

System

Usage

#### To add List sorting support for your Apex class, you must implement the Comparable interface with its compareTo method in

your class.

#### To implement the Comparable interface, you must first declare a class with the implements keyword as follows:

```
   public class Employee implements Comparable {

```

Next, your class must provide an implementation for the following method:

```
   public Integer compareTo(Object compareTo) {

      // Your code here

   }

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

#### Comparable Methods

Comparable Example Implementation

SEE ALSO:

List Class

#### Comparable Methods The following are methods for Comparable .

IN THIS SECTION:

##### compareTo(objectToCompareTo)

Returns an Integer value that is the result of the comparison.

##### compareTo(objectToCompareTo)

Returns an Integer value that is the result of the comparison.

Signature

```
   public Integer compareTo(Object objectToCompareTo)

```

Parameters

```
   objectToCompareTo
```

Type: Object


Apex Reference Guide Comparable Interface

Return Value

Type: Integer

Usage

The implementation of this method returns the following values:

**•** 0 if this instance and _`objectToCompareTo`_ are equal

**•**   - 0 if this instance is greater than _`objectToCompareTo`_

**•** < 0 if this instance is less than _`objectToCompareTo`_

If this object instance and _`objectToCompareTo`_ are incompatible, a `System.TypeException` is thrown.

#### Comparable Example Implementation This example implements the Comparable interface. The compareTo method in this example compares the employee of this

class instance with the employee passed in the argument. The method returns an Integer value based on the comparison of the employee
IDs.

```
   public class Employee implements Comparable {

      public Long id;

      public String name;

      public String phone;

      // Constructor

      public Employee(Long i, String n, String p) {

        id = i;

        name = n;

        phone = p;

      }

      // Implement the compareTo() method

      public Integer compareTo(Object compareTo) {

        Employee compareToEmp = (Employee)compareTo;

        if (id == compareToEmp.id) return 0;

        if (id > compareToEmp.id) return 1;

        return -1;

      }

   }

```

This example tests the sort order of a list of `Employee` objects.

```
   @isTest

   private class EmployeeSortingTest {

      @isTest

      static void test1() {

        List<Employee> empList = new List<Employee>();

        empList.add(new Employee(101,'Joe Smith', '4155551212'));

        empList.add(new Employee(101,'J. Smith', '4155551212'));

        empList.add(new Employee(25,'Caragh Smith', '4155551000'));

        empList.add(new Employee(105,'Mario Ruiz', '4155551099'));

        // Sort using the custom compareTo() method

```


### Apex Reference Guide Comparator Interface

```
        empList.sort();

        // Write list contents to the debug log

        System.debug(empList);

        // Verify list sort order.

        Assert.areEqual('Caragh Smith', empList[0].Name);

        Assert.areEqual('Joe Smith', empList[1].Name);

        Assert.areEqual('J. Smith', empList[2].Name);

        Assert.areEqual('Mario Ruiz', empList[3].Name);

      }

   }

### Comparator Interface

```

Implement different sort orders with the Comparator interface’s `compare()` method, and pass the Comparator as a parameter to
`List.sort()` . Your implementation must explicitly handle null inputs in the `compare()` method to avoid a null pointer exception.

Namespace

System

IN THIS SECTION:

#### Comparator Methods

Comparator Example Implementation
Use the Comparator interface to impose different kinds of sorting.

#### Comparator Methods

### The following are methods for Comparator .

IN THIS SECTION:

##### compare(var1, var2)

Compares the two arguments and returns a negative integer, zero, or a positive integer depending on whether the first argument
is less than, equal to, or greater than the second argument.

##### **`compare(var1, var2)`**

Compares the two arguments and returns a negative integer, zero, or a positive integer depending on whether the first argument is less
than, equal to, or greater than the second argument.

Signature

```
   public Integer compare(T var1, T var2)

```


Apex Reference Guide Comparator Interface

Parameters

```
   var1
```

Type: T

T - The type determined by the parameterized type of the Comparator. For example, if the class implements
`Comparator<Account>` then _`var1`_ and _`var2`_ are of type Account .

```
   var2
```

Type: T

T - The type determined by the parameterized type of the Comparator. For example, if the class implements
`Comparator<Account>` then _`var1`_ and _`var2`_ are of type Account .

Return Value

Type: Integer

#### Comparator Example Implementation

Use the Comparator interface to impose different kinds of sorting.

This example implements two different ways of sorting employees.

```
   public class Employee {

      private Long id;

      private String name;

      private Integer yearJoined;

      // Constructor

      public Employee(Long i, String n, Integer y) {

        id = i;

        name = n;

        yearJoined = y;

      }

      public String getName() { return name; }

      public Integer getYear() { return yearJoined; }

   }

   // Class to compare Employees by name

      public class NameCompare implements Comparator<Employee> {

        public Integer compare(Employee e1, Employee e2) {

           if(e1?.getName() == null && e2?.getName() == null) {

             return 0;

           } else if(e1?.getName() == null) {

             return -1;

           } else if(e2?.getName() == null) {

             return 1;

           }

           return e1.getName().compareTo(e2.getName());

           }

        }

      // Class to compare Employees by year joined

```


### Apex Reference Guide Continuation Class

```
      public class YearCompare implements Comparator<Employee> {

        public Integer compare(Employee e1, Employee e2) {

           // Guard against null operands for ‘<’ or ‘>’ operators because

           // they will always return false and produce inconsistent sorting

           Integer result;

           if(e1?.getYear() == null && e2?.getYear() == null) {

             result = 0;

           } else if(e1?.getYear() == null) {

              result = -1;

           } else if(e2?.getYear() == null) {

              result = 1;

           } else if (e1.getYear() < e2.getYear()) {

              result = -1;

           } else if (e1.getYear() > e2.getYear()) {

              result = 1;

           } else {

              result = 0;

           }

        return result;

        }

      }

```

The following example tests the implementation:

```
   @isTest

   private class EmployeeSortingTest {

      @isTest

      static void sortWithComparators() {

        List<Employee> empList = new List<Employee>();

        empList.add(new Employee(101,'Joe Smith', 2020));

        empList.add(new Employee(102,'J. Smith', 2020));

        empList.add(new Employee(25,'Caragh Smith', 2021));

        empList.add(new Employee(105,'Mario Ruiz', 2019));

        // Sort by name

        NameCompare nameCompare = new NameCompare();

        empList.sort(nameCompare);

        // Expected order: Caragh Smith, J. Smith, Joe Smith, Mario Ruiz

        Assert.areEqual('Caragh Smith', empList.get(0).getName());

        // Sort by year joined

        YearCompare yearCompare = new YearCompare();

        empList.sort(yearCompare);

        // Expected order: Mario Ruiz, J. Smith, Joe Smith, Caragh Smith

        Assert.areEqual('Mario Ruiz', empList.get(0).getName());

      }

   }

### Continuation Class Use the Continuation class to make callouts asynchronously to a SOAP or REST Web service.

```


Apex Reference Guide Continuation Class

Namespace

System

Example

[For a code example, see Make Long-Running Callouts from a Visualforce Page.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_continuation_overview.htm)

IN THIS SECTION:

#### Continuation Constructors Continuation Properties

Continuation Methods

#### Continuation Constructors The following are constructors for Continuation .

IN THIS SECTION:

##### Continuation(timeout)
#### Creates an instance of the Continuation class by using the specified timeout in seconds. The timeout maximum is 120 seconds.

##### Continuation(timeout)

#### Creates an instance of the Continuation class by using the specified timeout in seconds. The timeout maximum is 120 seconds.

Signature

```
   public Continuation(Integer timeout)

```

Parameters

```
   timeout
```

Type: Integer

The timeout for this continuation in seconds.

#### Continuation Properties The following are properties for Continuation .

IN THIS SECTION:

continuationMethod
The name of the callback method that is called after the callout response returns.

timeout
The timeout of the continuation in seconds. Maximum: 120 seconds.


Apex Reference Guide Continuation Class

##### state

Data that is stored in this continuation and that can be retrieved after the callout is finished and the callback method is invoked.

##### continuationMethod

The name of the callback method that is called after the callout response returns.

Signature

```
   public String continuationMethod {get; set;}

```

Property Value

Type: String

Usage

##### Note: If the continuationMethod property is not set for a Continuation, the same action method that made the asynchronous

callout is called again when the callout response returns.

##### timeout

The timeout of the continuation in seconds. Maximum: 120 seconds.

Signature

```
   public Integer timeout {get; set;}

```

Property Value

Type: Integer

##### state

Data that is stored in this continuation and that can be retrieved after the callout is finished and the callback method is invoked.

Signature

```
   public Object state {get; set;}

```

Property Value

Type: Object

Example

This example shows how to save state information for a continuation in a controller.

```
   // Declare inner class to hold state info

   private class StateInfo {

      String msg { get; set; }

```


Apex Reference Guide Continuation Class

```
      List<String> urls { get; set; }

      StateInfo(String msg, List<String> urls) {

        this.msg = msg;

        this.urls = urls;

      }

   }

   // Then in the action method, set state for the continuation

   continuationInstance.state = new StateInfo('Some state data', urls);

#### Continuation Methods The following are methods for Continuation .

```

IN THIS SECTION:

##### addHttpRequest(request)

Adds the HTTP request for the callout that is associated with this continuation.

getRequests()
Returns all labels and requests that are associated with this continuation as key-value pairs.

getResponse(requestLabel)
Returns the response for the request that corresponds to the specified label.

##### addHttpRequest(request)

Adds the HTTP request for the callout that is associated with this continuation.

Signature

```
   public String addHttpRequest(System.HttpRequest request)

```

Parameters

```
   request
```

Type: HttpRequest

The HTTP request to be sent to the external service by this continuation.

Return Value

Type: String

A unique label that identifies the HTTP request that is associated with this continuation. This label is used in the map that getRequests()
returns to identify individual requests in a continuation.

Usage

You can add up tothree requests to a continuation.

Note: The timeout that is set in each passed-in request is ignored. Only the global timeout maximum of 120 seconds applies for
a continuation.


### Apex Reference Guide Cookie Class

##### getRequests()

Returns all labels and requests that are associated with this continuation as key-value pairs.

Signature

```
   public Map<String,System.HttpRequest> getRequests()

```

Return Value

Type: Map<String,HttpRequest>

A map of all requests that are associated with this continuation. The map key is the request label, and the map value is the corresponding
HTTP request.

##### getResponse(requestLabel)

Returns the response for the request that corresponds to the specified label.

Signature

```
   public static HttpResponse getResponse(String requestLabel)

```

Parameters

```
   requestLabel
```

Type: String

The request label to get the response for.

Return Value

Type: HttpResponse

Usage

The status code is returned in the HttpResponse object and can be obtained by calling `getStatusCode()` on the response. A status
code of `200` indicates that the request was successful. Other status code values indicate the type of problem that was encountered.

**Sample of Error Status Codes**

When a problem occurs with the response, some possible status code values are:

**•** `2000` : The timeout was reached, and the server didn’t get a chance to respond.

**•** `2001` : There was a connection failure.

**•** `2002` : Exceptions occurred.

**•** `2003` : The response hasn’t arrived (which also means that the Apex asynchronous callout framework hasn’t resumed).

**•** `2004` : The response size is too large (greater than 1 MB).

### Cookie Class The Cookie class lets you access cookies for your Salesforce site using Apex.


Apex Reference Guide Cookie Class

Namespace

System

Usage

Use the `setCookies` method of the PageReference Class to attach cookies to a page.

Important:

**•** Cookie names and values set in Apex are URL encoded, that is, characters such as @ are replaced with a percent sign and their
hexadecimal representation.

**•** The `setCookies` method adds the prefix “ `apex__` ” to the cookie names.

**•** Setting a cookie's value to `null` sends a cookie with an empty string value instead of setting an expired attribute.

**•** After you create a cookie, the properties of the cookie can't be changed.

**•** Be careful when storing sensitive information in cookies. Pages are cached regardless of a cookie value. If you use a cookie
[value to generate dynamic content, you should disable page caching. For more information, see Configure Site Caching in](https://help.salesforce.com/articleView?id=sf.sites_caching.htm&language=en_US)
Salesforce Help.

Consider the following limitations when using the `Cookie` class:

**•** The `Cookie` class can only be accessed using Apex that is saved using the Salesforce API version 19 and above.

**•** The maximum number of cookies that can be set per Salesforce Sites domain depends on your browser. Newer browsers have higher
limits than older ones.

**•** Cookies must be less than 4K, including name and attributes.

**•** The maximum header size of a Visualforce page, including cookies, is 8,192 bytes.

For more information on sites, see “Salesforce Sites” in the Salesforce online help.

Example

The following example creates a class, `CookieController`, which is used with a Visualforce page (see markup below) to update
a counter each time a user displays a page. The number of times a user goes to the page is stored in a cookie.

```
   // A Visualforce controller class that creates a cookie

   // used to keep track of how often a user displays a page

   public class CookieController {

      public CookieController() {

        Cookie counter = ApexPages.currentPage().getCookies().get('counter');

        // If this is the first time the user is accessing the page,

        // create a new cookie with name 'counter', an initial value of '1',

        // path 'null', maxAge '-1', and isSecure 'true'.

        if (counter == null) {

           counter = new Cookie('counter','1',null,-1,true);

        } else {

        // If this isn't the first time the user is accessing the page

        // create a new cookie, incrementing the value of the original count by 1

           Integer count = Integer.valueOf(counter.getValue());

           counter = new Cookie('counter', String.valueOf(count+1),null,-1,true);

        }

```


Apex Reference Guide Cookie Class

```
        // Set the new cookie for the page

        ApexPages.currentPage().setCookies(new Cookie[]{counter});

      }

      // This method is used by the Visualforce action {!count} to display the current

      // value of the number of times a user had displayed a page.

      // This value is stored in the cookie.

      public String getCount() {

        Cookie counter = ApexPages.currentPage().getCookies().get('counter');

        if(counter == null) {

           return '0';

        }

        return counter.getValue();

      }

   }

   // Test class for the Visualforce controller

   @isTest

   private class CookieControllerTest {

     // Test method for verifying the positive test case

     static testMethod void testCounter() {

      //first page view

      CookieController controller = new CookieController();

      System.assert(controller.getCount() == '1');

      //second page view

      controller = new CookieController();

      System.assert(controller.getCount() == '2');

     }

   }

```

The following is the Visualforce page that uses the `CookieController` Apex controller above. The action `{!count}` calls the
`getCount` method in the controller above.

```
   <apex:page controller="CookieController">

   You have seen this page {!count} times

   </apex:page>

```

IN THIS SECTION:

#### Cookie Constructors

Cookie Methods

#### Cookie Constructors The following are constructors for Cookie .

IN THIS SECTION:

Cookie(name, value, path, maxAge, isSecure)
#### Creates a new instance of the Cookie class using the specified name, value, path, age, and the secure setting.


Apex Reference Guide Cookie Class

##### Cookie(name, value, path, maxAge, isSecure, SameSite) Creates a new instance of the Cookie class using the specified name, value, path, and age, and settings for security and cross-domain

behavior.

Cookie(name, value, path, maxAge, isSecure, SameSite, isHttpOnly)
##### Creates a new instance of the Cookie class using the specified name, value, path, age, and settings for security, cross-domain

behavior, and JavaScript access.

##### Cookie(name, value, path, maxAge, isSecure) Creates a new instance of the Cookie class using the specified name, value, path, age, and the secure setting.

Signature

```
   public Cookie(String name, String value, String path, Integer maxAge, Boolean isSecure)

```

Parameters

```
   name
```

Type: String

The cookie name. It can’t be `null` .

```
   value
```

Type: String

The cookie data, such as session ID.

```
   path
```

Type: String

The path from where you can retrieve the cookie.

```
   maxAge
```

Type: Integer

A number representing how long a cookie is valid for in seconds. If set to less than zero, a session cookie is issued. If set to zero, the
cookie is deleted.

```
   isSecure
```

Type: Boolean

A value indicating whether the cookie can only be accessed through HTTPS ( `true` ) or not ( `false` ).

##### Cookie(name, value, path, maxAge, isSecure, SameSite) Creates a new instance of the Cookie class using the specified name, value, path, and age, and settings for security and cross-domain

behavior.

Note: Google Chrome 80 introduces a new default cookie attribute setting of `SameSite`, which is set to `Lax` . Previously, the
`SameSite` cookie attribute defaulted to the value of `None` . When `SameSite` is set to `None`, cookies must be tagged with
the `isSecure` attribute indicating that they require an encrypted HTTPS connection.


Apex Reference Guide Cookie Class

Signature

```
   public Cookie(String name, String value, String path, Integer maxAge, Boolean isSecure,

   String SameSite)

```

Parameters

```
   name
```

Type: String

The cookie name. It can’t be `null` .

```
   value
```

Type: String

The cookie data, such as session ID.

```
   path
```

Type: String

The path from where you can retrieve the cookie.

```
   maxAge
```

Type: Integer

A number representing how long a cookie is valid for in seconds. If set to less than zero, a session cookie is issued. If set to zero, the
cookie is deleted.

```
   isSecure
```

Type: Boolean

A value indicating whether the cookie can only be accessed through HTTPS ( `true` ) or not ( `false` ).

```
   SameSite
```

Type: String

The `SameSite` attribute on a cookie controls its cross-domain behavior. The valid values are `None`, `Lax`, and `Strict` . After
the Chrome 80 release, a cookie with a `SameSite` value of `None` must also be marked secure by setting a value of `None;`
`Secure` .

SEE ALSO:

_Salesforce Spring ’20 Release Notes:_ [Prepare for Google Chrome’s Changes in SameSite Cookie Behavior That Can Break Salesforce](http://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_general_chrome_samesite.htm)
[Integrations](http://releasenotes.docs.salesforce.com/en-us/spring20/release-notes/rn_general_chrome_samesite.htm)

_Chrome Platform Status_ [: Reject insecure SameSite=None cookies](https://www.chromestatus.com/feature/5633521622188032)

##### Cookie(name, value, path, maxAge, isSecure, SameSite, isHttpOnly) Creates a new instance of the Cookie class using the specified name, value, path, age, and settings for security, cross-domain behavior,

and JavaScript access.

Signature

```
   public Cookie(String name, String value, String path, Integer maxAge, Boolean isSecure,

   String SameSite, Boolean isHttpOnly)

```


Apex Reference Guide Cookie Class

Parameters

```
   name
```

Type: String

The cookie name. It can’t be `null` .

```
   value
```

Type: String

The cookie data, such as session ID.

```
   path
```

Type: String

The path from where you can retrieve the cookie.

```
   maxAge
```

Type: Integer

A number representing how long a cookie is valid for in seconds. If set to less than zero, a session cookie is issued. If set to zero, the
cookie is deleted.

```
   isSecure
```

Type: Boolean

A value indicating whether the cookie can only be accessed through HTTPS ( `true` ) or not ( `false` ).

```
   SameSite
```

Type: String

The `SameSite` attribute on a cookie controls its cross-domain behavior. The valid values are `None`, `Lax`, and `Strict` . After
the Chrome 80 release, a cookie with a `SameSite` value of `None` must also be marked secure by setting a value of `None;`
`Secure` .

```
   isHttpOnly
```

Type: Boolean

[A value indicating whether the HttpOnly attribute for the cookie is set (](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#httponly) `true` ) or not ( `false` ). If `true`, client-side JavaScript can’t
access the cookie.

SEE ALSO:

_MDN Web Docs_ [: Set-Cookie HTTP Response Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#httponly)

#### Cookie Methods The following are methods for Cookie . All are instance methods.

IN THIS SECTION:

getDomain()
Returns the name of the server making the request.

getMaxAge()
Returns a number representing how long the cookie is valid for, in seconds. If set to `< 0`, a session cookie is issued. If set to `0`, the
cookie is deleted.

getName()
Returns the name of the cookie. Can't be `null` .


Apex Reference Guide Cookie Class

getPath()
Returns the path from which you can retrieve the cookie. If `null` or blank, the location is set to root, or “/”.

getSameSite()
Returns the value for the `SameSite` attribute of the cookie.

getValue()
Returns the data captured in the cookie, such as Session ID.

isSecure()
Returns `true` if the cookie can only be accessed through HTTPS, otherwise returns `false` .

isHttpOnly()
Returns `true` if client-side JavaScript is forbidden from accessing the cookie; otherwise returns `false` .

##### getDomain()

Returns the name of the server making the request.

Signature

```
   public String getDomain()

```

Return Value

Type: String

##### getMaxAge()

Returns a number representing how long the cookie is valid for, in seconds. If set to `< 0`, a session cookie is issued. If set to `0`, the cookie
is deleted.

Signature

```
   public Integer getMaxAge()

```

Return Value

Type: Integer

##### getName()

Returns the name of the cookie. Can't be `null` .

Signature

```
   public String getName()

```

Return Value

Type: String


Apex Reference Guide Cookie Class

##### getPath()

Returns the path from which you can retrieve the cookie. If `null` or blank, the location is set to root, or “/”.

Signature

```
   public String getPath()

```

Return Value

Type: String

##### getSameSite()

Returns the value for the `SameSite` attribute of the cookie.

Signature

```
   public String getSameSite()

```

Return Value

Type: String

SEE ALSO:

_web.dev_ [: SameSite Cookies Explained](https://web.dev/samesite-cookies-explained/)

##### getValue()

Returns the data captured in the cookie, such as Session ID.

Signature

```
   public String getValue()

```

Return Value

Type: String

##### isSecure()

Returns `true` if the cookie can only be accessed through HTTPS, otherwise returns `false` .

Signature

```
   public Boolean isSecure()

```

Return Value

Type: Boolean


### Apex Reference Guide Crypto Class

##### isHttpOnly()

Returns `true` if client-side JavaScript is forbidden from accessing the cookie; otherwise returns `false` .

Signature

```
   public Boolean isHttpOnly()

```

Return Value

Type: Boolean

SEE ALSO:

_MDN Web Docs_ [: Set-Cookie HTTP Response Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#httponly)

### Crypto Class

Provides methods for creating digests, message authentication codes, and signatures, as well as encrypting and decrypting information.

Namespace

System

Usage

### The methods in the Crypto class can be used for securing content in Lightning Platform, or for integrating with external services such

as Google or Amazon WebServices (AWS).

Each method in this class supports a unique set of AES encryption algorithms, depending on its purpose. To confirm which algorithms
are available for the action that you want to do, check each method.

Using Encryption Algorithms

The Crypto class supports Galois Counter Mode (GCM) and Cipher Block Chaining mode (CBC). The GCM AES256-GCM algorithm is valid
in all encrypt and decrypt variants Currently, only the 256-bit size is supported for GCM. CBC algorithms in 128-bit, 192-bit, and 256-bit
sizes are valid in all variants except those that expect additional authentication data (an _`aaD`_ parameter).

**•** When you use CBC with encrypt and decrypt, you provide a 16-bit initialization vector (IV).

**•** When you use GCM with encrypt and decrypt, you provide no initialization vector (IV).

**•** When you use CBC with encryptWithManagedIV and decryptWithManagedIV, Salesforce provides the IV. You provide no additional
authentication data (aaData). You can only use CBC with encryptWithManagedIV and decryptWithManagedIV if you use the version
which does not expect aaData.

**•** When you use GCM with encryptWithManagedIV and decryptWithManagedIV, Salesforce provides an IV. and you can optionally
provide the aaData

When use the Crypto class to encrypt using GCM, the final encrypted content includes the length of the IV (always 12), the
Salesforce-generated 12-byte IV, and the cipher text.


Apex Reference Guide Crypto Class

Encryption Algorithms

The Crypto class supports these encryption algorithms.

**MODE** **VARIANT** **DESCRIPTION**

CBC (Cipher Block Chaining) `AES128`, `AES128-CBC` AES 128-bit with CBC mode with PKCS7
padding. Use either of these two values.

`AES192`, `AES192-CBC` AES 192-bit with CBC mode with PKCS7
padding. Use either of these two values.

`AES256`, `AES256-CBC` AES 256-bit with CBC mode with PKCS7
padding. Use either of these two values.

GCM (Galois Counter Mode) `AES256-GCM`

Signing Algorithms

The Crypto class supports these signing algorithms.

AES 256-bit with GCM mode with no
padding. Currently, only the 256-bit size is
supported for GCM.

**TYPE** **VARIANT** **DESCRIPTION**

RSA `RSA`, `RSA-SHA1`

An RSA signature (with an asymmetric key
pair) of an SHA1 hash. Use either of these
two values.

`RSA-SHA256` RSA signature of an SHA256 hash

`RSA-SHA384` RSA signature of an SHA384 hash

`RSA-SHA512` RSA signature of an SHA512 hash

ECDSA (DER) `ECDSA-SHA256` ECDSA signature of an SHA256 hash

`ECDSA-SHA384` ECDSA signature of an SHA384 hash

`ECDSA-SHA512` ECDSA signature of an SHA512 hash

ECDSA (P1363) `ECDSA-SHA256-P1363` ECDSA signature of an SHA256 hash (P1363
format)

```
ECDSA-SHA256-PLAIN

```

ECDSA signature of an SHA256 hash (P1363
format). Use if the JWT returns invalid_client.
See Other Errors on this page.

`ECDSA-SHA384-P1363` ECDSA signature of an SHA256 hash (P1363
format)

ECDSA-SHA512-P1363


Apex Reference Guide Crypto Class

Encrypt and Decrypt Exceptions

These exceptions can be thrown for these methods.

**•** `decrypt`

**•** `encrypt`

**•** `decryptWithManagedIV`

**•** `encryptWithManagedIV`

**Exception** **Message** **Description**

`InvalidParameterValue` Unable to parse the initialization vector from
encrypted data.

Thrown if you’re using managed
initialization vectors, and the cipher text is
less than 16 bytes.

Invalid algorithm _`algoName`_ . Must be one Thrown if the algorithm name isn’t one of
of the suported AES algorithms listed on this the valid values.
page.

Invalid private key. Must be _`size`_ bytes. Thrown if the size of the private key doesn’t
match the specified algorithm.

Invalid initialization vector. For CBC, this Thrown if the initialization vector provided
must be 16 bytes. For GCM, the IV is 12 for a CBC encryption isn’t 16 bytes.
bytes.

AAD can only be used with AESGCM
algorithms.

Thrown if a value is supplied for _`aaData`_,
but the encryption algorithm isn’t a GCM
type.

Invalid data. Input data is _`size`_ bytes, Thrown if the data is greater than 1 MB. For
which exceeds the limit of 1,048,576 bytes. decryption, 1,048,608 bytes are allowed for
the initialization vector header, plus any
additional padding the encryption added
to align to block size.

`NullPointerException` _`Argument`_ can’t be null. Thrown if one of the required method
arguments is null.

`SecurityException` Given final block isn’t properly padded.

Thrown if the data isn’t properly
block-aligned or similar issues occur during
encryption or decryption.

`SecurityException` _`Message Varies`_ Thrown if something goes wrong during
either encryption or decryption.

These exceptions are a subset of the exceptions that can be thrown from the System namespace. Refer to Exception Class and Built-In
Exceptions

For CBC, the `Crypto` [class uses AES / CBC / PKCS7 padding, which is vulnerable to a Padding Oracle attack. You can protect against a](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/02-Testing_for_Padding_Oracle)
Padding Oracle attack by using the Encrypt-then-MAC method. In this method, you encrypt the cipher text and MAC separately.


Apex Reference Guide Crypto Class

**•** For encryption, first encrypt the data with AES by using one encryption key. Then, with a different encryption key, use the
generateMac(algorithmName, input, privateKey) method to generate a message authentication code (MAC) for the cipher text.
Append the MAC to the cipher text before sending it to its recipient.

**•** For decryption, start by checking the authenticity and integrity of the cipher text by using the verifyHMac(algorithmName, data,
privateKey, macToVerify) method. If either the authenticity or integrity check fails, throw an exception and don’t decrypt the cipher
text. The decryption of the cipher text must only happen in a second step, after the message authenticity and integrity has been
verified.

You can also protect against a Padding Oracle attack by using a GCM encryption algorithm.

Other Errors

Under rare conditions you may encounter the `invalid_client` error from the JSON Web Tokens (JWT) service.

**Error** **Message** **Description**

`invalid_client` The actual text varies, but describes the
inability to validate the client credentials.

The JWT public certificate in the Salesforce
Connected Application doesn’t appear to
match the known private key.

For Shield Platform Encryption, this error can happen when you use a custom JWT implementation that uses the P11363 format, and
you also want to use the `ECDSA-SHA256` algorithm. The solution is to specify the `ECDSA-SHA256-PLAIN` algorithm instead.
The `ECDSA-SHA256-PLAIN` is available to the several `sign()` and `verify()` methods.

For example, in order to comply with your program requirements, you sign your token using the Elliptic Curve Digital Signature Algorithm
(ECDSA) with the P-256 curve. This algorithm is in the P1363 format, so when you try to use `Crypto.verify()` using the `ECDSA`
`SHA256`, you receive a response containing `invalid_client` . You change `ECDSA-SHA256` to `ECDSA-SHA256-PLAIN`
and the error is resolved.

Running the Crypto Class Samples

Each of the methods in this section contains a code sample to demonstrate the method's use. The samples use curl to make calls into
[your Salesforce org. Use your preferred developer environment to run the samples. Use the Salesforce developer Introduction to REST](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
[API for basic information on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
you starter information on using REST to work with Shield Platform Encryption.

SEE ALSO:

[Encrypt-then-MAC (EtM)](https://en.wikipedia.org/wiki/Authenticated_encryption#Encrypt-then-MAC_(EtM))

[ISO/IEC 19772:2020 - Information Security Authenticated Encryption](https://www.iso.org/standard/81550.html)

Exception Class and Built-In Exceptions

#### Crypto Methods The following are methods for Crypto . All methods are static.


Apex Reference Guide Crypto Class

IN THIS SECTION:

decrypt(algorithmName, secretKey, initializationVector, cipherText)
Decrypts the _`cipherText`_ blob by using the specified algorithm, private key, and initialization vector. Use this method to decrypt
blobs encrypted by using a third-party application or the `encrypt` method.

decryptWithManagedIV(algorithmName, secretKey, IVAndCipherText)
Decrypts the _`IVAndCipherText`_ blob by using the specified algorithm and private key. Use this method to decrypt blobs
encrypted by using a third-party application or the `encryptWithManagedIV` method. This version of
`decryptWithManagedIV` doesn’t use additional authentication data.

decryptWithManagedIV(algorithmName, secretKey, IVAndCipherText, aaData)
Decrypts the _`IVAndCipherText`_ blob by using the specified algorithm and private key. Use this method to decrypt blobs
encrypted by using a third-party application or the `encryptWithManagedIV` method. This version of
`decryptWithManagedIV` uses additional authentication data. CBC isn’t supported for this method.

encrypt(algorithmName, secretKey, initializationVector, clearText)
Encrypts the _`clearText`_ blob by using the specified algorithm, private key, and initialization vector. Use this method when you
want to specify your own initialization vector.

encryptWithManagedIV(algorithmName, secretKey, clearText)
Encrypts the _`clearText`_ blob by using the specified algorithm and private key. Use this method when you want Salesforce to
generate the initialization vector. This version of `encryptWithManagedIV` doesn’t use additional authentication data.

encryptWithManagedIV(algorithmName, secretKey, clearText, aaData)
Encrypts the _`clearText`_ blob by using the specified algorithm and private key. Use this method when you want Salesforce to
generate the initialization vector. This version of `encryptWithManagedIV` uses additional authentication data. CBC isn’t
supported for this method.

generateAesKey(size)
Generates an Advanced Encryption Standard (AES) key.

generateDigest(algorithmName, input)
Computes a secure, one-way hash digest using the specified algorithm on the supplied _`input`_ blob.

generateMac(algorithmName, input, privateKey)
Computes a message authentication code (MAC) for the _`input`_ blob value using the private key and the specified algorithm.

getRandomInteger()
Returns a random integer value.

getRandomLong()
Returns a random long value.

sign(algorithmName, input, privateKey)
Computes a unique digital signature for the _`input`_ blob value, using the specified algorithm and the supplied private key.

signWithCertificate(algorithmName, input, certDevName)
Computes a unique digital signature for the input blob value, using the specified algorithm and the supplied certificate and key pair.

signXML(algorithmName, node, idAttributeName, certDevName)
Envelops the signature into an XML document.

signXML(algorithmName, node, idAttributeName, certDevName, refChild)
Inserts the signature envelope before the specified child node.


Apex Reference Guide Crypto Class

verify(algorithmName, data, signature, publicKey)
Verifies the digital signature for the _`data`_ blob using the specified algorithm and the supplied public key. Use this method to verify
a blob signed by a digital signature created using a third-party application or the sign method.

verify(algorithmName, data, signature, certDevName)
Verifies the digital signature for the _`data`_ blob using the specified algorithm and the public key associated with _`certDevName`_ .
Use this method to verify a blob signed by a digital signature created using a third-party application or the
`signWithCertificate` method.

verifyHMac(algorithmName, data, privateKey, macToVerify)
Verifies the HMAC signature for the _`data`_ blob using the specified algorithm, input data, private key, and the mac. Use this method
to verify a blob signed by a digital signature created using a third-party application or the sign method.

##### **`decrypt(algorithmName, secretKey, initializationVector, cipherText)`**

Decrypts the _`cipherText`_ blob by using the specified algorithm, private key, and initialization vector. Use this method to decrypt
blobs encrypted by using a third-party application or the `encrypt` method.

Signature

```
   public static Blob decrypt(String algorithmName, Blob secretKey, Blob

   initializationVector, Blob cipherText)

```

Parameters

```
   algorithmName
```

Type: String

decrypt supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES128`, `AES128-CBC`

**•** `AES192`, `AES192-CBC`

**•** `AES256`, `AES256-CBC`

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key.

```
   initializationVector
```

Type: Blob

**•** For CBC, the 128 bit (16 byte) IV. The IV must be 128 bits (16 bytes.)

**•** For GCM, don’t provide an IV. Any non-null IV will result in an error.

```
   cipherText
```

Type: Blob

The content to decrypt.


Apex Reference Guide Crypto Class

Return Value

Type: Blob

Contains the decrypted contents of _`cipherText`_ .

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestDecrypt {

        public void testDecrypt(){

           // 16-byte string

           Blob exampleIv = Blob.valueOf('Example of IV123');

           Blob key = Crypto.generateAesKey(128);

           Blob data = Blob.valueOf('Data to be encrypted');

           Blob encrypted = Crypto.encrypt('AES128', key, exampleIv, data);

           Blob decrypted = Crypto.decrypt('AES128', key, exampleIv, encrypted);

           String decryptedString = decrypted.toString();

           System.debug('Decrypted Value: ' + decryptedString);

          Assert.areEqual('Data to be encrypted', decryptedString, 'Error: not equal!');

           return;

        }

      }

```

To invoke this method, run:

```
   TestDecrypt td = new TestDecrypt();

   td.testDecrypt();

##### **`decryptWithManagedIV(algorithmName, secretKey, IVAndCipherText)`**

```

Decrypts the _`IVAndCipherText`_ blob by using the specified algorithm and private key. Use this method to decrypt blobs encrypted
##### by using a third-party application or the encryptWithManagedIV method. This version of decryptWithManagedIV

doesn’t use additional authentication data.

Signature

```
   public static Blob decryptWithManagedIV(String algorithmName, Blob secretKey, Blob

   IVAndCipherText)

```

Parameters

```
   algorithmName
```

Type: String

decryptWithManagedIV supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES128`, `AES128-CBC`

**•** `AES192`, `AES192-CBC`

**•** `AES256`, `AES256-CBC`


Apex Reference Guide Crypto Class

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key for you.

```
   IVAndCipherText
```

Type: Blob

A concatenation of the initialization vector and the encrypted text that you want to decrypt.

**•** For CBC, _`IVAndCipherText`_ must contain IV + ciphertext, where the IV must be the first 128 bits (16 bytes) with the
ciphertext following.

**•** FOR GCM, _`IVAndCipherText`_ must contain the length of the IV (always 12) followed by a 96 bit (12 byte) IV, with the
ciphertext following.

Return Value

Type: Blob

Contains the decrypted contents of _`IVAndCipherText`_ .

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestDecryptWithManagedIV {

        public void testDecryptWithManagedIV(){

           String algorithmName = 'AES128';

           Blob key = Crypto.generateAesKey(128);

           Blob data = Blob.valueOf('Data to be encrypted');

           Blob encrypted = Crypto.encryptWithManagedIV(algorithmName, key, data);

           Blob decrypted = Crypto.decryptWithManagedIV(algorithmName, key, encrypted);

           String decryptedString = decrypted.toString();

          Assert.areEqual('Data to be encrypted', decryptedString, 'Error: the strings

   are not equal!');

        }

      }

```

To invoke this method, run:

```
   TestDecryptWithManagedIV tdiv = new TestDecryptWithManagedIV();

   tdiv.testDecryptWithManagedIV();

##### **`decryptWithManagedIV(algorithmName, secretKey, IVAndCipherText, aaData)`**

```

Decrypts the _`IVAndCipherText`_ blob by using the specified algorithm and private key. Use this method to decrypt blobs encrypted
##### by using a third-party application or the encryptWithManagedIV method. This version of decryptWithManagedIV uses

additional authentication data. CBC isn’t supported for this method.


Apex Reference Guide Crypto Class

Signature

```
   public static Blob decryptWithManagedIV(String algorithmName, Blob secretKey, Blob

   IVAndCipherText, Blob aaData)

```

Parameters

```
   algorithmName
```

Type: String

decryptWithManagedIV supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key for you.

```
   IVAndCipherText
```

Type: Blob

_`IVAndCipherText`_ must contain the length of the IV (always 12) followed by a 96 bit (12 byte) IV, with the ciphertext following.

```
   aaData
```

Type: Blob

Additional authentication data. This value is required.

Return Value

Type: Blob

Contains the decrypted contents of _`IVAndCipherText`_ .

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestDecryptWithManagedIV {

        public void testDecryptWithManagedIV(){

           String algorithmName = 'AES256-GCM';

           Blob key = Crypto.generateAesKey(256);

           Blob data = Blob.valueOf('Data to be encrypted');

           Blob aad = Blob.valueOf('Additional tag');

           Blob encrypted = Crypto.encryptWithManagedIV(algorithmName, key, data, aad);

           Blob decrypted = Crypto.decryptWithManagedIV(algorithmName, key, encrypted,

   aad);

           String decryptedString = decrypted.toString();

          Assert.areEqual('Data to be encrypted', decryptedString, 'Error: the strings

   are not equal!');

        }

      }

```


Apex Reference Guide Crypto Class

To invoke this method, run:

```
   TestDecryptWithManagedIV tdiv = new TestDecryptWithManagedIV();

   tdiv.testDecryptWithManagedIV();

##### **`encrypt(algorithmName, secretKey, initializationVector, clearText)`**

```

Encrypts the _`clearText`_ blob by using the specified algorithm, private key, and initialization vector. Use this method when you want
to specify your own initialization vector.

Signature

```
   public static Blob encrypt(String algorithmName, Blob secretKey, Blob

   initializationVector, Blob clearText)

```

Parameters

```
   algorithmName
```

Type: String

Algorithm for encrypting _`clearText`_ .

encrypt supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES128`, `AES128-CBC`

**•** `AES192`, `AES192-CBC`

**•** `AES256`, `AES256-CBC`

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key for you.

```
   initializationVector
```

Type: Blob

**•** For CBC, any 128 bit (16 byte) string to provide the initial state to this method. The initialization vector must be 128 bits (16
bytes.)

**•** For GCM, don’t provide an IV. Any non-null IV results in an error.

```
   clearText
```

Type: Blob

The content that you want to encrypt.

Return Value

Type: Blob

Contains the encrypted contents of _`clearText`_ .


Apex Reference Guide Crypto Class

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestEncrypt {

        public void testEncrypt(){

           Blob exampleIv = Blob.valueOf('Example of IV123');

           Blob key = Crypto.generateAesKey(128);

           Blob data = Blob.valueOf('Encryption Example Text.');

           Blob encrypted = Crypto.encrypt('AES128', key, exampleIv, data);

           Blob decrypted = Crypto.decrypt('AES128', key, exampleIv, encrypted);

           String decryptedString = decrypted.toString();

          Assert.areEqual('Encryption Example Text.', decryptedString, 'Error: the values

    are not equal!');

           return;

        }

      }

```

To invoke this method, run:

```
   TestEncrypt te = new TestEncrypt();

   te.testEncrypt();

##### **`encryptWithManagedIV(algorithmName, secretKey, clearText)`**

```

Encrypts the _`clearText`_ blob by using the specified algorithm and private key. Use this method when you want Salesforce to generate
##### the initialization vector. This version of encryptWithManagedIV doesn’t use additional authentication data.

Signature

```
   public static Blob encryptWithManagedIV(String algorithmName, Blob secretKey, Blob

   clearText)

```

Parameters

```
   algorithmName
```

Type: String

encryptWithManagedIV supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES128`, `AES128-CBC`

**•** `AES192`, `AES192-CBC`

**•** `AES256`, `AES256-CBC`

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key for you.


Apex Reference Guide Crypto Class

```
   clearText
```

Type: Blob

The content you want to encrypt.

Return Value

Type: Blob

Contains the encrypted contents of _`clearText`_ .

**•** For CBC, the initialization vector is stored as the first 128 bits (16 bytes) of the encrypted blob.

**•** For GCM, the return value contains the length of the IV (always 12) followed by a 96 bit (12 byte) Salesforce generated IV, with the
ciphertext following.

Use either third-party applications or the `decryptWithManagedIV` method to decrypt blobs encrypted with this method. Use
##### the encrypt method if you want to generate your own initialization vector.

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestEncryptWithManagedIV {

        public void testEncryptWithManagedIV(){

           String algorithmName = 'AES128';

           Blob key = Crypto.generateAesKey(128);

           Blob data = Blob.valueOf('Data to be encrypted');

           Blob encrypted = Crypto.encryptWithManagedIV(algorithmName, key, data);

           Blob decrypted = Crypto.decryptWithManagedIV(algorithmName, key, encrypted);

           String decryptedString = decrypted.toString();

          Assert.areEqual('Data to be encrypted', decryptedString, 'Error: the strings

   are not equal!');

        }

      }

```

To invoke this method, run:

```
   TestEncryptWithManagedIV teiv = new TestEncryptWithManagedIV();

   teiv.testEncryptWithManagedIV();

##### **`encryptWithManagedIV(algorithmName, secretKey, clearText, aaData)`**

```

Encrypts the _`clearText`_ blob by using the specified algorithm and private key. Use this method when you want Salesforce to generate
##### the initialization vector. This version of encryptWithManagedIV uses additional authentication data. CBC isn’t supported for this

method.

Signature

```
   public static Blob encryptWithManagedIV(String algorithmName, Blob secretKey, Blob

   clearText, Blob aaData)

```


Apex Reference Guide Crypto Class

Parameters

```
   algorithmName
```

Type: String

encryptWithManagedIV supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

**•** `AES256-GCM`

```
   secretKey
```

Type: Blob

Private key text. The length of _`secretKey`_ must match the size required by _`algorithmName`_ : 128 bits, 192 bits, or 256 bits,
which is 16 bytes, 24 bytes, or 32 bytes, respectively. You can use a third-party application or the `generateAesKey` method to
generate this key for you.

```
   clearText
```

Type: Blob

The content you want to encrypt.

```
   aaData
```

Type: Blob

Additional authentication data. This is required .

Return Value

Type: Blob

Contains the encrypted contents of _`clearText`_ . For GCM, the return value contains the length of the IV (always 12) followed by a 96
bit (12 byte) Salesforce generated IV, with the ciphertext following.

Example

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestEncryptWithManagedIV {

        public void testEncryptWithManagedIV(){

           String algorithmName = 'AES256-GCM';

           /*

            No IV if you specify AES256-GCM

           */

           Blob key = Crypto.generateAesKey(256);

           Blob data = Blob.valueOf('Data to be encrypted');

           Blob aad = Blob.valueOf('Additional tag');

           Blob encrypted = Crypto.encryptWithManagedIV(algorithmName, key, data, aad);

           Blob decrypted = Crypto.decryptWithManagedIV(algorithmName, key, encrypted,

   aad);

           String decryptedString = decrypted.toString();

          Assert.areEqual('Data to be encrypted', decryptedString, 'Error: the strings

   are not equal!');

        }

      }

```


Apex Reference Guide Crypto Class

To invoke this method, run:

```
   TestEncryptWithManagedIV teiv = new TestEncryptWithManagedIV();

   teiv.testEncryptWithManagedIV();

##### **`generateAesKey(size)`**

```

Generates an Advanced Encryption Standard (AES) key.

Signature

```
   public static Blob generateAesKey(Integer size)

```

Parameters

```
   size
```

Type: Integer

The key's size in bits. Valid values are:

**•** 128

**•** 192

**•** 256

Return Value

Type: Blob

Contains the generated AES key.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestGenerateAESKey {

        public void testGenerateAESKey() {

         Blob key = Crypto.generateAesKey(128);

         System.debug('Generated AES Key: ');

         String strKey = EncodingUtil.base64Encode(key);

         System.debug(strKey);

        }

      }

```

To invoke this method, run the following:

```
   TestGenerateAESKey tgaes = new TestGenerateAESKey();

   tgaes.testGenerateAESKey();

##### **`generateDigest(algorithmName, input)`**

```

Computes a secure, one-way hash digest using the specified algorithm on the supplied _`input`_ blob.


Apex Reference Guide Crypto Class

Signature

```
   public static Blob generateDigest(String algorithmName, Blob input)

```

Parameters

```
   algorithmName
```

Type: String

The algorithm you want to use to generate the digest. Valid values for _`algorithmName`_ are:

**•** `MD5`

**•** `SHA1`

**•** `SHA3-256`

**•** `SHA3-384`

**•** `SHA3-512`

**•** `SHA-256`

**•** `SHA-512`

```
   input
```

Type: Blob

The content for which you want to generate the digest.

Return Value

Type: Blob

Contains the generated digest.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestGenerateDigest {

        public void testGenerateDigest(){

           Blob targetBlob = Blob.valueOf('ExampleMD5String');

           Blob hash = Crypto.generateDigest('MD5', targetBlob);

           String result = EncodingUtil.base64Encode(hash);

           System.debug('Value: ' + result);

        }

      }

```

To invoke this method, run the following:

```
   TestGenerateDigest tgd = new TestGenerateDigest();

   tgd.testGenerateDigest();

##### **`generateMac(algorithmName, input, privateKey)`**

```

Computes a message authentication code (MAC) for the _`input`_ blob value using the private key and the specified algorithm.


Apex Reference Guide Crypto Class

Signature

```
   public static Blob generateMac(String algorithmName, Blob input, Blob privateKey)

```

Parameters

```
   algorithmName
```

Type: String

These are valid values for _`algorithmName`_ .

**•** `hmacMD5`

**•** `hmacSHA1`

**•** `hmacSHA256`

**•** `hmacSHA512`

```
   input
```

Type: Blob

The content for which you want to generate the MAC.

```
   privateKey
```

Type: Blob

The key to use to generate the MAC. You may supply a private key that has been encoded using Base64 encoding. However if you
do, then you must also supply the Base64-encoded private key when verifying the MAC using the `verifyHMac` method. The
value of _`privateKey`_ can’t exceed 4 KB.

Return Value

Type: Blob

The message authentication code.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestGenerateMAC {

        public void testGenerateMAC() {

           String salt = String.valueOf(Crypto.getRandomInteger());

           String key = 'key';

           Blob data = crypto.generateMac('HmacSHA256',

                              Blob.valueOf(salt),

                              Blob.valueOf(key));

           System.debug('Generated MAC: ');

           System.debug(EncodingUtil.base64Encode(data));

        }

      }

```

To invoke this method, run the following:

```
   TestGenerateMAC tgm = new TestGenerateMAC();

   tgm.testGenerateMAC();

```


Apex Reference Guide Crypto Class

##### **`getRandomInteger()`**

Returns a random integer value.

Signature

```
   public static Integer getRandomInteger()

```

Return Value

Type: Integer

Returns a random 4-byte integer. Salesforce invokes the `java.security.SecureRandom` api to generate this number. For
[information on how the number is generated, see java.security.SecureRandom.](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/security/SecureRandom.html)

Example

[You can use your preferred Salesforce development environment to exercise this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestGetRandomInteger {

        public void testGetRandomInteger() {

           Integer i1 = Crypto.getRandomInteger();

           Integer i2 = Crypto.getRandomInteger();

           System.debug('Integer 1: ' + i1);

           System.debug('Integer 2: ' + i2);

           Assert.areNotEqual(i1, i2, 'Sorry, those aren’t random!');

           //This is just an example. This is not a true test of randomness

        }

      }

```

To invoke this method, run the following:

```
   TestGetRandomInteger tri = new TestGetRandomInteger();

   tri.testGetRandomInteger();

```

SEE ALSO:

[java.security.SecureRandom](https://docs.oracle.com/javase%2F9%2Fdocs%2Fapi%2F%2F/java/security/SecureRandom.html)

##### **`getRandomLong()`**

Returns a random long value.

Signature

```
   public static Long getRandomLong()

```

Return Value

Type: Long

Returns a random 8-byte long. Salesforce invokes the `java.security.SecureRandom` api to generate this number. For
[information on how the number is generated, see java.security.SecureRandom.](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/security/SecureRandom.html)


Apex Reference Guide Crypto Class

Example

[You can use your preferred Salesforce development environment to exercise this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestGetRandomLong {

        public void testGetRandomLong() {

           Long L1 = Crypto.getRandomLong();

           Long L2 = Crypto.getRandomLong();

           System.debug('Long 1: ' + L1);

           System.debug('Long 2: ' + L2);

           Assert.areNotEqual(L1, L2, 'Sorry, not random!');

           //This is just an example. This is not a true test of randomness

        }

      }

```

To invoke this method, run the following:

```
   TestGetRandomLong trl = new TestGetRandomLong();

   trl.testGetRandomLong();

```

SEE ALSO:

[java.security.SecureRandom](https://docs.oracle.com/javase%2F9%2Fdocs%2Fapi%2F%2F/java/security/SecureRandom.html)

##### **`sign(algorithmName, input, privateKey)`**

Computes a unique digital signature for the _`input`_ blob value, using the specified algorithm and the supplied private key.

Signature

```
   public static Blob sign(String algorithmName, Blob input, Blob privateKey)

```

Parameters

```
   algorithmName
```

Type: String

```
   input
```

signWithCertificate supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

Type: Blob

The data to sign.

```
   privateKey
```

Type: Blob

The key to use for signing. The value of _`privateKey`_ must be decoded using the `EncodingUtilbase64Decode` method,
[and should be in RSA's PKCS #8 (1.2) Private-Key Information Syntax Standard form. The value can’t exceed 4 KB.](https://datatracker.ietf.org/doc/html/rfc5958)

Return Value

Type: Blob


Apex Reference Guide Crypto Class

The new digital signature.

Example

[You can use your preferred Salesforce development environment to test this function. To run it correctly, you need a PKCS8 private key.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
At your terminal, use `openssl` to create one. First, create the key. Then convert it to PKCS8:

```
   $ openssl genrsa -out myprivatekey.pem 1024

   $ openssl pkey -in myprivatekey.pem -out myprivatekey.pkcs8.pem

```

After you create the PKCS8 compatible key, you decode just the key portion of the text (without the BEGIN PRIVATE KEY or END PRIVATE
KEY lines) for the _`privateKey`_ parameter.

```
      public class TestSign {

        public void testSign() {

             Blob input = Blob.valueOf('Some text.');

             String algorithmName = 'RSA';

             String rawKey = '<text value of your pkcs8 private key>';

             //no BEGIN PRIVATE KEY or END PRIVATE KEY header/footer !

             Blob privateKey = EncodingUtil.base64Decode(rawKey);

             System.debug(privateKey);

             Blob signedKey = Crypto.sign(algorithmName, input, privateKey);

        }

      }

```

To invoke this method, run the following:

```
   TestSign ts = new TestSign();

   ts.testSign();

##### **`signWithCertificate(algorithmName, input, certDevName)`**

```

Computes a unique digital signature for the input blob value, using the specified algorithm and the supplied certificate and key pair.

Signature

```
   public static Blob signWithCertificate(String algorithmName, Blob input, String

   certDevName)

```

Parameters

```
   algorithmName
```

Type: String

signWithCertificate supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

```
   input
```

Type: Blob

The data to sign.


Apex Reference Guide Crypto Class

```
   certDevName
```

Type: String

The value listed in the `Unique Name` field for a certificate stored in the Salesforce org’s Certificate and Key Management page
to use for signing.

To access the Certificate and Key Management page from Setup, enter _`Certificate and Key Management`_ in the **Quick**
**Find** box, then select **Certificate and Key Management** .

Return Value

Type: Blob

The signed content.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
_`TestCertName`_ variable, use the unique name value for a self-signed or CA certificate that you have created in the org in which you
run this test.

```
      public class TestSignWithCert {

        public void testSignWithCert() {

           String algorithmName = 'RSA';

           Blob input = Blob.valueOf('Test Sign With Certificate.');

           String TestCertName = ' your-cert-unique-name ';

          Blob signedKey = Crypto.signWithCertificate(algorithmName, input, TestCertName);

        }

      }

```

To invoke the method, run the following:

```
   TestSignWithCert tswc = new TestSignWithCert();

   tswc.testSignWithCert();

##### **`signXML(algorithmName, node, idAttributeName, certDevName)`**

```

Envelops the signature into an XML document.

Signature

```
   public Void signXML(String algorithmName, Dom.XmlNode node, String idAttributeName,

   String certDevName)

```

Parameters

```
   algorithmName
```

Type: String

signWithCertificate supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.


Apex Reference Guide Crypto Class

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

```
   node
```

Type: Dom.XmlNode

The XML node to sign and insert the signature into.

```
   idAttributeName
```

Type: String

The full name (including the namespace) of the attribute on the node (XmlNode) to use as the reference ID. If `null`, this method
uses the `ID` attribute on the node. If there’s no `ID` attribute, Salesforce generates a new ID and adds it to the node.

```
   certDevName
```

Type: String

The unique name for a certificate stored in the Salesforce org’s Certificate and Key Management page to use for signing.

To access the Certificate and Key Management page from Setup, enter _`Certificate and Key Management`_ in the **Quick**
**Find** box, then select **Certificate and Key Management** .

Return Value

Type: void

This method doesn’t return a value. The signature envelope is inserted within _`node`_ .

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
_`testCertName`_ variable, use the unique name value for a self-signed or CA certificate that you have created in the org in which you
run this test.

```
     public class TestSignXML {

      public void testSignXML() {

       String algorithmName = 'RSA';

       String testCertName = ' your-cert-unique-name ';

       Dom.Document doc = new Dom.Document();

       String docToLoad = '<?xml version=\"1.0\"?>\n' +

       '<customers>\n' +

       ' <customer id="2">\n' +

       ' <name>Company One</name>\n' +

       ' </customer>\n' +

       '</customers>';

       doc.load(docToLoad);

       System.Crypto.signXML(algorithmName, doc.getRootElement(), null, testCertName);

       //dump the content of the signed XML document to the debug log

       System.Debug(doc.toXmlString());

      }

     }

```

To invoke this method, run the following:

```
   TestSignXML tswxml = new TestSignXML();

   tswxml.testSignXML();

```


Apex Reference Guide Crypto Class

##### **`signXML(algorithmName, node, idAttributeName, certDevName, refChild)`**

Inserts the signature envelope before the specified child node.

Signature

```
   public static void signXml(String algorithmName, Dom.XmlNode node, String

   idAttributeName, String certDevName, Dom.XmlNode refChild)

```

Parameters

```
   algorithmName
```

Type: String

signWithCertificate supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

```
   node
```

Type: Dom.XmlNode

The XML node to sign and insert the signature into.

```
   idAttributeName
```

Type: String

The full name (including the namespace) of the attribute on the node (XmlNode) to use as the reference ID. If `null`, this method
uses the `ID` attribute on the node. If there’s no `ID` attribute, Salesforce generates a new ID and adds it to the node.

```
   certDevName
```

Type: String

The unique name for a certificate stored in the Salesforce org’s Certificate and Key Management page to use for signing.

To access the Certificate and Key Management page from Setup, enter _`Certificate and Key Management`_ in the **Quick**
**Find** box, then select **Certificate and Key Management** .

```
   refChild
```

Dom.XmlNode

The XML node before which to insert the signature. If _`refChild`_ is `null`, the signature is added at the end.

Return Value

Type: Void

This method doesn’t return a value. The signature envelope is inserted within _`node`_ .

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
_`testCertName`_ variable, use the unique name value for a self-signed or CA certificate that you have created in the org in which you
run this test.

```
      public class TestSignXML_2 {

        public void testSignXML_2() {

           String algorithmName = 'RSA';

           String testCertName = ' your-cert-unique-name ';

```


Apex Reference Guide Crypto Class

```
           Dom.Document doc = new Dom.Document();

           String docToLoad = '<?xml version="1.0"?>\n' +

           '<customers>\n' +

           ' <customer id="2">\n' +

           ' <name>Company One</name>\n' +

           ' </customer>\n' +

           '</customers>';

           doc.load(docToLoad);

           Dom.XmlNode rootNode = doc.getRootElement();

           Dom.XmlNode commentNode = rootNode.addCommentNode('SomeComment');

          System.Crypto.signXML(algorithmName, doc.getRootElement(), null, testCertName,

    commentNode);

           //send the content of the signed XML document to the debug log

           System.Debug(doc.toXmlString());

        }

      }

```

To invoke this method, run the following:

```
   TestSignXML_2 tswxml2 = new TestSignXML_2();

   tswxml2.testSignXML_2();

##### **`verify(algorithmName, data, signature, publicKey)`**

```

Verifies the digital signature for the _`data`_ blob using the specified algorithm and the supplied public key. Use this method to verify a
blob signed by a digital signature created using a third-party application or the sign method.

Signature

```
   public static Boolean verify(String algorithmName, Blob data, Blob signature, Blob

   publicKey)

```

Parameters

```
   algorithmName
```

Type: String

verify supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

```
   data
```

Type: Blob

The data to sign.

```
   signature
```

Type:

Blob

The RSA or EDSA-compliant signature.


Apex Reference Guide Crypto Class

```
   publicKey
```

Type: Blob

The value of _`publicKey`_ must be decoded using the `EncodingUtilbase64Decode` method, and be in X.509 standard
format.

Return Value

Type: Boolean

`true` if and only if the signature is successfully verified.

Example

[You can use your preferred Salesforce development environment to test this function. To run it correctly, you must:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

**•** generate an X.509 private key and public certificate

**•** convert the private key to PKCS8

**•** extract the public key from the public certificate

You provide the private PKCS8 key to the `sign` method, and the extracted public key to the `verify` method (along with the signature
you generate with `sign` .

At your terminal, use `openssl` to create the X.509 key pair:

```
   $ openssl req -x509 -newkey rsa:2048 -keyout myPriv509.key -out myPub509.cert -days 365

```

Convert the private key to PKCS8:

```
   openssl pkey -in myPriv509.key -out myPriv509pkcs8.pem

```

Extract the public key from `myPub509.cert` :

```
   openssl x509 -in myPub509.cert -inform pem -pubkey -out myPub509.pem

```

After you create the `myPub509.pem` key, you decode just the key portions of the text (without the BEGIN PRIVATE KEY or END PRIVATE
KEY lines) for both the _`privateKey`_ and _`publicKey`_ parameters.

```
      public class TestVerify {

        public void testVerify() {

           String algorithmName = 'RSA';

           Blob input = Blob.valueOf('Here is some text.');

           //contents of myPriv509pkcs8.pem

           String myPriv509pkcs8 = ' contents of myPriv509pkcs8.pem ';

           Blob privateKey = EncodingUtil.base64Decode(myPriv509pkcs8);

           Blob signature = Crypto.sign(algorithmName, input, privateKey);

           //contents of myPub509.pem

           String publicKeyTxt64 = ' contents of myPub509.pem ';

           Blob publicKey = EncodingUtil.base64Decode(publicKeyTxt64);

           Boolean verified = false;

```


Apex Reference Guide Crypto Class

```
           verified = Crypto.verify(algorithmName, input, signature, publicKey);

           Assert.areEqual(true, verified);

       }

     }

```

To invoke, run the following:

```
   TestVerify tv = new TestVerify();

   tv.testVerify();

```

SEE ALSO:

[X.509 Standard](https://www.itu.int/rec/T-REC-X.509)

##### **`verify(algorithmName, data, signature, certDevName)`**

Verifies the digital signature for the _`data`_ blob using the specified algorithm and the public key associated with _`certDevName`_ . Use
this method to verify a blob signed by a digital signature created using a third-party application or the `signWithCertificate`
method.

Signature

```
   public static Boolean verify(String algorithmName, Blob data, Blob signature, String

   certDevName)

```

Parameters

```
   algorithmName
```

Type: String

verify supports all these values for _`algorithmName`_ . See Crypto Class for details on each algorithm.

`RSA`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA384`, `RSA-SHA512`, `ECDSA-SHA256`, `ECDSA-SHA256-PLAIN`,
`ECDSA-SHA384`, and `ECDSA-SHA512`

```
   data
```

Type: Blob

The data to sign.

```
   signature
```

Type:

Blob

The RSA or ECDSA signature.

```
   certDevName
```

Type: String

The value listed in the `Unique Name` field for a certificate stored in the Salesforce organization’s Certificate and Key Management
page to use for signing.

To access the Certificate and Key Management page from Setup, enter _`Certificate and Key Management`_ in the **Quick**
**Find** box, then select **Certificate and Key Management** .


Apex Reference Guide Crypto Class

Return Value

Type: Boolean

Returns `true` if the signature is successfully verified.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
_`TestCertName`_ variable, use the unique name value for a self-signed or CA certificate that you have created in the org in which you
run this test.

```
      public class TestVerify_2 {

        public void testVerify_2() {

          String algorithmName = 'RSA';

          Blob input = Blob.valueOf('Test Sign With Certificate.');

          String TestCertName = ' your-cert-unique-name ';

         Blob signedKey = Crypto.signWithCertificate(algorithmName, input, TestCertName);

          Boolean verified = false;

          verified = Crypto.verify(algorithmName, input, signedKey, TestCertName);

          Assert.areEqual(true, verified);

        }

     }

```

To invoke this method, run the following:

```
   TestVerify_2 tv_2 = new TestVerify_2();

   tv_2.testVerify_2();

##### **`verifyHMac(algorithmName, data, privateKey, macToVerify)`**

```

Verifies the HMAC signature for the _`data`_ blob using the specified algorithm, input data, private key, and the mac. Use this method to
verify a blob signed by a digital signature created using a third-party application or the sign method.

Signature

```
   public static Boolean verifyHMac(String algorithmName, Blob data, Blob privateKey, Blob

   macToVerify)

```

Parameters

```
   algorithmName
```

Type: String

These are valid values for _`algorithmName`_ .

**•** `hmacMD5`

**•** `hmacSHA1`

**•** `hmacSHA256`

**•** `hmacSHA512`


### Apex Reference Guide Custom Metadata Type Methods

```
   data
```

Type: Blob

The data to sign.

```
   privateKey
```

Type: Blob

If the private key used to generate the MAC was Base64 encoded, then the value of _`privateKey`_ must also be Base64 encoded.
The value cannot exceed 4 KB.

```
   hmacToVerify
```

Type: Blob

The value of the mac must be verified against the provided _`privateKey`_, _`data`_, and _`algorithmName`_ .

Return Value

Type: Boolean

The verification status of the data to verify.

Example

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

```
      public class TestVerifyMAC {

        public void testVerifyMAC() {

           String salt = String.valueOf(Crypto.getRandomInteger());

           String key = 'key';

           Blob data = crypto.generateMac('HmacSHA256',

             Blob.valueOf(salt),

             Blob.valueOf(key));

           System.debug('Generated MAC: ');

           System.debug(EncodingUtil.base64Encode(data));

           Boolean verified = false;

         verified = Crypto.verifyHMac('HmacSHA256', Blob.valueOf(salt), Blob.valueOf(key),

    data);

           Assert.areEqual(true, verified);

        }

      }

```

To invoke this method, run the following:

```
   TestVerifyMAC tvm = new TestVerifyMAC();

   tvm.testVerifyMAC();

### Custom Metadata Type Methods

```

Custom metadata types are customizable, deployable, packageable, and upgradeable application metadata. All custom metadata is
exposed in the application cache, which allows access without repeated queries to the database. The metadata is then available for
formula fields, validation rules, flows, Apex, and SOAP API. All methods are static.


Apex Reference Guide Custom Metadata Type Methods

Usage

Custom metadata types methods are instance type methods and are called by and operate on a specific instance of a custom metadata
type.

Custom Metadata Types Example

#### The following example uses the getAll() method. The custom metadata type named Games has a field called GameType__c .

This example determines if the field value of the first record is equal to the string _`PC`_ .

```
   List<Games__mdt> mcs = Games__mdt.getAll().values();

   boolean textField = null;

   if (mcs[0].GameType__c == 'PC') {

     textField = true;

   }

   system.assertEquals(textField, true);

```

IN THIS SECTION:

#### getAll()

Returns a map containing custom metadata records for the specific custom metadata type. The map keys are the record
DeveloperNames and the map values are the record sObjects.

getInstance(recordId)
Returns a single custom metadata type record sObject for a specified record ID. Returns null if no record matches the parameter.

getInstance(developerName)
Returns a single custom metadata type record sObject for a specified developerName field of the custom metadata type object.
Returns null if no record matches the parameter.

getInstance(qualifiedApiName)
Returns a single custom metadata type record sObject for a qualified API name. Returns null if no record matches the parameter.

#### getAll()

Returns a map containing custom metadata records for the specific custom metadata type. The map keys are the record DeveloperNames
and the map values are the record sObjects.

Signature

```
   public Map<String, CustomMetadataType__mdt> getAll()

```

Return Value

Type: `Map<String, CustomMetadataType__mdt>`

Usage

If no records are defined for the type, this method returns an empty map. To iterate over the list of custom metadata type record sObjects,
#### use getAll().values() . Only the first 255 characters are returned for any field in a custom metadata type record, so longer text

fields get truncated. If you want all the field data from a custom metadata type record, use a SOQL query.


Apex Reference Guide Custom Metadata Type Methods

Example

This sample returns a map of all the records for a custom metadata type named `Games__mdt` .

```
   Map<String, Games__mdt> mcs = Games__mdt.getAll();

#### getInstance(recordId)

```

Returns a single custom metadata type record sObject for a specified record ID. Returns null if no record matches the parameter.

Signature

```
   public CustomMetadataType__mdt getInstance(recordId)

```

Parameters

```
   recordId
```

Type: String

Return Value

Type: `CustomMetadataType__mdt`

Usage

Use this method to explicitly retrieve custom metadata type information at the user level. Only the first 255 characters of any field in a
custom metadata type record are returned. Therefore, fields such as long text fields can be truncated. If you want all the field data from
a custom metadata type record, use a SOQL query.

Example

This sample returns a single record sObject for the custom metadata type named `Games_mdt` with _`recordID`_ specified as
`m00000000000001` .

```
   Games__mdt mc = Games__mdt.getInstance('m00000000000001');

#### getInstance(developerName)

```

Returns a single custom metadata type record sObject for a specified developerName field of the custom metadata type object. Returns
null if no record matches the parameter.

Signature

```
   public CustomMetadataType__mdt getInstance(String developerName)

```

Parameters

```
   developerName
```

Type: String


Apex Reference Guide Custom Metadata Type Methods

Return Value

Type: `CustomMetadataType__mdt`

Usage

Use this method to return a single custom metadata type record for the specified _`developerName`_ . The _`developerName`_ is the
unique name of the custom metadata type object in the API. Only the first 255 characters of any field in a custom metadata type record
are returned. Therefore, fields such as long text fields can be truncated. If you want all the field data from a custom metadata type record,
use a SOQL query.

Example

Returns a single record sObject for the custom metadata type named `Games_mdt` with _`developerName`_ specified as
`FirstRecord` .

```
   Games__mdt mc = Games__mdt.getInstance('FirstRecord');

#### getInstance(qualifiedApiName)

```

Returns a single custom metadata type record sObject for a qualified API name. Returns null if no record matches the parameter.

Signature

```
   public CustomMetadataType__mdt getInstance(String qualifiedApiName)

```

Parameters

```
   qualifiedApiName
```

Type: String

Return Value

Type: `CustomMetadataType__mdt`

Usage

Use this method to return a single custom metadata type record for the specified _`qualifiedApiName`_ . The _`qualifiedApiName`_
is a concatenation of the namespace prefix and developerName, and has this format: _`namespacePrefix__developerName`_ .
The developerName is the unique name of the custom metadata type object in the API. Only the first 255 characters of any field in a
custom metadata type record are returned. Therefore, fields such as long text fields can be truncated. If you want all the field data from
a custom metadata type record, use a SOQL query.

Example

This sample returns a single record sObject for the custom metadata type named `Games_mdt` with _`qualifiedApiName`_ specified
as `MyNamespace__FirstRecord` .

```
   Games__mdt mc = Games__mdt.getInstance('MyNamespace__FirstRecord');

```


### Apex Reference Guide Custom Settings Methods Custom Settings Methods

Custom settings are similar to custom objects and enable application developers to create custom sets of data, as well as create and
associate custom data for an organization, profile, or specific user. All custom settings data is exposed in the application cache, which
enables efficient access without the cost of repeated queries to the database. This data is then available for formula fields, validation
rules, flows, Apex, and the SOAP API.

Usage

Custom settings methods are all instance methods, that is, they are called by and operate on a specific instance of a custom setting.
There are two types of custom settings: hierarchy and list. There are two types of methods: methods that work with list custom settings,
and methods that work with hierarchy custom settings.

Note: All custom settings data is exposed in the application cache, which enables efficient access without the cost of repeated
queries to the database. However, querying custom settings data using Standard Object Query Language (SOQL) doesn't use the
application cache and is similar to querying a custom object. To benefit from caching, use other methods for accessing custom
settings data such as the Apex Custom Settings methods.

For more information on creating custom settings in the Salesforce user interface, see “Create Custom Settings” in the Salesforce online
help.

Custom Setting Examples

The following example uses a list custom setting called `Games` . The `Games` setting has a field called `GameType` . This example
determines if the value of the first data set is equal to the string `PC` .

```
   List<Games__C> mcs = Games__c.getall().values();

   boolean textField = null;

   if (mcs[0].GameType__c == 'PC') {

     textField = true;

   }

   system.assertEquals(textField, true);

```

The following example uses a custom setting called `Foundation_Countries` . This example demonstrates that the `getValues`
and `getInstance` methods return identical values.

```
   Foundation_Countries__c myCS1 = Foundation_Countries__c.getValues('United States');

   String myCCVal = myCS1.Country_code__c;

   Foundation_Countries__c myCS2 = Foundation_Countries__c.getInstance('United States');

   String myCCInst = myCS2.Country_code__c;

   system.assertEquals(myCCinst, myCCVal);

```

Hierarchy Custom Setting Examples

In the following example, the hierarchy custom setting GamesSupport has a field called `Corporate_number` . The code returns the
value for the profile specified with `pid` .

```
   GamesSupport__c mhc = GamesSupport__c.getInstance(pid);

   string mPhone = mhc.Corporate_number__c;

```

The example is identical if you choose to use the `getValues` method.


Apex Reference Guide Custom Settings Methods

The following example shows how to use hierarchy custom settings methods. For `getInstance`, the example shows how field values
that aren't set for a specific user or profile are returned from fields defined at the next lowest level in the hierarchy. The example also
shows how to use `getOrgDefaults` .

Finally, the example demonstrates how `getValues` returns fields in the custom setting record only for the specific user or profile,
and doesn't merge values from other levels of the hierarchy. Instead, `getValues` returns `null` for any fields that aren't set. This
example uses a hierarchy custom setting called Hierarchy. Hierarchy has two fields: `OverrideMe` and `DontOverrideMe` . In
addition, a user named Robert has a System Administrator profile. The organization, profile, and user settings for this example are as
follows:

**Organization settings**
`OverrideMe` : Hello

`DontOverrideMe` : World

**Profile settings**
`OverrideMe` : Goodbye

`DontOverrideMe` is not set.

**User settings**
`OverrideMe` : Fluffy

`DontOverrideMe` is not set.

The following example demonstrates the result of the `getInstance` method when Robert calls it in his organization:

```
   Hierarchy__c CS = Hierarchy__c.getInstance();

   System.Assert(CS.OverrideMe__c == 'Fluffy');

   System.assert(CS.DontOverrideMe__c == 'World');

```

If Robert passes his user ID specified by `RobertId` to `getInstance`, the results are the same. The identical results are because the
lowest level of data in the custom setting is specified at the user level.

```
   Hierarchy__c CS = Hierarchy__c.getInstance(RobertId);

   System.Assert(CS.OverrideMe__c == 'Fluffy');

   System.assert(CS.DontOverrideMe__c == 'World');

```

If Robert passes the System Administrator profile ID specified by `SysAdminID` to `getInstance`, the result is different. The data
specified for the profile is returned:

```
   Hierarchy__c CS = Hierarchy__c.getInstance(SysAdminID);

   System.Assert(CS.OverrideMe__c == 'Goodbye');

   System.assert(CS.DontOverrideMe__c == 'World');

```

When Robert tries to return the data set for the organization using `getOrgDefaults`, the result is:

```
   Hierarchy__c CS = Hierarchy__c.getOrgDefaults();

   System.Assert(CS.OverrideMe__c == 'Hello');

   System.assert(CS.DontOverrideMe__c == 'World');

```

By using the `getValues` method, Robert can get the hierarchy custom setting values specific to his user and profile settings. For
example, if Robert passes his user ID `RobertId` to `getValues`, the result is:

```
   Hierarchy__c CS = Hierarchy__c.getValues(RobertId);

   System.Assert(CS.OverrideMe__c == 'Fluffy');

   // Note how this value is null, because you are returning

   // data specific for the user

   System.assert(CS.DontOverrideMe__c == null);

```


Apex Reference Guide Custom Settings Methods

If Robert passes his System Administrator profile ID `SysAdminID` to `getValues`, the result is:

```
   Hierarchy__c CS = Hierarchy__c.getValues(SysAdminID);

   System.Assert(CS.OverrideMe__c == 'Goodbye');

   // Note how this value is null, because you are returning

   // data specific for the profile

   System.assert(CS.DontOverrideMe__c == null);

```

Country and State Code Custom Settings Example

This example illustrates using two custom setting objects for storing related information, and a Visualforce page to display the data in
a set of related picklists.

In the following example, country and state codes are stored in two different custom settings: Foundation_Countries and
Foundation_States.

The Foundation_Countries custom setting is a list type custom setting and has a single field, `Country_Code` .

The Foundation_States custom setting is also a List type of custom setting and has the following fields:

**•** `Country Code`

**•** `State Code`

**•** `State Name`


Apex Reference Guide Custom Settings Methods

The Visualforce page shows two picklists: one for country and one for state.

```
   <apex:page controller="CountryStatePicker">

     <apex:form >

       <apex:actionFunction name="rerenderStates" rerender="statesSelectList" >

         <apex:param name="firstParam" assignTo="{!country}" value="" />

       </apex:actionFunction>

     <table><tbody>

       <tr>

        <th>Country</th>

         <td>

           <apex:selectList id="country" styleclass="std" size="1"

             value="{!country}" onChange="rerenderStates(this.value)">

               <apex:selectOptions value="{!countriesSelectList}"/>

           </apex:selectList>

         </td>

       </tr>

       <tr id="state_input">

        <th>State/Province</th>

         <td>

           <apex:selectList id="statesSelectList" styleclass="std" size="1"

              value="{!state}">

               <apex:selectOptions value="{!statesSelectList}"/>

           </apex:selectList>

         </td>

       </tr>

     </tbody></table>

     </apex:form>

   </apex:page>

```


Apex Reference Guide Custom Settings Methods

The Apex controller `CountryStatePicker` finds the values entered into the custom settings, then returns them to the Visualforce
page.

```
   public with sharing class CountryStatePicker {

   // Variables to store country and state selected by user

      public String state { get; set; }

      public String country {get; set;}

      // Generates country dropdown from country settings

      public List<SelectOption> getCountriesSelectList() {

        List<SelectOption> options = new List<SelectOption>();

        options.add(new SelectOption('', '-- Select One --'));

        // Find all the countries in the custom setting

        Map<String, Foundation_Countries__c> countries = Foundation_Countries__c.getAll();

        // Sort them by name

        List<String> countryNames = new List<String>();

        countryNames.addAll(countries.keySet());

        countryNames.sort();

        // Create the Select Options.

        for (String countryName : countryNames) {

           Foundation_Countries__c country = countries.get(countryName);

           options.add(new SelectOption(country.country_code__c, country.Name));

        }

        return options;

      }

      // To generate the states picklist based on the country selected by user.

      public List<SelectOption> getStatesSelectList() {

        List<SelectOption> options = new List<SelectOption>();

        // Find all the states we have in custom settings.

        Map<String, Foundation_States__c> allstates = Foundation_States__c.getAll();

        // Filter states that belong to the selected country

       Map<String, Foundation_States__c> states = new Map<String, Foundation_States__c>();

        for(Foundation_States__c state : allstates.values()) {

           if (state.country_code__c == this.country) {

             states.put(state.name, state);

           }

        }

        // Sort the states based on their names

        List<String> stateNames = new List<String>();

        stateNames.addAll(states.keySet());

        stateNames.sort();

        // Generate the Select Options based on the final sorted list

        for (String stateName : stateNames) {

           Foundation_States__c state = states.get(stateName);

           options.add(new SelectOption(state.state_code__c, state.state_name__c));

```


Apex Reference Guide Custom Settings Methods

```
        }

        // If no states are found, just say not required in the dropdown.

        if (options.size() > 0) {

           options.add(0, new SelectOption('', '-- Select One --'));

        } else {

           options.add(new SelectOption('', 'Not Required'));

        }

        return options;

      }

   }

```

IN THIS SECTION:

#### List Custom Setting Methods

Hierarchy Custom Setting Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_customsettings.htm)_ : Custom Settings

#### List Custom Setting Methods

The following are instance methods for list custom settings.

IN THIS SECTION:

##### getAll()

Returns a map of the data sets defined for the custom setting.

getInstance(dataSetName)
Returns the custom setting data set record for the specified data set name. This method returns the exact same object as
`getValues(` _**`dataSetName`**_ `)` .

getValues(dataSetName)
Returns the custom setting data set record for the specified data set name. This method returns the exact same object as
`getInstance(` _**`dataSetName`**_ `)` .

##### getAll()

Returns a map of the data sets defined for the custom setting.

Signature

```
   public Map<String, CustomSetting__c> getAll()

```

Return Value

Type: Map<String, CustomSetting__c>


Apex Reference Guide Custom Settings Methods

Usage

If no data set is defined, this method returns an empty map.

Note: For Apex saved using Salesforce API version 20.0 or earlier, the data set names, which are the keys in the returned map, are
converted to lower case. For Apex saved using Salesforce API version 21.0 and later, the case of the data set names in the returned
map keys is not changed and the original case is preserved.

##### getInstance(dataSetName)

Returns the custom setting data set record for the specified data set name. This method returns the exact same object as
##### getValues( dataSetName ) .

Signature

```
   public CustomSetting__c getInstance(String dataSetName)

```

Parameters

```
   dataSetName
```

Type: String

Return Value

Type: CustomSetting__c

Usage

If no data is defined for the specified data set, this method returns `null` .

##### getValues(dataSetName)

Returns the custom setting data set record for the specified data set name. This method returns the exact same object as
##### getInstance( dataSetName ) .

Signature

```
   public CustomSetting__c getValues(String dataSetName)

```

Parameters

```
   dataSetName
```

Type: String

Return Value

Type: CustomSetting__c

Usage

If no data is defined for the specified data set, this method returns `null` .


Apex Reference Guide Custom Settings Methods

#### Hierarchy Custom Setting Methods

The following are instance methods for hierarchy custom settings.

Note:

**•** In API version 41.0 and below, each method in an Apex test class, including `testSetup` methods, are able to insert hierarchy
custom setting values. This behavior is true even when the methods have the same `SetupOwnerId` value as a hierarchy
custom setting record inserted in a different test method.

**•** In API version 42.0 and later, if a hierarchy custom setting is inserted in a `testSetup` method, inserting a hierarchy custom
setting record with the same `SetupOwnerId` in a test method throws a `DUPLICATE_VALUE` exception.

IN THIS SECTION:

##### getInstance()

Returns a custom setting data set record for the current user. The fields returned in the custom setting record are merged based on
the lowest level fields that are defined in the hierarchy.

getInstance(userId)
Returns the custom setting data set record for the specified user ID. The lowest level custom setting record and fields are returned.
Use this when you want to explicitly retrieve data for the custom setting at the user level.

getInstance(profileId)
Returns the custom setting data set record for the specified profile ID. The lowest level custom setting record and fields are returned.
Use this when you want to explicitly retrieve data for the custom setting at the profile level.

getOrgDefaults()
Returns the custom setting data set record for the organization.

getValues(userId)
Returns the custom setting data set record for the specified user ID.

getValues(profileId)
Returns the custom setting data set for the specified profile ID.

##### getInstance()

Returns a custom setting data set record for the current user. The fields returned in the custom setting record are merged based on the
lowest level fields that are defined in the hierarchy.

Signature

```
   public CustomSetting__c getInstance()

```

Return Value

Type: CustomSetting__c

Usage

If no custom setting data is defined for the user, this method returns a new custom setting object. The new custom setting object
contains an ID set to `null` and merged fields from higher in the hierarchy. You can add this new custom setting record for the user


Apex Reference Guide Custom Settings Methods

by using `insert` or `upsert` . If no custom setting data is defined in the hierarchy, the returned custom setting has empty fields, except
for the `SetupOwnerId` field which contains the user ID.

Note: For Apex saved using Salesforce API version 21.0 or earlier, this method returns the custom setting data set record with
fields merged from field values defined at the lowest hierarchy level, starting with the user. Also, if no custom setting data is defined
in the hierarchy, this method returns `null` .

This method is equivalent to a method call to `getInstance(User_Id)` for the current user.

Example

**•** Custom setting data set defined for the user: If you have a custom setting data set defined for the user “Uriel Jones,” for the profile
“System Administrator,” and for the organization as a whole, and the user running the code is Uriel Jones, this method returns the
custom setting record defined for Uriel Jones.

**•** Merged fields: If you have a custom setting data set with fields A and B for the user “Uriel Jones” and for the profile “System
Administrator,” and field A is defined for Uriel Jones, field B is `null` but is defined for the System Adminitrator profile, this method
returns the custom setting record for Uriel Jones with field A for Uriel Jones and field B from the System Administrator profile.

**•** No custom setting data set record defined for the user: If the current user is “Barbara Mahonie,” who also shares the “System
Administrator” profile, but no data is defined for Barbara as a user, this method returns a new custom setting record with the ID set
to `null` and with fields merged based on the fields defined in the lowest level in the hierarchy.

##### getInstance(userId)

Returns the custom setting data set record for the specified user ID. The lowest level custom setting record and fields are returned. Use
this when you want to explicitly retrieve data for the custom setting at the user level.

Signature

```
   public CustomSetting__c getInstance(ID userId)

```

Parameters

```
   userId
```

Type: ID

Return Value

Type: CustomSetting__c

Usage

If no custom setting data is defined for the user, this method returns a new custom setting object. The new custom setting object
contains an ID set to `null` and merged fields from higher in the hierarchy. You can add this new custom setting record for the user
by using `insert` or `upsert` . If no custom setting data is defined in the hierarchy, the returned custom setting has empty fields, except
for the `SetupOwnerId` field which contains the user ID.

Note: For Apex saved using Salesforce API version 21.0 or earlier, this method returns the custom setting data set record with
fields merged from field values defined at the lowest hierarchy level, starting with the user. Also, if no custom setting data is defined
in the hierarchy, this method returns `null` .


Apex Reference Guide Custom Settings Methods

##### getInstance(profileId)

Returns the custom setting data set record for the specified profile ID. The lowest level custom setting record and fields are returned.
Use this when you want to explicitly retrieve data for the custom setting at the profile level.

Signature

```
   public CustomSetting__c getInstance(ID profileId)

```

Parameters

```
   profileId
```

Type: ID

Return Value

Type: CustomSetting__c

Usage

If no custom setting data is defined for the profile, this method returns a new custom setting record. The new custom setting object
contains an ID set to `null` and with merged fields from your organization's default values. You can add this new custom setting for
the profile by using `insert` or `upsert` . If no custom setting data is defined in the hierarchy, the returned custom setting has empty
fields, except for the `SetupOwnerId` field which contains the profile ID.

Note: For Apex saved using SalesforceAPI version 21.0 or earlier, this method returns the custom setting data set record with
fields merged from field values defined at the lowest hierarchy level, starting with the profile. Also, if no custom setting data is
defined in the hierarchy, this method returns `null` .

##### getOrgDefaults()

Returns the custom setting data set record for the organization.

Signature

```
   public CustomSetting__c getOrgDefaults()

```

Return Value

Type: CustomSetting__c

Usage

If no custom setting data is defined for the organization, this method returns an empty custom setting object.

Note: For Apex saved using Salesforce API version 21.0 or earlier, this method returns `null` if no custom setting data is defined
for the organization.

##### getValues(userId)

Returns the custom setting data set record for the specified user ID.


### Apex Reference Guide Database Class

Signature

```
   public CustomSetting__c getValues(ID userId)

```

Parameters

```
   userId
```

Type: ID

Return Value

Type: CustomSetting__c

Usage

Use this if you only want the subset of custom setting data that has been defined at the user level. For example, suppose you have a
custom setting field that has been assigned a value of "alpha" at the organizational level, but has no value assigned at the user or profile
##### level. Using getValues( UserId ) returns null for this custom setting field. getValues(profileId)

Returns the custom setting data set for the specified profile ID.

Signature

```
   public CustomSetting__c getValues(ID profileId)

```

Parameters

```
   profileId
```

Type: ID

Return Value

Type: CustomSetting__c

Usage

Use this if you only want the subset of custom setting data that has been defined at the profile level. For example, suppose you have a
custom setting field that has been assigned a value of "alpha" at the organizational level, but has no value assigned at the user or profile
level. Using `getValues(ProfileId)` returns `null` for this custom setting field.

### Database Class

Contains methods for creating and manipulating data.

Namespace

System


Apex Reference Guide Database Class

Usage

Some Database methods also exist as DML statements.

Avoid specifying an `accessLevel` parameter in the same query as a `WITH SECURITY_ENFORCED` clause. Salesforce recommends
that you specify either system mode or user mode, and remove any redundant `WITH SECURITY_ENFORCED` clauses.

SEE ALSO:

Apex DML Operations

#### Database Methods The following are methods for Database . All methods are static.

IN THIS SECTION:

convertLead(leadToConvert, allOrNone)
Converts a lead into an account and contact, as well as (optionally) an opportunity.

convertLead(leadsToConvert, allOrNone)
Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

convertLead(leadToConvert, dmlOptions)
Converts a lead into an account and contact, as well as (optionally) an opportunity.

convertLead(leadsToConvert, dmlOptions)
Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

convertLead(leadToConvert, allOrNone, accessLevel)
Converts a lead into an account and contact, as well as (optionally) an opportunity.

convertLead(leadsToConvert, allOrNone, accessLevel)
Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

convertLead(leadToConvert, dmlOptions, accessLevel)
Converts a lead into an account and contact, as well as (optionally) an opportunity.

convertLead(leadsToConvert, dmlOptions, accessLevel)
Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

countQuery(query)
Returns the number of records that a dynamic SOQL query would return when executed.

countQuery(query, accessLevel)
Returns the number of records that a dynamic SOQL query would return when executed.

countQueryWithBinds(query, bindMap, accessLevel)
Returns the number of records that a dynamic SOQL query would return when executed. Bind variables in the query are resolved
from the _`bindMap`_ Map parameter directly with the key, rather than from Apex code variables.

delete(recordToDelete, allOrNone)
Deletes an existing sObject record, such as an individual account or contact, from your organization's data.

delete(recordsToDelete, allOrNone)
Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.


Apex Reference Guide Database Class

delete(recordID, allOrNone)
Deletes existing sObject records, such as individual accounts or contacts, from your organization’s data.

delete(recordIDs, allOrNone)
Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

delete(recordToDelete, allOrNone, accessLevel)
Deletes an existing sObject record, such as an individual account or contact, from your organization's data.

delete(recordsToDelete, allOrNone, accessLevel)
Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

delete(recordID, allOrNone, accessLevel)
Deletes existing sObject records, such as individual accounts or contacts, from your organization’s data.

delete(recordIDs, allOrNone, accessLevel)
Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

deleteAsync(sobjects, callback)
Initiates requests to delete the external data that corresponds to the specified external object records. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source. Allows referencing a callback class whose `processDelete` method is called for each record after deletion.

deleteAsync(sobject, callback)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source. Allows referencing a callback class whose `processDelete` method is called after deletion.

deleteAsync(sobjects)
Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
asynchronously, as background operations, and are sent to the external systems that are defined by the external objects' associated
external data sources.

deleteAsync(sobject)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source.

deleteAsync(sobjects, callback, accessLevel)
Initiates requests to delete the external data that corresponds to the specified external object records. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source. Allows referencing a callback class whose `processDelete` method is called for each record after deletion.

deleteAsync(sobject, callback, accessLevel)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source. Allows referencing a callback class whose `processDelete` method is called after deletion.

deleteAsync(sobjects, accessLevel)
Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
asynchronously, as background operations, and are sent to the external systems that are defined by the external objects' associated
external data sources.


Apex Reference Guide Database Class

deleteAsync(sobject, accessLevel)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated
external data source.

deleteImmediate(sobjects)
Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
synchronously and are sent to the external systems that are defined by the external objects' associated external data sources. If the
Apex transaction contains pending changes, the synchronous operations can't be completed and throw exceptions.

deleteImmediate(sobject)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
synchronously and is sent to the external system that's defined by the external object's associated external data source. If the Apex
transaction contains pending changes, the synchronous operation can't be completed and throws an exception.

deleteImmediate(sobjects, accessLevel)
Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
synchronously and are sent to the external systems that are defined by the external objects' associated external data sources. If the
Apex transaction contains pending changes, the synchronous operations can't be completed and throw exceptions.

deleteImmediate(sobject, accessLevel)
Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
synchronously and is sent to the external system that's defined by the external object's associated external data source. If the Apex
transaction contains pending changes, the synchronous operation can't be completed and throws an exception.

emptyRecycleBin(recordIds)
Permanently deletes the specified records from the Recycle Bin.

emptyRecycleBin(obj)
Permanently deletes the specified sObject from the Recycle Bin.

emptyRecycleBin(listOfSObjects)
Permanently deletes the specified sObjects from the Recycle Bin.

executeBatch(batchClassObject)
Submits a batch Apex job for execution corresponding to the specified class.

executeBatch(batchClassObject, scope)
Submits a batch Apex job for execution using the specified class and scope.

getAsyncDeleteResult(deleteResult)
Retrieves the status of an asynchronous delete operation that’s identified by a `Database.DeleteResult` object.

getAsyncDeleteResult(asyncLocator)
Retrieves the result of an asynchronous delete operation based on the result’s unique identifier.

getAsyncLocator(result)
Returns the `asyncLocator` associated with the result of a specified asynchronous insert, update, or delete operation.

getAsyncSaveResult(saveResult)
Returns the status of an asynchronous insert or update operation that’s identified by a `Database.SaveResult` object.

getAsyncSaveResult(asyncLocator)
Returns the status of an asynchronous insert or update operation based on the unique identifier associated with each modification.

getCursor(query)
Creates a cursor when the specified SOQL query is executed.


Apex Reference Guide Database Class

getCursor(query, accessLevel)
Creates a cursor when the specified SOQL query is executed.

getCursorWithBinds(query, bindMap, accessLevel)
Creates a cursor when the specified SOQL query is executed.

getDeleted(sObjectType, startDate, endDate)
Returns the list of individual records that have been deleted for an sObject type within the specified start and end dates and times
and that are still in the Recycle Bin.

getPaginationCursor(query)
Creates a pagination cursor when the specified SOQL query is executed.

getPaginationCursor(query, accessLevel)
Creates a pagination cursor when the specified SOQL query is executed.

getPaginationCursorWithBinds(query, bindMap, accessLevel)
Creates a pagination cursor when the specified SOQL query is executed.

getQueryLocator(staticSoqlQueryResult)
Creates a QueryLocator object used in batch Apex or Visualforce.

getQueryLocator(query)
Creates a QueryLocator object used in batch Apex or Visualforce.

getQueryLocator(staticSoqlQueryResult, accessLevel)
Creates a QueryLocator object used in batch Apex or Visualforce.

getQueryLocator(query, accessLevel)
Creates a QueryLocator object used in batch Apex or Visualforce.

getQueryLocatorWithBinds(query, bindMap, accessLevel)
Creates a QueryLocator object used in batch Apex or Visualforce. Bind variables in the query are resolved from the _`bindMap`_ Map
parameter directly with the key, rather than from Apex code variables.

getUpdated(sobjectType, startDate, endDate)
Returns the list of individual records that have been updated for an sObject type within the specified start and end dates and times.

insert(recordToInsert, allOrNone)
Adds an sObject, such as an individual account or contact, to your organization's data.

insert(recordsToInsert, allOrNone)
Adds one or more sObjects, such as individual accounts or contacts, to your organization’s data.

insert(recordToInsert, dmlOptions)
Adds an sObject, such as an individual account or contact, to your organization's data.

insert(recordsToInsert, dmlOptions)
Adds one or more sObjects, such as individual accounts or contacts, to your organization's data.

insert(recordToInsert, allOrNone, accessLevel)
Adds an sObject, such as an individual account or contact, to your organization's data.

insert(recordsToInsert, allOrNone, accessLevel)
Adds one or more sObjects, such as individual accounts or contacts, to your organization’s data.

insert(recordToInsert, dmlOptions, accessLevel)
Adds an sObject, such as an individual account or contact, to your organization's data.


Apex Reference Guide Database Class

insert(recordsToInsert, dmlOptions, accessLevel)
Adds one or more sObjects, such as individual accounts or contacts, to your organization's data.

insertAsync(sobjects, callback)
Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

insertAsync(sobject, callback)
Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

insertAsync(sobjects)
Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

insertAsync(sobject)
Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

insertAsync(sobjects, callback, accessLevel)
Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

insertAsync(sobject, callback, accessLevel)
Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

insertAsync(sobjects, accessLevel)
Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

insertAsync(sobject, accessLevel)
Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

insertImmediate(sobjects)
Initiates requests to add external object data to the relevant external systems. The requests are executed synchronously and are sent
to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains
pending changes, the synchronous operations can't be completed and throw exceptions.

insertImmediate(sobject)
Initiates a request to add external object data to the relevant external system. The request is executed synchronously and is sent to
the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

insertImmediate(sobjects, accessLevel)
Initiates requests to add external object data to the relevant external systems. The requests are executed synchronously and are sent
to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains
pending changes, the synchronous operations can't be completed and throw exceptions.


Apex Reference Guide Database Class

insertImmediate(sobject, accessLevel)
Initiates a request to add external object data to the relevant external system. The request is executed synchronously and is sent to
the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

merge(mergeToRecord, duplicateId)
Merges the duplicate record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and reparenting
any related records. Merges only accounts, contacts, or leads.

merge(mergeToRecord, duplicateRecord)
Merges the duplicate sObject record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and
reparenting any related records.

merge(mergeToRecord, duplicateIds)
Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

merge(mergeToRecord, duplicateRecords)
Merges up to two records of the same object type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

merge(mergeToRecord, duplicateId, allOrNone)
Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.

merge(mergeToRecord, duplicateRecord, allOrNone)
Merges the duplicate sObject record into the `mergeToRecord` sObject of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records.

merge(mergeToRecord, duplicateIds, allOrNone)
Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, optionally returning any errors,
deleting the duplicates, and reparenting any related records.

merge(mergeToRecord, duplicateRecords, allOrNone)
Merges up to two records of the same object type into the `mergeToRecord` sObject record, optionally returning any errors,
deleting the duplicates, and reparenting any related records.

merge(mergeToRecord, duplicateId, accessLevel)
Merges the duplicate record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and reparenting
any related records. Merges only accounts, contacts, or leads.

merge(mergeToRecord, duplicateRecord, accessLevel)
Merges the specified duplicate sObject record into the `mergeToRecord` sObject of the same type, deleting the duplicate, and
reparenting any related records.

merge(mergeToRecord, duplicateIds, accessLevel)
Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

merge(mergeToRecord, duplicateRecords, accessLevel)
Merges up to two records of the same object type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

merge(mergeToRecord, duplicateId, allOrNone, accessLevel)
Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.


Apex Reference Guide Database Class

merge(mergeToRecord, duplicateRecord, allOrNone, accessLevel)
Merges the duplicate sObject record into the `mergeToRecord` sObject record of the same type, optionally returning any errors,
deleting the duplicate, and reparenting any related records.

merge(mergeToRecord, duplicateIds, allOrNone, accessLevel)
Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, optionally returning any errors,
deleting the duplicates, and reparenting any related records.

merge(mergeToRecord, duplicateRecords, allOrNone, accessLevel)
Merges up to two records of the same object type into the `mergeToRecord` sObject record, optionally returning any errors,
deleting the duplicates, and reparenting any related records.

query(queryString)
Creates a dynamic SOQL query at runtime.

query(queryString, accessLevel)
Creates a dynamic SOQL query at runtime.

queryWithBinds(queryString, bindMap, accessLevel)
Creates a dynamic SOQL query at runtime. Bind variables in the query are resolved from the _`bindMap`_ Map parameter directly
with the key, rather than from Apex code variables.

releaseSavepoint(databaseSavepoint)
Releases a given savepoint. All savepoints that are subsequent to the given one are also released.

rollback(databaseSavepoint)
Restores the database to the state specified by the savepoint variable. Any emails submitted since the last savepoint are also rolled
back and not sent.

setSavepoint()
Returns a savepoint variable that can be stored as a local variable, then used with the `rollback` method to restore the database
to that point.

undelete(recordToUndelete, allOrNone)
Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

undelete(recordsToUndelete, allOrNone)
Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

undelete(recordID, allOrNone)
Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

undelete(recordIDs, allOrNone)
Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

undelete(recordToUndelete, allOrNone, accessLevel)
Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

undelete(recordsToUndelete, allOrNone, accessLevel)
Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

undelete(recordID, allOrNone, accessLevel)
Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

undelete(recordIDs, allOrNone, accessLevel)
Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.


Apex Reference Guide Database Class

update(recordToUpdate, allOrNone)
Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

update(recordsToUpdate, allOrNone)
Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

update(recordToUpdate, dmlOptions)
Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

update(recordsToUpdate, dmlOptions)
Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

update(recordToUpdate, allOrNone, accessLevel)
Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

update(recordsToUpdate, allOrNone, accessLevel)
Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

update(recordToUpdate, dmlOptions, accessLevel)
Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

update(recordsToUpdate, dmlOptions, accessLevel)
Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

upsert(recordToUpsert, externalIdField, allOrNone)
Creates a new sObject record or updates an existing sObject record within a single statement, using a specified field to determine
the presence of existing objects, or the ID field if no field is specified.

upsert(recordsToUpsert, externalIdField, allOrNone)
Creates new sObject records or updates existing sObject records within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

upsert(recordToUpsert, externalIdField, allOrNone, accessLevel)
Creates a new sObject record or updates an existing sObject record within a single statement, using a specified field to determine
the presence of existing objects, or the ID field if no field is specified.

upsert(recordsToUpsert, externalIdField, allOrNone, accessLevel)
Creates new sObject records or updates existing sObject records within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

updateAsync(sobjects, callback)
Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as
background operations, and are sent to the external systems that are defined by the external objects' associated external data sources.
Allows referencing a callback class whose `processSave` method is called for each record after the remote operations are
completed.

updateAsync(sobject, callback)
Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a
background operation, and is sent to the external system that's defined by the external object's associated external data source.
Allows referencing a callback class whose `processSave` method is called after the remote operation is completed.

updateAsync(sobjects)
Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as
background operations, and are sent to the external systems that are defined by the external objects' associated external data sources.


Apex Reference Guide Database Class

updateAsync(sobject)
Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a
background operation, and is sent to the external system that's defined by the external object's associated external data source.

updateAsync(sobjects, callback, accessLevel)
Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as
background operations, and are sent to the external systems that are defined by the external objects' associated external data sources.
Allows referencing a callback class whose `processSave` method is called for each record after the remote operations are
completed.

updateAsync(sobject, callback, accessLevel)
Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a
background operation, and is sent to the external system that's defined by the external object's associated external data source.
Allows referencing a callback class whose `processSave` method is called after the remote operation is completed.

updateAsync(sobjects, accessLevel)
Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as
background operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

updateAsync(sobject, accessLevel)
Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a
background operation, and is sent to the external system that's defined by the external object's associated external data source.

updateImmediate(sobjects)
Initiates requests to update external object data on the relevant external systems. The requests are executed synchronously and are
sent to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains
pending changes, the synchronous operations can't be completed and throw exceptions.

updateImmediate(sobject)
Initiates a request to update external object data on the relevant external system. The request is executed synchronously and is sent
to the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

updateImmediate(sobjects, accessLevel)
Initiates requests to update external object data on the relevant external systems. The requests are executed synchronously and are
sent to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains
pending changes, the synchronous operations can't be completed and throw exceptions.

updateImmediate(sobject, accessLevel)
Initiates a request to update external object data on the relevant external system. The request is executed synchronously and is sent
to the external system that's defined by the external object's associated external data source. If the Apex transaction contains pending
changes, the synchronous operation can't be completed and throws an exception.

##### **`convertLead(leadToConvert, allOrNone)`**

Converts a lead into an account and contact, as well as (optionally) an opportunity.

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   Boolean allOrNone)

```


Apex Reference Guide Database Class

Parameters

```
   leadToConvert
```

Type: Database.LeadConvert

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, allOrNone)`**

Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

Signature

```
   public static Database.LeadConvertResult[] convertLead(Database.LeadConvert[]

   leadsToConvert, Boolean allOrNone)

```

Parameters

```
   leadsToConvert
```

Type: Database.LeadConvert[]

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.LeadConvertResult[]

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.


Apex Reference Guide Database Class

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadToConvert, dmlOptions)`**

Converts a lead into an account and contact, as well as (optionally) an opportunity.

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   Database.DMLOptions dmlOptions)

```

Parameters

```
   leadToConvert
```

Type: Database.LeadConvert

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, dmlOptions)`**

Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

Signature

```
   public static List<Database.LeadConvertResult> convertLead(List<Database.LeadConvert>

   leadsToConvert, Database.DMLOptions dmlOptions)

```

Parameters

```
   leadsToConvert
```

Type: List<Database.LeadConvert>

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.


Apex Reference Guide Database Class

Return Value

Type: List<Database.LeadConvertResult>

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadToConvert, allOrNone, accessLevel)`**

Converts a lead into an account and contact, as well as (optionally) an opportunity.

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   Boolean allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   leadToConvert
```

Type: Database.LeadConvert

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, allOrNone, accessLevel)`**

Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.


Apex Reference Guide Database Class

Signature

```
   public static List<Database.LeadConvertResult> convertLead(List<Database.LeadConvert>

   leadsToConvert, Boolean allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   leadsToConvert
```

Type: List<Database.LeadConvert>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.LeadConvertResult>

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadToConvert, dmlOptions, accessLevel)`**

Converts a lead into an account and contact, as well as (optionally) an opportunity.

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   Database.DMLOptions dmlOptions, System.AccessLevel accessLevel)

```

Parameters

```
   leadToConvert
```

Type: Database.LeadConvert

```
   dmlOptions
```

Type: Database.DMLOptions


Apex Reference Guide Database Class

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, dmlOptions, accessLevel)`**

Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

Signature

```
   public static List<Database.LeadConvertResult> convertLead(List<Database.LeadConvert>

   leadsToConvert, Database.DMLOptions dmlOptions, System.AccessLevel accessLevel)

```

Parameters

```
   leadsToConvert
```

Type: List<Database.LeadConvert>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.LeadConvertResult>


Apex Reference Guide Database Class

Usage

We recommend passing a maximum of 100 `LeadConvert` objects to the `convertLead` method. Including more than 100 objects
per call can result in Apex governor limit errors.

Each executed `convertLead` method counts against the governor limit for DML statements.

##### countQuery(query)

Returns the number of records that a dynamic SOQL query would return when executed.

Signature

```
   public static Integer countQuery(String query)

```

Parameters

```
   query
```

Type: String

Return Value

Type: Integer

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

##### Each executed countQuery method counts against the governor limit for SOQL queries.

Example

```
   String QueryString =

      'SELECT count() FROM Account';

   Integer i =

      Database.countQuery(QueryString);

##### **`countQuery(query, accessLevel)`**

```

Returns the number of records that a dynamic SOQL query would return when executed.

Signature

```
   public static Integer countQuery(String query, System.AccessLevel accessLevel)

```

Parameters

```
   query
```

Type: String

```
   accessLevel
```

Type: System.AccessLevel


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Integer

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

##### Each executed countQuery method counts against the governor limit for SOQL queries. **`countQueryWithBinds(query, bindMap, accessLevel)`**

Returns the number of records that a dynamic SOQL query would return when executed. Bind variables in the query are resolved from
the _`bindMap`_ Map parameter directly with the key, rather than from Apex code variables.

Signature

```
   public static Integer countQueryWithBinds(String query, Map<String, Object> bindMap,

   System.AccessLevel accessLevel)

```

Parameters

```
   query
```

Type: String

SOQL query that includes Apex bind variables preceded by a colon. All bind variables must have a key in the _`bindMap`_ Map.

```
   bindMap
```

Type: Map<String, Object>

A map that contains keys for each bind variable specified in the SOQL _`queryString`_ and its value. The keys can’t be null or
duplicates, and the values can’t be null or empty strings.

```
   accessLevel
```

Type: System.AccessLevel

The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user
mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored,
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.

Return Value

Type: Integer

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

##### Each executed countQueryWithBinds method counts against the governor limit for SOQL queries.


Apex Reference Guide Database Class

Example

In this example, the SOQL query uses a bind variable for an Account name. Its value ( `Acme Inc.` ) is passed in to the method using
the _`nameBind`_ Map. The `accountName` variable isn't (and doesn’t have to be) in scope when the query is executed within the
method.

```
   public static Integer simpleBindingSoqlQuery(Map<String, Object> bindParams) {

      String queryString =

        'SELECT count() ' +

        'FROM Account ' +

        'WHERE name = :name';

      return Database.countQueryWithBinds(

        queryString,

        bindParams,

        AccessLevel.USER_MODE

      );

   }

   String accountName = 'Acme Inc.';

   Map<String, Object> nameBind = new Map<String, Object>{'name' => accountName};

   Integer acctCount = simpleBindingSoqlQuery(nameBind);

   System.debug(acctCount);

##### delete(recordToDelete, allOrNone)

```

Deletes an existing sObject record, such as an individual account or contact, from your organization's data.

Signature

```
   public static Database.DeleteResult delete(SObject recordToDelete, Boolean allOrNone)

```

Parameters

```
   recordToDelete
```

Type: sObject

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.DeleteResult

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### delete(recordsToDelete, allOrNone)

Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static Database.DeleteResult[] delete(SObject[] recordsToDelete, Boolean

   allOrNone)

```

Parameters

```
   recordsToDelete
```

Type: sObject[]

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.DeleteResult[]

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

Example

The following example deletes an account named 'DotCom':

```
   Account[] doomedAccts = [SELECT Id, Name FROM Account WHERE Name = 'DotCom'];

   Database.DeleteResult[] DR_Dels = Database.delete(doomedAccts);

##### delete(recordID, allOrNone)

```

Deletes existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static Database.DeleteResult delete(ID recordID, Boolean allOrNone)

```

Parameters

```
   recordID
```

Type: ID

```
   allOrNone
```

Type: Boolean


Apex Reference Guide Database Class

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.DeleteResult

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.

##### delete(recordIDs, allOrNone)

Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static Database.DeleteResult[] delete(ID[] recordIDs, Boolean allOrNone)

```

Parameters

```
   recordIDs
```

Type: ID[]

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.DeleteResult[]

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.


Apex Reference Guide Database Class

##### **`delete(recordToDelete, allOrNone, accessLevel)`**

Deletes an existing sObject record, such as an individual account or contact, from your organization's data.

Signature

```
   public static Database.DeleteResult delete(SObject recordToDelete, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordToDelete
```

Type: sObject

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.DeleteResult

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements. **`delete(recordsToDelete, allOrNone, accessLevel)`**

Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static List<Database.DeleteResult> delete(List<SObject> recordsToDelete, Boolean

   allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToDelete
```

Type: List<sObject>


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.DeleteResult>

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements. **`delete(recordID, allOrNone, accessLevel)`**

Deletes existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static Database.DeleteResult delete(Id recordID, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordID
```

Type: ID

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.


Apex Reference Guide Database Class

Return Value

Type: Database.DeleteResult

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.

##### **`delete(recordIDs, allOrNone, accessLevel)`**

Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static List<Database.DeleteResult> delete(List<Id> recordIDs, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordIDs
```

Type: List<ID>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.DeleteResult>

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.


Apex Reference Guide Database Class

##### deleteAsync(sobjects, callback)

Initiates requests to delete the external data that corresponds to the specified external object records. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source. Allows referencing a callback class whose `processDelete` method is called for each record after deletion.

Signature

```
   public static List<Database.DeleteResult> deleteAsync(List<SObject> sobjects,

   DataSource.AsyncDeleteCallback callback)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

```
   callback
```

Type: DataSource.AsyncDeleteCallback

The callback that contains the state in the originating context and an action (the `processDelete` method) that is executed
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncDeleteCallback` .

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobject, callback)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source. Allows referencing a callback class whose `processDelete` method is called after deletion.

Signature

```
   public static Database.DeleteResult deleteAsync(SObject sobject,

   DataSource.AsyncDeleteCallback callback)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.

```
   callback
```

Type: DataSource.AsyncDeleteCallback


Apex Reference Guide Database Class

The callback that contains the state in the originating context and an action (the `processDelete` method) that is executed
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncDeleteCallback` .

Return Value

Type: Database.DeleteResult

Status result for the delete operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobjects)

Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
asynchronously, as background operations, and are sent to the external systems that are defined by the external objects' associated
external data sources.

Signature

```
   public static List<Database.DeleteResult> deleteAsync(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobject)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source.

Signature

```
   public static Database.DeleteResult deleteAsync(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.


Apex Reference Guide Database Class

Return Value

Type: Database.DeleteResult

Status result for the delete operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobjects, callback, accessLevel)

Initiates requests to delete the external data that corresponds to the specified external object records. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source. Allows referencing a callback class whose `processDelete` method is called for each record after deletion.

Signature

```
   public static List<Database.DeleteResult> deleteAsync(List<SObject> sobjects,

   DataSource.AsyncDeleteCallback callback, System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

```
   callback
```

Type: DataSource.AsyncDeleteCallback

The callback that contains the state in the originating context and an action (the `processDelete` method) that is executed
after the insert operation is completed. The execution is in system mode regardless of the `accessLevel` parameter. Use the
action callback to update org data according to the operation’s results. The callback object must extend
`DataSource.AsyncDeleteCallback` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobject, callback, accessLevel)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source. Allows referencing a callback class whose `processDelete` method is called after deletion.


Apex Reference Guide Database Class

Signature

```
   public static Database.DeleteResult deleteAsync(SObject sobject,

   DataSource.AsyncDeleteCallback callback, System.AccessLevel accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.

```
   callback
```

Type: DataSource.AsyncDeleteCallback

The callback that contains the state in the originating context and an action (the `processDelete` method) that is executed
after the insert operation is completed. The execution is in system mode regardless of the `accessLevel` parameter. Use the
action callback to update org data according to the operation’s results. The callback object must extend
`DataSource.AsyncDeleteCallback` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.DeleteResult

Status result for the delete operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobjects, accessLevel)

Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
asynchronously, as background operations, and are sent to the external systems that are defined by the external objects' associated
external data sources.

Signature

```
   public static List<Database.DeleteResult> deleteAsync(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

```
   accessLevel
```

Type: System.AccessLevel


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobject, accessLevel)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source.

Signature

```
   public static Database.DeleteResult deleteAsync(SObject sobject, System.AccessLevel

   accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.DeleteResult

Status result for the delete operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteImmediate(sobjects)

Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
synchronously and are sent to the external systems that are defined by the external objects' associated external data sources. If the Apex
transaction contains pending changes, the synchronous operations can't be completed and throw exceptions.


Apex Reference Guide Database Class

Signature

```
   public static List<Database.DeleteResult> deleteImmediate(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation.

Usage

The batch limit for big objects using `deleteImmediate()` is 50,000 records at once.

##### deleteImmediate(sobject)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed synchronously
and is sent to the external system that's defined by the external object's associated external data source. If the Apex transaction contains
pending changes, the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.DeleteResult deleteImmediate(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.

Return Value

Type: Database.DeleteResult

Status result for the delete operation.

##### **`deleteImmediate(sobjects, accessLevel)`**

Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
synchronously and are sent to the external systems that are defined by the external objects' associated external data sources. If the Apex
transaction contains pending changes, the synchronous operations can't be completed and throw exceptions.

Signature

```
   public static List<Database.DeleteResult> deleteImmediate(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to delete.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation.

Usage

The batch limit for big objects using `deleteImmediate()` is 50,000 records at once.

##### **`deleteImmediate(sobject, accessLevel)`**

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed synchronously
and is sent to the external system that's defined by the external object's associated external data source. If the Apex transaction contains
pending changes, the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.DeleteResult deleteImmediate(SObject sobject, System.AccessLevel

   accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to delete.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.DeleteResult

Status result for the delete operation.


Apex Reference Guide Database Class

##### emptyRecycleBin(recordIds)

Permanently deletes the specified records from the Recycle Bin.

Signature

```
   public static Database.EmptyRecycleBinResult[] emptyRecycleBin(ID [] recordIds)

```

Parameters

```
   recordIds
```

Type: ID[]

Return Value

Type: Database.EmptyRecycleBinResult[]

Usage

Note the following:

**•** After records are deleted using this method, they cannot be undeleted.

**•** Only 10,000 records can be specified for deletion.

**•** Logged in users can delete any record that they can query in their Recycle Bin, or the recycle bins of any subordinates. If logged in
users have “Modify All Data” permission, they can query and delete records from any Recycle Bin in the organization.

**•** Cascade delete record IDs should not be included in the list of IDs; otherwise an error occurs. For example, if an account record is
deleted, all related contacts, opportunities, contracts, and so on are also deleted. Only include the Id of the top-level account. All
related records are automatically removed.

**•** Deleted items are added to the number of items processed by a DML statement, and the method call is added to the total number
##### of DML statements issued. Each executed emptyRecycleBin method counts against the governor limit for DML statements. emptyRecycleBin(obj)

Permanently deletes the specified sObject from the Recycle Bin.

Signature

```
   public static Database.EmptyRecycleBinResult emptyRecycleBin(sObject obj)

```

Parameters

```
   obj
```

Type: sObject

Return Value

Type: Database.EmptyRecycleBinResult

Usage

Note the following:


Apex Reference Guide Database Class

**•** After an sObject is deleted using this method, it cannot be undeleted.

**•** Only 10,000 sObjects can be specified for deletion.

**•** The logged-in user can delete any sObject (that can be queried) in their Recycle Bin, or the recycle bins of any subordinates. If the
logged-in user has “Modify All Data” permission, they can query and delete sObjects from any Recycle Bin in the organization.

**•** Do not include an sObject that was deleted due to a cascade delete; otherwise an error occurs. For example, if an account is deleted,
all related contacts, opportunities, contracts, and so on are also deleted. Only include sObjects of the top-level account. All related
sObjects are automatically removed.

##### emptyRecycleBin(listOfSObjects)

Permanently deletes the specified sObjects from the Recycle Bin.

Signature

```
   public static Database.EmptyRecycleBinResult[] emptyRecycleBin(sObject[] listOfSObjects)

```

Parameters

```
   listOfSObjects
```

Type: sObject[]

Return Value

Type: Database.EmptyRecycleBinResult[]

Usage

Note the following:

**•** After an sObject is deleted using this method, it cannot be undeleted.

**•** Only 10,000 sObjects can be specified for deletion.

**•** The logged-in user can delete any sObject (that can be queried) in their Recycle Bin, or the recycle bins of any subordinates. If the
logged-in user has “Modify All Data” permission, they can query and delete sObjects from any Recycle Bin in the organization.

**•** Do not include an sObject that was deleted due to a cascade delete; otherwise an error occurs. For example, if an account is deleted,
all related contacts, opportunities, contracts, and so on are also deleted. Only include sObjects of the top-level account. All related
sObjects are automatically removed.

##### executeBatch(batchClassObject)

Submits a batch Apex job for execution corresponding to the specified class.

Signature

```
   public static ID executeBatch(Object batchClassObject)

```

Parameters

```
   batchClassObject
```

Type: Object


Apex Reference Guide Database Class

An instance of a class that implements the Database.Batchable interface.

Return Value

Type: ID

The ID of the new batch job (AsyncApexJob).

Usage

When calling this method, Salesforce chunks the records returned by the `start` method of the batch class into batches of 200, and
##### then passes each batch to the execute method. Apex governor limits are reset for each execution of execute .

[For more information, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Versioned Behavior Changes

##### If the executeBatch call fails to acquire an Apex flex queue lock:

**•** In API version 52.0 and later, the call throws a `System.AsyncException` .

**•** In API version 51.0 and earlier, the call returns an empty ID, "000000000000000", instead of throwing an exception.

##### executeBatch(batchClassObject, scope)

Submits a batch Apex job for execution using the specified class and scope.

Signature

```
   public static ID executeBatch(Object batchClassObject, Integer scope)

```

Parameters

```
   batchClassObject
```

Type: Object

An instance of a class that implements the Database.Batchable interface.

```
   scope
```

Type: Integer

##### Number of records to be passed into the execute method for batch processing.

Return Value

Type: ID

The ID of the new batch job (AsyncApexJob).

Usage

The value for _`scope`_ must be greater than 0.

If the `start` method of the batch class returns a `Database.QueryLocator,` the scope parameter of
`Database.executeBatch` can have a maximum value of 2,000. If set to a higher value, Salesforce chunks the records returned


Apex Reference Guide Database Class

by the `QueryLocator` into smaller batches of up to 200 records. If the `start` method of the batch class returns an iterable, the
scope parameter value has no upper limit; however, if you use a very high number, you could run into other limits.

Apex governor limits are reset for each execution of `execute` .

[For more information, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Versioned Behavior Changes

If the `executeBatch` call fails to acquire an Apex flex queue lock:

**•** In API version 52.0 and later, the call throws a `System.AsyncException` .

**•** In API version 51.0 and earlier, the call returns an empty ID, "000000000000000", instead of throwing an exception.

##### getAsyncDeleteResult(deleteResult)

Retrieves the status of an asynchronous delete operation that’s identified by a `Database.DeleteResult` object.

Signature

```
   public static Database.DeleteResult getAsyncDeleteResult(Database.DeleteResult

   deleteResult)

```

Parameters

```
   deleteResult
```

Type: Database.DeleteResult

The result record for the delete operation being retrieved.

Return Value

Type: Database.DeleteResult

The result of a completed asynchronous delete of a record or records.

##### getAsyncDeleteResult(asyncLocator)

Retrieves the result of an asynchronous delete operation based on the result’s unique identifier.

Signature

```
   public static Database.DeleteResult getAsyncDeleteResult(String asyncLocator)

```

Parameters

```
   asyncLocator
```

Type: String

The unique identifier associated with the result of an asynchronous operation.

Return Value

Type: Database.DeleteResult


Apex Reference Guide Database Class

The result of a completed asynchronous delete of a record or records.

##### getAsyncLocator(result)

Returns the `asyncLocator` associated with the result of a specified asynchronous insert, update, or delete operation.

Signature

```
   public static String getAsyncLocator(Object result)

```

Parameters

```
   result
```

Type: Object

The saved result of an asynchronous insert, update, or delete operation. The result object can be of type `Database.SaveResult`
or `Database.DeleteResult` .

Return Value

Type: String

The unique identifier associated with the result of the specified operation.

##### getAsyncSaveResult(saveResult)

Returns the status of an asynchronous insert or update operation that’s identified by a `Database.SaveResult` object.

Signature

```
   public static Database.SaveResult getAsyncSaveResult(Database.SaveResult saveResult)

```

Parameters

```
   saveResult
```

Type: Database.SaveResult

The result record for the insert or update operation being retrieved.

Return Value

Database.SaveResult

The result of a completed asynchronous operation on a record or records.

##### getAsyncSaveResult(asyncLocator)

Returns the status of an asynchronous insert or update operation based on the unique identifier associated with each modification.

Signature

```
   public static Database.SaveResult getAsyncSaveResult(String asyncLocator)

```


Apex Reference Guide Database Class

Parameters

```
   asyncLocator
```

Type: String

The unique identifier associated with the result of an asynchronous operation.

Return Value

Database.SaveResult

The result of a completed asynchronous operation on a record or records.

##### **`getCursor(query)`**

Creates a cursor when the specified SOQL query is executed.

Signature

```
   public static Database.Cursor getCursor(String query)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

Return Value

Type: Database.Cursor

##### **`getCursor(query, accessLevel)`**

Creates a cursor when the specified SOQL query is executed.

Signature

```
   public static Database.Cursor getCursor(String query, Object accessLevel)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.


Apex Reference Guide Database Class

Return Value

Type: Database.Cursor

##### **`getCursorWithBinds(query, bindMap, accessLevel)`**

Creates a cursor when the specified SOQL query is executed.

Signature

```
   public static Database.Cursor getCursorWithBinds(String query, Map bindMap, Object

   accessLevel)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

```
   bindMap
```

Type: Map

A map that contains placeholder keys for each bind variable specified in the SOQL query string and its value.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.Cursor

##### getDeleted(sObjectType, startDate, endDate)

Returns the list of individual records that have been deleted for an sObject type within the specified start and end dates and times and
that are still in the Recycle Bin.

Signature

```
   public static Database.GetDeletedResult getDeleted(String sObjectType, Datetime

   startDate, Datetime endDate)

```

Parameters

```
   sObjectType
```

Type: String

The _`sObjectType`_ argument is the sObject type name for which to get the deleted records, such as account or merchandise__c.


Apex Reference Guide Database Class

```
   startDate
```

Type: Datetime

Start date and time of the deleted records time window.

```
   endDate
```

Type: Datetime

End date and time of the deleted records time window.

Return Value

Type: Database.GetDeletedResult

Usage

Because the Recycle Bin holds records up to 15 days, results are returned for no more than 15 days previous to the day the call is executed
(or earlier if an administrator has purged the Recycle Bin).

Example

```
   Database.GetDeletedResult r =

    Database.getDeleted(

     'Merchandise__c',

     Datetime.now().addHours(-1),

     Datetime.now());

##### **`getPaginationCursor(query)`**

```

Creates a pagination cursor when the specified SOQL query is executed.

Signature

```
   public static Database.PaginationCursor getPaginationCursor(String query)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

Return Value

Type: Database.PaginationCursor on page 2669

##### **`getPaginationCursor(query, accessLevel)`**

Creates a pagination cursor when the specified SOQL query is executed.


Apex Reference Guide Database Class

Signature

```
   public static Database.PaginationCursor getPaginationCursor(String query, Object

   accessLevel)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

```
   accessLevel
```

Type: System.AccessLevel on page 3483

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.PaginationCursor on page 2669

##### **`getPaginationCursorWithBinds(query, bindMap, accessLevel)`**

Creates a pagination cursor when the specified SOQL query is executed.

Signature

```
   public static Database.PaginationCursor getPaginationCursorWithBinds(String query, Map

   bindMap, Object accessLevel)

```

Parameters

```
   query
```

Type: String

The SOQL query to be run.

```
   bindMap
```

Type: Map

A map that contains placeholder keys for each bind variable specified in the SOQL query string and its value.

```
   accessLevel
```

Type: System.AccessLevel on page 3483

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.PaginationCursor on page 2669


Apex Reference Guide Database Class

##### getQueryLocator(staticSoqlQueryResult)

Creates a QueryLocator object used in batch Apex or Visualforce.

Signature

```
   public static Database. QueryLocator getQueryLocator(sObject [] staticSoqlQueryResult)

```

Parameters

```
   staticSoqlQueryResult
```

Type: sObject []

The _`staticSoqlQueryResult`_ parameter must be a static, inline SOQL query.

Return Value

Type: Database.QueryLocator

Usage

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and IdeaStandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

##### getQueryLocator(query)

Creates a QueryLocator object used in batch Apex or Visualforce.

Signature

```
   public static Database.QueryLocator getQueryLocator(String query)

```

Parameters

```
   query
```

Type: String

Return Value

Type: Database.QueryLocator

Usage

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)


Apex Reference Guide Database Class

##### getQueryLocator(staticSoqlQueryResult, accessLevel)

Creates a QueryLocator object used in batch Apex or Visualforce.

Signature

```
   public static Database.QueryLocator getQueryLocator(sObject [] staticSoqlQueryResult,

   System.AccessLevel accessLevel)

```

Parameters

```
   staticSoqlQueryResult
```

Type: sObject []

The _`staticSoqlQueryResult`_ parameter must be a static, inline SOQL query.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.QueryLocator

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and IdeaStandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

##### getQueryLocator(query, accessLevel)

Creates a QueryLocator object used in batch Apex or Visualforce.

Signature

```
   public static Database.QueryLocator getQueryLocator(String query, System.AccessLevel

   accessLevel)

```

Parameters

```
   query
```

Type: String


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.QueryLocator

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

##### **`getQueryLocatorWithBinds(query, bindMap, accessLevel)`**

Creates a QueryLocator object used in batch Apex or Visualforce. Bind variables in the query are resolved from the _`bindMap`_ Map
parameter directly with the key, rather than from Apex code variables.

Signature

```
   public static Database.QueryLocator getQueryLocatorWithBinds(String query, Map<String,

   Object> bindMap, System.AccessLevel accessLevel)

```

Parameters

```
   query
```

Type: String

SOQL query that includes Apex bind variables preceded by a colon. All bind variables must have a key in the _`bindMap`_ Map.

```
   bindMap
```

Type: Map<String, Object>

A map that contains keys for each bind variable specified in the SOQL _`queryString`_ and its value. The keys can’t be null or
duplicates, and the values can’t be null or empty strings.

```
   accessLevel
```

Type: System.AccessLevel

The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user
mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored,
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.


Apex Reference Guide Database Class

Return Value

Type: Database.QueryLocator

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

You can't use `getQueryLocatorWithBinds` [with any query that contains an aggregate function.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_agg_fns.htm)

Each executed `getQueryLocatorWithBinds` method counts against the governor limit for the total number of records retrieved
by Database.getQueryLocator(10,000) and the total number of SOQL queries issued. See Per Transaction Apex Limits.

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

Example

In this example, the SOQL query uses a bind variable for an Account name. Its value ( `Acme Corporation` ) is passed in using the
_`acctBinds`_ Map.

```
   public class TestBatch implements Database.Batchable<sObject>{

     private Map<String, Object> acctBinds = new Map<String, Object>{'acctName' => 'Acme

   Corporation'};

     private String query = 'Select Id From Account where name = :acctName';

     public Database.QueryLocator start(Database.BatchableContext BC){

       return Database.getQueryLocatorWithBinds(query, acctBinds, AccessLevel.USER_MODE);

     }

     public void execute(Database.BatchableContext BC, List<sObject> scope){

     }

     public void finish(Database.BatchableContext BC){

     }

   }

##### getUpdated(sobjectType, startDate, endDate)

```

Returns the list of individual records that have been updated for an sObject type within the specified start and end dates and times.

Signature

```
   public static Database.GetUpdatedResult getUpdated(String sobjectType, Datetime

   startDate, Datetime endDate)

```

Parameters

```
   sobjectType
```

Type: String

The _`sObjectType`_ argument is the sObject type name for which to get the updated records, such as account or merchandise__c.


Apex Reference Guide Database Class

```
   startDate
```

Type: Datetime

The _`startDate`_ argument is the start date and time of the updated records time window.

```
   endDate
```

Type: Datetime

The _`endDate`_ argument is the end date and time of the updated records time window.

Return Value

Type: Database.GetUpdatedResult

Usage

The date range for the returned results is no more than 30 days previous to the day the call is executed.

Example

```
   Database.GetUpdatedResult r =

    Database.getUpdated(

     'Merchandise__c',

     Datetime.now().addHours(-1),

     Datetime.now());

##### insert(recordToInsert, allOrNone)

```

Adds an sObject, such as an individual account or contact, to your organization's data.

Signature

```
   public static Database.SaveResult insert(sObject recordToInsert, Boolean allOrNone)

```

Parameters

```
   recordToInsert
```

Type: sObject

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.SaveResult


Apex Reference Guide Database Class

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. insert(recordsToInsert, allOrNone)

Adds one or more sObjects, such as individual accounts or contacts, to your organization’s data.

Signature

```
   public static Database.SaveResult[] insert(sObject[] recordsToInsert, Boolean allOrNone)

```

Parameters

```
   recordsToInsert
```

Type: sObject []

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

Type: Database.SaveResult[]

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements.

Example

Example:

The following example inserts two accounts:

```
   Account a = new Account(name = 'Acme1');

   Database.SaveResult[] lsr = Database.insert(

      new Account[]{a, new Account(Name = 'Acme2')},

      false);

```


Apex Reference Guide Database Class

##### insert(recordToInsert, dmlOptions)

Adds an sObject, such as an individual account or contact, to your organization's data.

Signature

```
   public static Database.SaveResult insert(sObject recordToInsert, Database.DMLOptions

   dmlOptions)

```

Parameters

```
   recordToInsert
```

Type: sObject

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

Return Value

Type: Database.SaveResult

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. insert(recordsToInsert, dmlOptions)

Adds one or more sObjects, such as individual accounts or contacts, to your organization's data.

Signature

```
   public static Database.SaveResult insert(sObject[] recordsToInsert, Database.DMLOptions

   dmlOptions)

```

Parameters

```
   recordsToInsert
```

Type: sObject[]

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.


Apex Reference Guide Database Class

Return Value

Type: Database.SaveResult[]

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. **`insert(recordToInsert, allOrNone, accessLevel)`**

Adds an sObject, such as an individual account or contact, to your organization's data.

Signature

```
   public static Database.SaveResult insert(SObject recordToInsert, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordToInsert
```

Type: sObject

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:


Apex Reference Guide Database Class

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. **`insert(recordsToInsert, allOrNone, accessLevel)`**

Adds one or more sObjects, such as individual accounts or contacts, to your organization’s data.

Signature

```
   public static List<Database.SaveResult> insert(List<SObject> recordsToInsert, Boolean

   allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToInsert
```

Type: List<sObject>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:


Apex Reference Guide Database Class

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. **`insert(recordToInsert, dmlOptions, accessLevel)`**

Adds an sObject, such as an individual account or contact, to your organization's data.

Signature

```
   public static Database.SaveResult insert(SObject recordToInsert, Database.DMLOptions

   dmlOptions, System.AccessLevel accessLevel)

```

Parameters

```
   recordToInsert
```

Type: sObject

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### **`insert(recordsToInsert, dmlOptions, accessLevel)`**

Adds one or more sObjects, such as individual accounts or contacts, to your organization's data.

Signature

```
   public static List<Database.SaveResult> insert(List<SObject> recordsToInsert,

   Database.DMLOptions dmlOptions, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToInsert
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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. insertAsync(sobjects, callback)

Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

Signature

```
   public static List<Database.SaveResult> insertAsync(List<SObject> sobjects,

   DataSource.AsyncSaveCallback callback)

```


Apex Reference Guide Database Class

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncSaveCallback` .

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobject, callback)

Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

Signature

```
   public static Database.SaveResult insertAsync(SObject sobject,

   DataSource.AsyncSaveCallback callback)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to insert.

```
   callback
```

Type: DataSource.AsyncSaveCallback

The callback object that contains the state in the originating context and an action (the `processSave` method) that executes
after the insert operation is completed. Use the action callback to update org data according to the operation’s results. The callback
object must extend `DataSource.AsyncSaveCallback` .

Return Value

Type: Database.SaveResult


Apex Reference Guide Database Class

Status result for the insert operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobjects)

Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

Signature

```
   public static List<Database.SaveResult> insertAsync(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobject)

Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

Signature

```
   public static Database.SaveResult insertAsync(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject


Apex Reference Guide Database Class

The external object record to insert.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobjects, callback, accessLevel)

Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources. Allows
referencing a callback class whose `processSave` method is called for each record after the remote operations are completed.

Signature>

```
   public static List<Database.SaveResult> insertAsync(List<SObject> sobjects,

   DataSource.AsyncSaveCallback callback, System.AccessLevel accessLevel)

```

Parameters>

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value>

Type: List<Database.SaveResult>


Apex Reference Guide Database Class

Status results for the insert operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage>

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobject, callback, accessLevel)

Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source. Allows referencing
a callback class whose `processSave` method is called after the remote operation is completed.

Signature

```
   public static Database.SaveResult insertAsync(SObject sobject,

   DataSource.AsyncSaveCallback callback, System.AccessLevel accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to insert.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .


Apex Reference Guide Database Class

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobjects, accessLevel)

Initiates requests to add external object data to the relevant external systems. The requests are executed asynchronously, as background
operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

Signature

```
   public static List<Database.SaveResult> insertAsync(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertAsync(sobject, accessLevel)

Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

Signature

```
   public static Database.SaveResult insertAsync(SObject sobject, System.AccessLevel

   accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   sobject
```

Type: SObject

The external object record to insert.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.

##### insertImmediate(sobjects)

Initiates requests to add external object data to the relevant external systems. The requests are executed synchronously and are sent to
the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains pending
changes, the synchronous operations can't be completed and throw exceptions.

Signature

```
   public static List<Database.SaveResult> insertImmediate(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation.


Apex Reference Guide Database Class

Usage

The operation allows partial success. If one or more record inserts fail, the method doesn’t throw an exception and the remainder of the
DML operation can still succeed. The returned `SaveResult` objects indicate whether the operation was successful. If it wasn’t
successful, the objects also return the error code and description.

##### insertImmediate(sobject)

Initiates a request to add external object data to the relevant external system. The request is executed synchronously and is sent to the
external system that's defined by the external object's associated external data source. If the Apex transaction contains pending changes,
the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.SaveResult insertImmediate(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to insert.

Return Value

Type: Database.SaveResult

Status result for the insert operation.

Usage

If a record insert fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it wasn’t successful, the object returns the error code and description.

##### **`insertImmediate(sobjects, accessLevel)`**

Initiates requests to add external object data to the relevant external systems. The requests are executed synchronously and are sent to
the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains pending
changes, the synchronous operations can't be completed and throw exceptions.

Signature

```
   public static List<Database.SaveResult> insertImmediate(List<SObject> sobjects,

   System.AccessLevel accessLevel)

```

Parameters

```
   sobjects
```

Type: List<SObject>

List of external object records to insert.

```
   accessLevel
```

Type: System.AccessLevel


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation.

Usage

The operation allows partial success. If one or more record inserts fail, the method doesn’t throw an exception and the remainder of the
DML operation can still succeed. The returned `SaveResult` objects indicate whether the operation was successful. If it wasn’t
successful, the objects also return the error code and description.

##### **`insertImmediate(sobject, accessLevel)`**

Initiates a request to add external object data to the relevant external system. The request is executed synchronously and is sent to the
external system that's defined by the external object's associated external data source. If the Apex transaction contains pending changes,
the synchronous operation can't be completed and throws an exception.

Signature

```
   public static Database.SaveResult insertImmediate(SObject sobject, System.AccessLevel

   accessLevel)

```

Parameters

```
   sobject
```

Type: SObject

The external object record to insert.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation.

Usage

If a record update fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it failed, the object returns the error code and description.


Apex Reference Guide Database Class

##### merge(mergeToRecord, duplicateId)

Merges the duplicate record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and reparenting any
related records. Merges only accounts, contacts, or leads.

Signature

```
   public static Database.MergeResult merge(sObject mergeToRecord, Id duplicateId)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateId
```

Type: ID

The ID of the record to merge with the mergeToRecord. This record must be of the same sObject type as the mergeToRecord.

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateRecord)

Merges the duplicate sObject record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and reparenting
any related records.

Signature

```
   public static Database.MergeResult merge(sObject mergeToRecord, sObject duplicateRecord)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateRecord
```

Type: sObject

The sObject record to merge with the mergeToRecord. This sObject must be of the same type as the mergeToRecord.

Return Value

Type: Database.MergeResult


Apex Reference Guide Database Class

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateIds)

Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

Signature

```
   public static List<Database.MergeResult> merge(sObject mergeToRecord, List<Id>

   duplicateIds)

```

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject record that the other records are merged into.

```
   duplicateIds
```

Type: List<Id>

A list of IDs of up to two records to merge with the mergeToRecord. These records must be of the same sObject type as the
mergeToRecord.

Return Value

Type: List<Database.MergeResult>

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateRecords)

Merges up to two records of the same object type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

Signature

```
   public static List<Database.MergeResult> merge(sObject mergeToRecord, List<SObject>

   duplicateRecords)

```

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject record that the other sObjects are merged into.

```
   duplicateRecords
```

Type: List<SObject>


Apex Reference Guide Database Class

A list of up to two sObject records to merge with the mergeToRecord. These sObjects must be of the same type as the mergeToRecord.

Return Value

Type: List<Database.MergeResult>

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateId, allOrNone)

Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting the
duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.

Signature

```
   public static Database.MergeResult merge(sObject mergeToRecord, Id duplicateId, Boolean

   allOrNone)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicate
```

Type: ID

The ID of the record to merge with the mergeToRecord. This record must be of the same sObject type as the mergeToRecord.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateRecord, allOrNone)

Merges the duplicate sObject record into the `mergeToRecord` sObject of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records.


Apex Reference Guide Database Class

Signature

```
   public static Database.MergeResult merge(sObject mergeToRecord, sObject duplicateRecord,

   Boolean allOrNone)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateRecord
```

Type: sObject

The sObject record to merge with the mergeToRecord. This sObject must be of the same type as the mergeToRecord.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateIds, allOrNone)

Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.

Signature

```
   public static List<Database.MergeResult> merge(sObject mergeToRecord, List<Id>

   duplicateIds, Boolean allOrNone)

```

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject record that the other records are merged into.

```
   duplicateIds
```

Type: List<Id>

A list of IDs of up to two records to merge with the mergeToRecord. These records must be of the same sObject type as the
mergeToRecord.


Apex Reference Guide Database Class

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: List<Database.MergeResult>

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateRecords, allOrNone)

Merges up to two records of the same object type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.

Signature

```
   public static List<Database.MergeResult> merge(sObject mergeToRecord, List<SObject>

   duplicateRecords, Boolean allOrNone)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the other sObjects are merged into.

```
   duplicateRecords
```

Type: List<SObject>

A list of up to two sObject records to merge with the mergeToRecord. These sObjects must be of the same type as the mergeToRecord.

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: List<Database.MergeResult>

Usage

##### Each executed merge method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### **`merge(mergeToRecord, duplicateId, accessLevel)`**

Merges the duplicate record into the `mergeToRecord` sObject record of the same type, deleting the duplicate, and reparenting any
related records. Merges only accounts, contacts, or leads.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, Id duplicateId,

   System.AccessLevel accessLevel)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateId
```

Type: ID

The ID of the record to merge with the mergeToRecord. This record must be of the same sObject type as the mergeToRecord.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecord, accessLevel)`**

Merges the specified duplicate sObject record into the `mergeToRecord` sObject of the same type, deleting the duplicate, and
reparenting any related records.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, SObject duplicateRecord,

   System.AccessLevel accessLevel)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.


Apex Reference Guide Database Class

```
   duplicateRecord
```

Type: sObject

The sObject record to merge with the mergeToRecord. This sObject must be of the same type as the mergeToRecord.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateIds, accessLevel)`**

Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

Signature

```
   public static List<Database.MergeResult> merge(SObject mergeToRecord, List<Id>

   duplicateIds, System.AccessLevel accessLevel)

```

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject record that the other records are merged into.

```
   duplicateIds
```

Type: List<Id>

A list of IDs of up to two records to merge with the mergeToRecord. These records must be of the same sObject type as the
mergeToRecord.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.MergeResult>


Apex Reference Guide Database Class

Usage

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecords, accessLevel)`**

Merges up to two records of the same object type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

Signature

```
   public static List<Database.MergeResult> merge(SObject mergeToRecord, List<SObject>

   duplicateRecords, System.AccessLevel accessLevel)

```

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject that the other sObject records are merged into.

```
   duplicateRecords
```

Type: List<SObject>

A list of up to two sObject records to merge with the mergeToRecord. These sObjects must be of the same type as the mergeToRecord.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.MergeResult>

Usage

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateId, allOrNone, accessLevel)`**

Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting the
duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, Id duplicateId, Boolean

   allOrNone, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateId
```

Type: ID

The ID of the record to merge with the mergeToRecord. This record must be of the same sObject type as the mergeToRecord.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.MergeResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecord, allOrNone, accessLevel)`**

Merges the duplicate sObject record into the `mergeToRecord` sObject record of the same type, optionally returning any errors,
deleting the duplicate, and reparenting any related records.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, SObject duplicateRecord,

   Boolean allOrNone, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the duplicate record is merged into.

```
   duplicateRecord
```

Type: sObject

The sObject record to merge with the mergeToRecord. This sObject must be of the same type as the mergeToRecord.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.MergeResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateIds, allOrNone, accessLevel)`**

Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.

Signature

```
   public static List<Database.MergeResult> merge(SObject mergeToRecord, List<Id>

   duplicateIds, Boolean allOrNone, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   mergeToRecord
```

Type: SObject

The sObject record that the other records are merged into.

```
   duplicateIds
```

Type: List<Id>

A list of IDs of up to two records to merge with the mergeToRecord. These records must be of the same sObject type as the
mergeToRecord.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.MergeResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecords, allOrNone, accessLevel)`**

Merges up to two records of the same object type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.


Apex Reference Guide Database Class

Signature

```
   public static List<Database.MergeResult> merge(SObject mergeToRecord, List<SObject>

   duplicateRecords, Boolean allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   mergeToRecord
```

Type: sObject

The sObject record that the other sObjects are merged into.

```
   duplicateRecords
```

Type: List<SObject>

A list of up to two sObject records to merge with the mergeToRecord. These sObjects must be of the same type as the mergeToRecord.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.MergeResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

Each executed `merge` method counts against the governor limit for DML statements.

##### query(queryString)

Creates a dynamic SOQL query at runtime.


Apex Reference Guide Database Class

Signature

```
   public static List<SObject> query(String queryString)

```

Parameters

```
   queryString
```

Type: String

Return Value

Type: List on page 3874<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops. Unlike
[inline SOQL, fields in bind variables aren’t supported. For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

`Database.query()` calls containing an inner query for a related child object may not return the entire result set based on the size
and complexity of the records requested. Instead, use `Database.getQueryLocator()` in conjunction with Apex Batch.
Alternatively, you can use the same SOQL query with SOAP API to be able to access all the resulting records.

##### Each executed query method counts against the governor limit for SOQL queries. **`query(queryString, accessLevel)`**

Creates a dynamic SOQL query at runtime.

Signature

```
   public static List<SObject> query(String queryString, System.AccessLevel accessLevel)

```

Parameters

```
   queryString
```

Type: String

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List on page 3874<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops. Unlike
[inline SOQL, fields in bind variables aren’t supported. For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)


Apex Reference Guide Database Class

`Database.query()` calls containing an inner query for a related child object may not return the entire result set based on the size
and complexity of the records requested. Instead, use `Database.getQueryLocator()` in conjunction with Apex Batch.
Alternatively, you can use the same SOQL query with SOAP API to be able to access all the resulting records.

##### Each executed query method counts against the governor limit for SOQL queries. **`queryWithBinds(queryString, bindMap, accessLevel)`**

Creates a dynamic SOQL query at runtime. Bind variables in the query are resolved from the _`bindMap`_ Map parameter directly with
the key, rather than from Apex code variables.

Signature

```
   public static List<SObject> queryWithBinds(String queryString, Map<String, Object>

   bindMap, System.AccessLevel accessLevel)

```

Parameters

```
   queryString
```

Type: String

SOQL query that includes Apex bind variables or expressions preceded by a colon. All bind variables must have a key in the _`bindMap`_
Map.

```
   bindMap
```

Type: Map<String, Object>

A map that contains keys for each bind variable specified in the SOQL _`queryString`_ and its value. The keys can’t be null or
duplicates, and the values can’t be null or empty strings.

```
   accessLevel
```

Type: System.AccessLevel

The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user
mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored,
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.

Return Value

Type: List on page 3874<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops.

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

##### Each executed queryWithBinds method counts against the governor limit for SOQL queries.


Apex Reference Guide Database Class

Example

In this example, the SOQL query uses a bind variable for an Account name. Its value ( `Acme Inc.` ) is passed in to the method using
the _`nameBind`_ Map. The `accountName` variable isn't (and doesn’t have to be) in scope when the query is executed within the
method.

```
   public static List<Account> simpleBindingSoqlQuery(Map<String, Object> bindParams) {

      String queryString =

        'SELECT Id, Name ' +

        'FROM Account ' +

        'WHERE name = :name';

      return Database.queryWithBinds(

        queryString,

        bindParams,

        AccessLevel.USER_MODE

      );

   }

   String accountName = 'Acme Inc.';

   Map<String, Object> nameBind = new Map<String, Object>{'name' => accountName};

   List<Account> accounts = simpleBindingSoqlQuery(nameBind);

   System.debug(accounts);

##### **`releaseSavepoint(databaseSavepoint)`**

```

Releases a given savepoint. All savepoints that are subsequent to the given one are also released.

Signature

```
   public static void releaseSavepoint(System.Savepoint databaseSavepoint)

```

Parameters

```
   databaseSavepoint
```

Type: System.Savepoint

Return Value

Type: void

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(databaseSavepoint)` and `Database.setSavepoint()` calls incremented the DML row
usage limit.


Apex Reference Guide Database Class

##### rollback(databaseSavepoint)

Restores the database to the state specified by the savepoint variable. Any emails submitted since the last savepoint are also rolled back
and not sent.

Signature

```
   public static Void rollback(System.Savepoint databaseSavepoint)

```

Parameters

```
   databaseSavepoint
```

Type: System.Savepoint

Return Value

Type: Void

Usage

Note the following:

**•** Static variables aren’t reverted during a rollback. If you try to run the trigger again, the static variables retain the values from the first
run.

**•** Each rollback counts against the governor limit for DML statements. You receive a runtime error if you try to roll back the database
additional times.

**•** The ID on an sObject inserted after setting a savepoint isn’t cleared after a rollback. Create an sObject to insert after a rollback.
Attempting to insert the sObject using the variable created before the rollback fails because the sObject variable has an ID. Updating
or upserting the sObject using the same variable also fails because the sObject isn’t in the database and, thus, can’t be updated.

[For an example, see Transaction Control.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(Savepoint)` and `Database.setSavepoint()` calls incremented the DML row usage limit.

##### setSavepoint() Returns a savepoint variable that can be stored as a local variable, then used with the rollback method to restore the database to

that point.

Signature

```
   public static System.Savepoint setSavepoint()

```


Apex Reference Guide Database Class

Return Value

Type: System.Savepoint

Usage

Note the following:

**•** If you set more than one savepoint, then roll back to a savepoint that isn’t the last savepoint you generated, the later savepoint
variables become invalid. For example, if you generated savepoint `SP1` first, savepoint `SP2` after that, and then you rolled back
to `SP1`, the variable `SP2` would no longer be valid. You receive a runtime error if you try to use it.

**•** References to savepoints can’t cross trigger invocations because each trigger invocation is a new trigger context. If you declare a
savepoint as a static variable then try to use it across trigger contexts, you receive a run-time error.

**•** Each savepoint you set counts against the governor limit for DML statements.

[For an example, see Transaction Control.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(Savepoint)` and `Database.setSavepoint()` calls incremented the DML row usage limit.

##### undelete(recordToUndelete, allOrNone)

Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

Signature

```
   public static Database.UndeleteResult undelete(sObject recordToUndelete, Boolean

   allOrNone)

```

Parameters

```
   recordToUndelete
```

Type: sObject

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.UndeleteResult


Apex Reference Guide Database Class

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. undelete(recordsToUndelete, allOrNone)

Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

Signature

```
   public static Database.UndeleteResult[] undelete(sObject[] recordsToUndelete, Boolean

   allOrNone)

```

Parameters

```
   recordsToUndelete
```

Type: sObject []

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.UndeleteResult[]

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements.

Example

The following example restores all accounts named 'Universal Containers'. The `ALL ROWS` keyword queries all rows for both top-level
and aggregate relationships, including deleted records and archived activities.

```
   Account[] savedAccts = [SELECT Id, Name FROM Account

                                           WHERE Name = 'Universal

    Containers' ALL ROWS];

   Database.UndeleteResult[] UDR_Dels = Database.undelete(savedAccts);

##### undelete(recordID, allOrNone)

```

Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.


Apex Reference Guide Database Class

Signature

```
   public static Database.UndeleteResult undelete(ID recordID, Boolean allOrNone)

```

Parameters

```
   recordID
```

Type: ID

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.UndeleteResult

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. undelete(recordIDs, allOrNone)

Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

Signature

```
   public static Database.UndeleteResult[] undelete(ID[] recordIDs, Boolean allOrNone)

```

Parameters

```
   RecordIDs
```

Type: ID[]

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.UndeleteResult[]


Apex Reference Guide Database Class

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. **`undelete(recordToUndelete, allOrNone, accessLevel)`**

Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

Signature

```
   public static Database.UndeleteResult undelete(SObject recordToUndelete, Boolean

   allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordToUndelete
```

Type: SObject

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.UndeleteResult

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. **`undelete(recordsToUndelete, allOrNone, accessLevel)`**

Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

Signature

```
   public static List<Database.UndeleteResult> undelete(List<SObject> recordsToUndelete,

   Boolean allOrNone, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

Parameters

```
   recordsToUndelete
```

Type: List<sObject>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.UndeleteResult>

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. **`undelete(recordID, allOrNone, accessLevel)`**

Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

Signature

```
   public static Database.UndeleteResult undelete(Id recordID, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordID
```

Type: Id

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


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.UndeleteResult

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. **`undelete(recordIDs, allOrNone, accessLevel)`**

Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

Signature

```
   public static List<Database.UndeleteResult> undelete(List<Id> recordIDs, Boolean

   allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordIDs
```

Type: List<ID>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.UndeleteResult>

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### update(recordToUpdate, allOrNone)

Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

Signature

```
   public static Database.SaveResult update(sObject recordToUpdate, Boolean allOrNone)

```

Parameters

```
   recordToUpdate
```

Type: sObject

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.SaveResult

Usage

##### update is analogous to the UPDATE statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed update method counts against the governor limit for DML statements.

Example

The following example updates the `BillingCity` field on a single account.

```
   Account a = new Account(Name='SFDC');

   insert(a);

   Account myAcct =

     [SELECT Id, Name, BillingCity

     FROM Account WHERE Id = :a.Id];

   myAcct.BillingCity = 'San Francisco';

   Database.SaveResult SR =

     Database.update(myAcct);

##### update(recordsToUpdate, allOrNone)

```

Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.


Apex Reference Guide Database Class

Signature

```
   public static Database.SaveResult[] update(sObject[] recordsToUpdate, Boolean allOrNone)

```

Parameters

```
   recordsToUpdate
```

Type: sObject []

```
   allOrNone
```

Type: Boolean

(Optional) The _`allOrNone`_ parameter specifies whether the operation allows partial success. If _`allOrNone`_ is set to `false`
and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify
which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

Return Value

Type: Database.SaveResult[]

Usage

##### update is analogous to the UPDATE statement in SQL. Each executed update method counts against the governor limit for DML statements. update(recordToUpdate, dmlOptions)

Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

Signature

```
   public static Database.SaveResult update(sObject recordToUpdate, Database.DmlOptions

   dmlOptions)

```

Parameters

```
   recordToUpdate
```

Type: sObject

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

Return Value

Type: Database.SaveResult

Usage

##### update is analogous to the UPDATE statement in SQL.


Apex Reference Guide Database Class

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed update method counts against the governor limit for DML statements. update(recordsToUpdate, dmlOptions)

Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

Signature

```
   public static Database.SaveResult[] update(sObject[] recordsToUpdate, Database.DMLOptions

   dmlOptions)

```

Parameters

```
   recordsToUpdate
```

Type: sObject []

```
   dmlOptions
```

Type: Database.DMLOptions

The optional _`dmlOptions`_ parameter specifies additional data for the transaction, such as assignment rule information or rollback
behavior when errors occur during record insertions.

Return Value

Type: Database.SaveResult[]

Usage

##### update is analogous to the UPDATE statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed update method counts against the governor limit for DML statements. **`update(recordToUpdate, allOrNone, accessLevel)`**

Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

Signature

```
   public static Database.SaveResult update(SObject recordToUpdate, Boolean allOrNone,

   System.AccessLevel accessLevel)

```

Parameters

```
   recordToUpdate
```

Type: SObject

```
   allOrNone
```

Type: Boolean


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### **`update(recordsToUpdate, allOrNone, accessLevel)`**

Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.

Signature

```
   public static List<Database.SaveResult> update(List<SObject> recordsToUpdate, Boolean

   allOrNone, System.AccessLevel accessLevel)

```

Parameters

```
   recordsToUpdate
```

Type: List<sObject>

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


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### **`update(recordToUpdate, dmlOptions, accessLevel)`**

Modifies an existing sObject record, such as an individual account or contact, in your organization's data.

Signature

```
   public static Database.SaveResult update(SObject recordToUpdate, Database.DMLOptions

   dmlOptions, System.AccessLevel accessLevel)

```

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.


Apex Reference Guide Database Class

Return Value

Type: Database.UpsertResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed upsert method counts against the governor limit for DML statements.

For more information on how the upsert operation works, see the upsert() statement.

##### **`upsert(recordsToUpsert, externalIdField, allOrNone, accessLevel)`**

Creates new sObject records or updates existing sObject records within a single statement, using a specified field to determine the
presence of existing objects, or the ID field if no field is specified.

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


Apex Reference Guide Database Class

which records succeeded or failed. If _`allOrNone`_ is set to `true` and the method isn’t successful, an exception is thrown. The
default for the parameter is `true` .

If _`allOrNone`_ is set to `false` and a before-trigger assigns an invalid value to a field, the partial set of valid records isn’t inserted.

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.UpsertResult>

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

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


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the update operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

##### updateAsync(sobject, accessLevel)

Initiates a request to update external object data on the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Database.SaveResult

Status result for the update operation.

Usage

If a record update fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it failed, the object returns the error code and description.


### Apex Reference Guide Date Class Date Class

Contains methods for the Date primitive data type.

Namespace

System

Usage

[For more information on Dates, see Date Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Date Methods

### The following are methods for Date .

IN THIS SECTION:

addDays(additionalDays)
Adds the specified number of additional days to a Date.

addMonths(additionalMonths)
Adds the specified number of additional months to a Date

addYears(additionalYears)
Adds the specified number of additional years to a Date

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


Apex Reference Guide Date Class

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


Apex Reference Guide Date Class

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


Apex Reference Guide Date Class

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

##### daysBetween(secondDate)

```

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

```


Apex Reference Guide Date Class

##### daysInMonth(year, month)

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

##### format()

```

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


Apex Reference Guide Date Class

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


Apex Reference Guide Date Class

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

Example

```
   Date firstDate = Date.newInstance(2006, 12, 2);

   Date secondDate = Date.newInstance(2012, 12, 8);

   Integer monthsBetween = firstDate.monthsBetween(secondDate);

   System.assertEquals(72, monthsBetween);

##### newInstance(year, month, day) Constructs a Date from Integer representations of the year, month (1=Jan), and day .

```

Signature

```
   public static Date newInstance(Integer year, Integer month, Integer day)

```

Parameters

```
   year
```

Type: Integer

##### _`month`_

Type: Integer

```
   day
```

Type: Integer

Return Value

Type: Date


Apex Reference Guide Date Class

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


Apex Reference Guide Date Class

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

```


Apex Reference Guide Date Class

```
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


### Apex Reference Guide Datetime Class

**API version 33.0 or earlier**
### If you call Date.valueOf with a Datetime object, the method returns a Date value that contains the hours, minutes,

seconds, and milliseconds set.

**API version 34.0 to API version 53.0**
### If you call Date.valueOf with a Datetime object, the method converts Datetime to a valid Date without the time information, but the result depends on the manner in which the Datetime object was initialized. For example, if the Datetime object was initialized using Datetime.valueOf(stringDate), the returned Date value contains time (hours) information. If the Datetime object is initialized using Datetime.newInstance(year, month, day, hour, minute, second) the returned Date value doesn’t contain time information.

**API version 54.0 and later**
### If you call Date.valueOf with a Datetime object, the method converts the object to a valid Date without the time

information.

##### year()

Returns the year component of a Date

Signature

```
   public Integer year()

```

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
[Datetime value. For more information about the Datetime, see Datetime Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Datetime Methods

### The following are methods for Datetime .


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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

```


Apex Reference Guide Datetime Class

```
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


Apex Reference Guide Datetime Class

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

##### format()

```

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

```


Apex Reference Guide Datetime Class

##### format(dateFormatString)

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

##### format(dateFormatString, timezone)

```

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


Apex Reference Guide Datetime Class

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

```


Apex Reference Guide Datetime Class

##### formatLong()

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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

##### minute()

```

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


Apex Reference Guide Datetime Class

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

##### monthGmt()

```

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


Apex Reference Guide Datetime Class

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

```


Apex Reference Guide Datetime Class

##### newInstance(year, month, day)

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

##### newInstance(year, month, day, hour, minute, second)

```

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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

##### This example uses parse to create a Datetime from a date passed in as a string and that is formatted for the English (United States)

locale. You may need to change the format of the date string if you have a different locale.


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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


Apex Reference Guide Datetime Class

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

```


Apex Reference Guide Datetime Class

##### valueOfGmt(dateTimeString)

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


### Apex Reference Guide Decimal Class

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

[For more information on Decimal, see Decimal Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

IN THIS SECTION:

#### Rounding Mode

Rounding mode specifies the rounding behavior for numerical operations capable of discarding precision.

Decimal Methods

#### Rounding Mode

Rounding mode specifies the rounding behavior for numerical operations capable of discarding precision.

Each rounding mode indicates how the least significant returned digit of a rounded result is to be calculated. The following are the valid
values for _`roundingMode`_ .


Apex Reference Guide Decimal Class

**Name** **Description**

```
CEILING

DOWN

FLOOR

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


Apex Reference Guide Decimal Class

**Name** **Description**

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

```
                   Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

                   Long[] expected = new Long[]{6, 1, -1, -3};

                   for(integer x = 0; x < example.size(); x++){

                     System.assertEquals(expected[x],

                        example[x].round(System.RoundingMode.HALF_EVEN));

                   }

```

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


Apex Reference Guide Decimal Class

**Name** **Description**

```
                     System.assertEquals(expected[x],

                        example[x].round(System.RoundingMode.HALF_UP));

                   }

```

```
UNNECESSARY

UP

#### Decimal Methods

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

**•** Input number -2.7: `UP` round mode result: -3

```
Decimal[] example = new Decimal[]{5.5, 1.1, -1.1, -2.7};

Long[] expected = new Long[]{6, 2, -2, -3};

for(integer x = 0; x < example.size(); x++){

   System.assertEquals(expected[x],

     example[x].round(System.RoundingMode.UP));

}

```

#### The following are methods for Decimal .

IN THIS SECTION:

abs()
Returns the absolute value of the Decimal.


Apex Reference Guide Decimal Class

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


Apex Reference Guide Decimal Class

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


Apex Reference Guide Decimal Class

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


Apex Reference Guide Decimal Class

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


Apex Reference Guide Decimal Class

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

##### precision()

```

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

```


Apex Reference Guide Decimal Class

##### round()

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


Apex Reference Guide Decimal Class

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

Parameters

##### _`scale`_

Type: Integer

##### The value of scale must be between –33 and 33. If the value of scale is negative, your unscaled value is multiplied by 10 to the power of the negation of scale . For example, after this operation, the value of d is 4*10^3 .

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


Apex Reference Guide Decimal Class

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


Apex Reference Guide Decimal Class

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

```


### Apex Reference Guide Domain Class

##### valueOf(longToDecimal)

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


Apex Reference Guide Domain Class

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

#### Domain Methods Domain Methods The following are methods for Domain .

IN THIS SECTION:

##### getDomainType()

Returns the domain’s type, such as `CONTENT_DOMAIN`, `EXPERIENCE_CLOUD_SITES_DOMAIN`, or `LIGHTNING_DOMAIN` .

getMyDomainName()
Returns the domain’s My Domain name.

getPackageName()
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


Apex Reference Guide Domain Class

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


### Apex Reference Guide DomainCreator Class

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

#### DomainCreator Methods DomainCreator Methods

### The following are methods for DomainCreator .

IN THIS SECTION:

getContentHostname()
Returns the hostname for content stored in the org, such as files.


Apex Reference Guide DomainCreator Class

##### getExperienceCloudSitesBuilderHostname()

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


Apex Reference Guide DomainCreator Class

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


Apex Reference Guide DomainCreator Class

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


### Apex Reference Guide DomainParser Class

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

### DomainParser Class

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

```


Apex Reference Guide DomainParser Class

```
   //Get the org’s My Domain name

   String myDomainName = domain.getMyDomainName(); // Returns mycompany

   //Get the package name

   String packageName = domain.getPackageName(); // Returns abcpackage

```

IN THIS SECTION:

#### DomainParser Methods DomainParser Methods The following are methods for DomainParser .

IN THIS SECTION:

##### parse(hostname)

Parses a passed hostname of a domain that Salesforce hosts for the org, and returns the System.Domain.

##### parse(url)

Parses a passed uniform resource locator (URL) of a domain that Salesforce hosts for the org, and returns the System.Domain.

##### **`parse(hostname)`**

Parses a passed hostname of a domain that Salesforce hosts for the org, and returns the System.Domain.

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


### Apex Reference Guide DomainType Enum

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


### Apex Reference Guide Double Class

**Value** **Description**

`ORG_MY_DOMAIN` My Domain login domains.

`SALESFORCE_SITES_DOMAIN` Salesforce-hosted domains that serve Salesforce Sites.

`SETUP_DOMAIN` The Salesforce-hosted domain that serves Setup pages.

`VISUALFORCE_DOMAIN` Domains that serve Visualforce pages.

### Double Class

Contains methods for the Double primitive data type.

Namespace

System

Usage

[For more information on Double, see Double Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Double Methods

### The following are methods for Double .

IN THIS SECTION:

##### format()

Returns the String value for this Double using the locale of the context user

intValue()
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


Apex Reference Guide Double Class

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

##### longValue()

```

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

```


Apex Reference Guide Double Class

##### round()

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


### Apex Reference Guide EmailMessages Class

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

### EmailMessages Class Use the methods in the EmailMessages class to interact with emails and email threading.

```

Namespace

System

#### EmailMessages Methods

### The following are static methods for EmailMessages .

IN THIS SECTION:

getFormattedThreadingToken(recordId)
Returns an email threading token that’s formatted with the correct prefix and suffix. This token can be embedded in an outbound
email body, email subject, or both the body and subject. When users reply to the email, threading tokens can be used to attach
responses to a record, such as a Case record in Email-to-Case.


Apex Reference Guide EmailMessages Class

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
use EmailMessages.getRecordIdFromEmail(subject, textBody, htmlBody) on page 3756.

##### If there is no existing token, getFormattedThreadingToken may perform a Data Manipulation Language (DML) operation to

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

```


Apex Reference Guide EmailMessages Class

```
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


Apex Reference Guide EmailMessages Class

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

```


### Apex Reference Guide EncodingUtil Class

```
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

Namespace

System

Usage

Note: You cannot use the EncodingUtil methods to move documents with non-ASCII characters to Salesforce. You can, however,
download a document from Salesforce. To do so, query the ID of the document using the API `query` call, then request it by ID.

#### EncodingUtil Methods

### The following are methods for EncodingUtil . All methods are static.

IN THIS SECTION:

base64Decode(inputString)
Converts a Base64-encoded String to a Blob representing its normal form.


Apex Reference Guide EncodingUtil Class

##### base64Encode(inputBlob)

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


Apex Reference Guide EncodingUtil Class

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

##### convertToHex(inputBlob)

```

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


Apex Reference Guide EncodingUtil Class

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


### Apex Reference Guide Enum Methods

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

[For more information about Enum, see Enums.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

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


Apex Reference Guide EventBus Class

IN THIS SECTION:

#### EventBus Methods

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish.htm)_ : Publishing Platform Events

#### EventBus Methods The following are methods for EventBus . All methods are static.

IN THIS SECTION:

##### getOperationId(result)

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


Apex Reference Guide EventBus Class

Usage

**•** If the event publish request fails to be enqueued in Salesforce, and `EventBus.publish` returns a synchronous error,
`getOperationId` returns null. Also in this case, `getOperationId` returns null even when the event was created using the
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

Return Value

Type: Database.SaveResult

The result of publishing the given event. `Database.SaveResult` contains information about whether the operation was successful
and the errors encountered. If the `isSuccess()` method returns `true`, the publish request is queued in Salesforce and the event
[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

`Database.SaveResult` also contains the `Id` system field. The `Id` field value isn’t included in the event message delivered to
subscribers. It isn’t used to identify an event message, and isn’t always unique.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

Usage

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3866 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3869 method.

##### publish(events)

Publishes the given list of platform events.


Apex Reference Guide EventBus Class

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
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in
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
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3866 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3869 method.

##### **`publish(event, callback)`**

Publishes the given platform event using the specified callback. To track asynchronous publish failures, you can implement an Apex
publish callback.

Signature

```
   public static Database.SaveResult publish(SObject event, Object callback)

```


Apex Reference Guide EventBus Class

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
[message is published asynchronously. For more information, see High-Volume Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns
`false`, the event publish operation resulted in errors, which are returned in the `Database.Error` object. This method doesn’t
throw an exception due to an unsuccessful publish operation.

This method returns a `System.UnexpectedException` if you attempt to publish an `SObject` that represents an object that
isn’t a platform event.

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3866 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3869 method.

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


### Apex Reference Guide Exception Class and Built-In Exceptions

```
   callback
```

Type: Object

An Apex class that implements the EventPublishFailureCallback Interface or EventPublishSuccessCallback Interface.

Return Value

Type: List<Database.SaveResult>

A list of results, each corresponding to the result of publishing one event. For each event, `Database.SaveResult` contains
information about whether the operation was successful and the errors encountered. If the `isSuccess()` method returns `true`,
[the publish request is queued in Salesforce and the event message is published asynchronously. For more information, see High-Volume](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors)
[Platform Event Persistence. If](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_considerations.htm#pe_async_publish_errors) `isSuccess()` returns `false`, the event publish operation resulted in errors, which are returned in
the `Database.Error` object. `EventBus.publish()` can publish some passed-in events, even when other events can’t be
published due to errors. The `EventBus.publish()` method doesn’t throw exceptions caused by an unsuccessful publish operation.
It’s similar in behavior to the Apex `Database.insert` method when called with the partial success option.

If an empty list is passed in for the _`events`_ parameter, no event is published, and an empty `List<Database.SaveResult>`
is returned.

This method returns a `System.UnexpectedException` if you attempt to publish a list of type `List<SObject>` that contains
objects that aren’t platform events.

Usage

**•** [Use this method with Apex publish callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

**•** The platform event message is published either immediately or after a transaction is committed, depending on the publish behavior
[you set in the platform event definition. For more information, see Platform Event Fields in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_define_ui.htm) _[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_ .

**•** Apex governor limits apply. For events configured with the **Publish After Commit** behavior, each method execution is counted as
one DML statement against the Apex DML statement limit. You can check limit usage using the `Limits.getDMLStatements()`
on page 3866 method. For events configured with the **Publish Immediately** behavior, each method execution is counted against
a separate event publishing limit of 150 `EventBus.publish()` calls. You can check limit usage using the
`Limits.getPublishImmediateDML()` on page 3869 method.

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


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

`AuraHandledException` [Returns a custom error message to a JavaScript controller. See Returning Errors from](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/controllers_server_apex_custom_errors.htm)
[an Apex Server-Side Controller.](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/controllers_server_apex_custom_errors.htm)

`AsyncException` Any problem with an asynchronous operation, such as failing to enqueue an
asynchronous call.

`BigObjectException` Any problem with big object records, such as connection timeouts during attempts to
access or insert big object records.

`CalloutException` Any problem with a Web service operation, such as failing to make a callout to an
external system.

`DataWeaveScriptException` Any run-time script errors that occur within DataWeave in Apex.

`DmlException` Any problem with a DML statement, such as an `insert` statement missing a required
field on a record.

`DuplicateMessageException` Attempt to enqueue job with duplicate queueable signature

`EmailException` [Any problem with email, such as failure to deliver. For more information, see Outbound](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_forcecom_email_outbound.htm)
[Email.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_forcecom_email_outbound.htm)

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

InvalidParameterValueException

```

An illegal header argument was provided to an Apex REST call. For example, a call to
the `RestResponse.addHeader(name, value)` method throws this
exception if the header name is `cookie` .

This exception is used with both Visualforce pages and Salesforce Functions.

**Visualforce**
The exception is thrown when an invalid parameter is supplied for a method, or
any problem is encountered with a URL used with Visualforce pages. For more
[information on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

**Salesforce Functions**
The exception is thrown when the `functionName` parameter to
`Function.get()` doesn’t have the correct `project name.function`
`name` format. For more information on Salesforce functions, see
`[Function.get()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_functions_Function.htm)` .


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

`LimitException` A governor limit has been exceeded. This exception can’t be caught.

```
JSONException

```

Any problem with JSON serialization and deserialization operations. For more
information, see the methods of `System.JSON`, `System.JSONParser`, and
`System.JSONGenerator` .

`ListException` Any problem with a list, such as attempting to access an index that is out of bounds.

`MathException` Any problem with a mathematical operation, such as dividing by zero.

```
NoAccessException

NoDataFoundException

```

Any problem with unauthorized access, such as trying to access an sObject that the
current user doesn’t have access to. This exception is used with Visualforce pages. For
[more information on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

This exception is used with both Visualforce pages and Salesforce Functions.

**Visualforce**
The exception is thrown with data that doesn't exist, such as trying to access an
sObject that has been deleted. For more information on Visualforce, see the
[Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

**Salesforce Functions**
The exception is thrown when the project or function name provided in the
`functionName` parameter to the `Function.get()` method can't be found.
For more information on Salesforce functions, see `[Function.get()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_functions_Function.htm)` .

`NoSuchElementException` This exception is thrown if you try to access items that are outside the bounds of a list.
[This exception is used by the Iterator](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_iterable.htm) `next` method. For example, if

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
[information, see the SOAP API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/)

`SecurityException` Any problem with static methods in the Crypto utility class. For more information, see
Crypto Class.

`SerializationException` Any problem with the serialization of data. This exception is used with Visualforce pages.
[For more information on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)


Apex Reference Guide Exception Class and Built-In Exceptions

**Exception** **Description**

`SObjectException` Any problem with sObject records, such as attempting to change a field in an `update`
statement that can only be changed during `insert` .

`StringException` Any problem with Strings, such as a String that is exceeding your heap size.

`TransientCursorException` A transient problem with an Apex cursor transaction. The failed transaction can be
retried.

`TypeException` Any problem with type conversions, such as attempting to convert the String 'a' to an
Integer using the `valueOf` method.

`UnexpectedException` A non-recoverable internal error within Salesforce has occurred. This exception causes
execution to halt. If necessary, contact Salesforce Customer Support for more information.

`VisualforceException` Any problem with a Visualforce page. For more information on Visualforce, see the
[Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

`XmlException` Any problem with the XmlStream classes, such as failing to read or write XML.

The following is an example using the DmlException exception:

```
   Account[] accts = new Account[]{new Account(billingcity = 'San Jose')};

   try {

      insert accts;

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


Apex Reference Guide Exception Class and Built-In Exceptions

**Name** **Arguments** **Return Type** **Description**

`getLineNumber` Integer Returns the line number from where the exception was
thrown.

`getMessage` String Returns the error message that displays for the user.

`getStackTraceString` String Returns the stack trace of a thrown exception as a string.

`getTypeName` String Returns the type of exception, such as DmlException,
ListException, MathException, and so on.

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
[information on field tokens, see Dynamic Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic.htm)

`getDmlId` Integer _`i`_ String Returns the ID of the failed record that caused the error
described by the _`i`_ _`[th]`_ failed row.

`getDmlIndex` Integer _`i`_ Integer Returns the original row position of the _`i`_ _`[th]`_ failed row.

`getDmlMessage` Integer _`i`_ String Returns the user message for the _`i`_ _`[th]`_ failed row.

`getDmlStatusCode` Integer _`i`_ String Deprecated. Use getDmlType instead. Returns the Apex
failure code for the _`i`_ _`[th]`_ failed row.

`getDmlType` Integer _`i`_ [System.StatusCode](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

Returns the value of the System.StatusCode enum. For
example:

```
try {

  insert new Account();

} catch (System.DmlException ex) {

    System.assertEquals(

StatusCode.REQUIRED_FIELD_MISSING,

      ex.getDmlType(0));

}

```

[For more information about System.StatusCode, see Enums.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

`getNumDml` Integer Returns the number of failed rows for DML exceptions.


### Apex Reference Guide ExternalServiceTest Class

QueryException Method

In addition to the common exception methods, QueryException has this method.

**Name** **Arguments** **Return Type** **Description**

```
getInaccessibleFields

### ExternalServiceTest Class

```

Map on page Returns a map in which each key is an `sObjectType`
3894<String,Set< on and its corresponding value is the set of inaccessible field
page 4038String>> names in fully qualified format

(Namespace__FieldName__c).

Use this method to determine the cause of the
`QueryException` . The returned map contains data only
if the method that threw the `QueryException` is
running in user mode (as opposed to the default system
mode).

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


### Apex Reference Guide FlexQueue Class

IN THIS SECTION:

#### ExternalServiceTest Methods

An instance of the ExternalServiceTest method is used when the test class triggers a mocked external service’s callback response.
You can access ExternalServiceTest through `Test.getExternalService()`

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

Type: System.HttpRequest on page 3790

Return Value

Type: System.HttpResponse on page 3799

### FlexQueue Class

Contains methods that reorder batch jobs in the Apex flex queue.

Namespace

System

Usage

You can place up to 100 batch jobs in a holding status for future execution. When system resources become available, the jobs are taken
from the top of the Apex flex queue and moved to the batch job queue. Up to five queued or active jobs can be processed simultaneously


Apex Reference Guide FlexQueue Class

for each org. When a job is moved out of the flex queue for processing, its status changes from Holding to Queued. Queued jobs are
executed when the system is ready to process new jobs.

#### Use this class’s methods to reorder your Holding jobs in the flex queue. As best practice and for safe usage, a FlexQueue reorder

method must be the final statement in a transaction.

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)_ : Using Batch Apex

#### FlexQueue Methods The following are methods for FlexQueue .

IN THIS SECTION:

moveAfterJob(jobToMoveId, jobInQueueId)
Moves the job with the ID _`jobToMoveId`_ immediately after the job with the ID _`jobInQueueId`_ in the flex queue. You can
move _`jobToMoveId`_ forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception.
Returns `true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately after _`jobInQueueId`_, so no change
is made.

moveBeforeJob(jobToMoveId, jobInQueueId)
Moves the job with the ID _`jobToMoveId`_ immediately before the job with the ID _`jobInQueueId`_ in the flex queue. You can
move _`jobToMoveId`_ forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception.
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


Apex Reference Guide FlexQueue Class

##### moveAfterJob(jobToMoveId, jobInQueueId)

Moves the job with the ID _`jobToMoveId`_ immediately after the job with the ID _`jobInQueueId`_ in the flex queue. You can move
_`jobToMoveId`_ forward or backward in the queue. If either job isn’t in the queue, it throws an element-not-found exception. Returns
`true` if the job is moved, or `false` if _`jobToMoveId`_ is already immediately after _`jobInQueueId`_, so no change is made.

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


### Apex Reference Guide FeatureManagement Class

##### moveJobToEnd(jobId)

Moves the specified job the end of the flex queue, to index position `(size - 1)` . All jobs after the job’s starting position move one
spot forward. If the job isn’t in the queue, it throws an element-not-found exception. Returns `true` if the job is moved, or `false` if
the job is already at the end of the queue, so no change is made.

Signature

```
   public static Boolean moveJobToEnd(Id jobId)

```

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

### FeatureManagement Class

Use the methods in the `System.FeatureManagement` class to check and modify the values of feature parameters, and to show
or hide custom objects and custom permissions in your subscribers’ orgs.

Namespace

System


Apex Reference Guide FeatureManagement Class

Usage

[For information about feature parameters, see Manage Features in Second Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_fma_manage_features.htm) _Second-Generation_
_Managed Packaging Developer Guide_ [, or Manage Features in First-Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_manage_features.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

The set methods (setPackageBooleanValue, setPackageDateValue, setPackageIntegerValue) use DML operations on setup sObjects. To
[learn more about mixing operations in a test, see Mixed DML Operations in Test Methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects_test_methods.htm)

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


Apex Reference Guide FeatureManagement Class

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


Apex Reference Guide FeatureManagement Class

Parameters

```
   apiName
```

Type: String

The `fullName__c` value of the feature parameter whose value you want to check—for example,

`'SpecialAccessAvailable'` .

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


Apex Reference Guide FeatureManagement Class

Return Value

Type: Integer

The value that’s currently assigned to the `value__c` field on the `FeatureParameterInteger__c` record that associates the
feature parameter with its related license.

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


Apex Reference Guide FeatureManagement Class

##### setPackageDateValue(apiName, value)

Sets the `value__c` value of the `FeatureParameterDate__c` record for a subscriber-to-LMO feature parameter in your
subscriber’s org. You can check the record’s value using `checkPackageDateValue(apiName)` .

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


### Apex Reference Guide Formula Class Formula Class

Contains methods to get a builder for creating a formula instance and to update all formula fields on the input SObjects.

Namespace

System

Usage

Use the Formula class in conjunction with the FormulaBuilder and FormulaInstance on page 2830 classes in the FormulaEval on page 2824
namespace.

[See Formula Evaluation in Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_formulaeval.htm)

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

#### Formula Methods Formula Methods

### The following are methods for Formula .

IN THIS SECTION:

##### builder()

Creates an instance of `FormulaBuilder` for configuring the formula with formula expression, context type, and output data
type as inputs.

recalculateFormulas(sobjects)
Updates (recalculates) all formula fields on the input SObjects.

##### **`builder()`**

Creates an instance of `FormulaBuilder` for configuring the formula with formula expression, context type, and output data type
as inputs.

Signature

```
   public static formulaeval.FormulaBuilder builder()

```


### Apex Reference Guide FormulaRecalcFieldError Class

Return Value

Type: FormulaEval.FormulaBuilder

##### recalculateFormulas(sobjects)

Updates (recalculates) all formula fields on the input SObjects.

Signature

```
   public static List<System.FormulaRecalcResult> recalculateFormulas(List<SObject>

   sobjects)

```

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


### Apex Reference Guide FormulaRecalcResult Class

IN THIS SECTION:

#### FormulaRecalcFieldError Methods FormulaRecalcFieldError Methods The following are methods for FormulaRecalcFieldError .

IN THIS SECTION:

##### getFieldError()

Returns a message describing the errors encountered during formula recalculation.

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


Apex Reference Guide FormulaRecalcResult Class

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

   System.debug(fieldError.getFieldName()); // 'divide'

   System.debug(fieldError.getFieldError()); // 'Division by zero'

```

IN THIS SECTION:

#### FormulaRecalcResult Methods FormulaRecalcResult Methods The following are methods for FormulaRecalcResult .

IN THIS SECTION:

##### getErrors()

If an error occurs during formula recalculation, an array of one or more database error objects, along with error codes and descriptions,
is returned.

getSObject()
Returns the sObject with formulas recalculated.

isSuccess()
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


### Apex Reference Guide Http Class

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

toString()
Returns a string that displays and identifies the object's properties.

##### send(request)

Sends an HttpRequest and returns the response.

Signature

```
   public HttpResponse send(HttpRequest request)

```


### Apex Reference Guide HttpCalloutMock Interface

Parameters

```
   request
```

Type: System.HttpRequest

Return Value

Type: System.HttpResponse

##### toString()

Returns a string that displays and identifies the object's properties.

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


### Apex Reference Guide HttpRequest Class

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

### HttpRequest Class Use the HttpRequest class to programmatically create HTTP requests like GET, POST, PATCH, PUT, and DELETE.

Namespace

System

Usage

### Use the XML classes or JSON classes to parse XML or JSON content in the body of a request created by HttpRequest .

Example

The following example illustrates how you can use an authorization header with a request and handle the response.

```
   public class AuthCallout {

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

```


Apex Reference Guide HttpRequest Class

```
      System.debug(res.getBody());

     }

   }

```

Note: You can set the endpoint as a named credential URL. A named credential URL contains the scheme `callout:`, the name
of the named credential, and an optional path. For example: `callout:` _`My_Named_Credential`_ `/` _`some_path`_ . A named
credential specifies the URL of a callout endpoint and its required authentication parameters in one definition. Salesforce manages
all authentication for Apex callouts that specify a named credential as the callout endpoint so that your code doesn’t have to. See
[Named Credentials as Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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

#### HttpRequest Constructors

HttpRequest Methods

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_methods_system_json_overview.htm)_ : JSON Support

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_support.htm)_ : XML Support

#### HttpRequest Constructors The following are constructors for HttpRequest .

IN THIS SECTION:

##### HttpRequest()
#### Creates a new instance of the HttpRequest class.

##### HttpRequest()

#### Creates a new instance of the HttpRequest class.

Signature

```
   public HttpRequest()

```


Apex Reference Guide HttpRequest Class

#### HttpRequest Methods The following are methods for HttpRequest . All are instance methods.

IN THIS SECTION:

getBody()
Retrieves the body of this request.

getBodyAsBlob()
Retrieves the body of this request as a Blob.

getBodyDocument()
Retrieves the body of this request as a DOM document.

getCompressed()
If `true`, the request body is compressed, `false` otherwise.

getEndpoint()
Retrieves the URL for the endpoint of the external server for this request.

getHeader(key)
Retrieves the contents of the request header.

getMethod()
#### Returns the type of method used by HttpRequest .

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


Apex Reference Guide HttpRequest Class

toString()
Returns a string containing the URL for the endpoint of the external server for this request and the method used, for example,

```
    Endpoint=http://YourServer, Method=POST

##### getBody()

```

Retrieves the body of this request.

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


Apex Reference Guide HttpRequest Class

Signature

```
   public Boolean getCompressed()

```

Return Value

Type: Boolean

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


Apex Reference Guide HttpRequest Class

**•** DELETE

**•** GET

**•** HEAD

**•** PATCH

**•** POST

**•** PUT

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


Apex Reference Guide HttpRequest Class

Usage

Limit: 6 MB for synchronous Apex or 12 MB for asynchronous Apex.

The HTTP request and response sizes count towards the total heap size.

##### setBodyDocument(document)

Sets the contents of the body for this request. The contents represent a DOM document.

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

##### setClientCertificate(clientCert, password)

This method is deprecated. Use `setClientCertificateName` instead.

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


Apex Reference Guide HttpRequest Class

##### setClientCertificateName(certDevName)

If the external service requires a client certificate for authentication, set the certificate name.

Signature

```
   public Void setClientCertificateName(String certDevName)

```

Parameters

```
   certDevName
```

Type: String

Return Value

Type: Void

Usage

[See Using Certificates with HTTP Requests.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_client_certs_http.htm)

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


Apex Reference Guide HttpRequest Class

**•** Endpoint URL

```
       https://my_endpoint.example.com/some_path

```

**•** Named credential URL, which contains the scheme `callout`, the name of the named credential, and, optionally, an appended
path

```
       callout:My_Named_Credential/some_path

```

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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


Apex Reference Guide HttpRequest Class

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


### Apex Reference Guide HttpResponse Class

Return Value

Type: String

### HttpResponse Class Use the HttpResponse class to handle the HTTP response returned by the Http class.

Namespace

System

Usage

### Use the XML classes or JSON Classes to parse XML or JSON content in the body of a response accessed by HttpResponse .

Example

In the following `getXmlStreamReader` example, content is retrieved via an HTTP callout, then the XML is parsed using
the `XmlStreamReader` class.

```
   public class ReaderFromCalloutSample {

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

```


Apex Reference Guide HttpResponse Class

```
     }

   }

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_methods_system_json_overview.htm)_ : JSON Support

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_support.htm)_ : XML Support

#### HttpResponse Methods The following are methods for HttpResponse . All are instance methods.

IN THIS SECTION:

getBody()
Retrieves the body returned in the response.

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


Apex Reference Guide HttpResponse Class

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

```


Apex Reference Guide HttpResponse Class

##### getHeader(key)

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


Apex Reference Guide HttpResponse Class

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


Apex Reference Guide HttpResponse Class

Return Value

Type: Void

##### setHeader(key, value)

Specifies the contents of the response header.

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


### Apex Reference Guide Id Class

Parameters

```
   statusCode
```

Type: Integer

Return Value

Type: Void

##### toString()

Returns the status message and status code returned in the response, for example:

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

```


Apex Reference Guide Id Class

```
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


Apex Reference Guide Id Class

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


Apex Reference Guide Id Class

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


Apex Reference Guide Id Class

Return Value

Type: Void

Usage

This method is similar to the `addError(exceptionError)` sObject method.

This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`, `\u2028`,
`\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user interface.

Example

```
   public class MyException extends Exception{}

   Trigger.new[0].Id.addError(new myException('Invalid Id'));

##### addError(exceptionError, escape)

```

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


Apex Reference Guide Id Class

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

Return Value

Type: Schema.SObjectType

Usage

[For more information about describes, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

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

```


Apex Reference Guide Id Class

##### valueOf(toID)

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


### Apex Reference Guide Ideas Class

Note: If the _`str`_ is invalid, the method throws a `System.StringException` exception.

### Ideas Class

Represents zone ideas.

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

```


Apex Reference Guide Ideas Class

```
       idea.CommunityId = community.Id;

       ID[] results = Ideas.findSimilar(idea);

     }

   }

```

The following example uses a Visualforce page in conjunction with a _custom controller_, that is, a special Apex class. For more information
[on Visualforce, see the Visualforce Developer's Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/)

This example creates an Apex method in the controller that returns unread recent replies. You can leverage this same example for the
`getAllRecentReplies` and `getReadRecentReplies` methods. For this example to work, there must be ideas posted to
the zone. In addition, at least one zone member must have posted a comment to another zone member's idea or comment.

```
   // Create an Apex method to retrieve the recent replies marked as unread in all communities

   public class IdeasController {

     public Idea[] getUnreadRecentReplies() {

        Idea[] recentReplies;

        if (recentReplies == null) {

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

```


Apex Reference Guide Ideas Class

```
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

findSimilar(idea)
Returns a list of similar ideas based on the title of the specified idea.

getAllRecentReplies(userID, communityID)
Returns ideas that have recent replies for the specified user or zone. This includes all read and unread replies.


Apex Reference Guide Ideas Class

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

Parameters

```
   idea
```

Type: Idea

Return Value

Type: ID[]

Usage

##### Each findSimilar call counts against the SOSL query limits. See Execution Governors and Limits. getAllRecentReplies(userID, communityID)

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


Apex Reference Guide Ideas Class

Usage

Each `getAllRecentReplies` [call counts against the SOQL query limits. See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

##### getReadRecentReplies(userID, communityID)

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

Return Value

Type: ID[]

Usage

##### Each getReadRecentReplies call counts against the SOQL query limits. See Execution Governors and Limits. getUnreadRecentReplies(userID, communityID)

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

##### Each getUnreadRecentReplies call counts against the SOQL query limits. See Execution Governors and Limits.


### Apex Reference Guide InstallHandler Interface

##### markRead(ideaID)

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
[package from successfully installing. To learn more, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)


Apex Reference Guide InstallHandler Interface

#### The InstallHandler interface has a single method called onInstall, which specifies the actions to be performed on install

or upgrade.

```
   public interface InstallHandler {

     void onInstall(InstallContext context)

   };

##### The onInstall method takes a context object as its argument, which provides the following information.

```

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

IN THIS SECTION:

#### InstallHandler Methods

InstallHandler Example Implementation

#### InstallHandler Methods The following are methods for InstallHandler .

IN THIS SECTION:

##### onInstall(context)

Specifies the actions to be performed on install/upgrade.

##### onInstall(context)

Specifies the actions to be performed on install/upgrade.

Signature

```
   public Void onInstall(InstallContext context)

```


Apex Reference Guide InstallHandler Interface

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

```


### Apex Reference Guide Integer Class

```
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

Namespace

System

Usage

[For more information on integers, see Integer Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Integer Methods

### The following are methods for Integer .

IN THIS SECTION:

format()
Returns the integer as a string using the locale of the context user.

valueOf(stringToInteger)
Returns an Integer that contains the value of the specified String. As in Java, the String is interpreted as representing a signed decimal
integer.

valueOf(fieldValue)
Converts the specified object to an Integer. Use this method to convert a history tracking field value or an object that represents an
Integer value.


Apex Reference Guide Integer Class

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


### Apex Reference Guide JSON Class

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

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'NumberOfEmployees') {

      Integer oldValue =

       Integer.valueOf(ah.OldValue);

      Integer newValue =

       Integer.valueOf(ah.NewValue);

   }

### JSON Class

```

Contains methods for serializing Apex objects into JSON format and deserializing JSON content that was serialized using the `serialize`
method in this class.

Namespace

System

Usage

Use the methods in the `System.JSON` class to perform round-trip JSON serialization and deserialization of Apex objects.

SEE ALSO:

_Apex Developer Guide_ [: Roundtrip Serialization and Deserialization](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_json_json.htm)


Apex Reference Guide JSON Class

#### JSON Methods The following are methods for JSON . All methods are static.

IN THIS SECTION:

##### createGenerator(prettyPrint)

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


Apex Reference Guide JSON Class

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


Apex Reference Guide JSON Class

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

```


Apex Reference Guide JSON Class

```
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

```


Apex Reference Guide JSON Class

```
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

```


Apex Reference Guide JSON Class

```
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


### Apex Reference Guide JSONGenerator Class

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_json_jsongenerator.htm)_ : JSON Generator

#### JSONGenerator Methods

### The following are methods for JSONGenerator . All are instance methods.


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


Apex Reference Guide JSONGenerator Class

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


### Apex Reference Guide JSONParser Class

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_json_jsonparser.htm)_ : JSON Parsing

#### JSONParser Methods

### The following are methods for JSONParser . All are instance methods.

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


Apex Reference Guide JSONParser Class

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
##### Returns the last token that was cleared by the clearCurrentToken method.

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


Apex Reference Guide JSONParser Class

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

```


Apex Reference Guide JSONParser Class

##### getCurrentName()

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

```


Apex Reference Guide JSONParser Class

```
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


Apex Reference Guide JSONParser Class

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


Apex Reference Guide JSONParser Class

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


Apex Reference Guide JSONParser Class

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


Apex Reference Guide JSONParser Class

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

Usage

No current token exists, and therefore this method returns `null`, if `nextToken` has not been called yet for the first time or if the
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

```


Apex Reference Guide JSONParser Class

```
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


Apex Reference Guide JSONParser Class

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

```


Apex Reference Guide JSONParser Class

```
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

```


### Apex Reference Guide JSONToken Enum

```
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

### JSONToken Enum

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


### Apex Reference Guide Label Class

**Enum Value** **Description**

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

[For information on passing in labels into Aura components, see Getting Labels in Apex in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/labels_apex.htm) _Lightning Aura Components Developer Guide_ .


Apex Reference Guide Label Class

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


Apex Reference Guide Label Class

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


### Apex Reference Guide Limits Class

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

[See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

#### Limits Methods

### The following are methods for Limits . All methods are static.

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


Apex Reference Guide Limits Class

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


### Apex Reference Guide List Class

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

Note:

**•** When using a custom type for the list elements, provide an `equals` method in your class. Apex uses this method to determine
equality and uniqueness for your objects. For more information on providing an `equals` [method, see Using Custom Types](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)
[in Map Keys and Sets.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)

**•** If the list contains String elements, the elements are case-sensitive. Two list elements that differ only by case are considered
distinct.

[For more information on lists, see Lists.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_lists.htm)

IN THIS SECTION:

#### List Constructors

List Methods

#### List Constructors

### The following are constructors for List .

IN THIS SECTION:

List<T>()
### Creates a new instance of the List class. A list can hold elements of any data type T.

List<T>(listToCopy)
### Creates a new instance of the List class by copying the elements from the specified list. T is the data type of the elements in both

lists and can be any data type.

List<T>(setToCopy)
### Creates a new instance of the List class by copying the elements from the specified set. T is the data type of the elements in the

set and list and can be any data type.


Apex Reference Guide List Class

##### List<T>() Creates a new instance of the List class. A list can hold elements of any data type T.

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

##### List<T>(listToCopy) Creates a new instance of the List class by copying the elements from the specified list. T is the data type of the elements in both
```

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


Apex Reference Guide List Class

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

#### List Methods The following are methods for List . All are instance methods.

```

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


Apex Reference Guide List Class

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


Apex Reference Guide List Class

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


Apex Reference Guide List Class

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

```


Apex Reference Guide List Class

```
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


Apex Reference Guide List Class

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

```


Apex Reference Guide List Class

```
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

##### equals(list2)

```

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


Apex Reference Guide List Class

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

[For more information, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

Example

```
   // Create a generic sObject variable.

   SObject sObj = Database.query('SELECT Id FROM Account LIMIT 1');

```


Apex Reference Guide List Class

```
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

##### hashCode()

```

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

```


Apex Reference Guide List Class

##### isEmpty()

Returns true if the list has zero elements.

Signature

```
   public Boolean isEmpty()

```

Return Value

Type: Boolean

##### iterator()

Returns an instance of an iterator for this list.

Signature

```
   public Iterator iterator()

```

Return Value

Type: Iterator

Usage

From the returned iterator, you can use the iterable methods `hasNext` and `next` to iterate through the list.

Note: You don’t have to implement the `iterable` interface to use the `iterable` methods with a list.

[See Custom Iterators.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_iterable.htm)

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

```


Apex Reference Guide List Class

```
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


Apex Reference Guide List Class

Return Value

Type: Void

Usage

To set an element of a one-dimensional list of primitives or sObjects, you can also follow the name of the list with the element's index
position in square brackets.

Example

```
   List<Integer> myList = new Integer[6];

   myList.set(0, 47);

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


Apex Reference Guide List Class

Return Value

Type: Void

Usage

Using this method, you can sort primitive types, SelectOption elements, and sObjects (standard objects and custom objects). For more
[information on the sort order used for sObjects, see Sorting Lists of sObjects. You can sort custom types (your Apex classes) if they](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_list_sorting_sobject.htm)
implement the Comparable interface. Alternatively, a class implementing the Comparator interface can be passed as a parameter to the
`List.sort` method.

When you use `sort()` methods on `List<Id>s` that contain both 15-character and 18-character IDs, IDs for the same record sort
together in API version 35.0 and later.

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


### Apex Reference Guide Location Class

Usage

When used in cyclic references, the output is truncated to prevent infinite recursion. When used with large collections, the output is
truncated to avoid exceeding total heap size and maximum CPU time.

**•** Up to 10 items per collection are included in the output, followed by an ellipsis (…).

**•** If the same object is included multiple times in a collection, it’s shown in the output only once; subsequent references are shown
as `(already output)` .

### Location Class

Contains methods for accessing the component fields of geolocation compound fields.

Namespace

system

Usage

Each of these methods is also equivalent to a read-only property. For each getter method you can access the property using dot notation.
For example, `myLocation.getLatitude()` is equivalent to `myLocation.latitude` .

You can’t use dot notation to access compound fields’ subfields directly on the parent field. Instead, assign the parent field to a variable
### of type Location, and then access its components.

```
   Location loc = myAccount.MyLocation__c;

   Double lat = loc.latitude;

```

Important: “Location” in Salesforce can also refer to the Location standard object. When referencing the Location object in your
### Apex code, always use Schema.Location instead of Location to prevent confusion with the standard Location compound

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


Apex Reference Guide Location Class

IN THIS SECTION:

#### Location Methods Location Methods The following are methods for Location .

IN THIS SECTION:

##### getDistance(toLocation, unit)

Calculates the distance between this location and the specified location, using an approximation of the haversine formula and the
specified unit.

##### getDistance(firstLocation, secondLocation, unit)

Calculates the distance between the two specified locations, using an approximation of the haversine formula and the specified
unit.

getLatitude()
Returns the latitude field of this location.

getLongitude()
Returns the longitude field of this location.

newInstance(latitude, longitude)
#### Creates an instance of the Location class, with the specified latitude and longitude.

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

#### The Location to which you want to calculate the distance from the current Location .

```
   unit
```

Type: String

The distance unit you want to use: `mi` or `km` .

Return Value

Type: Double

##### getDistance(firstLocation, secondLocation, unit)

Calculates the distance between the two specified locations, using an approximation of the haversine formula and the specified unit.


Apex Reference Guide Location Class

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


### Apex Reference Guide LoggingLevel Enum

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


### Apex Reference Guide Long Class

[For more information on log levels, see Debug Log Levels in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.code_setting_debug_log_levels.htm&language=en_US)

### Long Class

Contains methods for the Long primitive data type.

Namespace

System

Usage

[For more information on Long, see Long Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Long Methods

### The following are methods for Long .

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


### Apex Reference Guide Map Class

Signature

```
   public Integer intValue()

```

Return Value

Type: Integer

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


Apex Reference Guide Map Class

Note:

**•** Map keys and values can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex
types.

**•** Uniqueness of map keys of user-defined types is determined by the `equals` and `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)` methods, which you provide
in your classes. Uniqueness of keys of all other non-primitive types, such as sObject keys, is determined by comparing the
objects’ field values. Use caution when you use an sObject as a map key because when the sObject is changed, it no longer
maps to the same value. For information and examples, see
[https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_map_sobject_considerations.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_map_sobject_considerations.htm)

**•** Map keys of type String are case-sensitive. Two keys that differ only by the case are considered unique and have corresponding
distinct Map entries. Subsequently, the Map methods, including `put`, `get`, `containsKey`, and `remove` treat these keys
as distinct.

**•** With the `keySet()` method, the returned keySet is backed by the map and reflects any changes made to the map, and
vice versa.

[For more information on maps, see Maps.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)

IN THIS SECTION:

#### Map Constructors

Map Methods

#### Map Constructors The following are constructors for Map .

IN THIS SECTION:

##### Map<T1,T2>()
#### Creates a new instance of the Map class. T1 is the data type of the keys and T2 is the data type of the values.

Map<T1,T2>(mapToCopy)
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


Apex Reference Guide Map Class

Example

```
   Map<Integer, String> m1 = new Map<Integer, String>();

   m1.put(1, 'First item');

   m1.put(2, 'Second item');

##### Map<T1,T2>(mapToCopy) Creates a new instance of the Map class and initializes it by copying the entries from the specified map. T1 is the data type of the keys
```

and T2 is the data type of the values.

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

```


Apex Reference Guide Map Class

#### Map Methods The following are methods for Map . All are instance methods.

IN THIS SECTION:

clear()
Removes all of the key-value mappings from the map.

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


Apex Reference Guide Map Class

##### clear()

Removes all of the key-value mappings from the map.

Signature

```
   public Void clear()

```

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

```


Apex Reference Guide Map Class

##### containsKey(key)

Returns `true` if the map contains a mapping for the specified key.

Signature

```
   public Boolean containsKey(Object key)

```

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

```


Apex Reference Guide Map Class

```
     BillingCity='New York');

   Map<Integer, Account> map1 = new Map<Integer, Account> {};

   map1.put(1, a);

   Map<Integer, Account> map2 = map1.deepClone();

   // Update the first entry of map1

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


Apex Reference Guide Map Class

Parameters

```
   key
```

Type: Object

Return Value

Type: Object

Usage

If the key is a string, the key value is case-sensitive.

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

[For more information, see Understanding Apex Describe Information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

Example

```
   // Create a generic sObject variable.

   SObject sObj = Database.query('SELECT Id FROM Account LIMIT 1');

```


Apex Reference Guide Map Class

```
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

##### hashCode()

```

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


Apex Reference Guide Map Class

Return Value

Type: Set (of key type)

The returned keySet is backed by the map, so the keySet reflects any changes made to the map, and vice-versa.

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

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


Apex Reference Guide Map Class

Signature

```
   public Void putAll(Map fromMap)

```

Parameters

```
   fromMap
```

Type: Map

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


Apex Reference Guide Map Class

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

##### remove(key)

```

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


Apex Reference Guide Map Class

Return Value

Type: Integer

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

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


### Apex Reference Guide Matcher Class

Example

```
   Map<String, String> colorCodes = new Map<String, String>();

   colorCodes.put('Red', 'FF0000');

   colorCodes.put('Blue', '0000A0');

   List<String> colors = new List<String>();

   colors = colorCodes.values();

### Matcher Class

```

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


Apex Reference Guide Matcher Class

hasTransparentBounds()
Returns true if the Matcher object has transparent bounds, false if it uses opaque bounds. By default, a Matcher object uses opaque
region boundaries.

hitEnd()
Returns true if the end of input was found by the search engine in the last match operation performed by this Matcher object. When
this method returns true, it is possible that more input would have changed the result of the last search.

lookingAt()
Attempts to match the input sequence, starting at the beginning of the region, against the pattern.

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


Apex Reference Guide Matcher Class

usePattern(pattern)
Changes the Pattern object that the Matcher object uses to find matches. This method causes the Matcher object to lose information
about the groups of the last match that occurred. The Matcher object's position in the input is maintained.

useTransparentBounds(transparentBounds)
Sets the transparency bounds for this Matcher object. By default, a Matcher object uses anchoring bounds regions.

##### end()

Returns the position after the last matched character.

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

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

##### find()

Attempts to find the next subsequence of the input sequence that matches the pattern. This method returns true if a subsequence of
the input sequence matches this Matcher object's pattern.

Signature

```
   public Boolean find()

```


Apex Reference Guide Matcher Class

Return Value

Type: Boolean

Usage

This method starts at the beginning of this Matcher object's region, or, if a previous invocation of the method was successful and the
Matcher object has not since been reset, at the first character not matched by the previous match.

##### If the match succeeds, more information can be obtained using the start, end, and group methods.

[For more information, see Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

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


Apex Reference Guide Matcher Class

##### group(groupIndex)

Returns the input subsequence captured by the specified group index during the previous match operation. If the match was successful
but the specified group failed to match any part of the input sequence, `null` is returned.

Signature

```
   public String group(Integer groupIndex)

```

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

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

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

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

##### hasAnchoringBounds()

Returns true if the Matcher object has anchoring bounds, false otherwise. By default, a Matcher object uses anchoring bounds regions.

Signature

```
   public Boolean hasAnchoringBounds()

```


Apex Reference Guide Matcher Class

Return Value

Type: Boolean

Usage

If a Matcher object uses anchoring bounds, the boundaries of this Matcher object's region match start and end of line anchors such as
^ and $.

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

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

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

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


Apex Reference Guide Matcher Class

Usage

##### Like the matches method, this method always starts at the beginning of the region; unlike that method, it does not require the entire

region be matched.

If the match succeeds, more information can be obtained using the `start`, `end`, and `group` methods.

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

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

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

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


Apex Reference Guide Matcher Class

Return Value

Type: String

Usage

Metacharacters (such as `$` or `^` ) and escape sequences in the input string are treated as literal characters with no special meaning.

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

[See Using Regions and Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

##### regionEnd()

Returns the end index (exclusive) of this Matcher object's region.

Signature

```
   public Integer regionEnd()

```

Return Value

Type: Integer

Usage

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)


Apex Reference Guide Matcher Class

##### regionStart()

Returns the start index (inclusive) of this Matcher object's region.

Signature

```
   public Integer regionStart()

```

Return Value

Type: Integer

Usage

[See Using Regions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_regions.htm)

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


Apex Reference Guide Matcher Class

Signature

```
   public String replaceFirst(String replacementString)

```

Parameters

```
   replacementString
```

Type: String

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


Apex Reference Guide Matcher Class

Return Value

Type: Matcher

Usage

This method does not change whether the Matcher object uses anchoring bounds. You must explicitly use the `useAnchoringBounds`
method to change the anchoring bounds.

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

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


Apex Reference Guide Matcher Class

Parameters

```
   groupIndex
```

Type: Integer

Return Value

Type: Integer

Usage

[See Understanding Capturing Groups.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_capturing_groups.htm)

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

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

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


### Apex Reference Guide Math Class

Return Value

Type: Matcher

##### useTransparentBounds(transparentBounds)

Sets the transparency bounds for this Matcher object. By default, a Matcher object uses anchoring bounds regions.

Signature

```
   public Matcher object useTransparentBounds(Boolean transparentBounds)

```

Parameters

```
   transparentBounds
```

Type: Boolean

If you specify `true`, the Matcher object uses transparent bounds. If you specify `false`, opaque bounds are used.

Return Value

Type: Matcher

Usage

[For more information, see Using Bounds.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_pattern_and_matcher_bounds.htm)

### Math Class

Contains methods for mathematical operations.

Namespace

System

#### Math Fields

### The following are fields for Math .

IN THIS SECTION:

##### E

Returns the mathematical constant _e_, which is the base of natural logarithms.

PI
Returns the mathematical constant _pi_, which is the ratio of the circumference of a circle to its diameter.

##### E

Returns the mathematical constant _e_, which is the base of natural logarithms.


Apex Reference Guide Math Class

Signature

```
   public static final Double E

```

Property Value

Type: Double

##### PI

Returns the mathematical constant _pi_, which is the ratio of the circumference of a circle to its diameter.

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


Apex Reference Guide Math Class

atan2(xCoordinate, yCoordinate)
Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the
phase _`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

atan2(xCoordinate, yCoordinate)
Converts rectangular coordinates ( _`xCoordinate`_ and _`yCoordinate`_ ) to polar ( _`r`_ and _`theta`_ ). This method computes the
phase _`theta`_ by computing an arc tangent of _`xCoordinate`_ / _`yCoordinate`_ in the range of - _pi_ to _pi_ .

cbrt(decimalValue)
Returns the cube root of the specified Decimal. The cube root of a negative value is the negative of the cube root of that value's
magnitude.

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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

```


Apex Reference Guide Math Class

##### abs(longValue)

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

Parameters

```
   doubleAngle
```

Type: Double

Return Value

Type: Double

##### cosh(decimalAngle) Returns the hyperbolic cosine of decimalAngle . The hyperbolic cosine of d is defined to be ( e [x] + e [-x] )/2 where e is Euler's number.

Signature

```
   public static Decimal cosh(Decimal decimalAngle)

```

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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

```


Apex Reference Guide Math Class

##### max(doubleValue1, doubleValue2)

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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

##### mod(longValue1, longValue2)

```

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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

```


Apex Reference Guide Math Class

##### roundToLong(decimalValue)

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


Apex Reference Guide Math Class

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


### Apex Reference Guide Messaging Class

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

#### Messaging Methods

### The following are methods for Messaging . All are instance methods.

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


Apex Reference Guide Messaging Class

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


Apex Reference Guide Messaging Class

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


Apex Reference Guide Messaging Class

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


Apex Reference Guide Messaging Class

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


Apex Reference Guide Messaging Class

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

Usage

Use this method in situations in which you want to dynamically compose blocks of text that are enriched with data from the database.
You can then use the the rendered blocks of text to compose and send an email or update a text value in another database record.

Executing the `renderEmailTemplate` method counts toward the SOQL governor limit. The number of SOQL queries that this
method consumes is the number of elements in the list of strings passed in the _`bodies`_ parameter.

SEE ALSO:

[Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

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


Apex Reference Guide Messaging Class

Identifies an object in the database, like an account or opportunity. The record for that object is read and used in merge field
processing.

Return Value

Type: Messaging.SingleEmailMessage

Usage

##### Executing the renderStoredEmailTemplate method counts toward the SOQL governor limit as one query.

SEE ALSO:

[Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

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


Apex Reference Guide Messaging Class

(ContentVersion or Document). The `fileAttachments` property contains the IDs of attachments, in addition to all the
IDs in the `entityAttachments` property. As a result, the ID values in `entityAttachments` are duplicates of the
IDs in the `fileAttachments` property. If you call `renderStoredEmailTemplate()` by passing the
`METADATA_WITH_BODY` option, and send the rendered email message, the email will contain duplicate attachments.
Before using the returned email message with sendEmail(emails, allOrNothing), you can remove attachments from
`fileAttachments` that are duplicated in `entityAttachments` .

Return Value

Type: Messaging.SingleEmailMessage

Usage

##### Executing the renderStoredEmailTemplate method counts toward the SOQL governor limit as one query. renderStoredEmailTemplate(templateId, whoId, whatId, attachmentRetrievalOption,

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


### Apex Reference Guide MultiStaticResourceCalloutMock Class

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

Usage

Executing the `renderStoredEmailTemplate` method counts toward the SOQL governor limit as one query.

### MultiStaticResourceCalloutMock Class

Utility class used to specify a fake response using multiple resources for testing HTTP callouts.

Namespace

System

Usage

Use the methods in this class to set the response properties for testing HTTP callouts. You can specify a resource for each endpoint.

IN THIS SECTION:

#### MultiStaticResourceCalloutMock Constructors

MultiStaticResourceCalloutMock Methods

#### MultiStaticResourceCalloutMock Constructors

### The following are constructors for MultiStaticResourceCalloutMock .

IN THIS SECTION:

MultiStaticResourceCalloutMock()
Creates a new instance of the `System.MultiStaticResourceCalloutMock` class.


Apex Reference Guide MultiStaticResourceCalloutMock Class

##### MultiStaticResourceCalloutMock()

Creates a new instance of the `System.MultiStaticResourceCalloutMock` class.

Signature

```
   public MultiStaticResourceCalloutMock()

#### MultiStaticResourceCalloutMock Methods

##### The following are methods for MultiStaticResourceCalloutMock . All are instance methods.

```

IN THIS SECTION:

##### setHeader(headerName, headerValue)

Sets the specified header name and value for the fake response.

##### setStaticResource(endpoint, resourceName)

Sets the specified static resource corresponding to the endpoint. The static resource contains the response body.

setStatus(httpStatus)
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


### Apex Reference Guide Network Class

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


Apex Reference Guide Network Class

Namespace

System

IN THIS SECTION:

#### Network Constructors

Create an instance of the `System.Network` class.

#### Network Methods

