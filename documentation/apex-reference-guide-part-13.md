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


Apex Reference Guide KnowledgeSuggestionFilter Class

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

A publish status. Valid values are:

**•** `Draft` –Articles aren’t published in Salesforce Knowledge.

**•** `Online` –Articles are published in Salesforce Knowledge.

**•** `Archived` –Articles aren’t published and are available in Archived Articles view.

##### setValidationStatus(validationStatus)

Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.


### Apex Reference Guide QuestionSuggestionFilter Class

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

addUserId(userId)
Adds a filter to display questions belonging to the single specified user whose ID is passed in as an argument. This filter is optional.

setGroupIds(groupIds)
Sets a new list of groups to replace the current list of groups where the group IDs are passed in as an argument. This filter is optional.

setNetworkIds(networkIds)
Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.


Apex Reference Guide QuestionSuggestionFilter Class

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

Return Value

Type: void

Usage

To add more than one network, call the method multiple times.


Apex Reference Guide QuestionSuggestionFilter Class

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

##### setNetworkIds(networkIds)

Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.

Signature

```
   public void setNetworkIds(List<String> networkIds)

```


### Apex Reference Guide SearchResult Class

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

Return Value

Type: void

### SearchResult Class

A wrapper object that contains an sObject and search metadata.


Apex Reference Guide SearchResult Class

Namespace

#### Search SearchResult Methods The following are methods for SearchResult .

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### getSnippet(fieldName)

Returns a snippet from a Case, Feed, or Knowledge Article SearchResult object based on the specified field name.

Signature

```
   public String getSnippet(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

The field name to use for creating the snippet.

Valid values: `Case.Casenumber`, `FeedPost.Title`, `KnowledgeArticleVersion.Title`


### Apex Reference Guide SearchResults Class

Return Value

Type: String

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SearchResults Class

Wraps the results returned by the `Search.find(String)` method.

Namespace

### Search

#### SearchResults Methods

### The following are methods for SearchResults .

IN THIS SECTION:

##### get(sObjectType)

Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.

##### get(sObjectType)

Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.

Signature

```
   public List<Search.SearchResult> get(String sObjectType)

```


### Apex Reference Guide SuggestionOption Class

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SuggestionOption Class

Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

Namespace

Search

#### SuggestionOption Methods

### The following are methods for SuggestionOption .

IN THIS SECTION:

##### setFilter(knowledgeSuggestionFilter)

Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

setLimit(limit)
The maximum number of record or article suggestions to retrieve.

##### setFilter(knowledgeSuggestionFilter)

Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .


Apex Reference Guide SuggestionOption Class

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

Parameters

```
   limit
```

Type: Integer

The maximum number of record or article suggestions to retrieve.

Return Value

Type: void


### Apex Reference Guide SuggestionResult Class

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

### SuggestionResults Class

Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

Namespace

Search


## Apex Reference Guide setup_flow_performance Namespace

#### SuggestionResults Methods The following are methods for SuggestionResults .

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

Usage

If a limit isn’t specified, 5 records are returned in calls to `System.Search.suggest(String, String,`
##### Search.SuggestionOption) . If there are more suggested records than the limit specified, a call to hasMoreResults()

returns `true` .

## setup_flow_performance Namespace

The class and methods in this namespace are for internal use only.

## The following are the classes in the setup_flow_performance namespace.


### Apex Reference Guide FlowPerformanceSetupDetails Class

IN THIS SECTION:

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

Namespace

setup_flow_performance

## Sfc Namespace

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


### Apex Reference Guide ContentDownloadHandler Class

**Value** **Description**

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

Sfc on page 3555

IN THIS SECTION:

#### ContentDownloadHandler Properties ContentDownloadHandler Properties

### The following are properties for ContentDownloadHandler .

IN THIS SECTION:

##### downloadErrorMessage

A customized error message explaining why the download isn’t allowed.

isDownloadAllowed
Indicates whether or not download is allowed.

redirectUrl
The URL the user is redirected to when the download action isn't available, for applying Information Rights Management (IRM)
control, virus scanning, or other behavior.

##### downloadErrorMessage

A customized error message explaining why the download isn’t allowed.

Signature

```
   public String downloadErrorMessage {get; set;}

```


### Apex Reference Guide ContentDownloadHandlerFactory Interface

Property Value

Type: String

##### This message is used if a redirectUrl is not provided. If the download is not allowed, Salesforce will throw a

`ContentCustomizedDownloadException` exception that contains the `downloadErrorMessage` .

##### isDownloadAllowed

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

Namespace

Sfc on page 3555

Usage

ContentDownloadHandler getContentDownloadHandler(List<ID> ids, ContentDownloadContext context);

IN THIS SECTION:

ContentDownloadHandlerFactory Methods

ContentDownloadHandlerFactory Example Implementation


Apex Reference Guide ContentDownloadHandlerFactory Interface

#### ContentDownloadHandlerFactory Methods The following are methods for ContentDownloadHandlerFactory .

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

Type: Sfc.ContentDownloadContext on page 3555

Return Value

Type: Sfc.ContentDownloadHandler on page 3556

#### ContentDownloadHandlerFactory Example Implementation

This example creates a class that implements the `Sfc.ContentDownloadHandlerFactory` interface and returns a download
handler that blocks downloading content to mobile devices.

```
   // Allow customization of the content Download experience

   public class ContentDownloadHandlerFactoryImpl implements Sfc.ContentDownloadHandlerFactory

    {

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

```


## Apex Reference Guide Sfdc_Checkout Namespace

```
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

#### AsyncCartProcessor Methods

AsyncCartProcessor Example Implementation

#### AsyncCartProcessor Methods

### The following are methods for AsyncCartProcessor .

IN THIS SECTION:

startCartProcessAsync(integrationInfo, cartId)
The startCartProcessAsync method is called asynchronously by the integration framework. Calling this method begins cart processing
for Commerce checkout.


### Apex Reference Guide B2BCheckoutController Class

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

### B2BCheckoutController Class

Communicate with simple checkout Apex methods to work with data related to B2B Commerce checkout.

Namespace

sfdc_checkout


### Apex Reference Guide IntegrationInfo Class

Usage

You must specify the `sfdc_checkout` namespace when creating an instance of this class.

IN THIS SECTION:

#### B2BCheckoutController Methods B2BCheckoutController Methods The following are methods for B2BCheckoutController .

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

### IntegrationInfo Class

Provides the values that B2B Commerce Checkout uses to map requests to responses, necessary metadata, and context.

Namespace

sfdc_checkout on page 3559


Apex Reference Guide IntegrationInfo Class

Usage

This class provides information about a B2B Commerce integration. An instance of this class is passed as a parameter into the integration
interface.

IN THIS SECTION:

#### IntegrationInfo Properties IntegrationInfo Properties The following are properties for IntegrationInfo .

IN THIS SECTION:

##### integrationId

The unique ID of a B2B Commerce integration.

##### jobId

The ID of the job, specific to the Salesforce Background Operation framework.

##### siteLanguage

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

Property Value

Type: String

##### siteLanguage

Site language to be used by third party services.


### Apex Reference Guide IntegrationStatus Class

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

Property Value

Type: sfdc_checkout.IntegrationStatus.Status on page 3563

### IntegrationStatus.Status Enum

The IntegrationStatus.Status enum describes the status of the current integration.


## Apex Reference Guide Sfdc_Enablement Namespace

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

Usage

Pass this class as input to the sfdc_enablement.LearningEvaluationResult class.

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3568.


Apex Reference Guide LearningEvaluation Class

IN THIS SECTION:

#### LearningEvaluation Methods LearningEvaluation Methods The following are methods for LearningEvaluation .

IN THIS SECTION:

##### getDetails()

Retrieves the details associated with the learning evaluation instance.

##### getLearningItemId()

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

##### setDetails(details)

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

Type: Map on page 4013<String,Object on page 4080>

##### **`getLearningItemId()`**

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

Signature

```
   public String getLearningItemId()

```

Return Value

Type: String

##### **`setDetails(details)`**

Sets or updates the details of the learning item record for this learning evaluation instance.


### Apex Reference Guide LearningEvaluationResult Class

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

Usage

To calculate the user’s progress through an exercise as a percentage and return the progress status, use the
`sfdc_enablement.LearningEvaluationResult` class inside the sfdc_enablement.LearningItemEvaluationHandler. In
your custom code, set the percentages to correspond to these sfdc_enablement.LearningItemProgressStatus on page 3570 enum values.

**•** `NotStarted` is equal to 0.00

**•** `InProgress` is from 0.01 through 99.99

**•** `Completed` is equal to 100.00


Apex Reference Guide LearningEvaluationResult Class

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3568.

IN THIS SECTION:

#### LearningEvaluationResult Methods LearningEvaluationResult Methods The following are methods for LearningEvaluationResult .

IN THIS SECTION:

##### getLearningItemProgress()

Returns the progress percentage of the learning item.

##### getLearningItemProgressStatus()

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

##### **`getLearningItemProgressStatus()`**

Retrieves the progress status of the learning item.

Signature

```
   public sfdc_enablement.LearningItemProgressStatus getLearningItemProgressStatus()

```

Return Value

Type: sfdc_enablement.LearningItemProgressStatus on page 3570


### Apex Reference Guide LearningItemEvaluationHandler Class

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

Type: Sfdc_enablement.LearningItemProgressStatus on page 3570

Return Value

Type: void

### LearningItemEvaluationHandler Class

Contains methods to customize the evaluation process of a learning item.

Namespace

sfdc_enablement

Usage

[Extend this class and implement your custom progress evaluation method. Then link this class to a LearningItemType metadata record](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
by passing the Apex class name to the `ApexEvaluationHandler` field.


Apex Reference Guide LearningItemEvaluationHandler Class

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

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.Completed);

        } else if (percentage == 0.0d) {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.NotStarted);

        } else {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.InProgress);

