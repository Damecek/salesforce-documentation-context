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
560.

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
External Objects on page 524.

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

**•** SOAP Services: Defining a Class from a WSDL Document on page 609

**•** Invoking HTTP Callouts on page 622

**•** Asynchronous Callouts for Long-Running Requests on page 634

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

The following samples work with the sample WSDL file in Generated WSDL2Apex Code on page 615:

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
page 633.

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
`DocSamplePort` class described in Generated WSDL2Apex Code on page 615. Set the timeout value in milliseconds by assigning a
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
long-running requests on page 351 . But by using asynchronous callouts, the requests aren’t subjected to this limit and can be executed.

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

In this example, the API version is 66.0, and the following debug log categories and levels have been set.

Apex Code DEBUG

Apex Profiling INFO

Callout INFO

Database INFO

System DEBUG

Validation INFO

Visualforce INFO

Workflow INFO

Warning: If the Apex Code log level is set to FINEST, the debug log includes details of all Apex variable assignments. Ensure
that the Apex Code being traced doesn’t handle sensitive data. Before enabling FINEST log level, be sure to understand the
level of sensitive data your organization's Apex handles. Be careful with processes such as community users self-registration
where user passwords can be assigned to an Apex string variable.

**Execution Units**
An execution unit is equivalent to a transaction. It contains everything that occurred within the transaction. `EXECUTION_STARTED`
and `EXECUTION_FINISHED` delimit an execution unit.

**Code Units**
A code unit is a discrete unit of work within a transaction. For example, a trigger is one unit of code, as is a `webservice` method
or a validation rule.

Note: A class isn’t a discrete unit of code.


Apex Developer Guide Debugging Apex

`CODE_UNIT_STARTED` and `CODE_UNIT_FINISHED` delimit units of code. Units of work can embed other units of work.
For example:

```
     EXECUTION_STARTED

     CODE_UNIT_STARTED|[EXTERNAL]execute_anonymous_apex

     CODE_UNIT_STARTED|[EXTERNAL]MyTrigger on Account trigger event BeforeInsert for

     [new]|__sfdc_trigger/MyTrigger

     CODE_UNIT_FINISHED <-- The trigger ends

     CODE_UNIT_FINISHED <-- The executeAnonymous ends

     EXECUTION_FINISHED

```

Units of code include, but aren’t limited to, the following:

**•** Triggers

**•** Workflow invocations and time-based workflow

**•** Validation rules

**•** Approval processes

**•** Apex lead convert

**•** `@future` method invocations

**•** Web service invocations

**•** `executeAnonymous` calls

**•** Visualforce property access on Apex controllers

**•** Visualforce actions on Apex controllers

**•** Execution of the batch Apex `start` and `finish` methods, and each execution of the `execute` method

**•** Execution of the Apex `System.Schedule execute` method

**•** Incoming email handling

**Log Lines**
Log lines are included inside units of code and indicate which code or rules are being executed. Log lines can also be messages
written to the debug log.

Log lines are made up of a set of fields, delimited by a pipe ( `|` ). The format is:

**•** _timestamp_ : Consists of the time when the event occurred and a value between parentheses. The time is in the user’s time zone
and in the format _`HH:mm:ss.SSS`_ . The value in parentheses represents the time elapsed in nanoseconds since the start of
the request. The elapsed time value is excluded from logs reviewed in the Developer Console when you use the Execution Log
view. However, you can see the elapsed time when you use the Raw Log view. To open the Raw Log view, from the Developer
Console’s Logs tab, right-click the name of a log and select **Open Raw Log** .

**•** _event identifier_ : Specifies the event that triggered the debug log entry (such as `SAVEPOINT_RESET` or `VALIDATION_RULE` ).

Also includes additional information logged with that event, such as the method name or the line and character number where
the code was executed. If a line number can’t be located, `[EXTERNAL]` is logged instead. For example, `[EXTERNAL]` is
logged for built-in Apex classes or code that’s in a managed package.

For some events ( `CODE_UNIT_STARTED`, `CODE_UNIT_FINISHED`, `VF_APEX_CALL_START`, `VF_APEX_CALL_END`,
`CONSTRUCTOR_ENTRY`, and `CONSTRUCTOR_EXIT` ), the end of the event identifier includes a pipe ( `|` ) followed by a
typeRef for an Apex class or trigger.

For a trigger, the typeRef begins with the SFDC trigger prefix `__sfdc_trigger/` . For example,
`__sfdc_trigger/` _**`YourTriggerName`**_ or `__sfdc_trigger/` _**`YourNamespace`**_ `/` _**`YourTriggerName`**_ .

For a class, the typeRef uses the format _**`YourClass`**_, _**`YourClass`**_ `$` _**`YourInnerClass,`**_, or
_**`YourNamespace`**_ `/` _**`YourClass`**_ `$` _**`YourInnerClass`**_ .


Apex Developer Guide Debugging Apex

**More Log Data**
In addition, the log contains the following information.

**•** Cumulative resource usage is logged at the end of many code units. Among these code units are triggers, `executeAnonymous`,
batch Apex message processing, `@future` methods, Apex test methods, Apex web service methods, and Apex lead convert.

**•** Cumulative profiling information is logged once at the end of the transaction and contains information about DML invocations,
expensive queries, and so on. “Expensive” queries use resources heavily.

**•** Heap usage is accurately reported in the debug log and an exception is thrown whenever an Apex Heap Size error occurs. At
other times, the heap size shown in the debug log is the largest heap size that was calculated during the transaction. To reduce
the overhead on small transactions, minimal heap usage doesn’t warrant an accurate calculation and is reported as 0(zero).

The following is an example debug log.

```
   37.0 APEX_CODE,FINEST;APEX_PROFILING,INFO;CALLOUT,INFO;DB,INFO;SYSTEM,DEBUG;

      VALIDATION,INFO;VISUALFORCE,INFO;WORKFLOW,INFO

   Execute Anonymous: System.debug('Hello World!');

   16:06:58.18 (18043585)|USER_INFO|[EXTERNAL]|005D0000001bYPN|devuser@example.org|

      Pacific Standard Time|GMT-08:00

   16:06:58.18 (18348659)|EXECUTION_STARTED

   16:06:58.18 (18383790)|CODE_UNIT_STARTED|[EXTERNAL]|execute_anonymous_apex

   16:06:58.18 (23822880)|HEAP_ALLOCATE|[72]|Bytes:3

   16:06:58.18 (24271272)|HEAP_ALLOCATE|[77]|Bytes:152

   16:06:58.18 (24691098)|HEAP_ALLOCATE|[342]|Bytes:408

   16:06:58.18 (25306695)|HEAP_ALLOCATE|[355]|Bytes:408

   16:06:58.18 (25787912)|HEAP_ALLOCATE|[467]|Bytes:48

   16:06:58.18 (26415871)|HEAP_ALLOCATE|[139]|Bytes:6

   16:06:58.18 (26979574)|HEAP_ALLOCATE|[EXTERNAL]|Bytes:1

   16:06:58.18 (27384663)|STATEMENT_EXECUTE|[1]

   16:06:58.18 (27414067)|STATEMENT_EXECUTE|[1]

   16:06:58.18 (27458836)|HEAP_ALLOCATE|[1]|Bytes:12

   16:06:58.18 (27612700)|HEAP_ALLOCATE|[50]|Bytes:5

   16:06:58.18 (27768171)|HEAP_ALLOCATE|[56]|Bytes:5

   16:06:58.18 (27877126)|HEAP_ALLOCATE|[64]|Bytes:7

   16:06:58.18 (49244886)|USER_DEBUG|[1]|DEBUG|Hello World!

   16:06:58.49 (49590539)|CUMULATIVE_LIMIT_USAGE

   16:06:58.49 (49590539)|LIMIT_USAGE_FOR_NS|(default)|

     Number of SOQL queries: 0 out of 100

     Number of query rows: 0 out of 50000

     Number of SOSL queries: 0 out of 20

     Number of DML statements: 0 out of 150

     Number of DML rows: 0 out of 10000

     Maximum CPU time: 0 out of 10000

     Maximum heap size: 0 out of 6000000

     Number of callouts: 0 out of 100

     Number of Email Invocations: 0 out of 10

     Number of future calls: 0 out of 50

     Number of queueable jobs added to the queue: 0 out of 50

     Number of Mobile Apex push calls: 0 out of 10

   16:06:58.49 (49590539)|CUMULATIVE_LIMIT_USAGE_END

   16:06:58.18 (52417923)|CODE_UNIT_FINISHED|execute_anonymous_apex

   16:06:58.18 (54114689)|EXECUTION_FINISHED

```


Apex Developer Guide Debugging Apex

Setting Debug Log Filters for Apex Classes and Triggers

To debug complex Apex logic, you can set Apex class and trigger trace flags, also known as debug log filters. For example, you can raise
the log verbosity for a given class while turning off logging for other classes or triggers. These trace flags have the debug log type
`CLASS_TRACING` and override the debug log levels of the `USER_DEBUG` and `DEVELOPER_LOG` trace flags.

