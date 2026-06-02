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

[DataWeave in Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex.htm)

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

[Reading and Writing XML Using the DOM](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_xml_dom.htm)

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

[For more information about namespaces, see Reading and Writing XML Using the DOM.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_xml_dom.htm)

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

Type: List<embeddedai.ApexMap on page 2860>

The field-level data for the primary record as a collection of key–value pairs. Each ApexMap entry corresponds to a field name and
its associated value used to construct the record context.

```
   relatedRecordData
```

Type: List<embeddedai.RecordApexRepresentation on page 2863>

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

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_

### ChangeEventHeader Class

Contains header fields of Change Data Capture events.

Namespace

EventBus

IN THIS SECTION:

#### ChangeEventHeader Properties

SEE ALSO:

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.change_data_capture.meta/change_data_capture/cdc_intro.htm)_

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

**•** [REST API: Sforce-Call-Options Header. (Bulk API also uses the Sforce-Call-Options header. )](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/headers_calloptions.htm)

**•** [SOAP API: CallOptions Header. (Apex API also uses the CallOptions element.)](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_header_calloptions.htm)

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

_Change Data Capture Developer Guide_ [: Sending Data Differences for Fields of Updated Records](https://developer.salesforce.com/docs/atlas.en-us.262.0.change_data_capture.meta/change_data_capture/cdc_data_diff.htm)

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

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
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

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .


### Apex Reference Guide EventPublishSuccessCallback Interface EventPublishSuccessCallback Interface

Implement this interface to track platform event messages that were published successfully. The `onSuccess()` method in this
interface is called when the final result of the asynchronous publish operation becomes available.

Namespace

EventBus

Usage

[For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events_
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

[For an example implementation and a test class, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
[Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm) _Platform Events Developer Guide_ .

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

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_events_intro.htm)_

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

_Tooling API Objects_ [: FlowTestCoverage](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_flowtestcoverage.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_qs_test.htm)_ : Add a Test Class

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

_[Salesforce CLI Setup Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)_ Before You Begin

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

[For usage notes, see Formula Evaluation in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_formulaeval.htm)

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

ise_bots_apex on page 2922


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


## Apex Reference Guide IssueCreditMemo Namespace

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

## IssueCreditMemo Namespace

The IssueCreditMemo namespace provides classes to create and apply credit memos against invoices or invoice lines based on dispute
adjustments.

## The IssueCreditMemo namespace includes these classes.

**•** [CreditLineRequestInputRepresentations Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditLineRequestInputRepresentations.htm)

**•** [CreditRequestInputRepresentations Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditRequestInputRepresentations.htm)

**•** [CreditResponseOutputRepresentations Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_IssueCreditMemo_CreditResponseOutputRepresentations.htm)

## ind_mfg_sample_mgmt_apex Namespace

The ind_mfg_sample_mgmt_apex namespace provides classes and properties to manage the lifecycle and documentation of product
requirements in manufacturing. Create, update, or version Product Requirement Specification records to ensure sample data remains
consistent and compliant with production standards.

## The following are the classes in the ind_mfg_sample_mgmt_apex namespace.

**•** ProductRequirementSpecification Class

**•** ProductRequirementSpecificationItem Class

**•** ProductRequirementSpecificationVersion Class


## Apex Reference Guide industriesNlpSvc industriesNlpSvc

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

Namespace

## industriesNlpSvc

IN THIS SECTION:

#### NlpResponse Properties NlpResponse Properties

### The following are properties for NlpResponse .

IN THIS SECTION:

##### summarizationResult

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

errors
Represents the property to store errors that occurred as a result of the NLP Operation.

##### **`summarizationResult`**

Represents the property that stores the NLP Summarization result performed for an NLP Operation. NLP operation can be
SurveyLongSummarization and SurveyShortSummarization.

Signature

```
   public industriesNlpSvc.NlpSummarizationResult summarizationResult {get; set;}

```


### Apex Reference Guide NlpSummarizationResult Class

Property Value

Type: List<industriesNlpSvc.NlpSummarizationResult on page 2928>

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

Namespace

industriesNlpSvc

IN THIS SECTION:

#### NlpSummarizationResult Properties NlpSummarizationResult Properties

### The following are properties for NlpSummarizationResult :

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


## Apex Reference Guide IndustriesDigitalLending Namespace IndustriesDigitalLending Namespace

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

[See industriesDigitalLending namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/apex_namespace_industriesDigitalLending.htm)

## Invocable Namespace The Invocable namespace provides classes for calling invocable actions from Apex. These classes are in the Invocable namespace.

IN THIS SECTION:

Action Class
Contains methods to create, update, and retrieve information about invocable actions.

Action.AdditionalAttribute Class
Contains methods to get metadata about attributes associated with invocable action parameters.

Action.DescribeResult Class
Contains methods to get metadata about invocable actions.

Action.Error Class
Contains methods to retrieve errors returned by invocable actions.

Action.GenericType Class
Contains methods to get metadata about generic type parameters for invocable actions.

Action.InputParameter Class
Contains methods to get metadata about input parameters for invocable actions.

Action.OutputParameter Class
Contains methods about metadata returned by invocable actions.

Action.PicklistValue Class
Contains methods to get metadata about a single value in a picklist used by invocable action parameters.

Action.Result Class
Contains methods to retrieve results from invocable actions called from Apex code.


### Apex Reference Guide Action Class Action Class

Contains methods to create, update, and retrieve information about invocable actions.

Namespace

Invocable

Usage

The `getDescribe()` method returns detailed metadata about an invocable action, including its inputs, outputs, and configuration.
Because this method retrieves comprehensive describe information, it can have performance implications. Use `getDescribe()`
judiciously, especially in performance-sensitive contexts such as loops or frequently executed code paths.

When calling `createStandardAction()` or `createCustomAction()`, the version parameter is optional. If you don't
specify a version, the base version of the action is used.

Example

```
   // Create an action and get its metadata

   Invocable.Action action = Invocable.Action.createStandardAction('someActionName');

   List<Invocable.Action.DescribeResult> describeResults = action.getDescribe();

   for (Invocable.Action.DescribeResult dr : describeResults) {

      System.debug('Action Name: ' + dr.getName());

      System.debug('Action Label: ' + dr.getLabel());

      System.debug('Description: ' + dr.getDescription());

      System.debug('Has Callout: ' + dr.getHasCallout());

      // Access input parameters

      if (dr.getInputs() != null) {

        for (Invocable.Action.InputParameter input : dr.getInputs()) {

           System.debug('Input: ' + input.getName() + ' (' + input.getType() + ')');

           System.debug('Required: ' + input.getRequired());

           System.debug('Description: ' + input.getDescription());

        }

      }

      // Access output parameters

      if (dr.getOutputs() != null) {

        for (Invocable.Action.OutputParameter output : dr.getOutputs()) {

           System.debug('Output: ' + output.getName() + ' (' + output.getType() + ')');

        }

      }

   }

```


Apex Reference Guide Action Class

IN THIS SECTION:

#### Action Methods

SEE ALSO:

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_Salesforce Help_ [: Launch a Flow from Apex](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_system_apex_invoke_a_flow_from_apex.htm&language=en_US)

#### Action Methods These methods are for Action .

IN THIS SECTION:

addInvocation()
Creates an empty invocation in preparation for calling an invocable action. After you create the invocation, you can add parameters
to the invocation.

clearInvocations()
Clears the existing invocations from the action.

clone()
Creates a copy of the `Invocable.Action` .

createCustomAction(type, namespace, name, version)
Creates a wrapper for the specified version of a custom invocable action in a specified package namespace.

createCustomAction(type, namespace, name)
Creates a wrapper for a custom invocable action in a specified package namespace.

createCustomAction(type, name)
Creates a wrapper for a custom invocable action.

createStandardAction(type, version)
Creates a wrapper for a standard invocable action.

createStandardAction(type)
Creates a wrapper for a standard invocable action.

getDescribe()
Gets metadata related to an invocable action.

getName()
Gets the name of an invocable action.

getNamespace()
Gets the namespace of a custom invocable action.

getType()
Gets the type of an invocable action.

getVersion()
Gets the version of an invocable action.

invoke()
Invokes an invocable action from Apex code.


Apex Reference Guide Action Class

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

Type: Invocable.Action on page 2930

##### **`clearInvocations()`**

Clears the existing invocations from the action.

Signature

```
   public Invocable.Action clearInvocations()

```

Return Value

Type: Invocable.Action on page 2930

##### **`clone()`**

Creates a copy of the `Invocable.Action` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### **`createCustomAction(type, namespace, name, version)`**

Creates a wrapper for the specified version of a custom invocable action in a specified package namespace.


Apex Reference Guide Action Class

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

```
   version
```

Type: String

Version of the invocable action.

Return Value

Type: Invocable.Action

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


Apex Reference Guide Action Class

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

Type of invocable action.

```
   name
```

Type: String

Name for the custom invocable action.

Return Value

Type: Invocable.Action

##### **`createStandardAction(type, version)`**

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

```
   version
```

Type: String

Version of the invocable action.

Return Value

Type: Invocable.Action

##### **`createStandardAction(type)`**

Creates a wrapper for a standard invocable action.


Apex Reference Guide Action Class

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

##### **`getDescribe()`**

Gets metadata related to an invocable action.

Signature

```
   public List<Invocable.Action.DescribeResult> getDescribe()

```

Return Value

Type: List<Invocable.Action.DescribeResult on page 2942>

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

Return Value

Type: String


Apex Reference Guide Action Class

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

##### **`getVersion()`**

Gets the version of an invocable action.

Signature

```
   public String getVersion()

```

Return Value

Type: String

Version of the invocable action.

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


### Apex Reference Guide Action.AdditionalAttribute Class

Return Value

Type: Boolean

This method returns `true` if the invocable action is a standard invocable action.

##### **`setInvocationParameter(parameterName, parameterValue)`**

Sets a value for an invocable action parameter.

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

Type: Invocable.Action on page 2930

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

Type: List on page 3992<Map on page 4013<String on page 4226,ANY>>

List of invocations for the invocable action.

Return Value

Type: Invocable.Action on page 2930

### Action.AdditionalAttribute Class

Contains methods to get metadata about attributes associated with invocable action parameters.


Apex Reference Guide Action.AdditionalAttribute Class

Namespace

Invocable

Usage

Additional attributes extend invocable action parameters with custom metadata beyond the standard parameter properties. Use the
`AdditionalAttribute` class to access this extensibility metadata when working with invocable actions.

For type-safe access to collection values, use the typed getter methods such as `getValueAsStringList()`,
`getValueAsIntegerList()`, `getValueAsDoubleList()`, or `getValueAsBooleanList()` . These methods return
`null` when the requested data type doesn't match the attribute's actual data type. Check `getDataType()` and
`getIsCollection()` before calling typed getters to ensure you use the appropriate method.

Example

```
   Invocable.Action action = Invocable.Action.createStandardAction('otherActionName');

   List<Invocable.Action.DescribeResult> results = action.getDescribe();

   for (Invocable.Action.DescribeResult result : results) {

      for (Invocable.Action.InputParameter input : result.getInputs()) {

        List<Invocable.Action.AdditionalAttribute> attrs = input.getAdditionalAttributes();

        if (attrs != null) {

           for (Invocable.Action.AdditionalAttribute attr : attrs) {

             System.debug('Attribute: ' + attr.getName());

             System.debug('Data Type: ' + attr.getDataType());

             // Handle collection vs single value

             if (attr.getIsCollection()) {

               if (attr.getDataType() == 'STRING') {

                  List<String> stringValues = attr.getValueAsStringList();

                  System.debug('String Values: ' + stringValues);

               }

             } else {

               System.debug('Value: ' + attr.getValue());

             }

           }

        }

      }

   }

```

IN THIS SECTION:

#### Action.AdditionalAttribute Methods Action.AdditionalAttribute Methods The following are methods for Action.AdditionalAttribute .


Apex Reference Guide Action.AdditionalAttribute Class

IN THIS SECTION:

##### getApexClass()

Gets the Apex class name of an additional attribute for an invocable action parameter.

##### getDataType()

Gets the data type of an additional attribute for an invocable action parameter.

getIsCollection()
Indicates whether an additional attribute for an invocable action parameter contains a collection of values.

getName()
Gets the name of an additional attribute for an invocable action parameter.

getValue()
Gets the value for an additional attribute for an invocable action parameter.

getValueAsBooleanList()
Returns a value as a list of Booleans when `isCollection` is `true` and `dataType` is BOOLEAN.

getValueAsDateList()
Returns a value as a list of dates when `isCollection` is `true` and `dataType` is DATE.

getValueAsDoubleList()
Returns a value as a list of doubles when `isCollection` is `true` and `dataType` is DOUBLE.

getValueAsIntegerList()
Returns a value as a list of integers when `isCollection` is `true` and `dataType` is INTEGER.

getValueAsList()
Returns a value as a list when `isCollection` is `true` . The list elements have the type specified by the `dataType` property.

getValueAsLongList()
Returns a value as a list of longs when `isCollection` is `true` and `dataType` is LONG.

getValueAsStringList()
Returns a value as a list of strings when `isCollection` is `true` and `dataType` is STRING.

##### **`getApexClass()`**

Gets the Apex class name of an additional attribute for an invocable action parameter.

Signature

```
   public String getApexClass()

```

Return Value

Type: String

Apex class name of the additional attribute for the invocable action parameter.

##### **`getDataType()`**

Gets the data type of an additional attribute for an invocable action parameter.


Apex Reference Guide Action.AdditionalAttribute Class

Signature

```
   public String getDataType()

```

Return Value

Type: String

Data type of the additional attribute for the invocable action parameter. For example: STRING, INTEGER, BOOLEAN, DOUBLE, LONG, DATE.

##### **`getIsCollection()`**

Indicates whether an additional attribute for an invocable action parameter contains a collection of values.

Signature

```
   public Boolean getIsCollection()

```

Return Value

Type: Boolean

This method returns `true` if the additional attribute for the invocable action parameter is a collection.

##### **`getName()`**

Gets the name of an additional attribute for an invocable action parameter.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the additional attribute for the invocable action parameter.

##### **`getValue()`**

Gets the value for an additional attribute for an invocable action parameter.

Signature

```
   public Object getValue()

```

Return Value

Type: Object

Value of the additional attribute for the invocable action parameter. Cast to the appropriate type based on the `dataType` and
`isCollection` .


Apex Reference Guide Action.AdditionalAttribute Class

##### **`getValueAsBooleanList()`**

Returns a value as a list of Booleans when `isCollection` is `true` and `dataType` is BOOLEAN.

Signature

```
   public List<Boolean> getValueAsBooleanList()

```

Return Value

Type: List<Boolean>

List of Boolean values, or null if not a Boolean collection.

##### **`getValueAsDateList()`**

Returns a value as a list of dates when `isCollection` is `true` and `dataType` is DATE.

Signature

```
   public List<Date> getValueAsDateList()

```

Return Value

Type: List<Date>

List of date values, or null if not a date collection.

##### **`getValueAsDoubleList()`**

Returns a value as a list of doubles when `isCollection` is `true` and `dataType` is DOUBLE.

Signature

```
   public List<Double> getValueAsDoubleList()

```

Return Value

Type: List<Double>

List of double values, or null if not a double collection.

##### **`getValueAsIntegerList()`**

Returns a value as a list of integers when `isCollection` is `true` and `dataType` is INTEGER.

Signature

```
   public List<Integer> getValueAsIntegerList()

```

Return Value

Type: List<Integer>


### Apex Reference Guide Action.DescribeResult Class

List of integer values, or null if not an integer collection.

##### **`getValueAsList()`**

Returns a value as a list when `isCollection` is `true` . The list elements have the type specified by the `dataType` property.

Signature

```
   public List<ANY> getValueAsList()

```

Return Value

Type: List<Object>

List of values type according to `dataType`, or null if not a collection.

##### **`getValueAsLongList()`**

Returns a value as a list of longs when `isCollection` is `true` and `dataType` is LONG.

Signature

```
   public List<Long> getValueAsLongList()

```

Return Value

Type: List<Long>

List of long values, or null if not a long collection.

##### **`getValueAsStringList()`**

Returns a value as a list of strings when `isCollection` is `true` and `dataType` is STRING.

Signature

```
   public List<String> getValueAsStringList()

```

Return Value

Type: List<String>

List of string values, or null if not a string collection.

### Action.DescribeResult Class

Contains methods to get metadata about invocable actions.

Namespace

Invocable


Apex Reference Guide Action.DescribeResult Class

Example

```
   Invocable.Action action = Invocable.Action.createStandardAction('otherActionName');

   List<Invocable.Action.DescribeResult> results = action.getDescribe();

   for (Invocable.Action.DescribeResult result : results) {

      for (Invocable.Action.InputParameter input : result.getInputs()) {

        List<Invocable.Action.AdditionalAttribute> attrs = input.getAdditionalAttributes();

        if (attrs != null) {

           for (Invocable.Action.AdditionalAttribute attr : attrs) {

             System.debug('Attribute: ' + attr.getName());

             System.debug('Data Type: ' + attr.getDataType());

             // Handle collection vs single value

             if (attr.getIsCollection()) {

               if (attr.getDataType() == 'STRING') {

                  List<String> stringValues = attr.getValueAsStringList();

                  System.debug('String Values: ' + stringValues);

               }

             } else {

               System.debug('Value: ' + attr.getValue());

             }

           }

        }

      }

   }

```

IN THIS SECTION:

#### Action.DescribeResult Methods Action.DescribeResult Methods The following are methods for Action.DescribeResult .

IN THIS SECTION:

getAction()
Gets the invocable action that was invoked and caused a result to be returned.

getAllowsTransactionControl()
Indicates whether the invocable action allows transaction control.

getCapabilityTypes()
Gets the capability types supported by an invocable action.

getCategory()
Gets the category of an invocable action.

getConfigurationEditor()
Gets the type of an invocable action.


Apex Reference Guide Action.DescribeResult Class

getDescription()
Gets the description of an invocable action.

getGenericTypes()
Gets a list of the generic types defined for an invocable action.

getHasCallout()
Indicates whether an invocable action makes external callouts.

getHasSystemGeneratedOutput()
Indicates whether an invocable action is a standard invocable action.

getIconId()
Gets the icon ID for an invocable action.

getIconName()
Gets the icon name for an invocable action.

getInputs()
Gets a list of input parameters for an invocable action.

getLabel()
Gets the type of an invocable action.

getMethodDescription()
Gets the description of an invocable action method.

getMethodLabel()
Gets the label of an invocable action method.

getMethodName()
Gets the name of an invocable action method.

getName()
Gets the name of an invocable action.

getOutputs()
Gets a list of output parameters for an invocable action.

getTargetEntityName()
Gets the target entity name for an invocable action.

getType()
Gets the type of an invocable action.

##### **`getAction()`**

Gets the invocable action that was invoked and caused a result to be returned.

Signature

```
   public Invocable.Action getAction()

```

Return Value

Type: Invocable.Action


Apex Reference Guide Action.DescribeResult Class

##### **`getAllowsTransactionControl()`**

Indicates whether the invocable action allows transaction control.

Signature

```
   public Boolean getAllowsTransactionControl()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action allows transaction control.

##### **`getCapabilityTypes()`**

Gets the capability types supported by an invocable action.

Signature

```
   public List<String> getCapabilityTypes()

```

Return Value

Type: List<String>

List of capability type identifiers of the invocable action.

##### **`getCategory()`**

Gets the category of an invocable action.

Signature

```
   public String getCategory()

```

Return Value

Type: String

Category of the invocable action.

##### **`getConfigurationEditor()`**

Gets the type of an invocable action.

Signature

```
   public String getConfigurationEditor()

```

Return Value

Type: String


Apex Reference Guide Action.DescribeResult Class

Configuration editor identifier of the invocable action.

##### **`getDescription()`**

Gets the description of an invocable action.

Signature

```
   public String getDescription()

```

Return Value

Type: String

Description of the invocable action.

##### **`getGenericTypes()`**

Gets a list of the generic types defined for an invocable action.

Signature

```
   public List<Invocable.Action.GenericType> getGenericTypes()

```

Return Value

Type: List<Invocable.Action.GenericType>

##### **`getHasCallout()`**

Indicates whether an invocable action makes external callouts.

Signature

```
   public Boolean getHasCallout()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action makes external callouts.

##### **`getHasSystemGeneratedOutput()`**

Indicates whether an invocable action is a standard invocable action.

Signature

```
   public Boolean getHasSystemGeneratedOutput()

```


Apex Reference Guide Action.DescribeResult Class

Return Value

Type: Boolean

This method returns `true` if the invocable action has system-generated output.

##### **`getIconId()`**

Gets the icon ID for an invocable action.

Signature

```
   public String getIconId()

```

Return Value

Type: String

Icon ID of the invocable action.

##### **`getIconName()`**

Gets the icon name for an invocable action.

Signature

```
   public String getIconName()

```

Return Value

Type: String

Icon name for the invocable action.

##### **`getInputs()`**

Gets a list of input parameters for an invocable action.

Signature

```
   public List<Invocable.Action.InputParameter> getInputs()

```

Return Value

Type: List<Invocable.Action.InputParameter>

##### **`getLabel()`**

Gets the type of an invocable action.

Signature

```
   public String getLabel()

```


Apex Reference Guide Action.DescribeResult Class

Return Value

Type: String

Label of the invocable action.

##### **`getMethodDescription()`**

Gets the description of an invocable action method.

Signature

```
   public String getMethodDescription()

```

Return Value

Type: String

Describe of the invocable action method.

##### **`getMethodLabel()`**

Gets the label of an invocable action method.

Signature

```
   public String getMethodLabel()

```

Return Value

Type: String

Label of the invocable action method.

##### **`getMethodName()`**

Gets the name of an invocable action method.

Signature

```
   public String getMethodName()

```

Return Value

Type: String

Name of the invocable action method.

##### **`getName()`**

Gets the name of an invocable action.


### Apex Reference Guide Action.Error Class

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the invocable action.

##### **`getOutputs()`**

Gets a list of output parameters for an invocable action.

Signature

```
   public List<Invocable.Action.OutputParameter> getOutputs()

```

Return Value

Type: List<Invocable.Action.OutputParameter>

##### **`getTargetEntityName()`**

Gets the target entity name for an invocable action.

Signature

```
   public String getTargetEntityName()

```

Return Value

Type: String

Target entity name of the invocable action.

##### **`getType()`**

Gets the type of an invocable action.

Signature

```
   public String getType()

```

Return Value

Type: String

Type of the invocable action.

### Action.Error Class

Contains methods to retrieve errors returned by invocable actions.


Apex Reference Guide Action.Error Class

Namespace

Invocable

IN THIS SECTION:

#### Action.Error Methods Action.Error Methods These methods are for Action.Error .

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


### Apex Reference Guide Action.GenericType Class

Signature

```
   public String getMessage()

```

Return Value

Type: String

### Action.GenericType Class

Contains methods to get metadata about generic type parameters for invocable actions.

Namespace

Invocable

IN THIS SECTION:

#### Action.GenericType Methods Action.GenericType Methods

### The following are methods for Action.GenericType .

IN THIS SECTION:

##### getDescription()

Gets the description of a generic type parameter of an invocable action.

getLabel()
Gets the label of a generic type parameter of an invocable action.

getName()
Gets the name of a generic type parameter of an invocable action.

getSuperType()
Gets the super type of a generic type parameter of an invocable action.

##### **`getDescription()`**

Gets the description of a generic type parameter of an invocable action.

Signature

```
   public String getDescription()

```

Return Value

Type: String

Description of the generic type parameter of the invocable action.


### Apex Reference Guide Action.InputParameter Class

##### **`getLabel()`**

Gets the label of a generic type parameter of an invocable action.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Label of the generic type parameter of the invocable action.

##### **`getName()`**

Gets the name of a generic type parameter of an invocable action.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the generic type parameter of the invocable action.

##### **`getSuperType()`**

Gets the super type of a generic type parameter of an invocable action.

Signature

```
   public String getSuperType()

```

Return Value

Type: String

Super type of the generic type parameter of the invocable action.

### Action.InputParameter Class

Contains methods to get metadata about input parameters for invocable actions.

Namespace

Invocable on page 2929


Apex Reference Guide Action.InputParameter Class

Example

```
   Invocable.Action action = Invocable.Action.createStandardAction('otherActionName');

   List<Invocable.Action.DescribeResult> results = action.getDescribe();

   for (Invocable.Action.DescribeResult result : results) {

      for (Invocable.Action.InputParameter input : result.getInputs()) {

        List<Invocable.Action.AdditionalAttribute> attrs = input.getAdditionalAttributes();

        if (attrs != null) {

           for (Invocable.Action.AdditionalAttribute attr : attrs) {

             System.debug('Attribute: ' + attr.getName());

             System.debug('Data Type: ' + attr.getDataType());

             // Handle collection vs single value

             if (attr.getIsCollection()) {

               if (attr.getDataType() == 'STRING') {

                  List<String> stringValues = attr.getValueAsStringList();

                  System.debug('String Values: ' + stringValues);

               }

             } else {

               System.debug('Value: ' + attr.getValue());

             }

           }

        }

      }

   }

```

IN THIS SECTION:

#### Action.InputParameter Methods Action.InputParameter Methods The following are methods for Action.InputParameter .

IN THIS SECTION:

getAdditionalAttributes()
Gets a list of additional attributes for an invocable action input parameter.

getApexClass()
Gets the Apex class name of an input parameter for an invocable action.

getByteLength()
Gets the maximum byte length of an input parameter of an invocable action.

getConfiguration()
Indicates whether an input parameter of an invocable action is a configuration parameter.

getDefaultValue()
Gets the default value for an input parameter of an invocable action.


Apex Reference Guide Action.InputParameter Class

getDescription()
>Gets the description of an input parameter of an invocable action.

getLabel()
Gets the label of an input parameter of an invocable action.

getMaxOccurs()
Gets the maximum number of occurrences for an input parameter of an invocable action.

getName()
Gets the name of an input parameter of an invocable action.

getPicklistValues()
Gets a list of picklist values for an input parameter of an invocable action.

getPlaceholderText()
Gets the placeholder text of an input parameter of an invocable action.

getRequired()
Indicates whether an input parameter of an invocable action is required.

getSObjectType()
Gets the sObject type of an input parameter of an invocable action.

getSetupReferenceType()
Gets the setup reference types of an input parameter of an invocable action.

getToolingType()
Gets the tooling type of and input parameter of an invocable action.

getType()
Gets the data type of an input parameter of an invocable action.

##### **`getAdditionalAttributes()`**

Gets a list of additional attributes for an invocable action input parameter.

Signature

```
   public List<Invocable.Action.AdditionalAttribute> getAdditionalAttributes()

```

Return Value

Type: List<Invocable.Action.AdditionalAttribute>

##### **`getApexClass()`**

Gets the Apex class name of an input parameter for an invocable action.

Signature

```
   public String getApexClass()

```


Apex Reference Guide Action.InputParameter Class

Return Value

Type: String

Apex class name of the input parameter of the invocable action.

##### **`getByteLength()`**

Gets the maximum byte length of an input parameter of an invocable action.

Signature

```
   public Integer getByteLength()

```

Return Value

Type: Integer

Maximum byte length of the input parameter of the invocable action.

##### **`getConfiguration()`**

Indicates whether an input parameter of an invocable action is a configuration parameter.

Signature

```
   public Boolean getConfiguration()

```

Return Value

Type: Boolean

This method returns `true` if the input parameter of the invocable action is a configuration parameter.

##### **`getDefaultValue()`**

Gets the default value for an input parameter of an invocable action.

Signature

```
   public Object getDefaultValue()

```

Return Value

Type: Object

The default value, or null if no default is defined.

##### **`getDescription()`**

>Gets the description of an input parameter of an invocable action.


Apex Reference Guide Action.InputParameter Class

Signature

```
   public String getDescription()

```

Return Value

Type: String

Description of the input parameter of the invocable action.

##### **`getLabel()`**

Gets the label of an input parameter of an invocable action.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Label of the input parameter of the invocable action.

##### **`getMaxOccurs()`**

Gets the maximum number of occurrences for an input parameter of an invocable action.

Signature

```
   public Integer getMaxOccurs()

```

Return Value

Type: Integer

Maximum number of occurrences for the input parameter of the invocable action. If occurrences are unbounded, returns -1.

##### **`getName()`**

Gets the name of an input parameter of an invocable action.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the input parameter of the invocable action.


Apex Reference Guide Action.InputParameter Class

##### **`getPicklistValues()`**

Gets a list of picklist values for an input parameter of an invocable action.

Signature

```
   public List<Invocable.Action.PicklistValue> getPicklistValues()

```

Return Value

Type: List<Invocable.Action.PicklistValue>

##### **`getPlaceholderText()`**

Gets the placeholder text of an input parameter of an invocable action.

Signature

```
   public String getPlaceholderText()

```

Return Value

Type: String

Placeholder text of the input parameter of the invocable action.

##### **`getRequired()`**

Indicates whether an input parameter of an invocable action is required.

Signature

```
   public Boolean getRequired()

```

Return Value

Type: Boolean

This method returns `true` if the input parameter of the invocable action is required.

##### **`getSObjectType()`**

Gets the sObject type of an input parameter of an invocable action.

Signature

```
   public String getSObjectType()

```

Return Value

Type: String

SObject type of the input parameter of the invocable action.


### Apex Reference Guide Action.OutputParameter Class

##### **`getSetupReferenceType()`**

Gets the setup reference types of an input parameter of an invocable action.

Signature

```
   public List<String> getSetupReferenceType()

```

Return Value

Type: List<String>

List of setup reference type identifiers of the input parameter of the invocable action.

##### **`getToolingType()`**

Gets the tooling type of and input parameter of an invocable action.

Signature

```
   public String getToolingType()

```

Return Value

Type: String

Tooling type of the input parameter of the invocable action.

##### **`getType()`**

Gets the data type of an input parameter of an invocable action.

Signature

```
   public String getType()

```

Return Value

Type: String

Data type of the input parameter of the invocable action.

### Action.OutputParameter Class

Contains methods about metadata returned by invocable actions.

Namespace

Invocable on page 2929


Apex Reference Guide Action.OutputParameter Class

Example

```
   Invocable.Action action = Invocable.Action.createStandardAction('otherActionName');

   List<Invocable.Action.DescribeResult> results = action.getDescribe();

   for (Invocable.Action.DescribeResult result : results) {

      for (Invocable.Action.InputParameter input : result.getInputs()) {

        List<Invocable.Action.AdditionalAttribute> attrs = input.getAdditionalAttributes();

        if (attrs != null) {

           for (Invocable.Action.AdditionalAttribute attr : attrs) {

             System.debug('Attribute: ' + attr.getName());

             System.debug('Data Type: ' + attr.getDataType());

             // Handle collection vs single value

             if (attr.getIsCollection()) {

               if (attr.getDataType() == 'STRING') {

                  List<String> stringValues = attr.getValueAsStringList();

                  System.debug('String Values: ' + stringValues);

               }

             } else {

               System.debug('Value: ' + attr.getValue());

             }

           }

        }

      }

   }

```

IN THIS SECTION:

#### Action.OutputParameter Methods Action.OutputParameter Methods The following are methods for Action.OutputParameter .

IN THIS SECTION:

getAdditionalAttributes()
Gets a list of additional attributes for an invocable action output parameter.

getApexClass()
Gets the Apex class name of an output parameter for an invocable action.

getDescription()
Gets the description of an output parameter of an invocable action.

getLabel()
Gets the label of an output parameter of an invocable action.

getMaxOccurs()
Gets the maximum number of occurrences for an output parameter of an invocable action.


Apex Reference Guide Action.OutputParameter Class

getName()
Gets the name of an output parameter of an invocable action.

getPicklistValues()
Gets a list of picklist values for an output parameter of an invocable action.

getSObjectType()
Gets the sObject type of an output parameter of an invocable action.

getType()
Gets the data type of an output parameter of an invocable action.

##### **`getAdditionalAttributes()`**

Gets a list of additional attributes for an invocable action output parameter.

Signature

```
   public List<Invocable.Action.AdditionalAttribute> getAdditionalAttributes()

```

Return Value

Type: List<Invocable.Action.AdditionalAttribute>

##### **`getApexClass()`**

Gets the Apex class name of an output parameter for an invocable action.

Signature

```
   public String getApexClass()

```

Return Value

Type: String

Apex class name of the output parameter of the invocable action.

##### **`getDescription()`**

Gets the description of an output parameter of an invocable action.

Signature

```
   public String getDescription()

```

Return Value

Type: String

Description of the output parameter of the invocable action.


Apex Reference Guide Action.OutputParameter Class

##### **`getLabel()`**

Gets the label of an output parameter of an invocable action.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Label of the output parameter of the invocable action.

##### **`getMaxOccurs()`**

Gets the maximum number of occurrences for an output parameter of an invocable action.

Signature

```
   public Integer getMaxOccurs()

```

Return Value

Type: Integer

Maximum number of occurrences for the output parameter of the invocable action. If occurrences are unbounded, returns -1.

##### **`getName()`**

Gets the name of an output parameter of an invocable action.

Signature

```
   public String getName()

```

Return Value

Type: String

Name of the output parameter of the invocable action.

##### **`getPicklistValues()`**

Gets a list of picklist values for an output parameter of an invocable action.

Signature

```
   public List<Invocable.Action.PicklistValue> getPicklistValues()

```

Return Value

Type: List<Invocable.Action.PicklistValue on page 2962>


### Apex Reference Guide Action.PicklistValue Class

##### **`getSObjectType()`**

Gets the sObject type of an output parameter of an invocable action.

Signature

```
   public String getSObjectType()

```

Return Value

Type: String

SObject type of the output parameter of the invocable action.

##### **`getType()`**

Gets the data type of an output parameter of an invocable action.

Signature

```
   public String getType()

```

Return Value

Type: String

Data type of the output parameter of the invocable action.

### Action.PicklistValue Class

Contains methods to get metadata about a single value in a picklist used by invocable action parameters.

Namespace

Invocable

Example

```
   Invocable.Action action = Invocable.Action.createStandardAction('anotherActionName');

   List<Invocable.Action.DescribeResult> describeResults = action.getDescribe();

   for (Invocable.Action.DescribeResult dr : describeResults) {

      for (Invocable.Action.InputParameter input : dr.getInputs()) {

        List<Invocable.Action.PicklistValue> picklistValues = input.getPicklistValues();

        if (picklistValues != null) {

           for (Invocable.Action.PicklistValue plv : picklistValues) {

             System.debug('Label: ' + plv.getLabel());

             System.debug('Value: ' + plv.getValue());

             System.debug('Is Default: ' + plv.getDefaultValue());

             System.debug('Is Active: ' + plv.getActive());

           }

        }

```


Apex Reference Guide Action.PicklistValue Class

```
      }

   }

```

IN THIS SECTION:

#### Action.PicklistValue Methods Action.PicklistValue Methods The following are methods for Action.PicklistValue .

IN THIS SECTION:

##### getActive()

Indicates whether a picklist value used by an invocable action parameter is active.

##### getDefaultValue()

Indicates whether a picklist value used by an invocable action parameter is the default value.

getLabel()
Gets the label of a picklist value used by an invocable action parameter.

getValidFor()
Gets the valid-for dependency information for a picklist value used by an invocable action parameter.

getValue()
Gets the API value of a picklist option used by an invocable action parameter.

##### **`getActive()`**

Indicates whether a picklist value used by an invocable action parameter is active.

Signature

```
   public Boolean getActive()

```

Return Value

Type: Boolean

This method returns `true` if the picklist value for the invocable action parameter is active.

##### **`getDefaultValue()`**

Indicates whether a picklist value used by an invocable action parameter is the default value.

Signature

```
   public Boolean getDefaultValue()

```

Return Value

Type: Boolean


### Apex Reference Guide Action.Result Class

This method returns `true` if the picklist value used by the invocable action parameter is the default value.

##### **`getLabel()`**

Gets the label of a picklist value used by an invocable action parameter.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Label of the picklist value used by the invocable action parameter.

##### **`getValidFor()`**

Gets the valid-for dependency information for a picklist value used by an invocable action parameter.

Signature

```
   public String getValidFor()

```

Return Value

Type: String

Valid-for dependency string of the picklist value used by the invocable action parameter, or null if no dependencies exist.

##### **`getValue()`**

Gets the API value of a picklist option used by an invocable action parameter.

Signature

```
   public String getValue()

```

Return Value

Type: String

API value of the picklist option used by the invocable action parameter.

### Action.Result Class

Contains methods to retrieve results from invocable actions called from Apex code.

Namespace

Invocable


Apex Reference Guide Action.Result Class

IN THIS SECTION:

#### Action.Result Methods Action.Result Methods The methods are for Action.Result .

IN THIS SECTION:

##### clone()

Creates a copy of the `Invocable.Action.Result` .

##### getAction()

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

##### **`getAction()`**

Gets the invocable action that was invoked and caused a result to be returned.

Signature

```
   public Invocable.Action getAction()

```

Return Value

Type: Invocable.Action on page 2930


Apex Reference Guide Action.Result Class

##### **`getErrors()`**

Gets a list of errors that were returned by an invocable action.

Signature

```
   public List on page 4226<Invocable.Action.Error on page 2949> getErrors()

```

Return Value

Type: List on page 4226<Invocable.Action.Error on page 2949>

##### **`getInvocationParameters()`**

Gets a list of the parameter values set for an invocable action. This method returns a list that contains the input parameter values for
each invocation of an action. Each map in the list contains a key for the name of each input parameter.

Signature

```
   public Map<String,Object> getInvocationParameters()

```

Return Value

Type: Map on page 4013<String on page 4226,Object>

##### **`getOutputParameters()`**

Gets a list of the parameter values returned by an invocable action. This method returns a list that contains the result for each invocation
of an action. Each map in the list contains a key for the name of each output parameter.

Signature

```
   public Map<String,Object> getOutputParameters()

```

Return Value

Type: Map on page 4013<String on page 4226,Object>

##### **`isSuccess()`**

Determines if an invocable action ran without errors.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

This method returns `true` if the invocable action ran successfully.


## Apex Reference Guide InvoiceWriteOff Namespace InvoiceWriteOff Namespace The InvoiceWriteOff namespace provides classes to create credit memos with the total charge amount on the invoice as the

write-off amount.

## The InvoiceWriteOff namespace includes these classes.

**•** [WriteOffInvoiceInputList Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInputList.htm)

**•** [WriteOffInvoiceInput Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceInput.htm)

**•** [WriteOffInvoiceResponseList Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseList.htm)

**•** [WriteOffInvoiceResponse Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponse.htm)

**•** [WriteOffInvoiceResponseError Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_InvoiceWriteOff_WriteOffInvoiceResponseError.htm)

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

Usage

### Use AppAnalytics and its methods to log App Analytics custom interactions.

Example

```
   public void submitClicked() {

        Id jobId = System.enqueueJob(new MyQueueable(colorValue));

        IsvPartners.AppAnalytics.logCustomInteraction(

           MyPageInteractions.SUBMIT_CLICKED, jobId);

```


Apex Reference Guide AppAnalytics Class

IN THIS SECTION:

#### AppAnalytics Methods AppAnalytics Methods These are methods for AppAnalytics .

IN THIS SECTION:

##### logCustomInteraction(interactionLabel, interactionId)

Logs the custom interaction using a label that you provide as an enum value and an interaction ID.

##### logCustomInteraction(interactionLabel, interactionUuid)

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

Return Value

Type: Void

##### **`logCustomInteraction(interactionLabel, interactionUuid)`**

Logs the custom interaction using a label that you provide as an enum value and an interaction ID that you provide as an Apex UUID.

Signature

```
   public static void logCustomInteraction(Object interactionLabel, System.UUID

   interactionUuid)

```


## Apex Reference Guide KbManagement Namespace

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

## KbManagement Namespace The KbManagement namespace provides a class for managing knowledge articles. The following is the class in the KbManagement namespace.

IN THIS SECTION:

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.

### PublishingService Class

Use the methods in the `KbManagement.PublishingService` class to manage the lifecycle of an article and its translations.


Apex Reference Guide PublishingService Class

Namespace

KbManagement

Usage

Use the methods in the `KbManagement.PublishingService` class to manage the following parts of the lifecycle of an article
and its translations:

#### • Publishing

**•** Updating

**•** Retrieving

**•** Deleting

**•** Submitting for translation

**•** Setting a translation to complete or incomplete status

**•** Archiving

**•** Assigning review tasks for draft articles or translations

Note: Date values are based on GMT.

[To use the methods in this class, you must enable Salesforce Knowledge. See Salesforce Knowledge Implementation Guide for more](https://resources.docs.salesforce.com/262/latest/en-us/sfdc/pdf/salesforce_knowledge_implementation_guide.pdf)
information on setting up Salesforce Knowledge.

#### PublishingService Methods The following are methods for PublishingService . All methods are static.

IN THIS SECTION:

archiveOnlineArticle(articleId, scheduledDate)
Archives an online version of an article. If the specified scheduledDate is null, the article is archived immediately. Otherwise, it archives
the article on the scheduled date.

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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

##### cancelScheduledArchivingOfArticle(articleId)

```

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

```


Apex Reference Guide PublishingService Class

##### cancelScheduledPublicationOfArticle(articleId)

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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


Apex Reference Guide PublishingService Class

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

```


## Apex Reference Guide LxScheduler Namespace LxScheduler Namespace The LxScheduler namespace provides an interface and classes for integrating Salesforce Scheduler with external calendars. The following are the classes and the interface in the LxScheduler namespace.

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


### Apex Reference Guide GetAppointmentCandidatesInput Class GetAppointmentCandidatesInput Class

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


Apex Reference Guide GetAppointmentCandidatesInput Class

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

Important:

**•** When you're using shifts: You must specify `workTypeGroupId` or the ID of the work type. When you specify the ID of the
work type, all other Builder parameters are optional and Scheduler retrieves their values from the database.

**•** When you're using operating hours: You don't need to specify `workTypeGroupId` or the ID of the work type. Scheduler
applies `durationInMinutes` and all other builder parameters as you configure them.

```
   //Build SkillRequirement

     lxscheduler.SkillRequirement skillReq = new lxscheduler.SkillRequirementBuilder()

      .setSkillId('0C5RM0000004EZS0A2')

      .setSkillLevel(90)

      .build();

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

```


### Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

```
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

IN THIS SECTION:

#### GetAppointmentCandidatesInputBuilder Methods GetAppointmentCandidatesInputBuilder Methods

### The following are methods for GetAppointmentCandidatesInputBuilder .

IN THIS SECTION:

build()
Returns an instance of the `lxscheduler.GetAppointmentCandidatesInput` object.

setAccountId(accountId)
Sets the ID of the associated account for which you want to create the appointments.


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


Apex Reference Guide GetAppointmentCandidatesInputBuilder Class

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


### Apex Reference Guide GetAppointmentSlotsInput Class

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

### GetAppointmentSlotsInput Class

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


Apex Reference Guide GetAppointmentSlotsInput Class

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


Apex Reference Guide GetAppointmentSlotsInput Class

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

```


### Apex Reference Guide GetAppointmentSlotsInputBuilder Class GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


Apex Reference Guide GetAppointmentSlotsInputBuilder Class

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


### Apex Reference Guide SchedulerResources Class SchedulerResources Class

Contains methods that holds the business logic to get resources availability.

Namespace

LxScheduler

Implementation Considerations

### Apex implementation of the methods in the SchedulerResources class should adhere to Apex Governor Limits. It includes

synchronous heap size limit, synchronous CPU time limit, and synchronous concurrent transactions for long running transactions. To
avoid governor limits, you must tune the input by reducing the time frame, limiting number of service resources, or limiting number or
territories at a time. This will reduce the overall transaction time and response size of the implementation. For more information on
[standard Apex Governer Limits, see Salesforce Developer Limits and Allocations Quick Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm)

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

#### SchedulerResources Methods SchedulerResources Methods

### The following are methods for SchedulerResources .

IN THIS SECTION:

getAppointmentCandidates(getAppointmentCandidatesInput)
Returns a list of service resources based on work type group or work type and service territories.

getAppointmentSlots(getAppointmentSlotsInput)
Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

setAppointmentCandidatesMock(expectedResponse)
Sets a mock object when running tests for the `getAppointmentCandidates` method.

setAppointmentSlotsMock(expectedResponse)
Sets a mock object when running tests for the `getAppointmentSlots` method.


Apex Reference Guide SchedulerResources Class

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


Apex Reference Guide SchedulerResources Class

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


Apex Reference Guide SchedulerResources Class

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


Apex Reference Guide SchedulerResources Class

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


### Apex Reference Guide SkillRequirement Class

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

IN THIS SECTION:

#### SkillRequirementBuilder Methods SkillRequirementBuilder Methods

### The following are methods for SkillRequirementBuilder .

IN THIS SECTION:

##### build()

Returns an instance of the `lxscheduler.SkillRequirement` object.

setSkillId(skillId)
Sets the skill that is required to complete a particular task for a work type. This is a required field.

setSkillLevel(skillLevel)
Sets the level of the skill that is required to complete a particular task for a work type

##### **`build()`**

Returns an instance of the `lxscheduler.SkillRequirement` object.


### Apex Reference Guide WorkType Class

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


### Apex Reference Guide WorkTypeBuilder Class

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

setBlockTimeAfterAppointmentInMinutes(blockTimeAfterAppointmentInMinutes)
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


Apex Reference Guide WorkTypeBuilder Class

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


Apex Reference Guide WorkTypeBuilder Class

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


Apex Reference Guide WorkTypeBuilder Class

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


### Apex Reference Guide ServiceResourceScheduleHandler Interface

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

#### ServiceResourceScheduleHandler Methods

### The following are methods for ServiceResourceScheduleHandler .

IN THIS SECTION:

getUnavailableTimeslots(var1)
Passes the required information to get unavailable time slots from an external system. The implementation of this method returns
the `lxscheduler.ServiceResourceSchedule` class.


Apex Reference Guide ServiceResourceScheduleHandler Interface

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

```


Apex Reference Guide ServiceResourceScheduleHandler Interface

```
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

```


### Apex Reference Guide ServiceAppointmentRequestInfo Class

```
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

#### ServiceAppointmentRequestInfo Constructors

ServiceAppointmentRequestInfo Methods

#### ServiceAppointmentRequestInfo Constructors

### The following are constructors for ServiceAppointmentRequestInfo .

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


Apex Reference Guide ServiceAppointmentRequestInfo Class

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

getAccountId()
Returns the account ID of the customer if the API request contains one.

getCorrelationId()
Returns a unique identifier for a request.

getEndDate()
Returns the end date and time for which unavailable time slots are requested.


Apex Reference Guide ServiceAppointmentRequestInfo Class

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


Apex Reference Guide ServiceAppointmentRequestInfo Class

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


### Apex Reference Guide ServiceResourceInfo Class

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

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceInfo Constructors

ServiceResourceInfo Methods

#### ServiceResourceInfo Constructors

### The following are constructors for ServiceResourceInfo .

IN THIS SECTION:

##### ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds, resourceType)

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.

##### **`ServiceResourceInfo(userId, userName, email, serviceResourceId, territoryIds,`**

```
  resourceType)

```

Creates a new instance of the `lxscheduler.ServiceResourceInfo` class using the specified service resource details.


Apex Reference Guide ServiceResourceInfo Class

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

```
   resourceType
```

Type: String

The type of the service resource such as Technician or Asset.

#### ServiceResourceInfo Methods The following are methods for ServiceResourceInfo .

IN THIS SECTION:

getEmail()
Returns the email ID of the service resource.

getResourceType()
Returns the type of the service resource such as Technician or Asset.

getServiceResourceId()
Returns the ID of the service resource.

getTerritoryIds()
Returns a list of requested service territories for the service resource.

getUserId()
Returns the user ID of the service resource.

getUserName()
Returns the user name of the service resource.


Apex Reference Guide ServiceResourceInfo Class

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


### Apex Reference Guide ServiceResourceSchedule Class

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

Namespace

LxScheduler

IN THIS SECTION:

#### ServiceResourceSchedule Constructors

ServiceResourceSchedule Properties

#### ServiceResourceSchedule Constructors

### The following are constructors for ServiceResourceSchedule .

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


### Apex Reference Guide UnavailableTimeslot Class

Parameters

##### _`serviceResourceId`_

Type: String

Record ID of the service resource.

##### _`unavailableTimeslots`_

Type: Set<lxscheduler.UnavailableTimeslot>

An instance of lxscheduler.UnavailableTimeslot class.

#### ServiceResourceSchedule Properties The following are properties for ServiceResourceSchedule .

IN THIS SECTION:

##### serviceResourceId

Record ID of the service resource.

##### unavailableTimeslots

An instance of lxscheduler.UnavailableTimeslot class.

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


Apex Reference Guide UnavailableTimeslot Class

Namespace

LxScheduler

IN THIS SECTION:

#### UnavailableTimeslot Constructors UnavailableTimeslot Properties UnavailableTimeslot Constructors The following are constructors for UnavailableTimeslot .

IN THIS SECTION:

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.

##### UnavailableTimeslot(timeMin, timeMax)

Creates an instance of lxscheduler.UnavailableTimeslot class.

Signature

```
   public UnavailableTimeslot(Datetime timeMin, Datetime timeMax)

```

Parameters

```
   timeMin
```

Type: Datetime

Start time of an unavailable time slot.

```
   timeMax
```

Type: Datetime

End time of an unavailable time slot.

#### UnavailableTimeslot Properties The following are properties for UnavailableTimeslot .

IN THIS SECTION:

timeMax
End time of an unavailable time slot.

timeMin
Start time of an unavailable time slot.


## Apex Reference Guide Messaging Namespace

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

## Messaging Namespace The Messaging namespace provides classes and methods for Salesforce notifications and email functionality. The Messaging namespace includes these classes, enums, and interfaces.

IN THIS SECTION:

AttachmentRetrievalOption Enum
Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

ActionableNotification Class
Contains information about an actionable custom notification.

ActionableNotification.Builder Class
Contains methods to build an instance of the `Messaging.ActionableNotification` class, which is used to configure
actionable notifications for mobile devices.

ActionError Enum
Specifies the error that occurred during the execution of an actionable notification.

ActionResult Class
Contains information about the execution of an actionable notification.

ActionResult.Builder Class
Contains methods to build and validate an instance of the `Messaging.ActionResult` class.

CustomNotification Class

`CustomNotification` is used to create, configure, and send custom notifications from Apex code.


Apex Reference Guide Messaging Namespace

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

NotificationActionHandler Interface
Implement this interface to execute an action on a custom notification.

RenderEmailTemplateBodyResult Class
Contains the results for rendering email templates.

RenderEmailTemplateError Class
Represents an error that the `RenderEmailTemplateBodyResult` object can contain.

SendEmailError Class
Represents an error that the SendEmailResult object may contain.

SendEmailResult Class
Contains the result of sending an email message.

SingleEmailMessage Class
Contains methods for sending single email messages.


### Apex Reference Guide AttachmentRetrievalOption Enum AttachmentRetrievalOption Enum

Provides options for including attachment metadata only, attachment metadata and content, or excluding attachments.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

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

### ActionableNotification Class

Contains information about an actionable custom notification.

Namespace

Messaging

Example

This example shows how to create an ActionableNotification object by using the `ActionableNotification.Builder` on
page 3030 class.

```
Messaging.ActionableNotification notification =

new Messaging.ActionableNotification.Builder()

.withNotificationTypeId('0MLXXXXXXXXXXXX4AC')

```


Apex Reference Guide ActionableNotification Class

```
   .withActionIdentifier('testAction')

   .withRecipientId('005XXXXXXXXXXXX')

   .withSenderId('005XXXXXXXXXXXX')

   .withTargetId('500XXXXXXXXXXXXYAI')

   .withTargetPageRef('/lightning/r/Case/500XXXXXXXXXXXXYAI/view')

   .build();

```

IN THIS SECTION:

#### ActionableNotification Methods ActionableNotification Methods The following are methods for ActionableNotification .

IN THIS SECTION:

##### getActionIdentifier()

Return the unique action identifier (API name) for the custom notification action.

##### getNotificationTypeId()

Return the ID of the custom notification type used for the notification.

getRecipientId()
Return the user ID of the recipient of the notification.

getSenderId()
Return the user ID of the sender of the notification.

getTargetId()
Return the record ID for the target record of the notification.

getTargetPageRef()
Return the `PageReference` for the navigation target of the notification.

##### **`getActionIdentifier()`**

Return the unique action identifier (API name) for the custom notification action.

This `actionIdentifier` must belong to the action group associated with the custom notification.

Signature

```
   public String getActionIdentifier()

```

Return Value

Type: String

##### **`getNotificationTypeId()`**

Return the ID of the custom notification type used for the notification.


Apex Reference Guide ActionableNotification Class

Signature

```
   public String getNotificationTypeId()

```

Return Value

Type: String

##### **`getRecipientId()`**

Return the user ID of the recipient of the notification.

Signature

```
   public String getRecipientId()

```

Return Value

Type: String

##### **`getSenderId()`**

Return the user ID of the sender of the notification.

Signature

```
   public String getSenderId()

```

Return Value

Type: String

##### **`getTargetId()`**

Return the record ID for the target record of the notification.

Signature

```
   public String getTargetId()

```

Return Value

Type: String

##### **`getTargetPageRef()`**

Return the `PageReference` for the navigation target of the notification.

Signature

```
   public String getTargetPageRef()

```


### Apex Reference Guide ActionableNotification.Builder Class

Return Value

Type: String

### ActionableNotification.Builder Class

Contains methods to build an instance of the `Messaging.ActionableNotification` class, which is used to configure
actionable notifications for mobile devices.

Namespace

Messaging

Example

See the example for the `Messaging.ActionableNotification` class on page 3027.

IN THIS SECTION:

#### ActionableNotification.Builder Methods ActionableNotification.Builder Methods

### The following are methods for ActionableNotification.Builder .

IN THIS SECTION:

##### build()

Returns an instance of the `Messaging.ActionableNotification` class.

withActionIdentifier(actionIdentifier)
Sets the unique action identifier (API name) for the custom notification action.

withNotificationTypeId(notificationTypeId)
Sets the ID of the custom notification type.

withRecipientId(recipientId)
Sets the user ID of the custom notification recipient.

withSenderId(senderId)
Sets the sender of the custom notification.

withTargetId(targetId)
Sets the record ID for the target record of the notification.

withTargetPageRef(targetPageRef)
The PageReference for the navigation target of the notification.

##### **`build()`**

Returns an instance of the `Messaging.ActionableNotification` class.


Apex Reference Guide ActionableNotification.Builder Class

Signature

```
   public Messaging.ActionableNotification build()

```

Return Value

Type: Messaging.ActionableNotification on page 3027

##### **`withActionIdentifier(actionIdentifier)`**

Sets the unique action identifier (API name) for the custom notification action.

This `actionIdentifier` must belong to the action group associated with the custom notification.

Signature

```
   public Messaging.ActionableNotification.Builder withActionIdentifier(String

   actionIdentifier)

```

Parameters

```
   actionIdentifier
```

Type: String

The API name of the action.

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030

##### **`withNotificationTypeId(notificationTypeId)`**

Sets the ID of the custom notification type.

Signature

```
   public Messaging.ActionableNotification.Builder withNotificationTypeId(String

   notificationTypeId)

```

Parameters

```
   notificationTypeId
```

Type: String

The ID of the custom notification type being used for the notification.

A notification type is required to send a custom notification.

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030


Apex Reference Guide ActionableNotification.Builder Class

##### **`withRecipientId(recipientId)`**

Sets the user ID of the custom notification recipient.

Signature

```
   public Messaging.ActionableNotification.Builder withRecipientId(String recipientId)

```

Parameters

```
   recipientId
```

Type: String

The user ID of the notification recipient.

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030

##### **`withSenderId(senderId)`**

Sets the sender of the custom notification.

Signature

```
   public Messaging.ActionableNotification.Builder withSenderId(String senderId)

```

Parameters

```
   senderId
```

Type: String

The user ID of the sender of the notification. Setting a sender is optional.

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030

##### **`withTargetId(targetId)`**

Sets the record ID for the target record of the notification.

You must specify either a `targetID` or a `targetPageRef` .

Signature

```
   public Messaging.ActionableNotification.Builder withTargetId(String targetId)

```

Parameters

```
   targetId
```

Type: String

The ID of the target record.


### Apex Reference Guide ActionError Enum

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030

##### **`withTargetPageRef(targetPageRef)`**

The PageReference for the navigation target of the notification.

You must specify either a `targetID` or a `targetPageRef` .

Signature

```
   public Messaging.ActionableNotification.Builder withTargetPageRef(String targetPageRef)

```

Parameters

```
   targetPageRef
```

Type: String

The target page reference as a URL string, for example `'/lightning/r/Case/500XXXXXXXXXXXXYAI/view'` . For more
examples, see pageReference Types.

Return Value

Type: Messaging.ActionableNotification.Builder on page 3030

### ActionError Enum

Specifies the error that occurred during the execution of an actionable notification.

Enum Values

The following are the values of the `Messaging.ActionError` enum.

**Value** **Description**

`ACCESS_DENIED` Indicates that the user is not authorized to execute the action.

`ACTION_NOT_IMPLEMENTED` Indicates that the action identifier is unsupported.

`INTERNAL_ERROR` Indicates an internal error during execution of the action.

`INVALID_ACTION_PARAMETERS` Indicates that the parameters passed to the methods for
`Messaging.ActionableNotification.Builder` are invalid.

`INVALID_STATE` Indicates an invalid state.

### ActionResult Class

Contains information about the execution of an actionable notification.


Apex Reference Guide ActionResult Class

Namespace

Messaging

Usage

#### This ActionResult instance represents the successful execution of an actionable notification.

```
   Messaging.ActionResult result =

   new Messaging.ActionResult.Builder()

   .withSuccess(true)

   .withMessage('Action is executed successfully')

   .build();

#### This ActionResult instance represents the unsuccessful execution of an actionable notification.

   Messaging.ActionResult result =

   new Messaging.ActionResult.Builder()

   .withSuccess(false)

   .withMessage('Error updating case')

   .withErrorCode(Messaging.ActionError.INTERNAL_ERROR)

   .build();

```

IN THIS SECTION:

#### ActionResult Methods ActionResult Methods The following are methods for ActionResult .

IN THIS SECTION:

##### getErrorCode()

If an error occurred, returns an object that provides the error code and a description.

getMessage()
Returns the success or error message that displays for the user.

isSuccess()
Returns `true` if the action executed successfully; otherwise returns `false` .

##### **`getErrorCode()`**

If an error occurred, returns an object that provides the error code and a description.

Signature

```
   public Messaging.ActionError getErrorCode()

```

Return Value

Type: Messaging.ActionError on page 3033


### Apex Reference Guide ActionResult.Builder Class

##### **`getMessage()`**

Returns the success or error message that displays for the user.

Signature

```
   public String getMessage()

```

Return Value

Type: String

##### **`isSuccess()`**

Returns `true` if the action executed successfully; otherwise returns `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### ActionResult.Builder Class

Contains methods to build and validate an instance of the `Messaging.ActionResult` class.

Namespace

Messaging

Usage

See the example for the NotificationActionHandler Interface on page 3076.

IN THIS SECTION:

#### ActionResult.Builder Methods ActionResult.Builder Methods

### The following are methods for ActionResult.Builder .

IN THIS SECTION:

build()
### Validates and returns the action result instance created by using the ActionResult.Builder methods.

withErrorCode(errorCode)
Sets the error message associated with the action error.


Apex Reference Guide ActionResult.Builder Class

##### withMessage(message)

Sets the success or error message associated with the execution of the action.

withSuccess(success)
Sets a Boolean that informs the user whether the execution of the action was successful ( `true` ) or not ( `false` ).

##### **`build()`**

Validates and returns the action result instance created by using the `ActionResult.Builder` methods.

Signature

```
   public Messaging.ActionResult build()

```

Return Value

Type: Messaging.ActionResult on page 3033

##### **`withErrorCode(errorCode)`**

Sets the error message associated with the action error.

Signature

```
   public Messaging.ActionResult.Builder withErrorCode(Messaging.ActionError errorCode)

```

Parameters

```
   errorCode
```

Type: Messaging.ActionError

The error message.

Return Value

Type: Messaging.ActionResult.Builder on page 3035

##### **`withMessage(message)`**

Sets the success or error message associated with the execution of the action.

Signature

```
   public Messaging.ActionResult.Builder withMessage(String message)

```

Parameters

```
   message
```

Type: String

The notification message.


### Apex Reference Guide CustomNotification Class

Return Value

Type: Messaging.ActionResult.Builder on page 3035

##### **`withSuccess(success)`**

Sets a Boolean that informs the user whether the execution of the action was successful ( `true` ) or not ( `false` ).

Signature

```
   public Messaging.ActionResult.Builder withSuccess(Boolean success)

```

Parameters

```
   success
```

Type: Boolean

Return Value

Type: Messaging.ActionResult.Builder on page 3035

### CustomNotification Class CustomNotification is used to create, configure, and send custom notifications from Apex code.

Namespace

Messaging

Usage

### CustomNotification allows two approaches to creating and configuring a custom notification.

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


Apex Reference Guide CustomNotification Class

Important: Before Winter ’21 you could set only a target record ( `targetID` ) for a notification. Most client applications expect
to find a `targetID` in the notification payload. If you can’t update a client app to handle notifications that include only a
`targetPageRef`, set the `targetID` to a dummy value.

**Execution Context and Notification Permissions**

By default, Apex code executes in user mode, which means that user permissions on objects and field-level security are respected. A
user cannot run code that tries to access fields or objects that are hidden from the user. Therefore, to send notifications with
`CustomNotification`, you must have the Send Custom Notifications user permission. If you don’t have the required permission,
the `send()` method fails.

Example

This example Apex class provides a static method for sending a custom notification to a recipient list. Call this method from a trigger,
flow, or wherever you want to send a custom notification from Apex.

```
   public without sharing class CustomNotificationFromApex {

      public static void notifyUsers(Set<String> recipientsIds, String targetId, String

   actionGroupId) {

        // Get the Id for our custom notification type

        CustomNotificationType notificationType =

           [SELECT Id, DeveloperName

           FROM CustomNotificationType

           WHERE DeveloperName='Custom_Notification'

           WITH USER_MODE

           LIMIT 1];

        // Create a new custom notification

        Messaging.CustomNotification notification = new Messaging.CustomNotification();

        // Set the contents for the notification

        notification.setTitle('Apex Custom Notification');

        notification.setBody('The notifications are coming from INSIDE the Apex!');

        // Set the notification type and target

        notification.setNotificationTypeId(notificationType.Id);

        notification.setTargetId(targetId);

        // Set the Action Group (This makes the notification actionable)

        if (String.isNotBlank(actionGroupId)) {

           notification.setActionGroupId(actionGroupId);

        }

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


Apex Reference Guide CustomNotification Class

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

_Actions Developer Guide_ [: Custom Notification Actions](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_action.meta/api_action/actions_obj_custom_notification.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customnotificationtype.htm)_ : CustomNotificationType

#### CustomNotification Constructors The following are constructors for CustomNotification .

IN THIS SECTION:

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

##### CustomNotification(typeId, sender, title, body, targetId, targetPageRef)

Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this
constructor, you don’t need to call the various setter methods to define the custom notification attributes.

##### CustomNotification()

Creates a new instance of the `Messaging.CustomNotification` class.

Signature

```
   public CustomNotification()

##### CustomNotification(typeId, sender, title, body, targetId, targetPageRef)

```

Creates an instance of the `Messaging.CustomNotification` class using the specified parameters. When you use this constructor,
you don’t need to call the various setter methods to define the custom notification attributes.

Signature

```
   public CustomNotification(String typeId, String sender, String title, String body,

   String targetId, String targetPageRef)

```


Apex Reference Guide CustomNotification Class

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

The `PageReference` [for the navigation target of the notification. To see how to specify the target using JSON, see pageReference](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/components_navigation_page_definitions.htm)
[Types.](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/components_navigation_page_definitions.htm)

You must specify either a `targetID` or a `targetPageRe` . See Custom Notification Usage.

Usage

A client may see a truncated notification title or body depending on the delivery channel or app, and how the Connect API notification
parameters are configured. For more information on the `trimMessages` [query parameter, see Notification .](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_notifications_list.htm)

#### CustomNotification Methods The following are methods for CustomNotification .

IN THIS SECTION:

send(users)
Sends a custom notification to the specified users.

setNotificationTypeId(id)
Sets the type of the custom notification.

setTitle(title)
Sets the title of the custom notification.

setBody(body)
Sets the body of the custom notification.


Apex Reference Guide CustomNotification Class

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

Example

See the Custom Notification Example.

##### setNotificationTypeId(id)

Sets the type of the custom notification.

Signature

```
   public void setNotificationTypeId(String id)

```


Apex Reference Guide CustomNotification Class

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


Apex Reference Guide CustomNotification Class

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


### Apex Reference Guide Email Class (Base Email Methods)

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

### Email Class (Base Email Methods)

Contains base email methods common to both single and mass email.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

If templates are not being used, all email content must be in plain text, HTML, or both.Visualforce email templates cannot be used for
mass email.


Apex Reference Guide Email Class (Base Email Methods)

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

Usage

Note: If the BCC compliance option is set at the organization level, the user cannot add BCC addresses on standard messages.
The following error code is returned: `BCC_NOT_ALLOWED_IF_BCC_ COMPLIANCE_ENABLED` . Contact your Salesforce
representative for information on BCC compliance.


Apex Reference Guide Email Class (Base Email Methods)

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

Signature

```
   public Void setSaveAsActivity(Boolean saveAsActivity)

```


### Apex Reference Guide EmailFileAttachment Class

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

### EmailFileAttachment Class

EmailFileAttachment is used in SingleEmailMessage to specify attachments passed in as part of the request, as opposed to existing
documents in Salesforce.


Apex Reference Guide EmailFileAttachment Class

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

IN THIS SECTION:

#### EmailFileAttachment Constructors EmailFileAttachment Properties EmailFileAttachment Constructors The following are constructors for EmailFileAttachment .

IN THIS SECTION:

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

##### EmailFileAttachment()

Creates a new instance of the `Messaging.EmailFileAttachment` class.

Signature

```
   public EmailFileAttachment()

#### EmailFileAttachment Properties The following are properties for EmailFileAttachment .

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


Apex Reference Guide EmailFileAttachment Class

inline
Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).

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


### Apex Reference Guide InboundEmail Class

##### inline

Specifies a Content-Disposition of inline ( `true` ) or attachment ( `false` ).

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


Apex Reference Guide InboundEmail Class

binaryAttachments
A list of binary attachments received with the email, if any.

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

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

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

MassEmailMessage()
Creates a new instance of the `Messaging.MassEmailMessage` class.


Apex Reference Guide MassEmailMessage Class

##### MassEmailMessage()

Creates a new instance of the `Messaging.MassEmailMessage` class.

Signature

```
   public MassEmailMessage()

#### MassEmailMessage Methods

##### The following are methods for MassEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the MassEmailMessage objects. These methods are described in Email Class (Base Email Methods).

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


Apex Reference Guide MassEmailMessage Class

Parameters

```
   targetObjectIds
```

Type: ID[]

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


### Apex Reference Guide InboundEmail.Header Class

Note: If you specify `whatIds`, specify one for each `targetObjectId` ; otherwise, you will receive an `INVALID_ID_FIELD`
error.

### InboundEmail.Header Class

An InboundEmail object stores RFC 2822 email header information in an InboundEmail.Header object with the following properties.

Namespace

Messaging

#### InboundEmail.Header Properties

### The following are properties for InboundEmail.Header .

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


### Apex Reference Guide PushNotification Class

Property Value

Type: String

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_email_inbound_what_is.htm)_ : Apex Email Service

_Apex Developer Guide_ [: Using the InboundEmail Object](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_email_inbound_using.htm)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_email_inbound.htm)_ : Inbound Email

_[Internet Engineering Task Force (IETF) Data Tracker](https://datatracker.ietf.org/doc/html/rfc2822#section-3.6)_ : RFC 2822 Section 3.6

### PushNotification Class PushNotification is used to configure push notifications and send them from an Apex trigger.

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

```


Apex Reference Guide PushNotification Class

```
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

#### PushNotification Constructors

PushNotification Methods

#### PushNotification Constructors The following are the constructors for PushNotification .

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


Apex Reference Guide PushNotification Class

Parameters

```
   payload
```

Type:Map<String, Object>

The payload, expressed as a map of key-value pairs.

#### PushNotification Methods The following are the methods for PushNotification . All are global methods.

IN THIS SECTION:

##### send(application, users)

Sends a push notification message to the specified users.

##### setPayload(payload)

Sets the payload of the push notification message.

setTtl(ttl)
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


### Apex Reference Guide PushNotificationPayload Class

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

PushNotificationPayload Methods


Apex Reference Guide PushNotificationPayload Class

#### PushNotificationPayload Methods The following are the methods for PushNotificationPayload . All are global static methods.

IN THIS SECTION:

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

apple(alertBody, actionLocKey, locKey, locArgs, launchImage, sound, badgeCount, userData)
Helper method that creates a valid Apple payload from the specified arguments.

##### apple(alert, sound, badgeCount, userData)

Helper method that creates a valid Apple payload from the specified arguments.

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


Apex Reference Guide PushNotificationPayload Class

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


### Apex Reference Guide NotificationActionHandler Interface

Return Value

Type: Map<String, Object>

Returns a formatted payload that includes all of the specified arguments.

Usage

To generate a valid payload, you must provide a value for at least one of the following parameters: `alert`, `sound`, `badgeCount` .

### NotificationActionHandler Interface

Implement this interface to execute an action on a custom notification.

Namespace

Messaging

IN THIS SECTION:

#### NotificationActionHandler Methods

NotificationActionHandler Example Implementation
This is an example implementation of the `Messaging.NotificationActionHandler` interface.

#### NotificationActionHandler Methods

### The following are methods for NotificationActionHandler .

IN THIS SECTION:

##### executeAction(actionableNotification)

Executes the actionable notification.

##### **`executeAction(actionableNotification)`**

Executes the actionable notification.

Signature

```
   public Messaging.ActionResult executeAction(Messaging.ActionableNotification

   actionableNotification)

```

Parameters

```
   actionableNotification
```

Type: Messaging.ActionableNotification on page 3027

An actionable custom notification.


Apex Reference Guide NotificationActionHandler Interface

Return Value

Type: Messaging.ActionResult on page 3033

#### NotificationActionHandler Example Implementation

This is an example implementation of the `Messaging.NotificationActionHandler` interface.

```
   global class CaseNotificationActionHandler implements Messaging.NotificationActionHandler

    {

      private static final String ACTION_REASSIGN_TO_QUEUE = 'reassignToQueue';

     private static final String DEFAULT_QUEUE_NAME = 'Queue_Exec'; // Default queue name,

   can be customized

      global Messaging.ActionResult executeAction(Messaging.ActionableNotification

   actionableNotification) {

        try {

           String actionIdentifier = actionableNotification.getActionIdentifier();

           String targetId = actionableNotification.getTargetId();

           if (String.isBlank(actionIdentifier) || String.isBlank(targetId)) {

             return new Messaging.ActionResult.Builder()

               .withSuccess(false)

               .withMessage('Action identifier and target ID are required')

               .withErrorCode(Messaging.ActionError.INVALID_ACTION_PARAMETERS)

               .build();

           }

           // Validate that targetId is a valid Case ID

           if (!targetId.startsWith('500')) {

             return new Messaging.ActionResult.Builder()

               .withSuccess(false)

               .withMessage('Target ID must be a valid Case ID')

               .withErrorCode(Messaging.ActionError.INVALID_ACTION_PARAMETERS)

               .build();

           }

           switch on actionIdentifier {

             when 'reassignToQueue' {

               return reassignCaseToQueue(targetId);

             }

             when else {

               return new Messaging.ActionResult.Builder()

                  .withSuccess(false)

                 .withMessage('Unsupported action identifier: ' + actionIdentifier)

                  .withErrorCode(Messaging.ActionError.ACTION_NOT_IMPLEMENTED)

                  .build();

             }

           }

        } catch (Exception e) {

           return new Messaging.ActionResult.Builder()

             .withSuccess(false)

             .withMessage('An unexpected error occurred: ' + e.getMessage())

```


Apex Reference Guide NotificationActionHandler Interface

```
             .withErrorCode(Messaging.ActionError.INTERNAL_ERROR)

             .build();

        }

      }

      private Messaging.ActionResult reassignCaseToQueue(String caseId) {

        try {

           // Query the case to ensure it exists

          List<Case> cases = [SELECT Id, CaseNumber, OwnerId FROM Case WHERE Id = :caseId

    LIMIT 1];

           if (cases.isEmpty()) {

             return new Messaging.ActionResult.Builder()

               .withSuccess(false)

               .withMessage('Case not found with ID: ' + caseId)

               .withErrorCode(Messaging.ActionError.INVALID_ACTION_PARAMETERS)

               .build();

           }

           Case caseToUpdate = cases[0];

           // Query for the queue to assign the case to

           List<Group> queues = [SELECT Id, Name FROM Group WHERE Type = 'Queue' AND

   DeveloperName = :DEFAULT_QUEUE_NAME LIMIT 1];

           if (queues.isEmpty()) {

             return new Messaging.ActionResult.Builder()

               .withSuccess(false)

               .withMessage('Queue not found: ' + DEFAULT_QUEUE_NAME)

               .withErrorCode(Messaging.ActionError.INVALID_STATE)

               .build();

           }

           // Assign the case to the queue

           caseToUpdate.OwnerId = queues[0].Id;

           update caseToUpdate;

           return new Messaging.ActionResult.Builder()

             .withSuccess(true)

             .withMessage('Case ' + caseToUpdate.CaseNumber + ' successfully assigned

   to queue: ' + DEFAULT_QUEUE_NAME)

             .build();

        } catch (DmlException e) {

           return new Messaging.ActionResult.Builder()

             .withSuccess(false)

             .withMessage('Failed to update case: ' + e.getMessage())

             .withErrorCode(Messaging.ActionError.ACCESS_DENIED)

             .build();

        } catch (Exception e) {

           return new Messaging.ActionResult.Builder()

             .withSuccess(false)

             .withMessage('Error reassigning case to queue: ' + e.getMessage())

             .withErrorCode(Messaging.ActionError.INTERNAL_ERROR)

```


### Apex Reference Guide RenderEmailTemplateBodyResult Class

```
             .build();

        }

      }

   }

```

The following example tests the implementation:

```
   @IsTest

   global class TestNotificationActionHandler {

      @IsTest

      static void testActionHandler() {

        //Set up the data, for example creating a case

        Case newCase = new Case(

           Subject = 'Important Case',

           Status = 'New',

           Priority = 'High'

        );

        insert newCase;

        //Set up Actionable Notification data

        Messaging.ActionableNotification notification =

           new Messaging.ActionableNotification.Builder()

             .withNotificationTypeId('0MLXXXXXXXXXXXX4AC')

             .withActionIdentifier('testAction')

             .withRecipientId(UserInfo.getUserId())

             .withSenderId(UserInfo.getUserId())

             .withTargetId(newCase.Id)

             .withTargetPageRef('/lightning/r/Case/' + newCase.Id + '/view')

             .build();

        Messaging.ActionResult result = Test.testNotificationActionHandler(new

   CaseNotificationActionHandler(), notification);

        //Insert assert statements here to verify your action

      }

   }

### RenderEmailTemplateBodyResult Class

```

Contains the results for rendering email templates.

Namespace

Messaging

IN THIS SECTION:

RenderEmailTemplateBodyResult Methods


Apex Reference Guide RenderEmailTemplateBodyResult Class

#### RenderEmailTemplateBodyResult Methods The following are methods for RenderEmailTemplateBodyResult .

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

Return Value

Type: Boolean


### Apex Reference Guide RenderEmailTemplateError Class RenderEmailTemplateError Class

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

Signature

```
   public String getMessage()

```


### Apex Reference Guide SendEmailError Class

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

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

#### SendEmailError Methods

### The following are methods for SendEmailError . All are instance methods.

IN THIS SECTION:

getFields()
A list of one or more field names. Identifies which fields in the object, if any, affected the error condition.


Apex Reference Guide SendEmailError Class

##### getMessage()

The text of the error message.

##### getStatusCode()

Returns a code that characterizes the error.

getTargetObjectId()
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


### Apex Reference Guide SendEmailResult Class

##### getTargetObjectId()

The ID of the target record for which the error occurred.

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

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

#### SendEmailResult Methods

### The following are methods for SendEmailResult . All are instance methods.

IN THIS SECTION:

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

isSuccess()
Indicates whether the email was successfully submitted for delivery ( `true` ) or not ( `false` ). Even if `isSuccess` is true, it does
not mean the intended recipients received the email, as there could have been a problem with the email address or it could have
bounced or been blocked by a spam blocker.

##### getErrors()

If an error occurred during the `sendEmail` method, a `SendEmailError` object is returned.

Signature

```
   public SendEmailError[] getErrors()

```


### Apex Reference Guide SingleEmailMessage Class

Return Value

Type: Messaging.SendEmailError[]

##### isSuccess() Indicates whether the email was successfully submitted for delivery ( true ) or not ( false ). Even if isSuccess is true, it does not

mean the intended recipients received the email, as there could have been a problem with the email address or it could have bounced
or been blocked by a spam blocker.

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### SingleEmailMessage Class

Contains methods for sending single email messages.

Namespace

Messaging

Usage

Important: Sending an email by using Apex requires domain-level and user-level email verification. System-generated emails
[also require verification of the From email address. Email delivery fails if any of these verifications is incomplete. See Requirements](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)
[to Send Email from Salesforce.](https://help.salesforce.com/s/articleView?id=xcloud.security_email_verification_requirements.htm&language=en_US&type=5)

SingleEmailMessage extends Email and inherits all of its methods. All base email ( `Email` class) methods are also available to the
### SingleEmailMessage objects. Emails sent via SingleEmailMessage count against the sending organization's daily single email

limit.

Email properties are readable and writable. Each property has corresponding setter and getter methods. For example, the
`toAddresses()` property is equivalent to the `setToAddresses()` and `getToAddresses()` methods. Only the setter
methods are documented. However, the `getTemplateName()` method doesn’t have an equivalent setter method; use
`setTemplateId()` to specify a template name.

IN THIS SECTION:

SingleEmailMessage Constructors

SingleEmailMessage Methods

SEE ALSO:

Email Class (Base Email Methods)


Apex Reference Guide SingleEmailMessage Class

#### SingleEmailMessage Constructors The following are constructors for SingleEmailMessage .

IN THIS SECTION:

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

##### SingleEmailMessage()

Creates a new instance of the `Messaging.SingleEmailMessage` class.

Signature

```
   public SingleEmailMessage()

#### SingleEmailMessage Methods The following are methods for SingleEmailMessage . All are instance methods. All base email ( Email class) methods are also available to the SingleEmailMessage objects. These methods are described in Email Class (Base Email Methods).

```

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
[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

setFileAttachments(fileNames)
Optional. A list containing the file names of the binary and text files you want to attach to the email.


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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

Signature

```
   public Boolean getOneClickPost()

```

Parameters

Type: Boolean

Return Value

Type: Boolean

Usage

##### Invoke the setOneClickPost method before using getOneClickPost . The value of getOneClickPost will be false if

the `setOneClickPost` method is set to true only after invoking the `setUnsubscribeUrls` method.

##### getTemplateName()

The name of the template used to create the email.

Signature

```
   public STRING getTemplateName()

```

Return Value

Type: String


Apex Reference Guide SingleEmailMessage Class

Usage

There is no equivalent setter method for `getTemplateName()` . If the email didn’t use a template, `getTemplateName()`
returns nothing. If you use `setTemplateId()`, and then call `getTemplateName()`, the template name associated to the
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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

##### setEntityAttachments(ids)

[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

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


Apex Reference Guide SingleEmailMessage Class

Parameters

```
   unsubscribeComment
```

Type: String

Return Value

Type: void

Usage

Invoke the `setUnsubscribeUrls` method before using `setUnsubscribeComment` .

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

```


Apex Reference Guide SingleEmailMessage Class

##### **`setUnsubscribeUrls(UnsubscribeUrls)`**

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

```


Apex Reference Guide SingleEmailMessage Class

```
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


## Apex Reference Guide Metadata Namespace Metadata Namespace The Metadata namespace provides classes and methods for working with custom metadata in Salesforce

Salesforce uses metadata types and components to represent org configuration and customization. Metadata is used for org settings
## that admins control or configuration information applied by installed apps and packages. Use the classes in the Metadata namespace

to access metadata from within Apex code.

Metadata access in Apex is available for Apex classes using API version 40.0 and later.

[For more information, see Metadata.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_metadata.htm)

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


Apex Reference Guide Metadata Namespace

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


Apex Reference Guide Metadata Namespace

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


### Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

UiBehavior Enum
Describes the behavior for a layout item on a layout page.

### AnalyticsCloudComponentLayoutItem Class

Represents the settings for a Wave Analytics dashboard on a standard or custom page.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“AnalyticsCloudComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### AnalyticsCloudComponentLayoutItem Properties

AnalyticsCloudComponentLayoutItem Methods

#### AnalyticsCloudComponentLayoutItem Properties

### The following are properties for AnalyticsCloudComponentLayoutItem .

IN THIS SECTION:

assetType
Specifies the type of Wave Analytics asset.

devName
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


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

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


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

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


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

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


### Apex Reference Guide ConsoleComponent Class ConsoleComponent Class

Represents a custom console component on a section of a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “ConsoleComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### ConsoleComponent Properties

ConsoleComponent Methods

#### ConsoleComponent Properties

### The following are properties for ConsoleComponent .

IN THIS SECTION:

##### height

The height of the custom console component in pixels.

##### location

The location of the custom console component on the page layout. Valid values are right, left, top, and bottom.

visualforcePage
The unique name of the custom console component.

width
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


Apex Reference Guide ConsoleComponent Class

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


### Apex Reference Guide Container Class

Return Value

Type: Object

### Container Class

Represents a location and style in which to display more than one custom console component in the sidebars of the console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “Container” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### Container Properties

Container Methods

#### Container Properties

### The following are properties for Container .

IN THIS SECTION:

##### height

The height of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

isContainerAutoSizeEnabled
If set to true, stacked console components in the sidebars autosize vertically.

region
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


Apex Reference Guide Container Class

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


Apex Reference Guide Container Class

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


### Apex Reference Guide CustomConsoleComponents Class CustomConsoleComponents Class

Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “CustomConsoleComponents”
in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### CustomConsoleComponents Properties

CustomConsoleComponents Methods

#### CustomConsoleComponents Properties

### The following are properties for CustomConsoleComponents .

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


### Apex Reference Guide CustomMetadata Class

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

Use `Metadata.CustomMetadata` [to represent records of custom metadata types in Apex. For more information, see Custom](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm)
[Metadata Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm) _Metadata API Developer Guide_ .

Example

```
   // Set up custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

```


Apex Reference Guide CustomMetadata Class

```
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

#### CustomMetadata Properties The following are properties for CustomMetadata .

IN THIS SECTION:

##### description

The description of the custom metadata.

##### label

The label of the custom metadata record.

protected_x
Property that describes whether the custom metadata record is a protected component.

values
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


Apex Reference Guide CustomMetadata Class

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


### Apex Reference Guide CustomMetadataValue Class CustomMetadataValue Class

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

#### CustomMetadataValue Properties

### The following are properties for CustomMetadataValue .

IN THIS SECTION:

field
The field name for the custom metadata value.

value
The field value for the custom metadata value.


Apex Reference Guide CustomMetadataValue Class

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

[For more information, see Primitive Data Types.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### CustomMetadataValue Methods The following are methods for CustomMetadataValue .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .


### Apex Reference Guide DeployCallback Interface

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

Salesforce calls your `DeployCallback.handleResult()` method asynchronously once the queued deployment completes.
Because the callback is called as asynchronous Apex after deployment, there may be a brief period where the deploy has completed,
but your callback has not been called yet.

IN THIS SECTION:

#### DeployCallback Methods

DeployCallback Example Implementation

#### DeployCallback Methods

### The following are methods for DeployCallback .

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


### Apex Reference Guide DeployCallbackContext Class

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


Apex Reference Guide DeployCallbackContext Class

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

#### DeployCallbackContext Methods DeployCallbackContext Methods The following are methods for DeployCallbackContext .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployCallbackContext` .

##### getCallbackJobId()

Gets the asynchronous Apex job ID for the callback job.

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


### Apex Reference Guide DeployContainer Class DeployContainer Class

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

IN THIS SECTION:

#### DeployContainer Methods DeployContainer Methods

### The following are methods for DeployContainer .

IN THIS SECTION:

##### addMetadata(md)

Add a custom metadata component to the container.

clone()
Makes a duplicate copy of the `Metadata.DeployContainer` .

getMetadata()
Retrieves a list of custom metadata components from the container.

removeMetadata(md)
Removes a metadata component from the container.

removeMetadataByFullName(fullName)
Removes a metadata component from the container using the component’s full name.

##### addMetadata(md)

Add a custom metadata component to the container.


Apex Reference Guide DeployContainer Class

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


### Apex Reference Guide DeployDetails Class

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

DeployDetails Properties

DeployDetails Methods


Apex Reference Guide DeployDetails Class

#### DeployDetails Properties The following are properties for DeployDetails .

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


### Apex Reference Guide DeployMessage Class

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

for a completed deployment via the `DeployDetails` and `DeployResults` instances sent in the
`DeployCallback.handleResult()` callback.

IN THIS SECTION:

#### DeployMessage Properties

DeployMessage Methods

#### DeployMessage Properties

### The following are properties for DeployMessage .

IN THIS SECTION:

changed
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


Apex Reference Guide DeployMessage Class

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


Apex Reference Guide DeployMessage Class

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


Apex Reference Guide DeployMessage Class

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


Apex Reference Guide DeployMessage Class

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


### Apex Reference Guide DeployProblemType Enum

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

### DeployResult Class

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

```


Apex Reference Guide DeployResult Class

```
      }

   }

```

IN THIS SECTION:

#### DeployResult Properties

DeployResult Methods

#### DeployResult Properties The following are properties for DeployResult .

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


Apex Reference Guide DeployResult Class

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


Apex Reference Guide DeployResult Class

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


Apex Reference Guide DeployResult Class

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

Signature

```
   public Boolean done {get; set;}

```

Property Value

Type: Boolean

##### errorMessage

Message corresponding to the values in the `errorStatusCode` property, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String


Apex Reference Guide DeployResult Class

##### errorStatusCode

If an error occurs during deployment, a status code is returned. The message corresponding to the status code is returned in the
`errorMessagefield` property.

Signature

```
   public String errorStatusCode {get; set;}

```

Property Value

Type: String

[For a description of each status code value, see Core Data Types Used in API Calls in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_concepts_core_data_objects.htm) _SOAP API Developer Guide_ .

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


Apex Reference Guide DeployResult Class

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

##### numberComponentsDeployed The number of components deployed in the deployment process. Use this value with the numberComponentsTotal property

to get an estimate of the deployment’s progress.

Signature

```
   public Integer numberComponentsDeployed {get; set;}

```

Property Value

Type: Integer

##### numberComponentsTotal The total number of components in the deployment. Use this value with the numberComponentsDeployed property to get an

estimate of the deployment’s progress.

Signature

```
   public Integer numberComponentsTotal {get; set;}

```

Property Value

Type: Integer


Apex Reference Guide DeployResult Class

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


### Apex Reference Guide DeployStatus Enum

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


### Apex Reference Guide FeedItemTypeEnum Enum

**Value** **Description**

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


### Apex Reference Guide FeedLayout Class

**Value** **Description**

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

### FeedLayout Class

Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case, Contact,
Lead, Opportunity, custom, and external objects. They include a feed view and a detail view.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

FeedLayout Properties

FeedLayout Methods


Apex Reference Guide FeedLayout Class

#### FeedLayout Properties The following are properties for FeedLayout .

IN THIS SECTION:

##### autocollapsePublisher

Specifies whether the publisher is collapsed when the page loads (true) or not (false).

##### compactFeed

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


Apex Reference Guide FeedLayout Class

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


Apex Reference Guide FeedLayout Class

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


### Apex Reference Guide FeedLayoutComponent Class

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

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutComponent” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutComponent Properties

FeedLayoutComponent Methods

#### FeedLayoutComponent Properties

### The following are properties for FeedLayoutComponent . See FeedLayoutComponent in the Metadata API Developer Guide

IN THIS SECTION:

componentType
Represents a component in the feed view of a feed-based page layout. The type of component is required.


Apex Reference Guide FeedLayoutComponent Class

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

##### page_x

The name of the Visualforce page used as a custom component.

##### componentType

Represents a component in the feed view of a feed-based page layout. The type of component is required.

Signature

```
   public Metadata.FeedLayoutComponentType componentType {get; set;}

```

Property Value

Type: Metadata.FeedLayoutComponentType on page 3148

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

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

clone()
Makes a duplicate copy of the `Metadata.FeedLayoutComponent` .


### Apex Reference Guide FeedLayoutComponentType Enum

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


Apex Reference Guide FeedLayoutFilter Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutFilter” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutFilter Properties

FeedLayoutFilter Methods

#### FeedLayoutFilter Properties The following are properties for FeedLayoutFilter .

IN THIS SECTION:

##### feedFilterName

The name of a `CustomFeedFilter` component. Names are prefixed with the name of the parent object. For example,
`Case.MyCustomFeedFilter` .

##### feedFilterType

The type of filter.

feedItemType
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


### Apex Reference Guide FeedLayoutFilterPosition Enum

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

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutFilter` .

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


### Apex Reference Guide FeedLayoutFilterType Enum

**Value** **Description**

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

Namespace

Metadata

Usage

[Use this class to access layout metadata components. For more information, see Layout in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_layouts.htm) _Metadata API Developer Guide_ .

IN THIS SECTION:

#### Layout Properties

Layout Methods

#### Layout Properties

### The following are properties for Layout .

IN THIS SECTION:

customButtons
The custom buttons for this layout.

customConsoleComponents
Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


Apex Reference Guide Layout Class

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


### Apex Reference Guide LayoutColumn Class

Return Value

Type: Object

### LayoutColumn Class

Represents the items in a column within a layout section.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutColumn” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutColumn Properties

LayoutColumn Methods

#### LayoutColumn Properties

### The following are properties for LayoutColumn .

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


### Apex Reference Guide LayoutHeader Enum

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


Apex Reference Guide LayoutItem Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutItem Properties

LayoutItem Methods

#### LayoutItem Properties The following are properties for LayoutItem .

IN THIS SECTION:

analyticsCloudComponent
A Wave Analytics dashboard component on a page.

behavior
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


Apex Reference Guide LayoutItem Class

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


Apex Reference Guide LayoutItem Class

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


Apex Reference Guide LayoutItem Class

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


### Apex Reference Guide LayoutSection Class

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

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutSection” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .


Apex Reference Guide LayoutSection Class

IN THIS SECTION:

#### LayoutSection Properties

LayoutSection Methods

#### LayoutSection Properties The following are properties for LayoutSection .

IN THIS SECTION:

##### customLabel

Indicates if this section's label is custom or standard (built-in).

##### detailHeading

Controls whether this heading appears on the detail page.

editHeading
Controls whether this heading appears on the edit page.

label
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


Apex Reference Guide LayoutSection Class

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


### Apex Reference Guide LayoutSectionStyle Enum

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

Signature

```
   public Object clone()

```

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
from `Metadata.Metadata`, such as `Metadata.CustomMetadata` [. For more information, see Metadata in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) _Metadata API_
_Developer Guide_ .


Apex Reference Guide Metadata Class

IN THIS SECTION:

#### Metadata Properties Metadata Methods Metadata Properties The following are properties for Metadata .

IN THIS SECTION:

##### fullName

The full name of the custom metadata, which can include the namespace, type, and component name.

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
see reference documentation on the metadata types in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_intro.htm)_ .

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


### Apex Reference Guide MetadataType Enum

Return Value

Type: Object

### MetadataType Enum

Represents the custom metadata components available in Apex.

Enum Values

The following are the values of the `Metadata.MetadataType` enum.

**Value** **Description**

`CustomMetadata` Records of custom metadata types

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


### Apex Reference Guide MiniLayout Class

Signature

```
   public Object clone()

```

Return Value

Type: Object

### MiniLayout Class

Represents a mini view of a record in the Console tab, hover details, and event overlays.

Namespace

Metadata

Usage