```


### Apex Reference Guide LearningItemProgressStatus Enum

```
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

Type: Sfdc_enablement.LearningEvaluation on page 3564

The details of the learning item record to be evaluated.

Return Value

Type: Sfdc_enablement.LearningEvaluationResult on page 3566

The result of the evaluation, including progress and status details.

### LearningItemProgressStatus Enum

Represents the status of a user’s progress for a learning item in an Enablement program.

Usage

To set the progress status in the sfdc_enablement.LearningEvaluationResult on page 3566 class, use this enum.


### Apex Reference Guide LearningItemSerializeDeserializer Class

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
to the `ApexSerializerDeserializer` [field of the LearningItemType metadata record. If you don’t add the class name to the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
LearningItemType metadata record, the `customContent` property for the custom exercise is empty in the destination org and no
[corresponding LearningItem record is created for the exercise’s EnblProgramTaskDefinition record.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_enblprogramtaskdefinition.htm)

The serialize on page 3573 method serializes the custom content of the learning item from the source org. This method is called when
you retrieve custom content from the source org.

The deserialize on page 3573 method is called during the deployment of a program. This method takes the serialized custom content,
recreates the custom object record in the target org, and returns a new learning item record ID.

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

```


Apex Reference Guide LearningItemSerializeDeserializer Class

```
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

        insert screenFlowRecord;

        // Return the new screen flow record ID for the new learning item

        // in the destination org.

        return screenFlowRecord.Id;

      }

   }

```

IN THIS SECTION:

LearningItemSerializeDeserializer Methods


Apex Reference Guide LearningItemSerializeDeserializer Class

#### LearningItemSerializeDeserializer Methods The following are methods for LearningItemSerializeDeserializer .

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

The serialized information of custom content associated with a learning item The serialize(learningItemId) on page 3573 method
returns this information as a string that is less than or equal to 250 characters.

Return Value

Type: String

The ID of the learning item created for the target org.

##### **`serialize(learningItemId)`**

Serializes the custom content associated with the specified learning item. The serialized string represents the metadata of the custom
content and is used to recreate the custom content in the target Salesforce org during deployment.

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


## Apex Reference Guide sfdc_surveys Namespace

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

IN THIS SECTION:

#### SurveyInvitationLinkShortener Methods

SurveyInvitationLinkShortener Example Implementation

#### SurveyInvitationLinkShortener Methods

### The following are methods for SurveyInvitationLinkShortener .


Apex Reference Guide SurveyInvitationLinkShortener Interface

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

[This sample code uses Named Credentials for authentication. For more information on Named Credentials, see Named Credentials as](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)
[Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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

       'group_guid' => '{!$Credential.UserName}',

       'long_url' => invitationURL

       }));

       Http http = new Http();

       HttpResponse res = http.send(request);

       Object result = JSON.deserializeUntyped(res.getBody());

       if (result instanceof Map<String, Object>) {

         Map<String, Object> resultMap = (Map<String, Object>) result;

```


### Apex Reference Guide Example Implementation to Associate SurveySubjects with

SurveyInvitation and SurveyResponses

```
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

     private static void createSurveySubject(String invitationId, String associatedRecordId)

    {

        SurveySubject subj = new SurveySubject();

        subj.Name = 'Sur_Subject_for_invitation';

       subj.ParentId = invitationId; // similary you can use survey response id to associate

    survey subject to a response record.

        subj.SubjectId = associatedRecordId;

        // Insert the SurveySubject Record

        insert subj;

```


## Apex Reference Guide Site Namespace

```
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

IN THIS SECTION:

UrlRewriter Interface
Enables rewriting Sites URLs.

Site Exceptions
## The Site namespace contains an exception class.


### Apex Reference Guide UrlRewriter Interface UrlRewriter Interface

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

Parameters

```
   salesforceUrls
```

Type: System.PageReference[]

Return Value

Type: System.PageReference[]


### Apex Reference Guide Site Exceptions

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

## Slack Namespace

Use the `String getMessage()` to get the error message
and write it to debug log.

Use `List<String> getDisplayMessages()` to get
a list of errors displayed to the end user.

This exception can’t be subclassed or thrown in code.

## The Slack Namespace provides tools designed to accelerate and ease the process of developing Slack apps on the Salesforce platform. The following are the classes in the Slack namespace.

[App Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_access.html)

[Action Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_dispatchers.html)

[AppClient](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client.html)


Apex Reference Guide Slack Namespace

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

[Star Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_stars.html)

[Team Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_teams.html)

[TestHarness Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_testharness.html)

[Topic Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_topics.html)

[User Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_users.html)

[UserClient Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_user.html)

[Usergroup Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_usergroups.html)


## Apex Reference Guide Support Namespace

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

#### EmailTemplateSelector Methods

EmailTemplateSelector Example Implementation

#### EmailTemplateSelector Methods

### The following are methods for EmailTemplateSelector .

IN THIS SECTION:

getDefaultTemplateId(caseId)
Returns the ID of the email template to preload for the case currently being viewed in the case feed using the specified case ID.


Apex Reference Guide EmailTemplateSelector Interface

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

      }

   }

```

The following example tests the above code:

```
   @isTest

   private class MyCaseTemplateChooserTest {

      static testMethod void testChooseTemplate() {

```


