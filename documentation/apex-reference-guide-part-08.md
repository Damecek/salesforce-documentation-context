Get the default landing page, login page, and self-registration page of a site. Asynchronously create site users and records. Get the
login and logout URLs for a site. Get a user’s current site. Map dashboards and Insights reports.

#### Network Constructors

Create an instance of the `System.Network` class.

#### The following are constructors for Network .

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

#### The following are methods for Network . All methods are static.

IN THIS SECTION:

communitiesLanding()
Returns a Page Reference to the default landing page for the Experience Cloud site. This is the first tab of the site.

createExternalUserAsync(user, contact, account)
Asynchronously creates an Experience Cloud site user for the given account or contact and associates it with the site. This method
processes requests in batches and then sends an email with login information to the user.

createRecordAsync(processType, mbObject)
Asynchronously creates case, lead, and custom object records. This method collects record creation requests and processes them
in batches.


Apex Reference Guide Network Class

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


Apex Reference Guide Network Class

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


Apex Reference Guide Network Class

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


Apex Reference Guide Network Class

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


### Apex Reference Guide Object Class

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


Apex Reference Guide Object Class

Usage

All Apex classes have the Object class as the base class, and therefore implement all the Object class methods.

IN THIS SECTION:

#### Object Methods Object Methods The following are methods for Object .

IN THIS SECTION:

##### equals(obj)

Compares an object to the specified object and returns true if both are equal. Otherwise, returns false.

hashCode()
Returns a hash code for the object.

toString()
Returns a string that represents the object. The string includes the class name of which the object is an instance, the at (@) character,
and the unsigned hexadecimal representation of the object’s hash code value.

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


Apex Reference Guide Object Class

**•** For any non-null reference value x, `x.equals(null)` returns `false`

Use the `equals` method in your class to simplify comparision of objects. You can use the `==` operator to compare objects, or the
`equals` method. For example:

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

Usage

##### • If the hashCode method is invoked on the same object more than once during execution of an Apex request, it must return the

same value.

**–** The hash code value is same provided no information used in equals comparisons on the object is modified.

**–** The hash code value need not remain consistent from one Apex execution request to another execution of the same application.

##### • If two objects are equal, based on the equals method, hashCode must return the same value. • If two objects are unequal, based on the result of the equals method, it is not required that hashCode return distinct values. **`toString()`**

Returns a string that represents the object. The string includes the class name of which the object is an instance, the at (@) character,
and the unsigned hexadecimal representation of the object’s hash code value.

Signature

```
   public String toString()

```

Return Value

Type: String


### Apex Reference Guide OrgLimit Class

Versioned Behavior Changes

In API version 57.0 and later, the `toString()` method only includes member variables of Apex objects that are visible in the current
namespace. Non-global properties are suppressed from output when you invoke `toString()` on managed Apex types. To keep the
non-global state of the object visible in debug output, you can explicitly override the `toString()` method.

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

#### OrgLimit Methods OrgLimit Methods

### The following are methods for OrgLimit .

IN THIS SECTION:

##### getLimit()

Returns the maximum allowed limit value.

getName()
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


Apex Reference Guide OrgLimit Class

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

```


### Apex Reference Guide OrgLimits Class

##### **`toString()`**

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

Namespace

System

Usage

Use the `System.OrgLimits getAll` and `getMap` methods to obtain either a list or a map of all your org limits. To get details
on each limit, use instance methods from `System.OrgLimit` .

For comparison, the Limits Class returns Apex governor limits and not Salesforce API limits.

Note: Limit values are updated asynchronously, in near-real-time.

IN THIS SECTION:

#### OrgLimits Methods

SEE ALSO:

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_limits.htm)_ : Limits

#### OrgLimits Methods

### The following are methods for OrgLimits .

IN THIS SECTION:

getAll()
Returns a list of OrgLimit instances.


### Apex Reference Guide PageReference Class

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


Apex Reference Guide PageReference Class

Instantiation

In a custom controller or controller extension, you can refer to or instantiate a PageReference in one of these ways.

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


Apex Reference Guide PageReference Class

**Header** **Description**

X-Salesforce-SIP The source IP address of the request. This header is always set on HTTP and HTTPS requests that
are initiated outside of Salesforce's data centers.

Note: If a request passes through a content delivery network (CDN) or proxy server, the
source IP address might be altered, and no longer the original client IP address.

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


Apex Reference Guide PageReference Class

Example: Navigating to a New Page as the Result of an Action Method

Any action method in a custom controller or controller extension can return a PageReference object as the result of the method. If the
`redirect` attribute on the PageReference is set to `true`, the user navigates to the URL specified by the PageReference.

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

```


Apex Reference Guide PageReference Class

```
        // This is a permanent redirection

        target.setRedirectCode(301);

        return target;

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

PageReference(record)
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


Apex Reference Guide PageReference Class

##### PageReference(record) Generate a new instance of the PageReference class for the specified sObject record.

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

_[Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_compref_page.htm)_ : apex:page

_[SOAP API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_objects_apexpage.htm)_ : ApexPage

#### PageReference Methods

##### The following are methods for PageReference . All are instance methods.

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


Apex Reference Guide PageReference Class

getRedirectCode()
Returns the HTTP redirect code used when getRedirect() is set to `true` for the PageReference object.

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


Apex Reference Guide PageReference Class

Parameters

```
   resourceName
```

Type: String

The resource name

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


Apex Reference Guide PageReference Class

You also can’t use the method to retrieve the output of a different Visualforce page with the same controller and controller extensions.
Instead, pass the base URL of the destination page.

```
   new PageReference(Site.getBaseUrl() + '/apex/ VisualforcePageName ').getContent();

##### getContentAsPDF()

```

Returns the page in PDF, regardless of the `<apex:page>` component’s `renderAs` attribute.

Signature

```
   public Blob getContentAsPDF()

```

Return Value

Type: Blob

Usage

This method can’t be used in:

**•** Triggers

##### • Test methods. If you use getContentAsPDF in a test method, the test method fails. getContentAsPDF is treated as a

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


Apex Reference Guide PageReference Class

Signature

```
   public Map<String, String> getHeaders()

```

Return Value

Type: Map<String, String>

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


Apex Reference Guide PageReference Class

Usage

Note that if the URL of the PageReference object is set to a website outside of the `salesforce.com` domain, the redirect always
occurs, regardless of whether the `redirect` attribute is set to `true` or `false` .

##### getRedirectCode()

Returns the HTTP redirect code used when getRedirect() is set to `true` for the PageReference object.

Signature

```
   public Integer getRedirectCode()

```

Return Value

Type: Integer

Possible Values:

**•** 0 — Redirect using the default redirect action for this PageReference. Typically a JavaScript-based redirection or HTTP 302.

Note: [Site URLRewriter Interface implementations pointing to a PageReference with a](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_site_urlRewriter.htm) _`redirectCode`_ of 0 are not
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


Apex Reference Guide PageReference Class

Signature

```
   public System.PageReference setAnchor(String anchor)

```

Parameters

```
   anchor
```

Type: String

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


Apex Reference Guide PageReference Class

Parameters

```
   redirect
```

Type: Boolean

Return Value

Type: System.PageReference

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

Note: [Site URLRewriter Interface implementations pointing to a PageReference with a](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_site_urlRewriter.htm) _`redirectCode`_ of 0 are not
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

If the redirect code contains an invalid integer, an error message is displayed when `PageReference` is used by Salesforce for
redirection.


### Apex Reference Guide Packaging Class

Return Value

Type: System.PageReference

### Packaging Class

Contains a method for obtaining information about managed and unlocked packages.

Namespace

System

Usage

In the context of a package, use the getCurrentPackageId method to retrieve the packageID.

IN THIS SECTION:

#### Packaging Methods Packaging Methods

### The following are methods for Packaging .

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


Apex Reference Guide Pattern Class

Namespace

System

#### Pattern Methods The following are methods for Pattern .

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


Apex Reference Guide Pattern Class

Signature

```
   public Matcher matcher(String stringtoMatch)

```

Parameters

```
   stringtoMatch
```

Type: String

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


Apex Reference Guide Pattern Class

Signature

```
   public String pattern()

```

Return Value

Type: String

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


### Apex Reference Guide Queueable Interface

Usage

The substrings are placed in the list in the order in which they occur in the String. If _`regExp`_ does not match the pattern, the resulting
list has just one element containing the original String.

##### split(regExp, limit)

Returns a list that contains each substring of the String that is terminated either by the regular expression _`regExp`_ that matches this
pattern, or by the end of the String.

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

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

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)_ : Queueable Apex

### QueueableDuplicateSignature Class

Used in the `AsyncOptions` class to store the queueable job signature in the `DuplicateSignature` property.

Namespace

System


### Apex Reference Guide QueueableDuplicateSignature.Builder Class

IN THIS SECTION:

#### QueueableDuplicateSignature Methods

SEE ALSO:

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)

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

_Apex Developer Guide_ [: Detecting Duplicate Queueable Jobs](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dedupe_queueable.htm)

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
[service, see Exposing Apex Classes as REST Web Services.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_rest.htm)

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

#### RestRequest Properties The following are properties for RestRequest . Note: While the RestRequest List and Map properties are read-only, their contents are read-write. You can modify them by calling the collection methods directly or you can use of the associated RestRequest methods shown in the previous table.

```

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

Signature

```
   public Map<String, String> headers {get; set;}

```


Apex Reference Guide RestRequest Class

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

Property Value

Type: String


Apex Reference Guide RestRequest Class

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

Example

##### For example, if the Apex REST class defines a urlMapping of /MyResource/*, the resourcePath property returns

`/services/apexrest/MyResource/*` .


Apex Reference Guide RestRequest Class

#### RestRequest Methods The following are methods for RestRequest . All are instance methods. Note: At runtime, you typically don't need to add a header or parameter to the RestRequest object because they are

automatically deserialized into the corresponding properties. The following methods are intended for unit testing Apex REST
#### classes. You can use them to add header or parameter values to the RestRequest object without having to recreate the REST

method call.

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

**•** authorization

If any of these headers are used, an Apex exception is thrown.


### Apex Reference Guide RestResponse Class

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
[of the REST annotations.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_annotations_rest.htm)

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

##### The following are properties for RestResponse . Note: While the RestResponse List and Map properties are read-only, their contents are read-write. You can modify them by calling the collection methods directly or you can use of the associated RestResponse methods shown in the previous
```

table.

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

#### RestResponse Methods The following are instance methods for RestResponse . Note: At runtime, you typically don't need to add a header to the RestResponse object because it's automatically deserialized

into the corresponding properties. The following methods are intended for unit testing Apex REST classes. You can use them to
add header or parameter values to the `RestRequest` object without having to recreate the REST method call.

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


### Apex Reference Guide SandboxPostCopy Interface

Return Value

Type: Void

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

_Tooling API_ [: SandboxInfo](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxinfo.htm)

_Tooling API_ [: SandboxProcess](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxprocess.htm)

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

[For more information on testing, see Testing Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing.htm)

### Schedulable Interface

The class that implements this interface can be scheduled to run at different intervals.

Namespace

System

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_scheduler.htm)_ : Scheduler


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

[For more information on accessing SObjects, see Accessing All sObjects.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_global_describe.htm)

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

[For more information and code examples using describeDataCategoryGroups, see Accessing All Data Categories Associated with an](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)
[sObject.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

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

[See Use Dynamic SOSL to Return Snippets.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm#snippet_title)

SEE ALSO:

get(sObjectType)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

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

[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

Return Value

Type: Search.SearchResults

Usage

Use this method wherever a static SOSL query can be used, such as in regular assignment statements and `for` loops.

[See Use Dynamic SOSL to Return Snippets.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm#snippet_title)

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

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

[For more information, see Dynamic SOSL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

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

_Apex Developer Guide_ [: Suggest Salesforce Knowledge Articles](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_forcecom_kb_suggestions.htm)

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
[ignored, and the record sharing rules are controlled by the class sharing keywords. In user mode, the object permissions, field-level](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)
security, and sharing rules of the current user are enforced. System mode is the default.

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

**•** Uniqueness of set elements of user-defined types is determined by the `equals` and `[hashCode](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)` methods, which you
provide in your classes. Uniqueness of all other non-primitive types is determined by comparing the objects’ fields.

**•** If the set contains String elements, the elements are case-sensitive. Two set elements that differ only by case are considered
distinct.

[For more information on sets, see Sets.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_sets.htm)

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

The ID of the user that this method creates.


Apex Reference Guide Site Class

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

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.


Apex Reference Guide Site Class

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

##### createPersonAccountPortalUser(user, ownerId, password)

Creates a person account using the default record type defined on the guest user's profile, then enables it for the site's portal.


Apex Reference Guide Site Class

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

Return Value

Type: ID


Apex Reference Guide Site Class

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

Note: `Site.forgotPassword` cannot be used with the `@future` method, which enables asynchronous execution.

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

Return Value

Type: Boolean


Apex Reference Guide Site Class

Note: The return value is always true unless it’s called outside of a Visualforce page.

Usage

Calls to this method in API version 30.0 and later can’t commit the transaction automatically. Calls to this method before API version
30.0 commit the transaction, making it impossible to roll back to a save point before the call.

Calls to this method are subject to rate-limiting. If your rate of calls exceeds the limit, Salesforce doesn't send the password reset email.
If you experience this issue, try waiting for an hour before you send another call.

Note: `Site.forgotPassword` cannot be used with the `@future` method, which enables asynchronous execution.

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

[For more information on sObjects, see Working with sObjects.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SObjects.htm)

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

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers.htm)

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

When used in Visualforce controllers, the generated message is added to the collection of errors for the page. For more information, see
[Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_std.htm) _Visualforce Developer's Guide_ .

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

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers.htm)

Note: This method escapes any HTML markup in the specified error message. The escaped characters are: `\n`, `<`, `>`, `&`, `"`, `\`,
`\u2028`, `\u2029`, and `\u00a9` . As a result, HTML markup is not rendered; instead, it is displayed as text in the Salesforce user
interface.

When used in Visualforce controllers, the generated message is added to the collection of errors for the page. For more information, see
[Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_std.htm) _Visualforce Developer's Guide_ .

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
[component. For more information, see Validation Rules and Standard Controllers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_controller_std_validation_rules.htm) _Visualforce Developer's Guide_ .

**•** This method is highly specialized because the field identifier is not actually the invoking object—the sObject record is the invoker.
The field is simply used to identify the field that should be used to display the error.

[See Triggers and Trigger Exceptions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers.htm)

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

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

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

[For more information, see Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)


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

[If the method references polymorphic fields, a Name object is returned. Use the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_name.htm) `TYPEOF` clause in the SOQL SELECT statement to
[directly get results that depend on the runtime object type referenced by the polymorphic field. See Working with Polymorphic](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_polymorphic_relationships.htm)
[Relationships in SOQL Queries.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_SOQL_polymorphic_relationships.htm)

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

[For more information, see Dynamic DML.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_dml.htm)


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