[For an explanation and an example of how Apex class and trigger trace flags work, see Debug Log Filtering for Apex Classes and Apex](https://help.salesforce.com/s/articleView?id=platform.code_debug_log_classes.htm&type=5&language=en_US)
[Triggers in](https://help.salesforce.com/s/articleView?id=platform.code_debug_log_classes.htm&type=5&language=en_US) _Salesforce Help_ .

[For concrete instructions about how to configure debug log filters, see Set Up Apex Class and Trigger Trace Flags in](https://help.salesforce.com/s/articleView?id=platform.code_debug_log_classes_setup.htm&type=5&language=en_US) _Salesforce Help_ .

##### Working with Logs in the Developer Console

Use the Logs tab in the Developer Console to open debug logs.

Debugging Apex API Calls

Debug Log Order of Precedence
Which events are logged depends on various factors. These factors include your trace flags, the default logging levels, your API
header, user-based system log enablement, and the log levels set by your entry points.

SEE ALSO:

_Salesforce Help_ [: Set Up Debug Logging](https://help.salesforce.com/HTViewHelpDoc?id=code_add_users_debug_log.htm&language=en_US)

_Salesforce Help_ [: View Debug Logs](https://help.salesforce.com/HTViewHelpDoc?id=code_viewing_log_details.htm&language=en_US)

_Salesforce Help_ [: Delete Debug Logs](https://help.salesforce.com/HTViewHelpDoc?id=code_debug_log_delete.htm&language=en_US)

##### Working with Logs in the Developer Console

Use the Logs tab in the Developer Console to open debug logs.

Logs open in Log Inspector. Log Inspector is a context-sensitive execution viewer in the Developer Console. It shows the source of an
operation, what triggered the operation, and what occurred next. Use this tool to inspect debug logs that include database events, Apex
processing, workflow, and validation logic.

To learn more about working with logs in the Developer Console, see _Log Inspector_ in the Salesforce online help.

When using the Developer Console or monitoring a debug log, you can specify the level of information that gets included in the log.

**Log category**
The type of information logged, such as information from Apex or workflow rules.

**Log level**
The amount of information logged.

**Event type**
The combination of log category and log level that specify which events get logged. Each event can log additional information, such
as the line and character number where the event started, fields associated with the event, and duration of the event.

Debug Log Categories

Each debug level includes a debug log level for each of these log categories. The amount of information logged for each category
depends on the log level.


Apex Developer Guide Debugging Apex

**Log Category** **Description**

`Database` Includes information about database activity, including every data manipulation language
(DML) statement or inline SOQL or SOSL query.

`Database Access` Logs rules and policy information for objects accessed from the UI, which can be used to
determine why an object isn’t accessible.

`Workflow` Includes information for workflow rules, flows, and processes, such as the rule name and the
actions taken.

`NBA` Includes information about Einstein Next Best Action activity, including strategy execution
details from Strategy Builder.

`Validation` Includes information about validation rules, such as the name of the rule and whether the
rule evaluated true or false.

```
Callout

Apex Code

```

Includes the request-response XML that the server is sending and receiving from an external
web service. Useful when debugging issues related to using Lightning Platform web service
API calls or troubleshooting user access to external objects via Salesforce Connect.

Includes information about Apex code. Can include information such as log messages
generated by DML statements, inline SOQL or SOSL queries, the start and completion of any
triggers, and the start and completion of any test method.

`Apex Profiling` Includes cumulative profiling information, such as the limits for your namespace and the
number of emails sent.

`Visualforce` Includes information about Visualforce events, including serialization and deserialization of
the view state or the evaluation of a formula field in a Visualforce page.

`System` Includes information about calls to all system methods such as the `System.debug`
method.

Debug Log Levels

Each debug level includes one of these log levels for each log category. The levels are listed from lowest to highest. Specific events are
logged based on the combination of category and levels. Most events start being logged at the INFO level. The level is cumulative, that
is, if you select FINE, the log also includes all events logged at the DEBUG, INFO, WARN, and ERROR levels.

Note: Not all levels are available for all categories. Only the levels that correspond to one or more events are available.

**•** `NONE`

**•** `ERROR`

**•** `WARN`

**•** `INFO`

**•** `DEBUG`

**•** `FINE`

**•** `FINER`

**•** `FINEST`


Apex Developer Guide Debugging Apex

Important: Before running a deployment, verify that the Apex Code log level isn’t set to FINEST. Otherwise, the deployment is
likely to take longer than expected. If the Developer Console is open, the log levels in the Developer Console affect all logs, including
logs created during a deployment.

Debug Event Types

This example shows what is written to the debug log. The event is `USER_DEBUG` . The format is _`timestamp`_ | _`event identifier`_ .
This example shows a debug log line.

**Debug Log Line Example**

**•** _timestamp_ : Consists of the time when the event occurred and a value between parentheses. The time is in the user’s time zone and
in the format _`HH:mm:ss.SSS`_ . The value in parentheses represents the time elapsed in nanoseconds since the start of the request.
The elapsed time value is excluded from logs reviewed in the Developer Console when you use the Execution Log view. However,
you can see the elapsed time when you use the Raw Log view. To open the Raw Log view, from the Developer Console’s Logs tab,
right-click the name of a log and select **Open Raw Log** .

**•** _event identifier_ : Specifies the event that triggered the debug log entry, such as `SAVEPOINT_RESET` or `VALIDATION_RULE` .

Also includes additional information logged with that event, such as the method name or the line and character number where the
code was executed. If a line number can’t be located, `[EXTERNAL]` is logged instead. For example, `[EXTERNAL]` is logged for
built-in Apex classes or code that’s in a managed package.

For some events, such as `CODE_UNIT_STARTED`, `CODE_UNIT_FINISHED`, `VF_APEX_CALL_START`,
`VF_APEX_CALL_END`, `CONSTRUCTOR_ENTRY`, and `CONSTRUCTOR_EXIT`, the end of the event identifier includes a pipe
( `|` ) followed by a typeRef for an Apex class or trigger.

For a trigger, the typeRef begins with the SFDC trigger prefix `__sfdc_trigger/` . For example,
`__sfdc_trigger/` _**`YourTriggerName`**_ or `__sfdc_trigger/` _**`YourNamespace`**_ `/` _**`YourTriggerName`**_ .

For a class, the typeRef uses the format _**`YourClass`**_, _**`YourClass`**_ `$` _**`YourInnerClass,`**_ or
_**`YourNamespace`**_ `/` _**`YourClass`**_ `$` _**`YourInnerClass`**_ .

In this example, the event identifier consists of:

**•** Event name:

```
     USER_DEBUG

```

**•** Line number of the event in the code:

```
     [2]

```

**•** Logging level the `System.Debug` method was set to:

```
     DEBUG

```


Apex Developer Guide Debugging Apex

**•** User-supplied string for the `System.Debug` method:

```
     Hello world!

```

This code snippet triggers this example log line.

**Debug Log Line Code Snippet**

This log line is recorded when the test reaches line 5 in the code.

```
   15:51:01.071 (55856000)|DML_BEGIN|[5]|Op:Insert|Type:Invoice_Statement__c|Rows:1

```

In this example, the event identifier consists of:

**•** Event name:

```
     DML_BEGIN

```

**•** Line number of the event in the code:

```
     [5]

```

**•** DML operation type— `Insert` :

```
     Op:Insert

```

**•** Object name:

```
     Type:Invoice_Statement__c

```

**•** Number of rows passed into the DML operation:

```
     Rows:1

```

These event types are logged. The table lists which fields or other information are logged with each event, and which combination of
log level and category causes an event to be logged.

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`BULK_HEAP_ALLOCATE` Number of bytes allocated Apex FINEST
Code

`CALLOUT_REQUEST` Line number and request headers Callout INFO and
above

`CALLOUT_REQUEST` External endpoint and method Callout INFO and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

(External object access via cross-org
and OData adapters for Salesforce
Connect)

`CALLOUT_RESPONSE` Line number and response body Callout INFO and
above

`CALLOUT_RESPONSE` Status and status code Callout INFO and
above

(External object access via cross-org
and OData adapters for Salesforce
Connect)

ERROR
and
above

ERROR
and
above

```
CODE_UNIT_FINISHED

CODE_UNIT_STARTED

```

Line number, code unit name, such as Apex
`MyTrigger on Account` Code

```
trigger event
```

`BeforeInsert for [new]`,
and:

**•** For Apex methods, the namespace
(if applicable), class name, and
method name; for example,

```
  YourNamespace.YourClass.yourMethod()
```

or

```
  YourClass.yourMethod()

```

**•** For Apex triggers, a typeRef; for
example,

```
  __sfdc_trigger/YourNamespace.YourTrigger
```

or

```
  __sfdc_trigger/YourTrigger

```

Line number, code unit name, such as Apex
`MyTrigger on Account` Code

```
trigger event
```

`BeforeInsert for [new]`,
and:

**•** For Apex methods, the namespace
(if applicable), class name, and
method name; for example,

```
  YourNamespace.YourClass.yourMethod()
```

or

```
  YourClass.yourMethod()

```

**•** For Apex triggers, a typeRef; for
example,

```
  __sfdc_trigger/YourTrigger

```


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

```
CONSTRUCTOR_ENTRY

CONSTRUCTOR_EXIT

```

Line number, Apex class ID, the string Apex FINE and
`<init>()` with the types of Code above
parameters (if any) between the

parentheses, and a typeRef; for
example, `YourClass` or

```
YourClass.YourInnerClass

```

Line number, the string `<init>()` Apex FINE and
with the types of parameters (if any) Code above
between the parentheses, and a

typeRef; for example, `YourClass`
or

```
YourClass.YourInnerClass

```

`CUMULATIVE_LIMIT_USAGE` None Apex INFO and
Profiling above

`CUMULATIVE_LIMIT_USAGE_END` None Apex INFO and
Profiling above

`CUMULATIVE_PROFILING` None Apex FINE and
Profiling above

`CUMULATIVE_PROFILING_BEGIN` None Apex FINE and
Profiling above

`CUMULATIVE_PROFILING_END` None Apex FINE and
Profiling above

```
CURSOR_CREATE_BEGIN

CURSOR_CREATE_END

CURSOR_FETCH

CURSOR_FETCH_PAGE

```

DB INFO and
Line number and SOQL query
above

This event occurs when you call
`[Database.getCursor()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getCursor)` or
`[Database.getPaginationCursor()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_database.htm#apex_System_Database_getPaginationCursor)` .

DB INFO and
Line number, query ID, and number of
above
rows in the result set

This event occurs when a cursor or
pagination cursor is created.

DB INFO and
Line number, query ID, cursor offset
above
position, and number of rows fetched

This event occurs when you call
`[Cursor.fetch()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Database_Cursor.htm#apex_Database_Cursor_fetch)` .

DB INFO and
Line number, query ID, cursor offset
above
position, and number of rows on the
current page


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

This event occurs when you call
`[PaginationCursor.fetchPage()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Database_PaginationCursor.htm#apex_Database_PaginationCursor_fetchPage)` .

```
DATA_ACCESS_EVALUATION

DML_BEGIN

```

Request and Response for the data Data FINE
access request. Used regardless of the Access
data space or policy being accessed.

Line number, operation (such as DB INFO and
`Insert` or `Update` ), record name above
or type, and number of rows passed
into DML operation

`DML_END` Line number DB INFO and
above

`EMAIL_QUEUE` Line number Apex INFO and
Code above

`ENTERING_MANAGED_PKG` Package namespace Apex FINE and
Code above

`EVENT_SERVICE_PUB_BEGIN` Event Type Workflow INFO and
above

FINER
and
above

```
EVENT_SERVICE_PUB_DETAIL

```

Subscription IDs, ID of the user who Workflow
published the event, and event
message data

`EVENT_SERVICE_PUB_END` Event Type Workflow INFO and
above

`EVENT_SERVICE_SUB_BEGIN` Event type and action (subscribe or Workflow INFO and
unsubscribe) above

FINER
and
above

```
EVENT_SERVICE_SUB_DETAIL

```

ID of the subscription, ID of the Workflow
subscription instance, reference data
(such as process API name), ID of the
user who activated or deactivated the
subscription, and event message data

`EVENT_SERVICE_SUB_END` Event type and action (subscribe or Workflow INFO and
unsubscribe) above

`EXCEPTION_THROWN` Line number, exception type, and Apex INFO and
message Code above

`EXECUTION_FINISHED` None Apex
Code


ERROR
and
above

Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`EXECUTION_STARTED` None Apex
Code

`FATAL_ERROR` Exception type, message, and stack Apex
trace Code

ERROR
and
above

ERROR
and
above

FINER
and
above

FINER
and
above

```
FLOW_ACTIONCALL_DETAIL

```

Interview ID, element name, action Workflow
type, action enum or ID, whether the
action call succeeded, and error
message

`FLOW_ASSIGNMENT_DETAIL` Interview ID, reference, operator, and Workflow
value

`FLOW_BULK_ELEMENT_BEGIN` Interview ID and element type Workflow FINE and
above

`FLOW_BULK_ELEMENT_DETAIL` Interview ID, element type, element Workflow
name, number of records

FINER
and
above

```
FLOW_BULK_ELEMENT_END

FLOW_BULK_ELEMENT_LIMIT_USAGE

FLOW_BULK_ELEMENT_NOT_SUPPORTED

```

Interview ID, element type, element Workflow FINE and
name, number of records, and above
execution time

Operation, element name, and entity Workflow INFO and
name that doesn’t support bulk above
operations

Incremented usage toward a limit for Workflow
this bulk element. Each event displays
the usage for one of these limits.

```
SOQL queries

SOQL query rows

SOSL queries

DML statements

DML rows

CPU time in ms

Heap size in bytes

Callouts

Email invocations

Future calls

Jobs in queue

Push notifications

```

FINER
and
above

`FLOW_CREATE_INTERVIEW_BEGIN` Organization ID, definition ID, and Workflow INFO and
version ID above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`FLOW_CREATE_INTERVIEW_END` Interview ID and flow name Workflow INFO and
above

`FLOW_CREATE_INTERVIEW_ERROR` Message, organization ID, definition Workflow
ID, and version ID

ERROR
and
above

`FLOW_ELEMENT_BEGIN` Interview ID, element type, and Workflow FINE and
element name above

`FLOW_ELEMENT_DEFERRED` Element type and element name Workflow FINE and
above

`FLOW_ELEMENT_END` Interview ID, element type, and Workflow FINE and
element name above

`FLOW_ELEMENT_ERROR` Message, element type, and element Workflow
name (flow runtime exception)

`FLOW_ELEMENT_ERROR` Message, element type, and element Workflow
name (spark not found)

`FLOW_ELEMENT_ERROR` Message, element type, and element Workflow
name (designer exception)

`FLOW_ELEMENT_ERROR` Message, element type, and element Workflow
name (designer limit exceeded)

`FLOW_ELEMENT_ERROR` Message, element type, and element Workflow
name (designer runtime exception)

`FLOW_ELEMENT_FAULT` Message, element type, and element Workflow
name (fault path taken)

ERROR
and
above

ERROR
and
above

ERROR
and
above

ERROR
and
above

ERROR
and
above

WARNING
and
above

FINER
and
above

```
FLOW_ELEMENT_LIMIT_USAGE

```

Incremented usage toward a limit for Workflow
this element. Each event displays the
usage for one of these limits.


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

```
                                 Email invocations

                                 Future calls

                                 Jobs in queue

                                 Push notifications

```

FINER
and
above

```
FLOW_INTERVIEW_FINISHED_LIMIT_USAGE

```

Usage toward a limit when the Workflow
interview finishes. Each event displays
the usage for one of these limits.

```
SOQL queries

SOQL query rows

SOSL queries

DML statements

DML rows

CPU time in ms

Heap size in bytes

Callouts

Email invocations

Future calls

Jobs in queue

Push notifications

```

`FLOW_INTERVIEW_PAUSED` Interview ID, flow name, and why the Workflow INFO and
user paused above

`FLOW_INTERVIEW_RESUMED` Interview ID and flow name Workflow INFO and
above

FINER
and
above

FINER
and
above

```
FLOW_LOOP_DETAIL

```

Interview ID, index, and value Workflow

The index is the position in the
collection variable for the item that the
loop is operating on.

`FLOW_RULE_DETAIL` Interview ID, rule name, and result Workflow

`FLOW_START_INTERVIEW_BEGIN` Interview ID and flow name Workflow INFO and
above

`FLOW_START_INTERVIEW_END` Interview ID and flow name Workflow INFO and
above

`FLOW_START_INTERVIEWS_BEGIN` Requests Workflow INFO and
above

`FLOW_START_INTERVIEWS_END` Requests Workflow INFO and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`FLOW_START_INTERVIEWS_ERROR` Message, interview ID, and flow name Workflow

ERROR
and
above

FINER
and
above

```
FLOW_START_INTERVIEW_LIMIT_USAGE

```

Usage toward a limit at the interview’s Workflow
start time. Each event displays the
usage for one of these limits.

```
SOQL queries

SOQL query rows

SOSL queries

DML statements

DML rows

CPU time in ms

Heap size in bytes

Callouts

Email invocations

Future calls

Jobs in queue

Push notifications

```

`FLOW_START_SCHEDULED_RECORDS` Message and number of records that Workflow INFO and
the flow runs for above

`FLOW_SUBFLOW_DETAIL` Interview ID, name, definition ID, and Workflow
version ID

`FLOW_VALUE_ASSIGNMENT` Interview ID, key, and value Workflow

`FLOW_WAIT_EVENT_RESUMING_DETAIL` Interview ID, element name, event Workflow
name, and event type

```
FLOW_WAIT_EVENT_WAITING_DETAIL

```

Interview ID, element name, event Workflow
name, event type, and whether
conditions were met

`FLOW_WAIT_RESUMING_DETAIL` Interview ID, element name, and Workflow
persisted interview ID

FINER
and
above

FINER
and
above

FINER
and
above

FINER
and
above

FINER
and
above

FINER
and
above

FINER
and
above

```
FLOW_WAIT_WAITING_DETAIL

```

Interview ID, element name, number Workflow
of events that the element is waiting
for, and persisted interview ID

`HEAP_ALLOCATE` Line number and number of bytes Apex
Code


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`HEAP_DEALLOCATE` Line number and number of bytes Apex
deallocated Code

FINER
and
above

`IDEAS_QUERY_EXECUTE` Line number DB FINEST

```
LIMIT_USAGE_FOR_NS

```

Namespace and these limits: Apex FINEST
Profiling
```
Number of SOQL queries

Number of query rows

Number of SOSL queries

Number of DML statements

Number of DML rows

Number of code statements

Maximum heap size

Number of callouts

Number of Email

Invocations

Number of fields

describes

Number of record type

describes

Number of child

relationships

 describes

Number of picklist

describes

Number of future calls

Number of find similar

calls

Number of System.runAs()

invocations

```


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

```
METHOD_ENTRY

METHOD_EXIT

NAMED_CREDENTIAL_REQUEST

NAMED_CREDENTIAL_RESPONSE

NAMED_CREDENTIAL_RESPONSE_DETAIL

```

Line number, the Lightning Platform Apex FINE and
ID of the class, and method signature Code above
(with namespace, if applicable)

Line number, the Lightning Platform Apex FINE and
ID of the class, and method signature Code above
(with namespace, if applicable)

For constructors, this information is
logged: line number and class name.

Named Credential Id, Named Callout INFO and
Credential Name, Endpoint, Method, above
External Credential Type, Http Header

Authorization, Request Size bytes, and
Retry on 401.

If using an outbound network
connection, these fields are also
logged: Outbound Network
Connection Id, Outbound Network
Connection Name, Outbound Network
Connection Status, Host Type, Host
Region, and Private Connect
Outbound Hourly Data Usage Percent.

Truncated section of the response Callout INFO and
body that’s returned from the above
NamedCredential callout.

Named Credential Id, Named Callout
Credential Name, Status Code,
Response Size bytes, Overall Callout
Time ms, and Connect Time ms.

If using an outbound network
connection, these fields are also

logged: Outbound Network
Connection Id, Outbound Network
Connection Name, and Private
Connect Outbound Hourly Data Usage
Percent.

FINER
and
above

`NBA_NODE_BEGIN` Element name, element type NBA FINE and
above

`NBA_NODE_DETAIL` Element name, element type, message NBA FINE and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`NBA_NODE_END` Element name, element type, message NBA FINE and
above

`NBA_NODE_ERROR` Element name, element type, error NBA
message

ERROR
and
above

`NBA_OFFER_INVALID` Name, ID, reason NBA FINE and
above

`NBA_STRATEGY_BEGIN` Strategy name NBA FINE and
above

`NBA_STRATEGY_END` Strategy name, count of outputs NBA FINE and
above

`NBA_STRATEGY_ERROR` Strategy name, error message NBA

ERROR
and
above

```
POLICY_RULE_DEFINITION_CONDITION_EVALUATION_RESPONSE

```

Condition evaluation response for a Data FINER
policy. Used for identifying conditions Access
that match the policy.

`POLICY_RULE_EVALUATION_REQUEST` Request received for the evaluation of Data FINE
access via the policy. Access

```
POLICY_RULE_EVALUATION_RESPONSE

POLICY_RULE_EVALUATION_SKIPPED

```

Response for the evaluation of access Data FINER
via the policy, including why access is Access
granted or denied.

Object for which the policy evaluation Data FINER
is skipped. If the policy evaluation is Access
skipped, the user is allowed access to
the object.

`POLICY_RULE_EVALUATION_START` Rule being evaluated. Data FINER
Access

```
POP_TRACE_FLAGS

PUSH_NOTIFICATION_INVALID_APP

```

Line number, the Lightning Platform System INFO and
ID of the class or trigger that has its log above
levels set and that is going into scope,

the name of this class or trigger, and
the log level settings that are in effect
after leaving this scope

App namespace, app name Apex ERROR
Code

This event occurs when Apex code is
trying to send a notification to an app

that doesn't exist in the org, or isn’t
push-enabled.


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

```
PUSH_NOTIFICATION_INVALID_CERTIFICATE

PUSH_NOTIFICATION_INVALID_NOTIFICATION

PUSH_NOTIFICATION_NO_DEVICES

PUSH_NOTIFICATION_NOT_ENABLED

PUSH_NOTIFICATION_SENT

PUSH_TRACE_FLAGS

```

App namespace, app name Apex ERROR
Code

This event indicates that the certificate
is invalid. For example, it’s expired.

App namespace, app name, service Apex ERROR
type (Apple or Android GCM), user ID, Code
device, payload (substring), payload
length.

This event occurs when a notification
payload is too long.

App namespace, app name Apex DEBUG
Code

This event occurs when none of the
users we’re trying to send notifications
to have devices registered.

Apex INFO
This event occurs when push
Code
notifications aren’t enabled in your
org.

App namespace, app name, service Apex DEBUG
type (Apple or Android GCM), user ID, Code
device, payload (substring)

This event records that a notification
was accepted for sending. We don’t
guarantee delivery of the notification.

Line number, the Salesforce ID of the System INFO and
class or trigger that has its log levels above
set and that is going out of scope, the

name of this class or trigger, and the
log level settings that are in effect after
entering this scope

`QUERY_MORE_BEGIN` Line number DB INFO and
above

`QUERY_MORE_END` Line number DB INFO and
above

`QUERY_MORE_ITERATIONS` Line number and the number of DB INFO and
`queryMore` iterations above

`SAVEPOINT_ROLLBACK` Line number and Savepoint name DB INFO and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`SAVEPOINT_SET` Line number and Savepoint name DB INFO and
above

```
SLA_END

```

Number of cases, load time, processing Workflow INFO and
time, number of case milestones to above
insert, update, or delete, and new
trigger

`SLA_EVAL_MILESTONE` Milestone ID Workflow INFO and
above

`SLA_NULL_START_DATE` None Workflow INFO and
above

`SLA_PROCESS_CASE` Case ID Workflow INFO and
above

`SOQL_EXECUTE_BEGIN` Line number, number of aggregations, DB INFO and
and query source above

`SOQL_EXECUTE_END` Line number, number of rows, and DB INFO and
duration in milliseconds above

`SOQL_EXECUTE_EXPLAIN` Query Plan details for the executed DB FINEST
SOQL query. To get feedback on query

[performance, see Get Feedback on](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/dome_query_explain.htm)
[Query Performance.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/dome_query_explain.htm)

`SOSL_EXECUTE_BEGIN` Line number and query source DB INFO and
above

`SOSL_EXECUTE_END` Line number, number of rows, and DB INFO and
duration in milliseconds above

```
STACK_FRAME_VARIABLE_LIST

```

Frame number and variable list of the Apex FINE and
form: _`Variable number`_ | Profiling above
_`Value`_ . For example:

```
var1:50

var2:'Hello World'

```

`STATEMENT_EXECUTE` Line number Apex
Code

FINER
and
above

```
STATIC_VARIABLE_LIST

```

Variable list of the form: _`Variable`_ Apex FINE and
_`number`_ | _`Value`_ . For example: Profiling above

```
var1:50

var2:'Hello World'

```


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

```
SYSTEM_CONSTRUCTOR_ENTRY

SYSTEM_CONSTRUCTOR_EXIT

```

Line number and the string System FINE and
`<init>()` with the types of above
parameters, if any, between the
parentheses

Line number and the string System FINE and
`<init>()` with the types of above
parameters, if any, between the
parentheses

`SYSTEM_METHOD_ENTRY` Line number and method signature System FINE and
above

`SYSTEM_METHOD_EXIT` Line number and method signature System FINE and
above

`SYSTEM_MODE_ENTER` Mode name System INFO and
above

`SYSTEM_MODE_EXIT` Mode name System INFO and
above

`TESTING_LIMITS` None Apex INFO and
Profiling above

`TOTAL_EMAIL_RECIPIENTS_QUEUED` Number of emails sent Apex FINE and
Profiling above

`USER_DEBUG` Line number, logging level, and Apex DEBUG
user-supplied string Code and

above by
default. If
the user
sets the
log level
for the

```
                                               System.Debug
```

method,
the event
is logged
at that
level
instead.

`USER_INFO` Line number, user ID, username, user Apex
timezone, and user timezone in GMT Code

ERROR
and
above

`VALIDATION_ERROR` Error message Validation INFO and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`VALIDATION_FAIL` None Validation INFO and
above

`VALIDATION_FORMULA` Formula source and values Validation INFO and
above

`VALIDATION_PASS` None Validation INFO and
above

`VALIDATION_RULE` Rule name Validation INFO and
above

```
VARIABLE_ASSIGNMENT

VARIABLE_SCOPE_BEGIN

```

Line number, variable name (including Apex FINEST
the variable’s namespace, if Code
applicable), a string representation of

the variable’s value, and the variable’s
address

Line number, variable name (including Apex FINEST
the variable’s namespace, if Code
applicable), type, a value that indicates

whether the variable can be
referenced, and a value that indicates
whether the variable is static

`VARIABLE_SCOPE_END` None Apex FINEST
Code

```
VF_APEX_CALL_START

VF_APEX_CALL_END

```

Element name, method name, return Apex INFO and
type, and the typeRef for the Code above
Visualforce controller (for example,
`YourApexClass` )

Element name, method name, return Apex INFO and
type, and the typeRef for the Code above
Visualforce controller (for example,
`YourApexClass` )

`VF_DESERIALIZE_VIEWSTATE_BEGIN` View state ID Visualforce INFO and
above

`VF_DESERIALIZE_VIEWSTATE_END` None Visualforce INFO and
above

`VF_EVALUATE_FORMULA_BEGIN` View state ID and formula Visualforce

`VF_EVALUATE_FORMULA_END` None Visualforce


FINER
and
above

FINER
and
above

Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`VF_PAGE_MESSAGE` Message text Apex INFO and
Code above

`VF_SERIALIZE_VIEWSTATE_BEGIN` View state ID Visualforce INFO and
above

`VF_SERIALIZE_VIEWSTATE_END` None Visualforce INFO and
above

`WF_ACTION` Action description Workflow INFO and
above

`WF_ACTION_TASK` Task subject, action ID, rule name, rule Workflow INFO and
ID, owner, and due date above

`WF_ACTIONS_END` Summary of actions performed Workflow INFO and
above

```
WF_APPROVAL

```

Transition type, `EntityName:` Workflow INFO and
`NameField Id`, and process node above
name

`WF_APPROVAL_REMOVE` `EntityName: NameField Id` Workflow INFO and
above

`WF_APPROVAL_SUBMIT` `EntityName: NameField Id` Workflow INFO and
above

`WF_APPROVAL_SUBMITTER` Submitter ID, submitter full name, and Workflow INFO and
error message above

`WF_ASSIGN` Owner and assignee template ID Workflow INFO and
above

```
WF_CRITERIA_BEGIN

```

`EntityName: NameField Id`, Workflow INFO and
rule name, rule ID, and (if rule respects above
trigger types) trigger type and
recursive count

`WF_CRITERIA_END` Boolean value indicating success (true Workflow INFO and
or false) above

`WF_EMAIL_ALERT` Action ID, rule name, and rule ID Workflow INFO and
above

`WF_EMAIL_SENT` Email template ID, recipients, and CC Workflow INFO and
emails above

`WF_ENQUEUE_ACTIONS` Summary of actions enqueued Workflow INFO and
above

`WF_ESCALATION_ACTION` Case ID and escalation date Workflow INFO and
above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`WF_ESCALATION_RULE` None Workflow INFO and
above

```
WF_EVAL_ENTRY_CRITERIA

```

Process name, email template ID, and Workflow INFO and
Boolean value indicating result (true above
or false)

`WF_FIELD_UPDATE` `EntityName: NameField Id` Workflow INFO and
and the object or field name above

`WF_FLOW_ACTION_BEGIN` ID of flow trigger Workflow INFO and
above

```
WF_FLOW_ACTION_DETAIL

```

ID of flow trigger, object type and ID Workflow FINE and
of record whose creation or update above
caused the workflow rule to fire, name

and ID of workflow rule, and the
names and values of flow variables

`WF_FLOW_ACTION_END` ID of flow trigger Workflow INFO and
above

ERROR
and
above

ERROR
and
above

```
WF_FLOW_ACTION_ERROR

```

ID of flow trigger, ID of flow definition, Workflow
ID of flow version, and flow error
message

`WF_FLOW_ACTION_ERROR_DETAIL` Detailed flow error message Workflow

`WF_FORMULA` Formula source and values Workflow INFO and
above

`WF_HARD_REJECT` None Workflow INFO and
above

`WF_NEXT_APPROVER` Owner, next owner type, and field Workflow INFO and
above

`WF_NO_PROCESS_FOUND` None Workflow INFO and
above

`WF_OUTBOUND_MSG` `EntityName: NameField Id`, Workflow INFO and
action ID, rule name, and rule ID above

`WF_PROCESS_FOUND` Process definition ID and process label Workflow INFO and
above

`WF_PROCESS_NODE` Process name Workflow INFO and
above

`WF_REASSIGN_RECORD` `EntityName: NameField Id` Workflow INFO and
and owner above


Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`WF_RESPONSE_NOTIFY` Notifier name, notifier email, notifier Workflow INFO and
template ID, and reply-to email above

`WF_RULE_ENTRY_ORDER` Integer indicating order Workflow INFO and
above

`WF_RULE_EVAL_BEGIN` Rule type Workflow INFO and
above

`WF_RULE_EVAL_END` None Workflow INFO and
above

`WF_RULE_EVAL_VALUE` Value Workflow INFO and
above

`WF_RULE_FILTER` Filter criteria Workflow INFO and
above

`WF_RULE_INVOCATION` `EntityName: NameField Id` Workflow INFO and
above

`WF_RULE_NOT_EVALUATED` None Workflow INFO and
above

`WF_SOFT_REJECT` Process name Workflow INFO and
above

`WF_SPOOL_ACTION_BEGIN` Node type Workflow INFO and
above

```
WF_TIME_TRIGGER

```

`EntityName: NameField Id`, Workflow INFO and
time action, time action container, and above
evaluation Datetime

`WF_TIME_TRIGGERS_BEGIN` None Workflow INFO and
above

FINER
and
above

```
XDS_DETAIL

```

(External object access via cross-org
and OData adapters for Salesforce
Connect)

```
XDS_RESPONSE

```

(External object access via cross-org
and OData adapters for Salesforce
Connect)

For OData adapters, the POST body Callout
and the name and evaluated formula
for custom HTTP headers

External data source, external object, Callout INFO and
request details, number of returned above
records, and system usage

`XDS_RESPONSE_DETAIL` Truncated response from the external Callout
system, including returned records

(External object access via cross-org
and OData adapters for Salesforce
Connect)


FINER
and
above

##### Apex Developer Guide Debugging Apex

**Event Name** **Fields or Information Logged** **Category** **Level**
**with Event** **Logged** **Logged**

`XDS_RESPONSE_ERROR` Error message Callout

(External object access via cross-org
and OData adapters for Salesforce
Connect)

SEE ALSO:

_Salesforce Help_ [: Debug Log Levels](https://help.salesforce.com/HTViewHelpDoc?id=code_setting_debug_log_levels.htm&language=en_US)

_Salesforce Help_ [: Partition Your Data with Enhanced Security Data Spaces](https://help.salesforce.com/s/articleView?id=data.c360_a_data_spaces_secure_data.htm&type=5&language=en_US)

_Salesforce Help_ [: User Access Policies](https://help.salesforce.com/s/articleView?id=platform.perm_user_access_policies.htm&type=5&language=en_US)

##### Debugging Apex API Calls

ERROR
and
above

All API calls that invoke Apex support a debug facility that allows access to detailed information about the execution of the code, including
any calls to `System.debug()` . The `categories` field of a SOAP input header called `DebuggingHeader` allows you to set
the logging granularity according to the levels outlined in this table.

**Element Name** **Type** **Description**

`category` LogCategory Specify the type of information returned in the debug log. Valid values are:

**•** `Db`

**•** `Workflow`

**•** `Validation`

**•** `Callout`

**•** `Apex_code`

**•** `Apex_profiling`

**•** `Visualforce`

**•** `System`

**•** `All`

`level` LogCategoryLevel

Specifies the level of detail returned in the debug log.

Valid log levels are (listed from lowest to highest):

**•** `NONE`

**•** `ERROR`

**•** `WARN`

**•** `INFO`

**•** `DEBUG`

**•** `FINE`

**•** `FINER`

**•** `FINEST`


Apex Developer Guide Debugging Apex

In addition, the following log levels are still supported as part of the `DebuggingHeader` for backwards compatibility.

**Log Level** **Description**

`NONE` Does not include any log messages.

`DEBUGONLY` Includes lower-level messages, and messages generated by calls to the `System.debug`
method.

`DB` Includes log messages generated by calls to the `System.debug` method, and every data
manipulation language (DML) statement or inline SOQL or SOSL query.

`PROFILE` Includes log messages generated by calls to the `System.debug` method, every DML
statement or inline SOQL or SOSL query, and the entrance and exit of every user-defined method.

In addition, the end of the debug log contains overall profiling information for the portions of
the request that used the most resources. This profiling information is presented in terms of
SOQL and SOSL statements, DML operations, and Apex method invocations. These three sections
list the locations in the code that consumed the most time, in descending order of total
cumulative time. Also listed is the number of times the categories executed.

```
CALLOUT

```

Includes the request-response XML that the server is sending and receiving from an external
web service. Useful when debugging issues related to using Lightning Platform web service
API calls or troubleshooting user access to external objects via Salesforce Connect.

`DETAIL` Includes all messages generated by the `PROFILE` level and the following.

**•** Variable declaration statements

**•** Start of loop executions

**•** All loop controls, such as break and continue

**•** Thrown exceptions *

**•** Static and class initialization code *

**•** Any changes in the `with sharing` context

The corresponding output header, `DebuggingInfo`, contains the resulting debug log. For more information, see `[DebuggingHeader](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_header_debuggingheader.htm)`
in the _SOAP API Developer Guide_ .

##### Debug Log Order of Precedence

Which events are logged depends on various factors. These factors include your trace flags, the default logging levels, your API header,
user-based system log enablement, and the log levels set by your entry points.

The order of precedence for debug log levels is:

**1.** Trace flags override all other logging logic. The Developer Console sets a trace flag when it loads, and that trace flag remains in effect
until it expires. You can set trace flags in the Developer Console or in Setup or by using the `TraceFlag` and `DebugLevel`
Tooling API objects.

Note: Setting class and trigger trace flags doesn’t cause logs to be generated or saved. Class and trigger trace flags override
other logging levels, including logging levels set by user trace flags, but they don’t cause logging to occur. If logging is enabled
when classes or triggers execute, logs are generated at the time of execution.


Apex Developer Guide Debugging Apex

**2.** If you don’t have active trace flags, synchronous and asynchronous Apex tests execute with the default logging levels. Default logging
levels are:

**DB**
INFO

**APEX_CODE**
DEBUG

**APEX_PROFILING**
INFO

**WORKFLOW**
INFO

**VALIDATION**
INFO

**CALLOUT**
INFO

**VISUALFORCE**
INFO

**SYSTEM**
DEBUG

**3.** If no relevant trace flags are active, and no tests are running, your API header sets your logging levels. API requests that are sent
without debugging headers generate transient logs—logs that aren’t saved—unless another logging rule is in effect.

**4.** If your entry point sets a log level, that log level is used. For example, Visualforce requests can include a debugging parameter that
sets log levels.

If none of these cases apply, logs aren’t generated or persisted.

#### Exceptions in Apex Exceptions note errors and other events that disrupt the normal flow of code execution. throw statements are used to generate

exceptions, while `try`, `catch`, and `finally` statements are used to gracefully recover from exceptions.

There are many ways to handle errors in your code, including using assertions like `System.assert` calls, or returning error codes
or Boolean values, so why use exceptions? The advantage of using exceptions is that they simplify error handling. Exceptions bubble up
from the called method to the caller, as many levels as necessary, until a `catch` statement is found to handle the error. This bubbling
up relieves you from writing error-handling code in each of your methods. Also, by using `finally` statements, you have one place
to recover from exceptions, like resetting variables and deleting data.

What Happens When an Exception Occurs?

When an exception occurs, code execution halts. Any DML operations that were processed before the exception are rolled back and
aren’t committed to the database. Exceptions get logged in debug logs. For unhandled exceptions (exceptions that the code doesn’t
catch) Salesforce sends an email that includes the exception information. The end user sees an error message in the Salesforce user
interface.


Apex Developer Guide Debugging Apex

Unhandled Exception Emails

Tip: Take advantage of free-tier access to Event Monitoring, and track unhandled exceptions in Apex code execution instead of
[relying only on unhandled exception emails. Troubleshoot your Apex code by analyzing the information captured in the event](https://help.salesforce.com/s/articleView?id=xcloud.real_time_em_elf_browser.htm&type=5&language=en_US)
[log files for the Apex Unexpected Exception event type.](https://help.salesforce.com/s/articleView?id=xcloud.real_time_em_elf_browser.htm&type=5&language=en_US)

When unhandled Apex exceptions occur, emails sent contain the Apex stack trace, exception message, customer’s org and user ID, org
name, and My Domain name. No other data is returned with the report. Unhandled exception emails are sent by default to the developer
specified in the `LastModifiedBy` field on the failing class or trigger. In addition, you can have emails sent to users of your Salesforce
org and to arbitrary email addresses. These email recipients can also receive process or flow error emails. To set up these email notifications,
from Setup, enter _`Apex Exception Email`_ in the `Quick Find` box, then select **Apex Exception Email** . The entered email
addresses then apply to all managed packages in the customer's org. You can also configure Apex exception emails using Tooling API
object ApexEmailNotification.

Note:

**•** If duplicate exceptions occur in Apex code that runs synchronously or asynchronously, subsequent exception emails are
suppressed and only the first email is sent. This email suppression prevents flooding of the developer’s inbox with emails about
the same error.

**•** Emails aren’t sent for exceptions encountered with anonymous Apex executions or with Apex methods accessed by Aura
[components and Lightning web components via the @AuraEnabled annotation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_annotation_AuraEnabled.htm)

**•** Apex exception emails are limited to 10 emails per hour, per application server. Because this limit isn’t on a per-org basis, email
delivery to a particular org can be unreliable.

Unhandled Exceptions in the User Interface

If an end user runs into an exception that occurred in Apex code while using the standard user interface, an error message appears. The
error message includes text similar to the notification shown here.

Exception Statements

Exception Handling Example
Learn how exception handling works in Apex.

Built-In Exceptions and Common Methods

Catching Different Exception Types


Apex Developer Guide Debugging Apex

Create Custom Exceptions

##### Exception Statements

Apex uses _exceptions_ to note errors and other events that disrupt the normal flow of code execution. `throw` statements can be used
to generate exceptions, while `try`, `catch`, and `finally` can be used to gracefully recover from an exception.

Throw Statements

A `throw` statement allows you to signal that an error has occurred. To throw an exception, use the `throw` statement and provide it
with an exception object to provide information about the specific error. For example:

```
   throw exceptionObject ;

```

Try-Catch-Finally Statements

The `try`, `catch`, and `finally` statements can be used to gracefully recover from a thrown exception:

**•** The `try` statement identifies a block of code in which an exception can occur.

**•** The `catch` statement identifies a block of code that can handle a particular type of exception. A single `try` statement can have
zero or more associated `catch` statements. Each `catch` statement must have a unique exception type. Also, once a particular
exception type is caught in one `catch` block, the remaining `catch` blocks, if any, aren’t executed.

**•** The `finally` statement identifies a block of code that is guaranteed to execute and allows you to clean up your code. A single

`try` statement can have up to one associated `finally` statement. Code in the `finally` block always executes regardless of
whether an exception was thrown or the type of exception that was thrown. Because the `finally` block always executes, use it
for cleanup code, such as for freeing up resources.

Syntax

The syntax of the `try`, `catch`, and `finally` statements is as follows.

```
   try {

     // Try block

    code_block

   } catch ( exceptionType variableName ) {

     // Initial catch block.

     // At least the catch block or the finally block must be present.

    code_block

   } catch (Exception e) {

     // Optional additional catch statement for other exception types.

     // Note that the general exception type, 'Exception',

     // must be the last catch block when it is used.

    code_block

   } finally {

     // Finally block.

     // At least the catch block or the finally block must be present.

    code_block

   }

```


Apex Developer Guide Debugging Apex

At least a `catch` block or a `finally` block must be present with a `try` block. The following is the syntax of a try-catch block.

```
   try {

    code_block

   } catch ( exceptionType variableName ) {

    code_block

   }

   // Optional additional catch blocks

```

The following is the syntax of a try-finally block.

```
   try {

    code_block

   } finally {

    code_block

   }

```

This is a skeletal example of a try-catch-finally block.

```
   try {

      // Perform some operation that

      // might cause an exception.

   } catch(Exception e) {

      // Generic exception handling code here.

   } finally {

      // Perform some clean up.

   }

```

Exceptions that Can’t be Caught

Some special types of built-in exceptions can’t be caught. Those exceptions are associated with critical situations in the Lightning
Platform. These situations require the abortion of code execution and don’t allow for execution to resume through exception handling.
One such exception is the limit exception ( `System.LimitException` ) that the runtime throws if a governor limit such as heap
size or CPU time has been exceeded, when the maximum number of SOQL queries issued has been exceeded, an attempt is made to
retrieve more than the maximum number of records, and so on. Other examples are exceptions thrown when assertion statements fail
(through `System.assert` methods) or license exceptions.

When exceptions are uncatchable, `catch` blocks, as well as `finally` blocks if any, aren’t executed.

Versioned Behavior Changes

In API version 41.0 and later, unreachable statements in your code will cause compilation errors. For example, the following code block
generates a compile time error in API version 41.0 and later. The third statement can never be reached because the previous statement
throws an unconditional exception.

```
   Boolean x = true;

   throw new NullPointerException();

   x = false;

##### Exception Handling Example

```

Learn how exception handling works in Apex.


Apex Developer Guide Debugging Apex

To see an exception in action, execute some code that causes a DML exception to be thrown. Execute the following in the Developer
Console:

```
   Merchandise__c m = new Merchandise__c();

   insert m;

```

The `insert` DML statement in the example causes a DmlException because we’re inserting a merchandise item without setting any
of its required fields. This is the exception error that you see in the debug log.

```
   System.DmlException: Insert failed. First exception on row 0; first error:

   REQUIRED_FIELD_MISSING, Required fields are missing: [Description, Price, Total

   Inventory]: [Description, Price, Total Inventory]

```

Next, execute this snippet in the Developer Console. It’s based on the previous example but includes a try-catch block.

```
   try {

      Merchandise__c m = new Merchandise__c();

      insert m;

   } catch(DmlException e) {

      System.debug('The following exception has occurred: ' + e.getMessage());

   }

```

Notice that the request status in the Developer Console now reports success. This is because the code handles the exception.

Any statements in the try block occurring after the exception are skipped and aren’t executed. For example, if you add a statement after

`insert m;`, this statement won’t be executed. Execute the following:

```
   try {

      Merchandise__c m = new Merchandise__c();

      insert m;

      // This doesn't execute since insert causes an exception

      System.debug('Statement after insert.');

   } catch(DmlException e) {

      System.debug('The following exception has occurred: ' + e.getMessage());

   }

```

In the new debug log entry, notice that you don’t see a debug message of `Statement after insert` . This is because this debug
statement occurs after the exception caused by the insertion and never gets executed. To continue the execution of code statements
after an exception happens, place the statement after the try-catch block. Execute this modified code snippet and notice that the debug
log now has a debug message of `Statement after insert` .

```
   try {

      Merchandise__c m = new Merchandise__c();

      insert m;

   } catch(DmlException e) {

      System.debug('The following exception has occurred: ' + e.getMessage());

   }

   // This will get executed

   System.debug('Statement after insert.');

```

Alternatively, you can include additional try-catch blocks. This code snippet has the `System.debug` statement inside a second
try-catch block. Execute it to see that you get the same result as before.

```
   try {

      Merchandise__c m = new Merchandise__c();

      insert m;

   } catch(DmlException e) {

```


Apex Developer Guide Debugging Apex

```
      System.debug('The following exception has occurred: ' + e.getMessage());

   }

   try {

      System.debug('Statement after insert.');

      // Insert other records

   }

   catch (Exception e) {

      // Handle this exception here

   }

```

The finally block always executes regardless of what exception is thrown, and even if no exception is thrown. Let’s see it used in action.
Execute the following:

```
   // Declare the variable outside the try-catch block

   // so that it will be in scope for all blocks.

   XmlStreamWriter w = null;

   try {

      w = new XmlStreamWriter();

      w.writeStartDocument(null, '1.0');

      w.writeStartElement(null, 'book', null);

      w.writeCharacters('This is my book');

      w.writeEndElement();

      w.writeEndDocument();

      // Perform some other operations

      String s;

      // This causes an exception because

      // the string hasn't been assigned a value.

      Integer i = s.length();

   } catch(Exception e) {

      System.debug('An exception occurred: ' + e.getMessage());

   } finally {

      // This gets executed after the exception is handled

      System.debug('Closing the stream writer in the finally block.');

      // Close the stream writer

      w.close();

   }

```

The previous code snippet creates an XML stream writer and adds some XML elements. Next, an exception occurs due to accessing the
null String variable `s` . The catch block handles this exception. Then the finally block executes. It writes a debug message and closes the
stream writer, which frees any associated resources. Check the debug output in the debug log. You’ll see the debug message `Closing`
`the stream writer in the finally block.` after the exception error. This tells you that the finally block executed
after the exception was caught.

SEE ALSO:

Create Custom Exceptions

_Salesforce Developers Blog_ [: Error Handling Best Practices for Lightning and Apex](https://developer.salesforce.com/blogs/2017/09/error-handling-best-practices-lightning-apex)


Apex Developer Guide Debugging Apex

##### Built-In Exceptions and Common Methods

Apex provides a number of built-in exception types that the runtime engine throws if errors are encountered during execution. You've
seen the DmlException in the previous example. Here is a sample of some other built-in exceptions. For a complete list of built-in
[exception types, see Exception Class and Built-In Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

**DmlException**
Any problem with a DML statement, such as an `insert` statement missing a required field on a record.

This example makes use of DmlException. The `insert` DML statement in this example causes a DmlException because it’s inserting
a merchandise item without setting any of its required fields. This exception is caught in the `catch` block and the exception
message is written to the debug log using the `System.debug` statement.

```
     try {

       Merchandise__c m = new Merchandise__c();

       insert m;

     } catch(DmlException e) {

       System.debug('The following exception has occurred: ' + e.getMessage());

     }

```

**ListException**
Any problem with a list, such as attempting to access an index that is out of bounds.

This example creates a list and adds one element to it. Then, an attempt is made to access two elements, one at index 0, which
exists, and one at index 1, which causes a ListException to be thrown because no element exists at this index. This exception is
caught in the catch block. The `System.debug` statement in the catch block writes the following to the debug log: `The`
`following exception has occurred: List index out of bounds: 1` .

```
     try {

       List<Integer> li = new List<Integer>();

       li.add(15);

       // This list contains only one element,

       // but we're attempting to access the second element

       // from this zero-based list.

       Integer i1 = li[0];

       Integer i2 = li[1]; // Causes a ListException

     } catch(ListException le) {

       System.debug('The following exception has occurred: ' + le.getMessage());

     }

```

**NullPointerException**
Any problem with dereferencing a `null` variable.

This example creates a String variable named `s` but we don’t initialize it to a value, hence, it is null. Calling the `contains` method
on our null variable causes a NullPointerException. The exception is caught in our catch block and this is what is written to the debug
log: `The following exception has occurred: Attempt to de-reference a null object` .

```
     try {

       String s;

       Boolean b = s.contains('abc'); // Causes a NullPointerException

     } catch(NullPointerException npe) {

       System.debug('The following exception has occurred: ' + npe.getMessage());

     }

```

**QueryException**
Any problem with SOQL queries, such as assigning a query that returns no records or more than one record to a singleton sObject
variable.


Apex Developer Guide Debugging Apex

The second SOQL query in this example causes a QueryException. The example assigns a Merchandise object to what is returned
from the query. Note the use of `LIMIT 1` in the query. This ensures that at most one object is returned from the database so we
can assign it to a single object and not a list. However, in this case, we don’t have a Merchandise named XYZ, so nothing is returned,
and the attempt to assign the return value to a single object results in a QueryException. The exception is caught in our catch block
and this is what you’ll see in the debug log: `The following exception has occurred: List has no rows`
`for assignment to SObject` .

```
     try {

       // This statement doesn't cause an exception, even though

       // we don't have a merchandise with name='XYZ'.

       // The list will just be empty.

       List<Merchandise__c> lm = [SELECT Name FROM Merchandise__c WHERE Name = 'XYZ'];

       // lm.size() is 0

       System.debug(lm.size());

       // However, this statement causes a QueryException because

       // we're assiging the return value to a Merchandise__c object

       // but no Merchandise is returned.

       Merchandise__c m = [SELECT Name FROM Merchandise__c WHERE Name = 'XYZ' LIMIT 1];

     } catch(QueryException qe) {

       System.debug('The following exception has occurred: ' + qe.getMessage());

     }

```

**SObjectException**
Any problem with sObject records, such as attempting to change a field in an `update` statement that can only be changed during

`insert` .

This example results in an SObjectException in the try block, which is caught in the catch block. The example queries an invoice
statement and selects only its Name field. It then attempts to get the Description__c field on the queried sObject, which isn’t available
because it isn’t in the list of fields queried in the SELECT statement. This results in an SObjectException. This exception is caught in
our catch block and this is what you’ll see in the debug log: `The following exception has occurred: SObject`

```
    row was retrieved via SOQL without querying the requested field:
```

`Invoice_Statement__c.Description__c` .

```
     try {

       Invoice_Statement__c inv = new Invoice_Statement__c(

          Description__c='New Invoice');

       insert inv;

       // Query the invoice we just inserted

       Invoice_Statement__c v = [SELECT Name FROM Invoice_Statement__c WHERE Id = :inv.Id];

       // Causes an SObjectException because we didn't retrieve

       // the Description__c field.

       String s = v.Description__c;

     } catch(SObjectException se) {

       System.debug('The following exception has occurred: ' + se.getMessage());

     }

```

Common Exception Methods

You can use common exception methods to get more information about an exception, such as the exception error message or the stack
trace. The previous example calls the `getMessage` method, which returns the error message associated with the exception. There
are other exception methods that are also available. Here are descriptions of some useful methods:


Apex Developer Guide Debugging Apex

**•** `getCause` : Returns the cause of the exception as an exception object.

**•** `getLineNumber` : Returns the line number from where the exception was thrown.

**•** `getMessage` : Returns the error message that displays for the user.

**•** `getStackTraceString` : Returns the stack trace of a thrown exception as a string.

**•** `getTypeName` : Returns the type of exception, such as DmlException, ListException, MathException, and so on.

**Example**

To find out what some of the common methods return, try running this example.

```
   try {

      Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];

      // Causes an SObjectException because we didn't retrieve

      // the Total_Inventory__c field.

      Double inventory = m.Total_Inventory__c;

   } catch(Exception e) {

      System.debug('Exception type caught: ' + e.getTypeName());

      System.debug('Message: ' + e.getMessage());

      System.debug('Cause: ' + e.getCause()); // returns null

      System.debug('Line number: ' + e.getLineNumber());

      System.debug('Stack trace: ' + e.getStackTraceString());

   }

```

The output of all `System.debug` statements looks like the following:

```
   17:38:04:149 USER_DEBUG [7]|DEBUG|Exception type caught: System.SObjectException

   17:38:04:149 USER_DEBUG [8]|DEBUG|Message: SObject row was retrieved via SOQL without

   querying the requested field: Merchandise__c.Total_Inventory__c

   17:38:04:150 USER_DEBUG [9]|DEBUG|Cause: null

   17:38:04:150 USER_DEBUG [10]|DEBUG|Line number: 5

   17:38:04:150 USER_DEBUG [11]|DEBUG|Stack trace: AnonymousBlock: line 5, column 1

```

The catch statement argument type is the generic Exception type. It caught the more specific SObjectException. You can verify that this
is so by inspecting the return value of `e.getTypeName()` in the debug output. The output also contains other properties of the
SObjectException, like the error message, the line number where the exception occurred, and the stack trace. You might be wondering
why `getCause` returned null. This is because in our sample there was no previous exception (inner exception) that caused this
exception. In Create Custom Exceptions, you’ll get to see an example where the return value of `getCause` is an actual exception.

More Exception Methods

Some exception types, such as DmlException, have specific exception methods that apply to only them and aren’t common to other
exception types:

**•** `getDmlFieldNames(Index of the failed record)` : Returns the names of the fields that caused the error for the
specified failed record.

**•** `getDmlId(Index of the failed record)` : Returns the ID of the failed record that caused the error for the specified
failed record.

**•** `getDmlMessage(Index of the failed record)` : Returns the error message for the specified failed record.

**•** `getNumDml` : Returns the number of failed records.

**Example**


Apex Developer Guide Debugging Apex

This snippet makes use of the DmlException methods to get more information about the exceptions returned when inserting a list of
Merchandise objects. The list of items to insert contains three items, the last two of which don’t have required fields and cause exceptions.

```
   Merchandise__c m1 = new Merchandise__c(

      Name='Coffeemaker',

      Description__c='Kitchenware',

      Price__c=25,

      Total_Inventory__c=1000);

   // Missing the Price and Total_Inventory fields

   Merchandise__c m2 = new Merchandise__c(

      Name='Coffeemaker B',

      Description__c='Kitchenware');

   // Missing all required fields

   Merchandise__c m3 = new Merchandise__c();

   Merchandise__c[] mList = new List<Merchandise__c>();

   mList.add(m1);

   mList.add(m2);

   mList.add(m3);

   try {

      insert mList;

   } catch (DmlException de) {

      Integer numErrors = de.getNumDml();

      System.debug('getNumDml=' + numErrors);

      for(Integer i=0;i<numErrors;i++) {

        System.debug('getDmlFieldNames=' + de.getDmlFieldNames(i));

        System.debug('getDmlMessage=' + de.getDmlMessage(i));

      }

   }

```

Note how the sample above didn’t include all the initial code in the try block. Only the portion of the code that could generate an
exception is wrapped inside a `try` block, in this case the `insert` statement could return a DML exception in case the input data is
not valid. The exception resulting from the `insert` operation is caught by the `catch` block that follows it. After executing this
sample, you’ll see an output of `System.debug` statements similar to the following:

```
   14:01:24:939 USER_DEBUG [20]|DEBUG|getNumDml=2

   14:01:24:941 USER_DEBUG [23]|DEBUG|getDmlFieldNames=(Price, Total Inventory)

   14:01:24:941 USER_DEBUG [24]|DEBUG|getDmlMessage=Required fields are missing: [Price,

   Total Inventory]

   14:01:24:942 USER_DEBUG [23]|DEBUG|getDmlFieldNames=(Description, Price, Total Inventory)

   14:01:24:942 USER_DEBUG [24]|DEBUG|getDmlMessage=Required fields are missing:

   [Description, Price, Total Inventory]

```

The number of DML failures is correctly reported as two since two items in our list fail insertion. Also, the field names that caused the
failure, and the error message for each failed record is written to the output.


Apex Developer Guide Debugging Apex

##### Catching Different Exception Types

In the previous examples, we used the specific exception type in the catch block. We could have also just caught the generic Exception
type in all examples, which catches all exception types. For example, try running this example that throws an SObjectException and has
a catch statement with an argument type of Exception. The SObjectException gets caught in the catch block.

```
   try {

      Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];

      // Causes an SObjectException because we didn't retrieve

      // the Total_Inventory__c field.

      Double inventory = m.Total_Inventory__c;

   } catch(Exception e) {

      System.debug('The following exception has occurred: ' + e.getMessage());

   }

```

Alternatively, you can have several catch blocks—a catch block for each exception type, and a final catch block that catches the generic
Exception type. Look at this example. Notice that it has three catch blocks.

```
   try {

      Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];

      // Causes an SObjectException because we didn't retrieve

      // the Total_Inventory__c field.

      Double inventory = m.Total_Inventory__c;

   } catch(DmlException e) {

      System.debug('DmlException caught: ' + e.getMessage());

   } catch(SObjectException e) {

      System.debug('SObjectException caught: ' + e.getMessage());

   } catch(Exception e) {

      System.debug('Exception caught: ' + e.getMessage());

   }

```

Remember that only one catch block gets executed and the remaining ones are bypassed. This example is similar to the previous one,
except that it has a few more catch blocks. When you run this snippet, an SObjectException is thrown on this line: `Double inventory`
`= m.Total_Inventory__c;` . Every catch block is examined in the order specified to find a match between the thrown exception
and the exception type specified in the catch block argument:

**1.** The first catch block argument is of type DmlException, which doesn’t match the thrown exception (SObjectException.)

**2.** The second catch block argument is of type SObjectException, which matches our exception, so this block gets executed and the
following message is written to the debug log: `SObjectException caught: SObject row was retrieved via`
`SOQL without querying the requested field: Merchandise__c.Total_Inventory__c` .

**3.** The last catch block is ignored since one catch block has already executed.

The last catch block is handy because it catches any exception type, and so catches any exception that was not caught in the previous
catch blocks. Suppose we modified the code above to cause a NullPointerException to be thrown, this exception gets caught in the last
catch block. Execute this modified example. You’ll see the following debug message: `Exception caught: Attempt to`
`de-reference a null object` .

```
   try {

      String s;

      Boolean b = s.contains('abc'); // Causes a NullPointerException

   } catch(DmlException e) {

      System.debug('DmlException caught: ' + e.getMessage());

   } catch(SObjectException e) {

      System.debug('SObjectException caught: ' + e.getMessage());

   } catch(Exception e) {

```


Apex Developer Guide Debugging Apex

```
      System.debug('Exception caught: ' + e.getMessage());

   }

##### Create Custom Exceptions

```

Custom exceptions enable you to specify detailed error messages and have more custom error handling in your catch blocks.

Exceptions can be top-level classes, that is, they can have member variables, methods and constructors, they can implement interfaces,
and so on.

To create your custom exception class, extend the built-in `Exception` class and make sure your class name ends with the word
`Exception`, such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class `Exception`,
and therefore, inherits all common Exception methods.

This example defines a custom exception called `MyException` .

```
   public class MyException extends Exception {}

```

Like Java classes, user-defined exception types can form an inheritance tree, and catch blocks can catch any object in this inheritance
tree. For example:

```
   public class ExceptionExample {

      public virtual class BaseException extends Exception {}

      public class OtherException extends BaseException {}

      public static void testExtendedException() {

        try {

           Integer i=0;

           // Your code here

           if (i < 5) throw new OtherException('This is bad');

        } catch (BaseException e) {

           // This catches the OtherException

           System.debug(e.getMessage());

        }

      }

   }

```

Here are some ways you can create your exceptions objects, which you can then throw.

You can construct exceptions:

**•** With no arguments:

```
     new MyException();

```

**•** With a single String argument that specifies the error message:

```
     new MyException('This is bad');

```

**•** With a single Exception argument that specifies the cause and that displays in any stack trace:

```
     new MyException(e);

```

**•** With both a String error message and a chained exception cause that displays in any stack trace:

```
     new MyException('This is bad', e);

```


Apex Developer Guide Debugging Apex

Rethrowing Exceptions and Inner Exceptions

After catching an exception in a catch block, you have the option to rethrow the caught exception variable. This is useful if your method
is called by another method and you want to delegate the handling of the exception to the caller method. You can rethrow the caught
exception as an inner exception in your custom exception and have the main method catch your custom exception type.

The following example shows how to rethrow an exception as an inner exception. The example defines two custom exceptions,
`My1Exception` and `My2Exception`, and generates a stack trace with information about both.

```
   // Define two custom exceptions

   public class My1Exception extends Exception {}

   public class My2Exception extends Exception {}

   try {

      // Throw first exception

      throw new My1Exception('First exception');

   } catch (My1Exception e) {

      // Throw second exception with the first

      // exception variable as the inner exception

      throw new My2Exception('Thrown with inner exception', e);

   }

```

This is how the stack trace looks like resulting from running the code above:

```
   15:52:21:073 EXCEPTION_THROWN [7]|My1Exception: First exception

   15:52:21:077 EXCEPTION_THROWN [11]|My2Exception: Throw with inner exception

   15:52:21:000 FATAL_ERROR AnonymousBlock: line 11, column 1

   15:52:21:000 FATAL_ERROR Caused by

   15:52:21:000 FATAL_ERROR AnonymousBlock: line 7, column 1

```

The example in the next section shows how to handle an exception with an inner exception by calling the `getCause` method.

Inner Exception Example

Now that you’ve seen how to create a custom exception class and how to construct your exception objects, let’s create and run an
example that demonstrates the usefulness of custom exceptions.

**1.** In the Developer Console, create a class named `MerchandiseException` and confirm that it has this content.

```
     public class MerchandiseException extends Exception {

     }

```

You’ll use this exception class in the second class that you create. The curly braces at the end enclose the body of your exception
class, which we left empty because we get some free code—our class inherits all the constructors and common exception methods,
such as `getMessage`, from the built-in `Exception` class.

**2.** Next, create a second class named `MerchandiseUtility` .

```
     public class MerchandiseUtility {

       public static void mainProcessing() {

          try {

            insertMerchandise();

          } catch(MerchandiseException me) {

            System.debug('Message: ' + me.getMessage());

```


Apex Developer Guide Debugging Apex

```
            System.debug('Cause: ' + me.getCause());

            System.debug('Line number: ' + me.getLineNumber());

            System.debug('Stack trace: ' + me.getStackTraceString());

          }

       }

       public static void insertMerchandise() {

          try {

            // Insert merchandise without required fields

            Merchandise__c m = new Merchandise__c();

            insert m;

          } catch(DmlException e) {

            // Something happened that prevents the insertion

            // of Employee custom objects, so throw a more

            // specific exception.

            throw new MerchandiseException(

               'Merchandise item could not be inserted.', e);

          }

       }

     }

```

This class contains the `mainProcessing` method, which calls `insertMerchandise` . The latter causes an exception by
inserting a Merchandise without required fields. The catch block catches this exception and throws a new exception, the custom
MerchandiseException you created earlier. Notice that we called a constructor for the exception that takes two arguments: the error
message, and the original exception object. You might wonder why we are passing the original exception? Because it is useful
information—when the MerchandiseException gets caught in the first method, `mainProcessing`, the original exception
(referred to as an inner exception) is really the cause of this exception because it occurred before the MerchandiseException.

**3.** Now let’s see all this in action to understand better. Execute the following:

```
     MerchandiseUtility.mainProcessing();

```

**4.** Check the debug log output. You should see something similar to the following:

```
    18:12:34:928 USER_DEBUG [6]|DEBUG|Message: Merchandise item could not be inserted.

    18:12:34:929 USER_DEBUG [7]|DEBUG|Cause: System.DmlException: Insert failed. First

    exception on row 0; first error: REQUIRED_FIELD_MISSING, Required fields are missing:

    [Description, Price, Total Inventory]: [Description, Price, Total Inventory]

    18:12:34:929 USER_DEBUG [8]|DEBUG|Line number: 22

    18:12:34:930 USER_DEBUG [9]|DEBUG|Stack trace:

    Class.EmployeeUtilityClass.insertMerchandise: line 22, column 1

```

A few items of interest:

**•** The cause of MerchandiseException is the DmlException. You can see the DmlException message also that states that required
fields were missing.

**•** The stack trace is line 22, which is the second time an exception was thrown. It corresponds to the throw statement of
MerchandiseException.

```
       throw new MerchandiseException('Merchandise item could not be inserted.', e);

```


### Apex Developer Guide Testing Apex Testing Apex

Apex provides a testing framework that allows you to write unit tests, run your tests, check test results, and have code coverage results.

Let's talk about unit tests, data visibility for tests, and the tools that are available on the Lightning platform for testing Apex. We'll also
describe testing best practices and a testing example.

Note: To protect the privacy of your data, make sure that test error messages and exception details don’t contain any personal
data. The Apex exception handler and testing framework can’t determine if sensitive data is contained in user-defined messages
and details. To include personal data in custom Apex exceptions, we recommend that you create an Exception subclass with new
properties that hold the personal data. Then, don’t include subclass property information in the exception's message string.

#### Understanding Testing in Apex

What to Test in Apex

What Are Apex Unit Tests?

Understanding Test Data
Apex test data is transient and isn’t committed to the database.

Run Unit Test Methods
To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup,
in the Salesforce extensions for Visual Studio Code, or using the API.

Testing Best Practices

Testing Example

Testing and Code Coverage
The Apex testing framework generates code coverage numbers for your Apex classes and triggers every time you run one or more
tests. Code coverage indicates how many executable lines of code in your classes and triggers have been exercised by test methods.
Write test methods to test your triggers and classes, and then run those tests to generate code coverage information.

Code Coverage Best Practices
Consider the following code coverage tips and best practices.

Build a Mocking Framework with the Stub API
Apex provides a stub API for implementing a mocking framework. A mocking framework has many benefits. It can streamline and
improve testing and help you create faster, more reliable tests. You can use it to test classes in isolation, which is important for unit
testing. Building your mocking framework with the stub API can also be beneficial because stub objects are generated at runtime.
Because these objects are generated dynamically, you don’t have to package and deploy test classes. You can build your own
mocking framework, or you can use one built by someone else.

#### Understanding Testing in Apex

Testing is the key to successful long-term development and is a critical component of the development process. We strongly recommend
that you use a _test-driven development_ process, that is, test development that occurs at the same time as code development.

Why Test Apex?

Testing is key to the success of your application, particularly if your application is to be deployed to customers. If you validate that your
application works as expected, that there are no unexpected behaviors, your customers are going to trust you more.


Apex Developer Guide Testing Apex

There are two ways of testing an application. One is through the Salesforce user interface, important, but merely testing through the
user interface will not catch all of the use cases for your application. The other way is to test for bulk functionality: up to 200 records can
be passed through your code if it's invoked using SOAP API or by a Visualforce standard set controller.

An application is seldom finished. You will have additional releases of it, where you change and extend functionality. If you have written
comprehensive tests, you can ensure that a regression is not introduced with any new functionality.

Before you can deploy your code or package it for the Salesforce AppExchange, the following must be true.

**•** Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully.

Note the following.

**–** When deploying Apex to a production organization, each unit test in your organization namespace is executed by default.

**–** Calls to `System.debug` aren’t counted as part of Apex code coverage.

**–** Test methods and test classes aren’t counted as part of Apex code coverage.

**–** While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead,
make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single
records. This approach ensures that 75% or more of your code is covered by unit tests.

**•** Every trigger must have some test coverage.

**•** All classes and triggers must compile successfully.

Salesforce runs all tests in all organizations that have Apex code to verify that no behavior has been altered as a result of any service
upgrades.

#### What to Test in Apex

Salesforce recommends that you write tests for the following:

**Single action**
Test to verify that a single record produces the correct, expected result.

**Bulk actions**
Any Apex code, whether a trigger, a class or an extension, may be invoked for 1 to 200 records. You must test not only the single
record case, but the bulk cases as well.

**Positive behavior**
Test to verify that the expected behavior occurs through every expected permutation, that is, that the user filled out everything
correctly and did not go past the limits.

**Negative behavior**
There are likely limits to your applications, such as not being able to add a future date, not being able to specify a negative amount,
and so on. You must test for the negative case and verify that the error messages are correctly produced as well as for the positive,
within the limits cases.

**Restricted user**
Test whether a user with restricted access to the sObjects used in your code sees the expected behavior. That is, whether they can
run the code or receive error messages.

Note: Conditional and ternary operators are not considered executed unless both the positive and negative branches are executed.

For examples of these types of tests, see Testing Example on page 736.


Apex Developer Guide Testing Apex

#### What Are Apex Unit Tests?

To facilitate the development of robust, error-free code, Apex supports the creation and execution of _unit tests_ . Unit tests are class
methods that verify whether a particular piece of code is working properly. Unit test methods take no arguments, commit no data to
the database, and send no emails. Such methods are flagged with the `@IsTest` annotation in the method definition. Unit test methods
must be defined in test classes, that is, classes annotated with `@IsTest` .

For example:

```
   @IsTest

   private class myClass {

      @IsTest

      static void myTest() {

        // code_block

      }

   }

```

Use the `@IsTest` annotation to define classes and methods that only contain code used for testing your application. The `@IsTest`
annotation can take multiple modifiers within parentheses and separated by blanks.

Note: The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce
recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future
release.

This example of a test class contains two test methods.

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

Classes and methods defined as `@IsTest` can be either `private` or `public` . The access level of test classes methods doesn’t
matter. You need not add an access modifier when defining a test class or test methods. The default access level in Apex is private. The
testing framework can always find the test methods and execute them, regardless of their access level.

Classes defined as `@IsTest` must be top-level classes and can't be interfaces or enums.

Methods of a test class can only be called from a test method or code invoked by a test method; non-test requests can’t invoke it.

This example shows a class to be tested and its corresponding test class. It contains two methods and a constructor.

```
   public class TVRemoteControl {

      // Volume to be modified

      Integer volume;

      // Constant for maximum volume value

      static final Integer MAX_VOLUME = 50;

```


Apex Developer Guide Testing Apex

```
      // Constructor

      public TVRemoteControl(Integer v) {

        // Set initial value for volume

        volume = v;

      }

      public Integer increaseVolume(Integer amount) {

        volume += amount;

        if (volume > MAX_VOLUME) {

           volume = MAX_VOLUME;

        }

        return volume;

      }

      public Integer decreaseVolume(Integer amount) {

        volume -= amount;

        if (volume < 0) {

           volume = 0;

        }

        return volume;

      }

      public static String getMenuOptions() {

        return 'AUDIO SETTINGS - VIDEO SETTINGS';

      }

   }

```

This example contains the corresponding test class with four test methods. Each method in the previous class is called. Although there’s
sufficient test coverage, the test methods in the test class perform extra testing to verify boundary conditions.

```
   @IsTest

   class TVRemoteControlTest {

      @IsTest

      static void testVolumeIncrease() {

        TVRemoteControl rc = new TVRemoteControl(10);

        Integer newVolume = rc.increaseVolume(15);

        System.assertEquals(25, newVolume);

      }

      @IsTest

      static void testVolumeDecrease() {

        TVRemoteControl rc = new TVRemoteControl(20);

        Integer newVolume = rc.decreaseVolume(15);

        System.assertEquals(5, newVolume);

      }

      @IsTest

      static void testVolumeIncreaseOverMax() {

        TVRemoteControl rc = new TVRemoteControl(10);

        Integer newVolume = rc.increaseVolume(100);

        System.assertEquals(50, newVolume);

      }

      @IsTest

```


Apex Developer Guide Testing Apex

```
      static void testVolumeDecreaseUnderMin() {

        TVRemoteControl rc = new TVRemoteControl(10);

        Integer newVolume = rc.decreaseVolume(100);

        System.assertEquals(0, newVolume);

      }

      @IsTest

      static void testGetMenuOptions() {

        // Static method call. No need to create a class instance.

        String menu = TVRemoteControl.getMenuOptions();

        System.assertNotEquals(null, menu);

        System.assertNotEquals('', menu);

      }

   }

```

Unit Test Considerations

Here are some things to note about unit tests.

**•** Starting with Salesforce API 28.0, test methods can no longer reside in non-test classes and must be part of classes annotated with
`IsTest` . See the `TestVisible` annotation to learn how you can access private class members from a test class.

**•** Test methods can’t be used to test Web service callouts. Instead, use mock callouts. See Test Web Service Callouts and Testing HTTP
Callouts.

**•** You can’t send email messages from a test method.

**•** Since test methods don’t commit data created in the test, you don’t have to delete test data upon completion.

**•** If the value of a static member variable in a test class is changed in a testSetup or test method, the new value isn’t preserved. Other
test methods in this class get the original value of the static member variable. This behavior also applies when the static member
variable is defined in another class and accessed in test methods.

**•** For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example,
inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must have
unique names.

**•** Tracked changes for a record (FeedTrackedChange records) in Chatter feeds aren't available when test methods modify the associated
record. FeedTrackedChange records require the change to the parent record they're associated with to be committed to the database
before they're created. Since test methods don't commit data, they don't result in the creation of FeedTrackedChange records.
Similarly, field history tracking records can't be created in test methods because they require other sObject records to be committed
first. For example, AccountHistory records can’t be created in test methods because Account records must be committed first.

**•** If your tests include DML, make sure that you don’t exceed the MAX_DML_ROWS limit. See “Miscellaneous Apex Limits” in Execution
Governors and Limits

##### 1. Accessing Private Test Class Members

SEE ALSO:

IsTest Annotation

##### Accessing Private Test Class Members

Test methods are defined in a test class, separate from the class they test. This can present a problem when having to access a private
class member variable from the test method, or when calling a private method. Because these are private, they aren’t visible to the test


Apex Developer Guide Testing Apex

class. You can either modify the code in your class to expose public methods that will make use of these private class members, or you
can simply annotate these private class members with `TestVisible` . When you annotate private or protected members with this
annotation, they can be accessed by test methods and only code running in test context.

This example shows how `TestVisible` is used with private member variables, a private inner class with a constructor, a private
method, and a private custom exception. All these can be accessed in the test class because they’re annotated with `TestVisible` .
The class is listed first and is followed by a test class containing the test methods.

```
   public class VisibleSampleClass {

      // Private member variables

      @TestVisible private Integer recordNumber = 0;

      @TestVisible private String areaCode = '(415)';

      // Public member variable

      public Integer maxRecords = 1000;

      // Private inner class

      @TestVisible class Employee {

        String fullName;

        String phone;

        // Constructor

        @TestVisible Employee(String s, String ph) {

           fullName = s;

           phone = ph;

        }

      }

      // Private method

      @TestVisible private String privateMethod(Employee e) {

        System.debug('I am private.');

        recordNumber++;

        String phone = areaCode + ' ' + e.phone;

        String s = e.fullName + '\'s phone number is ' + phone;

        System.debug(s);

        return s;

      }

      // Public method

      public void publicMethod() {

        maxRecords++;

        System.debug('I am public.');

      }

      // Private custom exception class

      @TestVisible private class MyException extends Exception {}

   }

   // Test class for VisibleSampleClass

   @isTest

   private class VisibleSampleClassTest {

      // This test method can access private members of another class

      // that are annotated with @TestVisible.

      static testmethod void test1() {

        VisibleSampleClass sample = new VisibleSampleClass ();

```


Apex Developer Guide Testing Apex

```
        // Access private data members and update their values

        sample.recordNumber = 100;

        sample.areaCode = '(510)';

        // Access private inner class

        VisibleSampleClass.Employee emp =

           new VisibleSampleClass.Employee('Joe Smith', '555-1212');

        // Call private method

        String s = sample.privateMethod(emp);

        // Verify result

        System.assert(

           s.contains('(510)') &&

           s.contains('Joe Smith') &&

           s.contains('555-1212'));

      }

      // This test method can throw private exception defined in another class

      static testmethod void test2() {

        // Throw private exception.

        try {

           throw new VisibleSampleClass.MyException('Thrown from a test.');

        } catch(VisibleSampleClass.MyException e) {

           // Handle exception

        }

      }

      static testmethod void test3() {

        // Access public method.

        // No @TestVisible is used.

        VisibleSampleClass sample = new VisibleSampleClass ();

        sample.publicMethod();

      }

   }

```

The `TestVisible` annotation can be handy when you upgrade the Salesforce API version of existing classes containing mixed test
and non-test code. Because test methods aren’t allowed in non-test classes starting in API version 28.0, you must move the test methods
from the old class into a new test class (a class annotated with `isTest` ) when you upgrade the API version of your class. You might
run into visibility issues when accessing private methods or member variables of the original class. In this case, just annotate these private
members with `TestVisible` .

#### Understanding Test Data

Apex test data is transient and isn’t committed to the database.

This means that after a test method finishes execution, the data inserted by the test doesn’t persist in the database. As a result, there is
no need to delete any test data at the conclusion of a test. Likewise, all the changes to existing records, such as updates or deletions,
don’t persist. This transient behavior of test data makes the management of data easier as you don’t have to perform any test data
cleanup. At the same time, if your tests access organization data, this prevents accidental deletions or modifications to existing records.


Apex Developer Guide Testing Apex

By default, existing organization data isn’t visible to test methods, with the exception of certain setup objects. You should create test
data for your test methods whenever possible. However, test code saved against Salesforce API version 23.0 or earlier has access to all
data in the organization. Data visibility for tests is covered in more detail in the next section.

##### Isolation of Test Data from Organization Data in Unit Tests

Using the isTest(SeeAllData=True) Annotation
Annotate your test class or test method with `IsTest(SeeAllData=true)` to open up data access to records in your
organization. The IsTest(SeeAllData=true) annotation applies to data queries but doesn't apply to record creation or changes,
including deletions. New and changed records are still rolled back in Apex tests even when using the annotation.

Loading Test Data
Using the `Test.loadData` method, you can populate data in your test methods without having to write many lines of code.

Common Test Utility Classes for Test Data Creation
Common test utility classes are public test classes that contain reusable code for test data creation.

Using Test Setup Methods
Use test setup methods (methods that are annotated with `@testSetup` ) to create test records once and then access them in
every test method in the test class. Test setup methods can be time-saving when you need to create reference or prerequisite data
for all test methods, or a common set of records that all test methods operate on.

##### Isolation of Test Data from Organization Data in Unit Tests

By default, Apex test methods (API version 24.0 and later) can’t access pre-existing org data such as standard objects, custom objects,
and custom settings data. They can only access data that they create. However, objects that are used to manage your organization or
metadata objects can still be accessed in your tests. These are some examples of such objects.

**•** User

**•** Profile

**•** Organization

**•** CronTrigger

**•** RecordType

**•** ApexClass

**•** ApexTrigger

**•** ApexComponent

**•** ApexPage

Whenever possible, create test data for each test. You can disable this restriction by annotating your test class or test method with the
`IsTest(SeeAllData=true)` annotation.

Test code saved using Salesforce API version 23.0 or earlier continues to have access to all data in the organization and its data access
is unchanged.

**Data Access Considerations**

**•** When working with data silo Apex tests, cross-object field references using the `Owner` relationship aren’t supported. Due to
this limitation, `SELECT Owner.IsActive FROM Account` returns null when run within a data silo Apex test.

**•** If a new test method saved using Salesforce API version 24.0 or later calls a method in another class saved using version 23.0 or
earlier, the data access restrictions of the caller are enforced in the called method. The called method can’t access organization
data because the caller can’t access it, even though it was saved in an earlier version.


Apex Developer Guide Testing Apex

**•** The `IsTest(SeeAllData=true)` annotation has no effect when added to Apex code saved using Salesforce API version
23.0 and earlier.

**•** This access restriction to test data applies to all code running in test context. For example, if a test method causes a trigger to
execute and the test can’t access organization data, the trigger won’t be able to either.

**•** If a test makes a Visualforce request, the executing test stays in test context but runs in a different thread. Therefore, test data
isolation is no longer enforced. In this case, the test will be able to access all data in the organization after initiating the Visualforce
request. However, if the Visualforce request performs a callback, such as a JavaScript remoting call, any data inserted by the
callback isn’t visible to the test.

**•** The VLOOKUP validation rule function, in API version 27.0 and earlier, always looks up org data in addition to test data when
fired by a running Apex test. Starting with version 28.0, the VLOOKUP validation rule function no longer accesses organization
data from a running Apex test. The function looks up only data created by the test, unless the test class or method is annotated
with `IsTest(SeeAllData=true)` .

**•** There can be some cases where you can’t create certain types of data from your test method because of specific limitations.
Here are some examples of such limitations.

**–** Some standard objects aren’t creatable. For more information on these objects, see the _[Object Reference for Salesforce](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/)_ .

**–** For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example,
inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must
have unique names. This error occurs whether your test is annotated with `IsTest(SeeAllData=true)`, or not.

**–** Records that are created only after related records are committed to the database, like tracked changes in Chatter. Tracked
changes for a record (FeedTrackedChange records) in Chatter feeds aren't available when test methods modify the associated
record. FeedTrackedChange records require the change to the parent record they're associated with to be committed to
the database before they're created. Since test methods don't commit data, they don't result in the creation of
FeedTrackedChange records. Similarly, field history tracking records can't be created in test methods because they require
other sObject records to be committed first. For example, AccountHistory records can’t be created in test methods because
Account records must be committed first.

**•** When working with data silo Apex tests, Salesforce recommends that you don’t share record IDs between test data and org data,
thereby preventing test data from accessing pre-existing org data.

##### Using the isTest(SeeAllData=True) Annotation

Annotate your test class or test method with `IsTest(SeeAllData=true)` to open up data access to records in your organization.
The IsTest(SeeAllData=true) annotation applies to data queries but doesn't apply to record creation or changes, including deletions.
New and changed records are still rolled back in Apex tests even when using the annotation.

Warning: By annotating your class with `@isTest(SeeAllData=true)`, you allow test methods to access all org records.
The best practice, however, is to run Apex tests with data silo using `@isTest(SeeAllData=false)` . For data access
considerations in Salesforce API version 23.0 and earlier, see Isolation of Test Data from Organization Data in Unit Tests on page
720.

This example shows how to define a test class with the `@IsTest(SeeAllData=true)` annotation. All the test methods in this
class have access to all data in the organization.

```
   // All test methods in this class can access all data.

   @IsTest(SeeAllData=true)

   public class TestDataAccessClass {

      // This test accesses an existing account.

      // It also creates and accesses a new test account.

      @IsTest

```


Apex Developer Guide Testing Apex

```
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

```


Apex Developer Guide Testing Apex

```
        // Access the account that was just created.

        Account insertedAcct = [SELECT Id,Name FROM Account

                       WHERE Name='Test Account'];

        System.assert(insertedAcct != null);

      }

   }

```

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

##### Loading Test Data

Using the `Test.loadData` method, you can populate data in your test methods without having to write many lines of code.

Follow these steps:

**1.** Add the data in a .csv file.

**2.** Create a static resource for this file.

**3.** Call `Test.loadData` within your test method and passing it the sObject type token and the static resource name.

For example, for Account records and a static resource name of _`myResource`_, make the following call:

```
   List<sObject> ls = Test.loadData(Account.sObjectType, 'myResource');

```

The `Test.loadData` method returns a list of sObjects that correspond to each record inserted.

You must create the static resource prior to calling this method. The static resource is a comma-delimited file ending with a .csv extension.
The file contains field names and values for the test records. The first line of the file must contain the field names and subsequent lines
are the field values. To learn more about static resources, see “Defining Static Resources” in the Salesforce online help.

Once you create a static resource for your .csv file, the static resource will be assigned a MIME type. Supported MIME types are:

**•** text/csv

**•** application/vnd.ms-excel

**•** application/octet-stream

**•** text/plain

**`Test.loadData`** Example

The following are steps for creating a sample .csv file and a static resource, and calling `Test.loadData` to insert the test records.

**1.** Create a .csv file that has the data for the test records. This sample .csv file has three account records. You can use this sample content
to create your .csv file.

```
     Name,Website,Phone,BillingStreet,BillingCity,BillingState,BillingPostalCode,BillingCountry

     sForceTest1,http://www.sforcetest1.com,(415) 901-7000,The Landmark @ One Market,San

```


Apex Developer Guide Testing Apex

```
     Francisco,CA,94105,US

     sForceTest2,http://www.sforcetest2.com,(415) 901-7000,The Landmark @ One Market Suite

     300,San Francisco,CA,94105,US

     sForceTest3,http://www.sforcetest3.com,(415) 901-7000,1 Market St,San

     Francisco,CA,94105,US

```

**2.** Create a static resource for the .csv file:

**a.** From Setup, enter _`Static Resources`_ in the `Quick Find` box, then select **Static Resources** .

**b.** Click **New** .

**c.** Name your static resource _`testAccounts`_ .

**d.** Choose the file you created.

**e.** Click **Save** .

**3.** Call `Test.loadData` in a test method to populate the test accounts.

```
     @isTest

     private class DataUtil {

       static testmethod void testLoadData() {

          // Load the test accounts from the static resource

          List<sObject> ls = Test.loadData(Account.sObjectType, 'testAccounts');

          // Verify that all 3 test accounts were created

          System.assert(ls.size() == 3);

          // Get first test account

          Account a1 = (Account)ls[0];

          String acctName = a1.Name;

          System.debug(acctName);

          // Perform some testing using the test records

       }

     }

##### Common Test Utility Classes for Test Data Creation

```

Common test utility classes are public test classes that contain reusable code for test data creation.

Public test utility classes are defined with the `IsTest` annotation, and as such, are excluded from the organization code size limit and
execute in test context. They can be called by test methods but not by non-test code.

The methods in the public test utility class are defined the same way methods are in non-test classes. They can take parameters and can
return a value. The methods must be declared as public or global to be visible to other test classes. These common methods can be
called by any test method in your Apex classes to set up test data before running the test. While you can create public methods for test
data creation in a regular Apex class, without the `IsTest` annotation, you don’t get the benefit of excluding this code from the
organization code size limit.

This is an example of a test utility class. It contains one method, `createTestRecords`, which accepts the number of accounts to
create and the number of contacts per account. The next example shows a test method that calls this method to create some data.

```
   @IsTest

   public class TestDataFactory {

      public static void createTestRecords(Integer numAccts, Integer numContactsPerAcct) {

        List<Account> accts = new List<Account>();

```


Apex Developer Guide Testing Apex

```
        for(Integer i=0;i<numAccts;i++) {

           Account a = new Account(Name='TestAccount' + i);

           accts.add(a);

        }

        insert accts;

        List<Contact> cons = new List<Contact>();

        for (Integer j=0;j<numAccts;j++) {

           Account acct = accts[j];

           // For each account just inserted, add contacts

           for (Integer k=numContactsPerAcct*j;k<numContactsPerAcct*(j+1);k++) {

             cons.add(new Contact(firstname='Test'+k,

                          lastname='Test'+k,

                          AccountId=acct.Id));

           }

        }

        // Insert all contacts for all accounts

        insert cons;

      }

   }

```

The test method in this class calls the test utility method, `createTestRecords`, to create five test accounts with three contacts
each.

```
   @IsTest

   private class MyTestClass {

      static testmethod void test1() {

        TestDataFactory.createTestRecords(5,3);

        // Run some tests

      }

   }

##### Using Test Setup Methods

```

Use test setup methods (methods that are annotated with `@testSetup` ) to create test records once and then access them in every
test method in the test class. Test setup methods can be time-saving when you need to create reference or prerequisite data for all test
methods, or a common set of records that all test methods operate on.

Test setup methods can reduce test execution times especially when you’re working with many records. Test setup methods enable
you to create common test data easily and efficiently. By setting up records once for the class, you don’t need to re-create records for
each test method. Also, because the rollback of records that are created during test setup happens at the end of the execution of the
entire class, the number of records that are rolled back is reduced. As a result, system resources are used more efficiently compared to
creating those records and having them rolled back for each test method.

If a test class contains a test setup method, the testing framework executes the test setup method first, before any test method in the
class. Records that are created in a test setup method are available to all test methods in the test class and are rolled back at the end of
test class execution. If a test method changes those records, such as record field updates or record deletions, those changes are rolled
back after each test method finishes execution. The next executing test method gets access to the original unmodified state of those
records.

Similarly, if you create a static variable in a test setup method, and then modify that variable in a test method, the change doesn’t persist
to other test methods. Every test method, including the test setup method, runs as a separate transaction. The static context of the test
class is reinitialized before each transaction begins. Therefore, static variable initializers and static blocks are executed fresh at the start


Apex Developer Guide Testing Apex

of every test method. Any change to a static variable within a test setup method is confined to that specific transaction. After the
transaction completes, those in-memory changes are discarded.

Syntax

Test setup methods are defined in a test class, take no arguments, and return no value. The following is the syntax of a test setup method.

```
   @testSetup static void methodName () {

   }

```

Example

This example shows how to create test records once and then access them in multiple test methods. Also, the example shows how
changes that are made in the first test method are rolled back and are not available to the second test method.

```
   @isTest

   private class CommonTestSetup {

      @testSetup static void setup() {

        // Create common test accounts

        List<Account> testAccts = new List<Account>();

        for(Integer i=0;i<2;i++) {

           testAccts.add(new Account(Name = 'TestAcct'+i));

        }

        insert testAccts;

      }

      @isTest static void testMethod1() {

        // Get the first test account by using a SOQL query

        Account acct = [SELECT Id FROM Account WHERE Name='TestAcct0' LIMIT 1];

        // Modify first account

        acct.Phone = '555-1212';

        // This update is local to this test method only.

        update acct;

        // Delete second account

        Account acct2 = [SELECT Id FROM Account WHERE Name='TestAcct1' LIMIT 1];

        // This deletion is local to this test method only.

        delete acct2;

        // Perform some testing

      }

      @isTest static void testMethod2() {

        // The changes made by testMethod1() are rolled back and

        // are not visible to this test method.

        // Get the first account by using a SOQL query

        Account acct = [SELECT Phone FROM Account WHERE Name='TestAcct0' LIMIT 1];

        // Verify that test account created by test setup method is unaltered.

        System.assertEquals(null, acct.Phone);

        // Get the second account by using a SOQL query

        Account acct2 = [SELECT Id FROM Account WHERE Name='TestAcct1' LIMIT 1];

```


Apex Developer Guide Testing Apex

```
        // Verify test account created by test setup method is unaltered.

        System.assertNotEquals(null, acct2);

        // Perform some testing

      }

   }

```

Test Setup Method Considerations

**•** Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has
access to organization data by using the `@isTest(SeeAllData=true)` annotation, test setup methods aren’t supported in
this class. Because data isolation for tests is available for API versions 24.0 and later, test setup methods are also available for those
versions only.

**•** You can have only one test setup method per test class.

**•** If a fatal error occurs during the execution of a test setup method, such as an exception that’s caused by a DML operation or an
assertion failure, the entire test class fails, and no further tests in the class are executed.

**•** If a test setup method calls a non-test method of another class, no code coverage is calculated for the non-test method.

#### Run Unit Test Methods

To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in
the Salesforce extensions for Visual Studio Code, or using the API.

You can run these groupings of unit tests.

**•** Some or all methods in a specific class

**•** Some or all methods in a set of classes

**•** A predefined suite of classes, known as a test suite

**•** All unit tests in your org

To run a test, use any of the following:

**•** Salesforce user interface

**•** [Salesforce extensions for Visual Studio Code and Code Builder](https://developer.salesforce.com/tools/vscode)

**•** Developer Console

**•** The API

All Apex tests that are started from the Salesforce user interface (including the Developer Console) run asynchronously and in parallel.
Apex test classes are placed in the Apex job queue for execution. The maximum number of test classes that you can run per 24-hour
period is the greater of 500 or 10 multiplied by the number of test classes in the org. For sandbox and Developer Edition organizations,
this limit is higher and is the greater of 500 or 20 multiplied by the number of test classes in the org.

Note: Apex tests that run as part of a deployment always run synchronously and serially.

Running Tests Through the Salesforce User Interface

You can run unit tests on the Application Test Execution page. Tests started on this page run asynchronously, that is, you don't have to
wait for a test class execution to finish. The Application Test Execution page refreshes the status of a test and displays the results after
the test completes.


Apex Developer Guide Testing Apex

**1.** From Setup, enter _`Application Test Execution`_ in the `Quick Find` box, then select **Application Test Execution** .

**2.** Click **Select Tests...** .

Note: If you have Apex classes that are installed from a managed package, you must compile these classes first by clicking
**Compile all classes** on the Apex Classes page so that they appear in the list.

**3.** Select the tests to run. The list of tests includes only classes that contain test methods.

**•** To select tests from an installed managed package, select the managed package’s corresponding namespace from the dropdown
list. Only the classes of the managed package with the selected namespace appear in the list.

**•** To select tests that exist locally in your organization, select **[My Namespace]** from the dropdown list. Only local classes that
aren't from managed packages appear in the list.

**•** To select any test, select **[All Namespaces]** from the dropdown list. All the classes in the organization appear, even those in a
managed package.

Note: Classes with tests currently running don't appear in the list.

**4.** To opt out of collecting code coverage information during test runs, select **Skip Code Coverage** .

**5.** Click **Run** .

After you run tests using the Application Test Execution page, you can view code coverage details in the Developer Console.

From Setup, enter _`Application`_ in the `Quick Find` box, select **Application Test Execution**, then click **View Test History** to
view all test results for your organization, not just tests that you have run. Test results are retained for 30 days after they finish running,
unless cleared.

Running Tests Using the Salesforce Extensions for Visual Studio Code

[You can execute tests with Visual Studio Code. See Salesforce Extensions for Visual Studio Code and Code Builder.](https://developer.salesforce.com/tools/vscode)

Running Tests Using the Developer Console

In the Developer Console, you can execute some or all tests in specific test classes, set up and run test suites, or run all tests. The Developer
Console runs tests asynchronously in the background, unless your test run includes only one class and you’ve not chosen **Always Run**
**Asynchronously** in the Test menu. Running tests asynchronously lets you work in other areas of the Developer Console while tests are


Apex Developer Guide Testing Apex

running. After the tests execute, you can inspect the test results in the Developer Console. Also, you can inspect the overall code coverage
for classes covered by the tests.

For more information, see the Developer Console documentation in Salesforce Help.

Running Tests Using the API

You can use the `runTests()` call from SOAP API to run tests synchronously.

```
   RunTestsResult[] runTests(RunTestsRequest ri)

```

This call allows you to run the following, as specified in the RunTestsRequest object:

**•** All tests in all classes

**•** All tests in a specific namespace

**•** All tests in a subset of classes in a specific namespace

It returns the following:

**•** Total number of tests that ran

**•** Code coverage statistics

**•** Error information for each failed test

**•** Information for each test that succeeds

**•** Time it took to run the test

For more information on `runTests()`, see `[runTests()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_runtests.htm)` in the _SOAP API Developer Guide_ .

You can also run tests using the Tooling REST API. Use the `/runTestsAsynchronous/` and `/runTestsSynchronous/`
endpoints to run tests asynchronously or synchronously. For usage details, see _Tooling API_ [: REST Resources.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/intro_rest_overview.htm)

Running Tests Using **`ApexTestQueueItem`**

You can run tests asynchronously using `[ApexTestQueueItem](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_apextestqueueitem.htm)` and `[ApexTestResult](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_apextestresult.htm)` . These objects let you add tests to the
Apex job queue and check the results of the completed test runs. This process enables you to not only start tests asynchronously but
also schedule your tests to execute at specific times by using the Apex scheduler. See Apex Scheduler for more information.

Insert an `ApexTestQueueItem` object to place its corresponding Apex class in the Apex job queue for execution. The Apex job
executes the test methods in the class. After the job executes, `ApexTestResult` contains the result for each single test method
executed as part of the test.

`ApexTestResult` rows are also generated for Apex tests run with the `@testSetup` annotation. The `IsTestSetup` field is
set to `true` for these annotated tests to distinguish them from other test methods. The `TestSetupTime` field on
`ApexTestRunResult` tracks the cumulative time of all setup methods for the given `ApexTestRunResult` .

To abort a class that is in the Apex job queue, perform an update operation on the ApexTestQueueItem object and set its `Status`
field to _`Aborted`_ .

If you insert multiple Apex test queue items in a single bulk operation, the queue items share a parent job and a test run can execute
tests for several classes.

The maximum number of test queue items, and hence classes, that you can insert in the Apex job queue is the greater of 500 or 10
multiplied by the number of test classes in the org. For sandbox and Developer Edition organizations, this limit is higher and is the greater
of 500 or 20 multiplied by the number of test classes in the org.

You may observe slower async test execution time when compilation is required, for example when tests are run after altering an Apex
class. This is because parallel test execution is restricted to one job until compilation is completed. If you have Apex code in your org that


Apex Developer Guide Testing Apex

is referenced by queued tests and fails to compile, you will be limited to the one concurrent job. You must ensure that Apex code in
your org compiles successfully.

This example uses DML operations to insert and query the `ApexTestQueueItem` and `ApexTestResult` objects. The
`enqueueTests` method inserts queue items for all classes that end with Test. It then returns the parent job ID of one queue item,
which is the same for all queue items because they were inserted in bulk. The `checkClassStatus` method retrieves all queue
items that correspond to the specified job ID. It then queries and outputs the name, job status, and pass rate for each class. The
`checkMethodStatus` method gets information of each test method that was executed as part of the job.

```
   public class TestUtil {

      // Enqueue all classes ending in "Test".

      public static ID enqueueTests() {

        ApexClass[] testClasses =

          [SELECT Id FROM ApexClass

           WHERE Name LIKE '%Test'];

        if (testClasses.size() > 0) {

           ApexTestQueueItem[] queueItems = new List<ApexTestQueueItem>();

           for (ApexClass cls : testClasses) {

             queueItems.add(new ApexTestQueueItem(ApexClassId=cls.Id));

           }

           insert queueItems;

           // Get the job ID of the first queue item returned.

           ApexTestQueueItem item =

            [SELECT ParentJobId FROM ApexTestQueueItem

             WHERE Id=:queueItems[0].Id LIMIT 1];

           return item.parentjobid;

        }

        return null;

      }

      // Get the status and pass rate for each class

      // whose tests were run by the job.

      // that correspond to the specified job ID.

      public static void checkClassStatus(ID jobId) {

        ApexTestQueueItem[] items =

          [SELECT ApexClass.Name, Status, ExtendedStatus

           FROM ApexTestQueueItem

           WHERE ParentJobId=:jobId];

        for (ApexTestQueueItem item : items) {

           String extStatus = item.extendedstatus == null ? '' : item.extendedStatus;

           System.debug(item.ApexClass.Name + ': ' + item.Status + extStatus);

        }

      }

      // Get the result for each test method that was executed.

      public static void checkMethodStatus(ID jobId) {

        ApexTestResult[] results =

          [SELECT Outcome, ApexClass.Name, MethodName, Message, StackTrace

           FROM ApexTestResult

           WHERE AsyncApexJobId=:jobId];

        for (ApexTestResult atr : results) {

          System.debug(atr.ApexClass.Name + '.' + atr.MethodName + ': ' + atr.Outcome);

```


Apex Developer Guide Testing Apex

```
           if (atr.message != null) {

             System.debug(atr.Message + '\n at ' + atr.StackTrace);

           }

        }

      }

   }

##### 1. Using the runAs Method Method
```

Generally, all Apex code runs in system mode, where the object-level and field-level permissions of the current user aren’t taken into
account. With the System method `runAs`, you can write test methods that change the user context to an existing user or a new
user. Then the user’s sharing rules and object-level and field-level permissions are enforced.

2. Using Limits, startTest, and, and stopTest

3. Adding SOSL Queries to Unit Tests

SEE ALSO:

Testing and Code Coverage

_Salesforce Help_ [: Open the Developer Console](https://help.salesforce.com/HTViewHelpDoc?id=code_dev_console_opening.htm&language=en_US)

##### Using the runAs Method Method

Generally, all Apex code runs in system mode, where the object-level and field-level permissions of the current user aren’t taken into
account. With the System method `runAs`, you can write test methods that change the user context to an existing user or a new user.
Then the user’s sharing rules and object-level and field-level permissions are enforced.

Note: The user’s sharing rules and object-level and field-level permissions are enforced within a `runAs` block, regardless of the
sharing mode ( `with sharing` or `without sharing` ) of the test class.

If a user-defined method is called in the `runAs` block, the sharing mode enforced is that of the class where the method is defined,
not the test class.

You can use `runAs` only in test methods. The original system context is started again after all `runAs` test methods complete.

The `runAs` method ignores user license limits. You can create users with `runAs` even if your organization has no additional user
licenses.

Note: Every call to `runAs` counts against the total number of DML statements issued in the process.

In the following example, a new test user is created, then code is run as that user, with that user's record sharing access:

```
   @isTest

   private class TestRunAs {

     public static testMethod void testRunAs() {

        // Setup test data

        // Create a unique UserName

       String uniqueUserName = 'standarduser' + DateTime.now().getTime() + '@testorg.com';

        // This code runs as the system user

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

        User u = new User(Alias = 'standt', Email='standarduser@testorg.com',

        EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',

```


Apex Developer Guide Testing Apex

```
        LocaleSidKey='en_US', ProfileId = p.Id,

        TimeZoneSidKey='America/Los_Angeles',

         UserName=uniqueUserName);

        System.runAs(u) {

            // The following code runs as user 'u'

            System.debug('Current User: ' + UserInfo.getUserName());

            System.debug('Current Profile: ' + UserInfo.getProfileId());

         }

      }

   }

```

You can nest more than one `runAs` method. For example:

```
   @isTest

   private class TestRunAs2 {

     public static testMethod void test2() {

       Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

       User u2 = new User(Alias = 'newUser', Email='newuser@testorg.com',

         EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',

         LocaleSidKey='en_US', ProfileId = p.Id,

         TimeZoneSidKey='America/Los_Angeles', UserName='newuser@testorg.com');

       System.runAs(u2) {

         // The following code runs as user u2.

         System.debug('Current User: ' + UserInfo.getUserName());

         System.debug('Current Profile: ' + UserInfo.getProfileId());

         // The following code runs as user u3.

         User u3 = [SELECT Id FROM User WHERE UserName='newuser@testorg.com'];

         System.runAs(u3) {

           System.debug('Current User: ' + UserInfo.getUserName());

           System.debug('Current Profile: ' + UserInfo.getProfileId());

         }

         // Any additional code here would run as user u2.

       }

     }

   }

```

Other Uses of **`runAs`**

You can also use the `runAs` method to perform mixed DML operations in your test by enclosing the DML operations within the `runAs`
block. In this way, you bypass the mixed DML error that is otherwise returned when inserting or updating setup objects together with
other sObjects. See sObjects That Cannot Be Used Together in DML Operations.


Apex Developer Guide Testing Apex

There’s another overload of the `runAs` method ( `runAs(System.Version)` ) that takes a package version as an argument. This
method causes the code of a specific version of a managed package to be used. For information on using the `runAs` method and
specifying a package version context, see Testing Behavior in Package Versions on page 755.

SEE ALSO:

Enforce Sharing Rules

Enforce Object and Field Permissions

_Apex Reference Guide_ [: System.runAs(userSObject)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_System_runAs_2)

##### Using Limits, startTest, and, and stopTest

The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap
size remaining.

Each method has two versions. The first version returns the amount of the resource that has been used in the current context. The second
version contains the word “limit” and returns the total amount of the resource that is available for that context. For example,
`getCallouts` returns the number of callouts to an external service that have already been processed in the current context, while
`getLimitCallouts` returns the total number of callouts available in the given context.

In addition to the Limits methods, use the `startTest` and `stopTest` methods to validate how close the code is to reaching
governor limits.

The `startTest` method marks the point in your test code when your test actually begins. Each test method is allowed to call this
method only once. All of the code before this method should be used to initialize variables, populate data structures, and so on, allowing
you to set up everything you need to run your test. Any code that executes after the call to `startTest` and before `stopTest` is
assigned a new set of governor limits.

The `startTest` method does not refresh the context of the test: it adds a context to your test. For example, if your class makes 98
SOQL queries before it calls `startTest`, and the first significant statement after `startTest` is a DML statement, the program can
now make an additional 100 queries. Once `stopTest` is called, however, the program goes back into the original context, and can
only make 2 additional SOQL queries before reaching the limit of 100.

The `stopTest` method marks the point in your test code when your test ends. Use this method in conjunction with the `startTest`
method. Each test method is allowed to call this method only once. Any code that executes after the `stopTest` method is assigned
the original limits that were in effect before `startTest` was called. All asynchronous calls made after the `startTest` method are
collected by the system. When `stopTest` is executed, all asynchronous processes are run synchronously. An exception encountered
during `stopTest` halts the synchronous processing. For example, an unhandled exception in a batch job’s `execute` method will
prevent the `finish` method from running in a test context.

SEE ALSO:

[Test Apex Triggers](https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_triggers)

##### Adding SOSL Queries to Unit Tests

To ensure that test methods always behave in a predictable way, any Salesforce Object Search Language (SOSL) query that is added to
an Apex test method returns an empty set of search results when the test method executes. If you do not want the query to return an
empty list of results, you can use the `Test.setFixedSearchResults` system method to define a list of record IDs that are
returned by the search. All SOSL queries that take place later in the test method return the list of record IDs that were specified by the
`Test.setFixedSearchResults` method. Additionally, the test method can call `Test.setFixedSearchResults`
multiple times to define different result sets for different SOSL queries. If you do not call the `Test.setFixedSearchResults`


Apex Developer Guide Testing Apex

method in a test method, or if you call this method without specifying a list of record IDs, any SOSL queries that take place later in the
test method return an empty list of results.

The list of record IDs specified by the `Test.setFixedSearchResults` method replaces the results that would normally be
returned by the SOSL query if it were not subject to any `WHERE` or `LIMIT` clauses. If these clauses exist in the SOSL query, they are
applied to the list of fixed search results. For example:

```
   @isTest

   private class SoslFixedResultsTest1 {

      public static testMethod void testSoslFixedResults() {

        Id [] fixedSearchResults= new Id[1];

        fixedSearchResults[0] = '001x0000003G89h';

        Test.setFixedSearchResults(fixedSearchResults);

        List<List<SObject>> searchList = [FIND 'test'

                            IN ALL FIELDS RETURNING

                              Account(id, name WHERE name = 'test' LIMIT

   1)];

      }

   }

```

Note: SOSL queries for `ContentDocument` (File) or `ContentNote` (Note) entities require using
`setFixedSearchResults` with `ContentVersion` IDs to remain consistent with how Salesforce indexes and searches
for files and notes.

Although the account record with an ID of `001x0000003G89h` may not match the query string in the FIND clause ( `'test'` ), the
record is passed into the `RETURNING` clause of the SOSL statement. If the record with ID `001x0000003G89h` matches the `WHERE`
clause filter, the record is returned. If it does not match the `WHERE` clause, no record is returned.

#### Testing Best Practices

Good tests do the following:

**•** Cover as many lines of code as possible. Before you can deploy Apex or package it for AppExchange, the following must be true.

Important:

**–** Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully.

Note the following.

**•** When deploying Apex to a production organization, each unit test in your organization namespace is executed by
default.

**•** Calls to `System.debug` aren’t counted as part of Apex code coverage.

**•** Test methods and test classes aren’t counted as part of Apex code coverage.

**•** While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered.
Instead, make sure that every use case of your application is covered, including positive and negative cases, as well as
bulk and single records. This approach ensures that 75% or more of your code is covered by unit tests.

**•** Tests don’t run in parallel in metadata deployments, package installations, or change set deployments.

**–** Every trigger must have some test coverage.

**–** All classes and triggers must compile successfully.

**•** If code uses conditional logic (including ternary operators), execute each branch.


Apex Developer Guide Testing Apex

**•** Make calls to methods using both valid and invalid inputs.

**•** Complete successfully without throwing any exceptions, unless those errors are expected and caught in a `try…catch` block.

**•** Always handle all exceptions that are caught, instead of merely catching the exceptions.

**•** [Use the methods of the Assert class to prove that the code behaves properly.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Assert.htm)

**•** Use the `runAs` method to test your application in different user contexts.

**•** Exercise bulk trigger functionality—use at least 20 records in your tests.

**•** Use the `ORDER BY` keywords to ensure that the records are returned in the expected order.

**•** Not assume that record IDs are in sequential order.

Record IDs aren’t created in ascending order unless you insert multiple records with the same request. For example, if you create an
account A, and receive the ID `001D000000IEEmT`, then create account B, the ID of account B need not be sequentially higher.

**•** Set up test data:

**–** Create the necessary data in test classes, so the tests don’t have to rely on data in a particular organization.

**–** Create all test data before calling the `Test.startTest` method.

**–** Since tests don't commit, you don't have to delete any data.

**•** Write comments stating not only what must be tested, but the assumptions the tester made about the data, the expected outcome,
and so on.

**•** Test the classes in your application individually. Never test your entire application in a single test.

Note: To protect the privacy of your data, make sure that test error messages and exception details don’t contain any personal
data. The Apex exception handler and testing framework can’t determine if sensitive data is contained in user-defined messages
and details. To include personal data in custom Apex exceptions, we recommend that you create an Exception subclass with new
properties that holds the personal data. Then, don’t include subclass property information in the exception's message string.

If you’re running many tests, test the classes in your organization individually in the Salesforce user interface instead of using the **Run**
**All Tests** button to run them all together.

Best Practices for Parallel Test Execution

Tests that are started from the Salesforce user interface (including the Developer Console) run in parallel. Parallel test execution can
speed up test run time. Sometimes, parallel test execution results in data contention issues, and you can turn off parallel execution in
those cases. In particular, data contention issues and `UNABLE_TO_LOCK_ROW` errors can occur in the following cases:

**•** When tests update the same records at the same time. Updating the same records typically occurs when tests don’t create their
own data and turn off data isolation to access the organization’s data.

**•** When a deadlock occurs in tests that are running in parallel and that try to create records with duplicate index field values. A deadlock
occurs when two running tests are waiting for each other to roll back data. Such a wait can happen if two tests insert records with
the same unique index field values.

You can prevent receiving those errors by turning off parallel test execution in the Salesforce user interface:

**1.** From Setup, enter _`Apex Test`_ .

**2.** Click **Options...** .

**3.** In the Apex Test Execution Options dialog, select **Disable Parallel Apex Testing** and then click **OK** .


Apex Developer Guide Testing Apex

Test classes annotated with `IsTest(IsParallel=true)` indicate that the test class can run concurrently with more than the
default number of concurrent test classes. This annotation overrides default settings.

SEE ALSO:

Code Coverage Best Practices

#### Testing Example

The following example includes cases for the following types of tests:

**•** Positive case with single and multiple records

**•** Negative case with single and multiple records

**•** Testing with other users

The test is used with a simple mileage tracking application. The existing code for the application verifies that not more than 500 miles
are entered in a single day. The primary object is a custom object named Mileage__c. The test creates one record with 300 miles and
verifies there are only 300 miles recorded. Then a loop creates 200 records with one mile each. Finally, it verifies there are 500 miles
recorded in total (the original 300 plus the new ones). Here’s the entire test class. The following sections step through specific portions
of the code.

```
   @isTest

   private class MileageTrackerTestSuite {

      static testMethod void runPositiveTestCases() {

        Double totalMiles = 0;

        final Double maxtotalMiles = 500;

        final Double singletotalMiles = 300;

        final Double u2Miles = 100;

        //Set up user

        User u1 = [SELECT Id FROM User WHERE Alias='auser'];

        //Run As U1

        System.RunAs(u1){

        System.debug('Inserting 300 miles... (single record validation)');

        Mileage__c testMiles1 = new Mileage__c(Miles__c = 300, Date__c = System.today());

        insert testMiles1;

        //Validate single insert

        for(Mileage__c m:[SELECT miles__c FROM Mileage__c

           WHERE CreatedDate = TODAY

           and CreatedById = :u1.id

           and miles__c != null]) {

             totalMiles += m.miles__c;

           }

        Assert.areEqual(singletotalMiles, totalMiles);

```


Apex Developer Guide Testing Apex

```
        //Bulk validation

        totalMiles = 0;

        System.debug('Inserting 200 mileage records... (bulk validation)');

        List<Mileage__c> testMiles2 = new List<Mileage__c>();

        for(integer i=0; i<200; i++) {

           testMiles2.add( new Mileage__c(Miles__c = 1, Date__c = System.today()) );

        }

        insert testMiles2;

        for(Mileage__c m:[SELECT miles__c FROM Mileage__c

           WHERE CreatedDate = TODAY

           and CreatedById = :u1.Id

           and miles__c != null]) {

             totalMiles += m.miles__c;

           }

        Assert.areEqual(maxtotalMiles, totalMiles);

        }//end RunAs(u1)

        //Validate additional user:

        totalMiles = 0;

        //Setup RunAs

        User u2 = [SELECT Id FROM User WHERE Alias='tuser'];

        System.RunAs(u2){

        Mileage__c testMiles3 = new Mileage__c(Miles__c = 100, Date__c = System.today());

        insert testMiles3;

             for(Mileage__c m:[SELECT miles__c FROM Mileage__c

           WHERE CreatedDate = TODAY

           and CreatedById = :u2.Id

           and miles__c != null]) {

             totalMiles += m.miles__c;

           }

        //Validate

        Assert.areEqual(u2Miles, totalMiles);

        } //System.RunAs(u2)

      } // runPositiveTestCases()

      static testMethod void runNegativeTestCases() {

        User u3 = [SELECT Id FROM User WHERE Alias='tuser'];

        System.RunAs(u3) {

          System.debug('Inserting a record with 501 miles... (negative test case)');

```


Apex Developer Guide Testing Apex

```
         Mileage__c testMiles3 = new Mileage__c( Miles__c = 501, Date__c = System.today()

    );

          try {

            insert testMiles3;

            Assert.fail('DmlException expected');

          } catch (DmlException e) {

            //Assert Status Code

           Assert.areEqual('FIELD_CUSTOM_VALIDATION_EXCEPTION', e.getDmlStatusCode(0));

            //Assert field

            Assert.areEqual(Mileage__c.Miles__c, e.getDmlFields(0)[0]);

            //Assert Error Message

            Assert.isTrue(e.getMessage().contains(

             'Mileage request exceeds daily limit(500): [Miles__c]'),

            'DMLException did not contain expected validation message:' + e.getMessage()

    );

           } //catch

          } //RunAs(u3)

      } // runNegativeTestCases()

   } // class MileageTrackerTestSuite

```

Positive Test Case

The following steps through the above code, in particular, the positive test case for single and multiple records.

**1.** Add text to the debug log, indicating the next step of the code:

```
     System.debug('Inserting 300 more miles...single record validation');

```

**2.** Create a Mileage__c object and insert it into the database.

```
     Mileage__c testMiles1 = new Mileage__c(Miles__c = 300, Date__c = System.today() );

     insert testMiles1;

```

**3.** Validate the code by returning the inserted records:

```
     for(Mileage__c m:[SELECT miles__c FROM Mileage__c

       WHERE CreatedDate = TODAY

       and CreatedById = :createdbyId

       and miles__c != null]) {

         totalMiles += m.miles__c;

       }

```

**4.** Use the `Assert.areEqual` method to verify that the expected result is returned:

```
     Assert.areEqual(singletotalMiles, totalMiles);

```


Apex Developer Guide Testing Apex

**5.** Before moving to the next test, set the number of total miles back to 0:

```
     totalMiles = 0;

```

**6.** Validate the code by creating a bulk insert of 200 records.

First, add text to the debug log, indicating the next step of the code:

```
     System.debug('Inserting 200 Mileage records...bulk validation');

```

**7.** Then insert 200 Mileage__c records:

```
     List<Mileage__c> testMiles2 = new List<Mileage__c>();

     for(Integer i=0; i<200; i++){

     testMiles2.add( new Mileage__c(Miles__c = 1, Date__c = System.today()) );

       }

     insert testMiles2;

```

**8.** Use `Assert.areEqual` to verify that the expected result is returned:

```
     for(Mileage__c m:[SELECT miles__c FROM Mileage__c

       WHERE CreatedDate = TODAY

       and CreatedById = :CreatedbyId

       and miles__c != null]) {

         totalMiles += m.miles__c;

       }

         Assert.areEqual(maxtotalMiles, totalMiles);

```

Negative Test Case

The following steps through the above code, in particular, the negative test case.

**1.** Create a static test method called `runNegativeTestCases` :

```
     static testMethod void runNegativeTestCases(){

```

**2.** Add text to the debug log, indicating the next step of the code:

```
     System.debug('Inserting 501 miles... negative test case');

```

**3.** Create a Mileage__c record with 501 miles.

```
     Mileage__c testMiles3 = new Mileage__c(Miles__c = 501, Date__c = System.today());

```

**4.** Place the `insert` statement within a `try` / `catch` block. This allows you to catch the validation exception and assert the generated
error message. Use the `Assert.fail` method to clearly assert that you expect the validation exception.

```
     try {

        insert testMiles3;

        Assert.fail('DmlException expected');

        } catch (DmlException e) {

```


Apex Developer Guide Testing Apex

**5.** Now use the `Assert.areEqual` and `Assert.isTrue` methods to do the testing. Add the following code to the `catch`

block you previously created:

```
     //Assert Status Code

     Assert.areEqual('FIELD_CUSTOM_VALIDATION_EXCEPTION', e.getDmlStatusCode(0));

     //Assert field

     Assert.areEqual(Mileage__c.Miles__c, e.getDmlFields(0)[0]);

     //Assert Error Message

     Assert.isTrue(e.getMessage().contains(

      'Mileage request exceeds daily limit(500): [Miles__c]'),

      'DMLException did not contain expected validation message:' + e.getMessage() );

```

Testing as a Second User

The following steps through the above code, in particular, running as a second user.

**1.** Before moving to the next test, set the number of total miles back to 0:

```
     totalMiles = 0;

```

**2.** Set up the next user.

```
         User u2 = [SELECT Id FROM User WHERE Alias='tuser'];

         System.RunAs(u2){

```

**3.** Add text to the debug log, indicating the next step of the code:

```
          System.debug('Setting up testing - deleting any mileage records for ' +

            UserInfo.getUserName() +

            ' from today');

```

**4.** Then insert one Mileage__c record:

```
     Mileage__c testMiles3 = new Mileage__c(Miles__c = 100, Date__c = System.today());

     insert testMiles3;

```

**5.** Validate the code by returning the inserted records:

```
     for(Mileage__c m:[SELECT miles__c FROM Mileage__c

       WHERE CreatedDate = TODAY

       and CreatedById = :u2.Id

       and miles__c != null]) {

         totalMiles += m.miles__c;

       }

```

**6.** Use the `Assert.areEqual` method to verify that the expected result is returned:

```
     Assert.areEqual(u2Miles, totalMiles);

```


Apex Developer Guide Testing Apex

#### Testing and Code Coverage

The Apex testing framework generates code coverage numbers for your Apex classes and triggers every time you run one or more tests.
Code coverage indicates how many executable lines of code in your classes and triggers have been exercised by test methods. Write
test methods to test your triggers and classes, and then run those tests to generate code coverage information.

**Apex Trigger and Class Covered by Test Methods**

In addition to ensuring the quality of your code, unit tests enable you to meet the code coverage requirements for deploying or packaging
Apex. To deploy Apex or package it for the Salesforce AppExchange, unit tests must cover at least 75% of your Apex code, and those
tests must pass.

Code coverage serves as one indication of test effectiveness, but doesn’t guarantee test effectiveness. The quality of the tests also matters,
but you can use code coverage as a tool to assess whether you need to add more tests. While you need to meet minimum code coverage
requirements for deploying or packaging your Apex code, code coverage shouldn’t be the only goal of your tests. Tests should assert
your app’s behavior and ensure the quality of your code.

How Is Code Coverage Calculated?

Code coverage percentage is a calculation of the number of covered lines divided by the sum of the number of covered lines and
uncovered lines. Only executable lines of code are included. (Comments and blank lines aren’t counted.) `System.debug()` statements
and curly brackets are excluded when they appear alone on one line. Multiple statements on one line are counted as one line for the
purpose of code coverage. If a statement consists of multiple expressions that are written on multiple lines, each line is counted for code
coverage.

The following is an example of a class with one method. The tests for this class have been run, and the option to show code coverage
was chosen for this class in the Developer Console. The blue lines represent the lines that are covered by tests. The lines that aren’t
highlighted are left out of the code coverage calculation. The red lines show the lines that weren’t covered by tests. To achieve full
coverage, more tests are needed. The tests must call `getTaskPriority()` with different inputs and verify the returned value.

This is the class that is partially covered by test methods. The corresponding test class isn’t shown.


Apex Developer Guide Testing Apex

Test classes (classes that are annotated with `@isTest` ) are excluded from the code coverage calculation. This exclusion applies to all
test classes regardless of what they contain—test methods or utility methods used for testing.

Note: The Apex compiler sometimes optimizes expressions in a statement. For example, if multiple string constants are concatenated
with the `+` operator, the compiler replaces those expressions with one string constant internally. If the string concatenation
expressions are on separate lines, the additional lines aren’t counted as part of the code coverage calculation after optimization.
To illustrate this point, a string variable is assigned to two string constants that are concatenated. The second string constant is
on a separate line.

```
      String s = 'Hello'

        + ' World!';

```

The compiler optimizes the string concatenation and represents the string as one string constant internally. The second line in
this example is ignored for code coverage.

```
      String s = 'Hello World!';

```

Inspecting Code Coverage

After running tests, you can view code coverage information in the Tests tab of the Developer Console. The code coverage pane includes
coverage information for each Apex class and the overall coverage for all Apex code in your organization.

[Also, code coverage is stored in two Lightning Platform Tooling API objects: ApexCodeCoverageAggregate and ApexCodeCoverage.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_apexcodecoverageaggregate.htm)
ApexCodeCoverageAggregate stores the sum of covered lines for a class after checking all test methods that test it. ApexCodeCoverage
stores the lines that are covered and uncovered by each individual test method. For this reason, a class can have multiple coverage
results in ApexCodeCoverage—one for each test method that has tested it. You can query these objects by using SOQL and the Tooling
API to retrieve coverage information. Using SOQL queries with Tooling API is an alternative way of checking code coverage and a quick
way to get more details.


Apex Developer Guide Testing Apex

For example, this SOQL query gets the code coverage for the `TaskUtil` class. The coverage is aggregated from all test classes that
exercised the methods in this class.

```
   SELECT ApexClassOrTrigger.Name, NumLinesCovered, NumLinesUncovered

   FROM ApexCodeCoverageAggregate

   WHERE ApexClassOrTrigger.Name = 'TaskUtil'

```

Note: This SOQL query requires the Tooling API. You can run this query by using the Query Editor in the Developer Console and
checking **Use Tooling API** .

Here’s a sample query result for a class that’s partially covered by tests:

This next example shows how you can determine which test methods covered the class. The query gets coverage information from a
different object, ApexCodeCoverage, which stores coverage information by test class and method.

```
   SELECT ApexTestClass.Name,TestMethodName,NumLinesCovered,NumLinesUncovered

   FROM ApexCodeCoverage

   WHERE ApexClassOrTrigger.Name = 'TaskUtil'

```

Here’s a sample query result.

Note: If a single deployment has over 2,000 Apex classes, ApexCodeCoverage objects for the deployed classes are deleted even
if the deployment fails or is rolled back.ApexCodeCoverageAggregate objects aren’t affected.

The NumLinesUncovered values in ApexCodeCoverage differ from the corresponding value for the aggregate result in
ApexCodeCoverageAggregate because they represent the coverage related to one test method each. For example, test method
`testTaskPriority()` covered 7 lines in the entire class out of a total of 10 coverable lines, so the number of uncovered lines
with regard to `testTaskPriority()` is 3 lines (10–7). Because the aggregate coverage stored in ApexCodeCoverageAggregate
includes coverage by all test methods, the coverage of `testTaskPriority()` and `testTaskHighPriority()` is included,
which leaves only 2 lines that are not covered by any test methods.

#### Code Coverage Best Practices

Consider the following code coverage tips and best practices.

Code Coverage General Tips

**•** Run tests to refresh code coverage numbers. Code coverage numbers aren't refreshed when updates are made to Apex code in the
organization unless tests are rerun.

**•** If the organization has been updated since the last test run, the code coverage estimate can be incorrect. Rerun Apex tests to get a
correct estimate.


Apex Developer Guide Testing Apex

**•** The overall code coverage percentage in your organization doesn’t include code coverage from package-related tests. The only
exception is when package tests cause your triggers to fire. For more information, see Managed and Unlocked Package Tests.

**•** Coverage is based on the total number of code lines in the organization. Adding or deleting lines of code changes the coverage
percentage. For example, let's say an organization has 50 lines of code covered by test methods. If you add a trigger that has 50 lines
of code not covered by tests, the code coverage percentage drops from 100% to 50%. The trigger increases the total code lines in
the organization from 50 to 100, of which only 50 are covered by tests.

Why Code Coverage Numbers Differ Between Sandbox and Production

When Apex is deployed to production or uploaded as part of a package to the Salesforce AppExchange, Salesforce runs local tests in
the destination organization. Sandbox and production environments often don’t contain the same data and metadata, so the code
coverage results don’t always match. If code coverage is less than 75% in production, increase the coverage to be able to deploy or
upload your code. The following are common causes for the discrepancies in code coverage numbers between your development or
sandbox environment and production. This information can help you troubleshoot and reconcile those differences.

**Test Failures**
If the test results in one environment are different, the overall code coverage percentage doesn’t match. Before comparing code
coverage numbers between sandbox and production, make sure that all tests for the code that you’re deploying or packaging pass
in your organization first. The tests that contribute to the code coverage calculation must all pass before deployment or a package
upload.

**Data Dependencies**
If your tests access organization data by using the `@IsTest(SeeAllData=true)` annotation, the test results can differ
depending on which data is available in the organization. If the records referenced in a test don’t exist or have changed, the test fails
or different code paths are executed in the Apex methods. Modify tests so that they create test data instead of accessing organization
data.

**Metadata Dependencies**
Changes in the metadata, such as changes in the user’s profile settings, can cause tests to fail or execute different code paths. Make
sure that the metadata in sandbox and production match, or ensure that the metadata changes aren’t the cause of different test
execution behavior.

**Managed and Unlocked Package Tests**
Code coverage that is computed after you run all Apex tests in the user interface, such as the Developer Console, can differ from
code coverage obtained in a deployment. If you run all tests, including package-related tests, in the user interface, the overall code
coverage in your organization doesn’t include coverage for packaging code. Although package-related tests cover lines of code in
managed or unlocked packages, this coverage isn’t part of the organization’s code coverage calculation as total lines and covered
lines. In contrast, the code coverage computed in a deployment after running all tests through the `RunAllTestsInOrg` test
level includes coverage of package-related code. If you’re running package tests in a deployment through the `RunAllTestsInOrg`
test level, we recommend that you run this deployment in a sandbox first or perform a validation deployment to verify code coverage.

**Deployment Resulting in Overall Coverage Lower Than 75%**
When deploying new components that have 100% coverage to production, the deployment fails if the average coverage between
the new and existing code doesn’t meet the 75% threshold. If a test run in the destination organization returns a coverage result of
less than 75%, modify the existing test methods or write additional test methods to raise the code coverage over 75%. Deploy the
modified or new test methods separately or with your new code that has 100% coverage.

**Code Coverage in Production Dropping Below 75%**
Sometimes the overall coverage in production drops below 75%, even though it was at least 75% when the components were
deployed from sandbox. Test methods that have dependencies on the organization’s data and metadata can cause a drop in code
coverage. If the data and metadata have changed sufficiently to alter the result of dependent test methods, some methods can fail
or behave differently. In that case, certain lines are no longer covered.


Apex Developer Guide Testing Apex

Recommended Process for Matching Code Coverage Numbers for Production

**•** Use a Full Sandbox as the staging sandbox environment for production deployments. A Full Sandbox mimics the metadata and data
in production and helps reduce differences in code coverage numbers between the two environments.

**•** To reduce dependencies on data in sandbox and production organizations, use test data in your Apex tests.

**•** If a deployment to production fails due to insufficient code coverage, write more tests to raise the overall code coverage to the
highest possible coverage or 100%. Retry the deployment.

**•** If a deployment to production fails even after you raise code coverage numbers in sandbox, run local tests from your production
organization. Identify the classes with less than 75% coverage. Write additional tests for these classes in sandbox to raise the code
coverage.

#### Build a Mocking Framework with the Stub API

Apex provides a stub API for implementing a mocking framework. A mocking framework has many benefits. It can streamline and
improve testing and help you create faster, more reliable tests. You can use it to test classes in isolation, which is important for unit
testing. Building your mocking framework with the stub API can also be beneficial because stub objects are generated at runtime.
Because these objects are generated dynamically, you don’t have to package and deploy test classes. You can build your own mocking
framework, or you can use one built by someone else.

You can define the behavior of stub objects, which are created at runtime as anonymous subclasses of Apex classes. The stub API
comprises the `System.StubProvider` interface and the `System.Test.createStub()` method.

Note: This feature is intended for advanced Apex developers. Using it requires a thorough understanding of unit testing and
mocking frameworks.

Let’s look at an example to illustrate how the stub API works. This example isn’t meant to demonstrate the wide range of possible uses
for mocking frameworks. It’s intentionally simple to focus on the mechanics of using the Apex stub API.

Let’s say we want to test the formatting method in the following class.

```
   public class DateFormatter {

      // Method to test

      public String getFormattedDate(DateHelper helper) {

        return 'Today\'s date is ' + helper.getTodaysDate();

      }

   }

```

Usually, when we invoke this method, we pass in a helper class that has a method that returns today’s date.

```
   public class DateHelper {

      // Method to stub

      public String getTodaysDate() {

        return Date.today().format();

      }

   }

```

The following code invokes the method.

```
   DateFormatter df = new DateFormatter();

   DateHelper dh = new DateHelper();

   String dateStr = df.getFormattedDate(dh);

```

For testing, we want to isolate the `getFormattedDate()` method to make sure that the formatting is working properly. The return
value of the `getTodaysDate()` method normally varies based on the day. However, in this case, we want to return a constant,
predictable value to isolate our testing to the formatting. Rather than writing a “fake” version of the class, where the method returns a


Apex Developer Guide Testing Apex

constant value, we create a stub version of the class. The stub object is created dynamically at runtime, and we can specify the “stubbed”
behavior of its method.

To use a stub version of an Apex class:

**1.** Define the behavior of the stub class by implementing the `System.StubProvider` interface.

**2.** Instantiate a stub object by using the `System.Test.createStub()` method.

**3.** Invoke the relevant method of the stub object from within a test class.

Implement the StubProvider Interface

Here’s an implementation of the `StubProvider` interface.

```
   @isTest

   public class MockProvider implements System.StubProvider {

      public Object handleMethodCall(Object stubbedObject, String stubbedMethodName,

        Type returnType, List<Type> listOfParamTypes, List<String> listOfParamNames,

        List<Object> listOfArgs) {

        // The following debug statements show an example of logging

        // the invocation of a mocked method.

       // You can use the method name and return type to determine which method was called.

        System.debug('Name of stubbed method: ' + stubbedMethodName);

        System.debug('Return type of stubbed method: ' + returnType.getName());

        // You can also use the parameter names and types to determine which method

        // was called.

        for (integer i =0; i < listOfParamNames.size(); i++) {

           System.debug('parameter name: ' + listOfParamNames.get(i));

           System.debug(' parameter type: ' + listOfParamTypes.get(i).getName());

        }

       // This shows the actual parameter values passed into the stubbed method at runtime.

        System.debug('number of parameters passed into the mocked call: ' +

           listOfArgs.size());

        System.debug('parameter(s) sent into the mocked call: ' + listOfArgs);

        // This is a very simple mock provider that returns a hard-coded value

        // based on the return type of the invoked.

        if (returnType.getName() == 'String')

           return '8/8/2016';

        else

           return null;

      }

   }

```

`StubProvider` is a callback interface. It specifies a single method that requires implementing: `handleMethodCall()` . When
a stubbed method is called, `handleMethodCall()` is called. You define the behavior of the stubbed class in this method. The
method has the following parameters.

**•** `stubbedObject` : The stubbed object


Apex Developer Guide Testing Apex

**•** `stubbedMethodName` : The name of the invoked method

**•** `returnType` : The return type of the invoked method

**•** `listOfParamTypes` : A list of the parameter types of the invoked method

**•** `listOfParamNames` : A list of the parameter names of the invoked method

**•** `listOfArgs` : The actual argument values passed into this method at runtime

You can use these parameters to determine which method of your class was called, and then you can define the behavior for each
method. In this case, we check the return type of the method to identify it and return a hard-coded value.

Instantiate a Stub Version of the Class

The next step is to instantiate a stub version of the class. The following utility class returns a stub object that you can use as a mock.

```
   public class MockUtil {

      private MockUtil(){}

      public static MockProvider getInstance() {

        return new MockProvider();

      }

      public static Object createMock(Type typeToMock) {

        // Invoke the stub API and pass it our mock provider to create a

        // mock class of typeToMock.

        return Test.createStub(typeToMock, MockUtil.getInstance());

      }

   }

```

This class contains the method `createMock()`, which invokes the `Test.createStub()` method. The `createStub()`
method takes an Apex class type and an instance of the `StubProvider` interface that we created previously. It returns a stub object
that we can use in testing.

Invoke the Stub Method

Finally, we invoke the relevant method of the stub class from within a test class.

```
   @isTest

   public class DateFormatterTest {

      @isTest

      public static void testGetFormattedDate() {

        // Create a mock version of the DateHelper class.

        DateHelper mockDH = (DateHelper)MockUtil.createMock(DateHelper.class);

        DateFormatter df = new DateFormatter();

        // Use the mocked object in the test.

        System.assertEquals('Today\'s date is 8/8/2016', df.getFormattedDate(mockDH));

      }

   }

```

In this test, we call the `createMock()` method to create a stub version of the `DateHelper` class. We can then invoke the
`getTodaysDate()` method on the stub object, which returns our hard-coded date. Using the hard-coded date allows us to test
the behavior of the `getFormattedDate()` method in isolation.


### Apex Developer Guide Deploying Apex

Apex Stub API Limitations

Keep the following limitations in mind when working with the Apex stub API.

**•** The object being mocked must be in the same namespace as the call to the `Test.createStub()` method. However, the
implementation of the `StubProvider` interface can be in another namespace.

**•** You can’t mock the following Apex elements.

**–** Static methods (including future methods)

**–** Private methods

**–** Properties (getters and setters)

**–** Triggers

**–** Inner classes

**–** System types

**–** Classes that implement the `Batchable` interface

**–** Classes that have only private constructors

**•** Iterators can’t be used as return types or parameter types.

SEE ALSO:

[StubProvider Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_System_StubProvider.htm)

[Test.createStub()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_test.htm#apex_System_Test_createStub)

### Deploying Apex

You can't develop Apex in your Salesforce production org. Your development work is done in a sandbox, in a scratch org, or in a Developer
Edition org.

Compile On Deploy

Each org’s Apex code is automatically recompiled before completing a metadata deploy, package install, or package upgrade. Compile
on deploy is enabled automatically for production orgs and full sandboxes to ensure that users don’t experience reduced performance
immediately following a deployment. You can’t disable the compile on deploy option in production orgs.

For developer sandbox, developer pro sandbox, partial copy sandbox, developer, trial, and scratch orgs, this feature is disabled by default.
To enable, select the **Perform Synchronous Compile on Deploy** option under Apex Settings in Setup. Deselect this option if you want
to disable the feature in full sandboxes.

With the Compile on Deploy feature, deployments to the org invoke the Apex compiler and save the resulting bytecode as part of the
deployment. For example, if you deploy a custom field, all the classes that use that custom field are recompiled. A minimal increase in
deployment times can occur, but Apex doesn’t need to be recompiled to process subsequent requests. The slight increase in deployment
time can, in fact, mitigate performance issues for currently active users or processes. Consider enabling this feature in sandboxes or
scratch orgs shared by multiple users for functional testing or used by continuous integration processes.

1. Deploy Apex Using Change Sets
Use change sets to deploy Apex classes and triggers between connected organizations, for example, from a sandbox org to your
production org.

2. Deploy Apex Using Salesforce Extensions for Visual Studio Code and Code Builder
Salesforce Extensions for VS Code and Code Builder are powered by Salesforce CLI and the Salesforce APIs.


Apex Developer Guide Deploying Apex

#### 3. Deploy Apex Using Metadata API

Use Metadata API to deploy customization information, such as custom object definitions for your org.

4. Deploy Apex Using Tooling API
Use Tooling API to deploy Apex classes or Apex triggers. Because Tooling API allows you to change just one element within a complex
type, it is easy to deploy using Tooling API.

5. Deploy Apex Using DevOps Center
Salesforce DevOps Center provides an improved experience around change and release management. Build a pipeline when you
configure DevOps Center and use the pipeline to promote work items through the release lifecycle from development to production.

#### Deploy Apex Using Change Sets

Use change sets to deploy Apex classes and triggers between connected organizations, for example,
from a sandbox org to your production org.

You can create an outbound change set in the Salesforce user interface and add the Apex
components that you want to upload and deploy to the target organization.

SEE ALSO:

_[Sandboxes: Staging Environments for Customizing and Testing](https://help.salesforce.com/s/articleView?id=platform.changesets.htm&type=5&language=en_US)_ : Change Sets

EDITIONS

Available in: Salesforce
Classic

Available in **Enterprise**,
**Performance**, **Unlimited**,
and **Database.com** Editions

#### Deploy Apex Using Salesforce Extensions for Visual Studio Code and Code Builder

Salesforce Extensions for VS Code and Code Builder are powered by Salesforce CLI and the Salesforce APIs.

[Salesforce Extensions for Visual Studio Code support different deployment options based on your role and needs as a customer, system](https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview)
integrator, or independent software vendor (ISV) partner. Salesforce DX supports Org Development and Package Development models
to authorize, create, and deploy code in your project. For information on how to deploy to a Salesforce org with Visual Studio Code, see
[Salesforce Development Models.](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/development-models.html)

Salesforce Code Builder is a web-based integrated development environment that has all the power and flexibility of Visual Studio Code
in your web browser. For information on how to connect an org to your Code Builder environment and deploy your code, see _Code_
_Builder_ [: Quick Start.](https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-quickstart-intro.html)

SEE ALSO:

_[Salesforce Extensions for Visual Studio Code](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-changes.htm)_ : Deploy and Retrieve Code

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_develop_any_org.htm)_ : Develop Against Any Org

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm#cli_reference_project_deploy_start_unified.htm)_ : project deploy start

#### Deploy Apex Using Metadata API

Use Metadata API to deploy customization information, such as custom object definitions for your org.

To deploy custom metadata, use the `Metadata.Operations.enqueueDeployment()` method to asynchronously deploy
[metadata to the current org. For more information, see Operations Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_Metadata_Operations.htm)


### Apex Developer Guide Apex in Managed Packages

[Note: If a single deployment has over 2,000 Apex classes, ApexCodeCoverage objects for the deployed classes are deleted even](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_apexcodecoverage.htm)
if the deployment fails or is rolled back. ApexCodeCoverageAggregate objects aren’t affected.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_deploy.htm)_ : deploy()

_[Using Salesforce Features with Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_metadata.htm)_ : Metadata

#### Deploy Apex Using Tooling API

Use Tooling API to deploy Apex classes or Apex triggers. Because Tooling API allows you to change just one element within a complex
type, it is easy to deploy using Tooling API.

[Use ContainerAsyncRequest to compile and deploy the changes with ApexTriggerMember, ApexComponentMember, and](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_containerasyncrequest.htm)
ApexPageMember.

SEE ALSO:

_Tooling API_ [: When to Use Tooling API](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/intro_tasks.htm)

#### Deploy Apex Using DevOps Center

Salesforce DevOps Center provides an improved experience around change and release management. Build a pipeline when you
configure DevOps Center and use the pipeline to promote work items through the release lifecycle from development to production.

For information, see _Manage and Release Changes Easily and Collaboratively with DevOps Center_ [: Promote Work Items Through Your](https://help.salesforce.com/s/articleView?id=platform.devops_center_work_items_promote.htm&type=5&language=en_US)
[Pipeline.](https://help.salesforce.com/s/articleView?id=platform.devops_center_work_items_promote.htm&type=5&language=en_US)

### Apex in Managed Packages

Learn how to develop, distribute, and use managed Apex. Apex in managed packages can behave differently than Apex in unmanaged
packages or Apex deployed directly to an org. Managed package developers and subscribers must understand these differences so that
they can safely evolve their packages and integrations.

Managed Package Types
Salesforce supports the creation and distribution of Apex through different types of packages. Understand the distinctions between
package types, and recognize that Apex behavior can vary across them.

Develop and Distribute Apex for Managed Packages
As an independent software vendor (ISV) or Salesforce partner, you can distribute Apex code to customer orgs by using managed
packages. For first-generation managed packages (1GP) and migrated second-generation managed packages (2GP), use versioning
to evolve components of your managed package gracefully without breaking existing customer integrations. Understand how global
Apex in managed packages behaves and learn how to develop global Apex in managed packages specifically for agents.

Use Apex Referenced by Managed Packages
Learn how to use managed Apex effectively as a managed package subscriber.

Safely Upgrade Packages from Developer and Subscriber Perspectives
Learn how to upgrade a managed package safely through this extended example. See the actions that package developers and
subscribers can take to ensure a smooth transition and safeguard the backwards compatibility of existing integrations.


Apex Developer Guide Apex in Managed Packages

#### Managed Package Types

Salesforce supports the creation and distribution of Apex through different types of packages. Understand the distinctions between
package types, and recognize that Apex behavior can vary across them.

A _package_ is a container that can be as small as an individual component or as large as a set of related apps. After creating a package,
you can distribute it to other Salesforce users and orgs, including orgs outside of your company.

Developers can create unmanaged packages and managed packages. These package types have different use cases and characteristics.

[Unmanaged packages are best suited for one-time drops of apps that require customization after installation. After the components are](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_developing_unmanaged.htm)
installed from an unmanaged package, the components can be edited in the org that they’re installed in. The developer who created
and uploaded the unmanaged package has no control over the installed components, and can’t change or upgrade them.

[Managed packages are ideal for commercial distribution through the AppExchange. Unlike unmanaged packages, package developers](https://appexchange.salesforce.com/)
can upgrade managed packages and push these changes to subscriber orgs. Preserving the backwards-compatibility of managed
packages is the package developer’s responsibility. However, Salesforce provides significant guardrails and tools that help package
developers safely upgrade managed packages while minimizing the risk of introducing changes that may break existing code.

[Salesforce supports first-generation managed packages (1GP) and second-generation managed packages (2GP). Salesforce also supports](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sharing_apps.htm)
[the conversion and migration of 1GP managed packages to 2GP managed packages. For new apps, we recommend using 2GP managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/move_to_second_gen_pkg.htm)
[packages, as they allow for source-driven development and flexible versioning. See Why Switch to Second-Generation Managed Packaging](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/why_switch_2GP.htm)
[and Comparison of First- and Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_comparison.htm)

Apex classes and triggers from 1GP, 2GP, and migrated 2GP managed packages can behave differently depending on the managed
package type. If a section of the _Apex Developer Guide_ or the _Apex Reference Guide_ doesn’t specify whether a behavior applies to only 1GP
or 2GP, then it applies to all managed package types.

SEE ALSO:

_[ISVforce Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/packaging_intro.htm)_

_[First-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/move_to_second_gen_pkg.htm)_ : Move to 2GP

_Second-Generation Managed Packaging Developer Guide_ [: Components Available in Second-Generation Managed Packages–Apex](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_apex_class)
[Class](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_apex_class)

#### Develop and Distribute Apex for Managed Packages

As an independent software vendor (ISV) or Salesforce partner, you can distribute Apex code to customer orgs by using managed
packages. For first-generation managed packages (1GP) and migrated second-generation managed packages (2GP), use versioning to
evolve components of your managed package gracefully without breaking existing customer integrations. Understand how global Apex
in managed packages behaves and learn how to develop global Apex in managed packages specifically for agents.

As you develop managed Apex, keep these points in mind.

**•** The code contained in an Apex class, trigger, or Visualforce component that’s part of a managed package is obfuscated. You generally
can’t view this code in an installing org. The only exceptions are methods declared as `global` . You can view global method
signatures in an installing org. In addition, license management organization users with the View and Debug Managed Apex
permission can view their packages’ obfuscated Apex classes when logged in to subscriber orgs via the Subscriber Support Console.

**•** 1GP managed packages each have a unique namespace. 2GP managed packages can have the same namespace as other 2GP
managed packages. However, you can’t associate a single 2GP managed package with more than one namespace. The namespace
is prepended to your class’s names, methods, variables, and so on, which helps prevent duplicate names in a subscriber’s org.

**•** You can use the `@NamespaceAccessible` on page 111 annotation to make public Apex in a 2GP managed package available
to other 2GP managed packages that use the same namespace.


Apex Developer Guide Apex in Managed Packages

**•** In a single transaction, you can reference only 10 unique namespaces. For example, suppose that you have an object that executes
a class in a managed package when the object is updated. Then that class updates a second object, which in turn executes a different
class in a different package. Even though the first package didn’t access the second package directly, the access occurs in the same
transaction. It’s therefore included in the number of namespaces accessed in a single transaction.

**•** You can use the `@Deprecated` on page 94 annotation to identify methods, classes, exceptions, enums, interfaces, and variables
that can no longer be referenced in subsequent releases of the managed package in which they reside. This annotation is useful
when you’re refactoring code in managed packages as the requirements evolve. See Deprecate Apex in Managed Packages on page
755.

**•** For 1GP and migrated 2GP managed packages, you can write test methods that change the package version context to a different
package version by using the `System.runAs()` method. See Testing Behavior in Package Versions on page 755.

**•** You can’t add a method to a global interface or an abstract method to a global class after you upload that interface or class in a
Managed - Released package version. If the class in the Managed - Released package is virtual, the method that you can add to it
must also be virtual and must have an implementation. If the class in the Managed - Release package extends another class, you
can’t remove the existing class’s contract. See Best Practices for Using Global Apex in Managed Packages on page 757.

Note: If a `ConnectApi` class has a dependency on Chatter, the code can be compiled and installed in orgs that don’t have
Chatter enabled. However, if Chatter isn’t enabled, the code throws an error at run time. See Packaging `ConnectApi` Classes
on page 460.

Apex Versioning in Managed Packages
A managed package component can exhibit different behavior in different package versions. By versioning managed Apex, you can
add and refine components in the managed package, while maintaining backwards compatibility for existing subscribers.

Version Apex Code Behavior
Package developers can use conditional logic in Apex classes and triggers to exhibit different behavior for different versions. With
this conditional logic, you can support existing behavior in classes and triggers in previous package versions while evolving the code.

Apex Code Items That Aren’t Versioned
Some Apex items in managed packages can’t be versioned. The changes that you make to these items are reflected across all package
versions. Additionally, there are limitations to the changes that you can make to some of these items when they are used in Apex
code in managed packages.

Deprecate Managed Apex
Use the `@Deprecated` annotation to specify Apex identifiers that can subscribers can no longer reference in subsequent releases
of the managed package. Deprecation is useful when you’re refactoring code in managed packages as the requirements evolve.

Testing Versioned Behavior in Apex Code
When you change the behavior in an Apex class or trigger for different package versions, it’s important to test that your code runs
as expected in the different package versions. You can write test methods that change the package version context to a different
package version by using the `System.runAs` method. You can only use `System.runAs` in a test method.

Best Practices for Using Global Apex in Managed Packages
As an independent software vendor (ISV) developer, understand when and how to use `global` Apex in managed packages. Learn
design patterns that maximize flexibility and comply with the strict manageability rules applied to `global` Apex after your managed
package’s release. By following these best practices, you can improve the stability and maintainability of your API.

Design Managed Apex for Agentforce
As an independent software vendor (ISV) developer, you can build custom agent actions using Apex and distribute them in managed
packages. To ensure that subscriber admins can declaratively configure your Apex agent actions and that Agentforce can invoke
the actions at run time, follow these requirements and recommendations.


Apex Developer Guide Apex in Managed Packages

##### Apex Versioning in Managed Packages

A managed package component can exhibit different behavior in different package versions. By versioning managed Apex, you can add
and refine components in the managed package, while maintaining backwards compatibility for existing subscribers.

A package version is a number that identifies the set of components uploaded in a package. The version number has the format
_`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major and minor numbers increase to a chosen value
during every major release. The _`patchNumber`_ is generated and updated only for a patch release.

Unmanaged packages aren’t upgradeable, so each package version is simply a set of components for distribution. A package version
has more significance for managed packages. With managed packages, you can specify different component behavior based on the
package version. This practice allows you to evolve the components in your managed package without breaking existing subscriber
integrations.

When an existing subscriber installs a new package version, there’s still only one instance of each component in the package. However,
the components can emulate older versions. For example, a subscriber can use a managed package that contains an Apex class. If the
publisher decides to deprecate a method in the Apex class and release a new package version, the subscriber still sees only one instance
of the Apex class after installing the new version. However, this Apex class can still emulate the previous version for any code that
references the deprecated method in the older version.

SEE ALSO:

##### Version Apex Code Behavior

Apex Code Items That Aren’t Versioned

Deprecate Managed Apex

Testing Versioned Behavior in Apex Code

Set Package Versions for Apex Classes and Triggers (for package subscribers)

##### Version Apex Code Behavior

Package developers can use conditional logic in Apex classes and triggers to exhibit different behavior for different versions. With this
conditional logic, you can support existing behavior in classes and triggers in previous package versions while evolving the code.

Note: Starting in Summer ’25, package subscribers can use Version Settings to specify the version of a migrated second-generation
managed package (2GP) that an Apex class depends on. This functionality is already available to first-generation managed packages
[(1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings in Migrated](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)
[Second-Generation Managed Packages (2GP).](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)

When subscribers install multiple versions of your package and write code that references Apex classes or triggers in your package, they
must select the version that they’re referencing. Within the Apex code that is being referenced in your package, you can conditionally
execute different code paths based on the version setting of the calling Apex code that is making the reference. The package version
setting of the calling code can be determined within the package code by calling the `System.requestVersion` method. In this
way, package developers can determine the request context and specify different behavior for different versions of the package.

This example uses the `System.requestVersion` method and instantiates the `System.Version` class to define different
behaviors in an Apex trigger for different package versions.

```
   trigger oppValidation on Opportunity (before insert, before update) {

      for (Opportunity opp : Trigger.new){

        // Add a new validation to the package

        // Applies to versions of the managed package greater than 1.0

        if (System.requestVersion().compareTo(new Version(1,0)) > 0) {

```


Apex Developer Guide Apex in Managed Packages

```
           if (opp.Probability >= 50 && opp.Description == null) {

             opp.addError('All deals over 50% require a description');

           }

        }

        // Validation applies to all versions of the managed package.

        if (opp.IsWon == true && opp.LeadSource == null) {

           opp.addError('A lead source must be provided for all Closed Won deals');

        }

      }

   }

```

[For a full list of methods that work with package versions, see Version Class and the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_version.htm) `System.requestVersion` [method in System](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm)
[Class.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm)

The request context persists if a class in an installed package invokes a method of another class in the package. For example, imagine
that a subscriber installs a GeoReports package that contains CountryUtil and ContinentUtil classes. The subscriber creates a GeoReportsEx
class and associates it with version 2.3 of the GeoReports package. If GeoReportsEx invokes a ContinentUtil method that internally invokes
a CountryUtil method, the request context propagates from ContinentUtil to CountryUtil. Therefore, the `System.requestVersion`
method in CountryUtil returns version 2.3 of the GeoReports package.

SEE ALSO:

Set Package Versions for Apex Classes and Triggers (for package subscribers)

Safely Upgrade Packages from Developer and Subscriber Perspectives

##### Apex Code Items That Aren’t Versioned

Some Apex items in managed packages can’t be versioned. The changes that you make to these items are reflected across all package
versions. Additionally, there are limitations to the changes that you can make to some of these items when they are used in Apex code
in managed packages.

As a package developer, you can add or remove these items from Apex in manage packages.

**•** `@Future`

**•** `@IsTest`

**•** `with sharing`

**•** `without sharing`

**•** `transient`

You can make limited changes to these Apex items in managed packages.

**•** `private` —can be changed to `global`

**•** `protected` —can be changed to `global`

**•** `public` —can be changed to `global`

**•** `abstract` —can be changed to `virtual` but can’t be removed

**•** `final` —can be removed but can’t be added

You can’t remove or change these Apex items in managed packages.

**•** `global`

**•** `virtual`

You can add the `webservice` keyword, but once it has been added, it can’t be removed.


Apex Developer Guide Apex in Managed Packages

Note: You can’t deprecate `webservice` methods or variables in managed package code.

If a package upgrade includes an explicit global constructor for a released global class that previously only had an implicit constructor,
then the new, explicit constructor will be called from the subscriber. Also, you can’t reduce the access modifier on the default constructor
on a released global class in a package. See Best Practices for Using Global Apex in Managed Packages on page 757.

##### Deprecate Managed Apex

Use the `@Deprecated` annotation to specify Apex identifiers that can subscribers can no longer reference in subsequent releases of
the managed package. Deprecation is useful when you’re refactoring code in managed packages as the requirements evolve.

Apex identifiers include methods, classes, exceptions, enums, interfaces, and variables. After you upload another package version as
Managed — Released, new subscribers that install the latest package version can’t see the deprecated identifiers. However, the identifiers
still function for existing subscribers and API integrations. As the package developer, you can still reference deprecated identifiers
internally.

Note: You can’t use the `@Deprecated` annotation in Apex classes or triggers in unmanaged packages.

You can use Managed — Beta package versions for evaluation and feedback with a pilot set of users in different Salesforce orgs. If you
deprecate an Apex identifier, and then upload a version of the package as Managed — Beta, subscribers that install the package version
still see the deprecated identifier in that package version. If the package developer then uploads a Managed — Released package version,
subscribers will no longer see the deprecated identifier in the package version after they install it.

SEE ALSO:

Best Practices for Using Global Apex in Managed Packages

##### Testing Versioned Behavior in Apex Code

When you change the behavior in an Apex class or trigger for different package versions, it’s important to test that your code runs as
expected in the different package versions. You can write test methods that change the package version context to a different package
version by using the `System.runAs` method. You can only use `System.runAs` in a test method.

This sample shows a trigger with different behavior for different package versions. For more information about defining different behavior
for package versions, see Version Apex Behavior on page 753.

```
   trigger oppValidation on Opportunity (before insert, before update) {

      for (Opportunity opp : Trigger.new){

        // Add a new validation to the package

        // Applies to versions of the managed package greater than 1.0

        if (System.requestVersion().compareTo(new Version(1,0)) > 0) {

           if (opp.Probability >= 50 && opp.Description == null) {

             opp.addError('All deals over 50% require a description');

           }

        }

        // Validation applies to all versions of the managed package.

        if (opp.IsWon == true && opp.LeadSource == null) {

           opp.addError('A lead source must be provided for all Closed Won deals');

        }

      }

   }

```


Apex Developer Guide Apex in Managed Packages

The following test class uses the `runAs` method to verify the trigger’s behavior with and without a specific version:

```
   @IsTest

   private class OppTriggerTests{

     static testMethod void testOppValidation(){

       // Set up 50% opportunity with no description

       Opportunity opp = new Opportunity();

       opp.Name = 'Test Job';

       opp.Probability = 50;

       opp.StageName = 'Prospect';

       opp.CloseDate = System.today();

       // Test running as latest package version

       try{

         insert opp;

       }

       catch(DMLException e){

         Assert.isTrue(

            e.getMessage().contains(

             'All deals over 50% require a description'),

              e.getMessage());

       }

       // Run test as managed package version 1.0

       System.runAs(new Version(1,0)){

         try{

            insert opp;

         }

         catch(DMLException e){

            Assert.isFalse(false, e.getMessage());

         }

       }

       // Set up a closed won opportunity with no lead source

       opp = new Opportunity();

       opp.Name = 'Test Job';

       opp.Probability = 50;

       opp.StageName = 'Prospect';

       opp.CloseDate = System.today();

       opp.StageName = 'Closed Won';

       // Test running as latest package version

       try{

         insert opp;

       }

       catch(DMLException e){

         Assert.isTrue(

           e.getMessage().contains(

            'A lead source must be provided for all Closed Won deals'),

             e.getMessage());

       }

       // Run test as managed package version 1.0

```


Apex Developer Guide Apex in Managed Packages

```
       System.runAs(new Version(1,0)){

         try{

            insert opp;

         }

         catch(DMLException e){

            Assert.isTrue(

              e.getMessage().contains(

               'A lead source must be provided for all Closed Won deals'),

                  e.getMessage());

         }

       }

     }

   }

##### Best Practices for Using Global Apex in Managed Packages

```

As an independent software vendor (ISV) developer, understand when and how to use `global` Apex in managed packages. Learn
design patterns that maximize flexibility and comply with the strict manageability rules applied to `global` Apex after your managed
package’s release. By following these best practices, you can improve the stability and maintainability of your API.

Important: We recommend using the `global` access modifier only when necessary. The API shape of `global` Apex, such
as the name, parameters, and return type of `global` methods, is subject to strict manageability rules. You generally can’t change
the API shape of `global` Apex after it’s released in a managed package.

The `global` modifier on page 68 provides the widest level of access. It makes your Apex classes, methods, interfaces, and variables
accessible and callable from any Apex code outside of your package namespace, including code written by subscribers or other installed
packages.

A key benefit of Apex in managed packages is Intellectual Property (IP) protection. Although `global` Apex signatures, such as `global`
class and method names, parameters, and return types, are visible so subscribers can use your API, the underlying implementation logic
within your methods is encapsulated and hidden. This allows you to provide powerful functionality without exposing your proprietary
source code.

When to Use Global Apex in Managed Packages

Use `global` Apex when:

**•** Exposing a global API. You intend for subscribers to use your package’s core services by directly calling your Apex methods or
instantiating your classes from their own Apex code, such as from their triggers, batch classes, or other custom logic.

**•** Providing extensibility points. You’re designing `global` interfaces or `global abstract` base classes that subscribers must
implement or extend to customize or enhance specific behaviors within your app.

**•** Creating web service endpoints. You’re exposing Apex classes to handle incoming REST API requests or SOAP web service calls from
external systems. These endpoint classes and their methods must be declared `global` to receive calls from external systems.

Avoid `global` Apex for:

**•** Internal package functionality, meaning any Apex code, such as business logic, helper classes, or utility methods, that’s designed
exclusively for use within your managed packages. For these internal components, access modifiers on page 68 such as `public`,

`protected`, or `private` avoid the manageability constraints of `global` . You can even combine the `public` access modifier
with the `@NamespaceAccessible` annotation to allow access throughout your package namespace.

**•** Controller methods, or methods within your package that are called by your Lightning web components (LWC) and aren’t used by
your subscribers directly. Make these methods `public` and annotate them with `@AuraEnabled` on page 94.


Apex Developer Guide Apex in Managed Packages

**•** Method signatures with external `global` types. Avoid using `global` Apex types from another managed package as parameters
or return types in your own `global` methods. This practice locks your package into a rigid dependency. If the other package later
changes or deprecates the types that your `global` signature relies on, it can become difficult or impossible for your package to
adopt newer versions of the dependency package.

Global Apex Manageability Rules

The decision to use `global` is significant because it subjects your code to strict _manageability rules_ after your package is released.
Manageability rules protect subscribers against package upgrades that break existing functionality. These rules make your initial `global`
Apex design critical, as changes in later versions are heavily restricted.

After your managed package is released, these restrictions apply to the `global` Apex in the package.

**•** You can’t delete a `global` class, interface, method, variable, or enum.

**•** You can’t change the name of a `global` class, interface, method, variable, or enum.

**•** You can’t change the access modifier of a `global` class, interface, method, variable, or enum from `global` to another access
modifier.

**•** You can’t change a `global` method’s signature, including the order, number, and types of parameters, as well as the method’s
return type. You can add new methods that overload existing `global` methods.

**•** You can’t change the value of a `global static final` variable.

**•** You can’t change the data type of a `global` variable to an incompatible one.

**•** You can’t change most annotations or modifiers on `global` members. For example, you can’t add or remove the `@AuraEnabled`
annotation or any Apex REST annotation on page 329 from a `global` method. Similarly, you can’t add or remove the `static`
or `final` keyword from a `global` method.

**•** You can’t remove a zero-argument constructor from a `global` class. This restriction applies both to explicitly deleting a constructor
you wrote, and to implicitly removing the default constructor by adding a new constructor that requires arguments.

**•** You can’t remove a `global` interface from a `global` class.

**•** You can’t extend a `global` interface with a new interface.

**•** You can’t change a `global` class to an interface, or vice versa.

**•** You can’t add `abstract` methods to `global` interfaces or `abstract` classes.

**•** You can’t add `final` methods to `global virtual` or `global abstract` classes.

**•** You can’t remove or reorder `global` enum values, although you can add new enum values.

**•** You can't add, remove or change that a global class extends another global class.

Given the strict manageability rules, a thoughtful design of your package’s global API is crucial. These best practices for defining and
managing `global` Apex promote flexibility, reduce maintenance, and help create a stable, evolvable API.

Only Use Global When Necessary

When designing `global` Apex, expose the fewest `global` members possible. Every `global` part of your package is a contract
with your subscribers. Fewer `global` members mean fewer restrictions and more freedom for you to update your package later.

Before making something `global`, consider these questions.

**•** Is it truly necessary? Can you use `public` instead? For example, use `public` for access only by other Apex within the same
package, or `public` and `@NamespaceAccessible` for access only by other Apex in packages that have the same namespace.

**•** Are there other designs? Can you achieve the same result without making methods or classes `global` ?


Apex Developer Guide Apex in Managed Packages

Delegate from Thin Global Entry Points

Make your `global` classes and methods act only as thin entry points. Place any business logic or complex processes in `public`
classes and methods within your package. The `global` method then calls these `public` methods.

Delegating logic to `public` classes and methods promotes:

**•** Flexibility. You can freely add new features or completely change the internal public implementation of your service in future versions
without altering the `global` method signature.

**•** Maintainability. Fixing bugs and refactoring your existing business logic is now safer and lower-risk because the work is decoupled
from the stable global API contract that your subscribers depend on.

**•** Testability. Your `public` business logic classes can be unit tested thoroughly and independently of their `global` entry point.

Example: In this example, `MyPackageApi.greetUsers` is the stable `global` contract. The actual work happens in
`createGreetings`, which is `public` and can be easily modified in future package versions as long as the `greetUsers`
signature in `MyPackageApi` remains unchanged. For example, the ISV developer can later optimize `createGreetings`
or add new helper methods without violating `global` Apex manageability rules.

```
      // --- ISV's Managed Package Code --
      // Global Entry Point

      global with sharing class MyPackageApi {

        // Note: This is a simplified example using a primitive data type. For a

        // more flexible and future-proof design, we recommend using parameter

        // objects for global method signatures, as explained in the next section.

        global static List<String> greetUsers(List<String> userNames) {

             // Delegate directly to a public class to do the actual work.

             // GreetingService is a 'public' class within your package.

           GreetingService service = new GreetingService();

             return service.createGreetings(userNames);

        }

      }

      // Public Class (Lives inside your package)

      // This class can be updated easily in future package versions.

      public with sharing class GreetingService {

        // This public method contains all the business logic to process a list of names.

        public List<String> createGreetings(List<String> names) {

           List<String> greetings = new List<String>();

           // Input validation and error handling, e.g. Return an empty list if input is

      null or empty.

           // Process each name in the list.

           for (String name : names) {

             greetings.add('Hello, ' + name + '!');

           }

           return greetings;

        }

        // If needed, you can freely add private methods here

        private void someHelperMethod() {

           // ...

        }

      }

```


Apex Developer Guide Apex in Managed Packages

```
      // --- Subscriber Code --
      // Subscriber creates a list and calls the global method

      List<String> welcomeMessages = TheIsvNamespace.MyPackageApi.greetUsers(

        new List<String>{'Jane Doe', 'Rose Gonzalez'});

      // The output is a corresponding list of greetings.

      // welcomeMessages will be: ['Hello, Jane Doe!', 'Hello, Rose Gonzalez!']

```

Use Parameter Objects for Global Method Inputs and Return Types

Using primitive data types, such as String or ID, directly in `global` method signatures creates a rigid contract that you can’t change.
To avoid this restriction, we recommend using custom `global` Apex classes as parameter objects for both inputs and outputs. This
pattern provides a stable API contract that’s evolvable, safer, and readable for subscribers.

Benefits of using parameter objects include:

**•** Evolvability. You can add new parameters to your API by adding new properties to your input or output classes. The `global`
method signature itself never changes, which avoids breaking changes.

**•** Safety and discoverability. Subscribers get compile-time safety and code completion while constructing the request object, which
reduces the risk of run-time errors from typos or incorrect data types.

**•** Readability. Grouping related parameters into a dedicated class makes your method signature clean and its purpose clear. For
example, `getCoordinates(Address location)` is easier for your subscribers to understand and use than

```
    getCoordinates(String street, String city, String state, String zip, ...).

```

Despite the benefits of using parameter objects, consider these costs.

**•** Increased upfront complexity. This pattern requires more initial code, such as multiple classes, and can be excessive for simple actions
that aren’t expected to change.

**•** Expanded global surface area. Although the primary method signature remains stable, each global property added to the input
object becomes a new, permanent part of your package’s API.

Example: In this example, the `GeocodingService.getCoordinates` method is the global contract. It uses the custom

`global AddressRequest` class as its input, and the custom `global GeolocationResponse` class as its output.

```
      // --- ISV's Managed Package Code --
      // The global entry point class contains the global method and input & output wrapper

      inner classes.

      global with sharing class GeocodingService {

        // 1. The Global Method

        // The signature is clean, using the inner classes for its input parameter and

      return type.

        global static GeolocationResponse getCoordinates(AddressRequest location) {

           // --- Internal logic to process the request --
          // We recommend calling a public method to delegate all business logic. Skipping

      this for brevity in this example

           // This could involve callouts to an external geocoding service.

           // For this example, we will return mock data.

           if (location.postalCode == '94105') {

             return new GeolocationResponse(37.7749, -122.4194);

           } else {

        return new GeolocationResponse(0, 0);

       }

        }

```


Apex Developer Guide Apex in Managed Packages

```
        // 2. The Input Parameter Object (as an inner class)

        // A simple inner class with global properties to bundle input parameters.

        global with sharing class AddressRequest {

           global String street;

           global String city;

           global String state;

           global String postalCode;

           // A constructor helps ensure required fields are provided.

           global AddressRequest(String street, String city, String state, String

      postalCode) {

             this.street = street;

             this.city = city;

             this.state = state;

             this.postalCode = postalCode;

           }

        }

        // 3. The Output Parameter Object (as an inner class)

        // A simple inner class to provide a structured result.

        global with sharing class GeolocationResponse {

           // Using 'private set' makes these properties read-only for subscribers.

           // @AuraEnabled makes these properties visible to Lightning web components,

      if necessary.

           @AuraEnabled global Decimal latitude { get; private set; }

           @AuraEnabled global Decimal longitude { get; private set; }

           // This constructor is public, not global, so subscribers can't create their

      own response objects.

           public GeolocationResponse(Decimal lat, Decimal lon) {

             this.latitude = lat;

             this.longitude = lon;

           }

        }

      }

      // --- Subscriber Code --
      // The subscriber's experience is clean and type-safe.

      // 1. Create an instance of the input object, referencing it via the outer class.

      TheIsvNamespace.GeocodingService.AddressRequest sfAddress = new

      TheIsvNamespace.GeocodingService.AddressRequest(

        '415 Mission St',

        'San Francisco',

        'CA',

        '94105'

      );

      // 2. Call the global method with the single parameter object.

      TheIsvNamespace.GeocodingService.GeolocationResponse coordinates =

      TheIsvNamespace.GeocodingService.getCoordinates(sfAddress);

      // 3. Process the structured, strongly-typed result.

      // For this example we will just log the results.

```


Apex Developer Guide Apex in Managed Packages

```
        System.debug('Coordinates found: ' + coordinates.latitude + ', ' +

      coordinates.longitude);

```

Alternative for Unpredictable Inputs: The Map Pattern

For scenarios where the inputs aren’t known at compile time, you can use a Map for your method’s input parameters. An example
signature with this pattern is `global static GeolocationResponse`
`processUnstructuredRequest(Map<String, Object> inputs)` .

Important: Use this pattern with caution. This pattern isn’t recommended for return types.

Accepting a Map allows the subscriber to construct the Map and populate the keys and values themselves. Although this pattern provides
maximum flexibility, returning a Map forces the subscriber to guess key names and data types, which leads to fragile code.

Additionally, using a Map for inputs sacrifices compile-time safety and discoverability. Subscribers must rely entirely on documentation
to know the required keys and their data types. Simple typos in map keys can result in hard-to-debug run-time errors instead of
compile-time errors.

[Note: The standard Callable interface uses the Map pattern through its](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_System_Callable.htm) `call(String action, Map<String,`

`Object> args)` method. However, this method returns a generic Object, which forces subscribers to cast the response and
risk run-time errors. It creates a single, generic entry point that can perform many different functions based on the action string.
For a single-purpose action that accepts unstructured inputs, a custom method such as `processUnstructuredRequest`
is clearer and safer.

Instead of using the Map pattern, prefer strongly-typed parameter objects as shown in the Use Parameter Objects for Global Method
Inputs and Return Types on page 760 section. Reserve the Map pattern for advanced use cases where the inputs are truly unpredictable
and its risks are acceptable, but always return a strongly-typed object.

Use Global Interfaces with Factory Methods

The _facade pattern_ is effective if you want to define a capability and then provide one or more ways to use it. In this pattern, a global
interface defines the capability, and the public classes that implement the interface define how to use the capability. A global factory
method gives the subscriber the specific implementation of the interface.

Benefits of using the facade pattern include:

**•** You can change the public class that does the work as long as it still follows the global interface rules.

**•** You can offer new implementations of the interface later.

Example: In this example, `Notifier` is the `global` contract, and the `public` class `EmailNotifierImpl` does the
work. Because the factory class is `global` but the classes that implement the `Notifier` interface are `public`, the ISV
developer can later change or add to these classes. For example, if the ISV developer later wants to offer an SMS notifier, they can
add `getSmsNotifier()` to the factory class and implement a new `public SmsNotifierImpl` class.

```
      // --- ISV's Managed Package Code --
      // Global Interface - Defines a capability

      global interface Notifier {

        global void send(String message);

      }

      // Global Factory Class - Provides instances

      global with sharing class NotificationFactory {

        global static Notifier getEmailNotifier() {

           return new EmailNotifierImpl(); // EmailNotifierImpl is public

```


Apex Developer Guide Apex in Managed Packages

```
        }

      }

      // Public Implementation (Lives inside your package)

      public with sharing class EmailNotifierImpl implements Notifier {

        public void send(String message) {

           // Logic to send an email (simplified here)

           System.debug('Emailing: ' + message);

        }

      }

      // --- Subscriber Code --
      // Subscriber gets an instance of a Notifier

      Notifier myEmailer = NotificationFactory.getEmailNotifier();

      // Subscriber uses the interface method

      myEmailer.send('Welcome to our service!'); // Outputs: Emailing: Welcome to our service!

```

Strategies for Retiring Global Apex

Even though deprecating Apex on page 755 only affects future versions of your package, phasing out a `global` Apex member requires
careful planning and clear communication to prevent subscriber disruption.

Here’s some recommendations for effectively retiring a `global` Apex member.

**•** Communicate early and clearly. Inform subscribers well in advance—ideally, multiple release cycles—of any deprecation. Explain
reasons, timelines, and migration paths. Update the documentation, and share it prominently.

**•** Provide alternatives. Release well-documented and robust alternatives before or concurrent with the deprecation announcement.

**•** Implement soft deprecation with non-breaking warnings.

**–** Add the `@Deprecated` annotation to the `global` member. This annotation generates compile-time warnings in developer
tools, but doesn’t alter run-time behavior.

**–** Consider run-time logging when the deprecated member is invoked, guiding subscribers to the new alternative.

Note: You can’t remove the `@Deprecated` annotation to undeprecate something in Apex after you’ve released a
package version where that item in Apex is deprecated. You also can’t add new `global` access modifiers to a

`@Deprecated` type.

**•** Enforce non-operation with exceptions. Change the code to throw an informative exception, such as
`FeatureDeprecatedException('` _**`Method X is retired. Use Method Y.`**_ `')` . This breaking change at run
time stops the old logic from running and forces attention to the deprecation. However, any breaking change requires extensive
prior communication.

**•** Retire code for obsolete `global` Apex. After ample time and communication, confirm that subscribers are no longer using the
deprecated `global` member. Then minimize the member’s internal code. Although the `global` signature must remain, its logic
can become non-operational (no-op), return a safe default, or throw a specific `Feature Retired` exception. Implementing
these changes reduces the risk and effort of maintaining the old code.


Apex Developer Guide Apex in Managed Packages

Always thoroughly test changes related to deprecating `global` Apex, including testing your package’s behavior if a subscriber attempts
to call the deprecated member. The goal is a graceful transition for your subscribers.

SEE ALSO:

Access Modifiers

Apex Class Definition

Exposing Apex Classes as REST Web Services

Exposing Apex Methods as SOAP Web Services

NamespaceAccessible Annotation Annotation

Deprecate Managed Apex

_[Apex Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_System_Callable.htm)_ : Callable Interface

_Second-Generation Managed Packaging Developer Guide_ [: Components Available in Second-Generation Managed Packages–Apex](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_apex_class)
[Class](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_apex_class)

##### Design Managed Apex for Agentforce

As an independent software vendor (ISV) developer, you can build custom agent actions using Apex and distribute them in managed
packages. To ensure that subscriber admins can declaratively configure your Apex agent actions and that Agentforce can invoke the
actions at run time, follow these requirements and recommendations.

Use Global Apex

[For Agentforce to use Apex agent actions in managed packages, these Apex members must have the](https://help.salesforce.com/s/articleView?id=ai.copilot_actions.htm&type=5&language=en_US) `global` access modifier on page
68.

**•** The Apex class containing the `@InvocableMethod` on page 96 that defines the agent action.

**•** The input wrapper class that defines the parameters an admin can configure for the action, and the output wrapper class that defines
the structured result returned to Agentforce.

**•** All `@InvocableVariable` on page 101 members within these input and output wrapper classes.

**•** Any custom Apex data types used as properties in your wrapper classes.

Important: If any of these Apex members aren’t `global`, then the Apex agent action can’t be invoked by Agentforce at run
time.

These Apex members must be `global` because Agentforce agents currently can’t be packaged directly, and therefore can’t have a
namespace. By definition, this means that Apex agent actions don’t have access to non- `global` Apex, such as `public` Apex, that’s
part of a managed package and does have a namespace.

Importantly, managed `global` Apex is subject to stricter manageability rules than managed non- `global` Apex. See the Global Apex
Manageability Rules on page 758 section of Best Practices for Using Global Apex in Managed Packages on page 757.

Although `global` Apex is required for any direct entry point to an agent action, delegate any business logic or heavy lifting to `public`
classes and methods. See the Delegate from Thin Global Entry Points on page 759 section of Best Practices for Using Global Apex in
Managed Packages on page 757.

Use @InvocableMethod to Define the Action

To define an Apex agent action, use the `@InvocableMethod` on page 96 annotation and follow these requirements.

**•** Your Apex method must be `global static` .


Apex Developer Guide Apex in Managed Packages

**•** Your Apex method must be annotated with `@InvocableMethod (label='` _**`Your Action Name`**_ `'`

```
    description=' Clear, concise description of what the action does ' category=' Your ISV
```

_**`App Name`**_ `')` .

**–** Use clear and descriptive `label` and `description` modifiers. The Agentforce reasoning engine uses them to determine
[when to invoke the action. Subscriber admins configuring Agentforce also use them to help decide which agent topics to add](https://help.salesforce.com/s/articleView?id=ai.copilot_topics.htm&type=5&language=en_US)
the action to.

**–** Use the `category` modifier to help organize actions. We recommend using your ISV app name.

Note: Only one method in a class can have the `@InvocableMethod` annotation. Create a separate `global` Apex class for
each agent action in your managed package.

Structure Inputs and Outputs with Global Wrapper Classes

In addition to the requirements of using `global` Apex and the `@InvocableMethod` annotation, we also recommend using
custom `global` classes to structure input and output parameters. By using parameter objects, you avoid changing the `global`
method signature when you modify the parameters of the agent action. To learn how to use this pattern, see the Use Parameter Objects
for Global Method Inputs and Return Types on page 760 section of Best Practices for Using Global Apex in Managed Packages on page
757. Then review these targeted guidelines to implement Apex agent actions using this pattern.

Because you can’t change managed `global` method signatures, make signatures flexible.

**•** Define `global` inner Apex classes to serve as containers for input and output parameters. These classes can be in the same top-level
class as the invocable method.

**•** Annotate both input and output classes with `@JsonAccess(serializable='always'`

`deserializable='always')` . The @JsonAccess annotation on page 110 governs the serialization and deserialization of
managed Apex. Because Agentforce serializes and deserializes complex Apex types from an unmanaged context at run time, both
`@JsonAccess` parameters must be set to `'always'` .

**•** Within these input and output classes, declare `global` member variables annotated with

```
    @InvocableVariable(label=' User-Friendly Name ' description=' Description of this
```

_**`parameter`**_ `' required=true/false)` .

**–** Use clear and descriptive `label` and `description` modifiers, so that subscribers can configure the inputs declaratively,
and Agentforce can understand the output.

**–** Set the `required` modifier as `true` or `false` to specify whether the input is required for the agent action to run. This
modifier also helps subscriber admins configure your actions.

**•** Define the invocable method to accept a `List` of its input class type, for example `List<MyInputAction> requests` .

**•** Define the invocable method to return a `List` of its output class type, for example `List<MyOutputAction> results` .

Example Code for an Apex Agent Action

In this example, the `getCoordinates` method is defined as an `@InvocableMethod` so it can be invoked by Agentforce. The
method accepts a list of `GeocodingRequest` objects and returns a corresponding list of `GeocodingResponse` objects. The
input and output wrapper classes are both annotated with `@JsonAccess(serializable='always'`

`deserializable='always')` so Agentforce can serialize and deserialize the objects from an unmanaged context. The properties
of both wrapper classes are defined as `@InvocableVariable` so an admin can configure them declaratively. The `label` and
`description` modifiers in both `@InvocableMethod` and `@InvocableVariable` are important because they help the
Agentforce reasoning engine to understand how to use the action.

```
   // --- ISV's Managed Package Code --
   // --- 1. The Global Entrypoint Class --
```


Apex Developer Guide Apex in Managed Packages

```
   // This class contains the @InvocableMethod and the input/output wrapper classes.

   global with sharing class GeocodingAction {

      // This method is the thin, global entry point that delegates any business logic to a

    separate public class.

        @InvocableMethod(

           label='Get Coordinates for Address'

          description='Retrieves the latitude and longitude for a given street address.'

           category='My ISV App Name'

        )

       global static List<GeocodingResponse> getCoordinates(List<GeocodingRequest> requests)

    {

           // Delegate the entire list to the internal logic class to ensure

           // any callouts or DML can be performed in bulk.

             GeocodingLogic logic = new GeocodingLogic();

             return logic.performGeocoding(requests);

        }

        // --- Input Wrapper Inner Class --
        // Defines the parameters an admin can configure for this action.

        @JsonAccess(serializable='always' deserializable='always')

        global with sharing class GeocodingRequest {

           @InvocableVariable(label='Street' required=true)

           global String street;

           @InvocableVariable(label='City' required=true)

           global String city;

           @InvocableVariable(label='State/Province' required=true)

           global String state;

           @InvocableVariable(label='Postal Code' required=true)

           global String postalCode;

        }

        // --- Output Wrapper Inner Class --
        // Defines the structured result returned to Agentforce.

        @JsonAccess(serializable='always' deserializable='always')

        global with sharing class GeocodingResponse {

           @InvocableVariable(label='Was Successful')

           global Boolean isSuccess;

           @InvocableVariable(label='Latitude')

           global Decimal latitude;

           @InvocableVariable(label='Longitude')

           global Decimal longitude;

           @InvocableVariable(label='Error Message')

           global String errorMessage;

        }

      // Static factory methods for creating consistent results.

        public static GeocodingResponse success(Decimal lat, Decimal lon) {

```


Apex Developer Guide Apex in Managed Packages

```
           GeocodingResponse result = new GeocodingResponse();

           result.isSuccess = true;

           result.latitude = lat;

           result.longitude = lon;

           return result;

        }

        public static GeocodingResponse error(String message) {

           GeocodingResponse result = new GeocodingResponse();

           result.isSuccess = false;

           result.errorMessage = message;

           return result;

        }

   }

   // --- 2. The Internal Logic Class (Public, not Global) --
   // This is where the actual business logic lives.

   // It's separate from the global entry point class for better organization and testing.

   public with sharing class GeocodingLogic {

      // Since we defined the inputs and outputs as inner classes, we use dot notation to

   reference them.

      public List<GeocodingAction.GeocodingResponse>

   performGeocoding(List<GeocodingAction.GeocodingRequest> requests) {

        List<GeocodingAction.GeocodingResponse> results = new

   List<GeocodingAction.GeocodingResponse>();

        // This method would contain your complex, bulkified business logic.

        // For example, you can aggregate all requests into a single callout

        // to an external geocoding service.

        // For this simplified example, we loop and return mock results.

        for (GeocodingAction.GeocodingRequest req : requests) {

           // In a real implementation, you would perform a callout and handle errors.

           if (req.postalCode == '94105') {

             results.add(GeocodingAction.success(37.7749, -122.4194));

           } else {

             results.add(GeocodingAction.error('Address could not be found.'));

           }

        }

        return results;

```


Apex Developer Guide Apex in Managed Packages

```
      }

   }

```

SEE ALSO:

Best Practices for Using Global Apex in Managed Packages

Access Modifiers

InvocableMethod Annotation

InvocableVariable Annotation

Use the with sharing, without sharing, and inherited sharing Keywords

Enforce User Mode for Database Operations

_Salesforce Developers Blog_ [: Build Custom Agent Actions Using Apex](https://developer.salesforce.com/blogs/2024/03/build-custom-copilot-actions-using-apex)

#### Use Apex Referenced by Managed Packages

Learn how to use managed Apex effectively as a managed package subscriber.

##### Set Package Versions for Apex Classes and Triggers

As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. Set the
package version in Setup, through metadata deployments, or with API requests.

Managed Apex Considerations for Package Subscribers
As you use managed Apex, keep these considerations in mind.

##### Set Package Versions for Apex Classes and Triggers

As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. Set the
package version in Setup, through metadata deployments, or with API requests.

Note: In Summer ’25 and later, package subscribers can use version settings to specify the version of a migrated second-generation
managed package (2GP) that an Apex class or trigger depends on. This functionality is already available to first-generation managed
[packages (1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)
[in Migrated Second-Generation Managed Packages (2GP).](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)

A package version is a number that identifies the set of components uploaded in a package. The version number has the format
majorNumber.minorNumber.patchNumber (for example, 2.1.3). The major and minor numbers increase to a chosen value during every
major release. The patchNumber is generated and updated only for a patch release.

If you install a new package version, only one instance of each component exists in the package, but the components can emulate older
versions. Say that you use a managed package that contains an Apex class. If the publisher decides to deprecate a method in the Apex
class and release a new package version, you still see only one instance of the Apex class after installing the new version. However, this
Apex class can still emulate the previous version for any code that references the deprecated method in the older version.

By default, an Apex class or trigger that references a managed package is associated with the package version installed when that class
or trigger was last saved or deployed. For example, say that you install version 1.0 of Package A, and then create and deploy an Apex
class that references that managed package. If you upgrade to version 2.0 of Package A but don’t redeploy the class, then the class
remains associated with version 1.0. However, if you upgrade Package A to version 2.0 and then redeploy the class, then the class is now
associated with version 2.0.

You can override the default package version settings for an Apex class or trigger. When set to a specific package version, the class or
trigger views the package’s global Apex as if that version was installed. Explicitly setting a package version is useful if your class or trigger


Apex Developer Guide Apex in Managed Packages

relies on an older shape of a packaged component. For an example where overriding the default package version is vital to maintain
backwards compatibility, see Safely Upgrade Packages from Developer and Subscriber Perspectives on page 771.

SEE ALSO:

Version Apex in Managed Packages (for package developers)

Safely Upgrade Packages from Developer and Subscriber Perspectives

Set a Package Version in Setup

Associate an Apex class or trigger with a specific package version in Setup.

To configure the package version settings for an Apex class or trigger:

**1.** From Setup, enter _`Apex Classes`_ or _`Apex Triggers`_ in the Quick Find box, and then select **Apex Classes** or **Apex Triggers** .

**2.** From the list, click **Edit** for the Apex class or trigger that you want to configure.

**3.** Click the **Version Settings** tab.

**4.** From the Version dropdown for the managed package, select the desired version referenced by the class or trigger.

The class or trigger continues to use this version even if your install later versions of the managed package, unless you manually
update the version setting.

**5.** Click **Save** .

Note: If the package is referenced in the class or trigger, you can’t remove a class or trigger’s version setting for a managed
package. To find where the class or trigger references a managed package, on the class or trigger’s Detail page, click **Show**
**Dependencies** .

Set a Package Version in Metadata API

Associate an Apex class or trigger with a specific package version by using Metadata API.

[With the PackageVersion field, you specify a managed package version in an Apex class or trigger’s metadata.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_classes.htm#PackageVersion)

**1.** Identify the managed package’s reference ID. This ID is either the subscriber package ID for migrated 2GP managed packages or the
package namespace for 1GP managed packages.

**a.** From Setup, in the Quick Find box, enter _`Installed Packages`_, and select **Installed Packages** .

**b.** Locate the installed package that you want to reference and click the Package Name.

**c.** On the Installed Package Detail page, locate the Version Setting field. The field identifies the type of reference ID.

**2.** In the Apex class or trigger’s metadata file, add a `<packageVersions>` element. If your Apex class or trigger references multiple
managed packages, include a separate `<packageVersions>` element for each package.

**3.** Within the `<packageVersions>` element, add the required fields and the desired values.

**•** For migrated 2GP managed packages, add the `packageId` field.

**•** For 1GP managed packages, use the `namespace` field instead.

Example: Here’s an example declarative metadata definition of an Apex class that references a migrated 2GP managed package.

```
      <?xml version="1.0" encoding="UTF-8"?>

      <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

        <apiVersion>66.0</apiVersion>

        <packageVersions>

```


Apex Developer Guide Apex in Managed Packages

```
           <majorNumber>3</majorNumber>

           <minorNumber>0</minorNumber>

           <packageId>033xx0000000001</packageId>

        </packageVersions>

        <status>Active</status>

      </ApexClass>

```

Here’s an example declarative metadata definition of an Apex class that references a 1GP managed package.

```
      <?xml version="1.0" encoding="UTF-8"?>

      <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

        <apiVersion>66.0</apiVersion>

        <packageVersions>

           <majorNumber>3</majorNumber>

           <minorNumber>0</minorNumber>

           <namespace>pkg1</namespace>

        </packageVersions>

        <status>Active</status>

      </ApexClass>

```

Note: **Metadata Usage Note for Migrated 2GP Packages**

If you set a package version for an Apex class or trigger that references a 1GP managed package before Summer ’25, your existing
version settings remain valid when the developer migrates the package to 2GP.

If you retrieve metadata using Salesforce API version 61.0 and earlier, `<namespace>` is still used in the `<packageVersions>`
section of the `meta.xml` file to identify the referenced migrated 2GP package. If you retrieve metadata using API version 62.0
and later, `<packageId>` is used in the `<packageVersions>` section instead.

An error can occur if you deploy metadata using `<packageId>` to an org that still has the 1GP or 2GP pre-migrated version of
the package installed. To resolve this issue, either upgrade the target org to the migrated package, or edit the

`<packageVersions>` section to use `<namespace>` instead.

Set a Package Version in API Requests

Specify a managed package version by using the package version header in your API request.

**1.** Identify the managed package’s reference ID. This ID is either the subscriber package ID for migrated 2GP managed packages or the
package namespace for 1GP managed packages.

**a.** From Setup, in the Quick Find box, enter _`Installed Packages`_, and select **Installed Packages** .

**b.** Locate the installed package that you want to reference and click the Package Name.

**c.** On the Installed Package Detail page, locate the Version Setting field. The field identifies the type of reference ID.

If the Version Setting field is set to `packageID`, then the value of the Package field is the package’s reference ID. If the Version
Setting field is set to `namespace`, then the value of the Namespace field is the package’s reference ID.

**2.** Set the package version header according to the managed package’s reference ID and the desired package version.

**•** For REST API calls, use the `x-sfdc-packageversion-[packageId/namespace]` [header. See Package Version](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/headers_packageversion.htm)
[Header in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/headers_packageversion.htm) _REST API Developer Guide_ .

**•** For SOAP API calls, use the `PackageVersionHeader` [header. See PackageVersionHeader in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_header_packageversionheader.htm) _SOAP API Developer Guide_ .


Apex Developer Guide Apex in Managed Packages

Note: If a package version isn’t specified in a request header, the API client uses the version of the package specified in Setup. To
set this value, from Setup, enter _`API`_ in the Quick Find box and select **API** . Then click **Configure Enterprise Package Version**
**Settings** under Enterprise Package Version Settings.

##### Managed Apex Considerations for Package Subscribers

As you use managed Apex, keep these considerations in mind.

**•** If a package developer deprecates a global Apex identifier in a managed package, you can only reference that identifier if you specify
a package version between the creation and the deprecation of the identifier. Identifiers include global Apex methods, classes,
exceptions, enums, interfaces, properties, and class variables. This behavior applies to both static and dynamic references, such as
identifiers accessed with the `[Type.forName()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_type.htm#apex_System_Type_forName)` method, the `instanceof` [on page 85 keyword, and the ApexTypeImplementor](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_apextypeimplementor.htm)
object.

**•** Similarly, if a package developer deletes a schema from a managed package, you can only reference the schema in Apex if you
specify a package version before the deletion of the schema. This behavior applies to both static and dynamic references, such as
objects and fields accessed with `[Schema.describe()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_schema.htm#apex_System_Schema_methods)` methods.

#### Safely Upgrade Packages from Developer and Subscriber Perspectives

Learn how to upgrade a managed package safely through this extended example. See the actions that package developers and subscribers
can take to ensure a smooth transition and safeguard the backwards compatibility of existing integrations.

These sections follow an example package developer and package subscriber as they move through a managed package upgrade
process.

1. Package Developer: Publishes Version 1.0

The package developer publishes version 1.0 of a 1GP managed package in the `eshop` namespace. The package contains Apex
`CustomCart` and `CartCalculator` classes.

```
   /**

    * CustomCart

    * Simple container for item prices used in a managed package context.

    * @version 1.0

    * @since 1.0

    */

   global with sharing class CustomCart {

      global List<Decimal> itemPrices;

      global CustomCart() {

        this.itemPrices = new List<Decimal>{0.0};

      }

   }

   /**

    * CartCalculator

    * Handles tasks about calculating items and prices in customer carts.

    * @version 1.0

    * @since 1.0

    */

   global virtual class CartCalculator {

      /**

```


Apex Developer Guide Apex in Managed Packages

```
      * Adds item prices in a custom cart.

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total price of items in the

      * cart

      * @version 1.0

      * @since 1.0

      */

      global virtual Decimal getTotalPrice(CustomCart c) {

        Decimal price = 0.0;

        // Add up items in cart

        for (Decimal itemPrice : c.itemPrices) {

           price += itemPrice;

        }

        return price;

      }

   }

```

2. Package Subscriber: Adds Functionality by Overriding a Method

The package subscriber installs version 1.0 of the managed package, but they find that the existing `CartCalculator` class is
inadequate. They want the ability to factor shipping costs into the total cart price.

So, the subscriber extends the `CartCalculator` class in the managed package with a custom
`CartCalculatorWithShipping` class. They override the `getTotalPrice()` method so that the total price includes the
shipping cost.

```
   // Package Subscriber - CartCalculatorWithShipping.cls

   /**

   * Handles tasks about calculating items and prices in customer carts,

   * including shipping costs.

   */

   public with sharing class CartCalculatorWithShipping extends eshop.CartCalculator {

      /**

      * Adds item prices in a cart and adds the shipping cost to the total price.

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total price of items in the

      * cart, including the shipping cost

      */

      public override Decimal getTotalPrice(eshop.CustomCart c) {

        return super.getTotalPrice(c) + getShippingCost(c);

      }

      /**

      * Get the shipping cost based on the items in a customer's cart

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total shipping cost

      * for the cart

      */

      public Decimal getShippingCost(eshop.CustomCart c) {

```


Apex Developer Guide Apex in Managed Packages

```
       // Flat rate shipping

       return 20.0;

      }

   }

```

3. Package Developer: Releases Version 2.0 and Implements the Subscriber’s Custom Functionality

The package developer releases version 2.0 of the managed package. In this version, the `CartCalculator` class now includes a
native shipping cost calculator. The updated `getTotalPrice()` method calls the new `getShippingCost()` method. Notice
that the package developer uses the same method name for `getShippingCost()` as the subscriber does for their custom override
method.

```
   // Package Developer - CartCalculator.cls

   /**

   * Handles tasks about calculating items and prices in customer carts.

   * @version 2.0

   * @since 1.0

   */

   global virtual class CartCalculator {

      /**

      * Adds item prices in a cart, including the shipping cost

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total price of items in the

      * cart, including the total shipping cost

      * @version 2.0

      * @since 1.0

      */

      global virtual Decimal getTotalPrice(CustomCart c) {

        Decimal price = 0.0;

        // Add up items in cart

        for (Decimal itemPrice : c.itemPrices) {

        price += itemPrice;

      }

      return price + getShippingCost(c);

     }

      /**

      * Get the shipping cost based on the items in a customer's cart

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total shipping cost

      * for the cart

      * @version 2.0

      * @since 2.0

      */

      global virtual Decimal getShippingCost(CustomCart c) {

        // Flat rate shipping

        return 20.0;

      }

   }

```


Apex Developer Guide Apex in Managed Packages

4. Package Subscriber: Upgrades to Version 2.0 Without Specifying a Package Version for the Apex
Class

By default, an Apex class or trigger is associated with the version of the managed package installed when the class or trigger was most
recently deployed.

In this example, the package subscriber created and saved the `CartCalculatorWithShipping` class when the `eshop` managed
package was on version 1.0. If the package subscriber upgrades their `eshop` managed package to version 2.0, and doesn’t redeploy
the `CartCalculatorWithShipping` class, then that class is still associated with version 1.0 of the managed package.

Let’s say that the package subscriber upgrades their `eshop` managed package to version 2.0, but does try to redeploy
`CartCalculatorWithShipping` . In this case, the subscriber encounters this compilation error: `Method must use the`
`override keyword: public Decimal getShippingCost(CustomCart c)` .

This error occurs because there’s a mismatch in the shape of the API. The subscriber’s original `CartCalculatorWithShipping`
class has a `getShippingCost()` method, and the `CartCalculator` class in version 2.0 of the managed package now also
includes a `getShippingCost()` method. The subscriber didn’t specify a package version for the
`CartCalculatorWithShipping` class, so upon redeployment, the class is now associated with version 2.0 of the managed
package. Therefore, the subscriber’s `getShippingCost()` method technically overrides the `getShippingCost()` method
in `CartCalculator`, and so the Apex compiler requires an `override` keyword for the method.

5. Package Subscriber: Sets Apex Class to Package Version 1.0

To avoid this compilation error, the package subscriber explicitly sets a package version for the `CartCalculatorWithShipping`
class. When is set to a specific package version, the class views the package’s global Apex as if that version was installed.

In this case, setting `CartCalculatorWithShipping` to version 1.0 of the managed package avoids a compilation error because
the package’s `CartCalculator` class doesn’t define a `getShippingCost()` method until version 2.0. As long as the
`CartCalculatorWithShipping` class is set to an earlier package version, the package’s `CartCalculator` class doesn’t
expose the `getShippingCost()` method to the subscriber. Therefore, the Apex compiler doesn’t flag the subscriber’s own
`getShippingCost()` method as needing to override the method in the managed package.

To override the default package version for an Apex class or trigger, use the Salesforce Setup UI or the `packageVersions` field of
the class’s ApexClass metadata type. See Set Package Versions for Apex Classes and Triggers on page 768.

Note: In Spring ’25 and earlier, setting Apex classes and triggers to a package version was available for only first-generation
managed packages (1GP). In Summer ’25 and later, package version setting is also available for migrated 2GP managed packages.
[Package version setting isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)
[in Migrated Second-Generation Managed Packages (2GP).](https://help.salesforce.com/s/articleView?id=005101483&type=1&language=en_US)

For migrated 2GP managed packages, the `packageVersions` field of the ApexClass metadata type is different from that of
1GP managed packages. 2GP managed packages are identified by their package ID, whereas 1GP managed packages are identified
by their namespace. This difference occurs because multiple 2GP managed packages can have the same namespace, whereas
1GP managed packages each require a unique namespace.

For example, here’s the metadata file for the subscriber’s `CartCalculatorWithShipping` class, where the class is set to version
1.0 of the managed package. Because the package is a 1GP managed package, the namespace is specified instead of the package ID.

```
   <!-- CartCalculatorWithShipping.cls-meta.xml -->

   <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>66.0</apiVersion>

      <status>Active</status>

      <packageVersions>

        <namespace>eshop</namespace> <!-- For only 1GP -->

        <majorNumber>1</majorNumber>

```


Apex Developer Guide Apex in Managed Packages

```
        <minorNumber>0</minorNumber>

      </packageVersions>

   </ApexClass>

```

6. Package Subscriber: getTotalPrice() Returns an Incorrect Value

The subscriber sets the `CartCalculatorWithShipping` class to version 1.0 of the managed package and successfully recompiles
the class. However, the subscriber now encounters a new issue at run time: the `getTotalPrice()` method in the
`CartCalculatorWithShipping` class returns the wrong total price.

Recall that specifying an earlier package version for an Apex class or trigger hides globals that are defined in later versions during
compilation. In other words, setting a package version preserves the shape of the API. However, it doesn’t necessarily preserve the
behavior of the API at run time.

In version 1.0, the `getTotalPrice()` method in the `CartCalculator` class returns only the base price. But in version 2.0, the
`getTotalPrice()` method now returns the price plus the result of `getTotalShippingCost()` . The `getTotalPrice()`
method exists in both versions of the managed package, even though its behavior differs. Therefore, even if the subscriber sets the
`CartCalculatorWithShipping` class to version 1.0, the `getTotalPrice()` executes with its version 2.0 behavior at run
time.

Remember that the subscriber’s `getTotalPrice()` method in their `CartCalculatorWithShipping` class overrides the
native `getTotalPrice()` method in the managed package. The subscriber’s override method adds the `getShippingCost()`
result to the result of the native `getTotalPrice()` method. In version 2.0 of the managed package, the native `getTotalPrice()`
method already adds the shipping cost, so the shipping cost is erroneously added twice.

```
   // Package Developer - CartCalculator.cls (v2.0) (code unchanged)

   global virtual class CartCalculator {

      global virtual Decimal getTotalPrice(CustomCart c) {

        Decimal price = 0.0;

        // Add up items in cart

        for (Decimal itemPrice : c.itemPrices) {

           price += itemPrice;

        }

        return price + getShippingCost(c);

      }

      global virtual Decimal getShippingCost(CustomCart c) {

        // Flat rate shipping

        return 20.0;

      }

   }

   // Package Subscriber - CartCalculatorWithShipping.cls (code unchanged)

   public with sharing class CartCalculatorWithShipping extends eshop.CartCalculator {

      // Now returns the wrong price because getShippingCost is added twice

      public override Decimal getTotalPrice(eshop.CustomCart c) {

        return super.getTotalPrice(c) + getShippingCost(c);

      }

      public Decimal getShippingCost(eshop.CustomCart c) {

        // Flat rate shipping

```


Apex Developer Guide Apex in Managed Packages

```
      return 20.0;

      }

   }

```

To resolve this problem without requiring the subscriber to change their code, the package developer must version the behavior of
Apex classes and triggers in the package.

7. Package Developer: Implements Backward Compatibility with System.requestVersion()

After the package subscriber informs the package developer about the unexpected `getTotalPrice()` behavior, the package
developer releases a patch update. Version 2.1 of the package allows the subscriber to keep their original
`CartCalculatorWithShipping` class by implementing backwards compatibility with `[System.requestVersion()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_System_requestVersion)` .

Here’s version 2.1 of the `CartCalculator` class that contains an updated `getTotalPrice()` method. In the method, a
`callerVersion` variable is set to `System.requestVersion()`, which returns a `[Version](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_version.htm)` object that represents the
managed package version of the calling class. A `minVersionWithShippingCost` variable is set to the managed package version
that introduced the changed `getTotalPrice()` behavior.

Then, the `[Version.compareTo()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_version.htm#apex_System_Version_compareTo)` method compares `callerVersion` and `minVersionWithShippingCost` . If the
caller version is earlier than the version that the shipping cost feature was introduced in, then `getTotalPrice()` returns the price.
This value aligns with the original behavior in version 1.0 of the managed package. If the caller version matches or is later than the version
that the shipping cost feature was introduced in, then `getTotalPrice()` returns the price addition to the shipping cost.

```
   // Package Developer - CartCalculator.cls

   /**

   * Handles tasks about calculating items and prices in customer carts.

   * @version 2.1

   * @since 1.0

   */

   global virtual class CartCalculator {

     /**

      * Adds item prices in a cart.

      * @param c A CustomCart object that represents a list of items that the customer

      * wants to buy

      * @return A Decimal object that represents the total price of items in the

      * cart. Total price includes the shipping cost for v2.0 and later.

      * @version 2.1

      * @since 1.0

     */

     global virtual Decimal getTotalPrice (CustomCart c) {

        Decimal price = 0.00;

        // Add up items in cart

        Version callerVersion = System.requestVersion();

        Version minVersionWithShippingCost = new Version(2, 0);

        if (callerVersion.compareTo(minVersionWithShippingCost) < 0) {

        // callVer < minVer that you introduced the shipping cost feature in

          return price;

        } else {

        return price + getShippingCost(c);

        }

```


Apex Developer Guide Apex in Managed Packages

```
     }

     /**

     * Get the shipping cost based on the items in a customer's cart

     * @param c A CustomCart object that represents a list of items that the customer

     * wants to buy

     * @return A Decimal object that represents the total shipping cost

     * for the cart

     * @version 2.1

     * @since 2.0

     */

     global virtual Decimal getShippingCost(CustomCart c) {

        return 20.00;

     }

   }

```

By versioning the behavior of `getTotalPrice()`, the package developer has implemented basic backward compatibility for the
class. Now, as long as package subscribers set Apex classes to the desired managed package version, then their existing implementations
won’t break when they upgrade from version 1.0 to version 2.1 of the package.

8: Package Developer: Tests Backward Compatibility with System.runAs()

To ensure that `getTotalPrice()` now behaves differently based on the package version of the calling code, the package developer
can use `[System.runAs()](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm#apex_System_System_runAs)` in their unit tests. This method, which can only be used in test methods, changes the current package
version to the package version specified in the argument Here’s a basic unit test that the package developer implements for
`getTotalPrice()` .

```
   // Package Developer - CartCalculatorTest.cls

   @isTest

   private class CartCalculatorTest {

      private static final List<Decimal> prices = new List<Decimal>{

        10.0,

        20.0,

        30.0

      };

      @isTest

      static void testGetTotalPrice_WithShippingCost() {

        CustomCart cart = new CustomCart();

        cart.itemPrices = prices;

        CartCalculator calculator = new CartCalculator();

        //Version 2.0 includes the shipping cost calculation

        System.runAs(new Version(2, 0)) {

           Decimal totalPrice = calculator.getTotalPrice(cart);

           // The expected total is sum of item prices (60.0) plus the shipping cost

   (20.0)

           Assert.areEqual(80.0, totalPrice, 'The total price should be 80.0');

        }

      }

```


## Apex Developer Guide Apex Reference

```
      @isTest

      static void testGetTotalPrice_WithoutShippingCost() {

        CustomCart cart = new CustomCart();

        cart.itemPrices = prices;

        CartCalculator calculator = new CartCalculator();

        // Version 1.0 doesn't include the shipping cost calculation

        System.runAs(new Version(1, 0)) {

           Decimal totalPrice = calculator.getTotalPrice(cart);

           // The expected total is the sum of item prices (60.0)

           Assert.areEqual(60.0, totalPrice, 'The total price should be 60.0');

        }

      }

   }

```

Summary: Shared Responsibilities for Safe Package Upgrades

The extended example demonstrates that the package developer and package subscriber both play a role in ensuring safe package
upgrades. Here’s a table that summarizes the recommended actions that each actor can take so that the package can evolve without
compromising subscriber implementations.

**Table 11: Safe Package Upgrade Responsibilities**

SEE ALSO:

Develop and Distribute Apex for Managed Packages

Use Apex Referenced by Managed Packages

## Apex Reference

In Summer ’21 and later versions, Apex reference content is moved to a separate guide called the Apex Reference Guide.


## Apex Developer Guide Appendices

[For reference information on Apex classes, interfaces, exceptions and so on, see Apex Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_ref_guide.htm)

## Appendices

### Shipping Invoice Example

Reserved Keywords
These words can be used only as keywords.

Documentation Typographical Conventions
Apex and Visualforce documentation uses these typographical conventions.

### Shipping Invoice Example

This appendix provides an example of an Apex application. This is a more complex example than the Hello World example.

**•** Shipping Invoice Walk-Through

### • Shipping Invoice Example Code 1. Shipping Invoice Example Walk-Through 2. Shipping Invoice Example Code Shipping Invoice Example Walk-Through

The sample application in this section includes traditional Salesforce functionality blended with Apex. Many of the syntactic and semantic
features of Apex, along with common idioms, are illustrated in this application.

Note: The Shipping Invoice sample requires custom objects. You can either create these on your own, or download the objects
and Apex code as an unmanaged package from the Salesforce AppExchange. To obtain the sample assets in your org, install the
[Apex Tutorials Package. This package also contains sample code and objects for the Apex Quick Start.](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000001saDCEAY)

Scenario

In this sample application, the user creates a new shipping invoice, or order, and then adds items to the invoice. The total amount for
the order, including shipping cost, is automatically calculated and updated based on the items added or deleted from the invoice.

Data and Code Models

This sample application uses two new objects: Item and Shipping_invoice.

The following assumptions are made:

**•** Item A cannot be in both orders shipping_invoice1 and shipping_invoice2. Two customers cannot obtain the same (physical)
product.

**•** The tax rate is 9.25%.

**•** The shipping rate is 75 cents per pound.

**•** Once an order is over $100, the shipping discount is applied (shipping becomes free).

The fields in the Item custom object include:


Apex Developer Guide Shipping Invoice Example

**Name** **Type** **Description**

Name String The name of the item

Price Currency The price of the item

Quantity Number The number of items in the order

Weight Number The weight of the item, used to calculate shipping costs

Shipping_invoice Master-Detail (shipping_invoice) The order this item is associated with

The fields in the Shipping_invoice custom object include:

**Name** **Type** **Description**

Name String The name of the shipping invoice/order

Subtotal Currency The subtotal

GrandTotal Currency The total amount, including tax and shipping

Shipping Currency The amount charged for shipping (assumes $0.75 per pound)

ShippingDiscount Currency Only applied once when subtotal amount reaches $100

Tax Currency The amount of tax (assumes 9.25%)

TotalWeight Number The total weight of all items

All of the Apex for this application is contained in triggers. This application has the following triggers:

**Object** **Trigger Name** **When Runs** **Description**

Item Calculate after insert, after update, after delete Updates the shipping invoice, calculates the totals and
shipping

Shipping_invoice ShippingDiscount after update Updates the shipping invoice, calculating if there is a
shipping discount

The following is the general flow of user actions and when triggers run:


#### Apex Developer Guide Shipping Invoice Example

**Flow of user action and triggers for the shopping cart application**

**1.** User clicks **Orders**    - **New**, names the shipping invoice and clicks **Save** .

**2.** User clicks **New Item**, fills out information, and clicks **Save** .

**3.** Calculate trigger runs. Part of the Calculate trigger updates the shipping invoice.

**4.** ShippingDiscount trigger runs.

**5.** User can then add, delete or change items in the invoice.

In Shipping Invoice Example Code both of the triggers and the test class are listed. The comments in the code explain the functionality.

Testing the Shipping Invoice Application

Before an application can be included as part of a package, 75% of the code must be covered by unit tests. Therefore, one piece of the
shipping invoice application is a class used for testing the triggers.

The test class verifies the following actions are completed successfully:

**•** Inserting items

**•** Updating items

**•** Deleting items

**•** Applying shipping discount

**•** Negative test for bad input

#### Shipping Invoice Example Code

The following triggers and test class make up the shipping invoice example application:


Apex Developer Guide Shipping Invoice Example

**•** Calculate trigger

**•** ShippingDiscount trigger

**•** Test class

Calculate Trigger

```
   trigger calculate on Item__c (after insert, after update, after delete) {

   // Use a map because it doesn't allow duplicate values

   Map<ID, Shipping_Invoice__C> updateMap = new Map<ID, Shipping_Invoice__C>();

   // Set this integer to -1 if we are deleting

   Integer subtract ;

   // Populate the list of items based on trigger type

   List<Item__c> itemList;

      if(trigger.isInsert || trigger.isUpdate){

        itemList = Trigger.new;

        subtract = 1;

      }

      else if(trigger.isDelete)

      {

        // Note -- there is no trigger.new in delete

        itemList = trigger.old;

        subtract = -1;

      }

   // Access all the information we need in a single query

   // rather than querying when we need it.

   // This is a best practice for bulkifying requests

   set<Id> AllItems = new set<id>();

   for(item__c i :itemList){

   // Assert numbers are not negative.

   // None of the fields would make sense with a negative value

   System.assert(i.quantity__c > 0, 'Quantity must be positive');

   System.assert(i.weight__c >= 0, 'Weight must be non-negative');

   System.assert(i.price__c >= 0, 'Price must be non-negative');

   // If there is a duplicate Id, it won't get added to a set

   AllItems.add(i.Shipping_Invoice__C);

   }

   // Accessing all shipping invoices associated with the items in the trigger

   List<Shipping_Invoice__C> AllShippingInvoices = [SELECT Id, ShippingDiscount__c,

               SubTotal__c, TotalWeight__c, Tax__c, GrandTotal__c

               FROM Shipping_Invoice__C WHERE Id IN :AllItems];

   // Take the list we just populated and put it into a Map.

   // This will make it easier to look up a shipping invoice

```


Apex Developer Guide Shipping Invoice Example

```
   // because you must iterate a list, but you can use lookup for a map,

   Map<ID, Shipping_Invoice__C> SIMap = new Map<ID, Shipping_Invoice__C>();

   for(Shipping_Invoice__C sc : AllShippingInvoices)

   {

      SIMap.put(sc.id, sc);

   }

   // Process the list of items

      if(Trigger.isUpdate)

      {

        // Treat updates like a removal of the old item and addition of the

        // revised item rather than figuring out the differences of each field

        // and acting accordingly.

        // Note updates have both trigger.new and trigger.old

        for(Integer x = 0; x < Trigger.old.size(); x++)

        {

           Shipping_Invoice__C myOrder;

           myOrder = SIMap.get(trigger.old[x].Shipping_Invoice__C);

           // Decrement the previous value from the subtotal and weight.

           myOrder.SubTotal__c -= (trigger.old[x].price__c *

                         trigger.old[x].quantity__c);

           myOrder.TotalWeight__c -= (trigger.old[x].weight__c *

                           trigger.old[x].quantity__c);

           // Increment the new subtotal and weight.

           myOrder.SubTotal__c += (trigger.new[x].price__c *

                         trigger.new[x].quantity__c);

           myOrder.TotalWeight__c += (trigger.new[x].weight__c *

                           trigger.new[x].quantity__c);

        }

        for(Shipping_Invoice__C myOrder : AllShippingInvoices)

        {

           // Set tax rate to 9.25% Please note, this is a simple example.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for tax rates is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Tax__c = myOrder.Subtotal__c * .0925;

           // Reset the shipping discount

           myOrder.ShippingDiscount__c = 0;

           // Set shipping rate to 75 cents per pound.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for the shipping rate is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Shipping__c = (myOrder.totalWeight__c * .75);

           myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +

                         myOrder.Shipping__c;

```


Apex Developer Guide Shipping Invoice Example

```
           updateMap.put(myOrder.id, myOrder);

         }

      }

      else

      {

        for(Item__c itemToProcess : itemList)

        {

           Shipping_Invoice__C myOrder;

           // Look up the correct shipping invoice from the ones we got earlier

           myOrder = SIMap.get(itemToProcess.Shipping_Invoice__C);

           myOrder.SubTotal__c += (itemToProcess.price__c *

                         itemToProcess.quantity__c * subtract);

           myOrder.TotalWeight__c += (itemToProcess.weight__c *

                           itemToProcess.quantity__c * subtract);

        }

        for(Shipping_Invoice__C myOrder : AllShippingInvoices)

        {

           // Set tax rate to 9.25% Please note, this is a simple example.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for tax rates is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Tax__c = myOrder.Subtotal__c * .0925;

           // Reset shipping discount

           myOrder.ShippingDiscount__c = 0;

           // Set shipping rate to 75 cents per pound.

           // Generally, you would never hard code values.

           // Leveraging Custom Settings for the shipping rate is a best practice.

           // See Custom Settings in the Apex Developer Guide

           // for more information.

           myOrder.Shipping__c = (myOrder.totalWeight__c * .75);

           myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +

                         myOrder.Shipping__c;

           updateMap.put(myOrder.id, myOrder);

         }

      }

      // Only use one DML update at the end.

      // This minimizes the number of DML requests generated from this trigger.

      update updateMap.values();

   }

```

ShippingDiscount Trigger

```
   trigger ShippingDiscount on Shipping_Invoice__C (before update) {

      // Free shipping on all orders greater than $100

```


Apex Developer Guide Shipping Invoice Example

```
      for(Shipping_Invoice__C myShippingInvoice : Trigger.new)

      {

        if((myShippingInvoice.subtotal__c >= 100.00) &&

          (myShippingInvoice.ShippingDiscount__c == 0))

        {

           myShippingInvoice.ShippingDiscount__c =

                  myShippingInvoice.Shipping__c * -1;

           myShippingInvoice.GrandTotal__c += myShippingInvoice.ShippingDiscount__c;

        }

      }

   }

```

Shipping Invoice Test

```
   @IsTest

   private class TestShippingInvoice{

      // Test for inserting three items at once

      public static testmethod void testBulkItemInsert(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert list1;

        // Retrieve the order, then do assertions

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE id = :order1.id];

        System.assert(order1.subtotal__c == 75,

             'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

             'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

             'Order shipping was not $4.50, but was ' + order1.shipping__c);

```


Apex Developer Guide Shipping Invoice Example

```
        System.assert(order1.totalweight__c == 6.00,

             'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

             'Order grand total was not $86.4375 but was '

              + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

             'Order shipping discount was not $0 but was '

             + order1.shippingdiscount__c);

      }

      // Test for updating three items at once

      public static testmethod void testBulkItemUpdate(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 1, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 2, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 4, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert list1;

        // Update the prices on the 3 items

        list1[0].price__c = 10;

        list1[1].price__c = 25;

        list1[2].price__c = 40;

        update list1;

        // Access the order and assert items updated

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        System.assert(order1.subtotal__c == 75,

                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was '

                 + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

```


Apex Developer Guide Shipping Invoice Example

```
                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

      }

      // Test for deleting items

      public static testmethod void testBulkItemDelete(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemA = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemB = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemC = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c itemD = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        list1.add(itemA);

        list1.add(itemB);

        list1.add(itemC);

        list1.add(itemD);

        insert list1;

        // Seven items are now in the shipping invoice.

        // The following deletes four of them.

        List<Item__c> list2 = new List<Item__c>();

        list2.add(itemA);

        list2.add(itemB);

        list2.add(itemC);

        list2.add(itemD);

        delete list2;

```


Apex Developer Guide Shipping Invoice Example

```
        // Retrieve the order and verify the deletion

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        System.assert(order1.subtotal__c == 75,

                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was ' + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

      }

      // Testing free shipping

      public static testmethod void testFreeShipping(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

        insert Order1;

        List<Item__c> list1 = new List<Item__c>();

        Item__c item1 = new Item__C(Price__c = 10, weight__c = 1,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = 2,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3,

                       quantity__c = 1, Shipping_Invoice__C = order1.id);

        list1.add(item1);

        list1.add(item2);

        list1.add(item3);

        insert list1;

        // Retrieve the order and verify free shipping not applicable

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        // Free shipping not available on $75 orders

        System.assert(order1.subtotal__c == 75,

```


Apex Developer Guide Shipping Invoice Example

```
                 'Order subtotal was not $75, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 6.9375,

                 'Order tax was not $6.9375, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 4.50,

                 'Order shipping was not $4.50, but was ' + order1.shipping__c);

        System.assert(order1.totalweight__c == 6.00,

                 'Order weight was not 6 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 86.4375,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == 0,

                 'Order shipping discount was not $0 but was '

                 + order1.shippingdiscount__c);

        // Add items to increase subtotal

        item1 = new Item__C(Price__c = 25, weight__c = 20, quantity__c = 1,

                    Shipping_Invoice__C = order1.id);

        insert item1;

        // Retrieve the order and verify free shipping is applicable

        order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,

              grandtotal__c, shippingdiscount__c

              FROM Shipping_Invoice__C

              WHERE Id = :order1.Id];

        // Order total is now at $100, so free shipping should be enabled

        System.assert(order1.subtotal__c == 100,

                 'Order subtotal was not $100, but was '+ order1.subtotal__c);

        System.assert(order1.tax__c == 9.25,

                 'Order tax was not $9.25, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 19.50,

                 'Order shipping was not $19.50, but was '

                 + order1.shipping__c);

        System.assert(order1.totalweight__c == 26.00,

                 'Order weight was not 26 but was ' + order1.totalweight__c);