### Apex Reference Guide MilestoneTriggerTimeCalculator Interface

```
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

Next, your class must provide an implementation for the following method:

```
   global Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId)

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

MilestoneTriggerTimeCalculator Methods

MilestoneTriggerTimeCalculator Example Implementation


Apex Reference Guide MilestoneTriggerTimeCalculator Interface

#### MilestoneTriggerTimeCalculator Methods The following are instance methods for MilestoneTriggerTimeCalculator .

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

```


## Apex Reference Guide System Namespace

```
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

IN THIS SECTION:

AccessLevel Class
Defines the different modes, such as system or user mode, that Apex database operations execute in.

AccessType Enum
Specifies the access check type for the fields of an sObject.

Address Class
Contains methods for accessing the component fields of address compound fields.


Apex Reference Guide System Namespace

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

Comparable Interface
Adds sorting support for Lists that contain non-primitive types, that is, Lists of user-defined types. Your implementation must explicitly
handle null inputs in the `compareTo()` method to avoid a null pointer exception.

Comparator Interface
Implement different sort orders with the Comparator interface’s `compare()` method, and pass the Comparator as a parameter
to `List.sort()` . Your implementation must explicitly handle null inputs in the `compare()` method to avoid a null pointer
exception.


Apex Reference Guide System Namespace

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

EmailMessages Class
Use the methods in the `EmailMessages` class to interact with emails and email threading.

EncodingUtil Class
Use the methods in the `EncodingUtil` class to encode and decode URL strings, and convert strings to hexadecimal format.

Enum Methods
An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Apex provides
built-in enums, such as `LoggingLevel`, and you can define your own enum.


Apex Reference Guide System Namespace

EventBus Class
Contains methods for publishing platform events.

Exception Class and Built-In Exceptions
An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create
custom exceptions. All exceptions have common methods.

ExternalServiceTest Class
Provides methods to test an external service's asynchronous callouts, enables sending a mock request, asserts the expected request
payload, then triggers the mocked external service’s asynchronous callback response.

FeatureManagement Class
Use the methods in the `System.FeatureManagement` class to check and modify the values of feature parameters, and to
show or hide custom objects and custom permissions in your subscribers’ orgs.

Finalizer Interface
Use this interface to attach actions that are executed at the end of asynchronous Queueable job executions. A specific use case is
to design recovery actions when a Queueable job fails.

FinalizerContext Interface
Represents the parameter type of the `execute` method in a class that implements the Finalizer interface. This interface is
implemented internally by Apex. The System.FinalizerContext interface contains four methods: `getAsyncApexJobId`,
`getRequestId`, `getResult`, and `getException` . An instance of `System.FinalizerContext` is injected by the
Apex runtime engine as an argument to the `Finalizer.execute` method.

FlexQueue Class
Contains methods that reorder batch jobs in the Apex flex queue.

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

IntegrationTest Class (Developer Preview)
Contains the `commitTestOnly()` method that can be called from an `@IntegrationMethod` to commit data mid-transaction
so that it’s visible to service threads such as Agentforce and Data 360.

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


Apex Reference Guide System Namespace

Object Class
Contains methods that are implemented by all Apex types.

OrgLimit Class
Contains methods that provide the name, maximum value, and current value of an org limit.

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

ParentJobResult Enum
Specifies the success or exception status of the parent Queueable job to which a Transaction Finalizer is attached.

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


Apex Reference Guide System Namespace

RestRequest Class
Use the `System.RestRequest` class to access and pass request data in a RESTful Apex method.

RestResponse Class
Represents an object used to pass data from an Apex RESTful Web service method to an HTTP response.

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
Contains a method to create a mock test class for handling SOQL query responses for Data 360 data model objects (DMOs).

StaticResourceCalloutMock Class
Utility class used to specify a fake response for testing HTTP callouts.

String Class
Contains methods for the String primitive data type.

StubProvider Interface

`StubProvider` is a callback interface that you can use as part of the Apex stub API to implement a mocking framework. Use this
interface with the `Test.createStub()` method to create stubbed Apex objects for testing.


Apex Reference Guide System Namespace

System Class
Contains methods for system operations, such as writing debug messages and scheduling jobs.

Test Class
Contains methods related to Apex tests.

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

XmlStreamReader Class
The `XmlStreamReader` class provides methods for forward, read-only access to XML data. You can pull data from XML or skip
unwanted events. You can parse nested XML content that’s up to 50 nodes deep.

XmlStreamWriter Class
The `XmlStreamWriter` class provides methods for writing XML data.


### Apex Reference Guide AccessLevel Class AccessLevel Class

Defines the different modes, such as system or user mode, that Apex database operations execute in.

Namespace

System

Usage

By default, Apex code runs in user mode, which means that the current user’s object permissions, field-level security, and sharing rules
are enforced. You can set a specific DML method to system mode, where the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Many of the DML methods of the `System.Database` and `System.Search` classes include an `accessLevel` parameter to
specify the execution mode.

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

#### AccessLevel Methods

### The following are methods for AccessLevel .

IN THIS SECTION:

withPermissionSetId(permissionSetId)(Developer Preview)
Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.


Apex Reference Guide AccessLevel Class

##### **`withPermissionSetId(permissionSetId)(Developer Preview)`**

Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.

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

```


Apex Reference Guide AccessLevel Class

```
               Assert.isTrue(ex.getMessage().contains('Account'));

             }

             //Get ID of previously created permission set named 'AllowCreateToAccount'

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
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

USER_MODE
Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.

##### **`SYSTEM_MODE`**

Execution mode in which the the object and field-level permissions of the current user are ignored, and the record sharing rules are
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Signature

```
   public System.AccessLevel SYSTEM_MODE {get;}

```

Property Value

Type: System.AccessLevel


### Apex Reference Guide AccessType Enum

##### **`USER_MODE`**

Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.

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


Apex Reference Guide Address Class

You can’t use dot notation to access compound fields’ subfields directly on the parent field. Instead, assign the parent field to a variable
#### of type Address, and then access its components. For example, to access the City field in myAccount.BillingAddress,

do the following:

```
   Address addr = myAccount.BillingAddress;

   String acctCity = addr.City;

```

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


Apex Reference Guide Address Class

getGeocodeAccuracy()
When using geolocation data for a given address, this method gives you relative location information based on latitude and longitude
values. For example, you can find out if the latitude and longitude values point to the middle of the street, instead of the exact
address.

getLatitude()
Returns the latitude field of this address.

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


Apex Reference Guide Address Class

Signature

```
   public String getCountryCode()

```

Return Value

Type: String

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


Apex Reference Guide Address Class

Return Value

Type: Double

##### getPostalCode()

Returns the postal code of this address.

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


### Apex Reference Guide Answers Class Answers Class

Represents zone answers.

Namespace

System

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

#### Answers Methods

### The following are methods for Answers . All methods are static.

```

IN THIS SECTION:

findSimilar(yourQuestion)
Returns a list of similar questions based on the title of the specified question.


### Apex Reference Guide ApexPages Class

##### setBestReply(questionId, replyId)

Sets the specified reply for the specified question as the best reply. Because a question can have multiple replies, setting the best
reply helps users quickly identify the reply that contains the most helpful information.

##### findSimilar(yourQuestion)

Returns a list of similar questions based on the title of the specified question.

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

##### Each findSimilar call counts against the SOSL statements governor limit allowed for the process. setBestReply(questionId, replyId)

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


Apex Reference Guide ApexPages Class

Namespace

System

Usage

#### In addition, ApexPages is used as a namespace for the PageReference Class and the Message Class. ApexPages Methods The following are methods for ApexPages . All are instance methods.

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


Apex Reference Guide ApexPages Class

Signature

```
   public Void addMessages(Exception exceptionThrown)