Each `recalculateFormulas` [call counts against the SOQL query limits. See Execution Governors and Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

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

Contains a method to create a mock test class for handling SOQL query responses for Data Cloud data model objects (DMOs).

Namespace

System

Usage

### To create mock test classes, extend the SoqlStubProvider class and override the handleSoqlQuery() class method.

Note: SOQL `[For](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_loops_for_SOQL.htm)` Loops in Apex aren't supported for SOQL stubs in static or dynamic SOQL queries against DMOs.

[See Mock SOQL Tests for Data Cloud Data Model Objects in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm) _Apex Developer Guide_ .

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

_Apex Developer Guide:_ [Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)

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

[For more information on Strings, see String Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

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

unescapeXml()
Unescapes the characters in a String using XML entities.


Apex Reference Guide String Class

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
[IDs, see the ID Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

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

[This method is useful when creating a dynamic SOQL statement to help prevent SOQL injection. See Dynamic SOQL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_soql.htm)

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

[For more details about the use of hash code methods with custom types, see Using Custom Types in Map Keys and Sets.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps_keys_userdefined.htm)

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

```


Apex Reference Guide String Class

##### uncapitalize()

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

##### unescapeCsv()

```

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

```


Apex Reference Guide String Class

##### unescapeEcmaScript()

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

##### unescapeHtml3()

```

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


Apex Reference Guide String Class

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

##### unescapeJava()

```

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


Apex Reference Guide String Class

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


Apex Reference Guide String Class

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

```


Apex Reference Guide String Class

##### valueOf(doubleToConvert)

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


Apex Reference Guide String Class

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

```


### Apex Reference Guide StubProvider Interface

```
   System.assertEquals(

     '(10, 20)', strList);

##### valueOfGmt(datetimeToConvert)

```

Returns a String that represents the specified Datetime in the standard “yyyy-MM-dd HH:mm:ss” format for the GMT time zone.

Signature

```
   public static String valueOfGmt(Datetime datetimeToConvert)

```

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


Apex Reference Guide StubProvider Interface

IN THIS SECTION:

#### StubProvider Methods

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

createStub(parentType, stubProvider)

#### StubProvider Methods The following are methods for StubProvider .

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


### Apex Reference Guide System Class

```
   listOfArgs
```

Type: List<Object>

The actual argument values passed into this method at runtime.

Return Value

Type: Object

Usage

You can use the parameters passed into this method to identify which method on the stubbed object was invoked. Then you can define
the behavior for each identified method.

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

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

currentPageReference()
Returns a reference to the current page. This is used with Visualforce pages.

currentTimeMillis()
Returns the current time in milliseconds, which is expressed as the difference between the current time and midnight, January 1,
1970 UTC.


Apex Reference Guide System Class

debug(msg)
Writes the specified message, in string format, to the execution debug log. The `DEBUG` log level is used.

debug(logLevel, msg)
Writes the specified message, in string format, to the execution debug log with the specified log level.

enqueueJob(queueableObj)
Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID.

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


Apex Reference Guide System Class

pauseJobById(cronTriggerId)
Pause a scheduled Apex job specified by its CronTrigger ID.

pauseJobByName(jobName)
Pause a scheduled Apex job specified by its name.

process(workItemIds, action, comments, nextApprover)
Processes the list of work item IDs.

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


Apex Reference Guide System Class

today()
Returns the current date in the current user's time zone.

##### **`abortJob(jobId)`**

Stops the specified job. If the job is currently executing, the stopped job is still visible in the job queue in the Salesforce user interface.
The specified job is stopped, but any code that is in progress will continue to execute until it completes.

Signature

```
   public static Void abortJob(String jobId)

```

Parameters

```
   jobId
```

Type: String

The _`jobId`_ [is the ID associated with an AsyncApexJob ID for batch or future Apex jobs, or a CronTrigger ID for scheduled Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)
jobs. You can't abort a scheduled Apex job using an AsyncApexJob ID.

Return Value

Type: Void

Usage

##### The following methods return the job ID that can be passed to abortJob .

**•** `System.schedule` method—returns the CronTrigger object ID associated with the scheduled job as a string.

**•** `[SchedulableContext.getTriggerId](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_scheduler.htm)` method—returns the CronTrigger object ID associated with the scheduled job as
a string.

**•** `[getJobId](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)` method—returns the AsyncApexJob object ID associated with the batch job as a string.

**•** [Using Batch Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm) `[Database.executeBatch](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)` method—returns the AsyncApexJob object ID associated with the batch job as
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


Apex Reference Guide System Class

```
   msg
```

Type: Object

(Optional) Custom message returned as part of the error message.

Return Value

Type: Void

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


Apex Reference Guide System Class

Signature

```
   public static Void assertNotEquals(Object expected, Object actual, Object msg)

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

##### currentTimeMillis()

Returns the current time in milliseconds, which is expressed as the difference between the current time and midnight, January 1, 1970
UTC.

Signature

```
   public static Long currentTimeMillis()

```


Apex Reference Guide System Class

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


Apex Reference Guide System Class

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

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)

##### **`enqueueJob(queueable, delay)`**

Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. The job is scheduled with a
specified minimum delay (0–10 minutes). The delay is ignored during Apex testing.


Apex Reference Guide System Class

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

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)

##### **`enqueueJob(queueable, asyncOptions)`**

Adds a job to the Apex job queue that corresponds to the specified queueable class and returns the job ID. Specify a unique signature
for your queueable job, the maximum stack depth or the minimum queue delay in the asyncOptions parameter.

Signature

```
   public static Id enqueueJob(Object queueable, Object asyncoptions)

```

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


Apex Reference Guide System Class

Specify a unique signature for your queueable job, the maximum stack depth, or a minimum queue delay in the AsyncOptions class
properties.

Return Value

Type: Id

The job ID, which corresponds to the ID of an AsyncApexJob record.

Usage

The `[System.AsyncInfo](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_AsyncInfo.htm)` class methods help you determine if maximum stack depth is set in your Queueable request and get the
stack depths and queue delay for queueables that are currently running. Use information about the current queueable execution to
make decisions on adjusting delays on subsequent calls.

These are methods in the `System.AsyncInfo` class.

**•** `hasMaxStackDepth()`

**•** `getCurrentQueueableStackDepth()`

**•** `getMaximumQueueableStackDepth()`

**•** `getMinimumQueueableDelayInMinutes()`

[For more information about Queueable Apex, including information about limits, see Queueable Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_queueing_jobs.htm)

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

Usage

_`obj1`_ and _`obj2`_ can be of any type. They can be values, or object references, such as sObjects and user-defined types.

The comparison rules for `System.equals` are identical to the ones for the `==` operator. For example, string comparison is case
[insensitive. For information about the comparison rules, see the == operator.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_expressions_operators_understanding.htm)


Apex Reference Guide System Class

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

Signature

```
   public String getQuiddityShortCode(System.Quiddity QuiddityValue)

```

Parameters

```
   QuiddityValue
```

Type: System.Quiddity


Apex Reference Guide System Class

The Quiddity enum value that has an associated short code. This short code is used in Event Monitoring logs. For more information,
[see Apex Execution Event Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_apexexecution.htm)

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

Usage

##### A batch Apex job can’t invoke a future method. Before invoking a future method, use isBatch() to check whether the executing

code is a batch Apex job.


Apex Reference Guide System Class

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

Return Value

Type: Boolean


Apex Reference Guide System Class

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

##### isScheduled()

Returns `true` if the currently executing code is invoked by a scheduled Apex job; `false` otherwise.


Apex Reference Guide System Class

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

##### now()

Returns the current date and time in the GMT time zone.


Apex Reference Guide System Class

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

Signature

```
   public static List<Id> process(List<Id> workItemIds, String action, String comments,

   String nextApprover)

```


Apex Reference Guide System Class

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

[Asynchronous Apex job records are records in AsyncApexJob.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)

The system cleans up asynchronous job records for jobs that have finished execution and are older than seven days. You can use this
method to further reduce the size of AsyncApexJob by cleaning up more records.

Each execution of this method counts as a single row against the governor limit for DML statements.

Example

This example shows how to delete all job records for jobs that have finished before today’s date.

```
   Integer count = System.purgeOldAsyncJobs

     (Date.today());

```


Apex Reference Guide System Class

```
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

[Asynchronous Apex job records are records in AsyncApexJob.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_asyncapexjob.htm)

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

##### **`requestVersion()`**

```

Returns a two-part version that contains the major and minor version numbers of a package. Applies to first-generation managed
packages.


Apex Reference Guide System Class

Signature

```
   public static System.Version requestVersion()

```

Return Value

Type: System.Version

Usage

Using this method, you can determine the version of an installed instance of your package from which the calling code is referencing
[your package. Based on the version that the calling code has, you can customize the behavior of your package code. See Version Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm)
[Code Behavior in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm) _Apex Developer Guide_ .

The `requestVersion` method isn’t supported for unmanaged packages. If you call it from an unmanaged package, an exception
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

##### resetPasswordWithEmailTemplate(userId, sendUserEmail, emailTemplateName)

Resets the user's password and sends an email to the user with their new password. You specify the email template that is sent to the
specified user. Use this method for external users of Experience Cloud sites.


Apex Reference Guide System Class

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

Return Value

Type: void


Apex Reference Guide System Class

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

Usage

A package developer can use Version methods to continue to support existing behavior in classes and triggers in previous package
versions while continuing to evolve the code. Apex classes and triggers are saved with the version settings for each installed managed
package that the class or trigger references.


Apex Reference Guide System Class

This method is used for testing your component behavior in different package versions that you upload to the AppExchange. This method
effectively sets a two-part version consisting of major and minor numbers in a test method so that you can test the behavior for different
package versions.

##### You can only use runAs in a test method. There is no limitation to the number of calls to this method in a transaction. For sample

[usage of this method, see Testing Behavior in Package Versions.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_manpkgs_behavior_testing.htm)

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

[more information, see Using the runAs() Method.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_tools_runas.htm)

##### Note: The runAs method ignores user license limits. You can create new users with runAs even if your organization has no

additional user licenses.

##### The runAs method implicitly inserts the user that is passed in as parameter if the user has been instantiated, but not inserted yet. You can also use runAs to perform mixed DML operations in your test by enclosing the DML operations within the runAs block. In

this way, you bypass the mixed DML error that is otherwise returned when inserting or updating setup objects together with other
[sObjects. See sObjects That Cannot Be Used Together in DML Operations.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dml_non_mix_sobjects.htm)

##### Note: Every call to runAs counts against the total number of DML statements issued in the process. schedule(jobName, cronExpression, schedulableClass) Use schedule with an Apex class that implements the Schedulable interface to schedule the class to run at the time specified

by a Cron expression.

Signature

```
   public static String schedule(String jobName, String cronExpression, Object

   schedulableClass)

```


Apex Reference Guide System Class

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

_`Minutes`_ 0–59 None

_`Hours`_ 0–23 `, - * /`

_`Day_of_month`_ 1–31 `, - * ? / L W`


Apex Reference Guide System Class

**Name** **Values** **Special Characters**

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


Apex Reference Guide System Class

**Special Character** **Description**

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

##### scheduleBatch(batchable, jobName, minutesFromNow)

```

Schedules a batch job to run once in the future after the specified time interval and with the specified job name.

Signature

```
   public static String scheduleBatch(Database.Batchable batchable, String jobName, Integer

   minutesFromNow)

```


Apex Reference Guide System Class

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
job using the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

[For an example, see Using Batch Apex.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)

##### scheduleBatch(batchable, jobName, minutesFromNow, scopeSize)

Schedules a batch job to run once in the future after the specified the time interval, with the specified job name and scope size. Returns
the scheduled job ID (CronTrigger ID).

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


Apex Reference Guide System Class

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
job using the `[System.abortJob](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_system.htm)` method.

For an example, see Using the `[System.scheduleBatch](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm)` Method.

##### setPassword(userId, password)

Sets the password for the specified user.

Signature

```
   public static Void setPassword(ID userId, String password)

```

Parameters

```
   userId
```

Type: ID

```
   password
```

Type: String


Apex Reference Guide System Class

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

Signature

```
   public static Date today()

```

Return Value

Type: Date


### Apex Reference Guide Test Class Test Class

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


Apex Reference Guide Test Class

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


Apex Reference Guide Test Class

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


Apex Reference Guide Test Class

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

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)


Apex Reference Guide Test Class

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
When you invoke methods on the stubbed object, the `handleMethodCall()` method of the `StubProvider` interface is called
to perform the behavior of the stubbed method.

SEE ALSO:

_Apex Developer Guide_ [: Build a Mocking Framework with the Stub API](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_stub_api.htm)

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


Apex Reference Guide Test Class

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

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)

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


Apex Reference Guide Test Class

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

_Apex Developer Guide_ [: Mock SOQL Tests for Data Cloud Data Model Objects](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm)

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

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_intro.htm)_


Apex Reference Guide Test Class

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
##### batch-job enqueueing. Using enqueueBatchJobs(numberOfJobs) is faster than enqueuing real batch jobs. getEventBus()

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

```


Apex Reference Guide Test Class

```
   // Perform validation

   // ...

   Test.stopTest();

```

SEE ALSO:

_[Platform Events Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)_

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

```


Apex Reference Guide Test Class

```
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


Apex Reference Guide Test Class

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


Apex Reference Guide Test Class

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

**•** application/octet-stream

**•** text/plain

##### newSendEmailQuickActionDefaults(contextId, replyToId)

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


Apex Reference Guide Test Class

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


Apex Reference Guide Test Class

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
You also can’t use `setCreatedDate` in methods annotated with `@isTest(SeeAllData=true)`, because those methods
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


Apex Reference Guide Test Class

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

[For more information, see Dynamic SOSL.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_SOSL.htm)

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


Apex Reference Guide Test Class

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

Parameters

```
   applicationMode
```

Type: Boolean

Return Value

Type: Void

Usage

Also see the `getApplicationReadWriteMode()` System method.

##### Do not use setReadOnlyApplicationMode for purposes unrelated to Read-Only Mode testing, such as simulating DML

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

```


Apex Reference Guide Test Class

```
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
##### Any code that executes after the call to startTest and before stopTest is assigned a new set of governor limits.


Apex Reference Guide Test Class

##### stopTest()

Marks the point in your test code when your test ends. Use this method in conjunction with the `startTest` method.

Signature

```
   public static Void stopTest()

```

Return Value

Type: Void

Usage

##### Each test method is allowed to call this method only once. Any code that executes after the stopTest method is assigned the original

limits that were in effect before `startTest` was called. All asynchronous calls made after the `startTest` method are collected
##### by the system. When stopTest is executed, all asynchronous processes are run synchronously. Note: Asynchronous calls, such as @future or executeBatch, called in a startTest, stopTest block, do not count

against your limits for the number of queued jobs.

##### testInstall(installImplementation, version, isPush)

Tests the implementation of the InstallHandler interface, which is used for specifying a post install script in packages. Tests run as the
test initiator in the development environment.

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


Apex Reference Guide Test Class

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


Apex Reference Guide Test Class

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


### Apex Reference Guide Time Class

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

[For more information on time, see Time Data Type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### Time Methods

### The following are methods for Time .


Apex Reference Guide Time Class

IN THIS SECTION:

##### addHours(additionalHours)

Adds the specified number of hours to a Time.

##### addMilliseconds(additionalMilliseconds)

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


Apex Reference Guide Time Class

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


Apex Reference Guide Time Class

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

```


Apex Reference Guide Time Class

##### minute()

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

```


### Apex Reference Guide TimeZone Class

##### second()

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


Apex Reference Guide TimeZone Class

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

#### TimeZone Methods The following are methods for TimeZone .

```

IN THIS SECTION:

##### getDisplayName()

Returns this time zone’s display name.

getID()
Returns this time zone’s ID.

getOffset(date)
Returns the time zone offset, in milliseconds, of the specified date to the GMT time zone.

getTimeZone(timeZoneIdString)
Returns the time zone corresponding to the specified time zone ID.

toString()
Returns the string representation of this time zone.

##### getDisplayName()

Returns this time zone’s display name.


Apex Reference Guide TimeZone Class

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


### Apex Reference Guide Trigger Class

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


Apex Reference Guide Trigger Class

**Variable** **Usage**

`isExecuting` Returns true if the current context for the Apex code is a trigger, not a Visualforce page, a Web service,
or an `executeanonymous()` API call.

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

oldMap

operationType

```

Returns a list of the new versions of the sObject records.

This sObject list is only available in `insert`, `update`, and `undelete` triggers, and the records
can only be modified in `before` triggers.

A map of IDs to the new versions of the sObject records.

This map is only available in `before update`, `after insert`, `after update`, and
`after undelete` triggers.

Returns a list of the old versions of the sObject records.

This sObject list is only available in `update` and `delete` triggers.

A map of IDs to the old versions of the sObject records.

This map is only available in `update` and `delete` triggers.

Returns an enum of type System.TriggerOperation corresponding to the current operation.

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


Apex Reference Guide Trigger Class

**•** `newMap`

**•** `old`

**•** `oldMap`

Example

For example, in this simple trigger, `Trigger.new` is a list of sObjects and can be iterated over in a `for` loop. It can also be used as
a bind variable in the `IN` clause of a SOQL query.

```
   Trigger simpleTrigger on Account (after insert) {

      for (Account a : Trigger.new) {

        // Iterate over each sObject

      }

      // This single query finds every contact that is associated with any of the

      // triggering accounts. Note that although Trigger.new is a collection of

      // records, when used as a bind variable in a SOQL query, Apex automatically

      // transforms the list of records into a list of corresponding Ids.

      Contact[] cons = [SELECT LastName FROM Contact

                 WHERE AccountId IN :Trigger.new];

   }

```

This trigger uses Boolean context variables like `Trigger.isBefore` and `Trigger.isDelete` to define code that only executes
for specific trigger conditions:

```
   trigger myAccountTrigger on Account(before delete, before insert, before update,

                         after delete, after insert, after update) {

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

           System.assertEquals('xxx', a.accountNumber);

           System.assertEquals('industry', a.industry);

           System.assertEquals(100, a.numberofemployees);

           System.assertEquals(100.0, a.annualrevenue);

           a.accountNumber = 'yyy';

```


### Apex Reference Guide TriggerOperation Enum

```
        }

   // If the trigger is not a before trigger, it must be an after trigger.

   } else {

      if (Trigger.isInsert) {

        List<Contact> contacts = new List<Contact>();

        for (Account a : Trigger.new) {

           if(a.Name == 'makeContact') {

             contacts.add(new Contact (LastName = a.Name,

                             AccountId = a.Id));

           }

        }

       insert contacts;

      }

     }

   }}}

### TriggerOperation Enum

```

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


Apex Reference Guide Type Class

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


Apex Reference Guide Type Class

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

IN THIS SECTION:

##### equals(typeToCompare)

Returns `true` if the specified type is equal to the current type; otherwise, returns `false` .

forName(fullyQualifiedName)
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


Apex Reference Guide Type Class

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


Apex Reference Guide Type Class

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


Apex Reference Guide Type Class

Example

This example shows how to get a Type’s name. It first obtains a Type by calling `forName`, then calls `getName` on the Type object.

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


Apex Reference Guide Type Class

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

```


Apex Reference Guide Type Class

```
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


### Apex Reference Guide UninstallHandler Interface

Example

This example shows how to create an instance of a Type. It first gets a Type by calling `forName` with the name of a class ( `ShapeImpl` ),
then calls `newInstance` on this Type object. The `newObj` instance is declared with the interface type ( `Shape` ) that the `ShapeImpl`
class implements. The return value of the `newInstance` method is cast to the `Shape` type.

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

Return Value

Type: String

Usage

This method returns the same value as `getName` . `String.valueOf` and `System.debug` use this method to convert their
Type argument into a String.

Example

##### This example calls toString on the Type corresponding to a list of Integers.

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


Apex Reference Guide UninstallHandler Interface

The uninstall script is subject to default governor limits. It runs as a special system user that represents your package, so all operations
performed by the script will appear to be done by your package. You can access this user by using UserInfo. You will only see this user
at runtime, not while running tests.

If the script fails, the uninstall continues but none of the changes performed by the script are committed. Any errors in the script are
emailed to the user specified in the **Notify on Apex Error** field of the package. If no user is specified, the uninstall details will be
unavailable.

The uninstall script has the following restrictions. You can’t use it to initiate batch, scheduled, and future jobs, to access Session IDs, or
to perform callouts.

#### The UninstallHandler interface has a single method called onUninstall, which specifies the actions to be performed on

uninstall.

```
   global interface UninstallHandler {

     void onUninstall(UninstallContext context)};

##### The onUninstall method takes a context object as its argument, which provides the following information.

```

**•** The org ID of the organization in which the uninstall takes place.

**•** The user ID of the user who initiated the uninstall.

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

#### UninstallHandler Methods

UninstallHandler Example Implementation

#### UninstallHandler Methods The following are methods for UninstallHandler .

IN THIS SECTION:

##### onUninstall(context)

Specifies the actions to be performed on uninstall.

##### onUninstall(context)

Specifies the actions to be performed on uninstall.

Signature

```
   public Void onUninstall(UninstallContext context)

```


Apex Reference Guide UninstallHandler Interface

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
#### that implements the UninstallHandler interface.

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

```


### Apex Reference Guide URL Class URL Class

Represents a uniform resource locator (URL) and provides access to parts of the URL. Enables access to the base URL used to access your
Salesforce org.

Namespace

System

Usage

Use the methods of the `System.URL` class to create links to objects in your organization. Such objects can be files, images, logos, or
records that you want to include in external emails, in activities, or in Chatter posts. For example, you can create a link to a file uploaded
as an attachment to a Chatter post by concatenating the Salesforce base URL with the file ID:

```
   // Get a file uploaded through Chatter.

   ContentDocument doc = [SELECT Id FROM ContentDocument

         WHERE Title = 'myfile'];

   // Create a link to the file.

   String fullFileURL = URL.getOrgDomainURL().toExternalForm() +

     '/' + doc.id;

   system.debug(fullFileURL);

```

The following example creates a link to a Salesforce record. The full URL is created by concatenating the Salesforce base URL with the
record ID.

```
   Account acct = [SELECT Id FROM Account WHERE Name = 'Acme' LIMIT 1];

   String fullRecordURL = URL.getOrgDomainURL().toExternalForm() + '/' + acct.Id;

```

Example

In this example, the base URL and the full request URL of the current Salesforce server instance are retrieved. Next, a URL pointing to a
specific account object is created. Finally, components of the base and full URL are obtained. This example prints out all the results to
the debug log output.

```
   // Create a new account called Acme that we will create a link for later.

   Account myAccount = new Account(Name='Acme');

   insert myAccount;

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

```


Apex Reference Guide URL Class

```
   System.debug('Host: ' + URL.getOrgDomainURL().getHost());

   System.debug('Protocol: ' + URL.getOrgDomainURL().getProtocol());

   // Get the query string of the current request.

   System.debug('Query: ' + URL.getCurrentRequestUrl().getQuery());

```

Versioned Behavior Changes

In API version 41.0 and later, Apex URL objects are represented by the `java.net.URI` type, not the `java.net.URL` type. The
API version in which the URL object was instantiated determines the behavior of subsequent method calls to the specific instance.
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

Url(context, spec)
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


Apex Reference Guide URL Class

Parameters

```
   spec
```

Type: String

The string to parse as a URL.

##### Url(context, spec)

Creates a new instance of the `URL` class by parsing the specified spec within the specified context.

Signature

```
   public Url(Url context, String spec)

```

Parameters

```
   context
```

Type: URL on page 4254

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


Apex Reference Guide URL Class

The host name for this URL.

```
   file
```

Type: String

The file name for this URL.

##### Url(protocol, host, port, file)

#### Creates a new instance of the URL class using the specified protocol, host, port, and file on the host.

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


Apex Reference Guide URL Class

getHost()
Returns the host name of the current URL.

getOrgDomainUrl()
Returns the canonical URL for your org. For example, `https://` _`MyDomainName`_ `.my.salesforce.com` .

getPath()
Returns the path portion of the current URL.

getPort()
Returns the port of the current URL.

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


Apex Reference Guide URL Class

Return Value

Type: `System.URL`

Usage

An example of a URL for an entire request is `https://` _`yourInstance`_ `.salesforce.com/apex/myVfPage.apexp` .

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


Apex Reference Guide URL Class

Specifies the API name of a file field component, such as `AttachmentBody` .

Return Value

Type: String

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

[This example uses the Salesforce REST API to get organization limit values. For information on limits, see Limits in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_limits.htm) _REST API Developer_
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

_[Lightning Aura Components Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/apex_api_calls.htm)_ : Making API Calls from Apex

_User Interface API Developer Guide_ [: Get Default Values to Clone a Record](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_resources_record_defaults_clone.htm)

_[User Interface API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_resources_picklist_values.htm)_ : Get Values for a Picklist Field

_[User Interface API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.uiapi.meta/uiapi/ui_api_resources_overview.htm)_ : User Inteface API Resources

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

**•** 1, 4155551234 (only numbers, no symbols)

**•** 1, 415-555-1234 (extra spaces)

Now, consider the following examples.

**•** Correct examples:

**–** `formatPhoneNumber('1', '4155551234');`

**–** `formatPhoneNumber('+1','(415) 555-1234');`

**–** `formatPhoneNumber('1', '415-555-1234');`

**•** Incorrect example, because the country code and mobile number aren’t separated:

**–** `formatPhoneNumber(null, '+1 415-555-1234');`

**•** Example that doesn’t generate an error, but likely won’t work as intended:

**–** `formatPhoneNumber('+1', '+1 (415) 555-1234');`

Format Phone Number Code Example

Here's a code example that uses the `formatPhoneNumber` method. It gets the mobile number from the user and converts it to the
format required by Salesforce. Then it updates the user’s record with the formatted mobile number.

```
   global with sharing class PhoneRegistrationController {

      //Input variables

```


Apex Reference Guide UserManagement Class

```
      global String countryCode {get; set;}

      global String phoneNumber {get; set;}

      global String addPhoneNumber()

      {

        if(countryCode == null) return 'Country code is required';

        if(phoneNumber == null) return 'Phone number is required';

        String userId = UserInfo.getUserId();

        User u = [SELECT Id FROM User WHERE Id=:userId LIMIT 1];

       String formatNum = System.UserManagement.formatPhoneNumber(countryCode, phoneNumber);

        u.MobilePhone = formatNum;

        update u;

        return null;

      }

   }

```

As long as the country code and phone number are separated, `formatPhoneNumber` returns a value in the proper format.

##### initPasswordlessLogin(userId, method)

Invokes a verification challenge for passwordless login when creating custom (Visualforce) Login and Verify pages for customers and
partners.

Signature

```
   public static String initPasswordlessLogin(Id userId, Auth.VerificationMethod method)

```

Parameters

```
   userId
```

Type: Id

ID of the user who’s logging in.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be EMAIL or SMS.

Return Value

Type: String

Identifier of the verification attempt.

Usage

Use this method along with its paired `verifyPasswordlessLogin` to customize the login experience with your own Visualforce
##### Login and Verify pages. Invoke initPasswordlessLogin from the Login page where the user enters an email address or phone

number.


Apex Reference Guide UserManagement Class

Note: An alternative to using this combination of methods is to use `Site.passwordlessLogin` . Both approaches let you
customize the Login page in Visualforce. With the paired methods, you can create custom Login and Verify pages. With
`Site.passwordlessLogin`, Salesforce supplies the Verify page.

First call the `initPasswordlessLogin` method to initiate an authentication challenge. This method:

**•** Gets the user ID and verification method, such as EMAIL or SMS, from the Login page.

**•** Looks up the user and checks that the user is unique and active.

**•** Sends a verification code to the user.

**•** Adds an entry for the verification attempt to the Identity Verification History log, assigning an identifier to the verification attempt
and setting the status to **User challenged, waiting for response** .

**•** Adds an entry for the Passwordless Login to the Login History log.

**•** Returns the identifier to `verifyPasswordlessLogin` to link the transactions.

Then call `verifyPasswordlessLogin`, which, if the user enters the verification code correctly, logs in the user.

Note: Users must verify their identity by email address or phone number before they can log in without a password. You can
check whether the user is verified from the user’s detail page in Setup. Or you can check programmatically with
`[TwoFactorMethodsInfo](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_twofactormethodsinfo.htm)` .

##### initRegisterVerificationMethod(method)

Invokes a verification challenge for registering identity verification methods with a custom (Visualforce) page. Users can register either
their email address or phone number.

Signature

```
   public static String initRegisterVerificationMethod(Auth.VerificationMethod method)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be EMAIL or SMS.

Return Value

Type: String

The method returns an error message if the phone number is already registered, the user isn’t a customer or partner, or if the context
isn’t an Experience Cloud site.

Usage

Use this method along with its paired `verifyRegisterVerificationMethod` on page 4288 to customize the process for
registering a user’s verification method using a Visualforce Verify page.

##### First call the initRegisterVerificationMethod method to get the verification code sent to the user as input, and validate

it. If the verification code isn’t valid, it returns an error message.


Apex Reference Guide UserManagement Class

Example

Here’s a code example that registers a user’s phone number as a verification method. When the user enters a verification code on the
Visualforce page, it invokes `registerUser()` [. The method calls the UserInfo class to get the User ID of the user who’s registering](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_userinfo.htm)
the verification method. Using the user ID, it then finds the user’s phone number. It also gets the user’s registration status to check
whether the phone number is verified already. If the user is registered with a different phone number, the number is updated.

```
   public void registerUser() {

        try {

           exceptionText='';

           String userId = UserInfo.getUserId();

           User u = [Select MobilePhone, Id from User Where Id=:userId];

           currPhone = u.MobilePhone;

           mobilePhone = getFormattedSms(mobilePhone);

          if (mobilePhone != null && mobilePhone != '') {

          u.MobilePhone = mobilePhone;

          update u;

           // We're updating the email and phone number before verifying. Roll back

          // the change in the verify API if it is unsuccessful.

           exceptionText = System.

           UserManagement.initRegisterVerificationMethod(Auth.VerificationMethod.SMS);

           if(exceptionText!= null && exceptionText!=''){

             isInit = false;

             showInitException = true;

           } else {

              isInit = false;

              isVerify = true;

           }

           } else {

             showInitException = true;

           }

        } catch (Exception e) {

           exceptionText = e.getMessage();

           isInit = false;

           showInitException = true;

        }

      }

   public void verifyUser() {

      // Take the user’s input for the code sent to their phone number

      exceptionText = System.UserManagement.

        verifyRegisterVerificationMethod(code, Auth.VerificationMethod.SMS);

      if(exceptionText != null && exceptionText !=''){

      showInitException = true;

      } else {

           //Success

      }

   }

##### initSelfRegistration(method, user)

```

Invokes a verification challenge for self-registration when creating a custom (Visualforce) Verify page for Experience Cloud self-registration.


Apex Reference Guide UserManagement Class

Signature

```
   public static String initSelfRegistration(Auth.VerificationMethod method, User user)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be EMAIL or SMS.

```
   user
```

Type: User

[User object to insert after successful registration. To see which fields are required, see User in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_user.htm) _Object Reference for the Salesforce_
_Platform_ .

Return Value

Type: String

Identifier of the registration attempt.

Usage

By default, when users sign up for your Experience Cloud site with an email address or phone number, Salesforce sends them a verification
code. At the same time, it generates a Verify page for users to confirm their identity. You can replace the default Salesforce Verify page
with your own Visualforce page and then invoke the verification process.

Call this method to initiate the authentication challenge, and include a User object to insert if the registration is successful. The method
returns the identifier for the self-registration attempt.

Note: If you specify a language in the `LanguageLocaleKey` field on the User object, Salesforce uses this language for
verification email and SMS messages.

Then call verifySelfRegistration, which, if the user enters the verification code correctly, logs in the user.

Example

This code contains the result of a verification challenge that registers a new user.

```
   String id = System.UserManagement.initSelfRegistration

         (Auth.VerificationMethod.SMS, user);

        Auth.VerificationResult res = System.UserManagement.verifySelfRegistration

         (Auth.VerificationMethod.SMS, id, ‘123456’, null);

        if(res.success == true){

      //redirect

   }

##### initVerificationMethod(method)

```

Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

Signature

```
   public static String initVerificationMethod(Auth.VerificationMethod method)

```


Apex Reference Guide UserManagement Class

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to initiate a verification service for `EMAIL`, `SMS`, or `SALESFORCE_AUTHENTICATOR` verification methods.

Return Value

Type: String

The returned identifier must be passed into `verifyVerificationMethod` .

Usage

Use this method along with its paired `verifyVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
##### SALESFORCE_AUTHENTICATOR verification methods. The returned identifier from initVerificationMethod must be

passed into `verifyVerificationMethod` .

##### First invoke the initVerificationMethod method to send a verification code to the user’s email or phone number, or to send

a push notification to the Salesforce Authenticator. The user then enters the code or approves the push notification. If the verification
code isn’t valid or the push notification isn’t approved, the service returns an error message.

Email Example

This example shows multi-factor authentication using email.

```
   public void initVerification() {

   // user will receive code on their registered verified email

    identifier = UserManagement.initVerificationMethod(Auth.VerificationMethod.EMAIL);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // the code will need to be entered in this method

   return UserManagement.verifyVerificationMethod(identifier, code,

   Auth.VerificationMethod.EMAIL);

   }

##### initVerificationMethod(method, actionName, extras)

```

Initiates a verification service for email, phone (SMS), and the Salesforce Authenticator verification methods.

Signature

```
   public static String initVerificationMethod(Auth.VerificationMethod method, String

   actionName, Map<String,String> extras)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to initiate a verification service for `EMAIL`, `SMS`, or `SALESFORCE_AUTHENTICATOR` verification methods.


Apex Reference Guide UserManagement Class

```
   actionName
```

Type: String

For the `SALESFORCE_AUTHENTICATOR` verification method only, the name of the action to display on the Salesforce
Authenticator, such as `Connect to My Salesforce Org` . The default action name is `Apex-Defined Activity` .

```
   extras
```

[Type: Map<String,String>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)

For the `SALESFORCE_AUTHENTICATOR` verification method only, the following extra settings.

**•** `secure_device_required` –If set to `true`, the user’s device must be secured. For example, the user must enter the
device’s passcode to approve the request. Default setting is `false` .

**•** `challenge_required` –If set to `true`, the user must complete a biometric challenge, such as face recognition, on the
device to approve the request. Default setting is `false` .

Return Value

Type: String

The returned identifier must be passed into `verifyVerificationMethod` method.

Usage

Use this method along with its paired `verifyVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
`SALESFORCE_AUTHENTICATOR` verification methods. The returned identifier from `initVerificationMethod` must be
passed into `verifyVerificationMethod` method.

First invoke the `initVerificationMethod` method to send a verification code to the user’s email or phone number, or to send
a push notification to the Salesforce Authenticator. The user then enters the code or approves the push notification. If the verification
code isn’t valid or the push notification isn’t approved, the service returns an error message.

Salesforce Authenticator Example

This example shows multi-factor authentication (MFA) using the Salesforce Authenticator mobile app. In this example, the _`actionName`_
parameter is set to the default setting and the _`extra`_ parameter settings are set to `false` .

```
   public void initVerification() {

   // user will receive push notification on their registered MFA devices

   identifier =

   UserManagement.initVerificationMethod(Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // user will need to take the action on their registered MFA devices

   return UserManagement.verifyVerificationMethod(identifier, '',

   Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

```

This example shows multi-factor authentication using Salesforce Authenticator. In this example, the _`actionName`_ parameter is set
to `Connect to My Salesforce Org` and the `challenge_required` _`extra`_ parameter is set to `true` .

```
   public void initVerification() {

   Map<String,String> extras = new Map<String,String>();

```


Apex Reference Guide UserManagement Class

```
   extras.put('challenge_required','true');

   // user will receive push notification in their registered MFA devices

   identifier =

   UserManagement.initVerificationMethod(Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR,

   'Connect to My Salesforce Org', extras);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // user will need to take the action on their registered MFA devices

   return UserManagement.verifyVerificationMethod(identifier, '',

   Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

   }

##### obfuscateUser(userId, username)

```

Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it. Use this method to set the username to a specific
value after it’s scrambled.

Signature

```
   public static void obfuscateUser(Id userId, String username)

```

Parameters

```
   userId
```

Type: Id

ID of the user whose data this method scrambles.

```
   username
```

Type: String

The username after the user’s data is scrambled. Sets the value of the scrambled username to a specific string.

Return Value

Type: void

Usage

This method is introduced in API version 43.0. It isn't available in earlier versions.

##### You can use the obfuscateUser method to protect the personal information of your org’s users. When invoked, Salesforce

permanently scrambles the user’s object data and replaces it with random character strings. The user’s detail page exists, but the fields
contain meaningless strings of characters. Salesforce merely obfuscates (scrambles) personal data because you can't delete a user in
Salesforce; you can only disable or deactivate a user. In other words, the user record remains in the database and this method performs
a soft delete.

Note: Take care when using this method. The users’ data becomes anonymous and can never be recovered.

**Considerations**

**•** This method requires that the org’s User Management setting, **Scramble Specific Users' Data**, is enabled from Setup.


Apex Reference Guide UserManagement Class

**•** This method affects the standard fields of the user object—excluding a few fields such as the user ID, timezone, locale, and profile.

**•** It is recommended that you note the user's ID and other attributes for post processing, such as the email address, if you want to
send the user a confirmation.

**•** This method changes only the user object. The association between the user and other objects is removed, but no other objects are
changed. For example, contact, ThirdPartyAccountLink (TPAL), and user password authentication (UPA) objects remain unchanged.

Note: Assure your admins that invoking this method doesn’t trigger an email change notification.

This method is part of our effort to protect users’ personal data and privacy. For more information on what you can do to actively protect
user data, see Data Protection and Privacy in Salesforce Help.

##### obfuscateUser(userId)

Scrambles users’ data on their request when they no longer want their personal data recognized in Salesforce. When you invoke the
method for the user, the data becomes anonymous, and you can never recover it.

Signature

```
   public static void obfuscateUser(Id userId)

```

Parameters

```
   userId
```

Type: Id

ID of the user whose data this method scrambles.

Return Value

Type: void

Usage

This method is introduced in API version 43.0. It isn't available in earlier versions.

##### You can use the obfuscateUser method to protect the personal information of your org’s users. When invoked, Salesforce

permanently scrambles the user’s object data and replaces it with random character strings. The user’s detail page exists, but the fields
contain meaningless strings of characters. Salesforce merely obfuscates (scrambles) personal data because you can't delete a user in
Salesforce; you can only disable or deactivate a user. In other words, the user record remains in the database and this method performs
a soft delete.

Note: Take care when using this method. The users’ data becomes anonymous and can never be recovered.

**Considerations**

**•** This method requires that the org’s User Management setting, **Scramble Specific Users' Data**, is enabled from Setup.

**•** This method affects the standard fields of the user object—excluding a few fields such as the user ID, timezone, locale, and profile.

**•** If you want to send the user a confirmation, it’s recommended that you note the user's ID and other attributes for post processing,
such as the email address.

**•** This method changes only the user object. The association between the user and other objects is removed, but no other objects are
changed. For example, contact, ThirdPartyAccountLink (TPAL), and user password authentication (UPA) objects remain unchanged.


Apex Reference Guide UserManagement Class

Note: Assure your admins that invoking this method doesn’t trigger an email change notification.

This method is part of our effort to protect users’ personal data and privacy. For more information on what you can do to actively protect
user data, see Data Protection and Privacy in Salesforce Help.

ObfuscateUser Code Example

```
   public class UserManagementController{

      public List <User> users {get; set;}

      public UserManagementController()

      {

        Profile p = [select id from profile where name = 'Customer Community User'];

        users = [select username, id from User where profileId=:p.id AND isactive=true];

      }

      //Use method with extreme caution. Data can't be recovered.

      @InvocableMethod(label='User Management' description='Obfuscate User data and more')

      static public void obfuscate(List<User> users)

      {

        String uid = ApexPages.currentPage().getParameters().get('uid');

        if(uid == null)

           return;

        User u = [select contactId from user where id=:uid];

        System.UserManagement.obfuscateUser(uid);

      }

   }

##### registerVerificationMethod(method, startUrl)

```

Registers an identity verification method. Verification methods can be a time-based one-time password (TOTP), email or text verification
code, Salesforce Authenticator, or U2F-compatible security key. End users register verification methods for themselves.

Signature

```
   public static System.PageReference registerVerificationMethod(Auth.VerificationMethod

   method, String startUrl)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Verification method used to verify the identity of the user.

```
   startUrl
```

Type: String

Path to the page that users see after they log in.


Apex Reference Guide UserManagement Class

Return Value

Type:System.PageReference

Usage

Use this method to enable users to complete identity verification, such as multi-factor authentication (MFA), or to log in to their Experience
Cloud site without a password. Users register these methods to verify their identity when logging in. You create a custom registration
page when implementing mobile-centric passwordless logins. See VerifyPasswordlessLogin.

The `PageReference` returned by `registerVerificationMethod` redirects the user to the Salesforce Verify page. If the
user enters the correct code, the user is redirected to the Experience Cloud site page specified by the start URL. For example:

```
   PageReference pr =

   System.UserManagement.registerVerificationMethod(Auth.VerificationMethod.TOTP,startUrl);

   PageReference p =

   System.UserManagement.deregisterVerificationMethod(userId,Auth.VerificationMethod.SALESFORCE_AUTHENTICATOR);

```

This method is available in API version 43.0 and later.

Note: As a security measure, when users add or update mobile numbers in their detail page, they must log in again to verify their
identity. As a result, unsaved changes in the app are lost. To disable this security measure, contact Salesforce Support.

##### sendAsyncEmailConfirmation(userId, emailTemplateId, networkId, startUrl)

Send an email message to a user’s email address for verification. The message contains a verification link (URL) that the user clicks to
verify the email address later on. You can send email verifications in bulk.

Signature

```
   public static Boolean sendAsyncEmailConfirmation(String userId, String emailTemplateId,

   String networkId, String startUrl)

```

Parameters

```
   userId
```

Type: String

ID of the user to receive the email confirmation.

```
   emailTemplateId
```

Type: String

ID of the email template in which the verification link is defined. If `null`, Salesforce sends a default email. Here's how the default
email looks.


Apex Reference Guide UserManagement Class

```
   networkId
```

Type: String

If verifying email addresses for Experience Cloud site users, the ID of the Experience Cloud site. In addition to external users (such as
customers and partners), Experience Cloud site users can include internal users (such as employees) who are members of the site.
To verify email addresses for internal users only, set this parameter to `null` .

```
   startUrl
```

Type: String

The user is redirected to this page after verification, with a success or error message as the parameter. If null, the user is redirected
to the login page.

Return Value

Type: Boolean

Indicates whether sending the email message succeeded or failed.

Usage

Sending an async email message is good practice to ensure that users are registered with a valid email address that they truly own. To
determine which users receive an email with the verification link, check whether the User Verified Email field in the User detail page is
set to true. You can also get this information from the `TwoFactorMethodsInfo` API.

Send async email verification to customers and partners to verify their email address. These users must verify their email address before
they can log in with email OTP (passwordless login).

The error code and description are passed as query parameters so that you can process any errors when building a custom landing page.

Example

```
   System.UserManagement.sendAsyncEmailConfirmation('005RM000001a0Ox',

   '00XRM000000hxnG','0DBRM000000015i', '/s/contactsupport');

##### verifyPasswordlessLogin(userId, method, identifier, code, startUrl)

```

Completes a verification challenge during a passwordless login that uses a custom Verify page (Visualforce only). If the user who is trying
to log in enters the verification code successfully, the user is logged in.


Apex Reference Guide UserManagement Class

Signature

```
   public static Auth.VerificationResult verifyPasswordlessLogin(Id userId,

   Auth.VerificationMethod method, String identifier, String code, String startUrl)

```

Parameters

```
   userId
```

Type: Id

ID of the user who’s logging in.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

```
   identifier
```

Type: String

ID of the verification attempt received from the `initPasswordlessLogin` method.

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   startUrl
```

Type: String

The page where the user is directed after successful login.

Return Value

Type: Auth.VerificationResult

Result of the verification challenge, which includes the message displayed, and where the user is directed if they enter the verification
code correctly.

Usage

Call this method to complete the passwordless login authentication process. It validates the verification method and verification code.
It also checks that the identifier is the same as the one returned by `initPasswordlessLogin` on page 4277.

Example

For an example, see `Auth.VerificationResult` .

##### verifyRegisterVerificationMethod(code, method)

Completes registering a user’s email address or phone number as a verification method when customizing the identity verification
process.

Signature

```
   public static String verifyRegisterVerificationMethod(String code,

   Auth.VerificationMethod method)

```


Apex Reference Guide UserManagement Class

Parameters

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

Return Value

Type: String

If the user enters an incorrect verification code, the method returns an error message.

Usage

Call `verifyRegisterVerificationMethod` to complete the process of registering a user’s verification method. This method
checks whether the user entered the correct verification code. If the verification code is correct, the method

**•** Confirms that the user entered the correct verification code

**•** From the user’s detail page, updates the user's verification method status (sets the verification bit)

**•** Sends an email to the user confirming that a verification method has been added to their record

If the verification code is incorrect, an error message is returned.

Note: If users want to change their email address after registering one, don’t use the `initRegisterVerificationMethod`
and `verify RegisterVerificationMethod` methods. To enable automatic identity verification for email address
changes, from the Identity Verification Setup page, select the field **Require email confirmations for email address changes**
**(applies to users in Experience Builder sites)** .

Example

Here’s a code example that registers a user’s phone number as a verification method. When the user enters a verification code on the
Visualforce page, it invokes `registerUser()` . The method gets the User ID of the user who’s registering the verification method
and the user’s phone number. It also gets the user’s registration status to check whether the phone number is verified already. If the
user is registered with a different phone number, the number is updated.

```
   public void registerUser() {

        try {

           exceptionText='';

           String userId = UserInfo.getUserId();

           User u = [Select MobilePhone, Id from User Where Id=:userId];

           currPhone = u.MobilePhone;

           mobilePhone = getFormattedSms(mobilePhone);

          if (mobilePhone != null && mobilePhone != '') {

          u.MobilePhone = mobilePhone;

          update u;

           // We're updating the email and phone number before verifying. Roll back

          // the change in the verify API if it is unsuccessful.

           exceptionText = System.

           UserManagement.initRegisterVerificationMethod(Auth.VerificationMethod.SMS);

           if(exceptionText!= null && exceptionText!=''){

```


Apex Reference Guide UserManagement Class

```
             isInit = false;

             showInitException = true;

           } else {

              isInit = false;

              isVerify = true;

           }

           } else {

             showInitException = true;

           }

        } catch (Exception e) {

           exceptionText = e.getMessage();

           isInit = false;

           showInitException = true;

        }

      }

   public void verifyUser() {

      // Take the user’s input for the code sent to their phone number

      exceptionText = System.UserManagement.

        verifyRegisterVerificationMethod(code, Auth.VerificationMethod.SMS);

      if(exceptionText != null && exceptionText !=''){

      showInitException = true;

      } else {

           //Success

      }

   }

##### verifySelfRegistration(method, identifier, code, startUrl)

```

Completes a verification challenge when creating a custom (Visualforce) Verify page for Experience Cloud site self-registration. If the
person who is attempting to register enters the verification code successfully, the user is created and logged in.

Signature

```
   public static Auth.VerificationResult verifySelfRegistration(Auth.VerificationMethod

   method, String identifier, String code, String startUrl)

```

Parameters

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the identity of the user, which can be either EMAIL or SMS.

```
   identifier
```

Type: String

The unique identifier received from the `initSelfRegistration` method.

```
   code
```

Type: String

Code used to verify the identity of the user.

```
   startUrl
```

Type: String


Apex Reference Guide UserManagement Class

[The page where the user is directed after successful self-registration. For the Self-Registration component, set the Start URL in the](https://help.salesforce.com/s/articleView?id=experience.rss_login_self_register.htm&language=en_US)
component properties instead.

Return Value

Type: Auth.VerificationResult

Result of the verification challenge, which includes the message displayed, and where the user is directed when they enter the verification
code correctly.

Usage

By default, when users sign up for your Experience Cloud site with an email address or phone number, Salesforce sends them a verification
code and generates a Verify page. This Verify page is where users enter the verification code to confirm their identity. You can replace
this Salesforce-generated Verify page with a custom Verify page that you create with Visualforce. Then you invoke the verification process
with Apex methods.

First, call the `initSelfRegistration` method, which returns the identifier of the user to create. Then call this
`verifySelfRegistration` method to complete the verification process. If the user enters the verification code correctly, the
user is created and directed to the page specified in the `startURL` .

This method returns the verification result, which contains the verification status and, if the user is created, the session ID. If the verification
method is SMS, the User object must contain a properly formatted mobile number, which is country code, space, and then phone
number, for example, +1 1234567890. Use `System.UserManagement.formatPhoneNumber` to ensure that the phone
number is formatted correctly.

Example

This code contains the result of a verification challenge that registers a new user.

```
   String id = System.UserManagement.initSelfRegistration

         (Auth.VerificationMethod.SMS, user);

        Auth.VerificationResult res = System.UserManagement.verifySelfRegistration

         (Auth.VerificationMethod.SMS, id, ‘123456’, null);

        if(res.success == true){

      //redirect

   }

##### verifyVerificationMethod(identifier, code, method)

```

Completes the verification service for email, phone (SMS), Salesforce Authenticator, password, or time-based one-time password (TOTP)
verification methods.

Signature

```
   public static VerificationResult verifyVerificationMethod(String identifier, String

   code, Auth.VerificationMethod method)

```

Parameters

```
   identifier
```

Type: String

Identifier returned from `initVerificationMethod` for `EMAIL`, `SMS`, and `SALESFORCE_AUTHENTICATOR` .


Apex Reference Guide UserManagement Class

```
   code
```

Type: String

Code used to verify the user’s identity for `EMAIL`, `SMS`, or `PASSWORD` .

```
   method
```

Type: Auth.VerificationMethod

Method used to verify the user’s identity, which can be `EMAIL`, `PASSWORD`, `SALESFORCE_AUTHENTICATOR`, `SMS`, or `TOTP` .

Return Value

Type: VerificationResult

Usage

Use this method along with its paired `initVerificationMethod` to customize a verification service for `EMAIL`, `SMS`, or
`SALESFORCE_AUTHENTICATOR` verification methods. Or use this method alone to provide a complete verification service for
`PASSWORD` and `TOTP` verification methods.

This method checks whether the user entered the correct verification code or password. If the verification code or password is correct,
the method verifies the user’s identity.

If the verification code or password isn’t valid, the service returns an error message.

Examples

This example shows multi-factor authentication using email.

```
   public void initVerification() {

   // user will receive code on their registered verified email

    identifier = UserManagement.initVerificationMethod(Auth.VerificationMethod.EMAIL);

   }

   public Auth.VerificationResult verifyVerification() {

   // requiring identifier from the initVerification

   // the code will need to be entered in this method

   return UserManagement.verifyVerificationMethod(identifier, code,

   Auth.VerificationMethod.EMAIL);

   }

```

The next two examples show multi-factor authentication using only the `verifyVerificationMethod` for password and TOTP
verifications.

```
   public Auth.VerificationResult verifyVerification() {

   // user will enter their password as a param in the verifyVerificationMethod for password

    verification method

   return UserManagement.verifyVerificationMethod('', password,

   Auth.VerificationMethod.PASSWORD);

   }

   public Auth.VerificationResult verifyVerification() {

   // user will enter their registered time-based one-time password (TOTP) code (token)

   return UserManagement.verifyVerificationMethod('', code, Auth.VerificationMethod.TOTP);

   }

```


### Apex Reference Guide UUID Class UUID Class

Contains methods to randomly generate a version 4 universally unique identifier (UUID), compare UUIDs, and convert UUID instance to
a string.

Namespace

System

Usage

The UUID is generated using a cryptographically strong pseudo-random number generator and is represented as 32 hexadecimal values.

IN THIS SECTION:

#### UUID Methods UUID Methods

### The following are methods for UUID .

IN THIS SECTION:

##### equals(obj)

Compares a UUID instance with the specified object and returns true if both are equal. Otherwise, returns false.

fromString(str)
Converts a 32 character hexadecimal string representation of a UUID to a UUID instance.

hashCode()
Returns the hashcode corresponding to the UUID instance.

randomUUID()
A static method that randomly generates a version 4 UUID.

toString()
Returns the string representation of the UUID instance.

##### **`equals(obj)`**

Compares a UUID instance with the specified object and returns true if both are equal. Otherwise, returns false.

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

The UUID object to be compared.


Apex Reference Guide UUID Class

Return Value

Type: Boolean

Example

```
   // UUIDs are equal when all the characters in the UUID are the same

   String uuidStr = '707b2538-98bb-41e7-95e3-1d77bf42b102';

   UUID fromStr = UUID.fromString(uuidStr);

   UUID fromStr2 = UUID.fromString(uuidStr);

   Assert.isTrue(fromStr.equals(fromStr2));

   // A UUID is never equal to a String or any non-UUID object

   Assert.isFalse(fromStr.equals(uuidStr));

##### **`fromString(str)`**

```

Converts a 32 character hexadecimal string representation of a UUID to a UUID instance.

Signature

```
   public static System.UUID fromString(String str)

```

Parameters

```
   str
```

Type: String

Return Value

Type: System.UUID

Example

```
   String uuidStr = '707b2538-98bb-41e7-95e3-1d77bf42b102';

   UUID fromStr = UUID.fromString(uuidStr);

   UUID.fromString(null); // Throws NullPointerException

   UUID.fromString(‘not a uuid’); // Throws IllegalArgumentException

##### **`hashCode()`**

```

Returns the hashcode corresponding to the UUID instance.

Signature

```
   public Integer hashCode()

```


### Apex Reference Guide Version Class

Return Value

Type: Integer

##### **`randomUUID()`**

A static method that randomly generates a version 4 UUID.

Signature

```
   public static System.UUID randomUUID()

```

Return Value

Type: System.UUID

A 32 hexadecimal value of the UUID generated.

Example

```
   UUID randomUUID = UUID.randomUUID();

   system.debug(randomUUID); // Prints the UUID string that was randomly generated

##### **`toString()`**

```

Returns the string representation of the UUID instance.

Signature

```
   public String toString()

```

Return Value

Type: String

### Version Class

Use the Version methods to get the version of a first-generation managed package (1GP) or a migrated second-generation managed
package (2GP), and to compare package versions.

Namespace

System

Usage

A package version is a number that identifies the set of components uploaded in a package. The version number has the format
_`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major and minor numbers increase to a chosen value
during every major release. The _`patchNumber`_ is generated and updated only for a patch release.


Apex Reference Guide Version Class

A called component can check the version against which the caller was compiled using the `System.requestVersion` on page
4201 method and behave differently depending on the caller’s expectations. This allows you to continue to support existing behavior in
classes and triggers in previous package versions while continuing to evolve the code.

The value returned by the `System.requestVersion` method is an instance of this class with a two-part version number containing
a major and a minor number. Since the `System.requestVersion` method doesn’t return a patch number, the patch number in
the returned Version object is null.

The `System.Version` class can also hold also a three-part version number that includes a patch number.

[See Version Apex Code Behavior in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_manpkgs_behavior.htm) _Apex Developer Guide_ .

Example

This example shows how to use the methods in this class, along with the `requestVersion` method, to determine the managed
package version of the code that is calling your package.

```
   if (System.requestVersion() == new Version(1,0))

   {

      // Do something

   }

   if ((System.requestVersion().major() == 1)

      && (System.requestVersion().minor() > 0)

      && (System.requestVersion().minor() <=9))

   {

      // Do something different for versions 1.1 to 1.9

   }

   else if (System.requestVersion().compareTo(new Version(2,0)) >= 0)

   {

      // Do something completely different for versions 2.0 or greater

   }

```

IN THIS SECTION:

#### Version Constructors

Version Methods

#### Version Constructors The following are constructors for Version .

IN THIS SECTION:

##### Version(major, minor)
#### Creates a new instance of the Version class as a two-part package version using the specified major and minor version numbers.

Version(major, minor, patch)
#### Creates a new instance of the Version class as a three-part package version using the specified major, minor, and patch version

numbers.

##### Version(major, minor)

#### Creates a new instance of the Version class as a two-part package version using the specified major and minor version numbers.


Apex Reference Guide Version Class

Signature

```
   public Version(Integer major, Integer minor)

```

Parameters

```
   major
```

Type: Integer

The major version number.

```
   minor
```

Type: Integer

The minor version number.

##### Version(major, minor, patch) Creates a new instance of the Version class as a three-part package version using the specified major, minor, and patch version

numbers.

Signature

```
   public Version(Integer major, Integer minor, Integer patch)

```

Parameters

```
   major
```

Type: Integer

The major version number.

```
   minor
```

Type: Integer

The minor version number.

```
   patch
```

Type: Integer

The patch version number.

#### Version Methods

##### The following are methods for Version . All are instance methods.

IN THIS SECTION:

compareTo(version)
Compares the current version with the specified version.

major()
Returns the major package version of the of the calling code.

minor()
Returns the minor package version of the calling code.


Apex Reference Guide Version Class

patch()
Returns the patch package version of the calling code or `null` if there is no patch version.

##### compareTo(version)

Compares the current version with the specified version.

Signature

```
   public Integer compareTo(System.Version version)

```

Parameters

```
   version
```

Type: System.Version

Return Value

Type: Integer

Returns one of the following values:

**•** zero if the current package version is equal to the specified package version

**•** an Integer value greater than zero if the current package version is greater than the specified package version

**•** an Integer value less than zero if the current package version is less than the specified package version

Usage

If a two-part version is being compared to a three-part version, the patch number is ignored and the comparison is based only on the
major and minor numbers.

##### major()

Returns the major package version of the of the calling code.

Signature

```
   public Integer major()

```

Return Value

Type: Integer

##### minor()

Returns the minor package version of the calling code.

Signature

```
   public Integer minor()

```


### Apex Reference Guide WebServiceCallout Class

Return Value

Type: Integer

##### patch()

Returns the patch package version of the calling code or `null` if there is no patch version.

Signature

```
   public Integer patch()

```

Return Value

Type: Integer

### WebServiceCallout Class

Enables making callouts to SOAP operations on an external Web service. This class is used in the Apex stub class that is auto-generated
from a WSDL.

Namespace

System

IN THIS SECTION:

#### WebServiceCallout Methods

SEE ALSO:

_Apex Developer Guide_ [: SOAP Services: Defining a Class from a WSDL Document](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex.htm)

#### WebServiceCallout Methods

### The following is the static method for WebServiceCallout .

IN THIS SECTION:

##### invoke(stub, request, response, infoArray)

Invokes an external SOAP web service operation based on an Apex class that is auto-generated from a WSDL.

##### invoke(stub, request, response, infoArray)

Invokes an external SOAP web service operation based on an Apex class that is auto-generated from a WSDL.

Signature

```
   public static void invoke(Object stub, Object request, Map<String,Object> response,

   List<String> infoArray)

```


### Apex Reference Guide WebServiceMock Interface

Parameters

```
   stub
```

Type: Object

An instance of the Apex class that is auto-generated from a WSDL (the stub class).

```
   request
```

Type: Object

The request to the external service. The request is an instance of a type that is created as part of the auto-generated stub class.

```
   response
```

Type: Map<String, Object>

A map of key-value pairs that represent the response that the external service sends after receiving the request. In each pair, the key
is a response identifier. The value is the response object, which is an instance of a type that is created as part of the auto-generated
stub class.

```
   infoArray
```

Type: String[]

An array of strings that contains information about the callout—web service endpoint, SOAP action, request, and response. The
order of the elements in the array matters.

**•** Element at index 0 ( `[0]` ): One of the following options for identifying the URL of the external web service.

**–** Endpoint URL. For example: `'http://YourServer/YourService'`

**–** Named credential URL, which contains the scheme `callout`, the name of the named credential, and optionally, an
appended path. For example: `'callout:MyNamedCredential/some/path'`

**•** Element at index 1 ( `[1]` ): The SOAP action. For example:

```
      'urn:dotnet.callouttest.soap.sforce.com/EchoString'

```

**•** Element at index 2 ( `[2]` ): The request namespace. For example: `'http://doc.sample.com/docSample'`

**•** Element at index 3 ( `[3]` ): The request name. For example: `'EchoString'`

**•** Element at index 4 ( `[4]` ): The response namespace. For example: `'http://doc.sample.com/docSample'`

**•** Element at index 5 ( `[5]` ): The response name. For example: `'EchoStringResponse'`

**•** Element at index 6 ( `[6]` ): The response type. For example: `'docSample.EchoStringResponse_element'`

Return Value

Type: Void

SEE ALSO:

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### WebServiceMock Interface

Enables sending fake responses when testing Web service callouts of a class auto-generated from a WSDL.

Namespace

System


Apex Reference Guide WebServiceMock Interface

Usage

[For an implementation example, see Test Web Service Callouts.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_wsdl2apex_testing.htm)

#### WebServiceMock Methods The following are methods for WebServiceMock .

IN THIS SECTION:

##### doInvoke(stub, soapRequest, responseMap, endpoint, soapAction, requestName, responseNamespace, responseName, responseType)

The implementation of this method is called by the Apex runtime to send a fake response when a Web service callout is made after
`Test.setMock` has been called.

##### doInvoke(stub, soapRequest, responseMap, endpoint, soapAction, requestName,

responseNamespace, responseName, responseType)

The implementation of this method is called by the Apex runtime to send a fake response when a Web service callout is made after
`Test.setMock` has been called.

Signature

```
   public Void doInvoke(Object stub, Object soapRequest, Map<String,Object> responseMap,

   String endpoint, String soapAction, String requestName, String responseNamespace, String

   responseName, String responseType)

```

Parameters

```
   stub
```

Type: Object

An instance of the auto-generated class.

```
   soapRequest
```

Type: Object

The SOAP Web service request being invoked.

```
   responseMap
```

Type: Map<String, Object>

A collection of key/value pairs representing the response to send for the request.

When implementing this interface, set the _`responseMap`_ argument to a key/value pair representing the response desired.

```
   endpoint
```

Type: String

The endpoint URL for the request.

```
   soapAction
```

Type: String

The requested SOAP operation.

```
   requestName
```

Type: String


### Apex Reference Guide XmlStreamReader Class Class

The requested SOAP operation name.

```
   responseNamespace
```

Type: String

The response namespace.

```
   responseName
```

Type: String

The name of the response element as defined in the WSDL.

```
   responseType
```

Type: String

The class for the response as defined in the auto-generated class.

Return Value

Type: Void

Usage

### XmlStreamReader Class Class The XmlStreamReader class provides methods for forward, read-only access to XML data. You can pull data from XML or skip

unwanted events. You can parse nested XML content that’s up to 50 nodes deep.

Namespace

System

Usage

### The XmlStreamReader class is similar to the XMLStreamReader utility class from StAX (Streaming API for XML). StAX is an API to

read and write XML documents, originating from the Java programming language community.

### Note: The XmlStreamReader class in Apex is based on its counterpart in Java. See Java XMLStreamReader class .

IN THIS SECTION:

#### XmlStreamReader Constructors

XmlStreamReader Methods

SEE ALSO:

_Apex Developer Guide_ [: Reading XML Using Streams](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_xml_streaming_reading.htm)

#### XmlStreamReader Constructors

### The following are constructors for XmlStreamReader .


Apex Reference Guide XmlStreamReader Class Class

IN THIS SECTION:

##### XmlStreamReader(xmlInput) Creates a new instance of the XmlStreamReader class for the specified XML input. XmlStreamReader(xmlInput) Creates a new instance of the XmlStreamReader class for the specified XML input.

Signature

```
   public XmlStreamReader(String xmlInput)

```

Parameters

```
   xmlInput
```

Type: String

The XML string input.

#### XmlStreamReader Methods

##### The following are methods for XmlStreamReader . All are instance methods.

IN THIS SECTION:

getAttributeCount()
Returns the number of attributes on the start element, excluding namespace definitions.

getAttributeLocalName(index)
Returns the local name of the attribute at the specified index.

getAttributeNamespace(index)
Returns the namespace URI of the attribute at the specified index.

getAttributePrefix(index)
Returns the prefix of this attribute at the specified index.

getAttributeType(index)
Returns the XML type of the attribute at the specified index.

getAttributeValue(namespaceUri, localName)
Returns the value of the attribute in the specified _`localName`_ at the specified URI.

getAttributeValueAt(index)
Returns the value of the attribute at the specified index.

getEventType()
Returns the type of XML event the cursor is pointing to.

getLocalName()
Returns the local name of the current event.

getLocation()
Return the current location of the cursor.


Apex Reference Guide XmlStreamReader Class Class

getNamespace()
If the current event is a start element or end element, this method returns the URI of the prefix or the default namespace.

getNamespaceCount()
Returns the number of namespaces declared on a start element or end element.

getNamespacePrefix(index)
Returns the prefix for the namespace declared at the index.

getNamespaceURI(prefix)
Return the URI for the given prefix.

getNamespaceURIAt(index)
Returns the URI for the namespace declared at the index.

getPIData()
Returns the data section of a processing instruction.

getPITarget()
Returns the target section of a processing instruction.

getPrefix()
Returns the prefix of the current XML event or `null` if the event does not have a prefix.

getText()
Returns the current value of the XML event as a string.

getVersion()
Returns the XML version specified on the XML declaration. Returns `null` if none was declared.

hasName()
Returns `true` if the current XML event has a name. Returns `false` otherwise.

hasNext()
Returns `true` if there are more XML events and `false` if there are no more XML events.

hasText()
Returns `true` if the current event has text, `false` otherwise.

isCharacters()
Returns `true` if the cursor points to a character data XML event. Otherwise, returns `false` .

isEndElement()
Returns `true` if the cursor points to an end tag. Otherwise, it returns `false` .

isStartElement()
Returns `true` if the cursor points to a start tag. Otherwise, it returns `false` .

isWhiteSpace()
Returns `true` if the cursor points to a character data XML event that consists of all white space. Otherwise it returns `false` .

next()
Reads the next XML event. A processor may return all contiguous character data in a single chunk, or it may split it into several
chunks. Returns an integer which indicates the type of event.

nextTag()
Skips any white space (the `isWhiteSpace` method returns `true` ), comment, or processing instruction XML events, until a start
element or end element is reached. Returns the index for that XML event.


Apex Reference Guide XmlStreamReader Class Class

setCoalescing(returnAsSingleBlock)
If you specify `true` for _`returnAsSingleBlock`_, text is returned in a single block, from a start element to the first end element
or the next start element, whichever comes first. If you specify it as `false`, the parser may return text in multiple blocks.

setNamespaceAware(isNamespaceAware)
If you specify `true` for _`isNamespaceAware`_, the parser recognizes namespace. If you specify it as `false`, the parser does
not. The default value is `true` .

toString()
Returns a string containing the length of the input XML given to `XmlStreamReader` and the first 50 characters of the input
XML.

##### getAttributeCount()

Returns the number of attributes on the start element, excluding namespace definitions.

Signature

```
   public Integer getAttributeCount()

```

Return Value

Type: Integer

Usage

This method is only valid on a start element or attribute XML events. The count for the number of attributes for an attribute XML event
starts with zero.

##### getAttributeLocalName(index)

Returns the local name of the attribute at the specified index.

Signature

```
   public String getAttributeLocalName(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If there is no name, an empty string is returned. This method is only valid with start element or attribute XML events.


Apex Reference Guide XmlStreamReader Class Class

##### getAttributeNamespace(index)

Returns the namespace URI of the attribute at the specified index.

Signature

```
   public String getAttributeNamespace(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If no namespace is specified, `null` is returned. This method is only valid with start element or attribute XML events.

##### getAttributePrefix(index)

Returns the prefix of this attribute at the specified index.

Signature

```
   public String getAttributePrefix(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

If no prefix is specified, `null` is returned. This method is only valid with start element or attribute XML events.

##### getAttributeType(index)

Returns the XML type of the attribute at the specified index.

Signature

```
   public String getAttributeType(Integer index)

```


Apex Reference Guide XmlStreamReader Class Class

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

For example, `id` is an attribute type. This method is only valid with start element or attribute XML events.

##### getAttributeValue(namespaceUri, localName)

Returns the value of the attribute in the specified _`localName`_ at the specified URI.

Signature

```
   public String getAttributeValue(String namespaceUri, String localName)

```

Parameters

```
   namespaceUri
```

Type: String

```
   localName
```

Type: String

Return Value

Type: String

Usage

Returns `null` if the value is not found. You must specify a value for _`localName`_ . This method is only valid with start element or
attribute XML events.

##### getAttributeValueAt(index)

Returns the value of the attribute at the specified index.

Signature

```
   public String getAttributeValueAt(Integer index)

```

Parameters

```
   index
```

Type: Integer


Apex Reference Guide XmlStreamReader Class Class

Return Value

Type: String

Usage

This method is only valid with start element or attribute XML events.

##### getEventType()

Returns the type of XML event the cursor is pointing to.

Signature

```
   public System.XmlTag getEventType()

```

Return Value

Type: System.XmlTag

**`XmlTag`** Enum

The values for `XmlTag` are:

**•** `ATTRIBUTE`

**•** `CDATA`

**•** `CHARACTERS`

**•** `COMMENT`

**•** `DTD`

**•** `END_DOCUMENT`

**•** `END_ELEMENT`

**•** `ENTITY_DECLARATION`

**•** `ENTITY_REFERENCE`

**•** `NAMESPACE`

**•** `NOTATION_DECLARATION`

**•** `PROCESSING_INSTRUCTION`

**•** `SPACE`

**•** `START_DOCUMENT`

**•** `START_ELEMENT`

##### getLocalName()

Returns the local name of the current event.

Signature

```
   public String getLocalName()

```


Apex Reference Guide XmlStreamReader Class Class

Return Value

Type: String

Usage

For start element or end element XML events, it returns the local name of the current element. For the entity reference XML event, it
returns the entity name. The current XML event must be start element, end element, or entity reference.

##### getLocation()

Return the current location of the cursor.

Signature

```
   public String getLocation()

```

Return Value

Type: String

Usage

If the location is unknown, returns -1. The location information is only valid until the `next` method is called.

##### getNamespace()

If the current event is a start element or end element, this method returns the URI of the prefix or the default namespace.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Usage

Returns `null` if the XML event does not have a prefix.

##### getNamespaceCount()

Returns the number of namespaces declared on a start element or end element.

Signature

```
   public Integer getNamespaceCount()

```

Return Value

Type: Integer


Apex Reference Guide XmlStreamReader Class Class

Usage

This method is only valid on a start element, end element, or namespace XML event.

##### getNamespacePrefix(index)

Returns the prefix for the namespace declared at the index.

Signature

```
   public String getNamespacePrefix(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

Returns `null` if this is the default namespace declaration. This method is only valid on a start element, end element, or namespace
XML event.

##### getNamespaceURI(prefix)

Return the URI for the given prefix.

Signature

```
   public String getNamespaceURI(String prefix)

```

Parameters

```
   prefix
```

Type: String

Return Value

Type: String

Usage

The returned URI depends on the current state of the processor.

##### getNamespaceURIAt(index)

Returns the URI for the namespace declared at the index.


Apex Reference Guide XmlStreamReader Class Class

Signature

```
   public String getNamespaceURIAt(Integer index)

```

Parameters

```
   index
```

Type: Integer

Return Value

Type: String

Usage

This method is only valid on a start element, end element, or namespace XML event.

##### getPIData()

Returns the data section of a processing instruction.

Signature

```
   public String getPIData()

```

Return Value

Type: String

##### getPITarget()

Returns the target section of a processing instruction.

Signature

```
   public String getPITarget()

```

Return Value

Type: String

##### getPrefix()

Returns the prefix of the current XML event or `null` if the event does not have a prefix.

Signature

```
   public String getPrefix()

```

Return Value

Type: String


Apex Reference Guide XmlStreamReader Class Class

##### getText()

Returns the current value of the XML event as a string.

Signature

```
   public String getText()

```

Return Value

Type: String

Usage

The valid values for the different events are:

**•** The string value of a character XML event

**•** The string value of a comment

##### • The replacement value for an entity reference. For example, assume getText reads the following XML snippet:

```
     <!ENTITY

      Title "Salesforce For Dummies" >

        ]>

      <moo a=\"b\">Name &Title;</moo>';

##### The getText method returns Salesforce for Dummies, not &Title .

```

**•** The string value of a CDATA section

**•** The string value for a space XML event

**•** The string value of the internal subset of the DTD

##### getVersion()

Returns the XML version specified on the XML declaration. Returns `null` if none was declared.

Signature

```
   public String getVersion()

```

Return Value

Type: String

##### hasName()

Returns `true` if the current XML event has a name. Returns `false` otherwise.

Signature

```
   public Boolean hasName()

```


Apex Reference Guide XmlStreamReader Class Class

Return Value

Type: Boolean

Usage

This method is only valid for start element and stop element XML events.

##### hasNext()

Returns `true` if there are more XML events and `false` if there are no more XML events.

Signature

```
   public Boolean hasNext()

```

Return Value

Type: Boolean

Usage

This method returns `false` if the current XML event is end document.

##### hasText()

Returns `true` if the current event has text, `false` otherwise.

Signature

```
   public Boolean hasText()

```

Return Value

Type: Boolean

Usage

The following XML events have text: characters, entity reference, comment and space.

##### isCharacters()

Returns `true` if the cursor points to a character data XML event. Otherwise, returns `false` .

Signature

```
   public Boolean isCharacters()

```

Return Value

Type: Boolean


Apex Reference Guide XmlStreamReader Class Class

##### isEndElement()

Returns `true` if the cursor points to an end tag. Otherwise, it returns `false` .

Signature

```
   public Boolean isEndElement()

```

Return Value

Type: Boolean

##### isStartElement()

Returns `true` if the cursor points to a start tag. Otherwise, it returns `false` .

Signature

```
   public Boolean isStartElement()

```

Return Value

Type: Boolean

##### isWhiteSpace()

Returns `true` if the cursor points to a character data XML event that consists of all white space. Otherwise it returns `false` .

Signature

```
   public Boolean isWhiteSpace()

```

Return Value

Type: Boolean

##### next()

Reads the next XML event. A processor may return all contiguous character data in a single chunk, or it may split it into several chunks.
Returns an integer which indicates the type of event.

Signature

```
   public Integer next()

```

Return Value

Type: Integer


Apex Reference Guide XmlStreamReader Class Class

##### nextTag()

Skips any white space (the `isWhiteSpace` method returns `true` ), comment, or processing instruction XML events, until a start
element or end element is reached. Returns the index for that XML event.

Signature

```
   public Integer nextTag()

```

Return Value

Type: Integer

Usage

This method throws an error if elements other than white space, comments, processing instruction, start elements or stop elements are
encountered.

##### setCoalescing(returnAsSingleBlock)

If you specify `true` for _`returnAsSingleBlock`_, text is returned in a single block, from a start element to the first end element
or the next start element, whichever comes first. If you specify it as `false`, the parser may return text in multiple blocks.

Signature

```
   public Void setCoalescing(Boolean returnAsSingleBlock)

```

Parameters

```
   returnAsSingleBlock
```

Type: Boolean

Return Value

Type: Void

##### setNamespaceAware(isNamespaceAware)

If you specify `true` for _`isNamespaceAware`_, the parser recognizes namespace. If you specify it as `false`, the parser does not.
The default value is `true` .

Signature

```
   public Void setNamespaceAware(Boolean isNamespaceAware)

```

Parameters

```
   isNamespaceAware
```

Type: Boolean


### Apex Reference Guide XmlStreamWriter Class

Return Value

Type: Void

##### toString()

Returns a string containing the length of the input XML given to `XmlStreamReader` and the first 50 characters of the input XML.

Signature

```
   public String toString()

```

Return Value

Type: String

### XmlStreamWriter Class The XmlStreamWriter class provides methods for writing XML data.

Namespace

System

Usage

### You can use the XmlStreamWriter class to programmatically construct an XML document, then use HTTP classes to send the

document to an external server.

### The XmlStreamWriter class is similar to the XMLStreamWriter utility class from StAX (Streaming API for XML). StAX is an API to

read and write XML documents, originating from the Java programming language community.

### Note: The XmlStreamWriter class in Apex is based on its counterpart in Java. See Java XMLStreamWriter class .

IN THIS SECTION:

#### XmlStreamWriter Constructors

XmlStreamWriter Methods

SEE ALSO:

Http Class

HttpRequest Class

HttpResponse Class

#### XmlStreamWriter Constructors

### The following are constructors for XmlStreamWriter .


Apex Reference Guide XmlStreamWriter Class

IN THIS SECTION:

##### XmlStreamWriter() Creates a new instance of the XmlStreamWriter class. XmlStreamWriter() Creates a new instance of the XmlStreamWriter class.

Signature

```
   public XmlStreamWriter()

#### XmlStreamWriter Methods

##### The following are methods for XmlStreamWriter . All are instance methods.

```

IN THIS SECTION:

close()
Closes this instance of an XmlStreamWriter and free any resources associated with it.

getXmlString()
Returns the XML written by the XmlStreamWriter instance.

setDefaultNamespace(uri)
Binds the specified URI to the default namespace. This URI is bound in the scope of the current START_ELEMENT – END_ELEMENT
pair.

writeAttribute(prefix, namespaceUri, localName, value)
Writes an attribute to the output stream.

writeCData(data)
Writes the specified CData to the output stream.

writeCharacters(text)
Writes the specified text to the output stream.

writeComment(comment)
Writes the specified comment to the output stream.

writeDefaultNamespace(namespaceUri)
Writes the specified namespace to the output stream.

writeEmptyElement(prefix, localName, namespaceUri)
Writes an empty element tag to the output stream.

writeEndDocument()
Closes any start tags and writes corresponding end tags to the output stream.

writeEndElement()
Writes an end tag to the output stream, relying on the internal state of the writer to determine the prefix and local name.

writeNamespace(prefix, namespaceUri)
Writes the specified namespace to the output stream.


Apex Reference Guide XmlStreamWriter Class

writeProcessingInstruction(target, data)
Writes the specified processing instruction.

writeStartDocument(encoding, version)
Writes the XML Declaration using the specified XML encoding and version.

writeStartElement(prefix, localName, namespaceUri)
Writes the start tag specified by _`localName`_ to the output stream.

##### close()

Closes this instance of an XmlStreamWriter and free any resources associated with it.

Signature

```
   public Void close()

```

Return Value

Type: Void

##### getXmlString()

Returns the XML written by the XmlStreamWriter instance.

Signature

```
   public String getXmlString()

```

Return Value

Type: String

##### setDefaultNamespace(uri)

Binds the specified URI to the default namespace. This URI is bound in the scope of the current START_ELEMENT – END_ELEMENT pair.

Signature

```
   public Void setDefaultNamespace(String uri)

```

Parameters

```
   uri
```

Type: String

Return Value

Type: Void


Apex Reference Guide XmlStreamWriter Class

##### writeAttribute(prefix, namespaceUri, localName, value)

Writes an attribute to the output stream.

Signature

```
   public Void writeAttribute(String prefix, String namespaceUri, String localName, String

   value)

```

Parameters

```
   prefix
```

Type: String

```
   namespaceUri
```

Type: String

```
   localName
```

Type: String

Specifies the name of the attribute.

```
   value
```

Type: String

Return Value

Type: Void

##### writeCData(data)

Writes the specified CData to the output stream.

Signature

```
   public Void writeCData(String data)

```

Parameters

```
   data
```

Type: String

Return Value

Type: Void

##### writeCharacters(text)

Writes the specified text to the output stream.

Signature

```
   public Void writeCharacters(String text)

```


Apex Reference Guide XmlStreamWriter Class

Parameters

```
   text
```

Type: String

Return Value

Type: Void

##### writeComment(comment)

Writes the specified comment to the output stream.

Signature

```
   public Void writeComment(String comment)

```

Parameters

```
   comment
```

Type: String

Return Value

Type: Void

##### writeDefaultNamespace(namespaceUri)

Writes the specified namespace to the output stream.

Signature

```
   public Void writeDefaultNamespace(String namespaceUri)

```

Parameters

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeEmptyElement(prefix, localName, namespaceUri)

Writes an empty element tag to the output stream.

Signature

```
   public Void writeEmptyElement(String prefix, String localName, String namespaceUri)

```


Apex Reference Guide XmlStreamWriter Class

Parameters

```
   prefix
```

Type: String

```
   localName
```

Type: String

Specifies the name of the tag to be written.

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeEndDocument()

Closes any start tags and writes corresponding end tags to the output stream.

Signature

```
   public Void writeEndDocument()

```

Return Value

Type: Void

##### writeEndElement()

Writes an end tag to the output stream, relying on the internal state of the writer to determine the prefix and local name.

Signature

```
   public Void writeEndElement()

```

Return Value

Type: Void

##### writeNamespace(prefix, namespaceUri)

Writes the specified namespace to the output stream.

Signature

```
   public Void writeNamespace(String prefix, String namespaceUri)

```

Parameters

```
   prefix
```

Type: String


Apex Reference Guide XmlStreamWriter Class

```
   namespaceUri
```

Type: String

Return Value

Type: Void

##### writeProcessingInstruction(target, data)

Writes the specified processing instruction.

Signature

```
   public Void writeProcessingInstruction(String target, String data)

```

Parameters

```
   target
```

Type: String

```
   data
```

Type: String

Return Value

Type: Void

##### writeStartDocument(encoding, version)

Writes the XML Declaration using the specified XML encoding and version.

Signature

```
   public Void writeStartDocument(String encoding, String version)

```

Parameters

```
   encoding
```

Type: String

```
   version
```

Type: String

Return Value

Type: Void

##### writeStartElement(prefix, localName, namespaceUri)

Writes the start tag specified by _`localName`_ to the output stream.


## Apex Reference Guide TerritoryMgmt Namespace

Signature

```
   public Void writeStartElement(String prefix, String localName, String namespaceUri)

```

Parameters

```
   prefix
```

Type: String

```
   localName
```

Type: String

```
   namespaceUri
```

Type: String

Return Value

Type: Void

## TerritoryMgmt Namespace The TerritoryMgmt namespace provides an interface used for territory management. The following is the interface in the TerritoryMgmt namespace.

IN THIS SECTION:

### OpportunityTerritory2AssignmentFilter Global Interface

Apex interface that allows an implementing class to assign a single territory to an opportunity.

### OpportunityTerritory2AssignmentFilter Global Interface

Apex interface that allows an implementing class to assign a single territory to an opportunity.

Namespace

## TerritoryMgmt

Usage

Method called by Opportunity Territory Assignment job to assign territory to opportunity. Input is a list of (up to 1000) opportunityIds
that have IsExcludedFromTerritory2Filter=false. Returns a map of OpportunityId to Territory2Id, which is used to update the Territory2Id
field on the Opportunity object.

IN THIS SECTION:

OpportunityTerritory2AssignmentFilter Methods

OpportunityTerritory2AssignmentFilter Example Implementation


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

#### OpportunityTerritory2AssignmentFilter Methods The following are methods for OpportunityTerritory2AssignmentFilter .

IN THIS SECTION:

##### getOpportunityTerritory2Assignments(opportunityIds)

Returns the mapping of opportunities to territory IDs. When Salesforce invokes this method, it supplies the list of opportunity IDs,
except for opportunities that have been excluded from territory assignment (IsExcludedFromTerritory2Filter=false).

##### getOpportunityTerritory2Assignments(opportunityIds)

Returns the mapping of opportunities to territory IDs. When Salesforce invokes this method, it supplies the list of opportunity IDs, except
for opportunities that have been excluded from territory assignment (IsExcludedFromTerritory2Filter=false).

Signature

```
   public Map<Id,Id> getOpportunityTerritory2Assignments(List<Id> opportunityIds)

```

Parameters

```
   opportunityIds
```

Type: List<Id>

Opportunity IDs.

Return Value

Type: Map<Id,Id>

A key value pair associating each Territory ID to an Opportunity ID.

#### OpportunityTerritory2AssignmentFilter Example Implementation

This is an example implementation of the `TerritoryMgmt.OpportunityTerritory2AssignmentFilter` interface.

```
   /*** Apex version of the default logic.

   * If opportunity's assigned account is assigned to

   * Case 1: 0 territories in active model

   * then set territory2Id = null

   * Case 2: 1 territory in active model

   * then set territory2Id = account's territory2Id

   * Case 3: 2 or more territories in active model

   * then set territory2Id = account's territory2Id that is of highest priority.

   * But if multiple territories have same highest priority, then set territory2Id

    = null

   */

   global class OppTerrAssignDefaultLogicFilter implements

   TerritoryMgmt.OpportunityTerritory2AssignmentFilter {

      /**

      * No-arg constructor.

      */

      global OppTerrAssignDefaultLogicFilter() {}

```


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

```
      /**

       * Get mapping of opportunity to territory2Id. The incoming list of opportunityIds

   contains only those with IsExcludedFromTerritory2Filter=false.

       * If territory2Id = null in result map, clear the opportunity.territory2Id if set.

       * If opportunity is not present in result map, its territory2Id remains intact.

       */

      global Map<Id,Id> getOpportunityTerritory2Assignments(List<Id> opportunityIds) {

        Map<Id, Id> OppIdTerritoryIdResult = new Map<Id, Id>();

        // Get the active territory model Id

        Id activeModelId = getActiveModelId();

        if(activeModelId != null){

           List<Opportunity> opportunities =

            [Select Id, AccountId, Territory2Id from Opportunity where Id IN

   :opportunityIds];

           Set<Id> accountIds = new Set<Id>();

           // Create set of parent accountIds

           for(Opportunity opp:opportunities){

             if(opp.AccountId != null){

               accountIds.add(opp.AccountId);

               }

             }

             Map<Id,Territory2Priority> accountMaxPriorityTerritory =

   getAccountMaxPriorityTerritory(activeModelId, accountIds);

           // For each opportunity, assign the highest priority territory if there is no

    conflict, else assign null.

           for(Opportunity opp: opportunities){

            Territory2Priority tp = accountMaxPriorityTerritory.get(opp.AccountId);

            // Assign highest priority territory if there is only 1.

           if((tp != null) && (tp.moreTerritoriesAtPriority == false) && (tp.territory2Id

    != opp.Territory2Id)){

               OppIdTerritoryIdResult.put(opp.Id, tp.territory2Id);

            }else{

               OppIdTerritoryIdResult.put(opp.Id, null);

            }

           }

        }

        return OppIdTerritoryIdResult;

      }

      /**

       * Query assigned territoryIds in active model for given accountIds.

       * Create a map of accountId to max priority territory.

       */

      private Map<Id,Territory2Priority> getAccountMaxPriorityTerritory(Id activeModelId,

   Set<Id> accountIds){

        Map<Id,Territory2Priority> accountMaxPriorityTerritory = new

   Map<Id,Territory2Priority>();

        for(ObjectTerritory2Association ota:[Select ObjectId, Territory2Id,

   Territory2.Territory2Type.Priority from ObjectTerritory2Association where objectId IN

```


Apex Reference Guide OpportunityTerritory2AssignmentFilter Global Interface

```
   :accountIds and Territory2.Territory2ModelId = :activeModelId]){

           Territory2Priority tp = accountMaxPriorityTerritory.get(ota.ObjectId);

           if((tp == null) || (ota.Territory2.Territory2Type.Priority > tp.priority)){

             // If this is the first territory examined for account or it has greater

   priority than current highest priority territory, then set this as new highest priority

   territory.

             tp = new

   Territory2Priority(ota.Territory2Id,ota.Territory2.Territory2Type.priority,false);

           }else if(ota.Territory2.Territory2Type.priority == tp.priority){

             // The priority of current highest territory is same as this, so set

   moreTerritoriesAtPriority to indicate multiple highest priority territories seen so far.

             tp.moreTerritoriesAtPriority = true;

           }

           accountMaxPriorityTerritory.put(ota.ObjectId, tp);

        }

        return accountMaxPriorityTerritory;

      }

      /**

      * Get the Id of the Active Territory Model.

      * If none exists, return null.

      */

      private Id getActiveModelId() {

        List<Territory2Model> models = [Select Id from Territory2Model where State =

   'Active'];

        Id activeModelId = null;

        if(models.size() == 1){

           activeModelId = models.get(0).Id;

        }

        return activeModelId;

      }

      /**

      * Helper class to help capture territory2Id, its priority, and whether there are more

    territories with same priority assigned to the account.

      */

      private class Territory2Priority {

        public Id territory2Id { get; set; }

        public Integer priority { get; set; }

        public Boolean moreTerritoriesAtPriority { get; set; }

        Territory2Priority(Id territory2Id, Integer priority, Boolean

   moreTerritoriesAtPriority){

           this.territory2Id = territory2Id;

           this.priority = priority;

           this.moreTerritoriesAtPriority = moreTerritoriesAtPriority;

        }

      }

   }

```


## Apex Reference Guide TxnSecurity Namespace TxnSecurity Namespace The TxnSecurity namespace provides an interface used for transaction security. The following is the interface and its supporting class in the TxnSecurity namespace.

IN THIS SECTION:

### Event Class

Contains event information that the `evaluate` method uses to evaluate a transaction security policy.

EventCondition Interface
Allows an implementing class to specify whether to take action when certain events occur based on a transaction security policy.
This interface is only used for Apex policies created in Real-Time Event Monitoring.

AsyncCondition Interface
Allows an implementing class to make asynchronous Apex calls. This interface is used only for transaction security Apex policies
created in Real-Time Event Monitoring.

PolicyCondition Interface
Apex interface that allows an implementing class to specify actions to take when certain events occur based on a transaction security
policy.

### Event Class

Contains event information that the `evaluate` method uses to evaluate a transaction security policy.

Namespace

## TxnSecurity

Usage

The Event class contains the information needed to determine if the event triggers a Transaction Security policy. Not all class attributes
are used for every type of event.

Tip: The `EventClass` interface applies only to Legacy Transaction Security, which is a retired feature as of Summer '20. Use
the `EventCondition` interface instead of the `EventClass` interface.

IN THIS SECTION:

#### Event Constructors

Event Properties

#### Event Constructors

### The following is the constructor for Event .


Apex Reference Guide Event Class

IN THIS SECTION:

##### Event()

Creates an instance of the `TxnSecurity.Event` class.

##### Event()

Creates an instance of the `TxnSecurity.Event` class.

Signature

```
   public Event()

#### Event Properties

##### The following are properties for Event .

```

IN THIS SECTION:

##### action

Specifies the action being taken on the resource for an Entity event. For example, a Login IP resource for an Entity event could have
##### an action of create . The action attribute is not used by any other event type.

data
Contains data used by actions. For example, `data` for a login event includes the login history ID. Returns a map whose keys are
the type of event data, like `SourceIp` .

entityId
The ID of any entity associated with the event. For example, the `entityId` of a DataExport event for an Account object contains
the Account ID.

entityName
The name of the object the event acts on.

organizationId
The ID of the Salesforce org where the event occurred.

resourceType
The type of resource for the event. For example, an AccessResource event could have a Connected Application as a resource type.
Not all event types have resources.

timeStamp
The time the event occurred.

userId
Identifies the user that caused the event.

##### action

Specifies the action being taken on the resource for an Entity event. For example, a Login IP resource for an Entity event could have an
##### action of create . The action attribute is not used by any other event type.


Apex Reference Guide Event Class

Signature

```
   public String action {get; set;}

```

Property Value

Type: String

##### data Contains data used by actions. For example, data for a login event includes the login history ID. Returns a map whose keys are the

type of event data, like `SourceIp` .

Signature

```
   public Map<String,String> data {get; set;}

```

Property Value

Type: Map<String, String>

The following table lists all the available data types. Not all types appear with all event types. The data type values are always string
representations. For example, the `isApi` value is a string in the map, but is actually a Boolean value. Convert the value from a string
to its true type this way: `Boolean.valueOf(event.data.get('isApi'));`


Apex Reference Guide Event Class

##### entityId The ID of any entity associated with the event. For example, the entityId of a DataExport event for an Account object contains the

Account ID.

Signature

```
   public String entityId {get; set;}

```

Property Value

Type: String

##### entityName

The name of the object the event acts on.

Signature

```
   public String entityName {get; set;}

```

Property Value

Type: String

##### organizationId

The ID of the Salesforce org where the event occurred.

Signature

```
   public String organizationId {get; set;}

```

Property Value

Type: String


### Apex Reference Guide EventCondition Interface

##### resourceType

The type of resource for the event. For example, an AccessResource event could have a Connected Application as a resource type. Not
all event types have resources.

Signature

```
   public String resourceType {get; set;}

```

Property Value

Type: String

##### timeStamp

The time the event occurred.

Signature

```
   public Datetime timeStamp {get; set;}

```

Property Value

Type: Datetime

##### userId

Identifies the user that caused the event.

Signature

```
   public String userId {get; set;}

```

Property Value

Type: String

### EventCondition Interface

Allows an implementing class to specify whether to take action when certain events occur based on a transaction security policy. This
interface is only used for Apex policies created in Real-Time Event Monitoring.

Usage

The `evaluate` method is called upon the occurrence of a real-time event monitored by a transaction security policy. A typical
implementation first selects the fields of interest from the event. Then the fields are tested to see if they meet the conditions being
monitored. If the conditions are met, the method returns `true` .

For example, imagine a transaction security policy that triggers when a user queries more than 1,000 lead records. For each API event,
the `evaluate` method checks whether the `RowsProcessed` value is greater than 1,000 and the `QueriedEntities` value
contains “Lead”. If so, `true` is returned.


Apex Reference Guide EventCondition Interface

We recommend having test classes for the policy condition interface to ensure it works correctly. Testing is required regardless of whether
the policy is moved from a sandbox to production, with a change set, or some other way. For example, test your policies in your
development environment before moving the policies to production.

[For more information about testing Apex transaction security policies, read Transaction Security Apex Testing.](https://help.salesforce.com/s/articleView?id=xcloud.enhanced_transaction_security_apex_testing.htm&type=5&language=en_US)

IN THIS SECTION:

#### EventCondition Methods

The EventCondition interface has one method, evaluate(event).

EventCondition Example Implementation
Use EventCondition to create a custom condition for Shield Platform Encryption.

#### EventCondition Methods

The EventCondition interface has one method, evaluate(event).

#### The following are methods for EventCondition .

IN THIS SECTION:

##### evaluate(event)

Evaluates an event against a transaction security policy created in Real-Time Event Monitoring. If the event triggers the policy, the
method returns `true` .

##### evaluate(event)

Evaluates an event against a transaction security policy created in Real-Time Event Monitoring. If the event triggers the policy, the method
returns `true` .

Signature

```
   public Boolean evaluate(SObject event)

```

Parameters

```
   var1
```

Type: SObject

The event to check against the transaction security policy.

Return Value

Type: Boolean

Returns `true` when the policy is triggered. For example, suppose that the policy is to limit users to a single login session. If a user tries
to log in a second time, the policy blocks the attempted login, and updates the Status, PolicyId, and PolicyOutcome fields of that
##### LoginEvent. The policy also sends an email notification to the Salesforce admin. The evaluate method only checks the login event,

and returns `true` if it’s the user’s second login attempt.

##### The system performs the action and notification, not the evaluate method.


### Apex Reference Guide AsyncCondition Interface

#### EventCondition Example Implementation

Use EventCondition to create a custom condition for Shield Platform Encryption.

This example shows an implementation of the `TxnSecurity.EventCondition` interface. The transaction security policy triggers
when the user queries an Account object.

```
   public boolean evaluate(ApiEvent event) {

       switch on event {

         when ApiEvent apiEvent {

           return handleApiEvent(apiEvent);

         }

         when null {

         // Trigger action if event is null

           return true;

         }

         when else {

         // Trigger action for unhandled events

           return true;

         }

       }

     }

     private boolean handleApiEvent(ApiEvent apiEvent){

       if(apiEvent.QueriedEntities.contains('Account')){

         return true;

       }

       return false;

     }

   }

```

[For more examples, see Enhanced Apex Transaction Security Implementation Examples.](https://help.salesforce.com/articleView?id=enhanced_transaction_security_policy_apex_examples.htm&language=en_US)

### AsyncCondition Interface

Allows an implementing class to make asynchronous Apex calls. This interface is used only for transaction security Apex policies created
in Real-Time Event Monitoring.

Namespace

TxnSecurity

Usage

[If you make an Asynchronous Apex call in the class that implements your transaction security policy condition, the class must implement](https://trailhead.salesforce.com/en/content/learn/modules/asynchronous_apex)
the `TxnSecurity.AsyncCondition` interface in addition to `TxnSecurity.EventCondition` . Use Asynchronous Apex
instead of Apex callouts and DML statements, neither of which is allowed in transaction security Apex policies.

Apex offers multiple ways to run your Apex code asynchronously and all are supported in the `TxnSecurity.AsyncCondition`
interface.

This interface has no methods.


### Apex Reference Guide PolicyCondition Interface

IN THIS SECTION:

#### AsyncCondition Example Implementation

SEE ALSO:

_[Apex Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_async_overview.htm)_ Asynchronous Apex

#### AsyncCondition Example Implementation

Here’s an example implementation of the `TxnSecurity.AsyncCondition` interface. The transaction security policy triggers
when a user logs in. In the example, ExternalValidation__c is a custom object that contains information from an external validation
system. The result of the SOQL query on ExternalValidation__c determines whether to block the user from logging in. The policy then
queues the `CalloutToExternalValidator` class for asynchronous execution. When it executes, the
`CalloutToExternalValidator` class makes an external call to the validation system to update it with information about this
log in event. Because `CalloutToExternalValidator` is triggered by Asynchronous Apex, you must implement the
`TxnSecurity.AsyncCondition` interface in the `ExternallyValidatedLoginCondition` Apex class along with
the usual `TxnSecurity.EventCondition` interface.

```
   global class ExternallyValidatedLoginCondition implements TxnSecurity.EventCondition,

   TxnSecurity.AsyncCondition {

      public boolean evaluate(SObject event) {

        LoginEvent loginEvent = (LoginEvent) event;

        Boolean userBlocked = [select blocked from ExternalValidation__c where loginId =

   loginEvent.UserId][0].Blocked;

        System.enqueueJob(new CalloutToExternalValidator(loginEvent.SourceIp,

   loginEvent.LoginUrl));

        return userBlocked;

      }

   }

   public class CalloutToExternalValidator implements Queueable {

      private String sourceIp;

      private String loginUrl;

      public CalloutToExternalValidator(String sourceIp, String loginUrl) {

        this.sourceIp = sourceIp;

        this.loginUrl = loginUrl;

      }

      public void execute(QueueableContext context) {

        // callout to external validation service

        // pass sourceIp, loginUrl

        // update ExternalValidation__c

      }

   }

### PolicyCondition Interface

```

Apex interface that allows an implementing class to specify actions to take when certain events occur based on a transaction security
policy.


Apex Reference Guide PolicyCondition Interface

Namespace

TxnSecurity

Usage

#### Tip: The PolicyCondition interface applies only to Legacy Transaction Security, which is a retired feature as of Summer '20. Use the EventCondition interface instead of the PolicyCondition interface.

##### The evaluate method is called upon the occurrence of an event monitored by a transaction security policy. A typical implementation

first selects the item of interest from the event. Then the item is tested to see if it meets the condition being monitored. If the condition
is met, the method returns `true` .

For example, imagine a transaction security policy that checks for the same user logging in more than once. For each login event, the
method would check if the user logging in already has a login session in progress, and if so, `true` is returned.

We recommend having test classes for the policy condition interface to ensure it works correctly. Testing is required regardless of whether
the policy is moved from a sandbox to production, with a change set, or some other way. For example, test your policies in your
development environment before moving the policies to production.

Don’t include DML statements in your custom policies because they can cause errors. When you send a custom email via Apex during
transaction policy evaluation, you get an error, even if the record isn’t explicitly related to another record. For more information, see
[Apex DML Operations in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_dml_section.htm) _Apex Reference Guide_ .

IN THIS SECTION:

#### PolicyCondition Methods PolicyCondition Methods The following is the method for PolicyCondition .

IN THIS SECTION:

##### evaluate(event)

Evaluates an event against a transaction security policy. If the event triggers the policy, `true` is returned.

##### evaluate(event)

Evaluates an event against a transaction security policy. If the event triggers the policy, `true` is returned.

Signature

```
   public Boolean evaluate(TxnSecurity.Event event)

```

Parameters

```
   event
```

Type: TxnSecurity.Event

The event to check against the transaction security policy.


## Apex Reference Guide UserProvisioning Namespace

Return Value

Type: Boolean

When the policy is triggered, `True` is returned. For example, let’s suppose the policy is to limit users to a single login session. If anyone
tries to log in a second time, the policy’s action requires that they end their current session. The policy also sends an email notification
to the Salesforce admin. The `evaluate()` method only checks the login event, and returns `True` if it’s the user’s second login. The
Transaction Security system performs the action and notification, and not the `evaluate()` method.

## UserProvisioning Namespace The UserProvisioning namespace provides methods for monitoring outbound user provisioning requests. The following is the class in the UserProvisioning namespace.

IN THIS SECTION:

### ConnectorTestUtil Class

Enables developers to write Apex test classes for connectors used by the connected app provisioning solution. This class simulates
provisioning for the associated app.

UserProvisioningLog Class
Provides methods for writing messages to monitor outbound user provisioning requests.

UserProvisioningPlugin Class
The `UserProvisioningPlugin` base class implements `Process.Plugin` for programmatic customization of the user
provisioning process for connected apps.

### ConnectorTestUtil Class

Enables developers to write Apex test classes for connectors used by the connected app provisioning solution. This class simulates
provisioning for the associated app.

Namespace

## UserProvisioning

Usage

Use this class for connector-based test accelerators. You can invoke it only from within an Apex test.

Example

This example creates an instance of a connected app, gets a value, and checks whether the value is correct. The test is simply a row
inserted in the database table.

```
        @isTest

        private class SCIMCreateUserPluginTest {

        public static void callPlugin(Boolean validInputParams) {

```


Apex Reference Guide ConnectorTestUtil Class

```
        //Create an instance of a connected app

        ConnectedApplication capp

   =UserProvisioning.ConnectorTestUtil.createConnectedApp('TestApp');

        Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];

        //Create a user

        User user = new User(username='testuser1@scimuserprov.test', Firstname= 'Test',

   Lastname='User1', email='testuser1@testemail.com',

        FederationIdentifier='testuser1@testemail.com', profileId= p.Id,

   communityNickName='tuser1', alias='tuser', TimeZoneSidKey='GMT',

        LocaleSidKey='en_US', EmailEncodingKey='ISO-8859-1', LanguageLocaleKey='en_US');

        //insert user into a row in the database table

        insert user;

        //Create a UPR

        UserProvisioningRequest upr = new UserProvisioningRequest(appname = capp.name,

   connectedAppId=capp.id, operation='Create',

        state='New', approvalStatus='NotRequired',salesforceUserId=user.id);

        //Insert the UPR to test the flow end to end

        insert upr;

        }}

```

IN THIS SECTION:

#### ConnectorTestUtil Method

SEE ALSO:

_Salesforce Help_ [: User Provisioning for Connected Apps](https://help.salesforce.com/articleView?id=connected_app_user_provisioning.htm&language=en_US)

#### ConnectorTestUtil Method The ConnectorTestUtil class has 1 method.

IN THIS SECTION:

##### createConnectedApp(connectedAppName)

Creates an instance of a connected app to simulate provisioning.

##### createConnectedApp(connectedAppName)

Creates an instance of a connected app to simulate provisioning.

Signature

```
   public static ConnectedApplication createConnectedApp(String connectedAppName)

```

Parameters

```
   connectedAppName
```

Type: String


### Apex Reference Guide UserProvisioningLog Class

Name of the connected app to test for provisioning.

Return Value

Type: ConnectedApplication

The instance of the connected app to test for provisioning.

### UserProvisioningLog Class

Provides methods for writing messages to monitor outbound user provisioning requests.

Namespace

### UserProvisioning

Example

This example writes the user account information sent to a third-party system for a provisioning request to the UserProvisioningLog
object.

```
   String inputParamsStr = 'Input parameters: uprId=' + uprId + ',

   endpointURL=' + endpointURL + ', adminUsername=' + adminUsername + ',

   email=' + email + ', username=' + username + ', defaultPassword=' + defaultPassword + ',

   defaultRoles =' + defaultRoles;

   UserProvisioning.UserProvisioningLog.log(uprId, inputParamsStr);

```

IN THIS SECTION:

#### UserProvisioningLog Methods UserProvisioningLog Methods

### The following are methods for UserProvisioningLog . All methods are static.

IN THIS SECTION:

##### log(userProvisioningRequestId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request.

log(userProvisioningRequestId, status, details)
Writes a specific status and message, such a status and detailed error message, to monitor the progress of a user provisioning request.

log(userProvisioningRequestId, externalUserId, externalUserName, userId, details)
Writes a specific message, such as an error message, to monitor the progress of a user provisioning request associated with a specific
user.

##### log(userProvisioningRequestId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request.


Apex Reference Guide UserProvisioningLog Class

Signature

```
   public void log(String userProvisioningRequestId, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

##### log(userProvisioningRequestId, status, details)

Writes a specific status and message, such a status and detailed error message, to monitor the progress of a user provisioning request.

Signature

```
   public void log(String userProvisioningRequestId, String status, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   status
```

Type: String

A description of the current state. For example, while invoking a third-party API, the status could be `invoke` .

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

##### log(userProvisioningRequestId, externalUserId, externalUserName, userId, details)

Writes a specific message, such as an error message, to monitor the progress of a user provisioning request associated with a specific
user.


### Apex Reference Guide UserProvisioningPlugin Class

Signature

```
   public void log(String userProvisioningRequestId, String externalUserId, String

   externalUserName, String userId, String details)

```

Parameters

```
   userProvisioningRequestId
```

Type: String

A unique identifier for the user provisioning request.

```
   externalUserId
```

Type: String

The unique identifier for the user in the target system.

```
   externalUserName
```

Type: String

The username for the user in the target system.

```
   userId
```

Type: String

Salesforce ID of the user making the request.

```
   details
```

Type: String

The text for the message.

Return Value

Type: void

### UserProvisioningPlugin Class The UserProvisioningPlugin base class implements Process.Plugin for programmatic customization of the user

provisioning process for connected apps.

Namespace

### UserProvisioning

Usage

Extending this class gives you a plug-in that can be used Flow Builder as a legacy Apex action, with the following input and output
parameters.

**Input Parameter Name** **Description**

`userProvisioningRequestId` The unique ID of the request for the plug-in to process.

`userId` The ID of the associated user for the request.


Apex Reference Guide UserProvisioningPlugin Class

**Input Parameter Name** **Description**

```
NamedCredDevName

reconFilter

```

The unique API name for the named credential to use for a request.
The named credential identifies the third-party system and the
third-party authentication settings.

When the named credential is set in the User Provisioning Wizard,
Salesforce stores the value in the

```
UserProvisioningConfig.NamedCredentialId
```

field.

When collecting and analyzing users on a third-party system, the
plug-in uses this filter to limit the scope of the collection.

When the filter is set in the User Provisioning Wizard, Salesforce
stores the value in the
`UserProvisioningConfig.ReconFilter` field.

`reconOffset` When collecting and analyzing users on a third-party system, the
plug-in uses this value as the starting point for the collection.

**Output Parameter Name** **Description**

```
Status

```

The vendor-specific status of the provisioning operation on the
third-party system.

`Details` The vendor-specific message related to the status of the
provisioning operation on the third-party system.

`ExternalUserId` The vendor-specific ID for the associated user on the third-party
system.

`ExternalUsername` The vendor-specific username for the associated user on the
third-party system.

`ExternalEmail` The email address assigned to the user on the third-party system.

`ExternalFirstName` The first name assigned to the user on the third-party system.

`ExternalLastName` The last name assigned to the user on the third-party system.

```
reconState

```

The state of the collecting and analyzing process on the third-party
system. When the value is `complete`, the process is finished and
a subsequent call to the plug-in is no longer needed, nor made.

`nextReconOffset` When collecting and analyzing users on a third-party system, the
process may encounter a transaction limit and have to stop before

finishing. The value specified here initiates a call to the plug-in with
a new quota limit.

If you want to add more custom parameters, use the `buildDescribeCall()` method.


Apex Reference Guide UserProvisioningPlugin Class

Example

The following example uses the `buildDescribeCall()` method to add a new input parameter and a new output parameter.
The example also demonstrates how to bypass the limit of the 10,000 records processed in DML statements in an Apex transaction.

```
   global class SampleConnector extends UserProvisioning.UserProvisioningPlugin {

      // Example of adding more input and output parameters to those defined in the base

   class

      global override Process.PluginDescribeResult buildDescribeCall() {

        Process.PluginDescribeResult describeResult = new Process.PluginDescribeResult();

        describeResult.inputParameters = new

           List<Process.PluginDescribeResult.InputParameter>{

            new Process.PluginDescribeResult.InputParameter('testInputParam',

                 Process.PluginDescribeResult.ParameterType.STRING, false)

           };

        describeResult.outputParameters = new

           List<Process.PluginDescribeResult.OutputParameter>{

            new Process.PluginDescribeResult.OutputParameter('testOutputParam',

                 Process.PluginDescribeResult.ParameterType.STRING)

           };

        return describeResult;

      }

      // Example Plugin that demonstrates how to leverage the

   reconOffset/nextReconOffset/reconState

      // parameters to create more than 10,000 users. (i.e. go beyond the 10,000 DML limit

   per transaction)

      global override Process.PluginResult invoke(Process.PluginRequest request) {

        Map<String,String> result = new Map<String,String>();

        String uprId = (String) request.inputParameters.get('userProvisioningRequestId');

        UserProvisioning.UserProvisioningLog.log(uprId, 'Inserting Log from test Apex

   connector');

        UserProvisioningRequest upr = [SELECT id, operation, connectedAppId, state

               FROM userprovisioningrequest WHERE id = :uprId];

        if (upr.operation.equals('Reconcile')) {

           String reconOffsetStr = (String) request.inputParameters.get('reconOffset');

           Integer reconOffset = 0;

           if (reconOffsetStr != null) {

             reconOffset = Integer.valueOf(reconOffsetStr);

           }

           if (reconOffset > 44999) {

             result.put('reconState', 'Completed');

           }

           Integer i = 0;

           List<UserProvAccountStaging> upasList = new List<UserProvAccountStaging>();

           for (i = 0; i < 5000; i++) {

             UserProvAccountStaging upas = new UserProvAccountStaging();

```


Apex Reference Guide UserProvisioningPlugin Class

```
             upas.Name = i + reconOffset + '';

             upas.ExternalFirstName = upas.Name;

             upas.ExternalEmail = 'externaluser@externalsystem.com';

             upas.LinkState = 'Orphaned';

             upas.Status = 'Active';

             upas.connectedAppId = upr.connectedAppId;

             upasList.add(upas);

           }

           insert upasList;

           result.put('nextReconOffset', reconOffset + 5000 + '');

        }

        return new Process.PluginResult(result);

      }

   }

```

IN THIS SECTION:

#### UserProvisioningPlugin Methods UserProvisioningPlugin Methods The following are methods for UserProvisioningPlugin .

IN THIS SECTION:

##### buildDescribeCall()

Use this method to add more input and output parameters to those defined in the base class.

describe()
Returns a `Process.PluginDescribeResult` object that describes this method call.

getPluginClassName()
Returns the name of the class implementing the plugin.

invoke(request)
Primary method that the system invokes when the class that implements the interface is instantiated.

##### buildDescribeCall()

Use this method to add more input and output parameters to those defined in the base class.

Signature

```
   public Process.PluginDescribeResult buildDescribeCall()

```

Return Value

Type: Process.PluginDescribeResult


## Apex Reference Guide VisualEditor Namespace

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

Signature

```
   public Process.PluginDescribeResult describe()

```

Return Value

Type: Process.PluginDescribeResult

##### getPluginClassName()

Returns the name of the class implementing the plugin.

Signature

```
   public String getPluginClassName()

```

Return Value

Type: String

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

Type: Process.PluginDescribeResult

## VisualEditor Namespace The VisualEditor namespace provides classes and methods for interacting with the Lightning App Builder. The classes and

methods in this namespace operate on Lightning components, which include Lightning web components and Aura components.

As of Spring ’19 (API version 45.0), you can build Lightning components using two programming models: the Lightning Web Components
model, and the original Aura Components model. Lightning web components are custom HTML elements built using HTML and modern
JavaScript. Lightning web components and Aura components can coexist and interoperate on a page.


### Apex Reference Guide DataRow Class

Configure Lightning web components and Aura components to work in Lightning App Builder and Experience Builder. Admins and end
users don’t know which programming model was used to develop the components. To them, they’re simply Lightning components.

The following are the classes in the `VisualEditor` namespace.

IN THIS SECTION:

### DataRow Class

Contains information about one item in a picklist used in a Lightning component on a Lightning page.

DesignTimePageContext Class
A class that provides context information about a Lightning page. It can be used to help define the values of a picklist in a Lightning
component on a Lightning page based on the page’s type and the object with which it’s associated.

DynamicPickList Class
An abstract class, used to display the values of a picklist in a Lightning component on a Lightning page.

DynamicPickListRows Class
Contains a list of picklist items in a Lightning component on a Lightning page.

### DataRow Class

Contains information about one item in a picklist used in a Lightning component on a Lightning page.

Namespace

VisualEditor

IN THIS SECTION:

#### DataRow Constructors

DataRow Methods

#### DataRow Constructors

### The following are constructors for DataRow .

IN THIS SECTION:

##### DataRow(label, value, selected)

Creates an instance of the `VisualEditor.DataRow` class using the specified label, value, and selected option.

DataRow(label, value)
Creates an instance of the `VisualEditor.DataRow` class using the specified label and value.

##### DataRow(label, value, selected)

Creates an instance of the `VisualEditor.DataRow` class using the specified label, value, and selected option.

Signature

```
   public DataRow(String label, Object value, Boolean selected)

```


Apex Reference Guide DataRow Class

Parameters

```
   label
```

Type: String

User-facing label for the picklist item.

```
   value
```

Type: Object

The value of the picklist item.

```
   selected
```

Type: Boolean

Specifies whether the picklist item is selected ( `true` ) or not ( `false` ).

##### DataRow(label, value)

Creates an instance of the `VisualEditor.DataRow` class using the specified label and value.

Signature

```
   public DataRow(String label, Object value)

```

Parameters

```
   label
```

Type: String

User-facing label for the picklist item.

```
   value
```

Type: Object

The value of the picklist item.

#### DataRow Methods

##### The following are methods for DataRow .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `VisualEditor.DataRow` object.

compareTo(o)
Compares the current `VisualEditor.DataRow` object to the specified one. Returns an integer value that is the result of the
comparison.

getLabel()
Returns the user-facing label of the picklist item.

getValue()
Returns the value of the picklist item.

isSelected()
Returns the state of the picklist item, indicating whether it’s selected or not.


Apex Reference Guide DataRow Class

##### clone()

Makes a duplicate copy of the `VisualEditor.DataRow` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### compareTo(o)

Compares the current `VisualEditor.DataRow` object to the specified one. Returns an integer value that is the result of the
comparison.

Signature

```
   public Integer compareTo(VisualEditor.DataRow o)

```

Parameters

```
   o
```

Type: VisualEditor.DataRow

A single item in a picklist.

Return Value

Type: Integer

Returns one of the following values:

**•** Zero if the current package version is equal to the specified package version

**•** An integer value greater than zero if the current package version is greater than the specified package version

**•** An integer value less than zero if the current package version is less than the specified package version

##### getLabel()

Returns the user-facing label of the picklist item.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of the picklist item.


### Apex Reference Guide DesignTimePageContext Class

Signature

```
   public Object getValue()

```

Return Value

Type: Object

##### isSelected()

Returns the state of the picklist item, indicating whether it’s selected or not.

Signature

```
   public Boolean isSelected()

```

Return Value

Type: Boolean

### DesignTimePageContext Class

A class that provides context information about a Lightning page. It can be used to help define the values of a picklist in a Lightning
component on a Lightning page based on the page’s type and the object with which it’s associated.

Namespace

VisualEditor

Usage

To use this class, create a parameterized constructor in the custom Apex class that extends `VisualEditor.DynamicPickList` .

Example

Here’s an example of a custom Apex class extending the `VisualEditor.DynamicPickList` class. It includes
`VisualEditor.DesignTimePageContext` to define a picklist value that is available only if the page type is `HomePage` .

```
   global class MyCustomPickList extends VisualEditor.DynamicPickList{

      VisualEditor.DesignTimePageContext context;

      global MyCustomPickList(VisualEditor.DesignTimePageContext context) {

        this.context = context;

      }

      global override VisualEditor.DataRow getDefaultValue(){

        VisualEditor.DataRow defaultValue = new VisualEditor.DataRow('red', 'RED');

        return defaultValue;

      }

      global override VisualEditor.DynamicPickListRows getValues() {

        VisualEditor.DataRow value1 = new VisualEditor.DataRow('red', 'RED');

```


Apex Reference Guide DesignTimePageContext Class

```
        VisualEditor.DataRow value2 = new VisualEditor.DataRow('yellow', 'YELLOW');

       VisualEditor.DynamicPickListRows myValues = new VisualEditor.DynamicPickListRows();

        myValues.addRow(value1);

        myValues.addRow(value2);

        if (context.pageType == 'HomePage') {

           VisualEditor.DataRow value3 = new VisualEditor.DataRow('purple', 'PURPLE');

           myValues.addRow(value3);

        }

        return myValues;

      }

   }

```

IN THIS SECTION:

#### DesignTimePageContext Properties

DesignTimePageContext Methods

#### DesignTimePageContext Properties The following are properties for DesignTimePageContext .

IN THIS SECTION:

##### entityName The API name of the sObject that a Lightning page is associated with, such as Account, Contact, or Custom_object__c. entityName

is available only for object pages, and not all Lightning pages are associated with objects.

##### pageType

The type of Lightning page, such as `HomePage`, `AppPage`, or `RecordPage` .

##### **`entityName`** The API name of the sObject that a Lightning page is associated with, such as Account, Contact, or Custom_object__c. entityName

is available only for object pages, and not all Lightning pages are associated with objects.

Signature

```
   public String entityName {get; set;}

```

Property Value

Type: String

##### pageType

The type of Lightning page, such as `HomePage`, `AppPage`, or `RecordPage` .


### Apex Reference Guide DynamicPickList Class

Signature

```
   public String pageType {get; set;}

```

Property Value

Type: String

#### DesignTimePageContext Methods The following are methods for DesignTimePageContext .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `VisualEditor.DesignTimePageContext` object.

##### clone()

Makes a duplicate copy of the `VisualEditor.DesignTimePageContext` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DynamicPickList Class

An abstract class, used to display the values of a picklist in a Lightning component on a Lightning page.

Namespace

VisualEditor

Usage

To use this class as the datasource of a picklist in a Lightning component, it must be extended by a custom Apex class and then that
class must be called in the component’s design file.

Example

Here’s an example of a custom Apex class extending the `VisualEditor.DynamicPickList` class.

```
   global class MyCustomPickList extends VisualEditor.DynamicPickList{

      global override VisualEditor.DataRow getDefaultValue(){

        VisualEditor.DataRow defaultValue = new VisualEditor.DataRow('red', 'RED');

```


Apex Reference Guide DynamicPickList Class

```
        return defaultValue;

      }

      global override VisualEditor.DynamicPickListRows getValues() {

        VisualEditor.DataRow value1 = new VisualEditor.DataRow('red', 'RED');

        VisualEditor.DataRow value2 = new VisualEditor.DataRow('yellow', 'YELLOW');

       VisualEditor.DynamicPickListRows myValues = new VisualEditor.DynamicPickListRows();

        myValues.addRow(value1);

        myValues.addRow(value2);

        return myValues;

      }

   }

```

Here’s an example of how the custom Apex class gets called in a design file so that the picklist appears in the Lightning component.

```
   <design:component>

        <design:attribute name="property1" datasource="apex://MyCustomPickList"/>

   </design:component>

```

IN THIS SECTION:

#### DynamicPickList Methods DynamicPickList Methods The following are methods for DynamicPickList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPicklist` object.

getDefaultValue()
Returns the picklist item that is set as the default value for the picklist.

getLabel(attributeValue)
Returns the user-facing label for a specified picklist value.

getValues()
Returns the list of picklist item values.

isValid(attributeValue)
Returns the valid state of the picklist item’s value. A picklist value is considered valid if it’s a part of any `VisualEditor.DataRow`
in the `VisualEditor.DynamicPickListRows` returned by `getValues()` .

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPicklist` object.

Signature

```
   public Object clone()

```


Apex Reference Guide DynamicPickList Class

Return Value

Type: Object

##### getDefaultValue()

Returns the picklist item that is set as the default value for the picklist.

Signature

```
   public VisualEditor.DataRow getDefaultValue()

```

Return Value

Type: VisualEditor.DataRow

##### getLabel(attributeValue)

Returns the user-facing label for a specified picklist value.

Signature

```
   public String getLabel(Object attributeValue)

```

Parameters

```
   attributeValue
```

Type: Object

The value of the picklist item.

Return Value

Type: String

##### getValues()

Returns the list of picklist item values.

Signature

```
   public VisualEditor.DynamicPickListRows getValues()

```

Return Value

Type: VisualEditor.DynamicPickListRows

##### isValid(attributeValue)

Returns the valid state of the picklist item’s value. A picklist value is considered valid if it’s a part of any `VisualEditor.DataRow`
##### in the VisualEditor.DynamicPickListRows returned by getValues() .


### Apex Reference Guide DynamicPickListRows Class

Signature

```
   public Boolean isValid(Object attributeValue)

```

Parameters

```
   attributeValue
```

Type: Object

The value of the picklist item.

Return Value

Type: Boolean

### DynamicPickListRows Class

Contains a list of picklist items in a Lightning component on a Lightning page.

Namespace

VisualEditor

IN THIS SECTION:

#### DynamicPickListRows Constructors

DynamicPickListRows Methods

#### DynamicPickListRows Constructors

### The following are constructors for DynamicPickListRows .

IN THIS SECTION:

##### DynamicPickListRows(rows, containsAllRows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameters.

DynamicPickListRows(rows)
Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameter.

DynamicPickListRows()
Creates an instance of the `VisualEditor.DynamicPickListRows` class. You can then add rows by using the class’s
`addRow` or `addAllRows` methods.

##### DynamicPickListRows(rows, containsAllRows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameters.

Signature

```
   public DynamicPickListRows(List<VisualEditor.DataRow> rows, Boolean containsAllRows)

```


Apex Reference Guide DynamicPickListRows Class

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist items.

```
   containsAllRows
```

Type: Boolean

Indicates if all values of the picklist are included in a type-ahead search query (true) or only those values initially displayed when the
list is clicked on (false).

A picklist in a Lightning component can display only the first 200 values of a list. If _`containsAllRows`_ is set to false, when a
user does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed,
not the complete set of picklist values.

##### DynamicPickListRows(rows)

Creates an instance of the `VisualEditor.DynamicPickListRows` class using the specified parameter.

Signature

```
   public DynamicPickListRows(List<VisualEditor.DataRow> rows)

```

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist rows.

##### DynamicPickListRows()

Creates an instance of the `VisualEditor.DynamicPickListRows` class. You can then add rows by using the class’s `addRow`
or `addAllRows` methods.

Signature

```
   public DynamicPickListRows()

#### DynamicPickListRows Methods

##### The following are methods for DynamicPickListRows .

```

IN THIS SECTION:

addAllRows(rows)
Adds a list of picklist items to a dynamic picklist rendered in a Lightning component on a Lightning page.

addRow(row)
Adds a single picklist item to a dynamic picklist rendered in a Lightning component on a Lightning page.

clone()
Makes a duplicate copy of the `VisualEditor.DynamicPickListRows` object.


Apex Reference Guide DynamicPickListRows Class

containsAllRows()
Returns a Boolean value indicating whether all values of the picklist are included when a user does a type-ahead search query (true)
or only those values initially displayed when the list is clicked on (false).

get(i)
Returns a picklist element stored at the specified index.

getDataRows()
Returns a list of picklist items.

setContainsAllRows(containsAllRows)
Sets the value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or only
those values initially displayed when the list is clicked on (false).

size()
Returns the size of the list of `VisualEditor.DynamicPickListRows` .

sort()
Sorts the list of `VisualEditor.DynamicPickListRows` .

##### addAllRows(rows)

Adds a list of picklist items to a dynamic picklist rendered in a Lightning component on a Lightning page.

Signature

```
   public void addAllRows(List<VisualEditor.DataRow> rows)

```

Parameters

```
   rows
```

Type: List VisualEditor.DataRow

List of picklist items.

Return Value

Type: void

##### addRow(row)

Adds a single picklist item to a dynamic picklist rendered in a Lightning component on a Lightning page.

Signature

```
   public void addRow(VisualEditor.DataRow row)

```

Parameters

```
   row
```

Type: VisualEditor.DataRow

A single picklist item.


Apex Reference Guide DynamicPickListRows Class

Return Value

Type: void

##### clone()

Makes a duplicate copy of the `VisualEditor.DynamicPickListRows` object.

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### containsAllRows()

Returns a Boolean value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or
only those values initially displayed when the list is clicked on (false).

Signature

```
   public Boolean containsAllRows()

```

Return Value

Type: Boolean

##### A picklist in a Lightning component can display only the first 200 values of a list. If containsAllRows is set to false, when a user

does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed, not the
complete set of picklist values.

##### get(i)

Returns a picklist element stored at the specified index.

Signature

```
   public VisualEditor.DataRow get(Integer i)

```

Parameters

```
   i
```

Type: Integer

The index.

Return Value

Type: VisualEditor.DataRow


Apex Reference Guide DynamicPickListRows Class

##### getDataRows()

Returns a list of picklist items.

Signature

```
   public List<VisualEditor.DataRow> getDataRows()

```

Return Value

Type: List VisualEditor.DataRow

##### setContainsAllRows(containsAllRows)

Sets the value indicating whether all values of the picklist are included when a user does a type-ahead search query (true) or only those
values initially displayed when the list is clicked on (false).

Signature

```
   public void setContainsAllRows(Boolean containsAllRows)

```

Parameters

```
   containsAllRows
```

Type: Boolean

Indicates if all values of the picklist are included in a type-ahead search query (true) or only those values initially displayed when the
list is clicked on (false).

A picklist in a Lightning component can display only the first 200 values of a list. If _`containsAllRows`_ is set to false, when a
user does a type-ahead search to find values in the picklist, the search will only look at those first 200 values that were displayed,
not the complete set of picklist values.

Return Value

Type: void

##### size()

Returns the size of the list of `VisualEditor.DynamicPickListRows` .

Signature

```
   public Integer size()

```

Return Value

Type: Integer

##### sort()

Sorts the list of `VisualEditor.DynamicPickListRows` .


## Apex Reference Guide Wave Namespace Namespace

Signature

```
   public void sort()

```

Return Value

Type: void

## Wave Namespace Namespace The classes in the Wave namespace are part of the CRM Analytics Analytics SDK, designed to facilitate querying CRM Analytics data

from Apex code.

## The following are the classes in the Wave namespace.

IN THIS SECTION:

### QueryBuilder Class

The QueryBuilder class provides methods for constructing well-formed SAQL queries to pass to CRM Analytics.

QueryNode Class
Define each node of the query - such as projection, groups, order, filters. Execute the query.

ProjectionNode Class
Add aggregate functions to the query, or define an alias.

Templates Class
The Templates class provides methods for retrieving CRM Analytics template collections, individual templates, and template
configurations.

TemplatesSearchOptions Class
The TemplatesSearchOptions class provides optional properties to filter the template collection.

### QueryBuilder Class

The QueryBuilder class provides methods for constructing well-formed SAQL queries to pass to CRM Analytics.

Namespace

wave

Usage

Use QueryBuilder and its associated classes, `Wave.ProjectionNode` and `Wave.QueryNode`, to incrementally build your SAQL
statement. For example:

```
   public static void executeApexQuery(String name){

     Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{

      Wave.QueryBuilder.get('State').alias('State'),

      Wave.QueryBuilder.get('City').alias('City'),

      Wave.QueryBuilder.get('Revenue').avg().alias('avg_Revenue'),

      Wave.QueryBuilder.get('Revenue').sum().alias('sum_Revenue'),

```


Apex Reference Guide QueryBuilder Class

```
      Wave.QueryBuilder.count().alias('count')};

     ConnectApi.LiteralJson result = Wave.QueryBuilder.load('0FbD00000004DSzKAM',

   '0FcD00000004FEZKA2')

      .group(new String[]{'State', 'City'})

      .foreach(projs)

      .execute('q');

     String response = result.json;

   }

```

Examples

QueryBuilder is the core of this first phase of the CRM Analytics Apex SDK, so let’s take a closer look. Here’s a simple count query.

```
   Wave.ProjectionNode[] projs = new

   Wave.ProjectionNode[]{Wave.QueryBuilder.count().alias('c')};

   String query = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group().foreach(projs).build('q');

```

The resulting SAQL query looks like this:

```
   q = load "datasetId/datasetVersionId";

   q = group q by all;

   q = foreach q generate count as c;

```

Here’s a more complex example that uses a union statement.

```
   Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{Wave.QueryBuilder.get('Name'),

   Wave.QueryBuilder.get('AnnualRevenue').alias('Revenue')};

   Wave.QueryNode nodeOne =

   Wave.QueryBuilder.load('datasetOne','datasetVersionOne').foreach(projs);

   Wave.QueryNode nodeTwo = Wave.QueryBuilder.load('datasetTwo',

   'datasetVersionTwo').foreach(projs);

   String query = Wave.QueryBuilder.union(new List<Wave.QueryNode>{nodeOne,

   nodeTwo}).build('q');

```

The resulting SAQL query has two projection streams, _`qa`_ and _`qb`_ .

```
   qa = load "datasetOne/datasetVersionOne";

   qa = foreach q generate Name,AnnualRevenue as Revenue;

   qb = load "datasetTwo/datasetVersionTwo";

   qb = foreach q generate Name,AnnualRevenue as Revenue;

   q = union qa, qb;

```

IN THIS SECTION:

#### QueryBuilder Methods QueryBuilder Methods The following are methods for QueryBuilder .


Apex Reference Guide QueryBuilder Class

IN THIS SECTION:

##### load(datasetID, datasetVersionID)

Load a stream from a dataset.

##### count()

Calculate the number of rows that match the query criteria.

get(projection)
Query by selecting specific attributes.

union(unionNodes)
Combine multiple result sets into one result set.

cogroup(cogroupNodes, groups)
Cogrouping means that two input streams are grouped independently and arranged side by side. Only data that exists in both
groups appears in the results.

##### load(datasetID, datasetVersionID)

Load a stream from a dataset.

Signature

```
   public static wave.QueryNode load(String datasetID, String datasetVersionID)

```

Parameters

```
   datasetID
```

Type: String

The ID of the dataset.

```
   datasetVersionID
```

Type: String

The ID identifying the version of the dataset.

Return Value

Type: wave.QueryNode

##### count()

Calculate the number of rows that match the query criteria.

Signature

```
   public static wave.ProjectionNode count()

```

Return Value

Type: wave.ProjectionNode


Apex Reference Guide QueryBuilder Class

##### get(projection)

Query by selecting specific attributes.

Signature

```
   public static wave.ProjectionNode get(String proj)

```

Parameters

```
   proj
```

Type: String

The name of the column to query.

Return Value

Type: wave.ProjectionNode

##### union(unionNodes)

Combine multiple result sets into one result set.

Signature

```
   global static Wave.QueryNode union(List<Wave.QueryNode> unionNodes)

```

Parameters

```
   unionNodes
```

Type: List<wave.QueryNode>

List of nodes to combine.

Return Value

Type: wave.QueryNode

##### cogroup(cogroupNodes, groups)

Cogrouping means that two input streams are grouped independently and arranged side by side. Only data that exists in both groups
appears in the results.

Signature

```
   global static Wave.QueryNode cogroup(List<Wave.QueryNode> cogroupNodes,

   List<List<String>> groups)

```

Parameters

```
   cogroupNodes
```

Type: wave.QueryNode


### Apex Reference Guide QueryNode Class

List of nodes to group.

```
   groups
```

Type: String

The type of grouping.

Return Value

Type: wave.QueryNode

### QueryNode Class

Define each node of the query - such as projection, groups, order, filters. Execute the query.

Namespace

wave

Usage

Refer to the QueryBuilder example.

IN THIS SECTION:

#### QueryNode Methods QueryNode Methods

### The following are methods for QueryNode .

IN THIS SECTION:

build(streamName)
Build the query string represented by this QueryNode and assign it to a stream name.

foreach(projections)
Applies a set of expressions to every row in a dataset. This action is often referred to as projection.

group(groups)
Groups matched records (group by specific dataset attributes).

group()
Groups matched records (group by all).

order(orders)
Sorts in ascending or descending order on one or more fields.

cap(cap)
Limits the number of results that are returned.

filter(filterCondition)
Selects rows from a dataset based on a filter condition (a predicate).


Apex Reference Guide QueryNode Class

filter(filterConditions)
Selects rows from a dataset based on multiple filter conditions (predicates).

execute(streamName)
Execute the query and return rows as JSON.

##### build(streamName)

Build the query string represented by this QueryNode and assign it to a stream name.

Signature

```
   public String build(String streamName)

```

Parameters

```
   streamName
```

Type: String

The identifier for the stream - for example, “q”.

Return Value

Type: String

The SAQL query string represented by the QueryNode.

##### foreach(projections)

Applies a set of expressions to every row in a dataset. This action is often referred to as projection.

Signature

```
   public wave.QueryNode foreach(List<wave.ProjectionNode> projections)

```

Parameters

```
   projections
```

Type: List<wave.ProjectionNode>

A list of ProjectionNodes to be added to this QueryNode.

Return Value

Type: wave.QueryNode

##### group(groups)

Groups matched records (group by specific dataset attributes).

Signature

```
   public wave.QueryNode group(List<String> groups)

```


Apex Reference Guide QueryNode Class

Parameters

```
   groups
```

Type: List<String>

A list of expressions.

Return Value

Type: wave.QueryNode

Example

```
   Wave.ProjectionNode[] projs = new Wave.ProjectionNode[]{Wave.QueryBuilder.get('Name'),

   Wave.QueryBuilder.get('Revenue').sum().alias('REVENUE_SUM')};

   ConnectApi.LiteralJson result = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group(new String[]{'Name'}).foreach(projs).build('q');

##### group()

```

Groups matched records (group by all).

Signature

```
   public wave.QueryNode group()

```

Return Value

Type: wave.QueryNode

Example

```
   String query = Wave.QueryBuilder.load('datasetId',

   'datasetVersionId').group().foreach(projs).build('q');

##### order(orders)

```

Sorts in ascending or descending order on one or more fields.

Signature

```
   public wave.QueryNode group(List<String> groups)

```

Parameters

```
   groups
```

Type: List<String>

A list of column names and associated ascending or descending keywords, for example

```
     List<List<String>>{new List<String>{'Name', 'asc'}, new List<String>{'Revenue', 'desc'}}

```


Apex Reference Guide QueryNode Class

Return Value

Type: wave.QueryNode

##### cap(cap)

Limits the number of results that are returned.

Signature

```
   global Wave.QueryNode cap(Integer cap)

```

Parameters

##### _`cap`_

Type: Integer

The maximum number of rows to return.

Return Value

Type: wave.QueryNode

##### filter(filterCondition)

Selects rows from a dataset based on a filter condition (a predicate).

Signature

```
   public wave.QueryNode filter(String filterCondition)

```

Parameters

```
   filterCondition
```

Type: String

For example: `filter('Name != \'My Name\'')`

Return Value

Type: wave.QueryNode

##### filter(filterConditions)

Selects rows from a dataset based on multiple filter conditions (predicates).

Signature

```
   public wave.QueryNode filter(List<String> filterCondition)

```


### Apex Reference Guide ProjectionNode Class

Parameters

```
   filterCondition
```

Type: List<String>

A list of filter conditions.

Return Value

Type: wave.QueryNode

##### execute(streamName)

Execute the query and return rows as JSON.

Signature

```
   global ConnectApi.LiteralJson execute(String streamName)

```

Parameters

```
   streamName
```

Type: String

The query stream to execute. For example:

```
     ConnectApi.LiteralJson result = Wave.QueryBuilder.load('datasetId',

         'datasetVersionId').group().foreach(projs).execute('q');

```

Return Value

Type: ConnectApi.LiteralJson

### ProjectionNode Class

Add aggregate functions to the query, or define an alias.

Namespace

wave on page 4358

Usage

Refer to the QueryBuilder example.

IN THIS SECTION:

#### ProjectionNode Methods ProjectionNode Methods

### The following are methods for ProjectionNode .


Apex Reference Guide ProjectionNode Class

IN THIS SECTION:

##### sum()

Returns the sum of a numeric field.

##### avg()

Returns the average value of a numeric field.

##### min()

Returns the minimum value of a field.

max()
Returns the maximum value of a field.

count()
Returns the number of rows that match the query criteria.

unique()
Returns the count of unique values.

alias(name)
Define output column names.

##### sum()

Returns the sum of a numeric field.

Signature

```
   public wave.ProjectionNode sum()

```

Return Value

Type: wave.ProjectionNode

##### avg()

Returns the average value of a numeric field.

Signature

```
   public wave.ProjectionNode avg()

```

Return Value

Type: wave.ProjectionNode

##### min()

Returns the minimum value of a field.

Signature

```
   public wave.ProjectionNode min()

```


Apex Reference Guide ProjectionNode Class

Return Value

Type: wave.ProjectionNode

##### max()

Returns the maximum value of a field.

Signature

```
   public wave.ProjectionNode max()

```

Return Value

Type: wave.ProjectionNode

##### count()

Returns the number of rows that match the query criteria.

Signature

```
   public wave.ProjectionNode count()

```

Return Value

Type: wave.ProjectionNode

##### unique()

Returns the count of unique values.

Signature

```
   public wave.ProjectionNode unique()

```

Return Value

Type: wave.ProjectionNode

##### alias(name)

Define output column names.

Signature

```
   public wave.ProjectionNode alias(String name)

```


### Apex Reference Guide Templates Class

Parameters

```
   name
```

Type: String

The name to use for this column. For example, this code defines the alias `c` :

```
     Wave.ProjectionNode[] projs = new

     Wave.ProjectionNode[]{Wave.QueryBuilder.count().alias('c')};

```

Return Value

Type: wave.ProjectionNode

### Templates Class

The Templates class provides methods for retrieving CRM Analytics template collections, individual templates, and template configurations.

Namespace

Wave

Usage

Use Templates and its associated class `Wave.TemplatesSearchOptions` to get CRM Analytics template information.

Examples

This code sample declares a method that returns a list of the template names.

```
   @AuraEnabled(cacheable=true)

   public static void List<String> getTemplateNames() {

     Map<String, Object> o = Wave.Templates.getTemplates(new Wave.TemplatesSearchOptions());

     List<Object> templates = (List<Object>) o.get('templates');

     List<String> names = new List<String>();

     for (Object templateObj : templates) {

      names.add((String) ((Map<String, Object>) templateObj.get('name'));

     }

     return names;

   }

```

Adding the `@AuraEnabled` annotation allows Lightning Web Components to access Templates methods directly.

For example, in the lwc.js file:

```
   import getTemplates from '@salesforce/apex/Wave.Templates.getTemplates';

   export default class Templates extends LightningElement {

     @wire(getTemplates, {

      // specifying 'options' is optional

      options: {

       // values in TemplatesSearchOptions go here; all optional

       type: 'app'

      }

```


Apex Reference Guide Templates Class

```
     })

     onTemplates({ data, error }) {

      if (data) {

       console.log('template names=' + data.templates.map(l => l.name).join(', '));

      }

     }

   }

```

IN THIS SECTION:

#### Templates Methods Templates Methods The following are methods for Templates .

IN THIS SECTION:

##### getTemplate(templateIdOrApiName)

Gets a CRM Analytics template by the specified ID or API name. The returned template is a map of the template JSON attributes as
name/value pairs.

getTemplateConfig(templateIdOrApiName)
Gets the CRM Analytics template configuration by the specified ID or API name. The returned template configuration is a map of the
JSON attributes as name/value pairs.

getTemplates(options)
Get a filtered collection of CRM Analytics templates using search options.

getTemplates()
Gets all CRM Analytics templates.

##### **`getTemplate(templateIdOrApiName)`**

Gets a CRM Analytics template by the specified ID or API name. The returned template is a map of the template JSON attributes as
name/value pairs.

Signature

```
   public static Map<String,Object> getTemplate(String templateIdOrApiName)

```

Parameters

```
   templateIdOrApiName
```

Type: String

The template ID or API name of the template to retrieve.

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm)


Apex Reference Guide Templates Class

A map of the template JSON attribute name/value pairs, where the name is a string with an object value. For attributes details, see
[TemplateRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates_id.htm)

Example

```
   String templateName = (String) Wave.Templates.getTemplate( templateId ).get('name');

##### **`getTemplateConfig(templateIdOrApiName)`**

```

Gets the CRM Analytics template configuration by the specified ID or API name. The returned template configuration is a map of the
JSON attributes as name/value pairs.

Signature

```
   public static Map<String,Object> getTemplateConfig(String templateIdOrApiName)

```

Parameters

```
   templateIdOrApiName
```

Type: String

The template ID or developer name to retrieve the template configuration for.

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

A map of template configuration JSON attribute names and the object values. For attribute details, see
[TemplateConfigurationRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates_configuration.htm)

Example

```
   Map<String, Object> templateVariables = (Map<String, Object>)

   Wave.Templates.getTemplateConfig( templateId ).get('variables');

##### **`getTemplates(options)`**

```

Get a filtered collection of CRM Analytics templates using search options.

Signature

```
   public static Map<String,Object> getTemplates(Wave.TemplatesSearchOptions options)

```

Parameters

```
   options
```

Type: Wave.TemplatesSearchOptions on page 4372

The search options to use for filtering the template collection.


### Apex Reference Guide TemplatesSearchOptions Class

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

[A map of template names and the template object values. For template collection details, see TemplateCollectionRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates.htm)

Example

```
   Map<String,Object> templatesMap = Wave.Templates.getTemplates(new

   Wave.TemplatesSearchOptions());

##### **`getTemplates()`**

```

Gets all CRM Analytics templates.

Signature

```
   public static Map<String,Object> getTemplates()

```

Return Value

[Type: Map<String,Object>](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

[A map of template names and the template object values. For template collection details, see TemplateCollectionRepresentation.](https://developer.salesforce.com/docs/atlas.en-us.260.0.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_resources_templates.htm)

Example

```
   Map<String,Object> templatesMap = Wave.Templates.getTemplates();

### TemplatesSearchOptions Class

```

The TemplatesSearchOptions class provides optional properties to filter the template collection.

Namespace

Wave

Usage

Use TemplatesSearchOptions with `Wave.Templates` class to filter the CRM Analytics template collection returned. For example:

```
   public static void List<String> getAppTemplates() {

     Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

     tsOptions.type = 'app';

     Map<String, Object> o = Wave.Templates.getTemplates(tsOptions);

     List<Object> appTemplates = (List<Object>) o.get('templates');

     List<String> names = new List<String>();

     for (Object templateObj : appTemplates) {

      names.add((String) ((Map<String, Object>) templateObj.get('name'));

     }

```


Apex Reference Guide TemplatesSearchOptions Class

```
     return names;

   }

```

IN THIS SECTION:

#### TemplatesSearchOptions Properties TemplatesSearchOptions Properties The following are properties for TemplatesSearchOptions .

IN THIS SECTION:

##### filterGroup

Specifies the Connect API filter group for CRM Analytics template search options.

##### options

Specifies the template visibility option to filter the CRM Analytics template collection by.

type
Sets the template type to filter the CRM Analytics template collection by.

##### **`filterGroup`**

Specifies the Connect API filter group for CRM Analytics template search options.

Signature

```
   public String filterGroup {get; set;}

```

Property Value

Type: String

[Uses the ConnectFilterGroupEnum values.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/intro_filter_groups.htm)

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.filterGroup = 'small';

##### **`options`**

```

Specifies the template visibility option to filter the CRM Analytics template collection by.

Signature

```
   public String options {get; set;}

```


## Apex Reference Guide Appendices

Property Value

Type: String

Uses the `ConnectWaveTemplateVisibilityOptionsEnum` values. Valid values are `CreateApp`, `ViewOnly`, and
`ManageableOnly` .

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.options = 'ViewOnly';

##### **`type`**

```

Sets the template type to filter the CRM Analytics template collection by.

Signature

```
   public String type {get; set;}

```

Property Value

Type: String

Uses the `ConnectWaveTemplateTypeEnum` values. Valid values are `app`, `dashboard`, `embedded`, and `lens` .

Example

```
   Wave.TemplateSearchOptions tsOptions = new Wave.TemplatesSearchOptions();

   tsOptions.type = 'app';

## Appendices

```

IN THIS SECTION:

### Shipping Invoice Example

Reserved Keywords
These words can be used only as keywords.

Documentation Typographical Conventions
Apex and Visualforce documentation uses these typographical conventions.

### Shipping Invoice Example

This appendix provides an example of an Apex application. This is a more complex example than the Hello World example.

**•** Shipping Invoice Walk-Through

### • Shipping Invoice Example Code


#### Apex Reference Guide Shipping Invoice Example

IN THIS SECTION:

#### 1. Shipping Invoice Example Walk-Through

2. Shipping Invoice Example Code

#### Shipping Invoice Example Walk-Through

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


Apex Reference Guide Shipping Invoice Example

**Name** **Type** **Description**

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

**Flow of user action and triggers for the shopping cart application**

**1.** User clicks **Orders**    - **New**, names the shipping invoice and clicks **Save** .


#### Apex Reference Guide Shipping Invoice Example

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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
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

```


Apex Reference Guide Shipping Invoice Example

```
                 'Order tax was not $9.25, but was ' + order1.tax__c);

        System.assert(order1.shipping__c == 19.50,

                 'Order shipping was not $19.50, but was '

                 + order1.shipping__c);

        System.assert(order1.totalweight__c == 26.00,

                 'Order weight was not 26 but was ' + order1.totalweight__c);

        System.assert(order1.grandtotal__c == 109.25,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == -19.50,

                 'Order shipping discount was not -$19.50 but was '

                 + order1.shippingdiscount__c);

      }

      // Negative testing for inserting bad input

      public static testmethod void testNegativeTests(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

        insert Order1;

        Item__c item1 = new Item__C(Price__c = -10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = -2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = -1,

                         Shipping_Invoice__C = order1.id);

        Item__c item4 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 0,

                         Shipping_Invoice__C = order1.id);

        try{

           insert item1;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Price must be non-negative'),

                  'Price was negative but was not caught');

        }

        try{

           insert item2;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Weight must be non-negative'),

                  'Weight was negative but was not caught');

        }

        try{

```


### Apex Reference Guide Reserved Keywords

```
           insert item3;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was negative but was not caught');

        }

        try{

           insert item4;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was zero but was not caught');

        }

      }

   }

### Reserved Keywords

```

These words can be used only as keywords.

**Table 3: Reserved Keywords**

abstract false package

activate final parallel

and finally pragma

any float private

array for protected

as from public

asc global retrieve

autonomous goto return

begin group rollback

bigdecimal having select

blob hint set

boolean if short

break implements sObject

bulk import sort

by in static

byte inner string

case insert super

cast instanceof switch

catch int synchronized


### Apex Reference Guide Documentation Typographical Conventions

char integer system

class interface testmethod

collect into then

commit join this

const like throw

continue limit time

currency list transaction

date long trigger

datetime loop true

decimal map try

default merge undelete

delete new update

desc not upsert

do null using

double nulls virtual

else number void

end object webservice

enum of when

exception on where

exit or while

export outer

extends override

These words are special types of keywords that aren't reserved words and can be used as identifiers.

**•** after

**•** before

**•** count

**•** excludes

**•** first

**•** includes

**•** last

**•** order

**•** sharing

**•** with

### Documentation Typographical Conventions

Apex and Visualforce documentation uses these typographical conventions.


Apex Reference Guide Documentation Typographical Conventions

**Convention** **Description**

```
Courier font

Italics

```

In descriptions of syntax, a monospace font indicates items that you should type as shown,
except for brackets. For example:

```
Public class HelloWorld

```

In descriptions of syntax, italics represent variables. You supply the actual value. In the following
example, three values must be supplied: _`datatype variable_name`_ [ = _`value`_ ];

If the syntax is bold and italic, the text represents a code element that needs a value supplied
by you, such as a class name or variable value:

```
 public static class YourClassHere { ... }

```

**`Bold Courier font`** In code samples and syntax descriptions, a bold courier font emphasizes a portion of the code
or syntax.

< >

{ }

[ ]

|

In descriptions of syntax, less-than and greater-than symbols (< >) are typed exactly as shown.

```
<apex:pageBlockTable value="{!account.Contacts}" var="contact">

  <apex:column value="{!contact.Name}"/>

  <apex:column value="{!contact.MailingCity}"/>

  <apex:column value="{!contact.Phone}"/>

</apex:pageBlockTable>

```

In descriptions of syntax, braces ({ }) are typed exactly as shown.

```
<apex:page>

   Hello {!$User.FirstName}!

</apex:page>

```

In descriptions of syntax, anything included in brackets is optional. In the following example,
specifying _**`value`**_ is optional:

```
 data_type variable_name [ = value ];

```

In descriptions of syntax, the pipe sign means “or”. You can do one of the following (not all).
In the following example, you can create a new unpopulated set in one of two ways, or you
can populate the set:

```
Set< data_type > set_name

  [= new Set< data_type >();] |

  [= new Set< data_type { value [, value2 . . .] };] |

  ;

```