```

Parameters

```
   exceptionThrown
```

Type: Exception

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


### Apex Reference Guide Approval Class

##### hasMessages()

Returns `true` if there are messages associated with the current context, `false` otherwise.

Signature

```
   public Boolean hasMessages()

```

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


Apex Reference Guide Approval Class

#### Approval Methods The following are methods for Approval . All methods are static.

IN THIS SECTION:

isLocked(id)
Returns `true` if the record with the ID `id` is locked, or `false` if it’s not.

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


Apex Reference Guide Approval Class

unlock(recordIds)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordToUnlock)
Unlocks an object, and returns the unlock results.

unlock(recordsToUnlock)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordId, allOrNothing)
Unlocks an object, with the option for partial success, and returns the unlock result.

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


Apex Reference Guide Approval Class

Return Value

Type: Map<Id,Boolean>

##### isLocked(sobject)

Returns `true` if the `sobject` record is locked, or `false` if it’s not.

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


Apex Reference Guide Approval Class

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

Return Value

Type: Approval.LockResult

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


Apex Reference Guide Approval Class

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


Apex Reference Guide Approval Class

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


Apex Reference Guide Approval Class

Return Value

Type: List<Approval.LockResult>

##### process(approvalRequest)

Submits a new approval request and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult process(Approval.ProcessRequest approvalRequest)

```

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


Apex Reference Guide Approval Class

```
   allOrNone
```

Type: Boolean

The optional _`allOrNone`_ parameter specifies whether the operation allows for partial success. If you specify `false` for this
parameter and an approval fails, the remainder of the approval processes can still succeed.

Return Value

Approval.ProcessResult

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


Apex Reference Guide Approval Class

##### unlock(recordId)

Unlocks an object, and returns the unlock results.

Signature

```
   public static Approval.UnlockResult unlock(Id recordId)

```

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


Apex Reference Guide Approval Class

Return Value

Type: Approval.UnlockResult

##### unlock(recordsToUnlock)

Unlocks a set of objects, and returns the unlock results, including failures.

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


Apex Reference Guide Approval Class

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


### Apex Reference Guide Assert Class

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


Apex Reference Guide Assert Class

isInstanceOfType(instance, expectedType, msg)
Asserts that the instance is of the specified type.

isInstanceOfType(instance, expectedType)
Asserts that the instance is of the specified type.

isNotInstanceOfType(instance, notExpectedType, msg)
Asserts that the instance isn’t of the specified type.

isNotInstanceOfType(instance, notExpectedType)
Asserts that the instance isn’t of the specified type.

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


Apex Reference Guide Assert Class

Usage

If the first two arguments aren't the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

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


Apex Reference Guide Assert Class

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


Apex Reference Guide Assert Class

Usage

If the two arguments are the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

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


Apex Reference Guide Assert Class

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

```


Apex Reference Guide Assert Class

##### isFalse(condition)

Asserts that the specified condition is `false` .

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

Type: System.Type on page 4366

Expected type.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.


Apex Reference Guide Assert Class

Return Value

Type: void

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

Type: System.Type on page 4366

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

```


Apex Reference Guide Assert Class

##### isNotInstanceOfType(instance, notExpectedType, msg)

Asserts that the instance isn’t of the specified type.

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

Type: System.Type on page 4366

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


Apex Reference Guide Assert Class

```
   notExpectedType
```

Type: System.Type on page 4366

Type that's not expected.

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

```


Apex Reference Guide Assert Class

##### isNotNull(value)

Asserts that the value isn’t null.

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


Apex Reference Guide Assert Class

Usage

If the value isn't null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

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


Apex Reference Guide Assert Class

Condition you’re checking to determine if it’s `true` .

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

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

```


### Apex Reference Guide AsyncInfo Class AsyncInfo Class

Provides methods to get the current stack depth, maximum stack depth, and the minimum queueable delay for Queueable transactions,
and to determine if maximum stack depth is set.

Namespace

System

IN THIS SECTION:

#### AsyncInfo Methods AsyncInfo Methods

### The following are methods for AsyncInfo .

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


### Apex Reference Guide AsyncOptions Class

Return Value

Type: Integer

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

AsyncOptions Properties

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)


Apex Reference Guide AsyncOptions Class

#### AsyncOptions Properties The following are properties for AsyncOptions .

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


### Apex Reference Guide Blob Class Blob Class

Contains methods for the Blob primitive data type.

Namespace

System

Usage

Salesforce supports Blob manipulation only with Apex class methods that are supplied by Salesforce. For more information on Blobs,
[see Primitive Data Types.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Blob Methods

### The following are methods for Blob .

IN THIS SECTION:

##### size()

Returns the number of bytes in the Blob.

toPdf(stringToConvert)
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

```


Apex Reference Guide Blob Class

##### toPdf(stringToConvert)

Creates a binary object out of the given string, encoding it as a PDF file.

Signature

```
   public static Blob toPdf(String stringToConvert)

```

Parameters

```
   stringToConvert
```

Type: String

Return Value

Type: Blob

Usage

`Blob.toPDF(stringToConvert)` works with any string value. Since the Spring ’26 release, `Blob.toPDF()` can use the
[same PDF rendering service as Visualforce. This change is currently controlled by a Release Update. See Use Visualforce PDF Rendering](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_system_blob_topdf.htm&release=260&type=5&language=en_US)
[Service with Apex Blob.toPdf() (Release Update) in the Salesforce release notes.](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_system_blob_topdf.htm&release=260&type=5&language=en_US)

[See Render a Visualforce Page as a PDF File for details of the improved PDF rendering service, including considerations and limitations](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_output_pdf_renderas.htm)
for rendering PDF files.

The Visualforce PDF rendering service expands the range of fonts available, and includes a multibyte-capable font. The default font is
`serif`, which is a change from the default `sans-serif` used by `Blob.toPDF()` [. See Fonts Available When Using Visualforce](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_output_pdf_supported_fonts.htm)
[PDF Rendering.](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/pages_output_pdf_supported_fonts.htm)

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


### Apex Reference Guide Boolean Class

Example

```
   String myString = 'StringToBlob';

   Blob myBlob = Blob.valueof(myString);

   System.assertEquals('StringToBlob', myBlob.toString());

##### valueOf(stringToBlob)

```

Casts the specified String to a Blob.

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

valueOf(stringToBoolean)
Converts the specified string to a Boolean value and returns `true` if the specified string value is `true` . Otherwise, returns `false` .

valueOf(fieldValue)
Converts the specified object to a Boolean value. Use this method to convert a history tracking field value or an object that represents
a Boolean value.


Apex Reference Guide Boolean Class

##### valueOf(stringToBoolean)

Converts the specified string to a Boolean value and returns `true` if the specified string value is `true` . Otherwise, returns `false` .

Signature

```
   public static Boolean valueOf(String stringToBoolean)

```

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


### Apex Reference Guide BusinessHours Class

Example

```
   List<AccountHistory> ahlist =

      [SELECT Field,OldValue,NewValue FROM AccountHistory];

   for(AccountHistory ah : ahlist) {

     System.debug('Field: ' + ah.Field);

     if (ah.field == 'IsPlatinum__c') {

       Boolean oldValue = Boolean.valueOf(ah.OldValue);

       Boolean newValue = Boolean.valueOf(ah.NewValue);

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


Apex Reference Guide BusinessHours Class

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


Apex Reference Guide BusinessHours Class

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


### Apex Reference Guide CallbackStatus Enum

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


### Apex Reference Guide Callable Interface Callable Interface

Enables developers to use a common interface to build loosely coupled integrations between Apex classes or triggers, even for code in
separate packages. Agreeing upon a common interface enables developers from different companies or different departments to build
upon one another’s solutions. Implement this interface to enable the broader community, which might have different solutions than
the ones you had in mind, to extend your code’s functionality.

Note: This interface is not an analog of the Java Callable interface, which is used for asynchronous invocation. Don’t confuse the
two.

Namespace

System

Usage

### To implement the Callable interface, you need to write only one method: call(String action, Map<String,

`Object> args)` .

### In code that utilizes or tests an implementation of Callable, cast an instance of your type to Callable . This interface is not intended to replace defining more specific interfaces. Rather, the Callable interface allows integrations in which

code from different classes or packages can use common base types.

IN THIS SECTION:

#### Callable Methods

Callable Example Implementation

#### Callable Methods

### The following are methods for Callable .

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


Apex Reference Guide Callable Interface

```
   args
```

Type: Map on page 4013<String,Object>

Arguments to be used by the specified action.

Return Value

Type: Object

The result of the method invocation.

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

```


### Apex Reference Guide Cases Class

```
       Decimal decimalTestValue = 10;

       // When

       Callable extension =

         (Callable) Type.forName(extensionClass).newInstance();

       Decimal result = (Decimal)

         extension.call('multiplyNumbers', new Map<String, Object> {

           'decimalValue' => decimalTestValue

         });

       // Then

       System.assertEquals(100, result);

     }

   }

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_casting.htm)_ : Classes and Casting

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


Apex Reference Guide Cases Class

Parameters

```
   caseId
```

Type: Id

The case SObject ID to which replies to this email should be attached.

Return Value

Type: String

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


Apex Reference Guide Cases Class

Usage

To optimize finding a match between email threads and cases in your custom code, we recommend that you use this method and
`EmailMessages.getRecordIdFromEmail` to implement a combination of token- and header-based threading.

If you are transitioning from Ref ID threading, we recommend that you replace `Cases.getCaseIdFromEmailThreadId` with
a combination of `Cases.getCaseIdFromEmailHeaders` and `EmailMessages.getRecordIdFromEmail` . If you
choose to implement header-based threading only, replace `Cases.getCaseIdFromEmailThreadId` with
`Cases.getCaseIdFromEmailHeaders` .

The _`headers`_ argument is used to find the matching Case Id using values for the `In-Reply-To` and `References` headers
based on RFC 2822. If Email-to-Case can’t find any emails with a matching `In-Reply-To` or `References` header, it also checks
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

```


Apex Reference Guide Cases Class

```
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


### Apex Reference Guide Collator Class

Usage

The argument for emailThreadId, also known as Ref ID, has the format `!00Dxx01gEW.!500xx0Yktl` . This format was introduced
in the Winter ‘24 release. The previous format, `_00Dxx1gEW._500xxYktl`, is supported for backward compatibility, but emails
sent from the Winter ‘24 release onward use the new format. Other formats that include `ref:` or `[ref:` aren’t supported by this
method.

### Collator Class

Contains methods to get locale-specific instances that can be used for comparisons and sorting. Use the `getInstance()` method
to obtain the Collator instance for a given locale and pass the Collator as the Comparator parameter to the `list.sort()` method.

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

```


Apex Reference Guide Collator Class

```
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

#### Collator Methods Collator Methods The following are methods for Collator .

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


### Apex Reference Guide Comparable Interface

Return Value

Type: Collator Class

### Comparable Interface

Adds sorting support for Lists that contain non-primitive types, that is, Lists of user-defined types. Your implementation must explicitly
handle null inputs in the `compareTo()` method to avoid a null pointer exception.

Namespace

System

Usage

### To add List sorting support for your Apex class, you must implement the Comparable interface with its compareTo method in

your class.

### To implement the Comparable interface, you must first declare a class with the implements keyword as follows:

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

#### Comparable Methods

### The following are methods for Comparable .

IN THIS SECTION:

##### compareTo(objectToCompareTo)

Returns an Integer value that is the result of the comparison.

##### compareTo(objectToCompareTo)

Returns an Integer value that is the result of the comparison.


Apex Reference Guide Comparable Interface

Signature

```
   public Integer compareTo(Object objectToCompareTo)

```

Parameters

```
   objectToCompareTo
```

Type: Object

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


### Apex Reference Guide Comparator Interface

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

compare(var1, var2)
Compares the two arguments and returns a negative integer, zero, or a positive integer depending on whether the first argument
is less than, equal to, or greater than the second argument.


Apex Reference Guide Comparator Interface

##### **`compare(var1, var2)`**

Compares the two arguments and returns a negative integer, zero, or a positive integer depending on whether the first argument is less
than, equal to, or greater than the second argument.

Signature

```
   public Integer compare(T var1, T var2)

```

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

```


Apex Reference Guide Comparator Interface

```
           } else if(e1?.getName() == null) {

             return -1;

           } else if(e2?.getName() == null) {

             return 1;

           }

           return e1.getName().compareTo(e2.getName());

           }

        }

      // Class to compare Employees by year joined

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

```


### Apex Reference Guide Continuation Class

```
      }

   }

### Continuation Class Use the Continuation class to make callouts asynchronously to a SOAP or REST Web service.

```

Namespace

System

Example

[For a code example, see Make Long-Running Callouts from a Visualforce Page.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_continuation_overview.htm)

IN THIS SECTION:

#### Continuation Constructors Continuation Properties

Continuation Methods

#### Continuation Constructors

### The following are constructors for Continuation .

IN THIS SECTION:

##### Continuation(timeout)
### Creates an instance of the Continuation class by using the specified timeout in seconds. The timeout maximum is 120 seconds.

##### Continuation(timeout)

### Creates an instance of the Continuation class by using the specified timeout in seconds. The timeout maximum is 120 seconds.

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

#### Continuation Properties

### The following are properties for Continuation .


Apex Reference Guide Continuation Class

IN THIS SECTION:

##### continuationMethod

The name of the callback method that is called after the callout response returns.

##### timeout

The timeout of the continuation in seconds. Maximum: 120 seconds.

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


Apex Reference Guide Continuation Class

Example

This example shows how to save state information for a continuation in a controller.

```
   // Declare inner class to hold state info

   private class StateInfo {

      String msg { get; set; }

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


Apex Reference Guide Continuation Class

Usage

You can add up tothree requests to a continuation.

Note: The timeout that is set in each passed-in request is ignored. Only the global timeout maximum of 120 seconds applies for
a continuation.

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


### Apex Reference Guide Cookie Class

**•** `2004` : The response size is too large (greater than 1 MB).

### Cookie Class The Cookie class lets you access cookies for your Salesforce site using Apex.

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

### Consider the following limitations when using the Cookie class: • The Cookie class can only be accessed using Apex that is saved using the Salesforce API version 19 and above.

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

```


Apex Reference Guide Cookie Class

```
           counter = new Cookie('counter','1',null,-1,true);

        } else {

        // If this isn't the first time the user is accessing the page

        // create a new cookie, incrementing the value of the original count by 1

           Integer count = Integer.valueOf(counter.getValue());

           counter = new Cookie('counter', String.valueOf(count+1),null,-1,true);

        }

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

Cookie Constructors

Cookie Methods


Apex Reference Guide Cookie Class

#### Cookie Constructors The following are constructors for Cookie .

IN THIS SECTION:

##### Cookie(name, value, path, maxAge, isSecure)
#### Creates a new instance of the Cookie class using the specified name, value, path, age, and the secure setting.

##### Cookie(name, value, path, maxAge, isSecure, SameSite)
#### Creates a new instance of the Cookie class using the specified name, value, path, and age, and settings for security and cross-domain

behavior.

Cookie(name, value, path, maxAge, isSecure, SameSite, isHttpOnly)
#### Creates a new instance of the Cookie class using the specified name, value, path, age, and settings for security, cross-domain

behavior, and JavaScript access.

##### Cookie(name, value, path, maxAge, isSecure)

#### Creates a new instance of the Cookie class using the specified name, value, path, age, and the secure setting.

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

##### Cookie(name, value, path, maxAge, isSecure, SameSite)

#### Creates a new instance of the Cookie class using the specified name, value, path, and age, and settings for security and cross-domain

behavior.


Apex Reference Guide Cookie Class

Note: Google Chrome 80 introduces a new default cookie attribute setting of `SameSite`, which is set to `Lax` . Previously, the
`SameSite` cookie attribute defaulted to the value of `None` . When `SameSite` is set to `None`, cookies must be tagged with
the `isSecure` attribute indicating that they require an encrypted HTTPS connection.

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


Apex Reference Guide Cookie Class

Signature

```
   public Cookie(String name, String value, String path, Integer maxAge, Boolean isSecure,

   String SameSite, Boolean isHttpOnly)

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


Apex Reference Guide Cookie Class

##### getMaxAge()

Returns a number representing how long the cookie is valid for, in seconds. If set to `< 0`, a session cookie is issued. If set to `0`, the
cookie is deleted.

##### getName()

Returns the name of the cookie. Can't be `null` .

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


Apex Reference Guide Cookie Class

Signature

```
   public String getName()

```

Return Value

Type: String

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


### Apex Reference Guide Crypto Class

Signature

```
   public Boolean isSecure()

```

Return Value

Type: Boolean

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


Apex Reference Guide Crypto Class

**•** When you use GCM with encryptWithManagedIV and decryptWithManagedIV, Salesforce provides an IV. and you can optionally
provide the aaData

When use the Crypto class to encrypt using GCM, the final encrypted content includes the length of the IV (always 12), the
Salesforce-generated 12-byte IV, and the cipher text.

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

Apex Reference Guide Crypto Class

**TYPE** **VARIANT** **DESCRIPTION**

`ECDSA-SHA384-P1363` ECDSA signature of an SHA256 hash (P1363
format)

ECDSA-SHA512-P1363

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


Apex Reference Guide Crypto Class

These exceptions are a subset of the exceptions that can be thrown from the System namespace. Refer to Exception Class and Built-In
Exceptions

#### For CBC, the Crypto class uses AES / CBC / PKCS7 padding, which is vulnerable to a Padding Oracle attack. You can protect against a

Padding Oracle attack by using the Encrypt-then-MAC method. In this method, you encrypt the cipher text and MAC separately.

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
[your Salesforce org. Use your preferred developer environment to run the samples. Use the Salesforce developer Introduction to REST](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_rest.htm)
[API for basic information on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_rest.htm)
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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create this Apex class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to exercise this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to exercise this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. To run it correctly, you need a PKCS8 private key.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
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

[You can use your preferred Salesforce development environment to test this function. To run it correctly, you must:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class. For the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)
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

[You can use your preferred Salesforce development environment to test this function. Create the following Apex class:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_intro_writing_apex.htm)

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

   Boolean isPcGameType = false;

   if (mcs[0].GameType__c == 'PC') {

      isPcGameType = true;

   }

   Assert.isTrue(isPcGameType);

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_customsettings.htm)_ : Custom Settings

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

By default, database operations run in user mode. To explicitly specify the access mode of database operation, set the `accessLevel`
parameter.

SEE ALSO:

Apex DML Operations

#### Database Methods The following are methods for Database . All methods are static.

IN THIS SECTION:

convertLead(leadToConvert, accessLevel)
Converts a lead into an account and contact, and, optionally, an opportunity.

convertLead(leadsToConvert, accessLevel)
Converts a list of LeadConvert objects into accounts and contacts, and, optionally, opportunities.

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


Apex Reference Guide Database Class

delete(recordToDelete, allOrNone)
Deletes an existing sObject record, such as an individual account or contact, from your organization's data.

delete(recordsToDelete, allOrNone)
Deletes a list of existing sObject records, such as individual accounts or contacts, from your organization’s data.

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


Apex Reference Guide Database Class

deleteAsync(sobjects, accessLevel)
Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
asynchronously, as background operations, and are sent to the external systems that are defined by the external objects' associated
external data sources.

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


Apex Reference Guide Database Class

getAsyncSaveResult(asyncLocator)
Returns the status of an asynchronous insert or update operation based on the unique identifier associated with each modification.

getCursor(query)
Creates a cursor when the specified SOQL query is executed.

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


Apex Reference Guide Database Class

insert(recordsToInsert, allOrNone, accessLevel)
Adds one or more sObjects, such as individual accounts or contacts, to your organization’s data.

insert(recordToInsert, dmlOptions, accessLevel)
Adds an sObject, such as an individual account or contact, to your organization's data.

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


Apex Reference Guide Database Class

insertImmediate(sobjects, accessLevel)
Initiates requests to add external object data to the relevant external systems. The requests are executed synchronously and are sent
to the external systems that are defined by the external objects' associated external data sources. If the Apex transaction contains
pending changes, the synchronous operations can't be completed and throw exceptions.

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


Apex Reference Guide Database Class

merge(mergeToRecord, duplicateRecords, accessLevel)
Merges up to two records of the same object type into the `mergeToRecord` sObject record, deleting the others, and reparenting
any related records.

merge(mergeToRecord, duplicateId, allOrNone, accessLevel)
Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.

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


Apex Reference Guide Database Class

undelete(recordID, allOrNone, accessLevel)
Restores an existing sObject record, such as an individual account or contact, from your organization's Recycle Bin.

undelete(recordIDs, allOrNone, accessLevel)
Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

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


Apex Reference Guide Database Class

updateAsync(sobjects)
Initiates requests to update external object data on the relevant external systems. The requests are executed asynchronously, as
background operations, and are sent to the external systems that are defined by the external objects' associated external data sources.

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

##### **`convertLead(leadToConvert, accessLevel)`**

Converts a lead into an account and contact, and, optionally, an opportunity.


Apex Reference Guide Database Class

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   System.AccessLevel accessLevel)

```

Parameters

```
   leadToConvert
```

Type: Database.LeadConvert

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, accessLevel)`**

Converts a list of LeadConvert objects into accounts and contacts, and, optionally, opportunities.

Signature

```
   public static List<Database.LeadConvertResult> convertLead(List<Database.LeadConvert>

   leadConverts, System.AccessLevel accessLevel)

```

Parameters

```
   leadsToConvert
```

Type: List<Database.LeadConvert>

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.LeadConvertResult>


Apex Reference Guide Database Class

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadToConvert, allOrNone)`**

Converts a lead into an account and contact, as well as (optionally) an opportunity.

Signature

```
   public static Database.LeadConvertResult convertLead(Database.LeadConvert leadToConvert,

   Boolean allOrNone)

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

Type: Database.LeadConvertResult[]

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.LeadConvertResult

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements. **`convertLead(leadsToConvert, allOrNone, accessLevel)`**

Converts a list of LeadConvert objects into accounts and contacts, as well as (optionally) opportunities.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.LeadConvertResult>

Usage

##### We recommend passing a maximum of 100 LeadConvert objects to the convertLead method. Including more than 100 objects

per call can result in Apex governor limit errors.

##### Each executed convertLead method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### **`convertLead(leadToConvert, dmlOptions, accessLevel)`**

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


Apex Reference Guide Database Class

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

Type: List<Database.LeadConvertResult>

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

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

##### Each executed countQuery method counts against the governor limit for SOQL queries.

Example

```
   String QueryString =

      'SELECT count() FROM Account';

   Integer i =

      Database.countQuery(QueryString);

```


Apex Reference Guide Database Class

##### **`countQuery(query, accessLevel)`**

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

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Integer

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

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


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user
mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored,
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.

Return Value

Type: Integer

Usage

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

Each executed `countQueryWithBinds` method counts against the governor limit for SOQL queries.

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

Type: Database.DeleteResult

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements. delete(recordsToDelete, allOrNone)

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


Apex Reference Guide Database Class

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

Type: Database.DeleteResult[]

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.DeleteResult


Apex Reference Guide Database Class

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

Type: List<Database.DeleteResult>

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements. **`delete(recordID, allOrNone, accessLevel)`**

Deletes existing sObject records, such as individual accounts or contacts, from your organization’s data.

Signature

```
   public static Database.DeleteResult delete(Id recordID, Boolean allOrNone,

   System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.DeleteResult>

Usage

##### delete is analogous to the delete() statement in the SOAP API. Each executed delete method counts against the governor limit for DML statements.

To delete a share object record for a custom object, you must pass an _`sObject`_ instead of a _`recordID`_ . The _`recordID`_ parameter
isn't supported for share objects for custom objects.

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

action callback to update org data according to the operation’s results. The callback object must extend
`DataSource.AsyncDeleteCallback` .

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteAsync(sobject, callback, accessLevel)

Initiates a request to delete the external data that corresponds to the specified external object record. The request is executed
asynchronously, as a background operation, and is sent to the external system that's defined by the external object's associated external
data source. Allows referencing a callback class whose `processDelete` method is called after deletion.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.


Apex Reference Guide Database Class

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

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.DeleteResult

Status result for the delete operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncDeleteResult()` .

##### deleteImmediate(sobjects)

Initiates requests to delete the external data that corresponds to the specified external object records. The requests are executed
synchronously and are sent to the external systems that are defined by the external objects' associated external data sources. If the Apex
transaction contains pending changes, the synchronous operations can't be completed and throw exceptions.

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.DeleteResult>

Status results for the delete operation.

Usage

The batch limit for big objects using `deleteImmediate()` is 50,000 records at once.


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.DeleteResult

Status result for the delete operation.

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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

An instance of a class that implements the Database.Batchable interface.

Return Value

Type: ID

The ID of the new batch job (AsyncApexJob).

Usage

When calling this method, Salesforce chunks the records returned by the `start` method of the batch class into batches of 200, and
##### then passes each batch to the execute method. Apex governor limits are reset for each execution of execute .

[For more information, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Versioned Behavior Changes

##### If the executeBatch call fails to acquire an Apex flex queue lock:

**•** In API version 52.0 and later, the call throws a `System.AsyncException` .

**•** In API version 51.0 and earlier, the call returns an empty ID, "000000000000000", instead of throwing an exception.


Apex Reference Guide Database Class

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
by the `QueryLocator` into smaller batches of up to 200 records. If the `start` method of the batch class returns an iterable, the
scope parameter value has no upper limit; however, if you use a very high number, you could run into other limits.

##### Apex governor limits are reset for each execution of execute .

[For more information, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_batch_interface.htm)

Versioned Behavior Changes

##### If the executeBatch call fails to acquire an Apex flex queue lock:

**•** In API version 52.0 and later, the call throws a `System.AsyncException` .

**•** In API version 51.0 and earlier, the call returns an empty ID, "000000000000000", instead of throwing an exception.

##### getAsyncDeleteResult(deleteResult)

Retrieves the status of an asynchronous delete operation that’s identified by a `Database.DeleteResult` object.

Signature

```
   public static Database.DeleteResult getAsyncDeleteResult(Database.DeleteResult

   deleteResult)

```


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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

```


Apex Reference Guide Database Class

```
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

Type: Database.PaginationCursor on page 2732

##### **`getPaginationCursor(query, accessLevel)`**

Creates a pagination cursor when the specified SOQL query is executed.

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

Type: System.AccessLevel on page 3593

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.PaginationCursor on page 2732

##### **`getPaginationCursorWithBinds(query, bindMap, accessLevel)`**

Creates a pagination cursor when the specified SOQL query is executed.


Apex Reference Guide Database Class

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

Type: System.AccessLevel on page 3593

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.PaginationCursor on page 2732

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

[For more information, see Understanding Apex Managed Sharing, and IdeaStandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)


Apex Reference Guide Database Class

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

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.QueryLocator


Apex Reference Guide Database Class

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and IdeaStandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

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

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.QueryLocator

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

##### You can't use getQueryLocator with any query that contains an aggregate function. Each executed getQueryLocator method counts against the governor limit of 10,000 total records retrieved and the total number

of SOQL queries issued.

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

##### **`getQueryLocatorWithBinds(query, bindMap, accessLevel)`**

Creates a QueryLocator object used in batch Apex or Visualforce. Bind variables in the query are resolved from the _`bindMap`_ Map
parameter directly with the key, rather than from Apex code variables.


Apex Reference Guide Database Class

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
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.

Return Value

Type: Database.QueryLocator

Usage

The access level is evaluated only when the `QueryLocator` is created. A `QueryLocator` can be long lived, such as when used
in a batch. We don’t reevaluate the object and field-level security with each iteration of the `QueryLocator` . As a result, if you specify
user mode, and then change the security settings after the `QueryLocator` is created, the new settings aren’t enforced.

You can't use `getQueryLocatorWithBinds` [with any query that contains an aggregate function.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_agg_fns.htm)

Each executed `getQueryLocatorWithBinds` method counts against the governor limit for the total number of records retrieved
by Database.getQueryLocator(10,000) and the total number of SOQL queries issued. See Per Transaction Apex Limits.

[For more information, see Understanding Apex Managed Sharing, and StandardSetController Class.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_bulk_sharing.htm)

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

```


Apex Reference Guide Database Class

```
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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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

##### insert(recordToInsert, dmlOptions)

```

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

##### Each executed insert method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### insert(recordsToInsert, dmlOptions)

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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

Type: List<Database.SaveResult>

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


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.SaveResult

Usage

##### insert is analogous to the INSERT statement in SQL.

Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that
is too long for the field.

##### Each executed insert method counts against the governor limit for DML statements. **`insert(recordsToInsert, dmlOptions, accessLevel)`**

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

Usage

##### insert is analogous to the INSERT statement in SQL.


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value>

Type: List<Database.SaveResult>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.


Apex Reference Guide Database Class

Return Value

Type: Database.SaveResult

Status result for the insert operation. The result corresponds to the record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation. Each result corresponds to a record processed by this asynchronous operation and is associated
with a unique identifier ( `asyncLocator` ). The `asyncLocator` value is included in the errors array of the result. You can retrieve
this identifier with `Database.getAsyncLocator()` . Retrieve the final result with `Database.getAsyncSaveResult()` .

Usage

`Database.insertAsync()` methods can’t be executed in the context of a portal user, even when the portal user is a community
member. To add external object records via Apex, use `Database.insertImmediate()` methods.


Apex Reference Guide Database Class

##### insertAsync(sobject, accessLevel)

Initiates a request to add external object data to the relevant external system. The request is executed asynchronously, as a background
operation, and is sent to the external system that's defined by the external object's associated external data source.

Signature

```
   public static Database.SaveResult insertAsync(SObject sobject, System.AccessLevel

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

Return Value

Type: List<Database.SaveResult>

Status results for the insert operation.

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.


Apex Reference Guide Database Class

Return Value

Type: Database.SaveResult

Status result for the insert operation.

Usage

If a record update fails, the method doesn’t throw an exception. The returned `SaveResult` object indicates whether the operation
was successful. If it failed, the object returns the error code and description.

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


Apex Reference Guide Database Class

The sObject record that the duplicate record is merged into.

```
   duplicateRecord
```

Type: sObject

The sObject record to merge with the mergeToRecord. This sObject must be of the same type as the mergeToRecord.

Return Value

Type: Database.MergeResult

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements. merge(mergeToRecord, duplicateRecord, allOrNone)

Merges the duplicate sObject record into the `mergeToRecord` sObject of the same type, optionally returning any errors, deleting
the duplicate, and reparenting any related records.

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


Apex Reference Guide Database Class

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

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateId, accessLevel)`**

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.MergeResult

Usage

##### Each executed merge method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### **`merge(mergeToRecord, duplicateRecord, accessLevel)`**

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.MergeResult>

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.MergeResult>


Apex Reference Guide Database Class

Usage

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateId, allOrNone, accessLevel)`**

Merges the duplicate record into the `mergeToRecord` sObject record of the same type, optionally returning any errors, deleting the
duplicate, and reparenting any related records. Merges only accounts, contacts, or leads.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, Id duplicateId, Boolean

   allOrNone, System.AccessLevel accessLevel)

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

Type: Database.MergeResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)


Apex Reference Guide Database Class

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecord, allOrNone, accessLevel)`**

Merges the duplicate sObject record into the `mergeToRecord` sObject record of the same type, optionally returning any errors,
deleting the duplicate, and reparenting any related records.

Signature

```
   public static Database.MergeResult merge(SObject mergeToRecord, SObject duplicateRecord,

   Boolean allOrNone, System.AccessLevel accessLevel)

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

```
   accessLevel
```

Type: System.AccessLevel

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.MergeResult

Usage

If you use the `accessLevel` parameter to specify that the method runs in user mode, we report all encountered inaccessible fields.
The way to retrieve the names of these inaccessible fields depends on the value of this method's `allOrNone` parameter, or the
equivalent `[DmlOptions.optAllOrNone](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_dmloptions.htm#apex_Database_DmlOptions_optAllOrNone)` property. If you specify that:


Apex Reference Guide Database Class

**•** `allOrNone=true` or `DmlOptions.optAllOrNone=true` : Catch the `DMLException` and use the
`DMLException.getDMLFieldNames()` [method to retrieve the list of inaccessible fields. See Exception Class and Built-In](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)
[Exceptions for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**•** `allOrNone=false` or `DmlOptions.optAllOrNone=false` : For each failing record, we update the `Database.Error`
object that results from the DML operation. Use the `Error.getFields()` method to retrieve the list of inaccessible fields. See
[the Error Class methods for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_methods_system_database_error.htm#apex_Database_Error_methods)

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateIds, allOrNone, accessLevel)`**

Merges up to two records of the same sObject type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.

Signature

```
   public static List<Database.MergeResult> merge(SObject mergeToRecord, List<Id>

   duplicateIds, Boolean allOrNone, System.AccessLevel accessLevel)

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

Type: List<Database.MergeResult>


Apex Reference Guide Database Class

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

##### Each executed merge method counts against the governor limit for DML statements. **`merge(mergeToRecord, duplicateRecords, allOrNone, accessLevel)`**

Merges up to two records of the same object type into the `mergeToRecord` sObject record, optionally returning any errors, deleting
the duplicates, and reparenting any related records.

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.MergeResult>


Apex Reference Guide Database Class

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

Each executed `merge` method counts against the governor limit for DML statements.

##### query(queryString)

Creates a dynamic SOQL query at runtime.

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

Type: List on page 3992<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops. Unlike
[inline SOQL, fields in bind variables aren’t supported. For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

`Database.query()` calls containing an inner query for a related child object may not return the entire result set based on the size
and complexity of the records requested. Instead, use `Database.getQueryLocator()` in conjunction with Apex Batch.
Alternatively, you can use the same SOQL query with SOAP API to be able to access all the resulting records.

##### Each executed query method counts against the governor limit for SOQL queries. **`query(queryString, accessLevel)`**

Creates a dynamic SOQL query at runtime.

Signature

```
   public static List<SObject> query(String queryString, System.AccessLevel accessLevel)

```


Apex Reference Guide Database Class

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List on page 3992<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops. Unlike
[inline SOQL, fields in bind variables aren’t supported. For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

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


Apex Reference Guide Database Class

The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user
mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored,
[and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level security,](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
and sharing rules of the current user are enforced.

Return Value

Type: List on page 3992<sObject>

Usage

This method can be used wherever a static SOQL query can be used, such as in regular assignment statements and `for` loops.

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

Each executed `queryWithBinds` method counts against the governor limit for SOQL queries.

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


Apex Reference Guide Database Class

Return Value

Type: void

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(databaseSavepoint)` and `Database.setSavepoint()` calls incremented the DML row
usage limit.

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

[For an example, see Transaction Control.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)

Versioned Behavior Changes

For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()`
are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged.


Apex Reference Guide Database Class

Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was
uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both
`Database.rollback(Savepoint)` and `Database.setSavepoint()` calls incremented the DML row usage limit.

##### setSavepoint()

Returns a savepoint variable that can be stored as a local variable, then used with the `rollback` method to restore the database to
that point.

Signature

```
   public static System.Savepoint setSavepoint()

```

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

[For an example, see Transaction Control.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)

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

Type: Database.UndeleteResult

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


Apex Reference Guide Database Class

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

Type: Database.UndeleteResult[]

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: Database.UndeleteResult


Apex Reference Guide Database Class

Usage

##### undelete is analogous to the UNDELETE statement in SQL. Each executed undelete method counts against the governor limit for DML statements. **`undelete(recordsToUndelete, allOrNone, accessLevel)`**

Restores one or more existing sObject records, such as individual accounts or contacts, from your organization’s Recycle Bin.

Signature

```
   public static List<Database.UndeleteResult> undelete(List<SObject> recordsToUndelete,

   Boolean allOrNone, System.AccessLevel accessLevel)

```

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

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

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

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


Apex Reference Guide Database Class

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.UndeleteResult>

Usage

`undelete` is analogous to the UNDELETE statement in SQL.

Each executed `undelete` method counts against the governor limit for DML statements.

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


Apex Reference Guide Database Class

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


Apex Reference Guide Database Class

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

##### Each executed update method counts against the governor limit for DML statements.


Apex Reference Guide Database Class

##### **`update(recordToUpdate, allOrNone, accessLevel)`**

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

Type: Database.SaveResult

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

##### **`update(recordsToUpdate, allOrNone, accessLevel)`**

Modifies one or more existing sObject records, such as individual accounts or contacts, in your organization’s data.


Apex Reference Guide Database Class

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

(Optional) The _`accessLevel`_ parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` )
or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. User mode is the default.

Return Value

Type: List<Database.SaveResult>

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

##### **`update(recordToUpdate, dmlOptions, accessLevel)`**

